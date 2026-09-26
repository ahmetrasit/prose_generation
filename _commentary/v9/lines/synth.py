#!/usr/bin/env python3
"""Synthesis arms on one identical package (lines/work/S_A/package.md + context.md).

  sol1   gpt-6-sol, reasoning effort max, one call: prompts/synth_one.md (connected readings → plan → reading)
  sol56  the same with gpt-5.6-sol (reasoning effort max)
  opus1  Claude Opus via `claude -p`, effort max, no tools, short system prompt, one call, same brief and inputs
  sol2   baseline: sol_pass.py plan → write (Sol, max) with the package in place of the backbone
  w10-opus-cold   baseline: the same prompt with context.md only (no package)
  w10-sol / w10-luna / w10-opus   the v10 writer prompt (_commentary/v10/prompts/write.md) on the same package:
         prose only, no plan; Sol and Luna at max reasoning, Opus at effort high (max spent its whole output on
         thinking on this input size)

Outputs: lines/work/S_A/synth/<arm>/ (plan, reading, harvest, raw final message, logs). Then the script checks
(verify_ar --fix against the package, validate_prose, plan structure) and prints problems; repairs are separate.
Token use: python3 _commentary/v9/lines/usage.py S:A

Usage: python3 _commentary/v9/lines/synth.py 18:86 --arm sol1
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

V9 = Path(__file__).resolve().parents[1]
REPO = V9.parents[1]
sys.path.insert(0, str(V9 / "luna"))
sys.path.insert(0, str(V9 / "network"))
import run as R  # noqa: E402
import sol_pass as SP  # noqa: E402

SYSTEM = ("You are a careful scholar of Quranic Arabic and a fine Turkish prose writer. Follow the brief in the "
          "user message exactly and return only the requested output.")


def split(text: str, sa: str) -> dict[str, str]:
    return SP.outputs(text, sa)


W10 = V9 / "prompts" / "write_v10.md"  # frozen copy of _commentary/v10/prompts/write.md (md5 dddcd1b2…), used by every w10 run


def run_w10(ref: str, arm: str) -> None:
    s, a = ref.split(":")
    sa = f"{s}_{a}"
    w = V9 / "lines" / "work" / sa
    out = w / "synth" / arm
    out.mkdir(parents=True, exist_ok=True)
    cold = arm.endswith("-cold")
    stdin = R.inline(W10, w / "context.md") if cold else R.inline(W10, w / "context.md", w / "package.md")
    evidence = ("context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and your own "
                "knowledge of Arabic and the Quran" if cold else
                "context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and package.md "
                "(discovery results with internal ids; their own header explains them)")
    prompt = (f"Focus: {ref}. Follow the brief below (write.md) exactly. The evidence is {evidence}. Return only the "
              f"reader's prose as your final message.")
    if arm in ("w10-sol", "w10-luna"):
        model = SP.SOL if arm == "w10-sol" else "gpt-6-luna"
        text = R.codex(model, prompt, out / "run.log.jsonl", stdin=stdin, last=out / "final.txt", sandbox="read-only")
    else:
        r = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", "",
                            "--output-format", "json", "--no-session-persistence", "--system-prompt", SYSTEM],
                           input=prompt + "\n\n" + stdin, capture_output=True, text=True, cwd=REPO)
        (out / "run.log.json").write_text((r.stdout or json.dumps({"error": r.stderr[-3000:]})).strip() + "\n",
                                          encoding="utf-8")
        try:
            text = json.loads(r.stdout).get("result", "")
        except json.JSONDecodeError:
            text = ""
        (out / "final.txt").write_text(text, encoding="utf-8")
    if len(text.split()) < 300:
        sys.exit(f"{arm}: no reading (see {out / 'final.txt'})")
    (out / f"{sa}.reading.tr.md").write_text(text.strip() + "\n", encoding="utf-8")
    problems, _ = R.reading_problems(out / f"{sa}.reading.tr.md", w)
    body = (out / f"{sa}.reading.tr.md").read_text(encoding="utf-8")
    print(f"{arm}: {len(body.split())} words, {len(set(re.findall(r'(\d{1,3}:\d{1,3})', body)))} distinct refs, "
          f"{body.count('{ar:')} Arabic tags; Arabic/prose problems {len(problems)}"
          f"{': ' + '; '.join(problems[:6]) if problems else ''}")


def run_arm(ref: str, arm: str) -> None:
    if arm.startswith("w10-"):
        return run_w10(ref, arm)
    s, a = ref.split(":")
    sa = f"{s}_{a}"
    w = V9 / "lines" / "work" / sa
    out = w / "synth" / arm
    out.mkdir(parents=True, exist_ok=True)
    stdin = R.inline(V9 / "prompts" / "synth_one.md", w / "context.md", w / "package.md")
    prompt = (f"Follow the brief below (synth_one.md) exactly. Ayah {ref}; S_A = {sa}. The brief, context.md and "
              f"package.md follow in full; return the plan, the reading and the harvest as your final message.")
    if arm in ("sol1", "sol56"):
        text = R.codex(SP.SOL if arm == "sol1" else "gpt-5.6-sol", prompt, out / "run.log.jsonl", stdin=stdin, last=out / "final.txt", sandbox="read-only")
    elif arm == "opus1":
        r = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "max", "--tools", "",
                            "--output-format", "json", "--no-session-persistence", "--system-prompt", SYSTEM],
                           input=prompt + "\n\n" + stdin, capture_output=True, text=True, cwd=REPO)
        (out / "run.log.json").write_text((r.stdout or json.dumps({"error": r.stderr[-3000:]})).strip() + "\n",
                                          encoding="utf-8")
        try:
            text = json.loads(r.stdout).get("result", "")
        except json.JSONDecodeError:
            text = ""
        (out / "final.txt").write_text(text, encoding="utf-8")
    else:
        sys.exit(f"unknown arm {arm}")
    parts = split(text, sa)
    for name, body in parts.items():
        (out / name).write_text(body, encoding="utf-8")
    reading = out / f"{sa}.reading.tr.md"
    if not reading.exists():
        sys.exit(f"{arm}: no reading in the final message (see {out / 'final.txt'})")
    check(ref, arm)


def check(ref: str, arm: str) -> None:
    s, a = ref.split(":")
    sa = f"{s}_{a}"
    w = V9 / "lines" / "work" / sa
    out = w / "synth" / arm
    reading = out / f"{sa}.reading.tr.md"
    problems, _ = R.reading_problems(reading, w)
    plan = out / f"{sa}.plan.md"
    plan_problems = SP.check_plan_text(plan.read_text(encoding="utf-8"), (w / "package.md").read_text(encoding="utf-8")) \
        if plan.exists() else ["no plan"]
    text = reading.read_text(encoding="utf-8")
    words = len(text.split())
    ayat = len(set(re.findall(r"\((\d{1,3}:\d{1,3})\)", text)))
    tags = text.count("{ar:")
    print(f"{arm}: {words} words, {ayat} distinct ayat cited, {tags} Arabic tags; reading problems {len(problems)}"
          f"{': ' + '; '.join(problems[:5]) if problems else ''}; plan problems {len(plan_problems)}"
          f"{': ' + '; '.join(plan_problems[:5]) if plan_problems else ''}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ref")
    ap.add_argument("--arm", required=True, choices=("sol1", "sol56", "opus1", "w10-sol", "w10-luna", "w10-opus", "w10-opus-cold"))
    ap.add_argument("--check-only", action="store_true")
    a = ap.parse_args()
    if a.check_only:
        return check(a.ref, a.arm)
    run_arm(a.ref, a.arm)


if __name__ == "__main__":
    main()
