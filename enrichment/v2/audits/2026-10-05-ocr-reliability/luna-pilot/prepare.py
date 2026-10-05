"""Freeze the authorized 24-page paired Luna pilot. Makes no model calls."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import pypdfium2 as pdfium

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SELECTION = [
    ("bintshati-vol-1", 50), ("bintshati-vol-1", 100),
    ("bintshati-vol-2", 49), ("bintshati-vol-2", 98),
    ("khuli-manahij-tajdid-1961", 92), ("khuli-manahij-tajdid-1961", 100),
    ("abduh-tafsir-juz-amma", 47), ("abduh-tafsir-juz-amma", 94),
    ("muqatil-wujuh-damin", 77), ("muqatil-wujuh-damin", 154),
    ("ibnkhalawayh-mukhtasar", 61), ("ibnkhalawayh-mukhtasar", 123),
    ("farahi-nizam-book", 158), ("farahi-nizam-book", 316),
    ("badawi-haleem-2008", 274), ("badawi-haleem-2008", 547),
    ("tadabbur-e-quran-vol-3-surah-tawbah-09", 55),
    ("tadabbur-e-quran-vol-1", 100), ("tadabbur-e-quran-vol-2", 158),
    ("tadabbur-e-quran-vol-6", 114), ("tadabbur-e-quran-vol-9", 154),
    ("tarama-vol-1", 100), ("tarama-vol-4", 194), ("tarama-vol-8", 107),
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path):
    return str(path.relative_to(ROOT))


def main():
    if (HERE / "manifest.json").exists():
        raise SystemExit("Frozen manifest exists; do not overwrite a running pilot.")
    scope = json.loads((HERE.parent / "scope.json").read_text())
    by_stem = {Path(row["pdf"]).stem: row for row in scope["files"]}
    records = []
    for number, (stem, page_number) in enumerate(SELECTION, 1):
        source = by_stem[stem]
        pdf_path = ROOT / source["pdf"]
        assert digest(pdf_path) == source["pdf_sha256"]
        candidate_dir = pdf_path.parent.parent / "ocr-candidates" / "luna-pilot-2026-10-05" / stem
        image_path = candidate_dir / "images" / f"p{page_number:04d}.png"
        image_path.parent.mkdir(parents=True, exist_ok=True)
        with pdfium.PdfDocument(str(pdf_path)) as document:
            page = document[page_number - 1]
            width, height = page.get_size()
            scale = min(300 / 72, 3500 / max(width, height))
            bitmap = page.render(scale=scale)
            rendered = bitmap.to_pil()
            rendered.save(image_path)
            dimensions = list(rendered.size)
            bitmap.close()
            page.close()
        outputs = {}
        notes = {}
        for effort in ("low", "medium"):
            out = candidate_dir / effort / f"p{page_number:04d}.txt"
            out.parent.mkdir(parents=True, exist_ok=True)
            outputs[effort] = relative(out)
            notes[effort] = relative(out.with_suffix(".review.json"))
        records.append({
            "id": f"page-{number:02d}", "batch": (number - 1) // 4 + 1,
            "source": source["source"], "pdf": source["pdf"],
            "pdf_sha256": source["pdf_sha256"], "pdf_page": page_number,
            "languages": source["languages"], "image": relative(image_path),
            "image_sha256": digest(image_path), "image_pixels": dimensions,
            "effective_dpi": round(scale * 72, 3),
            "outputs": outputs, "review_notes": notes,
        })
    manifest = {
        "schema_version": 1, "created_at": datetime.now(timezone.utc).isoformat(),
        "model": "gpt-6-luna", "efforts": ["low", "medium"],
        "design": "24 fixed pages, same render and brief; four pages per fresh agent; no inherited history or competing transcript; purposefully stratified, not a random accuracy sample",
        "render": {"engine": "pypdfium2", "target_dpi": 300, "longest_side_cap_px": 3500, "image_detail": "original", "full_page": True},
        "pages": records,
    }
    (HERE / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    for batch in range(1, 7):
        for effort in ("low", "medium"):
            assignment = []
            for row in records:
                if row["batch"] == batch:
                    assignment.append({k: row[k] for k in ("id", "source", "pdf_page", "languages", "image")} | {"output": row["outputs"][effort], "review_notes": row["review_notes"][effort]})
            (HERE / f"batch-{batch:02d}-{effort}.json").write_text(json.dumps(assignment, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"pages": len(records), "transcriptions": len(records) * 2, "batches": 12, "manifest": relative(HERE / "manifest.json")}))


if __name__ == "__main__":
    main()
