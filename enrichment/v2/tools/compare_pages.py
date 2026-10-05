#!/usr/bin/env python3
"""Compare trial pages of one target with a reference page (user, 2026-10-05: the cost trials must show what a
cheaper page loses). Per trial: records kept/dropped (check.json), cost recorded and estimated, turns, records by
tur, the reference's cited segments the trial also cites, the reference records with at least one shared segment,
the trial's own new segments, meal blocks, the coverage audit and unread sources. A proxy, not a judgement: the
user reads the pages.

  python3 enrichment/v2/tools/compare_pages.py --ref work/s001/zengin.1_1.opus.high work/s001/zengin-tur.1_1.opus.high …
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

V2 = Path(__file__).resolve().parents[1]


def load(d: Path) -> tuple[list[dict], dict]:
    ann = d / "annotations.jsonl"
    recs = [json.loads(x) for x in ann.read_text(encoding="utf-8").splitlines() if x.strip()] if ann.exists() else []
    log = json.loads((d / "run.log.json").read_text(encoding="utf-8")) if (d / "run.log.json").exists() else {}
    return recs, log


def locs(r: dict) -> set[str]:
    return {x.strip() for x in str(r.get("kaynak") or "").split("|") if x.strip() and x.strip() != "hafiza"}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ref", type=Path, required=True)
    ap.add_argument("dirs", type=Path, nargs="+")
    a = ap.parse_args()
    fix = lambda p: p if p.is_absolute() else (V2 / p)
    ref, rlog = load(fix(a.ref))
    ref_locs = set().union(*map(locs, ref)) if ref else set()
    rows = []
    for d in [fix(a.ref)] + [fix(x) for x in a.dirs]:
        recs, log = load(d)
        kept = log.get("kept", len(recs))
        mine = set().union(*map(locs, recs)) if recs else set()
        shared = mine & ref_locs
        ref_hit = sum(1 for r in ref if locs(r) & mine)
        cov = log.get("coverage") or {}
        rows.append({
            "dir": d.name, "status": log.get("status"), "records": len(recs), "kept": kept,
            "dropped": len(log.get("dropped") or []) if isinstance(log.get("dropped"), list) else log.get("dropped"),
            "cost": log.get("cost_usd"), "cost_est": log.get("cost_usd_est"), "turns": log.get("num_turns"),
            "segments_cited": len(mine), "ref_segments_also_cited": f"{len(shared)}/{len(ref_locs)}",
            "ref_records_with_shared_segment": f"{ref_hit}/{len(ref)}", "new_segments": len(mine - ref_locs),
            "meal_blocks": sum(1 for r in recs if r.get("tur") == "meal"),
            "by_tur": dict(Counter(r.get("tur") for r in recs).most_common()),
            "unread_sources": len(log.get("unread_sources") or []),
            "audit": {k: (len(v) if isinstance(v, list) else v) for k, v in cov.items()},
        })
    for r in rows:
        print(json.dumps(r, ensure_ascii=False))


if __name__ == "__main__":
    main()
