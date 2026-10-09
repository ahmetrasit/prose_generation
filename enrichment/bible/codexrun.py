#!/usr/bin/env python3
"""Bible-owned `codex exec` runner for a Claude Code orchestrator (no Codex parent session needed).

One turn starts a session (`codex exec`), a later turn continues the same session (`codex exec resume <thread>`);
both append to one rollout file under ~/.codex/sessions, which the existing Bible audits read. Each turn's JSON
event stream and last message are kept in the call directory. Costs are API-equivalent at the saved rates below
(Codex usage counts as real cost; the subscription charge itself is not per call).
"""
from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SESSIONS = Path.home() / '.codex/sessions'
# $ per million tokens: input, cached input, cache write, output (snapshot of enrichment/v5/common.py, 2026-10-08)
RATES = {'gpt-6-sol': (2.0, 0.2, 2.5, 10.0), 'gpt-6-luna': (0.1, 0.01, 0.125, 0.5),
         'gpt-5.6-terra': (1.0, 0.1, 1.25, 5.0)}  # Terra: half of Sol (user, 2026-10-09)
SOL_LONG = (4.0, 0.4, 5.0, 15.0)
LONG_CONTEXT = 272_000
KEYS = ('input_tokens', 'cached_input_tokens', 'cache_write_input_tokens', 'output_tokens')


def turn(d: Path, n: int, text: str, model: str, effort: str, thread: str | None = None, timeout: int = 5400) -> dict:
    """Run one turn; turn 1 starts a session, later turns resume `thread`. Returns the turn record."""
    stream, last = d / f'turn{n}.stream.jsonl', d / f'turn{n}.last.txt'
    if stream.exists():
        raise ValueError(f'{stream} exists: turn {n} was already started; never start it twice')
    common = ['--ignore-user-config', '-c', f'model_reasoning_effort="{effort}"', '-c', 'web_search="disabled"',
              '--skip-git-repo-check', '--json', '-o', str(last)]
    if thread is None:
        cmd = ['codex', 'exec', *common, '-m', model, '--disable', 'skill_search', '-s', 'workspace-write',
               '-C', str(ROOT), '-']
    else:  # resume takes no -s/-C: the sandbox is set by config, and the cwd is the repository root
        cmd = ['codex', 'exec', 'resume', *common, '-m', model, '-c', 'sandbox_mode="workspace-write"', thread, '-']
    with stream.open('w') as out:
        p = subprocess.run(cmd, input=text, text=True, stdout=out, stderr=subprocess.PIPE, cwd=ROOT, timeout=timeout,
                           env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'})
    tid, completed, usage = None, False, {}
    for line in stream.read_text().splitlines():
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        if ev.get('type') == 'thread.started':
            tid = ev.get('thread_id')
        elif ev.get('type') == 'turn.completed':
            completed, usage = True, ev.get('usage') or {}
    rec = {'turn': n, 'returncode': p.returncode, 'completed': completed, 'thread_id': tid, 'usage': usage,
           'stderr': (p.stderr or '')[-3000:]}
    if thread is not None and tid not in (None, thread):
        rec['error'] = f'resume started another thread {tid} instead of {thread}'
    (d / f'turn{n}.run.json').write_text(json.dumps(rec, indent=2) + '\n')
    return rec


def rollout(thread: str) -> Path:
    hits = sorted(SESSIONS.glob(f'*/*/*/*{thread}.jsonl'))
    if len(hits) != 1:
        raise ValueError(f'expected one rollout for thread {thread}, found {len(hits)}')
    return hits[0]


def cost(path: Path) -> dict:
    """API-equivalent cost of a whole rollout (every turn), per request, as enrichment/v5/account.py computes it."""
    model, prev = None, {k: 0 for k in KEYS}
    rec = {'usd_equivalent': 0.0, 'requests': 0, 'max_request_input_tokens': 0, 'model': None}
    for line in path.read_text().splitlines():
        try:
            row = json.loads(line)
        except ValueError:
            continue
        pl = row.get('payload', {})
        if row.get('type') == 'turn_context':
            model = pl.get('model', model)
        elif row.get('type') == 'event_msg' and pl.get('type') == 'token_count' and pl.get('info'):
            cur = pl['info']['total_token_usage']
            delta = {k: cur.get(k, 0) - prev[k] for k in KEYS}
            if not any(delta.values()):
                continue
            req = pl['info'].get('last_token_usage', {}).get('input_tokens', 0)
            if model not in RATES:
                raise ValueError(f'{path}: no saved rate for {model}; cost cannot be reported')
            r = SOL_LONG if model == 'gpt-6-sol' and req > LONG_CONTEXT else RATES[model]
            unc = max(0, delta['input_tokens'] - delta['cached_input_tokens'] - delta['cache_write_input_tokens'])
            rec['usd_equivalent'] += (unc * r[0] + delta['cached_input_tokens'] * r[1]
                                      + delta['cache_write_input_tokens'] * r[2] + delta['output_tokens'] * r[3]) / 1e6
            rec['requests'] += 1
            rec['max_request_input_tokens'] = max(rec['max_request_input_tokens'], req)
            prev = {k: cur.get(k, 0) for k in KEYS}
    rec.update(model=model, usd_equivalent=round(rec['usd_equivalent'], 6), **{f'total_{k}': prev[k] for k in KEYS})
    return rec
