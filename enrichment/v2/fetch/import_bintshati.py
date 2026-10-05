#!/usr/bin/env python3
"""BINTSHATI: ʿĀʾisha ʿAbd al-Raḥmān (Bint al-Shāṭiʾ), al-Tafsīr al-bayānī li-l-Qurʾān al-karīm, 2 vols (Dār
al-Maʿārif, 7th ed.), from the Shamela export the OCR audit found (archive.org tahirkhan576-1389, 373 records, «the
book's numbering follows the print»; enrichment/v2/audits/2026-10-05-ocr-reliability/luna-pilot/SOURCE_ALTERNATIVES.md).
User, 2026-10-05: "start with bint" (this text first; the scans stay the authority).

Text status: the Shamela text is a typed digital edition, not OCR, and it is NOT yet checked against the scans held
locally (raw/acquired-2026-10-05/bintshati-vol-{1,2}.pdf): typos occur («الغطلء» for «الغطاء»), verse delimiters and
vocalisation may differ from the print. Every segment says so (`text_status`); quote only after checking the page
image (`pdf_page` names it).

Segments:
  BINTSHATI:v<vol>p<printed page>   one per Shamela record (= printed page), `pdf_page` = the scan page it was matched
                                    to (character 3-grams against the archive's OCR of that page), tied to the
                                    chapter's surah: the verses of that surah quoted on the page (a page quoting
                                    none continues the previous page's verse; a chapter's opening pages before its
                                    first quotation: the whole surah); `refs` = every ayah quoted (any surah)
  BINTSHATI:v<vol>pdf<n>            a scan page no record covers (prefaces of other editions, title pages, blanks):
                                    the archive's Tesseract OCR of it, `text_status` «ocr draft», or an empty page
                                    marked as such (counted; to be confirmed on the image)

  python3 -B enrichment/v2/fetch/import_bintshati.py [--dry]
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402

C = IC.C
SID = "BINTSHATI"
CAND = "raw/ocr-candidates/archive-2026-10-05"
DB = "tahirkhan576-1389.db"
SURAHS = {"الضحى": 93, "الشرح": 94, "الزلزلة": 99, "العاديات": 100, "النازعات": 79, "البلد": 90, "التكاثر": 102,
          "العلق": 96, "القلم": 68, "العصر": 103, "الليل": 92, "الفجر": 89, "الهمزة": 104, "الماعون": 107}
STATUS_TYPED = ("Shamela digital edition (typed, not OCR); not yet checked against the scan: quote only after "
                "checking pdf_page")
STATUS_OCR = "ocr draft (archive Tesseract 5.3.0 of the scan page); unverified: do not quote"


def grams(t: str) -> set[str]:
    t = re.sub(r"[^ء-ي]", "", C.norm(t))
    return {t[i:i + 3] for i in range(len(t) - 2)}


def dice(a: set, b: set) -> float:
    return 2 * len(a & b) / (len(a) + len(b)) if a and b else 0.0


def djvu_pages(path: Path) -> list[str]:
    """The OCR text of each scan page (lines of words), in PDF page order."""
    out = []
    for _, obj in ET.iterparse(path, events=("end",)):
        if obj.tag != "OBJECT":
            continue
        paras = []
        for para in obj.iter("PARAGRAPH"):
            lines = [" ".join(w.text or "" for w in line.iter("WORD")) for line in para.iter("LINE")]
            paras.append("\n".join(x for x in lines if x.strip()))
        out.append("\n\n".join(p for p in paras if p.strip()))
        obj.clear()
    return out


def skel(t: str) -> str:
    """A spelling-blind skeleton for matching imlāʾī quotations with the Uthmani text: normalised, then without
    alifs, hamzas and their seats («اليل»/«الليل», «الضحي»), word breaks kept."""
    t = C.norm(t)
    t = re.sub(r"[اأإآٱءئؤ]", "", t).replace("ى", "ي").replace("ة", "ه")
    t = re.sub(r"(.)\1", r"\1", t)  # doubled letters (shadda written out or not)
    return " ".join(w for w in t.split() if w)


def quran_index() -> dict[int, dict[int, str]]:
    con = sqlite3.connect(C.INDEX)
    q: dict[int, dict[int, str]] = {}
    for s, a, txt in con.execute("SELECT s, a, text FROM seg WHERE src='QURAN'"):
        q.setdefault(s, {})[a] = " " + skel(txt) + " "
    return q


def quoted(text: str, q: dict, prefer: int) -> list[tuple[int, int]]:
    """The ayat the page quotes: Qurʾānic spans in braces («{…}», the opening sometimes typed as «"»), cut at their
    verse markers «(167)», each piece of 3+ words found inside an ayah (the chapter's surah tried first)."""
    out: list[tuple[int, int]] = []
    spans = [(m.group(1), False) for m in re.finditer(r"[{\"«]([^{}\"«»]{6,900})}", text)]
    # lecture transcripts quote in parentheses «(فسنيسره لليسرى)»: taken at 4+ words (3+ in the chapter's surah),
    # so that an ordinary aside cannot pass for a verse
    spans += [(m.group(1), True) for m in re.finditer(r"\(([^(){}]{8,900}?)(?:\(\s*[\d٠-٩]{1,3}\s*\)[^(){}]{0,40})?\)", text)]
    for span, paren in spans:
        for piece in re.split(r"\(\s*[\d٠-٩]{1,3}\s*\)", span):
            pn = skel(piece)
            if not pn or (paren and len(pn.split()) < 3):
                continue
            hit = None
            # a short piece only as a whole verse of the chapter's surah («والضحى»); 3+ words anywhere
            if len(pn.split()) < 3:
                # a short piece: a whole verse of the chapter's surah («والضحى»), or a part of exactly one of its
                # verses («الحمد لله» in al-Fātiḥa)
                if prefer in q:
                    hit = next(((prefer, a) for a, ay in q[prefer].items() if ay.strip() == pn), None)
                    if hit is None:
                        inside = [a for a, ay in q[prefer].items() if " " + pn + " " in ay]
                        hit = (prefer, inside[0]) if len(inside) == 1 else None
            else:
                order = ([prefer] if prefer in q else []) + ([] if paren and len(pn.split()) < 4 else
                                                              [k for k in q if k != prefer])
                for s in order:
                    for a, ay in q[s].items():
                        if " " + pn + " " in ay or (len(pn.split()) >= 4 and pn in ay):
                            hit = (s, a)
                            break
                    if hit:
                        break
            if hit and hit not in out:
                out.append(hit)
    return out


def named_refs(text: str, names: dict[str, int]) -> list[tuple[int, int]]:
    """«(البقرة 264)», «(النساء 38، 142)», «(آل عمران: 7)», «[الجاثية: 12]»: a surah named and its verse numbers."""
    out: list[tuple[int, int]] = []
    # «(البقرة 264)» (Bint al-Shāṭiʾ's print) and «[الجاثية: 12]» (Shamela's own references)
    for m in re.finditer(r"[(\[]([^()\[\]\d٠-٩]{2,20}?)\s*:?\s*([\d٠-٩]{1,3}(?:\s*[،,-]\s*[\d٠-٩]{1,3})*)[)\]]", text):
        name = re.sub("[أإآ]", "ا", m.group(1).strip())
        name = re.sub(r"^سورة\s+", "", name)
        s = names.get(name) or names.get("ال" + name)
        if not s:
            continue
        nums = [int(x.translate(str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789"))) for x in re.findall(r"[\d٠-٩]{1,3}", m.group(2))]
        for a in nums:
            if IC.valid(s, a) and (s, a) not in out:
                out.append((s, a))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--dump")
    a = ap.parse_args()
    d = IC.src_dir(SID)
    counts = IC.ayah_counts()
    stats: Counter = Counter()
    issues: list[str] = []
    con = sqlite3.connect(d / CAND / DB)
    recs = con.execute("SELECT id, CAST(part AS INT), CAST(page AS INT), nass FROM book ORDER BY id").fetchall()
    titles = con.execute("SELECT id, tit FROM title ORDER BY id").fetchall()
    scans = {v: djvu_pages(d / CAND / f"bintshati-vol-{v}.djvu.xml") for v in (1, 2)}
    scan_grams = {v: [grams(t) for t in scans[v]] for v in (1, 2)}
    q = quran_index()
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import biqai_intros  # the surah names as Biqāʿī's headings spell them (alef/hamza folded)
    names, _ = biqai_intros.names_and_lengths()
    names = {**names, **{k: v for k, v in SURAHS.items()}, "ال عمران": 3, "آل عمران": 3}
    # chapter (surah) of each record
    chapter_at = []
    for tid, tit in titles:
        m = re.match(r"سورة\s+(\S+)", tit.strip())
        chapter_at.append((tid, SURAHS.get(m.group(1)) if m else None, tit.strip()))
    segs, matched = [], {1: {}, 2: {}}
    last_verse: dict[int, int] = {}
    for rid, vol, pg, text in recs:
        text = text.replace("\r", "\n").strip()
        chap = [c for c in chapter_at if c[0] <= rid]
        surah = chap[-1][1] if chap else None
        # the scan page: PDF page = printed page in both volumes (checked: every record's best 3-gram match over the
        # whole volume is its own printed page, ~0.8 against ~0.33 for the next best, except the two noted below);
        # a record whose own page is not its best match is flagged, not moved
        g = grams(text)
        own = pg - 1
        sc = dice(g, scan_grams[vol][own]) if 0 <= own < len(scans[vol]) else 0.0
        best = max(range(len(scans[vol])), key=lambda i: dice(g, scan_grams[vol][i]))
        seg = {"seg": f"{SID}:v{vol}p{pg}", "printed_page": pg, "volume": vol, "head": chap[-1][2] if chap else
               "front matter", "text": text, "text_status": STATUS_TYPED, "shamela_record": rid,
               "pdf_page": pg, "scan_match": round(sc, 3)}
        if best != own and sc < 0.3:
            stats["records that are not their page's text (Shamela metadata): the scan page also imported"] += 1
        else:
            matched[vol][pg] = seg["seg"]
        if best != own:
            seg["scan_match_note"] = f"its best match is scan page {best + 1} (similarity {dice(g, scan_grams[vol][best]):.2f})"
            issues.append(f"v{vol}p{pg} (record {rid}): own scan page similarity {sc:.2f}; best is page {best + 1}")
            stats["records whose own scan page is not their best match (flagged)"] += 1
        else:
            stats["records confirmed on their scan page"] += 1
        hits = quoted(text, q, surah or 0)
        hits += [h for h in named_refs(text, names) if h not in hits]
        seg["refs"] = [f"{s}:{v}" for s, v in hits]
        if surah:
            own = sorted(v for s, v in hits if s == surah)
            if own and len(set(own)) >= max(3, 0.6 * counts[surah]):  # the surah's whole text printed
                seg.update({"s": surah, "a": 1, "a_end": counts[surah]})
                stats["pages printing the surah's text, tied to the whole surah"] += 1
            elif own:
                lo, hi = own[0], own[-1]
                if surah in last_verse and last_verse[surah] < lo:
                    lo = last_verse[surah]  # the page begins on the verse the previous page was on
                seg.update({"s": surah, "a": lo, "a_end": hi})
                last_verse[surah] = hi
                stats["pages tied to the verses they quote"] += 1
            elif surah in last_verse:
                v = last_verse[surah]
                seg.update({"s": surah, "a": v, "a_end": v})
                stats["pages tied to the previous page's verse (no quotation)"] += 1
            else:
                seg.update({"s": surah, "a": 1, "a_end": counts[surah]})
                stats["chapter opening pages tied to the whole surah"] += 1
        else:
            stats["pages outside the surah chapters (prefaces)"] += 1
        segs.append(seg)
    # scan pages no record covers
    for vol in (1, 2):
        for i, t in enumerate(scans[vol], 1):
            if i in matched[vol]:
                continue
            t = t.strip()
            g = {"seg": f"{SID}:v{vol}pdf{i}", "volume": vol, "pdf_page": i, "head": "scan page without a Shamela record",
                 "text": t, "text_status": STATUS_OCR if t else "the archive OCR found no text: blank or image page "
                 "(confirm on the scan)"}
            stats["scan pages without a record: OCR draft" if t else "scan pages without a record: no OCR text"] += 1
            segs.append(g)
    order = {s["seg"]: k for k, s in enumerate(segs)}
    segs.sort(key=lambda s: (s["volume"], s.get("pdf_page") or 10_000, order[s["seg"]]))
    print(f"records {len(recs)}; segments {len(segs)}; {dict(stats)}")
    print(f"issues {len(issues)} {issues[:8]}")
    low = sorted((s["scan_match"], s["seg"]) for s in segs if "scan_match" in s)[:6]
    print("weakest scan matches:", low)
    if a.dry:
        if a.dump:
            Path(a.dump).write_text("".join(json.dumps(g, ensure_ascii=False) + "\n" for g in segs))
        return
    old = json.loads((d / "source.json").read_text())
    IC.write(SID, segs, {
        "script": "enrichment/v2/fetch/import_bintshati.py",
        "from": {f"{CAND}/{DB}": C.sha256(d / CAND / DB),
                 **{f"{CAND}/bintshati-vol-{v}.djvu.xml": C.sha256(d / CAND / f"bintshati-vol-{v}.djvu.xml")
                    for v in (1, 2)}},
        "method": "Shamela records (printed pages) as text; each matched to its scan page by character 3-grams "
                  "against the archive OCR; scan pages without a record imported from that OCR as drafts; ties "
                  "from the Qurʾān quotations",
        "counts": dict(stats), "issues": issues,
        "text_status": "typed digital edition, unverified against the scans; OCR drafts for uncovered pages",
    }, {"edition": "Dār al-Maʿārif, Cairo, 7th ed., 2 vols (Shamela export, numbering follows the print); scans "
                   "of the same work held locally (archive.org elshandawily0546/0547)",
        "coverage": "14 surahs: 93, 94, 99, 100, 79, 90, 102 (vol 1); 96, 68, 103, 92, 89, 104, 107 (vol 2)",
        "locator": "page",
        "licence": "in copyright (author d. 1998); local research copy only (user, 2026-10-05: licence is no "
                   "barrier for local analysis)",
        "notes": "Ingested 2026-10-05 (fetch/import_bintshati.py) from the Shamela export; NOT yet checked against "
                 "the scans: every segment carries text_status and pdf_page. OCR pilots (Luna, Sol) did not reach "
                 "preservation quality: enrichment/v2/audits/2026-10-05-ocr-reliability/. Pointer note before "
                 "ingestion: " + (old.get("notes") or "")})


if __name__ == "__main__":
    main()
