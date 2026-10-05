#!/usr/bin/env python3
"""ASAD-NOTES: Muhammad Asad, The Message of the Qur'ān, translation with all its notes, from the user's download
(raw/acquired-2026-10-05/asad-message-of-quran-with-notes.pdf, islamicbulletin.org typesetting, 1,326 PDF pages;
its text layer is clean). Run fetch/pdf_pages.py ASAD-NOTES first.

Layout of a page's text: running header «www.islamicbulletin.org N»; the translation at column 0, each verse group
opened by a line «S:A» and further verses inside it marked «(S:A)»; note markers are numbers right after a word
(«God-conscious2»), numbered from 1 in every surah; the notes are indented («  1 According to …», continuation
lines «    …»). Surahs open with «The First Surah» … «The Hundred-Fourteenth Surah», the name, the period and
Asad's introduction.

Segments (locators):
  ASAD-NOTES:S:intro    the surah's introduction, tied to the whole surah
  ASAD-NOTES:S:A        a verse group's translation as printed (note markers kept as «[n]»), tied A..A_end
  ASAD-NOTES:S:A#nN     note N, tied to the verse whose text carries its marker (`get S:A` returns the group and
                        its notes); `refs` = the ayat the note cites
  ASAD-NOTES:pNNNN      front matter and the appendices, one per PDF page, with `refs`
Checks printed and recorded: per surah, notes found vs markers found, notes without a marker (tied to the verse
group they follow, flagged `marker_found: false`), markers without a note.

  python3 -B enrichment/v2/fetch/import_asad_notes.py [--dry]
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402

SID, STEM = "ASAD-NOTES", "asad-message-of-quran-with-notes"
HEADER = re.compile(r"^\s*www\.islamicbulletin\.org\s+\d+\s*$")
SURAH_HEAD = re.compile(r"^The ([A-Z][a-z]+(?:-[A-Za-z]+)*) Surah\s*$")
APPENDIX = re.compile(r"^Appendix [IVX]+\s*$")
VERSE_LINE = re.compile(r"^(\d{1,3})\s?:\s?(\d{1,3})\s*$")  # «81: 1» too
VERSE_INLINE = re.compile(r"\((\d{1,3}):(\d{1,3})\)")
NOTE_START = re.compile(r"^( {1,4})(\d{1,3}|[Il])\.?\s+(\S.*)$")  # «  I See Appendix II.» is note 1
MARKER = re.compile(r"(?<![\d(])(?<!\d:)(?<!\d :)(\d{1,3})(?![\d:)])")  # «own:2 this» is a marker; «2:3» is not


VERSE_INLINE = re.compile(r"[({](?:(\d{1,3})\s?:\s?)?(\d{1,3})[)}]")  # «(2:22)», «(2 :22)», late surahs «(2)»


def lines() -> tuple[list[tuple[int, str]], Counter]:
    """(pdf page, line) for every line of the book; only running headers and blank lines are dropped (counted)."""
    dropped, out = Counter(), []
    for r in IC.pages(SID, STEM):
        for ln in r["text"].split("\n"):
            if not ln.strip():
                dropped["blank"] += 1
            elif HEADER.match(ln):
                dropped["running header"] += 1
            else:
                out.append((r["page"], ln.rstrip()))
    return out, dropped


def classify(ls: list[tuple[int, str]]) -> list[str]:
    """N (note) for indented lines; a short column-0 line between two note lines is a note line that wrapped
    (late surahs: «  1 The expression … periods» / «of happiness» / «    in human life …»); M otherwise."""
    cls = ["N" if ln.startswith(" ") else "M" for _, ln in ls]
    for i in range(1, len(ls) - 1):
        body = ls[i][1].strip()
        if (cls[i] == "M" and cls[i - 1] == "N" and ls[i + 1][1].startswith(" ") and len(body) < 50
                and ls[i][0] == ls[i - 1][0] and not VERSE_LINE.match(body) and not SURAH_HEAD.match(body)
                and not APPENDIX.match(body)):
            cls[i] = "W"
    return cls


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--dump", help="with --dry: write the segments to this file for inspection")
    a = ap.parse_args()
    counts = IC.ayah_counts()
    ls, dropped = lines()
    cls = classify(ls)

    segs: list[dict] = []
    groups: list[dict] = []      # verse groups: {"s", "a", "a_end", "parts": [...], "page"}
    surah, mode = 0, "front"     # front | intro | verses | appendix
    intro: list[str] = []
    intro_page = None
    verse = 0
    cands: list[dict] = []       # possible note markers in the main text: {"s", "n", "verse", "orig"}
    notes: dict[tuple[int, int], dict] = {}
    note_surah, note_last, note_cur = 0, 0, None
    page_text: dict[int, list[str]] = {}
    issues: list[str] = []
    col0_notes: list[str] = []
    inline_notes: list[str] = []

    def close_intro():
        nonlocal intro
        if surah > 0 and intro:
            text = "\n".join(intro).strip()
            segs.append({"seg": f"{SID}:{surah}:intro", "s": surah, "a": 1, "a_end": counts[surah],
                         "page": f"pdf{intro_page}", "head": f"Asad's introduction to surah {surah}",
                         "text": text, "refs": IC.find_refs(text)})
        intro = []

    def candidates(piece: str) -> str:
        def mark(mm):
            cands.append({"s": surah, "n": int(mm.group(1)), "verse": verse, "orig": mm.group(0)})
            return f"\x00{len(cands) - 1}\x00"
        return MARKER.sub(mark, piece)

    for i, (page, ln) in enumerate(ls):
        body = ln.strip()
        if mode == "appendix" or (mode == "front" and not SURAH_HEAD.match(body)):
            page_text.setdefault(page, []).append(ln)
            continue
        # a note printed from column 0 («22 Lit., …» after the indented notes): its number is the next note's and
        # it follows a note line; it runs on (column 0) until a verse mark, a heading, an indented line or the page end
        m0 = re.match(r"^(\d{1,3})\s+([A-Z\"'(\[].*)$", ln)
        # (or opening the page's notes, «134 Lit., …», when its marker was already met in this surah's text)
        if (cls[i] == "M" and m0 and note_cur is not None and note_surah == surah and int(m0.group(1)) == note_last + 1
                and ((i and cls[i - 1] in "NW" and ls[i - 1][0] == page)
                     or any(c["s"] == surah and c["n"] == note_last + 1 for c in cands[-40:]))):
            note_last = int(m0.group(1))
            note_cur = (note_surah, note_last)
            notes[note_cur] = {"text": [m0.group(2).strip()], "page": page, "column0": True}
            col0_notes.append(f"{surah}:n{note_last} p{page}")
            j = i + 1
            while (j < len(ls) and cls[j] == "M" and ls[j][0] == page and not VERSE_LINE.match(ls[j][1].strip())
                   and not SURAH_HEAD.match(ls[j][1].strip())):
                cls[j] = "W"
                j += 1
            continue
        if cls[i] in "NW":
            m = NOTE_START.match(ln) if cls[i] == "N" else None
            if m:
                n = 1 if m.group(2) in ("I", "l") else int(m.group(2))
                if note_surah != surah and n <= 3:  # the surah's first note (its «1» may be lost)
                    if n != 1:
                        issues.append(f"{surah}: first note found is {n} (p{page})")
                    note_surah, note_last = surah, 0
                opens = re.match(r"[A-Z\"'“(\[]", m.group(3)) is not None  # «    141 below).» continues a note
                if (n == note_last + 1 and (len(m.group(1)) <= 3 or opens)) or (
                        note_last + 1 < n <= note_last + 3 and note_cur is not None and len(m.group(1)) <= 3 and opens):
                    if n != note_last + 1:
                        issues.append(f"{note_surah}: note numbers jump {note_last} -> {n} (p{page})")
                    note_last = n
                    note_cur = (note_surah, n)
                    notes[note_cur] = {"text": [m.group(3).strip()], "page": page}
                    while True:  # the next note on the same line
                        cur_txt = notes[note_cur]["text"][-1]
                        mi = re.search(rf"(?<=[.\"”'\]\)])\s+{note_last + 1}\s+(?=[A-Z\"'(])", cur_txt)
                        if not mi:
                            break
                        notes[note_cur]["text"][-1] = cur_txt[:mi.start()]
                        note_last += 1
                        note_cur = (note_surah, note_last)
                        notes[note_cur] = {"text": [cur_txt[mi.end():]], "page": page}
                        inline_notes.append(f"{note_surah}:n{note_last} p{page}")
                    continue
            if note_cur is not None:
                notes[note_cur]["text"].append(body)
                # «5 Lit., "…". 6 Cf. 5:109.»: the next note printed on the same line
                while True:
                    cur_txt = notes[note_cur]["text"][-1]
                    mi = re.search(rf"(?<=[.\"”'\]\)])\s+{note_last + 1}\s+(?=[A-Z\"'(])", cur_txt)
                    if not mi:
                        break
                    notes[note_cur]["text"][-1] = cur_txt[:mi.start()]
                    note_last += 1
                    note_cur = (note_surah, note_last)
                    notes[note_cur] = {"text": [cur_txt[mi.end():]], "page": page}
                    inline_notes.append(f"{note_surah}:n{note_last} p{page}")
            else:
                issues.append(f"p{page}: note line before any note: {body[:60]!r}")
                page_text.setdefault(page, []).append(ln)
            continue
        if SURAH_HEAD.match(body):
            close_intro()
            surah += 1
            mode, intro_page, verse, intro = "intro", page, 0, [body]
            continue
        if APPENDIX.match(body) and surah == 114:
            mode = "appendix"
            page_text.setdefault(page, []).append(ln)
            continue
        v = VERSE_LINE.match(body)
        if v and int(v.group(1)) == surah and int(v.group(2)) > verse:
            close_intro()
            mode, verse = "verses", int(v.group(2))
            groups.append({"s": surah, "a": verse, "a_end": verse, "parts": [], "page": page})
            continue
        if mode == "intro":
            intro.append(body)
            continue
        g = groups[-1]
        pos = 0
        for vm in VERSE_INLINE.finditer(body):
            s_in, a_in = vm.group(1), int(vm.group(2))
            if (s_in is None or int(s_in) == surah) and verse < a_in <= min(verse + 12, counts[surah]):
                g["parts"].append(candidates(body[pos:vm.start()]))
                verse = a_in
                g["a_end"] = verse
                g["parts"].append(f"({surah}:{verse})")
                pos = vm.end()
        g["parts"].append(candidates(body[pos:]))
    close_intro()

    # markers: in text order per surah, a candidate is note n's marker when n is the next unmatched note number
    # (or up to 3 ahead, a marker the text layer lost) and that note exists
    accepted: dict[int, str] = {}
    markers: dict[tuple[int, int], int] = {}
    last: dict[int, int] = {}
    for k, c in enumerate(cands):
        lo = last.get(c["s"], 0)
        if lo < c["n"] <= lo + 4 and (c["s"], c["n"]) in notes:
            last[c["s"]] = c["n"]
            markers[(c["s"], c["n"])] = c["verse"]
            accepted[k] = f"[{c['n']}]"
    restore = lambda txt: re.sub("\x00(\\d+)\x00", lambda m: accepted.get(int(m.group(1)), cands[int(m.group(1))]["orig"]), txt)  # noqa: E731
    starts: dict[int, list[int]] = {}
    for g in groups:
        segs.append({"seg": f"{SID}:{g['s']}:{g['a']}", "s": g["s"], "a": g["a"], "a_end": g["a_end"],
                     "page": f"pdf{g['page']}", "head": "translation",
                     "text": restore(" ".join(g["parts"])).strip()})
        starts.setdefault(g["s"], []).append(g["a"])
    unmarked = []
    for (s, n), x in sorted(notes.items()):
        text = " ".join(x["text"]).strip()
        v = markers.get((s, n))
        if v is None:
            unmarked.append(f"{s}:n{n}")
        tie = v if v else None
        group_a = max([a0 for a0 in starts.get(s, [1]) if tie is None or a0 <= tie], default=1) if tie else None
        if tie is None:  # no marker in the text layer: tied to the verses between the neighbouring notes' markers
            lo = [markers[(s, k)] for k in range(n - 1, 0, -1) if (s, k) in markers][:1]
            hi = [markers[(s, k)] for k in range(n + 1, n + 60) if (s, k) in markers][:1]
            before = [g for g in groups if g["s"] == s and g["page"] <= x["page"]]
            tie_a = lo[0] if lo else (before[-1]["a"] if before else 1)
            tie_b = max(tie_a, hi[0] if hi else (before[-1]["a_end"] if before else tie_a))
            group_a = max([a0 for a0 in starts.get(s, [1]) if a0 <= tie_a], default=1)
        else:
            tie_a = tie_b = tie
        g = {"seg": f"{SID}:{s}:{group_a}#n{n}", "s": s, "a": tie_a, "a_end": tie_b, "page": f"pdf{x['page']}",
             "head": f"Asad, note {n} on surah {s}" + (f", verse {tie}" if tie else " (marker not in the text "
                                                                                  "layer: tied to the verses between "
                                                                                  "its neighbours' markers)"),
             "text": text, "refs": IC.find_refs(text)}
        if tie is None:
            g["marker_found"] = False
        segs.append(g)
    for p_, lines_ in sorted(page_text.items()):
        text = "\n".join(lines_).strip()
        segs.append({"seg": f"{SID}:p{p_:04d}", "page": f"pdf{p_}",
                     "head": "front matter" if p_ < 100 else "appendix", "text": text, "refs": IC.find_refs(text)})

    def key(g):
        if g.get("s") is None:
            return (999, 0, 0)
        loc = g["seg"].split(":", 2)[2]
        if loc == "intro":
            return (g["s"], -1, 0)
        base, _, n = loc.partition("#n")
        return (g["s"], int(base), int(n or 0))
    segs.sort(key=key)

    marked = Counter()
    for g in groups:
        marked[g["s"]] += g["a_end"] - g["a"] + 1
    short = {s: (marked[s], counts[s]) for s in counts if marked[s] != counts[s]}
    per = Counter(s for s, _ in notes)
    print(f"surahs {surah}; verse groups {len(groups)}; notes {len(notes)}; markers matched {len(markers)}; "
          f"notes without a marker {len(unmarked)} {unmarked[:20]}")
    print(f"surahs whose verse marks do not reach every ayah (marked, total): {short}")
    print(f"pages outside the surahs: {len(page_text)}; dropped lines {dict(dropped)}; issues {len(issues)} "
          f"{issues[:8]}")
    print(f"notes printed from column 0: {len(col0_notes)} {col0_notes[:12]}; notes run into the previous note's "
          f"line: {len(inline_notes)} {inline_notes[:12]}")
    if a.dry:
        if a.dump:
            Path(a.dump).write_text("".join(IC.json.dumps(g, ensure_ascii=False) + "\n" for g in segs))
        return
    old = IC.json.loads((IC.src_dir(SID) / "source.json").read_text())
    IC.write(SID, segs, {
        "script": "enrichment/v2/fetch/import_asad_notes.py", "from": IC.inputs(SID, [STEM]),
        "method": "PDF text layer (pypdf via fetch/pdf_pages.py); verse marks and note markers matched in order",
        "notes_found": len(notes), "markers_matched": len(markers), "notes_without_marker": unmarked,
        "verses_not_marked": {str(k): v for k, v in short.items()},
        "dropped": {**dict(dropped), "what": "running headers and blank lines only"},
        "issues": issues, "notes_from_column_0": col0_notes, "notes_split_from_a_line": inline_notes,
    }, {"coverage": "1-114: translation, introductions and notes; front matter and appendices by PDF page",
        "edition": "islamicbulletin.org PDF typesetting of The Message of the Qur'an (Dar al-Andalus 1980 text), "
                   "1,326 PDF pages, all notes and the appendices",
        "licence": "copyrighted; local research copy only (user, 2026-10-05: licence is no barrier for local analysis)",
        "notes": "Ingested 2026-10-05 from the user's download (fetch/import_asad_notes.py). Note N of surah S is "
                 "S:A#nN under its verse group S:A (`get S:A` returns the group and its notes); the note's tie is "
                 "the verse whose text carries its marker. Translation markers are shown as [n]. Pointer note "
                 "before ingestion: " + (old.get("notes") or "")})


if __name__ == "__main__":
    main()
