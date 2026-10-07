#!/usr/bin/env python3
"""Validate v5 agent outputs and assemble pages. Never edits an agent's files.

  check.py extract DIR            every chunk: full coverage, quotes verbatim in their segment
  check.py write DIR LANE         blocks/ledger links, anchors present, sources match evidence
  check.py assemble RUN --lane L  attach write-L blocks of every family to the frozen page

A failure prints every problem and exits non-zero; CHECK files record the result.
"""
import argparse
import html
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

from common import FAMILIES, ROOT, body, compact, connect, contains, dump, page, rows, usable

KINDS = {'position', 'disagreement', 'preference', 'report', 'grading', 'translation', 'witness', 'context'}


def resolve(path):
    p = Path(path)
    return p if p.is_absolute() else ROOT / p


def segment_text(con, loc, family):
    row = con.execute('SELECT seg,src,head,text,extra FROM seg WHERE seg=?', (loc,)).fetchone()
    return (row[1], (row[2] or '') + '\n' + body(row, family)) if row else (None, None)


def check_extract(d, only=None, record=True):
    meta = json.loads((d / 'family.json').read_text())
    manifest = json.loads((d / 'packet/manifest.json').read_text())
    paragraphs = set(page(meta['unit'])[1])
    problems, summary = [], {}
    with connect() as con:
        for chunk in manifest['chunks']:
            if only is not None and chunk['n'] != only:
                continue
            c = f"c{chunk['n']:02d}"
            folder = d / 'extract' / c
            if not (folder / 'coverage.jsonl').exists() or not (folder / 'extracts.jsonl').exists():
                problems.append(f'{c}: outputs missing')
                continue
            expected = chunk['segments']
            coverage = rows(folder / 'coverage.jsonl')
            seen = [r['loc'] for r in coverage]
            if sorted(seen) != sorted(expected):
                missing, extra = set(expected) - set(seen), set(seen) - set(expected)
                dup = len(seen) - len(set(seen))
                problems.append(f'{c}: coverage mismatch (missing {len(missing)}, foreign {len(extra)}, repeated {dup})'
                                + (f' e.g. missing {sorted(missing)[:3]}' if missing else ''))
            status = defaultdict(int)
            for r in coverage:
                if r.get('status') not in ('extracted', 'not_relevant', 'unreadable'):
                    problems.append(f"{c}: bad coverage status {r.get('status')} at {r.get('loc')}")
                status[r.get('status')] += 1
            extracted_locs = set()
            items = rows(folder / 'extracts.jsonl')
            for i, x in enumerate(items, 1):
                where = f"{c} extract {i} {x.get('loc')}"
                if x.get('loc') not in expected:
                    problems.append(f'{where}: locator not in this chunk')
                    continue
                if not x.get('p') or not set(x['p']) <= paragraphs:
                    problems.append(f'{where}: invalid paragraphs {x.get("p")}')
                if x.get('kind') not in KINDS:
                    problems.append(f'{where}: invalid kind {x.get("kind")}')
                _, text = segment_text(con, x['loc'], meta['family'])
                if not contains(text, x.get('quote', '')):
                    problems.append(f'{where}: quote not found verbatim')
                extracted_locs.add(x['loc'])
            marked = {r['loc'] for r in coverage if r.get('status') == 'extracted'}
            if marked != extracted_locs:
                problems.append(f'{c}: coverage "extracted" disagrees with extracts for '
                                f'{len(marked ^ extracted_locs)} segments')
            summary[c] = {'segments': len(expected), 'extracts': len(items), 'coverage': dict(status)}
    if record:
        dump(d / 'extract/CHECK.json', {'ok': not problems, 'chunks': summary, 'problems': problems})
    return problems, summary


def check_write(d, lane):
    meta = json.loads((d / 'family.json').read_text())
    family, unit = meta['family'], meta['unit']
    folder = d / f'write-{lane}'
    expected = set(page(unit)[1])
    config = json.loads(((d / 'packet/sources.json') if (d / 'packet/sources.json').exists() else d / 'sources.json').read_text())
    allowed = set(usable(config))
    packet_locs = {s['loc'] for s in rows(d / 'packet/segments.jsonl')} if (d / 'packet/segments.jsonl').exists() else None
    problems = []
    blocks, ledger = rows(folder / 'blocks.jsonl'), rows(folder / 'ledger.jsonl')
    by_id = {b['id']: b for b in blocks}
    if len(by_id) != len(blocks):
        problems.append('repeated block ids')
    if sorted(r['p'] for r in ledger) != sorted(expected):
        problems.append('ledger must hold exactly one row per paragraph')
    entries = {r['p']: r for r in ledger}
    anchors = 0
    with connect() as con:
        for b in blocks:
            if not re.fullmatch(r'[A-Za-z0-9_-]+', b['id']) or not b.get('text', '').strip():
                problems.append(f"{b['id']}: bad id or empty text")
            if not b.get('p') or not set(b['p']) <= expected:
                problems.append(f"{b['id']}: bad paragraphs")
            cited = set()
            for e in b.get('evidence') or []:
                anchors += 1
                src, text = segment_text(con, e['loc'], family)
                if src not in allowed:
                    problems.append(f"{b['id']}: {e['loc']} outside the roster")
                    continue
                if packet_locs is not None and e['loc'] not in packet_locs and not meta.get('search'):
                    problems.append(f"{b['id']}: {e['loc']} outside the packet")
                if not contains(text, e.get('anchor', '')):
                    problems.append(f"{b['id']}: anchor not found in {e['loc']}: «{e.get('anchor', '')[:60]}»")
                cited.add(src)
            if not b.get('evidence'):
                problems.append(f"{b['id']}: no evidence")
            if set(b.get('sources', [])) != cited:
                problems.append(f"{b['id']}: sources differ from evidence sources")
            for p in b.get('p', []):
                if p in entries and b['id'] not in entries[p].get('blocks', []):
                    problems.append(f"{b['id']}: ledger row {p} lacks it")
    for r in ledger:
        if r.get('status') not in ('written', 'no_match') or bool(r.get('blocks')) != (r.get('status') == 'written'):
            problems.append(f"ledger {r.get('p')}: status/blocks mismatch")
        for i in r.get('blocks', []):
            if i not in by_id or r['p'] not in by_id[i]['p']:
                problems.append(f"ledger {r['p']}: broken link {i}")
    result = {'ok': not problems, 'blocks': len(blocks), 'anchors': anchors,
              'written': sum(r.get('status') == 'written' for r in ledger), 'problems': problems}
    dump(folder / 'CHECK.json', result)
    return problems, result


def assemble(run, lane):
    unit = run.parent.name
    frozen, paragraphs = page(unit)
    primary, links, count, families = defaultdict(list), defaultdict(list), 0, []
    for family in FAMILIES:
        folder = run / family / f'write-{lane}'
        if not (folder / 'CHECK.json').exists():
            continue
        if not json.loads((folder / 'CHECK.json').read_text())['ok']:
            raise SystemExit(f'{family}: write-{lane} has not passed check.py write')
        families.append(family)
        for b in rows(folder / 'blocks.jsonl'):
            ps = sorted(set(b['p']))
            primary[ps[0], family].append(b)
            for p in ps[1:]:
                links[p, family].append((b['id'], ps[0]))
            count += 1
    pieces, at = [], 0
    for p, (_, end) in paragraphs.items():
        sections = []
        for family in families:
            blocks, related = primary[p, family], links[p, family]
            if not blocks and not related:
                continue
            sections.append('### ' + FAMILIES[family])
            for b in blocks:
                refs = '; '.join(e['loc'] + ' — «' + compact(e['anchor']) + '»' for e in b['evidence'])
                sections.append(f'<a id="v5-{html.escape(b["id"], quote=True)}"></a>\n\n{b["text"]}\n\nKaynak konumları: {refs}.')
            if related:
                sections.append('Bu paragrafla da ilgili kaynak görüşü: ' +
                                ', '.join(f'[{o}. paragraf](#v5-{i})' for i, o in related) + '.')
        pieces.append(frozen[at:end])
        if sections:
            pieces.append(f'\n\n<!-- enrichment:v5 paragraph={p} -->\n\n' + '\n\n'.join(sections) + '\n\n<!-- /enrichment:v5 -->')
        at = end
    pieces.append(frozen[at:])
    rendered = ''.join(pieces)
    recovered = re.sub(r'\n\n<!-- enrichment:v5 paragraph=\d+ -->.*?\n\n<!-- /enrichment:v5 -->', '', rendered, flags=re.S)
    if recovered.encode() != frozen.encode() or rendered.count('<a id="v5-') != count:
        raise SystemExit('Assembly changed the frozen prose or lost a block')
    target = run / f'{unit}.{lane}.enriched.tr.md'
    target.write_text(rendered)
    print(f'{unit} {lane}: {len(families)} families, {count} blocks; frozen bytes preserved -> {target}')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('extract'); p.add_argument('dir')
    p = sub.add_parser('write'); p.add_argument('dir'); p.add_argument('lane')
    p = sub.add_parser('assemble'); p.add_argument('run'); p.add_argument('--lane', required=True)
    a = parser.parse_args()
    if a.cmd == 'assemble':
        return assemble(resolve(a.run), a.lane)
    problems, summary = check_extract(resolve(a.dir)) if a.cmd == 'extract' else check_write(resolve(a.dir), a.lane)
    for line in problems:
        print('PROBLEM', line)
    print(json.dumps(summary, ensure_ascii=False))
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
