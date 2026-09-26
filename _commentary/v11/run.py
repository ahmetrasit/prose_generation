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
  chains  whole-surah pass (after all ayat): the surah text + every ledger → chains across ayat, a reading of the
          whole surah, one note per ayah (added to each S_A.md as "Surenin bütününde")

  seeds   (arms S/S0) whole-surah seed pass before the ayah writers: seeds_input.py (branch table, HFT, surface
          staging, definitional links) + prompts/seeds.md → out/arms/<arm>/sNNN/seeds/<window>/{seeds.md,ayat.md}

Arms (--arm; REVIEW.md §5): B = the v11 baseline (prompts/write.md, surah.md; outputs in out/sNNN/);
  D = digest v2 (reasons per related passage) + prompts/write_s.md (Limits, source tags); S = seeds + D +
  prompts/surah_s.md for the chains pass; S0 = S without HFT in the seed input. Non-B outputs: out/arms/<arm>/sNNN/.
Outputs: _commentary/v11/out/sNNN/S_A/ (S_A.reading.tr.md, S_A.ledger.md, S_A.md, run.log.jsonl, check.txt).
Usage: python3 _commentary/v11/run.py all 100:1
       python3 _commentary/v11/run.py surah 100 [--parallel 6]   (all ayat of a surah, then the chains pass)
       python3 _commentary/v11/run.py seeds 1 --arm S ; python3 _commentary/v11/run.py surah 1 --arm S
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter
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


ARM = "B"  # set by main(); REVIEW.md §5


def root_out(surah: int) -> Path:
    return (V11 / "out" if ARM == "B" else V11 / "out" / "arms" / ARM) / f"s{surah:03d}"


def paths(ref: str) -> dict:
    s, a = (int(x) for x in ref.split(":"))
    sa = f"{s}_{a}"
    return {"sa": sa, "pkg": V9 / "input" / "v2" / f"s{s:03d}" / sa, "work": V9 / "lines" / "work" / sa,
            "out": root_out(s) / sa}


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
    if ARM != "B":
        sh(str(V9 / "lines" / "digest.py"), ref, "--v2")


def seed_sheets(surah: int) -> list[Path]:
    return sorted((root_out(surah) / "seeds").glob("*/seeds.md"))


def seeds_for(ref: str) -> str:
    """The seed systems with a member in this ayah, and the seed pass's note for it (from every window)."""
    out, cited = [], []
    for sheet in seed_sheets(int(ref.split(":")[0])):
        blocks = re.split(r"(?m)^(?=### )", sheet.read_text(encoding="utf-8"))
        for b in blocks:
            members = re.search(r"(?ms)^- members:(.*?)(?=^- \w+:|\Z)", b)  # wrapped member lists too
            if b.startswith("### ") and members and re.search(rf"(?<![\d:]){re.escape(ref)}(?!\d)", members.group(1)):
                out.append(b.strip())
                cited += re.findall(r"([\u0621-\u064a](?: [\u0621-\u064a]){1,4}) (B\d{3})", members.group(1))
        notes = sheet.with_name("ayat.md")
        if notes.exists():
            out += [l for l in notes.read_text(encoding="utf-8").splitlines() if re.match(rf"-\s*\**{re.escape(ref)}\b", l)]
    # the branch-table lines of every cited member (Arabic image and source phrase), so the writer can quote them
    table = {}
    for f in (root_out(int(ref.split(":")[0])) / "seeds").glob("*/seeds_input.md"):
        root = None
        for line in f.read_text(encoding="utf-8").splitlines():
            if line.startswith("## ") and not line.startswith("## a."):
                root = None
            m = re.match(r"### ([\u0621-\u064a](?: [\u0621-\u064a]){1,4})(?: ~\w+)? — ", line)
            if m:
                root = m.group(1)
            m = re.match(r"- (B\d{3}) ", line)
            if root and m:
                table.setdefault((root, m.group(1)), f"- {root} {line[2:]}")
    lines = [table[k] for k in dict.fromkeys(cited) if k in table]
    if lines:
        out.append("Branch lines of the cited members (Arabic you may quote, with `source: root Bnnn`):\n" + "\n".join(lines))
    return "\n\n".join(dict.fromkeys(out))


def seeds(surah: int, no_hft: bool) -> str:
    """Seed pass (arms S/S0): one Opus call per window over the script-built seed input."""
    args = [str(V11 / "seeds_input.py"), str(surah), "--arm", ARM] + (["--no-hft"] if no_hft else [])
    made = [Path(l.split(" (")[0]) for l in sh(*args).splitlines() if l.strip()]
    msgs = []
    for f in made:
        out = f.parent
        final = opus(f"Surah {surah}, window {out.name}. The evidence comes first (seeds_input.md); the brief "
                     f"(seeds.md) is last. Follow it exactly and return both parts with their marker lines.",
                     inline(f, V11 / "prompts" / "seeds.md"), out / "run.log.jsonl")
        (out / "final.txt").write_text(final, encoding="utf-8")
        a, _, b = final.partition("===== AYAT =====")
        (out / "seeds.md").write_text(a.split("===== SEEDS =====", 1)[-1].strip() + "\n", encoding="utf-8")
        (out / "ayat.md").write_text(b.strip() + "\n", encoding="utf-8")
        sheet = (out / "seeds.md").read_text(encoding="utf-8")
        mat = Counter(m.strip() for m in re.findall(r"(?m)^- maturity:\s*(\w+)", sheet))
        msg = (f"seeds {surah} {out.name}: {cost_of(out / 'run.log.jsonl')}; systems "
               f"{sum(1 for l in sheet.splitlines() if l.startswith('### '))} ({dict(mat)})")
        (out / "check.txt").write_text(msg + "\n", encoding="utf-8")
        msgs.append(msg)
    return "\n".join(msgs)


def inline(*files: Path) -> str:
    return "\n\n".join(f"===== {f.name} =====\n{f.read_text(encoding='utf-8')}" for f in files)


def write(ref: str) -> None:
    p = paths(ref)
    p["out"].mkdir(parents=True, exist_ok=True)
    if ARM == "B":
        files = [p["work"] / "context.md", p["pkg"] / "01_dictionary.md", p["work"] / "digest.md",
                 V11 / "prompts" / "write.md"]
    else:
        files = [p["work"] / "context.md", p["pkg"] / "01_dictionary.md", p["work"] / "digest_v2.md"]
        if ARM in ("S", "S0"):
            sd = seeds_for(ref)
            (p["out"] / "seeds.md").write_text((sd or "(no seed system passes through this ayah)") + "\n", encoding="utf-8")
            files.append(p["out"] / "seeds.md")
        files.append(V11 / "prompts" / "write_s.md")
    stdin = inline(*files)
    prompt = (f"Focus: {ref}. The evidence comes first ({', '.join(f.name for f in files[:-1])}); the brief "
              f"({files[-1].name}) is last. Follow the brief exactly and return the ledger and the reading with their "
              f"marker lines.")
    final = opus(prompt, stdin, p["out"] / "run.log.jsonl")
    (p["out"] / "final.txt").write_text(final, encoding="utf-8")
    ledger, _, reading = final.partition("===== READING =====")
    ledger = ledger.split("===== LEDGER =====", 1)[-1]
    if len(reading.split()) < 300:
        sys.exit(f"{ref}: no reading (see {p['out'] / 'final.txt'})")
    (p["out"] / f"{p['sa']}.ledger.md").write_text(ledger.strip() + "\n", encoding="utf-8")
    (p["out"] / f"{p['sa']}.reading.tr.md").write_text(reading.strip() + "\n", encoding="utf-8")


def opus(prompt: str, stdin: str, log: Path) -> str:
    """One Opus call (effort high, no tools, no MCP); every assistant text block, in order."""
    r = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", "", "--strict-mcp-config",
                        "--output-format", "stream-json", "--verbose", "--no-session-persistence",
                        "--system-prompt", SYSTEM],
                       input=prompt + "\n\n" + stdin, capture_output=True, text=True, cwd=REPO,
                       env={**os.environ, "CLAUDE_CODE_MAX_OUTPUT_TOKENS": "128000"})  # no CLI "output limit hit" resume
    log.write_text(r.stdout or json.dumps({"error": r.stderr[-3000:]}), encoding="utf-8")
    text = []
    for line in (r.stdout or "").splitlines():
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        if d.get("type") == "assistant":
            text += [b.get("text", "") for b in d["message"].get("content", []) if b.get("type") == "text"]
    return "\n".join(text)


def cost_of(log: Path) -> str:
    for line in log.read_text(encoding="utf-8").splitlines():
        if '"type":"result"' in line.replace(" ", ""):
            d = json.loads(line)
            u = d.get("usage", {})
            return (f"${d.get('total_cost_usd', 0):.2f} (in {u.get('input_tokens', 0) + u.get('cache_creation_input_tokens', 0) + u.get('cache_read_input_tokens', 0):,} "
                    f"out {u.get('output_tokens', 0):,})")
    return "?"


def chains(surah: int) -> str:
    """Whole-surah pass: the surah text + every ayah ledger → chains across ayat, the surah's reading, per-ayah notes."""
    refs = [r for r in quran() if r.startswith(f"{surah}:") and not r.endswith(":0")]
    first = paths(refs[0])
    out = root_out(surah) / "surah"
    out.mkdir(parents=True, exist_ok=True)
    ledgers = [paths(r)["out"] / f"{paths(r)['sa']}.ledger.md" for r in refs]
    missing = [str(l) for l in ledgers if not l.exists()]
    if missing:
        sys.exit(f"missing ledgers: {missing}")
    if ARM in ("S", "S0"):
        table = out / "branch_table.md"
        tables = []
        for f in sorted((root_out(surah) / "seeds").glob("*/seeds_input.md")):
            t = f.read_text(encoding="utf-8")
            tables.append(t[t.index("## a. Branch table"):t.index("\n## ", t.index("## a. Branch table") + 5)])
        table.write_text("\n\n".join(tables) + "\n", encoding="utf-8")
        files = [first["work"] / "context.md", table, *seed_sheets(surah), *ledgers, V11 / "prompts" / "surah_s.md"]
    else:
        files = [first["work"] / "context.md", *ledgers, V11 / "prompts" / "surah.md"]
    stdin = inline(*files)
    final = opus(f"Surah {surah}. The evidence comes first ({', '.join(dict.fromkeys(f.name for f in files[:-1]))}); "
                 f"the brief ({files[-1].name}) is last. Follow it exactly and return the three parts with their "
                 f"marker lines.", stdin, out / "run.log.jsonl")
    (out / "final.txt").write_text(final, encoding="utf-8")
    a, _, rest = final.partition("===== SURAH =====")
    b, _, c = rest.partition("===== AYAT =====")
    (out / "chains.md").write_text(a.split("===== CHAINS =====", 1)[-1].strip() + "\n", encoding="utf-8")
    (out / f"{surah}.surah.tr.md").write_text(b.strip() + "\n", encoding="utf-8")
    (out / "ayat.md").write_text(c.strip() + "\n", encoding="utf-8")
    v = verify(out / f"{surah}.surah.tr.md", first["pkg"])
    n = sum(1 for l in (out / "chains.md").read_text(encoding="utf-8").splitlines() if l.startswith("### "))
    msg = (f"surah {surah}: {cost_of(out / 'run.log.jsonl')}; chains {n}; surah reading "
           f"{len((out / f'{surah}.surah.tr.md').read_text(encoding='utf-8').split())} words; verify: "
           f"{next((l for l in v.splitlines() if 'exact=' in l), '?')}")
    (out / "check.txt").write_text(msg + "\n\n" + v, encoding="utf-8")
    for r in refs:
        render(r)
    return msg


def verify(reading: Path, pkg: Path) -> str:
    """B: verify_ar (quote anywhere in package or Quran); other arms: verify_src (quote in its declared source)."""
    cmd = ([PY, str(V9 / "verify_ar.py"), str(reading), str(pkg), "--fix"] if ARM == "B" else
           [PY, str(V11 / "verify_src.py"), str(reading), "--fix"])
    return subprocess.run(cmd, capture_output=True, text=True, cwd=REPO).stdout


def repair_tags(path: Path) -> int:
    """Mechanical: drop commas inside tr (and inside ar), which break the tag format; a source field is kept."""
    text = path.read_text(encoding="utf-8")
    n = 0

    def fix(m: re.Match) -> str:
        nonlocal n
        ar, tr, gloss, src = m.group(1), m.group(2), m.group(3), m.group(4)
        ar2, tr2 = ar.replace("،", "").replace(",", ""), tr.replace(",", "")
        n += (ar2 != ar) + (tr2 != tr)
        return f"{{ar:{ar2}, tr:{tr2}, gloss:{gloss}" + (f", source:{src}" if src is not None else "") + "}"

    text = re.sub(r"\{ar:(.*?), tr:(.*?), gloss:([^{}]*?)(?:, source:([^{}]*))?\}", fix, text)
    path.write_text(text, encoding="utf-8")
    return n


def check(ref: str) -> str:
    p = paths(ref)
    reading = p["out"] / f"{p['sa']}.reading.tr.md"
    fixed = repair_tags(reading)
    v = verify(reading, p["pkg"])
    probe = reading
    if ARM != "B":  # the frozen v5 validator knows three fields: validate a copy without the source field
        probe = p["out"] / "validate.tmp.md"
        probe.write_text(re.sub(r"(\{ar:[^{}]*?gloss:[^{}]*?), source:[^{}]*\}", r"\1}",
                                reading.read_text(encoding="utf-8")), encoding="utf-8")
    val = subprocess.run([PY, str(REPO / "_commentary" / "v5" / "validate_prose.py"), str(probe)],
                         capture_output=True, text=True, cwd=REPO).stdout
    if probe != reading:
        probe.unlink()
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
               f"verify: {next((l for l in v.splitlines() if 'exact=' in l), '?')}; validator errors {len(errors)}")
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
                    out.append(f"- **{', '.join(refs) or '—'}** ({grade}) {text}{pointers(refs) if ARM != 'B' else ''}")
                    if with_text:
                        for r in refs:
                            if r in q and r not in shown and r != ref:
                                shown.add(r)
                                out.append(f"  - {r} {q[r]}")
        return out

    reading = (p["out"] / f"{p['sa']}.reading.tr.md").read_text(encoding="utf-8").strip()
    paras = [x for x in re.split(r"\n\s*\n", reading) if x.strip() and not x.lstrip().startswith("#")]

    def pointers(refs: list[str]) -> str:  # reading paragraphs that cite these refs (script; REVIEW.md R5)
        refs = [r for r in refs if r != ref]
        hit = [str(i + 1) for i, x in enumerate(paras) if any(re.search(rf"(?<![\d:]){re.escape(r)}(?![\d])", x) for r in refs)]
        return f" [¶ {', '.join(hit)}]" if hit else ""
    doc = [reading, "", "---", "", "## Kur'an'ı Kur'an'la", "",
           "Sure içinden ve Kur'an'ın geri kalanından bu ayeti açan yerler: her biri, ne iş gördüğüyle.", ""]
    doc += entries(("surah", "quran", "limits", "fatiha"), True)
    doc += ["", "## Kelimeler ve okuyuşlar", ""] + entries(("dictionary", "readings"), False)
    notes = root_out(int(ref.split(':')[0])) / "surah" / "ayat.md"
    if notes.exists():
        mine = [l for l in notes.read_text(encoding="utf-8").splitlines() if re.match(rf"-\s*\**{re.escape(ref)}\b", l)]
        if mine:
            doc += ["", "## Surenin bütününde", ""] + [re.sub(rf"^-\s*\**{re.escape(ref)}\**:?\s*", "", m) for m in mine]
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
    ap.add_argument("step", choices=("prep", "write", "check", "render", "all", "surah", "chains", "seeds"))
    ap.add_argument("ref", help="S:A, or a surah number with the step 'surah'")
    ap.add_argument("--parallel", type=int, default=6)
    ap.add_argument("--arm", default="B", choices=("B", "D", "S", "S0", "Srep"))
    ap.add_argument("--no-hft", action="store_true", help="seeds: leave the HFT hypotheses out (arm S0)")
    ap.add_argument("--no-chains", action="store_true", help="surah: skip the chains pass")
    a = ap.parse_args()
    global ARM
    ARM = a.arm
    if a.step == "seeds":
        print(seeds(int(a.ref), a.no_hft or a.arm == "S0"), flush=True)
        return
    if a.step == "chains":
        print(chains(int(a.ref)), flush=True)
        return
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
    if not a.no_chains and all(status[r] in ("ok", "exists") for r in refs):
        print(chains(s), flush=True)


if __name__ == "__main__":
    main()
