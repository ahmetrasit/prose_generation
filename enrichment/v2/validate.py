#!/usr/bin/env python3
"""Check one page's records against schema 3.0, and the rendered page against its frozen base. Script only.

  python3 enrichment/v2/validate.py --surah 107 --target surah|107:3 --annotations PATH [--out DIR] [--report PATH]

Records: required and conditional fields, enum values, id pattern and code, ayah scope (an ayah page's records must
cover its ayah), word limits, every source locator resolves in the corpus index, hadis only sahih (and the cited
report sahih under the project rule), memory only with durum:degerlendirilmedi and never for hadis/nuzul/grades,
modern Arabic dictionaries only in anlam_tarihi, no intertext sources, duzeltme quotes the base verbatim, itiraz
carries its argument, unique ids, capa found in the page's base. The report lists the errors per record: the
orchestrator drops a failing record (it is not repaired) and renders the rest.
Page (if DIR holds the rendered page): every base paragraph present, byte-exact and in order; every block line
parses back to its record; nothing after the registry but the registry. Exit 1 on any error.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

V2 = Path(__file__).resolve().parent
sys.path.insert(0, str(V2 / "tools"))
sys.path.insert(0, str(V2))
import blocks as B  # noqa: E402
import corpus as C  # noqa: E402
import render as R  # noqa: E402


def check_page(page: Path, base: str, recs: list[dict]) -> list[str]:
    e = []
    text = page.read_text(encoding="utf-8")
    cursor = 0
    for n, p in enumerate(R.paragraphs(base), 1):
        i = text.find(p, cursor)
        if i < 0:
            e.append(f"{page.name}: base paragraph {n} missing or changed: {p[:80]!r}")
        else:
            cursor = i + len(p)
    by_id = {r["id"]: r for r in recs}
    reg = text.find("\n## Kaynak kayıtları")
    for line in text.splitlines():
        if line.startswith("{id:"):
            try:
                f = B.parse_line(line)
            except ValueError as x:
                e.append(f"{page.name}: unparsable block line: {x}")
                continue
            r = by_id.get(f.get("id"))
            if not r:
                e.append(f"{page.name}: block {f.get('id')} not in annotations")
            elif any(str(r.get(k)) != str(v) for k, v in f.items()):
                e.append(f"{page.name}: block {f['id']} does not round-trip")
            if reg >= 0 and text.find(line) > reg:
                e.append(f"{page.name}: block {f.get('id')} after the registry")
    return e


def check_records(s: int, target: str, recs: list[dict]) -> tuple[list[dict], list[dict], list[str]]:
    """(kept records, dropped [{id, errors}], warnings) for one page."""
    pk = V2 / "work" / f"s{s:03d}" / "pack"
    n_ayat = json.loads((pk / "pack.json").read_text(encoding="utf-8"))["ayat"]
    name, base, _ = R.target_page(s, target)
    paras = R.paragraphs(base)
    corpus = B.Corpus(C.INDEX)
    kept, dropped, warnings, seen = [], [], [], set()
    for r in recs:
        rid = r.get("id", "?")
        e = B.check_record(r, s, n_ayat, corpus, base)
        if target != "surah":
            a = int(target.split(":")[1])
            try:
                if not any(x[1] <= a <= x[2] for x in B.ayah_refs(r.get("ayet", ""))):
                    e.append(f"{rid}: ayet {r.get('ayet')} does not cover the page's ayah {target}")
            except ValueError:
                pass  # reported by check_record
        if r.get("capa") and R.find_para(paras, r["capa"]) is None:
            e.append(f"{rid}: capa not found in {name}: {r['capa'][:80]!r}")
        if rid in seen:
            e.append(f"{rid}: duplicate id")
        seen.add(rid)
        if e:
            dropped.append({"id": rid, "errors": e})
            continue
        kept.append(r)
        if r.get("tur") == "yenilik" and r.get("tarama") == "dilim" and r.get("klasik_tanik") == "bulunamadi" \
                and not any(w in r.get("metin", "").lower() for w in ("dilim", "yalnız", "sadece", "only")):
            warnings.append(f"{rid}: bulunamadi on the slice should say only the slice was searched")
        if not r.get("capa"):
            warnings.append(f"{rid}: no capa; it goes to the end of the page")
    return kept, dropped, warnings


def validate(s: int, target: str, recs: list[dict], out: Path | None) -> dict:
    kept, dropped, warnings = check_records(s, target, recs)
    page_errors = []
    name, base, _ = R.target_page(s, target)
    if out and (out / name).exists():
        page_errors = check_page(out / name, base, kept)
    return {"surah": s, "target": target, "records": len(recs), "kept": len(kept), "dropped": dropped,
            "by_tur": dict(Counter(r.get("tur") for r in kept)), "by_kat": dict(Counter(r.get("kat") for r in kept)),
            "words": sum(B.words(r.get("metin", "")) for r in kept), "page_errors": page_errors,
            "warnings": warnings, "passed": not dropped and not page_errors}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--surah", type=int, required=True)
    ap.add_argument("--target", default="surah")
    ap.add_argument("--annotations", type=Path, required=True)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--report", type=Path)
    a = ap.parse_args()
    rep = validate(a.surah, a.target, R.load(a.annotations), a.out)
    text = json.dumps(rep, ensure_ascii=False, indent=1)
    if a.report:
        a.report.write_text(text + "\n", encoding="utf-8")
    print(text)
    sys.exit(0 if rep["passed"] else 1)


if __name__ == "__main__":
    main()
