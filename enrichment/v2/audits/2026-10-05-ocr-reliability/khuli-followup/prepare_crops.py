"""Freeze a bounded crop rereading experiment; never launches a model."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]

# Deliberately reuse the old reference windows, with surrounding context. These
# are diagnostic selections, not an automatic production crop-selection rule.
# Coordinates use the same-scan DjVu XML raster, top-left origin.
WINDOWS = {
    "page-01": [("middle", [200, 1080, 1670, 1860], ["b1-p50-prose"])],
    "page-02": [("body", [130, 105, 1550, 710], ["b1-p100-full"])],
    "page-03": [
        ("middle", [180, 740, 1480, 1200], ["b2-p49-interpretation"]),
        ("lower", [170, 1890, 1510, 2370], ["b2-p49-attribution"]),
    ],
    "page-04": [("upper", [340, 180, 1700, 880], ["b2-p98-definition"])],
    "page-05": [("upper", [180, 310, 1600, 1620], ["khuli-p92-opening"])],
    "page-06": [
        ("upper", [140, 310, 1580, 815], ["khuli-p100-opening"]),
        ("lower", [140, 2075, 1570, 2640], ["khuli-p100-lower"]),
    ],
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    target = HERE / "crop_manifest.json"
    if target.exists():
        raise SystemExit("Refusing to overwrite frozen crop manifest")
    source_manifest = HERE.parent / "sol-pilot/manifest.json"
    references = HERE.parent / "luna-pilot/priority_references.json"
    alignment_path = ROOT / "enrichment/corpus/KHULI/raw/ocr-candidates/followup-2026-10-05/witness-alignments.json"
    manifest = json.loads(source_manifest.read_text())
    alignments = json.loads(alignment_path.read_text())
    pages = []
    for page in manifest["pages"]:
        raster = ROOT / page["image"]
        assert sha(raster) == page["image_sha256"]
        image = Image.open(raster)
        xml_w, xml_h = alignments[page["id"]]["xml_image_size"]
        outdir = ROOT / f"enrichment/corpus/{page['source']}/raw/ocr-candidates/crop-pilot-2026-10-05/{Path(page['pdf']).stem}"
        outdir.mkdir(parents=True, exist_ok=True)
        crops = []
        for name, box, refs in WINDOWS[page["id"]]:
            pixels = [round(box[0]*image.width/xml_w), round(box[1]*image.height/xml_h),
                      round(box[2]*image.width/xml_w), round(box[3]*image.height/xml_h)]
            crop_path = outdir / f"p{page['pdf_page']:04d}-{name}.png"
            image.crop(pixels).save(crop_path)
            crops.append({"id": f"{page['id']}-{name}", "reference_ids": refs,
                          "image": str(crop_path.relative_to(ROOT)), "image_sha256": sha(crop_path),
                          "xml_box_xyxy": box, "raster_box_xyxy": pixels,
                          "pixels": [pixels[2]-pixels[0], pixels[3]-pixels[1]],
                          "output": str(crop_path.with_suffix('.txt').relative_to(ROOT)),
                          "review": str(crop_path.with_suffix('.review.json').relative_to(ROOT))})
        assignment = {"page_id": page["id"], "source": page["source"], "pdf_page": page["pdf_page"],
                      "crops": [{k:v for k,v in c.items() if k not in ('reference_ids', 'xml_box_xyxy', 'raster_box_xyxy')} for c in crops]}
        assignment_path = HERE / f"crop-{page['id']}.json"
        assignment_path.write_text(json.dumps(assignment, ensure_ascii=False, indent=2) + "\n")
        pages.append({"page_id": page["id"], "source": page["source"], "pdf_page": page["pdf_page"],
                      "source_image": page["image"], "source_image_sha256": sha(raster), "crops": crops,
                      "assignment": str(assignment_path.relative_to(ROOT)), "assignment_sha256": sha(assignment_path),
                      "agent_path": f"/root/ocr_crop_{page['id'].replace('-', '_')}"})
    target.write_text(json.dumps({"date": "2026-10-05", "model_requested": "gpt-6-sol", "effort_override": None,
        "design": "Six fresh isolated agents; eight fixed diagnostic windows from previously evaluated pages, with context. Blind rereading: no witness text, reference or inherited history. No upsampling, enhancement or new scan detail. Not an automatic repair pipeline or independent whole-page accuracy test.",
        "image_detail": "original", "reference_sha256": sha(references), "source_manifest_sha256": sha(source_manifest),
        "brief_sha256": sha(HERE / 'CROP_BRIEF.md'), "pages": pages}, ensure_ascii=False, indent=2) + "\n")
    print(f"Prepared {len(pages)} assignments / {sum(len(p['crops']) for p in pages)} crops")


if __name__ == "__main__":
    main()
