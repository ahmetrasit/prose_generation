#!/usr/bin/env python3
"""Move agents that failed before running any command (rc != 0, 0 commands: network timeout or full disk at start,
$0) to <runs>_failed_start/ (evidence kept; a later move adds a numeric suffix) and print how many. Their spawn files
can then be run again with codex_run.py. Never touches an agent that ran a command.

  rerun_failed_start.py RUNS_DIR [RUNS_DIR …]
"""
import json, shutil, sys
from pathlib import Path
for runs in map(Path, sys.argv[1:]):
    dest = runs.with_name(runs.name + '_failed_start')
    n = 0
    for f in sorted(runs.glob('*/run.json')):
        try:
            r = json.loads(f.read_text())
        except ValueError:
            print(f'WARNING {f}: unreadable run.json (being written, or corrupt); left alone')
            continue
        if (r.get('returncode') or not r.get('turn_completed')) and not r.get('commands'):
            dest.mkdir(exist_ok=True)
            target, k = dest / f.parent.name, 1
            while target.exists():
                k += 1
                target = dest / f'{f.parent.name}.{k}'
            shutil.move(str(f.parent), target)
            n += 1
    print(f'{runs}: {n} agent(s) that failed at start moved to {dest.name}')
