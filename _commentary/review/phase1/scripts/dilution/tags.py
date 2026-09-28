#!/usr/bin/env python3
"""Classify every Arabic quotation tag of every run by where its Arabic can be found (loose match, verify_ar-style
folding): Quran text, the ayah's 01_dictionary.md, context.md, or nowhere (memory). Read-only; own reimplementation
of _commentary/v9/verify_ar.py's folding so no repo code is executed."""
from __future__ import annotations

import csv
import re
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
V9 = Path("/Volumes/OZTURK/_projects/prose_generation/_commentary/v9")
QURAN = Path("/Volumes/OZTURK/_projects/quran-data/data/text/quran-uthmani.tsv")
TAG = re.compile(r"\{\{?\s*ar\s*:\s*([^{}|\n]*?)\s*(?:,\s*(?:tr|gloss|src|source)\s*:|\||\}\}?)")
FOLD = str.maketrans({"ٱ": "ا", "أ": "ا", "إ": "ا", "آ": "ا", "ى": "ي", "ـ": None, "ة": "ه"})


def loose(t: str) -> str:
    t = unicodedata.normalize("NFC", t)
    out = []
    for ch in t:
        if unicodedata.category(ch) in ("Mn", "Cf") or ch in "ـۥۦۣ۞۩":
            continue
        out.append(ch)
    s = "".join(out).translate(FOLD)
    s = re.sub(r"[^ء-ي ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


QBLOB = loose("\n".join(l.split("|", 1)[1] for l in QURAN.read_text(encoding="utf-8-sig").splitlines() if "|" in l))

rows = list(csv.DictReader(open(HERE / "metrics.tsv", encoding="utf-8"), delimiter="\t"))
out = []
examples = []
cache = {}
for r in rows:
    if not r["path"] or not r.get("words"):
        continue
    s, a = r["ayah"].split(":")
    sa = f"{s}_{a}"
    if sa not in cache:
        d = V9 / "input" / "v2" / f"s{int(s):03d}" / sa / "01_dictionary.md"
        c = V9 / "lines" / "work" / sa / "context.md"
        cache[sa] = (loose(d.read_text(encoding="utf-8")), loose(c.read_text(encoding="utf-8")))
    dic, ctx = cache[sa]
    text = Path(r["path"]).read_text(encoding="utf-8", errors="replace")
    n = {"tags": 0, "quran": 0, "dict_only": 0, "context_only": 0, "memory": 0, "short_skipped": 0}
    mem = []
    dictq = []
    for m in TAG.finditer(text):
        ar = loose(m.group(1))
        if not ar:
            continue
        n["tags"] += 1
        if len(ar.replace(" ", "")) < 3:
            n["short_skipped"] += 1
            continue
        if ar in QBLOB:
            n["quran"] += 1
        elif ar in dic:
            n["dict_only"] += 1
            dictq.append(m.group(1).strip())
        elif ar in ctx:
            n["context_only"] += 1
        else:
            n["memory"] += 1
            mem.append(m.group(1).strip())
    out.append({"ayah": r["ayah"], "run": r["run"], **n,
                "dict_examples": " ; ".join(dictq[:6])[:300], "memory_examples": " ; ".join(mem[:8])[:400]})

with open(HERE / "tags.tsv", "w", encoding="utf-8") as fh:
    cols = list(out[0].keys())
    fh.write("\t".join(cols) + "\n")
    for o in out:
        fh.write("\t".join(str(o[c]).replace("\t", " ") for c in cols) + "\n")
print(len(out), "rows")
