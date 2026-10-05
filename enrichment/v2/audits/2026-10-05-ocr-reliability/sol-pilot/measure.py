"""Validate Sol candidates and compare frozen priority excerpts. No model calls."""
from __future__ import annotations

import hashlib
import json
import re
import runpy
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
BASELINE = HERE.parent / "luna-pilot"
helpers = runpy.run_path(str(BASELINE / "measure.py"))
sha, normalize, alignment, FIELDS = (helpers[k] for k in ("sha", "normalize", "alignment", "FIELDS"))


def collect_runs(pages):
    wanted = {p["agent_path"]: p for p in pages}
    runs = []
    for path in (Path.home() / ".codex/sessions/2026/10/05").glob("*.jsonl"):
        with path.open() as stream:
            try:
                meta = json.loads(next(stream)).get("payload", {})
            except (StopIteration, json.JSONDecodeError):
                continue
            if meta.get("agent_path") not in wanted:
                continue
            contexts, calls, done, errors, usage = [], [], [], [], None
            last_activity = ""
            for line in stream:
                event = json.loads(line)
                payload = event.get("payload", {})
                if event.get("type") == "turn_context":
                    contexts.append({k: payload.get(k) for k in ("model", "effort")})
                    last_activity = event["timestamp"]
                if event.get("type") == "event_msg":
                    if payload.get("type") == "token_count" and payload.get("info"):
                        usage = payload["info"].get("total_token_usage")
                    if payload.get("type") in ("task_complete", "task_completed"):
                        done.append(event["timestamp"])
                    if payload.get("type") in ("error", "warning"):
                        errors.append({"timestamp": event["timestamp"], "payload": payload})
                if event.get("type") == "response_item" and payload.get("type") in ("function_call", "custom_tool_call"):
                    last_activity = event["timestamp"]
                    arg = payload.get("arguments") or payload.get("input") or ""
                    calls.append({
                        "timestamp": event.get("timestamp"), "name": payload.get("name"),
                        "argument_sha256": hashlib.sha256(str(arg).encode()).hexdigest(),
                        "argument_characters": len(arg), "uses_view_image": "view_image" in arg,
                        "forwards_original_detail": bool(re.search(r'image\([^;]*[\"\']original[\"\']', arg)),
                        "head": arg[:200],
                    })
        page = wanted[meta["agent_path"]]
        runs.append({"agent_path": meta["agent_path"], "page_id": page["id"], "session_id": meta["id"],
                     "contexts": contexts, "model_verified": bool(contexts) and all(c["model"] == "gpt-6-sol" for c in contexts),
                     "completed_at": done[-1] if done and done[-1] >= last_activity else None,
                     "usage": usage, "errors": errors, "tool_calls": calls})
    return sorted(runs, key=lambda r: (r["page_id"], r["session_id"]))


def main():
    manifest = json.loads((HERE / "manifest.json").read_text())
    assert sha(HERE / "BRIEF.md") == manifest["brief_sha256"]
    assert sha(BASELINE / "priority_references.json") == manifest["reference_sha256"]
    pages = {p["id"]: p for p in manifest["pages"]}
    references = json.loads((BASELINE / "priority_references.json").read_text())["references"]
    artifacts, texts = [], {}
    for page in pages.values():
        assert sha(ROOT / page["image"]) == page["image_sha256"]
        assert sha(ROOT / page["assignment"]) == page["assignment_sha256"]
        output, review = ROOT / page["output"], ROOT / page["review"]
        row = {"page_id": page["id"], "source": page["source"], "present": output.exists() and review.exists()}
        if row["present"]:
            text = output.read_text(encoding="utf-8")
            texts[page["id"]] = text
            note = json.loads(review.read_text())
            row.update({"sha256": sha(output), "review_sha256": sha(review), "bytes": output.stat().st_size,
                        "characters": len(text), "lines": len(text.splitlines()),
                        "combining_marks": sum(unicodedata.category(c) == "Mn" for c in text),
                        "uncertainty_markers": text.count("[?]"), "agent_complete": note.get("complete"),
                        "verified_blank": note.get("verified_blank"),
                        "blank_contract_valid": (len(text) == 0) == bool(note.get("verified_blank")),
                        "review_page_id_valid": note.get("page_id") == page["id"]})
        artifacts.append(row)
    diagnostics = []
    for reference in references:
        if reference["page_id"] not in texts:
            continue
        original = texts[reference["page_id"]]
        if reference["id"] == "b1-p100-full":
            original = "\n".join(line for line in original.splitlines() if not re.fullmatch(r"\s*\d+\s*", line))
        ref, hyp = normalize(reference["text"]).split(), normalize(original).split()
        word = alignment(ref, hyp, substring=reference["id"] != "b1-p100-full")
        matched = hyp[word["start"]:word["end"]]
        diagnostics.append({"id": reference["id"], "page_id": reference["page_id"],
                            "source": pages[reference["page_id"]]["source"], "word": word,
                            "character": alignment(" ".join(ref), " ".join(matched)),
                            "matched_normalized_text": " ".join(matched)})
    quality = {}
    for source in ("BINTSHATI", "KHULI"):
        selected = [d for d in diagnostics if d["source"] == source]
        quality[source] = {}
        for unit in ("word", "character"):
            errors = sum(d[unit]["distance"] for d in selected)
            denominator = sum(d[unit]["reference_length"] for d in selected)
            quality[source][unit] = {"edit_distance": errors, "reference_units": denominator,
                                     "error_rate": errors / denominator if denominator else None}
    runs = collect_runs(manifest["pages"])
    totals = {f: sum((r["usage"] or {}).get(f, 0) for r in runs) for f in FIELDS}
    totals["non_reasoning_output_tokens"] = totals["output_tokens"] - totals["reasoning_output_tokens"]
    projections = {}
    for source, count in (("BINTSHATI", 418), ("KHULI", 368)):
        source_pages = [p for p in pages.values() if p["source"] == source]
        source_runs = [r for r in runs if pages[r["page_id"]]["source"] == source]
        complete = all(any(r["page_id"] == p["id"] and r["completed_at"] for r in source_runs) for p in source_pages)
        if complete:
            projections[source] = {f: round(sum((r["usage"] or {}).get(f, 0) for r in source_runs) / len(source_pages) * count) for f in FIELDS}
            projections[source].update({"pages": count, "sample_pages": len(source_pages)})
    result = {"created_at": datetime.now(timezone.utc).isoformat(), "manifest_sha256": sha(HERE / "manifest.json"),
              "artifacts": artifacts, "runs": runs, "totals": totals, "quality": quality,
              "diagnostic_alignments": diagnostics, "priority_projections": projections,
              "limits": "Purposive 440-word supervisor references, not independent gold or whole-page/corpus accuracy; harakat/punctuation excluded by normalized metric. Configuration changes include model, effort and page batching. Native usage includes harness/tool replay and retries, excludes supervisor review; cached input is a subset of input and reasoning a subset of output. Projection is a one-pass scenario, not a cost/quality guarantee."}
    (HERE / "results.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"present": sum(a["present"] for a in artifacts), "runs": len(runs),
                      "completed": sum(bool(r["completed_at"]) for r in runs), "quality": quality,
                      "totals": totals, "projections": projections}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
