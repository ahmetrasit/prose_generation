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


def outputs(text: str, sa: str) -> dict[str, str]:
    """Final-message sections; a model that kept the literal placeholder S_A in the markers is accepted too."""
    return R.split_outputs(re.sub(r"^===== S_A\.", f"===== {sa}.", text, flags=re.M), sa)

SOL = "gpt-6-sol"
REPAIR = "gpt-6-luna"  # localized quote/format repairs: bounded, script-checked (reasoning effort max)


OUT_DIR = "sol"  # output folder under network/out/S_A/ (--dir); the backbone is always sol/backbone.md


def paths(ref: str) -> dict[str, Path]:
    s, a = ref.split(":")
    sa = f"{s}_{a}"
    sol = V9 / "network" / "out" / sa / OUT_DIR
    sol.mkdir(parents=True, exist_ok=True)
    return {"sol": sol, "sa": Path(sa), "context": V9 / "luna" / "work" / sa / "context.md",
            "backbone": V9 / "network" / "out" / sa / "sol" / "backbone.md", "plan": sol / "plan.md", "pkg": V9 / "input" / "v2" / f"s{int(s):03d}" / sa,
            "reading": sol / f"{sa}.reading.tr.md", "work": V9 / "luna" / "work" / sa}


ID = r"\b([HLTJGCPMF]\d+(?:\.\d+)?)\b"


def plan_blocks(text: str) -> list[tuple[str, str]]:
    """(heading, bounded content) for every '## ' heading, in order."""
    parts = re.split(r"^## (.+)$", text, flags=re.M)
    return [(parts[i].strip(), parts[i + 1]) for i in range(1, len(parts) - 1, 2)]


def field(block: str, name: str) -> str:
    m = re.search(rf"^{name}:[ \t]*(.*)$", block, re.M)
    return m.group(1).strip() if m else ""


def check_plan_text(plan: str, backbone: str) -> list[str]:
    """Shape of the argument plan, checked block by block: 3–6 tensions; a question and a central claim; 4–8 sections,
    each with a claim, 2–6 numbered steps and 'adds'; known ids; every [dictionary] member of a backbone hub placed in a
    step, a brief_mentions line, Ek Notlar or Rejected (an id only in an image/adds/alternatives line is not placed)."""
    ids = set(re.findall(r"\*\*([A-Z]\d+(?:\.\d+)?)\*\*", backbone))
    blocks = plan_blocks(plan)
    by = {h: b for h, b in blocks}
    problems = []
    tensions = by.get("Tensions", "")
    n_t = len(re.findall(r"^- \S", tensions, re.M))
    if not 3 <= n_t <= 6:
        problems.append(f"{n_t} tensions (want 3–6)")
    qc = by.get("Question and central claim", "")
    if not field(qc, "question") or not field(qc, "claim"):
        problems.append("no question / central claim in its own block")
    sections = [(h, b) for h, b in blocks if re.match(r"Section \d+", h)]
    if not 4 <= len(sections) <= 8:
        problems.append(f"{len(sections)} sections (want 4–8)")
    placed = set()
    for h, b in sections:
        if not field(b, "claim"):
            problems.append(f"{h}: no claim")
        steps = re.findall(r"^- \d+\.(.*)$", b, re.M)
        if not 2 <= len(steps) <= 6:
            problems.append(f"{h}: {len(steps)} steps (want 2–6)")
        if not field(b, "adds"):
            problems.append(f"{h}: no adds")
        for line in steps:
            placed |= set(re.findall(ID, line))
        placed |= set(re.findall(ID, field(b, "brief_mentions")))
    for name in ("Ek Notlar", "Rejected"):
        placed |= set(re.findall(ID, by.get(name, "")))
    unknown = sorted(set(re.findall(ID, plan)) - ids)
    if unknown:
        problems.append(f"ids not in the backbone: {', '.join(unknown[:20])}")
    dict_members = set(re.findall(r"\*\*(H\d+\.\d+)\*\* \[dictionary\]", backbone))
    unplaced = sorted(dict_members - placed)
    if unplaced:
        problems.append(f"[dictionary] hub members not placed (steps, brief_mentions, Ek Notlar, Rejected): {', '.join(unplaced)}")
    return problems


def check_plan(p: dict) -> list[str]:
    return check_plan_text(p["plan"].read_text(encoding="utf-8"), p["backbone"].read_text(encoding="utf-8"))


def plan(ref: str) -> None:
    p = paths(ref)
    stdin = R.inline(V9 / "prompts" / "sol_plan.md", p["context"], p["backbone"])
    text = R.codex(SOL, f"Follow the brief below (sol_plan.md) exactly. Ayah {ref}; S_A = {p['sa']}. The brief, "
                        f"context.md and backbone.md follow in full; return the plan as your final message.",
                   p["sol"] / "plan.log.jsonl", stdin=stdin, last=p["sol"] / "plan.last.txt", sandbox="read-only")
    p["plan"].write_text(outputs(text, str(p["sa"])).get(f"{p['sa']}.plan.md") or text, encoding="utf-8")
    problems = check_plan(p)
    if problems:  # one bounded repair: a fresh session fixes the listed problems and returns the whole plan
        print(f"plan: problems: {problems}; repairing once")
        stdin = R.inline(V9 / "prompts" / "sol_plan.md", p["context"], p["backbone"], p["plan"])
        text = R.codex(SOL, f"Follow the brief below (sol_plan.md). Ayah {ref}; S_A = {p['sa']}. plan.md (below) is "
                            f"your earlier plan; a checker found these problems:\n- " + "\n- ".join(problems) +
                            "\nFix exactly these problems, keep everything else, and return the whole corrected plan as "
                            "your final message in the brief's output shape.",
                       p["sol"] / "plan.repair.log.jsonl", stdin=stdin, last=p["sol"] / "plan.repair.last.txt",
                       sandbox="read-only")
        fixed = outputs(text, str(p["sa"])).get(f"{p['sa']}.plan.md")
        if fixed:
            p["plan"].write_text(fixed, encoding="utf-8")
        problems = check_plan(p)
    body = p["plan"].read_text(encoding="utf-8")
    print(f"plan: {len(re.findall(r'^## Section', body, re.M))} sections; problems: {problems or 'none'}")
    if problems:
        sys.exit("plan still invalid after one repair; not writing")


def write(ref: str) -> None:
    p = paths(ref)
    problems = check_plan(p)
    if problems:
        sys.exit(f"plan invalid, not writing: {problems}")
    stdin = R.inline(V9 / "prompts" / "sol_write.md", p["context"], p["backbone"], p["plan"])
    text = R.codex(SOL, f"Follow the brief below (sol_write.md) exactly. Ayah {ref}; S_A = {p['sa']}. The brief, "
                        f"context.md, backbone.md and plan.md follow in full; return the reading and the harvest as "
                        f"your final message.", p["sol"] / "write.log.jsonl", stdin=stdin,
                   last=p["sol"] / "write.last.txt", sandbox="read-only")
    for name, body in outputs(text, str(p["sa"])).items():
        (p["sol"] / name).write_text(body, encoding="utf-8")
    print(f"write: {'reading written' if p['reading'].exists() else 'NO READING'}")


def check(ref: str) -> None:
    p = paths(ref)
    if not p["reading"].exists():
        sys.exit(f"no reading at {p['reading']}; nothing to check")
    status = "checks ok"
    for attempt in (1, 2):
        problems, flagged = R.reading_problems(p["reading"], p["pkg"])
        if not problems:
            break
        print(f"check {attempt}: {len(problems)} problem(s): " + "; ".join(problems[:6]))
        status = R.repair_reading(REPAIR, p["reading"], p["pkg"], p["pkg"], problems, flagged,
                                  p["sol"] / f"repair{attempt}.log.jsonl")
        if status.startswith("repair reverted"):
            break
    problems, _ = R.reading_problems(p["reading"], p["pkg"])
    cat = subprocess.run([sys.executable, str(V9 / "luna" / "check_reading.py"), str(p["reading"]), str(p["work"]),
                          "--max-citations", "8"], capture_output=True, text=True).stdout
    words = len(p["reading"].read_text(encoding="utf-8").split())
    print(f"check: {status}; {len(problems)} problem(s) left; {words} words; {cat.splitlines()[0] if cat else ''}")


def main() -> None:
    global SOL, OUT_DIR
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=("plan", "write", "check", "all"))
    ap.add_argument("ref")
    ap.add_argument("--model", default=SOL, help="writer model (default gpt-6-sol; e.g. gpt-6-luna)")
    ap.add_argument("--dir", default="sol", help="output folder under network/out/S_A/")
    a = ap.parse_args()
    SOL, OUT_DIR = a.model, a.dir
    steps = ("plan", "write", "check") if a.step == "all" else (a.step,)
    for s in steps:
        {"plan": plan, "write": write, "check": check}[s](a.ref)


if __name__ == "__main__":
    main()
