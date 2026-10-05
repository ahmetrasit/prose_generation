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

Models (--model, comma-separated, each key[:effort]; default opus:high): astra, sol, sol61 run through `codex exec`;
opus, sonnet through `claude -p`. Every agent can write only in its call directory (Codex's workspace-write sandbox also allows /tmp) and has no network: Codex by its own
sandbox; Claude by Claude Code's own sandbox (every Bash command sandboxed and auto-allowed, writes only in the
call directory, no network, no unsandboxed fallback) plus Write/Edit allowed only inside the call directory. Both
runners get the identical prompt. Read isolation is partial: a Claude call cannot read out/ or the call
directories that existed when it started, but can read ones created later (parallel runs); a Codex call has no read
limits. Trials are therefore blind only when run before the page's other calls, one wave at a time. Non-default models get their own call directory (zengin.<page>.<model>.<effort>).
--trial renders and checks the page in the call directory only: nothing is copied to out/ and no errata are logged
(for model comparisons).
Codex Codex keeps each call's session log (~/.codex/sessions/…/rollout-…-<thread id>.jsonl): run.log.json records
its token totals and the subscription's weekly-limit reading before and after the call; `status` shows a running
call's tokens live. Rules as in v16: a call directory with started.json is never run again (--attempt N for a deliberate new
attempt, which gets its own directory); every call is logged in work/ledger.jsonl with its prompt hash.

  python3 enrichment/v2/enrich.py status --surah 107
  python3 enrichment/v2/enrich.py build  --surah 107 --target surah        (builds a missing pack; sizes the prompts
                                                                            and estimates the cost; no model call)
  python3 enrichment/v2/enrich.py run    --surah 107 --target surah [--attempt 2]
  python3 enrichment/v2/enrich.py run    --surahs 1,87,100 --target surah --parallel 2
  python3 enrichment/v2/enrich.py accept --surah 100 --target surah --model opus:high   (accept a finished trial page)
  python3 enrichment/v2/enrich.py confirm-dead --surah 87 --dir zengin.surah.opus.high  (a call whose process is gone)
run and accept exit 1 when a page fails; every failure prints a WARNING: line.
--target is required for build and run: surah | S:A | ayat (every ayah page with a base) | all (surah + ayat).
Without --model, runs use opus:high (the user's choice after the S107/S100 trials). Each call records the sha256 of
its page's base; a page whose base changed since its call (a pack rebuilt meanwhile) is never accepted.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import os
import shutil
import signal
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
DEFAULT_MODEL = "astra"   # names the bare call directory (astra at the default effort; S107's first surah call)
RUN_MODEL = "opus:high"   # the model used when --model is not given (user, 2026-10-04, after the S107/S100 trials)
MAX_USD = 40          # per Claude call (--max-budget-usd); Codex runs are on the subscription
TIMEOUT = 8 * 3600    # seconds per call; a call past it is killed and logged as an error
CLAUDE_TOOLS = "Bash,Read,Write,Edit,Glob,Grep"
BRIEF = "zengin"          # the Islamic pass; --pass ehlikitap sets "ehlikitap" (the Bible layers, user 2026-10-04)
GELENEK = {"zengin": "islami", "ehlikitap": "ehlikitap"}
MODE = "agent"  # "dosya": one tool-free call on a script-built dossier (dossier.py), user 2026-10-04 evening
SESSIONS = Path.home() / ".codex" / "sessions"

sys.path.insert(0, str(V2))
sys.path.insert(0, str(PG / "_commentary" / "v16"))
import agentrun as AR  # noqa: E402  (agent-spawned runs, user 2026-10-04 evening)
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
    name = f"{BRIEF}{'-dosya' if MODE == 'dosya' else ''}.{tag(target)}" + ("" if (model, effort) == (DEFAULT_MODEL, EFFORT) else f".{model}.{effort}")
    return wd(s) / (name if attempt == 1 else f"{name}.a{attempt}")


def page_name(s: int, target: str) -> str:
    stem = "surah" if target == "surah" else tag(target)
    return f"{stem}.md" if BRIEF == "zengin" else f"{stem}.{BRIEF}.md"  # the Bible pass has its own page beside the Islamic one


def discovery_list(s: int, target: str) -> Path | None:
    """The merged Bible discovery list for a page (discover.py --bible --merge), when it exists."""
    f = PG / "_commentary" / "v16" / "out" / f"s{s:03d}" / "discovery_bible" / f"{tag(target)}.merged.tsv"
    return f if f.exists() else None


def accepted(s: int, target: str) -> bool:
    return (OUT / f"s{s:03d}" / page_name(s, target)).exists()


def blocked(d: Path) -> bool:
    return (d / "started.json").exists() or (d / "run.log.json").exists()


def targets(s: int) -> list[str]:
    """The surah page and every ayah page that has a base."""
    base = json.loads((wd(s) / "pack" / "base.json").read_text(encoding="utf-8"))
    return ["surah"] + [ref for ref, info in base["ayat"].items() if info]


def select(s: int, spec: str) -> list[str]:
    """--target: surah | S:A | ayat | all."""
    if spec == "all":
        return targets(s)
    if spec == "ayat":
        return targets(s)[1:]
    if spec == "surah":
        return ["surah"]
    if ":" not in spec or spec.split(":")[0] != str(s) or not spec.split(":")[1].isdigit():
        raise SystemExit(f"--target {spec!r}: expected surah, ayat, all or {s}:A")
    return [spec]


def missing_ayat(s: int) -> list[str]:
    """Ayat of the surah with no ayah base (v16 augment9 not run): no ayah page until the pack is rebuilt."""
    base = json.loads((wd(s) / "pack" / "base.json").read_text(encoding="utf-8"))
    return [ref for ref, info in base["ayat"].items() if not info]


def base_words(s: int, target: str) -> int | None:
    try:
        return len(R.target_page(s, target)[1].split())
    except (OSError, SystemExit, KeyError, ValueError):
        return None


def estimate(s: int, target: str, model: str, effort: str) -> str:
    """USD estimate for a Claude call from the ledger: past calls of the same model, effort and page kind, scaled by
    the base's word count (the surah pages ran $0.67–0.98 per 1k base words with Opus high)."""
    if MODELS[model][0] != "claude":
        return "subscription (no USD)"
    kind = ("surah" if target == "surah" else "ayah") + ("-dosya" if MODE == "dosya" else "")
    rates, failed, bad = [], [], 0
    for line in (LEDGER.read_text(encoding="utf-8").splitlines() if LEDGER.exists() else []):
        try:
            r = json.loads(line)
        except json.JSONDecodeError:  # e.g. a row being appended right now
            bad += 1
            continue
        if not (r.get("cost_usd") and (r.get("model"), r.get("effort")) == (model, effort)
                and ("surah" if r.get("target") == "surah" else "ayah") + ("-dosya" if r.get("mode") == "dosya" else "") == kind):
            continue
        if r.get("status") != "ok":
            failed.append(r["cost_usd"])
            continue
        w = r.get("base_words") or base_words(r["surah"], r["target"])
        if w:
            rates.append(r["cost_usd"] / w * 1000)
    w = base_words(s, target)
    notes = ([f"{len(failed)} failed calls of this kind cost ${sum(failed):.2f} in all"] if failed else []) + \
            ([f"{bad} unreadable ledger lines skipped"] if bad else [])
    tail = f"; {'; '.join(notes)}" if notes else ""
    if not rates or not w:
        return f"no calibration yet for {model}:{effort} {kind} pages (base {w or '?'} words){tail}"
    lo, hi = min(rates), max(rates)
    return f"${lo * w / 1000:.1f}–{hi * w / 1000:.1f} (base {w:,} words; {len(rates)} past calls){tail}"


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
        f"{d / 'annotations.jsonl'}" + (" --pass ehlikitap" if BRIEF == "ehlikitap" else ""),
        f"- Renderer (preview): {py} {V2 / 'render.py'} --surah {s} --target {target} --annotations "
        f"{d / 'annotations.jsonl'} --out {d / 'preview'}",
    ] + ([f"- Pass: ehlikitap (the Tevrat and İncil layers; brief ehlikitap.md); corpus tool: {py} "
          f"{V2 / 'tools' / 'corpus.py'} --intertext (the flag before the subcommand)",
          "- Discovery list: " + (str(discovery_list(s, target)) if discovery_list(s, target) else
                                  "none (no discover.py --bible run for this page; work from the corpus and your own search)")]
         if BRIEF == "ehlikitap" else [])) + "\n"


def build_prompt(s: int, target: str, d: Path, runner: str = "codex") -> str:
    if MODE == "dosya":  # tool-free: the job, the core, the brief, then the dossier (schema card inside it)
        if target == "surah":
            raise SystemExit("the dosya mode is for ayah pages")
        import dossier as DO
        df = DO.build(s, target, 3000, 24000)
        head = "\n".join(["# Job", "", f"- Surah: {s}; ids use S{s:03d}", f"- Target: {target} — the ayah page (base in the dossier)",
                           f"- Your call directory (write only here): {d}", "- Mode: dosya (no tools; everything is in this message)"]) + "\n"
        return "\n\n".join([head, (PROMPTS / "common.md").read_text(encoding="utf-8"),
                            (PROMPTS / "zengin_dosya.md").read_text(encoding="utf-8"), df.read_text(encoding="utf-8")])
    return "\n\n".join([header(s, target, d, runner), (PROMPTS / "common.md").read_text(encoding="utf-8"),
                        (PROMPTS / f"{BRIEF}.md").read_text(encoding="utf-8")])


# ---------------------------------------------------------------- call

def run_proc(cmd: list[str], prompt: str, out, err, env: dict, cwd: Path | None = None) -> tuple[int, bool]:
    """(returncode, timed_out). The call runs in its own process group; on timeout the whole group is killed, so
    no sandboxed grandchild keeps writing into the call directory after the call is logged."""
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=out, stderr=err, env=env, cwd=cwd, text=True,
                         start_new_session=True)
    try:
        p.communicate(prompt, timeout=TIMEOUT)
        return p.returncode, False
    except subprocess.TimeoutExpired:
        try:
            os.killpg(p.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass  # the group ended by itself between the timeout and the kill
        p.wait()
        return -9, True


def call_codex(prompt: str, d: Path, model: str, effort: str) -> dict:
    last = d / "response.md"
    cmd = ["codex", "exec", "--ignore-user-config", "-m", model, "-c", f'model_reasoning_effort="{effort}"',
           "-c", 'web_search="disabled"', "--disable", "skill_search", "--skip-git-repo-check",
           "-s", "workspace-write", "--json", "-o", str(last), "-C", str(d), "-"]
    (d / "command.json").write_text(json.dumps({"argv": cmd, "stdin": "prompt.md"}, indent=1) + "\n", encoding="utf-8")
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    with (d / "run.stream.jsonl").open("w", encoding="utf-8") as out, (d / "stderr.log").open("w") as err:
        returncode, timed_out = run_proc(cmd, prompt, out, err, env)
    usage, completed, tools, bad = {}, False, 0, 0
    for line in (d / "run.stream.jsonl").read_text(encoding="utf-8").splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            bad += 1  # counted and reported (stream_unparsable), never silently dropped
            continue
        if ev.get("type") == "turn.completed":
            completed, usage = True, ev.get("usage") or {}
        if ev.get("type") == "item.completed" and (ev.get("item") or {}).get("type") == "command_execution":
            tools += 1
    return {"returncode": returncode, "turn_completed": completed, "usage": usage, "commands": tools,
            "timed_out": timed_out, "stream_unparsable": bad}


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
        returncode, timed_out = run_proc(cmd, prompt, out, err, env, cwd=d)
    final, tools, denials, bad = {}, 0, 0, 0
    for line in (d / "run.stream.jsonl").read_text(encoding="utf-8").splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            bad += 1  # counted and reported (stream_unparsable), never silently dropped
            continue
        if ev.get("type") == "assistant":
            tools += sum(1 for c in (ev.get("message") or {}).get("content", []) if c.get("type") == "tool_use")
        if ev.get("type") == "result":
            final = ev
            denials = len(ev.get("permission_denials") or [])
    if final.get("result"):
        (d / "response.md").write_text(final["result"] + "\n", encoding="utf-8")
    return {"returncode": returncode,
            # complete only on a successful result: error_max_turns, error_max_budget_usd … never reach finish()
            "turn_completed": bool(final) and not final.get("is_error") and final.get("subtype") in (None, "success"),
            "usage": final.get("usage") or {}, "cost_usd": final.get("total_cost_usd"),
            "num_turns": final.get("num_turns"), "commands": tools, "permission_denials": denials, "session_id": sid,
            "result_subtype": final.get("subtype"), "result_is_error": bool(final.get("is_error")),
            "timed_out": timed_out, "stream_unparsable": bad}


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


def finish(s: int, target: str, d: Path, trial: bool = False, started: dict | None = None) -> dict:
    """Check the records, drop the failing ones, render, check the page, accept (unless trial). Nothing goes back to
    the agent. started: the call's started row; if the pack (base or any input) changed since the call, the page is
    never accepted, and the accepted record names the dictionary the call saw."""
    ann = d / "annotations.jsonl"
    if not ann.exists():
        return {"check": "no annotations.jsonl", "ok": False}
    started = started or {}
    dst = OUT / f"s{s:03d}" / page_name(s, target)
    if not trial and dst.exists():  # before anything is rendered or written
        return {"check": f"{rel(dst)} exists (never overwrite)", "ok": False}
    now = R.target_page(s, target)[2]["sha256"]
    if started.get("base_sha256") and now != started["base_sha256"]:
        return {"check": f"base changed since the call ({started['base_sha256'][:12]} -> {now[:12]}): never "
                         f"accepted; run a new attempt on the new base", "ok": False}
    pack_now = hashlib.sha256((wd(s) / "pack" / "pack.json").read_bytes()).hexdigest()
    if started.get("pack_sha256") and pack_now != started["pack_sha256"]:
        return {"check": "the pack was rebuilt since the call (pack.json differs): the page's inputs are no longer "
                         "the ones the call saw; never accepted; run a new attempt", "ok": False}
    try:
        recs = R.load(ann)
    except SystemExit as e:
        return {"check": f"annotations.jsonl unreadable: {e}", "ok": False}
    kept, dropped, warnings = VAL.check_records(s, target, recs, GELENEK[BRIEF])
    page_dir = d / "page"
    if page_dir.exists():
        shutil.rmtree(page_dir)
    page, placement = R.render(s, target, kept, page_dir)
    name, base, info = R.target_page(s, target)
    page_errors = VAL.check_page(page, base, kept) + placement
    check = {"surah": s, "target": target, "records": len(recs), "kept": len(kept), "dropped": dropped,
             "warnings": warnings, "page_errors": page_errors}
    (d / "check.json").write_text(json.dumps(check, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    counts = {"kept": len(kept), "dropped": len(dropped), "warnings": len(warnings)}
    if page_errors:
        return {"check": f"page errors: {len(page_errors)} (see check.json)", "ok": False, **counts}
    if trial:
        return {"check": "ok (trial: page in the call directory only)", "ok": True, **counts}
    dictionary = started.get("dictionary") or json.loads((wd(s) / "pack" / "pack.json").read_text(encoding="utf-8")).get("dictionary")
    errata = [r for r in kept if r.get("tur") == "duzeltme"]
    logged = set()
    for line in (ERRATA.read_text(encoding="utf-8").splitlines() if ERRATA.exists() else []):
        try:
            x = json.loads(line)
        except json.JSONDecodeError:
            continue  # a hand-edited line; never rewritten here
        logged.add((x.get("surah"), x.get("target"), x.get("id"), x.get("taban")))
    with ERRATA.open("a", encoding="utf-8") as f:  # before the page: an accepted page never lacks its errata
        for r in errata:
            if (s, target, r["id"], r.get("taban")) in logged:  # a failed earlier accept already logged it
                print(f"NOTE: {r['id']} already in errata.jsonl (an earlier accept of this page); not repeated",
                      flush=True)
                continue
            f.write(json.dumps({"surah": s, "target": target, "base": info["path"], "id": r["id"], "taban": r.get("taban"),
                                "hata": r.get("hata"), "metin": r.get("metin"), "kaynak": r.get("kaynak")},
                               ensure_ascii=False) + "\n")
    dst.parent.mkdir(parents=True, exist_ok=True)
    with open(page, "rb") as src, open(dst, "xb") as out:  # exclusive: never overwrite, even in a race
        out.write(src.read())
    rec = {"surah": s, "target": target, "accepted_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
           "page_sha256": hashlib.sha256(dst.read_bytes()).hexdigest(), "base": info,
           "dictionary": dictionary, "annotations": rel(ann),
           "kept": len(kept), "dropped": [x["id"] for x in dropped]}
    dst.with_suffix(".json").write_text(json.dumps(rec, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return {"check": "ok", "ok": True, **counts, "errata": len(errata)}


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
        _, base_text, info = R.target_page(s, target)
        pack_bytes = (wd(s) / "pack" / "pack.json").read_bytes()
        pack_sha = hashlib.sha256(pack_bytes).hexdigest()
        dictionary = json.loads(pack_bytes).get("dictionary")
    except (Exception, SystemExit) as e:  # a missing pack, base or brief stops this job, not the whole batch
        return {"surah": s, "target": target, "model": model, "status": "error", "reason": f"prompt: {e}"}
    d.mkdir(parents=True, exist_ok=True)
    row = {"surah": s, "target": target, "attempt": attempt, "brief": BRIEF, "model": model, "model_id": model_id,
           "runner": runner, "effort": effort, "trial": trial, "prompt_sha256": sha(prompt), "prompt_chars": len(prompt),
           "base_sha256": info["sha256"], "base_words": len(base_text.split()), "pack_sha256": pack_sha,
           "dictionary": dictionary,
           "started": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    try:
        with (d / "started.json").open("x", encoding="utf-8") as f:
            json.dump(row, f, ensure_ascii=False, indent=1)
    except FileExistsError:  # another orchestrator started it a moment ago
        return {"surah": s, "target": target, "model": model, "status": "skipped",
                "reason": "started by another process (never rerun)"}
    (d / "prompt.md").write_text(prompt, encoding="utf-8")
    if runner == "codex":
        row["weekly_before"] = weekly_now()
    t0 = time.monotonic()
    try:
        if runner == "codex":
            row.update(call_codex(prompt, d, model_id, effort))
            sf = session_file(d)
            row["session"] = read_session(sf) if sf else {"missing": "no Codex session log found for this call"}
        else:
            row.update(call_claude(prompt, d, model_id, effort))
        if row["returncode"] == 0 and row["turn_completed"]:
            res = finish(s, target, d, trial, row)
        else:
            why = ("timed out after %ds" % TIMEOUT if row.get("timed_out") else
                   f"result {row['result_subtype']}" if row.get("result_subtype") not in (None, "success") else
                   "result marked is_error" if row.get("result_is_error") else
                   f"exit code {row['returncode']}" if row["returncode"] else "no result or completed turn in the stream")
            res = {"check": f"call did not complete ({why}; see stderr.log and run.stream.jsonl)", "ok": False}
        row["status"] = "ok" if res.pop("ok") else "error"
        row.update(res)
    except (Exception, SystemExit) as e:  # keep the record (run.log.json, ledger); never retry automatically
        row.update(status="error", error=f"{type(e).__name__}: {e}")
    row["seconds"] = round(time.monotonic() - t0)
    (d / "run.log.json").write_text(json.dumps(row, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log(row)
    return row


def spawn_target(s: int, target: str, model: str, effort: str, attempt: int = 1, trial: bool = False) -> dict:
    """Prepare one page call for an agent the orchestrator spawns (user, 2026-10-04 evening): prompt.md, started.json
    (the never-rerun guard, with the base and pack hashes), spawn.md with the Agent tool's text. No model call."""
    runner, model_id = MODELS[model]
    if runner != "claude":
        return {"surah": s, "target": target, "model": model, "status": "error",
                "reason": "spawn is for Claude agents; Codex models run through `run`"}
    d = call_dir(s, target, attempt, model, effort)
    if blocked(d):
        return {"surah": s, "target": target, "model": model, "status": "skipped",
                "reason": "started or finished before (never rerun)"}
    if accepted(s, target) and not trial:
        return {"surah": s, "target": target, "model": model, "status": "skipped", "reason": "page already accepted"}
    try:
        prompt = build_prompt(s, target, d, runner)
        _, base_text, info = R.target_page(s, target)
        pack_bytes = (wd(s) / "pack" / "pack.json").read_bytes()
    except (Exception, SystemExit) as e:
        return {"surah": s, "target": target, "model": model, "status": "error", "reason": f"prompt: {e}"}
    row = {"surah": s, "target": target, "attempt": attempt, "brief": BRIEF, "model": model, "model_id": model_id,
           "runner": "agent", "effort": effort, "trial": trial, "prompt_sha256": sha(prompt), "prompt_chars": len(prompt),
           "base_sha256": info["sha256"], "base_words": len(base_text.split()),
           "pack_sha256": hashlib.sha256(pack_bytes).hexdigest(), "dictionary": json.loads(pack_bytes).get("dictionary")}
    row["mode"] = MODE
    AR.prepare(d, prompt, row, "enrich-dosya" if MODE == "dosya" else "enrich", "annotations.jsonl", lookup=False)
    return {"surah": s, "target": target, "model": model, "status": "prepared", "dir": rel(d),
            "spawn": rel(d / "spawn.md"), "agent": AR.AGENT_TYPE["enrich"]}


def finish_target(s: int, target: str, d: Path, trial: bool = False) -> dict:
    """Finish an agent-spawned page call: the agent's annotations.jsonl and its transcript (cost, commands, stop
    reason), then finish() exactly as after a CLI call; run.log.json and the ledger row as before."""
    st_path = d / "started.json"
    if not st_path.exists() or json.loads(st_path.read_text(encoding="utf-8")).get("runner") != "agent":
        return {"surah": s, "target": target, "status": "error", "reason": f"{rel(d)}: not an agent-spawned call"}
    if (d / "run.log.json").exists():
        return {"surah": s, "target": target, "status": "error", "reason": f"{rel(d)}: already finished; never twice"}
    row = json.loads(st_path.read_text(encoding="utf-8"))
    t0 = time.mktime(time.strptime(row["started"], "%Y-%m-%dT%H:%M:%S"))
    obj = AR.finish(d, "annotations.jsonl")
    row.update({"returncode": 0, "turn_completed": not obj.get("is_error") and obj.get("completed", obj.get("stop_reason") in (None, "end_turn")),
                "usage": obj.get("usage") or {}, "cost_usd": obj.get("total_cost_usd"), "cost_basis": obj.get("cost_basis"),
                "num_turns": obj.get("num_turns"), "commands": obj.get("tool_calls", 0), "transcript": obj.get("transcript"),
                "agent_id": obj.get("agent_id"), "stop_reason": obj.get("stop_reason"), "safety_stop": obj.get("safety_stop")})
    try:
        if row["turn_completed"]:
            res = finish(s, target, d, trial, row)
        else:
            res = {"check": f"call did not complete ({obj.get('error') or 'stop_reason ' + str(obj.get('stop_reason'))})",
                   "ok": False}
        row["status"] = "ok" if res.pop("ok") else "error"
        row.update(res)
    except (Exception, SystemExit) as e:
        row.update(status="error", error=f"{type(e).__name__}: {e}")
    row["seconds"] = round(time.time() - t0)
    (d / "run.log.json").write_text(json.dumps(row, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    log(row)
    return row


def merge_page(s: int, target: str) -> bool:
    """out/sNNN/<page>.merged.md from the accepted Islamic page and the accepted Bible page (whichever exist): the
    kept records of both, rendered into the frozen base; the Islamic records get gelenek islami. Never overwrites
    an accepted page; the merged file is rewritten each time."""
    global BRIEF
    stem = "surah" if target == "surah" else tag(target)
    recs, parts = [], []
    for brief in ("zengin", "ehlikitap"):
        BRIEF = brief
        rec_path = (OUT / f"s{s:03d}" / page_name(s, target)).with_suffix(".json")
        if not rec_path.exists():
            continue
        rec = json.loads(rec_path.read_text(encoding="utf-8"))
        dropped = set(rec.get("dropped") or [])
        rs = [r for r in R.load(PG / rec["annotations"]) if r.get("id") not in dropped]
        for r in rs:
            if brief == "zengin":
                r.setdefault("gelenek", "islami")
        recs += rs
        parts.append(f"{brief} {len(rs)}")
    BRIEF = "zengin"
    if not recs:
        print(f"WARNING: S{s} {target}: no accepted page of either pass; nothing merged", flush=True)
        return False
    name, base, info = R.target_page(s, target)
    metas = {m["id"]: m for m in VAL.C.sources()}
    head = (f"<!-- schema:zenginlestirme {VAL.B.SCHEMA['version']}; target:{'S' + str(s) if target == 'surah' else target}; "
            f"base:{info['path']} sha256:{info['sha256']}; merged:{time.strftime('%Y-%m-%d')}; layers: {', '.join(parts)} -->")
    text, errors = R.render_page(base, recs, head, None if target == "surah" else R.AYAH_SECTION, metas)
    if errors:
        for e in errors:
            print(f"WARNING: S{s} {target} merge: {e}", flush=True)
        return False
    dst = OUT / f"s{s:03d}" / f"{stem}.merged.md"
    dst.write_text(text, encoding="utf-8")
    print(json.dumps({"surah": s, "target": target, "merged": rel(dst), "layers": parts}, ensure_ascii=False), flush=True)
    return True


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
        if t != "surah" and not accepted(s, t):
            try:
                R.target_page(s, t)
            except SystemExit as e:
                line = f"blocked: {e}"
        for d in sorted(wd(s).glob(f"{BRIEF}.{tag(t)}*")):
            if d.name != f"{BRIEF}.{tag(t)}" and not d.name.startswith(f"{BRIEF}.{tag(t)}."):
                continue
            if (d / "run.log.json").exists():
                r = json.loads((d / "run.log.json").read_text(encoding="utf-8"))
                line += (f"\n      {d.name}: {r.get('status')} {r.get('check', '')} kept {r.get('kept', '-')} dropped "
                         f"{r.get('dropped', '-')} {r.get('seconds', '')}s in {(r.get('usage') or {}).get('input_tokens', '')}"
                         + (f" ${r['cost_usd']:.2f}" if r.get("cost_usd") else ""))
            elif (d / "dead.json").exists():
                dead = json.loads((d / "dead.json").read_text(encoding="utf-8"))
                line += f"\n      {d.name}: died (confirmed {dead.get('at')}; never rerun; a new attempt needs the go)"
            elif (d / "started.json").exists():
                line += f"\n      {d.name}: started (running or interrupted)"
                started = json.loads((d / "started.json").read_text(encoding="utf-8"))
                stream = d / "run.stream.jsonl"
                if started.get("runner") == "claude" and stream.exists():
                    turns = tools = 0
                    for ev_line in stream.read_text(encoding="utf-8").splitlines():
                        try:
                            ev = json.loads(ev_line)
                        except json.JSONDecodeError:
                            continue
                        if ev.get("type") == "assistant":
                            turns += 1
                            tools += sum(1 for c in (ev.get("message") or {}).get("content", [])
                                         if c.get("type") == "tool_use")
                    idle = round(time.time() - stream.stat().st_mtime)
                    line += (f"; so far {turns} assistant events, {tools} tool calls; last activity {idle}s ago"
                             + (" (finishing: the model is done when run.log.json appears)" if (d / "response.md").exists()
                                else ""))
                sf = session_file(d)
                if sf:
                    u = read_session(sf)
                    tok = u.get("tokens") or {}
                    line += (f"; so far: in {tok.get('input_tokens', 0):,} (cached {tok.get('cached_input_tokens', 0):,}) "
                             f"out {tok.get('output_tokens', 0):,}; context {u.get('context_tokens_last_turn') or 0:,}; "
                             f"weekly {u.get('weekly_used_first')}→{u.get('weekly_used_last')}%")
        print(f"  {t:8} {line}")
    if missing_ayat(s):
        print(f"  no ayah base (v16 augment9 not run, or the pack predates it): {', '.join(missing_ayat(s))}")


def confirm_dead(s: int, name: str) -> None:
    """Mark a call that started and never finished as dead (dead.json), after checking that no process still runs
    it. The directory stays blocked (never rerun); the marker only lets pack.py --force and corpus.py build proceed."""
    d = wd(s) / name
    if not (d / "started.json").exists() or (d / "run.log.json").exists():
        raise SystemExit(f"{rel(d)}: not a started call without run.log.json")
    ps = subprocess.run(["ps", "-ax", "-o", "pid=,command="], capture_output=True, text=True, check=True).stdout
    alive = [l.strip()[:120] for l in ps.splitlines()
             if str(d) in l or ("enrich.py" in l and (" run" in l or " accept" in l))]
    if alive:  # the orchestrator checks and renders for minutes after the model exits
        raise SystemExit(f"{rel(d)}: a call or an enrich.py run/accept is still alive: {alive}")
    recent = max(p.stat().st_mtime for p in d.rglob("*") if p.is_file())
    if time.time() - recent < 30 * 60:
        raise SystemExit(f"{rel(d)}: files changed {round((time.time() - recent) / 60)} min ago; wait 30 minutes "
                         f"of silence before confirming the call dead")
    row = {"at": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "checked": "no process command line names the directory"}
    with (d / "dead.json").open("x", encoding="utf-8") as f:
        json.dump(row, f, ensure_ascii=False, indent=1)
    log({"surah": s, "stage": "confirm-dead", "dir": rel(d), **row})
    print(f"{rel(d)}: marked dead; it stays blocked (a new try is --attempt N, with the user's go)")


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
    ap.add_argument("cmd", choices=("status", "build", "spawn", "finish", "run", "accept", "confirm-dead", "merge"))
    ap.add_argument("--surah", type=int)
    ap.add_argument("--surahs")
    ap.add_argument("--target", help="surah | S:A | ayat | all (required for build, run and accept)")
    ap.add_argument("--model", default=RUN_MODEL, help=f"key[:effort],... of {', '.join(MODELS)}")
    ap.add_argument("--effort", default=EFFORT, choices=("low", "medium", "high", "max"))
    ap.add_argument("--attempt", type=int, default=1)
    ap.add_argument("--trial", action="store_true", help="render in the call directory only; no out/, no errata")
    ap.add_argument("--parallel", type=int, default=2)
    ap.add_argument("--dir", help="confirm-dead: the call directory name (e.g. zengin.surah.opus.high)")
    ap.add_argument("--mode", choices=("agent", "dosya"), default="agent",
                    help="dosya: one tool-free call on a script-built dossier (ayah pages; call dir zengin-dosya.<page>…)")
    ap.add_argument("--pass", dest="pass_", choices=("zengin", "ehlikitap"), default="zengin",
                    help="ehlikitap: the Bible pass (its own call dirs, pages <page>.ehlikitap.md, the intertext index)")
    a = ap.parse_args()
    global BRIEF, MODE
    BRIEF = a.pass_
    MODE = a.mode
    ss = surahs(a.surahs) if a.surahs else [a.surah]
    if None in ss:
        ap.error("--surah or --surahs")
    if a.cmd == "status":
        for s in ss:
            status(s)
        return
    if a.cmd == "confirm-dead":
        if len(ss) != 1 or not a.dir:
            ap.error("confirm-dead takes --surah and --dir")
        confirm_dead(ss[0], a.dir)
        return
    specs = model_specs(a.model, a.effort)
    if not a.target:
        ap.error("--target is required: surah | S:A | ayat | all")
    if a.cmd == "merge":  # the layers of both passes on one page: islami, then tevrat, then incil after each paragraph
        failed = 0
        for s in ss:
            for t in select(s, a.target):
                failed += not merge_page(s, t)
        sys.exit(1 if failed else 0)
    if a.cmd == "accept":  # a finished trial page becomes the accepted page (no model call)
        if len(specs) != 1 or a.target in ("ayat", "all"):
            ap.error("accept takes one --model and one page (--target surah or S:A)")
        (m, e), = specs
        for s in ss:
            d = call_dir(s, a.target, a.attempt, m, e)
            log_path = d / "run.log.json"
            row = json.loads(log_path.read_text(encoding="utf-8")) if log_path.exists() else {}
            if row.get("status") != "ok":
                raise SystemExit(f"{rel(d)}: no successful run to accept")
            if not row.get("base_sha256"):
                print(f"NOTE: {rel(d)} predates base/pack hashing: the base-change guard is skipped for it", flush=True)
            res = finish(s, a.target, d, trial=False, started=row)
            ok = res.pop("ok")
            if ok:  # a failed accept goes to the ledger only; run.log.json keeps the call's own record
                row["accepted"] = {"at": time.strftime("%Y-%m-%dT%H:%M:%S%z"), **res}
                log_path.write_text(json.dumps(row, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            log({"surah": s, "target": a.target, "stage": "accept", "model": m, "effort": e, "dir": rel(d),
                 "status": "ok" if ok else "error", **res})
            print(json.dumps({"surah": s, "target": a.target, "dir": rel(d), "status": "ok" if ok else "error", **res},
                             ensure_ascii=False))
            if not ok:
                print(f"WARNING: S{s} {a.target}: not accepted — {res.get('check')}", flush=True)
                sys.exit(1)
        return
    if a.cmd == "run" and len(specs) > 1 and not a.trial:
        ap.error("several models on the same pages only with --trial (otherwise they race for the accepted page)")
    jobs, pack_failed = [], 0
    for s in ss:
        if not ensure_pack(s):
            pack_failed += 1
            print(f"WARNING: S{s}: no pack (pack.py failed; see the line above); no page of S{s} runs", flush=True)
            continue
        jobs += [(s, t, m, e) for t in select(s, a.target) for m, e in specs]
        if a.target in ("ayat", "all") and missing_ayat(s):
            print(f"NOTE: S{s}: no ayah page for {', '.join(missing_ayat(s))} (no augment9 base in the pack)", flush=True)
    if a.cmd == "build":
        for s, t, m, e in jobs:
            d = call_dir(s, t, a.attempt, m, e)
            p = build_prompt(s, t, d, MODELS[m][0])
            skip = (" [exists: will be skipped]" if blocked(d) else
                    " [page already accepted: will be skipped]" if accepted(s, t) and not a.trial else "")
            try:
                R.target_page(s, t)
            except SystemExit as err:
                skip += f" [BLOCKED: {err}]"
            print(f"S{s} {t} {m} ({MODELS[m][1]}, {e}): prompt {len(p):,} chars; estimate {estimate(s, t, m, e)} "
                  f"-> {rel(d)}{skip}")
        print(f"{len(jobs)} calls")
        if pack_failed:
            sys.exit(1)
        return
    failed = pack_failed
    if a.cmd in ("spawn", "finish"):  # agent-spawned runs: no model call here (user, 2026-10-04 evening)
        for s, t, m, e in jobs:
            r = (spawn_target(s, t, m, e, a.attempt, a.trial) if a.cmd == "spawn" else
                 finish_target(s, t, call_dir(s, t, a.attempt, m, e), a.trial))
            print(json.dumps({k: r.get(k) for k in ("surah", "target", "model", "status", "dir", "spawn", "agent", "check",
                                                     "kept", "dropped", "warnings", "errata", "seconds", "cost_usd",
                                                     "reason", "error", "commands", "stop_reason")
                              if r.get(k) not in (None, 0, False) or k in ("status",)}, ensure_ascii=False), flush=True)
            if r.get("status") not in ("ok", "prepared", "skipped"):
                failed += 1
                print(f"WARNING: S{s} {t} {m}: {r.get('status')} — {r.get('check') or r.get('reason') or r.get('error')}",
                      flush=True)
            elif r.get("status") == "skipped":
                print(f"NOTE: S{s} {t} {m}: skipped — {r.get('reason')}", flush=True)
        if failed:
            sys.exit(1)
        return
    with cf.ThreadPoolExecutor(a.parallel) as ex:
        for r in ex.map(lambda j: run_target(j[0], j[1], j[2], j[3], a.attempt, a.trial), jobs):
            print(json.dumps({k: r.get(k) for k in ("surah", "target", "model", "status", "check", "kept", "dropped",
                                                     "warnings", "errata", "seconds", "cost_usd", "reason", "error",
                                                     "permission_denials", "stream_unparsable", "timed_out")
                              if r.get(k) not in (None, 0, False) or k in ("status", "kept", "dropped")},
                             ensure_ascii=False), flush=True)
            if r.get("status") != "ok":
                failed += r.get("status") == "error"
                print(f"WARNING: S{r['surah']} {r['target']} {r.get('model')}: {r.get('status')} — "
                      f"{r.get('check') or r.get('reason') or r.get('error')}", flush=True)
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
