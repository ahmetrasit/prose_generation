#!/usr/bin/env python3
"""v13 step 0: the packet (scripts, no model). See DESIGN.md §3.

Per window (shared by every ayah of the window, placed first in each prompt so it is cached):
  window.md        the window's text; the scan: every branch of every root in the window, one line each
                   (Bnnn gloss | Arabic image); the channel review's index and the sub-channels anchored in the window
Per ayah:
  ayah.md          the ayah, its words (QAC), anchor translation, word notes (V9 context.md, focus part)
  dictionary.md    every branch of every focus root, one line each: gloss | Arabic image | definition | first classical
                   phrase (v12 branch_table with definitions; the fuller section_dictionary is 3× larger)
  pairs.md         script image partners of each focus branch: same ayah / ±7 ayat / surah (V9 03_pairs.md, partner
                   lines reduced to `root Bnnn ← where`: their gloss and image are in the scan)
  concordance.md   every use of each focus root with at most CONC_MAX non-stop uses (ref, form, clause);
                   larger roots: counts per lemma only
  hft.md           earlier readers' image-chain hypotheses for the ayah (where HFT exists)
  reciprocal.md    the reciprocal inter-ayah list (for the QeQ step's closing check only)
  window_text.md   the window's text alone (for the QeQ step)

Windows are fixed: a surah of at most v12 inputs.SHORT ayat is one window; a longer surah uses the ayah's pericope
widened by v12 inputs.OVERLAP ayat on each side (v12 inputs.window).

Usage: python3 _commentary/v13/packet.py 1:4 [1:5 …]
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

V13 = Path(__file__).resolve().parent
COMM = V13.parent
sys.path.insert(0, str(COMM / "v12"))
import inputs as I  # noqa: E402  (v12 evidence builders)

DOSSIER = COMM.parents[1] / "root-dossier"
sys.path.insert(0, str(DOSSIER))
import corpus as C  # noqa: E402  (QAC occurrences by root; stop lemmas)
import build as B  # noqa: E402

RECIPROCAL = I.P.QD / "analysis" / "inter-ayah" / "reciprocal"
CONC_MAX = 60
CLAUSE = 10  # words on each side of the use


def sa(ref: str) -> str:
    return ref.replace(":", "_")


def window_refs(ref: str) -> list[str]:
    return I.window(ref)


def window_dir(ref: str) -> Path:
    w = window_refs(ref)
    s = int(ref.split(":")[0])
    return V13 / "work" / f"s{s:03d}" / f"window_{w[0].split(':')[1]}-{w[-1].split(':')[1]}"


def ayah_dir(ref: str) -> Path:
    return V13 / "work" / f"s{int(ref.split(':')[0]):03d}" / sa(ref)


def scan(refs: list[str], title: str) -> str:
    """Every branch of every root (identity and cited alternatives) of the words of refs: `Bnnn gloss | image`."""
    roots: dict[str, dict] = {}
    for ref in refs:
        for w in I.src().words(ref):
            r = I.src().word_roots(w)
            for kind, rids in (("identity", r["identity"]), ("alternative", [x[0] for x in r["alternatives"]])):
                for rid in rids:
                    d = roots.setdefault(rid, {"kind": kind, "where": []})
                    if kind == "identity":
                        d["kind"] = "identity"
                    tag = f"{ref} w{w['w']} {w['surface']}"
                    if tag not in d["where"]:
                        d["where"].append(tag)
    lines = [title, "", "One line per branch: Bnnn | Turkish gloss | Arabic image. `~alt` = a cited alternative root "
             "analysis of the word. Cite a branch as `root Bnnn`.", ""]
    for rid in sorted(roots, key=lambda x: min(tuple(int(y) for y in t.split()[0].split(":")) for t in roots[x]["where"])):
        e = I.src().entry(rid)
        if not e:
            continue
        d = roots[rid]
        lines.append(f"### {I.src().root_name.get(rid) or rid}{' ~alt' if d['kind'] == 'alternative' else ''} — "
                     + "; ".join(d["where"][:8]) + (f" (+{len(d['where']) - 8})" if len(d["where"]) > 8 else ""))
        for b in e.get("branches", []):
            g = b.get("concept_gloss")
            g = (g.get("text") if isinstance(g, dict) else g) or ""
            lines.append(f"- {b['branch_ref'].split('/')[-1]} {g} | {b.get('branch_image_ar', '')}")
        lines.append("")
    return "\n".join(lines) + "\n"


def compact_pairs(text: str) -> str:
    return re.sub(r"(?m)^(  - (?:same|near|far): \S+ \S+ \S+ B\d+) .*? (← .*)$", r"\1 \2", text)


def quran_lines(refs: list[str]) -> str:
    q = C.quran()
    return "\n".join(f"{r}|{q[r]}" for r in refs if r in q)


def build_window(ref: str) -> Path:
    d = window_dir(ref)
    f = d / "window.md"
    if f.exists():
        return f
    d.mkdir(parents=True, exist_ok=True)
    w = window_refs(ref)
    s = int(ref.split(":")[0])
    text = quran_lines(w)
    scn = scan(w, f"## The scan: every branch of every root in {w[0]}–{w[-1].split(':')[1]}")
    ch = I.channels(s, refs=w)
    parts = [f"# window.md — {w[0]}–{w[-1].split(':')[1]} (shared by every ayah of this window)", "",
             f"## The text ({len(w)} ayat; `S:A|text`)", "", text, "", scn]
    if ch.strip():
        parts += ["## The surah's channel review (an earlier model's map of its image chains)", "", ch]
    f.write_text("\n".join(parts) + "\n", encoding="utf-8")
    (d / "window_text.md").write_text(f"# window_text.md — {w[0]}–{w[-1].split(':')[1]}\n\n{text}\n", encoding="utf-8")
    return f


def ayah_part(ref: str) -> str:
    """The focus part of V9's context.md: the ayah, anchor translation, words, word notes (up to the Fatiha)."""
    ctx = (I.V9 / "lines" / "work" / sa(ref) / "context.md").read_text(encoding="utf-8")
    head = ctx.split("\n# Fatiha", 1)[0]
    return head.replace(f"# {ref} — focus", f"# ayah.md — {ref} (the focus ayah)", 1).rstrip() + "\n"


def concordance(ref: str) -> str:
    keys = [k for k in C.roots_in_ayah(ref)]
    lines = [f"# concordance.md — every use of the focus roots of {ref} (roots with at most {CONC_MAX} uses; "
             "stop lemmas left out)", "",
             "Each use: its word id S:A:W, its form, and its clause with the word marked ⟦ ⟧. Larger roots: counts "
             "per lemma.", ""]
    for k in keys:
        occ = [o for o in C.occurrences(k) if not o["stop"]]
        if not occ:
            continue
        here = [o["id"] for o in occ if o["ref"] == ref]
        by_lemma = Counter(o["lemma"] for o in occ)
        lines.append(f"## {C.spaced(k)} — {len(occ)} uses; here {', '.join(here) or '(stop lemma only)'}; lemmas: "
                     + "; ".join(f"{l} {n}" for l, n in by_lemma.most_common()))
        if len(occ) <= CONC_MAX:
            groups = defaultdict(list)
            for o in occ:
                groups[o["lemma"]].append(o)
            for lem, os_ in groups.items():
                lines.append(f"### {lem}")
                for o in os_:
                    lines.append(f"- {o['id']} [{C.form_label(o)}] {B.mark(o, CLAUSE)}")
        lines.append("")
    return "\n".join(lines) + "\n"


def reciprocal(ref: str) -> str:
    f = RECIPROCAL / f"focus_{sa(ref)}_cutoff_100.tsv"
    if not f.exists():
        return ""
    rows = list(csv.DictReader(f.open(encoding="utf-8"), delimiter="\t"))
    lines = [f"# reciprocal.md — earlier GPT reviews' related passages for {ref} (incomplete, sometimes misleading)", ""]
    seen = set()
    for r in rows:
        t = r["target_ref"]
        if t in seen or r["record_type"] == "self_reiteration":
            continue
        seen.add(t)
        lab = r["focus_direction_label"] or f"reverse:{r['source_direction_label']}"
        lines.append(f"- {t} ({lab}): {B.clip(r['source_note'], 160)}")
    return "\n".join(lines) + "\n"


def build(ref: str) -> dict[str, int]:
    wf = build_window(ref)
    d = ayah_dir(ref)
    d.mkdir(parents=True, exist_ok=True)
    s, a = ref.split(":")
    pairs = I.V9 / "input" / "v2" / f"s{int(s):03d}" / sa(ref) / "03_pairs.md"
    files = {
        "ayah.md": ayah_part(ref),
        "dictionary.md": I.branch_table([ref], title=f"# dictionary.md — every branch of every root of {ref}'s words",
                                        definitions=True),
        "pairs.md": compact_pairs(pairs.read_text(encoding="utf-8")) if pairs.exists() else "",
        "concordance.md": concordance(ref),
        "hft.md": I.hft_for(ref, I.hft_records(window_refs(ref))),
        "reciprocal.md": reciprocal(ref),
    }
    for name, text in files.items():
        (d / name).unlink(missing_ok=True)
        if text.strip():
            (d / name).write_text(text, encoding="utf-8")
    (d / "window").unlink(missing_ok=True)
    (d / "window").write_text(str(wf.parent.relative_to(V13)) + "\n", encoding="utf-8")
    sizes = {"window.md": wf.stat().st_size}
    sizes.update({n: (d / n).stat().st_size for n in files if (d / n).exists()})
    return sizes


if __name__ == "__main__":
    for r in sys.argv[1:]:
        z = build(r)
        print(r, ", ".join(f"{k} {v:,}" for k, v in z.items()), f"total {sum(z.values()):,}")
