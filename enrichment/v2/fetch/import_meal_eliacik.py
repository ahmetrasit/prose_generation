#!/usr/bin/env python3
"""MEAL-ELIACIK: R. İhsan Eliaçık, Yaşayan Kur'an, Türkçe Meal/Tefsir (İnşa Yayınları, mushaf-ordered 3 volumes,
1st printing 2007), from the archive.org OCR text of the three volumes (raw/acquired-2026-10-09/
eliacik-yasayan-kuran-{1,2,3}.djvu.txt). The fourth file, eliacik-yasayan-kuran-nuzul-metin.djvu.txt (the later
revelation-ordered one-volume edition, 5th printing 2014), is kept as raw: its OCR has lost the Turkish diacritics and
its meal is rearranged in unnumbered sense groups, so it is not parsed; it is only used to fill gaps by eye.

Layout (checked on 1, 2, 87, 96, 103, 114): a surah opens with «NN- NAME SURESİ» and its introduction («Mekke'de
inmiştir, N ayettir. …»), then a meal page: «NN-NAME SURESİ» / «Mekke'de nazil olmuştur, N ayettir.» / the basmala
(«SEVGİ VE MERHAMETİ SONSUZ ALLAH'IN ADIYLA»; only in Fâtiha it is printed as verse 1) / verses «N- text» one per
paragraph; the Arabic text sits in a column whose OCR is Latin-letter garbage; below the verses the page's footnotes
(«N TERM: …», «N Yani: …», numbered from 1 in each surah, continued across the following commentary pages), and the
next meal page follows after those pages. Running headers «Cüz:N NN- NAME SURESİ Sayfa:M».

Segments: MEAL-ELIACIK:S:A (the verse; footnotes whose marker is found in the text are in `notes`, marker «[n]»
inserted), MEAL-ELIACIK:S:intro (surah introduction), MEAL-ELIACIK:S:notes (footnotes whose marker was not found,
tied to the whole surah, flagged), MEAL-ELIACIK:front (title page and front matter). The footnotes are Eliaçık's
commentary (tefsir): all of them are kept. Dropped and counted: running headers, repeated surah headings, the
basmala lines, Arabic-column garbage lines (a sample is kept in the ingestion record).

  python3 -I enrichment/v2/fetch/import_meal_eliacik.py [--dry] [--dump FILE] [--srcdir DIR]
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402

SID = "MEAL-ELIACIK"
STEMS = ["eliacik-yasayan-kuran-1", "eliacik-yasayan-kuran-2", "eliacik-yasayan-kuran-3"]
OCRDIG = str.maketrans({"l": "1", "I": "1", "i": "1", "ı": "1", "O": "0", "o": "0", "S": "5", "s": "5", "B": "8"})
N = r"[0-9lIiıOoSB]{1,3}"
CAP = r"[A-ZÇĞİÖŞÜÂ\"“'(\[]"
NAME = r"[A-ZÇĞİÖŞÜÂÎÛ'’\-\. ]{2,30}"
RUNHEAD = re.compile(rf"(C.z\s?:\s?\S+.*SURES[İI]|SURES[İI].*Sayfa\s?:\s?\d|Sayfa\s?:\s?\d+\s+{N}\s?-)")
HEADING = re.compile(rf"^\s*({N})\s?-\s?({NAME})\s?SURES[İI]\.?\s*$")
G = rf"{N}(?:\s?[/–—-]\s?{N}){{0,2}}"  # «5», «1/2», «14-15», «33-34-35»
VERSE = re.compile(rf"^[\W_]{{0,3}}({G})(?:\s?[-–—]\s*|\.\s+(?={CAP}))(.*)$")
NOTE_DIG = re.compile(r"^\s*([0-9lIO]{1,4})\s+(\S.*)$")
INLINE = re.compile(rf"(?:(?<=\s)|(?<=[.!?…;:”\"’)\]\w]))(?<!\d)({G})(?:\s?-\s*|\.\s+)(?={CAP}|$)")
NOTE_SYM = re.compile(r"^\s*(\S{1,2})\s+((?:Yani|[A-ZÇĞİÖŞÜÂ'’][A-ZÇĞİÖŞÜÂa-zçğıöşü'’\-/ ]{1,35}):.*)$")
BASMALA = re.compile(r"^\s*(SEVG[İI]\s+(VE\s+)?MERHAMET[İI]\w*|SONSUZ\s+ALLAH.{0,3}IN\s+ADIYLA|SEVG[İI]\s+VE\s+MERHAMET[İI]\s+SONSUZ.*)\s*$")
CLAIM = re.compile(r"(?:Mekke|Medine)'de\s+\w+.*?(\d{1,3})\s+ayet", re.I)
LET = re.compile(r"[A-Za-zÇĞİÖŞÜçğıöşüÂÎÛâîû]")


META = {
    "id": SID, "title": "Yaşayan Kur'an: Türkçe Meal/Tefsir", "author": "R. İhsan Eliaçık", "translator": "R. İhsan Eliaçık",
    "kind": "meal", "tradition": "", "language": "tr", "access": "hafiza", "locator": "ayah", "panel": False,
    "edition": "İnşa Yayınları, İstanbul; 3 volumes in mushaf order, 1st printing April 2007 (as stated on the title "
               "page of volume 1: «İnşa Yayınları:9 … © İnşa Yayınları, Nisan 2007»); the revelation-ordered "
               "one-volume edition (İnşa Yayınları:10, 5th printing September 2014) is held as raw only",
    "coverage": "", "licence": "In copyright (İnşa Yayınları); archive.org upload by a third party; local research use only.",
    "urls": [
        "https://archive.org/details/ihsan-eliacik-yasayan-kuran-1-turkce-meal-tefsir",
        "https://archive.org/details/YasayanKuranIhsanEliacikMetin",
    ],
    "provenance": {
        "archive_org_items": {
            "ihsan-eliacik-yasayan-kuran-1-turkce-meal-tefsir": "uploader vejowi@musiccode.me; 3 volumes, djvu.txt used",
            "YasayanKuranIhsanEliacikMetin": "uploader lazkopatgenc@hotmail.com; revelation-ordered edition, djvu.txt held as raw",
        },
    },
    "notes": "archive.org upload by a third party; in copyright; local research use.",
}


def ensure_source(d: Path) -> None:
    if (d / "source.json").exists():
        return
    d.mkdir(parents=True, exist_ok=True)
    IC.C  # noqa: B018
    (d / "source.json").write_text(IC.json.dumps(META, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def grp(s: str) -> tuple[int, int, bool] | None:
    """«1/2», «14-15», «33-34-35», «5» -> (first, last, slash form)."""
    ns = [num(x) for x in re.split(r"[/–—-]", s)]
    if None in ns or not ns:
        return None
    return ns[0], ns[-1], "/" in s


def num(s: str) -> int | None:
    t = re.sub(r"\s", "", s).translate(OCRDIG)
    return int(t) if t.isdigit() else None


def garbage(x: str) -> bool:
    """An OCR line of the Arabic column or of a drawn frame: few letters, or only very short tokens."""
    s = x.strip()
    if not s:
        return False
    toks = s.split()
    letters = len(LET.findall(s))
    if letters / max(1, len(s.replace(" ", ""))) < 0.5:
        return True
    return len(toks) >= 2 and sum(len(t) for t in toks) / len(toks) < 2.8


VOCAB_FROM = ["DIB", "BULAC", "ATAY", "CAKIR", "HAYRAT", "ESED", "ELMALILI", "DEMIRYENT", "BAYRAKLI", "ALIMIHR"]
_VOC: Counter | None = None
WORD = re.compile(r"[A-Za-zÇĞİÖŞÜçğıöşüÂÎÛâîû]+")


def tr_lower(w: str) -> str:
    return w.replace("İ", "i").replace("I", "ı").lower().translate(str.maketrans("âîû", "aiu"))


def vocab() -> Counter:
    """Words of other, cleanly digitised Turkish meals (their segments): what a word of this OCR text should look like."""
    global _VOC
    if _VOC is None:
        _VOC = Counter()
        for m in VOCAB_FROM:
            p = IC.src_dir(f"MEAL-{m}") / "segments.jsonl"
            if p.exists():
                for line in p.open(encoding="utf-8"):
                    for w in WORD.findall(IC.json.loads(line).get("text") or ""):
                        _VOC[tr_lower(w)] += 1
    return _VOC


def noisy(tok: str) -> bool:
    """A token of the Arabic column's OCR: no letters, or a short / odd-cased string that is no word of the vocabulary."""
    if re.fullmatch(r"\[\d+\]", tok):
        return False
    if len(tok) >= 3 and tok.endswith("-") and tok[-2].isalpha():
        return False  # a word broken at the line end
    left = tok.split("'")[0].split("’")[0]
    core = "".join(WORD.findall(left))
    if not core:
        return True
    f = vocab().get(tr_lower(core), 0)
    if len(core) == 1:
        return core.lower() != "o"
    if len(core) <= 3:
        return f < 150  # short strings are everywhere in the noise: only the frequent small words of Turkish pass
    if f:
        return False
    if left != tok and len(core) >= 3 and core[0].isupper():
        return False  # a proper name with a suffix: «Bend'den»
    if len(core) >= 2 and core.isupper():
        return True  # capitals that are no word
    return len(core) <= 4 or bool(re.search(r"[a-zçğıöşü][A-ZÇĞİÖŞÜ]", core))


def clean(text: str) -> tuple[str, list[str]]:
    """Removes the OCR noise of the Arabic column from a verse: a run of noisy tokens at its end (any length), or
    three or more inside it. The removed runs are returned (kept in the segment, never silently lost)."""
    toks = text.split()
    if len(toks) <= 3:  # a very short verse («Ta Ha.», «Ya Sin.»): nothing to separate from the Arabic column
        return " ".join(toks), []
    flags = [noisy(x) for x in toks]
    removed: list[str] = []
    end = len(toks)
    while end > 0 and flags[end - 1]:
        end -= 1
    if end < len(toks) and end > 0:
        removed.append(" ".join(toks[end:]))
        toks, flags = toks[:end], flags[:end]
    out, i = [], 0
    while i < len(toks):
        if flags[i]:
            j = i
            while j < len(toks) and flags[j]:
                j += 1
            if j - i >= 3:
                removed.append(" ".join(toks[i:j]))
            else:
                out.extend(toks[i:j])
            i = j
        else:
            out.append(toks[i])
            i += 1
    return " ".join(out), removed


def join(parts: list[str]) -> str:
    out = ""
    for p in parts:
        p = p.strip()
        if not p:
            continue
        if out.endswith("-") and out[-2:-1].isalpha() and p[:1].islower():
            out = out[:-1] + p  # hyphenated at the line end
        else:
            out = (out + " " + p) if out else p
    return re.sub(r"\s+", " ", out).strip()


def surah_of(verses: dict, unit: dict) -> int:
    return next(k[0] for k, v in verses.items() if v is unit)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--dump")
    a = ap.parse_args()
    counts = IC.ayah_counts()
    d = IC.src_dir(SID)
    ensure_source(d)
    stats: Counter = Counter()
    issues: list[str] = []
    sample: dict[str, list[str]] = {}
    verses: dict[tuple[int, int], dict] = {}
    intros: dict[int, list[str]] = {}
    notes: dict[int, dict[int, list[str]]] = {}
    front: list[str] = []
    claims: dict[int, int] = {}
    surah, verse, note_next = 0, 0, 1
    mode, cur = "front", None  # cur: list collecting the current item's lines
    mode_vol = ""

    run = {"first": 0, "notes": False}  # the verses of the current meal page; its footnotes follow them
    note_run: dict[tuple[int, int], tuple[int, int]] = {}

    def start(s: int, f: int, l: int, vol: str) -> list[str]:
        if run["notes"] or not run["first"]:
            run["first"], run["notes"] = f, False
        key = (s, f)
        while key in verses:  # the same first verse again (overlapping groups): next free key
            key = (s, f, key[2] + 1 if len(key) > 2 else 2)
        parts: list[str] = []
        verses[key] = {"parts": parts, "page": vol, "a": f, "a_end": l}
        return parts

    def tie_gap(s: int, f: int, l: int, where: str) -> None:
        """Verses f..l have no number in the OCR text: their text is in the unit before; tied there (flagged)."""
        last = max((k for k in verses if k[0] == s), key=lambda k: verses[k]["a_end"], default=None)
        if last is None:
            issues.append(f"{s}:{f}–{l}: no number found {where}; no unit before")
            return
        verses[last].setdefault("orig_end", verses[last]["a_end"])
        verses[last]["a_end"] = max(verses[last]["a_end"], l)
        verses[last].setdefault("absorbed", []).append(f"{s}:{f}" + (f"-{l}" if l > f else ""))
        issues.append(f"{s}:{f}–{l}: verse number(s) lost in the OCR {where}; their text is in the unit {s}:{verses[last]['a']}, tied there")

    def feed(rest: str) -> None:
        """Text of the current item; a verse number printed inside the line starts the next verse."""
        nonlocal cur, verse
        while mode == "verse" and surah:
            hit = None
            for mi in INLINE.finditer(rest):
                gi = grp(mi.group(1))
                if gi and gi[0] == verse + 1 and gi[0] <= gi[1] <= min(counts[surah], gi[0] + 3):
                    hit = mi
                    break
            if not hit:
                break
            cur.append(rest[:hit.start()])
            gi = grp(hit.group(1))
            cur = start(surah, gi[0], gi[1], mode_vol)
            verse = gi[1]
            stats["verses started inside a line"] += 1
            rest = rest[hit.end():]
        cur.append(rest)

    def drop(cat: str, x: str) -> None:
        stats[f"dropped: {cat}"] += 1
        s = sample.setdefault(cat, [])
        if len(s) < 8:
            s.append(x.strip()[:70])

    for stem in STEMS:
        path = d / "raw" / "acquired-2026-10-09" / f"{stem}.djvu.txt"
        if not path.exists():
            sys.exit(f"{path} missing")
        mode_vol = stem
        for raw in path.read_text(encoding="utf-8").split("\n"):
            x = raw.rstrip()
            if not x.strip():
                continue
            if RUNHEAD.search(x) and len(x) < 70:
                m = re.search(rf"({N})\s?-\s?{NAME}\s?SURES", x)
                n = num(m.group(1)) if m else None
                if n and n == surah + 1 and surah:
                    issues.append(f"surah {n}: opened by a running header (no heading found) in {mode_vol}")
                    surah, verse, note_next, mode = n, 0, 1, "intro"
                    intros[surah] = []
                    run["first"], run["notes"] = 0, False
                    cur = intros[surah]
                drop("running headers", x)
                continue
            mh = HEADING.match(x)
            if mh and len(x) < 50:
                n = num(mh.group(1))
                if n == surah + 1:
                    surah, verse, note_next, mode = n, 0, 1, "intro"
                    intros[surah] = [x.strip()]
                    run["first"], run["notes"] = 0, False
                    cur = intros[surah]
                    stats["surah headings"] += 1
                    continue
                if n == surah or (surah and n and abs(n - surah) <= 1):
                    drop("repeated surah headings (meal page head)", x)
                    continue
            if re.fullmatch(r"[—\-–\s\d]{3,}", x) and mode_vol:
                drop("volume page numbers", x)
                continue
            if surah == 0:
                front.append(x.strip())
                continue
            mc = CLAIM.search(x)
            if mc and len(x) < 60 and verse == 0:
                claims[surah] = int(mc.group(1))
            if verse == 0 and BASMALA.match(x) and surah != 1:
                drop("basmala lines", x)
                continue
            mv = VERSE.match(x)
            g = grp(mv.group(1)) if mv and surah else None
            if g and g[1] >= g[0] and g[1] <= counts[surah] and (g[1] - g[0] <= 3 or (g[2] and g[1] - g[0] <= 30)) and (g[1] - g[0] == 1 or g[0] == g[1] or not g[2] or True):
                f, l, slash = g
                if (verse - 3 <= f < verse and l == f and not slash and not any(
                        k[0] == surah and verses[k]["a"] <= f <= verses[k]["a_end"] for k in verses)):
                    issues.append(f"{surah}:{f}: printed after {surah}:{verse} (OCR page order); kept as its own verse")
                    cur = start(surah, f, l, mode_vol)
                    mode = "verse"
                    if mv.group(2).strip():
                        feed(mv.group(2))
                    continue
                ok = f == verse + 1 or (slash and f == verse and l == f + 1) or (f == 1 and surah == 1 and verse == 0)
                if not ok and verse > 0 and verse + 1 < f <= min(verse + 3, counts[surah]):
                    tie_gap(surah, verse + 1, f - 1, f"before {surah}:{f}")
                    ok = True
                if (not ok and verse > 0 and (mode == "verse" or f - verse <= 8) and re.match(r"^\W{0,3}[0-9lIiıOoSB ]{1,4}\s?[-–—]", x) and f == l and not slash and verse + 3 < f <= counts[surah]
                        and mv.group(2).strip()[:1].isupper() or (not ok and verse > 0 and (mode == "verse" or f - verse <= 8) and re.match(r"^\W{0,3}[0-9lIiıOoSB ]{1,4}\s?[-–—]", x) and f == l and not slash
                        and verse + 3 < f <= counts[surah] and mv.group(2).strip()[:1] in "“\"'(")):
                    # a long jump: the verses between were printed in a column the OCR read across (their text
                    # sits inside the units before); resynchronise on this number, flagged
                    tie_gap(surah, verse + 1, f - 1, f"before {surah}:{f} (long jump, resynchronised)")
                    stats["long jumps resynchronised"] += 1
                    ok = True
                if ok:
                    cur = start(surah, f, l, mode_vol)
                    verse = l
                    mode = "verse"
                    if mv.group(2).strip():
                        feed(mv.group(2))
                    continue
            if surah and verse > 0 and verse + 1 == counts[surah] and mode == "verse" and re.match(r"^\s*[-–—]\s+[A-ZÇĞİÖŞÜ“]", x) and not garbage(x) and len(x.split()) >= 4:
                # the last verse printed with its number lost and only the dash left by the OCR
                verse += 1
                cur = start(surah, verse, verse, mode_vol)
                cur.append(re.sub(r"^\s*[-–—]\s+", "", x))
                stats["last verse with the number lost (dash only), numbered by position"] += 1
                issues.append(f"{surah}:{verse}: number lost in the OCR (dash only); taken as the last verse by position")
                continue
            if surah == 1 and verse == 0 and re.match(r"^\s*[1lI]\s+SEVG", x):
                verse = 1
                cur = start(1, 1, 1, mode_vol)
                cur.append(re.sub(r"^\s*[1lI]\s+", "", x))
                mode = "verse"
                continue
            mn = NOTE_DIG.match(x)
            nn = None
            if mn and verse > 0:
                d_ = mn.group(1)
                n = num(d_)
                if n is not None and not x.lstrip()[len(d_):].lstrip().startswith("-"):
                    if note_next <= n <= note_next + 2 and (d_.isdigit() or n == note_next):
                        nn, body = n, mn.group(2)
                    elif len(d_) > 1 and d_[0] in "1l" and num(d_[1:]) == note_next:
                        nn, body = note_next, mn.group(2)
                        stats["footnote numbers garbled by the OCR (taken in sequence)"] += 1
            if nn is None and verse > 0:
                ms = NOTE_SYM.match(x)
                if ms and re.fullmatch(r"[^A-Za-zÇĞİÖŞÜçğıöşü]{1,2}|[lItTiJ]", ms.group(1)) and not VERSE.match(x) and not garbage(x):
                    nn, body = note_next, ms.group(2)
                    stats["footnote numbers garbled by the OCR (taken in sequence)"] += 1
            if nn is not None:
                if nn != note_next:
                    issues.append(f"{surah}: footnotes {note_next}–{nn - 1} not found before footnote {nn}")
                note_next = nn + 1
                cur = notes.setdefault(surah, {}).setdefault(nn, [])
                note_run[(surah, nn)] = (min(run["first"] or verse, verse), verse)
                run["notes"] = True
                cur.append(body)
                mode = "note"
                continue
            if garbage(x) and mode in ("verse", "intro"):
                drop("Arabic-column / frame garbage lines", x)
                continue
            if cur is None:
                front.append(x.strip())
                continue
            feed(x.strip())

    # footnote markers in the verse text, in order: a number glued to the end of a word
    segs: list[dict] = []
    placed: Counter = Counter()
    order = sorted(verses, key=lambda k: (k[0], verses[k]["a"], len(k)))
    for s in sorted(notes):
        nxt = 1
        for key in [k for k in order if k[0] == s]:
            u = verses[key]
            for i, part in enumerate(u["parts"]):
                def mark(m, u=u):
                    nonlocal nxt
                    n = int(m.group(1))
                    if n == nxt and n in notes[s]:
                        u.setdefault("notes", []).append(n)
                        nxt += 1
                        placed[s] += 1
                        return f"{m.group(0)[:m.start(1) - m.start(0)]} [{n}]"
                    return m.group(0)
                u["parts"][i] = re.sub(r"(?<=[^\s\d\[\]])(\d{1,3})(?=[\s.,;:!?”\"')]|$)", mark, part)
    for s, ls in sorted(intros.items()):
        segs.append({"seg": f"{SID}:{s}:intro", "s": s, "a": 1, "a_end": counts[s],
                     "head": "surah heading and introduction", "text": join(ls)})
        if s in claims and claims[s] != counts[s]:
            issues.append(f"{s}: the book says {claims[s]} ayat, the Quran source has {counts[s]}")
    for key in order:
        u = verses[key]
        suffix = "" if len(key) == 2 else chr(ord("a") + key[2] - 1)  # a second group with the same first verse
        txt, removed = clean(join(u["parts"]))
        g = {"seg": f"{SID}:{key[0]}:{u['a']}{suffix}", "s": key[0], "a": u["a"], "a_end": u["a_end"], "text": txt}
        if removed:
            g["ocr_noise_removed"] = removed
            stats["verse segments with OCR noise removed (kept in ocr_noise_removed)"] += 1
        if u.get("absorbed"):
            g["verses_without_own_number"] = u["absorbed"]
        if u["a_end"] > u["a"] and not u.get("absorbed"):
            g["group"] = f"{u['a']}-{u['a_end']} (printed as one paragraph)"
        if u.get("notes"):
            g["notes"] = "\n".join(f"[{k}] {join(notes[key[0]][k])}" for k in u["notes"])
        segs.append(g)
    for s in sorted(notes):
        used = {k for key in order if key[0] == s for k in (verses[key].get("notes") or [])}
        for k in sorted(notes[s]):
            if k in used:
                continue
            f, l = note_run[(s, k)]
            f = max(1, f)
            stats["footnotes tied to the verses of their page (no marker in the text)"] += 1
            segs.append({"seg": f"{SID}:{s}:{f}#n{k}", "s": s, "a": f, "a_end": max(f, l), "marker_found": False,
                         "head": f"Eliaçık, footnote {k} (marker not in the text layer: tied to the verses of its page)",
                         "text": join(notes[s][k])})
    stats["footnotes"] = sum(len(v) for v in notes.values())
    stats["footnotes placed by their marker"] = sum(placed.values())
    segs.append({"seg": f"{SID}:front", "head": "title page and front matter", "text": "\n".join(front)})
    owned = {(k[0], n) for k in verses for n in range(verses[k]["a"], verses[k].get("orig_end", verses[k]["a_end"]) + 1)}
    for k, u in verses.items():  # a verse printed out of order has its own unit: it is no longer «lost»
        if u.get("absorbed"):
            keep, top = [], u["orig_end"]
            for r in u["absorbed"]:
                f, _, l = r.partition(":")[2].partition("-")
                f = int(f)
                l = int(l) if l else f
                lost = [n for n in range(f, l + 1) if (k[0], n) not in owned]
                if lost:
                    keep.append(f"{k[0]}:{lost[0]}" + (f"-{lost[-1]}" if lost[-1] > lost[0] else ""))
                    top = max(top, lost[-1])
            u["a_end"], u["absorbed"] = top, keep
    issues[:] = [i for i in issues if not (i.startswith("2:244–244") and (2, 244) in owned)]
    for s in counts:
        ks = [k for k in verses if k[0] == s]
        if ks:
            top = max(verses[k]["a_end"] for k in ks)
            if top < counts[s]:
                tie_gap(s, top + 1, counts[s], "before the surah ends")
    cover = {(s, n) for key in verses for s in [key[0]] for n in range(verses[key]["a"], verses[key]["a_end"] + 1)}
    got = Counter(s for (s, _) in cover)
    short = {s: (got[s], counts[s]) for s in counts if got[s] != counts[s]}
    missing = [f"{s}:{n}" for s in counts for n in range(1, counts[s] + 1) if (s, n) not in cover]
    n_empty = 0
    for g_ in [u for u in verses.values() if not clean(join(u["parts"]))[0].strip()]:
        for n_ in range(g_["a"], g_["a_end"] + 1):
            if not any(m_ == f"{surah_of(verses, g_)}:{n_}" for m_ in missing):
                missing.append(f"{surah_of(verses, g_)}:{n_}")
                n_empty += 1
    print(f"surahs {len(intros)}; verses {len(cover)}/6236; surahs not matching {len(short)} {dict(list(short.items())[:15])}")
    print(f"{dict(stats)}; issues {len(issues)} {issues[:10]}")
    if a.dump:
        Path(a.dump).write_text("".join(IC.json.dumps(g, ensure_ascii=False) + "\n" for g in segs))
    if a.dry:
        print("missing:", missing[:80], len(missing))
        return
    old = IC.json.loads((d / "source.json").read_text())
    tied = [r for u in verses.values() for r in (u.get("absorbed") or [])]
    IC.write(SID, segs, {
        "script": "enrichment/v2/fetch/import_meal_eliacik.py", "from": IC.inputs(SID, STEMS + ["eliacik-yasayan-kuran-nuzul-metin"]),
        "method": "archive.org OCR text (djvu.txt) of the three mushaf-ordered volumes; state machine over lines; "
                  "verses «N- text» in sequence; footnotes in sequence, tied by marker where the OCR kept it",
        "verse_count_mismatch": {str(k): v for k, v in short.items()}, "missing": [{"ayah": m_, "reason": "the verse number is printed in the OCR text but no meal text follows it (verse text lost in the OCR of this copy)", "checked": ["the three mushaf-ordered djvu.txt volumes", "the revelation-ordered edition djvu.txt (a later, rephrased edition, not usable as the same text)"]} for m_ in missing],
        "number_lost_in_ocr_text_tied_to_previous_unit": tied, "issues": issues,
        "counts": dict(stats), "dropped_sample": sample,
    }, {"coverage": f"1-114 ({len(cover) - n_empty}/6236 ayat)", "locator": "ayah", "kind": "meal",
        "notes": META["notes"] + f" Ingested {IC._dt.date.today().isoformat()} (fetch/import_meal_eliacik.py) from the OCR text of the "
                 f"three mushaf-ordered volumes: {len(cover) - n_empty}/6236 ayat covered (2026-10-09 review: pages printed in two columns, which the OCR reads across, were resynchronised; their verses may carry words of a neighbouring verse); {len(tied)} places where the OCR lost a verse number "
                 f"(their text sits in the unit before, tied there: see ingestion.number_lost_in_ocr_text_tied_to_previous_unit); "
                 f"{len(missing)} verse(s) with no text at all (ingestion.missing). Some verses are printed as groups («1/2-», «14-15-»), kept as a..a_end "
                 f"(overlapping groups such as 18:1-2 and 18:2-3 are both kept). Footnotes (Eliaçık's commentary) are kept whole; "
                 f"{stats['footnotes placed by their marker']} are placed by their marker, the others are tied to the verses of their page. "
                 f"OCR noise from the Arabic column was removed from verse text and kept in each segment's ocr_noise_removed; some "
                 f"noise remains inside lines."})



if __name__ == "__main__":
    main()
