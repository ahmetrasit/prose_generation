#!/usr/bin/env python3
"""Calibrate a two-rate token estimate (Arabic-script chars vs other chars) on billed single-turn v9 Opus runs.
Input text per run = SYSTEM + prompt line + inlined files, rebuilt the same way synth.py builds it (files only; the
prompt line and system prompt are ~600 chars and absorbed in the intercept). Billed tokens = input + cache_write + cache_read.
Least squares with intercept (the claude -p system prefix, ~2.7k tokens cached). Writes calib.json."""
import csv, json, sys
sys.path.insert(0, __import__('os').path.dirname(__file__))
from common import *
rows = list(csv.DictReader(open(P / 'prose_generation/_commentary/review/phase1/scripts/dilution/metrics.tsv', encoding='utf-8'), delimiter='\t'))
W10 = V9 / 'prompts' / 'write_v10.md'
data = []
for r in rows:
    run = r['run']
    if not run.startswith('v9:w10-opus') or r['turns'] != '1' or not r['billed_input_total']:
        continue
    arm = run.split(':', 1)[1]
    s, a = r['ayah'].split(':'); sa = f'{s}_{a}'
    w = V9 / 'lines' / 'work' / sa
    dic = V9 / 'input' / 'v2' / f's{int(s):03d}' / sa / '01_dictionary.md'
    files = {'w10-opus-cold': [W10, w / 'context.md'], 'w10-opus-cold2': [W10, w / 'context.md'],
             'w10-opus-dict': [W10, w / 'context.md', dic], 'w10-opus-dslim': [W10, w / 'context.md', dic, w / 'package.slim.md'],
             'w10-opus-dhft': [W10, w / 'context.md', dic, dic.parent / '02_hft.md'], 'w10-opus': [W10, w / 'context.md', w / 'package.md']}.get(arm)
    if not files or not all(f.exists() for f in files):
        continue
    text = ''.join(f.read_text(encoding='utf-8') for f in files)
    n_ar = len(AR_CH.findall(text)); n_o = len(text) - n_ar
    data.append((r['ayah'], arm, n_ar, n_o, int(r['billed_input_total'])))
# least squares: y = c + a*n_ar + b*n_o
import itertools
n = len(data)
X = [(1.0, d[2], d[3]) for d in data]; Y = [d[4] for d in data]
XtX = [[sum(x[i] * x[j] for x in X) for j in range(3)] for i in range(3)]
XtY = [sum(x[i] * y for x, y in zip(X, Y)) for i in range(3)]
def solve(A, b):
    A = [row[:] + [bb] for row, bb in zip(A, b)]
    for i in range(3):
        p = max(range(i, 3), key=lambda k: abs(A[k][i])); A[i], A[p] = A[p], A[i]
        for k in range(3):
            if k != i:
                f = A[k][i] / A[i][i]
                A[k] = [x - f * y for x, y in zip(A[k], A[i])]
    return [A[i][3] / A[i][i] for i in range(3)]
c, a, b = solve(XtX, XtY)
err = [abs((c + a * d[2] + b * d[3]) - d[4]) / d[4] for d in data]
print(f'n={n} intercept={c:.0f} a_ar={a:.3f} a_other={b:.3f} median_rel_err={sorted(err)[n//2]:.3f} max_rel_err={max(err):.3f}')
for d, e in zip(data, err):
    print(f'  {d[0]:6} {d[1]:16} ar={d[2]:7} other={d[3]:7} billed={d[4]:7} pred={c + a*d[2] + b*d[3]:9.0f} err={e:.2f}')
json.dump({'intercept': c, 'a_ar': a, 'a_other': b, 'n': n}, open(HERE / 'calib.json', 'w'))
