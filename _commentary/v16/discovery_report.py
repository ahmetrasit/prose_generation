#!/usr/bin/env python3
"""Report a completed native discovery batch; merge/dry-build, never call models."""
import argparse
import csv
import json
import re
from collections import Counter

import discover as D
import augment_surah as A


def report(surah, tag, batch):
    root = D.discovery_dir(surah, tag)
    plan = json.loads((root / 'orchestration.json').read_text())
    jobs = [j for j in plan['jobs'] if j['batch'] == batch]
    if not jobs:
        raise ValueError('Unknown batch')
    q = D.M.verses()
    _, source, _ = D.B.surah_inputs(surah)
    sections = {s['k']: s for s in D.sections(source.read_text())}
    data = {'surah': surah, 'run_tag': tag, 'batch': batch, 'jobs': [], 'sections': [], 'opus_started': False}
    lines = [f'# S{surah} {tag} batch {batch}', '',
             '| Image | Model | Initial | Proposals | New | Repeats | Final | Check |',
             '|---|---|---:|---:|---:|---:|---:|---|']
    details = []
    for job in jobs:
        k, model = job['section'], job['model']
        d = root / f'sec{k}' / model
        log = json.loads((d / 'run.log.json').read_text())
        if log['status'] != 'ok' or not log['turn2']['completed']:
            raise ValueError(f'Unfinished/invalid job: {d}')
        rows, bad = D.parse_rows(d / 'list.tsv', surah, q)
        if bad or len({r['ref'] for r in rows}) != len(rows):
            raise ValueError(f'Invalid final list: {d}')
        cons = log.get('consolidation') or {}
        cited = {r for r in re.findall(r'source:(\d+:\d+)', sections[k]['prose']) if not r.startswith(f'{surah}:')}
        item = {'section': k, 'model': model, 'initial': log['turn1_rows'],
                'proposals': cons.get('raw_proposal_rows', log['turn2']['rows_added']),
                'added': log['turn2']['rows_added'], 'repeats': len(cons.get('repeated_proposals', [])),
                'final': len(rows), 'check': log['check'], 'arabic_flags': log['arabic_findings'],
                'missing_existing_citations': sorted(cited - {r['ref'] for r in rows}),
                'usage_tokens': log['usage_tokens'], 'cost_usd': log['cost_usd'],
                'diagnostics': log['tool_diagnostics'], 'strengths': dict(Counter(r['strength'] for r in rows))}
        for name in ('validation_review.json', 'protocol_review.json'):
            if (d / name).exists(): item[name] = json.loads((d / name).read_text())
        data['jobs'].append(item)
        lines.append(f"| {k} | {model} | {item['initial']} | {item['proposals']} | {item['added']} | {item['repeats']} | {len(rows)} | {item['check']} |")
        details.extend(['', f"Image {k} {model}: {item['arabic_flags']} Arabic review flags; see sec{k}/{model}/validation.json. "
                      f"Repeated proposals: {item['repeats']}; see consolidation.json. Missing existing citations: {item['missing_existing_citations']}.",
                      *[f"Recovered diagnostic: {x['message']}" for x in item['diagnostics']]])
    lines.extend(details)
    for k in sorted({j['section'] for j in jobs}):
        if not all((root / f'sec{k}' / m / 'run.log.json').exists() for m in D.MODELS):
            continue
        D.merge(surah, [sections[k]], q, tag)
        merged = root / f'sec{k}.merged.tsv'
        with merged.open() as stream: rows = list(csv.DictReader(stream, delimiter='\t'))
        text, meta = A.build(surah, k, merged)
        meta.update({'dry_run_only': True, 'opus_started': False,
                     'input_tokens_estimate': A.V.est_tokens(text),
                     'estimate_usd': round(A.estimate(text, meta['passages']), 2)})
        (root / f'sec{k}.handoff.dry.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n')
        item = {'section': k, 'union': len(rows), 'overlap': sum(bool(r['luna_label'] and r['terra_label']) for r in rows),
                'tiers': dict(Counter(r['tier'] for r in rows)),
                'dry_handoff': {key: meta[key] for key in ('passages', 'discovery_candidates', 'context_neighbours', 'input_tokens_estimate', 'estimate_usd')}}
        data['sections'].append(item)
        lines.extend(['', f"Image {k}: {len(rows)} unique candidates; {item['overlap']} named by both models. "
                      f"{meta['context_neighbours']} separate context neighbours. Dry Opus estimate ${meta['estimate_usd']:.2f}; no call."])
    lines.extend(['', 'Both turns completed for every job in this batch. Input hashes, model/effort, unchanged initial rows, schema, unique final references and follow-up delivery are checked in native logs. Tool calls were reviewed before finishing.',
                  '', 'All raw proposals remain intact. Repeated references do not change original grades. Arabic flags are review aids, not error counts. See validation_review.json where present; English meaning and relevance are not exhaustively verified.',
                  '', 'Recorded incremental discovery estimate/charge: $0 on the Codex subscription. Token usage and all recovered diagnostics are in the JSON and native logs.'])
    (root / f'batch{batch}.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    (root / f'batch{batch}.report.md').write_text('\n'.join(lines) + '\n')
    print(json.dumps({'batch': batch, 'jobs': [{k: v for k, v in j.items() if k not in ('usage_tokens', 'diagnostics') and not k.endswith('.json')} for j in data['jobs']], 'sections': data['sections']}, ensure_ascii=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--surah', type=int, required=True)
    parser.add_argument('--run-tag', required=True)
    parser.add_argument('--batch', type=int, required=True)
    args = parser.parse_args()
    report(args.surah, args.run_tag, args.batch)
