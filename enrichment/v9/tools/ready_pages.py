#!/usr/bin/env python3
"""Which pages of a surah can start while its verse maps are still running. Launches no model.

A verse is ready when the map run that holds it (not superseded) has a finished agent (run.json) for the map and for
every update built for it, and map.py's checks pass over the whole (`combined`). A ready verse whose assembled map is
missing or older than its agent outputs is assembled here (as `map.py check` would). A writer is ready when every
verse its page cites is ready; a meal when its focus ayah is.

  ready_pages.py S [--build] [--fresh]
      --build: assemble ready verses and run writer.py/meal.py build for every ready page not built yet (without it,
               nothing is written: a verse that still needs assembling is listed as READY (needs assemble))
      --fresh: also compare each verse's saved notes with tier 1 (one slow pass): notes added or changed since mapping
               make it WAIT until `map.py update-all` has run and its update agent finished; notes no longer in tier 1
               do not (map.py check marks them). Without it, run update-all after tier 1.
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
import q as Q  # noqa: E402
import surah  # noqa: E402
import writer  # noqa: E402

TAG = 'sol-high'
NEEDS_ASSEMBLE = set()   # ready verses whose assembled map is missing or older than their outputs (listing only)


def holders():
    """verse -> (run, manifest entry) of the non-superseded map run that lists it; a verse listed by two such runs is
    printed (the newest manifest is used, and ready() requires q.located() to agree)."""
    out, seen = {}, {}
    for f in sorted((V9 / 'work').glob('*/map/manifest.json'), key=lambda x: x.stat().st_mtime):
        run = f.parents[1].name
        for p in json.loads(f.read_text())['ayat']:
            if not p.get('superseded_by'):
                if p['ayah'] in seen:
                    print(f"WARNING {p['ayah']}: listed by two map runs ({seen[p['ayah']]}, {run})")
                seen[p['ayah']] = run
                out[p['ayah']] = (run, p)
    return out


_CURRENT = {}   # tier-1 tags -> verse -> rows, read in one pass for every verse the map runs hold


def fresh_problem(ayah, run, p, held):
    """Notes in tier 1 that the verse's map has not placed yet: new notes, and new versions of changed notes (an update
    not built yet). Unavailable or changed saved notes do not block; map.py check marks them (map.reconcile)."""
    import merge
    m = M.mdir(run)
    man = json.loads((m / 'manifest.json').read_text())
    tags = tuple(man['from'])
    if tags not in _CURRENT:
        _CURRENT[tags] = merge.tier1_rows_by_verse(list(tags), sorted(held))
    current = {r['id']: r for r in _CURRENT[tags][ayah]}       # ready() passes only verses in held
    saved = json.loads((m / 'rows' / f'{M.key(ayah)}.json').read_text())
    marks, _, offer, new = M.reconcile(saved, current)
    pulled = sum(1 for x in marks.values() if x['state'] == 'unavailable')
    if pulled:
        print(f'NOTE {ayah}: {pulled} saved note(s) no longer in tier 1; kept and marked by map.py check')
    if offer or new:
        return f'{run}: {len(new)} new and {len(offer)} changed tier-1 note(s) not placed yet (run map.py update-all)'
    return None


def ready(ayah, held, cache, build=False, fresh=False):
    if ayah in cache:
        return cache[ayah]
    if ayah not in held:
        cache[ayah] = 'no map run lists it (not built yet, or no tier-1 notes: never mapped)'
        return cache[ayah]
    run, p = held[ayah]
    m = M.mdir(run)
    ups = [u for u in p.get('updates', []) if u['tag'] == TAG]
    agents = [M.agent_name(run, TAG, ayah)] + [M.agent_name(run, TAG, ayah, u['n']) for u in ups]
    for ag in agents:
        directory = m / 'runs' / ag.split('/')[-1]
        if not M.digest.completed_record(M.digest.run_record(directory)):
            cache[ayah] = f'{run}: {ag.split("/")[-1]} not finished'
            return cache[ayah]
    problems, qs = M.combined(m, TAG, ayah, p.get('updates', []))
    if problems:
        cache[ayah] = f'{run}: {len(problems)} check problem(s), e.g. {problems[0]}'
        return cache[ayah]
    if fresh:
        x = fresh_problem(ayah, run, p, held)
        if x:
            cache[ayah] = x
            return x
    k = M.key(ayah)
    out = m / 'out' / TAG / f'{k}.jsonl'
    raws = [m / 'out' / TAG / f'{k}.raw.jsonl'] + [m / 'out' / TAG / f"{k}.u{u['n']}.raw.jsonl" for u in ups]
    stamp = out.with_suffix('.stamp.json')
    needs_assemble = (not out.exists() or out.stat().st_mtime < max(r.stat().st_mtime for r in raws)
                      or (stamp.exists() and json.loads(stamp.read_text()) != M.assembly_stamp(m, TAG, ayah, ups)))
    if needs_assemble:
        if not build:
            NEEDS_ASSEMBLE.add(ayah)
            cache[ayah] = True
            return True
        M.assemble(m, TAG, ayah, qs)
    loc = Q.located(ayah)
    if not loc or loc[0] != out:
        cache[ayah] = f'q.located() reads {loc[0] if loc else None}, not {out}'
        return cache[ayah]
    cache[ayah] = True
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('surah', type=int)
    ap.add_argument('--build', action='store_true')
    ap.add_argument('--fresh', action='store_true')
    a = ap.parse_args()
    plan = surah.load(a.surah)
    held, cache, todo = holders(), {}, []
    for ayah, path in plan['pages'].items():
        with contextlib.redirect_stdout(io.StringIO()):
            _, _, _, cites = writer.write7.page(path, ayah)
        # the page's own verse too: writer.py build requires its map (it is the focus map)
        verses = sorted({ayah} | {v for vs in cites.values() for v in vs}, key=lambda x: tuple(map(int, x.split(':'))))
        for kind, run, stage, need in (('writer', plan['runs']['writer'][ayah], 'write', verses),
                                       ('meal', plan['runs']['meal'][ayah], 'meal', [ayah])):
            if (V9 / 'work' / run / stage).exists():
                if (V9 / 'work' / run / stage / 'spawn' / 'opus-high.md').exists():
                    print(f'BUILT {ayah} {kind}')
                else:
                    print(f'WARNING {ayah} {kind}: INCOMPLETE BUILD (work/{run}/{stage} exists without a spawn file); '
                          'remove it and build again')
                continue
            waiting = [(v, ready(v, held, cache, a.build, a.fresh)) for v in need]
            waiting = [(v, r) for v, r in waiting if r is not True]
            if waiting:
                print(f'WAIT {ayah} {kind}: {len(waiting)} of {len(need)} verse(s) not ready, e.g. {waiting[0][0]} ({waiting[0][1]})')
            else:
                print(f'READY {ayah} {kind}' + (' (needs assemble)' if NEEDS_ASSEMBLE & set(need) else ''))
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
