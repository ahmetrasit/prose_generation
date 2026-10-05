#!/usr/bin/env python3
"""Planning scenarios, not measured Luna billing or OCR accuracy. No model calls."""
import collections
import json
import math
from pathlib import Path

import pypdfium2 as pdfium

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
scope = json.loads((HERE / "scope.json").read_text())
# Output ranges are planning assumptions based on page density/language, not
# extrapolated as accurate text from the corrupted Tesseract output.
RANGES = {"Arabic": (800, 1600), "Arabic/English dictionary": (900, 1700),
          "English": (600, 1000), "Urdu": (1000, 2000), "Turkish/Ottoman spread": (900, 1800)}
groups = collections.defaultdict(lambda: {"pages": 0, "patches_32px": 0})
files = []
for item in scope["files"]:
    group = ("Arabic/English dictionary" if item["source"] == "BADAWI-HALEEM" else
             "Turkish/Ottoman spread" if item["source"] == "TARAMA" else
             "Urdu" if item["languages"][0] == "ur" else
             "English" if item["languages"][0] == "en" else "Arabic")
    pdf = pdfium.PdfDocument(ROOT / item["pdf"])
    patches = []
    for page in pdf:
        width, height = page.get_size()
        width, height = math.ceil(width * 300 / 72), math.ceil(height * 300 / 72)
        scale = min(1, 3500 / max(width, height))
        width, height = max(1, int(width * scale)), max(1, int(height * scale))
        patches.append(math.ceil(width / 32) * math.ceil(height / 32))
        page.close()
    pdf.close()
    assert len(patches) == item["pdf_pages"]
    groups[group]["pages"] += len(patches)
    groups[group]["patches_32px"] += sum(patches)
    files.append({"pdf": item["pdf"], "pages": len(patches), "patches_32px": sum(patches),
                  "minimum_page_patches": min(patches), "maximum_page_patches": max(patches)})

for group, row in groups.items():
    lo, hi = RANGES[group]
    row["assumed_visible_output_per_page"] = [lo, hi]
    row["assumed_visible_output_total"] = [row["pages"] * lo, row["pages"] * hi]
pages = sum(r["pages"] for r in groups.values())
patches = sum(r["patches_32px"] for r in groups.values())
visible = [sum(r["assumed_visible_output_total"][i] for r in groups.values()) for i in [0, 1]]
payload = [math.ceil(patches * multiplier) + pages * 300 for multiplier in [1, 1.2]]
output = {
    "model": "gpt-6-luna", "status": "planning_scenarios_only; no Luna OCR calls",
    "pages": pages,
    "image_geometry": "300-dpi page geometry capped at 3500-pixel longest side; no rendering or crop requests made by this estimator",
    "image_billing_caveat": "Fetched official vision tables do not explicitly list GPT-6 Luna's sizing/multiplier. 32px patches and 1.0–1.2x are sensitivity assumptions, NOT a verified Luna billing rule; measure actual usage in pilot.",
    "raw_image_patches": patches,
    "minimal_call_input_scenario": payload,
    "minimal_call_prompt_assumption": "300 text tokens per page, one direct image-to-text response per page",
    "visible_output_assumed": visible,
    "reasoning_sensitivity": [{"assumed_reasoning_per_page": r, "extra_output_tokens": r * pages,
        "note": "Illustration only; not a low/medium prediction"} for r in [250, 1000, 3000]],
    "native_agent_scenario": {
        "pages_per_fresh_agent": 4, "assumed_harness_tokens": 10000,
        "model_passes": 3, "passes_containing_images": 2,
        "input_tokens_range": [int(2 * payload[0] + 3 * 10000 * math.ceil(pages / 4) + visible[0]),
                               int(2 * payload[1] + 3 * 10000 * math.ceil(pages / 4) + visible[1])],
        "note": "Illustrative view-images, write-files, completion sequence; actual harness/tool rounds/caching must be measured. No parent history assumed; transcription is read back in the completion pass. Reasoning/retries/corrections not included.",
    },
    "prices_usd_per_million": {"standard_input": 0.1, "standard_output": 0.5, "cached_input": 0.01, "cache_write": 0.125},
    "groups": dict(groups), "files": files,
}
(HERE / "luna_estimate.json").write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({k: output[k] for k in ["pages", "raw_image_patches", "minimal_call_input_scenario", "visible_output_assumed", "native_agent_scenario", "groups"]}, indent=2))
