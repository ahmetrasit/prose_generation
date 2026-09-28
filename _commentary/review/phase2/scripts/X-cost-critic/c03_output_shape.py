#!/usr/bin/env python3
"""Output (incl. thinking) per single Opus call by condition, joined from Phase 1 metrics.tsv and D's confound groups.
Question: every proposal borrows the v9 dict arm's ~22k output (FED-NOPERM: 'work only from the supplied evidence').
All proposals switch to memory-permitted synthesis. What output do permitted, fed calls actually produce?
Also: output vs ayah length (words) to extrapolate to 2:282 / 2:255 against the CLI's 64K per-response cap."""
import csv, statistics as st, collections, json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
PG = Path('/Volumes/OZTURK/_projects/prose_generation')
M = list(csv.DictReader(open(PG / '_commentary/review/phase1/scripts/dilution/metrics.tsv', encoding='utf-8'), delimiter='\t'))
G = {(r['ayah'], r['run']): r['group'] for r in csv.DictReader(open(HERE.parent / 'D-knowledge-supply/r3/confound.tsv'), delimiter='\t')}
def f(x):
    try: return float(x)
    except: return None
grp = collections.defaultdict(list)
for r in M:
    g = G.get((r['ayah'], r['run']))
    if not g or f(r['output_tokens']) is None: continue
    grp[g].append((r['ayah'], r['run'], f(r['billed_input_total']), f(r['output_tokens']), f(r['thinking_tokens']), f(r['cost_usd']), f(r['words'])))
for g, v in sorted(grp.items()):
    o = [x[3] for x in v]; t = [x[4] for x in v]; c = [x[5] for x in v]; i = [x[2] for x in v]
    print(f'{g:11s} n={len(v):2d} in med {st.median(i):8,.0f}  out med {st.median(o):7,.0f} (p75 {sorted(o)[int(.75*len(o))]:7,.0f}, max {max(o):7,.0f})  thinking med {st.median(t):7,.0f}  cost med ${st.median(c):.2f}')
    runs = collections.Counter(x[1].split(':')[0] + ':' + x[1].split(':')[1][:14] for x in v)
    print('            runs:', dict(runs))
# quran word counts per ayah (from v15 data words.tsv)
W = collections.Counter()
for line in open(PG / '_commentary/v15/data/words.tsv', encoding='utf-8'):
    p = line.split('\t')
    if len(p) > 2 and re.match(r'^\d+$', p[0]) and re.match(r'^\d+$', p[1]):
        W[(int(p[0]), int(p[1]))] += 1
if not W:
    hdr = open(PG / '_commentary/v15/data/words.tsv', encoding='utf-8').readline()
    print('words.tsv header:', hdr[:200])
def words(ref):
    s, a = map(int, ref.split(':')); return W.get((s, a))
print('\ncold arm (memory permitted, context only): output vs ayah words')
pts = []
for x in grp['COLD']:
    w = words(x[0]); pts.append((w, x[3], x[0], x[2]))
    print(f'  {x[0]:7s} words={w} in={x[2]:,.0f} out={x[3]:,.0f}')
# simple least squares out = a + b*words
if all(p[0] for p in pts):
    n = len(pts); mx = sum(p[0] for p in pts) / n; my = sum(p[1] for p in pts) / n
    b = sum((p[0] - mx) * (p[1] - my) for p in pts) / sum((p[0] - mx) ** 2 for p in pts); a = my - b * mx
    print(f'  fit out = {a:,.0f} + {b:,.0f} x words')
    for ref in ['2:282', '2:255', '4:34', '5:6', '2:102', '24:31', '73:20', '2:196']:
        w = words(ref); print(f'   extrapolated {ref}: words={w} out~{a + b * w:,.0f}')
    dist = sorted(W.values()); n = len(dist)
    thr = (64000 - a) / b
    print(f'  ayat whose extrapolated cold-arm output exceeds 64K: words > {thr:.0f}: {sum(1 for v in dist if v > thr)} ayat')
    thr2 = (50000 - a) / b
    print(f'  ... exceeds 50K (within 1.3x of the cap given replicate spread): words > {thr2:.0f}: {sum(1 for v in dist if v > thr2)} ayat')
    print(f'  ayah length: median {st.median(dist)} words; >=37 words (4:34 size): {sum(1 for v in dist if v >= words("4:34"))}')
