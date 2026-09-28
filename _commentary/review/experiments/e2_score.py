#!/usr/bin/env python3
"""Pre-registered mechanical scoring for E2 (written before any E2 output existed, 2026-09-28).

Per ayah and replicate, for the two inputs (cold, dict), the integrated draft and the final (after the return call):
- pooled ingredients = refs (S:A, focus excluded) + Arabic quotations (diacritics folded) across BOTH inputs;
- recall = share of the pooled ingredients present in a text;
- form: words, longest paragraph (words), negation/disclaimer frames per 1,000 words (değil/sayılmaz/anlamına gelmez/
  demek değildir/söylemez), [bellek] marks, same-surah and other-surah refs outside the pool (new material).
Criterion 1 passes for an ayah-replicate when final recall >= max(input recall) + 0.10.
Criterion 2 passes when words <= 1.5 x longer input, longest paragraph <= 300, negation rate <= max(input rates).
Usage: python3 e2_score.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import e2_integration as E

NEG = re.compile(r"\b(değil(?:dir|dir\.)?|sayılmaz|anlamına gelmez|demek değildir|söylemez|gerektirmez)\b", re.I)


def metrics(text: str, pool_refs: set[str], pool_quotes: set[str], focus: str) -> dict:
    refs, quotes = E.ingredients(text)
    refs.discard(focus)
    norm = E.norm_ar(text)
    got_q = {q for q in pool_quotes if q in quotes or (len(q) > 6 and q in norm)}
    got_r = refs & pool_refs
    pool = len(pool_refs) + len(pool_quotes)
    words = len(text.split())
    paras = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    s = focus.split(":")[0]
    new = refs - pool_refs
    return {"recall": round((len(got_r) + len(got_q)) / pool, 3) if pool else None,
            "refs_kept": len(got_r), "quotes_kept": len(got_q), "words": words,
            "longest_para": max((len(p.split()) for p in paras), default=0),
            "neg_per_1000": round(1000 * len(NEG.findall(text)) / words, 2) if words else None,
            "bellek": text.count("[bellek]"),
            "new_same_surah": len({r for r in new if r.split(':')[0] == s}),
            "new_other_surah": len({r for r in new if r.split(':')[0] != s})}


def main() -> None:
    rows = []
    for ref in E.AYAT:
        _, cold, dic = E.readings(ref)
        ct, dt = cold.read_text(encoding="utf-8"), dic.read_text(encoding="utf-8")
        cr, cq = E.ingredients(ct)
        dr, dq = E.ingredients(dt)
        pool_r, pool_q = (cr | dr) - {ref}, cq | dq
        base = {n: metrics(t, pool_r, pool_q, ref) for n, t in (("cold", ct), ("dict", dt))}
        for rep in (1, 2):
            d = E.OUT / ref.replace(":", "_") / f"rep{rep}"
            row = {"ref": ref, "rep": rep, "pool": len(pool_r) + len(pool_q), **{f"in_{k}": v for k, v in base.items()}}
            for name in ("integrate", "final"):
                f = d / f"{name}.tr.md"
                if f.exists():
                    row[name] = metrics(f.read_text(encoding="utf-8"), pool_r, pool_q, ref)
            fin = row.get("final") or row.get("integrate")
            if fin:
                best = max(base["cold"]["recall"], base["dict"]["recall"])
                longer = max(base["cold"]["words"], base["dict"]["words"])
                negmax = max(base["cold"]["neg_per_1000"], base["dict"]["neg_per_1000"])
                row["c1_recall_pass"] = fin["recall"] >= best + 0.10
                row["c2_form_pass"] = (fin["words"] <= 1.5 * longer and fin["longest_para"] <= 300
                                       and fin["neg_per_1000"] <= negmax)
            rows.append(row)
    E.OUT.mkdir(parents=True, exist_ok=True)
    out = E.OUT / "score.json"
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    for r in rows:
        f = r.get("final") or {}
        print(f"{r['ref']:6} rep{r['rep']} pool {r['pool']:3} | cold {r['in_cold']['recall']} dict {r['in_dict']['recall']}"
              f" | final {f.get('recall')} words {f.get('words')} para {f.get('longest_para')} neg {f.get('neg_per_1000')}"
              f" | C1 {r.get('c1_recall_pass')} C2 {r.get('c2_form_pass')}")


if __name__ == "__main__":
    main()
