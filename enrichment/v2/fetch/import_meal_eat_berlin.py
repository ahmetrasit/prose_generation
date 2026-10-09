#!/usr/bin/env python3
"""REF-EAT-BERLIN-TUNA-NOTES: the introduction and apparatus of Cem Tuna's master's thesis «Berlin El Yazmaları
Kütüphanesi'ndeki Eski Anadolu Türkçesi Satır-Arası Kur'an Tercümesi (Giriş-Metin)» (Akdeniz Üniversitesi, Sosyal Bilimler
Enstitüsü, Türk Dili ve Edebiyatı Ana Bilim Dalı, Antalya 2016; supervisor Doç. Dr. Suat Ünlü), from archive.org item
berlin-el-yazmalari-kutuphanesindeki-eski-anadolu-turkcesi-satir-arasi-kuran-tercumesi (uploader empireofhassaan@hotmail.com).

This work is NOT imported a second time as a meal source: its text (folios 1a-320b of the Berlin manuscript, all 114 surahs) is
exactly the text the corpus already holds as MEAL-ESKIANADOLU. The kuranmeali.com page behind MEAL-ESKIANADOLU says so
(«Bu meal Akdeniz Üniversitesi Sosyal Bilimler Enstitüsüne 2016 yılında Cem Tuna tarafından Yüksek lisans tezi olarak sunulmuş ...
Berlin El Yazmaları Kütüphanesi'nde kayıtlı Satır-arası Kur'an Tercümesi»), and this script measures it on the OCR text: the first
words of MEAL-ESKIANADOLU's verses are looked up in the thesis's Metin part (the number is recorded in the ingestion record). The
host-cleaned MEAL-ESKIANADOLU text is also much cleaner than the OCR of the thesis scan, so the thesis Metin is kept only as the raw
file; what this script adds is the thesis's introduction and the rest of its apparatus, as sections of a reference source.

How the edition marks the text (read from the thesis introduction): leaf numbers in bold square brackets «[5a]», «(17b)»; surah
numbers between slashes «/1/ /2/»; verse numbers «1. 2. 3.»; manuscript lines in parentheses «(2) (3)»; unreadable places «|...|».

  python3 -B enrichment/v2/fetch/import_meal_eat_berlin.py [--dry]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402
import turkic_common as T  # noqa: E402

NSID = "REF-EAT-BERLIN-TUNA-NOTES"
OTHER = "MEAL-ESKIANADOLU"
IDENT = "berlin-el-yazmalari-kutuphanesindeki-eski-anadolu-turkcesi-satir-arasi-kuran-tercumesi"
URL = f"https://archive.org/details/{IDENT}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    raw = T.ensure_raw(NSID, IDENT, "_djvu.txt", "tuna_berlin_djvu.txt")
    L = T.read_lines(raw)
    m0 = next(i for i, l in enumerate(L) if l.strip() == "METİN" and i > 300)
    mend = next((i for i in range(len(L) - 1, m0, -1) if re.match(r"^\s*(KAYNAKÇA|Kaynakça)\s*$", L[i])), len(L))
    # identity evidence: first 3 words of every verse of MEAL-ESKIANADOLU found in the thesis Metin (line / leaf markers removed)
    body = "\n".join(L[m0:mend])
    body = re.sub(r"\(\s*\d{1,3}\s*[ab]?\s*\)|\[\s*\d+[ab]\s*\]|\|\d+[ab]J", " ", body)
    hay = " ".join(T.fold(w) for w in body.split())
    hay = re.sub(r"\s+", " ", hay)
    n = hit = 0
    for line in (IC.CORPUS / OTHER / "segments.jsonl").open(encoding="utf-8"):
        r = json.loads(line)
        if not r.get("a"):
            continue
        ws = [T.fold(w) for w in r["text"].split()][:3]
        key = " ".join(w for w in ws if w)
        if len(key) < 8:
            continue
        n += 1
        hit += key in hay
    print(f"first three words of {n} verses of {OTHER}: {hit} found in the thesis Metin ({100 * hit / n:.1f}%)")
    if a.dry:
        return
    nsegs: list[dict] = []
    for name, lo, hi, label in (("front", 0, m0, "front matter and introduction (Giriş) of the thesis"),
                                ("back", mend, len(L), "bibliography and the rest after the Metin")):
        for c, (f, e, text) in enumerate(T.chunks(L[lo:hi], 3500)):
            nsegs.append({"seg": f"{NSID}:{name}:{c:04d}", "page": f"line{lo + f}", "head": label, "text": text,
                          "refs": IC.find_refs(text)})
    T.ensure_source(NSID, {
        "id": NSID, "title": "Tuna, Berlin Old Anatolian interlinear thesis: introduction and apparatus",
        "author": "Cem Tuna", "kind": "reference", "tradition": "academic", "language": "tr", "turkic_stage": "Old Anatolian Turkish",
        "edition": "Cem Tuna, Berlin El Yazmaları Kütüphanesi'ndeki Eski Anadolu Türkçesi Satır-Arası Kur'an Tercümesi (Giriş-Metin), "
                   "master's thesis, Akdeniz Üniversitesi, Sosyal Bilimler Enstitüsü, Antalya 2016 (supervisor Doç. Dr. Suat Ünlü)",
        "edition_editor": "Cem Tuna", "edition_publisher": "Akdeniz Üniversitesi (master's thesis)", "edition_year": 2016,
        "manuscript": "Staatsbibliothek zu Berlin (Berlin El Yazmaları Kütüphanesi), Old Anatolian Turkish interlinear, folios 1a-320b transcribed",
        "access": "yerel", "locator": "section", "urls": [URL], "uploader": "empireofhassaan@hotmail.com", "archive_identifier": IDENT,
        "licence": "scholarly edition; archive.org third-party upload; local research use", "panel": False,
        "duplicate_of_meal": OTHER,
        "coverage": "introduction and apparatus; the translation text itself is MEAL-ESKIANADOLU",
    }, raw)
    IC.write(NSID, nsegs, {
        "script": "enrichment/v2/fetch/import_meal_eat_berlin.py", "from": {str(raw.relative_to(IC.CORPUS / NSID)): IC.C.sha256(raw)},
        "method": "OCR djvu.txt; front and back matter as chunks; the Metin part is not stored as a meal source (identical to MEAL-ESKIANADOLU)",
        "identity_with_MEAL-ESKIANADOLU": {"verses_checked": n, "first_three_words_found_in_thesis_metin": hit, "percent": round(100 * hit / n, 1),
                                           "why_not_100": "OCR of the thesis scan (the letter ñ/ŋ of «Tañrı», ā, ī, ū come out as other letters)"},
        "counts": {}, "issues": []}, {
        "notes": "The thesis edits the whole Berlin manuscript (1a-320b); that text is already in the corpus as MEAL-ESKIANADOLU "
                 "(kuranmeali.com, taken from this thesis), so no second meal source was made. " + T.NOTE})


if __name__ == "__main__":
    main()
