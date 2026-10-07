#!/usr/bin/env python3
"""Native per-agent usage and Standard API-equivalent cost for a v5 run.

Reads the Codex session files of agents whose agent_path starts with the run's prefix,
costs every usage update at its model's saved rate (Sol's long-context tier applies per
request above 272k input), and writes usage.json, usage.csv and COSTS.md next to the
run plan. Parent orchestration is not included. Not a billing statement.

  python3 -B enrichment/v5/account.py pilot-20261007
"""
import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

from common import LONG_CONTEXT, RATES, SOL_LONG, V5, dump

SESSIONS = Path.home() / '.codex/sessions'
KEYS = ('input_tokens', 'cached_input_tokens', 'cache_write_input_tokens', 'output_tokens', 'reasoning_output_tokens')


def rate(model, long_context):
    key = next((k for k in RATES if k.split('-')[-1] in (model or '')), None)
    if key is None:
        return None, False
    if long_context and key == 'gpt-6-sol':
        return SOL_LONG, False
    return RATES[key], long_context and key != 'gpt-6-sol'   # long tier unknown for others: flagged


def session(file, prefix):
    with file.open() as handle:
        try:
            meta = json.loads(handle.readline()).get('payload', {})
        except ValueError:
            return None
        agent = meta.get('agent_path', '')
        if not agent.startswith(prefix):
            return None
        rec = {'agent': agent, 'session_id': meta.get('id'), 'model': None, 'effort': None, 'completed': False,
               'tool_calls': 0, 'requests': 0, 'long_context_requests': 0, 'unpriced_long_context': 0,
               'usd': 0.0, **{k: 0 for k in KEYS}}
        previous = {k: 0 for k in KEYS}
        for line in handle:
            try:
                row = json.loads(line)
            except ValueError:
                continue
            payload = row.get('payload', {})
            kind = row.get('type')
            if kind == 'turn_context':
                rec['model'] = payload.get('model', rec['model'])
                rec['effort'] = payload.get('effort', payload.get('reasoning_effort', rec['effort']))
            elif kind == 'response_item' and payload.get('type') in ('custom_tool_call', 'function_call'):
                rec['tool_calls'] += 1
            elif kind == 'event_msg' and payload.get('type') in ('task_complete', 'task_completed'):
                rec['completed'] = True
            elif kind == 'event_msg' and payload.get('type') == 'token_count' and payload.get('info'):
                current = payload['info']['total_token_usage']
                delta = {k: current.get(k, 0) - previous[k] for k in KEYS}
                if not any(delta.values()):
                    continue
                if any(v < 0 for v in delta.values()):
                    raise ValueError(f'{file}: native counter decreased')
                long_context = payload['info'].get('last_token_usage', {}).get('input_tokens', 0) > LONG_CONTEXT
                r, unpriced = rate(rec['model'], long_context)
                if r is None:
                    raise ValueError(f'{file}: no saved rate for model {rec["model"]}')
                uncached = max(0, delta['input_tokens'] - delta['cached_input_tokens'] - delta['cache_write_input_tokens'])
                rec['usd'] += (uncached * r[0] + delta['cached_input_tokens'] * r[1]
                               + delta['cache_write_input_tokens'] * r[2] + delta['output_tokens'] * r[3]) / 1e6
                rec['requests'] += 1
                rec['long_context_requests'] += long_context
                rec['unpriced_long_context'] += unpriced
                previous = {k: current.get(k, 0) for k in KEYS}
        rec.update({k: previous[k] for k in KEYS})
        rec['usd'] = round(rec['usd'], 6)
        return rec


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('run')
    run = parser.parse_args().run
    plan = json.loads((V5 / f'work/{run}.json').read_text())
    expected = {a['agent']: a for stage in plan['stages'].values() for a in stage}
    records = [r for f in sorted(SESSIONS.glob('2026/*/*/*.jsonl')) if (r := session(f, plan['prefix']))]
    for r in records:
        r['role'] = expected.get(r['agent'], {}).get('role', 'unexpected')
    totals = defaultdict(lambda: defaultdict(float))
    for r in records:
        for key in ('usd', *KEYS):
            totals[r['role']][key] += r[key]
            totals['ALL'][key] += r[key]
    out = V5 / f'work/{run}-usage'
    dump(out / 'usage.json', {'run': run, 'scope': 'Native agent usage only; parent excluded; Standard API-equivalent rates, not billing.',
                              'expected_agents': len(expected), 'found_agents': len(records),
                              'missing': sorted(set(expected) - {r['agent'] for r in records}),
                              'totals_by_role': totals, 'agents': records})
    if records:
        with (out / 'usage.csv').open('w', newline='') as h:
            w = csv.DictWriter(h, fieldnames=list(records[0]), lineterminator='\n')
            w.writeheader()
            w.writerows(records)
    lines = [f'# {run} agent costs', '', 'Native usage; input includes cached reads; output includes reasoning. '
             'Standard API-equivalent at the saved rates; parent excluded.', '',
             '| Agent | Model | Done | Input | Cached | Output | Reasoning | Calls | USD |', '|---|---|---|---:|---:|---:|---:|---:|---:|']
    for r in sorted(records, key=lambda r: r['agent']):
        lines.append(f"| {r['agent'].removeprefix(plan['prefix'])} | {r['model']} {r['effort']} | {'yes' if r['completed'] else 'no'} | "
                     f"{r['input_tokens']:,} | {r['cached_input_tokens']:,} | {r['output_tokens']:,} | "
                     f"{r['reasoning_output_tokens']:,} | {r['tool_calls']} | ${r['usd']:.4f} |")
    lines += ['', f"Total: ${totals['ALL']['usd']:.4f} for {len(records)} of {len(expected)} agents."]
    flagged = [r['agent'] for r in records if r['unpriced_long_context']]
    if flagged:
        lines.append(f'Long-context requests priced at the short rate (no saved long tier): {", ".join(flagged)}.')
    (out / 'COSTS.md').write_text('\n'.join(lines) + '\n')
    print('\n'.join(lines[-2:]))


if __name__ == '__main__':
    main()
