"""Audit Sol/Tesseract disagreement as an error detector; no OCR or model calls."""
from __future__ import annotations

import hashlib
import json
import runpy
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
BASE = HERE.parent
normalize = runpy.run_path(str(BASE / "luna-pilot/measure.py"))["normalize"]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def align(a, b, substring=False):
    """Levenshtein alignment retaining token and gap positions in both witnesses."""
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        dp[i][0] = i
    if not substring:
        dp[0] = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            dp[i][j] = min(dp[i-1][j-1] + (a[i-1] != b[j-1]), dp[i-1][j] + 1, dp[i][j-1] + 1)
    end = min(range(len(b) + 1), key=lambda j: dp[-1][j]) if substring else len(b)
    i, j, steps = len(a), end, []
    while i or (j and not substring):
        if i and j and dp[i][j] == dp[i-1][j-1] + (a[i-1] != b[j-1]):
            steps.append({"op": "equal" if a[i-1] == b[j-1] else "substitute", "a": i-1, "b": j-1,
                          "a_text": a[i-1], "b_text": b[j-1]})
            i, j = i-1, j-1
        elif i and dp[i][j] == dp[i-1][j] + 1:
            steps.append({"op": "delete", "a": i-1, "b": None, "b_gap": j, "a_text": a[i-1], "b_text": ""})
            i -= 1
        else:
            steps.append({"op": "insert", "a": None, "b": j-1, "a_gap": i, "a_text": "", "b_text": b[j-1]})
            j -= 1
    return {"distance": dp[-1][end], "start": j, "end": end, "steps": list(reversed(steps))}


def extract_object(obj):
    tokens, lines = [], []
    for line_index, line in enumerate(obj.findall(".//LINE")):
        words, boxes = [], []
        for word in line.findall(".//WORD"):
            raw = word.text or ""
            xy = [int(v) for v in word.attrib["coords"].split(",")]
            box = [min(xy[0], xy[2]), min(xy[1], xy[3]), max(xy[0], xy[2]), max(xy[1], xy[3])]
            boxes.append(box)
            words.append(raw)
            for normalized in normalize(raw).split():
                tokens.append({"text": normalized, "raw": raw, "line": line_index, "box": box})
        if boxes:
            lines.append({"line": line_index, "text": " ".join(words),
                          "box": [min(b[0] for b in boxes), min(b[1] for b in boxes),
                                  max(b[2] for b in boxes), max(b[3] for b in boxes)]})
    return tokens, lines


def main():
    manifest_path = BASE / "sol-pilot/manifest.json"
    ref_path = BASE / "luna-pilot/priority_references.json"
    manifest, refs = json.loads(manifest_path.read_text()), json.loads(ref_path.read_text())["references"]
    xml_cache, summaries, records, detections = {}, [], {}, []
    for page in manifest["pages"]:
        stem = Path(page["pdf"]).stem
        xml_path = ROOT / f"enrichment/corpus/{page['source']}/raw/ocr-candidates/archive-2026-10-05/{stem}.djvu.xml"
        if xml_path not in xml_cache:
            xml_cache[xml_path] = ET.parse(xml_path).findall(".//OBJECT")
        obj = xml_cache[xml_path][page["pdf_page"]-1]
        tess, lines = extract_object(obj)
        sol = normalize((ROOT / page["output"]).read_text()).split()
        pair = align(sol, [w["text"] for w in tess])
        flags = {s["a"] for s in pair["steps"] if s["op"] != "equal" and s["a"] is not None}
        gaps = {s["a_gap"] for s in pair["steps"] if s["op"] == "insert"}
        alerted_lines = {tess[s["b"]]["line"] for s in pair["steps"] if s["op"] != "equal" and s["b"] is not None}
        # OCR omissions may have no box: use adjacent mapped lines as a fallback.
        for pos, step in enumerate(pair["steps"]):
            if step["op"] == "delete":
                neighbours = [s for s in pair["steps"][max(0,pos-1):pos+2] if s["b"] is not None]
                alerted_lines.update(tess[s["b"]]["line"] for s in neighbours)
        row = {"page_id": page["id"], "source": page["source"], "pdf_page": page["pdf_page"],
               "sol_sha256": sha(ROOT / page["output"]), "tesseract_xml_sha256": sha(xml_path),
               "sol_tokens": len(sol), "tesseract_tokens": len(tess),
               "flagged_sol_tokens": len(flags), "flagged_sol_token_fraction": len(flags)/len(sol),
               "additional_flagged_gaps": len(gaps), "tesseract_lines": len(lines),
               "alerted_lines_with_adjacent_omission_fallback": len(alerted_lines),
               "unvocalized_word_alignment_distance": pair["distance"]}
        summaries.append(row)
        records[page["id"]] = {"sol_tokens": sol, "tesseract_tokens": tess, "lines": lines,
                               "xml_image_size": [int(obj.attrib['width']), int(obj.attrib['height'])],
                               "alignment": pair, "flagged_sol_indices": sorted(flags), "flagged_gap_indices": sorted(gaps),
                               "alerted_line_indices": sorted(alerted_lines)}
        for ref in [r for r in refs if r["page_id"] == page["id"]]:
            mapped = align(normalize(ref["text"]).split(), sol, substring=True)
            findings = []
            for step in mapped["steps"]:
                if step["op"] == "equal":
                    continue
                if step["b"] is not None:
                    strict = step["b"] in flags
                    context = strict or any(g in gaps for g in (step["b"], step["b"]+1))
                else:
                    strict = step["b_gap"] in gaps
                    context = strict or any(t in flags for t in (step["b_gap"]-1, step["b_gap"]))
                findings.append(step | {"direct_disagreement_flag": strict, "flag_with_adjacent_gap_or_token": context})
            correct = [s for s in mapped["steps"] if s["op"] == "equal"]
            detections.append({"reference_id": ref["id"], "page_id": page["id"], "source": page["source"],
                               "reference_words": len(normalize(ref["text"]).split()), "sol_errors": len(findings),
                               "directly_flagged_errors": sum(f["direct_disagreement_flag"] for f in findings),
                               "errors_flagged_with_adjacent_context": sum(f["flag_with_adjacent_gap_or_token"] for f in findings),
                               "correct_sol_tokens": len(correct), "correct_sol_tokens_directly_flagged": sum(s["b"] in flags for s in correct),
                               "errors": findings})
    totals = defaultdict(Counter)
    for d in detections:
        for key in ("reference_words", "sol_errors", "directly_flagged_errors", "errors_flagged_with_adjacent_context",
                    "correct_sol_tokens", "correct_sol_tokens_directly_flagged"):
            totals[d["source"]][key] += d[key]
    for source in totals:
        totals[source]["direct_error_recall"] = totals[source]["directly_flagged_errors"] / totals[source]["sol_errors"]
        totals[source]["correct_token_flag_rate"] = totals[source]["correct_sol_tokens_directly_flagged"] / totals[source]["correct_sol_tokens"]
    # Full recognized text and all coordinates stay in ignored raw data; compact evidence is versioned.
    raw_path = ROOT / "enrichment/corpus/KHULI/raw/ocr-candidates/followup-2026-10-05/witness-alignments.json"
    raw_path.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n")
    result = {"date": "2026-10-05", "method": "Strict normalized word Levenshtein alignment of Sol and existing same-scan Archive Tesseract XML. Reference evaluation is a separate semiglobal alignment. Harakat/punctuation/spelling normalization matches prior pilots.",
              "manifest_sha256": sha(manifest_path), "reference_sha256": sha(ref_path),
              "pages": summaries, "diagnostics": detections, "summary": totals,
              "raw_alignment_path": str(raw_path.relative_to(ROOT)), "raw_alignment_sha256": sha(raw_path),
              "limits": "Six pages comprise four Bint and two Khuli rhetoric pages, not six Khuli pages or a tafsir sample. Error operations/alignments are diagnostic; matching mistakes and joint omissions can escape, and diacritics are excluded. Disagreement proposes review, never automatic replacement. No fresh model/crop re-reading is performed by this script."}
    (HERE / "witness_results.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"pages": summaries, "reference_error_detection": totals}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
