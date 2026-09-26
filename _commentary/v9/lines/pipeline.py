#!/usr/bin/env python3
"""One ayah end to end: script preparation → Luna discovery → package → synthesis arms.

  prep      input package (prepare.py), context.md (luna/worklists.py), line worklists (candidates.py),
            lexical network (network.py --k 3 --inter), network meaning-pass bundles (luna_pass.py build)
  discover  Luna, max reasoning: the network meaning pass and the four discovery lines, in parallel
  package   network with Luna edges + backbone (when the ayah has in-ayah pairs), then package.py
  write     synthesis arms (default: w10-opus-cold, w10-opus, sol56), in parallel
  all       prep → discover → package (write is separate: commit and push before Sol runs)

Every step skips work already on disk unless --force; model steps never restart a finished bundle.
Usage: python3 _commentary/v9/lines/pipeline.py all 103:2
       python3 _commentary/v9/lines/pipeline.py write 103:2 --arms w10-opus-cold,w10-opus,sol56
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

V9 = Path(__file__).resolve().parents[1]
REPO = V9.parents[1]
PY = sys.executable


def sh(*args: str, log: Path | None = None) -> str:
    r = subprocess.run([PY, *args], capture_output=True, text=True, cwd=REPO)
    out = (r.stdout or "") + (r.stderr or "")
    if log:
        log.parent.mkdir(parents=True, exist_ok=True)
        log.write_text(out, encoding="utf-8")
    tail = "\n".join(out.strip().splitlines()[-3:])
    print(f"  {Path(args[0]).name} {' '.join(args[1:])}\n    {tail}", flush=True)
    if r.returncode:
        sys.exit(f"failed: {args}")
    return out


def names(ref: str) -> tuple[str, Path, Path]:
    s, a = ref.split(":")
    sa = f"{s}_{a}"
    return sa, V9 / "input" / "v2" / f"s{int(s):03d}" / sa, V9 / "lines" / "work" / sa


def prep(ref: str, force: bool) -> None:
    sa, pkg, w = names(ref)
    if force or not (pkg / "00_ayah.md").exists():
        sh(str(V9 / "prepare.py"), "--ayah", ref, "--out", str(pkg))
    if force or not (V9 / "luna" / "work" / sa / "context.md").exists():
        sh(str(V9 / "luna" / "worklists.py"), str(pkg), str(V9 / "luna" / "work" / sa))
    if force or not (w / "items.tsv").exists():
        sh(str(V9 / "lines" / "candidates.py"), ref)
    net = V9 / "network" / "out" / sa
    if force or not (net / "network.k3-inter.json").exists():
        sh(str(V9 / "network" / "network.py"), ref, "--k", "3", "--inter")
    if force or not (net / "luna" / "map.json").exists():
        sh(str(V9 / "network" / "luna_pass.py"), "build", ref)


def discover(ref: str) -> None:
    sa, _, w = names(ref)
    net = V9 / "network" / "out" / sa / "luna"
    jobs = [(str(V9 / "lines" / "run.py"), "run", ref, "--parallel", "4")]
    if any(net.glob("W_network_*.md")):
        jobs.append((str(V9 / "network" / "luna_pass.py"), "run", ref))
    with ThreadPoolExecutor(len(jobs)) as pool:
        list(pool.map(lambda j: sh(*j, log=w / f"{Path(j[0]).stem}.stdout.txt"), jobs))
    sh(str(V9 / "lines" / "run.py"), "check", ref)


def package(ref: str) -> None:
    sa, _, _ = names(ref)
    net = V9 / "network" / "out" / sa
    if any((net / "luna").glob("records_*.jsonl")):
        sh(str(V9 / "network" / "network.py"), ref, "--k", "3", "--inter", "--luna", str(net / "luna"))
        sh(str(V9 / "network" / "backbone.py"), ref)
    else:  # no in-ayah word pairs (e.g. a one-word ayah): the backbone comes from the script network alone
        sh(str(V9 / "network" / "backbone.py"), ref, "--net", "network.k3-inter.json")
    sh(str(V9 / "lines" / "package.py"), ref)


def write(ref: str, arms: list[str]) -> None:
    sa, _, w = names(ref)
    with ThreadPoolExecutor(len(arms)) as pool:
        list(pool.map(lambda arm: sh(str(V9 / "lines" / "synth.py"), ref, "--arm", arm,
                                     log=w / "synth" / arm / "stdout.txt"), arms))
    sh(str(V9 / "lines" / "usage.py"), ref)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=("prep", "discover", "package", "write", "all"))
    ap.add_argument("ref")
    ap.add_argument("--arms", default="w10-opus-cold,w10-opus,sol56")
    ap.add_argument("--force", action="store_true", help="redo script preparation already on disk")
    a = ap.parse_args()
    print(f"== {a.ref} {a.step}", flush=True)
    if a.step in ("prep", "all"):
        prep(a.ref, a.force)
    if a.step in ("discover", "all"):
        discover(a.ref)
    if a.step in ("package", "all"):
        package(a.ref)
    if a.step == "write":
        write(a.ref, [x for x in a.arms.split(",") if x])


if __name__ == "__main__":
    main()
