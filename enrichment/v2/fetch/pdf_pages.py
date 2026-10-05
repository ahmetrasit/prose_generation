#!/usr/bin/env python3
"""Every page of a downloaded PDF, as extracted, cached once (Task B, HYBRID_PLAN.md: import the user's downloads).

For each PDF under <source dir>/raw/acquired-*/ this writes <source dir>/raw/pages/<pdf stem>.jsonl, one line per PDF
page: {"pdf": stem, "page": n (1-based PDF page), "chars": n, "text": the text layer exactly as pypdf gives it}.
Nothing is cleaned or dropped here (the importers clean; this cache is their single input, so a page that comes out
empty is visible as "chars": 0). A cache whose PDF has not changed (sha256 recorded in the first line's "sha256")
is kept.

  python3 -B enrichment/v2/fetch/pdf_pages.py ACADEMIC/EQ MEAL-ATAY …   (source directories under enrichment/corpus)
  python3 -B enrichment/v2/fetch/pdf_pages.py --report ACADEMIC/EQ      (pages, empty pages, characters per PDF)
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

V2 = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(V2 / "tools"))
import corpus as C  # noqa: E402

logging.disable(logging.CRITICAL)  # pypdf warns on every odd font; the per-page result records what came out


def pdfs(src: str) -> list[Path]:
    return sorted((C.CORPUS / src).glob("raw/acquired-*/*.pdf"))


def cache_of(pdf: Path) -> Path:
    return pdf.parents[1] / "pages" / f"{pdf.stem}.jsonl"


def extract(pdf_path: str) -> str:
    import pypdf
    pdf = Path(pdf_path)
    out = cache_of(pdf)
    digest = C.sha256(pdf)
    if out.exists():
        first = json.loads(out.open(encoding="utf-8").readline() or "{}")
        if first.get("sha256") == digest:
            return f"{pdf.name}: cached"
    out.parent.mkdir(parents=True, exist_ok=True)
    reader = pypdf.PdfReader(pdf)
    tmp = out.with_suffix(".tmp")
    empty, total = 0, 0
    with tmp.open("w", encoding="utf-8") as f:
        for i, page in enumerate(reader.pages, 1):
            try:
                text, err = page.extract_text() or "", None
            except Exception as e:  # recorded on the page, never skipped
                text, err = "", f"{type(e).__name__}: {e}"
            row = {"pdf": pdf.stem, "page": i, "chars": len(text), "text": text}
            if err:
                row["error"] = err
            if i == 1:
                row["sha256"] = digest
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
            empty += not text.strip()
            total += len(text)
    tmp.replace(out)
    return f"{pdf.name}: {len(reader.pages)} pages, {empty} without text, {total:,} characters"


def report(src: str) -> None:
    for pdf in pdfs(src):
        c = cache_of(pdf)
        if not c.exists():
            print(f"{src} {pdf.name}: not extracted")
            continue
        rows = [json.loads(x) for x in c.open(encoding="utf-8")]
        empty = [r["page"] for r in rows if not r["text"].strip()]
        errs = [r["page"] for r in rows if r.get("error")]
        print(f"{src} {pdf.name}: {len(rows)} pages, {sum(r['chars'] for r in rows):,} chars, "
              f"{len(empty)} without text{(' e.g. ' + str(empty[:12])) if empty else ''}"
              f"{f', {len(errs)} extraction errors {errs[:12]}' if errs else ''}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sources", nargs="+")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--jobs", type=int, default=6)
    a = ap.parse_args()
    if a.report:
        for s in a.sources:
            report(s)
        return
    files = [str(p) for s in a.sources for p in pdfs(s)]
    if not files:
        sys.exit("no PDFs found under raw/acquired-*/")
    with ProcessPoolExecutor(a.jobs) as ex:
        for msg in ex.map(extract, files):
            print(msg, flush=True)


if __name__ == "__main__":
    main()
