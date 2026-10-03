#!/usr/bin/env python3
"""Enrichment v2 orchestrator (v16-like): one brief per stage, one agent call per stage, never rerun.

Stages per surah (work/sNNN/):
  paket     script   pack.py: the reference pack (frozen base, binding, dictionary, lexica, usage, meals, locators)
  harita    agent    claim map + evidence matrix + gaps                         (prompts/harita.md)
  meal      agent    Turkish translation review + meal blocks                   (prompts/meal.md)   [parallel to harita]
  yaz       agent    annotations.jsonl from the matrix + meal blocks            (prompts/yaz.md)
  dizgi     script   render.py + validate.py -> out/ pages and validation.json
  denetim   agent    independent audit -> review.json                           (prompts/denetim.md)
  onarim    agent    apply the audit -> annotations.jsonl                       (prompts/onarim.md)
            then dizgi and denetim again; at most 2 repair rounds (onarim1, denetim2, onarim2, denetim3)
  kabul     script   copy the pages to out/sNNN/, record hashes, append errata to errata.jsonl

Agent calls run `codex exec` (GPT-6 Astra by default) with the stage directory as the only writable place, no
network, and the prompt = job header + prompts/common.md + the stage brief. Rules as in v16: a stage directory with
started.json is never run again (use --attempt N for a deliberate new attempt, which gets its own directory); every
call is logged in work/ledger.jsonl with its prompt hash; the deterministic check runs after each call.

  python3 enrichment/v2/enrich.py status --surah 107
  python3 enrichment/v2/enrich.py build  --surah 107 --stage harita        (writes and sizes the prompt only)
  python3 enrichment/v2/enrich.py run    --surah 107 --stage harita [--effort high|max] [--attempt 2]
  python3 enrichment/v2/enrich.py next   --surah 107 [--run]               (the next due stage(s); harita+meal together)
  python3 enrichment/v2/enrich.py next   --surahs 87-114 --run --parallel 3
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
AGENT_STAGES = {"harita", "meal", "yaz", "denetim", "onarim"}
OUTPUTS = {"harita": ["claim_map.json", "evidence_matrix.json", "gaps.json"],
           "meal": ["meal_table.json", "meal_review.json", "annotations.meal.jsonl"],
           "yaz": ["annotations.jsonl"], "denetim": ["review.json"], "onarim": ["annotations.jsonl", "applied.json"]}
MAX_REPAIRS = 2


def wd(s: int) -> Path:
    return WORK / f"s{s:03d}"


def sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def log(row: dict) -> None:
    WORK.mkdir(parents=True, exist_ok=True)
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def stage_dir(s: int, name: str, attempt: int = 1) -> Path:
    return wd(s) / (name if attempt == 1 else f"{name}.a{attempt}")


def done(d: Path) -> bool:
    try:
        return json.loads((d / "run.log.json").read_text(encoding="utf-8")).get("status") == "ok"
    except (FileNotFoundError, json.JSONDecodeError):
        return False


def blocked(d: Path) -> bool:
    return (d / "started.json").exists() or (d / "run.log.json").exists()


def latest(s: int, name: str) -> Path | None:
    """The latest successful attempt of a stage (name may carry a round: onarim1, denetim2)."""
    cands = sorted(wd(s).glob(f"{name}*"), key=lambda p: (p.name.count(".a"), p.name))
    ok = [d for d in cands if d.name == name or d.name.startswith(name + ".a")]
    ok = [d for d in ok if done(d)]
    return ok[-1] if ok else None


# ---------------------------------------------------------------- prompts

def current_annotations(s: int) -> Path | None:
    """The annotations of the latest repair round, else of yaz."""
    for r in range(MAX_REPAIRS, 0, -1):
        d = latest(s, f"onarim{r}")
        if d:
            return d / "annotations.jsonl"
    d = latest(s, "yaz")
    return d / "annotations.jsonl" if d else None


def header(s: int, stage: str, round_: int, d: Path) -> str:
    pack = wd(s) / "pack"
    n = json.loads((pack / "pack.json").read_text(encoding="utf-8"))["ayat"]
    lines = ["# Job", "", f"- Surah: {s} (ayat 1–{n}); ids use S{s:03d}", f"- Stage: {stage}"
             + (f" (round {round_})" if round_ else ""),
             f"- Workspace root: {PG}", f"- PACK: {pack}", f"- Your stage directory (write only here): {d}",
             f"- Schema: {V2 / 'schema.json'} and {V2 / 'SCHEMA.md'}",
             f"- Corpus tool: python3 {V2 / 'tools' / 'corpus.py'}  (validator: python3 {V2 / 'validate.py'}; "
             f"renderer: python3 {V2 / 'render.py'})"]
    if stage in ("yaz",):
        lines += [f"- STAGE harita: {latest(s, 'harita')}", f"- STAGE meal: {latest(s, 'meal')}"]
    if stage == "denetim":
        ann = current_annotations(s)
        lines += [f"- Records under audit: {ann}", f"- OUT (rendered pages): {wd(s) / 'out'}",
                  f"- Validator report: {wd(s) / 'out' / 'validation.json'}", f"- STAGE harita: {latest(s, 'harita')}"]
    if stage == "onarim":
        lines += [f"- Records to correct: {current_annotations(s)}",
                  f"- Audit: {latest(s, f'denetim{round_}') / 'review.json'}"]
    return "\n".join(lines) + "\n"


def build_prompt(s: int, stage: str, round_: int, d: Path) -> str:
    brief = PROMPTS / f"{stage}.md"
    return "\n\n".join([header(s, stage, round_, d), (PROMPTS / "common.md").read_text(encoding="utf-8"),
                        brief.read_text(encoding="utf-8")])


# ---------------------------------------------------------------- calls

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


def post_check(s: int, stage: str, d: Path) -> tuple[bool, str]:
    missing = [f for f in OUTPUTS.get(stage.rstrip("0123456789"), []) if not (d / f).exists()]
    if missing:
        return False, f"missing outputs {missing}"
    if stage.startswith(("meal", "yaz", "onarim")):
        ann = d / ("annotations.meal.jsonl" if stage == "meal" else "annotations.jsonl")
        p = subprocess.run([sys.executable, "-B", str(V2 / "validate.py"), "--surah", str(s), "--annotations", str(ann),
                            "--out", "/nonexistent", "--report", str(d / "validation.json")], capture_output=True, text=True)
        if p.returncode:
            return False, "validator errors (see validation.json)"
    if stage.startswith("denetim"):
        try:
            json.loads((d / "review.json").read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            return False, f"review.json invalid: {e}"
    return True, "ok"


def run_agent(s: int, stage: str, round_: int, model: str, effort: str, attempt: int = 1) -> dict:
    name = f"{stage}{round_ or ''}"
    d = stage_dir(s, name, attempt)
    if blocked(d):
        return {"surah": s, "stage": name, "status": "skipped", "reason": "started or finished before (never rerun)"}
    d.mkdir(parents=True, exist_ok=True)
    prompt = build_prompt(s, stage, round_, d)
    row = {"surah": s, "stage": name, "attempt": attempt, "model": model, "effort": effort,
           "prompt_sha256": sha(prompt), "prompt_chars": len(prompt),
           "started": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    with (d / "started.json").open("x", encoding="utf-8") as f:
        json.dump(row, f, ensure_ascii=False, indent=1)
    (d / "prompt.md").write_text(prompt, encoding="utf-8")
    t0 = time.monotonic()
    try:
        row.update(call_codex(prompt, d, model, effort))
        ok, why = post_check(s, name, d)
        row["status"] = "ok" if ok and row["returncode"] == 0 and row["turn_completed"] else "error"
        row["check"] = why
    except Exception as e:  # keep the record; never retry automatically
        row.update(status="error", error=f"{type(e).__name__}: {e}")
    row["seconds"] = round(time.monotonic() - t0)
    (d / "run.log.json").write_text(json.dumps(row, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log(row)
    return row


def run_script(s: int, stage: str, round_: int = 0) -> dict:
    name = f"{stage}{round_ or ''}"
    t0 = time.monotonic()
    if stage == "paket":
        p = subprocess.run([sys.executable, "-B", str(V2 / "pack.py"), "--surah", str(s)], capture_output=True, text=True)
        row = {"surah": s, "stage": "paket", "status": "ok" if p.returncode == 0 else "error",
               "out": (p.stdout + p.stderr)[-1500:]}
        if p.returncode == 0:
            (wd(s) / "paket").mkdir(parents=True, exist_ok=True)
            (wd(s) / "paket" / "run.log.json").write_text(json.dumps(row, ensure_ascii=False) + "\n", encoding="utf-8")
    elif stage == "dizgi":
        ann = current_annotations(s)
        out = wd(s) / "out"
        if out.exists():
            shutil.rmtree(out)
        r = subprocess.run([sys.executable, "-B", str(V2 / "render.py"), "--surah", str(s), "--annotations", str(ann),
                            "--out", str(out)], capture_output=True, text=True)
        v = subprocess.run([sys.executable, "-B", str(V2 / "validate.py"), "--surah", str(s), "--annotations", str(ann),
                            "--out", str(out), "--report", str(out / "validation.json")], capture_output=True, text=True)
        row = {"surah": s, "stage": name, "annotations": str(ann.relative_to(PG)),
               "status": "ok" if r.returncode == 0 and v.returncode == 0 else "error",
               "render": r.stdout[-800:] + r.stderr[-800:], "validate_rc": v.returncode}
        d = wd(s) / name
        d.mkdir(parents=True, exist_ok=True)
        (d / "run.log.json").write_text(json.dumps(row, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    elif stage == "kabul":
        row = accept(s)
    else:
        raise ValueError(stage)
    row["seconds"] = round(time.monotonic() - t0)
    log(row)
    return row


def accept(s: int) -> dict:
    src = wd(s) / "out"
    dst = OUT / f"s{s:03d}"
    if dst.exists():
        return {"surah": s, "stage": "kabul", "status": "skipped", "reason": f"{dst} exists (never overwrite)"}
    review = None
    for r in range(MAX_REPAIRS + 1, 0, -1):
        d = latest(s, f"denetim{r}")
        if d:
            review = json.loads((d / "review.json").read_text(encoding="utf-8"))
            break
    shutil.copytree(src, dst)
    pack = json.loads((wd(s) / "pack" / "pack.json").read_text(encoding="utf-8"))
    hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(dst.glob("*.md"))}
    errata = [e for e in (review or {}).get("errata", [])]
    with ERRATA.open("a", encoding="utf-8") as f:
        for e in errata:
            f.write(json.dumps({"surah": s, "base": pack["base"]["surah"]["path"], **e}, ensure_ascii=False) + "\n")
    rec = {"surah": s, "stage": "kabul", "status": "ok", "accepted_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
           "audit_accepted": (review or {}).get("accepted"), "open_fixes": len((review or {}).get("fixes", [])),
           "annotations": str(current_annotations(s).relative_to(PG)), "pages": hashes,
           "base": pack["base"], "dictionary": pack["dictionary"], "errata_logged": len(errata)}
    (dst / "accepted.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return rec


# ---------------------------------------------------------------- pipeline

def plan(s: int) -> list[tuple[str, int]]:
    """The next due stage(s) for a surah, as (stage, round). Empty when accepted."""
    if (OUT / f"s{s:03d}" / "accepted.json").exists():
        return []
    if not (wd(s) / "pack" / "pack.json").exists():
        return [("paket", 0)]
    due = [st for st in ("harita", "meal") if not latest(s, st)]
    if due:
        return [(st, 0) for st in due]
    if not latest(s, "yaz"):
        return [("yaz", 0)]
    for r in range(1, MAX_REPAIRS + 2):
        if not done(wd(s) / f"dizgi{r}"):
            return [("dizgi", r)]
        audit = latest(s, f"denetim{r}")
        if not audit:
            return [("denetim", r)]
        review = json.loads((audit / "review.json").read_text(encoding="utf-8"))
        if review.get("accepted") or r > MAX_REPAIRS:
            return [("kabul", 0)]
        if not latest(s, f"onarim{r}"):
            return [("onarim", r)]
    return [("kabul", 0)]


def execute(s: int, stage: str, round_: int, model: str, effort: str) -> dict:
    if stage in AGENT_STAGES:
        return run_agent(s, stage, round_, model, effort)
    return run_script(s, stage, round_)


def advance(s: int, model: str, effort: str, until_blocked: bool = True) -> list[dict]:
    rows = []
    while True:
        steps = plan(s)
        if not steps:
            break
        with cf.ThreadPoolExecutor(len(steps)) as ex:
            res = list(ex.map(lambda st: execute(s, st[0], st[1], model, effort), steps))
        rows += res
        for r in res:
            print(json.dumps({k: r.get(k) for k in ("surah", "stage", "status", "check", "seconds", "reason")},
                             ensure_ascii=False), flush=True)
        if any(r.get("status") != "ok" for r in res) or not until_blocked:
            break
    return rows


def status(s: int) -> None:
    print(f"S{s}: next = {plan(s) or 'accepted'}")
    for d in sorted(wd(s).glob("*")):
        if d.is_dir() and (d / "run.log.json").exists():
            r = json.loads((d / "run.log.json").read_text(encoding="utf-8"))
            print(f"  {d.name:14} {r.get('status'):8} {r.get('check', '')} {r.get('seconds', '')}s "
                  f"{(r.get('usage') or {}).get('input_tokens', '')}")
        elif d.is_dir() and (d / "started.json").exists():
            print(f"  {d.name:14} started (running or interrupted)")


def surahs(arg: str) -> list[int]:
    out = []
    for part in arg.split(","):
        lo, _, hi = part.partition("-")
        out += list(range(int(lo), int(hi or lo) + 1))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=("status", "build", "run", "next"))
    ap.add_argument("--surah", type=int)
    ap.add_argument("--surahs")
    ap.add_argument("--stage")
    ap.add_argument("--round", type=int, default=0)
    ap.add_argument("--model", default=MODEL)
    ap.add_argument("--effort", default=EFFORT, choices=("low", "medium", "high", "max"))
    ap.add_argument("--attempt", type=int, default=1)
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--parallel", type=int, default=2)
    a = ap.parse_args()
    targets = surahs(a.surahs) if a.surahs else [a.surah]
    if None in targets:
        ap.error("--surah or --surahs")
    if a.cmd == "status":
        for s in targets:
            status(s)
    elif a.cmd == "build":
        for s in targets:
            name = f"{a.stage}{a.round or ''}"
            d = stage_dir(s, name, a.attempt)
            p = build_prompt(s, a.stage, a.round, d)
            print(f"S{s} {name}: prompt {len(p):,} chars (the agent reads the pack and corpus itself); "
                  f"model {a.model} effort {a.effort}; subscription run, USD not reported")
    elif a.cmd == "run":
        for s in targets:
            print(json.dumps(execute(s, a.stage, a.round, a.model, a.effort) if a.attempt == 1 else
                             run_agent(s, a.stage, a.round, a.model, a.effort, a.attempt), ensure_ascii=False))
    elif a.cmd == "next":
        if not a.run:
            for s in targets:
                print(f"S{s}: next = {plan(s) or 'accepted'}")
            return
        with cf.ThreadPoolExecutor(a.parallel) as ex:
            list(ex.map(lambda s: advance(s, a.model, a.effort), targets))


if __name__ == "__main__":
    main()
