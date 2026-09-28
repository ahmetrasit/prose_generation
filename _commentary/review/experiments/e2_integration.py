#!/usr/bin/env python3
"""E2: integration pilot on existing readings (review PHASE2_REPORT.md §8).

For 18:86, 4:34 and 1:6: integrate the existing v9 cold reading (w10-opus-cold) and dictionary reading
(w10-opus-dict) into one commentary (prompts/e2_integrate.md), 2 replicates with the reading order swapped. Then one
return call per replicate (prompts/e2_return.md) that sees the commentary, both readings and the script-computed list
of reading sentences whose refs or Arabic quotations the commentary does not carry. No guard flags, no must-land.

Pre-registered success criteria (scored by e2_score.py, then my comparison and the user's blind read):
 1. recall: the final commentary's pooled ingredient recall (refs + Arabic quotations across both inputs) is at
    least the better input's recall + 0.10 on >= 2 of 3 ayat, in both replicates;
 2. form: words <= 1.5 x the longer input; longest paragraph <= 300 words; disclaimer/negation rate <= the inputs';
 3. the user's blind read prefers the final commentary over the better input in >= 4 of 6 pairs.
Named ayat only (18:86 inputs are contaminated by the old brief example), so this tests integration mechanics,
not discovery.

Rules: never rerun; no retries; estimate gate $5 per call; ledger e2/ledger.jsonl; safe mode from a temp dir.
Usage: python3 e2_integration.py --dry | --run [--parallel 3]
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
V9W = REPO / "_commentary" / "v9" / "lines" / "work"
OUT = HERE / "e2"
BRIEF = HERE / "prompts" / "e2_integrate.md"
RETURN = HERE / "prompts" / "e2_return.md"
SYSTEM = ("You are a careful scholar of Quranic Arabic and a fine Turkish prose writer. Follow the brief in the "
          "user message exactly and return only the requested output.")
AYAT = ["18:86", "4:34", "1:6"]
GATE_USD = 5.0
OUT_TOKENS_ASSUMED = 50_000
REF = re.compile(r"\b(\d{1,3}):(\d{1,3})\b")
TAG = re.compile(r"\{\{?ar:([^,}]+)")
ARABIC = re.compile(r"[؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿]")
DIAC = re.compile(r"[ً-ٰٟۖ-ۭـ]")


def readings(ref: str) -> tuple[Path, Path, Path]:
    s, a = ref.split(":")
    w = V9W / f"{s}_{a}"
    return (w / "context.md", w / "synth" / "w10-opus-cold" / f"{s}_{a}.reading.tr.md",
            w / "synth" / "w10-opus-dict" / f"{s}_{a}.reading.tr.md")


def est_tokens(text: str) -> int:
    ar = len(ARABIC.findall(text))
    return int(4581 + 1.151 * ar + 0.366 * (len(text) - ar))


def estimate(text: str) -> float:
    return est_tokens(text) * 8e-6 + OUT_TOKENS_ASSUMED * 20e-6


def build_integrate(ref: str, rep: int) -> str:
    ctx, cold, dic = readings(ref)
    first, second = (cold, dic) if rep == 1 else (dic, cold)
    return (f"Focus: {ref}. Follow the brief below exactly.\n\n===== brief =====\n{BRIEF.read_text(encoding='utf-8')}"
            f"\n\n===== context.md =====\n{ctx.read_text(encoding='utf-8')}"
            f"\n\n===== reading 1 =====\n{first.read_text(encoding='utf-8')}"
            f"\n\n===== reading 2 =====\n{second.read_text(encoding='utf-8')}")


def norm_ar(s: str) -> str:
    return re.sub(r"\s+", " ", DIAC.sub("", s)).strip()


def ingredients(text: str) -> tuple[set[str], set[str]]:
    refs = {f"{int(a)}:{int(b)}" for a, b in REF.findall(text)}
    quotes = {norm_ar(q) for q in TAG.findall(text) if ARABIC.search(q)}
    return refs, quotes


def unselected(commentary: str, *sources: str) -> list[str]:
    """Sentences of the readings with at least one ref or Arabic quotation, none of which the commentary carries."""
    c_refs, c_quotes = ingredients(commentary)
    c_norm = norm_ar(commentary)
    out = []
    for src in sources:
        for sent in re.split(r"(?<=[.!?])\s+|\n{2,}", src):
            refs, quotes = ingredients(sent)
            if not refs and not quotes:
                continue
            carried = (refs & c_refs) or any(q in c_quotes or (len(q) > 6 and q in c_norm) for q in quotes)
            if not carried:
                out.append(sent.strip())
    return out


def claude(text: str, d: Path, name: str) -> dict:
    cmd = ["claude", "-p", "--model", "claude-opus-5-5", "--effort", "high", "--tools", "",
           "--output-format", "json", "--no-session-persistence", "--safe-mode",
           "--permission-mode", "dontAsk", "--system-prompt", SYSTEM]
    (d / f"{name}.prompt.md").write_text(text, encoding="utf-8")
    t0 = time.time()
    with tempfile.TemporaryDirectory(prefix="e2_opus_") as cwd:
        p = subprocess.run(cmd, input=text, capture_output=True, text=True, cwd=cwd)
    (d / f"{name}.run.log.json").write_text((p.stdout or json.dumps({"error": p.stderr[-3000:]})).strip() + "\n",
                                            encoding="utf-8")
    try:
        obj = json.loads(p.stdout)
    except json.JSONDecodeError:
        obj = {}
    result = (obj.get("result") or "").strip()
    if result:
        (d / f"{name}.tr.md").write_text(result + "\n", encoding="utf-8")
    usage = obj.get("usage", {}) or {}
    return {"status": "ok" if result and not obj.get("is_error") else "error", "seconds": round(time.time() - t0),
            "cost_usd": obj.get("total_cost_usd"), "output_tokens": usage.get("output_tokens"),
            "thinking_tokens": (usage.get("output_tokens_details") or {}).get("thinking_tokens"),
            "cache_write": usage.get("cache_creation_input_tokens"), "num_turns": obj.get("num_turns"),
            "words": len(result.split()) if result else 0, "prompt_chars": len(text), "result": result}


def log(row: dict) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "ledger.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps({k: v for k, v in row.items() if k != "result"}, ensure_ascii=False) + "\n")


def run_one(ref: str, rep: int) -> str:
    s, a = ref.split(":")
    d = OUT / f"{s}_{a}" / f"rep{rep}"
    if (d / "integrate.run.log.json").exists():
        return f"{ref} rep{rep}: exists, skipped (never rerun)"
    d.mkdir(parents=True, exist_ok=True)
    text = build_integrate(ref, rep)
    est = estimate(text)
    if est >= GATE_USD:
        log({"ref": ref, "rep": rep, "step": "integrate", "status": "gated", "estimate_usd": round(est, 2)})
        return f"{ref} rep{rep}: integrate gated ${est:.2f}"
    r1 = claude(text, d, "integrate")
    log({"ref": ref, "rep": rep, "step": "integrate", "estimate_usd": round(est, 2), **r1})
    if r1["status"] != "ok":
        return f"{ref} rep{rep}: integrate {r1['status']} (no rerun)"
    _, cold, dic = readings(ref)
    un = unselected(r1["result"], cold.read_text(encoding="utf-8"), dic.read_text(encoding="utf-8"))
    (d / "unselected.md").write_text("\n\n".join(f"- {u}" for u in un) + "\n", encoding="utf-8")
    first, second = (cold, dic) if rep == 1 else (dic, cold)
    rtext = (f"Focus: {ref}.\n\n===== instruction =====\n{RETURN.read_text(encoding='utf-8')}"
             f"\n\n===== original brief =====\n{BRIEF.read_text(encoding='utf-8')}"
             f"\n\n===== reading 1 =====\n{first.read_text(encoding='utf-8')}"
             f"\n\n===== reading 2 =====\n{second.read_text(encoding='utf-8')}"
             f"\n\n===== your commentary =====\n{r1['result']}"
             f"\n\n===== sentences from the readings not carried ({len(un)}) =====\n" + "\n\n".join(f"- {u}" for u in un))
    est2 = estimate(rtext)
    if est2 >= GATE_USD:
        log({"ref": ref, "rep": rep, "step": "return", "status": "gated", "estimate_usd": round(est2, 2)})
        return f"{ref} rep{rep}: return gated ${est2:.2f}"
    r2 = claude(rtext, d, "final")
    log({"ref": ref, "rep": rep, "step": "return", "estimate_usd": round(est2, 2), "unselected": len(un), **r2})
    return (f"{ref} rep{rep}: integrate ${r1['cost_usd']} {r1['words']}w; unselected {len(un)}; "
            f"return {r2['status']} ${r2['cost_usd']} {r2['words']}w")


def main() -> None:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry", action="store_true")
    g.add_argument("--run", action="store_true")
    ap.add_argument("--parallel", type=int, default=3)
    a = ap.parse_args()
    jobs = [(r, k) for r in AYAT for k in (1, 2)]
    if a.dry:
        total = 0.0
        for r in AYAT:
            t = build_integrate(r, 1)
            e = estimate(t)
            # the return call re-reads brief + both readings + commentary (~ the readings' size) + unselected list
            e2 = estimate(t) + 0.0
            total += (e + e2) * 2
            print(f"{r:6} integrate {len(t):>8,} chars ~{est_tokens(t):>6,} tok  est ${e:.2f}; return ~${e2:.2f}")
        print(f"upper-bound total for {len(jobs)} replicates x 2 calls: ${total:.2f}")
        return
    with cf.ThreadPoolExecutor(a.parallel) as ex:
        for msg in ex.map(lambda j: run_one(*j), jobs):
            print(msg, flush=True)


if __name__ == "__main__":
    sys.exit(main())
