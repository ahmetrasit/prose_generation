#!/usr/bin/env python3
"""One-time Luna jobs the proposals hide or call optional.
(1) A's S0b Luna-HFT on the 24 no-trace surahs: packet sizes (calibrated tokens) from the existing HFT packets,
    token cost at Luna list $0.20/$1.20 (v8_batch/COSTS.md per A), and wall time from v15's measured Luna throughput.
(2) Luna throughput and token intensity from v15's ledger (frames, profiles, loanwords, evidence jobs).
(3) B's whole-Quran loanword cards (~187 jobs), C2's construction extraction (~30 jobs)."""
import json, re, glob, statistics as st, collections
from pathlib import Path
HERE = Path(__file__).resolve().parent
P = Path('/Volumes/OZTURK/_projects')
cal = json.load(open(HERE / 'calib.json'))
AR = re.compile(r'[؀-ۿݐ-ݿࢠ-ࣿ]')
def tok(t):
    a = len(AR.findall(t)); return cal['a_ar'] * a + cal['a_other'] * (len(t) - a)
sc = json.load(open(HERE / 'out_c04_surah_scale.json'))
hft_surahs = set(sc['hft_surahs'])
nohft = [s for s in range(1, 115) if s not in hft_surahs]
# (2) Luna throughput from v15
led = [json.loads(l) for l in open(P / 'prose_generation/_commentary/v15/out/ledger.jsonl')] + \
      [json.loads(l) for l in open(P / 'prose_generation/_commentary/v15/out-nocap/ledger.jsonl')]
lu = collections.defaultdict(list)
for r in led:
    if r['model'].startswith('gpt') and r.get('usage'):
        u = r['usage']; lu[r['step']].append((u['input_tokens'], u['output_tokens'], u.get('reasoning_output_tokens', 0), r['seconds']))
print('v15 Luna jobs (tokens from codex usage; seconds wall):')
for k, v in lu.items():
    print(f'  {k:10s} n={len(v):3d} in med {st.median(x[0] for x in v):7,.0f} out med {st.median(x[1] for x in v):6,.0f} reasoning med {st.median(x[2] for x in v):6,.0f} sec med {st.median(x[3] for x in v):4.0f} max {max(x[3] for x in v)}')
ev = lu.get('evidence', [])
# out tokens per input token for the evidence job (closest to an HFT trace: per-ayah, large packet, max reasoning)
# (1) HFT packets for no-trace surahs
sizes = []; per_s = {}
for s in nohft:
    fs = sorted(glob.glob(str(P / f'latent_activation/focus_trace/runs/s{s}/packets/*.packet.json')))
    ts = []
    for f in fs:
        t = open(f, encoding='utf-8').read(); ts.append(tok(t))
    per_s[s] = (len(fs), st.median(ts) if ts else 0, max(ts) if ts else 0)
    sizes += ts
print(f'\nHFT packets for the {len(nohft)} no-trace surahs: {len(sizes)} packets; calibrated tokens median {st.median(sizes):,.0f}, p90 {sorted(sizes)[int(.9*len(sizes))]:,.0f}, max {max(sizes):,.0f}; >200k: {sum(1 for x in sizes if x > 200000)}')
for s in (2, 3, 4, 6, 7, 26):
    print(f'  S{s}: {per_s[s][0]} packets, median {per_s[s][1]:,.0f}, max {per_s[s][2]:,.0f}')
# trace output: existing trace json sizes as output proxy
tr = [tok(open(f, encoding='utf-8').read()) for f in glob.glob(str(P / 'latent_activation/focus_trace/runs/s*/readers/*/*.focus_trace.json'))[:600]]
print(f'existing focus_trace JSON (output proxy, 600 sampled): calibrated tokens median {st.median(tr):,.0f}, p90 {sorted(tr)[int(.9*len(tr))]:,.0f}')
# cost at Luna list and wall time
out_mult = 2.0  # reasoning ~ equal to visible output in v15 Luna jobs (see medians above) -> assume trace + equal reasoning
inp = sum(sizes); outp = len(sizes) * st.median(tr) * out_mult
print(f'S0b token total: input {inp/1e6:,.1f}M, output ~{outp/1e6:,.1f}M -> Luna list ${inp*0.2e-6 + outp*1.2e-6:,.0f} (standard), ${(inp*0.2e-6 + outp*1.2e-6)/2:,.0f} (Batch)')
if ev:
    spt = st.median(x[3] / x[0] * 1000 for x in ev)
    print(f'wall time: v15 evidence jobs took median {st.median(x[3] for x in ev):.0f}s for {st.median(x[0] for x in ev):,.0f} input tokens; at 15 parallel (v15 luna_parallel) and the same seconds/job:')
    secs = st.median(x[3] for x in ev) * (st.median(sizes) / st.median(x[0] for x in ev)) ** 0.5
    print(f'  ~{secs:.0f}s/job (sqrt-scaled to packet size) -> {len(sizes)*secs/15/3600:,.0f} h wall at 15 parallel; {len(sizes)*st.median(x[3] for x in ev)/15/3600:,.0f} h unscaled')
