#!/usr/bin/env python3
"""v16: one permitted Opus reading per ayah on the E1 base plus assembled findings (see DESIGN.md).

Base (every arm): the E1 prompt byte for byte (review/experiments/e1_permission.py: write_v10.md, context.md,
01_dictionary.md, memory permitted) plus prompts/additions.md (three writer_rules additions, Ek Notlar valve).

Arms (the assembled-findings slot):
  H  the ayah's HFT records verbatim (v9/input/v2/…/02_hft.md) and the surah channel review's subchannels anchored
     in the ayah, verbatim (latent_activation/network/v3/reviews/sNNN/reader_a_pilot.md)
  V  v5 scope prose (raw/<analysis>/sNNN/S_A/{micro,macro,global}.scope.tr.md); a lane whose gzip ratio is below
     0.2 is template-generated ledger text, not prose, and is left out
  D  no findings slot, and the v16 dictionary (dictionary.py) in place of v9's clipped 01_dictionary.md
  VD V with the v16 dictionary
  DM D plus the surah map (out/sNNN/surah/map.md), written once per surah by the surah call

Surah call (`surah`): one Opus call reads the whole surah (text, v16 surah dictionary, the trimmed HFT of every
ayah, the whole channel review) with prompts/surah_map.md and writes the map of its image chains.

Rules: one call per arm per ayah; never rerun an existing output; no retries; a call starts only if its estimate is
below $5; every call is logged in out/ledger.jsonl; check.py runs after writing and never edits the prose.

Usage:
  python3 _commentary/v16/v16.py build            write every packet to work/ and print sizes and estimates
  python3 _commentary/v16/v16.py run --arm H|V|D|VD|DM [--ayah S:A] [--parallel N]
  python3 _commentary/v16/v16.py surah --surah 1 [--run]   build (and with --run, make) the surah call
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
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
C = REPO / "_commentary"
V9 = C / "v9"
V5 = C / "v5"
CHANNELS = REPO.parent / "latent_activation" / "network" / "v3" / "reviews"
CHECK = C / "review" / "e0" / "checks" / "check.py"
W10 = V9 / "prompts" / "write_v10.md"
ADD = HERE / "prompts" / "additions.md"
SURAH_BRIEF = HERE / "prompts" / "surah_map.md"
WORK = HERE / "work"
OUT = HERE / "out"

SYSTEM = ("You are a careful scholar of Quranic Arabic and a fine Turkish prose writer. Follow the brief in the "
          "user message exactly and return only the requested output.")
AYAT = ["1:6", "100:1", "100:6"]
ARMS = ["H", "V", "D", "VD", "DM"]
V16_DICT = {"D", "VD", "DM"}  # arms that read the v16 dictionary
V5_RUN = {1: "s001-fresh-20260910", 100: "s100-regular-20260911"}
LANES = ["micro", "macro", "global"]
PROSE_MIN_GZ = 0.2  # natural prose compresses to 0.28-0.38 of its size; templated lanes to 0.06-0.09
GATE_USD = 5.0
OUT_TOKENS_ASSUMED = 40_000  # E1 permitted calls measured 15-30k

BASE_EVIDENCE = ("context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and "
                 "01_dictionary.md (every attested branch of every root of the ayah's words, with the classical "
                 "dictionaries' source phrases)")
JUDGEMENTS = ("both are earlier readers' proposals: ignore their judgements (grades, strength or confidence labels, "
              "reading types, statements of what a reading may or may not do) and make your own")
ARM_EVIDENCE = {
    "H": ("02_hft.md (earlier activation hypotheses for this ayah in its surah) and channels.md (the surah's "
          f"channel-review subchannels anchored in this ayah; {JUDGEMENTS})"),
    "V": ("the scope notes (an earlier reader's findings: micro on the ayah's own words, macro on its surah, "
          "global on the Quran and the Fatiha; that reader had to state every limit, so its boundary sentences are "
          "its caution, not rules for you)"),
    "D": None,
    "DM": ("surah_map.md (an earlier reader's map of the image chains that run through the whole surah, with the "
           "dictionary phrases of their members in other ayat; a proposal, not an authority)"),
}
ARM_EVIDENCE["VD"] = ARM_EVIDENCE["V"]
_SRC = None


def v16_dictionary(ref: str, path: Path) -> Path:
    global _SRC
    sys.path.insert(0, str(HERE))
    import dictionary as D
    if _SRC is None:
        _SRC = D.P.Sources()
    path.write_text(D.section(_SRC, ref), encoding="utf-8")
    return path


def rel(p: Path) -> str:
    return str(p.relative_to(REPO))


def inline(*files: Path) -> str:  # identical to v9/luna/run.py inline()
    return "\n\n".join(f"===== {rel(p)} =====\n{p.read_text(encoding='utf-8')}" for p in files)


def sa(ref: str) -> tuple[int, str]:
    s, a = ref.split(":")
    return int(s), f"{s}_{a}"


def channel_slice(ref: str) -> str:
    """Parent headers plus every subchannel whose 'Ayah anchors' line names the ayah, verbatim."""
    s, _ = sa(ref)
    src = CHANNELS / f"s{s:03d}" / "reader_a_pilot.md"
    blocks, cur = [], []
    for line in src.read_text(encoding="utf-8").splitlines():
        if line.startswith("#"):
            blocks.append(cur)
            cur = []
        cur.append(line)
    blocks.append(cur)
    out, parent = [], None
    for b in blocks:
        if not b:
            continue
        head = b[0]
        if head.startswith("#### ") or (head.startswith("### S") and head[5:6].isdigit()):
            anchors = " ".join(l for l in b if "Ayah anchors" in l)
            if ref in re.findall(r"\b\d{1,3}:\d{1,3}\b", anchors):
                if parent:
                    out.append("\n".join(parent).rstrip())
                    parent = None
                out.append("\n".join(b).rstrip())
        elif head.startswith("### "):
            parent = b
        elif head.startswith("## "):
            parent = None
            out.append(head)
    text = "\n\n".join(x for x in out if x)
    return f"# Channel review of surah {s}: subchannels anchored in {ref}\n\n(source: {src.relative_to(REPO.parent)})\n\n{text}\n"


def v5_lanes(ref: str) -> list[tuple[Path, float]]:
    s, name = sa(ref)
    d = V5 / "raw" / V5_RUN[s] / f"s{s:03d}" / name
    lanes = []
    for lane in LANES:
        p = d / f"{lane}.scope.tr.md"
        b = p.read_bytes()
        lanes.append((p, len(zlib.compress(b, 9)) / len(b)))
    return lanes


def build(ref: str, arm: str) -> tuple[str, dict]:
    s, name = sa(ref)
    ctx = V9 / "lines" / "work" / name / "context.md"
    wd = WORK / name / arm
    wd.mkdir(parents=True, exist_ok=True)
    dic = (v16_dictionary(ref, wd / "01_dictionary.md") if arm in V16_DICT
           else V9 / "input" / "v2" / f"s{s:03d}" / name / "01_dictionary.md")
    meta = {"ref": ref, "arm": arm}
    if arm == "H":
        ch = wd / "channels.md"
        ch.write_text(channel_slice(ref), encoding="utf-8")
        extra = [V9 / "input" / "v2" / f"s{s:03d}" / name / "02_hft.md", ch]
    elif arm == "D":
        extra = []
    elif arm == "DM":
        m = OUT / f"s{s:03d}" / "surah" / "map.md"
        if not m.exists():
            raise SystemExit(f"{ref} DM: no surah map at {rel(m)}; run the surah call first")
        extra = [m]
    else:
        lanes = v5_lanes(ref)
        extra = [p for p, r in lanes if r >= PROSE_MIN_GZ]
        meta["v5_lanes"] = {p.name: {"gz_ratio": round(r, 3), "kept": r >= PROSE_MIN_GZ} for p, r in lanes}
    stdin = inline(W10, ADD, ctx, dic, *extra)
    prompt = (f"Focus: {ref}. Follow the brief below (write.md) and its additions (additions.md) exactly. The "
              f"evidence is {BASE_EVIDENCE}{' and ' + ARM_EVIDENCE[arm] if ARM_EVIDENCE[arm] else ''} and your own "
              f"knowledge of Arabic and the Quran. "
              f"Return only the reader's prose as your final message.")
    text = prompt + "\n\n" + stdin
    (wd / "prompt.md").write_text(text, encoding="utf-8")
    meta["files"] = [rel(p) for p in (W10, ADD, ctx, dic, *extra)]
    (wd / "packet.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return text, meta


def est_tokens(text: str) -> int:  # the cost critic's calibrated formula, as in E1
    ar = len(re.findall(r"[؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿]", text))
    return int(4581 + 1.151 * ar + 0.366 * (len(text) - ar))


def estimate(text: str) -> float:  # measured E1 rates: cache write $8/M, output $20/M
    return est_tokens(text) * 8e-6 + OUT_TOKENS_ASSUMED * 20e-6


def log(row: dict) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "ledger.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def call_opus(text: str, d: Path) -> dict:
    cmd = ["claude", "-p", "--model", "claude-opus-5-5", "--effort", "high", "--tools", "",
           "--output-format", "json", "--no-session-persistence", "--safe-mode",
           "--permission-mode", "dontAsk", "--system-prompt", SYSTEM]
    with tempfile.TemporaryDirectory(prefix="v16_opus_") as cwd:
        p = subprocess.run(cmd, input=text, capture_output=True, text=True, cwd=cwd)
    (d / "run.log.json").write_text((p.stdout or json.dumps({"error": p.stderr[-3000:]})).strip() + "\n",
                                    encoding="utf-8")
    try:
        return json.loads(p.stdout)
    except json.JSONDecodeError:
        return {}


def usage_row(obj: dict) -> dict:
    usage = obj.get("usage", {}) or {}
    return {"cost_usd": obj.get("total_cost_usd"), "output_tokens": usage.get("output_tokens"),
            "thinking_tokens": (usage.get("output_tokens_details") or {}).get("thinking_tokens"),
            "cache_write": usage.get("cache_creation_input_tokens"), "num_turns": obj.get("num_turns")}


def run_one(ref: str, arm: str) -> str:
    _, name = sa(ref)
    d = OUT / name / arm
    if (d / "run.log.json").exists():
        return f"{ref} {arm}: exists, skipped (never rerun)"
    text, _ = build(ref, arm)
    est = estimate(text)
    if est >= GATE_USD:
        log({"ref": ref, "arm": arm, "status": "gated", "estimate_usd": round(est, 2)})
        return f"{ref} {arm}: gated at ${est:.2f}"
    d.mkdir(parents=True, exist_ok=True)
    (d / "prompt.md").write_text(text, encoding="utf-8")
    t0 = time.time()
    obj = call_opus(text, d)
    result = (obj.get("result") or "").strip()
    status = "ok" if result and not obj.get("is_error") else "error"
    reading = d / f"{name}.reading.tr.md"
    if result:
        reading.write_text(result + "\n", encoding="utf-8")
        subprocess.run([sys.executable, str(CHECK), str(reading), "--ref", ref, "--out", str(d / "check.json"),
                        "--quiet"], cwd=CHECK.parent)
    row = {"ref": ref, "arm": arm, "status": status, "seconds": round(time.time() - t0),
           "estimate_usd": round(est, 2), **usage_row(obj),
           "words": len(result.split()) if result else 0, "prompt_chars": len(text)}
    log(row)
    return f"{ref} {arm}: {status} ${row['cost_usd']} {row['words']}w {row['seconds']}s"


HFT_TRACE = re.compile(r"^(\s*- )(\d+:\d+)\s+w[\d,]+\s+(\*\*.+?\*\*)\s+\((.+?)\s+(B\d+):.*?\)\s+—\s+(.*)$")
HFT_PREFIX = re.compile(r"^(?:baseline|base|ctx|context|delta|outlier|out|[bcdo]\d*)[_-]", re.I)


def trim_hft(text: str) -> str:
    """One ayah's HFT records without judgements: the record name without its class prefix and [label], the
    changed reading, the mechanism, and each trace step as ayah, word, branch and contribution (the dictionary
    carries the branch glosses). Drops `before`, `containment` and the reader overview."""
    out, keep = [], False
    for line in text.splitlines():
        if line.startswith("## "):
            keep = not line.startswith("## HFT reader overview")
            if keep:
                name = HFT_PREFIX.sub("", re.sub(r"\s*\[[^\]]*\]\s*$", "", line[3:]))
                name = re.sub(r"^(?:\d+[_-])+", "", name)
                out += ["", "## " + re.sub(r"[_-]", " ", name).lower()]
            continue
        if not keep:
            continue
        if line.startswith("- after:"):
            reading = re.sub(r"^Exploratorily,\s*", "", line[len("- after:"):].strip())
            out.append("- reading: " + reading[:1].upper() + reading[1:])
        elif line.startswith(("- mechanism:", "- trace:")):
            out.append(line)
        elif line.startswith("  - "):
            m = HFT_TRACE.match(line)
            out.append(f"{m[1]}{m[2]} {m[3]} {m[4]} {m[5]}: {m[6]}" if m else line)
    return "\n".join(out).strip() + "\n"


def surah_build(s: int) -> tuple[str, Path]:
    global _SRC
    sys.path.insert(0, str(HERE))
    import dictionary as D
    if _SRC is None:
        _SRC = D.P.Sources()
    refs = []
    while f"{s}:{len(refs) + 1}" in _SRC.quran:
        refs.append(f"{s}:{len(refs) + 1}")
    wd = WORK / f"s{s:03d}" / "surah"
    wd.mkdir(parents=True, exist_ok=True)
    text = wd / "text.md"
    text.write_text(f"# Surah {s}\n\n" + "\n".join(f"- {r} {_SRC.quran[r]}" for r in refs) + "\n", encoding="utf-8")
    dic = wd / "dictionary.md"
    dic.write_text(D.surah_section(_SRC, refs), encoding="utf-8")
    hft = wd / "hft.md"
    parts = [f"# HFT: earlier activation hypotheses, per focus ayah of surah {s}"]
    for r in refs:
        f = V9 / "input" / "v2" / f"s{s:03d}" / r.replace(":", "_") / "02_hft.md"
        parts.append(f"\n# Focus {r}\n\n" + trim_hft(f.read_text(encoding="utf-8")))
    hft.write_text("\n".join(parts), encoding="utf-8")
    src = CHANNELS / f"s{s:03d}" / "reader_a_pilot.md"
    ch = wd / "channels.md"
    ch.write_text(f"(source: {src.relative_to(REPO.parent)})\n\n" + src.read_text(encoding="utf-8"), encoding="utf-8")
    prompt = (f"Surah: {s}. Follow the brief below (surah_map.md) exactly. The evidence is text.md (the surah), "
              f"dictionary.md (every root of the surah's words, each branch with the classical dictionaries' own "
              f"phrases), hft.md and channels.md ({JUDGEMENTS}) and your own knowledge of Arabic and the Quran. "
              f"Return only the map as your final message.")
    full = prompt + "\n\n" + inline(SURAH_BRIEF, text, dic, hft, ch)
    (wd / "prompt.md").write_text(full, encoding="utf-8")
    return full, wd


def surah_run(s: int) -> str:
    d = OUT / f"s{s:03d}" / "surah"
    if (d / "run.log.json").exists():
        return f"S{s} surah: exists, skipped (never rerun)"
    text, _ = surah_build(s)
    est = estimate(text)
    if est >= GATE_USD:
        log({"ref": f"S{s}", "arm": "surah", "status": "gated", "estimate_usd": round(est, 2)})
        return f"S{s} surah: gated at ${est:.2f}"
    d.mkdir(parents=True, exist_ok=True)
    (d / "prompt.md").write_text(text, encoding="utf-8")
    t0 = time.time()
    obj = call_opus(text, d)
    result = (obj.get("result") or "").strip()
    status = "ok" if result and not obj.get("is_error") else "error"
    if result:
        (d / "map.md").write_text(result + "\n", encoding="utf-8")
    row = {"ref": f"S{s}", "arm": "surah", "status": status, "seconds": round(time.time() - t0),
           "estimate_usd": round(est, 2), **usage_row(obj),
           "words": len(result.split()) if result else 0, "prompt_chars": len(text)}
    log(row)
    return f"S{s} surah: {status} ${row['cost_usd']} {row['words']}w {row['seconds']}s"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=("build", "run", "surah"))
    ap.add_argument("--surah", type=int)
    ap.add_argument("--run", action="store_true", help="surah: make the call (default: build and estimate)")
    ap.add_argument("--arm", choices=ARMS)
    ap.add_argument("--ayah")
    ap.add_argument("--parallel", type=int, default=3)
    a = ap.parse_args()
    ayat = [a.ayah] if a.ayah else AYAT
    arms = [a.arm] if a.arm else ARMS
    jobs = [(r, k) for r in ayat for k in arms]
    if a.cmd == "surah":
        if not a.surah:
            ap.error("surah needs --surah N")
        if a.run:
            print(surah_run(a.surah))
            return
        full, wd = surah_build(a.surah)
        for f in ("text.md", "dictionary.md", "hft.md", "channels.md"):
            print(f"  {f:14} {len((wd / f).read_text(encoding='utf-8')):>8,} chars")
        print(f"S{a.surah} surah: {len(full):,} chars ~{est_tokens(full):,} tokens  est ${estimate(full):.2f}"
              f"  ({'ok' if estimate(full) < GATE_USD else 'BLOCK'})")
        return
    if a.cmd == "run" and not a.arm:
        ap.error("run needs --arm (each arm is approved separately)")
    if a.cmd == "build":
        total = 0.0
        for r, k in jobs:
            try:
                t, meta = build(r, k)
            except SystemExit as e:
                print(f"{r:6} {k}  skipped: {e}")
                continue
            e = estimate(t)
            total += e
            lanes = ""
            if "v5_lanes" in meta:
                lanes = "  v5: " + ", ".join(f"{n.split('.')[0]} {v['gz_ratio']}{'' if v['kept'] else ' (out)'}"
                                             for n, v in meta["v5_lanes"].items())
            print(f"{r:6} {k}  {len(t):>8,} chars ~{est_tokens(t):>7,} tokens  est ${e:.2f}"
                  f"  ({'ok' if e < GATE_USD else 'BLOCK'}){lanes}")
        print(f"total for {len(jobs)} calls: ${total:.2f} (assumes {OUT_TOKENS_ASSUMED:,} output tokens each)")
        return
    with cf.ThreadPoolExecutor(a.parallel) as ex:
        for msg in ex.map(lambda j: run_one(*j), jobs):
            print(msg, flush=True)


if __name__ == "__main__":
    sys.exit(main())
