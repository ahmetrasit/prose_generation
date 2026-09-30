#!/usr/bin/env python3
"""Run approved v16 packets once through the Codex subscription with GPT-6 Astra.

Build only by default. --run launches one call per requested ayah, at high effort.
USD cost is unavailable from this subscription CLI; never borrow another model's
prices. Preserve the exact prompt, command, event stream, final response and usage.
Example: python3 _commentary/v16/run_astra.py --ayah 1:5 --ayah 1:6 --run
"""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time

import v16 as V

MODEL = "gpt-6-astra"
EFFORT = "high"


def output_dir(ref: str, arm: str, brief: str, effort: str, model: str = MODEL) -> Path:
    # Preserve the initial max runs' historical name; high never shares that directory.
    model_key = ("astra" if effort == "max" else f"astra.{effort}") if model == MODEL else f"{model}.{effort}"
    return V.arm_dir(V.OUT, V.sa(ref)[1], arm, brief, model_key)


def save_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build_frozen(ref: str, arm: str, brief: str, from_brief: str) -> str:
    """Replace only the two briefs in a saved run prompt; retain all evidence byte for byte.

    This also permits controlled comparisons when the upstream data checkout no
    longer has the historical root gateway needed by the live packet builder.
    """
    name = V.sa(ref)[1]
    source = V.arm_dir(V.OUT, name, arm, from_brief) / "prompt.md"
    original = source.read_text(encoding="utf-8")
    prompt = original
    for key in ("write", "add"):
        old = V.rel(V.BRIEFS[from_brief][key])
        new = V.BRIEFS[brief][key]
        pattern = r"(?ms)^===== " + re.escape(old) + r" =====\n.*?(?=^===== |\Z)"
        replacement = f"===== {V.rel(new)} =====\n{new.read_text(encoding='utf-8')}\n\n"
        prompt, count = re.subn(pattern, lambda _: replacement, prompt)
        if count != 1:
            raise ValueError(f"Expected exactly one frozen {key} brief in {source}; got {count}")
    evidence_marker = f"===== _commentary/v16/work/{name}/{arm}.{from_brief}/context.md ====="
    if evidence_marker not in original or original.split(evidence_marker, 1)[1] != prompt.split(evidence_marker, 1)[1]:
        raise ValueError("Frozen evidence changed")
    work = V.arm_dir(V.WORK, name, arm, brief)
    work.mkdir(parents=True, exist_ok=True)
    (work / "prompt.md").write_text(prompt, encoding="utf-8")
    save_json(work / "packet.json", {"ref": ref, "arm": arm, "brief": brief,
              "frozen_from": V.rel(source), "source_prompt_sha256": hashlib.sha256(original.encode()).hexdigest(),
              "evidence_sha256": hashlib.sha256(original.split(evidence_marker, 1)[1].encode()).hexdigest(),
              "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(), "evidence_unchanged": True})
    return prompt


def run_one(ref: str, arm: str, brief: str, prompt: str, cli: str, effort: str = EFFORT,
            model: str = MODEL) -> dict:
    name = V.sa(ref)[1]
    out = output_dir(ref, arm, brief, effort, model)
    out.mkdir(parents=True, exist_ok=True)
    if V.blocked(out):
        return {"ref": ref, "status": "skipped", "reason": "started or finished before"}
    row = {"ref": ref, "arm": arm, "brief": brief, "model": model, "effort": effort,
           "cli": cli, "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
           "prompt_chars": len(prompt), "started": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
           "cost_usd": None, "estimate_usd": None,
           "cost_note": "User-authorized Codex subscription run; CLI does not report USD cost."}
    # Exclusive creation also prevents simultaneous launchers from duplicating a call.
    with (out / "started.json").open("x", encoding="utf-8") as f:
        json.dump(row, f, ensure_ascii=False, indent=2)
        f.write("\n")
    (out / "prompt.md").write_text(prompt, encoding="utf-8")
    started = time.monotonic()
    response = ""
    try:
        with tempfile.TemporaryDirectory(prefix="v16_astra_") as cwd:
            last = Path(cwd) / "response.md"
            cmd = ["codex", "exec", "--ignore-user-config", "-m", model,
                   "-c", f'model_reasoning_effort="{effort}"', "-c", 'web_search="disabled"',
                   "--disable", "skill_search", "--skip-git-repo-check", "--ephemeral",
                   "-s", "read-only", "--json", "-o", str(last), "-C", cwd, "-"]
            save_json(out / "command.json", {"argv": cmd, "stdin": "prompt.md"})
            with (out / "run.stream.jsonl").open("w", encoding="utf-8") as stream, \
                    (out / "stderr.log").open("w", encoding="utf-8") as stderr:
                result = subprocess.run(cmd, input=prompt, text=True, stdout=stream, stderr=stderr, cwd=cwd)
            row["returncode"] = result.returncode
            if last.exists():
                response = last.read_text(encoding="utf-8").strip()
        (out / "response.md").write_text(response + "\n", encoding="utf-8")
        usage, tool_events, completed = {}, [], False
        for line in (out / "run.stream.jsonl").read_text(encoding="utf-8").splitlines():
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            if event.get("type") == "thread.started":
                row["thread_id"] = event.get("thread_id")
            if event.get("type") == "turn.completed":
                completed = True
                usage = event.get("usage") or {}
            item = event.get("item") or {}
            if event.get("type") == "item.completed" and item.get("type") in (
                    "command_execution", "mcp_tool_call", "web_search", "file_change"):
                tool_events.append(item.get("type"))
        row.update(usage=usage, tool_events=tool_events, turn_completed=completed)
        prose, separator, ledger = response.partition(V.LEDGER_MARK)
        row["ledger"] = bool(separator and ledger.strip())
        row["status"] = "ok" if response and row["returncode"] == 0 and completed else "error"
        if row["status"] == "ok" and (not row["ledger"] or tool_events):
            row["status"] = "needs_review"
        if response:
            reading = out / f"{name}.reading.tr.md"
            reading.write_text(prose.strip() + "\n", encoding="utf-8")
            row["prose_words"] = len(prose.split())
            if separator:
                (out / "ledger.md").write_text(ledger.strip() + "\n", encoding="utf-8")
            check = subprocess.run([sys.executable, "-B", str(V.CHECK), str(reading), "--ref", ref,
                                    "--out", str(out / "check.json"), "--quiet"], cwd=V.CHECK.parent,
                                   capture_output=True, text=True)
            row["check_returncode"] = check.returncode
            if check.returncode:
                (out / "check.error.log").write_text(check.stdout + check.stderr, encoding="utf-8")
    except Exception as exc:
        row.update(status="error", error=f"{type(exc).__name__}: {exc}")
    row["seconds"] = round(time.monotonic() - started)
    save_json(out / "run.log.json", row)
    V.log(row)
    return row


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ayah", action="append", required=True)
    parser.add_argument("--brief", choices=[k for k, v in V.BRIEFS.items() if v.get("ledger")], default="r4")
    parser.add_argument("--arm", default="DM")
    parser.add_argument("--model", choices=(MODEL, "gpt-6.1-sol"), default=MODEL)
    parser.add_argument("--effort", choices=("high", "max"), default=EFFORT)
    parser.add_argument("--from-brief", choices=("r3", "r4"), default="r3",
                        help="Use the evidence frozen in this earlier Opus run; replace only its briefs")
    parser.add_argument("--run", action="store_true")
    args = parser.parse_args()
    jobs = []
    for ref in dict.fromkeys(args.ayah):
        out = output_dir(ref, args.arm, args.brief, args.effort, args.model)
        if V.blocked(out):
            print(f"{ref}: started or finished before, skipped (never rerun)", flush=True)
            continue
        prompt = build_frozen(ref, args.arm, args.brief, args.from_brief)
        jobs.append((ref, args.arm, args.brief, prompt))
        print(f"{ref} {args.arm} {args.brief}: {len(prompt):,} chars; {args.model} {args.effort}; "
              "subscription cost unreported", flush=True)
    if not args.run or not jobs:
        return 0
    cli = subprocess.run(["codex", "--version"], capture_output=True, text=True, check=True).stdout.strip()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(run_one, *job, cli, args.effort, args.model) for job in jobs]
        rows = []
        for future in concurrent.futures.as_completed(futures):
            row = future.result()
            rows.append(row)
            print(json.dumps(row, ensure_ascii=False), flush=True)
    return int(any(row["status"] not in ("ok", "skipped") for row in rows))


if __name__ == "__main__":
    sys.exit(main())
