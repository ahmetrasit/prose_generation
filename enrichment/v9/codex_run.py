#!/usr/bin/env python3
"""Run spawn files through `codex exec` (Luna, Sol) with a total parallelism the user approved. Each agent writes
<stage>/runs/<agent>/{stream.jsonl,last.txt,run.json} as enrichment/v5/run_codex.py does (its `run` is reused).

An agent that already has a run directory is never started again: with run.json it is done; without run.json it
is running or died, which is printed (rerun only with --retry, after the user's go and after checking no process
is still running it).

  python3 -B enrichment/v9/codex_run.py --parallel 40 SPAWN_FILE [SPAWN_FILE …] [--retry]
"""
import argparse
import concurrent.futures
import sys
from pathlib import Path

V9 = Path(__file__).resolve().parent
sys.path.insert(0, str(V9.parent / 'v5'))
import run_codex  # noqa: E402


def one(spawn, retry):
    m = run_codex.HEADER.match(spawn.read_text())
    if not m:
        return f'{spawn}: no agent header; skipped'
    out = spawn.parent.parent / 'runs' / m.group(1).rsplit('/', 1)[1]
    if (out / 'run.json').exists():
        return f'{m.group(1)}: already run, skipped'
    if out.exists() and not retry:
        return f'WARNING {m.group(1)}: started earlier without run.json (running or died); not started again'
    if out.exists():
        for f in out.iterdir():
            f.unlink()
    try:
        return run_codex.run(spawn)
    except Exception as e:  # recorded, never silent
        return f'WARNING {m.group(1)}: {type(e).__name__}: {e}'


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('spawn', nargs='+')
    ap.add_argument('--parallel', type=int, required=True)
    ap.add_argument('--retry', action='store_true')
    a = ap.parse_args()
    files = [Path(s).resolve() for s in a.spawn]
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.parallel) as pool:
        for line in pool.map(lambda f: one(f, a.retry), files):
            print(line, flush=True)


if __name__ == '__main__':
    main()
