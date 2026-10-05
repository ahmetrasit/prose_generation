#!/usr/bin/env python3
"""Bookkeeping for native discovery agents. Never invokes a model.

Use discover.py without --go to prepare packages. Then start a fresh job here,
spawn its printed task with the native Agent tool, snapshot after turn one,
send followup.txt in the same session, inspect audit, and finish after turn two.
"""
import argparse
import hashlib
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path

import discover as D
import check_discovery as C


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def consolidate(d, surah, verses):
    """Preserve raw proposals; append each new ref once without regrading."""
    first = (d / "turn1.list.tsv").read_bytes()
    if (d / "list.tsv").read_bytes() != first:
        raise ValueError("Agent changed list.tsv during the separate-proposals follow-up")
    initial, bad = D.parse_rows(d / "turn1.list.tsv", surah, verses)
    proposed, extra_bad = D.parse_rows(d / "followup.tsv", surah, verses)
    if bad or extra_bad or len({r['ref'] for r in initial}) != len(initial):
        raise ValueError(f"Invalid discovery input: {bad + extra_bad}")
    if first and not first.endswith(b"\n"):
        raise ValueError("First-turn TSV must end with newline before consolidation")
    seen = {r['ref']: {'phase': 1, 'line': r['line']} for r in initial}
    raw = (d / "followup.tsv").read_bytes()
    raw_lines = raw.splitlines(keepends=True)
    additions, repeated = [], []
    for row in proposed:
        if row['ref'] in seen:
            repeated.append({**row, 'kept': seen[row['ref']]})
            continue
        seen[row['ref']] = {'phase': 2, 'line': row['line']}
        line = raw_lines[row['line'] - 1]
        additions.append(line if line.endswith(b"\n") else line + b"\n")
    final = first + b"".join(additions)
    report = {'mode': 'separate-proposals-v1', 'raw_proposal_rows': len(proposed),
              'unique_additions': len(additions), 'repeated_proposals': repeated,
              'turn1_sha256': hashlib.sha256(first).hexdigest(),
              'followup_sha256': hashlib.sha256(raw).hexdigest(),
              'list_sha256': hashlib.sha256(final).hexdigest(),
              'policy': 'First occurrence retained; no existing row or grade changed. Raw followup.tsv preserved.'}
    save(d / "consolidation.json", report)
    (d / "list.tsv").write_bytes(final)
    return report


def session_for(d):
    if (d / "session.json").exists():
        return json.loads((d / "session.json").read_text())
    start = json.loads((d / "started.json").read_text())
    matches = []
    for path in Path.home().joinpath(".codex/sessions").glob("*/*/*/*.jsonl"):
        with path.open() as stream:
            try:
                meta = json.loads(next(stream)).get("payload", {})
            except (StopIteration, json.JSONDecodeError):
                continue
        if meta.get("agent_path") == start["agent_path"]:
            matches.append({"agent_path": start["agent_path"], "agent_id": meta["id"], "transcript": str(path)})
    if len(matches) != 1:
        raise ValueError(f"Expected one native session for {start['agent_path']}, found {len(matches)}")
    save(d / "session.json", matches[0])
    return matches[0]


def events_for(d):
    session = session_for(d)
    events = [json.loads(line) for line in Path(session["transcript"]).read_text().splitlines()]
    done = [e for e in events if e.get("type") == "event_msg" and
            e.get("payload", {}).get("type") in ("task_complete", "task_completed")]
    contexts = [e["payload"] for e in events if e.get("type") == "turn_context"]
    usage = [e["payload"]["info"]["total_token_usage"] for e in events if e.get("type") == "event_msg" and
             e.get("payload", {}).get("type") == "token_count" and e["payload"].get("info")]
    return session, events, done, contexts, usage[-1] if usage else None


def tool_audit(events, first_done):
    outputs = {e["payload"].get("call_id"): e["payload"].get("output") for e in events
               if e.get("type") == "response_item" and e.get("payload", {}).get("type") in
               ("function_call_output", "custom_tool_call_output")}
    calls, diagnostics = [], []
    for e in events:
        p = e.get("payload", {})
        if e.get("type") != "response_item" or p.get("type") not in ("function_call", "custom_tool_call"):
            continue
        out = outputs.get(p.get("call_id"))
        calls.append({"timestamp": e["timestamp"], "phase": 1 if e["timestamp"] < first_done else 2,
                      "name": p.get("name"), "call_id": p.get("call_id"),
                      "arguments": p.get("arguments") or p.get("input") or "", "output": out})
        if isinstance(out, list):
            out_text = "\n".join(x.get("text", "") for x in out if isinstance(x, dict))
        else:
            out_text = str(out or "")
        for line in out_text.splitlines():
            if re.search(r"(?:^Traceback|^\w*Error:|^Script (?:failed|error)|apply_patch verification failed|Failed to find expected lines|No such file or directory|^WARNING:|^BLOCKED:|^duplicate|^bad[_ -](?:field|strength|basis|reference|ref))", line):
                diagnostics.append({"call_id": p.get("call_id"), "message": line[:700]})
    return calls, diagnostics


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("phase", choices=["start", "snapshot", "audit", "finish"])
    ap.add_argument("--surah", type=int, required=True)
    ap.add_argument("--section", type=int, required=True)
    ap.add_argument("--model", choices=D.MODELS, required=True)
    ap.add_argument("--run-tag", required=True)
    ap.add_argument("--task", help="native agent task name for start")
    ap.add_argument("--reviewed", action="store_true", help="orchestrator has reviewed tool_calls.json")
    a = ap.parse_args()
    d = D.discovery_dir(a.surah, a.run_tag) / f"sec{a.section}" / a.model
    if a.phase == "start":
        if D.V.blocked(d):
            raise SystemExit(f"BLOCKED: {d} already started; never reuse a call directory")
        if not a.task:
            ap.error("start requires --task")
        for name in ("prompt.md", "package.md"):
            if not (d / name).is_file():
                raise SystemExit(f"Missing prepared {d / name}")
        prompt_hash = hashlib.sha256((d / "prompt.md").read_bytes()).hexdigest()
        _, source, _ = D.B.surah_inputs(a.surah)
        save(d / "started.json", {"source_file": str(source), "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),"started": datetime.now().astimezone().isoformat(), "model": D.MODELS[a.model],
             "effort": D.EFFORT, "runner": "agent", "agent_path": "/root/" + a.task,
             "followup_mode": "separate-proposals-v1",
             "run_tag": a.run_tag, "surah": a.surah, "section": a.section, "prompt_sha256": prompt_hash,
             "package_sha256": hashlib.sha256((d / "package.md").read_bytes()).hexdigest()})
        message = (f"Read {d / 'prompt.md'} fully, then follow it using its package.md. "
                   "Work independently from that package and your own Quran knowledge. "
                   "Read only your own prompt.md and package.md. Once you have created your list.tsv, "
                   "you may read it for formatting checks during this first turn. Do not try to read it before creating it. "
                   "Write only your own list.tsv. No web, retrieval, other agents, other run files, or scripts for "
                   "discovering candidates. Do not call models or read repository instructions beyond the supplied inputs. Tools may read the permitted inputs, write your TSV, and check its format. "
                   "Return a short completion message after saving. A follow-up will arrive in this same session; "
                   "do not anticipate it.")
        (d / "spawn.md").write_text(message + "\n")
        (d / "followup.txt").write_text(D.FOLLOWUP_SEPARATE.format(output=d / "followup.tsv") + "\n")
        print(message)
        return
    session, events, done, contexts, usage = events_for(d)
    rows, bad = D.parse_rows(d / "list.tsv", a.surah, D.M.verses())
    if a.phase == "snapshot":
        if (d / "turn1.json").exists():
            raise SystemExit("BLOCKED: first turn already snapshotted")
        if len(done) != 1 or not (d / "list.tsv").exists():
            raise SystemExit(f"Expected one completed turn and an output file; completions={len(done)}")
        data = (d / "list.tsv").read_bytes()
        if bad or len({r['ref'] for r in rows}) != len(rows) or (data and not data.endswith(b"\n")):
            raise SystemExit(f"Invalid first-turn TSV; no follow-up permitted: {bad}")
        (d / "turn1.list.tsv").write_bytes(data)
        save(d / "turn1.json", {**session, "rows": len(rows), "lines": len(data.splitlines()),
             "bad_rows": bad, "usage": usage, "completed_at": done[0]["timestamp"]})
        print(json.dumps({"section": a.section, "model": a.model, "rows": len(rows), "bad_rows": bad}))
        return
    first = json.loads((d / "turn1.json").read_text())
    calls, diagnostics = tool_audit(events, first["completed_at"])
    save(d / "tool_calls.json", calls)
    if a.phase == "audit":
        print(json.dumps({"job": str(d), "completions": len(done), "contexts": [
            {"model": c.get("model"), "effort": c.get("effort")} for c in contexts], "diagnostics": diagnostics}))
        for c in calls:
            arg = c["arguments"] if isinstance(c["arguments"], str) else json.dumps(c["arguments"])
            print(json.dumps({"phase": c["phase"], "call_id": c["call_id"], "name": c["name"],
                              "head": arg[:500], "tail": arg[-900:] if len(arg) > 500 else ""}, ensure_ascii=False))
        return
    if not a.reviewed:
        ap.error("finish requires --reviewed after inspecting the tool audit")
    if (d / "run.log.json").exists():
        raise SystemExit("BLOCKED: already finished")
    start = json.loads((d / "started.json").read_text())
    consolidation, consolidation_error = None, None
    if start.get("followup_mode") == "separate-proposals-v1":
        if len(done) != 2:
            raise SystemExit("Expected two completed turns before consolidation")
        try:
            consolidation = consolidate(d, a.surah, D.M.verses())
        except (ValueError, FileNotFoundError) as exc:
            consolidation_error = str(exc)
        rows, bad = D.parse_rows(d / "list.tsv", a.surah, D.M.verses())
    final = (d / "list.tsv").read_bytes()
    prefix_ok = final.startswith((d / "turn1.list.tsv").read_bytes())
    duplicates = {r: n for r, n in Counter(r["ref"] for r in rows).items() if n > 1}
    model_ok = bool(contexts) and all(c.get("model") == D.MODELS[a.model] and c.get("effort") == D.EFFORT for c in contexts)
    inputs_ok = all(hashlib.sha256((d / filename).read_bytes()).hexdigest() == start[field]
                    for filename, field in (("prompt.md", "prompt_sha256"), ("package.md", "package_sha256")))
    fatal = bool(consolidation_error or bad or duplicates or len(done) != 2 or not prefix_ok or not model_ok or not inputs_ok)
    meta = next(e["payload"] for e in events if e.get("type") == "session_meta")
    parent_id = meta.get("parent_thread_id") or meta.get("source", {}).get("subagent", {}).get("thread_spawn", {}).get("parent_thread_id")
    proof = []
    for parent in Path.home().joinpath(".codex/sessions").glob(f"*/*/*/*{parent_id}.jsonl") if parent_id else []:
        for line in parent.read_text().splitlines():
            event = json.loads(line)
            payload = event.get("payload", {})
            if event.get("type") != "response_item" or payload.get("name") != "followup_task":
                continue
            args = json.loads(payload.get("arguments") or "{}")
            if args.get("target") not in (session["agent_path"], session["agent_path"].split("/")[-1]):
                continue
            message = args.get("message", "")
            proof.append({"call_id": payload.get("call_id"), "timestamp": event.get("timestamp"),
                          "target": args["target"], "parent_transcript": str(parent),
                          "message_encrypted": message.startswith("gAAAAA"),
                          "plaintext_matches": message == (d / "followup.txt").read_text().strip()})
    protocol_findings = [] if len(proof) == 1 else [f"Expected one follow-up delivery record, found {len(proof)}"]
    if any(not p['message_encrypted'] and not p['plaintext_matches'] for p in proof):
        protocol_findings.append("Delivered follow-up does not match saved followup.txt")
    if protocol_findings:
        fatal = True
    validation = C.check(d / "list.tsv", a.surah, D.M.verses())
    save(d / "validation.json", validation)
    row = {"ref": f"S{a.surah}", "arm": "discover", "brief": f"{a.run_tag}.{a.model}.sec{a.section}",
           "run_tag": a.run_tag, "section_number": a.section, "model": D.MODELS[a.model], "effort": D.EFFORT,
           "runner": "agent", **session, "estimate_usd": 0, "cost_usd": 0, "cost_basis": "Codex subscription",
           "status": "partial" if fatal else "ok", "check": "findings" if fatal or diagnostics or validation["arabic_findings"] or (consolidation and consolidation['repeated_proposals']) else "ok",
           "followup_mode": start.get("followup_mode", "legacy-append"),
           "consolidation": consolidation, "consolidation_error": consolidation_error,
           "usage_tokens": usage, "turn1_rows": first["rows"], "turn1_lines": first["lines"],
           "turn1": first, "turn2": {"completed": len(done) == 2, "rows_total": len(rows), "rows_added": len(rows) - first["rows"],
                                    "usage": {k: v - first["usage"].get(k, 0) for k, v in usage.items()} if usage and first["usage"] else None},
           "append_only": prefix_ok, "model_effort_verified": model_ok, "bad_rows": bad, "duplicates": duplicates,
           "source_sha256": start["source_sha256"], "inputs_unchanged": inputs_ok,
           "followup_delivery": proof, "protocol_findings": protocol_findings,
           "tool_audit_reviewed": True, "tool_diagnostics": diagnostics, "arabic_findings": len(validation["arabic_findings"]),
           "followup": (d / "followup.txt").read_text().strip(), "strength_counts": dict(Counter(r["strength"] for r in rows)),
           "list_sha256": hashlib.sha256(final).hexdigest(), "prompt_sha256": start["prompt_sha256"],
           "package_sha256": start["package_sha256"], "completed_at": done[-1]["timestamp"] if done else None,
           "seconds": round((datetime.fromisoformat(done[-1]["timestamp"].replace("Z", "+00:00")) - datetime.fromisoformat(start["started"])).total_seconds()) if done else None}
    save(d / "run.log.json", row)
    D.V.log(row)
    print(json.dumps({k: row[k] for k in ("section_number", "model", "status", "check", "turn1_rows", "turn2", "arabic_findings", "tool_diagnostics", "seconds")}, ensure_ascii=False))
    if fatal:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
