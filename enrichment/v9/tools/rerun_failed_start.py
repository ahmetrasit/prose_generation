#!/usr/bin/env python3
"""Move proven failures before session creation (no thread, usage or completed items) to
<runs>_failed_start/ (evidence kept; a later move adds a numeric suffix) and print how many.
Their spawn files can then be run again with codex_run.py. Zero shell commands alone is insufficient.

  rerun_failed_start.py RUNS_DIR [RUNS_DIR …]
"""
import json, shutil, sys
from pathlib import Path


def failed_before_session(record, directory):
    """Zero shell commands does not prove that no model/file-writing work happened."""
    if (not isinstance(record, dict) or record.get('returncode') in (None, 0)
            or record.get('turn_completed') is not False or record.get('commands') != 0
            or record.get('thread_id') or record.get('requests') or record.get('usd_equivalent')
            or record.get('usage') and any(record['usage'].values())):
        return False
    stream = directory / 'stream.jsonl'
    if not stream.exists():
        return False
    for line in stream.read_text().splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            return False                  # interrupted/unknown evidence is never an automatic retry
        if not isinstance(event, dict) or event.get('type') != 'error':
            return False
    return not any(directory.glob('repair*.*'))


def main(paths):
    for runs in map(Path, paths):
        recover(runs)


def recover(runs):
    if not runs.is_dir():
        raise ValueError(f'{runs}: no runs directory')
    dest = runs.with_name(runs.name + '_failed_start')
    n = 0
    for f in sorted(runs.glob('*/run.json')):
        try:
            r = json.loads(f.read_text())
        except ValueError:
            print(f'WARNING {f}: unreadable run.json (being written, or corrupt); left alone')
            continue
        if failed_before_session(r, f.parent) and not (f.parent / '.repair.lock').exists():
            dest.mkdir(exist_ok=True)
            target, k = dest / f.parent.name, 1
            while target.exists():
                k += 1
                target = dest / f'{f.parent.name}.{k}'
            shutil.move(str(f.parent), target)
            n += 1
    print(f'{runs}: {n} agent(s) that failed at start moved to {dest.name}')


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            raise ValueError('usage: rerun_failed_start.py RUNS_DIR [RUNS_DIR ...]')
        main(sys.argv[1:])
    except (OSError, ValueError) as exc:
        print(f'WARNING {exc}', file=sys.stderr)
        sys.exit(1)
