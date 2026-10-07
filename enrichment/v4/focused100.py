#!/usr/bin/env python3
"""Prepare and account for the authorized four-family 100:1 comparison."""
import argparse
import csv
import json
import re
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'enrichment/v3'))
import pilot
from memory_benchmark import collect
from benchmark import request_costs
from corpus_read import connect, contains_anchor, eligible

STAMP = '20261007'
FAMILIES = ('rivayet', 'historical', 'poetry', 'meal')
OUTPUT = ROOT / f'enrichment/v4/work/100_1/benchmark-{STAMP}'
LANES = {
    **{f'sol-{effort}': ROOT / f'enrichment/v4/work/100_1/corpus-sol-{effort}-{STAMP}' for effort in ('high', 'max')},
    **{f'astra-{effort}': ROOT / f'enrichment/v3/work/100_1/family-memory-astra-{effort}-{STAMP}' for effort in ('high', 'max')},
}
INPUT = ROOT / '_commentary/v16/out/100_1/DM.r13.images.r13.map3.nohft.tool.tool.tool/augment.augment2/100_1.reading.tr.md'
PREFIX = '/root/pilot100_'
PURPOSES = {
    'rivayet': 'Early and transmitted tafsir: competing identifications and lexical explanations, who transmits each position, contextual arguments and later reception. Preserve independent voices and distinguish a report from its grading. Address all substantial paragraph findings, not only 100:1.',
    'historical': 'History and revelation context: competing occasion narratives, dating and contextual arguments; persons, animals, raids, pilgrimage, routes and institutions where relevant. Distinguish a historical explanation from an occasion report and uncertain chronology. Address all substantial paragraph findings.',
    'poetry': 'Poetry witnesses: direct lexical attestations for the supplied words and concrete images, with poem or collection attribution and commentator gloss where available. Distinguish direct word evidence from thematic parallels; do not substitute a famous general horse poem for an actual lexical witness. Address all substantial paragraph findings.',
    'meal': 'Turkish translations: wording that narrows or shifts meaning, interpretive additions, omitted distinctions and consistent translation errors supported by repeated examples. Preserve alternatives and edition identities; a defensible tafsir choice is not automatically a translation error. Compare secondary verses where relevant; English originals and Turkish versions are both in scope when supplied.',
}


def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def prepare():
    if any(folder.exists() for folder in LANES.values()):
        raise ValueError('Run directories already exist; preparation never overwrites a run')
    pilot.BASE = INPUT
    frozen, paragraphs = pilot.prose()
    if len(paragraphs) != 22:
        raise ValueError('Unexpected input paragraph count')
    for lane, folder in LANES.items():
        folder.mkdir(parents=True)
        (folder / 'frozen.reading.tr.md').write_bytes(INPUT.read_bytes())
        model, effort = lane.split('-')
        mode = 'corpus' if model == 'sol' else 'memory'
        template = ROOT / (f'enrichment/v4/work/1_6/corpus-sol-{effort}-20261006/BRIEF.md' if mode == 'corpus' else f'enrichment/v3/work/1_6/family-memory-astra-{effort}-20261006/BRIEF.md')
        brief = template.read_text().replace('1:6', '100:1').replace('nineteen', 'four').replace('of 19', 'of four').replace('augment9', 'augment2')
        brief = brief.replace('enrichment/v4/corpus_read.py --lane', f'enrichment/v4/corpus_read.py --unit 100_1 --run-date {STAMP} --lane')
        brief += '\nThis is the authorized four-family 100:1 benchmark. Keep all 22 paragraph decisions. Do not read earlier benchmark results or any other lane. The parent will evaluate distinct substantive findings, author disagreements, attribution accuracy and omissions; block length alone is not quality.\n'
        (folder / 'BRIEF.md').write_text(brief)
        for part, (lo, hi) in enumerate(((1, 5), (6, 10), (11, 16), (17, 22)), 1):
            contents = '\n\n'.join(f'[Paragraph {p}]\n{frozen[paragraphs[p][0]:paragraphs[p][1]].strip()}' for p in range(lo, hi + 1))
            (folder / f'input-{part}.txt').write_text(contents + '\n')
        dump(folder / 'run.json', {'unit': '100_1', 'model': f'gpt-6-{model}', 'effort': effort, 'evidence_mode': mode, 'service_tier': 'default', 'fast_mode': False, 'agents': 4, 'families': list(FAMILIES), 'paragraphs': 22, 'input_basis': str(INPUT.relative_to(ROOT)), 'status': 'prepared', 'corpus_keyword_search': mode == 'corpus', 'web_search': False, 'repository_search': False, 'memory_findings': mode == 'memory'})
        for family in FAMILIES:
            dest = folder / family
            dest.mkdir()
            (dest / 'source-roster.txt').write_bytes((ROOT / f'enrichment/v3/work/1_6/family-memory-astra-max-20261006/{family}/source-roster.txt').read_bytes())
            if mode == 'corpus':
                (dest / 'sources.json').write_bytes((ROOT / f'enrichment/v4/work/1_6/corpus-sol-high-20261006/{family}/sources.json').read_bytes())
            dump(dest / 'assignment.json', {'family': family, 'research_purpose': PURPOSES[family], 'outputs': ['blocks.jsonl', 'ledger.jsonl']})
    OUTPUT.mkdir(parents=True)
    dump(OUTPUT / 'run-plan.json', {'unit': '100_1', 'agents': 16, 'families': list(FAMILIES), 'lanes': {k: str(v.relative_to(ROOT)) for k, v in LANES.items()}, 'native_agent_prefix': PREFIX, 'input_words': len(frozen.split()), 'paragraphs': len(paragraphs), 'reference_cost_usd': 23.016077, 'reference_cost_scope': 'Observed same four families and four configurations on 1:6; not a budget cap or forecast. Parent excluded.', 'review': 'Read all outputs. Compare source-specific findings, disagreements, attribution errors and important omissions. Check memory claims against available corpus sources; unavailable claims remain unverified, not false. Compare efforts within each mode; between models also changes evidence mode.'})
    print(f'Prepared 16 isolated assignments: {len(paragraphs)} paragraphs, {len(frozen.split())} words, identical frozen bytes across four lanes')


def account():
    records = []
    files = {}
    for day in ('06', '07', '08'):
        sessions = Path(f'/Users/ahmetrasit/.codex/sessions/2026/10/{day}')
        if not sessions.is_dir():
            continue
        records.extend(collect(sessions, prefix=PREFIX, lanes=LANES))
        for file in sessions.glob('*.jsonl'):
            with file.open() as handle:
                try:
                    meta = json.loads(handle.readline()).get('payload', {})
                except ValueError:
                    continue
            if meta.get('agent_path', '').startswith(PREFIX):
                files[meta['id']] = file
    records.sort(key=lambda r: (r['lane'], r['family']))
    totals = defaultdict(lambda: defaultdict(int))
    for r in records:
        if r['family'] not in FAMILIES:
            raise ValueError('Unexpected family in native sessions')
        if r['lane'].startswith('sol-'):
            r['standard_api_equivalent_usd'], r['long_context_usage_updates'], r['costed_usage_updates'] = request_costs(files[r['session_id']])
        else:
            r['long_context_usage_updates'] = 0 if r['max_context_input_tokens'] <= 272000 else None
            r['costed_usage_updates'] = r['native_usage_updates']
        ledger = LANES[r['lane']] / r['family'] / 'ledger.jsonl'
        r['no_match_paragraphs'] = sum(json.loads(line).get('status') == 'no_match' for line in ledger.read_text().splitlines() if line.strip()) if ledger.exists() else 0
        t = totals[r['lane']]
        t['agents'] += 1
        t['completed_agents'] += r['status'] == 'completed'
        for key in ('input_tokens', 'cached_input_tokens', 'uncached_input_tokens', 'output_tokens', 'reasoning_output_tokens', 'visible_output_tokens', 'blocks', 'prose_words'):
            t[key] += r.get(key) or 0
        t['standard_api_equivalent_usd'] += r['standard_api_equivalent_usd'] or 0
    report = {'updated_at': datetime.now(timezone.utc).isoformat(), 'expected_agents': 16, 'scope': 'Native fresh-context research-agent usage; parent preparation, review and assembly excluded. Saved benchmark Standard API-equivalent rates, not billing.', 'pricing_sources': ['https://developers.openai.com/api/docs/models/gpt-6-sol', 'https://developers.openai.com/api/docs/models/gpt-6-astra'], 'lane_totals': dict(totals), 'agents': records}
    dump(OUTPUT / 'usage.json', report)
    if records:
        with (OUTPUT / 'usage.csv').open('w', newline='') as handle:
            writer = csv.DictWriter(handle, fieldnames=list(records[0]), lineterminator='\n')
            writer.writeheader(); writer.writerows(records)
    lines = ['# 100:1 four-family benchmark usage', '', 'Native cumulative usage. Input includes cached reads; output includes reasoning. API-equivalent estimates at the saved benchmark rates; parent excluded.', '', '| Lane | Family | Status | Input | Cached input | Output | Reasoning | USD |', '|---|---|---|---:|---:|---:|---:|---:|']
    for r in records:
        cost = f"${r['standard_api_equivalent_usd']:.6f}" if r['standard_api_equivalent_usd'] is not None else 'Pending'
        lines.append(f"| {r['lane']} | {r['family']} | {r['status']} | {r['input_tokens'] or 0:,} | {r['cached_input_tokens'] or 0:,} | {r['output_tokens'] or 0:,} | {r['reasoning_output_tokens'] or 0:,} | {cost} |")
    (OUTPUT / 'AGENT_COSTS.md').write_text('\n'.join(lines) + '\n')
    print(json.dumps({'completed': sum(t['completed_agents'] for t in totals.values()), 'expected': 16, 'lane_totals': dict(totals)}))


def audit():
    """Read-only structural/source audit; preserve raw agent outputs."""
    report = {'scope': 'Structure, source IDs and exact source anchors; not an exhaustive semantic verification', 'lanes': {}, 'issues': []}
    original = INPUT.read_bytes()
    with connect() as con:
        for lane, folder in LANES.items():
            if (folder / 'frozen.reading.tr.md').read_bytes() != original:
                raise ValueError('Frozen input differs')
            counts = report['lanes'][lane] = {'blocks': 0, 'anchors': 0, 'paragraph_decisions': 0}
            for family in FAMILIES:
                blocks = [json.loads(x) for x in (folder / family / 'blocks.jsonl').read_text().splitlines() if x.strip()]
                ledger = [json.loads(x) for x in (folder / family / 'ledger.jsonl').read_text().splitlines() if x.strip()]
                if len(ledger) != 22 or {x['p'] for x in ledger} != set(range(1, 23)):
                    raise ValueError(f'{lane}/{family}: paragraph decisions incomplete')
                by_id = {x['id']: x for x in blocks}
                if len(by_id) != len(blocks):
                    raise ValueError('Repeated block IDs')
                entries = {x['p']: x for x in ledger}
                empty_status = 'no_match' if lane.startswith('sol-') else 'no_recall'
                for entry in ledger:
                    if entry['status'] not in ('written', empty_status) or bool(entry['blocks']) != (entry['status'] == 'written'):
                        raise ValueError(f'{lane}/{family}: bad status/block pairing')
                    for identifier in entry['blocks']:
                        if identifier not in by_id or entry['p'] not in by_id[identifier]['p']:
                            raise ValueError('Broken ledger link')
                config = json.loads((folder / family / 'sources.json').read_text()) if lane.startswith('sol-') else None
                for block in blocks:
                    if not block['text'].strip() or not block['p'] or not set(block['p']) <= set(entries):
                        raise ValueError('Invalid block text or paragraph set')
                    for p in block['p']:
                        if block['id'] not in entries[p]['blocks']:
                            raise ValueError('Missing ledger backlink')
                    if config:
                        if not block.get('evidence'):
                            raise ValueError('Missing evidence')
                        cited = set()
                        for pointer in block['evidence']:
                            counts['anchors'] += 1
                            row = con.execute('SELECT seg,src,head,text,extra FROM seg WHERE seg=?', (pointer['loc'],)).fetchone()
                            if not row or row[1] not in eligible(config):
                                raise ValueError('Unavailable or out-of-family source')
                            cited.add(row[1])
                            if not contains_anchor(row, config, pointer['anchor']):
                                report['issues'].append({'lane': lane, 'family': family, 'block': block['id'], **pointer})
                        if cited != set(block['sources']):
                            raise ValueError('Source IDs differ from evidence')
                counts['blocks'] += len(blocks)
                counts['paragraph_decisions'] += len(ledger)
    dump(OUTPUT / 'SOURCE_ANCHOR_AUDIT.json', report)
    print(json.dumps({'lanes': report['lanes'], 'anchor_issues': len(report['issues'])}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('prepare', 'account', 'monitor', 'audit'))
    args = parser.parse_args()
    if args.command == 'prepare':
        prepare()
    elif args.command == 'account':
        account()
    elif args.command == 'audit':
        audit()
    else:
        while True:
            try:
                account()
                report = json.loads((OUTPUT / 'usage.json').read_text())
                if len(report['agents']) == 16 and all(r['status'] == 'completed' for r in report['agents']):
                    break
            except (ValueError, OSError) as error:
                print(f'Live snapshot retry: {error}', flush=True)
            time.sleep(30)
