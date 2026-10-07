#!/usr/bin/env python3
"""Build a family's source packet for a frozen page: no model, no text cuts.

For every paragraph, the packet takes the verses it cites (plus the target ayah and its
neighbours) and gathers each usable roster segment indexed to those verses, including the
range overlay (ranges.py). Segments are kept whole. A per-ayah slice of a work that is also
held whole (X versus X-FULL) is used only for verses the FULL copy does not cover.

The packet is split into chunks (one fresh extractor context each); chunk text files carry a
header per segment naming its locator, source and the paragraphs it serves.

  python3 -B enrichment/v5/packet.py plan --unit 1_6
  python3 -B enrichment/v5/packet.py build --unit 100_1 --family rivayet --out DIR
"""
import argparse
import json
from collections import defaultdict
from pathlib import Path

from common import (CHUNK_CHARS, DIRECT_MAX_TOKENS, FAMILIES, OVERLAY, PACKET_PLUS_SEARCH, SEARCH,
                    body, connect, dump, rows, sources, tokens, usable, verses_by_paragraph, write_rows)


def overlay():
    by_verse = defaultdict(set)
    if OVERLAY.exists():
        for r in rows(OVERLAY):
            for a in range(r['indexed_end'] + 1, r['a_end'] + 1):
                by_verse[r['s'], a].add(r['seg_id'])
    return by_verse


def gather(con, unit, family):
    config = sources(family)
    ids = usable(config)
    full = {i[:-5] for i in ids if i.endswith('-FULL')}
    extra = overlay()
    wanted = defaultdict(lambda: {'verses': set(), 'paragraphs': set()})
    for p, verses in verses_by_paragraph(unit).items():
        for s, a in sorted(verses):
            hits = {r[0]: r[1] for r in con.execute(
                f'SELECT id,src FROM seg WHERE src IN ({",".join("?" * len(ids))}) '
                'AND s=? AND a<=? AND coalesce(a_end,a)>=?', [*ids, s, a, a])}
            for seg_id in extra.get((s, a), ()):
                src = con.execute('SELECT src FROM seg WHERE id=?', (seg_id,)).fetchone()[0]
                if src in ids:
                    hits[seg_id] = src
            covered = {src[:-5] for src in hits.values() if src.endswith('-FULL')}
            for seg_id, src in hits.items():
                if src in full and src in covered:
                    continue          # slice duplicates the whole work for this verse
                wanted[seg_id]['verses'].add(f'{s}:{a}')
                wanted[seg_id]['paragraphs'].add(p)
    segments = []
    for seg_id in sorted(wanted, key=lambda i: con.execute('SELECT src,id FROM seg WHERE id=?', (i,)).fetchone()):
        row = con.execute('SELECT seg,src,head,text,extra FROM seg WHERE id=?', (seg_id,)).fetchone()
        text = body(row, family)
        segments.append({'loc': row[0], 'src': row[1], 'head': row[2] or '',
                         'verses': sorted(wanted[seg_id]['verses'], key=lambda v: tuple(map(int, v.split(':')))),
                         'paragraphs': sorted(wanted[seg_id]['paragraphs']), 'chars': len(text), 'text': text})
    return config, segments


def route_for(family, packet_tokens):
    if family in SEARCH:
        return 'search'
    base = 'direct' if packet_tokens <= DIRECT_MAX_TOKENS else 'extract'
    return base + '+search' if family in PACKET_PLUS_SEARCH else base


def header(seg):
    return (f"=== SEGMENT {seg['loc']} | source {seg['src']} | {seg['head'][:160]} | "
            f"verses {', '.join(seg['verses'])} | paragraphs {', '.join(map(str, seg['paragraphs']))} ===")


def chunk(segments, limit=CHUNK_CHARS):
    chunks, current, size = [], [], 0
    for seg in segments:
        t = seg['chars'] + len(header(seg)) + 2
        if t > limit:
            raise ValueError(f"{seg['loc']}: one segment exceeds the chunk limit; split rule needed")
        if current and size + t > limit:
            chunks.append(current)
            current, size = [], 0
        current.append(seg)
        size += t
    if current:
        chunks.append(current)
    return chunks


def build(unit, family, out, route=None):
    out = Path(out)
    if (out / 'manifest.json').exists():
        raise ValueError(f'{out} already holds a packet; packets are never overwritten')
    with connect() as con:
        config, segments = gather(con, unit, family)
    total = sum(s['chars'] for s in segments)
    chosen = route or route_for(family, tokens(total))
    chunks = chunk(segments) if chosen.startswith('extract') else [segments]
    write_rows(out / 'segments.jsonl', segments)
    for n, group in enumerate(chunks, 1):
        text = '\n\n'.join(header(s) + '\n' + s['text'] for s in group)
        (out / f'chunk-{n:02d}.txt').write_text(text + '\n')
    per_source = defaultdict(lambda: [0, 0])
    for s in segments:
        per_source[s['src']][0] += 1
        per_source[s['src']][1] += s['chars']
    dump(out / 'manifest.json', {
        'unit': unit, 'family': family, 'route': chosen, 'segments': len(segments), 'characters': total,
        'estimated_tokens': tokens(total), 'chunks': [{'n': n, 'segments': [s['loc'] for s in g],
                                                     'characters': sum(s['chars'] for s in g)}
                                                    for n, g in enumerate(chunks, 1)],
        'per_source': {k: {'segments': v[0], 'characters': v[1]} for k, v in sorted(per_source.items())},
        'unusable_sources': [{'id': s['id'], 'limitation': s.get('limitation', '')}
                             for s in config['sources'] if not s['usable']],
        'translations': {s['id']: s['translation'] for s in config['sources'] if s.get('translation')},
        'rule': 'Every usable roster segment indexed to a cited verse (plus overlay), whole; '
                'X slice skipped where X-FULL covers the verse. Token figures are chars/3 estimates.'})
    (out / 'sources.json').write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n')
    print(f'{unit} {family}: {len(segments)} segments, ~{tokens(total):,} tokens, route {chosen}, {len(chunks)} chunk(s) -> {out}')
    return chosen


def plan(unit):
    with connect() as con:
        print(f'{unit}: {len(set().union(*verses_by_paragraph(unit).values()))} verses cited')
        for family in FAMILIES:
            if family in SEARCH:
                print(f'  {family:20} route search (not verse-indexed)')
                continue
            _, segments = gather(con, unit, family)
            t = tokens(sum(s['chars'] for s in segments))
            r = route_for(family, t)
            n = len(chunk(segments)) if r.startswith('extract') else 1
            print(f'  {family:20} {len(segments):5} segments ~{t:>9,} tokens  route {r:15} chunks {n}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('command', choices=('plan', 'build'))
    parser.add_argument('--unit', required=True, choices=('1_6', '87_6', '100_1'))
    parser.add_argument('--family', choices=tuple(FAMILIES))
    parser.add_argument('--out')
    parser.add_argument('--route', choices=('direct', 'extract', 'direct+search', 'extract+search'))
    args = parser.parse_args()
    if args.command == 'plan':
        plan(args.unit)
    else:
        if not (args.family and args.out):
            parser.error('build needs --family and --out')
        build(args.unit, args.family, args.out, args.route)
