#!/usr/bin/env python3
"""Run the V9 findings lane with Codex: Luna judges worklists, a writer model writes the reading.

  python3 _commentary/v9/luna/run.py discover 29:38 [--parallel 4]
      builds worklists (if absent), runs one Luna session per worklist whose records do not pass the
      checker, then one repair turn (resume) per session that still fails; merges when all pass
  python3 _commentary/v9/luna/run.py write 29:38 --model gpt-6-sol [--model gpt-6-luna]
      one writer session per model, in parallel; outputs to pilot/S_A-<model>/
  python3 _commentary/v9/luna/run.py usage 29:38
      token usage per session from the Codex JSON logs

Every session: reasoning effort max, tool output limit 20k tokens, workspace-write sandbox.
Logs: luna/work/S_A/logs/<session>.jsonl (Codex events; usage is on turn.completed).
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

V9 = Path(__file__).resolve().parents[1]
REPO = V9.parents[1]
CHECK = V9 / "luna" / "check_records.py"
EFFORT = ["-c", 'model_reasoning_effort="max"', "-c", "tool_output_token_limit=20000", "--json"]


def dirs(ref: str) -> tuple[Path, Path]:
    s, a = ref.split(":")
    return V9 / "input" / "v2" / f"s{int(s):03d}" / f"{s}_{a}", V9 / "luna" / "work" / f"{s}_{a}"


def codex(model: str, prompt: str, log: Path, resume: str | None = None, stdin: str | None = None) -> int:
    """One Codex turn (a new session, or a resumed one); events are appended to `log`."""
    log.parent.mkdir(parents=True, exist_ok=True)
    if resume:  # `exec resume` takes no -s/-C: sandbox via config, cwd via subprocess
        cmd = ["codex", "exec", "resume", resume, "-m", model, "-c", 'sandbox_mode="workspace-write"'] + EFFORT
    else:
        cmd = ["codex", "exec", "-m", model, "-s", "workspace-write", "-C", str(REPO)] + EFFORT
    with log.open("a", encoding="utf-8") as out:  # stdin is appended to the prompt as a <stdin> block
        return subprocess.run(cmd + [prompt], stdout=out, stderr=subprocess.STDOUT, cwd=REPO,
                              input=stdin or "", text=True).returncode


def inline(*paths: Path) -> str:
    return "\n\n".join(f"===== {p.relative_to(REPO)} =====\n{p.read_text(encoding='utf-8')}" for p in paths)


def thread_id(log: Path) -> str | None:
    for line in log.read_text(encoding="utf-8").splitlines():
        if line.startswith("{") and '"thread.started"' in line:
            return json.loads(line)["thread_id"]
    return None


def check(work: Path, name: str) -> tuple[bool, str]:
    r = subprocess.run([sys.executable, str(CHECK), str(work), name], capture_output=True, text=True)
    return r.returncode == 0, r.stdout[-4000:]


def discover(ref: str, parallel: int) -> None:
    pkg, work = dirs(ref)
    if not (work / "items.tsv").exists():
        subprocess.run([sys.executable, str(V9 / "luna" / "worklists.py"), str(pkg), str(work)], check=True)
    names = sorted({l.split("\t")[1] for l in (work / "items.tsv").read_text(encoding="utf-8").splitlines() if l})
    rel = work.relative_to(REPO)

    def one(name: str) -> str:
        ok, _ = check(work, name)
        if ok:
            return f"{name}: already ok"
        log = work / "logs" / f"{Path(name).stem}.jsonl"
        codex("gpt-6-luna", f"Follow the brief below (luna_worker.md) exactly. Work directory: {rel}. "
                            f"Your worklist: {rel}/{name}. The brief, context.md and the worklist follow in full.",
              log, stdin=inline(V9 / "prompts" / "luna_worker.md", work / "context.md", work / name))
        ok, report = check(work, name)
        if not ok and (tid := thread_id(log)):
            codex("gpt-6-luna", "The checker still reports problems. Fix every one, rerun the checker until "
                                f"it prints ok:\n{report}", log, resume=tid)
            ok, report = check(work, name)
        return f"{name}: {'ok' if ok else 'FAILED'}" + ("" if ok else f"\n{report}")

    with ThreadPoolExecutor(parallel) as pool:
        for line in pool.map(one, names):
            print(line, flush=True)
    if all(check(work, n)[0] for n in names):
        subprocess.run([sys.executable, str(V9 / "luna" / "merge.py"), str(work)], check=True)


def write(ref: str, models: list[str]) -> None:
    _, work = dirs(ref)
    s, a = ref.split(":")

    def one(model: str) -> str:
        out = V9 / "pilot" / f"{s}_{a}-{model}"
        out.mkdir(parents=True, exist_ok=True)
        rc = codex(model, f"Follow the brief below (findings_writer.md) and the rules it names (writer_rules.md) "
                          f"exactly. Work directory: {work.relative_to(REPO)}. Output directory: "
                          f"{out.relative_to(REPO)} (files {s}_{a}.reading.tr.md and {s}_{a}.harvest.md). The two "
                          f"briefs, context.md and findings.md follow in full; do not read them again from disk.",
                   work / "logs" / f"writer-{model}.jsonl",
                   stdin=inline(V9 / "prompts" / "findings_writer.md", V9 / "prompts" / "writer_rules.md",
                                work / "context.md", work / "findings.md"))
        return f"{model}: exit {rc}"

    with ThreadPoolExecutor(len(models)) as pool:
        for line in pool.map(one, models):
            print(line, flush=True)


def usage(ref: str) -> None:
    _, work = dirs(ref)
    keys = ("input_tokens", "cached_input_tokens", "output_tokens", "reasoning_output_tokens")
    total = dict.fromkeys(keys, 0)
    print(f"{'session':24} {'turns':>5} {'input':>10} {'cached':>10} {'output':>8} {'reasoning':>9}")
    for log in sorted((work / "logs").glob("*.jsonl")):
        row, turns = dict.fromkeys(keys, 0), 0
        for line in log.read_text(encoding="utf-8").splitlines():
            if line.startswith("{") and '"turn.completed"' in line:
                u = json.loads(line).get("usage", {})
                turns += 1
                for k in keys:
                    row[k] += u.get(k, 0) or 0
        for k in keys:
            total[k] += row[k]
        print(f"{log.stem:24} {turns:5} {row['input_tokens']:10,} {row['cached_input_tokens']:10,} "
              f"{row['output_tokens']:8,} {row['reasoning_output_tokens']:9,}")
    print(f"{'TOTAL':24} {'':5} {total['input_tokens']:10,} {total['cached_input_tokens']:10,} "
          f"{total['output_tokens']:8,} {total['reasoning_output_tokens']:9,}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("step", choices=("discover", "write", "usage"))
    ap.add_argument("ref")
    ap.add_argument("--parallel", type=int, default=4)
    ap.add_argument("--model", action="append")
    args = ap.parse_args()
    if args.step == "discover":
        discover(args.ref, args.parallel)
    elif args.step == "write":
        write(args.ref, args.model or ["gpt-6-sol", "gpt-6-luna"])
    else:
        usage(args.ref)


if __name__ == "__main__":
    main()
