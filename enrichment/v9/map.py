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
  map.py update RUN --model gpt-6-sol:high     notes added to tier 1 since mapping: one agent per verse places them
                                              in the existing map (ids stay); briefs/map-update.md
  map.py refresh-rows RUN                     add fields missing from saved notes (anchor), same note ids only

Files (RUN = enrichment/v9/work/RUN/map): rows/<k>.json (notes by id), rows/<k>.pK.txt (input parts), spawn/,
runs/ (written by enrichment/v5/run_codex.py), out/<TAG>/<k>.raw.jsonl (agent output), out/<TAG>/<k>.jsonl and
<k>.md (assembled: question ids <ayah>/qNN, position ids <ayah>/qNN/pN).
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

V9 = Path(__file__).resolve().parent
sys.path.insert(0, str(V9.parent / 'v7'))
import digest  # noqa: E402
import merge  # noqa: E402
from digest import PART_CHARS, ROOT, TYPES, connect, dump  # noqa: E402

BRIEF = V9 / 'briefs/map.md'
BRIEF_UPDATE = V9 / 'briefs/map-update.md'
ROW_FIELDS = ('src', 'author', 'death', 'speaker', 'stance', 'claim', 'anchor', 'mentions')
BIG = 90_000  # input characters above which a verse is printed as large (never split)


def mdir(run):
    return V9 / 'work' / run / 'map'


def key(ayah):
    return ayah.replace(':', '-')


def agent_name(run, tag, ayah, n=None):
    return f'/root/v9m_{run}_{tag}_{key(ayah)}' if n is None else f'/root/v9u_{run}_{tag}_{key(ayah)}_u{n}'


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
             {r['id']: {x: r.get(x) for x in ROW_FIELDS} for r in rs})
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


def refresh_rows(a):
    """Add fields missing from a run's saved notes (e.g. anchor), from tier 1; the note ids must be exactly the same."""
    m = mdir(a.run)
    man = json.loads((m / 'manifest.json').read_text())
    for p in man['ayat']:
        f = m / 'rows' / f"{key(p['ayah'])}.json"
        old = json.loads(f.read_text())
        rs = {r['id']: r for r in merge.tier1_rows(None, man['from'], p['ayah'], quiet=True)}
        if set(rs) != set(old):
            print(f"WARNING {p['ayah']}: tier-1 notes changed since the map was built "
                  f"({len(set(rs) - set(old))} new, {len(set(old) - set(rs))} gone); not refreshed")
            continue
        dump(f, {i: {x: rs[i].get(x) for x in ROW_FIELDS} for i in old})
        print(f"{p['ayah']}: {len(old)} notes refreshed")


QID = re.compile(r'^\d+:\d+/q\d+$')
PID = re.compile(r'^\d+:\d+/q\d+/p\d+$')


def number(qs, ayah):
    """Ids by order (questions qNN, positions pN); ids already given are kept, so later additions never renumber."""
    for n, q in enumerate(qs, 1):
        q.setdefault('id', f'{ayah}/q{n:02d}')
        for j, p in enumerate(q['positions'], 1):
            p.setdefault('id', f"{q['id']}/p{j}")


def read_lines(f):
    problems, out = [], []
    for i, line in enumerate(f.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            out.append((i, json.loads(line)))
        except ValueError as e:
            problems.append(f'{f.name} line {i}: not JSON ({e})')
    return problems, out


def question_ok(q, where, ayah):
    if not q.get('question') or not q.get('positions'):
        return [f'{where}: missing question or positions']
    return [f'{where}: {x}' for x in digest.tag_problems({'words': q.get('words'), 'type': q.get('type'), 'verses': [ayah]})]


def combined(m, tag, ayah, updates=()):
    """(problems, questions): the agent's map plus every update for this model, in order, with stable ids; then the
    checks over the whole: ids known, every note placed, prefer ⊆ rows, never rows and against together."""
    k = key(ayah)
    rows = json.loads((m / 'rows' / f'{k}.json').read_text())
    mine = [u for u in updates if u['tag'] == tag]
    later = {i for u in updates if u['tag'] != tag for i in u['ids']}
    known = set(rows) - later
    f = m / 'out' / tag / f'{k}.raw.jsonl'
    if not f.exists():
        return [f'{f.name}: no output file'], []
    problems, lines = read_lines(f)
    qs = []
    for i, q in lines:
        bad = question_ok(q, f'line {i}', ayah)
        problems += bad
        if not bad:
            qs.append(q)
    number(qs, ayah)
    for u in mine:
        f = m / 'out' / tag / f"{k}.u{u['n']}.raw.jsonl"
        if not f.exists():
            problems.append(f'{f.name}: no output file')
            continue
        bad, lines = read_lines(f)
        problems += bad
        byq = {q['id']: q for q in qs}
        byp = {p['id']: p for q in qs for p in q['positions']}
        for i, x in lines:
            where = f'{f.name} line {i}'
            if 'positions' in x:                                   # a new question
                b = question_ok(x, where, ayah)
                problems += b
                if not b:
                    qs.append(x)
                    number(qs, ayah)
            elif QID.match(str(x.get('question', ''))):           # a new position under an existing question
                q = byq.get(x['question'])
                if q is None:
                    problems.append(f"{where}: question {x['question']} does not exist")
                elif not x.get('position'):
                    problems.append(f'{where}: missing "position"')
                else:
                    q['positions'].append({y: x.get(y) for y in ('position', 'reasons', 'rows', 'prefer', 'against')})
                    number(qs, ayah)
            elif PID.match(str(x.get('position', ''))):           # notes added to an existing position
                p = byp.get(x['position'])
                if p is None:
                    problems.append(f"{where}: position {x['position']} does not exist")
                    continue
                for y in ('rows', 'prefer', 'against'):
                    p[y] = list(dict.fromkeys((p.get(y) or []) + (x.get(y) or [])))
                if x.get('reasons_add'):
                    p['reasons'] = ((p.get('reasons') or '') + ' ' + x['reasons_add']).strip()
            else:
                problems.append(f'{where}: not a new question, a new position (question: <question id>) or an '
                                'addition (position: <position id>)')
    covered = set()
    for q in qs:
        for n, p in enumerate(q['positions'], 1):
            where = p.get('id', f"{q['id']} position {n}")
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
    (m / 'out' / tag / f'{k}.jsonl').write_text(''.join(json.dumps(q, ensure_ascii=False) + '\n' for q in qs))
    known = json.loads((m / 'rows' / f'{k}.json').read_text())
    (m / 'out' / tag / f'{k}.md').write_text(render(ayah, qs, known))


def map_text(qs):
    """The current map as the update agent reads it: question and position ids, texts and reasons (no holders)."""
    out = []
    for q in qs:
        out.append(f"{q['id']} {q['question']} [{' '.join(q['words'])} · {q['type']}]"
                   + (f" (turns on: {q['turns_on']})" if q.get('turns_on') else ''))
        for p in q['positions']:
            out.append(f"  {p['id']} {p['position']}" + (f" — reasons: {p['reasons']}" if p.get('reasons') else ''))
    return '\n'.join(out) + '\n'


def update(a):
    """Notes added to tier 1 since a verse was mapped: one agent per verse places them in the existing map
    (stable ids). The verse's saved notes gain the new ones; the update is recorded in the manifest."""
    m = mdir(a.run)
    man = json.loads((m / 'manifest.json').read_text())
    model, effort = a.model.split(':')
    tag = digest.tag_of(model, effort)
    built = 0
    for p in man['ayat']:
        ayah, k = p['ayah'], key(p['ayah'])
        if a.ayat and ayah not in a.ayat:
            continue
        old = json.loads((m / 'rows' / f'{k}.json').read_text())
        rs = merge.tier1_rows(None, man['from'], ayah, quiet=True)
        ids = {r['id'] for r in rs}
        gone = set(old) - ids
        if gone:
            print(f'WARNING {ayah}: {len(gone)} saved notes are no longer in tier 1; they stay in the map')
        new = [r for r in rs if r['id'] not in old]
        if not new:
            print(f'{ayah}: no new notes')
            continue
        ups = p.setdefault('updates', [])
        problems, qs = combined(m, tag, ayah, ups)
        if problems:
            print(f'WARNING {ayah}: the current {tag} map has {len(problems)} problem(s); no update built (run check)')
            continue
        n = len(ups) + 1
        old.update({r['id']: {x: r.get(x) for x in ROW_FIELDS} for r in new})
        dump(m / 'rows' / f'{k}.json', old)
        order = sorted(new, key=lambda r: (r['death'] if isinstance(r['death'], int) else 9999, r['src'], r['id']))
        text = ('## THE CURRENT MAP\n' + map_text(qs) + '\n## THE NEW NOTES\n'
                + '\n'.join(merge.row_line(r) for r in order) + '\n')
        parts = [text[i:i + PART_CHARS] for i in range(0, len(text), PART_CHARS)]
        for j, t in enumerate(parts):
            tail = f'\n<<part {j} ends; continues in part {j + 1}>>' if j + 1 < len(parts) else '\n<<end of input>>'
            (m / 'rows' / f'{k}.u{n}.p{j}.txt').write_text(f'<<{ayah} update {n}, part {j} of 0..{len(parts) - 1}>>\n{t}{tail}\n')
        fill = {'AGENT': agent_name(a.run, tag, ayah, n), 'MODEL': model, 'EFFORT': effort, 'RUN': a.run, 'TAG': tag,
                'AYAH': ayah, 'KEY': k, 'N': str(n), 'LAST': str(len(parts) - 1), 'NEW': str(len(new)),
                'QUESTIONS': str(len(qs)), 'VERSE': verse_text(ayah),
                'TYPES': '\n'.join(f'  - `{x}`: {v}' for x, v in digest.TYPE_GUIDE.items())}
        brief = BRIEF_UPDATE.read_text()
        for x, v in fill.items():
            brief = brief.replace('{' + x + '}', v)
        f = m / 'spawn' / f'{tag}_{k}.u{n}.md'
        if f.exists():
            raise SystemExit(f'{f} exists')
        f.write_text(brief)
        ups.append({'n': n, 'tag': tag, 'model': a.model, 'ids': [r['id'] for r in new], 'chars': len(text),
                    'parts': len(parts)})
        built += 1
        print(f'{ayah}: update {n}, {len(new)} new notes, {len(text):,} characters  spawn {f.relative_to(ROOT)}')
    dump(m / 'manifest.json', man)
    print(f'{built} update(s) built')


def check(a):
    m = mdir(a.run)
    man = json.loads((m / 'manifest.json').read_text())
    tags = [a.model] if a.model else [digest.tag_of(*s.split(':')) for s in man['models']]
    ups = {p['ayah']: p.get('updates', []) for p in man['ayat']}
    ayat = [a.ayah] if a.ayah else [p['ayah'] for p in man['ayat']]
    bad = 0
    for tag in tags:
        for ayah in ayat:
            problems, qs = combined(m, tag, ayah, ups.get(ayah, []))
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
            for u in p.get('updates', []):
                if u['tag'] != tag:
                    continue
                y = digest.usage(m / 'runs', agent_name(a.run, tag, p['ayah'], u['n']))
                if y is None:
                    print(f"WARNING {tag} {p['ayah']} update {u['n']}: no run record")
                    continue
                total += y['usd']
                print(f"{tag} {p['ayah']} update {u['n']}: ${y['usd']:.3f}, {y['requests']} requests, peak {y['peak']} "
                      f"tokens, {len(u['ids'])} new notes" + ('' if y['completed'] else ' — DID NOT COMPLETE'))
        print(f'{tag}: ${total:.2f} total')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('build'); p.add_argument('run')
    p.add_argument('--from', dest='from_tags', nargs='+', required=True, help='tier-1 model tags, e.g. luna-max')
    p.add_argument('--ayat', nargs='+', required=True); p.add_argument('--models', nargs='+', required=True)
    p = sub.add_parser('check'); p.add_argument('run'); p.add_argument('--model'); p.add_argument('--ayah')
    p = sub.add_parser('report'); p.add_argument('run')
    p = sub.add_parser('refresh-rows'); p.add_argument('run')
    p = sub.add_parser('update'); p.add_argument('run'); p.add_argument('--model', required=True, help='e.g. gpt-6-sol:high')
    p.add_argument('--ayat', nargs='+', help='only these verses')
    a = parser.parse_args()
    {'build': build, 'check': check, 'report': report, 'refresh-rows': refresh_rows, 'update': update}[a.cmd](a)


if __name__ == '__main__':
    main()
