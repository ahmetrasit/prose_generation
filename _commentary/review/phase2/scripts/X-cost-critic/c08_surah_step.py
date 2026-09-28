#!/usr/bin/env python3
"""Can one surah-commentary call (A's S5, B's step 6) read what the designs hand it, for long surahs?
Measure recorded ayah-commentary sizes (calibrated tokens) and multiply by ayat per surah; compare with the 1M context,
the ~140k thinking-collapse band, and B's own <=110k budget. Output side: v15's S1 surah commentary (7 ayat) output."""
import json, re, glob, statistics as st
from pathlib import Path
HERE = Path(__file__).resolve().parent; PG = Path('/Volumes/OZTURK/_projects/prose_generation')
cal = json.load(open(HERE / 'calib.json')); AR = re.compile(r'[؀-ۿݐ-ݿࢠ-ࣿ]')
def tok(t):
    a = len(AR.findall(t)); return cal['a_ar'] * a + cal['a_other'] * (len(t) - a)
fs = glob.glob(str(PG / '_commentary/v15/out*/s*/*/commentary.tr.md')) + glob.glob(str(PG / '_commentary/v9/lines/work/*/w10-opus-cold*.md')) + glob.glob(str(PG / '_commentary/v9/lines/work/*/*cold*/*.md'))
vals = []
for f in fs:
    t = open(f, encoding='utf-8').read()
    if len(t) > 2000: vals.append((tok(t), len(t.split()), f.split('_commentary/')[1]))
print(f'recorded commentaries: n={len(vals)}; calibrated tokens median {st.median(v[0] for v in vals):,.0f}, max {max(v[0] for v in vals):,.0f}; words median {st.median(v[1] for v in vals):,.0f}')
for v in sorted(vals)[-5:]: print('  ', round(v[0]), v[1], v[2])
med = st.median(v[0] for v in vals)
sc = json.load(open(HERE / 'out_c04_surah_scale.json')); ay = {int(k): v for k, v in sc['ay'].items()}
print('\nsurah  ayat  full commentaries  lead 20%  (tokens)')
for s in (2, 3, 4, 26, 18, 100):
    n = ay[s] - (1 if s != 1 and s != 9 else 0)
    print(f'S{s:<4d} {n:4d} {n*med:>12,.0f} {n*med*0.2:>10,.0f}')
big = [s for s in ay if (ay[s]) * med > 1_000_000]; over140 = [s for s in ay if ay[s] * med * 0.2 > 140_000]
print(f'surahs whose full ayah commentaries exceed 1M tokens: {len(big)}; whose lead-20% still exceeds 140k: {len(over140)} -> {sum(ay[s] for s in over140)} lines')
r = json.load(open(PG / '_commentary/v15/out/s001/surah.tr.md.raw.json'))['usage']
print(f"v15 S1 surah commentary (7 ayat): out {r['output_tokens']:,} (thinking {r['output_tokens_details']['thinking_tokens']:,}) -> {r['output_tokens']/7:,.0f} out tokens per ayah")
print(f"  scaled to S2 (286 ayat) at even 1/10 of that per ayah: {r['output_tokens']/7*286/10:,.0f} tokens vs CLI 64K per response")
