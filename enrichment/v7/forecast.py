#!/usr/bin/env python3
"""Forecast a v7 Luna chunk's peak request input from completed native sessions.

This is a planning estimate, not a context limit. It records a reproducible list of
original chunks to split before launching a new run.
"""
import argparse
import json
from collections import defaultdict
from pathlib import Path

import numpy as np

import digest


def rows(run, with_usage):
    d = digest.run_dir(run)
    man = json.loads((d / 'manifest.json').read_text())
    result = []
    for c in man['chunks']:
        prompt = d / 'spawn' / f'luna-max_c{c["chunk"]:02d}.md'
        row = {'run': run, 'chunk': c['chunk'], 'source_chars': c['chars'],
               'segments': len(c['locs']), 'prompt_chars': len(prompt.read_text()),
               'source_group': c['sources'][0] if len(c['sources']) == 1 else 'MULTI'}
        if with_usage:
            agent = f'/root/v7d_{run}_luna-max_c{c["chunk"]:02d}'
            usage = digest.usage(d / 'runs', agent)
            if not usage or not usage['completed'] or not usage['peak']:
                raise SystemExit(f'missing completed usage for {agent}')
            row['peak'] = usage['peak']
        result.append(row)
    return result


def features(row):
    return [1, row['source_chars'] / 10_000, row['segments'] / 10,
            row['prompt_chars'] / 10_000]


def fit_predict(train, target):
    x = np.array([features(r) for r in train])
    y = np.array([r['peak'] / 1_000 for r in train])
    coefficients = np.linalg.lstsq(x, y, rcond=None)[0]
    residuals = defaultdict(list)
    for row, error in zip(train, y - x @ coefficients):
        residuals[row['source_group']].append(error)
    # A source's historical deviation helps, but shrink small samples toward zero.
    predictions = []
    for row in target:
        group = residuals[row['source_group']]
        source_adjustment = sum(group) / (len(group) + 5)
        predictions.append(1_000 * (np.dot(features(row), coefficients) + source_adjustment))
    return [float(c) for c in coefficients], predictions


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run', help='original built but unrun v7 run')
    parser.add_argument('--threshold', type=int, required=True, help='predicted peak request input tokens')
    parser.add_argument('--reference-runs', nargs='+', default=['s103-1', 's103-23', 's1_87_114'])
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    train = [r for run in args.reference_runs for r in rows(run, True)]
    target = rows(args.run, False)
    coefficients, estimates = fit_predict(train, target)
    validation = []
    for run in args.reference_runs:
        held_out = [r for r in train if r['run'] == run]
        other = [r for r in train if r['run'] != run]
        _, forecast = fit_predict(other, held_out)
        validation.append({'run': run, 'sessions': len(held_out),
                           'mean_absolute_error_tokens': int(round(sum(abs(p - r['peak'])
                                                                       for p, r in zip(forecast, held_out)) / len(held_out))),
                           'predicted_above_threshold': int(sum(p > args.threshold for p in forecast)),
                           'actual_above_threshold': sum(r['peak'] > args.threshold for r in held_out),
                           'correctly_predicted_above_threshold': int(sum(p > args.threshold and r['peak'] > args.threshold
                                                                          for p, r in zip(forecast, held_out)))})
    predictions = [{**row, 'predicted_peak_tokens': int(round(estimate))} for row, estimate in zip(target, estimates)]
    selected = [r['chunk'] for r in predictions if r['predicted_peak_tokens'] > args.threshold]
    record = {'run': args.run, 'threshold_tokens': args.threshold,
              'method': 'OLS on source chars, segment count and spawn prompt chars; per-source residual shrunk by 5 sessions',
              'reference_runs': args.reference_runs, 'training_sessions': len(train),
              'coefficients_peak_thousands': coefficients, 'leave_one_run_out': validation,
              'split_chunks': selected, 'predictions': predictions}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print(f'{args.run}: {len(target)} original chunks, {len(train)} completed reference sessions, '
          f'{len(selected)} forecast above {args.threshold:,} tokens; split chunks: {selected}')
    for v in validation:
        print(f"{v['run']}: holdout error {v['mean_absolute_error_tokens']:,} tokens; "
              f"{v['correctly_predicted_above_threshold']}/{v['actual_above_threshold']} "
              'actual over-threshold chunks identified')


if __name__ == '__main__':
    main()
