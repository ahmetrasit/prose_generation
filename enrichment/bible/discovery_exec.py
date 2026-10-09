#!/usr/bin/env python3
"""Run prepared Bible discovery readers through `codex exec` from a Claude Code orchestrator (no Codex parent).

Same two-turn protocol as discovery_native.py, in the same files: start → turn 1 (`codex exec`) → snapshot →
the fixed follow-up as turn 2 in the same session (`codex exec resume`) → audit → policy review → finish. The run log
also records the API-equivalent cost of the whole session (codexrun.RATES).

  discovery_exec.py run --surah S --run-tag TAG [--targets 103:1,surah] [--parallel 50]
  discovery_exec.py cost --surah S --run-tag TAG       expected cost before a run, actual after

Each phase is done once: a finished phase is skipped, a turn whose stream exists is never started again (a dead
turn is printed as a WARNING; it needs a fresh attempt). The policy review finishes a session only when its tool
calls stayed inside the session's call directory (reads of prompt/package, writes of list.tsv/followup.tsv) with no
network, scripts or other files; anything else is printed and the session is left for the operator.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
import shlex
import sys
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from enrichment.bible import codexrun as X, discovery as D, discovery_native as N  # noqa: E402

# Expected cost per reader session (both turns), from the S87 Luna sessions (~1.0M input tokens, ~90% cached,
# ~50k output) priced at codexrun.RATES; Sol high is assumed to read about the same.
EXPECTED = {'luna': 0.05, 'sol': 1.00}
NETWORK = re.compile(r'\b(curl|wget|http|https|ssh|scp|nc|git)\b')


def task_name(s, tag, target, model):
    return re.sub(r'[^a-z0-9_]', '_', f'bible_s{s:03d}_{tag}_{target}_{model}'.lower())


def commands(call):
    """(kind, payload) of one native tool call: shell command text or patch text."""
    name, args = call.get('name', '').split('.')[-1], call.get('arguments') or ''
    if name == 'apply_patch':
        return 'patch', args
    if name == 'exec_command':
        return 'cmd', json.loads(args).get('cmd', '')
    if name == 'exec':
        m = re.search(r'tools\.exec_command\(\s*\{[\s\S]*?\bcmd\s*:\s*("(?:[^"\\]|\\.)*")', args)
        if m:
            return 'cmd', json.loads(m[1])
        m = re.search(r'tools\.apply_patch\(\s*("(?:[^"\\]|\\.)*")', args)
        if m:
            return 'patch', json.loads(m[1])
        return 'other', args
    return 'other', f'{name}: {args}'


def path_tokens(cmd):
    try:
        toks = shlex.split(cmd.split('<<', 1)[0])   # never read heredoc bodies as paths
    except ValueError:
        toks = cmd.split()
    return [t for t in toks if t.startswith(('/', './', '../', 'enrichment/', '~'))
            or re.search(r'\.(md|tsv|json|jsonl|py|txt|sqlite)$', t)]


def policy(d, calls):
    """(violations, notes) for a reader's tool calls."""
    bad, notes = [], []
    own = {d / 'prompt.md', d / 'package.md', d / 'list.tsv', d / 'followup.tsv'}
    for c in calls:
        kind, text = commands(c)
        where = f"turn {c.get('phase')} {c.get('call_id')}"
        if kind == 'other':
            bad.append(f'{where}: tool outside the reader rules: {text[:200]}')
            continue
        if kind == 'patch':
            for m in re.finditer(r'\*\*\* (?:Add File|Update File|Delete File|Move to): (.+)', text):
                p = Path(m[1].strip())
                p = (p if p.is_absolute() else X.ROOT / p).resolve()
                if p not in {d / 'list.tsv', d / 'followup.tsv'}:
                    bad.append(f'{where}: patch writes {p}')
            continue
        if NETWORK.search(cmd_head(text)):
            bad.append(f'{where}: network or repository command: {text[:200]}')
        if re.search(r'\bpython|\bnode\b|\bcodex\b|\bclaude\b', cmd_head(text)):
            bad.append(f'{where}: script or model call: {text[:200]}')
        for t in path_tokens(text):
            p = Path(t).expanduser()
            p = (p if p.is_absolute() else X.ROOT / p).resolve()
            if p == Path('/dev/null'):
                continue
            if p not in own:
                bad.append(f'{where}: touches {p}')
        if c.get('phase') == 2 and not re.search(r'followup\.tsv', text):
            notes.append(f'{where}: follow-up turn command not about followup.tsv: {text[:160]}')
        elif c.get('phase') == 2 and re.match(r'\s*(cat|head|tail|wc|awk|sed)\b', text) and '>' not in text:
            notes.append(f'{where}: follow-up turn read its own followup.tsv: {text[:160]}')
    return bad, notes


def cmd_head(text):
    return text.split('<<', 1)[0]


def one(s, tag, target, model):
    d = D.tdir(s, target, tag) / model
    a = SimpleNamespace(surah=s, target=target, run_tag=tag, model=model, task=task_name(s, tag, target, model),
                        reviewed=False, protocol_finding=[], phase='start')
    say = lambda m: f'{target} {model}: {m}'  # noqa: E731
    if (d / 'run.log.json').exists():
        return say('already finished, skipped')
    if not (d / 'prompt.md').exists():
        return say('WARNING not prepared')
    start = json.loads((d / 'started.json').read_text()) if (d / 'started.json').exists() else None
    if start is None:
        N.run_phase(a, runner='codex-exec')
        start = json.loads((d / 'started.json').read_text())
    elif start.get('runner') != 'codex-exec':
        return say(f"WARNING started by runner {start.get('runner')}; not continued here")
    model_id, effort = start['model'], start['effort']
    if not (d / 'turn1.stream.jsonl').exists():
        r = X.turn(d, 1, (d / 'spawn.md').read_text(), model_id, effort)
        if not (r['completed'] and r['thread_id']):
            return say(f"WARNING turn 1 failed (rc {r['returncode']}): {r['stderr'][-300:]}")
        D.save(d / 'session.json', {'agent_path': start['agent_path'], 'agent_id': r['thread_id'],
                                    'transcript': str(X.rollout(r['thread_id'])), 'runner': 'codex-exec'})
    if not (d / 'session.json').exists():
        return say('WARNING turn 1 started earlier but never completed (no session.json); needs a fresh attempt')
    session = json.loads((d / 'session.json').read_text())
    if not (d / 'turn1.json').exists():
        a.phase = 'snapshot'
        N.run_phase(a, runner='codex-exec')
    if not (d / 'turn2.stream.jsonl').exists():
        r = X.turn(d, 2, (d / 'followup.txt').read_text(), model_id, effort, thread=session['agent_id'])
        if not r['completed'] or r.get('error'):
            return say(f"WARNING turn 2 failed (rc {r['returncode']}): {r.get('error') or r['stderr'][-300:]}")
    a.phase = 'audit'
    calls = N.run_phase(a, runner='codex-exec')
    bad, notes = policy(d, calls)
    D.save(d / 'policy_review.json', {'violations': bad, 'notes': notes, 'calls': len(calls),
                                      'reviewer': 'discovery_exec.policy (automatic) for the Claude Code orchestrator'})
    if bad:
        return say('WARNING policy review found violations; not finished:\n  ' + '\n  '.join(bad))
    c = X.cost(Path(session['transcript']))
    a.phase, a.reviewed = 'finish', True
    try:
        row = N.run_phase(a, runner='codex-exec', extra={**c, 'cost_basis': 'API-equivalent at codexrun.RATES '
                                                          '(Codex subscription; usage counts)', 'policy_notes': notes})
    except SystemExit:
        row = json.loads((d / 'run.log.json').read_text())
        return say(f"WARNING finished with status {row['status']}: {row.get('protocol_findings')} "
                   f"{row.get('consolidation_error') or ''}")
    extra = f"; NOTE {len(notes)} policy note(s): " + ' | '.join(notes) if notes else ''
    return say(f"ok, {row['turn1_rows']} + {row['turn2']['rows_added']} rows, ${c['usd_equivalent']:.3f}{extra}")


def jobs(s, tag, targets):
    ts = D.targets_of(s)
    if targets:
        want = set(targets.split(','))
        ts = [t for t in ts if t['target'] in want or ('surah' in want and t['target'].startswith('sec'))]
    return [(t['target'], m) for t in ts for m in D.readers(s, tag)
            if (D.tdir(s, t['target'], tag) / m / 'prompt.md').exists()]


def cost(s, tag, targets):
    js = jobs(s, tag, targets)
    exp = sum(EXPECTED.get(m, 0) for _, m in js)
    act, done = 0.0, 0
    for target, m in js:
        f = D.tdir(s, target, tag) / m / 'run.log.json'
        if f.exists():
            act += json.loads(f.read_text()).get('usd_equivalent') or 0
            done += 1
    print(f'S{s} {tag}: {len(js)} reader sessions; expected ≈ ${exp:.2f} API-equivalent; '
          f'finished {done}, actual ${act:.2f}')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('phase', choices=('run', 'cost'))
    ap.add_argument('--surah', type=int, required=True)
    ap.add_argument('--run-tag', required=True)
    ap.add_argument('--targets')
    ap.add_argument('--parallel', type=int, default=7)
    a = ap.parse_args()
    if a.phase == 'cost':
        return cost(a.surah, a.run_tag, a.targets)
    js = jobs(a.surah, a.run_tag, a.targets)
    cost(a.surah, a.run_tag, a.targets)
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.parallel) as pool:
        futs = {pool.submit(one, a.surah, a.run_tag, t, m): (t, m) for t, m in js}
        for f in concurrent.futures.as_completed(futs):
            try:
                print(f.result(), flush=True)
            except Exception as e:  # recorded, never silent
                t, m = futs[f]
                print(f'{t} {m}: WARNING {type(e).__name__}: {e}', flush=True)
    cost(a.surah, a.run_tag, a.targets)


if __name__ == '__main__':
    main()
