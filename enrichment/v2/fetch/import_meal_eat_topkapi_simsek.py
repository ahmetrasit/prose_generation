#!/usr/bin/env python3
"""MEAL-EAT-TOPKAPI-SIMSEK + REF-EAT-TOPKAPI-SIMSEK-NOTES: an Old Anatolian Turkish interlinear Qur'an translation, complete
(surahs 1-114), Topkapı Sarayı Müzesi Koğuşlar Kitaplığı K. 252, in Yaşar Şimşek's doctoral thesis «Eski Anadolu Türkçesi
Satırarası Kur'ân Tercümesi (Topkapı Nüshası, Giriş - Metin - Notlar - Dizin)» (Kırıkkale Üniversitesi, Sosyal Bilimler
Enstitüsü, Yeni Türk Dili Bilim Dalı, January 2017; supervisor Prof. Dr. Bilgehan A. Gökdağ).

Input: the OCR text of archive.org item eski-anadolu-turkcesi-satirarasi-kuran-tercumesi (uploader
empireofhassaan@hotmail.com), fetched into raw/acquired-2026-10-09/.

How the edition prints the text (the «METİN» part, one block per surah headed «2.Süretü'l-Bakara ve Hiye ... Ayeten»): a
running transliteration with NO verse numbers ("*" or "?" now and then, not one per verse); the leaf is marked «(3b|»,
«(5a)» and the manuscript line «(4)» inside the text; the basmala of the surahs after the first is printed in Arabic
transliteration and is not translated.

Because the OCR keeps no verse boundary, the verses are cut by aligning each surah's text with the verses of
MEAL-ESKIANADOLU (the Berlin Old Anatolian interlinear, same tradition and very close wording, verse numbers exact): a
dynamic programme over word positions with the cut points kept near the proportional place, maximising the trigram
similarity of every run with its verse. Every segment says it (boundary_inferred, similarity_to_eskianadolu; below 0.25
low_similarity); where the oracle itself holds merged verse groups, the group is stored once as a..a_end. Nothing is cut
away: all the words of a surah are distributed to its verses.

  python3 -B enrichment/v2/fetch/import_meal_eat_topkapi_simsek.py [--dry] [--only S[,S...]]
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

SID, NSID = "MEAL-EAT-TOPKAPI-SIMSEK", "REF-EAT-TOPKAPI-SIMSEK-NOTES"
ORACLE = "MEAL-ESKIANADOLU"
IDENT = "eski-anadolu-turkcesi-satirarasi-kuran-tercumesi"
URL = f"https://archive.org/details/{IDENT}"
HEAD = re.compile(r"^\s*(\d{1,4})\s?\.?\s?S[üuû]r?[eé]t")
BASMALA = re.compile(r"b[ie]?\W{0,3}sm[ie]\W?l+[aâ]h|bi\W?smi", re.I)
MARK = re.compile(r"^[\(\[|T]?\d{0,3}[abAB]?[|\)\]j]?$")


def load_oracle() -> dict[int, list[tuple[int, int, str]]]:
    p = IC.CORPUS / ORACLE / "segments.jsonl"
    out: dict[int, list[tuple[int, int, str]]] = {}
    for line in p.open(encoding="utf-8"):
        r = json.loads(line)
        if r.get("s") and r.get("a"):
            out.setdefault(r["s"], []).append((r["a"], r.get("a_end") or r["a"], r["text"]))
    for v in out.values():
        v.sort()
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--only")
    a = ap.parse_args()
    counts = IC.ayah_counts()
    oracle = load_oracle()
    only = {int(x) for x in a.only.split(",")} if a.only else None
    raw = T.ensure_raw(SID, IDENT, "Topkap", "topkapi_simsek_djvu.txt")
    L = T.read_lines(raw)
    stats: Counter = Counter()
    issues: list[str] = []
    m0 = next(i for i, l in enumerate(L) if l.strip() == "METİN" and i > 4000)
    m1 = next(i for i in range(m0, len(L)) if L[i].strip() == "NOTLAR")
    heads = [i for i in range(m0, m1) if HEAD.match(L[i].strip()) and len(L[i].strip()) < 160
             and not re.search(r"m[üu]stensih|yaz[ıi]lm[ıi][şs]|hata", L[i], re.I)]
    # one heading per surah, in order
    sel: list[tuple[int, int]] = []
    for i in heads:
        n = int(HEAD.match(L[i].strip()).group(1))
        exp = len(sel) + 1
        if n != exp:
            issues.append(f"line {i}: heading «{L[i].strip()[:50]}» numbered {n}, expected {exp}: taken as surah {exp}")
        if exp <= 114:
            sel.append((i, exp))
    if len(sel) != 114:
        sys.exit(f"found {len(sel)} surah headings, expected 114")
    bounds = [i for i, _ in sel] + [m1]
    segs: list[dict] = []
    per_surah: dict[int, list[int]] = {}
    sims_all: list[float] = []
    low: list[str] = []
    grouped: list[str] = []
    per_surah_sim: dict[str, float] = {}
    for k, (h, sn) in enumerate(sel):
        if only and sn not in only:
            continue
        V = counts[sn]
        lines = [L[i].strip() for i in range(h + 1, bounds[k + 1])]
        head_parts = [L[h].strip()]
        body: list[str] = []
        for ln in lines:
            if not ln:
                continue
            if re.fullmatch(r"\d{1,3}", ln):
                stats["thesis page numbers dropped"] += 1
                continue
            if not body and BASMALA.search(ln) and sn != 1 and len(ln) < 50:
                head_parts.append(ln)
                continue
            body.append(ln)
        txt = ""
        for ln in body:
            if txt.endswith("-") and not txt.endswith("--"):
                txt = txt[:-1] + (" " + ln if ln.startswith("(") else ln)
            else:
                txt = (txt + " " + ln).strip()
        words = txt.split()
        segs.append({"seg": f"{SID}:{sn}:head", "s": sn, "a": None, "a_end": None, "page": f"line{h}",
                     "head": "surah heading and basmala as printed", "text": " ".join(head_parts)})
        orc = oracle.get(sn, [])
        res = T.align_to_oracle(words, [t for _, _, t in orc]) if orc and len(words) >= len(orc) else None
        if not res:
            issues.append(f"{sn}: could not align {len(words)} words to {len(orc)} oracle units: the surah is stored as one group 1-{V}")
            segs.append({"seg": f"{SID}:{sn}:1", "s": sn, "a": 1, "a_end": V, "page": f"line{h}", "grouped": True,
                         "head": "whole surah as one group (alignment failed)", "text": " ".join(words)})
            per_surah.setdefault(sn, []).extend(range(1, V + 1))
            continue
        ends, sims = res
        p0 = 0
        for (a0, a1, _), e, sm in zip(orc, ends, sims):
            g = {"seg": f"{SID}:{sn}:{a0}", "s": sn, "a": a0, "a_end": a1, "page": f"line{h}", "boundary_inferred": True,
                 "similarity_to_eskianadolu": round(sm, 2), "text": " ".join(words[p0:e])}
            if a1 > a0:
                g["grouped"] = True
                grouped.append(f"{sn}:{a0}-{a1}")
            if sm < 0.25:
                g["low_similarity"] = True
                low.append(f"{sn}:{a0}")
            segs.append(g)
            per_surah.setdefault(sn, []).extend(range(a0, a1 + 1))
            p0 = e
            sims_all.append(sm)
        per_surah_sim[str(sn)] = round(sum(sims) / len(sims), 2)
        if sn % 10 == 0:
            print(f"  surah {sn}: {len(words)} words, {len(orc)} units, mean similarity {per_surah_sim[str(sn)]}", flush=True)
    miss = T.missing_in_range(per_surah, 1, 114) if not only else {}
    got = sum(len(set(v)) for v in per_surah.values())
    print(f"{SID}: {got} verses in {len(per_surah)} surahs; low similarity {len(low)}; merged oracle groups {len(grouped)}; issues {len(issues)}")
    if a.dry:
        return
    nsegs: list[dict] = []
    for name, lo, hi, label in (("front", 0, m0, "thesis front matter, introduction, description of the manuscript, language"),
                                ("notes", m1, next(i for i in range(m1 + 5, len(L)) if L[i].strip() == "DİZİN"), "Notlar: lexical notes on words of the text"),
                                ("index", next(i for i in range(m1 + 5, len(L)) if L[i].strip() == "DİZİN"), len(L), "Dizin (index of the words of the text), bibliography")):
        for c, (f, e, text) in enumerate(T.chunks(L[lo:hi], 3500)):
            nsegs.append({"seg": f"{NSID}:{name}:{c:04d}", "page": f"line{lo + f}", "head": label, "text": text,
                          "refs": IC.find_refs(text)})
    T.ensure_source(SID, {
        "id": SID, "title": "Eski Anadolu Türkçesi satırarası Kur'ân tercümesi, Topkapı manuscript (Şimşek)",
        "author": "anonymous", "translator": "anonymous", "death_ah": None, "kind": "meal", "tradition": "", "language": "tr",
        "turkic_stage": "Old Anatolian Turkish",
        "edition": "Yaşar Şimşek, Eski Anadolu Türkçesi Satırarası Kur'ân Tercümesi (Topkapı Nüshası, Giriş - Metin - Notlar - Dizin), "
                   "doctoral thesis, Kırıkkale Üniversitesi, Sosyal Bilimler Enstitüsü, Türk Dili ve Edebiyatı Anabilim Dalı, Yeni Türk "
                   "Dili Bilim Dalı, Kırıkkale, January 2017 (supervisor Prof. Dr. Bilgehan A. Gökdağ)",
        "edition_editor": "Yaşar Şimşek", "edition_publisher": "Kırıkkale Üniversitesi (doctoral thesis)", "edition_year": 2017,
        "manuscript": "Topkapı Sarayı Müzesi Koğuşlar Kitaplığı K. 252 (complete translation)",
        "access": "yerel", "locator": "ayah", "urls": [URL], "uploader": "empireofhassaan@hotmail.com", "archive_identifier": IDENT,
        "licence": "scholarly edition; archive.org third-party upload; local research use", "panel": False,
        "cross_witnesses": [ORACLE],
    }, raw)
    T.ensure_source(NSID, {
        "id": NSID, "title": "Şimşek, Topkapı interlinear thesis: introduction, lexical notes, index",
        "author": "Yaşar Şimşek", "kind": "reference", "tradition": "academic", "language": "tr", "turkic_stage": "Old Anatolian Turkish",
        "edition": "same thesis as MEAL-EAT-TOPKAPI-SIMSEK", "access": "yerel", "locator": "section", "urls": [URL],
        "uploader": "empireofhassaan@hotmail.com", "archive_identifier": IDENT,
        "licence": "scholarly edition; archive.org third-party upload; local research use",
        "raw_shared": [f"../{SID}/{raw.relative_to(IC.CORPUS / SID)}"], "panel": False, "files": {},
    }, None)
    ing = {"script": "enrichment/v2/fetch/import_meal_eat_topkapi_simsek.py", "from": {str(raw.relative_to(IC.CORPUS / SID)): IC.C.sha256(raw)},
           "method": "OCR djvu.txt, METİN part; per surah the unnumbered text aligned to the verses of MEAL-ESKIANADOLU (word-level dynamic programme)",
           "edition_range": "surahs 1-114 (complete)", "covered": T.covered(per_surah), "missing": miss,
           "verse_count_mismatch": {}, "mean_similarity_per_surah": per_surah_sim,
           "low_similarity_verses": low, "oracle_merged_groups": grouped, "issues": issues, "counts": T.tally(stats), "dropped_sample": []}
    IC.write(SID, segs, ing, {
        "coverage": f"1-114 ({got}/6236 ayat)",
        "notes": "Complete Old Anatolian interlinear (Topkapı K. 252) from a thesis scan whose OCR keeps NO verse numbers: every surah's "
                 "running text is cut into verses by alignment with MEAL-ESKIANADOLU (Berlin manuscript, close wording); each verse segment "
                 f"carries boundary_inferred and similarity_to_eskianadolu; {len(low)} verses are flagged low_similarity (<0.25, boundary uncertain); "
                 f"{len(grouped)} segments cover verse groups because the oracle itself stores merged groups. The text is OCR as is; leaf markers "
                 "like (3b| and line numbers (4) stay inside it. " + T.NOTE})
    IC.write(NSID, nsegs, {"script": "enrichment/v2/fetch/import_meal_eat_topkapi_simsek.py",
                           "from": {str(raw.relative_to(IC.CORPUS / SID)): IC.C.sha256(raw)}, "counts": T.tally(stats), "issues": []}, {})


if __name__ == "__main__":
    main()
