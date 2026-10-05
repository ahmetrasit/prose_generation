"""Compare blind crop readings with frozen excerpts; never repairs candidates."""
from __future__ import annotations

import json
import runpy
import unicodedata
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
helpers = runpy.run_path(str(HERE.parent / "sol-pilot/measure.py"))
sha, normalize, alignment, collect_runs, FIELDS = (helpers[k] for k in ("sha", "normalize", "alignment", "collect_runs", "FIELDS"))


def main():
    manifest_path = HERE / "crop_manifest.json"
    manifest = json.loads(manifest_path.read_text())
    reference_path = HERE.parent / "luna-pilot/priority_references.json"
    assert sha(reference_path) == manifest["reference_sha256"]
    assert sha(HERE / "CROP_BRIEF.md") == manifest["brief_sha256"]
    refs = {r["id"]: r for r in json.loads(reference_path.read_text())["references"]}
    baseline_path = HERE.parent / "sol-pilot/results.json"
    baseline = json.loads(baseline_path.read_text())
    prior = {d["id"]: d for d in baseline["diagnostic_alignments"]}
    artifacts, diagnostics = [], []
    for page in manifest["pages"]:
        assert sha(ROOT / page["assignment"]) == page["assignment_sha256"]
        assert sha(ROOT / page["source_image"]) == page["source_image_sha256"]
        for crop in page["crops"]:
            assert sha(ROOT / crop["image"]) == crop["image_sha256"]
            output, review = ROOT / crop["output"], ROOT / crop["review"]
            if not output.exists() or not review.exists():
                raise SystemExit(f"Pending crop: {crop['id']}")
            text = output.read_text(encoding="utf-8")
            note = json.loads(review.read_text())
            assert note["crop_id"] == crop["id"]
            assert isinstance(note["complete"], bool)
            artifacts.append({"crop_id": crop["id"], "source": page["source"], "output_sha256": sha(output),
                              "review_sha256": sha(review), "characters": len(text), "agent_complete": note["complete"],
                              "uncertainty_markers": text.count("[?]"),
                              "combining_marks": sum(unicodedata.category(c) == "Mn" for c in text)})
            for ref_id in crop["reference_ids"]:
                ref, hyp = normalize(refs[ref_id]["text"]).split(), normalize(text).split()
                # The short p100 crop contains all body text and no page label.
                word = alignment(ref, hyp, substring=ref_id != "b1-p100-full")
                matched = hyp[word["start"]:word["end"]]
                diagnostics.append({"reference_id": ref_id, "crop_id": crop["id"], "source": page["source"],
                    "word": word, "character": alignment(" ".join(ref), " ".join(matched)),
                    "matched_normalized_text": " ".join(matched),
                    "prior_full_page_sol_word_errors": prior[ref_id]["word"]["distance"],
                    "prior_full_page_sol_matched_text": prior[ref_id]["matched_normalized_text"]})
    quality = defaultdict(dict)
    for source in ("BINTSHATI", "KHULI"):
        rows = [d for d in diagnostics if d["source"] == source]
        for unit in ("word", "character"):
            errors, count = sum(d[unit]["distance"] for d in rows), sum(d[unit]["reference_length"] for d in rows)
            quality[source][unit] = {"edit_distance": errors, "reference_units": count, "error_rate": errors/count}
        quality[source]["prior_full_page_sol_word_errors"] = sum(d["prior_full_page_sol_word_errors"] for d in rows)
    runs = collect_runs([p | {"id": p["page_id"]} for p in manifest["pages"]])
    if len(runs) != 6 or not all(r["completed_at"] and r["model_verified"] and r["usage"] for r in runs):
        raise SystemExit("Waiting for six completed, verified native sessions")
    totals = {f: sum(r["usage"].get(f, 0) for r in runs) for f in FIELDS}
    totals["non_reasoning_output_tokens"] = totals["output_tokens"] - totals["reasoning_output_tokens"]
    result = {"created_at": datetime.now(timezone.utc).isoformat(), "manifest_sha256": sha(manifest_path),
              "baseline_results_sha256": sha(baseline_path), "reference_sha256": sha(reference_path),
              "quality": quality, "diagnostics": diagnostics, "artifacts": artifacts, "runs": runs, "totals": totals,
              "limits": "Frozen 440-word supervisor reference excerpts, not independent gold. Crops deliberately cover reference windows, with surrounding context; not automatic region selection. Independent fresh model reading, no candidate hints or supervisor correction. Reference normalization hides diacritics/punctuation/spelling distinctions; semiglobal alignment permits free surrounding text. This is a candidate reread, not adjudicated two-witness repair or accepted corpus text. Native session usage excludes parent research/review."}
    (HERE / "crop_results.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"quality": quality, "crops": len(artifacts), "runs": len(runs), "totals": totals}, indent=2))


if __name__ == "__main__":
    main()
