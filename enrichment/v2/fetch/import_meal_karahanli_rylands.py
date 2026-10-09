#!/usr/bin/env python3
"""MEAL-KARAHANLI-RYLANDS + REF-KARAHANLI-RYLANDS-NOTES: the Karakhanid Turkish interlinear Qur'an translation of the
John Rylands Library manuscript (Manchester, Arabic MSS 25-38: fourteen volumes of a thirty-part Qur'an, so the
translation is incomplete), in Aysu Ata, «Karahanlı Türkçesinde İlk Kur'an Tercümesi (Rylands Nüshası,
Giriş-Metin-Notlar-Dizin)», Ankara: Türk Dil Kurumu, 2nd printing 2013 (Türk Dil Kurumu Yayınları 854;
ISBN 975-16-1737-5).

Input: the OCR text of archive.org item 1.denememKARAHANLITURKCESNDEELKKURKUANTERCUMESERRyiandsNR14ShasGiriMetinNotlarDizin
(uploader lazkopatgenc@hotmail.com), fetched into raw/acquired-2026-10-09/. The OCR is poor (the book's special letters
come out as digits and symbols: «9» for ç, «§» for ş, «i» for ü, «Tangn» for Tañrı, spaced word gaps).

How the edition prints the text (the «Metin» part, from «SORETU'L-AL-I IMRAN» on): one block per surah, headed «SURETU'L-...»
and the basmala «Başladım Tangrı atı birle ...»; every verse is a paragraph that opens with its number («158 Eger ölse
siz ...»), «...» marks a lacuna, «[22a 1]» is folio 22a line 1 (the OCR often reads « [22a  1] », « (24b 1]» ...), «(2)» /
«(3)» are line numbers; the editor's footnotes follow the text («8 22b1'de 3:159. ayetten 167. ayete atlanmıştır»: the
manuscript jumps from 3:159 to 3:167). The manuscript skips verses and whole surahs; every verse the edition prints is
stored, and the verses of the covered surahs it does not print are listed as missing.

  python3 -B enrichment/v2/fetch/import_meal_karahanli_rylands.py [--dry]
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

SID, NSID = "MEAL-KARAHANLI-RYLANDS", "REF-KARAHANLI-RYLANDS-NOTES"
IDENT = "1.denememKARAHANLITURKCESNDEELKKURKUANTERCUMESERRyiandsNR14ShasGiriMetinNotlarDizin"
URL = "https://archive.org/details/1.denememKARAHANLITURKCESNDEELKKURKUANTERCUMESERRyiandsNR14ShasGiriMetinNotlarDizin"
HEAD = re.compile(r"^\s*S[A-Z0-9]RETU")
FOLIO = re.compile(r"[\[(]\s*\d{1,3}\s?[ab]\s?[1l]?\s?[\])]")
FOOT_WORDS = re.compile(r"\d+\s?:\s?\d+|mukerrer|miikerrer|m[uü]kerrer|ayet|ni[sş]hasinda|nushas|Rylands|Dublin|Chester|\bbk\.|bkz|atlan|yazilmi|silinmi|Ar\.|Far\.")
NAMES = {3: r"imran", 4: r"nis", 5: r"ma.?[a-z]?de", 6: r"enc?am", 7: r"a.?raf", 8: r"enfal", 9: r"tevbe", 10: r"yunus", 11: r"\bhud",
         12: r"yusuf", 13: r"ra.?d\b", 14: r"ibrahim", 15: r"\W?icr|hicr|ijcr", 16: r"nahl", 17: r"isra", 18: r"kehf", 19: r"meryem",
         20: r"taha", 21: r"enbiya", 22: r"hacc?", 23: r"mu.?minun", 24: r"\bnur", 25: r"furkan", 26: r"su.?ara", 27: r"neml",
         28: r"kasas|ka.as", 29: r"cankebut|ankebut", 30: r"rum", 31: r"lokman", 32: r"secde", 33: r"ahzab", 34: r"seba", 35: r"fa.?[tj]ir|fatir",
         36: r"yas", 37: r"saffat", 38: r"\bsad", 39: r"z.{0,3}mer", 40: r"mu.?min\b|mu.?m.n\b", 41: r"fussilet", 42: r"sura", 43: r"zu.?hruf|zuhruf|zlhruf",
         44: r"du.?an|duhan|duuan", 45: r"cas.?ye|casiye|cathiye", 46: r"ahkaf", 47: r"muhammed", 48: r"feth", 49: r"hucurat|jucurat|ijucurat", 50: r"\bkaf",
         58: r"mucadele", 59: r"kla.?r|hasr|ha.r", 61: r"saff|\$aff|aff", 62: r"cum", 63: r"munaf", 64: r"tag.?abun|t\s+ag|gabun", 65: r"talak", 66: r"tahrim"}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    counts = IC.ayah_counts()
    raw = T.ensure_raw(SID, IDENT, "_djvu.txt", "ata_rylands_djvu.txt")
    L = T.read_lines(raw)
    stats: Counter = Counter()
    issues: list[str] = []
    m0 = next(i for i, l in enumerate(L) if HEAD.match(l) and "IMRAN" in l.upper())
    m1 = next(i for i in range(m0 + 100, len(L)) if L[i].strip() == "NOTLAR")
    heads = [i for i in range(m0, m1) if HEAD.match(L[i]) and len(L[i].strip()) < 40]
    # surah of each heading: by name, else the only surah that fits between its neighbours
    names_f = []
    for i in heads:
        t = L[i].lower()
        t = t.translate(str.maketrans({"’": "", "'": "", "`": ""}))
        t = re.sub(r"^\s*s\w?retu\W*(?:[a-z]{1,2}-)?", "", t)
        names_f.append(t.strip())
    sids: list[int | None] = []
    prev = 2
    for t in names_f:
        got = None
        for n in range(prev + 1, 115):
            if n in NAMES and re.search(NAMES[n], t):
                got = n
                break
        sids.append(got)
        if got:
            prev = got
    for k, g in enumerate(sids):
        if g is None:
            lo = next((sids[j] for j in range(k - 1, -1, -1) if sids[j]), 2)
            hi = next((sids[j] for j in range(k + 1, len(sids)) if sids[j]), 115)
            if hi - lo == 2:
                sids[k] = lo + 1
                issues.append(f"heading line {heads[k]} «{L[heads[k]].strip()}» is garbled: surah {lo + 1} (the only one between {lo} and {hi})")
            else:
                issues.append(f"heading line {heads[k]} «{L[heads[k]].strip()}» could not be placed (between {lo} and {hi})")
    print("surahs in the text:", [s for s in sids if s])
    bounds = heads + [m1]
    verses: dict[tuple[int, int], dict] = {}
    notes: dict[int, list[str]] = {}
    for k, h in enumerate(heads):
        sn = sids[k]
        if not sn:
            notes.setdefault(0, []).extend(x.strip() for x in L[h:bounds[k + 1]] if x.strip())
            continue
        V = counts[sn]
        last = 0
        cur: tuple[int, int] | None = None
        folio_pending = ""
        head_lines: list[str] = []
        for i in range(h + 1, bounds[k + 1]):
            t = re.sub(r"\s+", " ", L[i]).strip()
            if not t:
                continue
            if re.fullmatch(r"[\d\s]{1,5}", t) and not FOLIO.search(t):
                stats["page numbers / lone figures dropped"] += 1
                continue
            m = re.match(r"^(\d{1,3})\s+(.*)$", t)
            if m and 1 <= int(m.group(1)) <= V and (int(m.group(1)) > last or (last == 0 and int(m.group(1)) == 1)):
                n = int(m.group(1))
                rest = m.group(2)
                footnote_like = bool(FOOT_WORDS.search(rest[:60])) and not rest.startswith("...") and not FOLIO.search(rest[:20])
                if not footnote_like and (last == 0 or n <= last + 40):
                    cur = (sn, n)
                    verses[cur] = {"text": rest, "line": i, "lacuna_start": rest.startswith("...")}
                    last = n
                    continue
            m = re.match(r"^(\d{1,2})\s+(.*)$", t)
            if m and cur is not None and (int(m.group(1)) <= last or FOOT_WORDS.search(m.group(2)[:60])):
                notes.setdefault(sn, []).append(t)
                stats["footnote lines of the edition, kept in the reference source"] += 1
                continue
            if cur is None:
                head_lines.append(t)
            else:
                verses[cur]["text"] += " " + t
        if head_lines:
            verses[(sn, 0)] = {"text": " ".join(head_lines), "line": h, "lacuna_start": False}
    segs: list[dict] = []
    per_surah: dict[int, list[int]] = {}
    for (sn, n), v in sorted(verses.items()):
        text = re.sub(r"\s+", " ", v["text"]).strip()
        if n == 0:
            segs.append({"seg": f"{SID}:{sn}:head", "s": sn, "a": None, "a_end": None, "page": f"line{v['line']}",
                         "head": "surah heading lines and basmala", "text": text})
            continue
        g = {"seg": f"{SID}:{sn}:{n}", "s": sn, "a": n, "a_end": n, "page": f"line{v['line']}", "text": text}
        if v["lacuna_start"]:
            g["lacuna_at_start"] = True
        segs.append(g)
        per_surah.setdefault(sn, []).append(n)
        stats["folio markers in the text (approx.)"] += len(FOLIO.findall(text))
    covered_surahs = sorted(per_surah)
    miss = T.missing_in_range(per_surah, 1, 114)
    absent = [s for s in range(1, 115) if s not in per_surah]
    miss_in = {k: v for k, v in miss.items() if int(k) in per_surah}
    present = T.covered(per_surah)
    got = sum(len(set(v)) for v in per_surah.values())
    tot_in = sum(counts[s] for s in covered_surahs)
    print(f"{SID}: {len(covered_surahs)} surahs, {got} verses of {tot_in} in those surahs; missing inside them {sum(len(v) for v in miss_in.values())}")
    print(dict(stats))
    print("issues", issues)
    if a.dry:
        print("covered:", present)
        print("missing:", {k: T.ranges(v) for k, v in miss_in.items()})
        return
    nsegs: list[dict] = []
    for sn, ls in sorted(notes.items()):
        for c, (_, _, text) in enumerate(T.chunks(ls, 3000)):
            nsegs.append({"seg": f"{NSID}:{sn}:notes:{c:02d}", "s": sn or None, "a": 1 if sn else None, "a_end": counts[sn] if sn else None,
                          "head": "footnotes of the edition for this surah (marker numbers are not kept by the OCR)" if sn else "text of headings that could not be placed",
                          "text": text})
    for name, lo, hi, label in (("front", 0, m0, "introduction (Giriş), transliteration signs, bibliography"),
                                ("back", m1, len(L), "Notlar, Türkçe Dizin, Farsça Dizin")):
        for c, (f, e, text) in enumerate(T.chunks(L[lo:hi], 3500)):
            nsegs.append({"seg": f"{NSID}:{name}:{c:04d}", "page": f"line{lo + f}", "head": label,
                          "text": re.sub(r"[ \t]+", " ", text)})
    T.ensure_source(SID, {
        "id": SID, "title": "Karahanlı Türkçesinde İlk Kur'an Tercümesi, Rylands manuscript (Ata edition)",
        "author": "anonymous (Karakhanid interlinear, XI-XII century)", "translator": "anonymous", "death_ah": None, "kind": "meal",
        "tradition": "", "language": "tr", "turkic_stage": "Karakhanid",
        "edition": "Aysu Ata, Karahanlı Türkçesinde İlk Kur'an Tercümesi (Rylands Nüshası, Giriş-Metin-Notlar-Dizin), Ankara: Türk Dil Kurumu, "
                   "2nd printing 2013 (Türk Dil Kurumu Yayınları 854; ISBN 975-16-1737-5; 1st printing 1998)",
        "edition_editor": "Aysu Ata", "edition_publisher": "Türk Dil Kurumu", "edition_year": 2013,
        "manuscript": "John Rylands Library, Manchester, Arabic MSS 25-38 (fourteen volumes; the manuscript has a thirty-part Qur'an and "
                      "lacks parts and verses)",
        "access": "yerel", "locator": "ayah", "urls": [URL], "uploader": "lazkopatgenc@hotmail.com", "archive_identifier": IDENT,
        "licence": "scholarly edition; archive.org third-party upload; local research use", "panel": False, "cross_witnesses": [],
    }, raw)
    T.ensure_source(NSID, {
        "id": NSID, "title": "Ata, Rylands Qur'an translation: introduction, footnotes, notes, indexes",
        "author": "Aysu Ata", "kind": "reference", "tradition": "academic", "language": "tr", "turkic_stage": "Karakhanid",
        "edition": "same book as MEAL-KARAHANLI-RYLANDS", "access": "yerel", "locator": "section", "urls": [URL],
        "uploader": "lazkopatgenc@hotmail.com", "archive_identifier": IDENT,
        "licence": "scholarly edition; archive.org third-party upload; local research use",
        "raw_shared": [f"../{SID}/{raw.relative_to(IC.CORPUS / SID)}"], "panel": False, "files": {},
    }, None)
    ing = {"script": "enrichment/v2/fetch/import_meal_karahanli_rylands.py", "from": {str(raw.relative_to(IC.CORPUS / SID)): IC.C.sha256(raw)},
           "method": "OCR djvu.txt, Metin part: verse paragraphs by their opening number (increasing within a surah)",
           "edition_range": f"{len(covered_surahs)} surahs: {covered_surahs}; the manuscript has no text for the other {len(absent)} surahs",
           "covered": present, "missing": miss_in,
           "verse_count_mismatch": {k: [len(set(per_surah[int(k)])), counts[int(k)]] for k in miss_in},
           "surahs_absent_from_the_edition": absent,
           "editor_statements_on_gaps": [t for ls in notes.values() for t in ls if re.search(r"cilt|atlan|ba..?l[iıy]or|biterek|eksik|dubl", t, re.I)][:80], "issues": issues, "counts": T.tally(stats), "dropped_sample": []}
    IC.write(SID, segs, ing, {
        "coverage": f"{len(covered_surahs)} surahs ({got}/{tot_in} verses of those surahs); {len(absent)} surahs have no text in the manuscript",
        "notes": "Partial manuscript (Rylands, Manchester). Surahs present: " + ", ".join(map(str, covered_surahs)) +
                 f". {got} verses are printed; {sum(len(v) for v in miss_in.values())} verses of those surahs are not printed (manuscript lacunae and "
                 "OCR losses; listed in ingestion.missing, and the editor's footnotes in the reference source say where the manuscript jumps). "
                 "OCR is poor: the special letters of the transliteration come out as digits and symbols (9=ç, §=ş, i=ü, 'Tangn'=Tañrı). "
                 "Folio and line markers [22a 1] and (2) stay in the text as the OCR gives them. " + T.NOTE})
    IC.write(NSID, nsegs, {"script": "enrichment/v2/fetch/import_meal_karahanli_rylands.py",
                           "from": {str(raw.relative_to(IC.CORPUS / SID)): IC.C.sha256(raw)}, "counts": T.tally(stats), "issues": []}, {})


if __name__ == "__main__":
    main()
