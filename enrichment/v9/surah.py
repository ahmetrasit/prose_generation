#!/usr/bin/env python3
"""Enrichment v9 production driver for one surah: plan, page builds, agent prompts, status, finish. Launches no
model. RUNBOOK.md says when to run each command and how to spawn the agents.

  surah.py plan S [--date YYYYMMDD]   pages (base r13 readings, never augment), every verse they cite, run names,
                                      expected cost → work/prod_sNNN/{plan.json,verses.txt}
  surah.py pages S                    writer and meal runs for every ayah page (refuses while a cited verse lacks a map)
  surah.py agents S                   the Opus agent prompts for every page run not yet run → work/prod_sNNN/agents.md
  surah.py status S                   what is done and what is missing, stage by stage
  surah.py finish S                   checks every page run, renders each page (md, strip check) and the surah HTML

Costs (API-equivalent, measured on the 103:1 test): tier 1 ≈ $0.16/verse + quotation packet ≈ $0.09/verse (Luna);
verse map ≈ $0.32/verse (Sol); map translation ≈ $0.03/verse (Luna); writer ≈ $4/page and meal ≈ $0.4/page (Opus).
"""
import argparse
import contextlib
import io
import json
import subprocess
import sys
import time
from pathlib import Path

V9 = Path(__file__).resolve().parent
ROOT = V9.parents[1]
sys.path.insert(0, str(V9))
import writer  # noqa: E402
import q as Q  # noqa: E402

OPUS = 'claude-opus-5-5:high'


def pdir(s):
    return V9 / 'work' / f'prod_s{s:03d}'


def pages_of(s):
    out = {}
    for d in sorted((ROOT / '_commentary/v16/out').glob(f'{s}_*')):
        a = int(d.name.split('_')[1])
        fs = [f for f in d.glob(f'*/{s}_{a}.reading.tr.md') if 'augment' not in str(f.relative_to(d))]
        if len(fs) != 1:
            print(f'WARNING {s}:{a}: {len(fs)} base readings found; page left out until resolved: {fs}')
            continue
        out[f'{s}:{a}'] = str(fs[0].relative_to(ROOT))
    return dict(sorted(out.items(), key=lambda kv: int(kv[0].split(':')[1])))


def load(s):
    f = pdir(s) / 'plan.json'
    if not f.exists():
        raise SystemExit(f'no plan for S{s}: run `surah.py plan {s}` first')
    return json.loads(f.read_text())


def plan(a):
    d = pdir(a.surah)
    if (d / 'plan.json').exists():
        raise SystemExit(f'{d / "plan.json"} exists')
    date = a.date or time.strftime('%Y%m%d')
    pages = pages_of(a.surah)
    if a.pages:
        for k in a.pages:
            if k not in pages:
                print(f'WARNING {k}: not a page with one base reading; left out')
        pages = {k: v for k, v in pages.items() if k in a.pages}
    verses, paras = set(), 0
    for ayah, path in pages.items():
        with contextlib.redirect_stdout(io.StringIO()):
            _, ps, _, cites = writer.write7.page(path, ayah)
        paras += len(ps)
        verses |= {v for vs in cites.values() for v in vs}
    verses = sorted(verses, key=lambda x: tuple(map(int, x.split(':'))))
    mapped = [v for v in verses if Q.located(v)]
    k = f's{a.surah:03d}'
    p = {'surah': a.surah, 'date': date, 'pages': pages, 'verses': verses,
         'runs': {'tier1': f't1_{k}_{date}', 'maps': f'map_{k}_{date}', 'maptr': f'tr_{k}_{date}',
                  'writer': {x: f'w_{x.replace(":", "_")}_{date}' for x in pages},
                  'meal': {x: f'meal_{x.replace(":", "_")}_{date}' for x in pages}}}
    d.mkdir(parents=True)
    (d / 'plan.json').write_text(json.dumps(p, ensure_ascii=False, indent=1))
    (d / 'verses.txt').write_text(' '.join(verses) + '\n')
    new = len(verses) - len(mapped)
    print(f"S{a.surah}: {len(pages)} pages, {paras} paragraphs, {len(verses)} verses cited ({len(mapped)} already mapped)")
    print(f"expected cost (API-equivalent): tier 1 ≤ ${0.25 * len(verses):.0f} (less where already digested), maps "
          f"${0.32 * new:.0f}, translation ${0.03 * len(verses):.0f}, writers ${4 * len(pages):.0f}, meals ${0.4 * len(pages):.0f}")
    print(f'runs: {json.dumps(p["runs"]["tier1"])}, {p["runs"]["maps"]}, {p["runs"]["maptr"]}; verses in {(d / "verses.txt").relative_to(ROOT)}')


def pages(a):
    p = load(a.surah)
    for ayah, path in p['pages'].items():
        for kind, run, script in (('writer', p['runs']['writer'][ayah], 'writer.py'), ('meal', p['runs']['meal'][ayah], 'meal.py')):
            stage = 'write' if kind == 'writer' else 'meal'
            if (V9 / 'work' / run / stage).exists():
                print(f'SKIPPED {ayah} {kind}: {run} exists')
                continue
            r = subprocess.run([sys.executable, '-B', str(V9 / script), 'build', run, '--ayah', ayah, '--page', path,
                                '--model', OPUS], capture_output=True, text=True, cwd=ROOT)
            print((r.stdout + r.stderr).strip().splitlines()[-1] if (r.stdout + r.stderr).strip() else f'{ayah} {kind}: no output')
            if r.returncode:
                print(f'WARNING {ayah} {kind}: build failed (exit {r.returncode})')


def agent_line(run, stage):
    spawn = V9 / 'work' / run / stage / 'spawn' / 'opus-high.md'
    header = spawn.read_text().splitlines()[0]
    out = f'enrichment/v9/work/{run}/{stage}/out/opus-high/'
    return header, (f"{header}\nYour prompt.md is `{spawn.relative_to(ROOT)}` (paths are relative to the repository root "
                    f"{ROOT}). Read it and follow it exactly, including its final pass. Write only the output files it "
                    f"names, inside `{out}`. When done, reply with one line.")


def ran(header, run, stage):
    """True when the agent has a transcript (so it is never spawned twice). A transcript that is not completed (still
    running, or interrupted) or whose output fails the check is printed as a WARNING: resume that same agent, do not
    spawn a new one."""
    agent = header.split()[2]
    u = writer.digest.claude_usage(agent)
    if u is None:
        return False
    if not u['completed']:
        print(f'WARNING {run} {stage}: transcript not completed (still running, or interrupted: resume the same agent); not listed')
        return True
    ok, last = check_run('writer.py' if stage == 'write' else 'meal.py', run)
    if not ok:
        print(f'WARNING {run} {stage}: finished but the check fails ({last}); resume the same agent; not listed')
    return True


def agents(a):
    p = load(a.surah)
    out = [f'# S{a.surah}: Opus agent prompts (agent type `enrich-page-high`, one per block below)', '']
    n = 0
    for ayah in p['pages']:
        for run, stage in ((p['runs']['writer'][ayah], 'write'), (p['runs']['meal'][ayah], 'meal')):
            if not (V9 / 'work' / run / stage / 'spawn' / 'opus-high.md').exists():
                out += [f'## {ayah} {stage}: NOT BUILT (run `surah.py pages {a.surah}`)', '']
                continue
            header, text = agent_line(run, stage)
            if ran(header, run, stage):
                continue
            n += 1
            out += [f'## {ayah} {stage}', '```', text, '```', '']
    (pdir(a.surah) / 'agents.md').write_text('\n'.join(out) + '\n')
    print(f'{n} agent prompt(s) in {(pdir(a.surah) / "agents.md").relative_to(ROOT)}')


def check_run(script, run):
    r = subprocess.run([sys.executable, '-B', str(V9 / script), 'check', run], capture_output=True, text=True, cwd=ROOT)
    return r.returncode == 0, ((r.stdout + r.stderr).strip().splitlines() or ['no output'])[-1]


def status(a):
    p = load(a.surah)
    t1 = ROOT / 'enrichment/v7/work' / p['runs']['tier1'] / 'manifest.json'
    print(f"tier 1 {p['runs']['tier1']}: {'built' if t1.exists() else 'not built'}")
    missing = [v for v in p['verses'] if not Q.located(v)]
    print(f"maps: {len(p['verses']) - len(missing)} of {len(p['verses'])} verses mapped" + (f"; missing {' '.join(missing[:20])}{' …' if len(missing) > 20 else ''}" if missing else ''))
    import maptr
    stale = 0
    same = {k.replace('-', ':') for k in Q.mapped() if k.split('-')[0] == str(a.surah)}
    not_current = []
    for v in sorted(set(p['verses']) | same, key=lambda x: tuple(map(int, x.split(':')))):
        qs, _, why = Q.load_current(v)
        if why:
            not_current.append(f'{v} ({why})')
        if qs:
            tr = Q.translation(v)
            stale += sum(1 for q in qs if tr.get(q['id'], {}).get('src') != maptr.qhash(q))
    print(f'map questions without a current Turkish rendering (cited verses and every mapped verse of S{a.surah}): {stale}')
    if not_current:
        print(f'maps not current (run map.py check on their run), not counted above: {len(not_current)}: '
              + '; '.join(not_current[:10]) + (' …' if len(not_current) > 10 else ''))
    for ayah in p['pages']:
        cells = []
        for run, stage, script in ((p['runs']['writer'][ayah], 'write', 'writer.py'), (p['runs']['meal'][ayah], 'meal', 'meal.py')):
            if not (V9 / 'work' / run / stage).exists():
                cells.append(f'{stage}: not built')
                continue
            ok, last = check_run(script, run)
            cells.append(f"{stage}: {'OK' if ok else last}")
        print(f'{ayah}: ' + ' | '.join(cells))


def finish(a):
    p = load(a.surah)
    d = pdir(a.surah)
    with contextlib.redirect_stdout(io.StringIO()) as buf:
        now = pages_of(a.surah)
    for x in buf.getvalue().splitlines():
        print(x)
    for k in now:
        if k not in p['pages']:
            print(f'WARNING {k}: has a base reading but is not in the plan; not rendered')
    bad = []
    for ayah in p['pages']:
        w, m = p['runs']['writer'][ayah], p['runs']['meal'][ayah]
        okw, lw = check_run('writer.py', w)
        okm, lm = check_run('meal.py', m)
        if not (okw and okm):
            bad.append(f'{ayah}: writer {lw}; meal {lm}')
            continue
        for cmd in (['render.py', w, '--meal', m],
                    ['page_html.py', w, '--meal', m, '--out', str(d / f"{ayah.replace(':', '_')}.html")]):
            r = subprocess.run([sys.executable, '-B', str(V9 / cmd[0])] + cmd[1:], capture_output=True, text=True, cwd=ROOT)
            print((r.stdout + r.stderr).strip())
            if r.returncode:
                bad.append(f'{ayah}: {cmd[0]} failed')
                break
        else:
            h = d / f"{ayah.replace(':', '_')}.html"
            n = h.read_text(encoding='utf-8').count('· İngilizce (çevir') if h.exists() else 0
            if n:
                print(f'WARNING {ayah}: {n} map question(s) shown in English only (no current Turkish rendering: missing or stale)')
    for x in bad:
        print(f'WARNING {x}')
    print(f"{len(p['pages']) - len(bad)} of {len(p['pages'])} pages rendered into {d.relative_to(ROOT)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    x = sub.add_parser('plan'); x.add_argument('surah', type=int); x.add_argument('--date'); x.add_argument('--pages', nargs='+', help='only these ayah pages, e.g. 103:2 103:3')
    for c in ('pages', 'agents', 'status', 'finish'):
        sub.add_parser(c).add_argument('surah', type=int)
    a = ap.parse_args()
    {'plan': plan, 'pages': pages, 'agents': agents, 'status': status, 'finish': finish}[a.cmd](a)


if __name__ == '__main__':
    main()
