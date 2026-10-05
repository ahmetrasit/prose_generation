#!/usr/bin/env python3
"""The Bible discovery for the enrichment's Bible pass (user, 2026-10-04 evening), the sibling of discover.py's
image discovery: per ayah reading and per image section of a surah, GPT agents (Luna max, Terra max, two turns each)
name the Hebrew Bible, New Testament, Jewish and Christian texts the commentary activates (paralel, motif,
karsi_anlati, soydas, yorum_gelenegi), merged into one list per page that the Bible-pass agent (enrich.py --pass
ehlikitap) reads as its seed, and prefetched from Sefaria so the page agent, which has no network, finds the texts
in the intertext index.

  python3 -B _commentary/v16/discover_bible.py --surah 1                         # packages and prompts, no call
  python3 -B _commentary/v16/discover_bible.py --surah 1 --go                    # every ayah with a reading and every section x luna, terra
  python3 -B _commentary/v16/discover_bible.py --surah 1 --targets 1:1,sec1 --models luna --go
  python3 -B _commentary/v16/discover_bible.py --surah 1 --merge --prefetch      # <target>.merged.tsv + Sefaria texts
  python3 -B _commentary/v16/discover_bible.py --surah 1 --status

Output: out/sNNN/discovery_bible/<S_A | secK>/<model>/ (package.md, prompt.md, list.tsv, streams, run.log.json;
blocked by started.json) and out/sNNN/discovery_bible/<S_A | secK>.merged.tsv. Then `corpus.py --intertext build`.
"""
from __future__ import annotations

import argparse
import json
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
import discover as DS  # noqa: E402

ROOT_PG = HERE.parents[1]
MODELS, EFFORT, FOLLOWUP = DS.MODELS, DS.EFFORT, DS.FOLLOWUP
STRENGTH = {"strong", "medium", "weak"}
TRAD = {"tevrat", "incil"}
KIND = {"paralel", "motif", "karsi_anlati", "soydas", "yorum_gelenegi"}
OSIS = re.compile(r"^(?:[1-4]?[A-Z][A-Za-z]{1,6})\.\d+\.\d+$")


def targets_of(s: int, text: str, run_dir: str) -> list[dict]:
    """Every ayah with a finished reading (target S:A) and every image section (target secK)."""
    out, q = [], M.verses()
    n = sum(1 for a in range(1, 300) if f"{s}:{a}" in q)
    for a in range(1, n + 1):
        ref = f"{s}:{a}"
        f = HERE / "out" / f"{s}_{a}" / run_dir / f"{s}_{a}.reading.tr.md"
        if f.exists():
            out.append({"target": ref, "ayat": [ref], "prose": f.read_text(encoding="utf-8"),
                        "what": f"ayah {ref}, with the commentary written on it"})
        else:
            print(f"NOTE: {ref}: no finished reading; no Bible discovery for it")
    for sec in DS.sections(text):
        out.append({"target": f"sec{sec['k']}", "ayat": sec["ayat"] or [f"{s}:{a}" for a in range(1, n + 1)],
                    "prose": sec["prose"], "what": f"image section {sec['k']} (\"{sec['title']}\") of the surah commentary"})
    return out


def package(s: int, t: dict, q: dict[str, str]) -> str:
    n = sum(1 for a in range(1, 300) if f"{s}:{a}" in q)
    lines = [f"# Surah {s}: {t['what']}", "", "## The ayat concerned (Arabic)", ""]
    lines += [f"{r}\t{q.get(r, '')}" for r in t["ayat"]]
    lines += ["", "## The commentary (Turkish)", "", t["prose"].strip(), "", f"## The whole surah {s} (Arabic)", ""]
    lines += [f"{s}:{a}\t{q[f'{s}:{a}']}" for a in range(1, n + 1)]
    return "\n".join(lines) + "\n"


def prompt_text(s: int, t: dict, d: Path) -> str:
    tpl = (HERE / "prompts" / "discover" / "bible.md").read_text(encoding="utf-8")
    for k, v in {"{{PACKAGE_PATH}}": str(d / "package.md"), "{{OUTPUT_PATH}}": str(d / "list.tsv"),
                 "{{SURAH}}": str(s), "{{WHAT}}": t["what"]}.items():
        tpl = tpl.replace(k, v)
    assert "{{" not in tpl, "a placeholder was left in the Bible discovery prompt"
    return tpl


def parse_rows(path: Path) -> tuple[list[dict], list[str]]:
    rows, bad = [], []
    if not path.exists():
        return rows, bad
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        f = [x.strip() for x in line.split("\t")]
        if len(f) != 6:
            bad.append(f"line {i}: {len(f)} fields: {line[:120]}")
            continue
        strength, trad, kind, ref, basis, note = f
        if strength not in STRENGTH or trad not in TRAD or kind not in KIND or not ref:
            bad.append(f"line {i}: strength/tradition/kind/ref not in the schema: {line[:120]}")
            continue
        rows.append({"line": i, "strength": strength, "tradition": trad, "kind": kind, "ref": ref,
                     "osis": bool(OSIS.match(ref)), "basis": basis, "note": note})
    return rows, bad


def tdir(s: int, target: str) -> Path:
    return DS.surah_dir(s) / "discovery_bible" / target.replace(":", "_")


def run(s: int, t: dict, model: str, q: dict[str, str]) -> dict:
    d = tdir(s, t["target"]) / model
    if V.blocked(d):
        return {"target": t["target"], "model": model, "status": "skipped", "why": "started or finished before (never rerun)"}
    d.mkdir(parents=True, exist_ok=True)
    (d / "package.md").write_text(package(s, t, q), encoding="utf-8")
    text = prompt_text(s, t, d)
    (d / "prompt.md").write_text(text, encoding="utf-8")
    (d / "started.json").write_text(json.dumps({"started": time.strftime("%Y-%m-%dT%H:%M:%S"), "model": MODELS[model],
                                                "effort": EFFORT, "runner": "codex"}) + "\n", encoding="utf-8")
    t0 = time.time()
    cmd1 = ["codex", "exec", "--ignore-user-config", "-m", MODELS[model], "-c", f'model_reasoning_effort="{EFFORT}"',
            "-c", 'web_search="disabled"', "--disable", "skill_search", "--skip-git-repo-check", "-s", "workspace-write",
            "--json", "-o", str(d / "turn1.last.md"), "-C", str(d), "-"]
    rc1, out1 = DS.codex(cmd1, text, d, "turn1")
    i1 = DS.stream_info(out1)
    rows1, bad1 = parse_rows(d / "list.tsv")
    row = {"ref": f"S{s}", "arm": "discover-bible", "brief": f"bible1.{model}.{t['target']}", "model": MODELS[model],
           "effort": EFFORT, "runner": "codex", "cost_usd": 0.0, "target": t["target"],
           "turn1": {"returncode": rc1, **i1, "rows": len(rows1), "bad_rows": len(bad1)}}
    status = "ok"
    if rc1 != 0 or not i1["completed"] or not rows1:
        status = "error"
        print(f"WARNING: S{s} {t['target']} {model} turn 1: exit {rc1}, completed {i1['completed']}, {len(rows1)} valid rows; "
              "no follow-up sent")
    elif not i1["thread_id"]:
        status = "error"
        print(f"WARNING: S{s} {t['target']} {model}: no thread id in the stream; the follow-up turn cannot be sent")
    else:
        cmd2 = ["codex", "exec", "resume", i1["thread_id"], "--skip-git-repo-check", "--json",
                "-o", str(d / "turn2.last.md"), FOLLOWUP]
        rc2, out2 = DS.codex(cmd2, None, d, "turn2")
        i2 = DS.stream_info(out2)
        rows2, bad2 = parse_rows(d / "list.tsv")
        row["turn2"] = {"returncode": rc2, **i2, "rows_total": len(rows2), "rows_added": len(rows2) - len(rows1),
                        "bad_rows": len(bad2)}
        if rc2 != 0 or not i2["completed"]:
            status = "partial"
            print(f"WARNING: S{s} {t['target']} {model} turn 2 (missing texts): exit {rc2}, completed {i2['completed']}; "
                  "turn 1's list stands")
        for b in bad2:
            print(f"WARNING: S{s} {t['target']} {model}: row outside the schema (kept in list.tsv, left out of the merge): {b}")
        row["turn1_rows"] = len(rows1)
    for b in bad1 if status == "error" else []:
        print(f"WARNING: S{s} {t['target']} {model}: row outside the schema: {b}")
    row.update({"status": status, "seconds": round(time.time() - t0)})
    (d / "run.log.json").write_text(json.dumps(row, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    V.log(row)
    print(f"S{s} {t['target']} {model}: {status} rows {row.get('turn2', {}).get('rows_total', len(rows1))} "
          f"(turn 1 {len(rows1)}) {row['seconds']}s")
    return row


def merge(s: int, targets: list[dict]) -> list[Path]:
    order = {"strong": 0, "medium": 1, "weak": 2}
    out = []
    for t in targets:
        base = tdir(s, t["target"])
        per: dict[str, dict] = {}
        for model in MODELS:
            if not (base / model / "run.log.json").exists():
                print(f"NOTE: S{s} {t['target']}: no finished {model} run; merged without it")
                continue
            rows, _ = parse_rows(base / model / "list.tsv")
            log = json.loads((base / model / "run.log.json").read_text(encoding="utf-8"))
            n1 = log.get("turn1_rows", len(rows))
            per[model] = {}
            for r in rows:
                per[model].setdefault(r["ref"], {**r, "turn": 1 if r["line"] <= n1 or n1 == 0 else 2})
        if not per:
            print(f"WARNING: S{s} {t['target']}: no Bible discovery list; nothing merged")
            continue
        refs = sorted({r for m in per.values() for r in m})
        lines = ["ref\ttier\ttradition\tkinds\t" + "\t".join(f"{m}_label\t{m}_turn" for m in per) + "\tbasis\texplanations"]
        for r in refs:
            got = [per[m][r] for m in per if r in per[m]]
            tier = min((g["strength"] for g in got), key=order.get)
            trad = "|".join(sorted({g["tradition"] for g in got}))
            kinds = "|".join(sorted({g["kind"] for g in got}))
            cells = []
            for m in per:
                cells += [per[m][r]["strength"] if r in per[m] else "", str(per[m][r]["turn"]) if r in per[m] else ""]
            basis = " | ".join(dict.fromkeys(g["basis"] for g in got))
            notes = " | ".join(f"{m}: {per[m][r]['note']}" for m in per if r in per[m])
            lines.append("\t".join([r, tier, trad, kinds, *cells, basis, notes]))
        f = base.with_name(base.name + ".merged.tsv")
        f.write_text("\n".join(lines) + "\n", encoding="utf-8")
        both = sum(1 for r in refs if all(r in per[m] for m in per)) if len(per) > 1 else None
        print(f"S{s} {t['target']}: merged {len(refs)} texts from {', '.join(per)}"
              + (f", {both} named by both" if both is not None else ""))
        out.append(f)
    return out


def prefetch(merged: list[Path], per_type: int) -> None:
    """The Sefaria texts the merged lists name, fetched before any page call (the agents have no network): Tanakh
    verses get their Targum, midrash, Talmud and commentary links; other Jewish texts are fetched by name; every
    failure is printed by the fetcher. New Testament and Christian texts come from SBLGNT and KJV, or from memory."""
    sys.path.insert(0, str(ROOT_PG / "enrichment" / "v2" / "fetch"))
    import bible_text as BT
    related, named = set(), set()
    for f in merged:
        for line in f.read_text(encoding="utf-8").splitlines()[1:]:
            c = line.split("\t")
            ref, trad = c[0], c[2]
            if OSIS.match(ref):
                b, ch, v = ref.split(".")
                if b in BT.WLC_BOOKS:
                    related.add(f"{BT.NAMES[b]} {ch}:{v}")
            elif "tevrat" in trad:
                named.add(ref)
    print(f"prefetch: {len(related)} Tanakh verses (their related texts, {per_type} per type), {len(named)} named Jewish texts")
    fetcher = ROOT_PG / "enrichment" / "v2" / "fetch" / "bible_sefaria.py"
    for ref in sorted(related):
        subprocess.run([sys.executable, "-B", str(fetcher), "related", ref, "--n", str(per_type)], cwd=ROOT_PG)
    if named:
        subprocess.run([sys.executable, "-B", str(fetcher), "text", *sorted(named)], cwd=ROOT_PG)
    print("then: python3 -B enrichment/v2/tools/corpus.py --intertext build")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--surah", type=int, required=True)
    ap.add_argument("--targets", help="e.g. 1:1,sec3; default every ayah with a reading and every section")
    ap.add_argument("--models", default=",".join(MODELS))
    ap.add_argument("--parallel", type=int, default=2)
    ap.add_argument("--go", action="store_true")
    ap.add_argument("--merge", action="store_true")
    ap.add_argument("--prefetch", action="store_true", help="with --merge: fetch the Sefaria texts the lists name")
    ap.add_argument("--per-type", type=int, default=6)
    ap.add_argument("--status", action="store_true")
    a = ap.parse_args()
    _, images, run_dir = B.surah_inputs(a.surah)
    text = images.read_text(encoding="utf-8")
    q = M.verses()
    targets = targets_of(a.surah, text, run_dir)
    if a.targets:
        want = set(a.targets.split(","))
        targets = [t for t in targets if t["target"] in want]
    models = [m.strip() for m in a.models.split(",")]
    for m in models:
        if m not in MODELS:
            raise SystemExit(f"unknown model {m}; known: {', '.join(MODELS)}")
    if a.status or a.merge:
        for t in targets:
            base = tdir(a.surah, t["target"])
            st = [f"{m}: " + ("done" if (base / m / "run.log.json").exists() else "BLOCKED" if V.blocked(base / m) else "-")
                  for m in MODELS]
            print(f"S{a.surah} {t['target']}: " + "; ".join(st)
                  + ("; merged" if base.with_name(base.name + ".merged.tsv").exists() else ""))
        if a.merge:
            merged = merge(a.surah, targets)
            if a.prefetch:
                prefetch(merged, a.per_type)
        return
    jobs = []
    for t in targets:
        for m in models:
            d = tdir(a.surah, t["target"]) / m
            if V.blocked(d):
                print(f"NOTE: S{a.surah} {t['target']} {m}: started or finished before, skipped (never rerun)")
                continue
            jobs.append((t, m))
            if not a.go:
                d.mkdir(parents=True, exist_ok=True)
                (d / "package.md").write_text(package(a.surah, t, q), encoding="utf-8")
                (d / "prompt.md").write_text(prompt_text(a.surah, t, d), encoding="utf-8")
                print(f"S{a.surah} {t['target']} {m} ({MODELS[m]}, {EFFORT}): package "
                      f"{len((d / 'package.md').read_text(encoding='utf-8')):,} chars -> {d.relative_to(V.HERE)}")
    print(f"{len(jobs)} call(s)" + ("" if a.go else "; add --go to run them (Codex subscription, no USD)"))
    if not a.go or not jobs:
        return
    with ThreadPoolExecutor(a.parallel) as ex:
        results = list(ex.map(lambda j: run(a.surah, j[0], j[1], q), jobs))
    bad = [r for r in results if r.get("status") != "ok"]
    print(f"{len(results)} run(s): {len(results) - len(bad)} ok" + (f", {len(bad)} not ok" if bad else ""))
    if bad:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
