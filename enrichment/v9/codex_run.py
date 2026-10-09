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
    name = str(spawn)
    try:                                   # every failure becomes a printed WARNING line, never a lost result
        m = run_codex.HEADER.match(spawn.read_text())
        if not m:
            return f'WARNING {spawn}: no agent header; skipped'
        name = m.group(1)
        out = spawn.parent.parent / 'runs' / Path(name).name
        if (out / 'run.json').exists():
            return f'{name}: already run, skipped'
        out.parent.mkdir(parents=True, exist_ok=True)
        try:
            out.mkdir()                    # the claim is atomic: two runners never start the same agent
        except FileExistsError:
            if not retry:
                return f'WARNING {name}: started earlier without run.json (running or died); not started again'
            for f in out.iterdir():
                f.unlink()
        return run_codex.run(spawn)
    except Exception as e:
        return f'WARNING {name}: {type(e).__name__}: {e} (no run.json: recover_run_json.py records its cost)'


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('spawn', nargs='+')
    ap.add_argument('--parallel', type=int, required=True)
    ap.add_argument('--retry', action='store_true')
    a = ap.parse_args()
    files = list(dict.fromkeys(Path(s).resolve() for s in a.spawn))   # the same spawn file twice runs once
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.parallel) as pool:
        for line in pool.map(lambda f: one(f, a.retry), files):
            print(line, flush=True)


if __name__ == '__main__':
    main()
