"""Distribution of R_lex supply size over a seeded random sample of 120 ayat (full vs light branch index)."""
import random, os, statistics, importlib
import load
random.seed(7)
refs = random.sample(sorted(load.quran()), 120)
res = {}
for light in (False, True):
    os.environ["LIGHT"] = "1" if light else ""
    import supply; importlib.reload(supply)
    supply.OUTD = os.path.join(load.OUT, "supply_sample" + ("_light" if light else ""))
    os.makedirs(supply.OUTD, exist_ok=True)
    toks = [supply.build(r)[2] for r in refs]
    res[light] = toks
for light, toks in res.items():
    s = sorted(toks)
    print(f"{'light' if light else 'full '}: median {statistics.median(s):.0f} tokens, p90 {s[int(.9*len(s))]}, max {s[-1]}, "
          f"> 110k: {sum(t > 110_000 for t in s)} of {len(s)}")
