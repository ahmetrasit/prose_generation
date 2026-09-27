#!/usr/bin/env python3
"""v14 runner. Copied v13 arms are immutable; new writer experiments freeze their upstream inputs.

Offline:
  prepare 1:6,1:7 --tag NAME --seed-from v2
  preview 1:6 --tag NAME                 build the exact writer input, report bytes/estimate
  external-start 1:6 --tag NAME --model gpt-6-sol --effort max
  ingest 1:6 --tag NAME --response /path/to/final.txt
  audit                                 verify v13 and the copied baseline data

Model calls (explicit --execute required; building/preparing does not authorize a call):
  write 1:6,1:7 --tag NAME --execute      Opus high, in ayah order, frozen upstream
  act/net/qeq retain the v13 implementation for fresh, unprepared arms only.

Every candidate needs source verification and independent semantic review before acceptance.
No score, writer coverage claim or successful generation promotes it automatically.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

V13 = Path(__file__).resolve().parent  # inherited name; resolves to v14, never the v13 baseline
sys.path.insert(0, str(V13))
sys.path.insert(0, str(V13.parent / "v12"))
import packet as PK  # noqa: E402
import importlib.util  # noqa: E402

_spec = importlib.util.spec_from_file_location("v12run", V13.parent / "v12" / "run.py")
R12 = importlib.util.module_from_spec(_spec)  # v12: opus, inline, check_text, quran (loaded by path: v13 has its own run.py)
_spec.loader.exec_module(R12)
I = PK.I
sys.path.insert(0, str(V13))
import experiment as EX  # noqa: E402
import synthesis as SYN  # noqa: E402

OUT = V13 / "out"
PROMPTS = V13 / "prompts"
MAX_COST = 5.0
PRICE_IN, PRICE_OUT = 8e-6, 20e-6      # claude -p: input as a one-hour cache write; output
TOK_PER_BYTE = 0.45                    # measured on v13 step 1 (1:1 60,035 tokens for 136,352 bytes; 1:2, 1:3, 1:5 alike)
EXPECTED_OUT = {"act": 80_000, "net": 50_000, "qeq": 40_000, "write": 70_000}   # at effort high
EFFORT_FACTOR = {"high": 1.0, "xhigh": 1.3, "max": 1.6}                         # guesses until measured
EFFORT = "high"
STAGGER = 60                           # seconds between the first call of a window and the rest
CONT = "===== CONTINUE ====="
MAX_PARTS = 6
SYSTEM = ("You are a careful scholar of Quranic Arabic and of the Quran, and a fine writer. Follow the brief exactly and "
          "return only the requested output. A single response of yours may hold at most about 60,000 tokens, your "
          "reasoning included. If what you have to write would go beyond that, write it in parts: end a part at a natural "
          f"boundary with the line {CONT} and nothing after it; you will then be asked to continue, and you continue "
          "exactly where you stopped, without repeating or summarising what you already wrote.")
R12.SYSTEM = SYSTEM
MODEL = "opus"


def _claude(args: list[str], stdin: str, log: Path) -> tuple[str, str]:
    """One claude -p response (no tools); returns (its text, its session id); the stream goes to the log."""
    r = subprocess.run(["claude", "-p", "--model", MODEL, "--effort", EFFORT, "--tools", "", "--strict-mcp-config",
                        "--output-format", "stream-json", "--verbose", "--system-prompt", SYSTEM, *args],
                       input=stdin, capture_output=True, text=True, cwd=R12.REPO,
                       env={**os.environ, "CLAUDE_CODE_MAX_OUTPUT_TOKENS": "128000"})
    with log.open("a", encoding="utf-8") as fh:
        fh.write(r.stdout or json.dumps({"error": r.stderr[-3000:]}) + "\n")
    text, sid = [], ""
    for line in (r.stdout or "").splitlines():
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        sid = d.get("session_id") or sid
        if d.get("type") == "assistant":
            text += [b.get("text", "") for b in d["message"].get("content", []) if b.get("type") == "text"]
    return "\n".join(text), sid


def opus(prompt: str, stdin: str, log: Path) -> tuple[str, dict]:
    """One logical call, written in parts when the model ends a part with CONT (the session is resumed; not a retry)."""
    text, sid = _claude([], prompt + "\n\n" + stdin, log)
    parts, n = [text], 1
    while CONT in parts[-1] and sid and n < MAX_PARTS:
        parts[-1] = parts[-1].split(CONT)[0].rstrip()
        more, sid2 = _claude(["--resume", sid], "Continue exactly where you stopped.", log)
        sid = sid2 or sid
        parts.append(more)
        n += 1
    complete = CONT not in parts[-1]
    parts[-1] = parts[-1].split(CONT)[0].rstrip()
    u = usage_detail(log)
    u.update(parts=n, complete=complete, **{"in": u.get("cache_write", 0) + u.get("cache_read", 0) + u.get("input", 0),
                         "out": u.get("output", 0)})
    return "\n".join(parts), u
CALLED = ("started", "done", "failed", "reused")
NETWORK_FROM: Path | None = None       # --network-from TAG: read the surah network of another arm (e.g. an effort arm)
BRANCH_RE = re.compile(r"([ء-ي](?: [ء-ي]){1,4}) (B\d{3})")


def out_dir(ref: str) -> Path:
    return OUT / f"s{int(ref.split(':')[0]):03d}" / PK.sa(ref)


def status_file(ref: str, step: str) -> Path:
    return out_dir(ref) / f"{step}.status.json"


def get_status(ref: str, step: str) -> dict:
    f = status_file(ref, step)
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {"state": "new"}


def set_status(ref: str, step: str, **kw) -> dict:
    f = status_file(ref, step)
    f.parent.mkdir(parents=True, exist_ok=True)
    d = get_status(ref, step)
    d.update(kw, updated=time.strftime("%Y-%m-%d %H:%M:%S"))
    f.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return d


def estimate(nbytes: int, step: str) -> float:
    return nbytes * TOK_PER_BYTE * PRICE_IN + EXPECTED_OUT[step] * EFFORT_FACTOR[EFFORT] * PRICE_OUT


def usage_detail(log: Path) -> dict:
    """Token use of the last call in a claude -p stream log: cache writes, cache reads, output, thinking, time."""
    tot = {"effort": EFFORT, "cost": 0.0, "minutes": 0.0, "cache_write": 0, "cache_read": 0, "input": 0, "output": 0,
           "thinking": 0, "responses": 0}
    for line in log.read_text(encoding="utf-8").splitlines() if log.exists() else []:
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        if d.get("type") != "result":
            continue
        u = d.get("usage") or {}
        tot["responses"] += 1
        # a resumed session (a call written in parts) reports its running total, so the cost is the last one
        tot["cost"] = round(max(tot["cost"], d.get("total_cost_usd") or 0), 3)
        tot["minutes"] = round(tot["minutes"] + (d.get("duration_ms") or 0) / 60000, 1)
        tot["cache_write"] += u.get("cache_creation_input_tokens", 0)
        tot["cache_read"] += u.get("cache_read_input_tokens", 0)
        tot["input"] += u.get("input_tokens", 0)
        tot["output"] += u.get("output_tokens", 0)
        tot["thinking"] += (u.get("output_tokens_details") or {}).get("thinking_tokens", 0)
    return tot if tot["responses"] else {}


def call(ref: str, step: str, files: list[Path], marker: str, target: Path) -> str:
    """One gated Opus call; never twice. The brief comes first, then the shared window part, then the ayah's files."""
    st = get_status(ref, step)
    if st["state"] in CALLED:
        return f"{ref} {step}: already called ({st['state']}; never again)"
    files = [f for f in files if f.exists()]
    stdin = R12.inline(*files)
    prompt = (f"Follow the brief ({files[0].name}, first below) exactly. The evidence follows it. Return your final message "
              f"in the brief's format, beginning with the line {marker}.")
    est = estimate(len((prompt + stdin).encode()), step)
    if est >= MAX_COST:
        set_status(ref, step, state="over-cost", estimate=round(est, 2), input_bytes=len(stdin.encode()))
        return f"{ref} {step}: NOT STARTED (estimate ${est:.2f} ≥ ${MAX_COST:.2f})"
    set_status(ref, step, state="started", estimate=round(est, 2), input_bytes=len(stdin.encode()),
               files=[f.name for f in files])
    try:
        text, u = opus(prompt, stdin, out_dir(ref) / f"{step}.log.jsonl")
        body = text.split(marker, 1)[1].strip() if marker in text else ""
        if not body:
            (out_dir(ref) / f"{step}.raw.txt").write_text(text, encoding="utf-8")
            set_status(ref, step, state="failed", error="no marker line in the answer (no retry, by rule)", **u)
            return f"{ref} {step}: FAILED (no {marker}); ${u['cost']:.2f}"
        target.write_text(body + "\n", encoding="utf-8")
        set_status(ref, step, state="done", **u)
        return f"{ref} {step}: done ${u['cost']:.2f} (estimate ${est:.2f}; in {u['in']:,} out {u['out']:,})"
    except Exception as e:  # noqa: BLE001 — recorded; never retried
        set_status(ref, step, state="failed", error=f"{type(e).__name__}: {str(e)[-500:]}")
        return f"{ref} {step}: FAILED {e}"


# ---------------------------------------------------------------- record checks (flag, never drop)
def branch_exists(root: str, bid: str) -> bool:
    for rid, name in I.src().root_name.items():
        if name == root:
            e = I.src().entry(rid) or {}
            if any(b["branch_ref"].endswith("/" + bid) for b in e.get("branches", [])):
                return True
    return False


def check_records(path: Path, kind_re: str) -> dict:
    lines = [l for l in path.read_text(encoding="utf-8").splitlines() if re.match(kind_re, l)]
    bad_branch, kinds = [], {}
    for l in lines:
        parts = [p.strip() for p in l.split("|")]
        if len(parts) > 1:
            kinds[parts[1]] = kinds.get(parts[1], 0) + 1
        field = next((p for p in parts if p.startswith("branches:")), "")
        for root, bid in BRANCH_RE.findall(field):
            if not branch_exists(root, bid):
                bad_branch.append(f"{parts[0]} {root} {bid}")
    res = {"records": len(lines), "kinds": kinds, "unknown_branches": bad_branch}
    path.with_suffix(".check.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return res


# ---------------------------------------------------------------- steps
def act(ref: str) -> str:
    if not (PK.ayah_dir(ref) / "ayah.md").exists():
        PK.build(ref)
    a, w = PK.ayah_dir(ref), PK.window_dir(ref)
    out = out_dir(ref)
    out.mkdir(parents=True, exist_ok=True)
    msg = call(ref, "act", [PROMPTS / "act.md", w / "window.md", a / "ayah.md", a / "dictionary.md", a / "pairs.md",
                            a / "concordance.md", a / "hft.md"], "===== RECORDS =====", out / "act.md")
    if (out / "act.md").exists():
        c = check_records(out / "act.md", r"^F\d+ \|")
        msg += f"; records {c['records']} {c['kinds']}; unknown branches {len(c['unknown_branches'])}"
    return msg


def net(surah: int, refs: list[str]) -> str:
    key = f"{surah}:net"
    out = OUT / f"s{surah:03d}"
    missing = [r for r in refs if not (out_dir(r) / "act.md").exists()]
    if missing:
        return f"surah {surah} net: waiting for step 1 of {', '.join(missing)}"
    w = PK.window_dir(refs[0])
    rec = out / "net.input.records.md"
    rec.write_text("# records — every ayah's step-1 findings\n\n" + "\n\n".join(
        f"## {r}\n" + "\n".join(f"{r} {l}" for l in (out_dir(r) / "act.md").read_text(encoding="utf-8").splitlines()
                                 if re.match(r"^F\d+ \|", l)) for r in refs) + "\n", encoding="utf-8")
    st = get_net_status(surah)
    if st["state"] in CALLED:
        return f"surah {surah} net: already called ({st['state']}; never again)"
    files = [PROMPTS / "net.md", w / "window.md", rec]
    stdin = R12.inline(*files)
    prompt = "Follow the brief (net.md, first below) exactly. Return your final message beginning with the line ===== NETWORK =====."
    est = estimate(len((prompt + stdin).encode()), "net")
    if est >= MAX_COST:
        return f"surah {surah} net: NOT STARTED (estimate ${est:.2f})"
    set_net_status(surah, state="started", estimate=round(est, 2), refs=refs)
    text, u = opus(prompt, stdin, out / "net.log.jsonl")
    body = text.split("===== NETWORK =====", 1)[1].strip() if "===== NETWORK =====" in text else ""
    if not body:
        (out / "net.raw.txt").write_text(text, encoding="utf-8")
        set_net_status(surah, state="failed", **u)
        return f"surah {surah} net: FAILED (no marker); ${u['cost']:.2f}"
    (out / "network.md").write_text(body + "\n", encoding="utf-8")
    set_net_status(surah, state="done", **u)
    n = len(re.findall(r"(?m)^I\d+ \|", body))
    return f"surah {surah} net: done ${u['cost']:.2f} (estimate ${est:.2f}); images {n}"


def get_net_status(surah: int) -> dict:
    f = OUT / f"s{surah:03d}" / "net.status.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {"state": "new"}


def set_net_status(surah: int, **kw) -> None:
    f = OUT / f"s{surah:03d}" / "net.status.json"
    f.parent.mkdir(parents=True, exist_ok=True)
    d = get_net_status(surah)
    d.update(kw, updated=time.strftime("%Y-%m-%d %H:%M:%S"))
    f.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def network_file(ref: str) -> Path | None:
    f = (NETWORK_FROM or OUT) / f"s{int(ref.split(':')[0]):03d}" / "network.md"
    return f if f.exists() else None


def seed(ref: str, src: Path) -> str:
    """Reuse another arm's step-1 records (copied, never recomputed): state `reused`."""
    s = src / f"s{int(ref.split(':')[0]):03d}" / PK.sa(ref)
    if get_status(ref, "act")["state"] in CALLED:
        return f"{ref} seed: step 1 already present ({get_status(ref, 'act')['state']})"
    if not (s / "act.md").exists():
        return f"{ref} seed: no step-1 records in {src.name}"
    out = out_dir(ref)
    out.mkdir(parents=True, exist_ok=True)
    (out / "act.md").write_text((s / "act.md").read_text(encoding="utf-8"), encoding="utf-8")
    set_status(ref, "act", state="reused", source=str((s / "act.md").relative_to(V13)))
    return f"{ref} seed: step-1 records reused from {src.name}"


def digest(ref: str) -> Path:
    return I.V9 / "lines" / "work" / PK.sa(ref) / "digest_v2.md"


def qeq(ref: str) -> str:
    a, w, out = PK.ayah_dir(ref), PK.window_dir(ref), out_dir(ref)
    if not (out / "act.md").exists():
        return f"{ref} qeq: waiting for step 1"
    nf = network_file(ref)
    files = [PROMPTS / "qeq.md", w / "window_text.md", a / "ayah.md", out / "act.md"]
    files += [nf] if nf else []
    files += [a / "concordance.md", digest(ref)]  # the reciprocal list is postponed to a final check (user, 2026-09-27)
    msg = call(ref, "qeq", files, "===== QEQ =====", out / "qeq.md")
    if (out / "qeq.md").exists():
        c = check_records(out / "qeq.md", r"^[FQ]\d+ \|")
        msg += f"; lines {c['records']} {c['kinds']}"
    return msg


def branches_file(ref: str) -> Path:
    """The dictionary lines of every branch the findings cite, outside the focus roots (dictionary.md has those)."""
    out = out_dir(ref)
    text = "\n".join((out / n).read_text(encoding="utf-8") for n in ("act.md", "qeq.md") if (out / n).exists())
    nf = network_file(ref)
    if nf:
        text += nf.read_text(encoding="utf-8")
    focus = set(re.findall(r"(?m)^### ([ء-ي](?: [ء-ي]){1,4})", (PK.ayah_dir(ref) / "dictionary.md").read_text(encoding="utf-8")))
    want = sorted({(r, b) for r, b in BRANCH_RE.findall(text) if r not in focus})
    lines = ["# branches.md — the dictionary lines of the branches the findings cite (focus roots: dictionary.md)", ""]
    for root, bid in want:
        for rid, name in I.src().root_name.items():
            if name != root:
                continue
            for b in (I.src().entry(rid) or {}).get("branches", []):
                if b["branch_ref"].endswith("/" + bid):
                    g = b.get("concept_gloss")
                    g = (g.get("text") if isinstance(g, dict) else g) or ""
                    cm = b.get("concept_map") or {}
                    lines.append(f"- {root} {bid} {g} | {b.get('branch_image_ar', '')} | {cm.get('definition', '')} | "
                                 f"{I.first_phrase(b.get('source_phrase_ar', ''))}")
    f = out / "branches.md"
    f.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return f


def write(ref: str) -> str:
    """Only prepared, frozen arms use the v14 writer; preceding candidates must finish first."""
    if EFFORT != "high":
        raise ValueError("The controlled Opus writer holds effort at high; external models have separate provenance")
    if get_status(ref, "write")["state"] in (*CALLED, "review-needed"):
        return f"{ref} write: already called; never again"
    EX.export(OUT, ref)
    text = (out_dir(ref) / "write.input.md").read_text()
    est = estimate(len(text.encode()), "write")
    if est >= MAX_COST:
        return f"{ref} write: NOT STARTED (estimate ${est:.2f})"
    EX.claim(OUT, ref, "opus", EFFORT)
    try:
        final, usage = opus("Follow write.md. Return prose and the SYNTHESIS JSON account.", text,
                            out_dir(ref) / "write.log.jsonl")
        if not usage.get("complete", False):
            final += "\n" + CONT
        status = EX.ingest(OUT, ref, final, usage)
        set_status(ref, "write", estimate=round(est, 2))
        return f"{ref}: {status['state']}; account valid={status['account_valid']}; semantic review pending"
    except Exception as exc:
        set_status(ref, "write", state="failed", error=str(exc))
        raise


def status(refs: list[str]) -> str:
    rows = []
    for r in refs:
        cells = []
        for step in ("act", "qeq", "write"):
            d = get_status(r, step)
            cells.append(f"{step} {d['state']}" + (f" ${d.get('cost', 0):.2f} [{d.get('effort', '')}: write "
                                                    f"{d.get('cache_write', 0):,} read {d.get('cache_read', 0):,} out "
                                                    f"{d.get('output', 0):,} think {d.get('thinking', 0):,}; "
                                                    f"{d.get('minutes', 0)} min]" if d.get("cost") else ""))
        rows.append(f"{r}\t" + "\t".join(cells))
    return "\n".join(rows)


def run_parallel(fn, refs: list[str], parallel: int) -> None:
    """The first ayah of each window starts alone; the rest follow after STAGGER seconds (the prefix is cached)."""
    firsts, rest, seen = [], [], set()
    for r in refs:
        (rest if PK.window_dir(r) in seen else firsts).append(r)
        seen.add(PK.window_dir(r))
    with ThreadPoolExecutor(parallel) as pool:
        futs = [pool.submit(fn, r) for r in firsts]
        if rest:
            time.sleep(STAGGER)
        futs += [pool.submit(fn, r) for r in rest]
        for f in futs:
            print(f.result(), flush=True)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=("prepare", "preview", "external-start", "ingest", "audit", "packet", "seed", "act", "net", "qeq", "write", "status"))
    ap.add_argument("ref", nargs="?", default="")
    ap.add_argument("--refs")
    ap.add_argument("--parallel", type=int, default=8)
    ap.add_argument("--effort", default="high", choices=("high", "xhigh", "max"))
    ap.add_argument("--model", default="opus", help="external-start provenance only")
    ap.add_argument("--tag")
    ap.add_argument("--max-cost", type=float, default=5.0)
    ap.add_argument("--seed-from", default="v2")
    ap.add_argument("--network-from")
    ap.add_argument("--response", type=Path)
    ap.add_argument("--execute", action="store_true", help="allow the explicitly requested model step")
    a = ap.parse_args()
    global EFFORT, OUT, MAX_COST, NETWORK_FROM
    EFFORT, MAX_COST = a.effort, min(a.max_cost, 5.0)
    if a.tag:
        if not re.fullmatch(r"[a-zA-Z0-9_-]+", a.tag):
            ap.error("Invalid arm tag")
        OUT = V13 / f"out-{a.tag}"
    if a.network_from:
        NETWORK_FROM = V13 / f"out-{a.network_from}"
    if a.step == "audit":
        report = EX.baseline_check()
        print(json.dumps(report, indent=2))
        raise SystemExit(0 if report["ok"] else 1)
    if not a.ref:
        ap.error("A reference is required")
    refs = list(dict.fromkeys(a.ref.split(",")))
    if a.step == "status":
        print(status(refs))
        return
    if not a.tag or EX.archived(OUT):
        ap.error("Choose a new --tag; copied v13 arms are read-only")
    if a.step == "prepare":
        src = V13 / (f"out-{a.seed_from}" if a.seed_from else "out")
        result = EX.prepare(OUT, src, refs)
        print(f"Frozen {len(result['files'])} files for {', '.join(result['refs'])}; no model called")
        return
    if a.step == "preview":
        for ref in refs:
            result = EX.export(OUT, ref)
            print(f"{ref}: {result['input_bytes']:,} bytes; Opus high estimate ${estimate(result['input_bytes'], 'write'):.2f}; no model called")
        return
    if a.step == "external-start":
        if len(refs) != 1:
            ap.error("Claim one external writer at a time")
        print(EX.claim(OUT, refs[0], a.model, a.effort))
        return
    if a.step == "ingest":
        if len(refs) != 1 or not a.response:
            ap.error("ingest requires one ref and --response")
        print(json.dumps(EX.ingest(OUT, refs[0], a.response.read_text()), ensure_ascii=False, indent=2))
        return
    if a.step == "write":
        if not a.execute:
            ap.error("Use preview for offline preparation; an authorized model run requires --execute")
        for ref in sorted(refs, key=lambda r: tuple(map(int, r.split(":")))):
            print(write(ref), flush=True)
        return
    if (OUT / "experiment.json").exists():
        ap.error("Prepared upstream is frozen; only preview/write/external-start/ingest can change this arm")
    if a.step in ("act", "net", "qeq") and not a.execute:
        ap.error("Model calls require --execute")
    if a.step == "net":
        s = int(a.ref)
        print(net(s, a.refs.split(",") if a.refs else R12.surah_refs(s)))
        return
    if a.step == "packet":
        for ref in refs:
            if PK.ayah_dir(ref).exists():
                ap.error("Existing copied packets are immutable")
            print(ref, PK.build(ref))
        return
    if a.step == "seed":
        src = V13 / (f"out-{a.seed_from}" if a.seed_from else "out")
        for ref in refs:
            print(seed(ref, src))
        return
    run_parallel({"act": act, "qeq": qeq}[a.step], refs, a.parallel)


if __name__ == "__main__":
    main()
