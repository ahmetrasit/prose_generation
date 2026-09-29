#!/usr/bin/env python3
"""selftest.py: frozen positive and negative controls for check.py, lint.py and scorecard.py (script only).

  python3 selftest.py        prints one line per control and exits 1 if any control fails

Controls were chosen from the smoke tests (2026-09-28): one quotation per source type, invented Arabic that must stay
unsourced, root names, silent elision, pieces joined by ؛, the ar-rubb / rabb trap, and a synthetic brief with one
hit per lint category. Temporary files go to smoke/selftest_tmp/.
"""
from __future__ import annotations

import sys
from pathlib import Path

import check as K
import common as C
import lint as L
import scorecard as S

TMP = C.HERE / "smoke" / "selftest_tmp"
results = []


def ok(name: str, cond: bool, got=None) -> None:
    results.append(cond)
    print(f"{'PASS' if cond else 'FAIL'}  {name}" + ("" if cond else f"   got: {got}"))


def src(res, focus, quote):
    r = res.resolve(quote)
    return r["source"], r


def main() -> int:
    R = K.Resolver("1:2")
    s, r = src(R, "1:2", "ٱلْحَمْدُ لِلَّهِ")
    ok("Quran quotation -> quran 1:2", s == "quran" and r["detail"]["refs"][0] == "1:2", r)
    s, r = src(R, "1:2", "الحمد نقيض الذم")
    ok("dictionary phrase -> dictionary with source tags",
       s == "dictionary" and any(b["source_tags"] for b in r["detail"]["branches"]), r)
    s, r = src(R, "1:2", "الرُّبّ")
    ok("ar-rubb (a dictionary noun) is not matched to rabb in 1:2", s == "dictionary", r)
    for inv in ("السيارة الحمراء في الشارع", "الصراط الطريق الذي يبتلع سالكه", "نفخ فيه الروح فصار حيا",
                "ضرب الرجل في الأرض إذا سافر بعيدا", "الحاسوب", "ديمقراطية"):
        s, r = src(R, "1:2", inv)
        ok(f"invented Arabic stays unsourced: {inv}", s == "unsourced", r)
    s, r = src(R, "1:2", "ق و م")
    ok("root name -> root_name (not a quotation)", s == "root_name" and r["detail"]["in_dictionary"], r)
    s, r = src(R, "1:2", "بِ")
    ok("single letter -> too_short", s == "too_short", r)
    R4 = K.Resolver("4:34")
    s, r = src(R4, "4:34", "حافظت على الرجل إذا حفظته في مغيبه")
    ok("silent elision -> gapped dictionary match", s == "dictionary" and r["level"] == "gapped", r)
    s, r = src(R4, "4:34", "قوام أهل بيته وقيام أهل بيته؛ الذي يقيم شأنهم")
    ok("pieces joined by ؛ -> resolved piecewise", s == "dictionary" and r["level"] == "pieces", r)
    s, r = src(K.Resolver("1:4"), "1:4", "نصب على النداء وقد تحذف ياء النداء")
    ok("Majaz direct text -> majaz", s == "majaz", r)
    s, r = src(K.Resolver("1:4"), "1:4", "والطير الضوارب المخترقات الأرض الطالبات الرزق")
    ok("early entry only (al-Ayn, d-r-b) -> early_entry", s == "early_entry" and r["detail"]["entries"][0]["source"] == "ayn", r)
    s, r = src(K.Resolver("1:4"), "1:4", "مَلِكِ")
    ok("variant reading at the focus -> quran or qiraat",
       s == "qiraat" or (s == "quran") or "qiraat" in r["also"], r)

    TMP.mkdir(parents=True, exist_ok=True)
    com = TMP / "commentary.tr.md"
    com.write_text(
        "Kelime {ar:ٱلطَّيِّبَٰتُ, tr:et-tayyibât, gloss:temiz şeyler} diye geçer. Sözlükte bir kalıp da vardır: "
        "{ar:الأطيبان الأكل والنكاح, tr:el-etyebân, gloss:iki güzel şey}; bu ancak yankı olarak duyulur.\n\n"
        "Bir başka söz \"الطوع نقيض الكره\" diye aktarılır. Bu yorum eskilere aittir [bellek].\n\n"
        "Uydurma bir söz: {ar:السيارة الحمراء في الشارع, tr:x, gloss:y}. Bu anlamına gelmez, değil.\n", encoding="utf-8")
    rec = K.check(com, "5:6")
    sm = rec["summary"]
    ok("check: unsourced unmarked quotation listed", sm["unsourced_unmarked"] == 1, sm)
    ok("check: Arabic in quotation marks flagged and sourced",
       sm["arabic_outside_tags_quotations"] == 1 and rec["arabic_outside_tags"][0]["context"] == "quotation marks"
       and rec["arabic_outside_tags"][0]["source"] == "dictionary", rec["arabic_outside_tags"])
    ok("check: [bellek] mark recorded with its sentence", sm["bellek_marks"] == 1, rec["bellek"])
    b = [c for c in rec["cited_branches"] if c["bound"]]
    ok("check: bound branch (non_bare) cited with an echo marker", bool(b) and b[0]["framing"].startswith("echo"), b)
    ok("check: negation counted (E2 regex)", sm["negation"]["neg_e2_count"] == 2, sm["negation"])

    brief = TMP / "brief.md"
    brief.write_text("Cite refs e.g. (15:26, 15:28, 15:33).\nThe lead animal walks in front.\n"
                     "B004 [collocation] present: no\nWrite at most 300 words.\nscene: travel.route\n"
                     "A clean sentence about grammar.\n", encoding="utf-8")
    T = L.load_terms(L.TERMS)
    rep = L.lint_file(brief, "brief", T)
    cats = {h["severity"] for h in rep["hits"]}
    for c in ("known", "named-ref", "answer", "verdict", "cap", "scene"):
        ok(f"lint: category '{c}' detected", c in cats, sorted(cats))
    ok("lint: clean line has no hit", not any(h["line"] == 6 for h in rep["hits"]), rep["hits"])

    sup = TMP / "supply.md"
    sup.write_text("## Branch index\n- ر ف ق B004 [mixed_non_bare] ...\n- ر ف ق B001 [plain] ...\n"
                   "## Definitional joins\n- ر ف ق B004 -> 5:95, 5:97\n", encoding="utf-8")
    ps = S.parse_supply(sup, "5:6")
    ok("scorecard: supply branches and [plain] parsed",
       len(ps["branches"]) == 2 and sum(e["plain"] for e in ps["branches"].values()) == 1, ps["branches"])
    ok("scorecard: typed link parsed", len(ps["links"]) == 1 and ps["links"][0]["refs"] == {"5:95", "5:97"}, ps["links"])
    ok("scorecard: frozen status readable", S.frozen_status()["status"] in ("match", "CHANGED", "no FROZEN.sha256"))

    sup0 = TMP / "supply_e0.md"
    sup0.write_text("## A. The ayah\n- 5:6:1 x\n## B. Dictionary: every branch\n"
                    "- root_000001/B001 [plain: 5:6:1] | a | b\n- root_000001/B002 | c | d\n"
                    "## C. Typed links\n### Definitional pointers: the window or the surah\n"
                    "- root_000001/B002 names x -> 5:95, 5:97\n## D. Quran usage\n### Every use\n- 2:3\n"
                    "## E. Parallels\n### Other surahs (1)\n- 7:1 — root: x\n"
                    "## F. Existing chains\n- root_000009/B004 «y» (3:3)\n## G. Majaz\n- 5:9\n", encoding="utf-8")
    p0 = S.parse_supply(sup0, "5:6")
    ok("scorecard: E0 page branches from section B only, [plain: ref] read",
       set(p0["branches"]) == {"root_000001/B001", "root_000001/B002"}
       and [b for b, e in p0["branches"].items() if e["plain"]] == ["root_000001/B001"], p0["branches"])
    ok("scorecard: E0 links from C, D, E, F (window/surah headings included), none from A or G",
       sorted(l["type"][0] for l in p0["links"]) == ["C", "D", "E", "F"], p0["links"])
    ok("scorecard: E0 mentions include chain branches", "root_000009/B004" in p0["mentioned"], p0["mentioned"])

    sys.path.insert(0, str(C.HERE.parent))
    import textclean as TC
    ft = "قال حميد (1) : # (1) في بعض النسخ بدله طفيل. وفى اللسان: قال طفيل # والابل معروفة"
    ok("textclean: Sihah edition footnote replaced by a marker, text kept",
       TC.FOOTNOTE_MARK in TC.strip_edition_footnotes(ft, "sihah") and "والابل معروفة" in TC.strip_edition_footnotes(ft, "sihah")
       and "اللسان" not in TC.strip_edition_footnotes(ft, "sihah"), TC.strip_edition_footnotes(ft, "sihah"))
    ok("textclean: other sources untouched", TC.strip_edition_footnotes(ft, "tahdhib") == ft)
    hits = K.Resolver("19:73").majaz("أي مجلسا والندى والنادي واحد")
    ok("check: a Majaz quote of surah 19 resolves to its own entry, mapped to 19:73 (not entry 1308 / 18:108)",
       bool(hits) and all(str(h["entry_id"]) != "1308" for h in hits) and hits[0].get("mapped_ref") == "19:73", hits[:3])
    print(f"\n{sum(results)} of {len(results)} controls pass")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
