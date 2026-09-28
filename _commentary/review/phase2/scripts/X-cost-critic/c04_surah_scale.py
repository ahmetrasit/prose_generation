#!/usr/bin/env python3
"""Surah-scale facts every proposal's per-ayah amortisation depends on:
ayat per surah, share of ayat in long surahs (>40), pericopes (A's S1 windows / B's S-reading windows),
channel-review size in calibrated tokens (the chains every surah step must read), HFT trace coverage (A Tier 2/3),
v5 coverage (A Tier 1), HFT packet sizes for the surahs without traces (A's S0b), and whole-surah text tokens (D, B's R_mem)."""
import json, re, glob, collections, statistics as st
from pathlib import Path
HERE = Path(__file__).resolve().parent
P = Path('/Volumes/OZTURK/_projects')
cal = json.load(open(HERE / 'calib.json'))
AR = re.compile(r'[؀-ۿݐ-ݿࢠ-ࣿ]')
def tok(t):
    a = len(AR.findall(t)); return cal['a_ar'] * a + cal['a_other'] * (len(t) - a)
# ayat and text per surah
ay = collections.Counter(); text = collections.defaultdict(str)
for line in open(P / 'quran-data/data/text/quran-uthmani.tsv', encoding='utf-8'):
    m = re.match(r'^(\d+):(\d+)\|(.*)$', line.rstrip('\n'))
    if m:
        s = int(m.group(1)); ay[s] += 1; text[s] += m.group(3) + ' '
tot = sum(ay.values())
long_ = sum(v for s, v in ay.items() if v > 40)
print(f'ayat {tot}; in surahs >40 ayat: {long_} ({long_/tot:.1%}); surahs >40 ayat: {sum(1 for v in ay.values() if v > 40)}')
per = collections.defaultdict(list)
for line in open(P / 'quran-data/data/analysis/channels/network-v3/pericopes/surah_pericopes.jsonl'):
    r = json.loads(line); per[r['surah']].append(r['ayah_to'] - r['ayah_from'] + 1)
sizes = [x for v in per.values() for x in v]
print(f'pericopes {len(sizes)} in {len(per)} surahs; size median {st.median(sizes)}, mean {sum(sizes)/len(sizes):.1f}, max {max(sizes)}; covered ayat {sum(sizes)}')
# channel reviews
rev = {}
for s in range(1, 115):
    f = P / f'quran-data/data/analysis/channels/network-v3/s{s:03d}/review/reader_a_pilot.md'
    if f.exists(): rev[s] = tok(f.read_text(encoding='utf-8'))
print(f'channel reviews: {len(rev)} surahs; missing {[s for s in range(1,115) if s not in rev]}')
lr = sorted(((v, s) for s, v in rev.items()), reverse=True)[:8]
print('largest reviews (calibrated tokens):', [(s, round(v)) for v, s in lr])
# HFT traces
hft = collections.defaultdict(set)
for f in glob.glob(str(P / 'latent_activation/focus_trace/runs/s*/readers/*/*.focus_trace.json')):
    m = re.search(r'/(\d+)_(\d+)\.focus_trace\.json$', f)
    if m: hft[int(m.group(1))].add(int(m.group(2)))
hft_ay = sum(len(v) for v in hft.values())
nohft = [s for s in range(1, 115) if s not in hft]
print(f'HFT traces: {hft_ay} ayat in {len(hft)} surahs; surahs without: {len(nohft)} -> {sum(ay[s] for s in nohft)} ayat: {nohft}')
v5 = {1, 5, 12, 17, 18, 19, 31, 32} | set(range(87, 115))
v5_ay = sum(ay[s] for s in v5)
print(f'v5 surahs {len(v5)} -> {v5_ay} ayat')
print(f'no v5 and no HFT surah: {sum(ay[s] for s in nohft if s not in v5)} ayat; of these in surahs >40 ayat: {sum(ay[s] for s in nohft if s not in v5 and ay[s] > 40)}')
# whole-surah text tokens
st_tok = {s: tok(text[s]) for s in ay}
print('whole-surah Arabic text tokens: S2', round(st_tok[2]), 'S3', round(st_tok[3]), 'S4', round(st_tok[4]), 'S5', round(st_tok[5]), 'S1', round(st_tok[1]))
print(f'surahs whose text alone exceeds 40k tokens: {[s for s,v in st_tok.items() if v > 40000]}')
# per surah table for the long ones
print('\nsurah ayat pericopes mean_per review_tok hft v5 text_tok')
rows = []
for s in sorted(ay, key=lambda s: -ay[s])[:20]:
    n = len(per.get(s, [])); rows.append(s)
    print(f'{s:4d} {ay[s]:4d} {n:4d} {ay[s]/max(1,n):6.1f} {round(rev.get(s,0)):8,d} {"y" if s in hft else "-"} {"y" if s in v5 else "-"} {round(st_tok[s]):7,d}')
json.dump({'ay': ay, 'pericopes': {s: len(v) for s, v in per.items()}, 'review_tok': rev, 'hft_surahs': sorted(hft), 'text_tok': st_tok},
          open(HERE / 'out_c04_surah_scale.json', 'w'), default=list)
