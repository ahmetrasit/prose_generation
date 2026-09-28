#!/usr/bin/env python3
"""Score E1 (dictionary + memory permission, no ledger) against the v9 baselines on the same ayat:
dict (same inputs, no permission) and cold (permission, no dictionary). Mechanical only.

Per run: words, thinking/output tokens, cost, same-surah and other-surah refs (focus excluded), Arabic tags,
dictionary-only tags (a tag whose folded text occurs in 01_dictionary.md but not in the Quran text), negation rate.
Per ayah: Jaccard of cited refs between runs (rep1 vs rep2 is the noise floor).
"""
from __future__ import annotations

import json
import re
from itertools import combinations
from pathlib import Path

import e1_permission as E

REF = re.compile(r"\b(\d{1,3}):(\d{1,3})\b")
TAG = re.compile(r"\{\{?ar:([^,}]+)")
DIAC = re.compile(r"[ً-ٰٟۖ-ۭـٱ]")
NEG = re.compile(r"\b(değil(?:dir)?|sayılmaz|anlamına gelmez|söylemez|gerektirmez)\b", re.I)
QURAN = E.REPO.parent / "quran-data" / "data" / "text" / "quran-uthmani.tsv"


def fold(s: str) -> str:
    s = DIAC.sub("", s).replace("ٱ", "ا").replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")
    return re.sub(r"\s+", " ", s).strip()


QTEXT = fold(QURAN.read_text(encoding="utf-8"))


def runs(ref: str) -> dict[str, Path]:
    s, a = ref.split(":")
    sa = f"{s}_{a}"
    base = E.V9 / "lines" / "work" / sa / "synth"
    out = {"cold": base / "w10-opus-cold" / f"{sa}.reading.tr.md", "dict": base / "w10-opus-dict" / f"{sa}.reading.tr.md"}
    for rep in E.REPS:
        out[f"perm{rep}"] = E.OUT / sa / f"rep{rep}" / f"{sa}.reading.tr.md"
    return out


def usage(p: Path) -> dict:
    j = p.parent / "run.log.json"
    try:
        o = json.loads(j.read_text())
    except Exception:
        return {}
    u = o.get("usage", {}) or {}
    return {"cost": round(o.get("total_cost_usd") or 0, 2), "out": u.get("output_tokens"),
            "think": (u.get("output_tokens_details") or {}).get("thinking_tokens")}


def score(text: str, ref: str, dic_fold: str) -> dict:
    s = ref.split(":")[0]
    refs = {f"{int(a)}:{int(b)}" for a, b in REF.findall(text)} - {ref}
    tags = [fold(t) for t in TAG.findall(text)]
    dict_only = [t for t in tags if len(t) > 4 and t in dic_fold and t not in QTEXT]
    w = len(text.split())
    return {"words": w, "same": len({r for r in refs if r.split(':')[0] == s}),
            "other": len({r for r in refs if r.split(':')[0] != s}), "tags": len(tags), "dict_only_tags": len(dict_only),
            "neg1000": round(1000 * len(NEG.findall(text)) / w, 1) if w else 0, "refs": sorted(refs)}


def jac(a: set, b: set) -> float:
    return round(len(a & b) / len(a | b), 3) if a | b else 1.0


def main() -> None:
    table = []
    for ref in E.AYAT:
        _, dic = E.paths(ref)
        dic_fold = fold(dic.read_text(encoding="utf-8"))
        res = {}
        for name, p in runs(ref).items():
            if p.exists():
                res[name] = {**score(p.read_text(encoding="utf-8"), ref, dic_fold), **usage(p)}
        pairs = {f"{x}~{y}": jac(set(res[x]["refs"]), set(res[y]["refs"])) for x, y in combinations(res, 2)}
        table.append({"ref": ref, "runs": {k: {kk: vv for kk, vv in v.items() if kk != "refs"} for k, v in res.items()},
                      "jaccard": pairs})
    (E.OUT / "score.json").write_text(json.dumps(table, ensure_ascii=False, indent=1), encoding="utf-8")
    for t in table:
        print(f"== {t['ref']}")
        for k, v in t["runs"].items():
            print(f"  {k:6} w={v['words']:>5} same={v['same']:>3} other={v['other']:>3} tags={v['tags']:>3} "
                  f"dictonly={v['dict_only_tags']:>3} neg={v['neg1000']:>5} think={v.get('think')} ${v.get('cost')}")
        print("  jaccard:", {k: v for k, v in t["jaccard"].items() if "perm" in k})


if __name__ == "__main__":
    main()
