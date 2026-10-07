#!/usr/bin/env python3
"""The only corpus/packet access a v5 agent uses. Read-only; scoped to one family directory.

  read.py DIR input N                 frozen page, part N (1-4)
  read.py DIR chunk C --part K        packet chunk C, delivery K (extractors; direct writers)
  read.py DIR extracts --part K       all checked extracts for this family, by paragraph (writers)
  read.py DIR get LOCATOR --part K    one whole segment, paged (writers; search routes)
  read.py DIR search "WORDS" [--source ID] [--offset N]   roster keyword discovery (search routes only)
  read.py DIR candidates --part K     memory leads with corpus hits found by leads.py (search routes)
  read.py DIR selfcheck C             extractor's own check of chunk C outputs (prints OK or the problems)

DIR is the family directory named in the brief, e.g. enrichment/v5/work/100_1/pilot-20261007/rivayet.
Every delivery is at most PART_CHARS characters and states the next offset; nothing is cut.
"""
import argparse
import json
import sys
from pathlib import Path

from common import PART_CHARS, ROOT, body, connect, normalized, rows, usable


def deliver(text, part, label):
    start = part * PART_CHARS
    if part < 0 or (start >= len(text) and text):
        raise SystemExit(f'No delivery {part} for {label}')
    end = min(start + PART_CHARS, len(text))
    total = max(1, -(-len(text) // PART_CHARS))
    nxt = part + 1 if end < len(text) else None
    print(f'<<{label} | delivery {part} of 0..{total - 1} | characters {start}-{end} of {len(text)} | next: {nxt}>>')
    print(text[start:end])
    if nxt is not None:
        print(f'<<continues in delivery {nxt}; a segment may span deliveries>>')


def family_dir(path):
    d = (ROOT / path).resolve() if not Path(path).is_absolute() else Path(path)
    if not (d / 'packet/manifest.json').exists() and not (d / 'family.json').exists():
        raise SystemExit(f'{path} is not a v5 family directory')
    return d


def render_extracts(d):
    items = []
    for f in sorted((d / 'extract').glob('c*/extracts.jsonl')):
        items += rows(f)
    if not items:
        raise SystemExit('No checked extracts yet')
    by_p = {}
    for x in items:
        for p in x['p']:
            by_p.setdefault(p, []).append(x)
    out = []
    for p in sorted(by_p):
        out.append(f'##### Paragraph {p}')
        for x in by_p[p]:
            out.append(f"[{x['loc']}] ({x['kind']}) {x['note']}\n«{x['quote']}»")
    return '\n\n'.join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('dir')
    sub = parser.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('input'); p.add_argument('n', type=int)
    p = sub.add_parser('chunk'); p.add_argument('c', type=int); p.add_argument('--part', type=int, default=0)
    p = sub.add_parser('extracts'); p.add_argument('--part', type=int, default=0)
    p = sub.add_parser('get'); p.add_argument('loc'); p.add_argument('--part', type=int, default=0)
    p = sub.add_parser('search'); p.add_argument('query'); p.add_argument('--source'); p.add_argument('--offset', type=int, default=0)
    p = sub.add_parser('candidates'); p.add_argument('--part', type=int, default=0)
    p = sub.add_parser('selfcheck'); p.add_argument('c', type=int)
    a = parser.parse_args()
    d = family_dir(a.dir)
    meta = json.loads((d / 'family.json').read_text())
    family = meta['family']
    if a.cmd == 'selfcheck':
        import check
        problems, _ = check.check_extract(d, only=a.c, record=False)
        print('OK' if not problems else '\n'.join(problems[:60]) + (f'\n... {len(problems) - 60} more' if len(problems) > 60 else ''))
        return
    if a.cmd == 'input':
        f = d.parent / f'input-{a.n}.txt'
        if not f.exists():
            raise SystemExit('Inputs are numbered 1-4')
        print(f.read_text())
    elif a.cmd == 'chunk':
        f = d / f'packet/chunk-{a.c:02d}.txt'
        if not f.exists():
            raise SystemExit('Unknown chunk')
        deliver(f.read_text(), a.part, f'{family} chunk {a.c}')
    elif a.cmd == 'extracts':
        deliver(render_extracts(d), a.part, f'{family} extracts')
    elif a.cmd == 'candidates':
        f = d / 'leads/candidates.txt'
        if not f.exists():
            raise SystemExit('No lead candidates for this family')
        deliver(f.read_text(), a.part, f'{family} lead candidates')
    elif a.cmd == 'get':
        locs = {s['loc'] for s in rows(d / 'packet/segments.jsonl')} if (d / 'packet/segments.jsonl').exists() else set()
        config = json.loads((d / 'packet/sources.json').read_text()) if (d / 'packet/sources.json').exists() else json.loads((d / 'sources.json').read_text())
        with connect() as con:
            row = con.execute('SELECT seg,src,head,text,extra FROM seg WHERE seg=?', (a.loc,)).fetchone()
        if not row or row[1] not in usable(config) or (a.loc not in locs and not meta.get('search')):
            raise SystemExit('Locator outside this family packet/roster; no fallback')
        text = f'=== {row[0]} | source {row[1]} | {row[2] or ""} ===\n' + body(row, family)
        deliver(text, a.part, a.loc)
    elif a.cmd == 'search':
        if not meta.get('search'):
            raise SystemExit('Keyword search is not part of this route')
        config = json.loads((d / 'sources.json').read_text())
        ids = usable(config)
        if a.source:
            if a.source not in ids:
                raise SystemExit('Source outside this family roster')
            ids = [a.source]
        words = normalized(a.query).split()
        if not words:
            raise SystemExit('Empty query')
        expr = ' '.join('"' + w.replace('"', '""') + '"*' for w in words)
        sql = (f'SELECT seg.seg,seg.src,seg.head,length(coalesce(seg.text,"")) FROM f JOIN seg ON seg.id=f.rowid '
               f'WHERE f MATCH ? AND seg.src IN ({",".join("?" * len(ids))}) ORDER BY seg.src,seg.id')
        with connect() as con:
            hits = con.execute(sql, [expr, *ids]).fetchall()
        shown = hits[a.offset:a.offset + 20]
        print(json.dumps({'query': expr, 'total': len(hits), 'offset': a.offset, 'shown': len(shown),
                          'next_offset': a.offset + 20 if a.offset + 20 < len(hits) else None}, ensure_ascii=False))
        for loc, src, head, chars in shown:
            print(json.dumps({'loc': loc, 'source': src, 'head': head, 'characters': chars}, ensure_ascii=False))
        print('DISCOVERY ONLY: read a passage with get before attributing anything to it.')


if __name__ == '__main__':
    sys.exit(main())
