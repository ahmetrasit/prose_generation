#!/usr/bin/env python3
"""Run a v16 per-ayah step on a queue of ayat, N at a time (user, 2026-10-04: always 7), one log per call, nothing silent.

  python3 -B _commentary/v16/batch.py --surah 87 --parallel 7                 # augment9: dry, estimates and BLOCKED, no call
  python3 -B _commentary/v16/batch.py --surah 87 --parallel 7 --go            # every ayah of S87 without an augment9
  python3 -B _commentary/v16/batch.py --surah 88 --step writer --parallel 7   # readings: dry
  python3 -B _commentary/v16/batch.py 1:1 1:2 1:3 --step writer --go          # named ayat

Steps: `augment` (default; `augment.py <reading dir> --brief augment9 --model opus`) and `writer` (`packets.py writer
--ayah S:A --brief r13 --tool --map … --images …`). The surah's map and image prose are found under out/sNNN/
(exactly one `images.r13.*/images.md`, whose dir name says which `surah.map3.*/map.md` it was built from; else the run refuses), and the reading dir is
`out/S_A/DM.r13.<images dir>.tool`, so surahs mapped with --no-channels --hft-bundle work the same way.
The queue is the ayat given, or every ayah of --surah that the step still lacks: for `writer` every ayah without a
finished reading, for `augment` every ayah with a finished reading and no `augment.<brief>.<model>` dir. A blocked
dir (started before) is skipped with a NOTE; the user decides about it. Each call has its own log in
work/logs/<S_A>.<step>.log. A call whose log shows a session limit or an API error stops the queue: the calls already
running finish, no new one starts, and the user decides (their dirs are blocked; never rerun without a rename). At
the end every WARNING, NOTE and BLOCKED line of every log is printed again, with each call's final line and its
actual cost against the estimate, a summary JSON is written, and the exit code is 1 if any call failed or did not
start. Replaces the xargs pattern in RUNBOOK.md, which xargs refused ("command line cannot be assembled, too long").
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
LOGS = HERE / "work" / "logs"
STOP = re.compile(r"session limit|api_error_status|status error|Traceback", re.I)
REPORT = re.compile(r"WARNING|NOTE|BLOCKED|never rerun|Traceback|Error|truncated|suspect|partial|safety", re.I)
EST = re.compile(r"est \$([0-9.]+)")
ACTUAL = re.compile(r": (ok|truncated|suspect|partial|safety-stop|error|accepted) \$([0-9.]+|None) ")
READING_BRIEF = "r13"
RENAMED = re.compile(r"-[0-9.]+usd$")


def surah_inputs(s: int) -> tuple[Path, Path, str]:
    """The surah's map, its image prose, and the reading dir name the writer derives from them."""
    sd = HERE / "out" / f"s{s:03d}"
    imgs = [p for p in sorted(sd.glob(f"images.{READING_BRIEF}.*/images.md"))
            if not RENAMED.search(p.parent.name)]  # a failed run renamed <dir>.<reason>-<cost>usd is not an input
    if len(imgs) != 1:
        raise SystemExit(f"S{s}: expected one image prose under {sd.relative_to(ROOT)}, found "
                         f"{[p.parent.name for p in imgs]}; the user decides")
    im = imgs[0]
    # the image prose dir is images.<brief>.<map dir without "surah.">[.tool]: its map is the one it was built from
    # (S1 has three trial maps beside the production one, 2026-10-04)
    map_tag = im.parent.name.removeprefix(f"images.{READING_BRIEF}.").removesuffix(".tool")
    mp = sd / f"surah.{map_tag}" / "map.md"
    if not mp.exists():
        raise SystemExit(f"S{s}: {im.parent.name} names a map {mp.parent.name} that does not exist; the user decides")
    return mp, im, f"DM.{READING_BRIEF}.{im.parent.name}.tool"


def blocked(d: Path) -> bool:
    return (d / "started.json").exists() or (d / "run.log.json").exists()


def surah_queue(s: int, step: str, brief: str, model: str) -> list[str]:
    sys.path.insert(0, str(HERE))
    import missing as M
    _, _, run_dir = surah_inputs(s)
    refs = []
    for a in range(1, 300):
        ref = f"{s}:{a}"
        if ref not in M.verses():
            break
        d = HERE / "out" / f"{s}_{a}" / run_dir
        reading = d / f"{s}_{a}.reading.tr.md"
        if step == "writer":
            if reading.exists():
                print(f"NOTE: {ref}: reading exists, skipped")
                continue
            if blocked(d):
                print(f"NOTE: {ref}: {run_dir} started before (BLOCKED, the user decides), skipped")
                continue
        else:
            if not reading.exists():
                print(f"NOTE: {ref}: no finished reading, skipped")
                continue
            ad = d / f"augment.{brief}.{model}"
            if (ad / reading.name).exists():
                print(f"NOTE: {ref}: {ad.name} done, skipped")
                continue
            if ad.exists():
                print(f"NOTE: {ref}: {ad.name} started before" + (" (BLOCKED, the user decides)" if blocked(ad) else "") + ", skipped")
                continue
        refs.append(ref)
    return refs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("refs", nargs="*")
    ap.add_argument("--surah", type=int, action="append", default=[])
    ap.add_argument("--step", choices=("augment", "writer"), default="augment")
    ap.add_argument("--parallel", type=int, default=7)
    ap.add_argument("--brief", default="augment9", help="augment only")
    ap.add_argument("--model", default="opus", help="augment only")
    ap.add_argument("--go", action="store_true")
    a = ap.parse_args()
    refs = list(a.refs)
    for s in a.surah:
        refs += surah_queue(s, a.step, a.brief, a.model)
    if not refs:
        raise SystemExit("nothing to run")
    LOGS.mkdir(parents=True, exist_ok=True)
    label = f"{a.brief}.{a.model}" if a.step == "augment" else f"writer.{READING_BRIEF}"
    inputs: dict[int, tuple[Path, Path, str]] = {}

    def cmd(ref: str) -> list[str]:
        s = int(ref.split(":")[0])
        if s not in inputs:
            inputs[s] = surah_inputs(s)
        mp, im, run_dir = inputs[s]
        if a.step == "writer":
            return [sys.executable, "-B", str(HERE / "packets.py"), "writer", "--ayah", ref, "--brief", READING_BRIEF,
                    "--tool", "--map", str(mp.relative_to(HERE)), "--images", str(im.relative_to(HERE))]
        return [sys.executable, "-B", str(HERE / "augment.py"), f"out/{ref.replace(':', '_')}/{run_dir}",
                "--brief", a.brief, "--model", a.model]

    if not a.go:  # dry: estimates, in the foreground
        for ref in refs:
            subprocess.run(cmd(ref), cwd=ROOT)
        print(f"{len(refs)} {a.step} call(s) queued: {', '.join(refs)}; add --go to run them {a.parallel} at a time")
        return
    queue, running, done, stopped = list(refs), {}, [], False
    while (queue and not stopped) or running:  # a stopped queue with calls still queued must not spin forever
        while queue and len(running) < a.parallel and not stopped:
            ref = queue.pop(0)
            log = LOGS / f"{ref.replace(':', '_')}.{label}.log"
            f = log.open("w", encoding="utf-8")
            running[ref] = (subprocess.Popen(cmd(ref) + ["--go"], cwd=ROOT, stdout=f, stderr=subprocess.STDOUT), f, log)
            print(f"{time.strftime('%H:%M:%S')} started {ref} -> {log.relative_to(ROOT)}", flush=True)
        time.sleep(5)
        for ref, (p, f, log) in list(running.items()):
            if p.poll() is None:
                continue
            f.close()
            del running[ref]
            text = log.read_text(encoding="utf-8")
            last = text.strip().splitlines()[-1] if text.strip() else "(empty log)"
            done.append((ref, p.returncode, log, last))
            print(f"{time.strftime('%H:%M:%S')} finished {ref} (exit {p.returncode}): {last[:160]}", flush=True)
            if p.returncode != 0 and STOP.search(text) and queue:
                stopped = True
                print(f"WARNING: {ref} failed with a session limit or an API error: the queue stops; "
                      f"not started: {', '.join(queue)}", flush=True)
    print("\n=== every WARNING / NOTE / BLOCKED line, per call ===")
    failed, rows = 0, []
    for ref, rc, log, last in done:
        failed += rc != 0
        text = log.read_text(encoding="utf-8")
        est = EST.search(text)
        act = ACTUAL.search(last)
        rows.append({"ref": ref, "exit": rc, "status": act.group(1) if act else "unknown",
                     "estimate_usd": float(est.group(1)) if est else None,
                     "cost_usd": float(act.group(2)) if act and act.group(2) != "None" else None, "log": str(log.relative_to(ROOT))})
        print(f"--- {ref} (exit {rc}) {log.relative_to(ROOT)}")
        for line in text.splitlines():
            if REPORT.search(line):
                print("   " + line[:220])
        print("   final: " + last[:220])
    if stopped:
        print(f"WARNING: queue stopped early; not started: {', '.join(queue)}")
    # actual costs against the estimates (user, 2026-10-04: always record actual costs)
    print("\n=== cost: actual against estimate ===")
    for r in rows:
        e, c = r["estimate_usd"], r["cost_usd"]
        ratio = f" ({c / e:.2f}x)" if e and c else ""
        print(f"   {r['ref']:7s} {r['status']:10s} est ${e if e is not None else '?'}  actual ${c if c is not None else '?'}{ratio}")
    tot_e = sum(r["estimate_usd"] or 0 for r in rows); tot_c = sum(r["cost_usd"] or 0 for r in rows)
    print(f"   total: est ${tot_e:.2f}  actual ${tot_c:.2f}" + (f" ({tot_c / tot_e:.2f}x)" if tot_e else ""))
    summary = LOGS / f"batch.{label}.{time.strftime('%Y%m%d-%H%M%S')}.json"
    summary.write_text(json.dumps({"step": a.step, "refs": refs, "parallel": a.parallel, "stopped": stopped, "not_started": queue,
                                   "calls": rows, "estimate_usd": round(tot_e, 2), "actual_usd": round(tot_c, 2)},
                                  ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"   summary: {summary.relative_to(ROOT)}")
    print(f"\n{len(done)} call(s) finished, {failed} failed, {len(queue)} not started")
    if failed or queue:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
