#!/usr/bin/env python3
"""A's S1 chain-map call reads, per window: window text + the surah's channel-review subchannels + a per-ayah compact
index (A's own list: A branches, C titles, F1, F2 intra-surah links, F7 top pairs). A estimates 40-80k input for
'7-10-ayat windows'. Measure the compact index from A's 909 digests (sections A, C [titles only ~ first line per item],
F1, F2, F7) in calibrated tokens and sum per pericope for the v5 surahs that have pericopes; add the surah review.
Upper bound for the review (whole file); lower bound 0 (if only window-anchored subchannels were pushed)."""
import json, re, statistics as st, collections
from pathlib import Path
HERE = Path(__file__).resolve().parent
PH = HERE.parent; P = Path('/Volumes/OZTURK/_projects')
cal = json.load(open(HERE / 'calib.json'))
AR = re.compile(r'[؀-ۿݐ-ݿࢠ-ࣿ]')
def tok(t):
    a = len(AR.findall(t)); return cal['a_ar'] * a + cal['a_other'] * (len(t) - a)
sc = json.load(open(HERE / 'out_c04_surah_scale.json'))
rev = {int(k): v for k, v in sc['review_tok'].items()}
idx = {}
for f in (PH / 'A-v5-step/out/digests').glob('*.digest.md'):
    m = re.match(r'(\d+)_(\d+)\.digest\.md', f.name)
    if not m: continue
    t = f.read_text(encoding='utf-8')
    secs = re.split(r'\n(?=## )', t)
    keep = 0.0; full = tok(t)
    for s in secs:
        h = s.split('\n', 1)[0]
        if h.startswith('## A.') or h.startswith('## F1.'):
            keep += tok(s)
        elif h.startswith('## F2.') or h.startswith('## F7.'):
            keep += sum(tok(l) for l in [l for l in s.split('\n')[1:] if l.strip()][:10])
        elif False:
            keep += tok(s)
        elif h.startswith('## C.'):
            # titles + first clause only: first 160 chars of each item line
            keep += sum(tok(l[:160]) for l in s.split('\n')[1:] if l.strip())
    idx[(int(m.group(1)), int(m.group(2)))] = (keep, full)
k = [v[0] for v in idx.values()]
print(f'A LEAN compact index per ayah (A+C-titles+F1+top10 F2+top10 F7), calibrated tokens: median {st.median(k):,.0f}, p90 {sorted(k)[int(.9*len(k))]:,.0f}, max {max(k):,.0f}; share of digest median {st.median([v[0]/v[1] for v in idx.values()]):.2f}')
per = collections.defaultdict(list)
for line in open(P / 'quran-data/data/analysis/channels/network-v3/pericopes/surah_pericopes.jsonl'):
    r = json.loads(line); per[r['surah']].append((r['ayah_from'], r['ayah_to']))
rows = []
for s in sorted({s for s, a in idx}):
    wins = per.get(s) or [(1, max(a for ss, a in idx if ss == s))]
    for a0, a1 in wins:
        ix = sum(idx.get((s, a), (0, 0))[0] for a in range(a0, a1 + 1))
        n = a1 - a0 + 1
        rows.append((s, a0, a1, n, ix, rev.get(s, 0), ix + rev.get(s, 0) + 3000))
print('\nsurah window ayat index_tok review_tok total_upper(index+whole review+3k text/brief)')
for r in rows:
    if r[0] in (5, 12, 17, 18, 19, 1, 100) or r[6] > 120000:
        print(f'{r[0]:4d} {r[1]:3d}-{r[2]:<3d} {r[3]:4d} {r[4]:9,.0f} {r[5]:9,.0f} {r[6]:9,.0f}')
tot = [r[6] for r in rows]; lo = [r[4] + 3000 for r in rows]
print(f'\nwindows {len(rows)}: total input (index + whole review) median {st.median(tot):,.0f}, max {max(tot):,.0f}; >120k: {sum(1 for x in tot if x > 120000)}; >140k: {sum(1 for x in tot if x > 140000)}')
print(f'lower bound (index only, no review): median {st.median(lo):,.0f}, max {max(lo):,.0f}')
# cost per window at claude -p rates with output 30-50k (A's own) and per ayah
for lab, inp in [('median', st.median(tot)), ('max', max(tot))]:
    for out in (30000, 50000):
        c = inp * 8e-6 + out * 20e-6
        print(f'  {lab} window: in {inp:,.0f} out {out:,} -> ${c:.2f} on claude -p')
