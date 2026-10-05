"""Compare downloaded digital alternatives on the same priority excerpts. No model calls."""
from __future__ import annotations

import hashlib
import json
import re
import sqlite3
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

from measure import HERE, ROOT, alignment, normalize, save, sha


def main():
    inputs = json.loads((HERE / "archive_inputs.json").read_text())
    manifest = json.loads((HERE / "manifest.json").read_text())
    pages = {r["id"]: r for r in manifest["pages"][:6]}
    refs = json.loads((HERE / "priority_references.json").read_text())["references"]
    downloads = []
    for job in inputs["downloads"]:
        path = ROOT / job["path"]
        data = path.read_bytes()
        assert len(data) == job["expected_bytes"] and hashlib.md5(data).hexdigest() == job["expected_md5"]
        downloads.append(job | {"bytes": len(data), "sha256": sha(path), "size_and_md5_verified": True})
    bint_dir = ROOT / "enrichment/corpus/BINTSHATI/raw/ocr-candidates/archive-2026-10-05"
    con = sqlite3.connect(f"file:{bint_dir}/tahirkhan576-1389.db?mode=ro", uri=True)
    db_rows = [{"part": part, "printed_page": page, "record_id": rid, "text": text} for part, page, rid, text in con.execute("select part,page,id,nass from book order by id")]
    (bint_dir / "shamela-pages.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in db_rows))
    native = {(row["part"], row["printed_page"]): row["text"] for row in db_rows}
    archive_pages = {}
    mapping = []
    for source, stem, count in (("BINTSHATI", "bintshati-vol-1", 222), ("BINTSHATI", "bintshati-vol-2", 196), ("KHULI", "khuli-manahij-tajdid-1961", 368)):
        parent = ROOT / f"enrichment/corpus/{source}/raw/ocr-candidates/archive-2026-10-05"
        objects = ET.parse(parent / (stem + ".djvu.xml")).findall(".//OBJECT")
        scan_pages = ET.parse(parent / (stem + ".scandata.xml")).findall(".//page")
        assert len(objects) == len(scan_pages) == count
        archive_pages[stem] = ["\n".join(" ".join(w.text or "" for w in line.findall(".//WORD")) for line in obj.findall(".//LINE")) for obj in objects]
        mapping.append({"stem": stem, "pdf_pages": count, "djvu_objects": len(objects), "scandata_pages": len(scan_pages), "sampled_pdf_page_identity": "Confirmed at the priority samples by matching the text to rendered PDF pages; not every leaf visually checked."})
    excerpt_results = []
    for reference in refs:
        row = pages[reference["page_id"]]
        stem = Path(row["pdf"]).stem
        options = {"archive_ocr_same_scan": archive_pages[stem][row["pdf_page"] - 1]}
        if row["source"] == "BINTSHATI":
            options["shamela_structured_text"] = native[(int(stem[-1]), row["pdf_page"])]
        for name, text in options.items():
            ref, hyp = normalize(reference["text"]).split(), normalize(text).split()
            # These are excerpt comparisons; free prefixes/suffixes exclude headers and neighbouring passages.
            word = alignment(ref, hyp, substring=True)
            matched = hyp[word["start"]:word["end"]]
            char = alignment(" ".join(ref), " ".join(matched))
            excerpt_results.append({"reference": reference["id"], "source": row["source"], "candidate": name,
                                    "word": word, "character": char, "matched_normalized_text": " ".join(matched)})
    summaries = defaultdict(lambda: defaultdict(lambda: {"word_errors": 0, "reference_words": 0, "character_errors": 0, "reference_characters": 0}))
    for row in excerpt_results:
        d = summaries[row["source"]][row["candidate"]]
        for unit, label in (("word", "words"), ("character", "characters")):
            d[unit + "_errors"] += row[unit]["distance"]
            d["reference_" + label] += row[unit]["reference_length"]
    for source in summaries.values():
        for d in source.values():
            d["word_error_rate"] = d["word_errors"] / d["reference_words"]
            d["character_error_rate"] = d["character_errors"] / d["reference_characters"]
    coverage = []
    for part, count in ((1, 222), (2, 196)):
        nums = [r["printed_page"] for r in db_rows if r["part"] == part]
        missing = sorted(set(range(1, count + 1)) - set(nums))
        coverage.append({"part": part, "database_rows": len(nums), "printed_page_min": min(nums), "printed_page_max": max(nums),
                         "unrepresented_pdf_indices_if_identity_mapping": missing,
                         "caution": "Numeric identity is only sample-verified. Missing indices include blanks, front matter and end matter. Vol 1 record 12 is bibliographic metadata, not a page transcription; do not claim complete PDF coverage."})
    catalogs = inputs["openiti_catalogs"]
    result = {"checked_date": "2026-10-05", "downloads": downloads, "archive_page_mapping": mapping,
              "shamela_coverage": coverage, "shamela_text_path": str((bint_dir / "shamela-pages.jsonl").relative_to(ROOT)),
              "shamela_text_sha256": sha(bint_dir / "shamela-pages.jsonl"), "openiti_catalogs": catalogs,
              "priority_excerpt_quality": summaries, "alignments": excerpt_results,
              "limitations": "Same non-random supervisor references as Luna comparison. Unvocalized normalized word/character errors are diagnostic only; extracted text retains original diacritics, and edition/coverage still require reconciliation. No downloaded text has been accepted into raw/ocr/."}
    save("archive_results.json", result)
    print(json.dumps({"quality": summaries, "coverage": coverage, "download_count": len(downloads), "catalogs": catalogs}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
