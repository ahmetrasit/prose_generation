#!/usr/bin/env python3
"""Bounded extraction pilot; originals and the corpus index are never modified.

Run from the repository root with pypdf, pypdfium2 and Pillow installed.
Text/images are saved beside each source's originals in git-ignored raw/.
The versioned report contains diagnostics, not copyrighted book contents.
No diagnostic in this script certifies OCR or quotation accuracy.
"""
from __future__ import annotations

import hashlib
import importlib.metadata
import json
import logging
import re
import unicodedata
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
MANIFEST = HERE.parent / "2026-10-05-source-downloads/manifest.json"
logging.getLogger("pypdf").setLevel(logging.ERROR)

# One diagnostic body page in each of these files is rendered at 300 dpi.
# These are purposive examples, not a random accuracy benchmark.
RENDER = {
    "bintshati-vol-1", "khuli-manahij-tajdid-1961", "farahi-nizam-book",
    "badawi-haleem-2008", "tadabbur-e-quran-vol-1", "tarama-vol-1",
    "noldeke-gdq-vol-1", "akdemir-son-cagri-kuran", "sinai-key-terms-2023",
    "zammit-comparative-lexical-study", "ibnkhalawayh-mukhtasar", "muqatil-wujuh-damin",
}


def metrics(text: str) -> dict:
    letters = [c for c in text if c.isalpha()]
    return {
        "chars": len(text), "nonspace": sum(not c.isspace() for c in text),
        "letters": len(letters),
        "arabic_letters": sum("ARABIC" in unicodedata.name(c, "") for c in letters),
        "latin_letters": sum("LATIN" in unicodedata.name(c, "") for c in letters),
        "private_use": sum(unicodedata.category(c) == "Co" for c in text),
        "replacement": text.count("\ufffd"),
        "unexpected_controls": sum(unicodedata.category(c) == "Cc" and c not in "\t\n\r\f" for c in text),
        "sha256_utf8": hashlib.sha256(text.encode()).hexdigest(),
    }


def normalized(text: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", text).split())


def check_file(item: dict) -> dict:
    import pypdf
    import pypdfium2 as pdfium

    path = ROOT / item["path"]
    out = path.parents[1] / "ocr-pilot-2026-10-05" / path.stem
    out.mkdir(parents=True, exist_ok=True)
    reader = pypdf.PdfReader(path)
    document = pdfium.PdfDocument(path)
    count = len(document)
    pages = {1, min(10, count), max(1, count // 10), max(1, count // 4),
             max(1, count // 2), max(1, 3 * count // 4), max(1, 9 * count // 10), count}
    if path.stem in RENDER:
        pages.add(min(100, count))
    rows = []
    for number in sorted(pages):
        row = {"pdf_page": number, "engines": {}}
        texts = {}
        for engine in ("pypdf", "pdfium"):
            try:
                if engine == "pypdf":
                    text = reader.pages[number - 1].extract_text() or ""
                else:
                    page = document[number - 1]
                    textpage = page.get_textpage()
                    text = textpage.get_text_bounded()
                    textpage.close()
                    page.close()
                texts[engine] = text
                target = out / f"p{number:04d}.{engine}.txt"
                target.write_text(text, encoding="utf-8")
                row["engines"][engine] = {**metrics(text), "path": str(target.relative_to(ROOT))}
            except Exception as exc:
                row["engines"][engine] = {"error": f"{type(exc).__name__}: {exc}"}
        if len(texts) == 2:
            a, b = (normalized(texts[x]) for x in ("pypdf", "pdfium"))
            ta, tb = set(a.split()), set(b.split())
            row["comparison"] = {
                "normalized_exact_match": a == b,
                "token_set_jaccard": round(len(ta & tb) / len(ta | tb), 4) if ta | tb else None,
                "warning": "Agreement measures extraction agreement, not correctness of the shared PDF text layer.",
            }
        if path.stem in RENDER and number == min(100, count):
            page = document[number - 1]
            bitmap = page.render(scale=300 / 72)
            im = bitmap.to_pil()
            image = out / f"p{number:04d}.300dpi.png"
            im.save(image)
            row["image"] = {"path": str(image.relative_to(ROOT)), "dpi": 300,
                            "width": im.width, "height": im.height,
                            "sha256": hashlib.sha256(image.read_bytes()).hexdigest()}
            im.close()
            bitmap.close()
            page.close()
        rows.append(row)
    document.close()
    return {"source": item["source"], "path": item["path"], "sha256": item["sha256"],
            "pdf_pages": count, "page_count_matches_download": count == item["pages"],
            "samples": rows}


def main() -> None:
    manifest = json.loads(MANIFEST.read_text())
    pdfs = [f for f in manifest["files"] if f["format"] == "pdf"]
    results, failures = [], []
    with ProcessPoolExecutor(max_workers=3) as pool:
        futures = {pool.submit(check_file, f): f for f in pdfs}
        for future in as_completed(futures):
            f = futures[future]
            try:
                result = future.result()
                results.append(result)
                print(f"checked {Path(f['path']).name}: {len(result['samples'])} pages", flush=True)
            except Exception as exc:
                failures.append({"path": f["path"], "error": f"{type(exc).__name__}: {exc}"})
    result = {
        "schema_version": 1, "created_at": datetime.now(timezone.utc).isoformat(),
        "purpose": "Pilot only; neither full extraction nor corpus ingestion nor measured OCR accuracy.",
        "selection": "First/last, page 10, 10/25/50/75/90 percent positions, plus page 100 in 12 purposive examples; all PDF page numbers are one-based.",
        "versions": {m: importlib.metadata.version(m) for m in ("pypdf", "pypdfium2", "Pillow")},
        "summary": {"pdfs": len(results), "sample_pages": sum(len(r["samples"]) for r in results), "failures": len(failures)},
        "files": sorted(results, key=lambda r: r["path"]), "failures": failures,
    }
    (HERE / "samples.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result["summary"]))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
