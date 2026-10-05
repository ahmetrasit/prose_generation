#!/usr/bin/env python3
"""The page agent's own check (user, 2026-10-05: the agent never writes or runs its own validator): the records the
finish step would drop, with the reason; where each kept block lands (¶n → ids, and paragraphs over five blocks);
and every Arabic stretch of four or more words in a record's metin that none of its cited segments holds (verbatim,
normalised, or as a near-verbatim run). Prints problems only, then one summary line. Fast (index lookups only).

  python3 enrichment/v2/tools/check.py --surah 1 --target 1:1 --annotations <call dir>/annotations.jsonl

Parts (annotations.1.jsonl, annotations.2.jsonl …) beside the named file are checked together, in order.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

V2 = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(V2))
sys.path.insert(0, str(V2 / "tools"))
import corpus as C  # noqa: E402
import render as R  # noqa: E402
import validate as VAL  # noqa: E402

ARABIC_RUN = re.compile(r"[؀-ۿ][؀-ۿً-ٰٟ\s،؛]*[؀-ۿً-ٰٟ]")


def parts_of(ann: Path) -> list[Path]:
    """annotations.jsonl itself if it exists, else annotations.1.jsonl, annotations.2.jsonl … in order."""
    if ann.exists():
        return [ann]
    return sorted(ann.parent.glob(f"{ann.stem}.[0-9]*.jsonl"), key=lambda p: int(p.suffixes[-2].lstrip(".")))


def load(paths: list[Path]) -> tuple[list[dict], list[str]]:
    recs, errs = [], []
    for p in paths:
        for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                recs.append(json.loads(line))
            except json.JSONDecodeError as e:
                errs.append(f"{p.name} line {n}: not JSON ({e})")
    return recs, errs


def segment_texts(con, locs: list[str]) -> str:
    out = []
    for loc in locs:
        row = (con.execute("SELECT text, extra FROM seg WHERE seg=?", (loc,)).fetchone()
               or con.execute("SELECT text, extra FROM seg WHERE seg>=? AND seg<? LIMIT 1", (loc + "#", loc + "$")).fetchone())
        if row:
            out.append((row[0] or "") + " " + C.flat(json.loads(row[1] or "{}").get("en", "")))
    return "\n".join(out)


def quote_problems(con, r: dict) -> list[str]:
    """Arabic stretches of 4+ words in metin that none of the record's cited segments holds."""
    locs = [x.strip() for x in str(r.get("kaynak") or "").split("|") if x.strip() and x.strip() != "hafiza"]
    if not locs:
        return []
    src = None
    probs = []
    for m in ARABIC_RUN.finditer(r.get("metin", "")):
        q = m.group().strip()
        if len(q.split()) < 4:
            continue
        if src is None:
            src = segment_texts(con, locs)
            src_n = C.norm(src)
        if C.norm(q) in src_n:
            continue
        sys.path.insert(0, str(V2))
        import okuma as O  # the near-verbatim matcher (punctuation, brackets, footnote marks ignored; 85% words)
        if O.near_quote(q, src):
            continue
        probs.append(f"{r.get('id')}: Arabic not found in its cited sources ({' | '.join(locs)}): {q[:80]}")
    return probs


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--surah", type=int, required=True)
    ap.add_argument("--target", required=True)
    ap.add_argument("--annotations", type=Path, required=True)
    a = ap.parse_args()
    paths = parts_of(a.annotations)
    if not paths:
        sys.exit(f"no {a.annotations.name} and no parts beside it")
    recs, errs = load(paths)
    for e in errs:
        print(f"FAIL {e}")
    kept, dropped, warnings = VAL.check_records(a.surah, a.target, recs)
    for d in dropped:
        for e in d["errors"]:
            print(f"FAIL {e}")
    for w in warnings:
        print(f"WARN {w}")
    con = C.connect()
    qp = [p for r in kept for p in quote_problems(con, r)]
    for p in qp:
        print(f"QUOTE {p}")
    where = defaultdict(list)
    for r in kept:
        where[str(r.get("paragraf", "?")).lstrip("¶").strip()].append(r.get("id"))
    n_prose = sum(1 for p in R.paragraphs(R.target_page(a.surah, a.target)[1]) if R.is_prose(p))  # the [¶n] count
    empty = [str(i) for i in range(1, n_prose + 1) if str(i) not in where]
    print("MAP " + "; ".join(f"¶{k}: {', '.join(v)}" for k, v in sorted(where.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 0)))
    if empty:
        print(f"MAP paragraphs with no block: {', '.join('¶' + x for x in empty)}")
    print(f"{len(recs)} records in {', '.join(p.name for p in paths)}: {len(kept)} kept, {len(dropped)} would be "
          f"dropped, {len(qp)} quotes not found, {len(warnings)} warnings")


if __name__ == "__main__":
    main()
