#!/usr/bin/env python3
"""Save native per-agent usage, including request-specific long-context pricing."""
import csv
import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'enrichment/v3'))
from memory_benchmark import collect

WORK = ROOT / 'enrichment/v4/work/1_6/corpus-sol-max-20261006'
LANES = {'sol-max': WORK, 'sol-high': WORK.with_name('corpus-sol-high-20261006')}
OUTPUT = ROOT / 'enrichment/v4/work/1_6/benchmark-20261006'
SESSIONS = Path('/Users/ahmetrasit/.codex/sessions/2026/10/06')
KEYS = ('input_tokens', 'cached_input_tokens', 'cache_write_input_tokens', 'output_tokens', 'reasoning_output_tokens')


def request_costs(file):
    previous = {k: 0 for k in KEYS}
    cost = 0.0
    long_requests = 0
    updates = 0
    with file.open() as handle:
        for line in handle:
            row = json.loads(line)
            payload = row.get('payload', {})
            if row.get('type') != 'event_msg' or payload.get('type') != 'token_count' or not payload.get('info'):
                continue
            info = payload['info']
            current = info['total_token_usage']
            delta = {k: current.get(k, 0) - previous[k] for k in KEYS}
            if not any(delta.values()):
                continue
            if any(v < 0 for v in delta.values()):
                raise ValueError('Native cumulative counter decreased; inspect before costing')
            last = info.get('last_token_usage', {})
            long_context = last.get('input_tokens', 0) > 272000
            rate = 4 if long_context else 2
            output_rate = 15 if long_context else 10
            uncached = max(0, delta['input_tokens'] - delta['cached_input_tokens'] - delta['cache_write_input_tokens'])
            cost += (uncached * rate + delta['cached_input_tokens'] * rate * .1
                     + delta['cache_write_input_tokens'] * rate * 1.25 + delta['output_tokens'] * output_rate) / 1e6
            previous = {k: current.get(k, 0) for k in KEYS}
            updates += 1
            long_requests += long_context
    return round(cost, 6), long_requests, updates


def main():
    global WORK, LANES, OUTPUT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--unit', choices=('1_6', '87_6'), default='1_6')
    args = parser.parse_args()
    unit = args.unit
    WORK = ROOT / f'enrichment/v4/work/{unit}/corpus-sol-max-20261006'
    LANES = {'sol-max': WORK}
    if unit == '1_6':
        LANES['sol-high'] = WORK.with_name('corpus-sol-high-20261006')
    OUTPUT = ROOT / f'enrichment/v4/work/{unit}/benchmark-20261006'
    prefix = '/root/corpus19_' if unit == '1_6' else '/root/corpus87_'
    expected_agents = len(LANES) * 19
    records = collect(SESSIONS, prefix=prefix, lanes=LANES)
    files = {}
    for file in SESSIONS.glob('*.jsonl'):
        with file.open() as handle:
            meta = json.loads(handle.readline()).get('payload', {})
            files[meta.get('id')] = file
    total = defaultdict(int)
    lane_totals = defaultdict(lambda: defaultdict(int))
    for record in records:
        ledger_path = LANES[record['lane']] / record['family'] / 'ledger.jsonl'
        ledger = [json.loads(line) for line in ledger_path.read_text().splitlines() if line.strip()] if ledger_path.is_file() else []
        record['no_match_paragraphs'] = sum(row.get('status') == 'no_match' for row in ledger)
        cost, long_requests, updates = request_costs(files[record['session_id']])
        record['standard_api_equivalent_usd'] = cost
        record['long_context_usage_updates'] = long_requests
        record['costed_usage_updates'] = updates
        for dest in (total, lane_totals[record['lane']]):
            for key in ('input_tokens', 'cached_input_tokens', 'cache_write_input_tokens', 'uncached_input_tokens',
                        'output_tokens', 'reasoning_output_tokens', 'visible_output_tokens', 'total_tokens', 'blocks', 'prose_words', 'no_match_paragraphs'):
                dest[key] += record.get(key) or 0
            dest['agents'] += 1
            dest['completed_agents'] += record['status'] == 'completed'
            dest['standard_api_equivalent_usd'] += cost
            dest['long_context_usage_updates'] += long_requests
    report = {'updated_at': datetime.now(timezone.utc).isoformat(), 'unit': unit, 'expected_agents': expected_agents,
              'runs': {lane: json.loads((folder / 'run.json').read_text()) for lane, folder in LANES.items()},
              'scope': 'native fresh-context agent usage; parent preparation and review excluded',
              'cost_basis': 'GPT-6 Sol Standard API equivalent per M: short input $2, cached $0.20, cache write $2.50, output $10; requests above 272K input $4/$0.40/$5/$15. Sum native cumulative deltas, apply each update last-request context tier. Reasoning included in output. Not an account billing statement.',
              'pricing_source': 'https://developers.openai.com/api/docs/models/gpt-6-sol', 'totals': dict(total),
              'lane_totals': {k: dict(v) for k, v in lane_totals.items()}, 'agents': records}
    OUTPUT.mkdir(exist_ok=True)
    (OUTPUT / 'usage.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    if records:
        with (OUTPUT / 'usage.csv').open('w', newline='') as handle:
            writer = csv.DictWriter(handle, fieldnames=list(records[0]), lineterminator='\n')
            writer.writeheader(); writer.writerows(records)
    lines = [f'# {unit.replace("_", ":")} corpus-only Sol benchmark', '',
             'Native per-agent counts; parent preparation and review excluded. Input includes cache reads; output includes reasoning. Figures are API-equivalent estimates, not account billing.', '',
             f"Completed: {total['completed_agents']}/{expected_agents}. Saved agent cost: ${total['standard_api_equivalent_usd']:.6f}.", '',
             '| Lane | Family | Status | Input | Cached input | Output | Reasoning | USD |', '|---|---|---|---:|---:|---:|---:|---:|']
    for r in records:
        lines.append(f"| {r['lane']} | {r['family']} | {r['status']} | {r['input_tokens'] or 0:,} | {r['cached_input_tokens'] or 0:,} | {r['output_tokens'] or 0:,} | {r['reasoning_output_tokens'] or 0:,} | ${r['standard_api_equivalent_usd']:.6f} |")
    lines += ['', 'Full native figures: [usage.csv](usage.csv), [usage.json](usage.json).', '',
              'Costing uses [official GPT-6 Sol pricing](https://developers.openai.com/api/docs/models/gpt-6-sol), including long-context premiums per native usage update when applicable.', '',
              'Comparisons with the Astra memory mix change both model and evidence access. Source availability, material inspected and unresolved coverage must accompany the final cost comparison.', '']
    reviews = ('PAIRWISE_COMPARISON.md', 'MODERN_COHERENCE_COMPARISON.md') if unit == '1_6' else ('COMPARISON.md',)
    for filename in (*reviews, 'AGENT_COSTS.md', 'PARENT_ANCHOR_REVIEW.json'):
        if (OUTPUT / filename).is_file():
            lines.append(f'[{filename}]({filename})')
    lines.append('')
    (OUTPUT / 'README.md').write_text('\n'.join(lines))
    print(json.dumps(dict(total)))


if __name__ == '__main__':
    main()
