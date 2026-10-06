#!/usr/bin/env python3
"""Bounded, read-only access to the assigned family's local corpus."""
import argparse
import json
import re
import sqlite3
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / 'enrichment/v4/work/1_6/corpus-sol-max-20261006'
DB = ROOT / 'enrichment/corpus/corpus.sqlite'
PAGE_CHARS = 10000


def connect():
    return sqlite3.connect(f'file:{DB}?mode=ro', uri=True)


def family_config(family):
    if not re.fullmatch(r'[a-z-]+', family):
        raise ValueError('Invalid family')
    return json.loads((WORK / family / 'sources.json').read_text())


def eligible(config):
    return [s['id'] for s in config['sources'] if s['usable']]


def filters(config, requested=None):
    ids = eligible(config)
    if requested:
        if requested not in ids:
            raise ValueError('Source is unavailable, lacks an allowed original, or outside this family')
        ids = [requested]
    if not ids:
        return 'NULL', []
    return ','.join('?' for _ in ids), ids


def list_rows(con, sql, values, offset, limit):
    total = con.execute('SELECT count(*) FROM (' + sql + ')', values).fetchone()[0]
    rows = con.execute(sql + ' ORDER BY seg.src,seg.id LIMIT ? OFFSET ?', [*values, limit, offset]).fetchall()
    print(json.dumps({'total_segments': total, 'offset': offset, 'shown': len(rows),
                      'next_offset': offset + len(rows) if offset + len(rows) < total else None}))
    for loc, sid, head, chars in rows:
        print(json.dumps({'loc': loc, 'source': sid, 'head': head, 'characters': chars}, ensure_ascii=False))


def index(con, config, verse, offset, limit):
    s, a = map(int, verse.split(':'))
    placeholders, ids = filters(config)
    sql = ('SELECT seg.seg,seg.src,seg.head,length(coalesce(seg.text,"")) FROM seg '
           f'WHERE seg.src IN ({placeholders}) AND seg.id IN ('
           'SELECT id FROM seg WHERE s=? AND a<=? AND coalesce(a_end,a)>=? '
           'UNION SELECT seg_id FROM ref WHERE s=? AND a<=? AND coalesce(a_end,a)>=?)')
    list_rows(con, sql, [*ids, s, a, a, s, a, a], offset, limit)


def catalog(con, config, source, offset, limit):
    placeholders, ids = filters(config, source)
    sql = ('SELECT seg.seg,seg.src,seg.head,length(coalesce(seg.text,"")) FROM seg '
           f'WHERE seg.src IN ({placeholders})')
    list_rows(con, sql, ids, offset, limit)


def body(row, config):
    loc, sid, head, text, extra = row
    extra = json.loads(extra or '{}')
    # Preserve all non-translation source flags, footnotes and grading metadata.
    details = {k: v for k, v in extra.items() if k not in ('en', 'tr')}
    parts = [text or '']
    if details:
        parts.append('CORPUS SOURCE NOTES / FLAGS: ' + json.dumps(details, ensure_ascii=False))
    if config['family'] == 'meal':
        for key in ('en', 'tr'):
            if extra.get(key):
                parts.append(key + ': ' + (extra[key] if isinstance(extra[key], str) else json.dumps(extra[key], ensure_ascii=False)))
    return '\n\n'.join(parts)


def get(con, config, locator, start):
    row = con.execute('SELECT seg,src,head,text,extra FROM seg WHERE seg=?', (locator,)).fetchone()
    if not row or row[1] not in eligible(config):
        raise ValueError('Unknown or out-of-family locator; no external fallback')
    text = body(row, config)
    if start < 0 or start >= len(text):
        raise ValueError('Invalid continuation offset')
    end = min(start + PAGE_CHARS, len(text))
    metadata = next(s for s in config['sources'] if s['id'] == row[1])
    print(json.dumps({'loc': locator, 'source': metadata, 'head': row[2], 'start': start,
                      'end': end, 'total_characters': len(text), 'next_start': end if end < len(text) else None}, ensure_ascii=False))
    print(text[start:end])


def normalized(text):
    text = unicodedata.normalize('NFKC', text)
    text = re.sub(r'[ؐ-ًؚ-ٰٟۖ-ۭـ]', '', text)
    text = text.translate(str.maketrans({'أ':'ا','إ':'ا','آ':'ا','ٱ':'ا','ى':'ي','ة':'ه','ؤ':'و','ئ':'ي','ı':'i','İ':'i','I':'i'})).lower()
    text = ''.join(c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c) or '؀' <= c <= 'ۿ')
    return re.sub(r'\s+', ' ', text).strip()


def search(con, config, query, source, offset, limit):
    mode = json.loads((WORK / 'run.json').read_text())['corpus_keyword_search']
    if not mode:
        raise ValueError('Keyword search is disabled for this run')
    placeholders, ids = filters(config, source)
    words = normalized(query).split()
    if not words:
        raise ValueError('Empty query')
    expression = ' '.join('"' + w.replace('"', '""') + '"*' for w in words)
    sql = ('SELECT seg.seg,seg.src,seg.head,length(coalesce(seg.text,"")) FROM f JOIN seg ON seg.id=f.rowid '
           f'WHERE f MATCH ? AND seg.src IN ({placeholders})')
    print('CORPUS DISCOVERY ONLY; read full relevant passages before attribution. Query:', expression)
    list_rows(con, sql, [expression, *ids], offset, limit)


def main():
    global WORK
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--unit', choices=('1_6', '87_6'), default='1_6')
    parser.add_argument('--lane', choices=('sol-max', 'sol-high'), default='sol-max')
    parser.add_argument('family')
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('index'); p.add_argument('verse')
    p = sub.add_parser('catalog'); p.add_argument('source')
    p = sub.add_parser('search'); p.add_argument('query'); p.add_argument('--source')
    p = sub.add_parser('get'); p.add_argument('locator'); p.add_argument('--start', type=int, default=0)
    for name in ('index', 'catalog', 'search'):
        p = sub.choices[name]
        p.add_argument('--offset', type=int, default=0); p.add_argument('--limit', type=int, default=12)
    args = parser.parse_args()
    WORK = ROOT / f'enrichment/v4/work/{args.unit}/corpus-{args.lane}-20261006'
    config = family_config(args.family)
    with connect() as con:
        if args.command == 'get':
            get(con, config, args.locator, args.start)
        else:
            if args.offset < 0 or not 1 <= args.limit <= 30:
                raise ValueError('Use nonnegative offset and a limit of 1–30')
            if args.command == 'index': index(con, config, args.verse, args.offset, args.limit)
            elif args.command == 'catalog': catalog(con, config, args.source, args.offset, args.limit)
            else: search(con, config, args.query, args.source, args.offset, args.limit)


if __name__ == '__main__':
    main()
