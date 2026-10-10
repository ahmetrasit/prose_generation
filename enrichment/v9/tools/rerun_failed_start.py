#!/usr/bin/env python3
"""Move agents that failed before any model request to <runs>_failed_start/ (evidence kept; a later move adds a
numeric suffix) and print how many. Their spawn files can then be run again with codex_run.py.

Proof of a failure before any model request (all of it): the run ended failed (returncode != 0, turn not completed);
its record shows no request, no usage and no cost; and its event stream holds only session/turn start, error events,
error items and the final turn.failed: no command, file change, message or reasoning item; and every error names a
known failure that happens before any request is sent (PRE_REQUEST: codex_run's run.json records no request count,
so an unknown disconnect could follow a billed request; it is left for review and same-session repair). A thread id alone proves
nothing (Codex opens the thread before the first request; every network failure recorded so far has one, e.g.
"workspace routing discovery timed out"). Zero shell commands alone is not enough either.

  rerun_failed_start.py RUNS_DIR [RUNS_DIR …]
"""
import json, shutil, sys
from pathlib import Path

START_EVENTS = {'thread.started', 'turn.started', 'error', 'turn.failed'}
PRE_REQUEST = ('workspace routing discovery timed out',)   # every recorded startup failure through 2026-10-10 (396)


def pre_request(message):
    return isinstance(message, str) and any(x in message for x in PRE_REQUEST)


def failed_before_session(record, directory):
    """True only with positive evidence that no model request or file-writing work happened (see the module doc)."""
    if (not isinstance(record, dict) or record.get('returncode') in (None, 0)
            or record.get('turn_completed') is not False or record.get('commands') not in (0, None)
            or record.get('requests') or record.get('usd_equivalent')
            or (isinstance(record.get('usage'), dict) and any(record['usage'].values()))
            or (record.get('usage') and not isinstance(record.get('usage'), dict))):
        return False
    stream = directory / 'stream.jsonl'
    if not stream.exists():
        return False
    failed = False
    for line in stream.read_text().splitlines():
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except ValueError:
            return False                  # interrupted/unknown evidence is never an automatic retry
        if not isinstance(event, dict):
            return False
        kind = event.get('type')
        if kind == 'item.completed' or kind == 'item.started':
            item = event.get('item')
            if not isinstance(item, dict) or item.get('type') != 'error' or not pre_request(item.get('message')):
                return False
        elif kind not in START_EVENTS:
            return False
        elif kind == 'error' and not pre_request(event.get('message')):
            return False
        elif kind == 'turn.failed':
            error = event.get('error')
            if not pre_request(error.get('message') if isinstance(error, dict) else error):
                return False
        failed |= kind == 'turn.failed'
    return failed and not any(directory.glob('repair*.*'))


def main(paths):
    for runs in map(Path, paths):
        recover(runs)


def recover(runs):
    if not runs.is_dir():
        raise ValueError(f'{runs}: no runs directory')
    dest = runs.with_name(runs.name + '_failed_start')
    n, kept = 0, []
    for f in sorted(runs.glob('*/run.json')):
        try:
            r = json.loads(f.read_text())
            proven = failed_before_session(r, f.parent)
        except (OSError, ValueError) as e:
            print(f'WARNING {f}: unreadable run record or stream ({e}); left alone')
            continue
        if not proven and not (isinstance(r, dict) and r.get('turn_completed') is True and r.get('returncode') == 0):
            kept.append(f.parent.name)
        if proven and (f.parent / '.repair.lock').exists():
            kept.append(f'{f.parent.name} (repair lock held)')
        elif proven:
            dest.mkdir(exist_ok=True)
            target, k = dest / f.parent.name, 1
            while target.exists():
                k += 1
                target = dest / f'{f.parent.name}.{k}'
            shutil.move(str(f.parent), target)
            n += 1
    print(f'{runs}: {n} agent(s) that failed at start moved to {dest.name}')
    if kept:
        print(f'{runs}: {len(kept)} failed or unfinished agent(s) left in place (not proven to have failed before any '
              'request; review, then same-session repair): ' + ', '.join(kept[:20]) + (' …' if len(kept) > 20 else ''))


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise ValueError('usage: rerun_failed_start.py RUNS_DIR [RUNS_DIR ...]')
        main(sys.argv[1:])
    except (OSError, ValueError) as exc:
        print(f'WARNING {exc}', file=sys.stderr)
        sys.exit(1)
