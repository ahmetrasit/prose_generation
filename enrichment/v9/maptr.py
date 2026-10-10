#!/usr/bin/env python3
"""Enrichment v9: Turkish rendering of the verse maps (reader-facing; the maps themselves stay English). Launches no
model.

Per question: the question, its "turns on" line, and every position with its reasons, rendered in Turkish from the
English original. Ids are unchanged. Each translated question records a hash of the English it was made from, so a
map that changed later (update) shows its stale questions, which the next build includes again.

  maptr.py build RUN (--ayat S:A … | --ayat-file FILE) --model gpt-6-luna:max [--chunk-chars 60000]
  maptr.py check RUN [--chunk N]       every question of the chunk translated once, every position, no ids in text
  maptr.py report RUN

Files: enrichment/v9/work/RUN/maptr/{chunks,spawn,runs,out/<TAG>/cNN.jsonl}. Readers: q.translation(ayah).
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

V9 = Path(__file__).resolve().parent
sys.path.insert(0, str(V9.parent / 'v7'))
import digest  # noqa: E402
from digest import PART_CHARS, ROOT, dump  # noqa: E402
sys.path.insert(0, str(V9))
import q as Q  # noqa: E402

BRIEF = V9 / 'briefs/maptr.md'
IDS = re.compile(r'\d+:\d+/q\d+')


def tdir(run):
    return V9 / 'work' / run / 'maptr'


def english(q):
    return {'id': q['id'], 'question': q['question'], 'turns_on': q.get('turns_on') or '',
            'positions': [{'id': p['id'], 'position': p['position'], 'reasons': p.get('reasons') or ''} for p in q['positions']]}


def qhash(q):
    return hashlib.sha1(json.dumps(english(q), ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:16]


def txt(v):
    return v.strip() if isinstance(v, str) else ''


def complete(t, q):
    """A rendering covers the current question: question text, turns_on when the English has one, and every position
    of the map with position text (and reasons when the English has them)."""
    if not t or not txt(t.get('question')):
        return False
    if q.get('turns_on') and not txt(t.get('turns_on')):
        return False
    tp = t.get('positions') or {}
    return all(txt((tp.get(p['id']) or {}).get('position'))
               and (not p.get('reasons') or txt((tp.get(p['id']) or {}).get('reasons'))) for p in q['positions'])


def translation_problems(t, q):
    """Shared per-question validation for checkers and readers; no partial rendering is published."""
    problems = []
    if not isinstance(t, dict) or t.get('id') != q['id']:
        return ['translation id does not match its assigned question']
    if not txt(t.get('question')):
        problems.append(f"{q['id']}: empty question")
    if q.get('turns_on') and not txt(t.get('turns_on')):
        problems.append(f"{q['id']}: turns_on not translated")
    positions = t.get('positions')
    if not isinstance(positions, list):
        return problems + [f"{q['id']}: positions must be a list"]
    by_id = {p['id']: p for p in positions if isinstance(p, dict) and isinstance(p.get('id'), str)}
    if len(by_id) != len(positions):
        problems.append(f"{q['id']}: malformed or duplicate position id")
    for p in q['positions']:
        x = by_id.get(p['id'], {})
        if not txt(x.get('position')):
            problems.append(f"{p['id']}: position not translated")
        if p.get('reasons') and not txt(x.get('reasons')):
            problems.append(f"{p['id']}: reasons not translated")
    extra = set(by_id) - {p['id'] for p in q['positions']}
    if extra:
        problems.append(f"{q['id']}: positions not in the map: {', '.join(sorted(extra))}")
    text = ' '.join([txt(t.get('question')), txt(t.get('turns_on'))]
                    + [txt(p.get('position')) + ' ' + txt(p.get('reasons')) for p in by_id.values()])
    if IDS.search(text):
        problems.append(f"{q['id']}: ids in the text")
    return problems


def build(a):
    d = tdir(a.run)
    if d.exists():
        raise SystemExit(f'{d} exists; use a new run')
    if not (a.ayat or a.ayat_file):
        raise SystemExit('give --ayat or --ayat-file')
    if a.chunk_chars < 1:
        raise SystemExit('--chunk-chars must be positive')
    ayat = list(dict.fromkeys(a.ayat or Path(a.ayat_file).read_text().split()))
    todo, skipped, partial = [], 0, 0
    planned = set()
    for man in (V9 / 'work').glob('*/maptr/manifest.json'):
        m = json.loads(man.read_text())
        waiting = []
        for c in m['chunks']:
            agent = f"v9t_{man.parents[1].name}_{m['tag']}_c{c['chunk']:03d}"
            if (man.parent / 'out' / m['tag'] / f"c{c['chunk']:03d}.jsonl").exists():
                continue
            if (man.parent / 'runs' / agent / 'run.json').exists():
                continue                   # the agent ended without output: not planned, its questions are built again
            planned |= {(q, h) for q, h in c['src'].items()}
            dead = (man.parent / 'runs_failed_start' / agent).exists() and not (man.parent / 'runs' / agent).exists()
            waiting.append(f"c{c['chunk']:03d}" + (' (failed at start, not rerun yet)' if dead else ''))
        if waiting:
            print(f"NOTE {man.parents[1].name}: {len(waiting)} chunk(s) not finished (queued or running) count as planned: "
                  f"{' '.join(waiting[:30])}{' …' if len(waiting) > 30 else ''}")
    for v in ayat:
        why = Q.stale(v)
        if why:
            raise SystemExit(f'{v}: map not current ({why}); nothing built')
        qs, _ = Q.load(v)
        if qs is None:
            print(f'NOTE {v}: no verse map; nothing to translate')
            continue
        have = Q.translation(v)
        for q in qs:
            t = have.get(q['id'])
            if (t and t.get('src') == qhash(q) and complete(t, q)) or (q['id'], qhash(q)) in planned:
                skipped += 1
            else:
                partial += bool(t and t.get('src') == qhash(q))
                todo.append(q)
    print(f'{len(todo)} questions to translate ({skipped} already translated, or planned in a running build; '
          f'{partial} of the {len(todo)} have a current but incomplete rendering)')
    if not todo:
        return
    (d / 'chunks').mkdir(parents=True)
    (d / 'spawn').mkdir()
    chunks, cur, size = [], [], 0
    for q in todo:
        line = json.dumps(english(q), ensure_ascii=False)
        if cur and size + len(line) > a.chunk_chars:
            chunks.append(cur)
            cur, size = [], 0
        cur.append(q)
        size += len(line) + 1
    if cur:
        chunks.append(cur)
    model, effort = a.model.split(':')
    tag = digest.tag_of(model, effort)
    plan = []
    for n, ch in enumerate(chunks, 1):
        text = ''.join(json.dumps(english(q), ensure_ascii=False) + '\n' for q in ch)
        parts = [text[i:i + PART_CHARS] for i in range(0, len(text), PART_CHARS)]
        for k, p in enumerate(parts):
            tail = f'\n<<part {k} ends; continues in part {k + 1}>>' if k + 1 < len(parts) else '\n<<end of chunk>>'
            (d / 'chunks' / f'c{n:03d}.p{k}.txt').write_text(f'<<chunk {n}, part {k} of 0..{len(parts) - 1}>>\n{p}{tail}\n')
        fill = {'AGENT': f'/root/v9t_{a.run}_{tag}_c{n:03d}', 'MODEL': model, 'EFFORT': effort, 'RUN': a.run, 'TAG': tag,
                'N': str(n), 'NN': f'{n:03d}', 'LAST': str(len(parts) - 1), 'QUESTIONS': str(len(ch))}
        brief = BRIEF.read_text()
        for x, v in fill.items():
            brief = brief.replace('{' + x + '}', v)
        (d / 'spawn' / f'{tag}_c{n:03d}.md').write_text(brief)
        plan.append({'chunk': n, 'questions': [q['id'] for q in ch], 'src': {q['id']: qhash(q) for q in ch},
                     'chars': len(text), 'parts': len(parts)})
    (d / 'out' / tag).mkdir(parents=True)
    dump(d / 'manifest.json', {'model': a.model, 'tag': tag, 'chunks': plan})
    print(f'{len(chunks)} chunk(s), {sum(c["chars"] for c in plan):,} characters; spawn files in {(d / "spawn").relative_to(ROOT)}')


def check_chunk(d, man, c):
    want, problems, stale = {}, [], set()
    for qid in c['questions']:
        qs, _ = Q.load(qid.split('/')[0])
        q = next((x for x in qs or [] if x['id'] == qid), None)
        if q is None:
            problems.append(f'{qid}: no longer in the verse map')
            continue
        if qhash(q) != c['src'][qid]:
            stale.add(qid)                 # the map changed after the build: checked against nothing, built again later
        want[qid] = q
    f = d / 'out' / man['tag'] / f"c{c['chunk']:03d}.jsonl"
    if not f.exists():
        return problems + [f'{f.name}: no output file']
    seen = set()
    for i, line in enumerate(f.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            t = json.loads(line)
        except ValueError as e:
            problems.append(f'line {i}: not JSON ({e})')
            continue
        if not isinstance(t, dict) or not isinstance(t.get('id'), str):
            problems.append(f'line {i}: not an object with a text "id"')
            continue
        if t['id'] in stale:
            seen.add(t['id'])
            continue
        q = want.get(t.get('id'))
        if q is None:
            problems.append(f"line {i}: {t.get('id')} is not a question of this chunk")
            continue
        if t['id'] in seen:
            problems.append(f"line {i}: {t['id']} translated twice")
        seen.add(t['id'])
        problems += translation_problems(t, q)
    for qid in want:
        if qid not in seen and qid not in stale:
            problems.append(f'{qid}: not translated')
    if stale:
        problems.append(f"NOTE (not a problem of this chunk): {len(stale)} question(s) changed in the map after this build "
                        f"and were not checked; a later build translates them again: {' '.join(sorted(stale))}")
    return problems


def check(a):
    d = tdir(a.run)
    man = json.loads((d / 'manifest.json').read_text())
    plan = [c for c in man['chunks'] if a.chunk is None or c['chunk'] == a.chunk]
    if a.chunk is not None and not plan:
        raise SystemExit(f'unknown chunk: {a.chunk}')
    bad = 0
    for c in plan:
        p = check_chunk(d, man, c)
        for x in [x for x in p if x.startswith('NOTE')]:
            print(f"c{c['chunk']:03d}: {x}")
        p = [x for x in p if not x.startswith('NOTE')]
        if p:
            bad += 1
            print(f"c{c['chunk']:03d}: {len(p)} problem(s)")
            for x in p:
                print('  ' + x)
        elif a.chunk:
            print(f"OK c{c['chunk']:03d}: {len(c['questions'])} questions")
    if not a.chunk:
        print(f"{len(man['chunks']) - bad} of {len(man['chunks'])} chunks OK")
    sys.exit(1 if bad else 0)


def report(a):
    d = tdir(a.run)
    man = json.loads((d / 'manifest.json').read_text())
    total = 0.0
    for c in man['chunks']:
        x = digest.usage(d / 'runs', f"/root/v9t_{a.run}_{man['tag']}_c{c['chunk']:03d}")
        if x is None:
            print(f"WARNING c{c['chunk']:03d}: no run record")
            continue
        total += x['usd']
        if not x['completed']:
            print(f"WARNING c{c['chunk']:03d}: did not complete")
    print(f"{man['tag']}: {len(man['chunks'])} chunks, ${total:.2f}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('build'); p.add_argument('run'); p.add_argument('--ayat', nargs='+'); p.add_argument('--ayat-file')
    p.add_argument('--model', required=True); p.add_argument('--chunk-chars', type=int, default=60_000)
    p = sub.add_parser('check'); p.add_argument('run'); p.add_argument('--chunk', type=int)
    p = sub.add_parser('report'); p.add_argument('run')
    a = ap.parse_args()
    {'build': build, 'check': check, 'report': report}[a.cmd](a)


if __name__ == '__main__':
    main()
