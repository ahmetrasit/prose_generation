#!/usr/bin/env python3
"""Which pages of a surah can start while its verse maps are still running. Launches no model.

A verse is ready when the map run that holds it (not superseded) has a finished agent (run.json) for the map and for
every update built for it, and map.py's checks pass over the whole (`combined`). A ready verse whose assembled map is
missing or older than its agent outputs is assembled here (as `map.py check` would). A writer is ready when every
verse its page cites is ready; a meal when its focus ayah is.

  ready_pages.py S [--build]     --build: writer.py/meal.py build for every ready page not built yet
Prints READY / WAIT lines, then the pages built.
"""
import argparse
import contextlib
import io
import json
import subprocess
import sys
from pathlib import Path

V9 = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(V9))
import map as M  # noqa: E402
import surah  # noqa: E402
import writer  # noqa: E402

TAG = 'sol-high'


def holders():
    """verse -> (run, manifest entry) of the newest non-superseded map run that lists it."""
    out = {}
    for f in sorted((V9 / 'work').glob('*/map/manifest.json'), key=lambda x: x.stat().st_mtime):
        run = f.parents[1].name
        for p in json.loads(f.read_text())['ayat']:
            if not p.get('superseded_by'):
                out[p['ayah']] = (run, p)
    return out


def ready(ayah, held, cache):
    if ayah in cache:
        return cache[ayah]
    if ayah not in held:
        cache[ayah] = 'no map run lists it'
        return cache[ayah]
    run, p = held[ayah]
    m = M.mdir(run)
    ups = [u for u in p.get('updates', []) if u['tag'] == TAG]
    agents = [M.agent_name(run, TAG, ayah)] + [M.agent_name(run, TAG, ayah, u['n']) for u in ups]
    for ag in agents:
        if not (m / 'runs' / ag.split('/')[-1] / 'run.json').exists():
            cache[ayah] = f'{run}: {ag.split("/")[-1]} not finished'
            return cache[ayah]
    problems, qs = M.combined(m, TAG, ayah, p.get('updates', []))
    if problems:
        cache[ayah] = f'{run}: {len(problems)} check problem(s), e.g. {problems[0]}'
        return cache[ayah]
    k = M.key(ayah)
    out = m / 'out' / TAG / f'{k}.jsonl'
    raws = [m / 'out' / TAG / f'{k}.raw.jsonl'] + [m / 'out' / TAG / f"{k}.u{u['n']}.raw.jsonl" for u in ups]
    if not out.exists() or out.stat().st_mtime < max(r.stat().st_mtime for r in raws):
        M.assemble(m, TAG, ayah, qs)
    cache[ayah] = True
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('surah', type=int)
    ap.add_argument('--build', action='store_true')
    a = ap.parse_args()
    plan = surah.load(a.surah)
    held, cache, todo = holders(), {}, []
    for ayah, path in plan['pages'].items():
        with contextlib.redirect_stdout(io.StringIO()):
            _, _, _, cites = writer.write7.page(path, ayah)
        verses = sorted({v for vs in cites.values() for v in vs}, key=lambda x: tuple(map(int, x.split(':'))))
        for kind, run, stage, need in (('writer', plan['runs']['writer'][ayah], 'write', verses),
                                       ('meal', plan['runs']['meal'][ayah], 'meal', [ayah])):
            if (V9 / 'work' / run / stage).exists():
                print(f'BUILT {ayah} {kind}')
                continue
            waiting = [(v, ready(v, held, cache)) for v in need]
            waiting = [(v, r) for v, r in waiting if r is not True]
            if waiting:
                print(f'WAIT {ayah} {kind}: {len(waiting)} of {len(need)} verse(s) not ready, e.g. {waiting[0][0]} ({waiting[0][1]})')
            else:
                print(f'READY {ayah} {kind}')
                todo.append((ayah, path, kind, run))
    if a.build:
        for ayah, path, kind, run in todo:
            script = 'writer.py' if kind == 'writer' else 'meal.py'
            r = subprocess.run([sys.executable, '-B', str(V9 / script), 'build', run, '--ayah', ayah, '--page', path,
                                '--model', surah.OPUS], capture_output=True, text=True, cwd=surah.ROOT)
            last = (r.stdout + r.stderr).strip().splitlines()
            print(f"BUILD {ayah} {kind}: {'exit ' + str(r.returncode) + ' ' if r.returncode else ''}{last[-1] if last else 'no output'}")


if __name__ == '__main__':
    main()
