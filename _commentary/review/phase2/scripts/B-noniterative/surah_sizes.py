"""Input size of the surah-level reading (S-reading) per surah, to decide windowing for long surahs.

S-reading input (per surah or per window): surah text + the channel review (existing chains, grounded/extended,
never rediscovered) + HFT traces compacted to 'ref word -> root Bnnn (role)' lines + a branch-image table of every
root in the surah (image + Turkish gloss + kind; no phrases).
Printed: ayat, text chars, review chars, compact HFT chars, branch-table chars, est tokens (1.0 ch/tok for vocalised
text, 1.55 otherwise), and the number of windows needed at a ~110k-token budget per S call (Phase 1: thinking falls
only above ~150k tokens; the budget keeps a margin).
"""
import os, json, glob, sys
import load

QD = load.QD
LA = "/Volumes/OZTURK/_projects/latent_activation/focus_trace/runs"
BUDGET = 110_000


def review_chars(s):
    f = f"{QD}/data/analysis/channels/network-v3/s{s:03d}/review/reader_a_pilot.md"
    return len(open(f, encoding="utf-8").read()) if os.path.exists(f) else 0


def hft_compact_chars(s):
    n = 0
    files = glob.glob(f"{LA}/s{s}/readers/reader_hft_a/*.focus_trace.json")
    for f in files:
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        # walk every activation step-like dict with root/branch/role
        stack = [d]
        while stack:
            x = stack.pop()
            if isinstance(x, dict):
                if "branch_id" in x and ("role" in x or "role_sentence" in x):
                    role = str(x.get("role") or x.get("role_sentence") or "")
                    n += len(str(x.get("source_ref", ""))) + 12 + min(len(role), 140)
                stack.extend(x.values())
            elif isinstance(x, list):
                stack.extend(x)
    return n, len(files)


def branch_table_chars(s):
    roots = set()
    for i in range(1, load.surah_len(s) + 1):
        roots |= set(load.ayah_roots(f"{s}:{i}"))
    n = 0
    bbr = load.branches_by_root()
    nb = 0
    for r in roots:
        for b in bbr.get(r, []):
            if b["qac_attested"] == "yes":
                n += len(r) + 6 + len(b["image"]) + len(b["tr_gloss"]) + 18
                nb += 1
    return n, len(roots), nb


if __name__ == "__main__":
    surahs = [int(x) for x in sys.argv[1:]] or [1, 2, 4, 5, 12, 18, 29, 36, 55, 100, 103]
    q = load.quran()
    print("surah | ayat | text | review | hft (files) | branch table (roots/branches) | est tokens | windows @110k")
    for s in surahs:
        na = load.surah_len(s)
        text = sum(len(q[f"{s}:{i}"]) for i in range(1, na + 1))
        rv = review_chars(s)
        hc, hf = hft_compact_chars(s)
        bt, nr, nb = branch_table_chars(s)
        tok = int(text / 1.0 + (rv + hc + bt) / 1.55)
        win = max(1, -(-tok // BUDGET))
        print(f"{s} | {na} | {text} | {rv} | {hc} ({hf}) | {bt} ({nr}/{nb}) | {tok} | {win}")
