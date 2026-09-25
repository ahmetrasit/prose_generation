#!/usr/bin/env python3
"""V9 pipeline for one ayah, end to end: one command, no hand steps.

  python3 _commentary/v9/luna/run.py ayah 29:38 [--writer opus] [--writer gpt-6-sol] [--parallel 4]
  python3 _commentary/v9/luna/run.py usage 29:38

Stages (each skips work that is already done and still valid):
  1 package    prepare.py → input/v2/sSSS/S_A/ (rebuilt only when missing, or with --refresh)
  2 worklists  worklists.py → luna/work/S_A/ (rebuilt when the package is newer; older work is archived)
  3 discover   one Luna session per bundle (gpt-6-luna, max): everything pushed in the prompt, records
               returned as the final message; the script writes and checks them; residual problems go to a
               FRESH small repair session (luna_repair.md) guarded against downgrading or deleting findings
  4 merge      merge.py → findings.md, records_index.md
  5 write      each writer: "opus" (Claude Code headless, reads its inputs, writes its files) or a GPT
               model via Codex (everything pushed, reading + harvest returned as the final message)
  6 check      verify_ar --fix, validate_prose, check_reading (catalogue report + automatic harvest);
               residual problems go to a fresh repair session that may change only the flagged lines

GPT sessions: reasoning effort max, tool output limit 20k. Outputs: output/sSSS/S_A/<writer>/.
Logs: luna/work/S_A/logs/ (Codex JSONL events; Claude JSON results).
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

V9 = Path(__file__).resolve().parents[1]
REPO = V9.parents[1]
PROMPTS = V9 / "prompts"
LUNA = "gpt-6-luna"
GPT_OPTS = ["-c", 'model_reasoning_effort="max"', "-c", "tool_output_token_limit=20000", "--json"]
CLAUDE_TOOLS = "Read Write Edit Grep Glob Bash(python3 _commentary/v9/verify_ar.py:*) " \
               "Bash(python3 _commentary/v5/validate_prose.py:*)"


def paths(ref: str) -> dict[str, Path]:
    s, a = ref.split(":")
    sa = f"{s}_{a}"
    return {"pkg": V9 / "input" / "v2" / f"s{int(s):03d}" / sa, "work": V9 / "luna" / "work" / sa,
            "out": V9 / "output" / f"s{int(s):03d}" / sa, "sa": Path(sa)}


def rel(p: Path) -> str:
    return str(p.relative_to(REPO))


def inline(*files: Path) -> str:
    return "\n\n".join(f"===== {rel(p)} =====\n{p.read_text(encoding='utf-8')}" for p in files)


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, cwd=REPO)


# ---------------------------------------------------------------- model calls
def codex(model: str, prompt: str, log: Path, stdin: str = "", last: Path | None = None,
          sandbox: str = "workspace-write") -> str:
    """One fresh Codex session; returns its final message (also appended to `log` as JSONL events)."""
    log.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["codex", "exec", "-m", model, "-s", sandbox, "-C", str(REPO)] + GPT_OPTS
    if last:
        cmd += ["-o", str(last)]
    with log.open("a", encoding="utf-8") as out:
        subprocess.run(cmd + [prompt], stdout=out, stderr=subprocess.STDOUT, cwd=REPO, input=stdin, text=True)
    return last.read_text(encoding="utf-8") if last and last.exists() else ""


def claude(model: str, prompt: str, log: Path) -> str:
    """One headless Claude Code session (subscription); the JSON result (with usage) is appended to `log`."""
    log.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(["claude", "-p", prompt, "--model", model, "--output-format", "json",
                        "--permission-mode", "acceptEdits", "--allowedTools", CLAUDE_TOOLS],
                       capture_output=True, text=True, cwd=REPO, stdin=subprocess.DEVNULL)
    with log.open("a", encoding="utf-8") as out:
        out.write((r.stdout or json.dumps({"error": r.stderr[-2000:]})).strip() + "\n")
    try:
        return json.loads(r.stdout).get("result", "")
    except json.JSONDecodeError:
        return ""


# ---------------------------------------------------------------- stages 1-2
def stage_package(ref: str, refresh: bool) -> None:
    p = paths(ref)
    if refresh or not (p["pkg"] / "00_ayah.md").exists():
        r = run([sys.executable, str(V9 / "prepare.py"), "--ayah", ref, "--out", str(p["pkg"])])
        if r.returncode:
            sys.exit(f"package failed:\n{r.stderr[-2000:]}")
        print(f"package: built {rel(p['pkg'])}", flush=True)


def stage_worklists(ref: str) -> list[str]:
    p = paths(ref)
    items = p["work"] / "items.tsv"
    newest_pkg = max(f.stat().st_mtime for f in p["pkg"].glob("*.md"))
    if items.exists() and items.stat().st_mtime < newest_pkg:
        archive = p["work"].with_name(f"{p['sa']}.archive-{time.strftime('%Y%m%d-%H%M%S')}")
        shutil.move(str(p["work"]), str(archive))
        print(f"worklists: package changed; archived old work to {rel(archive)}", flush=True)
    if not items.exists():
        r = run([sys.executable, str(V9 / "luna" / "worklists.py"), str(p["pkg"]), str(p["work"])])
        if r.returncode:
            sys.exit(f"worklists failed:\n{r.stderr[-2000:]}")
        print(f"worklists: {r.stdout.strip()[:200]}", flush=True)
    return sorted({l.split("\t")[1] for l in items.read_text(encoding="utf-8").splitlines() if l})


# ---------------------------------------------------------------- stage 3
def check_records(work: Path, name: str) -> tuple[bool, str]:
    r = run([sys.executable, str(V9 / "luna" / "check_records.py"), str(work), name])
    return r.returncode == 0, r.stdout[-6000:]


def parse_jsonl(text: str) -> list[dict]:
    out = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("{"):
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return out


def record_guard(before: list[dict], after: list[dict]) -> list[str]:
    """A repair may fix records, never lose findings."""
    b, a = {r.get("id"): r for r in before}, {r.get("id"): r for r in after}
    bad = []
    for rid, r in b.items():
        if r.get("verdict") in ("reading", "note") and rid not in a:
            bad.append(f"{rid}: finding deleted")
        if "lines" in r and rid in a:
            nb = sum(c in "nr" for c in str(r["lines"]))
            na = sum(c in "nr" for c in str(a[rid].get("lines", "")))
            if na < nb:
                bad.append(f"{rid}: line codes downgraded ({nb} → {na} n/r)")
    return bad


def stage_discover(ref: str, names: list[str], parallel: int) -> bool:
    work = paths(ref)["work"]
    (work / "records").mkdir(exist_ok=True)

    def one(name: str) -> str:
        stem = Path(name).stem
        recs = work / "records" / f"{stem}.jsonl"
        ok, report = check_records(work, name)
        if ok:
            return f"{name}: already ok"
        if not recs.exists():
            text = codex(LUNA, f"Follow the brief below (luna_worker.md) exactly. Work directory: {rel(work)}. "
                               f"Your worklist: {rel(work)}/{name}. The brief, context.md and the worklist "
                               f"follow in full.", work / "logs" / f"{stem}.jsonl",
                         stdin=inline(PROMPTS / "luna_worker.md", work / "context.md", work / name),
                         last=work / "logs" / f"{stem}.last.txt", sandbox="read-only")
            rows = parse_jsonl(text)
            recs.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
            ok, report = check_records(work, name)
        for attempt in (1, 2):
            if ok:
                break
            before_text = recs.read_text(encoding="utf-8")
            codex(LUNA, f"Follow the brief below (luna_repair.md). Work directory: {rel(work)}. Records file: "
                        f"{rel(recs)}. Worklist: {rel(work)}/{name}. Problems:\n{report}",
                  work / "logs" / f"{stem}.repair{attempt}.jsonl", stdin=inline(PROMPTS / "luna_repair.md"))
            violations = record_guard(parse_jsonl(before_text), parse_jsonl(recs.read_text(encoding="utf-8")))
            if violations:
                recs.write_text(before_text, encoding="utf-8")
                return f"{name}: repair {attempt} reverted (it would lose findings: {'; '.join(violations[:5])})"
            ok, report = check_records(work, name)
        return f"{name}: {'ok' if ok else 'FAILED'}" + ("" if ok else f"\n{report}")

    with ThreadPoolExecutor(parallel) as pool:
        results = list(pool.map(one, names))
    for line in results:
        print(f"discover: {line}", flush=True)
    return all(check_records(work, n)[0] for n in names)


# ---------------------------------------------------------------- stages 5-6
def split_outputs(text: str, sa: str) -> dict[str, str]:
    parts = re.split(r"^===== (\S+) =====\s*$", text, flags=re.M)
    return {parts[i].strip(): parts[i + 1].strip() + "\n" for i in range(1, len(parts) - 1, 2)
            if parts[i].strip().startswith(sa)}


def reading_problems(reading: Path, work: Path) -> tuple[list[str], set[int]]:
    problems, lines = [], set()
    v = run([sys.executable, str(V9 / "verify_ar.py"), str(reading), str(work), "--fix"])
    for m in re.finditer(r"^line (\d+): (missing|wrong-ayah)\s+(.*)$", v.stdout, re.M):
        problems.append(f"line {m.group(1)}: {m.group(2)} {m.group(3)}")
        lines.add(int(m.group(1)))
    p = run([sys.executable, str(REPO / "_commentary" / "v5" / "validate_prose.py"), str(reading)])
    for m in re.finditer(r":(\d+): error: (.*)$", p.stdout + p.stderr, re.M):
        problems.append(f"line {m.group(1)}: {m.group(2)}")
        lines.add(int(m.group(1)))
    return problems, lines


def repair_reading(writer: str, reading: Path, work: Path, pkg: Path, problems: list[str], flagged: set[int],
                   log: Path) -> str:
    before = reading.read_text(encoding="utf-8")
    prompt = (f"Fix only these problems in {rel(reading)} and change no other line. Correct an Arabic quote or "
              f"its reference from the sources (the Quran text, {rel(pkg)}, {rel(work)}; use grep, do not read "
              f"whole files); never delete a quote or a finding to silence a problem.\nProblems:\n"
              + "\n".join(problems))
    if writer == "opus":
        claude("opus", prompt, log)
    else:
        codex(writer, prompt, log)
    after = reading.read_text(encoding="utf-8")
    changed = {i + 1 for tag, i1, i2, _, _ in difflib.SequenceMatcher(None, before.splitlines(),
                                                                       after.splitlines()).get_opcodes()
               if tag != "equal" for i in range(i1, max(i2, i1 + 1))}
    if changed - flagged:
        reading.write_text(before, encoding="utf-8")
        return f"repair reverted (it changed unflagged lines {sorted(changed - flagged)[:8]})"
    return "repaired"


def stage_write(ref: str, writers: list[str]) -> None:
    p = paths(ref)
    work, pkg, sa = p["work"], p["pkg"], str(p["sa"])
    dictionary = next(pkg.glob("01_*.md"))

    def one(writer: str) -> str:
        out = p["out"] / writer
        out.mkdir(parents=True, exist_ok=True)
        reading = out / f"{sa}.reading.tr.md"
        if not reading.exists():
            files = f"{sa}.reading.tr.md and {sa}.harvest.md"
            if writer == "opus":
                claude("opus", f"Read {rel(PROMPTS / 'findings_writer.md')} and follow it exactly. Inputs: "
                               f"{rel(work / 'context.md')}, {rel(dictionary)}, {rel(work / 'findings.md')}. "
                               f"Work directory: {rel(work)}. Output directory: {rel(out)} (files {files}).",
                       work / "logs" / "writer-opus.json")
            else:
                text = codex(writer, f"Follow the briefs below (findings_writer.md, then findings_writer_gpt.md) "
                                     f"and the rules they name (writer_rules.md). Output files: {files}. The "
                                     f"briefs and all inputs follow in full.", work / "logs" / f"writer-{writer}.jsonl",
                             stdin=inline(PROMPTS / "findings_writer.md", PROMPTS / "findings_writer_gpt.md",
                                          PROMPTS / "writer_rules.md", work / "context.md", dictionary,
                                          work / "findings.md"),
                             last=work / "logs" / f"writer-{writer}.last.txt", sandbox="read-only")
                for name, body in split_outputs(text, sa).items():
                    (out / name).write_text(body, encoding="utf-8")
        if not reading.exists():
            return f"{writer}: no reading produced"
        status = "checks ok"
        for attempt in (1, 2):
            problems, flagged = reading_problems(reading, work)
            if not problems:
                break
            status = repair_reading(writer, reading, work, pkg, problems, flagged,
                                    work / "logs" / f"writer-{writer}.repair{attempt}.log")
            if status.startswith("repair reverted"):
                break
        problems, _ = reading_problems(reading, work)
        report = run([sys.executable, str(V9 / "luna" / "check_reading.py"), str(reading), str(work)]).stdout.strip()
        return f"{writer}: {status}; {len(problems)} problem(s) left\n  " + report.replace("\n", "\n  ")

    with ThreadPoolExecutor(max(1, len(writers))) as pool:
        for line in pool.map(one, writers):
            print(f"write: {line}", flush=True)


# ---------------------------------------------------------------- usage
def usage(ref: str) -> None:
    work = paths(ref)["work"]
    keys = ("input_tokens", "cached_input_tokens", "output_tokens", "reasoning_output_tokens")
    total = dict.fromkeys(keys, 0)
    print(f"{'codex session':30} {'input':>11} {'cached':>11} {'output':>9} {'reasoning':>9}")
    for log in sorted((work / "logs").glob("*.jsonl")):
        row = dict.fromkeys(keys, 0)
        for line in log.read_text(encoding="utf-8").splitlines():
            if line.startswith("{") and '"turn.completed"' in line:
                u = json.loads(line).get("usage", {})
                for k in keys:
                    row[k] += u.get(k, 0) or 0
        for k in keys:
            total[k] += row[k]
        print(f"{log.stem:30} {row['input_tokens']:11,} {row['cached_input_tokens']:11,} "
              f"{row['output_tokens']:9,} {row['reasoning_output_tokens']:9,}")
    print(f"{'TOTAL (codex)':30} {total['input_tokens']:11,} {total['cached_input_tokens']:11,} "
          f"{total['output_tokens']:9,} {total['reasoning_output_tokens']:9,}")
    for log in sorted((work / "logs").glob("*.json")) + sorted((work / "logs").glob("*.log")):
        for line in log.read_text(encoding="utf-8").splitlines():
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            u = r.get("usage") or {}
            print(f"claude {log.name}: turns {r.get('num_turns')}, input {u.get('input_tokens', 0):,}, cache write "
                  f"{u.get('cache_creation_input_tokens', 0):,}, cache read {u.get('cache_read_input_tokens', 0):,}, "
                  f"output {u.get('output_tokens', 0):,}, cost ${r.get('total_cost_usd', 0):.2f}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("step", choices=("ayah", "usage"))
    ap.add_argument("ref")
    ap.add_argument("--writer", action="append", help="opus or a GPT model name; repeatable (default: opus)")
    ap.add_argument("--parallel", type=int, default=4)
    ap.add_argument("--refresh", action="store_true", help="rebuild the package")
    a = ap.parse_args()
    if a.step == "usage":
        return usage(a.ref)
    stage_package(a.ref, a.refresh)
    names = stage_worklists(a.ref)
    if not stage_discover(a.ref, names, a.parallel):
        sys.exit("discover: some bundles still fail their checks; fix them before merging")
    r = run([sys.executable, str(V9 / "luna" / "merge.py"), str(paths(a.ref)["work"])])
    print(f"merge: {r.stdout.strip()}", flush=True)
    stage_write(a.ref, a.writer or ["opus"])
    usage(a.ref)


if __name__ == "__main__":
    main()
