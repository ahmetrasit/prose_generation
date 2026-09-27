#!/usr/bin/env python3
"""Score root dossiers against the known answers (known_dossiers.json; kept here, never in the root-dossier repo or
any model input). Script only.

Per root: mixed groups (a dossier group holding ids of two known classes: an error), fragments (a class spread over
several groups: reported, allowed), branch agreement where the class names one, repeated wording recorded, the
coverage (every occurrence grouped), salvage and interpretive-label flags.

Usage: python3 _commentary/v12/eval/score_dossiers.py [--final /Volumes/OZTURK/_projects/root-dossier/out/final]
       (two arms: run it on out/final and on out-wa/final)
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT = HERE.parents[3] / "root-dossier" / "out" / "final"


def loose(s: str) -> str:
    s = re.sub(r"[ؐ-ًؚ-ٰٟۖ-ۭـ]", "", s or "")
    s = s.translate(str.maketrans({"أ": "ء", "إ": "ء", "ؤ": "ء", "ئ": "ء", "آ": "ء", "ٱ": "ا", "ى": "ي", "ة": "ه"}))
    return re.sub(r"\s+", " ", s).strip()


def score(key: str, known: dict, d: dict) -> list[str]:
    out = [f"## {d.get('root', key)} ({key})"]
    cls = {i: name for name, c in known["classes"].items() for i in c["ids"]}
    groups = d.get("groups") or []
    gof = {i: g for g in groups for i in g.get("ids") or []}
    mixed = []
    for g in groups:
        names = sorted({cls[i] for i in g.get("ids") or [] if i in cls})
        if len(names) > 1:
            mixed.append(f"  - MIXED {g['id']} «{g.get('label')}»: " + " + ".join(names))
    out.append(f"- mixed groups: {len(mixed)}")
    out += mixed
    for name, c in known["classes"].items():
        gs = sorted({gof[i]["id"] for i in c["ids"] if i in gof})
        missing = [i for i in c["ids"] if i not in gof]
        bs = sorted({gof[i].get("b") for i in c["ids"] if i in gof})
        acts = {a["id"]: a.get("b") for a in d.get("act") or []}
        bmiss = [i for i in c["ids"] if c.get("b") and acts.get(i) != c["b"]]
        out.append(f"- {name}: {len(c['ids'])} ids in {len(gs)} group(s) {gs}"
                   + (f"; NOT GROUPED {missing}" if missing else "")
                   + (f"; branch {'ok' if not bmiss else 'differs at ' + ', '.join(bmiss) + ' (' + ', '.join(map(str, bs)) + ')'}"
                      if c.get("b") else ""))
    for w in known.get("wording") or []:
        hit = any(loose(w["ar"]) in loose(x.get("ar", "")) or loose(x.get("ar", "")) in loose(w["ar"])
                  for g in groups for x in g.get("wording") or [] if set(x.get("ids") or []) & set(w["ids"]))
        out.append(f"- wording «{w['ar']}»: {'recorded' if hit else 'not recorded'}")
    lint = [g["id"] for g in groups if g.get("lint")]
    script = [g["id"] for g in groups if g.get("basis") == "script"]
    out.append(f"- complete: {d.get('complete')}; groups {len(groups)}; interpretive labels flagged {lint or 'none'}; "
               f"script groups {script or 'none'}")
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--final", default=str(DEFAULT))
    a = ap.parse_args()
    known = json.loads((HERE / "known_dossiers.json").read_text(encoding="utf-8"))
    lines = [f"# Dossier score — {a.final}", ""]
    total_mixed = 0
    for key, k in known.items():
        if key.startswith("_"):
            continue
        f = Path(a.final) / f"{key}.json"
        if not f.exists():
            lines += [f"## {key}: no final dossier", ""]
            continue
        s = score(key, k, json.loads(f.read_text(encoding="utf-8")))
        total_mixed += int(s[1].split(": ")[1])
        lines += s + [""]
    lines.append(f"Total mixed groups: {total_mixed}")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
