#!/usr/bin/env python3
"""Check every Arabic tag against its declared source: {ar:…, tr:…, gloss:…, source:…}.

`source` is a comma-delimited list; each item is an ayah (`S:A`) or a dictionary branch (`ص ل و B006`, the root in
Arabic letters with spaces, then the branch id). For each tag:
  exact       the Arabic occurs verbatim in one of the declared sources
  fixed       it occurs there once diacritics, Quranic marks, tatweel and alef/ya variants are ignored (--fix
              rewrites the tag with the exact source form)
  elsewhere   not in the declared sources but in another branch of the same root or elsewhere in the Quran
              (a wrong or incomplete source)
  missing     not found in any declared source, nor in the Quran, nor in the dictionary entries of its roots
  no-source   the tag has no source field
  bad-source  a source item that is neither S:A nor `root Bnnn` of a known root and branch
Usage: python3 _commentary/v11/verify_src.py READING [--fix]
Exit status 1 when missing, no-source or bad-source tags remain.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

V11 = Path(__file__).resolve().parent
sys.path.insert(0, str(V11.parent / "v9"))
from verify_ar import QURAN_TEXT, exact_span, loose  # noqa: E402

DICT_DIR = QURAN_TEXT.parents[1] / "dictionary" / "tr"
CARDS = QURAN_TEXT.parents[3] / "quran-slm" / "resources" / "source" / "corpus_branches_ar.tsv"
TAG_RE = re.compile(r"\{\s*ar\s*:\s*(?P<ar>[^{},\n]*?)\s*,\s*tr\s*:[^{}]*?gloss\s*:[^{}]*?"
                    r"(?:,\s*source\s*:\s*(?P<src>[^{}]*?))?\s*\}")
BRANCH_RE = re.compile(r"^(?P<root>[ء-ي](?: [ء-ي]){1,4})\s+(?P<b>B\d{3})$")


class Dictionary:
    def __init__(self) -> None:
        self.by_name: dict[str, list[str]] = defaultdict(list)
        import csv
        with CARDS.open(encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                rid, name = row["source_root_id"], row["surface_root"]
                if rid not in self.by_name[name]:
                    self.by_name[name].append(rid)
        self._e: dict[str, dict] = {}

    def entry(self, rid: str) -> dict:
        if rid not in self._e:
            p = DICT_DIR / f"{rid}_entry.json"
            self._e[rid] = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
        return self._e[rid]

    def texts(self, name: str, bid: str | None) -> list[str]:
        """Arabic-bearing text of one branch (bid) or of every branch of every root with this name."""
        out = []
        for rid in self.by_name.get(name, []):
            for b in self.entry(rid).get("branches", []):
                if bid is None or b.get("branch_ref", "").endswith("/" + bid):
                    out.append(unicodedata.normalize("NFC", json.dumps(b, ensure_ascii=False)))
        return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("reading")
    ap.add_argument("--fix", action="store_true")
    a = ap.parse_args()
    path = Path(a.reading)
    text = unicodedata.normalize("NFC", path.read_text(encoding="utf-8"))
    quran = {}
    for line in QURAN_TEXT.read_text(encoding="utf-8-sig").splitlines():
        ref, _, ayah = line.partition("|")
        if ayah:
            quran[ref.strip()] = unicodedata.normalize("NFC", ayah.lstrip("﻿"))
    quran_all = "\n".join(quran.values())
    quran_all_loose = loose(quran_all)[0]
    d = Dictionary()
    counts = dict.fromkeys(("exact", "fixed", "fixable", "elsewhere", "missing", "no-source", "bad-source"), 0)
    problems, repl = [], []
    for m in TAG_RE.finditer(text):
        ar = m.group("ar").strip()
        line_no = text.count("\n", 0, m.start()) + 1
        src = (m.group("src") or "").strip()
        if not src:
            counts["no-source"] += 1
            problems.append(f"line {line_no}: no-source  {ar}")
            continue
        declared, roots, bad = [], [], []
        for item in (x.strip() for x in src.split(",") if x.strip()):
            if re.fullmatch(r"\d{1,3}:\d{1,3}", item):
                if item in quran:
                    declared.append(quran[item])
                else:
                    bad.append(item)
                continue
            bm = BRANCH_RE.match(item)
            if bm and d.texts(bm.group("root"), bm.group("b")):
                declared += d.texts(bm.group("root"), bm.group("b"))
                roots.append(bm.group("root"))
            elif bm and d.texts(bm.group("root"), None):
                bad.append(item + " (no such branch)")
                roots.append(bm.group("root"))
            else:
                bad.append(item)
        if bad:
            counts["bad-source"] += 1
            problems.append(f"line {line_no}: bad-source  {ar}  [{', '.join(bad)}]")
        ar_l = loose(ar)[0].strip()
        hit = None
        for s in declared:
            if ar in s:
                hit = "exact"
                break
            sl, idx = loose(s)
            pos = sl.find(ar_l) if ar_l else -1
            if pos >= 0:
                hit = exact_span(s, idx, pos, pos + len(ar_l))
                break
        if hit == "exact":
            counts["exact"] += 1
        elif hit is not None:
            if a.fix and '"' not in hit and "\n" not in hit:
                counts["fixed"] += 1
                repl.append((m.start("ar"), m.end("ar"), hit))
            else:
                counts["fixable"] += 1
                problems.append(f"line {line_no}: fixable  {ar}  →  {hit}")
        else:
            other = [t for r in roots for t in d.texts(r, None)]
            if (ar_l and ar_l in quran_all_loose) or any(ar_l in loose(t)[0] for t in other):
                counts["elsewhere"] += 1
                problems.append(f"line {line_no}: elsewhere  {ar}  (source: {src})")
            else:
                counts["missing"] += 1
                problems.append(f"line {line_no}: missing  {ar}  (source: {src})")
    if repl:
        for x, y, new in reversed(repl):
            text = text[:x] + new + text[y:]
        path.write_text(text, encoding="utf-8")
    print(" ".join(f"{k}={v}" for k, v in counts.items()))
    for p in problems:
        print(p)
    return 1 if counts["missing"] or counts["no-source"] or counts["bad-source"] else 0


if __name__ == "__main__":
    sys.exit(main())
