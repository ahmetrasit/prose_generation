#!/usr/bin/env python3
"""lint.py: contamination lint for briefs, prompts and supply files (script only; reports, never edits).

  python3 lint.py <file>... [--kind auto|brief|supply] [--json out.json] [--strict]

What it flags, with file and line:
  known       the known contaminated brief example '(15:26, 15:28, 15:33)'
  named-ref   refs of the named cases and the refs that answer them (Fatiha chains, 4:34, 5:6, 18:86, 18:96, 29:38,
              29:39-45, S100, S103, and their answer passages), and the case names (Fatiha, S100, ...)
  answer      answer phrases of the North Star 'aha' and examples and of the Phase 2 watch cases (English, Turkish,
              a few Arabic)
  scene       v15 scene-inventory ids, multi-word inventory roles and scene vocabulary (scene tags are dropped:
              decision 7); curated single-word roles that coincide with answers ('stray', 'follower', well 'frame'
              and 'beam' only next to a well word, ...)
  verdict     verdict labels: 'no value', strong/moderate/weak grades, 'DEPARTS', 'withheld', 'present: no',
              '[N readings]', script echo-tier labels, confidence/grade fields, dominant-role ratios
  cap         numeric length/count caps (and template-parameter caps such as 'up to {kwic_max} times');
  cap-review  counts stated as form rules ('in one sentence') and cap vocabulary, for the user to judge

Kinds: 'brief' (instructions: every hit counts) and 'supply' (script-built data: a hit on a data line, i.e. a
dictionary branch line, a Quran text line or a mostly Arabic line, is reported with context 'data-line'; refs in a
supply are data and are reported as 'info'). --kind auto calls a file a supply when its path names a supply, packet,
sheet, pull, dossier or dictionary file, else a brief.

The term list lives in lint_terms.eval.json (evaluation only; never a model input). Files named *.eval.json are
skipped unless --include-eval. The calibrated token size of every file is reported (4581 + 1.151 x Arabic chars +
0.366 x other chars); sizes are reported, never judged.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import common as C

TERMS = C.HERE / "lint_terms.eval.json"
INVENTORY = C.PROJ / "prose_generation/_commentary/v15/data/frames_inventory.json"
SUPPLY_HINT = re.compile(r"supply|packet|sheet|pull|dossier|dictionary|01_dictionary|harvest|context\.md", re.I)
DATA_LINE = re.compile(r"\bB\d{3}\b|root_\d{6}|^\s*[-*]?\s*\d{1,3}:\d{1,3}(?::\d{1,3})?\s*[|:]?\s*[؀-ۿ]")
SCENE_WORDS = re.compile(r"\bscene (?:lines?|paths?|lens(?:es)?|tags?|inventory|ids?|members?)\b|\bscene:\s|\bscenes? (?:that|touching)\b",
                         re.I)


def load_terms(path: Path) -> dict:
    t = json.loads(path.read_text(encoding="utf-8"))
    inv = json.loads(INVENTORY.read_text(encoding="utf-8")) if INVENTORY.exists() else {"frames": []}
    ids = [f["id"] for f in inv["frames"]]
    prefixes = sorted({i.split(".")[0] for i in ids} | {"new"})
    multi = sorted({r for f in inv["frames"] for r in f["roles"] if (" " in r or "-" in r)}, key=len, reverse=True)
    t["_scene_id"] = re.compile(r"\b(?:" + "|".join(map(re.escape, prefixes)) + r")\.[a-z_]{3,}\b")
    t["_multi_roles"] = [(r, re.compile(r"\b" + re.escape(r) + r"\b", re.I)) for r in multi]
    t["_inventory"] = {"frames": len(ids), "multi_word_roles": len(multi), "path": str(INVENTORY)}
    t["_case_refs"] = set()
    for group in ("cases", "answer_refs", "blind_probe_refs"):
        for r in t["named_refs"][group]:
            if "-" in r:
                s, span = r.split(":")
                lo, hi = span.split("-")
                t["_case_refs"] |= {(f"{s}:{x}", group) for x in range(int(lo), int(hi) + 1)}
            else:
                t["_case_refs"].add((r, group))
    t["_ref_group"] = {}
    for r, g in t["_case_refs"]:
        t["_ref_group"].setdefault(r, g)
    return t


def is_data_line(line: str) -> bool:
    if DATA_LINE.search(line):
        return True
    ar = len(re.findall(f"[{C.ARABIC_CHARS}]", line))
    letters = len(re.findall(r"\w", line))
    return letters > 0 and ar / letters >= 0.5


def lint_file(path: Path, kind: str, T: dict) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    if kind == "auto":
        kind = "supply" if SUPPLY_HINT.search(path.name) or "/supply" in str(path) else "brief"
    hits = []

    def add(n, cat, sev, match, frm, line):
        data = kind == "supply" and is_data_line(line)
        if cat == "named-ref" and kind == "supply":
            sev = "info"
        hits.append({"line": n, "category": cat, "severity": sev, "match": match.strip()[:120], "from": frm,
                     "context": "data-line" if data else "text", "text": line.strip()[:220]})

    for n, line in enumerate(text.splitlines(), 1):
        for k in T["known_contamination"]:
            for m in re.finditer(k["pattern"], line):
                add(n, "known", "known", m.group(0), k["from"], line)
        for r in sorted(C.refs_in(line), key=C.parse_ref):
            g = T["_ref_group"].get(r)
            if g:
                add(n, "named-ref", "named-ref", r, f"named_refs.{g}", line)
        for k in T["named_case_words"]:
            for m in re.finditer(k["pattern"], line, re.I):
                add(n, "named-ref", "named-ref", m.group(0), k["from"], line)
        for k in T["answer_phrases"]:
            for m in re.finditer(k["pattern"], line, re.I):
                add(n, "answer", "answer", m.group(0), k["from"], line)
        if re.search(f"[{C.ARABIC_CHARS}]", line):
            fl = C.fold(line)
            for k in T["answer_phrases_ar"]:
                if re.search(k["pattern"], fl):
                    add(n, "answer", "answer", k["pattern"], k["from"], line)
        for m in T["_scene_id"].finditer(line):
            add(n, "scene", "scene", m.group(0), "v15 scene inventory id (decision 7: scene tags dropped)", line)
        for m in SCENE_WORDS.finditer(line):
            add(n, "scene", "scene", m.group(0), "scene vocabulary (decision 7)", line)
        seen_roles = set()
        for role, rx in T["_multi_roles"]:
            if rx.search(line) and not any(role in s for s in seen_roles):
                seen_roles.add(role)
                add(n, "scene", "scene", role, "v15 inventory role (multi-word)", line)
        for role in T["curated_roles"]["roles"]:
            if " " in role or "-" in role:
                continue
            for m in re.finditer(r"\b" + re.escape(role) + r"\b", line, re.I):
                add(n, "scene", "role-term", m.group(0), "v15 inventory role that coincides with an answer", line)
        for role, ctx in T["curated_roles"]["near"].items():
            if re.search(r"\b" + re.escape(role) + r"\b", line, re.I) and any(re.search(c, line, re.I) for c in ctx):
                add(n, "scene", "role-term", role, f"v15 inventory role '{role}' next to a context word", line)
        for k in T["verdict_patterns"]:
            for m in re.finditer(k["pattern"], line, re.M):
                add(n, "verdict", "verdict", m.group(0), k["from"], line)
        for k in T["cap_patterns"]:
            for m in re.finditer(k["pattern"], line, re.I):
                add(n, "cap", k["severity"], m.group(0), k["from"], line)

    def count(pred):
        out = {}
        for h in hits:
            if pred(h):
                out[h["severity"]] = out.get(h["severity"], 0) + 1
        return out

    return {"file": str(path), "kind": kind, "sha256": C.sha256(path), "chars": len(text),
            "est_tokens": C.est_tokens(text), "hits": hits,
            "summary_text_lines": count(lambda h: h["context"] == "text"),
            "summary_data_lines": count(lambda h: h["context"] == "data-line")}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--kind", default="auto", choices=["auto", "brief", "supply"])
    ap.add_argument("--terms", default=str(TERMS))
    ap.add_argument("--json", help="write the full report here")
    ap.add_argument("--include-eval", action="store_true", help="also lint *.eval.json files")
    ap.add_argument("--strict", action="store_true", help="exit 1 if a brief has a known/named-ref/answer/scene/verdict/cap hit")
    ap.add_argument("--quiet", action="store_true", help="summary lines only")
    a = ap.parse_args()
    T = load_terms(Path(a.terms))
    reports = []
    for f in a.files:
        p = Path(f)
        if p.name.endswith(".eval.json") and not a.include_eval:
            print(f"skip (evaluation-only file): {f}", file=sys.stderr)
            continue
        reports.append(lint_file(p, a.kind, T))
    bad = 0
    for r in reports:
        print(f"== {r['file']} [{r['kind']}] ~{r['est_tokens']:,} tokens; text lines {r['summary_text_lines']}; "
              f"data lines {r['summary_data_lines']}")
        if not a.quiet:
            for h in r["hits"]:
                if h["severity"] == "info":
                    continue
                tag = f"{h['severity']}" + ("/data-line" if h["context"] == "data-line" else "")
                print(f"  {h['line']:>5}: [{tag}] {h['match']!r} ({h['from']}) | {h['text'][:140]}")
        if r["kind"] == "brief" and any(h["severity"] in ("known", "named-ref", "answer", "scene", "role-term", "verdict", "cap")
                                        for h in r["hits"]):
            bad += 1
    if a.json:
        Path(a.json).parent.mkdir(parents=True, exist_ok=True)
        Path(a.json).write_text(json.dumps({"tool_sha256": {p: C.sha256(C.HERE / p) for p in ("lint.py", "common.py",
                                                            "lint_terms.eval.json")},
                                            "inventory": T["_inventory"], "reports": reports},
                                           ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return 1 if (a.strict and bad) else 0


if __name__ == "__main__":
    sys.exit(main())
