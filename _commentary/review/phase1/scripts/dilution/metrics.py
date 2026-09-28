#!/usr/bin/env python3
"""Read-only mechanical metrics: input size vs output for every reading of the 17 cold-arm ayat.

Writes metrics.tsv, overlaps.tsv, q2a_branches.tsv, q2a_summary.tsv into this script's directory.
No model calls; reads local files only.
"""
from __future__ import annotations

import itertools
import json
import os
import re
import statistics
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path("/Volumes/OZTURK/_projects/prose_generation")
C = ROOT / "_commentary"
V9 = C / "v9"
QURAN = Path("/Volumes/OZTURK/_projects/quran-data/data/text/quran-uthmani.tsv")
COUNTS = Path("/Volumes/OZTURK/_projects/quran-slm/resources/source/quran_ayah_counts.tsv")

AYAT = ["1:1", "1:2", "1:3", "1:4", "1:5", "1:6", "1:7", "4:34", "5:6", "18:86", "18:96",
        "100:1", "100:6", "100:10", "103:1", "103:2", "103:3"]

AYAH_COUNT = {}
for line in COUNTS.read_text().splitlines()[1:]:
    s, n = line.split("\t")
    AYAH_COUNT[int(s)] = int(n)


def sa(ref):
    s, a = ref.split(":")
    return f"{s}_{a}"


def sdir(ref):
    return f"s{int(ref.split(':')[0]):03d}"


# ------------------------------------------------------------------ text metrics
REF_RE = re.compile(r"(?<![\d.:/])(\d{1,3}):(\d{1,3})(?::\d{1,3})?(?:\s?[-–]\s?(\d{1,3}))?(?![\d])")
CONCISE_CIT = re.compile(r"\(\s*\d{1,3}:\d{1,3}\s*¶[^)]*\)")
AR_CHARS = re.compile(r"[؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿]")
TAG1 = re.compile(r"(?<!\{)\{ar:")
TAG2 = re.compile(r"\{\{ar:")


def refs_of(text, focus):
    text = CONCISE_CIT.sub(" ", text)
    out = set()
    for m in REF_RE.finditer(text):
        s, a, b = int(m.group(1)), int(m.group(2)), m.group(3)
        if s < 1 or s > 114 or a < 1 or a > AYAH_COUNT[s]:
            continue
        out.add((s, a))
        if b:
            b = int(b)
            if a < b <= AYAH_COUNT[s] and b - a <= 20:
                for x in range(a + 1, b + 1):
                    out.add((s, x))
    fs, fa = map(int, focus.split(":"))
    same = {r for r in out if r[0] == fs and r != (fs, fa)}
    other = {r for r in out if r[0] != fs}
    return out, same, other


def text_metrics(path, focus):
    t = path.read_text(encoding="utf-8", errors="replace")
    words = t.split()
    tr_words = [w for w in words if not AR_CHARS.search(w)]
    allr, same, other = refs_of(t, focus)
    fs, fa = map(int, focus.split(":"))
    paras = [p for p in re.split(r"\n\s*\n", t) if p.strip() and not p.strip().startswith("#")]
    return {
        "words": len(words), "tr_words": len(tr_words),
        "distinct_refs": len(allr), "same_surah_refs": len(same), "other_surah_refs": len(other),
        "focus_cited": int((fs, fa) in allr),
        "arabic_tags_single": len(TAG1.findall(t)), "arabic_tags_double": len(TAG2.findall(t)),
        "headings": len(re.findall(r"^#{1,6}\s", t, re.M)), "paragraphs": len(paras),
        "recall_marks": len(re.findall(r"\[recall\]|hafızadan", t, re.I)),
        "sozluk_mentions": len(re.findall(r"sözlü[kğ]", t, re.I)),
        "prose_bytes": len(t.encode("utf-8")),
        "_refs": allr - {(fs, fa)}, "_text": t,
    }


# ------------------------------------------------------------------ usage parsers
def claude_usage(path):
    """claude -p --output-format json (one object) or stream-json (last result line)."""
    res = None
    raw = path.read_text(encoding="utf-8", errors="replace")
    try:
        d = json.loads(raw)
        if isinstance(d, dict) and "usage" in d:
            res = d
    except json.JSONDecodeError:
        for line in raw.splitlines():
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(d, dict) and d.get("type") == "result":
                res = d
    if not res or "usage" not in res:
        return None
    u = res["usage"]
    th = (u.get("output_tokens_details") or {}).get("thinking_tokens")
    if th is None:
        for mu in (res.get("modelUsage") or {}).values():
            th = mu.get("thinkingTokens")
    return {"in": u.get("input_tokens", 0) or 0, "cache_write": u.get("cache_creation_input_tokens", 0) or 0,
            "cache_read": u.get("cache_read_input_tokens", 0) or 0, "out": u.get("output_tokens", 0) or 0,
            "thinking": th if th is not None else "", "cost": res.get("total_cost_usd"),
            "turns": res.get("num_turns"), "model": ",".join((res.get("modelUsage") or {}).keys())}


def codex_usage(paths):
    t = {"in": 0, "cached": 0, "out": 0, "reasoning": 0, "turns": 0}
    for p in paths:
        for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
            if not line.startswith("{"):
                continue
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            if d.get("type") == "turn.completed":
                u = d.get("usage") or {}
                t["turns"] += 1
                t["in"] += u.get("input_tokens", 0) or 0
                t["cached"] += u.get("cached_input_tokens", 0) or 0
                t["out"] += u.get("output_tokens", 0) or 0
                t["reasoning"] += u.get("reasoning_output_tokens", 0) or 0
    return t


def fsize(p):
    return p.stat().st_size if p.exists() else 0


def fchars(p):
    return len(p.read_text(encoding="utf-8", errors="replace")) if p.exists() else 0


rows = []


def add(ayah, run, version, model, reading, **kw):
    r = {"ayah": ayah, "run": run, "version": version, "model": model,
         "path": str(reading) if reading else ""}
    r.update(kw)
    if reading and Path(reading).exists():
        r.update(text_metrics(Path(reading), ayah))
        # upstream record next to the reading (ledger / record / act+qeq): distinct refs it holds
        d = Path(reading).parent
        sa_ = ayah.replace(":", "_")
        ups = [f for f in (d / f"{sa_}.ledger.md", d / "record.json", d / "act.md", d / "qeq.md") if f.exists()]
        if ups:
            allr = set()
            for f in ups:
                allr |= refs_of(f.read_text(encoding="utf-8", errors="replace"), ayah)[0]
            fs, fa = map(int, ayah.split(":"))
            allr.discard((fs, fa))
            r["upstream_refs"] = len(allr)
            r["upstream_only_refs"] = len(allr - r["_refs"])
            r["upstream_source"] = "+".join(f.name for f in ups)
        rend = d / f"{sa_}.md"
        if rend.exists():
            rt = rend.read_text(encoding="utf-8", errors="replace")
            rr = refs_of(rt, ayah)[0]
            r["rendered_md_words"] = len(rt.split())
            r["rendered_md_refs"] = len(rr - {tuple(map(int, ayah.split(":")))})
        tg = d / "commentary.tagged.tr.md"
        if tg.exists():
            t = tg.read_text(encoding="utf-8")
            srcs = {tuple(map(int, m.groups())) for m in re.finditer(r"src:(\d{1,3}):(\d{1,3})", t)}
            fs, fa = map(int, ayah.split(":"))
            srcs.discard((fs, fa))
            r["tagged_src_refs_not_in_prose"] = len(srcs - r["_refs"])
    rows.append(r)
    return r


# ------------------------------------------------------------------ v9 lines synth arms
W10 = V9 / "prompts" / "write_v10.md"
LEDGER_P = V9 / "prompts" / "write_ledger.md"
V11P = V9 / "prompts" / "write_v11.md"
SYNTH1 = V9 / "prompts" / "synth_one.md"
ARM_MODEL = {"w10-sol": "gpt-6-sol max", "w10-luna": "gpt-6-luna max", "sol1": "gpt-6-sol max",
             "sol2": "gpt-6-sol max (plan+write)", "sol56": "gpt-5.6-sol max", "opus1": "opus effort max"}


def v9_inputs(ref, arm):
    w = V9 / "lines" / "work" / sa(ref)
    dic = V9 / "input" / "v2" / sdir(ref) / sa(ref) / "01_dictionary.md"
    hft = dic.parent / "02_hft.md"
    m = {
        "w10-opus-cold": [W10, w / "context.md"], "w10-opus-cold2": [W10, w / "context.md"],
        "w10-opus-dict": [W10, w / "context.md", dic],
        "w10-opus-dslim": [W10, w / "context.md", dic, w / "package.slim.md"],
        "w10-opus-ledger": [LEDGER_P, W10, w / "context.md", dic, w / "package.slim.md"],
        "w10-opus-dhft": [W10, w / "context.md", dic, hft],
        "w10-opus": [W10, w / "context.md", w / "package.md"],
        "w10-sol": [W10, w / "context.md", w / "package.md"],
        "w10-luna": [W10, w / "context.md", w / "package.md"],
        "v11-script": [w / "context.md", dic, w / "digest.md", V11P],
        "v11-luna": [w / "context.md", dic, w / "package.slim.md", V11P],
        "opus1": [SYNTH1, w / "context.md", w / "package.md"],
        "sol1": [SYNTH1, w / "context.md", w / "package.md"],
    }
    return m.get(arm)


for ref in AYAT:
    sd = V9 / "lines" / "work" / sa(ref) / "synth"
    if not sd.exists():
        continue
    for armdir in sorted(p for p in sd.iterdir() if p.is_dir()):
        arm = armdir.name
        reading = armdir / f"{sa(ref)}.reading.tr.md"
        model = ARM_MODEL.get(arm, "claude-opus-5-5 effort high")
        notes = []
        kw = {}
        cl = armdir / "run.log.json"
        logs_jsonl = sorted(armdir.glob("*.log.jsonl"))
        run_mtime = None
        if cl.exists():
            u = claude_usage(cl)
            run_mtime = cl.stat().st_mtime
            if u:
                kw.update(input_tokens=u["in"], cache_write=u["cache_write"], cache_read=u["cache_read"],
                          output_tokens=u["out"], thinking_tokens=u["thinking"],
                          cost_usd=round(u["cost"], 4) if u["cost"] is not None else "", turns=u["turns"])
                kw["billed_input_total"] = u["in"] + u["cache_write"] + u["cache_read"]
        elif logs_jsonl:
            t = codex_usage(logs_jsonl)
            run_mtime = max(p.stat().st_mtime for p in logs_jsonl)
            kw.update(input_tokens=t["in"], cache_read=t["cached"], output_tokens=t["out"],
                      thinking_tokens=t["reasoning"], turns=t["turns"], cost_usd="",
                      billed_input_total=t["in"])
            notes.append("codex tokens (input includes cached); no rate recorded -> cost unknown")
        inp = v9_inputs(ref, arm)
        if inp:
            kw["input_bytes"] = sum(fsize(p) for p in inp)
            kw["input_chars"] = sum(fchars(p) for p in inp)
            kw["input_files"] = "+".join(p.name for p in inp)
            logf = cl if cl.exists() else (logs_jsonl[0] if logs_jsonl else None)
            if logf:
                import subprocess
                rc = subprocess.run(["git", "-C", str(ROOT), "log", "--diff-filter=A", "--format=%h", "--", str(logf)],
                                    capture_output=True, text=True).stdout.split()
                if rc:
                    commit = rc[-1]
                    kw["run_commit"] = commit
                    changed = [p.name for p in inp if subprocess.run(
                        ["git", "-C", str(ROOT), "diff", "--quiet", commit, "--", str(p)]).returncode != 0]
                    untracked = [n for n in changed if subprocess.run(
                        ["git", "-C", str(ROOT), "cat-file", "-e",
                         f"{commit}:" + str(next(p for p in inp if p.name == n).relative_to(ROOT))],
                        capture_output=True).returncode != 0]
                    changed = [n for n in changed if n not in untracked]
                    if changed:
                        notes.append(f"input file(s) differ from their state at run commit {commit}: " + ",".join(changed))
                    if untracked == ["write_v10.md"]:
                        notes.append("run predates write_v10.md (read the then-untracked v10/prompts/write.md; synth.py records the same md5 dddcd1b2)")
                    elif untracked:
                        notes.append("not in git at run commit: " + ",".join(untracked))
        else:
            notes.append("input composition not reconstructed")
        so = armdir / "stdout.txt"
        if so.exists():
            s = so.read_text(errors="replace")
            m = re.search(r"problems (\d+)", s)
            if m:
                kw["validator_problems"] = int(m.group(1))
        if not reading.exists():
            notes.append("no reading produced (final.txt only)")
            reading = None
        kw["notes"] = "; ".join(notes)
        add(ref, f"v9:{arm}", "v9-lines", model, reading, **kw)

# ------------------------------------------------------------------ v11/out
for ref in AYAT:
    d = C / "v11" / "out" / sdir(ref) / sa(ref)
    if not d.exists():
        continue
    kw = {}
    u = claude_usage(d / "run.log.jsonl")
    if u:
        kw.update(input_tokens=u["in"], cache_write=u["cache_write"], cache_read=u["cache_read"],
                  output_tokens=u["out"], thinking_tokens=u["thinking"], cost_usd=round(u["cost"], 4), turns=u["turns"],
                  billed_input_total=u["in"] + u["cache_write"] + u["cache_read"])
    ck = (d / "check.txt").read_text().splitlines()[0] if (d / "check.txt").exists() else ""
    m = re.search(r"ledger (\d+) findings, (\d+) refs", ck)
    kw["notes"] = f"check.txt: {ck[:160]}" + ("; surah chains pass is a separate shared call" if ref.startswith(("1:", "100:")) else "")
    if m:
        kw["ledger_findings"] = int(m.group(1))
    add(ref, "v11:out", "v11", "claude-opus-5-5 effort high", d / f"{sa(ref)}.reading.tr.md", **kw)

# ------------------------------------------------------------------ v12/out
for ref in AYAT:
    d = C / "v12" / "out" / sdir(ref) / sa(ref)
    if not d.exists():
        continue
    st = json.loads((d / "status.json").read_text())
    u = claude_usage(d / "run.log.jsonl")
    kw = {"input_bytes": st.get("input_bytes"), "cost_usd": st.get("total_cost", st.get("cost")),
          "ledger_findings": st.get("ledger_findings")}
    try:
        kw["input_files"] = "+".join(f"{k}:{v}" for k, v in json.loads((d / "check.txt").read_text()).get("inputs", {}).items())
    except Exception:
        pass
    if u:
        kw.update(input_tokens=u["in"], cache_write=u["cache_write"], cache_read=u["cache_read"],
                  output_tokens=u["out"], thinking_tokens=u["thinking"], turns=u["turns"],
                  billed_input_total=u["in"] + u["cache_write"] + u["cache_read"])
    kw["notes"] = f"status verify {st.get('verify')}"
    add(ref, "v12:out", "v12", "claude-opus-5-5 effort high", d / f"{sa(ref)}.reading.tr.md", **kw)


# ------------------------------------------------------------------ v13 arms (v14/out* are byte-identical copies)
def v13_status(path):
    return json.loads(path.read_text()) if path.exists() else None


def v13_step(arm, ref, step, seen=None):
    """Return (status dict, arm it came from) following 'reused' sources."""
    d = C / "v13" / arm / sdir(ref) / sa(ref)
    st = v13_status(d / f"{step}.status.json")
    if st and st.get("state") == "reused":
        src = st.get("source", "")
        src_arm = src.split("/")[0]
        return v13_step(src_arm, ref, step)
    return st, arm


for arm in ["out", "out-v2", "out-v3", "out-v4", "out-mixed", "out-xhigh", "out-max"]:
    for ref in AYAT:
        d = C / "v13" / arm / sdir(ref) / sa(ref)
        if not d.exists():
            continue
        reading = d / f"{sa(ref)}.reading.tr.md"
        if not reading.exists() and arm != "out-max":
            continue
        tot = defaultdict(float)
        own_cost = 0.0
        steps = []
        for step in ("act", "qeq", "write"):
            st, src = v13_step(arm, ref, step)
            if not st:
                continue
            steps.append(f"{step}@{src}:${st.get('cost')}")
            for k in ("in", "out", "thinking", "cache_write", "cache_read", "input", "cost", "input_bytes"):
                tot[k] += st.get(k) or 0
            if src == arm:
                own_cost += st.get("cost") or 0
        setaside = 0.0
        for f in d.glob("*.status.json"):
            if "cap64k" in f.name or "refused" in f.name:
                setaside += (json.loads(f.read_text()).get("cost") or 0)
        net = v13_status(C / "v13" / arm / sdir(ref) / "net.status.json")
        wst = v13_status(d / "write.status.json") or {}
        kw = {"input_bytes": wst.get("input_bytes", ""), "input_tokens": int(tot["input"]),
              "cache_write": int(tot["cache_write"]), "cache_read": int(tot["cache_read"]),
              "output_tokens": int(tot["out"]), "thinking_tokens": int(tot["thinking"]),
              "cost_usd": round(tot["cost"], 3), "billed_input_total": int(tot["in"]),
              "input_files": "write step: " + "+".join(wst.get("files", [])),
              "notes": (f"per-ayah steps {' '.join(steps)}; all-step input_bytes {int(tot['input_bytes'])}; "
                        f"cost incl. reused upstream steps; own-arm cost ${own_cost:.3f}; set-aside failed calls ${setaside:.3f}"
                        + (f"; shared S1 network call ${net.get('cost')}" if net and net.get("cost") else "")
                        + ("; v14/" + arm + " is a byte-identical copy" if arm in ("out", "out-v2", "out-mixed", "out-xhigh", "out-max") else ""))}
        if arm == "out-max":
            a = v13_status(d / "act.status.json") or {}
            kw["notes"] = f"FAILED effort max step 1: {a.get('state')} cost ${a.get('cost')} (HANDOFF.md: $10.28, 256K output all thinking); no reading"
            kw["cost_usd"] = a.get("cost", "")
            reading = None
        add(ref, f"v13:{arm}", "v13", "claude-opus-5-5 effort " + ("xhigh" if arm == "out-xhigh" else "high/xhigh" if arm == "out-mixed" else "max" if arm == "out-max" else "high"),
            reading, **kw)

# ------------------------------------------------------------------ v14 Sol/Astra 1:6 trials
for arm in ["out-sol-max", "out-sol-stable", "out-sol-argument", "out-astra-argument"]:
    d = C / "v14" / arm / "s001" / "1_6"
    wst = json.loads((d / "write.status.json").read_text())
    add("1:6", f"v14:{arm}", "v14", f"{wst.get('model')} {wst.get('effort')}", d / "1_6.reading.tr.md",
        input_bytes=fsize(d / "write.input.md"), input_chars=fchars(d / "write.input.md"),
        notes="agent.provenance.json: token_usage null, cost null (not supplied); upstream frozen from v13 out-v2")

# ------------------------------------------------------------------ v15 out / out-nocap
for arm in ["out", "out-nocap"]:
    led = [json.loads(l) for l in (C / "v15" / arm / "ledger.jsonl").read_text().splitlines() if l.strip()]
    for ref in AYAT:
        d = C / "v15" / arm / sdir(ref) / sa(ref)
        if not d.exists():
            continue
        tot = defaultdict(int)
        for f in ("record.json.raw.json", "commentary.tr.md.raw.json"):
            u = claude_usage(d / f)
            if u:
                for k in ("in", "cache_write", "cache_read", "out"):
                    tot[k] += u[k]
                tot["thinking"] += u["thinking"] or 0
        opus_cost = sum(e.get("cost_usd") or 0 for e in led if e.get("ayah") == ref and e["model"].startswith("claude"))
        pchars = sum(e["prompt_chars"] for e in led if e.get("ayah") == ref and e["model"].startswith("claude"))
        luna = [e for e in led if e.get("ayah") == ref and e["model"].startswith("gpt")]
        lu = defaultdict(int)
        for e in luna:
            for k, v in (e.get("usage") or {}).items():
                lu[k] += v
        shared = [(e["unit"], e.get("cost_usd")) for e in led if e.get("ayah") is None and e["model"].startswith("claude")
                  and (e["unit"].split(":")[2] == ref.split(":")[0])]
        add(ref, f"v15:{arm}", "v15", "claude-opus-5-5 effort high (discover+write) + gpt-6-luna max (evidence)",
            d / "commentary.tr.md",
            input_chars=pchars, input_tokens=tot["in"], cache_write=tot["cache_write"], cache_read=tot["cache_read"],
            output_tokens=tot["out"], thinking_tokens=tot["thinking"], cost_usd=round(opus_cost, 4),
            billed_input_total=tot["in"] + tot["cache_write"] + tot["cache_read"],
            input_files="Opus prompts: record.json.prompt.md + commentary.tr.md.prompt.md (ledger prompt_chars)",
            notes=(f"Opus discover+write only; Luna evidence call: prompt_chars {sum(e['prompt_chars'] for e in luna)}, "
                   f"in {lu.get('input_tokens', 0)} (cached {lu.get('cached_input_tokens', 0)}), out {lu.get('output_tokens', 0)} "
                   f"(reasoning {lu.get('reasoning_output_tokens', 0)}), no cost recorded; shared Opus calls "
                   + ", ".join(f"{u} ${c:.2f}" for u, c in shared)
                   + "; shared Luna frames/profiles/loanwords (whole-Quran/surah preprocessing) not attributed"))

# ------------------------------------------------------------------ v5
V5 = C / "v5"
V5_EST = {  # s001-astra-token-usage-estimate.md totals (UTF-8 bytes/4 estimate, scope+CE+invitation)
    "1:1": (1544.6, 297.7), "1:2": (1947.8, 372.5), "1:3": (1366.2, 261.6), "1:4": (2155.4, 465.9),
    "1:5": (1947.9, 381.0), "1:6": (2127.7, 457.1), "1:7": (2315.9, 519.1)}
V5_PRICE = {"1:1": 30.33, "1:2": 38.10, "1:3": 26.74, "1:4": 44.85, "1:5": 38.53, "1:6": 44.13, "1:7": 49.11}


def v5_model(analysis, layer, luna6):
    if luna6:
        return "gpt-6-luna (luna-6 rerun)"
    if layer == "middle":
        return "gpt-5.6-luna max (runbook default)"
    if layer == "concise":
        return "unknown"
    if analysis.startswith("s001-fresh"):
        return "gpt-6-astra high (S1 override; s001-astra-*.md)"
    return "scope gpt-5.6-luna max + CE gpt-5.6-sol max (runbook defaults, not verified per run)"


for ref in AYAT:
    for layer, base, pat in [("canonical", "raw", "prose"), ("editorial", "editorial", "prose.editorial"),
                             ("middle", "middle", "prose.middle"), ("concise", "concise", "prose.concise")]:
        for f in sorted((V5 / base).glob(f"*/{sdir(ref)}/{sa(ref)}/{sa(ref)}.{pat}*.tr.md")):
            name = f.name
            if layer == "canonical" and not re.fullmatch(rf"{sa(ref)}\.prose(\.luna-6)?\.tr\.md", name):
                continue
            if layer == "editorial" and not re.fullmatch(rf"{sa(ref)}\.prose\.editorial(\.luna-6)?\.tr\.md", name):
                continue
            analysis = f.parts[f.parts.index(base) + 1]
            luna6 = ".luna-6." in name
            ip = V5 / "input" / analysis / sdir(ref) / sa(ref)
            disc = sum(fsize(ip / f"{l}.discovery.prompt.md") for l in ("micro", "macro", "global"))
            layer_prompt = {"canonical": "canonical.prompt.md", "editorial": "editorial.prompt.md",
                            "middle": "middle-layer.prompt.md", "concise": None}[layer]
            kw = {"input_bytes": disc, "input_files": f"3 discovery prompts ({analysis}); layer prompt "
                  + (f"{layer_prompt} {fsize(ip / layer_prompt)} B" if layer_prompt else "n/a")}
            notes = []
            if ref in V5_EST and analysis.startswith("s001-fresh") and layer == "editorial":
                i, o = V5_EST[ref]
                kw["input_tokens"] = int(i * 1000)
                kw["output_tokens"] = int(o * 1000)
                kw["cost_usd"] = f"est {V5_PRICE[ref]}"
                notes.append("whole-pipeline ESTIMATE (bytes/4) from s001-astra-token-usage-estimate.md; Astra list price from s001-astra-model-pricing-estimate.md")
            elif ref in V5_EST and analysis.startswith("s001-fresh"):
                notes.append("pipeline estimate attached to the editorial row")
            else:
                notes.append("no token/cost record found")
            if not disc:
                notes.append("discovery prompts not found for this analysis id")
            kw["notes"] = "; ".join(notes)
            add(ref, f"v5:{layer}{'-luna6' if luna6 else ''}:{analysis}", "v5", v5_model(analysis, layer, luna6), f, **kw)

# ------------------------------------------------------------------ v3
for f in sorted((C / "v3" / "outputs" / "authoring" / "s001").glob("*/merge/*/*.prose.tr.md")):
    ref = f.name.split(".")[0].replace("_", ":")
    if ref in AYAT:
        add(ref, "v3:authoring-merge", "v3", "unknown", f, notes="no token/cost record found")

# ------------------------------------------------------------------ write metrics.tsv
COLS = ["ayah", "run", "version", "model", "input_bytes", "input_chars", "billed_input_total", "input_tokens",
        "cache_write", "cache_read", "output_tokens", "thinking_tokens", "cost_usd", "turns", "words", "tr_words",
        "distinct_refs", "same_surah_refs", "other_surah_refs", "focus_cited", "arabic_tags_single",
        "arabic_tags_double", "headings", "paragraphs", "recall_marks", "sozluk_mentions", "ledger_findings",
        "validator_problems", "prose_bytes", "upstream_refs", "upstream_only_refs", "upstream_source", "tagged_src_refs_not_in_prose", "rendered_md_words", "rendered_md_refs", "run_commit", "input_files", "path", "notes"]
order = {a: i for i, a in enumerate(AYAT)}
rows.sort(key=lambda r: (order[r["ayah"]], r["version"], r["run"]))
with open(HERE / "metrics.tsv", "w", encoding="utf-8") as fh:
    fh.write("\t".join(COLS) + "\n")
    for r in rows:
        fh.write("\t".join(str(r.get(c, "")).replace("\t", " ").replace("\n", " ") for c in COLS) + "\n")

# ------------------------------------------------------------------ overlaps
with open(HERE / "overlaps.tsv", "w", encoding="utf-8") as fh:
    fh.write("ayah\trun_a\trun_b\tn_a\tn_b\tshared\tonly_a\tonly_b\tjaccard\n")
    for ref in AYAT:
        rs = [r for r in rows if r["ayah"] == ref and "_refs" in r]
        for a, b in itertools.combinations(rs, 2):
            A, B = a["_refs"], b["_refs"]
            u = A | B
            j = len(A & B) / len(u) if u else ""
            fh.write(f"{ref}\t{a['run']}\t{b['run']}\t{len(A)}\t{len(B)}\t{len(A & B)}\t{len(A - B)}\t{len(B - A)}\t"
                     f"{j if j == '' else round(j, 3)}\n")

# dump refs for later inspection
with open(HERE / "refs.json", "w") as fh:
    json.dump({f"{r['ayah']}|{r['run']}": sorted(f"{s}:{a}" for s, a in r["_refs"]) for r in rows if "_refs" in r}, fh,
              ensure_ascii=False, indent=0)
print(f"{len(rows)} rows")
