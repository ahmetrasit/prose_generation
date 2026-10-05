"""Freeze a six-page, one-page-per-agent Sol comparison. No model calls."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    if (HERE / "manifest.json").exists():
        raise SystemExit("Refusing to overwrite the frozen manifest")
    old_path = HERE.parent / "luna-pilot/manifest.json"
    old = json.loads(old_path.read_text())
    pages = []
    for old_page in old["pages"][:6]:
        page = {k: v for k, v in old_page.items() if k not in ("batch", "outputs", "review_notes")}
        assert sha(ROOT / page["image"]) == page["image_sha256"], page["id"]
        stem = Path(page["pdf"]).stem
        output_dir = Path(page["pdf"]).parents[1] / "ocr-candidates/sol-pilot-2026-10-05" / stem
        (ROOT / output_dir).mkdir(parents=True, exist_ok=True)
        page["output"] = str(output_dir / f"p{page['pdf_page']:04d}.txt")
        page["review"] = str(output_dir / f"p{page['pdf_page']:04d}.review.json")
        page["agent_path"] = f"/root/sol_ocr_{page['id'].replace('-', '_')}"
        page["assignment"] = str((HERE / f"{page['id']}.json").relative_to(ROOT))
        assignment = {
            "page_id": page["id"], "source": page["source"], "pdf_page": page["pdf_page"],
            "image": str(ROOT / page["image"]), "image_sha256": page["image_sha256"],
            "output": str(ROOT / page["output"]), "review": str(ROOT / page["review"]),
        }
        (ROOT / page["assignment"]).write_text(json.dumps(assignment, ensure_ascii=False, indent=2) + "\n")
        page["assignment_sha256"] = sha(ROOT / page["assignment"])
        pages.append(page)
    manifest = {
        "created_at": datetime.now(timezone.utc).isoformat(), "model_requested": "gpt-6-sol",
        "effort_override": None, "effort_note": "No override: native agent inherits parent effort; verify actual setting from session logs.",
        "design": "Six previously evaluated priority pages, one image per fresh agent, no inherited history, no competing text. Configuration comparison: model, effort and batch size are not independently controlled.",
        "render": old["render"], "luna_manifest_sha256": sha(old_path),
        "brief_sha256": sha(HERE / "BRIEF.md"),
        "reference_sha256": sha(HERE.parent / "luna-pilot/priority_references.json"),
        "acceptance": "Diagnostic only. Compare frozen 440-word references, meaningful errors, omissions and printed harakat; no automatic production promotion even if normalized excerpt error is zero.",
        "pages": pages,
    }
    (HERE / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"pages": len(pages), "model": manifest["model_requested"], "manifest": str(HERE / "manifest.json")}))


if __name__ == "__main__":
    main()
