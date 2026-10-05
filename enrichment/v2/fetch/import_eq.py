#!/usr/bin/env python3
"""EQ: Encyclopaedia of the Qurʾān, ed. J. D. McAuliffe (Brill 2001–2006), six volumes in one PDF from the user's
download (raw/acquired-2026-10-05/encyclopaedia-quran-six-volumes.pdf, 3,956 PDF pages; text layer good). Run
fetch/pdf_pages.py on ACADEMIC/EQ first.

One segment per printed page, cited the way EQ is cited: EQ:v<vol>p<page> (volume i–v body pages; the printed
number is read from the running header and must agree with its neighbours), else EQ:pdf<n> (plates, front matter,
the index volume, any page whose number cannot be read). `head` is the running header (the article's name).

Text repairs (counted in the ingestion record): glyph names the text layer writes out are replaced by their letters
(/righthalfmoon ʾ, /lefthalfmoon ʿ, /Asmallmacron ā, /Slowerdot Ṣ, /Hsmalldot ḥ, /G101 = chr(101) …); the font's
dot-above letters stand for EQ's dot-below transliteration (ḣ → ḥ, ḋ → ḍ, ṡ → ṣ, ṫ → ṭ, ż → ẓ). Nothing else.

`refs` = the ayat a page cites («q 5:108», «q 6:59, 63 and 97») plus the ayat the index volume's «Index of
Qurʾān citations» sends to that page (it lists, verse by verse, volume, page, column and article). Index lines
whose page cannot be found are counted and listed.

  python3 -B enrichment/v2/fetch/import_eq.py [--dry]
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402

SID, STEM = "EQ", "encyclopaedia-quran-six-volumes"
VOLUMES = [(1, 1, 620), (2, 621, 1218), (3, 1219, 1862), (4, 1863, 2499), (5, 2500, 3090)]  # PDF pages
INDEX_VOL = (3091, 3956)
CITATIONS = (3513, 3956)  # «Index of Qurʾān citations», to the end of the PDF
ROMAN = {"i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5}
GLYPH = {"righthalfmoon": "ʾ", "lefthalfmoon": "ʿ"}
MARKS = {"smallmacron": "̄", "macron": "̄", "lowerdot": "̣", "smalldot": "̣", "dot": "̣",
         "underscore": "̱", "cedilla2": "̧", "cedilla": "̧"}
GLYPH_RX = re.compile(r"/(righthalfmoon|lefthalfmoon|G(\d{2,3})|([A-Za-z])(smallmacron|macron|lowerdot|smalldot|"
                      r"underscore|cedilla2|cedilla|dot))")
DOT_ABOVE = str.maketrans({"ḣ": "ḥ", "Ḣ": "Ḥ", "ḋ": "ḍ", "Ḋ": "Ḍ", "ṡ": "ṣ", "Ṡ": "Ṣ", "ṫ": "ṭ", "Ṫ": "Ṭ",
                           "ż": "ẓ", "Ż": "Ẓ"})


def clean(t: str, stats: Counter) -> str:
    import unicodedata

    def sub(m):
        stats["glyph names replaced"] += 1
        if m.group(2):
            return chr(int(m.group(2)))
        if m.group(3):
            base, mark = m.group(3), MARKS[m.group(4)]
            if m.group(4).startswith("small"):  # small capitals: the lower-case letter
                base = base.lower()
            return unicodedata.normalize("NFC", base + mark)
        return GLYPH[m.group(1)]
    t = GLYPH_RX.sub(sub, t)
    before = sum(t.count(c) for c in "ḣḢḋḊṡṠṫṪżŻ")
    stats["dot-above letters made dot-below"] += before
    return t.translate(DOT_ABOVE)


def header(t: str) -> tuple[int | None, str]:
    first = t.strip().split("\n")[0].strip() if t.strip() else ""
    m = re.match(r"^(\d{1,3})\s*(\D.*)?$", first) or re.match(r"^(.*?\D)\s*(\d{1,3})$", first)
    if not m:
        return None, first
    if first[:1].isdigit():
        return int(m.group(1)), (m.group(2) or "").strip()
    return int(m.group(2)), m.group(1).strip()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--dump")
    a = ap.parse_args()
    stats: Counter = Counter()
    rows = IC.pages(SID, STEM)
    text = {r["page"]: clean(r["text"], stats) for r in rows}
    vol_of = {p: v for v, lo, hi in VOLUMES for p in range(lo, hi + 1)}
    # printed numbers: a page's own header number is taken when it agrees with a neighbour's (same offset)
    num = {p: header(text[p])[0] for p in text}
    loc, head = {}, {}
    for p in sorted(text):
        n, h = header(text[p])
        head[p] = h[:120]
        v = vol_of.get(p)
        ok = False
        if v and n is not None:
            for q in (p - 1, p + 1, p - 2, p + 2):
                if vol_of.get(q) == v and num.get(q) is not None and num[q] - n == q - p:
                    ok = True
                    break
        loc[p] = f"{SID}:v{v}p{n}" if ok else f"{SID}:pdf{p}"
        stats["pages cited by volume and printed page" if ok else "pages cited by PDF page"] += 1
    dup = [k for k, c in Counter(loc.values()).items() if c > 1]
    for p in loc:
        if loc[p] in dup:
            loc[p] = f"{SID}:pdf{p}"
            stats["printed locator shared by two pages: PDF page used"] += 1
    by_loc = {v: p for p, v in loc.items()}

    def by_offset(vol: int, n: int) -> int | None:
        """A printed page with no readable number of its own (a volume's first page, a page after a plate): the PDF
        page its numbered neighbours point to (both sides agree), else None."""
        lo, hi = next((lo, hi) for v, lo, hi in VOLUMES if v == vol)
        for d in range(1, 4):
            for nb in (n - d, n + d):
                q = by_loc.get(f"{SID}:v{vol}p{nb}")
                if q is not None:
                    cand = q + (n - nb)
                    if lo <= cand <= hi and loc[cand] == f"{SID}:pdf{cand}":
                        stats["index targets found by a neighbour's offset"] += 1
                        return cand
                    return None
        return None

    # the Index of Qurʾān citations: verse -> volume page column (article)
    index_refs: dict[int, set[str]] = defaultdict(set)
    unresolved: list[str] = []
    surah, verse = None, None
    lines = []
    for p in range(CITATIONS[0], CITATIONS[1] + 1):
        lines += [(p, ln) for ln in text[p].split("\n")]
    entries: list[tuple[int, int, int | None, str]] = []  # (surah, a, b, the rest)
    for p, ln in lines:
        st = ln.strip()
        ms = re.search(r"s[ūu]rat\b.*\((\d{1,3})\)", st, re.I)
        if ms:
            surah = int(ms.group(1))
            continue
        me = re.match(r"^(\d{1,3})(?:\s?-\s?(\d{1,3}))?\s+((?:i|ii|iii|iv|v)\s.*)$", st)
        if me and surah:
            entries.append([surah, int(me.group(1)), int(me.group(2)) if me.group(2) else None, me.group(3)])
        elif surah and re.match(r"^(?:i|ii|iii|iv|v)\s+\d", st) and not (entries and entries[-1][0] == surah):
            # citations of the surah as a whole (listed under its heading, before its first verse)
            entries.append([surah, 1, IC.ayah_counts()[surah], st])
            stats["whole-surah citation lines"] += 1
        elif entries and entries[-1][0] == surah and st:
            if re.match(r"^\d{1,3}\s*$", st):  # a page number line
                continue
            entries[-1][3] += " " + st
    n_cites = 0
    for s, x, y, rest in entries:
        if not IC.valid(s, x, y):
            unresolved.append(f"{s}:{x}{'-' + str(y) if y else ''} (not a valid ayah)")
            continue
        ref = f"{s}:{x}" + (f"-{y}" if y and y > x else "")
        parts = re.split(r"(?:^|\s)(i|ii|iii|iv|v)\s+(?=\d)", " " + rest)
        for k in range(1, len(parts) - 1, 2):
            vol = ROMAN[parts[k]]
            # page numbers outside the article names in parentheses
            for pm in re.finditer(r"(?<![\w(])(\d{1,3})[ab]\b", re.sub(r"\([^()]*\)", " ", parts[k + 1])):
                n_cites += 1
                target = by_loc.get(f"{SID}:v{vol}p{int(pm.group(1))}") or by_offset(vol, int(pm.group(1)))
                if target is None:
                    unresolved.append(f"{ref} -> {parts[k]} {pm.group(0)}")
                else:
                    index_refs[target].add(ref)

    segs = []
    for p in sorted(text):
        t = text[p].strip()
        if not t:
            stats["empty pages"] += 1
            continue
        refs = IC.find_refs(t) if not (INDEX_VOL[0] <= p <= INDEX_VOL[1]) else []
        extra = sorted(index_refs.get(p, set()) - set(refs), key=lambda r: tuple(int(x) for x in re.split("[:-]", r)))
        g = {"seg": loc[p], "page": f"pdf{p}", "head": head[p], "text": t, "refs": refs + extra}
        if extra:
            g["refs_from_index"] = extra
        if INDEX_VOL[0] <= p <= INDEX_VOL[1]:
            g["index_volume"] = True
        segs.append(g)
    print(f"pages {len(rows)}; segments {len(segs)}; {dict(stats)}")
    print(f"index of citations: {len(entries)} verse lines, {n_cites} page citations, {sum(len(v) for v in index_refs.values())} "
          f"page refs added; unresolved {len(unresolved)} {unresolved[:10]}")
    if a.dry:
        if a.dump:
            Path(a.dump).write_text("".join(IC.json.dumps(g, ensure_ascii=False) + "\n" for g in segs))
        return
    old = IC.json.loads((IC.src_dir(SID) / "source.json").read_text())
    IC.write(SID, segs, {
        "script": "enrichment/v2/fetch/import_eq.py", "from": IC.inputs(SID, [STEM]),
        "method": "PDF text layer (pypdf via fetch/pdf_pages.py), one segment per page; glyph names replaced; refs "
                  "from the text and from the Index of Qurʾān citations",
        "repairs": dict(stats), "index_citations": n_cites, "index_unresolved": unresolved,
    }, {"coverage": "volumes I–V (articles) and VI (indexes), by page; cited ayat in refs (`corpus.py cites S:A`)",
        "locator": "page",
        "edition": "Brill, Leiden 2001–2006, six volumes (one PDF, 3,956 pages)",
        "licence": "copyrighted; local research copy only (user, 2026-10-05: licence is no barrier for local analysis)",
        "notes": "Ingested 2026-10-05 from the user's download (fetch/import_eq.py). Locators EQ:v<vol>p<page> follow "
                 "the printed volume and page (columns a/b are on the same segment); EQ:pdf<n> where no printed "
                 "number could be read. The index of proper names uses a font whose text layer substitutes letters "
                 "(Ê = ā, { = ʿ …): not normalised. Pointer note before ingestion: " + (old.get("notes") or "")})


if __name__ == "__main__":
    main()
