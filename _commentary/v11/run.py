#!/usr/bin/env python3
"""V11: one ayah → one Opus call → reading + findings ledger → four chapters. See README.md.

  prep    scripts only (no model): V9 input package (prepare.py), context.md (luna/worklists.py), usage worklists
          (lines/candidates.py), script digest of Quranic reach (lines/digest.py: qirāʾāt, usage refs, inter-ayah)
  write   one Opus call (effort high, no tools, no MCP): evidence first — context.md, 01_dictionary.md, digest.md —
          and the brief last (prompts/write.md); returns the ledger, then the reading
  check   verify every Arabic quotation (verify_ar --fix: Quran text and the dictionary), validate the reading's tags,
          mechanical tag repair (commas inside tr), ledger/reading metrics
  render  chapters: S_A.md = reading + "Kur'an'ı Kur'an'la" (ledger Surah/Quran/Fatiha, each ref with its ayah text)
          + "Kelimeler ve okuyuşlar" (ledger Dictionary/Readings)
  all     prep → write → check → render

Outputs: _commentary/v11/out/sNNN/S_A/ (S_A.reading.tr.md, S_A.ledger.md, S_A.md, run.log.jsonl, check.txt).
Usage: python3 _commentary/v11/run.py all 100:1
       python3 _commentary/v11/run.py surah 100 [--parallel 6]   (all ayat of a surah: all steps)
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

V11 = Path(__file__).resolve().parent
REPO = V11.parents[1]
V9 = REPO / "_commentary" / "v9"
PY = sys.executable
SYSTEM = ("You are a careful scholar of Quranic Arabic and a fine Turkish prose writer. Follow the brief at the end of "
          "the user message exactly and return only the requested output.")
sys.path.insert(0, str(V9))
from verify_ar import QURAN_TEXT  # noqa: E402


def paths(ref: str) -> dict:
    s, a = (int(x) for x in ref.split(":"))
    sa = f"{s}_{a}"
    return {"sa": sa, "pkg": V9 / "input" / "v2" / f"s{s:03d}" / sa, "work": V9 / "lines" / "work" / sa,
            "out": V11 / "out" / f"s{s:03d}" / sa}


def sh(*args: str) -> str:
    r = subprocess.run([PY, *args], capture_output=True, text=True, cwd=REPO)
    if r.returncode:
        sys.exit(f"failed: {args}\n{(r.stdout + r.stderr)[-1500:]}")
    return r.stdout


def prep(ref: str) -> None:
    p = paths(ref)
    if not (p["pkg"] / "01_dictionary.md").exists():
        sh(str(V9 / "prepare.py"), "--ayah", ref, "--out", str(p["pkg"]))
    if not (V9 / "luna" / "work" / p["sa"] / "context.md").exists():
        sh(str(V9 / "luna" / "worklists.py"), str(p["pkg"]), str(V9 / "luna" / "work" / p["sa"]))
    if not (p["work"] / "items.tsv").exists():
        sh(str(V9 / "lines" / "candidates.py"), ref)
    sh(str(V9 / "lines" / "digest.py"), ref)


def inline(*files: Path) -> str:
    return "\n\n".join(f"===== {f.name} =====\n{f.read_text(encoding='utf-8')}" for f in files)


def write(ref: str) -> None:
    p = paths(ref)
    p["out"].mkdir(parents=True, exist_ok=True)
    stdin = inline(p["work"] / "context.md", p["pkg"] / "01_dictionary.md", p["work"] / "digest.md",
                   V11 / "prompts" / "write.md")
    prompt = (f"Focus: {ref}. The evidence comes first (context.md, 01_dictionary.md, digest.md); the brief (write.md) "
              f"is last. Follow the brief exactly and return the ledger and the reading with their marker lines.")
    r = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", "", "--strict-mcp-config",
                        "--output-format", "stream-json", "--verbose", "--no-session-persistence",
                        "--system-prompt", SYSTEM],
                       input=prompt + "\n\n" + stdin, capture_output=True, text=True, cwd=REPO)
    (p["out"] / "run.log.jsonl").write_text(r.stdout or json.dumps({"error": r.stderr[-3000:]}), encoding="utf-8")
    # every assistant text block, in order (a long answer can span several messages)
    text = []
    for line in (r.stdout or "").splitlines():
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        if d.get("type") == "assistant":
            text += [b.get("text", "") for b in d["message"].get("content", []) if b.get("type") == "text"]
    final = "\n".join(text)
    (p["out"] / "final.txt").write_text(final, encoding="utf-8")
    ledger, _, reading = final.partition("===== READING =====")
    ledger = ledger.split("===== LEDGER =====", 1)[-1]
    if len(reading.split()) < 300:
        sys.exit(f"{ref}: no reading (see {p['out'] / 'final.txt'})")
    (p["out"] / f"{p['sa']}.ledger.md").write_text(ledger.strip() + "\n", encoding="utf-8")
    (p["out"] / f"{p['sa']}.reading.tr.md").write_text(reading.strip() + "\n", encoding="utf-8")


def repair_tags(path: Path) -> int:
    """Mechanical: drop commas inside tr (and inside ar), which break the three-field tag format."""
    text = path.read_text(encoding="utf-8")
    n = 0

    def fix(m: re.Match) -> str:
        nonlocal n
        ar, tr, gloss = m.group(1), m.group(2), m.group(3)
        ar2, tr2 = ar.replace("،", "").replace(",", ""), tr.replace(",", "")
        n += (ar2 != ar) + (tr2 != tr)
        return f"{{ar:{ar2}, tr:{tr2}, gloss:{gloss}}}"

    text = re.sub(r"\{ar:(.*?), tr:(.*?), gloss:([^{}]*?)\}", fix, text)
    path.write_text(text, encoding="utf-8")
    return n


def check(ref: str) -> str:
    p = paths(ref)
    reading = p["out"] / f"{p['sa']}.reading.tr.md"
    fixed = repair_tags(reading)
    v = subprocess.run([PY, str(V9 / "verify_ar.py"), str(reading), str(p["pkg"]), "--fix"],
                       capture_output=True, text=True, cwd=REPO).stdout
    val = subprocess.run([PY, str(REPO / "_commentary" / "v5" / "validate_prose.py"), str(reading)],
                         capture_output=True, text=True, cwd=REPO).stdout
    errors = [l for l in val.splitlines() if ": error:" in l]
    ledger = (p["out"] / f"{p['sa']}.ledger.md").read_text(encoding="utf-8")
    body = reading.read_text(encoding="utf-8")
    cost = usage = ""
    for line in (p["out"] / "run.log.jsonl").read_text(encoding="utf-8").splitlines():
        if '"type":"result"' in line.replace(" ", ""):
            d = json.loads(line)
            u = d.get("usage", {})
            cost = f"${d.get('total_cost_usd', 0):.2f}"
            usage = f"in {u.get('input_tokens', 0) + u.get('cache_creation_input_tokens', 0) + u.get('cache_read_input_tokens', 0):,} out {u.get('output_tokens', 0):,}"
    summary = (f"{ref}: {cost} ({usage}); ledger {sum(1 for l in ledger.splitlines() if l.startswith('- '))} findings, "
               f"{len(set(re.findall(r'\b\d{1,3}:\d{1,3}\b', ledger)))} refs; reading {len(body.split())} words, "
               f"{len(set(re.findall(r'\b\d{1,3}:\d{1,3}\b', body)))} refs; tag repairs {fixed}; "
               f"verify: {v.strip().splitlines()[-1] if v.strip() else '?'}; validator errors {len(errors)}")
    (p["out"] / "check.txt").write_text(summary + "\n\n" + v + "\n" + "\n".join(errors) + "\n", encoding="utf-8")
    return summary


def quran() -> dict[str, str]:
    q = {}
    for line in QURAN_TEXT.read_text(encoding="utf-8-sig").splitlines():
        r, _, t = line.partition("|")
        q[r.strip()] = t.strip()
    return q


def render(ref: str) -> None:
    p = paths(ref)
    q = quran()
    ledger = (p["out"] / f"{p['sa']}.ledger.md").read_text(encoding="utf-8")
    fam, current = {}, None
    for line in ledger.splitlines():
        if line.startswith("### "):
            current = line[4:].strip().lower()
            fam[current] = []
        elif line.startswith("- ") and current:
            fam[current].append(line)

    def entries(names: tuple[str, ...], with_text: bool) -> list[str]:
        out, shown = [], set()
        for name in names:
            for key, lines in fam.items():
                if not key.startswith(name):
                    continue
                for line in lines:
                    m = re.match(r"- \[refs:\s*([^|\]]*)\|[^|\]]*\|\s*(\w+)\s*\]\s*(.*)", line)
                    refs = [r.strip() for r in m.group(1).split(",") if r.strip()] if m else []
                    grade, text = (m.group(2), m.group(3)) if m else ("", line[2:])
                    out.append(f"- **{', '.join(refs) or '—'}** ({grade}) {text}")
                    if with_text:
                        for r in refs:
                            if r in q and r not in shown and r != ref:
                                shown.add(r)
                                out.append(f"  - {r} {q[r]}")
        return out

    reading = (p["out"] / f"{p['sa']}.reading.tr.md").read_text(encoding="utf-8").strip()
    doc = [reading, "", "---", "", "## Kur'an'ı Kur'an'la", "",
           "Sure içinden ve Kur'an'ın geri kalanından bu ayeti açan yerler: her biri, ne iş gördüğüyle.", ""]
    doc += entries(("surah", "quran", "fatiha"), True)
    doc += ["", "## Kelimeler ve okuyuşlar", ""] + entries(("dictionary", "readings"), False)
    (p["out"] / f"{p['sa']}.md").write_text("\n".join(doc) + "\n", encoding="utf-8")


def one(ref: str, step: str) -> str:
    if step in ("prep", "all"):
        prep(ref)
    if step in ("write", "all"):
        write(ref)
    msg = ""
    if step in ("check", "all"):
        msg = check(ref)
    if step in ("render", "all"):
        render(ref)
    return msg or f"{ref}: {step} done"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=("prep", "write", "check", "render", "all", "surah"))
    ap.add_argument("ref", help="S:A, or a surah number with the step 'surah'")
    ap.add_argument("--parallel", type=int, default=6)
    a = ap.parse_args()
    if a.step != "surah":
        print(one(a.ref, a.step), flush=True)
        return
    s = int(a.ref)
    refs = [r for r in quran() if r.startswith(f"{s}:") and not r.endswith(":0")]
    for r in refs:  # scripts first, sequentially (shared caches)
        prep(r)
    def safe_write(r: str) -> str:
        if (paths(r)["out"] / f"{paths(r)['sa']}.reading.tr.md").exists():
            return "exists"
        try:
            write(r)
            return "ok"
        except SystemExit as e:
            return str(e)

    with ThreadPoolExecutor(a.parallel) as pool:
        status = dict(zip(refs, pool.map(safe_write, refs)))
    for r in refs:
        if status[r] in ("ok", "exists"):
            print(check(r), flush=True)
            render(r)
        else:
            print(f"{r}: {status[r]}", flush=True)


if __name__ == "__main__":
    main()
