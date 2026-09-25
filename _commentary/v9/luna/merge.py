#!/usr/bin/env python3
"""Merge checked Luna records into the writer's input and an index. Mechanical only: no ranking by
content, no image lexicon, and every kept record is pushed (nothing is held back for later lookup).

  findings.md        1. findings on the ayah's words (branch, usage, dictionary, HFT, lead and extra records),
                        grouped by focus word: readings with the image, Luna's reason and the branch's
                        dictionary sense (gloss, Arabic image, source phrase); notes compact, with the sense
                     2. whole-Quran parallels (inter-ayah and same-people records), compact, by focus word
                     3. shared triggers: the same Arabic trigger in the same ayah hit by records of two or
                        more roots (a mechanical join signal)
                     4. the full text of every cited ayah outside the surah and the Fatiha
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
    order = {w: i for i, w in enumerate(words)}

    def sense(r):
        """Dictionary sense of the record's branch: gloss / Arabic image / source phrase."""
        iid = re.sub(r"\.\d+$", "", r["id"])
        d = next((l for l in texts.get(iid, "").splitlines() if l.startswith("dictionary:")), "")
        f = [x.strip() for x in re.sub(r"\*\*B\d{3}\*\* ", "", d.removeprefix("dictionary: ")).split("|")]
        if len(f) < 2:
            return ""
        src_phrase = next((x.removeprefix("src:").strip() for x in f if x.startswith("src:")), "")
        return " / ".join(x for x in (f[0], f[1], src_phrase[:200]) if x)

    def partner(r):
        m = re.match(r"^(.+)\.(\d+)$", r["id"])
        if not m:
            return ""
        return next((l for l in texts.get(m.group(1), "").splitlines() if l.startswith(f"[{m.group(2)}] ")), "")[:260]

    def root_of(r):
        m = re.match(r"((?:[ء-ي] ){1,5}[ء-ي])", r.get("branch") or "")
        return m.group(1) if m else word_of(r)

    ayah_level = [r for r in kept if not r["id"].startswith(("G", "P"))]
    parallels = [r for r in kept if r["id"].startswith(("G", "P"))]
    lines = [f"# Findings for {focus_ref} — Luna kept {len(kept)} of {len(records)} records "
             f"({sum(r['verdict'] == 'reading' for r in kept)} readings, {sum(r['verdict'] == 'note' for r in kept)} notes)",
             "", "Luna judged generously on purpose (a miss costs more than a false alarm). Ids point to the worklist",
             "items in the W*.md files of this directory.", "", "# 1. Findings on the ayah's words", ""]
    by_word = defaultdict(list)
    for r in ayah_level:
        by_word[word_of(r)].append(r)
    for w in sorted(by_word, key=lambda w: order.get(w, 99)):
        lines += [f"## {w}", ""]
        for r in sorted((r for r in by_word[w] if r["verdict"] == "reading"), key=lambda r: r["id"]):
            lines.append(f"- **{r['id']}** reading · {r.get('branch') or ''} · {r.get('trigger_ar')} ({r.get('trigger_ref')})"
                         f" — {r.get('after', '')}")
            lines.append(f"  - {r.get('reason', '')}")
            for extra in (sense(r), partner(r)):
                if extra:
                    lines.append(f"  - {extra}")
        notes = sorted((r for r in by_word[w] if r["verdict"] == "note"), key=lambda r: r["id"])
        if notes:
            lines += ["", "Notes:"]
            for r in notes:
                sn = sense(r)
                lines.append(f"- {r['id']} {r.get('branch') or ''} · {r.get('trigger_ar')} ({r.get('trigger_ref')})"
                             f" — {r.get('after', '')}" + (f" [{sn}]" if sn else ""))
        lines.append("")

    lines += ["# 2. Whole-Quran parallels (other ayat; compact)", ""]
    by_word = defaultdict(list)
    for r in parallels:
        by_word[word_of(r)].append(r)
    for w in sorted(by_word, key=lambda w: order.get(w, 99)):
        lines += [f"## {w}", ""] + [
            f"- {r['id']} {r['verdict']} · {r.get('trigger_ar')} ({r.get('trigger_ref')}) — {str(r.get('after', ''))[:200]}"
            for r in sorted(by_word[w], key=lambda r: (r["verdict"] != "reading", r["id"]))] + [""]

    lines += ["# 3. Shared triggers (same Arabic trigger, same ayah, records of two or more roots)", ""]
    trig = defaultdict(list)
    for r in kept:
        key = (loose(str(r.get("trigger_ar", "")))[0].strip(), r.get("trigger_ref"))
        if key[0]:
            trig[key].append(r)
    for (t, ref), rs in sorted(trig.items(), key=lambda kv: -len({root_of(r) for r in kv[1]})):
        roots = sorted({root_of(r) for r in rs})
        if len(roots) >= 2:
            lines.append(f"- {rs[0].get('trigger_ar')} ({ref}) ← {len(roots)} roots: " +
                         "; ".join(f"{rt}: {', '.join(r['id'] for r in rs if root_of(r) == rt)}" for rt in roots))
    lines.append("")

    quran = {}
    for line in QURAN_TEXT.read_text(encoding="utf-8-sig").splitlines():
        ref, _, ayah = line.partition("|")
        if ayah:
            quran[ref.strip()] = ayah.lstrip("﻿")
    refs = sorted({r["trigger_ref"] for r in kept if r.get("trigger_ref") in quran and not r["trigger_ref"].startswith(("1:", focus_ref.split(":")[0] + ":"))},
                  key=lambda x: tuple(map(int, x.split(":"))))
    lines += ["# 4. Cited ayat outside the surah and the Fatiha (full text)", ""] + [f"- {x} {quran[x]}" for x in refs]
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
