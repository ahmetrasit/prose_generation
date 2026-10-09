#!/usr/bin/env python3
"""MEAL-EAT-SIVAS-KUTUKCU + REF-EAT-SIVAS-KUTUKCU-NOTES: an Old Anatolian Turkish interlinear Qur'an translation
(XV century; Sivas Kongre ve Etnografya Müzesi E.Y. 84/176, 622 leaves, Fātiḥa to Nās), folios 535b-616b only
(Qamar 54:1 to Nās 114), in Mehmet Kütükçü's master's thesis «Eski Anadolu Türkçesiyle Yazılmış Satır Arası Bir
Kur'ân Tercümesi (Gramer - Metin - Tertip - Sözlük) (535b - 616b)» (Cumhuriyet Üniversitesi, Sosyal Bilimler
Enstitüsü, Sivas, September 2005; supervisor Yrd. Doç. Dr. Burhan Paçacıoğlu). Partial: the leaves 535b-616b are
all this edition holds, and the thesis notes that Mücadele 58:22 is missing from the manuscript and Haşr 59:1 and
half of 59:2 as well (torn leaves).

Input: the OCR text of archive.org item eski-anadolu-turkcesiyle-yazilmis-satir-arasi-bir-kuran-tercumesi-gramer-metin-t
(uploader empireofhassaan@hotmail.com). The same thesis is uploaded a second time as EskiAnadoluTrkkesiyleYazalmlSatrArasrBirKurinTercmesi
(item «0456-»), with a slightly different OCR; only the first is read here.

The «METİN» part of the thesis has two layouts:
  - surahs 54-68 (Qamar to Qalam): the arranged text «N: <old text> (<modern Turkish>)», one verse per entry, verse
    ranges «1,2:», page headers «Kamer Süresi / 536a - 536b»;
  - surahs 69-114: a diplomatic transcription in which «/k/» is the manuscript line number, «(n)» the verse number
    that opens verse n, and a lone «584b» a folio; the OCR loses the first letters of many lines and interleaves the
    two page columns around the surah headings.
The modern Turkish glosses of the first layout, the editor's notes and the thesis's other parts go to the reference
source, the glosses tied to their verses.

  python3 -B enrichment/v2/fetch/import_meal_eat_sivas_kutukcu.py [--dry]
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

SID, NSID = "MEAL-EAT-SIVAS-KUTUKCU", "REF-EAT-SIVAS-KUTUKCU-NOTES"
IDENT = "eski-anadolu-turkcesiyle-yazilmis-satir-arasi-bir-kuran-tercumesi-gramer-metin-t"
URL = f"https://archive.org/details/{IDENT}"
FIRST_S = 54
V1 = re.compile(r"^\s*([\dilIİ|O]{1,3}(?:\s?[,:;.\-]+\s?[\dilIİ|O]{1,3}){0,5})\s?[:;]\s?(\S.*)$")
DIGFIX = str.maketrans({"i": "1", "l": "1", "I": "1", "İ": "1", "|": "1", "O": "0"})
FOLIO = re.compile(r"^[A-Za-z]?\s?\d{2,3}\s?[ab]\s?(?:[-–]\s?\d{2,3}\s?[ab])?\s?$")
PAGE_NO = re.compile(r"^\s*\d{1,3}\s*$")
HEADER = re.compile(r"S[üuâa]r?e?s[iı]?|Süres|Sâres", re.I)
HEADING = re.compile(r"S[ÜU]RE?[TP]?[ÜU]?\S*")
COUNT = re.compile(r"\(?\s*(\d{1,3})\s*[ÂA]YE?[TD]T?[İI]R\s*\)?")
MARK2 = re.compile(r"\(\s*(\d{1,3})\s*\)")
MARK2L = re.compile(r"\(\s*([\dilIİ|O]{1,3})\s*\)")


NAMES = {54: "kamer", 55: "rahman", 56: r"vak[ie]?a|vafi|fak", 57: "hadid", 58: r"mucadele", 59: r"hasr", 60: "mumtehine",
         61: r"saf\b|^saf", 62: r"cum.?a", 63: r"munaf", 64: r"tegabun|tegabun", 65: r"talak", 66: "tahrim", 67: "mulk", 68: "kalem",
         69: r"hakka|lakka|hakla", 70: r"mearic|me.?aric", 71: r"nuh", 72: r"cinn|cin\b", 73: "muzzemmil", 74: "muddessir",
         75: r"kiyame", 76: r"insan|dehr", 77: "murselat", 78: "nebe", 79: r"nazi", 80: r"abese", 81: "tekvir", 82: r"infit",
         83: r"mutaffif|musaffif", 84: r"insikak|insigak", 85: r"buruc", 86: r"tarik", 87: r"ala\b", 88: r"gasiye", 89: "fecr",
         90: "beled", 91: "sems", 92: "leyl", 93: r"duha", 94: r"insirah", 95: r"tin\b", 96: "alak", 97: "kadr", 98: "beyyine",
         99: "zilzal", 100: r"adiyat", 101: r"kari", 102: "tekasur", 103: r"asr\b", 104: "humeze", 105: r"fil\b", 106: "kures",
         107: r"ma.?un|maun", 108: "kevser", 109: "kafirun", 110: "nasr", 111: "tebbet", 112: r"ihlas|iylas|illas", 113: "felak",
         114: r"nas\b"}
_FOLD = str.maketrans({"ı": "i", "İ": "i", "ğ": "g", "Ğ": "g", "ş": "s", "Ş": "s", "ç": "c", "Ç": "c", "ö": "o", "Ö": "o", "ü": "u",
                       "Ü": "u", "â": "a", "Â": "a", "î": "i", "Î": "i", "û": "u", "Û": "u", "'": "", "’": "", "“": "", "”": ""})


def fold(x: str) -> str:
    return x.translate(_FOLD).lower()


def name_target(span: str, lo: int, hi: int) -> int | None:
    """The surah in lo..hi whose name occurs in the heading text (Turkish letters folded)."""
    f = fold(span)
    f = re.sub(r"^.*?suret\S*", "", f)
    for n in range(lo, min(hi, 114) + 1):
        if n in NAMES and re.search(NAMES[n], f):
            return n
    return None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    counts = IC.ayah_counts()
    raw = T.ensure_raw(SID, IDENT, "Eski_Anadolu_Tukcesi_Ile_Yazilmish", "kutukcu_535b-616b_djvu.txt")
    L = T.read_lines(raw)
    m0 = next(i for i, l in enumerate(L) if l.strip() == "METİN" and i > 3000)
    m1 = next(i for i in range(m0, len(L)) if L[i].strip() == "SÖZLÜK")
    stats: Counter = Counter()
    issues: list[str] = []
    notes_lines: list[tuple[int, str]] = []

    verses: dict[tuple[int, int], dict] = {}
    modern: dict[tuple[int, int], str] = {}
    cur_s = FIRST_S - 1          # becomes FIRST_S at the first heading / verse
    cur_a = 0
    last_a: dict[int, int] = {}
    folio = ""
    cur_key: tuple[int, int] | None = None
    fresh = True                 # a heading was seen and no verse of that surah yet
    seen_headings: list[tuple[int, int, int]] = []   # (line, surah, stated count)

    def start_surah(n: int, why: str) -> None:
        nonlocal cur_s, cur_a, fresh, cur_key
        if n != cur_s:
            cur_s, cur_a, cur_key = n, 0, None
        fresh = True

    def open_verse(s: int, a0: int, a1: int, text: str, line: int, flags: list[str] | None = None) -> None:
        nonlocal cur_key, cur_a, fresh
        key = (s, a0)
        if key in verses:                       # a repeated OCR page: keep the first, count the repeat
            stats["verse entries repeated by the OCR (a page printed twice), later copy dropped"] += 1
            cur_key = None
            return
        verses[key] = {"a_end": a1, "text": text, "page": folio, "line": line, "flags": flags or []}
        cur_key, cur_a, fresh = key, a1, False
        last_a[s] = max(last_a.get(s, 0), a1)

    def append(text: str) -> None:
        if cur_key is None:
            return
        if cur_key in modern:                    # the modern rendering has begun: this line continues it
            modern[cur_key] += " " + text
            return
        verses[cur_key]["text"] += " " + text
        if cur_key[0] <= 68 and not cur_key[0] >= 69:
            old, mod = split_modern(verses[cur_key]["text"])
            if mod:
                verses[cur_key]["text"], modern[cur_key] = old, mod

    def avg_len(sn: int) -> float:
        xs = [len(v["text"]) for (s2, a2), v in verses.items() if s2 == sn and a2 > 0 and v["a_end"] == a2 and v["text"]]
        return sum(xs) / len(xs) if len(xs) >= 3 else 90.0

    def extend(key: tuple[int, int], upto: int, why: str) -> bool:
        """The text kept after verse key[1] holds the verses up to `upto` whose markers the OCR lost, if it is long
        enough for them; otherwise those verses stay missing."""
        v = verses[key]
        k = upto - v["a_end"] + 1 + (0 if v["a_end"] > key[1] else 0)
        n_verses = upto - key[1] + 1
        if len(v["text"]) >= 0.25 * avg_len(key[0]) * n_verses:
            v["a_end"] = upto
            v["flags"].append(why)
            stats["verse groups made of verses whose markers the OCR lost (text long enough for them)"] += n_verses - 1
            return True
        issues.append(f"{key[0]}:{key[1]}: text too short for verses up to {upto} ({len(v['text'])} chars): those verses stay missing")
        return False

    def split_modern(t: str) -> tuple[str, str]:
        """«old text (modern Turkish)» -> (old text, modern); the first parenthesis that does not hold a number."""
        for m in re.finditer(r"\(", t):
            if not re.match(r"\(\s*\d{1,3}\s*\)", t[m.start():]):
                return t[:m.start()].strip(), t[m.start():].strip()
        return t.strip(), ""

    f2 = next(i for i in range(m0, m1) if len(re.findall(r"/\d{1,2}/", L[i])) >= 1 and i > m0 + 2000)
    for i in range(m0 + 1, f2):
        raw_l = L[i]
        s_ = raw_l.strip()
        if not s_:
            continue
        if PAGE_NO.match(s_):
            stats["thesis page numbers dropped"] += 1
            continue
        if FOLIO.match(s_) and len(s_) <= 18:
            folio = re.sub(r"\s", "", s_)
            continue
        if HEADER.search(s_) and not HEADING.search(s_) and len(s_) < 60 and "NOT" not in s_:
            stats["running page headers dropped (surah names of the page)"] += 1
            continue
        if s_.startswith("NOT"):
            notes_lines.append((i, s_))
            stats["editor's NOT lines (kept in the reference source)"] += 1
            continue
        # surah heading inside the line
        hm = HEADING.search(s_)
        cm = COUNT.search(s_) if hm else None
        if hm and (cm or "BİSM" in s_ or len(s_) < 40):
            before = s_[:hm.start()].strip()
            n_stated = int(cm.group(1)) if cm else None
            after = s_[cm.end():].strip() if cm else s_[hm.end():].strip()
            inter = s_[hm.end():cm.start()].strip() if cm else ""
            if before or inter:
                append((before + " " + inter).strip())
            target = name_target(s_[hm.start():cm.end() if cm else hm.end() + 30], max(cur_s, FIRST_S) if fresh else cur_s + 1, cur_s + 8)
            if target is None and n_stated:
                for n in range(max(cur_s, FIRST_S), min(cur_s + 8, 115)):
                    if counts[n] == n_stated and (n > cur_s or fresh):
                        target = n
                        break
                if target is None and cur_s >= FIRST_S:
                    for n in range(cur_s + 1, min(cur_s + 8, 115)):
                        if counts[n] == n_stated:
                            target = n
                            break
            else:
                target = cur_s + 1 if cur_s >= FIRST_S and not fresh else max(cur_s, FIRST_S)
            if target is None:
                issues.append(f"line {i}: heading «{s_[:50]}» does not fit any surah after {cur_s}; kept as text")
                append(s_)
                continue
            seen_headings.append((i, target, n_stated or 0))
            start_surah(target, "heading")
            s_ = after
            if not s_:
                continue
        # layout 1: «N: old text (modern)»
        m = V1.match(s_)
        if m and cur_s <= 68:
            s = max(cur_s, FIRST_S)
            nums = [int(x) for x in re.findall(r"\d+", m.group(1).translate(DIGFIX))]
            if not nums:
                append(s_)
                continue
            a0, a1 = nums[0], nums[-1] if nums[-1] >= nums[0] else nums[0]
            exp = last_a.get(s, 0) + 1
            if not fresh:
                if len(str(a0)) == 2 and str(a0)[0] == str(a0)[1] and not (exp - 1 <= a0 <= exp + 3):
                    a0 = int(str(a0)[0])       # «77:» for «7:», «11:» for «1:» ...
                    a1 = max(a0, a1 if a1 < 10 else a0)
                    stats["entry numbers with a doubled digit repaired («77:» read as 7)"] += 1
                if a0 < exp - 1 and a0 <= 3 and last_a.get(s, 0) >= counts[s] - 4:
                    start_surah(s + 1, "number reset")
                    s = cur_s
                elif a0 < exp - 1:
                    stats["entries whose number runs backwards, kept as text of the previous verse"] += 1
                    append(s_)
                    continue
            if not IC.valid(s, a0, a1):
                stats["entries whose verse number is outside the surah, kept as text"] += 1
                append(s_)
                continue
            old, mod = split_modern(m.group(2))
            open_verse(s, a0, a1, old, i)
            if mod:
                modern[(s, a0)] = mod
            continue
        append(s_)


    # --- layout 2: «(n)» opens verse n, «/k/» is a manuscript line, a lone «584b» a folio; headings inside lines
    seen_f2: set[str] = set()
    skip_block = False
    cur_s, cur_key, fresh = 69, None, True
    last_a.setdefault(69, 0)
    pre_text: dict[int, str] = {}
    for i in range(f2 - 6, m1):
        s_ = L[i].strip()
        if not s_ or PAGE_NO.match(s_):
            continue
        if FOLIO.match(s_) and len(s_) <= 18 or re.fullmatch(r"[S5][7T]{1,3}[ab]", s_):
            fid = re.sub(r"\s", "", s_)
            fid = {"S7T7b": "577b", "S7TTa": "577a"}.get(fid, fid)
            skip_block = fid in seen_f2          # a folio printed twice by the OCR: later copy dropped, counted
            if skip_block:
                stats["folio blocks printed twice by the OCR, later copy dropped"] += 1
            seen_f2.add(fid)
            folio = fid
            continue
        if skip_block:
            stats["lines of a repeated folio block dropped"] += 1
            continue
        if HEADER.search(s_) and not HEADING.search(s_) and len(s_) < 60:
            stats["running page headers dropped (surah names of the page)"] += 1
            continue
        pos = 0
        events = []
        for hm in HEADING.finditer(s_):
            cm = COUNT.search(s_, hm.end())
            if cm and cm.start() - hm.end() < 45:
                events.append((hm.start(), cm.end(), "head", int(cm.group(1)), s_[hm.end():cm.start()]))
            elif "SÜRET" in hm.group(0) and re.search(r"[ÂA]YE?[TD]", s_[hm.end():hm.end() + 40]):
                cm2 = re.search(r"\(?\s*([^\s()]{0,3})\s*[ÂA]YE?[TD]T?[İI]R\s*\)?", s_[hm.end():])
                if cm2:
                    events.append((hm.start(), hm.end() + cm2.end(), "head", 0, s_[hm.end():hm.end() + cm2.start()]))
        for mk in MARK2L.finditer(s_):
            if not any(e[0] <= mk.start() < e[1] for e in events):
                events.append((mk.start(), mk.end(), "mark", int(mk.group(1).translate(DIGFIX)) if mk.group(1).translate(DIGFIX).isdigit() else -1, ""))
        events.sort()
        for st, en, kind, n, inter in events:
            seg_text = s_[pos:st].strip()
            if seg_text:
                if cur_key is not None:
                    verses[cur_key]["text"] += " " + seg_text
                else:
                    pre_text[cur_s] = (pre_text.get(cur_s, "") + " " + seg_text).strip()
            pos = en
            if kind == "head":
                if inter.strip():
                    (verses[cur_key]["text"] if False else None)
                    if cur_key is not None:
                        verses[cur_key]["text"] += " " + inter.strip()
                target = name_target(s_[st:en] + " " + inter, cur_s + 1, cur_s + 8)
                for k in range(cur_s + 1, min(cur_s + 5, 115)):
                    if target is None and n and counts[k] == n:
                        target = k
                        break
                if target is None and not n and last_a.get(cur_s, 0) >= counts[cur_s] - 4:
                    target = cur_s + 1
                if target is None:
                    issues.append(f"line {i}: surah heading (count {n}) not placed after surah {cur_s}")
                    continue
                seen_headings.append((i, target, n))
                if cur_key is not None and verses[cur_key]["a_end"] < counts[cur_s]:
                    extend(cur_key, counts[cur_s], "the verses after this one have no markers in the OCR; their text is inside this entry")
                cur_s, cur_key, fresh = target, None, True
                last_a.setdefault(target, 0)
                continue
            if n < 0:
                continue
            exp = last_a.get(cur_s, 0) + 1
            if fresh:
                ok = n <= 10
            else:
                ok = exp <= n <= exp + 3
                if not ok and n <= 2 and last_a.get(cur_s, 0) >= counts[cur_s] - 4 and cur_s < 114:
                    cur_s += 1
                    last_a.setdefault(cur_s, 0)
                    ok, exp = True, 1
            if not ok or not IC.valid(cur_s, n):
                # not a verse number (a line-internal figure or a garbled marker): text
                if cur_key is not None:
                    verses[cur_key]["text"] += " " + s_[st:en]
                stats["parenthesised figures that do not continue the verse numbers, kept as text"] += 1
                continue
            flags = []
            if n != exp and not fresh:
                if cur_key is not None and extend(cur_key, n - 1, f"markers of verses {exp}-{n - 1} lost in the OCR; their text is inside this entry"):
                    pass
                issues.append(f"{cur_s}: marker ({n}) follows ({last_a.get(cur_s, 0)}): verse(s) {exp}-{n - 1} have no marker in the OCR")
            if fresh and n > 1:
                flags.append("first marker is not (1)")
            open_verse(cur_s, n, n, "", i, flags)
        tail = s_[pos:].strip()
        if tail:
            if cur_key is not None:
                verses[cur_key]["text"] += " " + tail
            else:
                pre_text[cur_s] = (pre_text.get(cur_s, "") + " " + tail).strip()
    if cur_key is not None and verses[cur_key]["a_end"] < counts[cur_s]:
        extend(cur_key, counts[cur_s], "the verses after this one have no markers in the OCR; their text is inside this entry")
    for s_, t in pre_text.items():
        t = t.strip()
        bm = re.match(r"^(.*?BİSM\S*.*?R[AÂ]HM\S*\s*R?\S*[İI]?M?)\s*(.*)$", t)
        head_t, body_t = (bm.group(1), bm.group(2)) if bm and len(bm.group(1)) < 80 else ("", t)
        if head_t:
            verses[(s_, 0)] = {"a_end": 0, "text": head_t, "page": "", "line": 0, "flags": []}
        if body_t:
            first = min((a0 for (s2, a0) in verses if s2 == s_ and a0 > 0), default=None)
            if first is not None and first > 1 and s_ != 69:
                verses[(s_, 1)] = {"a_end": first - 1, "text": body_t, "page": "", "line": 0,
                                   "flags": ["text before the first marker: verse 1" + (f"-{first - 1}" if first > 2 else "") + " unmarked in the OCR"]}
                if first > 2 and len(body_t) < 0.25 * avg_len(s_) * (first - 1):
                    issues.append(f"{s_}: text before the first marker is too short for verses 1-{first - 1}")
            elif first is None:
                V_ = counts[s_]
                if len(body_t) >= 0.25 * avg_len(s_) * V_:
                    verses[(s_, 1)] = {"a_end": V_, "text": body_t, "page": "", "line": 0,
                                       "flags": [f"no verse marker survives in the OCR: the whole surah text is kept as one group 1-{V_}"]}
                else:
                    issues.append(f"{s_}: text after the heading ({len(body_t)} chars) is too short for the {V_} verses: kept in the reference source only")
                    notes_lines.append((0, f"[{s_}: text without any verse marker] {body_t}"))
            elif first is not None and first > 1:
                verses[(s_, first - 1)] = {"a_end": first - 1, "text": body_t, "page": "", "line": 0,
                                           "flags": ["text before the first marker of the surah's first surviving page; may begin in a lost leaf"]}

    # --- finish: the pre-verse text (basmala) of each surah is the surah's head
    segs: list[dict] = []
    per_surah: dict[int, list[int]] = {}
    for (s, a0), v in sorted(verses.items()):
        text = re.sub(r"\s+", " ", v["text"]).strip()
        if a0 == 0:
            segs.append({"seg": f"{SID}:{s}:head", "s": s, "a": None, "a_end": None, "page": v["page"],
                         "head": "text before verse 1 (basmala, heading remains)", "text": text})
            continue
        g = {"seg": f"{SID}:{s}:{a0}", "s": s, "a": a0, "a_end": v["a_end"], "page": v["page"], "text": text}
        if v["flags"]:
            g["flags"] = v["flags"]
        segs.append(g)
        per_surah.setdefault(s, []).extend(range(a0, v["a_end"] + 1))
    seen_s = sorted(per_surah)
    miss = T.missing_in_range(per_surah, FIRST_S, 114)
    present = T.covered({s: per_surah[s] for s in seen_s})
    got = sum(len(set(v)) for v in per_surah.values())
    total = sum(counts[s] for s in range(FIRST_S, 115))
    print(f"{SID}: surahs {seen_s[0] if seen_s else None}-{seen_s[-1] if seen_s else None}: {got}/{total} verses; "
          f"surahs with misses {len(miss)}; headings {len(seen_headings)}; issues {len(issues)}")
    print(dict(stats))
    if a.dry:
        print("missing:", {k: T.ranges(v) for k, v in miss.items()})
        print("issues:", issues[:40])
        return
    nsegs: list[dict] = []
    for (s, a0), t in sorted(modern.items()):
        nsegs.append({"seg": f"{NSID}:{s}:{a0}#modern", "s": s, "a": a0, "a_end": verses[(s, a0)]["a_end"],
                      "head": "modern Turkish rendering printed after the old text (Kütükçü)", "text": t})
    for n, (i, t) in enumerate(notes_lines):
        nsegs.append({"seg": f"{NSID}:note:{n:02d}", "page": f"line{i}", "head": "editor's note in the text part", "text": t})
    for name, lo, hi, label in (("front", 0, m0, "thesis front matter, introduction, grammar"),
                                ("back", m1, len(L), "glossary (Sözlük), photocopy section, bibliography")):
        for n, (f, e, text) in enumerate(T.chunks(L[lo:hi], 3500)):
            nsegs.append({"seg": f"{NSID}:{name}:{n:04d}", "page": f"line{lo + f}", "head": label, "text": text})
    T.ensure_source(SID, {
        "id": SID, "title": "Eski Anadolu Türkçesi satır-arası Kur'an tercümesi, Sivas manuscript, leaves 535b-616b (Kütükçü)",
        "author": "anonymous (XV century; colophon note «tarih-i tahriri 903», waqf of Kezban Hatun)", "translator": "anonymous",
        "death_ah": None, "kind": "meal", "tradition": "", "language": "tr", "turkic_stage": "Old Anatolian Turkish",
        "edition": "Mehmet Kütükçü, Eski Anadolu Türkçesiyle Yazılmış Satır Arası Bir Kur'ân Tercümesi (Gramer - Metin - Tertip - "
                   "Sözlük) (535b - 616b), master's thesis, Cumhuriyet Üniversitesi, Sosyal Bilimler Enstitüsü, Sivas, "
                   "September 2005 (supervisor Yrd. Doç. Dr. Burhan Paçacıoğlu)",
        "edition_editor": "Mehmet Kütükçü", "edition_publisher": "Cumhuriyet Üniversitesi (master's thesis)", "edition_year": 2005,
        "manuscript": "Sivas Kongre ve Etnografya Müzesi E.Y. 84/176 (622 leaves; this edition: 535b-616b); "
                      "the other published part of the same manuscript is leaves 105b-170b (Delice, MEAL-EAT-SIVAS-DELICE)",
        "access": "yerel", "locator": "ayah", "urls": [URL, "https://archive.org/details/EskiAnadoluTrkkesiyleYazalmlSatrArasrBirKurinTercmesi"],
        "uploader": "empireofhassaan@hotmail.com", "archive_identifier": IDENT,
        "licence": "scholarly edition; archive.org third-party upload; local research use", "panel": False, "cross_witnesses": [],
    }, raw)
    T.ensure_source(NSID, {
        "id": NSID, "title": "Kütükçü, Sivas interlinear thesis: modern renderings, notes, grammar, glossary",
        "author": "Mehmet Kütükçü", "kind": "reference", "tradition": "academic", "language": "tr", "turkic_stage": "Old Anatolian Turkish",
        "edition": "same thesis as MEAL-EAT-SIVAS-KUTUKCU", "access": "yerel", "locator": "section", "urls": [URL],
        "uploader": "empireofhassaan@hotmail.com", "archive_identifier": IDENT,
        "licence": "scholarly edition; archive.org third-party upload; local research use",
        "raw_shared": [f"../{SID}/{raw.relative_to(IC.CORPUS / SID)}"], "panel": False, "files": {},
    }, None)
    ing = {"script": "enrichment/v2/fetch/import_meal_eat_sivas_kutukcu.py", "from": {str(raw.relative_to(IC.CORPUS / SID)): IC.C.sha256(raw)},
           "method": "OCR djvu.txt, METİN part; layout 1 «N:» entries, layout 2 «(n)» markers; surah by heading count and number reset",
           "edition_range": f"folios 535b-616b = surahs {FIRST_S}:1 to 114 (the manuscript lacks 58:22, 59:1 and half of 59:2)",
           "covered": present, "missing": miss,
           "verse_count_mismatch": {k: [len(set(per_surah.get(int(k), []))), counts[int(k)]] for k in miss},
           "headings_found": [{"line": l, "surah": s, "stated_count": c} for l, s, c in seen_headings],
           "issues": issues, "counts": T.tally(stats), "dropped_sample": []}
    IC.write(SID, segs, ing, {
        "coverage": f"{FIRST_S}-114 ({got}/{total} ayat of the edition's range 54:1-114:6; the manuscript itself lacks 58:22, 59:1-2a)",
        "notes": "Partial: leaves 535b-616b of the Sivas manuscript only (surahs 54-114). "
                 f"{got} of {total} verses present; {sum(len(v) for v in miss.values())} missing in {len(miss)} surahs "
                 "(listed in ingestion.missing: the manuscript's own lacunae 58:22 and 59:1-2, and verses lost to the OCR, whose first letters "
                 "of many lines are missing in surahs 69-114). Folio ids sit in `page`; manuscript line numbers /k/ stay in the text of surahs 69-114. "
                 "Text is OCR as is, not corrected. " + T.NOTE})
    IC.write(NSID, nsegs, {"script": "enrichment/v2/fetch/import_meal_eat_sivas_kutukcu.py",
                           "from": {str(raw.relative_to(IC.CORPUS / SID)): IC.C.sha256(raw)}, "counts": T.tally(stats), "issues": []}, {})


if __name__ == "__main__":
    main()
