#!/usr/bin/env python3
"""MEAL-AKDEMIR: Salih Akdemir, Son Çağrı Kur'an (2nd printing, December 2009), from the user's download
(raw/acquired-2026-10-05/akdemir-son-cagri-kuran.pdf, 660 PDF pages, scanned; its OCR text layer is used: the
archive's .ocr.txt interleaves the two columns line by line, the text layer keeps them apart). Run
fetch/pdf_pages.py MEAL-AKDEMIR first.

Layout: each surah opens «18. KEHF SÛRESİ» / «[Mekke'de inmişti ve 110 ayetten oluşmaktadır.]» / the basmala;
verses or verse groups «105-106. text» (the OCR splits numbers: «1 9 5 .», «lıo.»); footnotes numbered through the
book, printed at a page's foot («5 Muhammed Esed, …»), their marker glued to the word («perdelidir.”5»); a
column of Arabic text whose OCR is garbage; running headers «Bakara Sûresi, Cüz 2. Sûre 2» and page numbers.

Segments: MEAL-AKDEMIR:S:A (verse group A..A_end, markers [n], footnotes in `notes`), MEAL-AKDEMIR:S:intro,
MEAL-AKDEMIR:pNNN (front matter: Akdemir's introduction on translation, and back matter). Dropped and counted:
running headers, page numbers, and lines of the Arabic column (fewer than half their characters Turkish letters;
a sample is kept in the ingestion record).

  python3 -B enrichment/v2/fetch/import_meal_akdemir.py [--dry]
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402

SID, STEM = "MEAL-AKDEMIR", "akdemir-son-cagri-kuran"
DIG = str.maketrans({"ı": "1", "l": "1", "I": "1", "i": "1", "O": "0", "o": "0", "S": "5", "s": "5"})
N3 = r"[0-9ıIlOoS](?:\s?[0-9ıIlOoS]){0,2}"
SURAH = re.compile(rf"^\s*({N3})\s?\.\s*([A-Za-zÇĞİÖŞÜÂÎÛçğıöşüâîû’'\-\s]{{2,40}}?)\s*S\s?[ÛUÜ]\s?R\s?E\s?S\s?[İI]\b")
INLINE = re.compile(rf"(?:^\s*|(?<=\s))({N3})(?:\s?[-–]\s?({N3}))?\s?\.\s+")
HEADER = re.compile(r"(C\s?[ûüu]\s?z\s?\d|S[ûu]\s?re\s?\d|^\s*[0-9IVXLC]{1,6}\s*$|Son Çağr)")
NOTE = re.compile(r"^\s*(\d(?:\s?\d){0,2})\s+([A-ZÇĞİÖŞÜÂ“\"'(\[].*)$")  # «1 0 Biz …»
TR = re.compile(r"[A-Za-zÇĞİÖŞÜçğıöşüÂÎÛâîû]")


def slash_refs(text: str) -> list[str]:
    """«87/2-5: 50/15; 6/51, 70, 94»: surah/ayah (ranges, further ayat of the same surah)."""
    out: list[str] = []
    for m in re.finditer(r"(?<![\d/])(\d{1,3})\s?/\s?(\d{1,3})(?:\s?-\s?(\d{1,3}))?((?:\s?,\s?\d{1,3}(?![\d/]))*)",
                         text):
        s = int(m.group(1))
        items = [(m.group(2), m.group(3))] + [(x, None) for x in re.findall(r"\d{1,3}", m.group(4) or "")]
        for a, b in items:
            b2 = IC._end(a, b) if b else None
            if IC.valid(s, int(a), b2 if b2 and b2 >= int(a) else None):
                r = f"{s}:{int(a)}" + (f"-{b2}" if b2 and b2 > int(a) else "")
                if r not in out:
                    out.append(r)
    return out


def num(s: str) -> int | None:
    t = re.sub(r"\s", "", s).translate(DIG)
    return int(t) if t.isdigit() else None


def garbage(x: str) -> bool:
    """An OCR line of the Arabic column: fewer than half of its characters (digits and the punctuation of references
    such as «87/2-5: 50/15» not counted) are Turkish letters."""
    s = re.sub(r"[\s\d/:;,.\-–()]", "", x)
    return bool(s) and len(TR.findall(s)) / len(s) < 0.5


# Text that the two-column text layer printed inside the wrong verse unit although its verse number was lost or misread
# («8 .» for 99:6); moved by hand to its ayah (2026-10-09 review; every move is listed in the ingestion issues).
# (from unit, pattern of the stretch to cut, destination): destination (s, a, a_end) = a unit of its own,
# ("append", (s, a)) = the end of that unit, None = a running header left in the text.
RELOCATE = [
    ((101, 6), r"\s*Kâria-Tekâsür Sûreleri, Cüz 3Qt Sûre IOI -102", None),
    ((101, 6), r"\s*1 -2 \.\s+(Çok mal edinme hırsı.*?oyalamıştır\.)", (102, 1, 2)),
    ((100, 8), r"\s*8 \.\s+(İnsanlar, o gün.*?çıkacaklardır\.)", (99, 6, 6)),
    ((100, 8), r"\s*7 \.\s+(Her ldm zerre miktarı.*?görecektir\.)", (99, 7, 7)),
    ((99, 1), r"\s*(nankördür!)\s*$", ("append", (100, 1))),
]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--dump")
    a = ap.parse_args()
    counts = IC.ayah_counts()
    stats: Counter = Counter()
    issues: list[str] = []
    dropped_sample: list[str] = []
    verses: dict[tuple[int, int], dict] = {}
    own: dict[int, set] = {k: set() for k in range(0, 116)}  # verse numbers printed (not tied) per surah
    intros: dict[int, dict] = {}
    other: dict[int, list[str]] = {}
    surah, verse, unit = 0, 0, None
    back = False
    notes_started = False
    note_page: dict[int, int] = {}
    page_span: dict[int, tuple[int, int, int]] = {}

    def close_surah(s: int, v: int, page: int) -> None:
        """The surah's last verses were not found: their text is in its last verse unit, tied there."""
        if s and v < counts[s]:
            last = max((k for k in verses if k[0] == s), default=None)
            if last:
                verses[last]["a_end"] = counts[s]
                issues.append(f"{s}:{v + 1}–{counts[s]} not found before the next surah (p{page}); in {s}:{last[1]}")
    note_next, marker_next = 1, 1
    pending_notes: dict[int, str] = {}
    note_units: dict[int, dict] = {}
    for r in IC.pages(SID, STEM):
        page = r["page"]
        lines = [x for x in r["text"].split("\n") if x.strip()]
        kept = []
        for i, x in enumerate(lines):
            if i < 4 and HEADER.search(x) and len(x) < 70:
                stats["running headers and page numbers dropped"] += 1
                continue
            if garbage(x) and not SURAH.match(x):
                stats["Arabic-column lines dropped"] += 1
                stats["Arabic-column characters dropped"] += len(x)
                if len(dropped_sample) < 15:
                    dropped_sample.append(x.strip()[:60])
                continue
            kept.append(x)
        # footnotes at the page foot: a run of lines from «N Text» with N the next note number
        note_at = None
        if not surah and not any(SURAH.match(x) for x in kept):
            other.setdefault(page, []).extend(kept)  # front matter, its own footnotes included, as printed
            continue
        if not notes_started:
            notes_started, note_next, marker_next = True, 1, 1  # the translation's notes are numbered from 1
        for i, x in enumerate(kept):
            m = NOTE.match(x)
            if m and note_next <= num(m.group(1)) <= note_next + 3 and i > 0:
                note_at = i
                break
        body, foot = (kept[:note_at], kept[note_at:]) if note_at is not None else (kept, [])
        cur = None
        for x in foot:
            m = NOTE.match(x)
            if m and note_next <= num(m.group(1)) <= note_next + 3:
                if num(m.group(1)) != note_next:
                    issues.append(f"footnotes {note_next}–{num(m.group(1)) - 1} not found (p{page})")
                cur = num(m.group(1))
                pending_notes[cur] = m.group(2).strip()
                note_page[cur] = page
                note_next = cur + 1
            elif cur:
                pending_notes[cur] += " " + x.strip()
        span_start = (surah, verse + 1) if surah else None
        for x in body:
            ms = SURAH.match(x)
            n_head = num(ms.group(1)) if ms else None
            if not back and re.search(r"İ\s?N\s?D\s?E\s?K\s?S|[İi]ndeks", x) and surah == 114:
                back = True  # the index of topics, concepts and names (references S/A)
            if back:
                other.setdefault(page, []).append(x)
                continue
            if n_head and surah < n_head <= surah + 10:
                close_surah(surah, verse, page)
                if n_head != surah + 1:
                    issues.append(f"surah headings {surah + 1}–{n_head - 1} not found before p{page}")
                surah, verse = n_head, 0
                unit = intros.setdefault(surah, {"parts": [], "notes": [], "page": page})
                unit["parts"].append(x.strip())
                continue
            rest, done = x, False
            if surah and verse == 0 and re.match(r"^\s*[iItTlL1ı][.,]\s+\S", x):
                rest = re.sub(r"^\s*[iItTlL1ı][.,]\s+", "1. ", x)  # «i. Kıyamet…», «l, Hâ, Mim.»: the verse number 1 misread
                stats["verse 1 whose number the OCR misread (taken by position)"] += 1
            while surah:
                hit = None
                for mv in INLINE.finditer(rest):
                    n1 = num(mv.group(1))
                    if not n1:
                        continue
                    restart = n1 == 1 and verse >= counts[surah] - 1 and surah < 114  # heading lost
                    after = rest[mv.end():mv.end() + 1]
                    fits = mv.start() == 0 or re.match(r"[A-ZÇĞİÖŞÜÂÎÛ\"'“«(\[]", after)
                    if not fits:
                        continue
                    if (verse < n1 <= verse + 8 and n1 <= counts[surah]) or restart:
                        hit = (mv, restart, surah)
                        break
                    if n1 <= verse and n1 not in own[surah] and verse - n1 <= 12 and not mv.group(2):
                        hit = (mv, False, surah)  # printed out of order on a two-column page: a verse not seen yet
                        stats["verses printed out of order (kept as their own unit)"] += 1
                        break
                    if (surah > 1 and n1 <= counts[surah - 1] and n1 not in own[surah - 1]
                            and ((verse <= 2 and n1 > verse + 8) or (intros.get(surah, {}).get("page") == page and n1 in own[surah]
                                                                      and counts[surah - 1] - len(own[surah - 1]) >= 3))):
                        hit = (mv, False, surah - 1)  # the foot of the previous surah's page, printed after this heading
                        stats["verses of the previous surah printed after the next heading"] += 1
                        break
                if not hit:
                    break
                mv, restart, tgt = hit
                if tgt != surah or (num(mv.group(1)) <= verse and not restart):
                    n1_ = num(mv.group(1))
                    n2_ = num(mv.group(2)) if mv.group(2) else None
                    before = rest[:mv.start()].strip()
                    if before and unit is not None:
                        unit["parts"].append(before)
                    end_ = n2_ if n2_ and n1_ <= n2_ <= counts[tgt] else n1_
                    unit = verses[(tgt, n1_)] = {"a_end": end_, "parts": [], "notes": [], "page": page}
                    own[tgt].update(range(n1_, end_ + 1))
                    issues.append(f"{tgt}:{n1_}{'-' + str(end_) if end_ > n1_ else ''}: printed out of order on p{page}; kept as its own unit")
                    rest = rest[mv.end():]
                    done = True
                    continue
                if restart:
                    close_surah(surah, verse, page)
                    surah, verse = surah + 1, 0
                    intros.setdefault(surah, {"parts": [], "notes": [], "page": page})
                    issues.append(f"surah {surah}: heading not found; started at its verse 1 (p{page})")
                n1 = num(mv.group(1))
                n2 = num(mv.group(2)) if mv.group(2) else None
                if n1 != verse + 1:
                    issues.append(f"{surah}:{verse + 1}–{n1 - 1} not found (p{page}); in {surah}:{verse}")
                    last = max((k for k in verses if k[0] == surah), default=None)
                    if last and n1 > 1:  # the missing verses' text is in the unit before: tie it there
                        verses[last]["a_end"] = n1 - 1
                before = rest[:mv.start()].strip()
                if before and unit is not None:
                    unit["parts"].append(before)
                end = n2 if n2 and n1 <= n2 <= counts[surah] else n1
                unit = verses[(surah, n1)] = {"a_end": end, "parts": [], "notes": [], "page": page}
                own[surah].update(range(n1, end + 1))
                verse = end
                rest = rest[mv.end():]
                done = True
            if done:
                if rest.strip():
                    unit["parts"].append(rest.strip())
                continue
            if unit is None:
                other.setdefault(page, []).append(x)
            else:
                unit["parts"].append(x.strip())
            # note markers glued to a word («perdelidir.”5»), in order
        if surah and span_start:
            s0, a0 = span_start
            page_span[page] = (s0, a0 if s0 == surah else 1, verse) if s0 == surah else (surah, 1, verse)
        if unit is not None:
            for u in {id(v): v for v in list(verses.values())[-40:] + list(intros.values())[-2:]}.values():
                for i, part in enumerate(u["parts"]):
                    def mark(m):
                        nonlocal marker_next
                        n = int(m.group(1))
                        if marker_next <= n <= marker_next + 3 and n in pending_notes:
                            note_units[n] = u
                            marker_next = n + 1
                            return f" [{n}]"
                        return m.group(0)
                    if any(k in pending_notes for k in range(marker_next, marker_next + 4)):
                        u["parts"][i] = re.sub(r"(?<=[^\s\d\[])(\d{1,3})(?=\s|$)", mark, part)
    close_surah(surah, verse, 0)
    for frm, pat, dest in RELOCATE:
        u_ = verses.get(frm)
        if u_ is None:
            issues.append(f"relocation from {frm[0]}:{frm[1]} skipped: no such unit")
            continue
        txt_ = " ".join(u_["parts"])
        m_ = re.search(pat, txt_, re.S)
        if not m_:
            issues.append(f"relocation from {frm[0]}:{frm[1]} skipped: pattern not found")
            continue
        u_["parts"] = [(txt_[:m_.start()] + " " + txt_[m_.end():]).strip()]
        if dest is None:
            stats["running headers cut out of a verse"] += 1
            continue
        moved_ = m_.group(1)
        if dest[0] == "append":
            tgt_ = verses[dest[1]]
            tgt_["parts"].append(moved_)
            issues.append(f"{frm[0]}:{frm[1]}: «{moved_[:30]}» belongs to the end of {dest[1][0]}:{dest[1][1]}; moved")
        else:
            verses[(dest[0], dest[1])] = {"a_end": dest[2], "parts": [moved_], "notes": [], "page": u_["page"]}
            issues.append(f"{frm[0]}:{frm[1]}: «{moved_[:30]}» is {dest[0]}:{dest[1]}{'-' + str(dest[2]) if dest[2] > dest[1] else ''} "
                          f"(number lost in the text layer); moved")
    # a unit tied over verses whose own unit was found later (printed out of order) gives them back
    for sn_ in range(1, 115):
        keys_ = sorted(k for k in verses if k[0] == sn_)
        starts_ = [k[1] for k in keys_]
        for k in keys_:
            nxt_ = [a_ for a_ in starts_ if a_ > k[1]]
            if nxt_ and verses[k]["a_end"] >= nxt_[0]:
                verses[k]["a_end"] = max(k[1], nxt_[0] - 1)
        cov_ = set()
        for k in keys_:
            cov_.update(range(k[1], verses[k]["a_end"] + 1))
        gap_start = None
        for q_ in range(1, counts[sn_] + 2):
            if q_ <= counts[sn_] and q_ not in cov_:
                gap_start = q_ if gap_start is None else gap_start
            elif gap_start is not None:
                prev_ = [k for k in keys_ if k[1] < gap_start]
                if prev_:  # their text is in the unit before: tied there
                    verses[max(prev_, key=lambda k: k[1])]["a_end"] = q_ - 1
                gap_start = None
    loose = []
    for n, txt in sorted(pending_notes.items()):
        u = note_units.get(n)
        if u is None:  # no marker in the text layer: the note is tied to the verses printed on its page
            sp = page_span.get(note_page[n])
            if not sp:
                issues.append(f"footnote {n}: no verses on its page p{note_page[n]}; kept as a page segment")
                other.setdefault(note_page[n], []).append(f"[{n}] {txt}")
                continue
            s, a0, a1 = sp
            loose.append({"seg": f"{SID}:{s}:{a0}#n{n}", "s": s, "a": a0, "a_end": max(a0, a1),
                          "page": f"pdf{note_page[n]}", "marker_found": False,
                          "head": f"Akdemir, note {n} (marker not in the text layer: tied to the verses on its page)",
                          "text": txt})
            stats["footnotes tied to their page's verses (no marker)"] += 1
            continue
        u["notes"].append(f"[{n}] {txt}")
    segs = list(loose)
    for s, x in sorted(intros.items()):
        g = {"seg": f"{SID}:{s}:intro", "s": s, "a": 1, "a_end": counts[s], "page": f"pdf{x['page']}",
             "head": "surah heading and note", "text": " ".join(x["parts"]).strip()}
        if x["notes"]:
            g["notes"] = "\n".join(x["notes"])
        segs.append(g)
    for (s, a0), x in sorted(verses.items()):
        text = re.sub(r"\s+", " ", re.sub(r"[­]\s*", "", " ".join(x["parts"]))).strip()
        g = {"seg": f"{SID}:{s}:{a0}", "s": s, "a": a0, "a_end": x["a_end"], "page": f"pdf{x['page']}", "text": text}
        if x["notes"]:
            g["notes"] = "\n".join(x["notes"])
        segs.append(g)
    for pg, ls in sorted(other.items()):
        text = "\n".join(ls).strip()
        segs.append({"seg": f"{SID}:p{pg:03d}", "page": f"pdf{pg}",
                     "head": "index of topics, concepts and names" if pg > 600 else "front matter",
                     "text": text, "refs": slash_refs(text) if pg > 600 else IC.find_refs(text)})
    got = Counter()
    for (s, a0), x in verses.items():
        got[s] += x["a_end"] - a0 + 1
    short = {s: (got[s], counts[s]) for s in counts if got[s] != counts[s]}
    stats["footnotes"] = len(pending_notes)
    stats["footnotes placed by their marker"] = len(note_units)
    segs.sort(key=lambda g: (g.get("s") or 999, -1 if g["seg"].endswith("intro") else (g.get("a") or 0),
                             "#" in g["seg"], g["seg"]))
    longest = max((len(g["text"]), g["seg"]) for g in segs if g.get("s"))
    print(f"surahs {len(intros)}; verse units {len(verses)}; verses covered {sum(got.values())}/6236; surahs not "
          f"matching {len(short)} {dict(list(short.items())[:12])}; longest unit {longest}")
    print(f"{dict(stats)}; issues {len(issues)} {issues[:8]}")
    if a.dry:
        if a.dump:
            Path(a.dump).write_text("".join(IC.json.dumps(g, ensure_ascii=False) + "\n" for g in segs))
        return
    old = IC.json.loads((IC.src_dir(SID) / "source.json").read_text())
    IC.write(SID, segs, {
        "script": "enrichment/v2/fetch/import_meal_akdemir.py", "from": IC.inputs(SID, [STEM]),
        "method": "PDF text layer (pypdf via fetch/pdf_pages.py); verse groups in order; footnotes by marker",
        "verse_count_mismatch": {str(k): v for k, v in short.items()}, "issues": issues, "counts": dict(stats),
        "dropped_sample": dropped_sample,
    }, {"coverage": f"1-114 ({sum(got.values())}/6236 ayat)", "locator": "ayah", "kind": "meal",
        "notes": "Ingested 2026-10-05 from the user's download (fetch/import_meal_akdemir.py). OCR text: some "
                 "stretches are letter-spaced («H ani İsra ilo ğ u llan n d a n») and need care when quoted; verse "
                 "groups are Akdemir's own (a..a_end). 2026-10-09 review: the text layer of two-column pages prints verses out of "
                 "order and sometimes under the next surah's heading; such verses are kept as their own units (listed in "
                 "ingestion.issues); a few whose number the layer lost were moved by hand (RELOCATE in the importer). "
                 "Pointer note before ingestion: " + (old.get("notes") or "").split("Pointer note before ingestion: ")[-1]})


if __name__ == "__main__":
    main()
