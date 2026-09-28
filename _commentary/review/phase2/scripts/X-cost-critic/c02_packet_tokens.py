#!/usr/bin/env python3
"""Apply the calibrated token formula (c01: intercept 4581 = claude -p prefix + brief overhead, 1.151/Arabic char,
0.366/other char) to every packet file each proposal actually built, and compare with the proposal's own estimate.
Reports the packet alone (without the 4581 intercept) and the Arabic share."""
import json, re, statistics as st
from pathlib import Path
HERE = Path(__file__).resolve().parent
PH = HERE.parent
cal = json.load(open(HERE / 'calib.json'))
AR_CH = re.compile(r'[؀-ۿݐ-ݿࢠ-ࣿ]')
def tok(text):
    n_ar = len(AR_CH.findall(text)); n_o = len(text) - n_ar
    return cal['a_ar'] * n_ar + cal['a_other'] * n_o, n_ar / max(1, len(text)), len(text), len(text.encode('utf-8'))
def pct(v, q):
    v = sorted(v); return v[min(len(v) - 1, int(q * len(v)))]
out = {}
def report(label, files, claimed=None, claim_fn=None):
    res = []
    for f in files:
        t, sh, ch, by = tok(f.read_text(encoding='utf-8'))
        res.append((f.name, t, sh, ch, by, claim_fn(ch, by) if claim_fn else None))
    if not res:
        print(label, 'no files'); return
    ts = [r[1] for r in res]
    print(f'== {label}: n={len(res)} calibrated tokens median {st.median(ts):,.0f} p90 {pct(ts,0.9):,.0f} max {max(ts):,.0f}; arabic share median {st.median([r[2] for r in res]):.2f}')
    if claim_fn:
        errs = [(r[5] - r[1]) / r[1] for r in res]
        print(f'   proposal formula vs calibrated: median {st.median(errs):+.2f} (neg = proposal underestimates)')
    if len(res) <= 20:
        for r in sorted(res, key=lambda r: r[1]):
            extra = f' proposal={r[5]:,.0f}' if r[5] else ''
            print(f'   {r[0]:28s} chars={r[3]:>8,} ar={r[2]:.2f} calibrated={r[1]:>9,.0f}{extra}')
    out[label] = {'n': len(res), 'median': st.median(ts), 'p90': pct(ts, 0.9), 'max': max(ts), 'rows': [(r[0], round(r[1])) for r in res]}
    return res
A = PH / 'A-v5-step/out'
resA = report('A digest (909 v5 ayat)', sorted((A / 'digests').glob('*.digest.md')), claim_fn=lambda ch, by: by / 2.0)
report('A digest Tier-2', sorted((A / 'digests_tier2').glob('*.digest.md')), claim_fn=lambda ch, by: by / 2.0)
report('A lookup (909 v5 ayat)', sorted((A / 'digests').glob('*.lookup.jsonl')), claim_fn=lambda ch, by: by / 2.0)
B = PH / 'B-noniterative'
report('B supply named/blind', sorted((B / 'supply').glob('*.md')))
report('B supply random120 full', sorted((B / 'supply_sample').glob('*.md')))
report('B supply random120 light', sorted((B / 'supply_sample_light').glob('*.md')))
report('C1 push', sorted((PH / 'C1-branch-distance/harvest2').glob('*.push.md')), claim_fn=lambda ch, by: ch / 2.2)
report('C2 sheet', sorted((PH / 'C2-loaded-parallels/harvest').glob('*.md')), claim_fn=lambda ch, by: ch / 2.75)
report('D KA phrase packet', sorted((PH / 'D-knowledge-supply/r3/packets').glob('*.ka.phrase.md')))
# A: long-ayah tail and the 5:6-type maxima
if resA:
    big = sorted(resA, key=lambda r: -r[1])[:8]
    print('A largest digests:', [(r[0], round(r[1])) for r in big])
json.dump(out, open(HERE / 'out_c02_packet_tokens.json', 'w'), ensure_ascii=False, indent=1)
