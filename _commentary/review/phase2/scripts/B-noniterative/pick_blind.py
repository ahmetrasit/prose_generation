"""Pick blind validation ayat, deterministically (seed 20260928), that no version tuned on and that have:
  - v5 editorial prose (the North Star's bar: 'materially exceed v5'; no run needed on the v5 side)
  - a channel review (for the S-reading)
  - HFT traces (optional, reported)
Excluded: every surah any v9-v15 prompt/test touched or the North Star names (1, 2, 4, 5, 18, 29, 96, 100, 103) and
all S1-derived material. Strata: a long surah pericope (3 consecutive-window ayat, one of them >= 20 words), and a
short surah (2 ayat), so that one S-reading per stratum serves all of its ayat.
"""
import os, glob, random, re
import load

C = load.PG + "/_commentary/v5/editorial"
QD = load.QD
LA = "/Volumes/OZTURK/_projects/latent_activation/focus_trace/runs"
USED = {1, 2, 4, 5, 18, 29, 96, 100, 103}
random.seed(20260928)


def v5_ayat(s):
    out = set()
    for d in glob.glob(f"{C}/s{s:03d}-*/s{s:03d}/*"):
        m = re.search(r"/(\d+)_(\d+)$", d)
        if m and glob.glob(d + "/*.prose.editorial.tr.md"):
            out.add(f"{int(m.group(1))}:{int(m.group(2))}")
    return out


def has_review(s):
    return os.path.exists(f"{QD}/data/analysis/channels/network-v3/s{s:03d}/review/reader_a_pilot.md")


def has_hft(s):
    return bool(glob.glob(f"{LA}/s{s}/readers/reader_hft_a/*.focus_trace.json"))


_, by = load.words()
cands = {}
for s in range(1, 115):
    if s in USED:
        continue
    av = v5_ayat(s)
    if av and has_review(s):
        cands[s] = av
long_s = sorted(s for s in cands if load.surah_len(s) > 40)
short_s = sorted(s for s in cands if load.surah_len(s) <= 40)
print("candidate long surahs:", long_s)
print("candidate short surahs:", short_s)

s = random.choice(long_s)
av = sorted(cands[s], key=lambda r: int(r.split(":")[1]))
longs = [r for r in av if len(by.get(r, [])) >= 20]
anchor = random.choice(longs)
a = int(anchor.split(":")[1])
near = [r for r in av if r != anchor and abs(int(r.split(":")[1]) - a) <= 5]
pick_long = [anchor] + random.sample(near, 2)
s2 = random.choice(short_s)
pick_short = random.sample([r for r in sorted(cands[s2], key=lambda r: int(r.split(":")[1])) if len(by.get(r, [])) >= 6], 2)  # >= 6 words: enough words for coalitions
for r in pick_long + pick_short:
    ss = int(r.split(":")[0])
    print(f"blind {r}: {len(by[r])} words; surah {ss} ({load.surah_len(ss)} ayat); v5 prose yes; review yes; HFT {'yes' if has_hft(ss) else 'no'}")
