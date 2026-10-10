#!/usr/bin/env python3
"""Enrichment v9 C1: the material of each verse and its route, so that no source is dropped silently. Launches no
model; changes nothing.

For every verse: the segments tied to it (index range and range overlay), split into
  - in tier 1 (digested by the tier-1 model the maps were built from),
  - tier-1 kinds NOT yet digested (a gap: the map lacks them),
  - old outputs whose original input cannot be verified (unresolved legacy provenance),
  - other kinds, each with its route: meal → meal table and meal block; translation → meal block (control);
    lexicon → not used (project dictionary only; the writer gets no dictionary); poetry, wujūh, grammar →
    word stage (not built); no local text; empty text;
plus the quotation packet (works with no verse index that quote the verse's own words), digested or not, and the
surah-level segments of each surah (route: surah page).

  material.py RUN --ayat 103:1 12:49 … [--tier1 luna-max]      writes enrichment/v9/work/RUN/material/manifest.json
"""
import argparse
import sys
from collections import defaultdict
from pathlib import Path

V9 = Path(__file__).resolve().parent
sys.path.insert(0, str(V9.parent / 'v7'))
import digest  # noqa: E402
from digest import V7, dump  # noqa: E402

ROUTE = {
    'meal': 'meal table and meal block (C5, P3)',
    'translation': 'meal block (translation control)',
    'lexicon': 'not used: project dictionary only; the writer gets no dictionary',
    'poetry': 'word stage (not built)',
    'wujuh': 'word stage (not built)',
    'grammar': 'word stage (not built)',
    'quran': 'verse text',
}


def digested(tag):
    """Locators with verified Tier 1 lines, and locators whose legacy input cannot be checked."""
    locs = set()
    for f in (V7 / 'work').glob(f'*/out/{tag}/c*.jsonl'):
        locs.update(digest.valid_output_locs(f))
    return locs, digest.UNVERIFIED_OUTPUT_LOCS - locs


def route_of(reason, kind):
    if reason.startswith('kind '):
        return ROUTE.get(kind, f'no route for kind {kind}')
    if reason.startswith('access'):
        return 'no local text'
    if reason == 'empty text':
        return 'no text (empty segment)'
    return reason


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('run')
    ap.add_argument('--ayat', nargs='+', required=True)
    ap.add_argument('--tier1', default='luna-max')
    a = ap.parse_args()
    ayat = [tuple(map(int, x.split(':'))) for x in a.ayat]
    done, unresolved = digested(a.tier1)
    src, found, skipped = digest.gather(ayat)
    quotes = digest.quote_packet(ayat)
    quote_limits = digest.QUOTE_LIMITS
    surah = digest.surah_level(ayat)
    with digest.connect() as con:
        kind = {i: k for i, k in con.execute('SELECT id, kind FROM src')}
        size = {loc: n for loc, n in con.execute(
            f"SELECT seg, length(text) FROM seg WHERE seg IN ({','.join('?' * len({x['loc'] for x in skipped}))})",
            [x['loc'] for x in {x['loc']: x for x in skipped}.values()])} if skipped else {}
    per = {f'{s}:{x}': {'tier1': [], 'gap': [], 'unresolved_legacy': [], 'routes': defaultdict(list),
                        'quotes': [], 'quotes_gap': [], 'quotes_unresolved_legacy': []} for s, x in ayat}
    for g in found:
        for v in g['scope']:
            field = 'tier1' if g['loc'] in done else 'unresolved_legacy' if g['loc'] in unresolved else 'gap'
            per[v][field].append({'loc': g['loc'], 'src': g['src'], 'chars': len(g['text'])})
    for x in skipped:
        r = route_of(x['reason'], kind.get(x['src'], ''))
        per[x['ayah']]['routes'][r].append({'loc': x['loc'], 'src': x['src'], 'chars': size.get(x['loc'], 0)})
    for g in quotes:
        for v in g['scope']:
            field = 'quotes' if g['loc'] in done else 'quotes_unresolved_legacy' if g['loc'] in unresolved else 'quotes_gap'
            per[v][field].append({'loc': g['loc'], 'src': g['src'], 'kind': g['kind'], 'chars': len(g['text'])})
    surahs = defaultdict(list)
    for x in surah:
        surahs[x['ayah']].append({'loc': x['loc'], 'src': x['src']})

    def n(xs):
        return f"{len(xs)} ({sum(x['chars'] for x in xs) // 1000}k)"

    print(f"\n{'verse':<8} {'tier 1':>12} {'GAP tier1':>11} {'LEGACY ?':>11} {'quotes in':>10} {'QUOTES GAP':>11} {'Q LEGACY ?':>11}  other routes")
    for v, d in per.items():
        other = '; '.join(f"{r.split(':')[0].split(' (')[0]} {n(xs)}" for r, xs in sorted(d['routes'].items()))
        print(f"{v:<8} {n(d['tier1']):>12} {n(d['gap']):>11} {n(d['unresolved_legacy']):>11} "
              f"{n(d['quotes']):>10} {n(d['quotes_gap']):>11} {n(d['quotes_unresolved_legacy']):>11}  {other}")
    for s, xs in surahs.items():
        print(f'{s}: {len(xs)} surah-level segments → surah page')
    gaps = sum(len(d['gap']) + len(d['quotes_gap']) for d in per.values())
    unknown = sum(len(d['unresolved_legacy']) + len(d['quotes_unresolved_legacy']) for d in per.values())
    print(f'\n{gaps} segment placements have no valid Tier 1 output; {unknown} have unresolved legacy input provenance')
    out = V9 / 'work' / a.run / 'material'
    out.mkdir(parents=True, exist_ok=True)
    dump(out / 'manifest.json', {'tier1': a.tier1, 'verses': {v: {**d, 'routes': dict(d['routes'])} for v, d in per.items()},
                                 'quote_limits': quote_limits, 'surah_level': dict(surahs)})
    print(f'written {out.relative_to(digest.ROOT)}/manifest.json')


if __name__ == '__main__':
    main()
