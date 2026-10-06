#!/usr/bin/env python3
"""Record isolated single-page memory-agent usage using native session counters."""
import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path
import memory_benchmark as M


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--unit', required=True)
    parser.add_argument('--sessions', type=Path, default=Path('/Users/ahmetrasit/.codex/sessions/2026/10/06'))
    args = parser.parse_args()
    lanes = {'astra-high': M.WORK.parent / args.unit / 'family-memory-astra-high-20261006'}
    records = M.collect(args.sessions, prefix=f'/root/memory{args.unit}_', lanes=lanes)
    total = {'agents': len(records), 'completed_agents': sum(r['status'] == 'completed' for r in records)}
    for key in (*M.METRICS, 'blocks', 'prose_words', 'standard_api_equivalent_usd'):
        total[key] = sum(r.get(key) or 0 for r in records)
    out = M.WORK.parent / args.unit / 'family-memory-benchmark-20261006'
    out.mkdir(exist_ok=True)
    report = {'unit': args.unit, 'updated_at': datetime.now(timezone.utc).isoformat(), 'expected_agents': 19,
              'accounting': 'Native cumulative counters; input includes cached input, output includes reasoning; parent excluded. API equivalents use Astra $10 uncached/$1 cached/$12.50 cache write/$50 output per million, not account billing.',
              'totals': total, 'agents': records}
    (out / 'usage.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    if records:
        with (out / 'usage.csv').open('w', newline='') as h:
            writer = csv.DictWriter(h, fieldnames=list(records[0]), lineterminator='\n')
            writer.writeheader(); writer.writerows(records)
    lines = [f'# {args.unit.replace("_", ":")} Astra high memory benchmark', '',
             'Native cumulative per-agent usage; parent excluded. Attributions remain memory-based and unverified.', '',
             '| Family | Status | Input | Cached input | Output | Reasoning | Blocks | USD equivalent |',
             '|---|---|---:|---:|---:|---:|---:|---:|']
    for r in records:
        values = [str(r[k]) if r[k] is not None else 'Pending' for k in ['input_tokens', 'cached_input_tokens', 'output_tokens', 'reasoning_output_tokens', 'blocks']]
        cost = r['standard_api_equivalent_usd']
        lines.append('| ' + ' | '.join([r['family'], r['status'], *values, f'${cost:.6f}' if cost is not None else 'Pending']) + ' |')
    lines += ['', f'Completed: {total["completed_agents"]}/19. API-equivalent total: ${total["standard_api_equivalent_usd"]:.4f}.', '',
              'Costs use [official Standard API pricing](https://developers.openai.com/api/docs/pricing); output includes reasoning. These are not billing figures. Full native data: [usage.json](usage.json), [usage.csv](usage.csv).', '']
    (out / 'README.md').write_text('\n'.join(lines))
    print(json.dumps(total))


if __name__ == '__main__':
    main()
