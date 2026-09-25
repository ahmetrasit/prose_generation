#!/usr/bin/env python3
"""Mechanical checks on a written reading, plus an automatic harvest. No model involved.

  catalogue   paragraphs citing many distinct ayat (default ≥ 10; Ek Notlar excluded): a report on possible
              list-like stretches, for people to read — never an automatic rewrite
  harvest     for every kept Luna record, whether the reading uses it: its trigger Arabic appears in a tag
              or its cited ayah is cited (approximate, by string matching); written to <reading>.auto-harvest.md

Usage: python3 _commentary/v9/luna/check_reading.py READING WORK_DIR [--max-citations 10]
Prints `catalogue: <n> paragraph(s)` with line numbers and the harvest summary; always exits 0.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from verify_ar import loose  # noqa: E402

CITE = re.compile(r"\((\d{1,3}:\d{1,3})\)")
TAG = re.compile(r"\{\s*ar\s*:\s*([^,{}]+?)\s*,")


def paragraphs(text: str) -> list[tuple[int, str, str]]:
    """(first line number, section heading, paragraph text)."""
    out, section, start, buf = [], "", 1, []
    for n, line in enumerate(text.splitlines() + [""], 1):
        if line.startswith("## "):
            section = line[3:].strip()
        if line.strip():
            if not buf:
                start = n
            buf.append(line)
        elif buf:
            out.append((start, section, "\n".join(buf)))
            buf = []
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("reading")
    ap.add_argument("work")
    ap.add_argument("--max-citations", type=int, default=10)
    a = ap.parse_args()
    reading, work = Path(a.reading), Path(a.work)
    text = reading.read_text(encoding="utf-8")
    paras = paragraphs(text)

    flagged = [(n, sec, len(set(CITE.findall(p)))) for n, sec, p in paras
               if sec != "Ek Notlar" and len(set(CITE.findall(p))) >= a.max_citations]
    print(f"catalogue: {len(flagged)} paragraph(s) citing ≥{a.max_citations} ayat")
    for n, sec, k in flagged:
        print(f"  line {n} ({sec}): {k} ayat")

    records = []
    for f in sorted((work / "records").glob("*.jsonl")):
        for l in f.read_text(encoding="utf-8").splitlines():
            if l.strip():
                r = json.loads(l)
                if r.get("verdict") in ("reading", "note"):
                    if str(r.get("id", "")).startswith("X"):
                        r["id"] = f"{f.stem}.{r['id']}"
                    records.append(r)
    tag_by_para = [(sec, {loose(t)[0].strip() for t in TAG.findall(p)}, set(CITE.findall(p))) for _, sec, p in paras]
    used, unused = defaultdict(list), []
    for r in records:
        t = loose(str(r.get("trigger_ar", "")))[0].strip()
        ref = str(r.get("trigger_ref", ""))
        where = next((sec for sec, tags, cites in tag_by_para
                      if t and any(t in x or (len(x) > 3 and x in t) for x in tags)
                      and (ref in cites or ref.split(":")[0] == "1" or not cites or ref in text)), None)
        (used[where].append(r["id"]) if where else unused.append(r))
    lines = [f"# Automatic harvest for {reading.name} (string matching; approximate)", "",
             f"Used: {sum(len(v) for v in used.values())} of {len(records)} kept records.", ""]
    for sec, ids in used.items():
        lines.append(f"- **{sec}**: {', '.join(ids)}")
    lines += ["", "## Not found in the reading", ""]
    by_kind = defaultdict(list)
    for r in unused:
        by_kind[f"{r['verdict']} {r['id'][0]}"].append(r["id"])
    lines += [f"- {k} ({len(v)}): {', '.join(v)}" for k, v in sorted(by_kind.items())]
    out = reading.with_name(reading.stem.replace(".reading.tr", "") + ".auto-harvest.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"harvest: {sum(len(v) for v in used.values())}/{len(records)} records used → {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
