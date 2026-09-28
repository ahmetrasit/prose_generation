#!/usr/bin/env python3
"""Q2a mechanical signals (HEURISTICS): which dictionary branches (01_dictionary.md) surface in which runs.

Signal A (Arabic script): a branch's distinctive Arabic tokens (in its image/src fields, in no other branch of the
  file, not in context.md) found in the run text. A_strict = at least one such token that never occurs in the Quran.
Signal B (Turkish gloss): the branch's Turkish gloss content-word stems (5-letter prefixes, not present in context.md)
  found in the run text; hit = all stems when the gloss has 1-2 content words, else at least 2.
Reads metrics.tsv (paths) written by metrics.py. No model calls.
"""
from __future__ import annotations

import csv
import itertools
import json
import re
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path("/Volumes/OZTURK/_projects/prose_generation")
V9 = ROOT / "_commentary" / "v9"
QURAN = Path("/Volumes/OZTURK/_projects/quran-data/data/text/quran-uthmani.tsv")

DIAC = re.compile(r"[ؐ-ًؚ-ٰٟۖ-ۭـ࣓-ࣿ]")
AR_WORD = re.compile(r"[ء-يٱ-ۓۺ-ۿؐ-ًؚ-ٰٟۖ-ۭـ]+")
MAP = str.maketrans({"أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ى": "ي", "ة": "ه", "ؤ": "و", "ئ": "ي", "ۥ": "", "ۦ": ""})
AR_STOP = {"الذي", "التي", "الذين", "هذا", "هذه", "ذلك", "كان", "يقال", "قال", "اذا", "على", "الي", "عن", "من", "في",
           "مثل", "كل", "بعض", "غير", "ليس", "اي", "هو", "هي", "به", "له", "لها", "ما", "لا", "ان", "او", "ثم", "قد",
           "فلان", "فلانا", "شيء", "الشيء", "شي", "منه", "فيه", "عليه", "كذا", "وهو", "وهي", "والجمع", "جمع", "واحد",
           "الواحد", "يكون", "تقول", "ويقال", "اسم", "ايضا", "الامر", "امر"}


def norm(w: str) -> str:
    w = DIAC.sub("", w).translate(MAP)
    w = re.sub(r"[^ء-ي]", "", w)
    if len(w) > 3 and w[0] in "وف":
        w2 = w[1:]
        if w2.startswith("ال") or len(w2) >= 3:
            w = w2
    for p in ("بال", "كال", "فال", "وال", "لل"):
        if w.startswith(p) and len(w) > len(p) + 2:
            w = w[len(p):]
            break
    else:
        if w.startswith("ال") and len(w) > 4:
            w = w[2:]
    return w


def ar_tokens(text: str) -> set[str]:
    out = set()
    for m in AR_WORD.finditer(text):
        t = norm(m.group(0))
        if len(t) >= 3 and t not in AR_STOP:
            out.add(t)
    return out


TR_FOLD = str.maketrans({"İ": "i", "I": "ı", "Â": "a", "â": "a", "Î": "i", "î": "i", "Û": "u", "û": "u"})
TR_STOP = {"bir", "olan", "olarak", "şey", "şeyi", "kişi", "kimse", "veya", "ile", "gibi", "için", "özel", "yapı",
           "biçim", "biçimde", "durum", "türlü", "ayrı", "başka", "kendi", "birinin", "birine", "birini", "yer",
           "yeri", "olma", "olmak", "etme", "etmek", "yapma", "yapmak", "hale", "anlam", "anlamı", "çeşitli",
           "belirli", "kullanım", "kalıp", "kalıplaşmış", "genel", "tür", "türü", "bağlı", "ilgili", "gelme",
           "getirme", "verme", "alma", "kılma", "düşme", "tutma", "çıkma", "ortaya", "kadar", "üzere", "karşı",
           "doğru", "arası", "arasında", "üzerinde", "içinde", "dışında", "sonra", "önce", "daha", "çok", "az"}


def tr_words(text: str) -> list[str]:
    t = text.translate(TR_FOLD).lower()
    return re.findall(r"[a-zçğıöşü]+", t)


def tr_stems(text: str) -> set[str]:
    return {w[:5] for w in tr_words(text) if len(w) >= 4}


QVOCAB = set()
for line in QURAN.read_text(encoding="utf-8").splitlines():
    if "|" in line:
        QVOCAB |= ar_tokens(line.split("|", 1)[1])


def parse_dict(path: Path):
    branches = []
    root = None
    echo = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            root = line[3:].split(" (")[0]
            echo = "ECHO" in line
            continue
        m = re.match(r"- \*\*(B\d+)\*\* (.*)", line)
        if not m or root is None:
            continue
        fields = [f.strip() for f in m.group(2).split(" | ")]
        gloss = fields[0]
        image = fields[1] if len(fields) > 1 else ""
        src = next((f[4:] for f in fields if f.startswith("src:")), "")
        branches.append({"id": f"{root} {m.group(1)}", "echo": echo, "gloss": gloss, "image": image,
                         "src": src, "tok": ar_tokens(image + " " + src)})
    cnt = defaultdict(int)
    for b in branches:
        for t in b["tok"]:
            cnt[t] += 1
    return branches, cnt


rows = list(csv.DictReader(open(HERE / "metrics.tsv", encoding="utf-8"), delimiter="\t"))
DICT_V9 = {"v9:w10-opus-dict", "v9:w10-opus-dslim", "v9:w10-opus-dhft", "v9:w10-opus-ledger", "v9:v11-script",
           "v9:v11-luna"}
COLD = {"v9:w10-opus-cold", "v9:w10-opus-cold2"}

ALL_STEMS = []
for r in rows:
    if r["path"] and r.get("words"):
        ALL_STEMS.append(tr_stems(Path(r["path"]).read_text(encoding="utf-8", errors="replace")))
DF = defaultdict(int)
for st in ALL_STEMS:
    for x in st:
        DF[x] += 1
NRUNS = len(ALL_STEMS)
RARE = 0.10  # a stem counts for B_rare only if it occurs in <=10% of all run texts

branch_rows = []
summary = []
pairs = []
for ayah in dict.fromkeys(r["ayah"] for r in rows):
    s, a = ayah.split(":")
    sa = f"{s}_{a}"
    dpath = V9 / "input" / "v2" / f"s{int(s):03d}" / sa / "01_dictionary.md"
    ctx = (V9 / "lines" / "work" / sa / "context.md").read_text(encoding="utf-8")
    ctx_ar = ar_tokens(ctx)
    ctx_tr = tr_stems(ctx)
    branches, cnt = parse_dict(dpath)
    for b in branches:
        b["dist"] = {t for t in b["tok"] if cnt[t] == 1 and t not in ctx_ar}
        b["dist_nq"] = {t for t in b["dist"] if t not in QVOCAB}
        cw = [w for w in tr_words(b["gloss"]) if len(w) >= 4 and w not in TR_STOP]
        b["stems"] = list(dict.fromkeys(w[:5] for w in cw if w[:5] not in ctx_tr))
        b["rare"] = [x for x in b["stems"] if DF.get(x, 0) <= RARE * NRUNS]
    runs = {}
    for r in rows:
        if r["ayah"] == ayah and r["path"] and r.get("words"):
            t = Path(r["path"]).read_text(encoding="utf-8", errors="replace")
            runs[r["run"]] = (ar_tokens(t), tr_stems(t), int(r["words"]))

    def hits(run, sig):
        at, ts, _ = runs[run]
        out = set()
        for b in branches:
            if sig == "A_strict" and b["dist_nq"] & at:
                out.add(b["id"])
            elif sig == "A_loose" and b["dist"] & at:
                out.add(b["id"])
            elif sig == "B_rare" and b["rare"]:
                n = sum(1 for st in b["rare"] if st in ts)
                need = len(b["rare"]) if len(b["rare"]) <= 3 else 3
                if n >= need:
                    out.add(b["id"])
            elif sig == "B_gloss" and b["stems"]:
                n = sum(1 for st in b["stems"] if st in ts)
                need = len(b["stems"]) if len(b["stems"]) <= 2 else 2
                if n >= need:
                    out.add(b["id"])
        return out

    H = {run: {sig: hits(run, sig) for sig in ("A_strict", "A_loose", "B_rare", "B_gloss")} for run in runs}
    for b in branches:
        for run in runs:
            pass
    # per-branch table (v9 cold/dict arms and group unions)
    cold_runs = [r for r in runs if r in COLD]
    dict_runs = [r for r in runs if r in DICT_V9]
    other_runs = [r for r in runs if r not in COLD]
    for b in branches:
        rec = {"ayah": ayah, "branch": b["id"], "echo": int(b["echo"]), "gloss": b["gloss"][:80],
               "n_dist_tokens": len(b["dist"]), "n_dist_nonquranic": len(b["dist_nq"]),
               "gloss_stems": " ".join(b["stems"]), "rare_stems": " ".join(b["rare"])}
        for sig in ("A_strict", "A_loose", "B_rare", "B_gloss"):
            rec[f"cold_{sig}"] = ",".join(r.split(":", 1)[1] for r in cold_runs if b["id"] in H[r][sig])
            rec[f"dictv9_{sig}"] = ",".join(r.split(":", 1)[1] for r in dict_runs if b["id"] in H[r][sig])
            rec[f"any_other_{sig}"] = len([r for r in other_runs if b["id"] in H[r][sig]])
        mt = set()
        for r in dict_runs:
            mt |= (b["dist_nq"] & runs[r][0])
        rec["dict_matched_nonquranic_tokens"] = " ".join(sorted(mt))[:120]
        mc = set()
        for r in cold_runs:
            mc |= (b["dist_nq"] & runs[r][0])
        rec["cold_matched_nonquranic_tokens"] = " ".join(sorted(mc))[:120]
        branch_rows.append(rec)
    # summary per ayah and signal
    for sig in ("A_strict", "A_loose", "B_rare", "B_gloss"):
        C = set().union(*(H[r][sig] for r in cold_runs)) if cold_runs else set()
        D = set().union(*(H[r][sig] for r in dict_runs)) if dict_runs else set()
        O = set().union(*(H[r][sig] for r in other_runs)) if other_runs else set()
        summary.append({"ayah": ayah, "signal": sig, "branches": len(branches),
                        "cold_runs": len(cold_runs), "dict_v9_runs": len(dict_runs), "other_runs": len(other_runs),
                        "cold_hits": len(C), "dictv9_hits": len(D), "dictv9_only": len(D - C), "cold_only": len(C - D),
                        "both": len(C & D), "any_noncold_hits": len(O), "noncold_only_vs_cold": len(O - C),
                        "cold_only_vs_all_noncold": len(C - O),
                        "dictv9_only_ids": " ; ".join(sorted(D - C))[:400],
                        "cold_only_ids": " ; ".join(sorted(C - D))[:400]})
    # single-run pairs: cold vs each other run, per signal
    for c in cold_runs:
        for o in runs:
            if o == c:
                continue
            for sig in ("A_strict", "A_loose", "B_rare", "B_gloss"):
                X, Y = H[c][sig], H[o][sig]
                u = X | Y
                pairs.append({"ayah": ayah, "cold": c, "other": o, "signal": sig, "cold_hits": len(X),
                              "other_hits": len(Y), "shared": len(X & Y), "other_only": len(Y - X),
                              "cold_only": len(X - Y), "jaccard": round(len(X & Y) / len(u), 3) if u else "",
                              "cold_words": runs[c][2], "other_words": runs[o][2]})


def dump(name, recs):
    if not recs:
        return
    with open(HERE / name, "w", encoding="utf-8") as fh:
        cols = list(recs[0].keys())
        fh.write("\t".join(cols) + "\n")
        for r in recs:
            fh.write("\t".join(str(r[c]).replace("\t", " ") for c in cols) + "\n")


dump("q2a_branches.tsv", branch_rows)
dump("q2a_summary.tsv", summary)
dump("q2a_pairs.tsv", pairs)
print(len(branch_rows), "branch rows;", len(summary), "summary rows;", len(pairs), "pair rows")
