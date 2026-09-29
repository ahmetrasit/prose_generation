#!/usr/bin/env python3
"""Discovery and handover trace (script only; no model calls). Written 2026-09-28 after the user's 1:6 blind read
("no 'pulley' resonance of mustaqim … or h-d-y's 'needs support to walk'").

For each ayah it asks two questions over every branch of every root of the ayah (the project dictionary):
1. Discovery: which earlier stages ever activated the branch?
   HFT relay, v12 relay and the channel reviews (from the E0 pull file), v5 discovery files, the v13 and v14
   activation stages (act.md), the v15 record (record.json).
2. Handover: which final readings carry it?
   Every saved final reading of the ayah (v5, v9, v11, v13, v14, v15, E1, E2), read by the E0 checks: a branch
   counts as carried when an Arabic quotation of the reading resolves to it and to at most one other branch
   (check.py); a quoted bare root word resolves to many branches and counts for none. Senses written only in
   Turkish are invisible to that test, so the named items below also get a keyword check.

Named items are evaluation probes only (never a model input): the North Star's Fatiha items that fall in 1:6, the
user's 1:6 remarks, and the watch cases (29:38 eye film, 18:86 ḥamaʾ).
Usage: python3 trace.py   -> trace.json, TRACE_TABLES.md
"""
from __future__ import annotations

import collections
import glob
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMM = HERE.parents[1]
sys.path.insert(0, str(HERE.parent / "e0" / "checks"))
import common as C  # noqa: E402
import check as K  # noqa: E402
import scorecard as S  # noqa: E402

AYAT = ["1:6", "29:38", "18:86"]
LETTERS_B = re.compile(r"((?:[ء-ي] ){1,4}[ء-ي])\s*[:/]?\s*(B\d{3})")
REF_B = re.compile(r"(root_\d{6})/(B\d{3})")

# evaluation-only probes: (label, branch finder (root letters, image regex), marker regex over the reading text)
NAMED = {
    "1:6": [
        ("swallowing road (ṣirāṭ)", ("ص ر ط", r"بلع|ابتلاع|الغيبة في المرور"), r"yut|ابتلاع|بلع|سرط|yutul|yutan"),
        ("well pulley (mustaqīm)", ("ق و م", r"آلة قائمة"), r"makara|البكرة|بكرة"),
        ("walking held up between two (ihdinā)", ("ه د ي", r"مشي التهادي"),
         r"يهادي|يهادى|يُهَادَى|تهادى|تَهَادَى|التهادي|iki kişi(?:nin)? arasında|dayanarak yürü|yalpala"),
        ("the one that goes ahead (hādī)", ("ه د ي", r"المتقدم|ما يتقدم|أول|المقدم|العنق"),
         r"önde giden|öne düşen|öncü|هوادي|الهادي|boyn"),
        ("water that stands (qāma l-māʾ)", ("ق و م", r"جمود ووقوف"), r"qāma l-māʾ|قام الماء|duran su|durgun su|suyun dur"),
    ],
    "29:38": [
        ("eye film (as-sabīl) — watch case", ("س ب ل", r"غشاوة"), r"göz perdesi|السبل|السَّبَل|sebel|örümcek ağ|perde"),
    ],
    "18:86": [
        ("ḥamaʾ as the human fabric — watch case", ("ح م ء", r"طين|حمأ"), r"15:26|15:28|15:33|صلصال|salsal|balçı"),
        ("ʿayn as the sun's disk", ("ع ي ن", r"الشمس|قرص"), r"güneş(?:in)? (?:gözü|kursu|diski|yuvarla)|عين الشمس"),
    ],
}


def sa(ref):
    s, a = ref.split(":")
    return f"{s}_{a}", f"s{int(s):03d}"


def to_refs(text: str, roots: set[str]) -> set[str]:
    bl = C.branch_by_letters()
    out = {f"{a}/{b}" for a, b in REF_B.findall(text)}
    for letters, b in LETTERS_B.findall(text):
        k = f"{C.nroot(letters)} {b}"
        if k in bl:
            out.add(bl[k])
    return {r for r in out if r.split("/")[0] in roots}


def discovery_sources(ref: str, roots: set[str]) -> dict[str, set[str]]:
    s_a, sd = sa(ref)
    out = {}
    pull = json.loads((COMM / "review/e0/supply/out" / f"{s_a}.pull.json").read_text(encoding="utf-8"))
    out["HFT relay"] = {m["branch_ref"] for rec in pull.get("hft_relay", []) for m in rec["members"]
                        if m["branch_ref"].split("/")[0] in roots}
    out["v12 relay"] = {m["branch_ref"] for rec in pull.get("v12_relay", []) for m in rec["members"]
                        if m["branch_ref"].split("/")[0] in roots}
    out["channel reviews"] = {b for rec in pull.get("chains", []) for m in rec.get("members", [])
                              for b in m.get("branch_refs", []) if b.split("/")[0] in roots}
    for name, pat in (("v5 discovery", f"v5/raw/*/{sd}/{s_a}/*.discovery.json"),
                      ("v13 act", f"v13/out*/{sd}/{s_a}/act.md"),
                      ("v14 act", f"v14/out*/{sd}/{s_a}/act.md"),
                      ("v15 record", f"v15/out*/{sd}/{s_a}/record.json")):
        files = sorted(glob.glob(str(COMM / pat)))
        got = set()
        for f in files:
            got |= to_refs(Path(f).read_text(encoding="utf-8", errors="replace"), roots)
        if files:
            out[f"{name} ({len(files)} run{'s' if len(files) > 1 else ''})"] = got
    return out


def final_readings(ref: str) -> list[tuple[str, Path]]:
    s_a, sd = sa(ref)
    pats = [("v5", f"v5/raw/*/{sd}/{s_a}/{s_a}.prose.tr.md"),
            ("v9", f"v9/lines/work/{s_a}/synth/*/{s_a}.reading.tr.md"),
            ("v9 pilot", f"v9/pilot/{s_a}*/{s_a}.reading.tr.md"),
            ("v9 network", f"v9/network/out/{s_a}/*/{s_a}.reading.tr.md"),
            ("v11", f"v11/out*/{sd}/{s_a}/{s_a}.reading.tr.md"),
            ("v13", f"v13/out*/{sd}/{s_a}/{s_a}.reading.tr.md"),
            ("v14", f"v14/out*/{sd}/{s_a}/{s_a}.reading.tr.md"),
            ("v15", f"v15/out*/{sd}/{s_a}/commentary.tr.md"),
            ("E1", f"review/experiments/e1/{s_a}/rep*/{s_a}.reading.tr.md"),
            ("E2", f"review/experiments/e2/{s_a}/rep*/final.tr.md")]
    out = []
    for ver, pat in pats:
        for f in sorted(glob.glob(str(COMM / pat))):
            p = Path(f)
            tag = p.parent.name if p.parent.name not in (s_a,) else p.parents[2].name
            out.append((f"{ver}:{tag}", p))
    return out


def specific_citations(rec: dict) -> set[str]:
    """Branches a reading cites specifically: a dictionary quotation that resolves to at most two branches (a bare
    root word such as المستقيم resolves to many and names none of them)."""
    out = set()
    for q in rec["quotations"] + rec["arabic_outside_tags"]:
        if q["source"] != "dictionary":
            continue
        hits = {h["branch_ref"] for h in q["detail"].get("branches", [])}
        if 1 <= len(hits) <= 2 and q["detail"].get("n_matches", len(hits)) <= 2:
            out |= hits
    return out


def named_branch(root_letters: str, img_rx: str, roots: set[str]) -> str | None:
    bb = C.branch_by_ref()
    for r in sorted(bb):
        b = bb[r]
        if b["root"] == root_letters and r.split("/")[0] in roots and re.search(img_rx, b["image_ar"] + " " + b["what_is_ar"]):
            return r
    return None


def main() -> None:
    bb = C.branch_by_ref()
    report = {}
    for ref in AYAT:
        roots = set(C.ayah_roots(ref))
        universe = sorted(r for r, b in bb.items() if b["root_id"] in roots)
        plain = C.plain_branches(ref) & set(universe)
        src = discovery_sources(ref, roots)
        any_src = set().union(*src.values()) if src else set()
        finals = []
        for label, p in final_readings(ref):
            try:
                rec = K.check(p, ref)
                cited = specific_citations(rec) & set(universe)
            except Exception as e:  # a reading the checker cannot read is reported, not skipped silently
                cited, rec = set(), {"error": str(e)[:200]}
            text = p.read_text(encoding="utf-8", errors="replace")
            finals.append(dict(label=label, path=str(p.relative_to(COMM)), cited=sorted(cited), words=len(text.split()),
                               text=text))
        any_final = set().union(*(set(f["cited"]) for f in finals)) if finals else set()
        rows = []
        for r in universe:
            b = bb[r]
            rows.append(dict(branch=r, root=b["root"], bid=b["branch"], kind=b["branch_kind"], image=b["image_ar"],
                             plain=r in plain, sources=[k for k, v in src.items() if r in v],
                             finals=[f["label"] for f in finals if r in f["cited"]]))
        named = []
        for label, (rl, img_rx), mk in NAMED.get(ref, []):
            br = named_branch(rl, img_rx, roots)
            named.append(dict(item=label, branch=br,
                              sources=[k for k, v in src.items() if br in v] if br else [],
                              finals_by_keyword=[f["label"] for f in finals if re.search(mk, f["text"], re.I)],
                              finals_by_quote=[f["label"] for f in finals if br and br in f["cited"]]))
        nonplain = [x for x in rows if not x["plain"]]
        runs = []
        s_a, sd = sa(ref)
        for pat, rd in ((f"v13/out*/{sd}/{s_a}/act.md", f"{s_a}.reading.tr.md"), (f"v14/out*/{sd}/{s_a}/act.md", f"{s_a}.reading.tr.md"),
                        (f"v15/out*/{sd}/{s_a}/record.json", "commentary.tr.md")):
            for f in sorted(glob.glob(str(COMM / pat))):
                d = Path(f).parent
                act = to_refs(Path(f).read_text(encoding="utf-8", errors="replace"), roots) - plain
                fin = next((x for x in finals if Path(COMM / x["path"]).parent == d and x["path"].endswith(rd)), None)
                if fin is None:
                    continue
                kept = act & set(fin["cited"])
                runs.append(dict(run=str(d.relative_to(COMM)), activated=len(act), cited_in_reading=len(set(fin["cited"]) - plain),
                                 activated_and_cited=len(kept), lost=sorted(act - set(fin["cited"]))))
        report[ref] = dict(
            roots=[bb[u]["root"] for u in universe if u.endswith("/B001")] or sorted({bb[u]["root"] for u in universe}),
            universe=len(universe), plain=len(plain), nonplain=len(nonplain),
            discovered_any=sum(1 for x in nonplain if x["sources"]),
            carried_any_final=sum(1 for x in nonplain if x["finals"]),
            discovered_not_carried=sum(1 for x in nonplain if x["sources"] and not x["finals"]),
            carried_without_source=sum(1 for x in nonplain if x["finals"] and not x["sources"]),
            never=sum(1 for x in nonplain if not x["sources"] and not x["finals"]),
            by_source={k: len(v - plain) for k, v in src.items()},
            finals=[dict(label=f["label"], path=f["path"], words=f["words"], cited_nonplain=len(set(f["cited"]) - plain))
                    for f in finals],
            named=named, rows=rows, runs=runs)
    (HERE / "trace.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")

    L = ["# Discovery and handover trace: tables (generated by trace.py)", ""]
    for ref, R in report.items():
        L += [f"## {ref}", "",
              f"Roots: {', '.join(R['roots'])}. Branches: {R['universe']} ({R['plain']} plain at this ayah, "
              f"{R['nonplain']} not).", "",
              "| of the non-plain branches | count |", "|---|---|",
              f"| activated by at least one discovery stage | {R['discovered_any']} |",
              f"| cited (Arabic quotation) by at least one final reading | {R['carried_any_final']} |",
              f"| activated but never cited in a final reading | {R['discovered_not_carried']} |",
              f"| cited without any recorded activation | {R['carried_without_source']} |",
              f"| never activated, never cited | {R['never']} |", "",
              "| discovery stage | non-plain branches activated |", "|---|---|"]
        L += [f"| {k} | {v} |" for k, v in R["by_source"].items()]
        L += ["", "| final reading | words | non-plain branches cited |", "|---|---|---|"]
        L += [f"| {f['label']} | {f['words']:,} | {f['cited_nonplain']} |" for f in R["finals"]]
        if R["runs"]:
            L += ["", "| run (same directory) | non-plain branches activated | cited in its reading | activated and cited |",
                  "|---|---|---|---|"]
            L += [f"| {r['run']} | {r['activated']} | {r['cited_in_reading']} | {r['activated_and_cited']} |" for r in R["runs"]]
        L += ["", "| named item | branch | activated by | reading that states it (keyword) |", "|---|---|---|---|"]
        for n in R["named"]:
            L.append(f"| {n['item']} | {n['branch'] or '—'} | {', '.join(n['sources']) or '—'} | "
                     f"{', '.join(n['finals_by_keyword']) or '—'} |")
        L += ["", "Non-plain branches, one line each (activated by → cited in):", ""]
        for x in R["rows"]:
            if x["plain"]:
                continue
            L.append(f"- {x['root']} {x['bid']} [{x['kind']}] «{x['image']}»: "
                     f"{'; '.join(x['sources']) or 'never activated'} → {'; '.join(x['finals']) or 'no final reading'}")
        L.append("")
    (HERE / "TRACE_TABLES.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    for ref, R in report.items():
        print(ref, {k: R[k] for k in ('universe', 'plain', 'nonplain', 'discovered_any', 'carried_any_final',
                                       'discovered_not_carried', 'never')})


if __name__ == "__main__":
    main()
