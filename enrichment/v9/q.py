#!/usr/bin/env python3
"""Enrichment v9 lookup over verse maps and their notes (used by the writer and the orchestrator). Read-only.

  q.py index V [V …]                 one line per question of each verse's map: id, question, words, type, positions
  q.py question QID [QID …]          a question in full: positions, reasons, holders (+ prefers, - argues against),
                                     note ids, and the sources named
  q.py notes ID [ID …]               notes in full: source, author, death, speaker, stance, claim, «exact words»
  q.py find REGEX [--verse V …] [--page N]
                                     notes whose claim or exact words match (Arabic matched without vowels), with the
                                     position each note sits in; default all mapped verses; 25 per page

Maps: enrichment/v9/work/*/map/out/sol-high/<k>.jsonl (the newest when a verse was mapped twice). Output stays under
24,000 bytes; a cut is marked.
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

TAG = 'sol-high'
MAX_BYTES = 24_000
PAGE = 25
_DROP = {ord(c): None for c in digest._ARABIC_DROP}
_MAP = str.maketrans(digest._ARABIC_MAP)


def key(ayah):
    return ayah.replace(':', '-')


def plain(text):
    """Arabic without vowels and with letter variants folded (as in digest), for matching."""
    return (text or '').translate(_DROP).translate(_MAP)


def located(ayah):
    """(map file, rows file) of the newest map of the verse, or None."""
    fs = [f for f in (V9 / 'work').glob(f'*/map/out/{TAG}/{key(ayah)}.jsonl')]
    if not fs:
        return None
    f = max(fs, key=lambda x: x.stat().st_mtime)
    return f, f.parents[2] / 'rows' / f'{key(ayah)}.json'


def load(ayah):
    loc = located(ayah)
    if not loc:
        return None, None
    return [json.loads(l) for l in loc[0].read_text().splitlines() if l.strip()], json.loads(loc[1].read_text())


def mapped():
    return sorted({f.stem for f in (V9 / 'work').glob(f'*/map/out/{TAG}/*.jsonl') if '.' not in f.stem},
                  key=lambda k: tuple(map(int, k.split('-'))))


def out(lines):
    text, size = [], 0
    for ln in lines:
        n = len(ln.encode()) + 1
        if size + n > MAX_BYTES:
            text.append('[cut: output limit; ask for fewer items]')
            break
        text.append(ln)
        size += n
    print('\n'.join(text))


def holders(ids, rows, mark=''):
    by = defaultdict(set)
    for r in ids:
        x = rows.get(r)
        if x:
            by[x['src']].add('' if x['speaker'] == 'author' else x['speaker'])
    return [s + (f"({'، '.join(sorted(w for w in sp if w))})" if any(sp) else '') + mark for s, sp in by.items()]


def cmd_index(a):
    lines = []
    for v in a.verses:
        qs, rows = load(v)
        if qs is None:
            lines.append(f'# {v}: NO MAP')
            continue
        lines.append(f'# {v}: {len(qs)} questions, {len(rows)} notes')
        for q in qs:
            n = len({r for p in q['positions'] for r in p['rows'] + (p.get('against') or [])})
            lines.append(f"{q['id']} {q['question']} [{' '.join(q['words'])} · {q['type']}] "
                         f"{len(q['positions'])} positions, {n} notes")
    out(lines)


def cmd_question(a):
    lines = []
    for qid in a.qids:
        v = qid.split('/')[0]
        qs, rows = load(v)
        q = next((x for x in qs or [] if x['id'] == qid), None)
        if q is None:
            lines.append(f'# {qid}: not found')
            continue
        lines.append(f"# {q['id']} {q['question']} [{' '.join(q['words'])} · {q['type']}]")
        if q.get('turns_on'):
            lines.append(f"turns on: {q['turns_on']}")
        srcs = set()
        for p in q['positions']:
            pro, con = set(p.get('prefer') or []), p.get('against') or []
            who = holders([r for r in p['rows'] if r not in pro], rows) + holders(sorted(pro), rows, '+') + holders(con, rows, '-')
            srcs |= {rows[r]['src'] for r in p['rows'] + con if r in rows}
            lines.append(f"- {p['id']} {p['position']}")
            if p.get('reasons'):
                lines.append(f"  reasons: {p['reasons']}")
            lines.append(f"  holders ({len(p['rows'])} notes): {'; '.join(who)}")
            lines.append(f"  notes: {' '.join(p['rows'])}" + (f" | against: {' '.join(con)}" if con else ''))
        legend = {}
        for r in rows.values():
            if r['src'] in srcs:
                legend[r['src']] = f"{r['author']}" + (f", d. {r['death']}" if r['death'] else '')
        lines.append('sources: ' + '; '.join(f'{s} = {n}' for s, n in sorted(legend.items())))
        lines.append('')
    out(lines)


def cmd_notes(a):
    lines, cache = [], {}
    for i in a.ids:
        x = None
        for v in mapped():
            if v not in cache:
                cache[v] = load(v.replace('-', ':'))[1]
            if i in cache[v]:
                x = cache[v][i]
                break
        if x is None:
            lines.append(f'[{i}] not found')
            continue
        lines.append(f"[{i}] {x['src']} ({x['author']}" + (f", d. {x['death']}" if x['death'] else '') + f") · "
                     f"{x['speaker']} · {x['stance']} · {x['claim']} «{x.get('anchor') or ''}»")
    out(lines)


def cmd_find(a):
    rx = re.compile(plain(a.regex), re.I)
    verses = [v.replace(':', '-') for v in a.verse] if a.verse else mapped()
    hits = []
    for k in verses:
        v = k.replace('-', ':')
        qs, rows = load(v)
        if qs is None:
            continue
        where = defaultdict(list)
        for q in qs:
            for p in q['positions']:
                for r in p['rows'] + (p.get('against') or []):
                    where[r].append(p['id'])
        for i, x in rows.items():
            if rx.search(plain(x['claim'])) or rx.search(plain(x.get('anchor') or '')):
                hits.append((v, i, x, where.get(i, [])))
    lines = [f'{len(hits)} notes match' + (f' on {", ".join(a.verse)}' if a.verse else ' on all mapped verses')
             + f'; page {a.page} of {max(1, -(-len(hits) // PAGE))}']
    if not a.verse:
        per = defaultdict(int)
        for h in hits:
            per[h[0]] += 1
        lines.append('per verse: ' + ', '.join(f'{v} {n}' for v, n in per.items()))
    for v, i, x, w in hits[(a.page - 1) * PAGE:a.page * PAGE]:
        lines.append(f"[{i}] {v} {x['src']} · {x['speaker']} · {x['stance']} · {x['claim']} «{x.get('anchor') or ''}» → {' '.join(w)}")
    out(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('index'); p.add_argument('verses', nargs='+')
    p = sub.add_parser('question'); p.add_argument('qids', nargs='+')
    p = sub.add_parser('notes'); p.add_argument('ids', nargs='+')
    p = sub.add_parser('find'); p.add_argument('regex'); p.add_argument('--verse', nargs='+'); p.add_argument('--page', type=int, default=1)
    a = parser.parse_args()
    {'index': cmd_index, 'question': cmd_question, 'notes': cmd_notes, 'find': cmd_find}[a.cmd](a)


if __name__ == '__main__':
    main()
