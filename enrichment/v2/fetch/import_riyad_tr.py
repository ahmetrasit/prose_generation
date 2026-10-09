#!/usr/bin/env python3
"""RIYAD-TR: Riyâzüs-Sâlihîn, Turkish translation of the Diyanet İşleri Başkanlığı edition (tr. Prof. Dr. M. Emin
Özafşar and Prof. Dr. Bünyamin Erul; Ankara, DİB Yayınları, 2015, 3 volumes), from the archive.org item
riyazussalihincild-2 (uploader copy, Tesseract OCR text layer `_djvu.txt`, -l Arabic+tur).

Quality (recorded in source.json): the OCR is partial. Pages with decorative frames or Arabic blocks come out
garbled, many hadith numbers are lost (about 20 percent are readable), and the Arabic is noise. The edition
re-orders and shortens al-Nawawī's chapter titles and prints verses in footnotes («Hûd, 11/3»), so it is NOT
aligned hadith-by-hadith with RIYAD; use it as a searchable Turkish text.

Segments: one per PDF page, RIYAD-TR:v<vol>p<n> (n = page number in the footer «riyaz … .indd n»; text without a
footer after the last mark is kept as v<vol>pEND). `refs` = verses cited as «Name, S/A» (validated); `hadith_nos`
= the numbers of lines that open «N. » on the page (OCR-readable ones only).
  python3 -B enrichment/v2/fetch/import_riyad_tr.py [--fetch] [--dry]
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402

SID = "RIYAD-TR"
ITEM = "riyazussalihincild-2"
RAW = "raw/acquired-2026-10-09"
VOLS = {1: "Riyâzüssâlihîncild1_djvu.txt", 2: "Riyâzüssâlihîncild2_djvu.txt", 3: "Riyâzüssâlihîncild3_djvu.txt"}
FOOT = re.compile(r"^\s*riyaz[_ ]?\w*[_ ]?\w*[_ ]?ebat\s*2015\.indd\s+(\d+)\b.*$", re.M | re.I)
VREF = re.compile(r"([A-ZÂÎÛÇŞĞİÖÜ][\w'’\-âîûÂÎÛ]{1,18}(?: [A-Za-zÂÎÛâîû'’\-]{2,12})?),\s?(\d{1,3})/(\d{1,3})(?:\s?[-–]\s?(\d{1,3}))?")
HNO = re.compile(r"(?m)^(\d{1,4})\. (?=\S)")


def fetch() -> None:
    d = IC.src_dir(SID) / RAW
    d.mkdir(parents=True, exist_ok=True)
    for v, name in VOLS.items():
        dest = d / f"cild{v}_djvu.txt"
        if dest.exists():
            continue
        u = f"https://archive.org/download/{ITEM}/" + urllib.parse.quote(name)
        for _ in range(6):
            if subprocess.run(["curl", "-sfL", "-o", str(dest), u]).returncode == 0:
                break
            time.sleep(8)
        else:
            sys.exit(f"download failed: {u}")
        print("fetched", dest.name)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    d = IC.src_dir(SID)
    if a.fetch:
        fetch()
    if not a.dry and not (d / "source.json").exists():
        d.mkdir(parents=True, exist_ok=True)
        (d / "source.json").write_text(json.dumps({"id": SID}) + "\n", encoding="utf-8")
    segs, rejected, nolines = [], [], 0
    for v in VOLS:
        p = d / RAW / f"cild{v}_djvu.txt"
        if not p.exists():
            sys.exit(f"{p} missing: --fetch")
        t = p.read_text(encoding="utf-8")
        pos = 0
        for m in list(FOOT.finditer(t)) + [None]:
            end = m.start() if m else len(t)
            chunk = t[pos:end].strip()
            label = f"p{m.group(1)}" if m else "pEND"
            pos = m.end() if m else len(t)
            if not chunk:
                nolines += 1
                continue
            refs = []
            for r in VREF.finditer(chunk):
                s, x, y = int(r.group(2)), int(r.group(3)), r.group(4)
                y = int(y) if y else None
                if IC.valid(s, x, y if y and y >= x else None):
                    ref = f"{s}:{x}" + (f"-{y}" if y and y > x else "")
                    if ref not in refs:
                        refs.append(ref)
                else:
                    rejected.append(r.group(0))
            seg = f"{SID}:v{v}{label}"
            if any(g["seg"] == seg for g in segs):  # repeated footer number (OCR): keep, make unique
                seg += f"#{sum(1 for g in segs if g['seg'].startswith(seg)) + 1}"
            segs.append({"seg": seg, "vol": v, "page": int(m.group(1)) if m else None,
                         "hadith_nos": [int(x) for x in HNO.findall(chunk)], "text": chunk, "refs": refs})
    nos = sorted({n for g in segs for n in g["hadith_nos"]})
    print(f"{len(segs)} page segments, {len(nos)} hadith numbers readable (of 1896), refs on "
          f"{sum(1 for g in segs if g['refs'])} pages, rejected verse-like refs {len(rejected)}, empty pages {nolines}")
    if a.dry:
        return
    sha = IC.inputs(SID, [f"cild{v}_djvu" for v in VOLS])
    IC.write(SID, segs, {
        "script": "enrichment/v2/fetch/import_riyad_tr.py", "from": sha,
        "method": "archive.org OCR text layer split at the page footers",
        "page_segments": len(segs), "hadith_numbers_readable": len(nos), "of": 1896,
        "rejected_verse_like_refs": rejected, "empty_pages": nolines,
        "quality": "partial OCR (see notes); not aligned to RIYAD hadith numbers except where the number is readable",
    }, {
        "id": SID, "title": "Riyâzüs-Sâlihîn (Turkish translation, DİB)", "author": "al-Nawawī (tr. M. Emin Özafşar, "
        "Bünyamin Erul)", "death_ah": 676, "kind": "hadith", "tradition": "sunni-hadith", "language": "tr",
        "relay": "RIYAD", "locator": "page", "coverage": "3 volumes, all pages with a readable text layer",
        "edition": "Riyâzüs-Sâlihîn, Diyanet İşleri Başkanlığı Yayınları, Ankara 2015 (3 cilt), tr. Prof. Dr. M. Emin "
                   "Özafşar and Prof. Dr. Bünyamin Erul; foreword Mehmet Görmez; replaces the Hasan Hüsnü Erdem / "
                   "Kıvamüddin Burslan translation. Scan uploaded to archive.org by 'Lami Aydın' (2024-07-30).",
        "urls": [f"https://archive.org/details/{ITEM}"],
        "licence": "copyrighted DİB publication; third-party upload on archive.org, no licence stated; local research "
                   "copy only, not redistributed (segments git-ignored)",
        "notes": "OCR (Tesseract -l Arabic+tur) is partial: garbled on framed/Arabic pages, most hadith numbers lost; "
                 "chapter titles are DİB's own regrouping, not al-Nawawī's; verses are in footnotes («Hûd, 11/3»), "
                 "their translations from the Diyanet meal. Use for Turkish search, not for exact alignment.",
        "acquisition": {"date": "2026-10-09", "state": "raw_downloaded", "ingestion_status": "ingested",
                        "files": len(sha), "source": "archive.org"},
    })


if __name__ == "__main__":
    main()
