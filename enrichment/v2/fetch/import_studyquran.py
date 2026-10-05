#!/usr/bin/env python3
"""STUDYQURAN: S. H. Nasr et al., The Study Quran (HarperOne 2015), from the user's download
(raw/acquired-2026-10-05/study-quran.pdf, 4,664 PDF pages; text layer good). Run fetch/pdf_pages.py on
ACADEMIC/STUDYQURAN first.

The text layer breaks a line wherever the font changes (every transliterated letter «ḥ», every italic word); those
breaks are rejoined (repair(): a break next to a short fragment, a special letter, or a space is not a line end).
Nothing else is changed.

Layout per surah (each starts after an empty separator page, with its number): the introduction; the translation,
whose verse numbers are medallion glyphs of a decorative font (¡ = 1, * = 2, + = 3, J = 4 …); «Commentary»; then one
entry per verse or verse group: «***<glyph> <the verse quoted><N or N–M>» followed by the commentary. Entries are
found by their closing number in order (with a «***» separator between two entries); the glyph of each verse
number is learnt from the entries and used to mark the verses in the translation.

Segments (locators):
  STUDYQURAN:S:intro        the introduction, tied to the whole surah
  STUDYQURAN:S:translation  the surah's translation, verse glyphs shown as «(S:A)», tied to the whole surah;
                            `duplicate: true` (every verse is also quoted at the head of its commentary entry)
  STUDYQURAN:S:A            the commentary entry on A (or A..A_end), the quoted verses first; `refs` = the ayat
                            it cites. Verses with no entry of their own are added to the entry before them
                            (`absorbed` lists them; the book comments on some verses together, and refrains such as
                            55:16… have no entry)
  STUDYQURAN:pNNNN          front matter, essays, maps, indexes: one per PDF page, with `refs`

  python3 -B enrichment/v2/fetch/import_studyquran.py [--dry]
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402

SID, STEM = "STUDYQURAN", "study-quran"
SPECIAL = set("ḥḤʿʾṣṢṭṬẓẒḍḌāĀīĪūŪṯḏġšžčñ’‘“”—–")
# an entry's closing verse number: right after the quote's last character (or alone on a line), then a line end
# or the commentary's first word
TERM = re.compile(r"(?:(?<=[^\d\s:–\-/(])|(?<=\n))(\d{1,3})(?:[–-](\d{1,3}))?(?:[ ]*\n|(?=[A-ZĀ-ſḀ-ỿʿʾ“‘\"(]))")
BACK_START = 3650  # after the commentary on S114: essays, maps, indexes (checked: S114 ends on PDF page 3649)


def repair(t: str) -> str:
    t = t.replace("\t", " ")
    parts = t.split("\n")
    out = parts[0]
    for nxt in parts[1:]:
        prev = out
        if not prev or not nxt:
            out = prev + "\n" + nxt
        elif prev.endswith(" ") or nxt.startswith(" "):
            out = prev + nxt
        elif (prev[-1] in SPECIAL or nxt[0] in SPECIAL or len(nxt.strip()) <= 2
              or len(prev.rsplit("\n", 1)[-1].strip()) <= 2):
            out = prev + nxt
        else:
            out = prev + "\n" + nxt
    return re.sub(r" {2,}", " ", out)


def full_end(a: int, b: str | None) -> int:
    if b is None:
        return a
    n = int(b)
    if n < a:  # «190–94» = 190–194
        n = int(str(a)[:len(str(a)) - len(b)] + b)
    return n


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--dump")
    a = ap.parse_args()
    counts = IC.ayah_counts()
    rows = IC.pages(SID, STEM)
    P = {r["page"]: repair(r["text"]) for r in rows}
    empty = {p for p, t in P.items() if not t.strip()}
    starts: dict[int, int] = {}
    s = 0
    for p in sorted(P):
        if p - 1 in empty and s < 114 and re.match(rf"\s*{s + 1}\s*\D", P[p]):
            s += 1
            starts[s] = p
    if len(starts) != 114 or starts[114] >= BACK_START:
        sys.exit(f"surah starts found: {len(starts)} (expected 114); refusing to guess")
    ends = {k: (starts[k + 1] - 1 if k < 114 else BACK_START - 1) for k in starts}

    segs: list[dict] = []
    issues: list[str] = []
    absorbed_all: dict[str, list[int]] = {}
    glyph_votes: dict[int, Counter] = defaultdict(Counter)
    surah_parts = {}
    dropped = Counter()
    for s in range(1, 115):
        # the surah's text with page offsets (for each entry's first page)
        text, offs = "", []
        for p in range(starts[s], ends[s] + 1):
            offs.append((len(text), p))
            text += P[p] + "\n"
        page_at = lambda i: max(p for o, p in offs if o <= i)  # noqa: E731
        ci = text.find("Commentary")
        if ci < 0:
            sys.exit(f"S{s}: no «Commentary» heading")
        pre, com, base = text[:ci], text[ci:], ci
        # entries
        found, last, lastpos = [], 0, 0
        for m in TERM.finditer(com):
            x = int(m.group(1))
            y = full_end(x, m.group(2))
            if not (last - 1 <= x <= last + 6 and y > last and y <= counts[s]):
                continue
            if found and "***" not in com[lastpos:m.start()]:
                continue
            if x <= last:
                issues.append(f"{s}: entry {x}–{y} overlaps the previous one (printed so); tied {last + 1}–{y}")
                x = last + 1
            found.append((x, y, m.start(), m.end()))
            last, lastpos = y, m.end()
        if not found:
            sys.exit(f"S{s}: no commentary entry found")
        # each entry runs from its quote's start (the «***» before its closing number, or «Commentary») to the
        # next entry's quote start
        bounds = []
        for i, (x, y, ms, me) in enumerate(found):
            qs = com.rfind("***", found[i - 1][3] if i else 0, ms)
            while qs > 0 and com[qs - 1] == "*":  # «****»: the run's first three stars are the separator
                qs -= 1
            if qs < 0:
                qs = len("Commentary") if i == 0 else found[i - 1][3]
            bounds.append([x, y, qs, ms, me])
        entries = []
        for i, (x, y, qs, ms, me) in enumerate(bounds):
            end = bounds[i + 1][2] if i + 1 < len(bounds) else len(com)
            raw = com[qs:end]
            sep = re.match(r"\*{3}", raw)  # «****» = the separator and the glyph of verse 2 («*»)
            body = raw[sep.end():] if sep else raw
            g = re.match(r"\s*(\S{1,2})\s", body)  # the medallion glyph of verse x
            if g:
                glyph_votes[x][g.group(1)] += 1
            dropped["entry separators ***"] += 1 if sep else 0
            entries.append({"x": x, "y": y, "text": body.strip(), "start": base + qs})
        if bounds and bounds[0][2] > len("Commentary") + 5:
            issues.append(f"{s}: text between «Commentary» and the first entry: {com[10:bounds[0][2]][:80]!r}")
        # verses with no entry of their own go to the entry before them
        for i, e in enumerate(entries):
            nxt = entries[i + 1]["x"] if i + 1 < len(entries) else counts[s] + 1
            if nxt > e["y"] + 1:
                gap = list(range(e["y"] + 1, nxt))
                e["absorbed"] = gap
                absorbed_all[str(s)] = absorbed_all.get(str(s), []) + gap
                e["y"] = nxt - 1
        if entries[0]["x"] != 1:
            issues.append(f"{s}: first entry is on verse {entries[0]['x']}; verses before it are tied to it")
            entries[0]["absorbed"] = list(range(1, entries[0]["x"])) + entries[0].get("absorbed", [])
            entries[0]["x"] = 1
        for e in entries:
            g = {"seg": f"{SID}:{s}:{e['x']}", "s": s, "a": e["x"], "a_end": e["y"],
                 "page": f"pdf{page_at(e['start'])}", "head": "the verse quoted, then the commentary",
                 "text": e["text"], "refs": IC.find_refs(e["text"])}
            if e.get("absorbed"):
                g["absorbed"] = e["absorbed"]
            segs.append(g)
        surah_parts[s] = (pre, starts[s])
    # the glyph of each verse number (majority over the entries), then the translations
    glyph = {n: c.most_common(1)[0][0] for n, c in glyph_votes.items()}
    unmarked_tr = {}
    for s, (pre, p0) in surah_parts.items():
        i1 = pre.find(glyph.get(1, "¡"))
        if i1 < 0:
            issues.append(f"{s}: translation start (glyph of verse 1) not found; introduction and translation kept "
                          f"together")
            intro, tr = pre, ""
        else:
            intro, tr = pre[:i1], pre[i1:]
        segs.append({"seg": f"{SID}:{s}:intro", "s": s, "a": 1, "a_end": counts[s], "page": f"pdf{p0}",
                     "head": f"introduction to surah {s}", "text": intro.strip(), "refs": IC.find_refs(intro)})
        if tr:
            # mark the verses: the glyph of the next verse, standing alone, in order
            out, pos, v, missing = [], 0, 1, []
            while v <= counts[s]:
                gch = glyph.get(v)
                m = re.compile(r"(?:(?<=\s)|(?<=^)|(?<=[.,;:!?”’\"]))" + re.escape(gch) + r"(?=\s)").search(tr, pos) \
                    if gch else None
                if not m:
                    missing.append(v)
                    v += 1
                    continue
                out.append(tr[pos:m.start()])
                out.append(f"({s}:{v})")
                pos = m.end()
                v += 1
            out.append(tr[pos:])
            if missing:
                unmarked_tr[str(s)] = missing
            segs.append({"seg": f"{SID}:{s}:translation", "s": s, "a": 1, "a_end": counts[s], "page": f"pdf{p0}",
                         "head": f"translation of surah {s} (verse medallions shown as (S:A))",
                         "text": "".join(out).strip(), "duplicate": True})
    for p in sorted(P):
        if p < starts[1] or p >= BACK_START:
            if not P[p].strip():
                dropped["empty pages"] += 1
                continue
            segs.append({"seg": f"{SID}:p{p:04d}", "page": f"pdf{p}",
                         "head": "front matter" if p < starts[1] else "essays, maps and indexes",
                         "text": P[p].strip(), "refs": IC.find_refs(P[p])})

    def key(g):
        if g.get("s") is None:
            return (999, 0, g["seg"])
        loc = g["seg"].split(":")[2]
        return (g["s"], {"intro": -2, "translation": -1}.get(loc, int(loc) if loc.isdigit() else 0), "")
    segs.sort(key=key)
    n_entries = sum(1 for g in segs if g.get("s") and g["seg"].split(":")[2].isdigit())
    print(f"entries {n_entries}; verses added to the entry before them {sum(len(v) for v in absorbed_all.values())} "
          f"in {len(absorbed_all)} surahs; translation verses whose glyph was not found "
          f"{sum(len(v) for v in unmarked_tr.values())} {dict(list(unmarked_tr.items())[:8])}")
    print(f"pages outside the surahs {sum(1 for g in segs if g.get('s') is None)}; issues {len(issues)} {issues[:6]}")
    print(f"dropped: {dict(dropped)}; glyphs learnt for {len(glyph)} verse numbers")
    if a.dry:
        if a.dump:
            Path(a.dump).write_text("".join(IC.json.dumps(g, ensure_ascii=False) + "\n" for g in segs))
        return
    old = IC.json.loads((IC.src_dir(SID) / "source.json").read_text())
    IC.write(SID, segs, {
        "script": "enrichment/v2/fetch/import_studyquran.py", "from": IC.inputs(SID, [STEM]),
        "method": "PDF text layer (pypdf via fetch/pdf_pages.py), font-change line breaks rejoined; commentary "
                  "entries by their closing verse number in order",
        "verses_without_own_entry": absorbed_all, "translation_verses_unmarked": unmarked_tr,
        "issues": issues, "dropped": {**dict(dropped), "what": "entry separators «***» and empty pages only"},
    }, {"coverage": "1-114: introductions, translation, commentary per verse or verse group; essays and back "
                    "matter by PDF page",
        "locator": "ayah",
        "edition": "HarperOne 2015, PDF of 4,664 pages",
        "licence": "copyrighted; local research copy only (user, 2026-10-05: licence is no barrier for local analysis)",
        "notes": "Ingested 2026-10-05 from the user's download (fetch/import_studyquran.py). S:A is the "
                 "commentary entry (verse quoted first); S:translation repeats the verses (duplicate: true). "
                 "Commentator sigla (Ṭ = al-Ṭabarī, R = al-Rāzī, Bq = al-Biqāʿī …) are explained on the "
                 "front-matter pages (Commentator Key). Pointer note before ingestion: " + (old.get("notes") or "")})


if __name__ == "__main__":
    main()
