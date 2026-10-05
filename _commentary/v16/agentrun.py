#!/usr/bin/env python3
"""Agent-spawned runs (user, 2026-10-04 evening): no run is handled through scripts. The orchestrating Claude session
spawns each model call as a subagent (Agent tool) from a prompt the scripts built, and the scripts finish what the
agent wrote. This module is the shared piece: the spawn prompt, the transcript lookup, the cost from the transcript's
token counts, and the run record in the shape v16.call_opus produced, so usage_row/post_process/the ledger see no
difference.

  prepare(d, text, started, kind, output, lookup)   writes prompt.md, started.json (the never-rerun guard), spawn.md
  finish(d, output)                                 reads <d>/<output>, finds the subagent transcript, writes
                                                    run.log.json and tool_calls.json, returns the run object

The spawn prompt's first line is `v16-agent-run: <dir>`. The hook guard (hooks/guard.py) reads it from the
subagent's transcript to enforce the run's rules (lookup only, write only the output file), and finish() finds
the transcript by it under ~/.claude/projects/*/*/subagents/. The Agent tool itself reports no tokens or cost;
the transcript carries per-message usage, and the cost is computed from it at the CLI's rates (RATES).
"""
from __future__ import annotations

import hashlib
import json
import re
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PROJECTS = Path.home() / ".claude" / "projects"
MARK = "v16-agent-run:"
MISSING = HERE / "missing.py"
# $/MTok, the published list rates (5m write 1.25x input, 1h write 2x input). Corrected 2026-10-04 night: the
# earlier table had Opus input $8 and a 5m write of $10 (both double), reads at $0.17, and Sonnet at the same wrong
# ratios. Check: these rates reproduce the CLI's own cost_usd to the cent on three enrichment trials (S107 Opus
# $7.4612 with 1h writes, S100 Opus $6.7356 with 5m writes, S107 Sonnet $6.3220 with 1h writes). Fable: exact on
# the two 87:8 runs. The figure is the CLI's nominal dollar, as in the ledger, never cash.
RATES = {"claude-opus-5-5": {"input": 4.0, "cache_5m": 5.0, "cache_1h": 8.0, "cache_read": 0.20, "output": 20.0},
         "claude-fable-5-1": {"input": 10.0, "cache_5m": 12.5, "cache_1h": 20.0, "cache_read": 0.25, "output": 50.0},
         "claude-sonnet-5-5": {"input": 2.0, "cache_5m": 2.5, "cache_1h": 4.0, "cache_read": 0.20, "output": 10.0}}
AGENT_TYPE = {"writer": "v16-call", "augment": "v16-call", "enrich": "enrich-page", "enrich-dosya": "enrich-page",
              "okuma-plan": "general-purpose", "okuma": "general-purpose", "enrich-parts": "enrich-page-<effort>"}
AGENT_MODEL = {"okuma-plan": "Sonnet 5.5", "okuma": "Sonnet 5.5"}  # every other kind: Opus 5.5


def spawn_prompt(d: Path, kind: str, output: str, lookup: bool) -> str:
    """The text the orchestrator gives the Agent tool, verbatim."""
    lines = [f"{MARK} {d}", ""]
    if kind in ("okuma", "okuma-plan"):  # the staged enrichment's reading calls (enrichment/v2/okuma.py)
        lines += [f"Read {d / 'prompt.md'} with the Read tool: it is your brief and lists your material files. Read "
                  "every listed file completely, in order, one Read per file. Follow the brief exactly.",
                  f"Use no other tool and run no command. Write your output to {d / output} with the Write tool, in "
                  "one write; nothing else.",
                  "When the file is written, reply with one line: written. Do not put the output in your reply."]
        return "\n".join(lines) + "\n"
    if kind == "enrich-dosya":
        lines += [f"Read {d / 'prompt.md'} with the Read tool, completely: it is long, so read it in parts with offset and "
                  "limit until you have seen the last line; it is your whole job and all your material. Follow it exactly.",
                  f"Use no other tool and run no command: everything you need is in that file. Then write the records to "
                  f"{d / output} with the Write tool, in one write, and gaps.json beside it; nothing else.",
                  "When the files are written, reply with one line: written. Do not put the records in your reply."]
        return "\n".join(lines) + "\n"
    if kind == "enrich-parts":  # the cost-trial modes (enrichment v2 tur, dosya2): records in parts, joined by finish
        lines += [f"Read {d / 'prompt.md'} with the Read tool: it is your whole job. Follow it exactly. Your call "
                  f"directory is {d}; write only there. Write the page's records in parts, annotations.1.jsonl, "
                  f"annotations.2.jsonl … in that directory, as the job says (never annotations.jsonl itself), and "
                  f"gaps.json.",
                  "When the files are complete, reply with one line: written. Do not put the records in your reply."]
        return "\n".join(lines) + "\n"
    if kind == "enrich":
        lines += [f"Read {d / 'prompt.md'} with the Read tool: it is your whole job. Follow it exactly. Your call "
                  f"directory is {d}; write only there, and write the page's records to {d / output} as the job says.",
                  "When the file is complete, reply with one line: written. Do not put the records in your reply."]
    else:
        lines += [f"Read {d / 'prompt.md'} with the Read tool: it is your whole brief and your material. Follow it "
                  "exactly, and produce only the output the brief asks for."]
        if lookup:
            lines += [f"The only command you may run is the lookup the brief describes (`python3 {MISSING} …`), "
                      "exactly as written, as the whole command: no cd, no && and no ;. Every other command is "
                      "refused and the run is then treated as contaminated."]
        else:
            lines += ["Run no commands; the brief needs none, and any command is refused."]
        lines += [f"Write your complete answer, and nothing else, to {d / output} with the Write tool, in one write "
                  "when the answer is finished. Do not put the answer in your reply: when the file is saved, reply "
                  "with one line: written.",
                  "Read, write and run nothing else."]
    return "\n".join(lines) + "\n"


def prepare(d: Path, text: str, started: dict, kind: str, output: str = "response.md", lookup: bool = True) -> Path:
    d.mkdir(parents=True, exist_ok=True)
    (d / "prompt.md").write_text(text, encoding="utf-8")
    (d / "started.json").write_text(json.dumps({**started, "started": time.strftime("%Y-%m-%dT%H:%M:%S"),
                                                "prompt_sha256": hashlib.sha256(text.encode()).hexdigest(),
                                                "runner": "agent", "output": output}, ensure_ascii=False) + "\n",
                                    encoding="utf-8")
    sp = d / "spawn.md"
    sp.write_text(spawn_prompt(d, kind, output, lookup), encoding="utf-8")
    print(f"prepared {d.relative_to(ROOT)}: spawn one agent of type {AGENT_TYPE[kind]} "
          f"({AGENT_MODEL.get(kind, 'Opus 5.5, effort high')}) with "
          f"the text of {sp.relative_to(ROOT)}; when it replies, run the finish step for this dir")
    return sp


def transcripts(d: Path) -> list[Path]:
    """Every subagent transcript whose first message is this run's spawn prompt, oldest first."""
    key = f"{MARK} {d}"
    hits = []
    for f in PROJECTS.glob("*/*/subagents/agent-*.jsonl"):
        try:
            with f.open(encoding="utf-8") as fh:
                head = fh.read(20_000)
        except OSError:
            continue
        if key in head:
            hits.append(f)
    return sorted(hits, key=lambda p: p.stat().st_mtime)


def parse(f: Path) -> dict:
    """Usage summed over the distinct assistant messages (the transcript repeats a message's usage on every one of its
    content lines), the tool calls with their results, the last stop reason, the model, the text blocks."""
    seen, usage = set(), {"input": 0, "cache_5m": 0, "cache_1h": 0, "cache_read": 0, "output": 0}
    calls, ids, texts, safety, stop, model, agent_id, bad = [], [], [], [], None, None, None, 0
    handback = False  # a subagent ends its turn with the SubagentHandback tool call: that is its end_turn
    out_by_msg: dict[str, int] = {}  # the transcript records usage as the message starts streaming: output is a floor
    ctx_by_msg: dict[str, int] = {}  # the context each message was sent with (input + cache read + cache write)
    res_by_msg: dict[str, list[str]] = {}  # the tool results that came back after each message
    last_mid = None
    for line in f.read_text(encoding="utf-8").splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            bad += line.strip() != ""
            continue
        agent_id = agent_id or ev.get("agentId")
        if "safeguards stopped" in line:
            safety.append(line[:300])
        msg = ev.get("message") if isinstance(ev.get("message"), dict) else None
        if ev.get("type") == "attachment" and last_mid:  # a reminder the harness adds: context, not the agent's output
            res_by_msg.setdefault(last_mid, []).append(json.dumps(ev.get("attachment"), ensure_ascii=False))
        if ev.get("type") == "assistant" and msg:
            mid = msg.get("id")
            u = msg.get("usage") or {}
            if mid and mid not in seen:
                seen.add(mid)
                ids.append(mid)
                cc = u.get("cache_creation") or {}
                usage["input"] += u.get("input_tokens", 0) or 0
                usage["cache_5m"] += cc.get("ephemeral_5m_input_tokens", 0) or 0
                usage["cache_1h"] += cc.get("ephemeral_1h_input_tokens", 0) or 0
                usage["cache_read"] += u.get("cache_read_input_tokens", 0) or 0
                out_by_msg[mid] = u.get("output_tokens", 0) or 0
                ctx_by_msg[mid] = ((u.get("input_tokens", 0) or 0) + (u.get("cache_read_input_tokens", 0) or 0)
                                   + (u.get("cache_creation_input_tokens", 0) or 0))
                model = msg.get("model") or model
            elif mid in out_by_msg:  # the transcript repeats a message's usage per content line; take the largest output count
                out_by_msg[mid] = max(out_by_msg[mid], u.get("output_tokens", 0) or 0)
            last_mid = mid or last_mid
            stop = msg.get("stop_reason") or stop
            for c in msg.get("content", []) or []:
                if not isinstance(c, dict):
                    continue
                if c.get("type") == "tool_use":
                    if c.get("name") == "SubagentHandback":
                        handback = True
                        continue
                    calls.append({"id": c.get("id"), "name": c.get("name"), "input": c.get("input")})
                elif c.get("type") == "text" and c.get("text"):
                    texts.append(c["text"])
        elif ev.get("type") == "user" and msg:
            content = msg.get("content")
            for c in content if isinstance(content, list) else []:
                if isinstance(c, dict) and c.get("type") == "tool_result" and calls:
                    res = c.get("content")
                    if isinstance(res, list):
                        res = "".join(b.get("text", "") for b in res if isinstance(b, dict))
                    call = next((x for x in calls if x.get("id") == c.get("tool_use_id")), calls[-1])
                    call["result"], call["is_error"] = res, bool(c.get("is_error", False))
                    if last_mid:
                        res_by_msg.setdefault(last_mid, []).append(res if isinstance(res, str) else json.dumps(res, ensure_ascii=False))
    usage["output"] = sum(out_by_msg.values())
    # The real output, thinking included, from the context's growth: a message's output stays in the context, so the
    # next message's context minus this one's, minus the tool results that came back in between, is what it wrote.
    # Result tokens are estimated from characters (Arabic ~1.45 characters per token, other text ~2.4): an estimate.
    est = 0
    for k, mid in enumerate(ids):
        nxt = ids[k + 1] if k + 1 < len(ids) else None
        if nxt is None:
            est += out_by_msg.get(mid, 0)
            continue
        res = "".join(res_by_msg.get(mid, []))
        ar = sum(1 for ch in res if "\u0600" <= ch <= "\u06ff")
        res_tok = ar / 1.45 + (len(res) - ar) / 2.4
        est += max(out_by_msg.get(mid, 0), int(ctx_by_msg.get(nxt, 0) - ctx_by_msg.get(mid, 0) - res_tok))
    rates = RATES.get(model or "")
    cost = round(sum(usage[k] * rates[k] for k in usage) / 1e6, 6) if rates else None
    cost_est = round((sum(usage[k] * rates[k] for k in usage if k != "output") + est * rates["output"]) / 1e6, 6) if rates else None
    return {"transcript": str(f), "agent_id": agent_id, "model": model, "usage_tokens": usage, "cost_usd": cost,
            "output_tokens_est": est, "cost_usd_est": cost_est,
            "stop_reason": stop, "handback": handback, "completed": handback or stop == "end_turn",
            "num_messages": len(ids), "message_ids": ids, "tool_calls": calls, "texts": texts,
            "safety": safety, "unreadable_lines": bad}


def tool_use_outside_rule(d: Path, output: str, calls: list[dict]) -> list[str]:
    """v16 runs: Read of prompt.md, Bash lookups (the audit checks the command itself) and one Write of the output
    file are the rule; anything else is listed. Enrichment runs (dir under enrichment/v2/work/): any read inside
    the workspace, writes inside the call dir, Bash; listed otherwise."""
    enrich = "enrichment/v2/work" in str(d)
    okuma = "/okuma." in str(d)  # reading calls: Read inside the call dir, one Write of the output, nothing else
    out = []
    for c in calls:
        name, inp = c.get("name") or "", c.get("input") or {}
        path = str(inp.get("file_path") or inp.get("path") or inp.get("notebook_path") or "")
        if okuma:
            if name == "Read" and not path.startswith(str(d) + "/"):
                out.append(f"Read {path}")
            elif name == "Write" and path != str(d / output):
                out.append(f"Write {path}")
            elif name not in ("Read", "Write"):
                out.append(f"{name} {json.dumps(inp, ensure_ascii=False)[:120]}")
        elif enrich:
            if name in ("Write", "Edit", "MultiEdit", "NotebookEdit") and not path.startswith(str(d)):
                out.append(f"{name} {path}")
            elif name in ("Read", "Glob", "Grep") and ("enrichment/v2/out" in path or (
                    ("/zengin." in path or "/ehlikitap." in path) and not path.startswith(str(d)))):
                out.append(f"{name} {path}")  # another page's call directory, in any surah
            elif name == "Bash":
                cmd = str(inp.get("command", ""))
                if "enrichment/v2/out" in cmd or re.search(r"/(zengin|ehlikitap)\.[^/\s]+", cmd.replace(str(d), "")):
                    out.append(f"Bash {cmd[:160]}")
            elif name not in ("Read", "Glob", "Grep", "Write", "Edit", "MultiEdit", "NotebookEdit", "Bash"):
                out.append(f"{name} {json.dumps(inp, ensure_ascii=False)[:120]}")
        else:
            if name == "Read" and path != str(d / "prompt.md"):
                out.append(f"Read {path}")
            elif name == "Write" and path != str(d / output):
                out.append(f"Write {path}")
            elif name not in ("Read", "Write", "Bash"):
                out.append(f"{name} {json.dumps(inp, ensure_ascii=False)[:120]}")
    return out


def finish(d: Path, output: str = "response.md") -> dict:
    """The run object for an agent-written output, in v16.call_opus's shape, written to run.log.json."""
    out_file = d / output
    result = out_file.read_text(encoding="utf-8") if out_file.exists() else ""
    obj: dict = {"result": result, "returncode": 0, "runner": "agent", "output_file": output, "tool_calls": 0,
                 "text_message_ids": []}
    ts = transcripts(d)
    if not ts:
        obj["transcript"] = None
        print(f"WARNING: no subagent transcript names {d.relative_to(ROOT)}: cost, commands and stop reason not "
              "recovered (the ledger row says cost None); the output itself is unaffected")
    else:
        if len(ts) > 1:
            print(f"WARNING: {len(ts)} subagent transcripts name this run ({', '.join(p.name for p in ts)}): the "
                  "newest is used; a run spawned twice is never clean, tell the user")
            obj["transcripts_all"] = [str(p) for p in ts]
        p = parse(ts[-1])
        u = p["usage_tokens"]
        obj.update({"transcript": p["transcript"], "agent_id": p["agent_id"], "model": p["model"],
                    "usage": {"input_tokens": u["input"], "cache_creation_input_tokens": u["cache_5m"] + u["cache_1h"],
                              "cache_creation": {"ephemeral_5m_input_tokens": u["cache_5m"],
                                                 "ephemeral_1h_input_tokens": u["cache_1h"]},
                              "cache_read_input_tokens": u["cache_read"], "output_tokens": u["output"]},
                    "total_cost_usd": p["cost_usd"], "output_tokens_est": p["output_tokens_est"],
                    "cost_usd_est": p["cost_usd_est"],
                    "cost_basis": "transcript tokens x agentrun.RATES; output tokens are a floor (the transcript "
                                  "records usage as a message starts streaming), so the figure is a lower bound",
                    # the hand-back is the subagent's end of turn; usage_row reads stop_reason as the CLI's
                    "stop_reason": "end_turn" if p["handback"] else p["stop_reason"], "stop_reason_raw": p["stop_reason"],
                    "completed": p["completed"], "num_turns": p["num_messages"],
                    "text_message_ids": p["message_ids"], "tool_calls": len(p["tool_calls"]),
                    "reply": "".join(p["texts"])[-500:]})
        if p["cost_usd"] is None:
            print(f"WARNING: no rate for model {p['model']!r} in agentrun.RATES: cost None")
        if p["safety"]:
            obj["safety_stop"] = p["safety"]
        if p["unreadable_lines"]:
            obj["stream_unreadable_lines"] = p["unreadable_lines"]
        if p["tool_calls"]:
            (d / "tool_calls.json").write_text(json.dumps(p["tool_calls"], ensure_ascii=False, indent=1) + "\n",
                                               encoding="utf-8")
        # every tool use outside the run's rule is reported (detection; the hook guard, when installed, prevents)
        outside = tool_use_outside_rule(d, output, p["tool_calls"])
        if outside:
            obj["tool_use_outside_rule"] = outside
            for x in outside:
                print(f"WARNING: tool use outside the run's rule (treat the run as contaminated): {x[:220]}")
    if not result.strip():
        obj["is_error"] = True
        obj["error"] = f"the agent wrote no {output}"
    (d / "run.log.json").write_text(json.dumps(obj, ensure_ascii=False) + "\n", encoding="utf-8")
    return obj
