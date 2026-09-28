"""Per-ayah cost of design B and its fallbacks, from recorded token counts (Phase 1 metrics.tsv) and the measured
supply sizes (supply.py). No model calls.

Rates (task brief): claude -p: output $20/M, input billed as 1-hour cache write $8/M, cache read $0.20/M.
API Batch: half of list: input $2/M, output $10/M, cache read $0.20/M (list $4/$20; cache read 0.1x, halved).
"""
import csv, statistics, os
P1 = "/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase1/dilution/metrics.tsv"
rows = list(csv.DictReader(open(P1), delimiter="\t"))


def num(x):
    try:
        return float(str(x).split()[0])
    except Exception:
        return None


def arm(run, ayat):
    out = [r for r in rows if r["run"] == run and r["ayah"] in ayat]
    return [(num(r["cache_write"]) or 0) + (num(r["cache_read"]) or 0) for r in out], \
           [num(r["output_tokens"]) for r in out], [num(r["thinking_tokens"]) for r in out], \
           [num(r["words"]) for r in out]


SHORT = {"1:1", "1:2", "1:3", "1:4", "1:5", "1:6", "1:7", "100:1", "100:6", "100:10", "103:1", "103:2", "103:3"}
LONG = {"4:34", "5:6", "18:86", "18:96"}
rep = []
for name, run in (("R_mem (cold arm)", "v9:w10-opus-cold"), ("R_lex proxy (dict arm)", "v9:w10-opus-dict")):
    for lab, ay in (("short", SHORT), ("long", LONG)):
        i, o, t, w = arm(run, ay)
        if o:
            rep.append(f"{name} {lab}: n={len(o)} input median {statistics.median(i):.0f}, output median "
                       f"{statistics.median(o):.0f} (thinking {statistics.median(t):.0f}), words median {statistics.median(w):.0f}")
# prose tokens per word (output minus thinking) in cold arms
ptw = [(num(r["output_tokens"]) - num(r["thinking_tokens"])) / num(r["words"]) for r in rows
       if r["run"] in ("v9:w10-opus-cold", "v9:w10-opus-cold2") and num(r["words"])]
rep.append(f"Turkish reading prose: {statistics.median(ptw):.2f} output tokens per word (median over cold arms)")

CLI = dict(inp=8.0, out=20.0, cr=0.20)
BATCH = dict(inp=2.0, out=10.0, cr=0.20)


def cost(inp, out, rates, cr=0):
    return (inp * rates["inp"] + out * rates["out"] + cr * rates["cr"]) / 1e6


# Scenario token assumptions (short ayah = Fatiha/S100 class; long = 4:34/5:6/18:86 class)
S = {
    "short": dict(mem_in=8_000, mem_out=19_000, lex_in=20_000, lex_out=22_000,
                  reading_prose=8_000,  # tokens per reading passed to the integrator
                  ctx=4_000, brief=2_500, slice_=4_000, int_out=30_000, chal_out=18_000,
                  s_share=0.23 / 1, s_share_batch=0.12, surah_comm_share=0.16),
    "long": dict(mem_in=45_000, mem_out=56_000, lex_in=90_000, lex_out=43_000,
                 reading_prose=15_000, ctx=8_000, brief=2_500, slice_=5_000, int_out=38_000, chal_out=22_000,
                 s_share=0.11, s_share_batch=0.06, surah_comm_share=0.04),
}
lines = rep + [""]
lines.append("design | ayah class | claude -p (tests) | API Batch (production)")
for cls, a in S.items():
    int_in = 2 * a["reading_prose"] + a["ctx"] + a["brief"] + a["slice_"]
    # challenge turn: same session, prefix cached (cache read) + script diff (~2k) + revised commentary
    chal_in, chal_cr = 2_000, int_in + a["int_out"]
    calls = {
        "R_mem": (a["mem_in"], a["mem_out"], 0),
        "R_lex": (a["lex_in"] + a["brief"], a["lex_out"], 0),
        "integrate": (int_in, a["int_out"], 0),
        "challenge": (chal_in, a["chal_out"], chal_cr),
    }
    cli = {k: cost(i, o, CLI, c) for k, (i, o, c) in calls.items()}
    bat = {k: cost(i, o, BATCH, c) for k, (i, o, c) in calls.items()}
    prim_cli = sum(cli.values()) + a["s_share"] + a["surah_comm_share"]
    prim_bat = sum(bat.values()) + a["s_share_batch"] + a["surah_comm_share"] / 2
    f1_cli = cli["R_lex"] + cli["challenge"] * 0.8 + a["s_share"] + a["surah_comm_share"]
    f1_bat = bat["R_lex"] + bat["challenge"] * 0.8 + a["s_share_batch"] + a["surah_comm_share"] / 2
    lines.append(f"PRIMARY (S-reading share + R_mem + R_lex + integrate + challenge + surah commentary share) | {cls} | "
                 f"${prim_cli:.2f} | ${prim_bat:.2f}")
    lines.append("   per call (cli): " + ", ".join(f"{k} ${v:.2f}" for k, v in cli.items()))
    lines.append(f"FALLBACK F1 (single free reading R_lex+memory, with surah slice, + challenge) | {cls} | ${f1_cli:.2f} | ${f1_bat:.2f}")
txt = "\n".join(lines)
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cost_model.txt"), "w").write(txt + "\n")
print(txt)
