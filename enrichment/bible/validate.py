#!/usr/bin/env python3
"""Validate Bible annotations and unchanged frozen commentary pages.

Records must use the TEV/INC namespace, match source traditions, resolve every
locator, and name an exact paragraph anchor. Outputs use the Bible-owned index.
"""
from __future__ import annotations

import argparse
from contextlib import closing
import json
import re
import sys
from collections import Counter
from pathlib import Path

V2 = Path(__file__).resolve().parent
sys.path.insert(0, str(V2.parents[1]))
from enrichment.bible import blocks as B, corpus as C
from enrichment.bible import render as R

# the commentary called "taban" (taban, tabanın, tabandaki, tabana, tabanda …), not "ayak tabanı"/"dağın tabanında"
TABAN = re.compile(r"\btaban(?:ın|ı|a|da|daki|dan)?\b", re.IGNORECASE)
TABAN_OK = re.compile(r"\b(?:ayak|dağın|dağ|kabın|vadinin)\s+taban", re.IGNORECASE)


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
    found = Counter()
    reg = text.find("\n## Kaynak kayıtları")
    for line in text.splitlines():
        if line.startswith("{id:"):
            try:
                f = B.parse_line(line)
            except ValueError as x:
                e.append(f"{page.name}: unparsable block line: {x}")
                continue
            r = by_id.get(f.get("id"))
            found[f.get('id')] += 1
            if not r:
                e.append(f"{page.name}: block {f.get('id')} not in annotations")
            elif any(str(r.get(k)) != str(v) for k, v in f.items()):
                e.append(f"{page.name}: block {f['id']} does not round-trip")
            if reg >= 0 and text.find(line) > reg:
                e.append(f"{page.name}: block {f.get('id')} after the registry")
    if found != Counter(r['id'] for r in recs):
        e.append(f'{page.name}: missing or duplicate annotation blocks')
    return e


def check_records(s: int, target: str, recs: list[dict], gelenek: str = "ehlikitap") -> tuple[list[dict], list[dict], list[str]]:
    """(kept records, dropped [{id, errors}], warnings) for one page. gelenek: the pass ("islami") or "ehlikitap"
    for the Bible pass, whose records carry tevrat or incil themselves."""
    pk = V2 / "work" / f"s{s:03d}" / "pack"
    n_ayat = json.loads((pk / "pack.json").read_text(encoding="utf-8"))["ayat"]
    name, base, _ = R.target_page(s, target)
    paras = R.paragraphs(base)
    with closing(B.Corpus(C.INDEX)) as corpus:
        kept, dropped, warnings, seen = [], [], [], set()
        novelty_at: dict[str, str] = {}
        per_para: dict[str, int] = {}
        for r in recs:
            rid = r.get("id", "?")
            if gelenek == "islami":
                r.setdefault("gelenek", "islami")
            e = B.check_record(r, s, n_ayat, corpus, base)
            if gelenek == "islami" and r.get("gelenek") != "islami":
                e.append(f"{rid}: the Islamic pass writes only gelenek:islami")
            if gelenek == "ehlikitap" and r.get("gelenek") not in ("tevrat", "incil"):
                e.append(f"{rid}: the Bible pass writes gelenek tevrat or incil")
            if target != "surah":
                a = int(target.split(":")[1])
                try:
                    if not any(x[1] <= a <= x[2] for x in B.ayah_refs(r.get("ayet", ""))):
                        e.append(f"{rid}: ayet {r.get('ayet')} does not cover the page's ayah {target}")
                except ValueError:
                    pass  # reported by check_record
            if not str(r.get("paragraf", "")).strip() or not r.get("capa"):
                e.append(f"{rid}: paragraf and capa are required (every block goes after a paragraph of the base)")
            else:
                i, err = R.locate(paras, r)
                if i is None:
                    e.append(f"{rid}: {name}: {err}")
            if rid in seen:
                e.append(f"{rid}: duplicate id")
            try:  # the same number placement uses (render.locate): "¶3", " 3" and "03" are one paragraph
                para = str(int(str(r.get("paragraf", "")).strip().lstrip("¶").strip()))
            except ValueError:
                para = str(r.get("paragraf"))
            if r.get("tur") == "yenilik" and not e:
                if para in novelty_at:
                    e.append(f"{rid}: a second yenilik block after ¶{para} ({novelty_at[para]} is there); one per paragraph")
                else:
                    novelty_at[para] = rid
            seen.add(rid)
            if e:
                dropped.append({"id": rid, "errors": e})
                continue
            kept.append(r)
            per_para[para] = per_para.get(para, 0) + 1
            if TABAN.search(r.get("metin", "")) and not TABAN_OK.search(r.get("metin", "")):
                warnings.append(f"{rid}: metin calls the commentary 'taban'; say 'şerh' or state the point")
            if r.get("tur") == "yenilik" and r.get("tarama") == "dilim" and r.get("klasik_tanik") == "bulunamadi" \
                    and not any(w in r.get("metin", "").lower() for w in ("dilim", "yalnız", "sadece", "only")):
                warnings.append(f"{rid}: bulunamadi on the slice should say only the slice was searched")
        warnings += [f"¶{p}: {n} blocks after one paragraph (at most five)" for p, n in per_para.items() if n > 5]
        return kept, dropped, warnings


def validate(s: int, target: str, recs: list[dict], out: Path | None, gelenek: str = "ehlikitap") -> dict:
    kept, dropped, warnings = check_records(s, target, recs, gelenek)
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
    ap.add_argument("--pass", dest="pass_", choices=("ehlikitap",), default="ehlikitap",
                    help="ehlikitap: the Bible pass (records carry gelenek tevrat/incil; sources from the intertext index)")
    a = ap.parse_args()
    rep = validate(a.surah, a.target, R.load(a.annotations), a.out, a.pass_)
    text = json.dumps(rep, ensure_ascii=False, indent=1)
    if a.report:
        a.report.write_text(text + "\n", encoding="utf-8")
    print(text)
    sys.exit(0 if rep["passed"] else 1)


if __name__ == "__main__":
    main()
