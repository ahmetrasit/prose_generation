"""Audit paired native-agent artifacts and measure diagnostic excerpts. No model calls."""
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FIELDS = ("input_tokens", "cached_input_tokens", "cache_write_input_tokens", "output_tokens", "reasoning_output_tokens", "total_tokens")


def save(name, value):
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize(text):
    text = unicodedata.normalize("NFC", text).translate(str.maketrans({"ى": "ي", "ی": "ي", "ک": "ك"}))
    text = "".join(str(unicodedata.digit(c)) if c.isdecimal() else c for c in text)
    return " ".join("".join(c if c.isalnum() else " " for c in text if unicodedata.category(c) != "Mn" and c != "ـ").split())


def alignment(ref, hyp, substring=False):
    """Levenshtein alignment; optional free hypothesis prefix/suffix for a reference excerpt."""
    dp = [[0] * (len(hyp) + 1) for _ in range(len(ref) + 1)]
    for i in range(len(ref) + 1):
        dp[i][0] = i
    if not substring:
        dp[0] = list(range(len(hyp) + 1))
    for i in range(1, len(ref) + 1):
        for j in range(1, len(hyp) + 1):
            dp[i][j] = min(dp[i-1][j-1] + (ref[i-1] != hyp[j-1]), dp[i-1][j] + 1, dp[i][j-1] + 1)
    end = min(range(len(hyp) + 1), key=lambda j: dp[-1][j]) if substring else len(hyp)
    i, j = len(ref), end
    edits = Counter()
    while i or (j and not substring):
        if i and j and dp[i][j] == dp[i-1][j-1] + (ref[i-1] != hyp[j-1]):
            edits["equal" if ref[i-1] == hyp[j-1] else "substitutions"] += 1
            i, j = i - 1, j - 1
        elif i and dp[i][j] == dp[i-1][j] + 1:
            edits["deletions"] += 1
            i -= 1
        else:
            edits["insertions"] += 1
            j -= 1
    return {"distance": dp[-1][end], "reference_length": len(ref), "start": j, "end": end, "counts": dict(edits)}


def collect_runs():
    sessions = {}
    for path in (Path.home() / ".codex/sessions").glob("2026/10/05/*.jsonl"):
        with path.open() as stream:
            try:
                meta = json.loads(next(stream)).get("payload", {})
            except (StopIteration, json.JSONDecodeError):
                continue
        match = re.fullmatch(r"/root/ocr_pilot_b(\d{2})_(low|medium)", meta.get("agent_path", ""))
        if match:
            if meta["agent_path"] in sessions:
                raise ValueError("Duplicate native session")
            sessions[meta["agent_path"]] = (path, meta, int(match[1]), match[2])
    runs = []
    for agent_path, (path, meta, batch, effort) in sorted(sessions.items()):
        contexts, calls, done, usage = [], [], [], None
        with path.open() as stream:
            for line in stream:
                event = json.loads(line)
                payload = event.get("payload", {})
                if event.get("type") == "turn_context":
                    contexts.append({k: payload.get(k) for k in ("model", "effort")})
                if event.get("type") == "event_msg":
                    if payload.get("type") == "token_count" and payload.get("info"):
                        usage = payload["info"].get("total_token_usage")
                    if payload.get("type") in ("task_complete", "task_completed"):
                        done.append(event["timestamp"])
                if event.get("type") == "response_item" and payload.get("type") in ("function_call", "custom_tool_call"):
                    arg = payload.get("arguments") or payload.get("input") or ""
                    calls.append({
                        "timestamp": event.get("timestamp"), "name": payload.get("name"),
                        "argument_sha256": hashlib.sha256(str(arg).encode()).hexdigest(),
                        "argument_characters": len(arg), "uses_view_image": "view_image" in arg,
                        "forwards_original_detail": bool(re.search(r'image\([^;]*[\"\']original[\"\']', arg)),
                        "head": arg[:200] if payload.get("name") != "send_message" else "parent progress notification; content omitted",
                    })
        runs.append({"agent_path": agent_path, "session_id": meta["id"], "batch": batch, "effort": effort,
                     "contexts": contexts, "model_effort_verified": bool(contexts) and all(c == {"model": "gpt-6-luna", "effort": effort} for c in contexts),
                     "completed_at": done[-1] if done else None, "usage": usage, "tool_calls": calls,
                     "assignment_sha256": sha(HERE / f"batch-{batch:02d}-{effort}.json")})
    return runs


def main():
    manifest = json.loads((HERE / "manifest.json").read_text())
    pages = {r["id"]: r for r in manifest["pages"]}
    references = json.loads((HERE / "priority_references.json").read_text())
    diagnostics = []
    for reference in references["references"]:
        page = pages[reference["page_id"]]
        ref = normalize(reference["text"]).split()
        efforts = {}
        for effort in ("low", "medium"):
            original = (ROOT / page["outputs"][effort]).read_text()
            # Body-only full-page comparison on the short Bint al-Shati p100.
            if reference["id"] == "b1-p100-full":
                original = "\n".join(line for line in original.splitlines() if not re.fullmatch(r"\s*\d+\s*", line))
            hyp = normalize(original).split()
            word = alignment(ref, hyp, substring=reference["id"] != "b1-p100-full")
            matched = hyp[word["start"]:word["end"]]
            char = alignment(" ".join(ref), " ".join(matched))
            efforts[effort] = {"word": word, "character": char, "matched_normalized_text": " ".join(matched)}
        diagnostics.append({"id": reference["id"], "page_id": reference["page_id"], "source": page["source"], "efforts": efforts})
    quality_summary = {}
    for source in ("BINTSHATI", "KHULI"):
        quality_summary[source] = {}
        for effort in ("low", "medium"):
            selected = [d["efforts"][effort] for d in diagnostics if d["source"] == source]
            summary = {}
            for unit in ("word", "character"):
                errors = sum(s[unit]["distance"] for s in selected)
                denominator = sum(s[unit]["reference_length"] for s in selected)
                summary[unit] = {"edit_distance": errors, "reference_units": denominator, "error_rate": errors / denominator}
            quality_summary[source][effort] = summary
    runs = collect_runs()
    totals = {}
    projections = {}
    for effort in ("low", "medium"):
        subset = [r for r in runs if r["effort"] == effort and r["usage"]]
        totals[effort] = {f: sum(r["usage"].get(f, 0) for r in subset) for f in FIELDS}
        totals[effort]["non_reasoning_output_tokens"] = totals[effort]["output_tokens"] - totals[effort]["reasoning_output_tokens"]
        projections[effort] = {}
        for source, batch, count in (("BINTSHATI", 1, 418), ("KHULI", 2, 368)):
            run = next((r for r in subset if r["batch"] == batch), None)
            if not run:
                continue
            projection = {f: round(run["usage"].get(f, 0) / 4 * count) for f in FIELDS}
            projection["non_reasoning_output_tokens"] = projection["output_tokens"] - projection["reasoning_output_tokens"]
            projection["pages"] = count
            projection["basis"] = "Four-page Bint al-Shati batch; includes one unusually short page" if batch == 1 else "Mixed batch: two Khuli + two Abduh pages. Per-page allocation is a proxy, not source-isolated telemetry."
            projections[effort][source] = projection
        projections[effort]["TOTAL"] = {f: sum(projections[effort][s][f] for s in ("BINTSHATI", "KHULI")) for f in (*FIELDS, "non_reasoning_output_tokens", "pages")}
    artifacts = []
    for page in manifest["pages"]:
        assert sha(ROOT / page["image"]) == page["image_sha256"], page["id"]
        row = {"page_id": page["id"], "outputs": {}}
        for effort in ("low", "medium"):
            output, review = ROOT / page["outputs"][effort], ROOT / page["review_notes"][effort]
            if not output.exists() or not review.exists():
                row["outputs"][effort] = {"present": False}
                continue
            content = output.read_text(encoding="utf-8")
            try:
                note = json.loads(review.read_text())
                review_error = None
            except json.JSONDecodeError as error:
                note = {}
                review_error = str(error)
            row["outputs"][effort] = {"present": True, "sha256": sha(output), "review_sha256": sha(review),
                "bytes": output.stat().st_size, "characters": len(content), "lines": len(content.splitlines()),
                "combining_marks": sum(unicodedata.category(c) == "Mn" for c in content),
                "uncertainty_markers": content.count("[?]"), "agent_complete": note.get("complete"),
                "verified_blank": note.get("verified_blank"), "blank_contract_valid": (len(content) == 0) == bool(note.get("verified_blank")),
                "review_page_id_valid": note.get("page_id") == page["id"], "review_json_error": review_error}
        artifacts.append(row)
    result = {"created_at": datetime.now(timezone.utc).isoformat(), "brief_sha256": sha(HERE / "BRIEF.md"),
              "manifest_sha256": sha(HERE / "manifest.json"), "runs": runs, "totals": totals,
              "priority_projections": projections, "priority_quality": quality_summary,
              "quality_limit": "Diagnostic excerpt edit rates with permissive normalization and best-substring alignment; supervisor image readings, not independent gold, not whole-page/corpus accuracy. Harakat and punctuation excluded. Missing whole excerpts can align to unrelated text: inspect matched spans.",
              "diagnostic_alignments": diagnostics, "artifacts": artifacts}
    save("results.json", result)
    print(json.dumps({"runs": len(runs), "completed": sum(bool(r["completed_at"]) for r in runs), "totals": totals, "priority_projections": projections, "priority_quality": quality_summary}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
