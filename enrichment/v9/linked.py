#!/usr/bin/env python3
"""Segment links per verse (2026-10-10). A digest serves every verse it names: merge.tier1_rows already finds a note
under each verse its `verses` or `mentions` name. This index adds the segments tied to a verse by the corpus itself,
by the verse's index range (digest.gather) or by quoting the verse's own words (digest.quote_packet), so that
`q.py linked V` can show the ones whose notes are about other verses. Nothing is digested again.

  linked.py build (--ayat 96:1 96:2 | --surahs 1 59 87 …)    writes enrichment/v9/linked/<k>.json, one file per verse

The quotation search takes about 40 seconds per call, so the index is built once per range (all ayat in one call),
not at lookup time. Each file records a content stamp (a hash of the corpus index's sources and per-source segment
sizes, of the range overlay, and of the link code); q.py linked says when the current stamp differs. Segments that gather() ties to the verse but that tier 1 does not take
(kind, access, empty text) are kept per verse under "skipped" with the reason. Each build writes its own log
(window-by-window lines of the quotation search) under linked/logs/.
"""
import argparse
import contextlib
import hashlib
import inspect
import io
import sys
import time
from collections import Counter
from pathlib import Path

V9 = Path(__file__).resolve().parent
sys.path.insert(0, str(V9.parent / 'v7'))
import digest  # noqa: E402
import merge  # noqa: E402
from digest import ROOT, connect, dump  # noqa: E402

OUT = V9 / 'linked'
CORPUS = ROOT / 'enrichment/corpus/corpus.sqlite'
LINKED_VERSION = '2026-10-10'


def stamp():
    """What the links depend on, by content, so that a copy reassembled on another machine matches: the corpus index
    (a hash of its src rows; per source, segment count, text and heading lengths and last id; every verse key; the
    Qur'an text), the
    range overlay (sha256), and the link code (the source of gather, quote_packet and normalize_map and the constants
    they use)."""
    h = hashlib.sha256()
    with connect() as con:
        for r in con.execute('SELECT id, kind, access, meta FROM src ORDER BY id'):
            h.update(repr(r).encode())
        for r in con.execute('SELECT src, count(*), sum(length(text)), sum(length(head)), max(id) FROM seg '
                             'GROUP BY src ORDER BY src'):
            h.update(repr(r).encode())
        for r in con.execute('SELECT id, seg, src, s, a, a_end FROM seg WHERE s IS NOT NULL ORDER BY id'):
            h.update(repr(r).encode())       # every verse key: a re-index changes the links
        for r in con.execute("SELECT seg.id, seg.text FROM seg JOIN src ON src.id=seg.src WHERE src.kind='quran' "
                             'ORDER BY seg.id'):
            h.update(repr(r).encode())       # the verse text the quotation windows come from
    o = hashlib.sha256(digest.OVERLAY.read_bytes()).hexdigest() if digest.OVERLAY.exists() else None
    code = ''.join(inspect.getsource(fn) for fn in (digest.gather, digest.quote_packet, digest.normalize_map))
    code += repr((digest.KINDS, digest.QUOTE_KINDS_ONE, digest.QUOTE_KINDS_THREE, digest.QUOTE_MAX_HITS,
                  digest._ARABIC_MAP, sorted(digest._ARABIC_DROP)))
    return {'corpus_sha256': h.hexdigest(), 'overlay_sha256': o,
            'code_sha256': hashlib.sha256(code.encode()).hexdigest(), 'version': LINKED_VERSION}


def key(ayah):
    return ayah.replace(':', '-')


def build(a):
    if a.surahs:
        with connect() as con:
            ayat = [f'{s}:{x}' for s, x in con.execute(
                "SELECT s, a FROM seg JOIN src ON src.id=seg.src WHERE src.kind='quran' AND s IN (%s) ORDER BY s, a"
                % ','.join('?' * len(a.surahs)), a.surahs)]
    else:
        ayat = list(dict.fromkeys(a.ayat))
        with connect() as con:
            known = {f'{s}:{x}' for s, x in con.execute("SELECT s, a FROM seg JOIN src ON src.id=seg.src "
                                                        "WHERE src.kind='quran' AND a IS NOT NULL")}
        bad = [v for v in ayat if v not in known]
        if bad:
            raise SystemExit(f'not verses of the Qur\'an text: {", ".join(bad)}')
    if not ayat:
        raise SystemExit('no verses')
    pairs = [digest.parse_ayah(x) for x in ayat]
    st = {'built_at': time.strftime('%Y-%m-%dT%H:%M:%S'), **stamp()}     # before the build: a later change shows
    t0 = time.time()
    (OUT / 'logs').mkdir(parents=True, exist_ok=True)
    logf = OUT / 'logs' / f"{time.strftime('%Y%m%d-%H%M%S')}_{key(ayat[0])}_{key(ayat[-1])}.log"
    log = io.StringIO()
    try:
        with contextlib.redirect_stdout(log):      # the window-by-window lines of the quotation search
            _, found, skipped = digest.gather(pairs)
            quotes = digest.quote_packet(pairs)
    finally:
        logf.write_text(log.getvalue())
    notes = [x for x in log.getvalue().splitlines() if x.startswith('NOTE')]
    per = {v: {} for v in ayat}
    for g, how in [(g, 'index') for g in found] + [(g, 'quotes') for g in quotes]:
        for v in g['scope']:
            if v in per and g['loc'] not in per[v]:
                label = g['verses']
                if how == 'quotes':                 # quote_packet labels a segment by its first verse; label it per verse
                    label = f"{v} (quoted{label.split(' (quoted', 1)[1]}" if ' (quoted' in label else f'{v} (quoted)'
                per[v][g['loc']] = {'src': g['src'], 'kind': g['kind'], 'by': how, 'verses': label}
    skips = {v: [] for v in ayat}
    for x in skipped:
        for v in x['ayah'].split(','):
            if v in skips:
                skips[v].append({'loc': x['loc'], 'src': x['src'], 'reason': x['reason']})
    for v, segs in per.items():
        dump(OUT / f'{key(v)}.json', {'ayah': v, **st, 'segments': segs, 'skipped': skips[v]})
    n = sum(len(s) for s in per.values())
    reasons = Counter(x['reason'].split(':')[0] for xs in skips.values() for x in xs)
    print(f'{len(ayat)} verses, {n} segment links ({sum(1 for s in per.values() for x in s.values() if x["by"] == "quotes")} '
          f'by quotation), {time.time() - t0:.0f} s; written {OUT.relative_to(ROOT)}/<k>.json')
    print(f'not tier-1 material, kept per verse under "skipped": {sum(reasons.values())} '
          + (f"({', '.join(f'{r} {c}' for r, c in reasons.most_common())})" if reasons else ''))
    for x in notes:
        print(x)
    print(f'{len(notes)} NOTE line(s) above; window log {logf.relative_to(ROOT)}')
    unread, rows_nowhere = Counter(), 0          # verse values no verse lookup can read (merge.tier1_rows files by them)
    for _, x, _, _ in merge.tier1_segments(a.tier1):
        for r in x.get('rows') or []:
            rej = []
            vs = digest.verse_list(r.get('verses'), rej)
            digest.verse_list(r.get('mentions'), rej)
            unread.update(str(v) for v in rej)
            rows_nowhere += not vs
    if unread:
        with logf.open('a') as f:
            f.write('\nverse values not read (count, value):\n' + ''.join(f'{n}\t{v}\n' for v, n in unread.most_common()))
    print(f"tier 1 ({', '.join(a.tier1)}): {sum(unread.values())} verse values not read as Qur'an verses "
          f"({len(unread)} distinct, listed in the log); {rows_nowhere} rows name no readable verse and are filed only "
          'where their mentions name one')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('build')
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument('--ayat', nargs='+')
    g.add_argument('--surahs', nargs='+', type=int)
    p.add_argument('--tier1', nargs='+', default=['luna-max'], help='tier-1 model tags whose verse values are checked')
    a = ap.parse_args()
    build(a)


if __name__ == '__main__':
    main()
