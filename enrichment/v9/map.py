#!/usr/bin/env python3
"""Enrichment v9 verse map: one agent per verse turns all of the verse's tier-1 notes into questions, each with its
distinct positions, holders, reasons, and who prefers or argues against each position. Launches no model.

The map replaces v7 tier 2 (flat views): it is reused by every page that cites the verse, and it is the link target
of cited-verse blocks. Tier-1 notes are read from every v7 run (`merge.tier1_rows`, full-edition rule applied).
A verse is never split: one agent reads all of its notes.

  map.py build RUN --from luna-max --ayat 100:1 12:49 … --models gpt-6-luna:max gpt-6-sol:high
  map.py check RUN [--model TAG] [--ayah A]   the agent runs it with --model and --ayah until OK; without --ayah:
                                              checks every verse and assembles the finished ones
  map.py report RUN                           cost, questions, positions, notes per verse and model

Files (RUN = enrichment/v9/work/RUN/map): rows/<k>.json (notes by id), rows/<k>.pK.txt (input parts), spawn/,
runs/ (written by enrichment/v5/run_codex.py), out/<TAG>/<k>.raw.jsonl (agent output), out/<TAG>/<k>.jsonl and
<k>.md (assembled: question ids <ayah>/qNN, position ids <ayah>/qNN/pN).
"""
import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

V9 = Path(__file__).resolve().parent
sys.path.insert(0, str(V9.parent / 'v7'))
import digest  # noqa: E402
import merge  # noqa: E402
from digest import PART_CHARS, ROOT, TYPES, connect, dump  # noqa: E402

BRIEF = V9 / 'briefs/map.md'
BIG = 90_000  # input characters above which a verse is printed as large (never split)


def mdir(run):
    return V9 / 'work' / run / 'map'


def key(ayah):
    return ayah.replace(':', '-')


def agent_name(run, tag, ayah):
    return f'/root/v9m_{run}_{tag}_{key(ayah)}'


def verse_text(ayah):
    with connect() as con:
        return con.execute("SELECT text FROM seg JOIN src ON src.id=seg.src WHERE src.kind='quran' AND s=? AND a=?",
                           tuple(map(int, ayah.split(':')))).fetchone()[0]


def write_parts(m, ayah, rs):
    """Notes oldest author first, in parts of at most PART_CHARS; returns (characters, parts)."""
    k = key(ayah)
    order = sorted(rs, key=lambda r: (r['death'] if isinstance(r['death'], int) else 9999, r['src'], r['id']))
    text = '\n'.join(merge.row_line(r) for r in order) + '\n'
    parts = [text[i:i + PART_CHARS] for i in range(0, len(text), PART_CHARS)]
    for n, p in enumerate(parts):
        tail = f'\n<<part {n} ends; continues in part {n + 1}>>' if n + 1 < len(parts) else '\n<<end of notes>>'
        (m / 'rows' / f'{k}.p{n}.txt').write_text(f'<<{ayah} notes, part {n} of 0..{len(parts) - 1}>>\n{p}{tail}\n')
    return len(text), len(parts)


def spawn(m, run, spec, p):
    model, effort = spec.split(':')
    tag = digest.tag_of(model, effort)
    k = key(p['ayah'])
    fill = {'AGENT': agent_name(run, tag, p['ayah']), 'MODEL': model, 'EFFORT': effort, 'RUN': run, 'TAG': tag,
            'AYAH': p['ayah'], 'KEY': k, 'LAST': str(p['parts'] - 1), 'ROWS': str(p['rows']),
            'SOURCES': str(p['sources']), 'VERSE': verse_text(p['ayah']),
            'TYPES': '\n'.join(f'  - `{x}`: {v}' for x, v in digest.TYPE_GUIDE.items())}
    text = BRIEF.read_text()
    for x, v in fill.items():
        text = text.replace('{' + x + '}', v)
    f = m / 'spawn' / f'{tag}_{k}.md'
    if f.exists():
        raise SystemExit(f'{f} exists')
    f.write_text(text)
    (m / 'out' / tag).mkdir(parents=True, exist_ok=True)
    print(f'  spawn {f.relative_to(ROOT)}')


def build(a):
    m = mdir(a.run)
    if (m / 'manifest.json').exists():
        raise SystemExit(f'{m} has a manifest; use a new run')
    (m / 'rows').mkdir(parents=True, exist_ok=True)
    (m / 'spawn').mkdir(exist_ok=True)
    plan = []
    for ayah in a.ayat:
        rs = merge.tier1_rows(None, a.from_tags, ayah)
        if not rs:
            print(f'NOTE {ayah}: no tier-1 notes ({", ".join(a.from_tags)}); no map')
            continue
        dump(m / 'rows' / f'{key(ayah)}.json',
             {r['id']: {x: r.get(x) for x in ('src', 'author', 'death', 'speaker', 'stance', 'claim', 'mentions')}
              for r in rs})
        chars, parts = write_parts(m, ayah, rs)
        p = {'ayah': ayah, 'rows': len(rs), 'sources': len({r['src'] for r in rs}), 'chars': chars, 'parts': parts}
        plan.append(p)
        print(f"{ayah}: {p['rows']} notes from {p['sources']} sources, {chars:,} characters, {parts} parts"
              + (f' — NOTE: over {BIG:,} characters, one agent still reads it all' if chars > BIG else ''))
    if not plan:
        raise SystemExit('nothing to build')
    for spec in a.models:
        for p in plan:
            spawn(m, a.run, spec, p)
    dump(m / 'manifest.json', {'from': a.from_tags, 'models': a.models, 'ayat': plan})


def check_verse(m, tag, ayah):
    """(problems, questions) of one agent output."""
    k = key(ayah)
    known = set(json.loads((m / 'rows' / f'{k}.json').read_text()))
    f = m / 'out' / tag / f'{k}.raw.jsonl'
    if not f.exists():
        return [f'{f.name}: no output file'], []
    problems, qs, covered = [], [], set()
    for i, line in enumerate(f.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            q = json.loads(line)
        except ValueError as e:
            problems.append(f'line {i}: not JSON ({e})')
            continue
        if not q.get('question') or not q.get('positions'):
            problems.append(f'line {i}: missing question or positions')
            continue
        problems += [f'line {i}: {x}' for x in digest.tag_problems({'words': q.get('words'), 'type': q.get('type'),
                                                                     'verses': [ayah]})]
        for n, p in enumerate(q['positions'], 1):
            where = f'line {i} position {n}'
            if not p.get('position'):
                problems.append(f'{where}: missing "position"')
            ids = {x: p.get(x) or [] for x in ('rows', 'prefer', 'against')}
            if not ids['rows'] and not ids['against']:
                problems.append(f'{where}: no note in "rows" or "against"')
            for field, xs in ids.items():
                for r in xs:
                    if r not in known:
                        problems.append(f'{where}: {field} id {r} is not a note of {ayah}')
                    covered.add(r)
            for r in set(ids['prefer']) - set(ids['rows']):
                problems.append(f'{where}: {r} is in "prefer" but not in "rows" (a note that prefers a position holds it)')
            for r in set(ids['rows']) & set(ids['against']):
                problems.append(f'{where}: {r} is in both "rows" and "against" of the same position')
        qs.append(q)
    for r in sorted(known - covered):
        problems.append(f'note {r} is in no position')
    return problems, qs


def render(ayah, qs, known):
    """Compact map: question, positions with reasons and holders (source, speaker when not the author; + prefers,
    - argues against, from the map itself, not from the note's stance label)."""
    def holders(ids, mark=''):
        by = defaultdict(set)
        for r in ids:
            x = known.get(r)
            if x:
                by[x['src']].add('' if x['speaker'] == 'author' else x['speaker'])
        return [s + (f"({','.join(sorted(w for w in sp if w))})" if any(sp) else '') + mark for s, sp in by.items()]

    out = [f'# {ayah}: {len(qs)} questions']
    for q in qs:
        out.append(f"\n## {q['id']} {q['question']}  [{' '.join(q['words'])} · {q['type']}]")
        if q.get('turns_on'):
            out.append(f"turns on: {q['turns_on']}")
        for p in q['positions']:
            pro = set(p.get('prefer') or [])
            who = holders([r for r in p['rows'] if r not in pro]) + holders(sorted(pro), '+') + holders(p.get('against') or [], '-')
            out.append(f"- {p['id']} {p['position']}" + (f" — {p['reasons']}" if p.get('reasons') else '')
                       + f" [{len(p['rows'])} notes: {'; '.join(who)}]")
    return '\n'.join(out) + '\n'


def assemble(m, tag, ayah, qs):
    k = key(ayah)
    for n, q in enumerate(qs, 1):
        q['id'] = f'{ayah}/q{n:02d}'
        for j, p in enumerate(q['positions'], 1):
            p['id'] = f"{q['id']}/p{j}"
    (m / 'out' / tag / f'{k}.jsonl').write_text(''.join(json.dumps(q, ensure_ascii=False) + '\n' for q in qs))
    known = json.loads((m / 'rows' / f'{k}.json').read_text())
    (m / 'out' / tag / f'{k}.md').write_text(render(ayah, qs, known))


def check(a):
    m = mdir(a.run)
    man = json.loads((m / 'manifest.json').read_text())
    tags = [a.model] if a.model else [digest.tag_of(*s.split(':')) for s in man['models']]
    ayat = [a.ayah] if a.ayah else [p['ayah'] for p in man['ayat']]
    bad = 0
    for tag in tags:
        for ayah in ayat:
            problems, qs = check_verse(m, tag, ayah)
            if problems:
                bad += 1
                print(f'{tag} {ayah}: {len(problems)} problem(s)')
                for x in problems[:60]:
                    print('  ' + x)
                if len(problems) > 60:
                    print(f'  … and {len(problems) - 60} more')
                continue
            npos = sum(len(q['positions']) for q in qs)
            if a.ayah:
                print(f'OK {tag} {ayah}: {len(qs)} questions, {npos} positions')
            else:
                assemble(m, tag, ayah, qs)
                print(f'OK {tag} {ayah}: {len(qs)} questions, {npos} positions, assembled')
    if bad:
        sys.exit(1)


def report(a):
    m = mdir(a.run)
    man = json.loads((m / 'manifest.json').read_text())
    for spec in man['models']:
        tag = digest.tag_of(*spec.split(':'))
        total = 0.0
        for p in man['ayat']:
            x = digest.usage(m / 'runs', agent_name(a.run, tag, p['ayah']))
            f = m / 'out' / tag / f"{key(p['ayah'])}.jsonl"
            qs = [json.loads(l) for l in f.read_text().splitlines() if l.strip()] if f.exists() else []
            shape = f"{len(qs)} questions, {sum(len(q['positions']) for q in qs)} positions" if qs else 'not assembled'
            if x is None:
                print(f"WARNING {tag} {p['ayah']}: no run record; {shape}")
                continue
            total += x['usd']
            print(f"{tag} {p['ayah']}: ${x['usd']:.3f}, {x['requests']} requests, peak {x['peak']} tokens, "
                  f"{p['rows']} notes -> {shape}" + ('' if x['completed'] else ' — DID NOT COMPLETE'))
        print(f'{tag}: ${total:.2f} total')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('build'); p.add_argument('run')
    p.add_argument('--from', dest='from_tags', nargs='+', required=True, help='tier-1 model tags, e.g. luna-max')
    p.add_argument('--ayat', nargs='+', required=True); p.add_argument('--models', nargs='+', required=True)
    p = sub.add_parser('check'); p.add_argument('run'); p.add_argument('--model'); p.add_argument('--ayah')
    p = sub.add_parser('report'); p.add_argument('run')
    a = parser.parse_args()
    {'build': build, 'check': check, 'report': report}[a.cmd](a)


if __name__ == '__main__':
    main()
