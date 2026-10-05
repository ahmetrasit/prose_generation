"""Bible-owned native session and transcript inspection."""
import json
import re
from pathlib import Path
from enrichment.bible.discovery import save

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
