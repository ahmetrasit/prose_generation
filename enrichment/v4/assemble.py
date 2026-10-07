#!/usr/bin/env python3
"""Check paragraph/source links and attach corpus blocks to frozen prose."""
import html
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'enrichment/v3'))
import pilot
import corpus_read
from memory_assemble import FAMILIES
from corpus_read import WORK, connect, contains_anchor, eligible, family_config


def rows(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def compact(text):
    return re.sub(r'\s+', ' ', text).strip()


def main():
    global WORK
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--unit', choices=('1_6', '87_6', '100_1'), default='1_6')
    parser.add_argument('--run-date', default='20261006')
    parser.add_argument('--families', nargs='+', choices=tuple(FAMILIES))
    parser.add_argument('--lane', choices=('sol-max', 'sol-high'), default='sol-max')
    args = parser.parse_args()
    if not re.fullmatch(r'\d{8}', args.run_date):
        parser.error('--run-date must be YYYYMMDD')
    WORK = ROOT / f'enrichment/v4/work/{args.unit}/corpus-{args.lane}-{args.run_date}'
    corpus_read.WORK = WORK
    pilot.BASE = WORK / 'frozen.reading.tr.md'
    frozen, paragraphs = pilot.prose()
    expected = set(paragraphs)
    primary, links = defaultdict(list), defaultdict(list)
    seen = set()
    count = 0
    with connect() as con:
        families = args.families or list(FAMILIES)
        for family in families:
            config = family_config(family)
            blocks = rows(WORK / family / 'blocks.jsonl')
            ledger = rows(WORK / family / 'ledger.jsonl')
            if len(ledger) != len(expected) or {r['p'] for r in ledger} != expected:
                raise ValueError(f'{family}: missing or repeated paragraph ledger')
            entries = {r['p']: r for r in ledger}
            by_id = {b['id']: b for b in blocks}
            if len(by_id) != len(blocks):
                raise ValueError(f'{family}: repeated block IDs')
            for block in blocks:
                identifier = block['id']
                ps = sorted(set(block['p']))
                if identifier in seen or not re.fullmatch(r'[A-Za-z0-9_-]+', identifier):
                    raise ValueError('Duplicate or invalid block ID')
                if not ps or not set(ps) <= expected or not block['text'].strip():
                    raise ValueError('Empty or unanchored block')
                seen.add(identifier)
                cited = set()
                if not block.get('evidence'):
                    raise ValueError(f'{identifier}: missing corpus evidence')
                for pointer in block['evidence']:
                    loc, anchor = pointer['loc'], pointer['anchor']
                    row = con.execute('SELECT seg,src,head,text,extra FROM seg WHERE seg=?', (loc,)).fetchone()
                    if not row or row[1] not in eligible(config):
                        raise ValueError(f'{identifier}: unavailable or out-of-family evidence {loc}')
                    if not contains_anchor(row, config, anchor):
                        raise ValueError(f'{identifier}: supporting anchor not found in {loc}')
                    cited.add(row[1])
                if set(block['sources']) != cited:
                    raise ValueError(f'{identifier}: source IDs and evidence pointers differ')
                for p in ps:
                    if entries[p]['status'] != 'written' or identifier not in entries[p]['blocks']:
                        raise ValueError(f'{identifier}: missing written ledger link at {p}')
                primary[ps[0], family].append(block)
                for p in ps[1:]:
                    links[p, family].append((identifier, ps[0]))
                count += 1
            for entry in ledger:
                if entry['status'] not in ('written', 'no_match'):
                    raise ValueError(f'{family}: invalid status')
                if bool(entry['blocks']) != (entry['status'] == 'written'):
                    raise ValueError(f'{family}: status/block mismatch')
                for identifier in entry['blocks']:
                    if identifier not in by_id or entry['p'] not in by_id[identifier]['p']:
                        raise ValueError(f'{family}: broken ledger pointer')
    pieces, at = [], 0
    for p, (_, end) in paragraphs.items():
        sections = []
        for family in families:
            title = FAMILIES[family]
            blocks, related = primary[p, family], links[p, family]
            if not blocks and not related:
                continue
            sections.append('### ' + title)
            for block in blocks:
                references = '; '.join(pointer['loc'] + ' — «' + compact(pointer['anchor']) + '»' for pointer in block['evidence'])
                sections.append('<a id="corpus-' + html.escape(block['id'], quote=True) + '"></a>\n\n' + block['text'] + '\n\nKaynak konumları: ' + references + '.')
            if related:
                sections.append('Bu paragrafla da ilgili kaynak görüşü: ' + ', '.join(f'[{origin}. paragraf](#corpus-{identifier})' for identifier, origin in related) + '.')
        pieces.append(frozen[at:end])
        if sections:
            pieces.append(f'\n\n<!-- enrichment:corpus paragraph={p} -->\n\n' + '\n\n'.join(sections) + '\n\n<!-- /enrichment:corpus -->')
        at = end
    pieces.append(frozen[at:])
    rendered = ''.join(pieces)
    recovered = re.sub(r'\n\n<!-- enrichment:corpus paragraph=\d+ -->.*?\n\n<!-- /enrichment:corpus -->', '', rendered, flags=re.S)
    if recovered.encode() != frozen.encode() or rendered.count('<a id="corpus-') != count:
        raise ValueError('Assembly changed frozen prose or lost a block')
    intro = ('> **Kaynak notları hakkında:** Aile notları yalnız bu çalışmada okunan yerel korpus pasajlarına dayanır. '
             'Kaynak konumları ve kısa ibareler pasajları bulmaya yardım eder; bunların bulunması yorumun anlamsal doğruluğunu tek başına kanıtlamaz. '
             'Bulunamayan katkılar yalnız incelenen malzemeyle sınırlıdır; tarihsel yokluk veya yenilik iddiası değildir.\n\n')
    target = WORK / f'{args.unit}.enriched.tr.md'
    target.write_bytes((intro + rendered).encode())
    print(f'{len(families)} families; {count} blocks; source anchors and ledger links checked; frozen bytes preserved; {target}')


if __name__ == '__main__':
    main()
