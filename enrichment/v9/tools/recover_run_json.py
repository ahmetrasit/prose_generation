#!/usr/bin/env python3
"""Write run.json for agents whose codex_run.py runner was stopped while they ran (the agent itself finished: its
stream.jsonl has turn.completed or turn.failed and no codex process writes to that run dir any more). Same fields as
enrichment/v5/run_codex.py, plus "recovered": true. The session file is looked up in ~/.codex/sessions and in the
archive /Volumes/aro/codex_sessions_archive. Agents still running or with no ending are listed and left alone.

  recover_run_json.py RUNS_DIR [RUNS_DIR …]
"""
import hashlib, json, re, subprocess, sys, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'enrichment/v5'))
import account  # noqa: E402
from common import CONTEXT_CAP, dump  # noqa: E402
HEADER = re.compile(r'^<!-- agent (\S+) \| model (\S+) \| effort (\S+) -->')
live = subprocess.run(['ps', '-ax', '-o', 'command='], capture_output=True, text=True).stdout
for runs in map(Path, sys.argv[1:]):
    fixed, open_ = 0, []
    for d in sorted(p for p in runs.iterdir() if p.is_dir() and not (p / 'run.json').exists()):
        if f'{d.name}/' in live:
            open_.append(f'{d.name}: still running')
            continue
        evs = []
        for line in (d / 'stream.jsonl').read_text().splitlines() if (d / 'stream.jsonl').exists() else []:
            try:
                evs.append(json.loads(line))
            except ValueError:
                pass
        thread = next((e.get('thread_id') for e in evs if e.get('type') == 'thread.started'), None)
        done = next((e for e in evs if e.get('type') in ('turn.completed', 'turn.failed')), None)
        if not done:
            open_.append(f'{d.name}: no turn ending in stream.jsonl (interrupted)')
            continue
        spawn = next((s for s in (runs.parent / 'spawn').glob('*.md') if HEADER.match(s.read_text()) and
                      HEADER.match(s.read_text()).group(1).endswith('/' + d.name)), None)
        agent, model, effort = HEADER.match(spawn.read_text()).groups() if spawn else (d.name, '?', '?')
        commands = sum(1 for e in evs if e.get('type') == 'item.completed' and (e.get('item') or {}).get('type') == 'command_execution')
        rec = {'agent': agent, 'model': model, 'effort': effort, 'started': None,
               'ended': time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime((d / 'stream.jsonl').stat().st_mtime)),
               'returncode': 0 if done['type'] == 'turn.completed' else 1, 'turn_completed': done['type'] == 'turn.completed',
               'thread_id': thread, 'commands': commands, 'usage': done.get('usage') or {}, 'stderr': '',
               'prompt_sha256': hashlib.sha256(spawn.read_text().encode()).hexdigest() if spawn else None,
               'actual_charge_usd': 0, 'recovered': True,
               'charge_note': 'Codex subscription; usd_equivalent is Standard API-equivalent at the saved rates. '
                              'run.json written by recover_run_json.py: the runner was stopped while the agent ran.'}
        f = next((p for base in (Path.home() / '.codex/sessions', Path('/Volumes/aro/codex_sessions_archive'))
                  for p in base.glob(f'*/*/*/*{thread}.jsonl')), None) if thread else None
        if f:
            s = account.session(f, '')
            rec.update(session_file=str(f), usd_equivalent=s['usd'], requests=s['requests'],
                       max_request_input_tokens=s['max_request_input'], over_context_cap=s['max_request_input'] > CONTEXT_CAP)
        else:
            print(f'WARNING {d.name}: no session file found; cost unknown')
        dump(d / 'run.json', rec)
        fixed += 1
    print(f'{runs}: {fixed} run.json written; {len(open_)} left alone')
    for x in open_:
        print('  ' + x)
