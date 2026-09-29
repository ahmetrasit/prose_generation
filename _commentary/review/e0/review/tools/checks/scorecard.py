#!/usr/bin/env python3
"""scorecard.py: frozen mechanical diagnostics per commentary (script only). Principle: depth first, named items are
probes. Nothing here is a pass/fail; lengths are REPORTED and never judged; probe hits are diagnostics, not totals.
The other half of the evaluation is the user's blind read.

  python3 scorecard.py --ref S:A [LABEL=]FILE ... [--supply SUPPLY] [--pool FILE ...] [--json out.json]
  python3 scorecard.py --manifest smoke_manifest.json [--json out.json]
  python3 scorecard.py --freeze        (rewrite FROZEN.sha256 after a deliberate, versioned change)

Per commentary:
  form      words, paragraphs, longest and mean paragraph (words), headings, [bellek] marks, negation rate per 1,000
            words (the E2 regex, frozen) with a breakdown and 'not only' frames
  sourcing  share of checkable tags sourced (check.py), sources by type, match levels, Arabic outside tags
            (quotations and root names), unsourced quotations without a [bellek] mark, cited bound branches and
            whether an echo marker frames them (record only)
  reach     refs (focus excluded): in the window (±7), elsewhere in the surah, in other surahs
  pooled    share of the pool (refs + Arabic quotations across every file scored together, plus --pool files) that
            the file carries (TREC-style pooling: no single run is the gold)
  supply    with --supply: calibrated supply size; share of non-plain branches used (a quotation resolves to them);
            share of typed-link lines used (a ref of the line is cited); items used that are in no pooled input
            (neither the supply nor any --pool file nor any other scored file): candidate new findings, listed
  probes    watch probes for the focus from probes.eval.json (evaluation-only; never read by a model)
  frozen    whether the tool files still match FROZEN.sha256

Supply formats: JSON {"branches":[{"branch_ref":..,"plain":bool}], "links":[{"type":..,"refs":[..]}]} or Markdown.
In Markdown a branch is 'root_nnnnnn/Bnnn', 'ح م م B001', or a line starting 'Bnnn' under a line or heading that
names the root; '[plain]' on the branch's line marks it plain. A typed link is a line with refs under a heading
naming a join, bridge, concordance, echo, parallel, partner, formula, cross-reference, loaded word, contrast, use or
path; window, surah and word-table sections are text, not links.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import check as K
import common as C

FROZEN = C.HERE / "FROZEN.sha256"
FROZEN_FILES = ("common.py", "check.py", "lint.py", "scorecard.py", "lint_terms.eval.json", "probes.eval.json")
PROBES = C.HERE / "probes.eval.json"
LINK_SECTION = re.compile(r"join|bridge|concordance|echo|parallel|partner|formula|cross|definitional|loaded|contrast|"
                          r"\buses?\b|path|link|other places|same-surah|same surah|usage|neighbour", re.I)
TEXT_SECTION = re.compile(r"window|whole surah|the surah|surah text|focus|words|word table|its words|qira", re.I)
LETTERS_B = re.compile(r"((?:[ء-ي] ){1,4}[ء-ي])\s+(B\d{3})")
REF_B = re.compile(r"(root_\d{6})/(B\d{3})")
ROOT_LINE = re.compile(r"^\s*(?:#+|[-*])?\s*((?:[ء-ي] ){1,4}[ء-ي])(?=\s|$|\s*[(—:|-])")


def frozen_status() -> dict:
    if not FROZEN.exists():
        return {"status": "no FROZEN.sha256"}
    want = {}
    for line in FROZEN.read_text(encoding="utf-8").splitlines():
        if line.strip() and not line.startswith("#"):
            h, f = line.split(None, 1)
            want[f.strip()] = h
    changed = [f for f in FROZEN_FILES if want.get(f) != C.sha256(C.HERE / f)]
    return {"status": "match" if not changed else "CHANGED", "changed": changed}


def freeze() -> None:
    lines = ["# sha256 of the E0 check tools; a change to any of these files is a new scorecard version (see README)"]
    lines += [f"{C.sha256(C.HERE / f)}  {f}" for f in FROZEN_FILES]
    FROZEN.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(FROZEN.read_text(encoding="utf-8"))


# ------------------------------------------------------------------------------------------------ supply

def parse_supply(path: Path, focus: str) -> dict:
    text = path.read_text(encoding="utf-8")
    branches: dict[str, dict] = {}
    links: list[dict] = []
    if path.suffix == ".json":
        d = json.loads(text)
        for b in d.get("branches", []):
            branches[b["branch_ref"]] = {"plain": bool(b.get("plain")), "line": None}
        for i, l in enumerate(d.get("links", [])):
            links.append({"type": l.get("type", ""), "refs": set(l.get("refs", [])) - {focus}, "line": i})
        return {"text": text, "branches": branches, "links": links}
    by_letters = C.branch_by_letters()
    section, root = "", None
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith("#"):
            section = line.lstrip("#").strip()
        m = ROOT_LINE.match(line)
        if m and not re.search(r"\bB\d{3}\b", line[:m.end() + 3]):
            root = C.nroot(m.group(1))
        found = []  # (position, branch_ref)
        for m in REF_B.finditer(line):
            found.append((m.start(), f"{m.group(1)}/{m.group(2)}"))
        for m in LETTERS_B.finditer(line):
            k = f"{C.nroot(m.group(1))} {m.group(2)}"
            if k in by_letters:
                found.append((m.start(), by_letters[k]))
        if not found and root:  # 'B004 ...' lines and 'withheld: B003 ..., B010 ...' lines under a root line
            for m in re.finditer(r"\bB\d{3}\b", line):
                if f"{root} {m.group(0)}" in by_letters:
                    found.append((m.start(), by_letters[f"{root} {m.group(0)}"]))
        found.sort()
        for pos, b in found:
            branches.setdefault(b, {"plain": False, "line": n})
        for m in re.finditer(r"\[plain\]", line):  # the mark belongs to the nearest branch mentioned before it
            before = [b for pos, b in found if pos < m.start()]
            if before:
                branches[before[-1]]["plain"] = True
        if section and LINK_SECTION.search(section) and not TEXT_SECTION.search(section):
            refs = C.refs_in(line) - {focus}
            if refs:
                links.append({"type": section[:60], "refs": refs, "line": n})
    return {"text": text, "branches": branches, "links": links}


# ------------------------------------------------------------------------------------------------ per file

def form(text: str) -> dict:
    paras = C.paragraphs(text)
    pw = [len(p.split()) for p in paras] or [0]
    return {"words": len(text.split()), "paragraphs": len(paras), "longest_paragraph_words": max(pw),
            "mean_paragraph_words": round(sum(pw) / len(pw), 1), "headings": len(re.findall(r"^#", text, re.M)),
            "bellek_marks": len(K.BELLEK.findall(text)), "negation": C.negation(text)}


def reach(text: str, focus: str) -> dict:
    s, _ = C.parse_ref(focus)
    win = set(C.window(focus))
    refs = C.refs_in(text) - {focus}
    return {"refs_total": len(refs), "window": len([r for r in refs if r in win]),
            "same_surah_beyond_window": len([r for r in refs if r not in win and C.parse_ref(r)[0] == s]),
            "same_surah": len([r for r in refs if C.parse_ref(r)[0] == s]),
            "other_surah": len([r for r in refs if C.parse_ref(r)[0] != s]),
            "other_surahs_named": len({C.parse_ref(r)[0] for r in refs if C.parse_ref(r)[0] != s}),
            "refs": sorted(refs, key=C.parse_ref)}


def ingredients(text: str, rec: dict, focus: str) -> tuple[set, set]:
    refs = C.refs_in(text) - {focus}
    quotes = {C.fold(q["quote"]) for q in rec["quotations"] if q["source"] not in K.NOT_QUOTATIONS}
    quotes |= {C.fold(o["text"]) for o in rec["arabic_outside_tags"] if o["source"] not in K.NOT_QUOTATIONS}
    return refs, {q for q in quotes if q}


def cited_branch_refs(rec: dict) -> set[str]:
    out = set()
    for q in rec["quotations"] + rec["arabic_outside_tags"]:
        if q["source"] == "dictionary":
            for h in q["detail"].get("branches", []):
                out.add(h["branch_ref"])
    return out


def probes_for(focus: str, path: Path) -> list[dict]:
    if not path.exists():
        return []
    d = json.loads(path.read_text(encoding="utf-8"))["probes"]
    s, a = C.parse_ref(focus)
    out = []
    for key, ps in d.items():
        ks, span = key.split(":")
        lo, _, hi = span.partition("-")
        if int(ks) == s and int(lo) <= a <= int(hi or lo):
            out += [dict(p, key=key) for p in ps]
    return out


def run_probes(text: str, probes: list[dict]) -> list[dict]:
    """A probe hits if one 'any' regex matches, or if one sentence matches every 'all_in_sentence' regex."""
    spans = C.sentences(text)
    res = []
    for p in probes:
        m, snip = None, ""
        for rx in p.get("any", []):
            m = re.search(rx, text, re.I)
            if m:
                snip = text[max(0, m.start() - 60):m.end() + 60]
                break
        if not m and p.get("all_in_sentence"):
            for a, b in spans:
                sent = text[a:b]
                if all(re.search(rx, sent, re.I) for rx in p["all_in_sentence"]):
                    m, snip = True, sent[:240]
                    break
        res.append({"id": p["id"], "key": p["key"], "what": p["what"], "hit": bool(m),
                    "snippet": snip.replace("\n", " ").strip()})
    return res


def score_set(focus: str, files: list[tuple[str, Path]], supply: Path | None, pool: list[Path],
              probes_path: Path) -> dict:
    recs, texts = {}, {}
    for label, p in files + [(f"pool:{q.name}", q) for q in pool]:
        texts[label] = p.read_text(encoding="utf-8")
        recs[label] = K.check(p, focus)
    ingr = {k: ingredients(texts[k], recs[k], focus) for k in texts}
    pool_refs = set().union(*(v[0] for v in ingr.values())) if ingr else set()
    pool_quotes = set().union(*(v[1] for v in ingr.values())) if ingr else set()
    sup = parse_supply(supply, focus) if supply else None
    probes = probes_for(focus, probes_path)
    rows = []
    for label, p in files:
        t, rec = texts[label], recs[label]
        s = rec["summary"]
        refs, quotes = ingr[label]
        row = {"label": label, "file": str(p), "file_sha256": rec["file_sha256"], "ref": focus,
               "form": form(t),
               "sourcing": {"tags": s["tags"], "tags_checkable": s["tags_checkable"], "share_sourced": s["share_sourced"],
                            "by_source": s["by_source"], "levels": s["levels"],
                            "dictionary_early_phrase": s["dictionary_early_phrase"],
                            "dictionary_definition_only": s["dictionary_definition_only"],
                            "arabic_outside_tags_quotations": s["arabic_outside_tags_quotations"],
                            "arabic_outside_tags_quotations_sourced": s["arabic_outside_tags_quotations_sourced"],
                            "arabic_outside_tags_root_names": s["arabic_outside_tags_root_names"],
                            "unsourced_unmarked": s["unsourced_unmarked"], "bellek_status": s["bellek_status"],
                            "cited_bound_branches": s["cited_bound_branches"],
                            "bound_citations_with_echo_marker": s["bound_citations_with_echo_marker"],
                            "bound_citations_without_echo_marker": s["bound_citations_without_echo_marker"],
                            "bound_citations_extended_marker_only": s["bound_citations_extended_marker_only"]},
               "reach": reach(t, focus)}
        npool = len(pool_refs) + len(pool_quotes)
        row["pooled"] = {"pool_size": npool, "pool_files": len(texts),
                         "share_of_pool": round((len(refs) + len(quotes)) / npool, 3) if npool else None,
                         "refs_share": round(len(refs) / len(pool_refs), 3) if pool_refs else None,
                         "quotes_share": round(len(quotes) / len(pool_quotes), 3) if pool_quotes else None}
        if sup:
            row["supply"] = supply_use(sup, supply, rec, t, focus, refs, quotes,
                                       {k: v for k, v in ingr.items() if k != label},
                                       {k: cited_branch_refs(r) for k, r in recs.items() if k != label})
        row["probes"] = run_probes(t, probes)
        rows.append(row)
    return {"ref": focus, "supply": str(supply) if supply else None, "pool": [str(q) for q in pool], "rows": rows}


def supply_use(sup: dict, path: Path, rec: dict, text: str, focus: str, refs: set, quotes: set,
               other_ingr: dict, other_branches: dict) -> dict:
    cited = cited_branch_refs(rec)
    focus_roots = set(C.ayah_roots(focus))
    plain_dossier = C.plain_branches(focus)
    marked = {b for b, e in sup["branches"].items() if e["plain"]}
    plain_source = "supply [plain] marks" if marked else "root-dossier (the supply carries no [plain] marks)"
    plain_set = marked or plain_dossier
    nonplain = {b for b in sup["branches"] if b not in plain_set}
    nonplain_focus = {b for b in nonplain if b.split("/")[0] in focus_roots}
    used = nonplain & cited
    used_focus = nonplain_focus & cited
    link_used = [l for l in sup["links"] if l["refs"] & refs]
    link_refs = set().union(*(l["refs"] for l in sup["links"])) if sup["links"] else set()
    sup_refs = C.refs_in(sup["text"]) - {focus}
    sup_fold = C.fold(sup["text"])
    other_text_refs = set().union(*(v[0] for v in other_ingr.values())) if other_ingr else set()
    other_quotes = set().union(*(v[1] for v in other_ingr.values())) if other_ingr else set()
    other_b = set().union(*other_branches.values()) if other_branches else set()
    new_refs = sorted(refs - sup_refs - other_text_refs, key=C.parse_ref)
    new_quotes = sorted(q for q in quotes if q not in sup_fold and q not in other_quotes)
    new_branches = sorted(cited - set(sup["branches"]) - other_b)
    bb = C.branch_by_ref()
    spans = C.sentences(text)

    def where(item_rx):
        m = re.search(item_rx, text)
        if not m:
            return ""
        i = C.sentence_at(spans, m.start())
        return text[spans[i][0]:spans[i][1]].strip()[:300]
    qsrc = {C.fold(q["quote"]): q["source"] for q in rec["quotations"] + [dict(o, quote=o["text"]) for o in rec["arabic_outside_tags"]]}
    return {
        "supply_file": str(path), "supply_est_tokens": C.est_tokens(sup["text"]), "supply_chars": len(sup["text"]),
        "supply_branches": len(sup["branches"]), "supply_plain_marked": sum(1 for e in sup["branches"].values() if e["plain"]),
        "dossier_plain_at_focus": len(plain_dossier), "plain_source": plain_source,
        "nonplain_branches": len(nonplain), "nonplain_used": len(used),
        "share_nonplain_used": round(len(used) / len(nonplain), 3) if nonplain else None,
        "nonplain_focus_root_branches": len(nonplain_focus), "nonplain_focus_used": len(used_focus),
        "share_nonplain_focus_used": round(len(used_focus) / len(nonplain_focus), 3) if nonplain_focus else None,
        "nonplain_used_list": sorted(f"{bb[b]['root']} {bb[b]['branch']} [{bb[b]['branch_kind']}]" for b in used if b in bb),
        "typed_links": len(sup["links"]), "typed_links_used": len(link_used),
        "share_typed_links_used": round(len(link_used) / len(sup["links"]), 3) if sup["links"] else None,
        "typed_link_types": sorted({l["type"] for l in sup["links"]}),
        "link_refs": len(link_refs), "link_refs_cited": len(link_refs & refs),
        "candidate_new_findings": {
            "note": "used here, in no pooled input (not in the supply, not in any --pool file, not in any other file "
                    "scored for this ayah); for the user to read, not a score",
            "refs": [{"ref": r, "sentence": where(r"(?<![\d:])" + re.escape(r) + r"(?![\d])")} for r in new_refs],
            "arabic_quotations": [{"folded": q, "source": qsrc.get(q, "")} for q in new_quotes],
            "branches": [f"{bb[b]['root']} {bb[b]['branch']} [{bb[b]['branch_kind']}] ({b})" for b in new_branches if b in bb]},
    }


# ------------------------------------------------------------------------------------------------ output

def table(res: dict) -> str:
    out = [f"\n## {res['ref']}" + (f"  supply: {Path(res['supply']).name}" if res["supply"] else "")]
    out.append("label | words | paras | longest para | neg/1k | [bellek] | tags sourced | outside tags (quot/roots) | "
               "unsourced unmarked | bound cited (echo-marked) | refs win/surah/other | pool share" +
               (" | nonplain used: focus roots (all) | links used | new refs/quotes/branches" if res["supply"] else "") + " | probes")
    for r in res["rows"]:
        f, s, rc, pl = r["form"], r["sourcing"], r["reach"], r["pooled"]
        line = (f"{r['label']} | {f['words']} | {f['paragraphs']} | {f['longest_paragraph_words']} | "
                f"{f['negation']['neg_e2_per_1000']} | {f['bellek_marks']} | "
                f"{s['tags_checkable'] and sum(v for k, v in s['by_source'].items() if k in K.ATTESTED)}/{s['tags_checkable']} | "
                f"{s['arabic_outside_tags_quotations']}/{s['arabic_outside_tags_root_names']} | {s['unsourced_unmarked']} | "
                f"{s['cited_bound_branches']} ({s['bound_citations_with_echo_marker']}) | "
                f"{rc['window']}/{rc['same_surah_beyond_window']}/{rc['other_surah']} | {pl['share_of_pool']}")
        if res["supply"]:
            u = r["supply"]
            cn = u["candidate_new_findings"]
            line += (f" | {u['nonplain_focus_used']}/{u['nonplain_focus_root_branches']} "
                     f"(all {u['nonplain_used']}/{u['nonplain_branches']}) | {u['typed_links_used']}/{u['typed_links']} | "
                     f"{len(cn['refs'])}/{len(cn['arabic_quotations'])}/{len(cn['branches'])}")
        hits = [p["id"] for p in r["probes"] if p["hit"]]
        line += f" | {len(hits)}/{len(r['probes'])}" + (f" ({', '.join(hits)})" if hits else "")
        out.append(line)
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*", help="[LABEL=]path")
    ap.add_argument("--ref")
    ap.add_argument("--supply")
    ap.add_argument("--pool", nargs="*", default=[])
    ap.add_argument("--probes", default=str(PROBES))
    ap.add_argument("--manifest")
    ap.add_argument("--json")
    ap.add_argument("--freeze", action="store_true")
    a = ap.parse_args()
    if a.freeze:
        freeze()
        return 0
    sets = []
    if a.manifest:
        base = Path(a.manifest).resolve().parent
        for st in json.loads(Path(a.manifest).read_text(encoding="utf-8"))["sets"]:
            sets.append((st["ref"], [(k, (base / v).resolve()) for k, v in st["files"].items()],
                         (base / st["supply"]).resolve() if st.get("supply") else None,
                         [(base / q).resolve() for q in st.get("pool", [])]))
    else:
        if not a.ref or not a.files:
            ap.error("--ref and at least one file (or --manifest)")
        files = []
        for f in a.files:
            label, _, path = f.rpartition("=") if "=" in f else ("", "", f)
            files.append((label or Path(path).parent.name + "/" + Path(path).name, Path(path)))
        sets.append((a.ref, files, Path(a.supply) if a.supply else None, [Path(q) for q in a.pool]))
    results = [score_set(ref, files, sup, pool, Path(a.probes)) for ref, files, sup, pool in sets]
    fz = frozen_status()
    txt = "\n".join(table(r) for r in results)
    print(f"# scorecard (diagnostics only; no pass/fail; lengths reported, never judged); frozen tools: {fz['status']}"
          + (f" {fz['changed']}" if fz.get("changed") else ""))
    print(txt)
    if a.json:
        Path(a.json).parent.mkdir(parents=True, exist_ok=True)
        Path(a.json).write_text(json.dumps({"frozen": fz, "tool_sha256": {f: C.sha256(C.HERE / f) for f in FROZEN_FILES},
                                            "results": results}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
