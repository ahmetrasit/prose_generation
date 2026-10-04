#!/usr/bin/env python3
"""Enrichment v2 orchestrator (v16-like, after v16's augment step): one agent call per page, never rerun.

A target is a page: the surah page (`surah`) or one ayah page (`107:3`). Per surah, once:
  paket   script   pack.py: the reference pack (frozen base, binding, dictionary, lexica, usage, meals, locators)
Per target:
  zengin  agent    one call (prompts/common.md + prompts/zengin.md): research, meal review and composition, grounded
                   in the pack and the corpus files; writes the page's records (annotations.jsonl) and gaps.json
  then    script   every record checked (validate.py); a failing record is dropped and listed in check.json, never
                   sent back; the rest rendered into the frozen base (render.py); the page checked byte-exact against
                   the base; copied to out/sNNN/ (never overwritten); duzeltme records appended to errata.jsonl

Agent calls run `codex exec` (GPT-6 Astra by default) with the call directory as the only writable place and no
network. Rules as in v16: a call directory with started.json is never run again (--attempt N for a deliberate new
attempt, which gets its own directory); every call is logged in work/ledger.jsonl with its prompt hash.

  python3 enrichment/v2/enrich.py status --surah 107
  python3 enrichment/v2/enrich.py build  --surah 107 [--target 107:3]       (writes nothing; sizes the prompts)
  python3 enrichment/v2/enrich.py run    --surah 107 [--target surah] [--effort high|max] [--attempt 2]
  python3 enrichment/v2/enrich.py run    --surahs 87-114 --parallel 3
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

V2 = Path(__file__).resolve().parent
PG = V2.parents[1]
WORK = V2 / "work"
OUT = V2 / "out"
PROMPTS = V2 / "prompts"
LEDGER = WORK / "ledger.jsonl"
ERRATA = V2 / "errata.jsonl"
MODEL, EFFORT = "gpt-6-astra", "high"
BRIEF = "zengin"

sys.path.insert(0, str(V2))
import render as R  # noqa: E402
import validate as VAL  # noqa: E402


def wd(s: int) -> Path:
    return WORK / f"s{s:03d}"


def sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def log(row: dict) -> None:
    WORK.mkdir(parents=True, exist_ok=True)
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def rel(p: Path) -> str:
    return str(p.relative_to(PG)) if p.is_relative_to(PG) else str(p)


def tag(target: str) -> str:
    return target.replace(":", "_")


def call_dir(s: int, target: str, attempt: int = 1) -> Path:
    return wd(s) / f"{BRIEF}.{tag(target)}" if attempt == 1 else wd(s) / f"{BRIEF}.{tag(target)}.a{attempt}"


def page_name(s: int, target: str) -> str:
    return "surah.md" if target == "surah" else f"{tag(target)}.md"


def accepted(s: int, target: str) -> bool:
    return (OUT / f"s{s:03d}" / page_name(s, target)).exists()


def blocked(d: Path) -> bool:
    return (d / "started.json").exists() or (d / "run.log.json").exists()


def targets(s: int) -> list[str]:
    """The surah page and every ayah page that has a base."""
    base = json.loads((wd(s) / "pack" / "base.json").read_text(encoding="utf-8"))
    return ["surah"] + [ref for ref, info in base["ayat"].items() if info]


# ---------------------------------------------------------------- prompt

def header(s: int, target: str, d: Path) -> str:
    pack = wd(s) / "pack"
    n = json.loads((pack / "pack.json").read_text(encoding="utf-8"))["ayat"]
    name = page_name(s, target)
    if target == "surah":
        what = f"the surah page of S{s} (base PACK/numbered/surah.md; all ayat 1–{n})"
    else:
        what = (f"the ayah page of {target} (base PACK/numbered/{name}; ayah files PACK/ayah/{tag(target)}/); "
                f"every record's ayet must include {target}")
    return "\n".join([
        "# Job", "",
        f"- Surah: {s} (ayat 1–{n}); ids use S{s:03d}",
        f"- Target: {target} — {what}",
        f"- Workspace root: {PG}", f"- PACK: {pack}",
        f"- Your call directory (write only here): {d}",
        f"- Schema: {V2 / 'schema.json'} and {V2 / 'SCHEMA.md'}",
        f"- Corpus tool: python3 {V2 / 'tools' / 'corpus.py'}",
        f"- Validator: python3 {V2 / 'validate.py'} --surah {s} --target {target} --annotations "
        f"{d / 'annotations.jsonl'}",
        f"- Renderer (preview): python3 {V2 / 'render.py'} --surah {s} --target {target} --annotations "
        f"{d / 'annotations.jsonl'} --out {d / 'preview'}",
    ]) + "\n"


def build_prompt(s: int, target: str, d: Path) -> str:
    return "\n\n".join([header(s, target, d), (PROMPTS / "common.md").read_text(encoding="utf-8"),
                        (PROMPTS / f"{BRIEF}.md").read_text(encoding="utf-8")])


# ---------------------------------------------------------------- call

def call_codex(prompt: str, d: Path, model: str, effort: str) -> dict:
    last = d / "response.md"
    cmd = ["codex", "exec", "--ignore-user-config", "-m", model, "-c", f'model_reasoning_effort="{effort}"',
           "-c", 'web_search="disabled"', "--disable", "skill_search", "--skip-git-repo-check", "--ephemeral",
           "-s", "workspace-write", "--json", "-o", str(last), "-C", str(d), "-"]
    (d / "command.json").write_text(json.dumps({"argv": cmd, "stdin": "prompt.md"}, indent=1) + "\n", encoding="utf-8")
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    with (d / "run.stream.jsonl").open("w", encoding="utf-8") as out, (d / "stderr.log").open("w") as err:
        p = subprocess.run(cmd, input=prompt, text=True, stdout=out, stderr=err, env=env)
    usage, completed, tools = {}, False, 0
    for line in (d / "run.stream.jsonl").read_text(encoding="utf-8").splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "turn.completed":
            completed, usage = True, ev.get("usage") or {}
        if ev.get("type") == "item.completed" and (ev.get("item") or {}).get("type") == "command_execution":
            tools += 1
    return {"returncode": p.returncode, "turn_completed": completed, "usage": usage, "commands": tools}


def finish(s: int, target: str, d: Path) -> dict:
    """Check the records, drop the failing ones, render, check the page, accept. Nothing goes back to the agent."""
    ann = d / "annotations.jsonl"
    if not ann.exists():
        return {"check": "no annotations.jsonl", "ok": False}
    try:
        recs = R.load(ann)
    except SystemExit as e:
        return {"check": f"annotations.jsonl unreadable: {e}", "ok": False}
    kept, dropped, warnings = VAL.check_records(s, target, recs)
    page_dir = d / "page"
    if page_dir.exists():
        shutil.rmtree(page_dir)
    page, placement = R.render(s, target, kept, page_dir)
    name, base, info = R.target_page(s, target)
    page_errors = VAL.check_page(page, base, kept) + placement
    check = {"surah": s, "target": target, "records": len(recs), "kept": len(kept), "dropped": dropped,
             "warnings": warnings, "page_errors": page_errors}
    (d / "check.json").write_text(json.dumps(check, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if page_errors:
        return {"check": f"page errors: {len(page_errors)} (see check.json)", "ok": False,
                "kept": len(kept), "dropped": len(dropped)}
    dst = OUT / f"s{s:03d}" / name
    if dst.exists():
        return {"check": f"{rel(dst)} exists (never overwrite)", "ok": False}
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(page, dst)
    pack = json.loads((wd(s) / "pack" / "pack.json").read_text(encoding="utf-8"))
    rec = {"surah": s, "target": target, "accepted_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
           "page_sha256": hashlib.sha256(dst.read_bytes()).hexdigest(), "base": info,
           "dictionary": pack.get("dictionary"), "annotations": rel(ann),
           "kept": len(kept), "dropped": [x["id"] for x in dropped]}
    dst.with_suffix(".json").write_text(json.dumps(rec, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    errata = [r for r in kept if r.get("tur") == "duzeltme"]
    with ERRATA.open("a", encoding="utf-8") as f:
        for r in errata:
            f.write(json.dumps({"surah": s, "target": target, "base": info["path"], "id": r["id"], "taban": r.get("taban"),
                                "hata": r.get("hata"), "metin": r.get("metin"), "kaynak": r.get("kaynak")},
                               ensure_ascii=False) + "\n")
    return {"check": "ok", "ok": True, "kept": len(kept), "dropped": len(dropped), "errata": len(errata)}


def run_target(s: int, target: str, model: str, effort: str, attempt: int = 1) -> dict:
    d = call_dir(s, target, attempt)
    if blocked(d):
        return {"surah": s, "target": target, "status": "skipped", "reason": "started or finished before (never rerun)"}
    if accepted(s, target):
        return {"surah": s, "target": target, "status": "skipped", "reason": "page already accepted"}
    d.mkdir(parents=True, exist_ok=True)
    prompt = build_prompt(s, target, d)
    row = {"surah": s, "target": target, "attempt": attempt, "brief": BRIEF, "model": model, "effort": effort,
           "prompt_sha256": sha(prompt), "prompt_chars": len(prompt), "started": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    with (d / "started.json").open("x", encoding="utf-8") as f:
        json.dump(row, f, ensure_ascii=False, indent=1)
    (d / "prompt.md").write_text(prompt, encoding="utf-8")
    t0 = time.monotonic()
    try:
        row.update(call_codex(prompt, d, model, effort))
        res = finish(s, target, d) if row["returncode"] == 0 and row["turn_completed"] else \
            {"check": "call did not complete", "ok": False}
        row["status"] = "ok" if res.pop("ok") else "error"
        row.update(res)
    except Exception as e:  # keep the record; never retry automatically
        row.update(status="error", error=f"{type(e).__name__}: {e}")
    row["seconds"] = round(time.monotonic() - t0)
    (d / "run.log.json").write_text(json.dumps(row, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log(row)
    return row


def ensure_pack(s: int) -> bool:
    if (wd(s) / "pack" / "pack.json").exists():
        return True
    p = subprocess.run([sys.executable, "-B", str(V2 / "pack.py"), "--surah", str(s)], capture_output=True, text=True)
    log({"surah": s, "stage": "paket", "status": "ok" if p.returncode == 0 else "error",
         "out": (p.stdout + p.stderr)[-1500:], "at": time.strftime("%Y-%m-%dT%H:%M:%S%z")})
    if p.returncode:
        print(json.dumps({"surah": s, "stage": "paket", "status": "error", "out": (p.stdout + p.stderr)[-600:]},
                         ensure_ascii=False), flush=True)
    return p.returncode == 0


# ---------------------------------------------------------------- commands

def status(s: int) -> None:
    if not (wd(s) / "pack" / "pack.json").exists():
        print(f"S{s}: no pack")
        return
    print(f"S{s}:")
    for t in targets(s):
        line = "accepted" if accepted(s, t) else "due"
        for d in sorted(wd(s).glob(f"{BRIEF}.{tag(t)}*")):
            if d.name != f"{BRIEF}.{tag(t)}" and not d.name.startswith(f"{BRIEF}.{tag(t)}.a"):
                continue
            if (d / "run.log.json").exists():
                r = json.loads((d / "run.log.json").read_text(encoding="utf-8"))
                line += (f" | {d.name}: {r.get('status')} {r.get('check', '')} kept {r.get('kept', '-')} dropped "
                         f"{r.get('dropped', '-')} {r.get('seconds', '')}s in {(r.get('usage') or {}).get('input_tokens', '')}")
            elif (d / "started.json").exists():
                line += f" | {d.name}: started (running or interrupted)"
        print(f"  {t:8} {line}")


def surahs(arg: str) -> list[int]:
    out = []
    for part in arg.split(","):
        lo, _, hi = part.partition("-")
        out += list(range(int(lo), int(hi or lo) + 1))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=("status", "build", "run"))
    ap.add_argument("--surah", type=int)
    ap.add_argument("--surahs")
    ap.add_argument("--target", help="surah or S:A (default: every page of the surah)")
    ap.add_argument("--model", default=MODEL)
    ap.add_argument("--effort", default=EFFORT, choices=("low", "medium", "high", "max"))
    ap.add_argument("--attempt", type=int, default=1)
    ap.add_argument("--parallel", type=int, default=2)
    a = ap.parse_args()
    ss = surahs(a.surahs) if a.surahs else [a.surah]
    if None in ss:
        ap.error("--surah or --surahs")
    if a.cmd == "status":
        for s in ss:
            status(s)
        return
    jobs = []
    for s in ss:
        if not ensure_pack(s):
            continue
        jobs += [(s, t) for t in ([a.target] if a.target else targets(s))]
    if a.cmd == "build":
        for s, t in jobs:
            p = build_prompt(s, t, call_dir(s, t, a.attempt))
            print(f"S{s} {t}: prompt {len(p):,} chars (the agent reads the pack and corpus itself); "
                  f"model {a.model} effort {a.effort}; subscription run, USD not reported")
        print(f"{len(jobs)} calls")
        return
    with cf.ThreadPoolExecutor(a.parallel) as ex:
        for r in ex.map(lambda j: run_target(j[0], j[1], a.model, a.effort, a.attempt), jobs):
            print(json.dumps({k: r.get(k) for k in ("surah", "target", "status", "check", "kept", "dropped",
                                                     "seconds", "reason")}, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
