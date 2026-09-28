#!/usr/bin/env python3
"""E1: memory permission without a ledger (review PHASE2_REPORT.md §8).

The v9 dictionary arm (w10-opus-dict) rebuilt byte for byte (same brief write_v10.md md5 dddcd1b2, same system
prompt, same inlined files in the same order), with ONE change: the evidence clause adds "and your own knowledge of
Arabic and the Quran", exactly as the cold arm's clause did. No ledger. Two replicates per ayah.

Differences from the 2026-09-26 runs that cannot be avoided: safe mode from a temp directory (so no CLAUDE.md,
memory, skills or hooks reach the model), and today's CLI version.

Rules: never rerun an existing output; no retries; a call starts only if its estimate is below $5; every call is
logged in e1/ledger.jsonl.

Usage: python3 e1_permission.py --dry | --run [--parallel 4]
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
V9 = REPO / "_commentary" / "v9"
OUT = HERE / "e1"
W10 = V9 / "prompts" / "write_v10.md"
SYSTEM = ("You are a careful scholar of Quranic Arabic and a fine Turkish prose writer. Follow the brief in the "
          "user message exactly and return only the requested output.")
AYAT = ["1:2", "1:6", "4:34", "18:86", "100:1", "100:6"]
REPS = [1, 2]
EVIDENCE = ("context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md "
            "(every attested branch of every root of the ayah's words, with the classical dictionaries' source "
            "phrases) and your own knowledge of Arabic and the Quran")
GATE_USD = 5.0
OUT_TOKENS_ASSUMED = 60_000  # conservative (permitted calls are unmeasured; cold 4:34 reached 60k)


def rel(p: Path) -> str:
    return str(p.relative_to(REPO))


def inline(*files: Path) -> str:  # identical to v9/luna/run.py inline()
    return "\n\n".join(f"===== {rel(p)} =====\n{p.read_text(encoding='utf-8')}" for p in files)


def paths(ref: str) -> tuple[Path, Path]:
    s, a = ref.split(":")
    sa = f"{s}_{a}"
    return V9 / "lines" / "work" / sa / "context.md", V9 / "input" / "v2" / f"s{int(s):03d}" / sa / "01_dictionary.md"


def build(ref: str) -> str:
    ctx, dic = paths(ref)
    stdin = inline(W10, ctx, dic)
    prompt = (f"Focus: {ref}. Follow the brief below (write.md) exactly. The evidence is {EVIDENCE}. Return only the "
              f"reader's prose as your final message.")
    return prompt + "\n\n" + stdin


def est_tokens(text: str) -> int:  # cost critic's calibrated formula (c01)
    ar = len(re.findall(r"[؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿]", text))
    return int(4581 + 1.151 * ar + 0.366 * (len(text) - ar))


def estimate(text: str) -> float:
    return est_tokens(text) * 8e-6 + OUT_TOKENS_ASSUMED * 20e-6


def log(row: dict) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "ledger.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def run_one(ref: str, rep: int) -> str:
    s, a = ref.split(":")
    d = OUT / f"{s}_{a}" / f"rep{rep}"
    if (d / "run.log.json").exists():
        return f"{ref} rep{rep}: exists, skipped (never rerun)"
    text = build(ref)
    est = estimate(text)
    if est >= GATE_USD:
        log({"ref": ref, "rep": rep, "status": "gated", "estimate_usd": round(est, 2)})
        return f"{ref} rep{rep}: gated at ${est:.2f}"
    d.mkdir(parents=True, exist_ok=True)
    (d / "prompt.md").write_text(text, encoding="utf-8")
    cmd = ["claude", "-p", "--model", "claude-opus-5-5", "--effort", "high", "--tools", "",
           "--output-format", "json", "--no-session-persistence", "--safe-mode",
           "--permission-mode", "dontAsk", "--system-prompt", SYSTEM]
    t0 = time.time()
    with tempfile.TemporaryDirectory(prefix="e1_opus_") as cwd:
        p = subprocess.run(cmd, input=text, capture_output=True, text=True, cwd=cwd)
    (d / "run.log.json").write_text((p.stdout or json.dumps({"error": p.stderr[-3000:]})).strip() + "\n",
                                    encoding="utf-8")
    try:
        obj = json.loads(p.stdout)
    except json.JSONDecodeError:
        obj = {}
    result = (obj.get("result") or "").strip()
    status = "ok" if result and not obj.get("is_error") else "error"
    if result:
        (d / f"{s}_{a}.reading.tr.md").write_text(result + "\n", encoding="utf-8")
    usage = obj.get("usage", {}) or {}
    row = {"ref": ref, "rep": rep, "status": status, "seconds": round(time.time() - t0),
           "cost_usd": obj.get("total_cost_usd"), "estimate_usd": round(est, 2),
           "output_tokens": usage.get("output_tokens"),
           "thinking_tokens": (usage.get("output_tokens_details") or {}).get("thinking_tokens"),
           "cache_write": usage.get("cache_creation_input_tokens"), "num_turns": obj.get("num_turns"),
           "words": len(result.split()) if result else 0, "prompt_chars": len(text)}
    log(row)
    return f"{ref} rep{rep}: {status} ${row['cost_usd']} {row['words']}w {row['seconds']}s"


def main() -> None:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry", action="store_true")
    g.add_argument("--run", action="store_true")
    ap.add_argument("--parallel", type=int, default=4)
    a = ap.parse_args()
    jobs = [(r, k) for r in AYAT for k in REPS]
    if a.dry:
        total = 0.0
        for r in AYAT:
            t = build(r)
            e = estimate(t)
            total += e * len(REPS)
            print(f"{r:7} {len(t):>8,} chars ~{est_tokens(t):>7,} tokens  est ${e:.2f}/call  (gate {'ok' if e < GATE_USD else 'BLOCK'})")
        print(f"upper-bound total for {len(jobs)} calls: ${total:.2f} (assumes {OUT_TOKENS_ASSUMED:,} output tokens each)")
        return
    with cf.ThreadPoolExecutor(a.parallel) as ex:
        for msg in ex.map(lambda j: run_one(*j), jobs):
            print(msg, flush=True)


if __name__ == "__main__":
    sys.exit(main())
