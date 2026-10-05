#!/usr/bin/env python3
"""PreToolUse hook: the rules of an agent-spawned run (user, 2026-10-04 evening). To be wired by the user in
.claude/settings.json (RUNBOOK.md, "Agent-spawned runs") for every tool call in the project; it acts only inside a
subagent whose first message starts with `v16-agent-run: <dir>` (agentrun.spawn_prompt), and allows everything else.
Exit 2 refuses the call and the reason goes back to the agent.

v16 runs (dir under _commentary/v16/out/): Read only <dir>/prompt.md; Bash only the lookup `python3 missing.py …`
(packets.SAFE_CMD's rule); Write only <dir>/<output> (started.json names it); nothing else.
Enrichment runs (dir under enrichment/v2/work/): Read anywhere in the workspace except enrichment/v2/out/ and the
other call directories; Write and Edit only inside <dir>; Bash refused when the command names enrichment/v2/out/,
another call directory, or git. This is weaker than the CLI runner's sandbox (no network rule, no write rule for
arbitrary commands); the brief carries the rest.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MISSING = ROOT / "_commentary" / "v16" / "missing.py"
SAFE_CMD = re.compile(rf"python3 {re.escape(str(MISSING))} (?:S\d+|\d+:\d+|text)(?: [0-9:()\[\],;.\-–— ]*)?")
MARK = "v16-agent-run:"
V16_OUT = ROOT / "_commentary" / "v16" / "out"
ENRICH_WORK = ROOT / "enrichment" / "v2" / "work"
ENRICH_OUT = ROOT / "enrichment" / "v2" / "out"


def run_dir(transcript: str) -> Path | None:
    if not transcript or "/subagents/" not in transcript:
        return None
    try:
        with open(transcript, encoding="utf-8") as f:
            first = f.readline()
    except OSError:
        return None
    try:
        ev = json.loads(first)
        content = (ev.get("message") or {}).get("content")
        text = content if isinstance(content, str) else "".join(
            c.get("text", "") for c in content if isinstance(c, dict)) if isinstance(content, list) else ""
    except (json.JSONDecodeError, AttributeError):
        text = first
    m = re.search(rf"{MARK} (\S+)", text)
    return Path(m.group(1)) if m else None


def refuse(why: str) -> None:
    print(f"refused by the run guard: {why}", file=sys.stderr)
    sys.exit(2)


def main() -> None:
    try:
        h = json.load(sys.stdin)
    except json.JSONDecodeError:
        return
    d = run_dir(h.get("transcript_path", ""))
    if d is None:
        return  # not an agent-spawned run of ours: nothing to enforce
    tool, inp = h.get("tool_name", ""), h.get("tool_input") or {}
    path = inp.get("file_path") or inp.get("path") or inp.get("notebook_path") or ""
    p = Path(path).resolve() if path else None
    if d.is_relative_to(V16_OUT):
        output = "response.md"
        try:
            output = json.loads((d / "started.json").read_text(encoding="utf-8")).get("output", output)
        except (OSError, json.JSONDecodeError):
            pass
        if tool == "Read":
            if p != (d / "prompt.md").resolve():
                refuse(f"a v16 run reads only {d / 'prompt.md'}")
        elif tool == "Bash":
            if not SAFE_CMD.fullmatch(str(inp.get("command", "")).strip()):
                refuse(f"a v16 run may run only the lookup `python3 {MISSING} text <refs>` (or the check for its own "
                       "target), exactly as written, as the whole command")
        elif tool == "Write":
            if p != (d / output).resolve():
                refuse(f"a v16 run writes only {d / output}")
        else:
            refuse(f"a v16 run uses only Read (prompt.md), Bash (the lookup) and Write ({output}); not {tool}")
    elif d.is_relative_to(ENRICH_WORK):
        others = [x for x in d.parent.parent.glob("s*/zengin.*") if x.is_dir() and x != d] \
            + [x for x in d.parent.parent.glob("s*/ehlikitap.*") if x.is_dir() and x != d]  # any surah's call dirs
        others += [x for x in ENRICH_WORK.glob("s*/grup/*.opus.*") if x.is_dir() and x != d]  # group units (grup.py)
        if tool in ("Read", "Glob", "Grep"):
            if p and (p.is_relative_to(ENRICH_OUT) or any(p.is_relative_to(o) for o in others)):
                refuse("an enrichment run reads neither enrichment/v2/out/ nor another call directory")
            if p and not p.is_relative_to(ROOT):
                refuse(f"an enrichment run reads only inside {ROOT}")
        elif tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
            if not p or not p.is_relative_to(d):
                refuse(f"an enrichment run writes only inside its call directory {d}")
        elif tool == "Bash":
            cmd = str(inp.get("command", ""))
            if str(ENRICH_OUT) in cmd or "enrichment/v2/out" in cmd or any(str(o) in cmd for o in others) \
                    or re.search(r"(^|[;&|\s])git(\s|$)", cmd):
                refuse("an enrichment run's commands never touch enrichment/v2/out/, another call directory, or git")


if __name__ == "__main__":
    main()
