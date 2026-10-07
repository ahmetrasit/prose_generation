#!/usr/bin/env python3
"""Enrichment v7 tier 2: one consolidated view list per ayah, built from the tier-1 digest rows. Launches no model.

The agent groups every tier-1 row about the ayah into distinct views (each view once, with the row ids it covers);
the script fills in holders, sources and stances from those ids, so nothing is retyped. One check: every row id
is covered by at least one view, and no view names an unknown id.

  merge.py build RUN --from luna-max --ayat 100:1 87:6 --models gpt-6-luna:max
  merge.py check RUN [--model TAG] [--ayah 100:1]     the agent runs it with --ayah until OK
  merge.py report RUN                                   costs, views, rows, and a readable .md per ayah

Files: RUN/tier2/rows/<ayah>.pK.txt (input parts), RUN/tier2/spawn, RUN/tier2/runs, RUN/tier2/out/<TAG>/<ayah>.jsonl
"""
import argparse
import json
from collections import defaultdict

from digest import PART_CHARS, ROOT, V7, connect, dump, run_dir

BRIEF = V7 / 'briefs/merge.md'


def key(ayah):
    return ayah.replace(':', '-')


def tier1_rows(d, tag, ayah):
    """Every tier-1 row whose verses include the ayah, with a stable id <loc>/rN (N = position in its segment)."""
    with connect() as con:
        meta = {i: json.loads(m or '{}') for i, m in con.execute('SELECT id, meta FROM src')}
        seg_src = {}
        out = []
        for f in sorted((d / 'out' / tag).glob('c*.jsonl')):
            for line in f.read_text().splitlines():
                x = json.loads(line)
                if x['loc'] not in seg_src:
                    seg_src[x['loc']] = con.execute('SELECT src FROM seg WHERE seg=?', (x['loc'],)).fetchone()[0]
                for n, r in enumerate(x['rows'], 1):
                    if ayah in r.get('verses', []):
                        src = seg_src[x['loc']]
                        m = meta.get(src, {})
                        out.append({**r, 'id': f"{x['loc']}/r{n}", 'src': src, 'author': m.get('author') or src,
                                    'death': m.get('death_ah')})
    return out


def build(a):
    d = run_dir(a.run)
    t = d / 'tier2'
    old = json.loads((t / 'manifest.json').read_text()) if (t / 'manifest.json').exists() else None
    if old and (old['from'] != getattr(a, 'from') or [p['ayah'] for p in old['ayat']] != a.ayat):
        raise SystemExit('tier2 inputs exist for other rows or ayat; use a new run')
    plan = old['ayat'] if old else []  # existing row files are reused untouched (agents may be reading them)
    for ayah in ([] if old else a.ayat):
        rs = tier1_rows(d, getattr(a, 'from'), ayah)
        rs.sort(key=lambda r: (r['death'] if isinstance(r['death'], int) else 9999, r['src'], r['id']))
        lines, cur = [], None
        for r in rs:
            if r['src'] != cur:
                cur = r['src']
                lines.append(f"\n## {r['src']}: {r['author']}" + (f", d. {r['death']} AH" if r['death'] else ''))
            mentions = f" | mentions {', '.join(r.get('mentions') or [])}" if r.get('mentions') else ''
            lines.append(f"[{r['id']}] {r['speaker']} | {r['stance']} | {r['claim']}{mentions}")
        text = '\n'.join(lines).strip() + '\n'
        parts = [text[i:i + PART_CHARS] for i in range(0, len(text), PART_CHARS)]
        (t / 'rows').mkdir(parents=True, exist_ok=True)
        for k, p in enumerate(parts):
            tail = f'\n<<part {k} ends; continues in part {k + 1}>>' if k + 1 < len(parts) else '\n<<end of rows>>'
            (t / 'rows' / f'{key(ayah)}.p{k}.txt').write_text(f'<<{ayah} rows, part {k} of 0..{len(parts) - 1}>>\n{p}{tail}\n')
        dump(t / 'rows' / f'{key(ayah)}.json', {r['id']: {k: r.get(k) for k in ('src', 'author', 'death', 'speaker', 'stance', 'claim', 'mentions')} for r in rs})
        plan.append({'ayah': ayah, 'rows': len(rs), 'sources': len({r['src'] for r in rs}), 'chars': len(text), 'parts': len(parts)})
        print(f'{ayah}: {len(rs)} rows from {plan[-1]["sources"]} sources, {len(text):,} characters, {len(parts)} parts')
    with connect() as con:
        verse_text = {x: con.execute("SELECT text FROM seg JOIN src ON src.id=seg.src WHERE src.kind='quran' AND s=? AND a=?",
                                     tuple(map(int, x.split(':')))).fetchone()[0] for x in a.ayat}
    brief = BRIEF.read_text()
    for spec in a.models:
        model, effort = spec.split(':')
        tag = model.split('-')[-1] + '-' + effort
        (t / 'out' / tag).mkdir(parents=True, exist_ok=True)
        for p in plan:
            fill = {'AGENT': f"/root/v7m_{a.run}_{tag}_{key(p['ayah'])}", 'MODEL': model, 'EFFORT': effort, 'RUN': a.run,
                    'TAG': tag, 'AYAH': p['ayah'], 'KEY': key(p['ayah']), 'LAST': str(p['parts'] - 1),
                    'ROWS': str(p['rows']), 'SOURCES': str(p['sources']), 'VERSE': verse_text[p['ayah']]}
            text = brief
            for k, v in fill.items():
                text = text.replace('{' + k + '}', v)
            f = t / 'spawn' / f"{tag}_{key(p['ayah'])}.md"
            if f.exists():
                raise SystemExit(f'{f} exists')
            f.parent.mkdir(exist_ok=True)
            f.write_text(text)
            print(f'  spawn {f.relative_to(ROOT)}')
    dump(t / 'manifest.json', {'from': getattr(a, 'from'), 'ayat': plan,
                               'models': (old['models'] if old else []) + a.models})


def check_one(t, tag, ayah):
    known = json.loads((t / 'rows' / f'{key(ayah)}.json').read_text())
    f = t / 'out' / tag / f'{key(ayah)}.jsonl'
    if not f.exists():
        return [f'{f.name}: no output file'], []
    problems, views, covered = [], [], set()
    for i, line in enumerate(f.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            v = json.loads(line)
        except ValueError as e:
            problems.append(f'line {i}: not JSON ({e})')
            continue
        missing = [k for k in ('topic', 'view', 'rows') if not v.get(k)]
        if missing:
            problems.append(f'line {i}: missing {", ".join(missing)}')
        for r in v.get('rows') or []:
            if r not in known:
                problems.append(f'line {i}: unknown row id {r}')
            covered.add(r)
        views.append(v)
    for r in known:
        if r not in covered:
            problems.append(f'row {r} is in no view')
    return problems, views


def render(t, tag, ayah, views):
    """Compact view list for review and for writers: source ids, the speaker only when not the source's author,
    stance marks (+ prefers, - rejects). Full names, claims and anchors stay in tier 1 behind the row ids."""
    known = json.loads((t / 'rows' / f'{key(ayah)}.json').read_text())
    out, topic = [f'# {ayah}: {len(views)} views from {len(known)} rows ({tag})'], None
    for v in views:
        if v['topic'] != topic:
            topic = v['topic']
            out.append(f'\n## {topic}')
        holders = defaultdict(set)
        for r in v['rows']:
            k = known.get(r)
            if k:
                holders['' if k['speaker'] == 'author' else k['speaker']].add(
                    k['src'] + {'prefers': '+', 'rejects': '-'}.get(k['stance'], ''))
        who = '; '.join((f'{s}: ' if s else '') + ','.join(sorted(x)) for s, x in holders.items())
        out.append(f"- {v['view']}" + (f" ({v['note']})" if v.get('note') else '') + f' [{who}]')
    (t / 'out' / tag / f'{key(ayah)}.md').write_text('\n'.join(out) + '\n')


def check(a):
    t = run_dir(a.run) / 'tier2'
    man = json.loads((t / 'manifest.json').read_text())
    tags = [a.model] if a.model else sorted(p.name for p in (t / 'out').iterdir())
    ayat = [a.ayah] if a.ayah else [p['ayah'] for p in man['ayat']]
    if a.ayah:  # the agent's own check
        problems, _ = check_one(t, tags[0], a.ayah)
        print('OK' if not problems else '\n'.join(problems[:60]) + (f'\n... {len(problems) - 60} more' if len(problems) > 60 else ''))
        return
    for tag in tags:
        for ayah in ayat:
            problems, views = check_one(t, tag, ayah)
            for p in problems:
                print(f'WARNING {tag} {ayah}: {p}')
            if views:
                render(t, tag, ayah, views)
            print(f'{tag} {ayah}: {len(views)} views, {len(problems)} problems')


def report(a):
    t = run_dir(a.run) / 'tier2'
    man = json.loads((t / 'manifest.json').read_text())
    for tag in sorted(p.name for p in (t / 'out').iterdir()):
        for p in man['ayat']:
            r = t / 'runs' / f"v7m_{a.run}_{tag}_{key(p['ayah'])}" / 'run.json'
            f = t / 'out' / tag / f"{key(p['ayah'])}.jsonl"
            if not r.exists():
                print(f"WARNING {tag} {p['ayah']}: no run.json")
                continue
            x = json.loads(r.read_text())
            n = len(f.read_text().splitlines()) if f.exists() else 0
            out_chars = len(f.read_text()) if f.exists() else 0
            print(f"{tag} {p['ayah']}: ${x.get('usd_equivalent', 0):.3f}, {x.get('requests')} requests, peak "
                  f"{x.get('max_request_input_tokens')} tokens, {p['rows']} rows -> {n} views, "
                  f"output/input characters {out_chars / max(1, p['chars']):.2f}")
            if not x.get('turn_completed') or x.get('returncode'):
                print(f"WARNING {tag} {p['ayah']}: rc {x.get('returncode')}, completed {x.get('turn_completed')}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('build'); p.add_argument('run'); p.add_argument('--from', required=True)
    p.add_argument('--ayat', nargs='+', required=True); p.add_argument('--models', nargs='+', required=True)
    p = sub.add_parser('check'); p.add_argument('run'); p.add_argument('--model'); p.add_argument('--ayah')
    p = sub.add_parser('report'); p.add_argument('run')
    a = parser.parse_args()
    {'build': build, 'check': check, 'report': report}[a.cmd](a)


if __name__ == '__main__':
    main()
