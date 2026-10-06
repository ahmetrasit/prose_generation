#!/usr/bin/env python3
"""Attach memory-family blocks without editing the frozen commentary or blocks."""
import argparse
import html
import json
import re
from collections import defaultdict
from pathlib import Path

import pilot

WORK = Path(__file__).resolve().parent / 'work/1_6'
LANES = {
    'sol-high': WORK / 'family-memory-baseline-20261006',
    'luna6-max': WORK / 'family-memory-luna6-max-20261006',
    'astra-max': WORK / 'family-memory-astra-max-20261006',
    'astra-high': WORK / 'family-memory-astra-high-20261006',
    'sol-max': WORK / 'family-memory-sol-max-20261006',
}
FAMILIES = {
    'rivayet': 'Rivayet tefsiri',
    'kessaf': 'Keşşâf geleneği',
    'analytical': 'Kapsamlı dirayet tefsiri',
    'classical-coherence': 'Klasik nazm ve münasebet',
    'modern-coherence': 'Ferâhî–Islâhî ve retorik yapı',
    'bayani': 'Beyânî yorum',
    'ishari': 'İşârî yorum',
    'imami-mutazili': 'İmâmî ve Muʿtezilî yorum',
    'grammar': 'Nahiv, meânî ve garîb',
    'qiraat': 'Kıraat',
    'wujuh': 'Vücûh ve nezâir',
    'rhetoric': 'Belâgat ve iʿcâz',
    'modern-tafsir': 'Modern tefsir',
    'turkish-tafsir': 'Türkçe tefsir',
    'meal': 'Meal tercihleri ve anlam kaymaları',
    'hadith': 'Hadis',
    'historical': 'Tarih ve nüzul bağlamı',
    'academic': 'Akademik ve karşılaştırmalı çalışmalar',
    'poetry': 'Şiir şahitleri',
}


def rows(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def assemble(lane):
    folder = LANES[lane]
    pilot.BASE = folder / 'frozen.reading.tr.md'
    frozen, paragraphs = pilot.prose()
    expected = set(paragraphs)
    families = [family for family in FAMILIES if (folder / family).is_dir()]
    primary, links = defaultdict(list), defaultdict(list)
    seen, count = set(), 0
    for family in families:
        blocks = rows(folder / family / 'blocks.jsonl')
        ledger = rows(folder / family / 'ledger.jsonl')
        if len(ledger) != len(expected) or {row['p'] for row in ledger} != expected:
            raise ValueError(f'{lane}/{family}: missing or repeated paragraph ledger rows')
        by_id = {row['id']: row for row in blocks}
        if len(by_id) != len(blocks):
            raise ValueError(f'{lane}/{family}: repeated block IDs')
        for row in blocks:
            identifier = row['id']
            if identifier in seen or not re.fullmatch(r'[A-Za-z0-9_-]+', identifier):
                raise ValueError(f'Invalid or duplicate anchor ID: {identifier}')
            seen.add(identifier)
            locations = sorted(set(row['p']))
            if not locations or not set(locations) <= expected or not row['text'].strip():
                raise ValueError(f'Empty or unanchored block: {identifier}')
            primary[locations[0], family].append(row)
            for p in locations[1:]:
                links[p, family].append((identifier, locations[0]))
            for p in locations:
                entry = next(item for item in ledger if item['p'] == p)
                if identifier not in entry['blocks'] or entry['status'] != 'written':
                    raise ValueError(f'{identifier}: missing written ledger link at paragraph {p}')
            count += 1
        for entry in ledger:
            for identifier in entry['blocks']:
                if identifier not in by_id or entry['p'] not in by_id[identifier]['p']:
                    raise ValueError(f'{lane}/{family}: broken ledger link {identifier}')
    pieces, at = [], 0
    for p, (_, end) in paragraphs.items():
        sections = []
        for family in families:
            prose = primary[p, family]
            related = links[p, family]
            if not prose and not related:
                continue
            sections.append('### ' + FAMILIES[family])
            for row in prose:
                sections.append(f'<a id="memory-{html.escape(row["id"], quote=True)}"></a>\n\n' + row['text'])
            if related:
                pointers = ', '.join(f'[{origin}. paragraf](#memory-{identifier})' for identifier, origin in related)
                sections.append('Bu paragrafla da ilgili kaynak görüşü: ' + pointers + '.')
        pieces.append(frozen[at:end])
        if sections:
            pieces.append(f'\n\n<!-- enrichment:memory paragraph={p} -->\n\n' + '\n\n'.join(sections) + '\n\n<!-- /enrichment:memory -->')
        at = end
    pieces.append(frozen[at:])
    body = ''.join(pieces)
    recovered = re.sub(r'\n\n<!-- enrichment:memory paragraph=\d+ -->.*?\n\n<!-- /enrichment:memory -->', '', body, flags=re.S)
    if recovered.encode() != frozen.encode():
        raise ValueError('Assembly changed the frozen prose')
    if body.count('<a id="memory-') != count:
        raise ValueError('Assembly dropped or repeated a prose block')
    intro = ('> **Kaynak notları hakkında:** Aşağıdaki aile notları, öğrenilmiş bilgiden hatırlanan literatür görüşlerini tanıtır. '
             'Kaynaklar bu çalışmada taranmamış ve atıflar doğrulanmamıştır; bir görüşün hatırlanmaması tarihsel olarak bulunmadığı anlamına gelmez.\n\n')
    target = folder / '1_6.enriched.tr.md'
    target.write_bytes((intro + body).encode())
    print(f'{lane}: {len(families)} families, {count} blocks, frozen bytes preserved; {target}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('lane', choices=LANES)
    assemble(parser.parse_args().lane)
