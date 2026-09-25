#!/usr/bin/env python3
"""Sol writer on the ayah network: plan → write → script checks → guarded repair. GPT runs at reasoning effort max.

  plan   REF   gpt-6-sol session: sol_plan.md + context.md + backbone.md pushed; plan returned as final message;
               the script checks that every id exists and every thread has a thesis and 3–7 carry ids
  write  REF   gpt-6-sol session: sol_write.md + context.md + backbone.md + plan.md → reading + harvest
  check  REF   verify_ar --fix (package dir), validate_prose, catalogue report; residual problems go to a fresh
               repair session that may change only the flagged lines (luna/run.py guard), at most twice
  all    REF   plan, write, check

Outputs: network/out/S_A/sol/ (plan.md, S_A.reading.tr.md, S_A.harvest.md, logs).
Usage: python3 _commentary/v9/network/sol_pass.py all 29:38
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

V9 = Path(__file__).resolve().parents[1]
REPO = V9.parents[1]
sys.path.insert(0, str(V9 / "luna"))
import run as R  # noqa: E402  (codex runner with reasoning effort max, output splitting, guarded repair)

SOL = "gpt-6-sol"


def paths(ref: str) -> dict[str, Path]:
    s, a = ref.split(":")
    sa = f"{s}_{a}"
    sol = V9 / "network" / "out" / sa / "sol"
    return {"sol": sol, "sa": Path(sa), "context": V9 / "luna" / "work" / sa / "context.md",
            "backbone": sol / "backbone.md", "plan": sol / "plan.md", "pkg": V9 / "input" / "v2" / f"s{int(s):03d}" / sa,
            "reading": sol / f"{sa}.reading.tr.md", "work": V9 / "luna" / "work" / sa}


def check_plan(p: dict) -> list[str]:
    """Shape of the argument plan: tensions, question and claim, 4–8 sections each with a claim and 2–6 steps, known
    ids; every [dictionary] member of a backbone hub placed somewhere (steps, Ek Notlar or Rejected)."""
    backbone = p["backbone"].read_text(encoding="utf-8")
    ids = set(re.findall(r"\*\*([A-Z]\d+(?:\.\d+)?)\*\*", backbone))
    plan = p["plan"].read_text(encoding="utf-8")
    problems = []
    if not re.search(r"^## Tensions\s*\n- ", plan, re.M):
        problems.append("no tensions")
    if not (re.search(r"^question:\s*\S", plan, re.M) and re.search(r"^## Question and central claim[\s\S]*?^claim:\s*\S", plan, re.M)):
        problems.append("no question / central claim")
    sections = re.split(r"^## Section \d+", plan, flags=re.M)[1:]
    if not 4 <= len(sections) <= 8:
        problems.append(f"{len(sections)} sections (want 4–8)")
    for i, t in enumerate(sections, 1):
        t = t.split("\n## ", 1)[0]
        if not re.search(r"^claim:\s*\S", t, re.M):
            problems.append(f"section {i}: no claim")
        n_steps = len(re.findall(r"^- \d+\.", t, re.M))
        if not 2 <= n_steps <= 6:
            problems.append(f"section {i}: {n_steps} steps (want 2–6)")
        if not re.search(r"^adds:\s*\S", t, re.M):
            problems.append(f"section {i}: no adds")
    unknown = sorted(set(re.findall(r"\b([HLTJGCPMF]\d+(?:\.\d+)?)\b", plan)) - ids)
    if unknown:
        problems.append(f"ids not in the backbone: {', '.join(unknown[:20])}")
    dict_members = set(re.findall(r"\*\*(H\d+\.\d+)\*\* \[dictionary\]", backbone))
    unplaced = sorted(dict_members - set(re.findall(r"\b(H\d+\.\d+)\b", plan)))
    if unplaced:
        problems.append(f"[dictionary] hub members not placed: {', '.join(unplaced)}")
    return problems


def plan(ref: str) -> None:
    p = paths(ref)
    stdin = R.inline(V9 / "prompts" / "sol_plan.md", p["context"], p["backbone"])
    text = R.codex(SOL, f"Follow the brief below (sol_plan.md) exactly. Ayah {ref}; S_A = {p['sa']}. The brief, "
                        f"context.md and backbone.md follow in full; return the plan as your final message.",
                   p["sol"] / "plan.log.jsonl", stdin=stdin, last=p["sol"] / "plan.last.txt", sandbox="read-only")
    parts = R.split_outputs(text, str(p["sa"]))
    body = parts.get(f"{p['sa']}.plan.md") or text
    p["plan"].write_text(body, encoding="utf-8")
    problems = check_plan(p)
    print(f"plan: {len(re.findall(r'^## Section', body, re.M))} sections; problems: {problems or 'none'}")


def write(ref: str) -> None:
    p = paths(ref)
    stdin = R.inline(V9 / "prompts" / "sol_write.md", p["context"], p["backbone"], p["plan"])
    text = R.codex(SOL, f"Follow the brief below (sol_write.md) exactly. Ayah {ref}; S_A = {p['sa']}. The brief, "
                        f"context.md, backbone.md and plan.md follow in full; return the reading and the harvest as "
                        f"your final message.", p["sol"] / "write.log.jsonl", stdin=stdin,
                   last=p["sol"] / "write.last.txt", sandbox="read-only")
    for name, body in R.split_outputs(text, str(p["sa"])).items():
        (p["sol"] / name).write_text(body, encoding="utf-8")
    print(f"write: {'reading written' if p['reading'].exists() else 'NO READING'}")


def check(ref: str) -> None:
    p = paths(ref)
    status = "checks ok"
    for attempt in (1, 2):
        problems, flagged = R.reading_problems(p["reading"], p["pkg"])
        if not problems:
            break
        print(f"check {attempt}: {len(problems)} problem(s): " + "; ".join(problems[:6]))
        status = R.repair_reading(SOL, p["reading"], p["pkg"], p["pkg"], problems, flagged,
                                  p["sol"] / f"repair{attempt}.log.jsonl")
        if status.startswith("repair reverted"):
            break
    problems, _ = R.reading_problems(p["reading"], p["pkg"])
    cat = subprocess.run([sys.executable, str(V9 / "luna" / "check_reading.py"), str(p["reading"]), str(p["work"]),
                          "--max-citations", "8"], capture_output=True, text=True).stdout
    words = len(p["reading"].read_text(encoding="utf-8").split())
    print(f"check: {status}; {len(problems)} problem(s) left; {words} words; {cat.splitlines()[0] if cat else ''}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=("plan", "write", "check", "all"))
    ap.add_argument("ref")
    a = ap.parse_args()
    steps = ("plan", "write", "check") if a.step == "all" else (a.step,)
    for s in steps:
        {"plan": plan, "write": write, "check": check}[s](a.ref)


if __name__ == "__main__":
    main()
