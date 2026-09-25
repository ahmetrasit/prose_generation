#!/usr/bin/env python3
"""Merge checked Luna records into the writer's input and a mechanical harvest.

  findings.md        readings and notes grouped by focus word, each with the item's own evidence line
                     (dictionary sense for branches, trace for HFT, row label for inter-ayah), then the
                     full text of every ayah the records cite
  records_index.md   every record by verdict and code (accountability; the writer does not read it)

Usage: python3 _commentary/v9/luna/merge.py WORK_DIR
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from verify_ar import QURAN_TEXT, loose  # noqa: E402


def item_texts(work: Path) -> dict[str, str]:
    out = {}
    for f in sorted(work.glob("W*.md")):
        for chunk in f.read_text(encoding="utf-8").split("\n### ")[1:]:
            iid = chunk.split(" ", 1)[0]
            out[iid] = chunk
    return out


def evidence(iid: str, texts: dict[str, str]) -> str:
    """The item's source evidence: a numbered line (with its branch's dictionary sense) or the item head."""
    m = re.match(r"^(.+)\.(\d+)$", iid)
    if m and m.group(1) in texts:
        text = texts[m.group(1)]
        line = next((l for l in text.splitlines() if l.startswith(f"[{m.group(2)}] ")), "")
        return f"{line[:400]} | {evidence(m.group(1), texts)[:200]}"
    if iid not in texts:
        return ""
    lines = texts[iid].splitlines()
    if iid.startswith("R") and ".B" in iid:
        d = next((l for l in lines if l.startswith("dictionary:")), "")
        return re.sub(r"\*\*B\d{3}\*\* ", "", d.removeprefix("dictionary: "))[:400]
    if iid.startswith("G"):
        return " / ".join(l.strip("- ") for l in lines[1:] if l.startswith("- "))[:400]
    return lines[0][:200]


def main() -> None:
    work = Path(sys.argv[1])
    texts = item_texts(work)
    records = []
    for f in sorted((work / "records").glob("*.jsonl")):
        for l in f.read_text(encoding="utf-8").splitlines():
            if l.strip():
                r = json.loads(l)
                if str(r.get("id", "")).startswith("X"):  # extra findings: X ids restart in every worklist
                    r["id"] = f"{f.stem}.{r['id']}"
                records.append(r)
    context = (work / "context.md").read_text(encoding="utf-8")
    focus_ref = context.split(" — ", 1)[0].lstrip("# ").strip()
    words = re.findall(r"^\| \d+ \| (\S+) \|", context, re.M)

    def word_of(r):
        fa = loose(r.get("focus_ar", ""))[0]
        return next((w for w in words if fa and (fa in loose(w)[0] or loose(w)[0] in fa)), r.get("focus_ar") or "—")

    kept = [r for r in records if r.get("verdict") in ("reading", "note")]
    records = [r for r in records if "verdict" in r or "lines" not in r]  # line-code carriers are not findings
    by_word = defaultdict(list)
    for r in kept:
        by_word[word_of(r)].append(r)
    order = {w: i for i, w in enumerate(words)}
    lines = [f"# Findings for {focus_ref} (Luna records: {sum(r['verdict'] == 'reading' for r in kept)} readings, "
             f"{sum(r['verdict'] == 'note' for r in kept)} notes, {len(records) - len(kept)} not used)", "",
             "Per focus word: readings (both keys in Luna's judgement) with the image they hear, Luna's reason and,",
             "for dictionary branches, the branch sense; then notes (one key), one line each. Verify before use:",
             "the worklist item behind any id is in the W*.md files of this directory.", ""]
    for w in sorted(by_word, key=lambda w: order.get(w, 99)):
        lines += [f"## {w}", ""]
        for r in sorted((r for r in by_word[w] if r["verdict"] == "reading"), key=lambda r: r["id"]):
            lines.append(f"- **{r['id']}** {r.get('branch') or ''} · {r.get('trigger_ar')} ({r.get('trigger_ref')})"
                         f" — {r.get('after', '')}")
            lines.append(f"  - {r.get('reason', '')}")
            if r["id"].startswith("R"):
                src = evidence(r["id"], texts)
                sense = re.search(r"\| ([^|]+) \| ([^|]+) \|", src.split(" | ", 1)[-1] if ".B" in r["id"] else src)
                if sense:
                    lines.append(f"  - branch: {sense.group(1).strip()} / {sense.group(2).strip()}")
        notes = sorted((r for r in by_word[w] if r["verdict"] == "note"), key=lambda r: r["id"])
        if notes:
            lines += ["", "Notes:"] + [f"- {r['id']} {r.get('branch') or ''} · {r.get('trigger_ar')} "
                                       f"({r.get('trigger_ref')}) — {r.get('after', '')}" for r in notes]
        lines.append("")

    quran = {}
    for line in QURAN_TEXT.read_text(encoding="utf-8-sig").splitlines():
        ref, _, ayah = line.partition("|")
        if ayah:
            quran[ref.strip()] = ayah.lstrip("﻿")
    refs = sorted({r["trigger_ref"] for r in kept if r.get("trigger_ref") in quran and not r["trigger_ref"].startswith(("1:", focus_ref.split(":")[0] + ":"))},
                  key=lambda x: tuple(map(int, x.split(":"))))
    lines += ["# Cited ayat outside the surah and the Fatiha (full text)", ""] + [f"- {x} {quran[x]}" for x in refs]
    (work / "findings.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    idx = ["# Records index (every item's verdict)", ""]
    groups = defaultdict(list)
    for r in records:
        groups[r.get("verdict") if r.get("verdict") != "none" else f"none: {r.get('code', '').split(':')[0]}"].append(r["id"])
    for k in sorted(groups):
        idx.append(f"- {k} ({len(groups[k])}): {', '.join(sorted(groups[k]))}")
    (work / "records_index.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
    print(f"{len(records)} records → findings.md ({(work / 'findings.md').stat().st_size} bytes)")


if __name__ == "__main__":
    main()
