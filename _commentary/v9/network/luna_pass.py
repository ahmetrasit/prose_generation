#!/usr/bin/env python3
"""Bounded Luna pass over the ayah network: ayah-internal meaning links the script cannot make precisely.

  build  REF   worklist of rare branches × the other words of the ayah they already touch (any edge kind),
               with each word's plain sense and the script's hints → network/out/S_A/luna/W_network.md (+ map)
  run    REF   one Luna session per bundle (gpt-6-luna, reasoning effort max), everything pushed in the prompt,
               records returned as the final message → luna/records.jsonl; then check
  check  REF   every item has a lines string of the right length; every r/n line has a record with a reason

Kept lines (r, n) become `luna` edges when network.py runs with --luna network/out/S_A/luna/records.jsonl.

Usage: python3 _commentary/v9/network/luna_pass.py build|run|check 29:38 [--net network.k3-inter.json]
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

V9 = Path(__file__).resolve().parents[1]
REPO = V9.parents[1]
LUNA = "gpt-6-luna"
GPT_OPTS = ["-c", 'model_reasoning_effort="max"', "-c", "tool_output_token_limit=20000", "--json"]
BUNDLE_BYTES = 40_000


def paths(ref: str, net_name: str) -> dict[str, Path]:
    s, a = ref.split(":")
    out = V9 / "network" / "out" / f"{s}_{a}"
    return {"net": out / net_name, "dir": out / "luna", "context": V9 / "luna" / "work" / f"{s}_{a}" / "context.md"}


def short(e: dict) -> str:
    return f"{e['kind']}{'/' + e['sub'] if e['sub'] else ''}: {e['evidence'][:140]}"


def build(ref: str, net_name: str) -> None:
    p = paths(ref, net_name)
    d = json.loads(p["net"].read_text(encoding="utf-8"))
    N = d["nodes"]
    plain = defaultdict(list)
    for n, x in N.items():
        if x["type"] == "B" and x.get("plain"):
            plain[x["word"]].append(f"{x['gloss']} / {x['image']}")
    lines_of = defaultdict(lambda: defaultdict(list))
    for e in d["edges"]:
        for a, b in ((e["a"], e["b"]), (e["b"], e["a"])):
            if N.get(a, {}).get("type") == "B" and N[a]["rare"] and b.startswith("F:") and b != N[a]["word"] \
                    and e["kind"] not in ("hft", "luna"):
                lines_of[a][b].append(e)
    items, mapping = [], {}
    for i, (b, targets) in enumerate(sorted(lines_of.items(), key=lambda kv: (N[kv[0]]["word"], kv[0])), 1):
        x = N[b]
        iid = f"N{i:02d}"
        head = (f"### {iid} {x['root']} {x['bid']} «{x['gloss']}» @ {N[x['word']]['surface']} — lines: {len(targets)}"
                + (" (echo root: sound family, not identity)" if x["root_kind"] == "echo" else ""))
        body = [head, f"image: {x['image']}", f"source phrases: {x['src']}", f"codes: {'_' * len(targets)} ({len(targets)})"]
        for k, (f, es) in enumerate(sorted(targets.items(), key=lambda kv: N[kv[0]]["w"]), 1):
            hints = "; ".join(dict.fromkeys(short(e) for e in es))
            body.append(f"[{k}] → {N[f]['surface']} (w{N[f]['w']}) plain sense: {' | '.join(plain[f]) or '—'} || hints: {hints}")
            mapping[f"{iid}.{k}"] = {"b": b, "f": f}
        items.append("\n".join(body))
    p["dir"].mkdir(parents=True, exist_ok=True)
    bundles, cur = [], []
    for it in items:
        if cur and sum(len(x.encode()) for x in cur) + len(it.encode()) > BUNDLE_BYTES:
            bundles.append(cur)
            cur = []
        cur.append(it)
    if cur:
        bundles.append(cur)
    for n, bl in enumerate(bundles, 1):
        ids = [x.split()[1] for x in bl]
        (p["dir"] / f"W_network_{n}.md").write_text(
            f"# W_network_{n}.md — {len(bl)} items: {ids[0]} … {ids[-1]}\n\n" + "\n\n".join(bl) + "\n", encoding="utf-8")
    (p["dir"] / "map.json").write_text(json.dumps(mapping, ensure_ascii=False, indent=0), encoding="utf-8")
    print(f"{len(items)} items, {len(mapping)} lines, {len(bundles)} bundle(s) → {p['dir']}")


def check(ref: str, net_name: str) -> list[str]:
    p = paths(ref, net_name)
    mapping = json.loads((p["dir"] / "map.json").read_text(encoding="utf-8"))
    n_lines = defaultdict(int)
    for k in mapping:
        n_lines[k.split(".")[0]] += 1
    recs = {}
    for f in sorted(p["dir"].glob("records_*.jsonl")):
        for line in f.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("{"):
                r = json.loads(line)
                recs[r.get("id")] = r
    problems = []
    for iid, n in n_lines.items():
        codes = str(recs.get(iid, {}).get("lines", ""))
        if len(codes) != n or set(codes) - set("rn-"):
            problems.append(f"{iid}: lines {codes!r} should be {n} codes of r/n/-")
            continue
        for k, c in enumerate(codes, 1):
            r = recs.get(f"{iid}.{k}")
            if c in "rn" and (not r or len(str(r.get("reason", ""))) < 40):
                problems.append(f"{iid}.{k}: code {c} needs a record with a specific reason")
    kept = sum(str(r.get("lines", "")).count(c) for r in recs.values() for c in "rn")
    print(f"check: {len(problems)} problem(s); kept lines {kept} of {len(mapping)}")
    return problems


def run(ref: str, net_name: str) -> None:
    p = paths(ref, net_name)
    brief = (V9 / "prompts" / "luna_network.md").read_text(encoding="utf-8")
    context = p["context"].read_text(encoding="utf-8")
    for wl in sorted(p["dir"].glob("W_network_*.md")):
        out = p["dir"] / f"records_{wl.stem.split('_')[-1]}.jsonl"
        if out.exists():
            continue
        last = p["dir"] / f"{wl.stem}.last.txt"
        stdin = f"===== luna_network.md =====\n{brief}\n\n===== context.md =====\n{context}\n\n===== {wl.name} =====\n" \
                + wl.read_text(encoding="utf-8")
        cmd = ["codex", "exec", "-m", LUNA, "-s", "read-only", "-C", str(REPO)] + GPT_OPTS + [
            "-o", str(last), "Follow the brief below (luna_network.md) exactly. The brief, context.md and your worklist "
                             "follow in full; return the records as your final message."]
        with (p["dir"] / f"{wl.stem}.log.jsonl").open("a", encoding="utf-8") as log:
            subprocess.run(cmd, stdout=log, stderr=subprocess.STDOUT, cwd=REPO, input=stdin, text=True)
        text = last.read_text(encoding="utf-8") if last.exists() else ""
        rows = [ln for ln in text.splitlines() if ln.strip().startswith("{")]
        out.write_text("\n".join(rows) + "\n", encoding="utf-8")
        print(f"{wl.name}: {len(rows)} records")
    problems = check(ref, net_name)
    if problems:
        print("\n".join(problems[:30]))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=("build", "run", "check"))
    ap.add_argument("ref")
    ap.add_argument("--net", default="network.k3-inter.json")
    a = ap.parse_args()
    {"build": build, "run": run, "check": check}[a.step](a.ref, a.net)


if __name__ == "__main__":
    main()
