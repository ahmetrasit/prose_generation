"""Does a stance-diverse ensemble of single Opus readings grow the union more than a replicate does?

Data: Phase 1 dilution refs.json (cited Quran refs per run, focus excluded where noted) and q2a_branches.tsv
(dictionary-branch hit signals for cold and dict v9 arms). No model runs.

Measures per ayah:
  - |A|, |B|, |A u B|, gain = |A u B| / max(|A|,|B|), Jaccard
  - for 4:34: replicate pair (cold, cold2) vs stance pairs (cold, dict), (cold, v15-nocap), (dict, v15-nocap), and the
    3-way stance union (cold, dict, v15-nocap) vs the replicate union.
  - Opus-only union across all single-call Opus configurations per ayah vs the best single run.
"""
import json, csv, itertools, collections, os
P1 = "/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase1/dilution"
refs = json.load(open(f"{P1}/refs.json"))
OUT = os.path.dirname(os.path.abspath(__file__))

by = collections.defaultdict(dict)
for k, v in refs.items():
    ayah, run = k.split("|", 1)
    by[ayah][run] = set(v) - {ayah}


def stats(a, b):
    u = a | b
    j = len(a & b) / len(u) if u else 0
    return len(a), len(b), len(u), round(len(u) / max(len(a), len(b), 1), 2), round(j, 2)


lines = []
out = []
# 1. replicate vs stance on 4:34
r = by["4:34"]
pairs = [("v9:w10-opus-cold", "v9:w10-opus-cold2", "replicate"),
         ("v9:w10-opus-cold", "v9:w10-opus-dict", "stance: memory vs dictionary"),
         ("v9:w10-opus-cold2", "v9:w10-opus-dict", "stance: memory vs dictionary (rep2)"),
         ("v9:w10-opus-cold", "v15:out-nocap", "stance: memory vs v15 (chain/lexicon pipeline)"),
         ("v9:w10-opus-dict", "v15:out-nocap", "stance: dictionary vs v15")]
lines.append("## 4:34: replicate vs stance-diverse pairs (cited refs, focus excluded)")
lines.append("pair | kind | |A| | |B| | |AuB| | gain | Jaccard")
for a, b, kind in pairs:
    s = stats(r[a], r[b])
    lines.append(f"{a} + {b} | {kind} | " + " | ".join(map(str, s)))
    out.append(["4:34", a, b, kind, *s])
rep = r["v9:w10-opus-cold"] | r["v9:w10-opus-cold2"]
tri = r["v9:w10-opus-cold"] | r["v9:w10-opus-dict"] | r["v15:out-nocap"]
lines.append(f"cold u cold2 (2 replicate calls): {len(rep)} refs; cold u dict u v15-nocap (3 stances): {len(tri)}; "
             f"cold u dict (2 stances): {len(r['v9:w10-opus-cold'] | r['v9:w10-opus-dict'])}")
lines.append(f"refs in the 3-stance union but in neither replicate: {len(tri - rep)}; in replicates but not 3-stance: "
             f"{len(rep - tri)}")

# 2. cold vs dict on every ayah that has both
lines.append("\n## cold (memory) vs dict (dictionary, 'only the supplied evidence') per ayah")
lines.append("ayah | |cold| | |dict| | |u| | gain | Jaccard")
for ayah in sorted(by, key=lambda x: tuple(map(int, x.split(":")))):
    rr = by[ayah]
    if "v9:w10-opus-cold" in rr and "v9:w10-opus-dict" in rr:
        s = stats(rr["v9:w10-opus-cold"], rr["v9:w10-opus-dict"])
        lines.append(f"{ayah} | " + " | ".join(map(str, s)))
        out.append([ayah, "cold", "dict", "stance", *s])

# 3. Opus-only single-call configurations: union vs best single
OPUS = ("v9:w10-opus", "v9:w10-opus-cold", "v9:w10-opus-cold2", "v9:w10-opus-dict", "v9:w10-opus-dslim",
        "v9:w10-opus-dhft", "v9:w10-opus-ledger", "v9:v11-script", "v9:v11-luna", "v11:out", "v12:out", "v15:out",
        "v15:out-nocap", "v13:out", "v13:out-v2")
lines.append("\n## all Opus configurations per ayah: best single run vs union (how much any one run misses)")
lines.append("ayah | n runs | best single (run) | union | best/union")
for ayah in sorted(by, key=lambda x: tuple(map(int, x.split(":")))):
    rr = {k: v for k, v in by[ayah].items() if k in OPUS}
    if len(rr) < 3:
        continue
    u = set().union(*rr.values())
    best = max(rr, key=lambda k: len(rr[k]))
    lines.append(f"{ayah} | {len(rr)} | {len(rr[best])} ({best}) | {len(u)} | {len(rr[best]) / len(u):.2f}")

# 4. dictionary-branch signals: cold vs dict (q2a_branches.tsv)
lines.append("\n## dictionary branches surfaced (q2a A_strict or B_rare): cold vs dict per ayah")
q = list(csv.DictReader(open(f"{P1}/q2a_branches.tsv", encoding="utf-8"), delimiter="\t"))
per = collections.defaultdict(lambda: [set(), set()])
for row in q:
    hit_c = bool(row["cold_A_strict"] or row["cold_B_rare"])
    hit_d = bool(row["dictv9_A_strict"] or row["dictv9_B_rare"])
    if hit_c:
        per[row["ayah"]][0].add(row["branch"])
    if hit_d:
        per[row["ayah"]][1].add(row["branch"])
lines.append("ayah | cold | dict | union | only cold | only dict")
tc = td = tu = 0
for ayah in sorted(per, key=lambda x: tuple(map(int, x.split(":")))):
    c, d = per[ayah]
    tc += len(c); td += len(d); tu += len(c | d)
    lines.append(f"{ayah} | {len(c)} | {len(d)} | {len(c | d)} | {len(c - d)} | {len(d - c)}")
lines.append(f"total | {tc} | {td} | {tu} |")

txt = "\n".join(lines)
open(os.path.join(OUT, "ensemble_union.txt"), "w").write(txt + "\n")
print(txt)
