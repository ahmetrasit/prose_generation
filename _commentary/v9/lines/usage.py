#!/usr/bin/env python3
"""Token and tool-call monitor for every model session of one ayah, by stage.

Codex logs (JSONL events): turns = turn.completed events; tool calls = completed items that are not the agent's
message or reasoning (command executions, file changes, web searches …); tokens from turn.completed usage.
Claude logs (JSON result lines from `claude -p --output-format json`): turns, usage and total_cost_usd as reported.

Cost uses RATES (USD per million tokens) when a model's rates are filled in; cached input is billed at the cached
rate. Set rates from the providers' official pricing pages before quoting costs.

Usage: python3 _commentary/v9/lines/usage.py 18:86
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

V9 = Path(__file__).resolve().parents[1]

# USD per 1M tokens: input, cached input, output (reasoning is billed as output). None = not yet set.
RATES: dict[str, tuple[float, float, float] | None] = {
    "gpt-6-luna": None,
    "gpt-6-sol": None,
    "claude-opus": None,  # Claude runs report total_cost_usd themselves
}
NON_TOOL_ITEMS = {"agent_message", "reasoning"}


def codex_session(path: Path) -> dict:
    t = {"turns": 0, "tools": 0, "in": 0, "cached": 0, "out": 0, "reasoning": 0, "model": ""}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.startswith("{"):
            continue
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        if d.get("type") == "turn.completed":
            t["turns"] += 1
            u = d.get("usage") or {}
            t["in"] += u.get("input_tokens", 0) or 0
            t["cached"] += u.get("cached_input_tokens", 0) or 0
            t["out"] += u.get("output_tokens", 0) or 0
            t["reasoning"] += u.get("reasoning_output_tokens", 0) or 0
        elif d.get("type") == "item.completed":
            if ((d.get("item") or {}).get("type") or "") not in NON_TOOL_ITEMS:
                t["tools"] += 1
    return t


def claude_session(path: Path) -> dict:
    t = {"turns": 0, "tools": 0, "in": 0, "cached": 0, "cache_write": 0, "out": 0, "reasoning": 0, "cost": 0.0}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        u = d.get("usage") or {}
        t["turns"] += d.get("num_turns", 0) or 0
        t["in"] += u.get("input_tokens", 0) or 0
        t["cached"] += u.get("cache_read_input_tokens", 0) or 0
        t["cache_write"] += u.get("cache_creation_input_tokens", 0) or 0
        t["out"] += u.get("output_tokens", 0) or 0
        t["cost"] += d.get("total_cost_usd", 0) or 0
    t["tools"] = max(0, t["turns"] - 1)  # every turn after the first follows a tool call
    return t


def model_of(stage: str, path: Path) -> str:
    name = str(path)
    if path.suffix == ".json" or "opus" in name:
        return "claude-opus"
    if "sol" in name and "luna-write" not in name and "luna-writer" not in name and "review" not in path.stem \
            and "repair" not in path.stem:
        return "gpt-6-sol"
    return "gpt-6-luna"


def cost(model: str, t: dict) -> float | None:
    if "cost" in t and t.get("cost"):
        return t["cost"]
    r = RATES.get(model)
    if not r:
        return None
    rin, rcached, rout = r
    return ((t["in"] - t["cached"]) * rin + t["cached"] * rcached + t["out"] * rout) / 1e6


def main() -> None:
    ref = sys.argv[1]
    s, a = ref.split(":")
    sa = f"{s}_{a}"
    stages = {
        "network meaning pass": sorted((V9 / "network" / "out" / sa / "luna").glob("*.log.jsonl")),
        "discovery lines": sorted((V9 / "lines" / "work" / sa / "logs").glob("*.jsonl")),
        "synthesis arms": sorted((V9 / "lines" / "work" / sa / "synth").glob("*/*.log.json*")),
    }
    for d in sorted((V9 / "network" / "out" / sa).glob("sol*")):
        stages.setdefault(f"sol_pass {d.name}", sorted(d.glob("*.log.jsonl")))
    grand = {"in": 0, "cached": 0, "out": 0, "reasoning": 0, "tools": 0, "sessions": 0}
    for stage, files in stages.items():
        if not files:
            continue
        print(f"== {stage}")
        for f in files:
            t = claude_session(f) if f.suffix == ".json" else codex_session(f)
            m = model_of(stage, f)
            c = cost(m, t)
            flag = "  ⚠ tool calls" if t["tools"] else ""
            print(f"  {f.parent.name + '/' + f.name:48} {m:12} turns {t['turns']:>2} tools {t['tools']:>3} in {t['in']:>9,} "
                  f"cached {t['cached']:>9,} out {t['out']:>7,} reas {t.get('reasoning', 0):>7,} "
                  f"cost {('$%.3f' % c) if c is not None else 'n/a'}{flag}")
            for k in ("in", "cached", "out", "reasoning", "tools"):
                grand[k] += t.get(k, 0)
            grand["sessions"] += 1
    print(f"== TOTAL {grand['sessions']} sessions: in {grand['in']:,} cached {grand['cached']:,} out {grand['out']:,} "
          f"reasoning {grand['reasoning']:,} tool calls {grand['tools']}")


if __name__ == "__main__":
    main()
