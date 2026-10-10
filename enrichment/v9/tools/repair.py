#!/usr/bin/env python3
"""Portable same-session repair for Tier 1, rechecks, maps and map translations.

Called by repair_*.sh. Saves every request, event stream and result; never creates a
new model session. A changed/missing source requires a new build, not a repair.
"""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'enrichment/v7'))
import digest
import account


def session_root(name, default):
    path = Path(os.environ.get(name, str(default))).expanduser()
    return path if path.is_absolute() else ROOT / path


def unit(stage, run, selection, update=None, tag=None):
    if not run or Path(run).name != run or run in ('.', '..'):
        raise ValueError('RUN must be a single directory name')
    if stage in ('t1', 'recheck', 'maptr'):
        n = int(selection)
        if n < 1 or update is not None:
            raise ValueError('a positive chunk number is required; no update argument')
        if stage == 'maptr':
            d = ROOT / 'enrichment/v9/work' / run / 'maptr'
            m = json.loads((d / 'manifest.json').read_text())
            tag = tag or m['tag']
            if tag != m['tag']:
                raise ValueError('model tag is not in this translation run')
            model = m['model']
            key = f'c{n:03d}'
            agent = f'v9t_{run}_{tag}_{key}'
            script = ROOT / 'enrichment/v9/maptr.py'
            args = ['--chunk', str(n)]
        else:
            base = 'work' if stage == 't1' else 'recheck'
            d = ROOT / 'enrichment/v7' / base / run
            m = json.loads((d / 'manifest.json').read_text())
            tag = tag or 'luna-max'
            specs = {digest.tag_of(*s.split(':')): s for s in m['models']}
            if tag not in specs:
                raise ValueError('model tag is not in this run')
            model = specs[tag]
            key = f'c{n:02d}'
            agent = f'v7d_{run}_{tag}_{key}'
            script = ROOT / f'enrichment/v7/{"digest" if stage == "t1" else "recheck"}.py'
            args = ['--model', tag, '--chunk', str(n)]
        if not any(c['chunk'] == n for c in m['chunks']):
            raise ValueError(f'unknown chunk: {n}')
        output = d / 'out' / tag / f'{key}.jsonl'
    else:
        if not digest.verse_list(selection) or digest.verse_list(selection) != [selection]:
            raise ValueError('a single S:A verse is required')
        d = ROOT / 'enrichment/v9/work' / run / 'map'
        m = json.loads((d / 'manifest.json').read_text())
        tag = tag or 'sol-high'
        specs = {digest.tag_of(*s.split(':')): s for s in m['models']}
        p = next((p for p in m['ayat'] if p['ayah'] == selection and not p.get('superseded_by')), None)
        if p is None:
            raise ValueError('verse is absent or superseded in this run')
        key = selection.replace(':', '-')
        if update is not None:
            u = next((u for u in p.get('updates', []) if u['n'] == int(update) and u['tag'] == tag), None)
            if u is None:
                raise ValueError('unknown update for this verse/model')
            model = u['model']
            agent = f'v9u_{run}_{tag}_{key}_u{u["n"]}'
            output = d / 'out' / tag / f'{key}.u{u["n"]}.raw.jsonl'
        else:
            if tag not in specs:
                raise ValueError('model tag is not in this run')
            model = specs[tag]
            agent = f'v9m_{run}_{tag}_{key}'
            output = d / 'out' / tag / f'{key}.raw.jsonl'
        script = ROOT / 'enrichment/v9/map.py'
        args = ['--model', tag, '--ayah', selection]
    return d / 'runs' / agent, output, model.split(':')[1], [sys.executable, '-B', str(script), 'check', run, *args]


def events(path):
    out = []
    for line in path.read_text().splitlines() if path.exists() else []:
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if isinstance(event, dict):
            out.append(event)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('stage', choices=['t1', 'recheck', 'map', 'maptr'])
    ap.add_argument('run')
    ap.add_argument('selection')
    ap.add_argument('update', nargs='?')
    ap.add_argument('--tag')
    a = ap.parse_args()
    directory, output, effort, checker = unit(a.stage, a.run, a.selection, a.update, a.tag)
    if not directory.is_dir():
        raise ValueError(f'{directory}: no original session directory; no repair launched')
    original = digest.run_record(directory)
    lock = directory / '.repair.lock'
    try:
        lock.mkdir()
    except FileExistsError:
        raise ValueError(f'{directory}: a repair is already active, or its lock needs recovery')
    try:
        (lock / 'pid').write_text(str(os.getpid()))
        stream = events(directory / 'stream.jsonl')
        thread = next((e.get('thread_id') for e in stream if e.get('type') == 'thread.started'), None)
        if not thread:
            raise ValueError('original stream has no thread id; no repair launched')
        live_processes = subprocess.run(['ps', '-ax', '-o', 'command='], capture_output=True, text=True, check=True).stdout
        if any(thread in line and 'codex exec' in line for line in live_processes.splitlines()):
            raise ValueError('this session is still running; no second resume launched')
        # A missing original result can mean the first call is still active. A terminal
        # stream event permits recovery of a dead runner; a live turn must not be resumed.
        if not any(e.get('type') in ('turn.completed', 'turn.failed', 'error') for e in stream):
            raise ValueError('original stream has no terminal event; recover the runner before repairing')
        # repairN.stream.jsonl, or the oldest wrappers' unnumbered repair.stream.jsonl (digest.run_record: repair 0)
        if any(directory.glob('repair*.stream.jsonl')) and original is None:
            raise ValueError('latest repair has no completed result; recover it before repairing again')
        check = subprocess.run(checker, cwd=ROOT, capture_output=True, text=True)
        problems = (check.stdout + check.stderr).strip()
        print(problems, flush=True)
        if check.returncode == 0 and digest.completed_record(original):
            print('No repair needed; checker passed. No session resumed.')
            return 0
        if check.returncode == 0:
            problems += ('\nThe output passes, but the original session/latest repair did not complete successfully. '
                         'Keep valid output unchanged, run the checker, and finish this same session.')
        rebuild = ('changed since', 'missing from current corpus', 'legacy input snapshot unavailable',
                   'missing source provenance', 'missing CHECK', 'rebuild with --supersede',
                   'rebuild this chunk')
        if any(message in problems for message in rebuild) or 'Traceback (most recent call last)' in problems:
            raise ValueError('checker requires a rebuild or workflow repair; no model session resumed')
        live = session_root('CODEX_SESSIONS_DIR', Path.home() / '.codex/sessions')
        archive = session_root('CODEX_SESSIONS_ARCHIVE_DIR', ROOT / '.scratch/codex_sessions_archive')
        session = next(live.rglob(f'*{thread}.jsonl'), None)
        if session is None:
            archived = next(archive.rglob(f'*{thread}.jsonl'), None)
            if archived is None:
                raise ValueError(f'session {thread} not found in live or archive directories')
            session = live / archived.relative_to(archive)
            session.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(archived, session)
        n = max([0] + [int(f.name.split('.')[0][6:]) for f in directory.glob('repair*.*')
                       if f.name.split('.')[0][6:].isdigit()]) + 1
        prefix = directory / f'repair{n}'
        prompt = (f'Repair your existing session. Reread only your assigned input parts and read/edit only '
                  f'your own output file {output.relative_to(ROOT)}. Do not change any other files.\n\n'
                  f'The full checker output is:\n{problems}\n\n'
                  'Fix every listed output problem using the original brief and source body. Stop if a source '
                  'changed or disappeared, or a problem requires rebuilding inputs; you cannot repair that. '
                  'Never invent anchors or duplicate existing notes. Recheck until OK, then reply with one line.\n'
                  f'Checker command: {sys.executable} -B {Path(checker[2]).relative_to(ROOT)} '
                  + ' '.join(checker[3:]) + '\n')
        prefix.with_suffix('.message.txt').write_text(prompt)
        started = time.strftime('%Y-%m-%dT%H:%M:%S')
        command = ['codex', 'exec', 'resume', '--ignore-user-config', '-c', f'model_reasoning_effort="{effort}"',
                   '-c', 'web_search="disabled"', '-c', 'sandbox_mode="workspace-write"', '--skip-git-repo-check',
                   '--json', '-o', str(prefix.with_suffix('.last.txt')), thread, '-']
        with prefix.with_suffix('.stream.jsonl').open('w') as stdout, prefix.with_suffix('.stderr.txt').open('w') as stderr:
            proc = subprocess.run(command, input=prompt, text=True, cwd=ROOT, stdout=stdout, stderr=stderr)
        evs = events(prefix.with_suffix('.stream.jsonl'))
        terminal = next((e for e in reversed(evs) if e.get('type') in ('turn.completed', 'turn.failed', 'error')), {})
        record = {**(original or {}), 'returncode': proc.returncode,
                  'turn_completed': terminal.get('type') == 'turn.completed', 'thread_id': thread,
                  'completion_via': f'repair{n}.run.json', 'repair_cost_unknown': False,
                  'repair_started': started, 'ended': time.strftime('%Y-%m-%dT%H:%M:%S'),
                  'repair_prompt_sha256': hashlib.sha256(prompt.encode()).hexdigest()}
        try:
            cost = account.session(session, '')
            record.update(usd_equivalent=cost['usd'], requests=cost['requests'],
                          max_request_input_tokens=cost['max_request_input'])
        except (OSError, ValueError):
            record['repair_cost_unknown'] = True
        digest.dump(prefix.with_suffix('.run.json'), record)
        result = subprocess.run(checker, cwd=ROOT)
        print(f'repair{n}: session rc {proc.returncode}, checker rc {result.returncode}')
        return 0 if digest.completed_record(record) and result.returncode == 0 else 1
    finally:
        (lock / 'pid').unlink(missing_ok=True)
        lock.rmdir()


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        sys.exit(1)
