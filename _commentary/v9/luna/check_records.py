#!/usr/bin/env python3
"""Check Luna's records for one worklist (or all): nothing skipped, nothing generic, Arabic real.

Records: WORK_DIR/records/<worklist stem>.jsonl, one JSON object per line:
  {"id", "verdict": "reading"|"note"|"none", "focus_ar", "branch", "trigger_ar", "trigger_ref",
   "before", "after", "reason", "code", "lines"}

Items whose evidence lines are numbered ("— lines: N" in the heading) take a "lines" string of N codes
(- nothing, n note, r reading), one per line in order; every n/r line at position k needs its own full
record with id "<item>.<k>" and the matching verdict. Such an item's own verdict is optional (give one
with full fields only when the ayah itself activates the branch beyond the listed lines).

Checks:
  - every item id of the worklist has exactly one record; extra ids must start with X
  - line codes: right length, only - n r, and a matching record for each n/r (none for -)
  - reading/note: focus_ar, trigger_ar, trigger_ref, after and reason are filled; reading reason ≥ 60 chars
  - none: code is no-trigger | noise | canonical | wrong | same-as:<id>
  - focus_ar occurs in the focus ayah; trigger_ar occurs in the ayah trigger_ref (diacritics ignored)
  - no two records share the same reason or the same after text (generic sentences)

Usage: python3 _commentary/v9/luna/check_records.py WORK_DIR [WORKLIST_NAME ...]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from verify_ar import QURAN_TEXT, loose  # noqa: E402

CODES = re.compile(r"^(no-trigger|noise|canonical|wrong|same-as:[A-Z]\w*(\.\w+)?)$")
REF = re.compile(r"^\d{1,3}:\d{1,3}$")


def quran() -> dict[str, str]:
    out = {}
    for line in QURAN_TEXT.read_text(encoding="utf-8-sig").splitlines():
        ref, _, ayah = line.partition("|")
        if ayah:
            out[ref.strip()] = loose(ayah.lstrip("﻿"))[0]
    return out


def norm(s: str) -> str:
    return re.sub(r"\W+", " ", s.lower()).strip()


def check(work: Path, names: list[str], q: dict[str, str]) -> list[str]:
    index = [l.split("\t") for l in (work / "items.tsv").read_text(encoding="utf-8").splitlines() if l]
    n_lines = {}
    for name in names:
        for m in re.finditer(r"^### (\S+) — .* — lines: (\d+)$", (work / name).read_text(encoding="utf-8"), re.M):
            n_lines[m.group(1)] = int(m.group(2))
    focus_ref = (work / "context.md").read_text(encoding="utf-8").split(" — ", 1)[0].lstrip("# ").strip()
    focus = q[focus_ref]
    problems, seen_reason, seen_after = [], {}, {}
    for name in names:
        expected = [i for i, w in index if w == name]
        path = work / "records" / (Path(name).stem + ".jsonl")
        if not path.exists():
            problems.append(f"{name}: no records file {path.name}")
            continue
        got = {}
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError as e:
                problems.append(f"{path.name}:{n}: invalid JSON ({e.msg})")
                continue
            rid = str(r.get("id", ""))
            if rid in got:
                problems.append(f"{rid}: duplicate record")
            got[rid] = r
            parent = rid.rsplit(".", 1)[0] if re.search(r"\.\d+$", rid) else None
            if rid not in expected and not rid.startswith("X") and parent not in expected:
                problems.append(f"{rid}: not an item of {name} (extra findings use ids starting with X)")
            if rid in n_lines:
                codes = str(r.get("lines", ""))
                if len(codes) != n_lines[rid] or set(codes) - set("-nr"):
                    problems.append(f"{rid}: lines needs exactly {n_lines[rid]} codes from - n r (got {len(codes)})")
                if "verdict" not in r and n_lines[rid] > 0:
                    continue
            v = r.get("verdict")
            if v == "none":
                if not CODES.match(str(r.get("code", ""))):
                    problems.append(f"{rid}: none needs code no-trigger|noise|canonical|wrong|same-as:<id>")
                continue
            if v not in ("reading", "note"):
                problems.append(f"{rid}: verdict must be reading, note or none")
                continue
            for f in ("focus_ar", "trigger_ar", "trigger_ref", "after", "reason"):
                if not str(r.get(f, "")).strip():
                    problems.append(f"{rid}: {f} is empty")
            if v == "reading" and len(str(r.get("reason", ""))) < 60:
                problems.append(f"{rid}: reason too short for a reading (name the words and the image)")
            fa = loose(str(r.get("focus_ar", "")))[0].strip()
            if fa and fa not in focus:
                problems.append(f"{rid}: focus_ar {r['focus_ar']} is not in {focus_ref}")
            ref, ta = str(r.get("trigger_ref", "")).strip(), loose(str(r.get("trigger_ar", "")))[0].strip()
            if ref and not REF.match(ref):
                problems.append(f"{rid}: trigger_ref must be one S:A reference")
            elif ref and ta and ta not in q.get(ref, ""):
                problems.append(f"{rid}: trigger_ar {r['trigger_ar']} is not in {ref}")
            for key, seen in (("reason", seen_reason), ("after", seen_after)):
                k = norm(str(r.get(key, "")))
                if k and k in seen:
                    problems.append(f"{rid}: same {key} as {seen[k]} — write what is specific to this item")
                elif k:
                    seen[k] = rid
        problems += [f"{i}: missing record" for i in expected if i not in got]
        for iid, n in n_lines.items():
            codes = str(got.get(iid, {}).get("lines", ""))
            if len(codes) != n:
                continue
            for k, c in enumerate(codes, 1):
                sub = got.get(f"{iid}.{k}")
                if c in "nr" and not sub:
                    problems.append(f"{iid}.{k}: line coded {c} but has no record")
                elif c in "nr" and sub.get("verdict") != ("reading" if c == "r" else "note"):
                    problems.append(f"{iid}.{k}: verdict must be {'reading' if c == 'r' else 'note'} (line code {c})")
                elif c == "-" and sub:
                    problems.append(f"{iid}.{k}: has a record but its line code is -")
    return problems


def main() -> int:
    work = Path(sys.argv[1])
    names = sys.argv[2:] or sorted({l.split("\t")[1] for l in (work / "items.tsv").read_text(encoding="utf-8").splitlines() if l})
    problems = check(work, names, quran())
    for p in problems:
        print(p)
    print("ok" if not problems else f"{len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
