#!/usr/bin/env python3
"""The synthesizer's package: one document with everything the discovery found, ranked and never filtered.

  1  the lexical network: backbone hubs, Luna hubs, Fatiha links, triangles, bridges, word-level links
     (from network/out/S_A/sol/backbone.md, sections 2–7)
  2  the four discovery lines (local, usage, surah, related): readings and open observations in full (finding,
     exact excerpts, what activates it, limits or what is missing, support, relevance), ordered by relevance then
     support; notes compact; misreadings rejected as `wrong` one line each; other rejections counted
  3  the full text of every cited ayah outside the surah and the Fatiha (context.md holds those)

Usage: python3 _commentary/v9/lines/package.py 18:86  → lines/work/S_A/package.md
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

V9 = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(V9))
from verify_ar import QURAN_TEXT  # noqa: E402

LINES = ("local", "usage", "surah", "related")
TITLE = {"local": "Local language (the ayah's own words, grammar, variant readings)",
         "usage": "Quranic usage (each root's occurrences: same form, other forms)",
         "surah": "Surah context (the passage, the roots elsewhere in the surah, surah-level arguments)",
         "related": "Related passages (inter-ayah targets, the same people, formula families)"}
RANK = {"high": 0, "medium": 1, "low": 2, "strong": 0, "weak": 2}


def quran() -> dict[str, str]:
    q = {}
    for line in QURAN_TEXT.read_text(encoding="utf-8-sig").splitlines():
        r, _, t = line.partition("|")
        q[r.strip()] = t.strip()
    return q


def main() -> None:
    ref = sys.argv[1]
    s, a = ref.split(":")
    sa = f"{s}_{a}"
    w = V9 / "lines" / "work" / sa
    q = quran()
    titles = {}
    for f in w.glob("*_*.md"):
        for m in re.finditer(r"^### (\S+) (.*)$", f.read_text(encoding="utf-8"), re.M):
            titles[m.group(1)] = m.group(2)[:160]
    records = defaultdict(list)
    for f in sorted((w / "records").glob("*.jsonl")):
        line = f.stem.split("_")[0]
        for l in f.read_text(encoding="utf-8").splitlines():
            if l.strip().startswith("{"):
                r = json.loads(l)
                if str(r.get("id", "")).startswith("X"):
                    r["id"] = f"{f.stem}.{r['id']}"
                records[line].append(r)
    cited = set()
    L = [f"# Package for {ref}", "",
         "Everything the discovery stage found, for one reader who connects it. Section 1 is the lexical network",
         "(ids H, L, F, T, J, G): rare dictionary senses of the ayah's words converging on other words, checked by",
         "the dictionaries' own relations and a judge. Section 2 holds the four discovery lines (ids L.., U-, S-, R-,",
         "and X records): readings, open observations (a precise link whose decisive support is missing; another line",
         "may supply it), notes, and misreadings. `support` says how well the sources establish a record; `relevance`",
         "how much it could change the reading — they are separate judgments, and nothing here is filtered by them.",
         "Section 3 is the text of cited ayat outside the surah and the Fatiha (both are in context.md).", ""]
    # 1 lexical network
    bb = V9 / "network" / "out" / sa / "sol" / "backbone.md"
    if bb.exists():
        text = bb.read_text(encoding="utf-8")
        parts = re.split(r"^(## \d+\. .*)$", text, flags=re.M)
        keep = []
        for i in range(1, len(parts) - 1, 2):
            n = int(re.match(r"## (\d+)\.", parts[i]).group(1))
            if 2 <= n <= 7:
                keep.append(parts[i].replace("## ", "### ", 1) + parts[i + 1])
        body = "".join(keep)
        cited |= set(re.findall(r"\b(\d{1,3}:\d{1,3})\b", body))
        L += ["## 1. Lexical network", "", body.strip(), ""]
    else:
        L += ["## 1. Lexical network", "", "(not built for this ayah)", ""]
    # 2 lines
    L += ["## 2. Discovery lines", ""]
    for line in LINES:
        recs = records.get(line, [])
        live = [r for r in recs if r.get("status") in ("reading", "open")]
        live.sort(key=lambda r: (RANK.get(str(r.get("relevance")), 3), RANK.get(str(r.get("support")), 3),
                                 r.get("status") != "reading"))
        notes = [r for r in recs if r.get("status") == "note"]
        notes.sort(key=lambda r: (RANK.get(str(r.get("relevance")), 3), RANK.get(str(r.get("support")), 3)))
        wrong = [r for r in recs if r.get("status") == "none" and str(r.get("code", "")).startswith("wrong")]
        other = Counter(str(r.get("code", "?")).split(":")[0] for r in recs
                        if r.get("status") == "none" and not str(r.get("code", "")).startswith("wrong"))
        L += [f"### 2.{LINES.index(line) + 1} {TITLE[line]}", "",
              f"{len(live)} readings and open observations, {len(notes)} notes, {len(wrong)} misreadings rejected; "
              f"other items with nothing to add: {dict(other) or 0}.", ""]
        for r in live:
            ev = "; ".join(f"{e.get('ref')} «{e.get('ar')}»" for e in r.get("evidence") or [])
            cited |= {str(e.get("ref")) for e in r.get("evidence") or []}
            tail = f"missing: {r.get('missing', '')}" if r.get("status") == "open" else f"limits: {r.get('limits', '')}"
            L.append(f"- **{r['id']}** [{r['status']}; support {r.get('support')}, relevance {r.get('relevance')}] "
                     f"{titles.get(str(r['id']), '')}")
            L.append(f"  - finding: {r.get('finding', '')}")
            L.append(f"  - evidence: {ev}")
            if r.get("activation"):
                L.append(f"  - activation: {r['activation']}")
            L.append(f"  - {tail}")
        if notes:
            L += ["", "Notes:"]
            for r in notes:
                cited |= {str(e.get("ref")) for e in r.get("evidence") or []}
                L.append(f"- {r['id']} [support {r.get('support')}, relevance {r.get('relevance')}] {r.get('finding', '')}")
        if wrong:
            L += ["", "Rejected as misreadings:"]
            L += [f"- {r['id']}: {r.get('code')} {r.get('finding', '') or r.get('reason', '')}" for r in wrong]
        L.append("")
    # 3 texts
    focus_s = f"{s}:"
    refs = sorted({r for r in cited if r in q and not r.startswith((focus_s, "1:"))},
                  key=lambda r: tuple(map(int, r.split(":"))))
    L += ["## 3. Text of cited ayat outside the surah and the Fatiha", ""] + [f"- {r} {q[r]}" for r in refs]
    (w / "package.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"package: {w / 'package.md'} ({len(chr(10).join(L).encode()):,} bytes); line records "
          f"{ {k: len(v) for k, v in records.items()} }")


if __name__ == "__main__":
    main()
