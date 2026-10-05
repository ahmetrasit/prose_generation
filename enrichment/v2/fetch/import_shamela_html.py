#!/usr/bin/env python3
"""A book from a Shamela HTML export (al-Maktaba al-Shāmila «تم إعداد هذا الملف آليا», numbering following the print),
one segment per printed page: the export closes every page with its marker «(vol/page)». User, 2026-10-05 (the
al-Khūlī school: its works with ayah reach, typed text before any OCR).

  python3 -B enrichment/v2/fetch/import_shamela_html.py BINTSHATI-IJAZ raw/acquired-2026-10-05/ijaz-member-1.html

Segments <ID>:p<page> (or v<vol>p<page> for a multi-volume book), text as exported (tags removed, paragraph
breaks kept), `text_status` «Shamela digital edition, not checked against a scan», `refs` = the ayat it quotes
(spelling-blind skeleton match, import_bintshati.quoted) and names («(البقرة 264)»). Text before the first marker
(Shamela's title block) is its own segment <ID>:front. Characters are counted in and out (the ingestion record).
"""
from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402
import import_bintshati as BS  # noqa: E402

STATUS = "Shamela digital edition (typed); not checked against a scan of the print: quote with that caveat"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sid")
    ap.add_argument("html", help="path relative to the source dir")
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    d = IC.src_dir(a.sid)
    raw = (d / a.html).read_text(encoding="utf-8")
    body = re.sub(r"(?is)<(script|style|head)[^>]*>.*?</\1>", "", raw)
    body = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>", "\n", body)
    text = html.unescape(re.sub(r"<[^>]+>", "", body)).replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n", text))
    parts = re.split(r"\((\d{1,2})/(\d{1,4})\)", text)
    vols = {int(parts[i]) for i in range(1, len(parts), 3)}
    multi = len(vols) > 1
    q = BS.quran_index()
    import biqai_intros
    names, _ = biqai_intros.names_and_lengths()
    # chunk k (k = 0 … n-1) is the page that marker k closes
    segs, seen = [], set()
    chunks = [parts[0]] + [parts[i] for i in range(3, len(parts), 3)]
    markers = [(int(parts[i]), int(parts[i + 1])) for i in range(1, len(parts), 3)]
    tail = chunks[len(markers)] if len(chunks) > len(markers) else ""
    for k, (vol, pg) in enumerate(markers):
        chunk = chunks[k].strip()
        # (the first chunk also holds Shamela's title block: kept on that page, as exported)
        loc = f"{a.sid}:" + (f"v{vol}p{pg}" if multi else f"p{pg}")
        if loc in seen:  # a page marker repeated (Shamela splits long pages): a sub-segment
            n = 2
            while f"{loc}#{n}" in seen:
                n += 1
            loc = f"{loc}#{n}"
        seen.add(loc)
        hits = BS.quoted(chunk, q, 0)
        hits += [h for h in BS.named_refs(chunk, names) if h not in hits]
        segs.append({"seg": loc, "printed_page": pg, **({"volume": vol} if multi else {}), "text": chunk,
                     "text_status": STATUS, "refs": [f"{s}:{v}" for s, v in hits]})
    if tail.strip():
        segs.append({"seg": f"{a.sid}:end", "head": "text after the last page marker", "text": tail.strip(),
                     "text_status": STATUS})
    n_in = len(re.sub(r"\s", "", re.sub(r"\(\d{1,2}/\d{1,4}\)", "", text)))
    n_out = sum(len(re.sub(r"\s", "", g["text"])) for g in segs)
    print(f"{a.sid}: {len(markers)} page markers, {len(segs)} segments, volumes {sorted(vols)}; characters in "
          f"{n_in:,} out {n_out:,}; with refs {sum(1 for g in segs if g.get('refs'))}, refs "
          f"{sum(len(g.get('refs') or []) for g in segs)}")
    if n_in != n_out:
        raise SystemExit("character count differs: refusing to write")
    if a.dry:
        return
    IC.write(a.sid, segs, {
        "script": f"enrichment/v2/fetch/import_shamela_html.py {a.sid} {a.html}",
        "from": {a.html: IC.C.sha256(d / a.html)},
        "method": "Shamela HTML export split at its page markers «(vol/page)»; refs from Qurʾān quotations "
                  "(skeleton match) and named references",
        "text_status": STATUS, "characters": n_out,
    })


if __name__ == "__main__":
    main()
