#!/usr/bin/env python3
"""MEAL-KARAHANLI-TIEM73 + REF-KARAHANLI-TIEM73-NOTES: the Karakhanid Turkish interlinear Qur'an translation of
manuscript TİEM 73 (Istanbul, Türk ve İslam Eserleri Müzesi, no. 73; copied 734 H / 1333-34 by Muhammad b. al-Ḥājj
Dawlatshāh al-Shīrāzī), folios 1v-235v/2 only (Fātiḥa to Ṭāhā, surahs 1-20), in Abdullah Kök's doctoral thesis
«Karahanlı Türkçesi Satır-Arası Kur'an Tercümesi (TİEM 73 1v-235v/2), Giriş-İnceleme-Metin-Dizin»
(Ankara Üniversitesi, Sosyal Bilimler Enstitüsü, 2004; supervisor F. Sema Barutcu Özönder).

Input: the OCR text of archive.org item karahanli-turkcesi-satir-arasi-kuran-tercumesi-tiem-73-1v-235v2
(uploader empireofhassaan@hotmail.com), fetched by this script into raw/acquired-2026-10-09/.

How the edition prints the text (the «Metin» part, one block per surah, headed «sürâtü'l-bakara»):
  - a transliteration only (no Arabic): lower case, one verse after the other, the full stop closes a stop of the
    Qur'an text; folio and line markers sit inside the text: «(2r/1)» = folio 2r line 1, «(7)» = line 7 of the folio
    (the OCR often reads r/v wrongly: «(31/1)», «(3w1)», «J4r/1J»; kept as printed in the OCR);
  - the verse numbers stand in the margin: the OCR returns them as blocks of number-only lines («41.» «42.» ...,
    sometimes garbled: «294», «SI.», «ed»), before the text of those verses; on some pages a number stays at the
    start of its line («28. oo kaçan kılsalar ...»);
  - the editor's notes follow the text: «002/022-4r/2 kötrüm < ...» = surah 2 verse 22, folio 4r line 2.
Surah 1 counts the basmala as verse 1 (as the project's QURAN source does); the basmala of the other surahs is
kept with the surah heading (segment S:head). The thesis part before the text (introduction) and after it (Türkçe
Dizin, bibliography, summaries) goes to REF-KARAHANLI-TIEM73-NOTES with the editor's notes tied to their verses.

Segmentation (the OCR keeps no verse boundary inside the text): the text between two number blocks is a group of
units (a unit = text up to a line ending with a full stop). When the units of a group equal the verses its numbers
give, each unit is verse S:A; when they do not, the group is stored once as S:A (a..a_end) exactly as printed and
flagged `grouped`. Anchors: inline verse numbers split groups. Everything dropped is counted.

  python3 -B enrichment/v2/fetch/import_meal_karahanli_tiem73.py [--dry]
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402
import turkic_common as T  # noqa: E402

SID, NSID = "MEAL-KARAHANLI-TIEM73", "REF-KARAHANLI-TIEM73-NOTES"
IDENT = "karahanli-turkcesi-satir-arasi-kuran-tercumesi-tiem-73-1v-235v2"
RAW = "karahanli-turkcesi-satir-arasi-kuran-tercumesi-tiem73_djvu.txt"
URL = f"https://archive.org/details/{IDENT}"
HEAD = re.compile(r"^s[üu]r\S{0,2}t[üu]", re.I)
NOTE_START = re.compile(r"^\W{0,3}(?:\d{1,2}\s)?([0-9O]{3})\s?/\s?([0-9O]{3,4})")
NUMLINE = re.compile(r"^[0-9OIlS]{1,3}\s*[.,]?(?:\s*,\s*[0-9OIlS]{1,3}\s*[.,]?)*\s*$")
INLINE = re.compile(r"^(?:\(\w{1,3}\)\s*)?([0-9]{1,3})\s?\.\s+(\S.*)$")
NOTEISH = re.compile(r"\b(?:DLT|KB|ED|Çanga|Krş|Hekimoğlu|Sağol|Bkz|Atalay|Clauson|Kaşgarlı|EUTS|hapax|Ünlü|Mahmud|ETG|Gabain|Arat|TT\.?|OTWF|DTS)\b")
FOLIO = re.compile(r"\(\s*\d{1,3}\s?[rvwyJ1li]\s?[/1]?\s?\d\s*\)")
DIG = str.maketrans({"O": "0", "I": "1", "l": "1", "S": "5"})


def num_values(s: str) -> list[int | None]:
    """«12, 13.» -> [12, 13]; «294» -> [294]; a token that is no number -> [None]."""
    parts = [p for p in re.split(r"[,.\s]+", s.strip("()[] .")) if p]
    out: list[int | None] = []
    for p in parts:
        q = p.translate(DIG)
        out.append(int(q) if q.isdigit() else None)
    return out or [None]


ORACLE_SID = "MEAL-KARAHANLI-TIEM73-UNLU"
_TRANS = str.maketrans({"ı": "i", "İ": "i", "â": "a", "ä": "a", "ö": "o", "ü": "u", "ğ": "g", "ş": "s", "ç": "c", "î": "i",
                        "û": "u", "ñ": "n", "ŋ": "n", "&": "a", "é": "e", "ê": "e", "ô": "o", "ë": "e"})


def norm(x: str) -> str:
    x = re.sub(r"\([^)]*\)|\[[^\]]*\]|<[^>]*>", " ", x.lower().replace("i̇", "i"))   # line / folio markers, editor's brackets
    x = x.translate(_TRANS)
    return re.sub(r"[^a-z]", "", x)


def load_oracle() -> dict[tuple[int, int], str]:
    """Ünlü's verse lines (the same manuscript, verse numbers exact): the oracle of the verse boundaries inside a
    group whose margin numbers were not enough."""
    p = IC.CORPUS / ORACLE_SID / "segments.jsonl"
    out: dict[tuple[int, int], str] = {}
    if not p.exists():
        return out
    for line in p.open(encoding="utf-8"):
        r = IC.json.loads(line)
        if r.get("a") is not None and r["s"] <= 20:
            out[(r["s"], r["a"])] = norm(r["text"])
    return out


def tri(x: str) -> set[str]:
    return {x[i:i + 3] for i in range(len(x) - 2)} if len(x) > 2 else {x}


def bits(x: str) -> int:
    """Character trigrams of a normalised string as a bit set (crc32 mod 8192): union is OR, overlap is AND."""
    import zlib
    v = 0
    if len(x) < 3:
        return 1 << (zlib.crc32(x.encode()) % 8192) if x else 0
    for i in range(len(x) - 2):
        v |= 1 << (zlib.crc32(x[i:i + 3].encode()) % 8192)
    return v


def align_words(words: list[str], verses: list[str | None]) -> tuple[list[int], list[float]] | None:
    """Cut a group's words (in order) into len(verses) runs so that run j resembles the oracle verse j most: dynamic
    programme over word positions, cut points of verse j limited to a window around where its share of the oracle's
    characters puts it; similarity = Dice over character trigrams. Returns the end word index and similarity of each run."""
    N, m = len(words), len(verses)
    if N < m or N > 900 or m > 80:
        return None
    wb = [bits(norm(w)) for w in words]
    vb = [bits(v) if v else None for v in verses]
    vc = [b.bit_count() if b is not None else 0 for b in vb]
    lens = [len(v) if v else 0 for v in verses]
    known_lens = [x for x in lens if x]
    if not known_lens:
        return None
    avg = sum(known_lens) / len(known_lens)
    lens = [x or avg for x in lens]
    tot = sum(lens)
    cum, acc = [], 0.0
    for x in lens:
        acc += x
        cum.append(acc / tot)
    W = max(12, int(0.2 * N))
    window = []
    for j in range(m):
        e = round(N * cum[j])
        window.append((max(j + 1, e - W), min(N - (m - 1 - j), e + W)) if j < m - 1 else (N, N))
    NEG = -1e9
    prev: dict[int, float] = {0: 0.0}
    backs: list[dict[int, int]] = []
    for j in range(m):
        lo, hi = window[j]
        cur: dict[int, float] = {}
        bk: dict[int, int] = {}
        for p, val in prev.items():
            acc = 0
            for i in range(p + 1, hi + 1):
                acc |= wb[i - 1]
                if i < lo:
                    continue
                if vb[j] is None:
                    sc = 0.4
                else:
                    c = acc.bit_count()
                    sc = 2 * (acc & vb[j]).bit_count() / (c + vc[j]) if c else 0.0
                v2 = val + sc
                if v2 > cur.get(i, NEG):
                    cur[i] = v2
                    bk[i] = p
        if not cur:
            return None
        backs.append(bk)
        prev = cur
    if N not in prev:
        return None
    ends, sims = [], []
    i = N
    for j in range(m - 1, -1, -1):
        p = backs[j][i]
        acc = 0
        for t in wb[p:i]:
            acc |= t
        c = acc.bit_count()
        sims.append(0.4 if vb[j] is None else (2 * (acc & vb[j]).bit_count() / (c + vc[j]) if c else 0.0))
        ends.append(i)
        i = p
    return ends[::-1], sims[::-1]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--debug", type=int, help="print the groups of this surah")
    a = ap.parse_args()
    counts = IC.ayah_counts()
    oracle = load_oracle()
    raw = T.ensure_raw(SID, IDENT, "Karahanlı Türkçesi satır-arası", RAW)
    L = T.read_lines(raw)
    stats: Counter = Counter()
    issues: list[str] = []

    # --- the three parts of the thesis
    m0 = next(i for i, l in enumerate(L) if l.strip() == "Metin" and i > 3000)
    heads = [i for i in range(m0, len(L)) if HEAD.match(L[i].strip()) and len(L[i].strip()) < 40]
    idx0 = next(i for i in range(heads[-1], len(L)) if L[i].strip() == "Türkçe Dizin")
    heads = [h for h in heads if h < idx0]
    if len(heads) != 20:
        sys.exit(f"expected 20 surah headings in the text, found {len(heads)}")
    bounds = heads + [idx0]

    segs: list[dict] = []
    nsegs: list[dict] = []
    per_surah: dict[int, list[int]] = {}
    grouped: dict[str, list[str]] = {}
    aligned: dict[str, list[str]] = {}
    mismatches: dict[str, str] = {}
    intro_lines: dict[int, str] = {}

    for k, h in enumerate(heads):
        s = k + 1
        V = counts[s]
        body = L[h + 1:bounds[k + 1]]
        # pass 1: classify lines; notes are whole paragraphs from their code to the next blank line
        items: list[tuple[str, str, int]] = []  # (kind, text, absolute line)
        orphan: list[tuple[int, str]] = []
        in_note = False
        note: list[str] = []
        note_line = 0

        def flush_note() -> None:
            nonlocal note
            if note:
                txt = " ".join(x.strip() for x in note)
                mm = NOTE_START.match(note[0].strip())
                ns, na = int(mm.group(1).translate(DIG)), int(mm.group(2).translate(DIG)[:3])
                ok = IC.valid(ns, na)
                nsegs.append({"kind": "note", "s": ns if ok else s, "a": na if ok else None, "text": txt,
                              "line": note_line, "code_ok": ok, "surah_block": s})
                note = []
        for j, l in enumerate(body):
            st = l.strip()
            if not st:
                flush_note()
                in_note = False
                items.append(("blank", "", h + 1 + j))
                continue
            if in_note:
                note.append(st)
                continue
            if NOTE_START.match(st):
                in_note = True
                note = [st]
                note_line = h + 1 + j
                continue
            if HEAD.match(st) and len(st) < 40:
                stats["repeated surah heading lines dropped"] += 1
                continue
            tk = st.split()
            if len(tk) >= 3 and sum(len(re.sub(r"\W", "", t)) for t in tk) / len(tk) <= 2.2 and not NUMLINE.match(st):
                stats["lines made of 1-2 letter fragments (OCR of ornaments) dropped"] += 1
                continue
            if NOTEISH.search(st):
                orphan.append((h + 1 + j, st))
                continue
            if len(st) <= 14 and NUMLINE.match(st):
                items.append(("num", st, h + 1 + j))
            elif len(st) <= 4 and not re.search(r"[a-zçğıöşü]{3,}", st):
                items.append(("junk", st, h + 1 + j))
            else:
                items.append(("text", st, h + 1 + j))
        flush_note()
        # lines quoting dictionaries (no note code in front): kept as notes of the surah
        o_runs: list[list[tuple[int, str]]] = []
        for ln, st in orphan:
            if o_runs and ln - o_runs[-1][-1][0] <= 2:
                o_runs[-1].append((ln, st))
            else:
                o_runs.append([(ln, st)])
        for r in o_runs:
            nsegs.append({"kind": "orphan", "s": s, "a": None, "text": " ".join(x for _, x in r), "line": r[0][0],
                          "code_ok": False, "surah_block": s})
            stats["note lines without a verse code (dictionary quotations), kept as surah notes"] += len(r)

        # pass 2: runs of num/junk lines -> blocks (a single number alone is a page number unless it fits)
        seq: list[tuple[str, object]] = []  # ("text", line, abs) | ("block", [tokens])
        i = 0
        nonblank = [x for x in items if x[0] != "blank"]
        while i < len(nonblank):
            kind, txt, ab = nonblank[i]
            if kind in ("num", "junk"):
                run = []
                while i < len(nonblank) and nonblank[i][0] in ("num", "junk"):
                    run.append(nonblank[i][1])
                    i += 1
                nums = [r for r in run if NUMLINE.match(r)]
                if not nums:
                    stats["short garbled lines dropped (no number in the run)"] += len(run)
                    continue
                if len(run) == 1:
                    v = num_values(run[0])[0]
                    if v is None or v > V:
                        stats["lone page numbers / stray figures dropped"] += 1
                        continue
                seq.append(("block", run))
                continue
            seq.append(("text", (txt, ab)))
            i += 1

        # pass 3: blocks -> consecutive numbers; groups of text units between blocks
        def block_range(tokens: list[str], prev_hi: int) -> tuple[int, int, int]:
            """The consecutive verse numbers of one block of margin numbers, garbled tokens filled from their
            neighbours: (first, last, number of tokens that had to be filled)."""
            vals: list[int | None] = []
            for t in tokens:
                vals.extend(num_values(t) if NUMLINE.match(t) else [None])
            out: list[int | None] = []
            last = prev_hi
            for v in vals:
                if v is not None and last < v <= V and (v - last) <= (12 if any(x is not None for x in out) else 40):
                    out.append(v)
                    last = v
                else:
                    out.append(None)
            fixed = sum(1 for v in out if v is None)
            known = [(n, v) for n, v in enumerate(out) if v is not None]
            if not known:
                return prev_hi + 1, min(V, prev_hi + len(out)), fixed
            n0, v0 = known[0]
            n1, v1 = known[-1]
            return max(prev_hi + 1, v0 - n0, 1), min(V, v1 + (len(out) - 1 - n1)), fixed

        groups: list[dict] = [{"lo": 1, "hi": None, "units": [], "block": None}]
        cur_units: list[dict] = groups[0]["units"]
        open_lines: list[tuple[str, int]] = []

        def close_unit(forced: bool = False, terminated: bool = True) -> None:
            nonlocal open_lines
            if open_lines:
                text = " ".join(x for x, _ in open_lines)
                inline = None
                mm = INLINE.match(open_lines[0][0])
                if mm and 1 <= int(mm.group(1)) <= V:
                    inline = int(mm.group(1))
                if inline is not None:
                    text = re.sub(r"^((?:\(\w{1,3}\)\s*)?)\d{1,3}\s?\.\s*(?:[—–-]\s*)?", r"\1", text)
                    stats["printed verse numbers at the start of a unit removed from the text (kept in a/a_end)"] += 1
                cur_units.append({"text": text, "inline": inline, "line": open_lines[0][1], "terminated": terminated})
                open_lines = []
        prev_hi = 0
        for kind, payload in seq:
            if kind == "block":
                close_unit(terminated=False)
                lo, hi, fixed = block_range(payload, prev_hi)
                stats["garbled number lines repaired from their neighbours"] += fixed
                if groups[-1]["block"] is None and not groups[-1]["units"] and len(groups) == 1:
                    groups[0]["hi"] = lo - 1
                    groups[0]["empty_head"] = True
                else:
                    groups[-1]["hi"] = lo - 1 if lo - 1 > groups[-1]["lo"] else groups[-1]["hi"] or prev_hi
                groups.append({"lo": lo, "hi": hi, "units": [], "block": payload})
                cur_units = groups[-1]["units"]
                prev_hi = hi
                continue
            txt, ab = payload
            mm = INLINE.match(txt)
            if mm and 1 <= int(mm.group(1)) <= V and open_lines:
                close_unit(forced=True, terminated=False)
                stats["units split at an inline verse number (previous line had no full stop)"] += 1
            open_lines.append((txt, ab))
            if txt.endswith("."):
                close_unit()
        close_unit(terminated=False)
        groups[-1]["hi"] = V
        if prev_hi and prev_hi != V:
            issues.append(f"{s}: last number block ends at {prev_hi}, the surah has {V} verses (tail kept in the last group)")
        # groups[0] has no block: its range starts at 1 and ends where the first block begins
        g0 = groups[0]
        if g0["hi"] is None:
            g0["hi"] = V

        # head: intro line + basmala out of the first group
        head_parts = [L[h].strip()]
        u0 = g0["units"]
        take: list[dict] = []
        while u0 and len(take) < 3 and u0[0]["inline"] is None and re.search(r"âyât|ayât|sürâsi|süröâsi|sürösi", u0[0]["text"]):
            take.append(u0.pop(0))
        if s not in (1, 9) and not any(re.search(r"atı birl|başla", x["text"]) for x in take):
            if u0 and u0[0]["inline"] is None:
                take.append(u0.pop(0))
            else:
                issues.append(f"{s}: no basmala unit recognised at the start of the surah")
        if s == 9 and not take:
            issues.append("9: no heading note found before the first verse (Tevbe has no basmala)")
        head_parts += [x["text"] for x in take]
        intro_lines[s] = " ".join(head_parts)

        # merge groups with a deficit of units (numbers of the margin lost) with the next group, at most twice
        merged: list[dict] = []
        gi = 0
        while gi < len(groups):
            g = {"lo": groups[gi]["lo"], "hi": groups[gi]["hi"], "units": list(groups[gi]["units"])}
            steps = 0
            while len(g["units"]) < g["hi"] - g["lo"] + 1 and gi + 1 < len(groups) and steps < 2:
                gi += 1
                g["hi"] = groups[gi]["hi"]
                g["units"] += groups[gi]["units"]
                steps += 1
            merged.append(g)
            gi += 1

        if a.debug == s:
            for g in groups:
                print("GROUP", g["lo"], g["hi"], len(g["units"]), [(u["inline"], u["text"][:30]) for u in g["units"][:2]], (g["block"] or [])[:3])

        def emit(lo: int, hi: int, units: list[dict], why: str) -> None:
            if hi < lo:
                return
            size = hi - lo + 1
            if not units:
                return
            if len(units) == size:
                for n, u in enumerate(units):
                    segs.append({"seg": f"{SID}:{s}:{lo + n}", "s": s, "a": lo + n, "a_end": lo + n,
                                 "page": f"line{u['line']}", "text": u["text"]})
                    per_surah.setdefault(s, []).append(lo + n)
                stats["verses stored one per verse"] += size
                return
            if oracle and size > 1:
                words = " ".join(u["text"] for u in units).split()
                res = align_words(words, [oracle.get((s, lo + j)) for j in range(size)])
                if res:
                    ends, sims = res
                    known = [x for j, x in enumerate(sims) if oracle.get((s, lo + j))]
                    if known and sum(known) / len(known) >= 0.45 and len(known) >= 0.7 * size:
                        p0 = 0
                        for j, (e, sm) in enumerate(zip(ends, sims)):
                            g = {"seg": f"{SID}:{s}:{lo + j}", "s": s, "a": lo + j, "a_end": lo + j,
                                 "page": f"line{units[0]['line']}", "boundary_inferred": True,
                                 "similarity_to_unlu": round(sm, 2), "text": " ".join(words[p0:e])}
                            if oracle.get((s, lo + j)) and sm < 0.25:
                                g["low_similarity"] = True
                                stats["inferred verses with similarity < 0.25 to the Ünlü verse (flagged low_similarity)"] += 1
                            segs.append(g)
                            per_surah.setdefault(s, []).append(lo + j)
                            p0 = e
                        stats["verses whose boundaries were inferred by alignment with the Ünlü edition"] += size
                        aligned.setdefault(str(s), []).append(f"{lo}-{hi}")
                        return
                stats["groups the alignment could not split (kept as printed)"] += 1
            segs.append({"seg": f"{SID}:{s}:{lo}", "s": s, "a": lo, "a_end": hi, "page": f"line{units[0]['line']}",
                         "grouped": True, "units": len(units),
                         "head": f"group of verses {lo}-{hi}: {len(units)} text units for {size} verses ({why})",
                         "text": " ".join(u["text"] for u in units)})
            per_surah.setdefault(s, []).extend(range(lo, hi + 1))
            grouped.setdefault(str(s), []).append(f"{lo}-{hi} ({len(units)} units)")
            stats["verses stored in a group"] += size

        for g in merged:
            lo, hi, units = g["lo"], g["hi"], g["units"]
            # inline anchors cut the group
            cuts = [(n, u["inline"]) for n, u in enumerate(units)
                    if u["inline"] is not None and lo < u["inline"] <= hi]
            ok_cuts: list[tuple[int, int]] = []
            lastv = lo
            for n, v in cuts:
                if v > lastv and (not ok_cuts or n > ok_cuts[-1][0]):
                    ok_cuts.append((n, v))
                    lastv = v
            if units and units[0]["inline"] is not None and units[0]["inline"] > lo and not ok_cuts:
                pass
            pts = [(0, lo)] + [c for c in ok_cuts if c[0] > 0 or c[1] != lo] + [(len(units), hi + 1)]
            for (n0, v0), (n1, v1) in zip(pts, pts[1:]):
                emit(v0, v1 - 1, units[n0:n1], "inline numbers cut" if len(pts) > 2 else "margin numbers")

        stats["units total (text up to a line ending in a full stop)"] += sum(len(g["units"]) for g in groups) + len(take)
        segs.append({"seg": f"{SID}:{s}:head", "s": s, "a": None, "a_end": None, "page": f"line{h}",
                     "head": "surah heading, the edition's own surah note and the basmala",
                     "text": intro_lines[s]})
        stats["folio/line markers recognised in the text (approx.)"] += sum(len(FOLIO.findall(u["text"]))
                                                                            for g in groups for u in g["units"])

    # --- editor's notes, introduction, index, back matter -> the reference source
    for n, x in enumerate(nsegs, 1):
        a_ = x["a"]
        nsegs[n - 1] = {"seg": f"{NSID}:{x['s']}:{a_ if a_ else 'x'}#n{n}", "s": x["s"], "a": a_, "a_end": a_,
                        "page": f"line{x['line']}", "head": "editor's note" if x["code_ok"] else
                        "editor's note (verse code unreadable in the OCR: tied to its surah only)",
                        "text": x["text"]}
    stats["editor's notes (kept in the reference source)"] = len(nsegs)
    for name, lo_, hi_, label in (("front", 0, m0, "introduction (Giriş) and apparatus"),
                                  ("index", idx0, len(L), "Türkçe Dizin, bibliography, summaries")):
        for n, (f, e, text) in enumerate(T.chunks(L[lo_:hi_], 3500)):
            nsegs.append({"seg": f"{NSID}:{name}:{n:04d}", "page": f"line{lo_ + f}", "head": label, "text": text,
                          "refs": T.code_refs(text)})
    nsegs.append({"seg": f"{NSID}:text-head", "page": f"line{m0}", "head": "text-part heading and sign list",
                  "text": "\n".join(x.strip() for x in L[m0 - 30:m0 + 3] if x.strip())})

    segs.sort(key=lambda g: (g["s"], -1 if g["seg"].endswith(":head") else g["a"], g["seg"]))
    miss = T.missing_in_range(per_surah, 1, 20)
    present = T.covered(per_surah)
    print(f"{SID}: surahs 1-20; verses present {sum(len(set(v)) for v in per_surah.values())}/"
          f"{sum(counts[s] for s in range(1, 21))}; segments {len(segs)}; notes+reference segments {len(nsegs)}")
    print(f"{dict(stats)}")
    print(f"issues {len(issues)}: {issues[:6]}")
    print(f"missing {sum(len(v) for v in miss.values())}: { {k: T.ranges(v) for k, v in miss.items()} }")
    if a.dry:
        return
    total_present = sum(len(set(v)) for v in per_surah.values())
    ing_common = {"script": "enrichment/v2/fetch/import_meal_karahanli_tiem73.py",
                  "from": {str(raw.relative_to(IC.CORPUS / SID)): IC.C.sha256(raw)}}
    T.ensure_source(SID, {
        "id": SID, "title": "Karahanlı Türkçesi satır-arası Kur'an tercümesi (TİEM 73, 1v-235v/2), Kök edition",
        "author": "anonymous (Karakhanid interlinear; copyist Muhammad b. al-Ḥājj Dawlatshāh al-Shīrāzī, 734 H / 1333-34)",
        "translator": "anonymous", "death_ah": None, "kind": "meal", "tradition": "", "language": "tr",
        "turkic_stage": "Karakhanid",
        "edition": "Abdullah Kök, Karahanlı Türkçesi Satır-Arası Kur'an Tercümesi (TİEM 73 1v-235v/2), "
                   "Giriş-İnceleme-Metin-Dizin; doctoral thesis, Ankara Üniversitesi, Sosyal Bilimler Enstitüsü, Türk Dili ve "
                   "Edebiyatı Anabilim Dalı, Eski Türk Dili Bilim Dalı, Ankara 2004 (supervisor Prof. Dr. F. Sema Barutcu Özönder); "
                   "transliteration edition; unpublished thesis scanned by an archive.org user",
        "edition_editor": "Abdullah Kök", "edition_publisher": "Ankara Üniversitesi (doctoral thesis)", "edition_year": 2004,
        "manuscript": "Istanbul, Türk ve İslam Eserleri Müzesi (TİEM) 73, folios 1v-235v/2 of the 452-leaf manuscript",
        "access": "yerel", "locator": "ayah",
        "urls": [URL], "uploader": "empireofhassaan@hotmail.com", "archive_identifier": IDENT,
        "licence": "scholarly edition; archive.org third-party upload; local research use",
        "panel": False, "cross_witnesses": [],
        "notes_parts": {"static": "scholarly edition; archive.org third-party upload; local research use"},
    }, raw)
    T.ensure_source(NSID, {
        "id": NSID, "title": "Kök, TİEM 73 thesis: editor's notes, introduction, Türkçe Dizin",
        "author": "Abdullah Kök", "kind": "reference", "tradition": "academic", "language": "tr", "turkic_stage": "Karakhanid",
        "edition": "same thesis as MEAL-KARAHANLI-TIEM73 (Ankara 2004)", "access": "yerel", "locator": "section",
        "urls": [URL], "uploader": "empireofhassaan@hotmail.com", "archive_identifier": IDENT,
        "licence": "scholarly edition; archive.org third-party upload; local research use",
        "raw_shared": [f"../{SID}/{raw.relative_to(IC.CORPUS / SID)}"], "panel": False, "files": {},
        "coverage": "editor's notes tied to surahs 1-20 verses; introduction and index as sections",
    }, None)
    ing = {**ing_common, "method": "OCR djvu.txt; text between margin-number blocks grouped into units (see script docstring)",
           "covered": present, "missing": miss, "grouped_verse_ranges": grouped, "boundary_inferred_ranges": aligned,
           "verse_count_mismatch": {k: [len(set(per_surah.get(int(k), []))), counts[int(k)]] for k in miss},
           "edition_range": f"surahs 1-20 (folios 1v-235v/2) = {sum(counts[x] for x in range(1, 21))} verses in the project's numbering", "issues": issues,
           "counts": T.tally(stats), "dropped_sample": [], "surah_heads": intro_lines}
    IC.write(SID, segs, ing, {
        "coverage": f"1-20 ({total_present}/{sum(counts[s] for s in range(1, 21))} ayat of the edition's range; "
                    f"114-surah total 6236); surahs 21-114 are not in the edition",
        "notes": "Karakhanid interlinear of TİEM 73, folios 1v-235v/2 = surahs 1-20 only (the edition stops there); all 2,483 "
                 "verses of those surahs are present. OCR of a thesis scan: the margin verse numbers are separated from the text. "
                 f"Verse boundaries: {stats['verses stored one per verse']} verses from the margin numbers (units equal numbers), "
                 f"{stats['verses whose boundaries were inferred by alignment with the Ünlü edition']} verses cut out of a text block by "
                 "aligning it with the verse lines of MEAL-KARAHANLI-TIEM73-UNLU (same manuscript; segments flagged boundary_inferred "
                 "with similarity_to_unlu, 'low_similarity' below 0.25), "
                 f"{stats['verses stored in a group']} verses kept as printed groups a..a_end (flag grouped). "
                 "Folio markers like (2r/1) and line numbers like (7) stay in the text; the OCR often garbles them ((31/1), (3w1)). "
                 "The special letters of the transliteration (â, ä, ö, ü, ı, ŋ) are partly misread. " + T.NOTE})
    IC.write(NSID, nsegs, {**ing_common, "method": "notes = paragraphs starting with SSS/AAA codes; the rest in chunks",
                           "counts": T.tally(stats), "issues": []}, {})


if __name__ == "__main__":
    main()
