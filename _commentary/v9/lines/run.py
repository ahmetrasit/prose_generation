#!/usr/bin/env python3
"""Run the V9 discovery lines for one ayah: one Luna session per worklist bundle (gpt-6-luna, reasoning effort max,
everything pushed, records returned as the final message), then check the records.

  python3 _commentary/v9/lines/run.py run 18:86 [--parallel 4] [--only usage,related_2]
  python3 _commentary/v9/lines/run.py check 18:86
  python3 _commentary/v9/lines/run.py usage 18:86      token usage per session

Checks: every item of the bundle has exactly one record; status is reading / note / open / none; readings, notes and
open records have finding, evidence, support, relevance (open: missing); every evidence excerpt occurs in the cited
ayah (diacritics ignored). Problems for a bundle go to one fresh repair session that may only add or fix records.
"""
from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

V9 = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(V9 / "luna"))
sys.path.insert(0, str(V9))
import run as R  # noqa: E402
from verify_ar import QURAN_TEXT, loose  # noqa: E402

LUNA = "gpt-6-luna"
STATUSES = {"reading", "note", "open", "none"}


def work(ref: str) -> Path:
    s, a = ref.split(":")
    return V9 / "lines" / "work" / f"{s}_{a}"


def quran() -> dict[str, str]:
    q = {}
    for line in QURAN_TEXT.read_text(encoding="utf-8-sig").splitlines():
        r, _, t = line.partition("|")
        q[r.strip()] = loose(t)[0]
    return q


def check_bundle(w: Path, name: str, q: dict) -> list[str]:
    ids = [l.split("\t")[0] for l in (w / "items.tsv").read_text(encoding="utf-8").splitlines()
           if l.endswith("\t" + name)]
    recs = R.parse_jsonl((w / "records" / (Path(name).stem + ".jsonl")).read_text(encoding="utf-8")) \
        if (w / "records" / (Path(name).stem + ".jsonl")).exists() else []
    by = {}
    problems = []
    for r in recs:
        rid = str(r.get("id", ""))
        if rid in by:
            problems.append(f"{rid}: duplicate record")
        by[rid] = r
    for iid in ids:
        if iid not in by:
            problems.append(f"{iid}: no record")
    for rid, r in by.items():
        if rid not in ids and not rid.startswith("X"):
            problems.append(f"{rid}: not an item of this worklist (extra findings use X1, X2 …)")
        st = r.get("status")
        if st not in STATUSES:
            problems.append(f"{rid}: status {st!r}")
            continue
        if st == "none":
            continue
        for f in ("finding", "evidence", "support", "relevance"):
            if not r.get(f):
                problems.append(f"{rid}: no {f}")
        if st == "open" and not r.get("missing"):
            problems.append(f"{rid}: open without missing")
        for ev in r.get("evidence") or []:
            ref, ar = str(ev.get("ref", "")), loose(str(ev.get("ar", "")))[0].strip()
            if ref in q and ar and ar not in q[ref]:
                problems.append(f"{rid}: excerpt not in {ref}: {ev.get('ar', '')[:60]}")
            elif ref not in q:
                problems.append(f"{rid}: unknown ref {ref!r}")
    return problems


def run_bundle(w: Path, name: str, q: dict) -> str:
    stem = Path(name).stem
    (w / "records").mkdir(exist_ok=True)
    (w / "logs").mkdir(exist_ok=True)
    recs = w / "records" / f"{stem}.jsonl"
    if not recs.exists():
        text = R.codex(LUNA, f"Follow the brief below (luna_line.md) exactly. Your worklist is {name}; the brief, "
                             f"context.md and the worklist follow in full. Return the records as your final message.",
                       w / "logs" / f"{stem}.jsonl",
                       stdin=R.inline(V9 / "prompts" / "luna_line.md", w / "context.md", w / name),
                       last=w / "logs" / f"{stem}.last.txt", sandbox="read-only")
        recs.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in R.parse_jsonl(text)), encoding="utf-8")
    problems = check_bundle(w, name, q)
    if problems:
        before = recs.read_text(encoding="utf-8")
        text = R.codex(LUNA, "Follow the brief below (luna_line.md). Your earlier records for this worklist follow; a "
                             "checker found these problems:\n- " + "\n- ".join(problems[:40]) +
                             "\nReturn the complete corrected set of records (all items) as your final message. Never "
                             "drop a reading, note or open record; fix it.",
                       w / "logs" / f"{stem}.repair.jsonl",
                       stdin=R.inline(V9 / "prompts" / "luna_line.md", w / "context.md", w / name) +
                       f"\n\n===== earlier records =====\n{before}",
                       last=w / "logs" / f"{stem}.repair.last.txt", sandbox="read-only")
        fixed = R.parse_jsonl(text)
        kept_before = {r.get("id") for r in R.parse_jsonl(before) if r.get("status") in ("reading", "note", "open")}
        kept_after = {r.get("id") for r in fixed if r.get("status") in ("reading", "note", "open")}
        if fixed and kept_before <= kept_after:
            recs.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in fixed), encoding="utf-8")
        problems = check_bundle(w, name, q)
    n = len(R.parse_jsonl(recs.read_text(encoding="utf-8")))
    return f"{name}: {n} records, {len(problems)} problem(s)" + (f" — {problems[:3]}" if problems else "")


def usage(ref: str) -> None:
    w = work(ref)
    tot = {}
    for log in sorted((w / "logs").glob("*.jsonl")):
        t = {}
        for line in log.read_text(encoding="utf-8").splitlines():
            if '"turn.completed"' in line:
                for k, v in json.loads(line).get("usage", {}).items():
                    t[k] = t.get(k, 0) + (v or 0)
        for k, v in t.items():
            tot[k] = tot.get(k, 0) + v
        print(f"{log.stem:28} in {t.get('input_tokens', 0):>8,} cached {t.get('cached_input_tokens', 0):>8,} "
              f"out {t.get('output_tokens', 0):>7,} reasoning {t.get('reasoning_output_tokens', 0):>7,}")
    print(f"{'TOTAL':28} in {tot.get('input_tokens', 0):>8,} cached {tot.get('cached_input_tokens', 0):>8,} "
          f"out {tot.get('output_tokens', 0):>7,} reasoning {tot.get('reasoning_output_tokens', 0):>7,}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=("run", "check", "usage"))
    ap.add_argument("ref")
    ap.add_argument("--parallel", type=int, default=4)
    ap.add_argument("--only", default="", help="only these lines or bundles, comma-separated (usage, related_2 …)")
    a = ap.parse_args()
    if a.step == "usage":
        return usage(a.ref)
    w = work(a.ref)
    q = quran()
    only = [o for o in a.only.split(",") if o]
    names = sorted(p.name for p in w.glob("*_*.md")
                   if not only or any(p.stem == o or p.name.startswith(o + "_") for o in only))
    if a.step == "check":
        for n in names:
            print(n, check_bundle(w, n, q)[:5])
        return
    with ThreadPoolExecutor(a.parallel) as pool:
        for line in pool.map(lambda n: run_bundle(w, n, q), names):
            print(line, flush=True)


if __name__ == "__main__":
    main()
