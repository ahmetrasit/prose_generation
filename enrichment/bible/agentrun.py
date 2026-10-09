#!/usr/bin/env python3
"""Bible-only native page-agent bookkeeping and transcript audit; never calls models.

Accounting rates are a local snapshot inherited on 2026-10-05. Amounts are nominal
transcript estimates, not current pricing or billed charges. This module does not
rely on the Islamic pathway's hooks or agent definitions.
"""
from __future__ import annotations
import hashlib
import json
import re
import shlex
import time
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PROJECTS = Path.home() / '.claude/projects'
MARK = 'bible-agent-run:'
RATES = {'claude-opus-5-5': {'input':4.0, 'cache_5m':5.0, 'cache_1h':8.0, 'cache_read':0.20, 'output':20.0}}


def prepare(d, text, started, kind='enrich', output='annotations.jsonl', lookup=False):
    if kind != 'enrich' or lookup:
        raise ValueError('Bible page calls only')
    d.mkdir(parents=True, exist_ok=True)
    row = {**started, 'started':time.strftime('%Y-%m-%dT%H:%M:%S'),
           'prompt_sha256':hashlib.sha256(text.encode()).hexdigest(), 'runner':'agent', 'output':output}
    with (d/'started.json').open('x') as f:
        json.dump(row,f,ensure_ascii=False,indent=2)
    (d/'prompt.md').write_text(text)
    prompt = (f'{MARK} {d}\n\nRead {d/"prompt.md"} completely and follow it. '
              'Use only the Bible-owned inputs and tools named there. Write only in your call directory. '
              f'Write records to {d/output}, verdicts.jsonl, gaps.json and (when the prompt has a Semitic root table) '
              'root_verdicts.jsonl beside it. '
              'If no evidence qualifies, create an empty annotations.jsonl and explain why in gaps.json. '
              'Do not spawn agents or call models. Reply briefly after saving the files.\n')
    (d/'spawn.md').write_text(prompt)
    print(f'Prepared {d}: use a native general-purpose agent, model {row["model_id"]}, effort {row["effort"]}; '
          'this command makes no model call.')
    return d/'spawn.md'


def inside(path, root):
    return Path(path).resolve().is_relative_to(root.resolve())


def allowed_command(command, d):
    # No shell expansion or compound commands; all allowed scripts are Bible-owned.
    if re.search(r'[;&|<>`$\n\r]', command):
        return False
    try:
        args=shlex.split(command)
    except ValueError:
        return False
    if len(args)<3 or not re.fullmatch(r'python(?:3(?:\.\d+)?)?',Path(args[0]).name):
        return False
    script=Path(args[1])
    if not script.is_absolute(): script=ROOT/script
    if script.resolve().parent != HERE.resolve(): return False
    tail=args[2:]
    if script.name=='corpus.py':
        if tail[0]=='--intertext': tail=tail[1:]
        return bool(tail) and tail[0] in ('sources','get','ayah','search')
    if script.name=='hebrew.py':
        return bool(tail) and tail[0] in ('root','cognates','word','table')
    if script.name not in ('validate.py','render.py','verdicts.py'): return False
    paths={}
    for key in ('--annotations','--out','--report'):
        if key in tail:
            pos=tail.index(key)
            if pos+1==len(tail): return False
            path=Path(tail[pos+1])
            if not path.is_absolute(): path=ROOT/path
            if not inside(path,d): return False
            paths[key]=path
    return '--annotations' in paths and (script.name!='render.py' or '--out' in paths)


def old_rule_allows(d, call):
    """The original page-call grammar (before 2026-10-09): reads of the call directory, pack, frozen discovery files
    and corpus; writes in the call directory; the listed Bible tools."""
    started=json.loads((d/'started.json').read_text())
    pack=HERE/'work'/f's{started["surah"]:03d}'/'pack'
    exact={HERE/'SCHEMA_BIBLE_CARD.md',HERE/'SCHEMA.md',d/'prompt.md'}
    # Frozen provenance also contains native reader transcripts; those are for
    # operator auditing, not extra context for the independent page author.
    exact.update(ROOT/p for p in started['bible_inputs']
                 if Path(p).name=='prefetch.json' or Path(p).name.endswith(('.merged.tsv','.merged.json')))
    exact={p.resolve() for p in exact}
    name, inp=call.get('name'),call.get('input') or {}
    raw=inp.get('file_path') or inp.get('path') or inp.get('notebook_path')
    path=Path(raw) if raw else None
    if path and not path.is_absolute(): path=ROOT/path
    if name in ('Read','Glob','Grep'):
        return path is not None and (inside(path,d) or inside(path,pack) or path.resolve() in exact
                                     or inside(path,HERE/'corpus'))
    if name in ('Write','Edit','MultiEdit','NotebookEdit'):
        return path is not None and inside(path,d) and path.name!='operator-review.json'
    if name=='Bash':
        return allowed_command(str(inp.get('command','')),d)
    return False


def tool_use_outside_rule(d, output, calls, review_log=None):
    """Calls outside the grammar: not allowed by the original rules, not in the widened grammar (review.py kinds
    marked auto: read-only shell on allowed inputs, Read of own persisted outputs, helpers inside the call
    directory, own edits), and not covered by an operator-review.json. review_log collects how each was allowed."""
    from enrichment.bible import review as RV
    rows,_=RV.walk(d,calls)
    ok,problems=RV.covered(d,calls)
    out=[f'operator review: {x}' for x in problems]
    for i,call in enumerate(calls):
        if old_rule_allows(d,call):
            continue
        r=rows[i]
        if r['kind'] and r['auto']:
            how='widened grammar'
        elif i in ok:
            how='operator review'
        else:
            out.append(f"{call.get('name')}: {json.dumps(call.get('input') or {},ensure_ascii=False)[:240]}"
                       + (f" [{r['reason']}]" if r['reason'] else ''))
            continue
        if review_log is not None:
            review_log.append(dict(index=i,call_id=call.get('id'),kind=r['kind'],allowed_by=how,reason=r['reason']))
    return out


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
    models = set()
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
                if model: models.add(model)
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
    return {"transcript": str(f), "agent_id": agent_id, "model": model, "models": sorted(models), "usage_tokens": usage, "cost_usd": cost,
            "output_tokens_est": est, "cost_usd_est": cost_est,
            "stop_reason": stop, "handback": handback, "completed": handback or stop == "end_turn",
            "num_messages": len(ids), "message_ids": ids, "tool_calls": calls, "texts": texts,
            "safety": safety, "unreadable_lines": bad}


def finish(d, output='annotations.jsonl'):
    started=json.loads((d/'started.json').read_text())
    errors=[]
    if hashlib.sha256((d/'prompt.md').read_bytes()).hexdigest()!=started['prompt_sha256']:
        errors.append('prompt changed since preparation')
    ts=transcripts(d)
    obj={'runner':'agent','completed':False,'output_file':output}
    if len(ts)!=1:
        errors.append(f'expected exactly one native agent transcript, found {len(ts)}')
    else:
        parsed=parse(ts[0])
        calls=parsed['tool_calls']
        allowed_beyond=[]
        outside=tool_use_outside_rule(d,output,calls,allowed_beyond)
        (d/'tool_calls.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
        if not parsed['completed']: errors.append('native agent has not completed')
        if parsed['models']!=[started['model_id']]: errors.append('unexpected or mixed model in transcript')
        if parsed['safety'] or parsed['unreadable_lines']: errors.append('interrupted or unreadable transcript')
        if outside: errors.append('tool use outside Bible call rules')
        obj.update(transcript=parsed['transcript'],agent_id=parsed['agent_id'],model=parsed['model'],
                   completed=parsed['completed'],stop_reason=parsed['stop_reason'],
                   usage=parsed['usage_tokens'],total_cost_usd=parsed['cost_usd'],cost_usd_est=parsed['cost_usd_est'],
                   cost_basis='nominal transcript estimate using Bible-local accounting snapshot',
                   tool_use_outside_rule=outside,allowed_beyond_original_grammar=allowed_beyond)
    # An explicitly explained empty result is checked by enrich.finish, not treated as a missing file here.
    if not (d/output).is_file(): errors.append(f'missing {output}')
    obj.update(is_error=bool(errors),error='; '.join(errors))
    (d/'run.log.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
    return obj
