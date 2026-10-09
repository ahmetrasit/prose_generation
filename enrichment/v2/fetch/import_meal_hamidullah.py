#!/usr/bin/env python3
"""MEAL-HAMIDULLAH: Muhammed Hamidullah, Aziz Kur'an (Turkish by Abdülaziz Hatip and Mahmut Kanık from
Hamidullah's French), from the user's download (raw/acquired-2026-10-05/hamidullah-aziz-kuran-hatip-kanik.pdf,
531 PDF pages; text layer good but OCR'd: «ı» for «1», «S» for «5» in numbers). Run fetch/pdf_pages.py first.

Layout: each surah opens «Sure N» / its name / an introduction (name, order of revelation, number of ayat) / the
basmala; verses are «N. text» (a section mark «§k.» may precede); footnotes are numbered from 1 on every page,
printed after the page's verses («1 text»), their markers standalone numbers in the verse text.

Segments: MEAL-HAMIDULLAH:S:A (the verse, markers as [n], its footnotes in `notes` as «[n] text», like the other
meals), MEAL-HAMIDULLAH:S:intro (the surah's introduction, tied to the whole surah, its footnotes in `notes`).
Checked and recorded: every surah's verse count against the Qurʾān's; notes without a marker (kept on the verse
they follow on the page, flagged); running headers dropped (counted).

  python3 -B enrichment/v2/fetch/import_meal_hamidullah.py [--dry]
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402

SID, STEM = "MEAL-HAMIDULLAH", "hamidullah-aziz-kuran-hatip-kanik"
DIG = str.maketrans({"ı": "1", "l": "1", "I": "1", "i": "1", "O": "0", "o": "0", "S": "5", "s": "5"})
HEADER = re.compile(r"^\s*(?:\d{1,3}\s*/\s*\S.*?\s\d{1,3}|\d{1,3}\s+Aziz Kur.{1,4}n)\s*$")
SURAH = re.compile(r"^\s*[S5].{0,3}re\s*([0-9ıIlOoS]{1,3})\s*$")  # «Sure 4», OCR «SO.re4», «50.re 95»
N3 = r"[0-9ıIlOoS](?:\s?[0-9ıIlOoS]){0,2}"  # OCR may split a number: «7 4.»
VERSE = re.compile(rf"^\s*(?:[§~]\s?\S{{1,3}}\.?\s*)?({N3})(?:\s?[-–]\s?({N3}))?\.\s+(.*)$")
INLINE = re.compile(rf"(?:^\s*|(?<=\s))(?:\S{{1,4}}\.\s+)?({N3})(?:\s?[-–]\s?({N3}))?\.\s+")
NOTE = re.compile(r"^\s*([0-9ıIl]{1,2})\s+([^\s.,;:].*)$")  # «ı . l. Rahman,» is a verse, not note 1


def slash_refs(text: str) -> list[str]:
    """The index's «acı: 4/104, 22/22» and «açık: 2/55, 159,253» (further ayat of the same surah)."""
    out: list[str] = []
    for m in re.finditer(r"(?<![\d/])(\d{1,3})/(\d{1,3})((?:\s?,\s?\d{1,3}(?![\d/]))*)", text):
        s = int(m.group(1))
        for a in [m.group(2)] + re.findall(r"\d{1,3}", m.group(3) or ""):
            if IC.valid(s, int(a)) and f"{s}:{a}" not in out:
                out.append(f"{s}:{int(a)}")
    return out


def num(s: str) -> int | None:
    t = re.sub(r"\s", "", s).translate(DIG)
    return int(t) if t.isdigit() else None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--dump")
    a = ap.parse_args()
    counts = IC.ayah_counts()
    stats: Counter = Counter()
    issues: list[str] = []
    verses: dict[tuple[int, int], dict] = {}   # (s, a) -> {"a_end", "parts": [...], "notes": [...], "page"}
    intros: dict[int, dict] = {}
    surah, verse, unit = 0, 0, None              # unit: the verse or intro dict text goes to
    back = False
    for r in IC.pages(SID, STEM):
        page = r["page"]
        lines = [x for x in r["text"].split("\n") if x.strip()]
        if lines and HEADER.match(lines[0]):
            lines = lines[1:]
            stats["running headers dropped"] += 1
        # the notes block: from the last run of note lines numbered 1, 2, 3 … to the page end
        note_at = None
        for i, x in enumerate(lines):
            m = NOTE.match(x)
            if m and num(m.group(1)) == 1 and not VERSE.match(x) and i > 0:
                note_at = i
        body, notes_raw = (lines[:note_at], lines[note_at:]) if note_at is not None else (lines, [])
        notes: dict[int, list[str]] = {}
        k = 0
        for x in notes_raw:
            m = NOTE.match(x)
            if m and num(m.group(1)) == k + 1:
                k += 1
                notes[k] = [m.group(2).strip()]
            elif k:
                notes[k].append(x.strip())
        page_units: list[tuple[dict, int]] = []  # the units of this page, in order, with their text start
        for x in body:
            if back or (surah == 114 and verse == counts[114] and re.match(r"^\s*Dizin\s*$", x)):
                back = True  # the subject index and the publisher's pages after the last verse
                front.setdefault(page, []).append(x)
                continue
            ms = SURAH.match(x)
            if ms and num(ms.group(1)) == surah + 1:
                surah, verse = surah + 1, 0
                unit = intros.setdefault(surah, {"parts": [x.strip()], "notes": [], "page": page})
                page_units.append((unit, len(unit["parts"])))
                continue
            # verse starts in this line: «N. », «§k. N. » (the section mark often OCR'd: «şıs.», «1ı4.»), at the line
            # start or after a lost line break; only the next verse number (or one after it) is taken
            rest, done = x, False
            while surah:
                hit = None
                for mv in INLINE.finditer(rest):
                    n1 = num(mv.group(1))
                    if not n1 or not (verse < n1 <= verse + 2) or n1 > counts[surah]:
                        continue
                    after = rest[mv.end():mv.end() + 1]
                    if mv.start() == 0 or re.match(r"[A-ZÇĞİÖŞÜÂÎÛ\"'“«(\-]", after):
                        hit = mv
                        break
                if not hit and verse == 0 and surah:  # verse 1 behind a margin mark the OCR read as letters: «,, ı 1. Ta Sın Mim.»
                    m1 = re.search(r"(?<![0-9ıIlOoS])1\.\s+(?=\S)", rest)
                    if m1 and not re.search(r"[A-Za-zÇĞİÖŞÜçğöşü]", re.sub(r"[ıIl]", "", rest[:m1.start()])):
                        hit = m1
                        stats["verse 1 behind a margin mark read as letters"] += 1
                        n1_ = 1
                        class _H:  # a match-like object for the code below
                            def group(self, i, m=m1):
                                return "1" if i == 1 else None
                            def start(self, m=m1):
                                return 0
                            def end(self, m=m1):
                                return m.end()
                        hit = _H()
                if not hit:
                    break
                n1 = num(hit.group(1))
                n2 = num(hit.group(2)) if hit.group(2) else None
                if n1 != verse + 1:
                    issues.append(f"{surah}:{verse + 1} not found (p{page}); its text is in {surah}:{verse}")
                    if (surah, verse) in verses:  # the missing verse's text is in the one before: tie it there
                        verses[(surah, verse)]["a_end"] = n1 - 1
                before = rest[:hit.start()].strip()
                if before and unit is not None:
                    if not page_units or page_units[-1][0] is not unit:
                        page_units.append((unit, len(unit["parts"])))
                    unit["parts"].append(before)
                if hit.start() > 0:
                    stats["verses found inside a line (lost line break)"] += 1
                end = n2 if n2 and n2 >= n1 else n1
                unit = verses[(surah, n1)] = {"a_end": end, "parts": [], "notes": [], "page": page}
                verse = end
                page_units.append((unit, 0))
                rest = rest[hit.end():]
                done = True
            if done:
                if rest.strip():
                    unit["parts"].append(rest.strip())
                continue
            if unit is None:
                stats["lines before the first surah (front matter)"] += 1
                front.setdefault(page, []).append(x)
                continue
            if not page_units or page_units[-1][0] is not unit:
                page_units.append((unit, len(unit["parts"])))
            unit["parts"].append(x.strip())
        # markers: note k is marked by a standalone k in this page's text, in order
        nk = 1
        for u, start in page_units:
            for i in range(start, len(u["parts"])):
                def mark(m):
                    nonlocal nk
                    if num(m.group(1)) == nk and nk in notes:
                        u["notes"].append(f"[{nk}] " + " ".join(notes[nk]))
                        nk += 1
                        return f" [{num(m.group(1))}]"
                    return m.group(0)
                u["parts"][i] = re.sub(r"(?<=\S)\s([0-9ıIl]{1,2})(?=\s|$|[.,;:!?])", mark, u["parts"][i])
        for j in range(nk, len(notes) + 1):  # notes whose marker was not found: on the last unit of the page
            if page_units:
                page_units[-1][0]["notes"].append(f"[{j}?] " + " ".join(notes[j]))
                stats["footnotes whose marker was not found (kept, [n?])"] += 1
            else:
                issues.append(f"p{page}: footnote {j} with no text unit on the page")
        stats["footnotes"] += len(notes)
    segs = []
    for s, x in sorted(intros.items()):
        g = {"seg": f"{SID}:{s}:intro", "s": s, "a": 1, "a_end": counts[s], "page": f"pdf{x['page']}",
             "head": "surah introduction", "text": "\n".join(x["parts"]).strip()}
        if x["notes"]:
            g["notes"] = "\n".join(x["notes"])
        segs.append(g)
    for (s, a0), x in sorted(verses.items()):
        g = {"seg": f"{SID}:{s}:{a0}", "s": s, "a": a0, "a_end": x["a_end"], "page": f"pdf{x['page']}",
             "text": re.sub(r"\s+", " ", re.sub(r"[­]\s*", "", " ".join(x["parts"]))).strip()}
        if x["notes"]:
            g["notes"] = "\n".join(x["notes"])
        segs.append(g)
    for pg, ls in sorted(front.items()):
        text = "\n".join(ls).strip()
        g = {"seg": f"{SID}:p{pg:03d}", "page": f"pdf{pg}", "head": "front matter" if pg < 100 else
             "index (Dizin) and back matter", "text": text}
        refs = slash_refs(text)
        if refs:
            g["refs"] = refs
        segs.append(g)
    got = Counter()
    for (s, a0), x in verses.items():
        got[s] += x["a_end"] - a0 + 1
    short = {s: (got[s], counts[s]) for s in counts if got[s] != counts[s]}
    segs.sort(key=lambda g: (g.get("s") or 999, -1 if g["seg"].endswith("intro") else (g.get("a") or 0), g["seg"]))
    stats["front and back matter pages"] = len(front)
    print(f"surahs {len(intros)}; verse units {len(verses)}; verses covered {sum(got.values())}/6236; surahs not "
          f"matching their count {len(short)} {dict(list(short.items())[:12])}")
    print(f"{dict(stats)}; issues {len(issues)} {issues[:6]}")
    if a.dry:
        if a.dump:
            Path(a.dump).write_text("".join(IC.json.dumps(g, ensure_ascii=False) + "\n" for g in segs))
        return
    old = IC.json.loads((IC.src_dir(SID) / "source.json").read_text())
    IC.write(SID, segs, {
        "script": "enrichment/v2/fetch/import_meal_hamidullah.py", "from": IC.inputs(SID, [STEM]),
        "method": "PDF text layer (pypdf via fetch/pdf_pages.py); verses «N.» in order; page footnotes by marker",
        "verse_count_mismatch": {str(k): v for k, v in short.items()}, "issues": issues, "counts": dict(stats),
    }, {"coverage": f"1-114 ({sum(got.values())}/6236 ayat)", "locator": "ayah", "kind": "meal",
        "edition": "Aziz Kur'an, Beyan Yayınları (Abdülaziz Hatip, Mahmut Kanık), PDF of 531 pages",
        "notes": "Ingested 2026-10-05 from the user's download (fetch/import_meal_hamidullah.py). OCR text: digits "
                 "read as «ı»/«S» were normalised in verse and note numbers only; the verse text is as OCR'd "
                 "(«sapnrır» for «saptırır» occurs: quote with care). Pointer note before ingestion: "
                 + (old.get("notes") or "").split("Pointer note before ingestion: ")[-1]})


front: dict[int, list[str]] = {}

if __name__ == "__main__":
    main()
