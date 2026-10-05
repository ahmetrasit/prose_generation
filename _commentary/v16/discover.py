#!/usr/bin/env python3
"""Prepare and merge image-based inter-ayah discovery packages.

Native Luna/Terra agents perform two turns in each same session; no model calls
are launched by this script. Use discovery_native.py for start/snapshot/audit/
finish bookkeeping. Every user-authorized rerun requires a fresh --run-tag.
Legacy CLI runner code remains below for historical inspection, but is blocked.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import v16 as V  # noqa: E402
import missing as M  # noqa: E402
import batch as B  # noqa: E402

MODELS = {"luna": "gpt-6-luna", "terra": "gpt-5.6-terra"}
EFFORT = "max"
STRENGTH = {"strong", "medium", "weak", "contrast"}
BASES = {"scene", "root", "theme", "speaker", "contrast", "neighbour"}
FOLLOWUP = ("Review your remembered coverage for qualifying omissions under the same inclusion and grading rules, "
            "checking the section's distinct scenes and secondary details, repeated formulations, specific indirect "
            "parallels, reversals, and necessary passage continuations. Append only previously unlisted ayah references "
            "using the same TSV schema. Keep existing bytes unchanged. Zero additions is valid. Do not read any files, "
            "retrieve sources, or run scripts; a file-write tool or a literal append-only shell write solely to save "
            "the rows is permitted. Do not regrade, sort, or rewrite the existing list. Return only a brief completion notice.")
SECTION = re.compile(r"(?m)^## (.+)$")
KAYNAK = re.compile(r"(?m)^Kaynaklar:\s*(.*)$")
MEMBER = re.compile(r"\s*(\d+:\d+)\s+(.+?)\s+([ء-ي](?:\s+[ء-ي]){2,3})\s+(B\d+(?:\s*,\s*B\d+)*)\s*")
TIMEOUT = 3 * 3600


def sections(text: str) -> list[dict]:
    """The `## ` sections of images.md in order: title, span, prose, the surah ayat named in Kaynaklar, the roots."""
    heads = list(SECTION.finditer(text))
    out = []
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        body = text[h.end():end]
        km = KAYNAK.search(body)
        members = []
        if km:
            for item in km.group(1).split(";"):
                m = MEMBER.fullmatch(item)
                if not m:
                    raise ValueError(f"section {i + 1}: unparsed Kaynaklar item: {item!r}")
                members.append({"ayah": m.group(1), "word": m.group(2), "root": " ".join(m.group(3).split()),
                                "branch": ", ".join(re.findall(r"B\d+", m.group(4)))})
        elif not h.group(1).strip().lower().startswith("buluşma"):
            raise ValueError(f"section {i + 1}: missing Kaynaklar line")
        prose = KAYNAK.sub("", body).strip()
        out.append({"k": i + 1, "title": h.group(1).strip(), "start": h.start(), "end": end, "prose": prose,
                    "members": members, "ayat": sorted({x["ayah"] for x in members}, key=lambda r: tuple(map(int, r.split(":")))),
                    "roots": sorted({x["root"] for x in members}), "meetings": h.group(1).strip().lower().startswith("buluşma")})
    return out


def surah_dir(s: int) -> Path:
    return HERE / "out" / f"s{s:03d}"


def discovery_dir(s: int, run_tag: str = "") -> Path:
    if run_tag and not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", run_tag):
        raise ValueError("run tag must contain only letters, digits, underscores or hyphens")
    base = surah_dir(s) / "discovery"
    return base / run_tag if run_tag else base


def package(s: int, sec: dict, q: dict[str, str]) -> str:
    n = sum(1 for a in range(1, 300) if f"{s}:{a}" in q)
    ayat = sec["ayat"] or [f"{s}:{a}" for a in range(1, n + 1)]
    lines = [f"# Surah {s}, image section {sec['k']}: {sec['title']}", "",
             "## The section's prose (Turkish commentary)", "", sec["prose"], "",
             "## The ayat of the surah this image rests on (Arabic)", ""]
    lines += [f"{r}\t{q.get(r, '')}" for r in ayat]
    lines += ["", "## Roots and words the section names (ayah, word, root, branch)", ""]
    lines += [f"{m['ayah']}\t{m['word']}\t{m['root']}\t{m['branch']}" for m in sec["members"]] or ["(none: a meetings section)"]
    lines += ["", f"## The whole surah {s} (Arabic)", ""]
    lines += [f"{s}:{a}\t{q[f'{s}:{a}']}" for a in range(1, n + 1)]
    return "\n".join(lines) + "\n"


def prompt_text(s: int, sec: dict, d: Path) -> str:
    t = (HERE / "prompts" / "discover" / "brief.md").read_text(encoding="utf-8")
    for k, v in {"{{PACKAGE_PATH}}": str(d / "package.md"), "{{OUTPUT_PATH}}": str(d / "list.tsv"),
                 "{{SURAH}}": str(s), "{{SECTION_TITLE}}": sec["title"]}.items():
        t = t.replace(k, v)
    assert "{{" not in t, "a placeholder was left in the discovery prompt"
    return t


def parse_rows(path: Path, s: int, q: dict[str, str]) -> tuple[list[dict], list[str]]:
    """Valid rows and the lines that break the schema (reported, never dropped silently)."""
    rows, bad = [], []
    if not path.exists():
        return rows, [f"missing deliverable: {path}"]
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        f = line.split("\t")
        if len(f) != 4:
            bad.append(f"line {i}: {len(f)} fields: {line[:120]}")
            continue
        strength, ref, basis, note = (x.strip() for x in f)
        bases = {b.strip() for b in basis.split("+")}
        if not note or strength not in STRENGTH or not re.fullmatch(r"\d+:\d+", ref) or ref not in q or not bases <= BASES:
            bad.append(f"line {i}: strength/ref/basis not in the schema: {line[:120]}")
            continue
        if ref.split(":")[0] == str(s):
            bad.append(f"line {i}: an ayah of surah {s} itself: {line[:120]}")
            continue
        rows.append({"line": i, "strength": strength, "ref": ref, "basis": sorted(bases), "note": note})
    return rows, bad


def codex(cmd: list[str], stdin: str | None, d: Path, name: str) -> tuple[int, str]:
    (d / f"{name}.command.json").write_text(json.dumps({"argv": cmd, "stdin": bool(stdin)}, indent=1) + "\n", encoding="utf-8")
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    try:
        p = subprocess.run(cmd, input=stdin, capture_output=True, text=True, env=env, timeout=TIMEOUT, cwd=d)
    except subprocess.TimeoutExpired as x:
        p = subprocess.CompletedProcess(cmd, -9, x.stdout or "", (x.stderr or "") + "\ntimed out")
    (d / f"{name}.stream.jsonl").write_text(p.stdout or "", encoding="utf-8")
    (d / f"{name}.stderr.log").write_text(p.stderr or "", encoding="utf-8")
    return p.returncode, p.stdout or ""


def stream_info(stdout: str) -> dict:
    tid, usage, completed, commands = None, {}, False, 0
    for line in stdout.splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        tid = tid or ev.get("thread_id")
        if ev.get("type") == "turn.completed":
            completed, usage = True, ev.get("usage") or {}
        if ev.get("type") == "item.completed" and (ev.get("item") or {}).get("type") == "command_execution":
            commands += 1
    return {"thread_id": tid, "usage": usage, "completed": completed, "commands": commands}


def run(s: int, sec: dict, model: str, q: dict[str, str], run_tag: str = "") -> dict:
    raise RuntimeError("Legacy script-run discovery is disabled; spawn native agents")
    d = discovery_dir(s, run_tag) / f"sec{sec['k']}" / model
    if V.blocked(d):
        return {"sec": sec["k"], "model": model, "status": "skipped", "why": "started or finished before (never rerun)"}
    d.mkdir(parents=True, exist_ok=True)
    (d / "package.md").write_text(package(s, sec, q), encoding="utf-8")
    text = prompt_text(s, sec, d)
    (d / "prompt.md").write_text(text, encoding="utf-8")
    (d / "started.json").write_text(json.dumps({"started": time.strftime("%Y-%m-%dT%H:%M:%S"), "model": MODELS[model],
                                                "effort": EFFORT, "runner": "codex"}) + "\n", encoding="utf-8")
    t0 = time.time()
    cmd1 = ["codex", "exec", "--ignore-user-config", "-m", MODELS[model], "-c", f'model_reasoning_effort="{EFFORT}"',
            "-c", 'web_search="disabled"', "--disable", "skill_search", "--skip-git-repo-check", "-s", "workspace-write",
            "--json", "-o", str(d / "turn1.last.md"), "-C", str(d), "-"]
    rc1, out1 = codex(cmd1, text, d, "turn1")
    i1 = stream_info(out1)
    rows1, bad1 = parse_rows(d / "list.tsv", s, q)
    row = {"ref": f"S{s}", "arm": "discover", "brief": f"discover1.{model}.sec{sec['k']}", "model": MODELS[model],
           "effort": EFFORT, "runner": "codex", "cost_usd": 0.0, "section": sec["title"],
           "turn1": {"returncode": rc1, **i1, "rows": len(rows1), "bad_rows": len(bad1)}}
    status = "ok"
    if rc1 != 0 or not i1["completed"] or not rows1:
        status = "error"
        print(f"WARNING: S{s} sec{sec['k']} {model} turn 1: exit {rc1}, completed {i1['completed']}, {len(rows1)} valid rows; "
              "no follow-up sent")
    elif not i1["thread_id"]:
        status = "error"
        print(f"WARNING: S{s} sec{sec['k']} {model}: no thread id in the stream; the follow-up turn cannot be sent")
    else:
        cmd2 = ["codex", "exec", "resume", i1["thread_id"], "--skip-git-repo-check", "--json",
                "-o", str(d / "turn2.last.md"), FOLLOWUP]
        rc2, out2 = codex(cmd2, None, d, "turn2")
        i2 = stream_info(out2)
        rows2, bad2 = parse_rows(d / "list.tsv", s, q)
        row["turn2"] = {"returncode": rc2, **i2, "rows_total": len(rows2), "rows_added": len(rows2) - len(rows1),
                        "bad_rows": len(bad2)}
        if rc2 != 0 or not i2["completed"]:
            status = "partial"
            print(f"WARNING: S{s} sec{sec['k']} {model} turn 2 (missing ayat): exit {rc2}, completed {i2['completed']}; "
                  "turn 1's list stands, the follow-up is missing")
        for b in bad2:
            print(f"WARNING: S{s} sec{sec['k']} {model}: row outside the schema (kept in list.tsv, left out of the merge): {b}")
        row["turn1_rows"] = len(rows1)
    for b in bad1 if status == "error" else []:
        print(f"WARNING: S{s} sec{sec['k']} {model}: row outside the schema: {b}")
    row.update({"status": status, "run_tag": run_tag, "seconds": round(time.time() - t0)})
    (d / "run.log.json").write_text(json.dumps(row, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    V.log(row)
    print(f"S{s} sec{sec['k']} {model}: {status} rows {row.get('turn2', {}).get('rows_total', len(rows1))} "
          f"(turn 1 {len(rows1)}) {row['seconds']}s")
    return row


def merge(s: int, secs: list[dict], q: dict[str, str], run_tag: str = "") -> None:
    order = {"strong": 0, "medium": 1, "weak": 2, "contrast": 3}
    for sec in secs:
        base = discovery_dir(s, run_tag) / f"sec{sec['k']}"
        per = {}
        for model in MODELS:
            f = base / model / "list.tsv"
            if not (base / model / "run.log.json").exists():
                raise ValueError(f"S{s} sec{sec['k']}: missing finished {model} run; no partial merge")
            rows, bad = parse_rows(f, s, q)
            log = json.loads((base / model / "run.log.json").read_text(encoding="utf-8"))
            first_path = base / model / "turn1.list.tsv"
            if (log.get("status") != "ok" or not log.get("turn2", {}).get("completed")
                    or bad or len({r["ref"] for r in rows}) != len(rows) or not first_path.exists()):
                raise ValueError(f"S{s} sec{sec['k']} {model}: incomplete or invalid discovery run")
            original = first_path.read_bytes()
            if not f.read_bytes().startswith(original) or not log.get("append_only"):
                raise ValueError(f"S{s} sec{sec['k']} {model}: first-turn prefix changed")
            if log.get("protocol_findings") or (log.get("tool_audit_reviewed") is not True and
                    not (base / model / "protocol_review.json").exists()):
                raise ValueError(f"S{s} sec{sec['k']} {model}: unresolved protocol findings")
            first_rows, first_bad = parse_rows(first_path, s, q)
            if first_bad:
                raise ValueError(f"S{s} sec{sec['k']} {model}: invalid first-turn snapshot")
            first_refs = {r["ref"] for r in first_rows}
            per[model] = {r["ref"]: {**r, "turn": 1 if r["ref"] in first_refs else 2} for r in rows}
        if not per:
            print(f"WARNING: S{s} sec{sec['k']}: no discovery list at all; nothing merged")
            continue
        refs = sorted({r for m in per.values() for r in m}, key=lambda r: tuple(map(int, r.split(":"))))
        lines = ["ref\ttier\t" + "\t".join(f"{m}_label\t{m}_turn" for m in per) + "\tbases\texplanations"]
        for r in refs:
            labels = [per[m][r]["strength"] for m in per if r in per[m]]
            tier = "contrast" if labels and all(l == "contrast" for l in labels) else min(
                (l for l in labels if l != "contrast"), key=order.get, default="contrast")
            bases = sorted({b for m in per if r in per[m] for b in per[m][r]["basis"]})
            notes = " | ".join(f"{m}: {per[m][r]['note']}" for m in per if r in per[m])
            cells = []
            for m in per:
                cells += [per[m][r]["strength"] if r in per[m] else "", str(per[m][r]["turn"]) if r in per[m] else ""]
            lines.append("\t".join([r, tier, *cells, "+".join(bases), notes]))
        (base.with_name(f"sec{sec['k']}.merged.tsv")).write_text("\n".join(lines) + "\n", encoding="utf-8")
        import hashlib
        merged_file = base.with_name(f"sec{sec['k']}.merged.tsv")
        source_hashes = {json.loads((base / m / "run.log.json").read_text()).get("source_sha256") for m in per}
        if len(source_hashes) != 1:
            raise ValueError("Model runs used different source commentary versions")
        audit = {"surah": s, "section": sec["k"], "run_tag": run_tag,
                 "source_sha256": next(iter(source_hashes)),
                 "list_sha256": hashlib.sha256(merged_file.read_bytes()).hexdigest(),
                 "models": {m: {"run_log": str(base / m / "run.log.json"),
                                 "validation_review": json.loads((base / m / "validation_review.json").read_text())
                                 if (base / m / "validation_review.json").exists() else None,
                                 "validation": json.loads((base / m / "validation.json").read_text())
                                 if (base / m / "validation.json").exists() else None}
                            for m in per}}
        merged_file.with_suffix(".audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
        both = sum(1 for r in refs if all(r in per[m] for m in per)) if len(per) > 1 else None
        print(f"S{s} sec{sec['k']} '{sec['title']}': merged {len(refs)} passages from {', '.join(per)}"
              + (f", {both} named by both" if both is not None else ""))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--surah", type=int, required=True)
    ap.add_argument("--sections", help="e.g. 1,3; default every section")
    ap.add_argument("--models", default=",".join(MODELS))
    ap.add_argument("--run-tag", default="", help="isolated attempt directory; never overwrites an earlier run")
    ap.add_argument("--parallel", type=int, default=2)
    ap.add_argument("--go", action="store_true")
    ap.add_argument("--merge", action="store_true")
    ap.add_argument("--status", action="store_true")
    a = ap.parse_args()
    if a.go:
        raise SystemExit("BLOCKED: discovery model calls must use native agents; use discovery_native.py for bookkeeping")
    root = discovery_dir(a.surah, a.run_tag)
    _, images, _ = B.surah_inputs(a.surah)
    text = images.read_text(encoding="utf-8")
    secs = sections(text)
    if a.sections:
        want = {int(x) for x in a.sections.split(",")}
        secs = [x for x in secs if x["k"] in want]
    q = M.verses()
    models = [m.strip() for m in a.models.split(",")]
    for m in models:
        if m not in MODELS:
            raise SystemExit(f"unknown model {m}; known: {', '.join(MODELS)}")
    if a.status or a.merge:
        for sec in secs:
            base = root / f"sec{sec['k']}"
            st = []
            for m in MODELS:
                d = base / m
                if (d / "run.log.json").exists():
                    log = json.loads((d / "run.log.json").read_text())
                    state = f"{log.get('status', 'unknown')} (check: {log.get('check', 'unknown')})"
                else:
                    state = "BLOCKED (started)" if V.blocked(d) else "-"
                st.append(f"{m}: {state}")
            print(f"S{a.surah} sec{sec['k']} '{sec['title']}' ({len(sec['ayat'])} ayat, {len(sec['roots'])} roots): "
                  + "; ".join(st) + ("; merged" if base.with_name(f"sec{sec['k']}.merged.tsv").exists() else ""))
        if a.merge:
            merge(a.surah, secs, q, a.run_tag)
        return
    jobs = []
    for sec in secs:
        for m in models:
            d = root / f"sec{sec['k']}" / m
            if V.blocked(d):
                print(f"NOTE: S{a.surah} sec{sec['k']} {m}: started or finished before, skipped (never rerun)")
                continue
            jobs.append((sec, m))
            if not a.go:
                d.mkdir(parents=True, exist_ok=True)
                (d / "package.md").write_text(package(a.surah, sec, q), encoding="utf-8")
                (d / "prompt.md").write_text(prompt_text(a.surah, sec, d), encoding="utf-8")
                print(f"S{a.surah} sec{sec['k']} '{sec['title']}' {m} ({MODELS[m]}, {EFFORT}): package "
                      f"{len((d / 'package.md').read_text(encoding='utf-8')):,} chars -> {d.relative_to(V.HERE)}")
    print(f"{len(jobs)} call(s)" + ("" if a.go else "; spawn native agents using discovery_native.py (Codex subscription, no USD)"))
    if not a.go or not jobs:
        return
    with ThreadPoolExecutor(a.parallel) as ex:
        results = list(ex.map(lambda j: run(a.surah, j[0], j[1], q, a.run_tag), jobs))
    bad = [r for r in results if r.get("status") not in ("ok",)]
    print(f"{len(results)} run(s): {len(results) - len(bad)} ok" + (f", {len(bad)} not ok: " + ", ".join(
        f"sec{r['sec'] if 'sec' in r else r['brief']} {r.get('model', '')} {r['status']}" for r in bad) if bad else ""))
    if bad:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
