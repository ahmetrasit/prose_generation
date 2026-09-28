#!/usr/bin/env python3
"""Unified per-ayah cost model for the five proposals, two output scenarios:
  P = the proposal's own output assumption;
  R = recorded shape for the call's condition (c03): fed + memory-permitted synthesis calls produced median 50.6k output
      (32.7k thinking) [FED-PERM, n=16], cold (permitted, context only) 20.3k short / 52.8-60.2k long; output grows
      ~764 tokens per ayah word (cold-arm fit). R uses: short 40k, medium 48k, long 60k, extreme 110k for fed+permitted
      single-call synthesis; B's R_mem keeps the cold arm (short 20k, medium 30k, long 56k, extreme 110k).
Rates: claude -p input as 1-hour cache write $8/M, output $20/M, cache read $0.20/M (v15 raw.json reconciles exactly).
Batch (claude-api skill): 50% of every token incl. cache: input $2/M, output $10/M, cache read $0.10/M, 1h write $4/M.
CLI 64K per-response cap (v13 HANDOFF; v11 REVIEW: each extra response re-bills ~$0.5): responses over 64k are
charged +1 continuation = 64k*$8/M + input*$0.2/M per extra 64k block.
Inputs are calibrated tokens (c02) where a proposal built the packet; otherwise stated assumptions.
Classes: short = short surah, short ayah (Fatiha/S100); medium = long-surah ayah <20 words (29:38, 18:86/96 class);
long = 4:34/5:6 class (40-61 words); extreme = 2:282 class (128 words; S2 has no HFT/v5)."""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
CAP = 64000
def cli(i, o, cr=0):
    extra = max(0, -(-o // CAP) - 1)  # continuation responses
    return i * 8e-6 + o * 20e-6 + cr * 0.2e-6 + extra * (CAP * 8e-6 + i * 0.2e-6)
def bat(i, o, cr=0, cw1h=0):
    return i * 2e-6 + o * 10e-6 + cr * 0.1e-6 + cw1h * 4e-6
CL = ['short', 'medium', 'long', 'extreme']
R_FED = dict(short=40000, medium=48000, long=60000, extreme=110000)
R_COLD = dict(short=20000, medium=30000, long=56000, extreme=110000)
res = {}
def show(name, rows):
    res[name] = rows
    print(f'\n== {name}')
    print(f'{"class":8s} {"CLI P":>7s} {"CLI R":>7s} {"Batch P":>8s} {"Batch R":>8s}  notes')
    for c in CL:
        r = rows[c]; print(f'{c:8s} {r[0]:7.2f} {r[1]:7.2f} {r[2]:8.2f} {r[3]:8.2f}  {r[4]}')
# ---------------- A: S2 + shares (S1, S5, repair) ----------------
digest = dict(short=10000, medium=14300, long=36700, extreme=45000)   # c02 calibrated; extreme unmeasured (A max 41.9k)
ctx = dict(short=3000, medium=8000, long=8000, extreme=8000)            # surah/window text (A: ~8k)
s1map = 12000                                                            # v15 window JSON output ~12-17k tokens (c: raw.json)
A = {}
for c in CL:
    i_p = 2500 + ctx[c] + digest[c] * 1.29  # A's own input: bytes/2.0 (overstates by 29%), no S1 map
    i_r = 2500 + ctx[c] + digest[c] + s1map
    shares_cli = 0.12 + 0.12 + 0.09   # S1 window share (pericope ~17 ayat, $1.3-2.1/window; short surahs $1.0-1.6/7-11 ayat), S5 share incl. hierarchy, repair at 30% x $0.3
    shares_bat = shares_cli / 2
    p_cli = cli(i_p, 22000) + shares_cli; r_cli = cli(i_r, R_FED[c]) + shares_cli
    p_bat = bat(i_p - 8000, 22000, cr=8000) + shares_bat; r_bat = bat(i_r - 8000, R_FED[c], cr=8000) + shares_bat
    A[c] = (p_cli, r_cli, p_bat, r_bat, f'S2 in P {i_p/1e3:.0f}k / R {i_r/1e3:.0f}k')
show('A-v5-step (S2 + S1/S5/repair shares)', A)
# ---------------- B: S-reading share + R_mem + R_lex + integrate + challenge + surah share ----------------
mem_in = dict(short=8000, medium=35000, long=45000, extreme=65000)     # whole surah context (S2 text 60k, c04)
lex_in = dict(short=20000, medium=31000, long=118000, extreme=118000)  # c02 supply (random median 24k; 5:6 light ~111k) + brief + slice; extreme at B's 110k budget
lex_out_p = dict(short=22000, medium=30000, long=43000, extreme=43000)
mem_out_p = dict(short=19000, medium=30000, long=56000, extreme=56000)
int_in = dict(short=26500, medium=32000, long=45500, extreme=50000); int_out = dict(short=30000, medium=34000, long=38000, extreme=45000)
chal_out = dict(short=18000, medium=20000, long=22000, extreme=24000)
share = dict(short=0.39, medium=0.15, long=0.15, extreme=0.15)          # B's S-reading + surah shares (short surah heavier)
B = {}
for c in CL:
    # P: B's own challenge pricing: prior prefix + output as cache read
    chal_p_cli = cli(2000 + 0, chal_out[c], cr=int_in[c] + int_out[c])
    # R: claude -p resume re-ingests the integrator's output (thinking preserved on Opus 5.5) as a new 1h write
    chal_r_cli = cli(4000 + int_out[c], chal_out[c], cr=int_in[c])
    chal_p_bat = bat(2000, chal_out[c], cr=int_in[c] + int_out[c])
    chal_r_bat = bat(4000 + int_out[c], chal_out[c], cr=int_in[c])        # second batch request; prefix hit best-effort
    p_cli = cli(mem_in[c], mem_out_p[c]) + cli(lex_in[c], lex_out_p[c]) + cli(int_in[c], int_out[c]) + chal_p_cli + share[c]
    r_cli = cli(mem_in[c], R_COLD[c]) + cli(lex_in[c], R_FED[c]) + cli(int_in[c], int_out[c]) + chal_r_cli + share[c]
    p_bat = bat(mem_in[c], mem_out_p[c]) + bat(lex_in[c], lex_out_p[c]) + bat(int_in[c], int_out[c]) + chal_p_bat + share[c] / 2
    r_bat = bat(mem_in[c], R_COLD[c]) + bat(lex_in[c], R_FED[c]) + bat(int_in[c], int_out[c]) + chal_r_bat + share[c] / 2
    B[c] = (p_cli, r_cli, p_bat, r_bat, f'5 Opus calls; challenge P ${chal_p_cli:.2f} vs R ${chal_r_cli:.2f} (CLI)')
show('B-noniterative primary', B)
BF1 = {}
for c in CL:
    chal_r_cli = cli(4000 + R_FED[c], chal_out[c], cr=lex_in[c])
    p = cli(lex_in[c], lex_out_p[c]) + 0.8 * cli(2000, chal_out[c], cr=lex_in[c] + lex_out_p[c]) + share[c]
    r = cli(lex_in[c], R_FED[c]) + chal_r_cli + share[c]
    pb = bat(lex_in[c], lex_out_p[c]) + 0.8 * bat(2000, chal_out[c], cr=lex_in[c] + lex_out_p[c]) + share[c] / 2
    rb = bat(lex_in[c], R_FED[c]) + bat(4000 + R_FED[c], chal_out[c], cr=lex_in[c]) + share[c] / 2
    BF1[c] = (p, r, pb, rb, 'R_lex writes + challenge')
show('B fallback F1', BF1)
# ---------------- supply layers hosted in ONE permitted synthesis call (C1, C2, D) ----------------
host_ctx = dict(short=3500, medium=15000, long=38000, extreme=12000)   # brief + surah text (whole long surah: S4 37k) / S2 window
packs = {
    'C1 push': (dict(short=2000, medium=12000, long=31000, extreme=50000), dict(short=1500, medium=9000, long=23000, extreme=37000)),  # (calibrated, C1's chars/2.2)
    'C2 sheet': (dict(short=4800, medium=22500, long=61000, extreme=101400), dict(short=3000, medium=13400, long=36000, extreme=60300)),
    'D KA packet (incl. surah)': (dict(short=15500, medium=46400, long=86900, extreme=80900), dict(short=15500, medium=46400, long=86900, extreme=80900)),
}
out_p = {'C1 push': dict(short=20000, medium=25000, long=45000, extreme=45000),   # C1 V3 assumes cold-arm median $0.44/call
         'C2 sheet': dict(short=30000, medium=40000, long=60000, extreme=60000),  # C2: 30-60k
         'D KA packet (incl. surah)': dict(short=20000, medium=32000, long=45000, extreme=45000)}  # D: 20-45k
for name, (cal_p, own_p) in packs.items():
    rows = {}
    for c in CL:
        base = 0 if name.startswith('D') else host_ctx[c]
        i_own = base + own_p[c]; i_cal = base + cal_p[c]
        rows[c] = (cli(i_own, out_p[name][c]), cli(i_cal, R_FED[c]), bat(i_own, out_p[name][c]), bat(i_cal, R_FED[c]),
                   f'host in own {i_own/1e3:.0f}k / calibrated {i_cal/1e3:.0f}k; packet alone CLI ${cal_p[c]*8e-6:.2f}, Batch ${cal_p[c]*2e-6:.3f}')
    show(f'{name} hosted in one synthesis call', rows)
# weighted whole-Quran production (Batch R) using B's class counts: 930 short, 4262 medium, 1044 long; 16 of the long as extreme
W = dict(short=930, medium=4262, long=1044 - 16, extreme=16)
print('\nWhole-Quran production (Batch), weighted by class counts (930/4262/1028/16):')
for name, rows in res.items():
    p = sum(W[c] * rows[c][2] for c in CL); r = sum(W[c] * rows[c][3] for c in CL)
    print(f'  {name:48s} P ${p:8,.0f} (${p/6236:.2f}/ayah)   R ${r:8,.0f} (${r/6236:.2f}/ayah)')
json.dump({k: {c: v[c][:4] for c in CL} for k, v in res.items()}, open(HERE / 'out_c07_cost_model.json', 'w'), indent=1)
