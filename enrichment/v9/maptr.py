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


def build(a):
    d = tdir(a.run)
    if d.exists():
        raise SystemExit(f'{d} exists; use a new run')
    ayat = a.ayat or Path(a.ayat_file).read_text().split()
    todo, skipped = [], 0
    for v in ayat:
        qs, _ = Q.load(v)
        if qs is None:
            print(f'NOTE {v}: no verse map; nothing to translate')
            continue
        have = Q.translation(v)
        for q in qs:
            if have.get(q['id'], {}).get('src') == qhash(q):
                skipped += 1
            else:
                todo.append(q)
    print(f'{len(todo)} questions to translate ({skipped} already translated and current)')
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
    want = {}
    for qid in c['questions']:
        qs, _ = Q.load(qid.split('/')[0])
        want[qid] = next(q for q in qs if q['id'] == qid)
    f = d / 'out' / man['tag'] / f"c{c['chunk']:03d}.jsonl"
    if not f.exists():
        return [f'{f.name}: no output file']
    problems, seen = [], set()
    for i, line in enumerate(f.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            t = json.loads(line)
        except ValueError as e:
            problems.append(f'line {i}: not JSON ({e})')
            continue
        q = want.get(t.get('id'))
        if q is None:
            problems.append(f"line {i}: {t.get('id')} is not a question of this chunk")
            continue
        if t['id'] in seen:
            problems.append(f"line {i}: {t['id']} translated twice")
        seen.add(t['id'])
        if not (t.get('question') or '').strip():
            problems.append(f"{t['id']}: empty question")
        if q.get('turns_on') and not (t.get('turns_on') or '').strip():
            problems.append(f"{t['id']}: turns_on not translated")
        tp = {p.get('id'): p for p in t.get('positions') or []}
        for p in q['positions']:
            x = tp.get(p['id'])
            if x is None or not (x.get('position') or '').strip():
                problems.append(f"{p['id']}: position not translated")
            elif p.get('reasons') and not (x.get('reasons') or '').strip():
                problems.append(f"{p['id']}: reasons not translated")
        extra = set(tp) - {p['id'] for p in q['positions']}
        if extra:
            problems.append(f"{t['id']}: positions not in the map: {', '.join(sorted(extra))}")
        text = ' '.join([t.get('question') or '', t.get('turns_on') or ''] + [(x.get('position') or '') + ' ' + (x.get('reasons') or '') for x in tp.values()])
        if IDS.search(text):
            problems.append(f"{t['id']}: ids in the text")
    for qid in want:
        if qid not in seen:
            problems.append(f'{qid}: not translated')
    return problems


def check(a):
    d = tdir(a.run)
    man = json.loads((d / 'manifest.json').read_text())
    bad = 0
    for c in man['chunks']:
        if a.chunk and c['chunk'] != a.chunk:
            continue
        p = check_chunk(d, man, c)
        if p:
            bad += 1
            print(f"c{c['chunk']:03d}: {len(p)} problem(s)")
            for x in p[:40]:
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
