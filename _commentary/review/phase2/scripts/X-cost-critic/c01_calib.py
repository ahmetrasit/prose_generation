#!/usr/bin/env python3
"""Refit a two-rate token estimate (Arabic-script chars vs other chars) on billed single-turn v9 Opus runs
(same method as D's r3/calib.py, re-run here so the critic does not depend on the proposer's number), and
also check two alternatives the proposals used: A's bytes/2.0, C1's chars/2.2, C2's chars/2.5-3.
Also validates against v15's single-turn write calls (prompt file + usage in raw.json)."""
import csv, json, re, statistics as st
from pathlib import Path
HERE = Path(__file__).resolve().parent
P = Path('/Volumes/OZTURK/_projects'); PG = P / 'prose_generation'; V9 = PG / '_commentary' / 'v9'; V15 = PG / '_commentary' / 'v15'
AR_CH = re.compile(r'[؀-ۿݐ-ݿࢠ-ࣿ]')
rows = list(csv.DictReader(open(PG / '_commentary/review/phase1/scripts/dilution/metrics.tsv', encoding='utf-8'), delimiter='\t'))
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
    data.append((r['ayah'], arm, n_ar, n_o, len(text.encode('utf-8')), len(text), int(r['billed_input_total'])))

def solve3(X, Y):
    XtX = [[sum(x[i] * x[j] for x in X) for j in range(3)] for i in range(3)]
    XtY = [sum(x[i] * y for x, y in zip(X, Y)) for i in range(3)]
    A = [row[:] + [bb] for row, bb in zip(XtX, XtY)]
    for i in range(3):
        p = max(range(i, 3), key=lambda k: abs(A[k][i])); A[i], A[p] = A[p], A[i]
        for k in range(3):
            if k != i:
                f = A[k][i] / A[i][i]; A[k] = [x - f * y for x, y in zip(A[k], A[i])]
    return [A[i][3] / A[i][i] for i in range(3)]
c, a, b = solve3([(1.0, d[2], d[3]) for d in data], [d[6] for d in data])
err = [abs((c + a * d[2] + b * d[3]) - d[6]) / d[6] for d in data]
print(f'fit n={len(data)} intercept={c:.0f} a_ar={a:.3f} a_other={b:.3f} median_rel_err={st.median(err):.3f} max={max(err):.3f}')
# the alternatives, net of the ~2.7k claude -p system prefix (cache_read 2694 in every v9 run)
for name, fn in [('bytes/2.0 (A)', lambda d: d[4] / 2.0 + 2694), ('chars/2.2 (C1)', lambda d: d[5] / 2.2 + 2694),
                 ('chars/2.5 (C2 low)', lambda d: d[5] / 2.5 + 2694), ('chars/3.0 (C2 high)', lambda d: d[5] / 3.0 + 2694)]:
    rel = [(fn(d) - d[6]) / d[6] for d in data]
    print(f'{name:22s} median signed err {st.median(rel):+.3f}  (neg = underestimate)  range {min(rel):+.2f}..{max(rel):+.2f}')
# bytes/token observed, by Arabic share
print('observed bytes per billed token (net of 2694 prefix), by Arabic share of chars:')
for d in sorted(data, key=lambda d: d[2] / (d[2] + d[3])):
    pass
buckets = {}
for d in data:
    sh = d[2] / (d[2] + d[3]); k = round(sh, 1)
    buckets.setdefault(k, []).append(d[4] / max(1, d[6] - 2694))
for k in sorted(buckets):
    print(f'  arabic share ~{k:.1f}: n={len(buckets[k])} bytes/token median {st.median(buckets[k]):.2f}')
# out-of-sample check: v15 single-turn write calls (num_turns == 1)
print('out-of-sample: v15 single-turn write/surah calls')
oos = []
for raw in sorted(V15.glob('out*/s*/**/*.raw.json')):
    d = json.load(open(raw))
    if d.get('num_turns') != 1:
        continue
    pr = Path(str(raw).replace('.raw.json', '.prompt.md'))
    if not pr.exists():
        continue
    t = pr.read_text(encoding='utf-8'); n_ar = len(AR_CH.findall(t)); n_o = len(t) - n_ar
    u = d['usage']; billed = u['input_tokens'] + u['cache_creation_input_tokens'] + u['cache_read_input_tokens']
    pred = c + a * n_ar + b * n_o
    oos.append((pred - billed) / billed)
    print(f'  {raw.relative_to(V15)}: chars={len(t)} ar_share={n_ar/len(t):.2f} billed={billed} pred={pred:.0f} err={(pred-billed)/billed:+.3f} bytes/tok={len(t.encode())/billed:.2f}')
print(f'  median signed err {st.median(oos):+.3f}')
json.dump({'intercept': c, 'a_ar': a, 'a_other': b, 'n': len(data)}, open(HERE / 'calib.json', 'w'))
