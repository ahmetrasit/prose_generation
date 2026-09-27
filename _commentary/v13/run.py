#!/usr/bin/env python3
"""v13 test runner: the funnel of DESIGN.md §3 (packet → activations → network → QeQ → Turkish prose).

  packet  S:A,…          step 0 (scripts): packet.py
  act     S:A,…          step 1, one Opus call per ayah: prompts/act.md → out/sNNN/S_A/act.md (records)
  net     S [--refs …]   step N, one Opus call per surah (or the given ayat): prompts/net.md → out/sNNN/network.md
  qeq     S:A,…          step 2, one Opus call per ayah: prompts/qeq.md → out/sNNN/S_A/qeq.md
  write   S:A,…          step 3, one Opus call per ayah: prompts/write.md → out/sNNN/S_A/S_A.reading.tr.md, then the
                         v12 tag checks (verify, at most one repair call, strip what stays unverifiable)
  status  S:A,…

All model steps: Opus 5.5, effort high, no tools (v12 run.opus). Rules (user): a call starts only when its estimate is
below $5; it is never stopped or retried; a step that had a call for an ayah is never called again (no --force; only the
user clears an output). Parallel calls of one window start after the first has begun (shared prefix cached).
Records are checked by script and flagged, never dropped.

Usage: python3 _commentary/v13/run.py act 1:1,1:2,1:3,1:4,1:5,1:6,1:7,18:96 --parallel 8
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

V13 = Path(__file__).resolve().parent
sys.path.insert(0, str(V13))
sys.path.insert(0, str(V13.parent / "v12"))
import packet as PK  # noqa: E402
import importlib.util  # noqa: E402

_spec = importlib.util.spec_from_file_location("v12run", V13.parent / "v12" / "run.py")
R12 = importlib.util.module_from_spec(_spec)  # v12: opus, inline, check_text, quran (loaded by path: v13 has its own run.py)
_spec.loader.exec_module(R12)
I = PK.I

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
    parts[-1] = parts[-1].split(CONT)[0].rstrip()
    u = usage_detail(log)
    u.update(parts=n, **{"in": u.get("cache_write", 0) + u.get("cache_read", 0) + u.get("input", 0),
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
        tot["cost"] = round(tot["cost"] + (d.get("total_cost_usd") or 0), 3)
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


def plan_role(seg: str, ref: str) -> str:
    """The role (meet/touch/develop/assemble) a disclosure-plan segment gives this ayah; refs and ranges in any order."""
    m = re.search(r"\b(meet|touch|develop|assemble)\b", seg)
    if not m:
        return ""
    s, a = (int(x) for x in ref.split(":"))
    for lo, hi in re.findall(r"(\d{1,3}:\d{1,3})(?:\s*[–-]\s*(\d{1,3}:\d{1,3}))?", seg):
        l = tuple(int(x) for x in lo.split(":"))
        h = tuple(int(x) for x in (hi or lo).split(":"))
        if l[0] == s and l[1] <= a <= h[1]:
            return m.group(1)
    return ""


def mustland(ref: str) -> Path:
    """What the prose must carry (script, from the network and the QeQ tags): M-items for the coverage block."""
    out = out_dir(ref)
    lines = [f"# mustland.md — what the commentary of {ref} must carry", ""]
    n = 0
    nf = network_file(ref)
    if nf:
        for l in nf.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^(I\d+) \| ([^|]+)\|", l)
            if not m:
                continue
            disc = next((p for p in l.split(" | ") if p.startswith("disclosure:")), "")
            roles = [role for seg in re.split(r"[;,]", disc[len("disclosure:"):]) if (role := plan_role(seg, ref))]
            member_here = re.search(rf"(?<![\d:]){re.escape(ref)}:\d+", l.split(" | meets:")[0])
            if not roles and not member_here:
                continue
            role = roles[0] if roles else "touch (member here; not in the plan)"
            n += 1
            lines.append(f"- M{n} | image {m.group(1)} {m.group(2).strip()} | role here: {role}"
                         + (" | show the whole image with every member (see the network line)" if role == "assemble" else ""))
            meets = next((p for p in l.split(" | ") if p.startswith("meets:")), "")
            for seg in meets[len("meets:"):].split(";"):
                if re.search(rf"(?<![\d:]){re.escape(ref)}:\d+", seg):
                    n += 1
                    lines.append(f"- M{n} | meeting {m.group(1)} × {seg.strip()}")
    q = out / "qeq.md"
    if q.exists():
        seen = set()
        for r_, tag in re.findall(r"(\d{1,3}:\d{1,3})\s*\[(staging|same-word)\]", q.read_text(encoding="utf-8")):
            if (r_, tag) in seen:
                continue
            seen.add((r_, tag))
            n += 1
            lines.append(f"- M{n} | passage {r_} [{tag}]")
    f = out / "mustland.md"
    f.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return f


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
    a, out = PK.ayah_dir(ref), out_dir(ref)
    if not (out / "qeq.md").exists():
        return f"{ref} write: waiting for step 2"
    nf = network_file(ref)
    files = [PROMPTS / "write.md", a / "ayah.md", out / "act.md", out / "qeq.md"] + ([nf] if nf else [])
    files += [mustland(ref), a / "dictionary.md", branches_file(ref)]
    return _write_call(ref, files, out / f"{PK.sa(ref)}.reading.tr.md")


def _write_call(ref: str, files: list[Path], target: Path) -> str:
    st = get_status(ref, "write")
    if st["state"] in CALLED:
        return f"{ref} write: already called ({st['state']}; never again)"
    stdin = R12.inline(*files)
    prompt = "Follow the brief (write.md, first below) exactly. Return the Turkish commentary, then the coverage block."
    est = estimate(len((prompt + stdin).encode()), "write")
    if est >= MAX_COST:
        set_status(ref, "write", state="over-cost", estimate=round(est, 2))
        return f"{ref} write: NOT STARTED (estimate ${est:.2f})"
    set_status(ref, "write", state="started", estimate=round(est, 2), input_bytes=len(stdin.encode()),
               files=[f.name for f in files])
    try:
        text, u = opus(prompt, stdin, out_dir(ref) / "write.log.jsonl")
        if len(text.split()) < 300:
            (out_dir(ref) / "write.raw.txt").write_text(text, encoding="utf-8")
            set_status(ref, "write", state="failed", error="no usable commentary (no retry, by rule)", **u)
            return f"{ref} write: FAILED; ${u['cost']:.2f}"
        body, _, cov = text.partition("===== COVERAGE =====")
        target.write_text(body.strip() + "\n", encoding="utf-8")
        cov_lines = [l.strip() for l in cov.splitlines() if re.match(r"^\s*M\d+ \|", l)]
        (out_dir(ref) / "coverage.md").write_text("\n".join(cov_lines) + "\n", encoding="utf-8")
        items = [l for l in (out_dir(ref) / "mustland.md").read_text(encoding="utf-8").splitlines() if l.startswith("- M")] \
            if (out_dir(ref) / "mustland.md").exists() else []
        got = {re.match(r"M\d+", l).group(0) for l in cov_lines if "landed" in l}
        held = [l for l in items if re.search(r"M\d+", l).group(0) not in got]
        (out_dir(ref) / "handforward.md").write_text(
            f"# handforward.md — mustland items of {ref} not landed (for the surah commentary)\n\n" + "\n".join(held) + "\n",
            encoding="utf-8")
        c = R12.check_text(target, out_dir(ref) / "repair.log.jsonl")
        c.update(mustland=len(items), landed=len(got), not_landed=len(held))
        set_status(ref, "write", state="done", check=c, **u)
        return (f"{ref} write: done ${u['cost']:.2f} (estimate ${est:.2f}); {len(text.split())} words; "
                f"verify {c['verify']}; repairs {c['repair_calls']} (${c['repair_cost']:.2f}); stripped {c['stripped']}; "
                f"mustland {c['landed']}/{c['mustland']} landed")
    except Exception as e:  # noqa: BLE001
        set_status(ref, "write", state="failed", error=f"{type(e).__name__}: {str(e)[-500:]}")
        return f"{ref} write: FAILED {e}"


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
    ap.add_argument("step", choices=("packet", "seed", "act", "net", "qeq", "write", "status"))
    ap.add_argument("ref")
    ap.add_argument("--refs", help="net: the ayat whose records form the network (default: the whole surah)")
    ap.add_argument("--parallel", type=int, default=8)
    ap.add_argument("--effort", default="high", choices=("high", "xhigh", "max"))
    ap.add_argument("--tag", help="outputs in out-TAG/ (an arm, e.g. --tag max --effort max)")
    ap.add_argument("--max-cost", type=float, default=5.0)
    ap.add_argument("--seed-from", default="", help="seed: the arm whose step-1 records are reused ('' = out/)")
    ap.add_argument("--network-from", help="read the surah network of arm TAG (out-TAG/)")
    a = ap.parse_args()
    global EFFORT, OUT, MAX_COST, NETWORK_FROM
    EFFORT, MAX_COST = a.effort, a.max_cost
    if a.tag:
        OUT = V13 / f"out-{a.tag}"
    if a.network_from:
        NETWORK_FROM = V13 / f"out-{a.network_from}"
    if a.step == "net":
        s = int(a.ref)
        refs = a.refs.split(",") if a.refs else R12.surah_refs(s)
        print(net(s, refs), flush=True)
        return
    refs = list(dict.fromkeys(a.ref.split(",")))
    if a.step == "status":
        print(status(refs))
        return
    if a.step == "seed":
        src = V13 / (f"out-{a.seed_from}" if a.seed_from else "out")
        for r in refs:
            print(seed(r, src), flush=True)
        return
    if a.step == "packet":
        for r in refs:
            print(r, PK.build(r), flush=True)
        return
    run_parallel({"act": act, "qeq": qeq, "write": write}[a.step], refs, a.parallel)


if __name__ == "__main__":
    main()
