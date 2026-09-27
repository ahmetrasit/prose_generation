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
import re
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
TOK_PER_BYTE = 1.16                    # calibrated on the v12 S1 run
EXPECTED_OUT = {"act": 80_000, "net": 50_000, "qeq": 40_000, "write": 70_000}
STAGGER = 60                           # seconds between the first call of a window and the rest
SYSTEM = ("You are a careful scholar of Quranic Arabic and of the Quran, and a fine writer. Follow the brief exactly and "
          "return only the requested output.")
R12.SYSTEM = SYSTEM
CALLED = ("started", "done", "failed")
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
    return nbytes * TOK_PER_BYTE * PRICE_IN + EXPECTED_OUT[step] * PRICE_OUT


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
        text, u = R12.opus(prompt, stdin, out_dir(ref) / f"{step}.log.jsonl")
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
    text, u = R12.opus(prompt, stdin, out / "net.log.jsonl")
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
    f = OUT / f"s{int(ref.split(':')[0]):03d}" / "network.md"
    return f if f.exists() else None


def digest(ref: str) -> Path:
    return I.V9 / "lines" / "work" / PK.sa(ref) / "digest_v2.md"


def qeq(ref: str) -> str:
    a, w, out = PK.ayah_dir(ref), PK.window_dir(ref), out_dir(ref)
    if not (out / "act.md").exists():
        return f"{ref} qeq: waiting for step 1"
    nf = network_file(ref)
    files = [PROMPTS / "qeq.md", w / "window_text.md", a / "ayah.md", out / "act.md"]
    files += [nf] if nf else []
    files += [a / "concordance.md", digest(ref), a / "reciprocal.md"]
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
    files += [a / "dictionary.md", branches_file(ref)]
    return _write_call(ref, files, out / f"{PK.sa(ref)}.reading.tr.md")


def _write_call(ref: str, files: list[Path], target: Path) -> str:
    st = get_status(ref, "write")
    if st["state"] in CALLED:
        return f"{ref} write: already called ({st['state']}; never again)"
    stdin = R12.inline(*files)
    prompt = "Follow the brief (write.md, first below) exactly. Return only the Turkish commentary."
    est = estimate(len((prompt + stdin).encode()), "write")
    if est >= MAX_COST:
        set_status(ref, "write", state="over-cost", estimate=round(est, 2))
        return f"{ref} write: NOT STARTED (estimate ${est:.2f})"
    set_status(ref, "write", state="started", estimate=round(est, 2), input_bytes=len(stdin.encode()),
               files=[f.name for f in files])
    try:
        text, u = R12.opus(prompt, stdin, out_dir(ref) / "write.log.jsonl")
        if len(text.split()) < 300:
            (out_dir(ref) / "write.raw.txt").write_text(text, encoding="utf-8")
            set_status(ref, "write", state="failed", error="no usable commentary (no retry, by rule)", **u)
            return f"{ref} write: FAILED; ${u['cost']:.2f}"
        target.write_text(text.strip() + "\n", encoding="utf-8")
        c = R12.check_text(target, out_dir(ref) / "repair.log.jsonl")
        set_status(ref, "write", state="done", check=c, **u)
        return (f"{ref} write: done ${u['cost']:.2f} (estimate ${est:.2f}); {len(text.split())} words; "
                f"verify {c['verify']}; repairs {c['repair_calls']} (${c['repair_cost']:.2f}); stripped {c['stripped']}")
    except Exception as e:  # noqa: BLE001
        set_status(ref, "write", state="failed", error=f"{type(e).__name__}: {str(e)[-500:]}")
        return f"{ref} write: FAILED {e}"


def status(refs: list[str]) -> str:
    rows = []
    for r in refs:
        cells = []
        for step in ("act", "qeq", "write"):
            d = get_status(r, step)
            cells.append(f"{step} {d['state']}" + (f" ${d.get('cost', 0):.2f}" if d.get("cost") else ""))
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
    ap.add_argument("step", choices=("packet", "act", "net", "qeq", "write", "status"))
    ap.add_argument("ref")
    ap.add_argument("--refs", help="net: the ayat whose records form the network (default: the whole surah)")
    ap.add_argument("--parallel", type=int, default=8)
    a = ap.parse_args()
    if a.step == "net":
        s = int(a.ref)
        refs = a.refs.split(",") if a.refs else R12.surah_refs(s)
        print(net(s, refs), flush=True)
        return
    refs = list(dict.fromkeys(a.ref.split(",")))
    if a.step == "status":
        print(status(refs))
        return
    if a.step == "packet":
        for r in refs:
            print(r, PK.build(r), flush=True)
        return
    run_parallel({"act": act, "qeq": qeq, "write": write}[a.step], refs, a.parallel)


if __name__ == "__main__":
    main()
