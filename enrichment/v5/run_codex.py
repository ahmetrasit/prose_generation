#!/usr/bin/env python3
"""Run v5 spawn files through `codex exec` (Codex subscription), at most seven at a time.

Follows the v16 pattern (_commentary/v16/augment.py call_codex): no user config, web search
off, skill search off, prompt on stdin, JSON event stream kept. Differences: the sandbox is
workspace-write at the repository root, because v5 agents write their own output files, and the
session file is kept (not ephemeral) so per-request context can be checked against the cap.

Per agent it writes <run>/runs/<agent>/: stream.jsonl, last.txt, run.json (usage, thread id,
largest single-request context, API-equivalent cost at the saved rates; actual charge $0 on
the subscription). It refuses to rerun an agent that already has a run.json.

  python3 -B enrichment/v5/run_codex.py SPAWN_FILE [SPAWN_FILE ...] [--jobs 7]
"""
import argparse
import concurrent.futures
import hashlib
import json
import os
import re
import subprocess
import time
from pathlib import Path

from common import CONTEXT_CAP, ROOT, dump
import account

HEADER = re.compile(r'<!-- agent (\S+) \| model (\S+) \| effort (\S+) ')
SESSIONS = Path(os.environ.get('CODEX_SESSIONS_DIR', str(Path.home() / '.codex/sessions'))).expanduser()
ARCHIVE = Path(os.environ.get('CODEX_SESSIONS_ARCHIVE_DIR', str(ROOT / '.scratch/codex_sessions_archive'))).expanduser()
SESSIONS = SESSIONS if SESSIONS.is_absolute() else ROOT / SESSIONS
ARCHIVE = ARCHIVE if ARCHIVE.is_absolute() else ROOT / ARCHIVE


def session_file(thread_id):
    if thread_id:
        for base in (SESSIONS, ARCHIVE):
            for f in sorted(base.glob(f'*/*/*/*{thread_id}.jsonl'), reverse=True):
                return f
    return None


def run(spawn):
    text = spawn.read_text()
    m = HEADER.match(text)
    if not m:
        raise ValueError(f'{spawn}: no agent header')
    agent, model, effort = m.groups()
    out = spawn.parent.parent / 'runs' / agent.rsplit('/', 1)[1]
    if (out / 'run.json').exists():
        return f'{agent}: already run, skipped'
    out.mkdir(parents=True, exist_ok=True)
    started = time.strftime('%Y-%m-%dT%H:%M:%S')
    cmd = ['codex', 'exec', '--ignore-user-config', '-m', model, '-c', f'model_reasoning_effort="{effort}"',
           '-c', 'web_search="disabled"', '--disable', 'skill_search', '--skip-git-repo-check',
           '-s', 'workspace-write', '-C', str(ROOT), '--json', '-o', str(out / 'last.txt'), '-']
    with (out / 'stream.jsonl').open('w') as stream:
        p = subprocess.run(cmd, input=text, text=True, stdout=stream, stderr=subprocess.PIPE,
                           env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'}, timeout=14400)  # 4 h: wall clock, and a disk-throttle pause counts
    usage, thread, completed, commands = {}, None, False, 0
    for line in (out / 'stream.jsonl').read_text().splitlines():
        try:
            ev = json.loads(line)
        except ValueError:
            continue
        if ev.get('type') == 'thread.started':
            thread = ev.get('thread_id')
        elif ev.get('type') == 'turn.completed':
            completed, usage = True, ev.get('usage') or {}
        elif ev.get('type') == 'item.completed' and (ev.get('item') or {}).get('type') == 'command_execution':
            commands += 1
    record = {'agent': agent, 'model': model, 'effort': effort, 'started': started,
              'ended': time.strftime('%Y-%m-%dT%H:%M:%S'), 'returncode': p.returncode, 'turn_completed': completed,
              'thread_id': thread, 'commands': commands, 'usage': usage, 'stderr': (p.stderr or '')[-3000:],
              'prompt_sha256': hashlib.sha256(text.encode()).hexdigest(), 'actual_charge_usd': 0,
              'charge_note': 'Codex subscription; usd_equivalent is Standard API-equivalent at the saved rates.'}
    f = session_file(thread)
    if f:
        rec = account.session(f, '')
        record.update(session_file=str(f), usd_equivalent=rec['usd'], requests=rec['requests'],
                      max_request_input_tokens=rec['max_request_input'],
                      over_context_cap=rec['max_request_input'] > CONTEXT_CAP)
    dump(out / 'run.json', record)
    cap = record.get('max_request_input_tokens')
    return (f"{agent}: rc {p.returncode}, completed {completed}, commands {commands}, "
            f"max request {cap if cap is not None else '?'} tokens, ${record.get('usd_equivalent', 0):.4f} equivalent")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('spawn', nargs='+')
    parser.add_argument('--jobs', type=int, default=7)
    a = parser.parse_args()
    if a.jobs > 7:
        parser.error('At most seven agents at a time')
    files = [Path(s) if Path(s).is_absolute() else ROOT / s for s in a.spawn]
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.jobs) as pool:
        for line in pool.map(run, files):
            print(line, flush=True)


if __name__ == '__main__':
    main()
