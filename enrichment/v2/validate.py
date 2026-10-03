#!/usr/bin/env python3
"""Check annotations.jsonl against schema 3.0 and the rendered pages against the frozen base. Script only.

  python3 enrichment/v2/validate.py --surah 107 [--annotations PATH] [--out DIR] [--report PATH]

Records: required and conditional fields, enum values, id pattern and code, ayah scope, word limits, every source
locator resolves in the corpus index, hadis only sahih (and the cited report sahih under the project rule), memory
only with durum:degerlendirilmedi and never for hadis/nuzul/grades, modern Arabic dictionaries only in anlam_tarihi,
no intertext sources, duzeltme quotes the base verbatim, itiraz carries its argument, unique ids, anchors found.
Pages (if rendered): every base paragraph present, byte-exact and in order; every block line parses back to its
record; nothing after the registry but the registry. Exit 1 on any error.
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


def validate(s: int, ann: Path, out: Path | None) -> dict:
    wd = V2 / "work" / f"s{s:03d}"
    pk = wd / "pack"
    manifest = json.loads((pk / "pack.json").read_text(encoding="utf-8"))
    n_ayat = manifest["ayat"]
    base_surah = (pk / "base" / "surah.md").read_text(encoding="utf-8")
    base_all = base_surah + "\n".join(p.read_text(encoding="utf-8") for p in (pk / "base").glob("*_*.md"))
    corpus = B.Corpus(C.INDEX)
    recs = R.load(ann)
    errors, warnings = [], []
    for r in recs:
        errors += B.check_record(r, s, n_ayat, corpus, base_all)
        if r.get("tur") == "yenilik" and r.get("tarama") == "dilim" and r.get("klasik_tanik") == "bulunamadi" \
                and not any(w in r.get("metin", "").lower() for w in ("dilim", "yalnız", "sadece", "only")):
            warnings.append(f"{r['id']}: bulunamadi on the slice should say only the slice was searched")
        if not r.get("capa"):
            warnings.append(f"{r['id']}: no capa; it goes to the end of the surah page")
    dup = [k for k, c in Counter(r.get("id") for r in recs).items() if c > 1]
    if dup:
        errors.append(f"duplicate ids: {dup}")
    paras = R.paragraphs(base_surah)
    for r in recs:
        if r.get("capa") and R.find_para(paras, r["capa"]) is None:
            errors.append(f"{r['id']}: capa not found in the surah base")
    if out and out.exists():
        errors += check_page(out / "surah.md", base_surah, recs)
        for p in sorted(out.glob(f"{s}_*.md")):
            errors += check_page(p, (pk / "base" / p.name).read_text(encoding="utf-8"), recs)
    return {"surah": s, "records": len(recs), "by_tur": dict(Counter(r.get("tur") for r in recs)),
            "by_kat": dict(Counter(r.get("kat") for r in recs)),
            "words": sum(B.words(r.get("metin", "")) for r in recs),
            "errors": errors, "warnings": warnings, "passed": not errors}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--surah", type=int, required=True)
    ap.add_argument("--annotations", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--report", type=Path)
    a = ap.parse_args()
    wd = V2 / "work" / f"s{a.surah:03d}"
    rep = validate(a.surah, a.annotations or wd / "annotations.jsonl", a.out or wd / "out")
    text = json.dumps(rep, ensure_ascii=False, indent=1)
    if a.report:
        a.report.write_text(text + "\n", encoding="utf-8")
    print(text)
    sys.exit(0 if rep["passed"] else 1)


if __name__ == "__main__":
    main()
