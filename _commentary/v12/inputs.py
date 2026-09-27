#!/usr/bin/env python3
"""V12 evidence for one ayah (scripts, no model): _commentary/v12/work/sNNN/S_A/

Reused from V9/V11 (built by `_commentary/v11/run.py` prep, digest v2):
  context.md        the ayah, its words, word notes, the Fatiha, the whole surah (or its passage)
  01_dictionary.md  every attested branch of every root of the ayah (V9 input package)
  digest_v2.md      qirāʾāt, each root's occurrences, related passages with the earlier review's reason
New in V12:
  hft.md            the existing image-chain hypotheses (HFT, latent_activation/focus_trace/runs/sN/readers/
                    reader_hft_a/S_A.focus_trace.json, 90 surahs): records whose focus is this ayah in full, and records of other ayat whose trace passes through it; every trace step is
                    resolved to its word and dictionary branch (gloss, image, first classical phrase, quotable) and
                    flagged when the branch does not exist or the root is an echo / alternative / not the word's
  channels.md       the surah's channel review (quran-data network-v3/sNNN/review/reader_a_pilot.md): an index of
                    every channel, and in full the sub-channels anchored in this ayah (motif ids as `root Bnnn`)
  neighbours.md     one line per branch of every other root in the surah (short surahs) or in the ayah's passage
                    (pericope ± 7 ayat), so a picture this ayah starts can be completed with another ayah's word
  usage.md          root dossiers for the ayah's roots (`_projects/root-dossier/deliver.py`), when they exist: each
                    root's occurrences grouped by stated context, this ayah's group marked, the plain-reading branch
  digest_v2.md      (v12 copy, only when usage.md exists) V11's digest with the usage block of every root that usage.md
                    covers replaced by a pointer (the dossier lists every occurrence; the digest skipped common forms);
                    run.py uses V11's own digest when usage.md is switched off
  inputs.tsv        bytes per input file

Usage: python3 _commentary/v12/inputs.py 1:7 [--window-only]
       (as a module: build(ref), window(ref), hft_records(refs), channels(surah, ref), branch_table(refs, skip))
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from functools import lru_cache
from pathlib import Path

V12 = Path(__file__).resolve().parent
REPO = V12.parents[1]
V9 = REPO / "_commentary" / "v9"
V11 = REPO / "_commentary" / "v11"
sys.path.insert(0, str(V9))
import prepare as P  # noqa: E402

HFT_RUNS = REPO.parent / "latent_activation" / "focus_trace" / "runs"  # 90 surahs; bundles/ holds only 64 of them
REVIEWS = P.QD / "analysis" / "channels" / "network-v3"
PERICOPES = REVIEWS / "pericopes" / "surah_pericopes.jsonl"
DOSSIER = REPO.parent / "root-dossier"  # standalone repo (_projects/root-dossier)
DOSSIER_OUT = Path(os.environ.get("DOSSIER_OUT") or DOSSIER / "out")  # e.g. …/root-dossier/out-wa for the --wa arm
SHORT = 40     # surahs up to this many ayat are one window (as V11 seeds_input.py)
OVERLAP = 7    # ayat added on each side of the ayah's pericope
SPAN = 7       # long surahs: neighbours.md covers the focus ayah ± SPAN ayat (the surah pass gets the whole window)
PRIMARY_READER = "reader_hft_a"

_SRC: P.Sources | None = None


def src() -> P.Sources:
    global _SRC
    if _SRC is None:
        _SRC = P.Sources()
    return _SRC


def work_dir(ref: str) -> Path:
    s, a = (int(x) for x in ref.split(":"))
    return V12 / "work" / f"s{s:03d}" / f"{s}_{a}"


def surah_len(surah: int) -> int:
    return max(int(r.split(":")[1]) for r in src().quran if r.startswith(f"{surah}:"))


def window(ref: str) -> list[str]:
    """The whole surah when short; otherwise the ayah's pericope widened by OVERLAP ayat on both sides."""
    s, a = (int(x) for x in ref.split(":"))
    n = surah_len(s)
    lo, hi = 1, n
    if n > SHORT and PERICOPES.exists():
        for line in PERICOPES.read_text(encoding="utf-8").splitlines():
            d = json.loads(line)
            if d["surah"] == s and d["ayah_from"] <= a <= d["ayah_to"]:
                lo, hi = max(1, d["ayah_from"] - OVERLAP), min(n, d["ayah_to"] + OVERLAP)
                break
    return [f"{s}:{x}" for x in range(lo, hi + 1)]


# ---------------------------------------------------------------- HFT
@lru_cache(maxsize=None)
def _words(ref: str) -> dict[str, dict]:
    return {str(w["w"]): w for w in src().words(ref)}


@lru_cache(maxsize=None)
def _roots_of(ref: str, w: str) -> tuple[set, set, set]:
    word = _words(ref).get(w)
    if not word:
        return set(), set(), set()
    r = src().word_roots(word)
    return set(r["identity"]), {x[0] for x in r["alternatives"]}, {x[0] for x in r["echo"]}


def first_phrase(s: str) -> str:
    return re.split(r"[؛;]", s or "", maxsplit=1)[0].strip()


def _bare(s: str) -> str:
    s = re.sub(r"[\u0610-\u061a\u064b-\u065f\u0670\u06d6-\u06ed\u0640]", "", s or "")
    return s.translate(str.maketrans({"أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ى": "ي", "ة": "ه"})).strip()


def phrase_indices(words: dict[str, dict], phrase: str) -> list[str]:
    """Protocol v3 (S100) names the word by its Arabic (`source_phrase_ar`), not by index: the words whose bare form
    contains the phrase's words, in order (the first run that matches)."""
    want = [_bare(x) for x in (phrase or "").split() if _bare(x)]
    ks = sorted(words, key=int)
    for i in range(len(ks)):
        run = ks[i:i + len(want)]
        if len(run) == len(want) and all(w and w in _bare(words[k]["surface"]) for w, k in zip(want, run)):
            return run
    return []


def resolve_step(step: dict) -> dict:
    ref = step.get("source_ref", "")
    words = _words(ref) if re.match(r"^\d+:\d+$", ref or "") else {}
    idxs = [str(i) for i in step.get("source_word_indices") or []] or phrase_indices(words, step.get("source_phrase_ar", ""))
    surface = " ".join(words[i]["surface"] for i in idxs if i in words) or "?"
    rid, bid = step.get("mapped_root_id", ""), step.get("branch_id", "")
    b = src().branch(f"quranic:{rid}:{bid}") if rid and bid else {}
    name = src().root_name.get(rid) or step.get("root", "") or rid
    flags = []
    if not b:
        flags.append("no such branch in the dictionary")
    ident, alt, echo = set(), set(), set()
    for i in idxs:
        a, b2, c = _roots_of(ref, i)
        ident |= a
        alt |= b2
        echo |= c
    if rid and idxs:
        if rid in ident:
            pass
        elif rid in alt:
            flags.append("~alt: a cited alternative analysis, not the word's primary root")
        elif rid in echo:
            flags.append("~echo: a sound-family root, not the word's root")
        else:
            flags.append("root not mapped to this word by the current gateway")
    g = b.get("concept_gloss") if b else ""
    g = (g.get("text") if isinstance(g, dict) else g) or ""
    return {"ref": ref, "w": ",".join(idxs), "surface": surface, "root": name, "rid": rid, "bid": bid, "gloss": g,
            "image": (b or {}).get("branch_image_ar", ""), "phrase": first_phrase((b or {}).get("source_phrase_ar", "")),
            "role": step.get("role") or step.get("assigned_role") or step.get("literal_contribution") or "",
            "flags": flags}


@lru_cache(maxsize=None)
def dossier_map() -> dict[str, dict]:
    """QAC word id → its canonical-map row (root-dossier out/activation_map.tsv: the plain reading's branch, group)."""
    f = DOSSIER_OUT / "activation_map.tsv"
    if not f.exists():
        return {}
    lines = f.read_text(encoding="utf-8").splitlines()
    cols = lines[0].split("\t")
    rows = (dict(zip(cols, l.split("\t"))) for l in lines[1:] if l)
    return {r["qac_word_ref"]: r for r in rows if r.get("role") == "dominant"}


@lru_cache(maxsize=None)
def group_labels(root: str) -> dict[str, str]:
    f = DOSSIER_OUT / "final" / f"{re.sub(r'[^ء-ي]', '', root)}.json"
    if not f.exists():
        return {}
    return {g["id"]: g.get("label", "") for g in json.loads(f.read_text(encoding="utf-8")).get("groups") or []}


def plain_note(st: dict) -> str:
    """For a trace step whose word has a root dossier: the branch its plain reading realises and its usage group, so
    a trace that uses another branch is visibly a latent reading."""
    rid = st.get("rid", "")
    for w in st["w"].split(","):
        row = dossier_map().get(f"{st['ref']}:{w}")
        if not row or not row.get("branch_ref", "").startswith(rid + "/"):
            continue
        b = row["branch_ref"].split("/")[-1]
        lab = group_labels(row["root"]).get(row.get("group", ""), "")
        return (f" [plain here: {'the same branch' if b == st['bid'] else b}"
                + (f"; usage group: {P.clip(lab, 80)}" if lab else "") + "]")
    return ""


def step_line(st: dict) -> str:
    """The branch's Arabic image and phrases are in 01_dictionary.md / neighbours.md, so only the gloss is repeated."""
    fl = f" [{'; '.join(st['flags'])}]" if st["flags"] else ""
    return (f"{st['ref']} w{st['w']} {st['surface']} → {st['root']} {st['bid']} ({st['gloss'] or '—'})"
            f" — {P.clip(st['role'], 170)}{fl}{plain_note(st)}")


def hft_records(refs: list[str]) -> list[dict]:
    """Every HFT record of the given ayat (primary reader; others only when it is absent), steps resolved."""
    out = []
    for ref in refs:
        s, a = ref.split(":")
        d = HFT_RUNS / f"s{int(s)}" / "readers"
        # the exact name: sNNN/readers also holds model-comparison runs (100_1.5.5-high.focus_trace.json …)
        files = {x.name: x / f"{s}_{a}.focus_trace.json" for x in sorted(d.glob("*")) if x.is_dir()} if d.is_dir() else {}
        files = {k: v for k, v in files.items() if v.exists()}
        if not files:
            continue
        r = json.loads(files[PRIMARY_READER if PRIMARY_READER in files else sorted(files)[0]].read_text(encoding="utf-8"))
        for kind in ("baseline_models", "context_deltas", "surprising_valid_outliers"):
            for rec in r.get(kind) or []:
                cr = rec.get("changed_reading") or {}
                out.append({"focus": ref, "kind": kind.rstrip("s").replace("_", " "),
                            "name": rec.get("model_id") or rec.get("delta_id") or rec.get("outlier_id") or "?",
                            "confidence": rec.get("confidence", "?"), "before": cr.get("before", ""),
                            "after": cr.get("after", ""), "mechanism": rec.get("mechanism", ""),
                            "containment": rec.get("containment", ""),
                            "steps": [resolve_step(x) for x in rec.get("activation_trace") or []]})
    return out


def hft_for(ref: str, records: list[dict]) -> str:
    own = [r for r in records if r["focus"] == ref]
    through = [r for r in records if r["focus"] != ref and any(st["ref"] == ref for st in r["steps"])]
    if not own and not through:
        return ""
    flagged = sum(1 for r in own for st in r["steps"] if st["flags"]) + \
        sum(1 for r in through for st in r["steps"] if st["flags"] and st["ref"] == ref)
    lines = [f"# hft.md — earlier readers' image-chain hypotheses touching {ref} (proposals, checked by script)", "",
             "HFT readers proposed these readings earlier. They are what is already known: ground, correct, connect",
             "and go beyond them; do not re-list them. Each trace step: ayah, word, the dictionary branch it uses (its",
             "gloss; the Arabic image and classical phrases are in 01_dictionary.md or neighbours.md), the role, and a",
             f"script flag in brackets when something is wrong ({flagged} flagged steps here).", ""]
    if own:
        lines += [f"## Records whose focus is {ref}", ""]
        for r in own:
            lines += [f"### {r['name']} [{r['kind']}, {r['confidence']}]",
                      f"- before: {r['before']}", f"- after: {r['after']}",
                      f"- mechanism: {P.clip(r['mechanism'], 350)}"]
            if r["containment"]:
                lines.append(f"- containment: {P.clip(r['containment'], 250)}")
            lines.append("- trace:")
            lines += [f"  - {step_line(st)}" for st in r["steps"]]
            lines.append("")
    if through:
        lines += [f"## Records of other ayat whose trace passes through {ref}", ""]
        for r in through:
            here = [st for st in r["steps"] if st["ref"] == ref]
            others = [st for st in r["steps"] if st["ref"] != ref]
            lines.append(f"- **{r['name']}** (focus {r['focus']}, {r['confidence']}) — after: {P.clip(r['after'], 300)}")
            lines += [f"  - here: {step_line(st)}" for st in here]
            if others:
                lines.append("  - with: " + "; ".join(f"{st['ref']} {st['surface']} {st['root']} {st['bid']}"
                                                      + (" [!]" if st["flags"] else "") for st in others))
        lines.append("")
    return "\n".join(lines) + "\n"


def hft_window(records: list[dict]) -> str:
    """Compact view of every record of a window (the surah pass)."""
    if not records:
        return ""
    lines = ["# hft.md — the earlier readers' image-chain hypotheses for this window (compact, checked by script)", "",
             "One record per line group: focus ayah, name, confidence, the changed reading, then the trace (ayah, word,",
             "root Bnnn — the branch is in branch_table.md; [!] = the script found a problem: no such branch, or an echo /",
             "alternative root). The ayah ledgers' Chains lines judge these records ayah by ayah.", ""]
    for r in records:
        lines.append(f"- **{r['focus']} {r['name']}** ({r['kind']}, {r['confidence']}) — {P.clip(r['after'], 260)}")
        lines.append("  - trace: " + "; ".join(
            f"{st['ref']} {st['surface']} {st['root']} {st['bid']}" + (" [!]" if st["flags"] else "")
            for st in r["steps"]))
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- channel review
REF_RUN = re.compile(r"(\d{1,3}):(\d{1,3}(?:\s*[-–]\s*\d{1,3})?(?:\s*,\s*\d{1,3}(?:\s*[-–]\s*\d{1,3})?)*)")


def refs_in(text: str) -> set[str]:
    out = set()
    for m in REF_RUN.finditer(text):
        s = m.group(1)
        for part in m.group(2).split(","):
            part = part.strip()
            if re.match(r"^\d+\s*[-–]\s*\d+$", part):
                lo, hi = (int(x) for x in re.split(r"\s*[-–]\s*", part))
                out |= {f"{s}:{x}" for x in range(lo, hi + 1)} if hi - lo < 300 else set()
            elif part.isdigit():
                out.add(f"{s}:{part}")
    return out


def motif_ids(text: str) -> str:
    """`quranic:root_000671:B001/m01` and `ر ب ب:B001/m01` → `root Bnnn` in Arabic letters."""
    text = re.sub(r"quranic:(root_\d+):(B\d{3})(?:/m\d+)?",
                  lambda m: f"{src().root_name.get(m.group(1), m.group(1))} {m.group(2)}", text)
    return re.sub(r"([ء-ي](?: [ء-ي]){1,4}):(B\d{3})(?:/m\d+)?", r"\1 \2", text)


def review_path(surah: int) -> Path:
    return REVIEWS / f"s{surah:03d}" / "review" / "reader_a_pilot.md"


def parse_review(surah: int) -> list[dict]:
    f = review_path(surah)
    if not f.exists():
        return []
    parents: list[dict] = []
    for line in f.read_text(encoding="utf-8").splitlines():
        if line.startswith("### "):
            parents.append({"title": line[4:].strip(), "head": [], "subs": []})
        elif line.startswith("#### ") and parents:
            parents[-1]["subs"].append({"title": line[5:].strip(), "lines": []})
        elif parents and line.strip():
            (parents[-1]["subs"][-1]["lines"] if parents[-1]["subs"] else parents[-1]["head"]).append(line)
    return parents


def channels(surah: int, ref: str | None = None, refs: list[str] | None = None) -> str:
    """ref: the index plus the sub-channels anchored in that ayah; refs (a window) or None: the whole review."""
    parents = parse_review(surah)
    if not parents:
        return ""
    want = {ref} if ref else set(refs or [])
    lines = [f"# channels.md — the surah's image chains as an earlier whole-surah review mapped them", "",
             "Source: quran-data channels network-v3 review (reader_a_pilot). Parent channels, then sub-channels with",
             "their scene, active motifs (root Bnnn) and ayah anchors. What is already known: ground, correct, connect",
             "and go beyond it.", ""]
    if ref:
        lines += ["## Index of every channel in the surah", ""]
        for p in parents:
            lines.append(f"- {p['title']}: " + "; ".join(s["title"] for s in p["subs"]))
        lines += ["", f"## The channels anchored in {ref}, in full", ""]
    for p in parents:
        subs = [s for s in p["subs"] if not want or want & refs_in(" ".join(s["lines"]))]
        if want and not subs:
            continue
        lines += [f"### {p['title']}"] + [motif_ids(x) for x in p["head"]]
        for s in subs:
            lines += [f"#### {s['title']}"] + [motif_ids(x) for x in s["lines"]]
        lines.append("")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- branch table (V11 seeds_input.py, with a skip set)
def branch_table(refs: list[str], skip: set[str] | None = None, title: str = "", echo: bool = False,
                 definitions: bool = True) -> str:
    skip = skip or set()
    roots: dict[str, dict] = {}
    for ref in refs:
        for w in src().words(ref):
            r = src().word_roots(w)
            kinds = [("identity", r["identity"]), ("alternative", [a[0] for a in r["alternatives"]])]
            if echo:
                kinds.append(("echo", [e[0] for e in r["echo"]]))
            for kind, rids in kinds:
                for rid in rids:
                    if rid in skip:
                        continue
                    d = roots.setdefault(rid, {"kind": kind, "where": []})
                    if kind == "identity":
                        d["kind"] = "identity"
                    tag = f"{ref} w{w['w']} {w['surface']}"
                    if tag not in d["where"]:
                        d["where"].append(tag)
    lines = [title or "# Branch table", "",
             "One line per branch: Bnnn | gloss | Arabic image | " + ("definition | " if definitions else "")
             + "first classical source phrase.",
             "`~alt` = a cited alternative analysis of the word; `~echo` = a sound-family root (not the word's root).",
             "Cite a branch as `root Bnnn`, e.g. `ر ب ب B007`; its Arabic may be quoted with that source.", ""]
    order = sorted(roots, key=lambda x: ({"identity": 0, "alternative": 1, "echo": 2}[roots[x]["kind"]],
                                         min(tuple(int(y) for y in t.split()[0].split(":")) for t in roots[x]["where"])))
    for rid in order:
        d = roots[rid]
        e = src().entry(rid)
        if not e:
            continue
        flag = {"identity": "", "alternative": " ~alt", "echo": " ~echo"}[d["kind"]]
        lines.append(f"### {src().root_name.get(rid) or rid}{flag} — {'; '.join(d['where'][:10])}"
                     + (f" (+{len(d['where']) - 10})" if len(d["where"]) > 10 else ""))
        for b in e.get("branches", []):
            bid = b["branch_ref"].split("/")[-1]
            g = b.get("concept_gloss")
            g = (g.get("text") if isinstance(g, dict) else g) or ""
            cm = b.get("concept_map") or {}
            lines.append(f"- {bid} {g} | {b.get('branch_image_ar', '')} | "
                         + (f"{cm.get('definition', '')} | " if definitions else "")
                         + (first_phrase(b.get('source_phrase_ar', '')) if definitions
                            else P.clip(first_phrase(b.get('source_phrase_ar', '')), 110)))
        lines.append("")
    return "\n".join(lines) + "\n"


def neighbour_refs(ref: str) -> list[str]:
    s, a = (int(x) for x in ref.split(":"))
    n = surah_len(s)
    if n <= SHORT:
        return [f"{s}:{x}" for x in range(1, n + 1) if x != a]
    return [f"{s}:{x}" for x in range(max(1, a - SPAN), min(n, a + SPAN) + 1) if x != a]


def focus_rids(ref: str) -> set[str]:
    out = set()
    for w in src().words(ref):
        r = src().word_roots(w)
        out |= set(r["identity"]) | {a[0] for a in r["alternatives"]} | {e[0] for e in r["echo"]}
    return out


# ---------------------------------------------------------------- driver
def prep_v11(ref: str) -> None:
    """V9 package, context.md and digest v2, exactly as V11 builds them."""
    r = subprocess.run([sys.executable, "-c",
                        "import sys; sys.path.insert(0, %r); import run; run.ARM = 'D'; run.prep(%r)"
                        % (str(V11), ref)], capture_output=True, text=True, cwd=REPO)
    if r.returncode:
        sys.exit(f"v11 prep failed for {ref}:\n{(r.stdout + r.stderr)[-2000:]}")


def deliver(args: list[str], target: Path) -> bool:
    """usage.md from the root dossiers (_projects/root-dossier/deliver.py). A failure is recorded next to the target
    (usage.error.txt; the run records it in status.json) instead of passing silently; success clears it."""
    err = target.with_name("usage.error.txt")
    script = DOSSIER / "deliver.py"
    if not script.exists():
        return False
    r = subprocess.run([sys.executable, str(script), *args, "--final", str(DOSSIER_OUT / "final"), "--out", str(target)],
                       capture_output=True, text=True, cwd=REPO)
    if r.returncode:
        err.write_text(f"deliver.py {' '.join(args)} failed (exit {r.returncode}):\n{r.stderr[-2000:]}\n", encoding="utf-8")
        target.unlink(missing_ok=True)  # never a stale usage.md from an earlier run
        return False
    err.unlink(missing_ok=True)
    return True


def digest_with_pointers(digest: Path, usage: Path, target: Path) -> None:
    """V11's digest with the usage block (### U-…) of every root that usage.md covers replaced by one line."""
    if not usage.exists() or not digest.exists():
        target.unlink(missing_ok=True)
        return
    covered = set(re.findall(r"(?m)^### ([ء-ي](?: [ء-ي]){1,4}) — ", usage.read_text(encoding="utf-8")))
    out, skip = [], False
    for line in digest.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^### U-\S+ root ([ء-ي](?: [ء-ي]){1,4}) ", line)
        if m:
            skip = m.group(1) in covered
            out.append(line + ("\n- every occurrence, grouped by context: see usage.md" if skip else ""))
            continue
        if line.startswith("#"):
            skip = False
        if not skip:
            out.append(line)
    target.write_text("\n".join(out) + "\n", encoding="utf-8")


def build(ref: str) -> dict[str, int]:
    prep_v11(ref)
    s = int(ref.split(":")[0])
    out = work_dir(ref)
    out.mkdir(parents=True, exist_ok=True)
    win = window(ref)
    nb = neighbour_refs(ref)
    files = {
        "hft.md": hft_for(ref, hft_records(win)),
        "channels.md": channels(s, ref),
        "neighbours.md": branch_table(nb, focus_rids(ref),
                                      f"# neighbours.md — every branch of the other roots of {nb[0]}–"
                                      f"{nb[-1].split(':')[1]} (the focus roots are in 01_dictionary.md)",
                                      definitions=False),
    }
    for name, text in files.items():
        f = out / name
        if text.strip():
            f.write_text(text, encoding="utf-8")
        elif f.exists():
            f.unlink()
    deliver(["ayah", ref], out / "usage.md")
    v9w = V9 / "lines" / "work" / f"{s}_{ref.split(':')[1]}"
    digest_with_pointers(v9w / "digest_v2.md", out / "usage.md", out / "digest_v2.md")
    pkg = V9 / "input" / "v2" / f"s{s:03d}" / f"{s}_{ref.split(':')[1]}"
    sizes = {}
    for f in [v9w / "context.md", pkg / "01_dictionary.md", v9w / "digest_v2.md",
              *(out / n for n in ("usage.md", "hft.md", "channels.md", "neighbours.md"))]:
        if f.exists():
            sizes[f.name] = f.stat().st_size
    if (out / "digest_v2.md").exists():
        sizes["digest_v2.md (with usage.md)"] = (out / "digest_v2.md").stat().st_size
    (out / "inputs.tsv").write_text("".join(f"{k}\t{v}\n" for k, v in sizes.items()), encoding="utf-8")
    return sizes


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ref")
    ap.add_argument("--window-only", action="store_true", help="print the ayah's window and exit")
    a = ap.parse_args()
    if a.window_only:
        w = window(a.ref)
        print(f"{w[0]}–{w[-1]} ({len(w)} ayat)")
        return
    sizes = build(a.ref)
    print(f"{a.ref}: " + ", ".join(f"{k} {v:,}" for k, v in sizes.items()) + f"; total {sum(sizes.values()):,} bytes")


if __name__ == "__main__":
    main()
