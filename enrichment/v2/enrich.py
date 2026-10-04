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

Models (--model, comma-separated, each key[:effort]): astra (default), sol, sol61 run through `codex exec`; opus,
sonnet through `claude -p`. Every agent can write only in its call directory and has no network: Codex by its own
sandbox; Claude by Claude Code's own sandbox (every Bash command sandboxed and auto-allowed, writes only in the
call directory, no network, no unsandboxed fallback) plus Write/Edit allowed only inside the call directory. Both
runners get the identical prompt. Non-default models get their own call directory (zengin.<page>.<model>.<effort>).
--trial renders and checks the page in the call directory only: nothing is copied to out/ and no errata are logged
(for model comparisons).
Codex Codex keeps each call's session log (~/.codex/sessions/…/rollout-…-<thread id>.jsonl): run.log.json records
its token totals and the subscription's weekly-limit reading before and after the call; `status` shows a running
call's tokens live. Rules as in v16: a call directory with started.json is never run again (--attempt N for a deliberate new
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
EFFORT = "high"
MODELS = {"astra": ("codex", "gpt-6-astra"), "sol": ("codex", "gpt-6-sol"), "sol61": ("codex", "gpt-6.1-sol"),
          "opus": ("claude", "claude-opus-5-5"), "sonnet": ("claude", "claude-sonnet-5-5")}
DEFAULT_MODEL = "astra"
MAX_USD = 40          # per Claude call (--max-budget-usd); Codex runs are on the subscription
TIMEOUT = 8 * 3600    # seconds per call; a call past it is killed and logged as an error
CLAUDE_TOOLS = "Bash,Read,Write,Edit,Glob,Grep"
BRIEF = "zengin"
SESSIONS = Path.home() / ".codex" / "sessions"

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


def call_dir(s: int, target: str, attempt: int = 1, model: str = DEFAULT_MODEL, effort: str = EFFORT) -> Path:
    # the bare directory belongs to astra at the default effort (S107's first surah call, astra max, also sits there)
    name = f"{BRIEF}.{tag(target)}" + ("" if (model, effort) == (DEFAULT_MODEL, EFFORT) else f".{model}.{effort}")
    return wd(s) / (name if attempt == 1 else f"{name}.a{attempt}")


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

def header(s: int, target: str, d: Path, runner: str = "codex") -> str:
    pack = wd(s) / "pack"
    n = json.loads((pack / "pack.json").read_text(encoding="utf-8"))["ayat"]
    name = page_name(s, target)
    py = "python3"
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
        f"- Schema card: {V2 / 'SCHEMA_CARD.md'} (read it once; the full reference is {V2 / 'SCHEMA.md'})",
        f"- Corpus tool: {py} {V2 / 'tools' / 'corpus.py'}",
        f"- Validator: {py} {V2 / 'validate.py'} --surah {s} --target {target} --annotations "
        f"{d / 'annotations.jsonl'}",
        f"- Renderer (preview): {py} {V2 / 'render.py'} --surah {s} --target {target} --annotations "
        f"{d / 'annotations.jsonl'} --out {d / 'preview'}",
    ]) + "\n"


def build_prompt(s: int, target: str, d: Path, runner: str = "codex") -> str:
    return "\n\n".join([header(s, target, d, runner), (PROMPTS / "common.md").read_text(encoding="utf-8"),
                        (PROMPTS / f"{BRIEF}.md").read_text(encoding="utf-8")])


# ---------------------------------------------------------------- call

def call_codex(prompt: str, d: Path, model: str, effort: str) -> dict:
    last = d / "response.md"
    cmd = ["codex", "exec", "--ignore-user-config", "-m", model, "-c", f'model_reasoning_effort="{effort}"',
           "-c", 'web_search="disabled"', "--disable", "skill_search", "--skip-git-repo-check",
           "-s", "workspace-write", "--json", "-o", str(last), "-C", str(d), "-"]
    (d / "command.json").write_text(json.dumps({"argv": cmd, "stdin": "prompt.md"}, indent=1) + "\n", encoding="utf-8")
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    with (d / "run.stream.jsonl").open("w", encoding="utf-8") as out, (d / "stderr.log").open("w") as err:
        try:
            p = subprocess.run(cmd, input=prompt, text=True, stdout=out, stderr=err, env=env, timeout=TIMEOUT)
        except subprocess.TimeoutExpired:
            p = subprocess.CompletedProcess(cmd, -9)
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


def others(d: Path) -> list[Path]:
    """What a trial must not see: accepted pages and every other call directory (other models' records and notes)
    and the Codex/Claude session stores (transcripts of other calls)."""
    return ([OUT] + [x for x in sorted(WORK.glob(f"s*/{BRIEF}.*")) if x.is_dir() and x != d]
            + [Path.home() / ".codex" / "sessions", Path.home() / ".claude" / "projects"])


def call_claude(prompt: str, d: Path, model: str, effort: str) -> dict:
    """One `claude -p` call in the call directory, customizations off (--safe-mode), unlisted actions refused
    (--permission-mode dontAsk). The stream is kept; the result event carries tokens and the cost in USD."""
    sid = str(__import__("uuid").uuid4())
    allowed = [f"Read(/{PG}/**)", f"Write(/{d}/**)", f"Edit(/{d}/**)"]
    hidden = others(d)
    denied = [f"{tool}(/{h}/**)" for h in hidden for tool in ("Read", "Edit", "Write")]
    settings = {"sandbox": {"enabled": True, "failIfUnavailable": True, "autoAllowBashIfSandboxed": True,
                            "allowUnsandboxedCommands": False, "network": {"allowedDomains": []},
                            "filesystem": {"allowWrite": [str(d)], "denyRead": [str(h) for h in hidden]}}}
    cmd = ["claude", "-p", "--model", model, "--effort", effort, "--tools", CLAUDE_TOOLS, "--allowedTools", *allowed,
           "--disallowedTools", *denied, "--settings", json.dumps(settings), "--max-budget-usd", str(MAX_USD),
           "--output-format", "stream-json", "--verbose", "--session-id", sid, "--safe-mode",
           "--permission-mode", "dontAsk"]
    (d / "command.json").write_text(json.dumps({"argv": cmd, "stdin": "prompt.md"}, indent=1) + "\n", encoding="utf-8")
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "ENRICH_CALL_DIR": str(d),
           "CLAUDE_CODE_MAX_OUTPUT_TOKENS": "128000",
           # 5-minute cache: writes cost 1.25x input instead of 2x; turns come every few seconds, so it stays warm
           "FORCE_PROMPT_CACHING_5M": "1"}
    with (d / "run.stream.jsonl").open("w", encoding="utf-8") as out, (d / "stderr.log").open("w") as err:
        try:
            p = subprocess.run(cmd, input=prompt, text=True, stdout=out, stderr=err, env=env, cwd=d, timeout=TIMEOUT)
        except subprocess.TimeoutExpired:
            p = subprocess.CompletedProcess(cmd, -9)
    final, tools, denied = {}, 0, 0
    for line in (d / "run.stream.jsonl").read_text(encoding="utf-8").splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "assistant":
            tools += sum(1 for c in (ev.get("message") or {}).get("content", []) if c.get("type") == "tool_use")
        if ev.get("type") == "result":
            final = ev
            denied = len(ev.get("permission_denials") or [])
    if final.get("result"):
        (d / "response.md").write_text(final["result"] + "\n", encoding="utf-8")
    return {"returncode": p.returncode, "turn_completed": bool(final) and not final.get("is_error"),
            "usage": final.get("usage") or {}, "cost_usd": final.get("total_cost_usd"),
            "num_turns": final.get("num_turns"), "commands": tools, "permission_denials": denied, "session_id": sid}


def session_file(d: Path) -> Path | None:
    """The Codex session log of the call in d, found by the thread id the stream starts with."""
    try:
        with (d / "run.stream.jsonl").open(encoding="utf-8") as f:
            tid = json.loads(f.readline()).get("thread_id")
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    hits = sorted(SESSIONS.glob(f"*/*/*/rollout-*-{tid}.jsonl")) if tid else []
    return hits[-1] if hits else None


def read_session(f: Path) -> dict:
    """Token totals, the last turn's context, and the weekly-limit readings (first, last) of one session log."""
    out = {"session": str(f)}
    for line in f.read_text(encoding="utf-8").splitlines():
        try:
            p = json.loads(line).get("payload") or {}
        except json.JSONDecodeError:
            continue
        if p.get("type") != "token_count":
            continue
        info = p.get("info") or {}
        if info.get("total_token_usage"):
            out["tokens"] = info["total_token_usage"]
            out["context_tokens_last_turn"] = (info.get("last_token_usage") or {}).get("input_tokens")
        week = ((p.get("rate_limits") or {}).get("primary") or {}).get("used_percent")
        if week is not None:
            out.setdefault("weekly_used_first", week)
            out["weekly_used_last"] = week
    return out


def weekly_now() -> dict:
    """The latest weekly-limit reading in any saved session (a baseline before a call; may be hours old)."""
    for f in sorted(SESSIONS.glob("*/*/*/rollout-*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)[:5]:
        r = read_session(f)
        if "weekly_used_last" in r:
            return {"weekly_used": r["weekly_used_last"], "read_from": f.name,
                    "as_of": time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(f.stat().st_mtime))}
    return {}


def finish(s: int, target: str, d: Path, trial: bool = False) -> dict:
    """Check the records, drop the failing ones, render, check the page, accept (unless trial). Nothing goes back to
    the agent."""
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
    if trial:
        return {"check": "ok (trial: page in the call directory only)", "ok": True, "kept": len(kept),
                "dropped": len(dropped)}
    dst = OUT / f"s{s:03d}" / name
    if dst.exists():
        return {"check": f"{rel(dst)} exists (never overwrite)", "ok": False}
    pack = json.loads((wd(s) / "pack" / "pack.json").read_text(encoding="utf-8"))
    errata = [r for r in kept if r.get("tur") == "duzeltme"]
    with ERRATA.open("a", encoding="utf-8") as f:  # before the page: an accepted page never lacks its errata
        for r in errata:
            f.write(json.dumps({"surah": s, "target": target, "base": info["path"], "id": r["id"], "taban": r.get("taban"),
                                "hata": r.get("hata"), "metin": r.get("metin"), "kaynak": r.get("kaynak")},
                               ensure_ascii=False) + "\n")
    dst.parent.mkdir(parents=True, exist_ok=True)
    with open(page, "rb") as src, open(dst, "xb") as out:  # exclusive: never overwrite, even in a race
        out.write(src.read())
    rec = {"surah": s, "target": target, "accepted_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
           "page_sha256": hashlib.sha256(dst.read_bytes()).hexdigest(), "base": info,
           "dictionary": pack.get("dictionary"), "annotations": rel(ann),
           "kept": len(kept), "dropped": [x["id"] for x in dropped]}
    dst.with_suffix(".json").write_text(json.dumps(rec, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return {"check": "ok", "ok": True, "kept": len(kept), "dropped": len(dropped), "errata": len(errata)}


def run_target(s: int, target: str, model: str, effort: str, attempt: int = 1, trial: bool = False) -> dict:
    runner, model_id = MODELS[model]
    d = call_dir(s, target, attempt, model, effort)
    if blocked(d):
        return {"surah": s, "target": target, "model": model, "status": "skipped",
                "reason": "started or finished before (never rerun)"}
    if accepted(s, target) and not trial:
        return {"surah": s, "target": target, "model": model, "status": "skipped", "reason": "page already accepted"}
    try:
        prompt = build_prompt(s, target, d, runner)
    except Exception as e:  # a missing pack or brief stops this job, not the whole batch
        return {"surah": s, "target": target, "model": model, "status": "error", "reason": f"prompt: {e}"}
    d.mkdir(parents=True, exist_ok=True)
    row = {"surah": s, "target": target, "attempt": attempt, "brief": BRIEF, "model": model, "model_id": model_id,
           "runner": runner, "effort": effort, "trial": trial, "prompt_sha256": sha(prompt), "prompt_chars": len(prompt),
           "started": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    with (d / "started.json").open("x", encoding="utf-8") as f:
        json.dump(row, f, ensure_ascii=False, indent=1)
    (d / "prompt.md").write_text(prompt, encoding="utf-8")
    if runner == "codex":
        row["weekly_before"] = weekly_now()
    t0 = time.monotonic()
    try:
        if runner == "codex":
            row.update(call_codex(prompt, d, model_id, effort))
            sf = session_file(d)
            if sf:
                row["session"] = read_session(sf)
        else:
            row.update(call_claude(prompt, d, model_id, effort))
        res = finish(s, target, d, trial) if row["returncode"] == 0 and row["turn_completed"] else \
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
            if d.name != f"{BRIEF}.{tag(t)}" and not d.name.startswith(f"{BRIEF}.{tag(t)}."):
                continue
            if (d / "run.log.json").exists():
                r = json.loads((d / "run.log.json").read_text(encoding="utf-8"))
                line += (f"\n      {d.name}: {r.get('status')} {r.get('check', '')} kept {r.get('kept', '-')} dropped "
                         f"{r.get('dropped', '-')} {r.get('seconds', '')}s in {(r.get('usage') or {}).get('input_tokens', '')}"
                         + (f" ${r['cost_usd']:.2f}" if r.get("cost_usd") else ""))
            elif (d / "started.json").exists():
                line += f"\n      {d.name}: started (running or interrupted)"
                sf = session_file(d)
                if sf:
                    u = read_session(sf)
                    tok = u.get("tokens") or {}
                    line += (f"; so far: in {tok.get('input_tokens', 0):,} (cached {tok.get('cached_input_tokens', 0):,}) "
                             f"out {tok.get('output_tokens', 0):,}; context {u.get('context_tokens_last_turn') or 0:,}; "
                             f"weekly {u.get('weekly_used_first')}→{u.get('weekly_used_last')}%")
        print(f"  {t:8} {line}")


def surahs(arg: str) -> list[int]:
    out = []
    for part in arg.split(","):
        lo, _, hi = part.partition("-")
        out += list(range(int(lo), int(hi or lo) + 1))
    return out


def model_specs(arg: str, default_effort: str) -> list[tuple[str, str]]:
    """"sol:max,opus:high" -> [("sol", "max"), ("opus", "high")]; a key without :effort takes --effort."""
    out = []
    for part in arg.split(","):
        key, _, effort = part.strip().partition(":")
        if key not in MODELS:
            raise SystemExit(f"unknown model {key!r}; known: {', '.join(MODELS)}")
        out.append((key, effort or default_effort))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=("status", "build", "run"))
    ap.add_argument("--surah", type=int)
    ap.add_argument("--surahs")
    ap.add_argument("--target", help="surah or S:A (default: every page of the surah)")
    ap.add_argument("--model", default=DEFAULT_MODEL, help=f"key[:effort],... of {', '.join(MODELS)}")
    ap.add_argument("--effort", default=EFFORT, choices=("low", "medium", "high", "max"))
    ap.add_argument("--attempt", type=int, default=1)
    ap.add_argument("--trial", action="store_true", help="render in the call directory only; no out/, no errata")
    ap.add_argument("--parallel", type=int, default=2)
    a = ap.parse_args()
    ss = surahs(a.surahs) if a.surahs else [a.surah]
    if None in ss:
        ap.error("--surah or --surahs")
    if a.cmd == "status":
        for s in ss:
            status(s)
        return
    specs = model_specs(a.model, a.effort)
    if a.cmd == "run" and len(specs) > 1 and not a.trial:
        ap.error("several models on the same pages only with --trial (otherwise they race for the accepted page)")
    jobs = []
    for s in ss:
        if not ensure_pack(s):
            continue
        jobs += [(s, t, m, e) for t in ([a.target] if a.target else targets(s)) for m, e in specs]
    if a.cmd == "build":
        for s, t, m, e in jobs:
            d = call_dir(s, t, a.attempt, m, e)
            p = build_prompt(s, t, d, MODELS[m][0])
            print(f"S{s} {t} {m} ({MODELS[m][1]}, {e}): prompt {len(p):,} chars -> {rel(d)}"
                  + (" [exists: will be skipped]" if blocked(d) else ""))
        print(f"{len(jobs)} calls")
        return
    with cf.ThreadPoolExecutor(a.parallel) as ex:
        for r in ex.map(lambda j: run_target(j[0], j[1], j[2], j[3], a.attempt, a.trial), jobs):
            print(json.dumps({k: r.get(k) for k in ("surah", "target", "model", "status", "check", "kept", "dropped",
                                                     "seconds", "cost_usd", "reason")}, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
