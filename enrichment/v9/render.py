#!/usr/bin/env python3
"""Enrichment v9 P4: render one ayah page with its blocks. Launches no model.

The frozen page is copied unchanged; after each paragraph come its tradition blocks (focus, cited, agreement, in
writer order) and then its meal blocks; the closing group follows the last paragraph. Every block is wrapped in
markers, and the strip check removes them and requires the frozen page back byte for byte. The verse maps the
blocks cite are copied next to the page so the links work.

  render.py WRITE_RUN [--meal MEAL_RUN]     writes enrichment/v9/work/WRITE_RUN/render/<page>.enriched.md
"""
import argparse
import json
import re
import shutil
import sys
from pathlib import Path

V9 = Path(__file__).resolve().parent
sys.path.insert(0, str(V9))
import writer  # noqa: E402  (v7 page numbering, through writer.write7)
import q as Q  # noqa: E402

KIND = {'focus': 'Gelenek', 'cited': 'Gelenek · atıf', 'agreement': 'Gelenek · mutabakat', 'closing': 'Gelenek · kapanış',
        'meal': 'Mealler'}
OPEN, CLOSE = '<!-- v9:enrich', '<!-- /v9:enrich -->'
STRIP = re.compile(r'\n\n<!-- v9:enrich [^>]*-->.*?<!-- /v9:enrich -->', re.S)


def block_md(b, kind):
    links = []
    for x in b.get('questions') or []:
        links.append(f"[{x}](maps/{x.split('/')[0].replace(':', '-')}.md)")
    meta = []
    if links:
        meta.append('harita: ' + ', '.join(links))
    if b.get('notes'):
        meta.append(f"{len(b['notes'])} not")
    if b.get('meals'):
        meta.append(f"{len(b['meals'])} meal")
    text = b['text'].strip().replace('\n', '\n> ')
    return (f"\n\n{OPEN} {b.get('id', kind)} {kind} -->\n> **{KIND[kind]} · {b['topic']}**\n>\n> {text}\n>\n"
            f"> <sub>{' · '.join(meta)}</sub>\n{CLOSE}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('run')
    ap.add_argument('--meal')
    a = ap.parse_args()
    d = writer.wdir(a.run)
    man = json.loads((d / 'manifest.json').read_text())
    blocks = [json.loads(l) for l in (d / 'out' / man['tag'] / 'blocks.jsonl').read_text().splitlines() if l.strip()]
    meals = []
    if a.meal:
        md = V9 / 'work' / a.meal / 'meal'
        mm = json.loads((md / 'manifest.json').read_text())
        for i, l in enumerate((md / 'out' / mm['tag'] / 'blocks.jsonl').read_text().splitlines(), 1):
            if l.strip():
                meals.append({**json.loads(l), 'id': f'm{i:02d}'})
    text, paras, _, _ = writer.write7.page(man['page'], man['ayah'])
    last = max(paras)
    after = {p: [] for p in paras}
    for b in blocks:
        p = last if b['kind'] == 'closing' else min(b['p'])
        after[p].append(block_md(b, b['kind']))
    for b in meals:
        after[b['p']].append(block_md(b, 'meal'))
    out = text
    for p in sorted(paras, reverse=True):          # insert from the end so earlier offsets stay valid
        hi = paras[p][1]
        while hi > 0 and out[hi - 1] == '\n':
            hi -= 1
        out = out[:hi] + ''.join(after[p]) + out[hi:]
    if STRIP.sub('', out) != text:
        raise SystemExit('strip check failed: removing the blocks does not give the frozen page back')
    r = d.parent / 'render'
    (r / 'maps').mkdir(parents=True, exist_ok=True)
    cited = {x.split('/')[0] for b in blocks + meals for x in (b.get('questions') or []) + (b.get('positions') or [])}
    for v in sorted(cited):
        loc = Q.located(v)
        if loc:
            shutil.copy(loc[0].with_suffix('.md'), r / 'maps' / f"{v.replace(':', '-')}.md")
    f = r / f"{Path(man['page']).stem}.enriched.md"
    f.write_text(out)
    n = len(blocks) + len(meals)
    print(f'{f.relative_to(writer.ROOT)}: {n} blocks ({len(meals)} meal), {len(cited)} verse maps, strip check OK')


if __name__ == '__main__':
    main()
