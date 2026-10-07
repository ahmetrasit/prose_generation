#!/usr/bin/env python3
"""Build a verse-range overlay for segments whose text runs past their indexed ayah.

Example: WAHIDI-ASBAB:v1p55#2 is indexed to 2:190, yet it quotes and explains 2:190-194.
A packet built from the index alone misses it for 2:194 (seen on 100:1). The corpus is
never modified: the overlay is a separate file that packet.py reads.

Rule (deliberately narrow): a verse number in braces directly after a closing verse-quote
brace, optionally with الآية/الآيات between, e.g. «...} {194}» or «...} الآية {79}».
Plain parenthesised numbers are footnote markers in several editions and are ignored.

  python3 -B enrichment/v5/ranges.py build
"""
import argparse
import re
from collections import Counter

from common import OVERLAY, connect, write_rows

MARKER = re.compile(r'\}\s*(?:الآية|الآيات|الاية|الايات)?\s*\{\s*(\d{1,3})\s*\}')


def build():
    out, per_source = [], Counter()
    with connect() as con:
        for seg_id, seg, src, s, a, a_end, text in con.execute(
                'SELECT id,seg,src,s,a,a_end,text FROM seg WHERE s IS NOT NULL AND a IS NOT NULL'):
            hi = a_end or a
            marks = sorted({int(m[1]) for m in MARKER.finditer(text or '') if hi < int(m[1]) <= a + 40})
            if marks:
                out.append({'seg_id': seg_id, 'seg': seg, 'src': src, 's': s, 'a': a,
                            'indexed_end': hi, 'a_end': marks[-1], 'markers': marks})
                per_source[src] += 1
    write_rows(OVERLAY, out)
    print(f'{len(out)} segments extended; {OVERLAY}')
    for src, n in per_source.most_common(15):
        print(f'  {src:20} {n}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('command', choices=('build',))
    parser.parse_args()
    build()
