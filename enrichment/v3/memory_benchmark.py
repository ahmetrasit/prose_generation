#!/usr/bin/env python3
"""Save native per-agent token usage for the 1:6 model/effort benchmark."""
import argparse
import csv
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / 'enrichment/v3/work/1_6'
OUTPUT = WORK / 'family-memory-benchmark-20261006'
LANES = {
    'sol-high': WORK / 'family-memory-baseline-20261006',
    'luna6-max': WORK / 'family-memory-luna6-max-20261006',
    'astra-max': WORK / 'family-memory-astra-max-20261006',
    'astra-high': WORK / 'family-memory-astra-high-20261006',
    'sol-max': WORK / 'family-memory-sol-max-20261006',
}
METRICS = ('input_tokens', 'cached_input_tokens', 'cache_write_input_tokens',
           'uncached_input_tokens', 'output_tokens', 'reasoning_output_tokens',
           'visible_output_tokens', 'total_tokens')
MATCHED_FAMILIES = {'bayani', 'classical-coherence', 'meal', 'hadith'}


def read_jsonl(path):
    if not path.is_file():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def collect(sessions, prefix='/root/memory19_', lanes=None):
    lanes = LANES if lanes is None else lanes
    records = []
    for file in sessions.glob('*.jsonl'):
        with file.open() as handle:
            try:
                metadata = json.loads(handle.readline()).get('payload', {})
            except (ValueError, OSError):
                continue
            agent = metadata.get('agent_path', '')
            if not agent.startswith(prefix):
                continue
            suffix = agent.split(prefix, 1)[1]
            lane = ('luna6-max' if suffix.startswith('luna_') else
                    'astra-high' if suffix.startswith('astrahigh_') else
                    'astra-max' if suffix.startswith('astra_') else
                    'sol-high' if suffix.startswith('solhigh_') else
                    'sol-max' if suffix.startswith('solmax_') else 'sol-high')
            family = (suffix[5:] if suffix.startswith('luna_') else
                      suffix[10:] if suffix.startswith('astrahigh_') else
                      suffix[6:] if suffix.startswith('astra_') else
                      suffix[8:] if suffix.startswith('solhigh_') else
                      suffix[7:] if suffix.startswith('solmax_') else suffix).replace('_', '-')
            model = effort = None
            usage = None
            completed = False
            last_timestamp = metadata.get('timestamp')
            calls = set()
            tool_calls = 0
            policy_flags = []
            max_context_input = 0
            for line in handle:
                try:
                    row = json.loads(line)
                except ValueError:
                    continue
                payload = row.get('payload', {})
                last_timestamp = row.get('timestamp', last_timestamp)
                if row.get('type') == 'turn_context':
                    model = payload.get('model', model)
                    effort = payload.get('effort', payload.get('reasoning_effort', effort))
                if row.get('type') == 'response_item' and payload.get('role') == 'user' and family is None:
                    for item in payload.get('content', []):
                        match = re.search(r'ENRICHMENT_MEMORY_1_6 family=([^\s]+)', item.get('text', ''))
                        if match:
                            family = match[1]
                if row.get('type') == 'response_item' and payload.get('role') == 'assistant' and payload.get('channel') == 'final':
                    completed = True
                if row.get('type') == 'response_item' and payload.get('type') in ('custom_tool_call', 'function_call'):
                    tool_calls += 1
                    tool_input = str(payload.get('input', payload.get('arguments', '')))
                    if re.search(r'tools\.(?:web__run|[^\s(]*search[^\s(]*)\s*\(', tool_input):
                        policy_flags.append('search-tool reference in executed tool input')
                    if re.search(r'(?:cmd\s*:\s*[\"\x27]|\n|&&|;)\s*(?:rg|grep|find)\b|\.rglob\(|os\.walk\(', tool_input):
                        policy_flags.append('repository-search pattern in executed tool input')
                    for other_lane, other_folder in lanes.items():
                        if other_lane != lane and other_folder.name in tool_input:
                            policy_flags.append('other-lane path in executed tool input: ' + other_lane)
                if row.get('type') == 'event_msg':
                    if payload.get('type') in ('task_complete', 'task_completed'):
                        completed = True
                    if payload.get('type') == 'token_count' and payload.get('info'):
                        usage = payload['info']['total_token_usage']
                        max_context_input = max(max_context_input, payload['info'].get('last_token_usage', {}).get('input_tokens', 0))
                        calls.add(tuple(sorted(usage.items())))
        if family is None:
            continue
        record = {
            'lane': lane, 'family': family, 'agent': agent,
            'session_id': metadata.get('id'), 'model': model, 'effort': effort,
            'status': 'completed' if completed else 'running',
            'started_at': metadata.get('timestamp'), 'last_event_at': last_timestamp,
            'native_usage_updates': len(calls), 'usage_available': usage is not None,
            'tool_calls': tool_calls, 'policy_flags': list(dict.fromkeys(policy_flags)),
            'max_context_input_tokens': max_context_input,
        }
        for key in METRICS:
            record[key] = usage.get(key, 0) if usage else None
        if usage:
            record['uncached_input_tokens'] = max(0, record['input_tokens'] - record['cached_input_tokens'] - record['cache_write_input_tokens'])
            record['visible_output_tokens'] = record['output_tokens'] - record['reasoning_output_tokens']
            rate = {'sol-high': 2.0, 'sol-max': 2.0, 'luna6-max': 0.1, 'astra-max': 10.0, 'astra-high': 10.0}[lane]
            record['standard_api_equivalent_usd'] = round((
                record['uncached_input_tokens'] * rate
                + record['cached_input_tokens'] * rate * 0.1
                + record['cache_write_input_tokens'] * rate * 1.25
                + record['output_tokens'] * rate * 5
            ) / 1_000_000, 6) if max_context_input <= 272000 else None
        else:
            record['standard_api_equivalent_usd'] = None
        folder = lanes[lane] / family
        blocks = read_jsonl(folder / 'blocks.jsonl')
        ledger = read_jsonl(folder / 'ledger.jsonl')
        record['blocks'] = len(blocks)
        record['prose_words'] = sum(len(block.get('text', '').split()) for block in blocks)
        record['ledger_rows'] = len(ledger)
        record['no_recall_paragraphs'] = sum(row.get('status') == 'no_recall' for row in ledger)
        records.append(record)
    return sorted(records, key=lambda row: (row['lane'], row['family'], row['started_at']))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sessions', type=Path, default=Path('/Users/ahmetrasit/.codex/sessions/2026/10/06'))
    args = parser.parse_args()
    records = collect(args.sessions)
    totals = defaultdict(lambda: defaultdict(int))
    matched_totals = defaultdict(lambda: defaultdict(int))
    for record in records:
        destinations = [totals[record['lane']]]
        if record['family'] in MATCHED_FAMILIES:
            destinations.append(matched_totals[record['lane']])
        for total in destinations:
            total['agents'] += 1
            total['completed_agents'] += record['status'] == 'completed'
            total['agents_with_usage'] += record['usage_available']
            for key in (*METRICS, 'blocks', 'prose_words'):
                total[key] += record.get(key) or 0
            total['standard_api_equivalent_usd'] += record['standard_api_equivalent_usd'] or 0
    OUTPUT.mkdir(exist_ok=True)
    report = {
        'updated_at': datetime.now(timezone.utc).isoformat(),
        'scope': '19 independent family tasks each for Sol high/Luna max/Astra max/Astra high, four for Sol max; native cumulative usage only, parent orchestration excluded',
        'accounting': 'Input includes cached input; output includes reasoning. Repeated contexts count at each call. Fresh agent contexts have no inherited parent usage.',
        'cost_basis': 'Standard API-equivalent rates per million: GPT-6 Sol input $2, cached $0.20, cache write $2.50, output $10; GPT-6 Luna $0.10/$0.01/$0.125/$0.50; GPT-6 Astra $10/$1/$12.50/$50. https://developers.openai.com/api/docs/pricing . Requests above 272K are not costed by this estimator. This is not an account billing report.',
        'expected_agents_per_lane': {'sol-high': 19, 'luna6-max': 19, 'astra-max': 19, 'astra-high': 19, 'sol-max': 4},
        'totals': dict(totals), 'matched_families': sorted(MATCHED_FAMILIES),
        'matched_four_family_totals': dict(matched_totals), 'agents': records,
    }
    (OUTPUT / 'usage.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    if records:
        with (OUTPUT / 'usage.csv').open('w', newline='') as handle:
            writer = csv.DictWriter(handle, fieldnames=list(records[0]), lineterminator='\n')
            writer.writeheader()
            writer.writerows(records)
    lines = [
        '# 1:6 memory-family token benchmark', '',
        'Native cumulative per-agent usage; parent orchestration and assembly are excluded. Input includes cached reads; output includes reasoning. Counts are not a measure of scholarly accuracy.', '',
        '| Lane | Completed | Input | Cached input | Uncached input | Output | Reasoning | Blocks | API-equivalent USD |',
        '|---|---:|---:|---:|---:|---:|---:|---:|---:|',
    ]
    for lane, total in sorted(totals.items()):
        lines.append(f"| {lane} | {total['completed_agents']}/{total['agents']} | {total['input_tokens']:,} | {total['cached_input_tokens']:,} | {total['uncached_input_tokens']:,} | {total['output_tokens']:,} | {total['reasoning_output_tokens']:,} | {total['blocks']} | ${total['standard_api_equivalent_usd']:.4f} |")
    lines += ['', 'Full per-agent figures are in [usage.csv](usage.csv) and [usage.json](usage.json).', '',
              'Cost equivalents use [official Standard API pricing](https://developers.openai.com/api/docs/pricing), with no cache writes recorded in these runs. Output includes reasoning. These are not account billing figures.', '',
              'The Sol spot review is in [SOL_SPOT_REVIEW.md](SOL_SPOT_REVIEW.md). No baseline blocks were revised following that review.', '',
              'The matched Luna/Sol spot comparison is in [LUNA_SOL_SPOT_COMPARISON.md](LUNA_SOL_SPOT_COMPARISON.md).', '',
              'The four-family Sol effort comparison is in [SOL_EFFORT_COMPARISON.md](SOL_EFFORT_COMPARISON.md).', '',
              'The Astra spot comparison is in [ASTRA_SPOT_COMPARISON.md](ASTRA_SPOT_COMPARISON.md).', '',
              'The Astra high/max comparison is in [ASTRA_EFFORT_COMPARISON.md](ASTRA_EFFORT_COMPARISON.md), with the detailed paragraph review in [ASTRA_DEEP_COMPARISON.md](ASTRA_DEEP_COMPARISON.md). These reviews concern the original four matched families.', '',
              'The completed 19-family review and effort recommendations are in [ASTRA_19_FAMILY_COMPARISON.md](ASTRA_19_FAMILY_COMPARISON.md).', '',
              'S87 frozen paragraph counts are in [S87_PARAGRAPH_COUNTS.md](S87_PARAGRAPH_COUNTS.md).', '',
              'The first three Sol tasks needed a path clarification; their extra calls remain included. Agents received the complete page in four separate deliveries. Common instructions and runtime context repeat across calls. Agent count or block count alone does not establish quality or efficiency.', '']
    lines += ['## Matched four-family comparison', '',
              'Bayani, classical coherence, meal, and hadith; one run per family per lane. Sol high versus Sol max and Astra high versus Astra max change reasoning effort within each model. Other lane comparisons also change the model. Fresh contexts received byte-identical prose and source rosters; outputs were kept separate.', '',
              '| Lane | Completed | Input | Output | Reasoning | Visible output | Blocks | Prose words | API-equivalent USD |',
              '|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    for lane, total in sorted(matched_totals.items()):
        lines.append(f"| {lane} | {total['completed_agents']}/{total['agents']} | {total['input_tokens']:,} | {total['output_tokens']:,} | {total['reasoning_output_tokens']:,} | {total['visible_output_tokens']:,} | {total['blocks']} | {total['prose_words']:,} | ${total['standard_api_equivalent_usd']:.4f} |")
    lines.append('')
    for lane in sorted(totals):
        lines += ['## ' + lane, '', '| Family | Input | Cached input | Output | Reasoning | Tool calls | USD equivalent |',
                  '|---|---:|---:|---:|---:|---:|---:|']
        for record in records:
            if record['lane'] != lane:
                continue
            cost = record['standard_api_equivalent_usd']
            cost_text = f'${cost:.6f}' if cost is not None else 'Pending'
            def number(key):
                return f"{record[key]:,}" if record[key] is not None else 'Pending'
            lines.append(f"| {record['family']} | {number('input_tokens')} | {number('cached_input_tokens')} | {number('output_tokens')} | {number('reasoning_output_tokens')} | {record['tool_calls']} | {cost_text} |")
        lines.append('')
    flags = [record for record in records if record['policy_flags']]
    lines += ['Executed tool input was scanned for search commands and other-lane paths. ' + (f'{len(flags)} agent(s) have flags in usage.json requiring inspection.' if flags else 'No such patterns were flagged. This scan is observational, not a filesystem access control.'), '',
              f"Updated: {report['updated_at']}", '']
    (OUTPUT / 'README.md').write_text('\n'.join(lines))
    print(json.dumps({'updated_at': report['updated_at'], 'totals': report['totals'], 'output': str(OUTPUT)}, indent=2))


if __name__ == '__main__':
    main()
