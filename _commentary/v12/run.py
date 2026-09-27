#!/usr/bin/env python3
"""V12: one ayah → one Opus call (ledger + reading) on V11's evidence plus the existing chains (HFT, channel review),
the neighbours' branches and the root dossiers; one surah (or passage) pass over every ledger. Fully automated:
every step validates its own output, repairs what a script can, sends the rest to a small repair call, and records
the outcome in status.json. See RUNBOOK.md (commands) and README.md (design).

Cost rule (the user's): a call starts only when its estimated cost is below --max-cost ($5); once started it is never
stopped and never retried, whatever it costs. The estimate (estimate()) is input tokens (bytes × tokens per byte) at
$8/M (one-hour cache write) plus the expected output tokens at $20/M, both calibrated on the finished calls in out/.

  prep    scripts only: inputs.py (V11 prep + hft.md, channels.md, neighbours.md, usage.md)
  write   one Opus call (no tools): evidence first, prompts/write.md last → ledger, reading (no retry: an unusable
          answer marks the ayah failed)
  check   tag repair (commas), verify_src --fix, wrong-source fix (the quote occurs in exactly one place), validator;
          residual problems → one repair call for the affected paragraphs (up to 2 rounds); what still fails is
          reduced to plain Turkish (the tag's gloss) and counted — nothing waits for a human
  render  S_A.md = reading + Kur'an'ı Kur'an'la (Surah, Quran, Limits, Fatiha, with ayah texts) + Kur'an'da bu
          kelimeler (Usage) + Kelimeler ve okuyuşlar (Dictionary, Readings) + Surenin bütününde (surah pass notes)
  ayah    prep → write → check → render for one or more refs (comma-separated), skipping finished ones
  surah   every ayah of a surah (parallel), then the surah pass (short surahs: one; long: one per passage window)
  chains  the surah pass only: chains S [--window LO-HI]
  status  one line per ayah of a surah (state, cost, checks)

Usage: python3 _commentary/v12/run.py ayah 29:39,29:41,29:45 --parallel 3
       python3 _commentary/v12/run.py surah 1 --parallel 7
       python3 _commentary/v12/run.py status 1
Options: --effort high|xhigh|max (writer; default high), --force (redo finished ayat), --max-cost 5 (a call starts only
         below this estimate), --no-usage (leave usage.md out), --tag NAME (outputs in out-NAME/, for arms).
Outputs: _commentary/v12/out/sNNN/S_A/, out/sNNN/surah/<window>/.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

V12 = Path(__file__).resolve().parent
REPO = V12.parents[1]
V9 = REPO / "_commentary" / "v9"
V11 = REPO / "_commentary" / "v11"
PY = sys.executable
sys.path.insert(0, str(V9))
sys.path.insert(0, str(V11))
sys.path.insert(0, str(V12))
from verify_ar import QURAN_TEXT, loose  # noqa: E402
import inputs as I  # noqa: E402

SYSTEM = ("You are a careful scholar of Quranic Arabic and a fine Turkish prose writer. Follow the brief at the end of "
          "the user message exactly and return only the requested output.")
EFFORT = "high"
MAX_COST = 5.0
FORCE = False
USAGE = True                  # --no-usage: usage.md (root dossiers) is left out of the evidence
OUT = V12 / "out"             # --tag NAME: V12 / "out-NAME"
PRICE_IN, PRICE_OUT = 8e-6, 20e-6        # $/token: input as a one-hour cache write, output (V11 100:7 bill: exact)
TOK_PER_BYTE = 1.0                      # default until calibrated (Arabic-heavy evidence)
EXPECTED_OUT = {"high": 60_000, "xhigh": 80_000, "max": 110_000}   # defaults until calibrated
SURAH_OUT = 50_000
TAG_RE = re.compile(r"\{\s*ar\s*:\s*([^{},\n]*?)\s*,\s*tr\s*:\s*([^{}]*?)\s*,\s*gloss\s*:\s*([^{}]*?)"
                    r"(?:\s*,\s*source\s*:\s*([^{}]*?))?\s*\}")


# ---------------------------------------------------------------- paths
def paths(ref: str) -> dict:
    s, a = (int(x) for x in ref.split(":"))
    sa = f"{s}_{a}"
    return {"sa": sa, "pkg": V9 / "input" / "v2" / f"s{s:03d}" / sa, "v9w": V9 / "lines" / "work" / sa,
            "in": I.work_dir(ref), "out": OUT / f"s{s:03d}" / sa}


def quran() -> dict[str, str]:
    q = {}
    for line in QURAN_TEXT.read_text(encoding="utf-8-sig").splitlines():
        r, _, t = line.partition("|")
        if t:
            q[r.strip()] = t.strip().lstrip("﻿")
    return q


def surah_refs(s: int) -> list[str]:
    return [r for r in quran() if r.startswith(f"{s}:") and not r.endswith(":0")]


def inline(*files: Path) -> str:
    return "\n\n".join(f"===== {f.name} =====\n{f.read_text(encoding='utf-8')}" for f in files)


def status_path(ref: str) -> Path:
    return paths(ref)["out"] / "status.json"


def set_status(ref: str, **kw) -> dict:
    f = status_path(ref)
    f.parent.mkdir(parents=True, exist_ok=True)
    d = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {"ref": ref}
    d.update(kw, updated=time.strftime("%Y-%m-%d %H:%M:%S"))
    f.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return d


def get_status(ref: str) -> dict:
    f = status_path(ref)
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {"ref": ref, "state": "new"}


def _median(xs: list[float]) -> float | None:
    xs = sorted(xs)
    return xs[len(xs) // 2] if xs else None


def calibration() -> tuple[float, dict[str, float]]:
    """Tokens per input byte and output tokens per effort, from the finished ayah calls (≥ 3 each), else defaults."""
    ratios, outs = [], {}
    for f in V12.glob("out*/s*/*/status.json"):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if d.get("in") and d.get("input_bytes") and d.get("attempts") == 1:
            ratios.append(d["in"] / d["input_bytes"])
        if d.get("out") and d.get("effort"):
            outs.setdefault(d["effort"], []).append(d["out"])
    tpb = _median(ratios) if len(ratios) >= 3 else TOK_PER_BYTE
    exp = {e: (_median(outs.get(e, [])) if len(outs.get(e, [])) >= 3 else n) for e, n in EXPECTED_OUT.items()}
    return tpb, exp


def estimate(input_bytes: int, out_tokens: float | None = None) -> float:
    tpb, exp = calibration()
    out = out_tokens if out_tokens is not None else exp.get(EFFORT, EXPECTED_OUT["high"])
    return round(input_bytes * tpb * PRICE_IN + out * PRICE_OUT, 2)


def locked(ref: str) -> bool:
    """A running write of this ayah (another process) is never restarted."""
    lock = paths(ref)["out"] / "lock"
    if not lock.exists():
        return False
    try:
        os.kill(int(lock.read_text().strip()), 0)
        return True
    except (ValueError, ProcessLookupError, PermissionError):
        lock.unlink(missing_ok=True)
        return False


_HELD: set[str] = set()


def acquire(ref: str) -> bool:
    """Take the ayah's lock atomically (O_EXCL; a stale lock is cleared first), so two runs — or one ref listed twice —
    can never start two writer calls for the same ayah."""
    lock = paths(ref)["out"] / "lock"
    lock.parent.mkdir(parents=True, exist_ok=True)
    for _ in range(2):
        try:
            fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            if locked(ref):
                return False
            continue
        with os.fdopen(fd, "w") as fh:
            fh.write(str(os.getpid()))
        return True
    return False


# ---------------------------------------------------------------- the model call
def opus(prompt: str, stdin: str, log: Path, effort: str | None = None) -> tuple[str, dict]:
    """One fresh Opus call (no tools, no MCP). Returns (every assistant text block in order, usage summary)."""
    r = subprocess.run(["claude", "-p", "--model", "opus", "--effort", effort or EFFORT, "--tools", "",
                        "--strict-mcp-config", "--output-format", "stream-json", "--verbose",
                        "--no-session-persistence", "--system-prompt", SYSTEM],
                       input=prompt + "\n\n" + stdin, capture_output=True, text=True, cwd=REPO,
                       env={**os.environ, "CLAUDE_CODE_MAX_OUTPUT_TOKENS": "128000"})
    with log.open("a", encoding="utf-8") as fh:
        fh.write(r.stdout or json.dumps({"error": r.stderr[-3000:]}) + "\n")
    text, usage = [], {"cost": 0.0, "in": 0, "out": 0}
    for line in (r.stdout or "").splitlines():
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        if d.get("type") == "assistant":
            text += [b.get("text", "") for b in d["message"].get("content", []) if b.get("type") == "text"]
        elif d.get("type") == "result":
            u = d.get("usage", {})
            usage = {"cost": round(d.get("total_cost_usd", 0) or 0, 3),
                     "in": u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0)
                     + u.get("cache_read_input_tokens", 0), "out": u.get("output_tokens", 0)}
    return "\n".join(text), usage


# ---------------------------------------------------------------- steps
def prep(ref: str) -> dict:
    return I.build(ref)


def evidence(ref: str) -> list[Path]:
    p = paths(ref)
    dig = p["in"] / "digest_v2.md" if USAGE and (p["in"] / "digest_v2.md").exists() else p["v9w"] / "digest_v2.md"
    files = [p["v9w"] / "context.md", p["pkg"] / "01_dictionary.md", dig]
    names = ("usage.md", "hft.md", "channels.md", "neighbours.md") if USAGE else ("hft.md", "channels.md", "neighbours.md")
    files += [p["in"] / n for n in names if (p["in"] / n).exists()]
    return files


def write(ref: str) -> dict:
    p = paths(ref)
    p["out"].mkdir(parents=True, exist_ok=True)
    files = evidence(ref) + [V12 / "prompts" / "write.md"]
    prompt = (f"Focus: {ref}. The evidence comes first ({', '.join(f.name for f in files[:-1])}); the brief "
              f"({files[-1].name}) is last. Follow the brief exactly and return the ledger and the reading with their "
              f"marker lines.")
    stdin = inline(*files)
    final, u = opus(prompt, stdin, p["out"] / "run.log.jsonl")
    set_status(ref, attempts=1, effort=EFFORT, **u)
    (p["out"] / "final.txt").write_text(final, encoding="utf-8")
    ledger, _, reading = final.partition("===== READING =====")
    ledger = ledger.split("===== LEDGER =====", 1)[-1]
    if len(reading.split()) >= 300 and "===== LEDGER =====" in final and ledger.count("\n- ") >= 10:
        (p["out"] / f"{p['sa']}.ledger.md").write_text(ledger.strip() + "\n", encoding="utf-8")
        (p["out"] / f"{p['sa']}.reading.tr.md").write_text(reading.strip() + "\n", encoding="utf-8")
        return {"attempts": 1, "effort": EFFORT, **u}
    raise RuntimeError(f"{ref}: no usable ledger + reading (no retry, by rule; see final.txt)")


def repair_commas(path: Path) -> int:
    """Commas inside ar/tr break the tag format; drop them (V11)."""
    text = path.read_text(encoding="utf-8")
    n = 0

    def fix(m: re.Match) -> str:
        nonlocal n
        ar, tr, gloss, src = m.group(1), m.group(2), m.group(3), m.group(4)
        ar2, tr2 = ar.replace("،", "").replace(",", ""), tr.replace(",", "")
        n += (ar2 != ar) + (tr2 != tr)
        return f"{{ar:{ar2}, tr:{tr2}, gloss:{gloss}" + (f", source:{src}" if src is not None else "") + "}"

    text = re.sub(r"\{\s*ar\s*:\s*(.*?)\s*,\s*tr\s*:\s*(.*?)\s*,\s*gloss\s*:\s*([^{}]*?)(?:\s*,\s*source\s*:\s*([^{}]*?))?\s*\}",
                  fix, text)
    path.write_text(text, encoding="utf-8")
    return n


def verify(path: Path) -> tuple[str, list[str]]:
    """verify_src exits 1 when problems remain (normal); a crash (no summary line) raises, so an unverified reading is
    never taken for a clean one."""
    r = subprocess.run([PY, str(V11 / "verify_src.py"), str(path), "--fix"], capture_output=True, text=True, cwd=REPO)
    out = r.stdout.splitlines()
    if not out or "exact=" not in out[0]:
        raise RuntimeError(f"verify_src failed on {path.name}: {(r.stderr or r.stdout)[-600:]}")
    return out[0], out[1:]


_DICT = None


def fix_sources(path: Path, problems: list[str]) -> int:
    """`elsewhere`: the quote is not in its declared source but occurs in exactly one ayah (or one branch of a
    declared root): the source is rewritten to that place."""
    global _DICT
    bad = [re.match(r"line \d+: elsewhere  (.*?)  \(source: (.*)\)$", p) for p in problems]
    bad = [m for m in bad if m]
    if not bad:
        return 0
    if _DICT is None:
        from verify_src import Dictionary  # noqa: E402
        _DICT = Dictionary()
    q = {r: loose(unicodedata.normalize("NFC", t))[0] for r, t in quran().items()}
    text = path.read_text(encoding="utf-8")
    n = 0
    for m in bad:
        ar, src = m.group(1).strip(), m.group(2).strip()
        al = loose(unicodedata.normalize("NFC", ar))[0].strip()
        if not al:
            continue
        hits = [r for r, t in q.items() if al in t]
        new = None
        if len(hits) == 1:
            new = hits[0]
        else:
            roots = re.findall(r"([ء-ي](?: [ء-ي]){1,4})\s+B\d{3}", src)
            bh = []
            for root in dict.fromkeys(roots):
                for rid in _DICT.by_name.get(root, []):
                    for b in _DICT.entry(rid).get("branches", []):
                        bid = b.get("branch_ref", "").split("/")[-1]
                        if any(al in loose(t)[0] for t in _DICT.texts(root, bid)):
                            bh.append(f"{root} {bid}")
            bh = list(dict.fromkeys(bh))
            if len(bh) == 1:
                new = bh[0]
        if new:
            pat = re.compile(r"(\{\s*ar\s*:\s*" + re.escape(ar) + r"\s*,[^{}]*?source\s*:\s*)" + re.escape(src) + r"(\s*\})")
            text, k = pat.subn(lambda mm: mm.group(1) + new + mm.group(2), text, count=1)
            n += k
    path.write_text(text, encoding="utf-8")
    return n


def validate(path: Path) -> list[str]:
    probe = path.with_name(path.stem + ".validate.tmp.md")
    probe.write_text(re.sub(r"(\{ar:[^{}]*?gloss:[^{}]*?), source:[^{}]*\}", r"\1}", path.read_text(encoding="utf-8")),
                     encoding="utf-8")
    r = subprocess.run([PY, str(REPO / "_commentary" / "v5" / "validate_prose.py"), str(probe)],
                       capture_output=True, text=True, cwd=REPO)
    probe.unlink(missing_ok=True)
    if "Traceback" in r.stderr or (r.returncode not in (0, 1) and not r.stdout.strip()):
        raise RuntimeError(f"validate_prose failed on {path.name}: {r.stderr[-600:]}")
    return [l for l in r.stdout.splitlines() if ": error:" in l]


BLOCKING = ("missing", "no-source", "bad-source", "fixable")


def blocking(problems: list[str]) -> list[str]:
    return [p for p in problems if re.match(rf"line \d+: ({'|'.join(BLOCKING)}) ", p)]


REPAIR_BRIEF = """# Repair brief (v12): fix only the flagged Arabic tags in these paragraphs

Below are paragraphs of a Turkish reading, and a list of problems a script found in their Arabic tags
`{ar:…, tr:…, gloss:…, source:…}` (line numbers refer to the whole file). For each flagged tag:
- missing / fixable: the Arabic is not found (or not exactly) in its declared source. Correct it to the exact
  wording of the source (a Quran ayah `S:A`, or a dictionary branch `root Bnnn`), or, if you cannot be sure of the
  exact wording, remove the tag and say the same thing in plain Turkish;
- no-source: add the correct source (the ayah it is quoted from, or `root Bnnn`);
- bad-source: the source is not a valid ayah or branch; correct it, or remove the tag as above;
- validator: the tag's format is broken (exactly four fields, no comma inside ar or tr, no colon inside gloss).
Change nothing else: same wording, same order, same paragraphs. Return every paragraph, in order, each preceded
by its marker line exactly as given (`===== P<n> =====`), and nothing else.
"""


def repair_call(path: Path, problems: list[str], log: Path) -> tuple[int, float]:
    """One small Opus call over the paragraphs that hold the flagged tags; the script replaces those paragraphs.
    Returns (paragraphs replaced, cost)."""
    text = path.read_text(encoding="utf-8")
    paras = re.split(r"(\n\s*\n)", text)
    starts, pos = [], 0
    for chunk in paras:
        starts.append(pos)
        pos += len(chunk)
    lines = [int(m.group(1)) for m in (re.match(r"line (\d+):", p) for p in problems) if m]
    want = set()
    for ln in lines:
        off = sum(len(l) + 1 for l in text.split("\n")[:ln - 1])
        for i, st in enumerate(starts):
            if st <= off < st + len(paras[i]) and paras[i].strip():
                want.add(i)
    if not want:
        return 0, 0.0
    order = sorted(want)
    body = "\n\n".join(f"===== P{k} =====\n{paras[i]}" for k, i in enumerate(order, 1))
    final, u = opus("Follow the repair brief at the end exactly.",
                    "## Problems\n" + "\n".join(problems) + "\n\n## Paragraphs\n" + body + "\n\n" + REPAIR_BRIEF,
                    log, effort="medium")
    got = {int(m.group(1)): m.group(2).strip("\n") for m in
           re.finditer(r"===== P(\d+) =====\n(.*?)(?=\n===== P\d+ =====|\Z)", final, re.S)}
    n = 0
    for k, i in enumerate(order, 1):
        new = got.get(k, "").strip()
        if new and abs(len(new) - len(paras[i].strip())) < 0.5 * len(paras[i]) + 200:
            paras[i] = new
            n += 1
    path.write_text("".join(paras), encoding="utf-8")
    return n, u["cost"]


def strip_unverified(path: Path, problems: list[str]) -> int:
    """Last resort, still automatic: a flagged tag whose Arabic cannot be verified becomes its gloss in plain Turkish.
    Only the flagged occurrence (its line and Arabic) is touched, never the same Arabic verified elsewhere."""
    lines = path.read_text(encoding="utf-8").split("\n")
    bad: dict[int, set[str]] = {}
    for p in problems:
        m = re.match(r"line (\d+): (missing|bad-source|no-source|fixable)  (.*?)(  |$)", p)
        if m:
            bad.setdefault(int(m.group(1)), set()).add(m.group(3).strip())
    n = 0
    for ln, ars in bad.items():
        if not 0 < ln <= len(lines):
            continue

        def sub(m: re.Match) -> str:
            nonlocal n
            if m.group(1).strip() in ars:
                n += 1
                return m.group(3).strip()
            return m.group(0)

        lines[ln - 1] = TAG_RE.sub(sub, lines[ln - 1])
    path.write_text("\n".join(lines), encoding="utf-8")
    return n


def check_text(path: Path, log: Path) -> dict:
    """The whole automatic check-and-repair loop for one reading file."""
    res = {"comma_fixes": repair_commas(path), "source_fixes": 0, "repair_calls": 0, "repair_cost": 0.0, "stripped": 0}
    for rnd in range(3):
        summary, problems = verify(path)
        res["source_fixes"] += fix_sources(path, problems)
        if res["source_fixes"]:
            summary, problems = verify(path)
        errs = validate(path)
        block = blocking(problems) + [f"line {m.group(1)}: validator  {m.group(2)}"
                                      for m in (re.search(r":(\d+): error: (.*)$", e) for e in errs) if m]
        if not block:
            break
        if rnd < 2:
            res["repair_calls"] += 1
            res["repair_cost"] = round(res["repair_cost"] + repair_call(path, block, log)[1], 3)
            repair_commas(path)
        else:
            res["stripped"] = strip_unverified(path, block)
            summary, problems = verify(path)
            errs = validate(path)
    res["verify"] = summary
    res["elsewhere"] = sum(1 for p in problems if ": elsewhere " in p)
    res["validator_errors"] = len(validate(path))
    return res


def check(ref: str) -> dict:
    p = paths(ref)
    reading = p["out"] / f"{p['sa']}.reading.tr.md"
    res = check_text(reading, p["out"] / "repair.log.jsonl")
    ledger = (p["out"] / f"{p['sa']}.ledger.md").read_text(encoding="utf-8")
    fam = families(ledger)
    body = reading.read_text(encoding="utf-8")
    cited = set(re.findall(r"\b\d{1,3}:\d{1,3}\b", ledger + body))
    digest = (p["v9w"] / "digest_v2.md").read_text(encoding="utf-8") if (p["v9w"] / "digest_v2.md").exists() else ""
    related = re.findall(r"(?m)^\s*- (\d{1,3}:\d{1,3}) — ", digest)
    uncited = [r for r in dict.fromkeys(related) if r not in cited]
    sizes = read_sizes(ref)
    res.update({
        "ledger_findings": sum(len(v) for v in fam.values()),
        "families": {k: len(v) for k, v in fam.items()},
        "reading_words": len(body.split()),
        "reading_refs": len(set(re.findall(r"\b\d{1,3}:\d{1,3}\b", body))),
        "related_uncited": len(uncited), "related_uncited_first": uncited[:15],
        "input_bytes": sum(f.stat().st_size for f in evidence(ref) + [V12 / "prompts" / "write.md"]), "inputs": sizes})
    (p["out"] / "check.txt").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return res


def families(ledger: str) -> dict[str, list[str]]:
    fam, current = {}, None
    for line in ledger.splitlines():
        if line.startswith("### "):
            current = line[4:].strip().lower()
            fam.setdefault(current, [])
        elif line.startswith("- ") and current:
            fam[current].append(line)
    return fam


def surah_out(surah: int, win: tuple[int, int] | None) -> Path:
    n = I.surah_len(surah)
    name = "all" if not win or win == (1, n) else f"{win[0]}-{win[1]}"
    return OUT / f"s{surah:03d}" / "surah" / name


def render(ref: str) -> None:
    p = paths(ref)
    q = quran()
    fam = families((p["out"] / f"{p['sa']}.ledger.md").read_text(encoding="utf-8"))
    reading = (p["out"] / f"{p['sa']}.reading.tr.md").read_text(encoding="utf-8").strip()
    paras = [x for x in re.split(r"\n\s*\n", reading) if x.strip() and not x.lstrip().startswith("#")]

    def pointers(refs: list[str]) -> str:
        refs = [r for r in refs if r != ref]
        hit = [str(i + 1) for i, x in enumerate(paras) if any(re.search(rf"(?<![\d:]){re.escape(r)}(?![\d])", x) for r in refs)]
        return f" [¶ {', '.join(hit)}]" if hit else ""

    def entries(names: tuple[str, ...], with_text: bool) -> list[str]:
        out, shown = [], set()
        for name in names:
            for key, lines in fam.items():
                if not key.startswith(name):
                    continue
                for line in lines:
                    m = re.match(r"- \[refs:\s*([^|\]]*)\|[^|\]]*\|\s*(\w+)\s*\]\s*(.*)", line)
                    refs = [r.strip() for r in m.group(1).split(",") if r.strip()] if m else []
                    grade, txt = (m.group(2), m.group(3)) if m else ("", line[2:])
                    out.append(f"- **{', '.join(refs) or '—'}** ({grade}) {txt}{pointers(refs)}")
                    if with_text:
                        for r in refs:
                            if r in q and r not in shown and r != ref:
                                shown.add(r)
                                out.append(f"  - {r} {q[r]}")
        return out

    doc = [reading, "", "---", "", "## Kur'an'ı Kur'an'la", "",
           "Sure içinden ve Kur'an'ın geri kalanından bu ayeti açan yerler: her biri, ne iş gördüğüyle.", ""]
    doc += entries(("surah", "quran", "limits", "fatiha"), True)
    usage = entries(("usage",), True)
    if usage:
        doc += ["", "## Kur'an'da bu kelimeler", "", "Bu ayetin kelimeleri Kur'an'ın başka yerlerinde nasıl kullanılır.", ""]
        doc += usage
    doc += ["", "## Kelimeler ve okuyuşlar", ""] + entries(("dictionary", "readings"), False)
    s, a = (int(x) for x in ref.split(":"))
    for notes in sorted((OUT / f"s{s:03d}" / "surah").glob("*/ayat.md")):
        mine = [l for l in notes.read_text(encoding="utf-8").splitlines() if re.match(rf"-\s*\**{re.escape(ref)}\b", l)]
        if mine:
            doc += ["", "## Surenin bütününde", ""] + [re.sub(rf"^-\s*\**{re.escape(ref)}\**:?\s*", "", m) for m in mine]
            break
    (p["out"] / f"{p['sa']}.md").write_text("\n".join(doc) + "\n", encoding="utf-8")


def read_sizes(ref: str) -> dict[str, int]:
    f = paths(ref)["in"] / "inputs.tsv"
    out = {}
    for line in f.read_text(encoding="utf-8").splitlines():
        parts = line.split("\t")
        if len(parts) == 2 and parts[1].isdigit():
            out[parts[0]] = int(parts[1])
    return out


def done(ref: str) -> bool:
    return get_status(ref).get("state") == "done" and (paths(ref)["out"] / f"{paths(ref)['sa']}.md").exists()


def ayah(ref: str, prepped: bool = False) -> str:
    """prep → write → check → render, with status and lock; never raises (the status says what happened)."""
    if done(ref) and not FORCE:
        return f"{ref}: done (skipped)"
    p = paths(ref)
    if ref in _HELD or not acquire(ref):
        return f"{ref}: running elsewhere (skipped)"
    _HELD.add(ref)
    try:
        set_status(ref, state="prep")
        sizes = read_sizes(ref) if prepped and (p["in"] / "inputs.tsv").exists() else prep(ref)
        usage_err = (p["in"] / "usage.error.txt").read_text(encoding="utf-8")[-300:] if (p["in"] / "usage.error.txt").exists() else ""
        nbytes = sum(f.stat().st_size for f in evidence(ref) + [V12 / "prompts" / "write.md"])
        est = estimate(nbytes)
        if est >= MAX_COST:
            set_status(ref, state="over-cost", input_bytes=nbytes, estimate=est, usage_error=usage_err)
            return f"{ref}: NOT STARTED (estimated ${est:.2f} ≥ ${MAX_COST:.2f})"
        set_status(ref, state="writing", input_bytes=nbytes, estimate=est, usage=USAGE, usage_error=usage_err)
        u = write(ref)
        set_status(ref, state="checking", **u)
        c = check(ref)
        render(ref)
        st = set_status(ref, state="done", verify=c["verify"], stripped=c["stripped"], repair_calls=c["repair_calls"],
                        repair_cost=c["repair_cost"], total_cost=round(u["cost"] + c["repair_cost"], 3),
                        validator_errors=c["validator_errors"], ledger_findings=c["ledger_findings"],
                        new=c["families"].get("new", 0), reading_words=c["reading_words"])
        return (f"{ref}: done ${st.get('total_cost', 0):.2f} (estimate ${est:.2f}; in {st.get('in', 0):,} out "
                f"{st.get('out', 0):,}); "
                f"ledger {c['ledger_findings']} (new {st['new']}); reading {c['reading_words']} words; "
                f"verify {c['verify']}; repairs {c['repair_calls']} (${c['repair_cost']:.2f}), stripped {c['stripped']}")
    except (Exception, SystemExit) as e:  # noqa: BLE001 — the status records every failure; the run goes on
        set_status(ref, state="failed", error=f"{type(e).__name__}: {str(e)[-800:]}")
        return f"{ref}: FAILED {str(e)[-300:]}"
    finally:
        _HELD.discard(ref)
        (p["out"] / "lock").unlink(missing_ok=True)


# ---------------------------------------------------------------- surah pass
def surah_windows(s: int) -> list[tuple[int, int]]:
    n = I.surah_len(s)
    if n <= I.SHORT or not I.PERICOPES.exists():
        return [(1, n)]
    out = []
    for line in I.PERICOPES.read_text(encoding="utf-8").splitlines():
        d = json.loads(line)
        if d["surah"] == s:
            out.append((max(1, d["ayah_from"] - I.OVERLAP), min(n, d["ayah_to"] + I.OVERLAP)))
    return out or [(1, n)]


def chains(s: int, win: tuple[int, int] | None = None) -> str:
    n = I.surah_len(s)
    lo, hi = win or (1, n)
    refs = [f"{s}:{a}" for a in range(lo, hi + 1)]
    out = surah_out(s, (lo, hi))
    out.mkdir(parents=True, exist_ok=True)
    ledgers = [paths(r)["out"] / f"{paths(r)['sa']}.ledger.md" for r in refs]
    missing = [r for r, l in zip(refs, ledgers) if not l.exists()]
    if missing:
        return f"surah {s} {lo}-{hi}: waiting for ledgers {', '.join(missing)}"
    records = I.hft_records(refs)
    files = {"hft.md": I.hft_window(records), "channels.md": I.channels(s, refs=None if (lo, hi) == (1, n) else refs),
             "branch_table.md": I.branch_table(refs, title=f"# branch_table.md — every branch of every root in "
                                                           f"{s}:{lo}–{hi}")}
    I.deliver(["window", f"{s}:{lo}-{hi}"], out / "usage.md")
    for name, text in files.items():
        if text.strip():
            (out / name).write_text(text, encoding="utf-8")
    ev = [paths(refs[0])["v9w"] / "context.md"] + [out / x for x in ("channels.md", "hft.md", "branch_table.md",
                                                                      "usage.md") if (out / x).exists()]
    stdin = inline(*ev, *ledgers, V12 / "prompts" / "surah.md")
    prompt = (f"Surah {s}, ayat {lo}–{hi}. The evidence comes first ({', '.join(f.name for f in ev)}, then the ledger "
              f"of every ayah); the brief (surah.md) is last. Follow it exactly and return the three parts with their "
              f"marker lines.")
    est = estimate(len((prompt + stdin).encode()), SURAH_OUT)
    if est >= MAX_COST:
        (out / "check.txt").write_text(json.dumps({"failed": f"not started: estimated ${est:.2f} >= ${MAX_COST:.2f}",
                                                   "estimate": est}) + "\n", encoding="utf-8")
        return f"surah {s} {lo}-{hi}: NOT STARTED (estimated ${est:.2f} ≥ ${MAX_COST:.2f}; raise --max-cost to run it)"
    final, u = opus(prompt, stdin, out / "run.log.jsonl")
    total = u["cost"]
    (out / "final.txt").write_text(final, encoding="utf-8")
    a, _, rest = final.partition("===== SURAH =====")
    b, _, c = rest.partition("===== AYAT =====")
    if not ("===== CHAINS =====" in a and len(b.split()) >= 400 and c.strip()):
        (out / "check.txt").write_text(json.dumps({"failed": "no usable answer (no retry, by rule)", "estimate": est,
                                                   "cost": round(total, 3)}) + "\n", encoding="utf-8")
        return f"surah {s} {lo}-{hi}: FAILED (no usable answer; see {out}/final.txt)"
    (out / "chains.md").write_text(a.split("===== CHAINS =====", 1)[-1].strip() + "\n", encoding="utf-8")
    reading = out / f"{s}.surah.tr.md"
    reading.write_text(b.strip() + "\n", encoding="utf-8")
    (out / "ayat.md").write_text(c.strip() + "\n", encoding="utf-8")
    res = check_text(reading, out / "repair.log.jsonl")
    nch = sum(1 for l in (out / "chains.md").read_text(encoding="utf-8").splitlines() if l.startswith("### "))
    res.update(estimate=est, cost=round(total + res["repair_cost"], 3), chains=nch, words=len(reading.read_text(encoding="utf-8").split()),
               input_bytes=sum(f.stat().st_size for f in ev + ledgers))
    (out / "check.txt").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for r in refs:
        if done(r):
            render(r)
    return (f"surah {s} {lo}-{hi}: ${total:.2f}; chains {nch}; reading {res['words']} words; verify {res['verify']}; "
            f"repairs {res['repair_calls']}, stripped {res['stripped']}")


def status(s: int) -> str:
    rows = []
    for r in surah_refs(s):
        d = get_status(r)
        rows.append(f"{r}\t{d.get('state')}\t${d.get('total_cost', d.get('cost', 0)):.2f} (est ${d.get('estimate', 0):.2f})\t"
                    f"in {d.get('in', 0):,}\tout {d.get('out', 0):,}\t"
                    f"{d.get('verify', '')}\tstripped {d.get('stripped', '')}\t{d.get('error', '')[:120]}")
    for f in sorted((OUT / f"s{s:03d}" / "surah").glob("*/check.txt")):
        d = json.loads(f.read_text(encoding="utf-8"))
        rows.append(f"surah {f.parent.name}\t{'FAILED ' + d['failed'] if d.get('failed') else 'done'}\t"
                    f"${d.get('cost', 0):.2f}\tchains {d.get('chains', '-')}\t{d.get('verify', '')}")
    return "\n".join(rows)


def main() -> None:
    global EFFORT, MAX_COST, FORCE, USAGE, OUT
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=("prep", "write", "check", "render", "ayah", "surah", "chains", "status"))
    ap.add_argument("ref", help="S:A (comma-separated for several), or a surah number")
    ap.add_argument("--parallel", type=int, default=4)
    ap.add_argument("--effort", default="high", choices=("high", "xhigh", "max"))
    ap.add_argument("--max-cost", type=float, default=5.0)
    ap.add_argument("--window", help="chains: LO-HI (default: the whole surah, or every passage window)")
    ap.add_argument("--no-chains", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--no-usage", action="store_true", help="leave usage.md (root dossiers) out of the evidence")
    ap.add_argument("--tag", help="write to out-TAG/ instead of out/ (arms, e.g. --tag nousage)")
    ap.add_argument("--estimate", action="store_true", help="ayah/surah: print the cost estimate per ayah and exit")
    a = ap.parse_args()
    EFFORT, MAX_COST, FORCE, USAGE = a.effort, a.max_cost, a.force, not a.no_usage
    if a.tag:
        OUT = V12 / f"out-{a.tag}"
    if a.step == "status":
        print(status(int(a.ref)))
        return
    if a.step == "chains":
        s = int(a.ref)
        wins = [tuple(int(x) for x in a.window.split("-"))] if a.window else surah_windows(s)
        for w in wins:
            print(chains(s, w), flush=True)
        return
    if a.step in ("prep", "write", "check", "render"):
        for r in a.ref.split(","):
            fn = {"prep": prep, "write": write, "check": check, "render": render}[a.step]
            print(r, json.dumps(fn(r), ensure_ascii=False, default=str)[:600] if a.step != "render" else fn(r) or "rendered")
        return
    refs = list(dict.fromkeys(a.ref.split(","))) if a.step == "ayah" else surah_refs(int(a.ref))
    for r in refs:  # scripts first, sequentially (shared caches), so the parallel writers start at once
        if FORCE or not done(r):
            prep(r)
    if a.estimate:
        tpb, exp = calibration()
        for r in refs:
            nb = sum(f.stat().st_size for f in evidence(r) + [V12 / "prompts" / "write.md"])
            print(f"{r}\t{nb:,} bytes\t${estimate(nb):.2f}", flush=True)
        print(f"(tokens/byte {tpb:.2f}; expected output {exp.get(EFFORT):,.0f} tokens at effort {EFFORT}; limit "
              f"${MAX_COST:.2f})")
        return
    with ThreadPoolExecutor(a.parallel) as pool:
        for line in pool.map(lambda r: ayah(r, prepped=True), refs):
            print(line, flush=True)
    if a.step == "surah" and not a.no_chains:
        s = int(a.ref)
        if all(done(r) for r in refs):
            for w in surah_windows(s):
                print(chains(s, w), flush=True)
        else:
            print(f"surah {s}: chains pass not run (not every ayah is done; rerun the same command)", flush=True)


if __name__ == "__main__":
    main()
