#!/usr/bin/env python3
"""Seed-pass input for one surah window (script, no model): out/arms/<arm>/sNNN/seeds/<window>/seeds_input.md

  a  branch table: every branch of every root of every word in the window (identity roots; word-scoped
     alternatives and echo roots flagged), one line each: Bnnn | gloss | Arabic image | definition | first source
     phrase — the unit the seed pass and the chains pass may cite (`source: ر ب ب B007`)
  b  HFT hypotheses where the surah has them, compacted: name, after, trace as S:A word → root Bnnn
  c  surface staging: Quran windows (6 ayat, outside the surah) where several of the window's roots' branch images
     are told on the surface with other words (field roots from each branch's Arabic image and source phrase)
  d  definitional links: a branch whose Arabic image or source phrase uses another root of the window
  e  network pairs (near / surah partners) from the V9 packages' 03_pairs.md, deduplicated (--pairs; off by default)

Windows: the whole surah when it is short (≤ 40 ayat); otherwise each pericope widened by 7 ayat on both sides
(quran-data network-v3 pericopes), so a link across a pericope boundary (e.g. 29:39 sābiqīn ↔ 29:45 ṣalāh) is
inside one window.
Usage: python3 _commentary/v11/seeds_input.py 1 [--arm S] [--list]
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

V11 = Path(__file__).resolve().parent
REPO = V11.parents[1]
V9 = REPO / "_commentary" / "v9"
sys.path.insert(0, str(V9))
import prepare as P  # noqa: E402

PERICOPES = P.QD / "analysis" / "channels" / "network-v3" / "pericopes" / "surah_pericopes.jsonl"
SHORT = 40      # surahs up to this many ayat are one window
OVERLAP = 7     # ayat added on each side of a pericope
STAGE_W = 6     # surface-staging window length (ayat)
STAGE_TOP = 40  # staging windows listed
COMMON_DF = 250  # roots in more ayat than this are too common to mark a field
FILLER = {"فلن", "ذكر", "بعد", "سمو", "قول", "كون", "شيء", "ءخذ", "جيء", "ءتي", "فعل", "رجل", "صحب", "خير", "حسن", "نزل"}


def windows(surah: int, n: int) -> list[tuple[int, int]]:
    if n <= SHORT or not PERICOPES.exists():
        return [(1, n)]
    out = []
    for line in PERICOPES.read_text(encoding="utf-8").splitlines():
        d = json.loads(line)
        if d["surah"] == surah:
            out.append((max(1, d["ayah_from"] - OVERLAP), min(n, d["ayah_to"] + OVERLAP)))
    return out or [(1, n)]


def root_label(src: P.Sources, rid: str) -> str:
    return src.root_name.get(rid) or rid


def first_phrase(s: str) -> str:
    return re.split(r"[؛;]", s or "", maxsplit=1)[0].strip()


class Lex:
    """Arabic token → QAC root join keys (via lemmas and surface forms), with document frequency per root."""

    def __init__(self, src: P.Sources) -> None:
        self.by_form: dict[str, set[str]] = defaultdict(set)
        for lemma, surf, key in src.qac.execute(
                "select lemma_ar, surface_ar, root_join_key from qac_morphemes where root_join_key!=''"):
            for f in (lemma, surf):
                if f:
                    self.by_form[P._norm(f)].add(key)
        self.df = dict(src.qac.execute(
            "select root_join_key, count(distinct surah||':'||ayah) from qac_morphemes where root_join_key!='' "
            "group by root_join_key"))
        self.rid_keys: dict[str, set[str]] = defaultdict(set)
        for key, row in src.gateway.items():
            for rid in row.get("rootIds", []):
                self.rid_keys[rid].add(key)
        self.ayah_roots: dict[str, set[str]] = defaultdict(set)
        for s, a, key in src.qac.execute("select surah, ayah, root_join_key from qac_morphemes where root_join_key!=''"):
            self.ayah_roots[f"{s}:{a}"].add(key)

    def roots(self, text: str) -> set[str]:
        out = set()
        for t in P.concept_tokens(text):
            n = P._norm(t)
            cands = [n] + [n[len(p):] for p in "وفبلك" if n.startswith(p) and len(n) > 4 for p in [p]]
            cands += [c[:-len(s)] for c in list(cands) for s in ("هما", "هم", "ها", "ه", "ات", "ين", "ون") if c.endswith(s) and len(c) - len(s) >= 3]
            for c in cands:
                if c in self.by_form:
                    out |= self.by_form[c]
                    break
        return out


def branch_table(src: P.Sources, refs: list[str]) -> tuple[list[str], dict, dict]:
    """Lines of the table; rid -> {branches, where, kind}; QAC key -> rid (identity)."""
    roots: dict[str, dict] = {}
    key_to_rid: dict[str, str] = {}
    for ref in refs:
        for w in src.words(ref):
            r = src.word_roots(w)
            for kind, rids in (("identity", r["identity"]), ("alternative", [a[0] for a in r["alternatives"]]),
                               ("echo", [e[0] for e in r["echo"]])):
                for rid in rids:
                    d = roots.setdefault(rid, {"kind": kind, "where": []})
                    if kind == "identity":
                        d["kind"] = "identity"
                        for k in r["keys"]:
                            key_to_rid.setdefault(k, rid)
                    tag = f"{ref} w{w['w']} {w['surface']}"
                    if tag not in d["where"]:
                        d["where"].append(tag)
    lines = ["## a. Branch table: every branch of every root in the window", "",
             "One line per branch: Bnnn | gloss | Arabic image | definition | first classical source phrase.",
             "`~alt` = a cited alternative analysis of the word; `~echo` = a sound-family root the gateway withholds",
             "(an echo is not the word's root). Cite a branch as `root Bnnn`, e.g. `ر ب ب B007`.", ""]
    order = sorted(roots, key=lambda x: ({"identity": 0, "alternative": 1, "echo": 2}[roots[x]["kind"]],
                                         min(tuple(int(y) for y in t.split()[0].split(":")) for t in roots[x]["where"])))
    for rid in order:
        d = roots[rid]
        e = src.entry(rid)
        if not e:
            continue
        flag = {"identity": "", "alternative": " ~alt", "echo": " ~echo"}[d["kind"]]
        lines.append(f"### {root_label(src, rid)}{flag} — {'; '.join(d['where'][:12])}"
                     + (f" (+{len(d['where']) - 12})" if len(d["where"]) > 12 else ""))
        d["branches"] = []
        for b in e.get("branches", []):
            bid = b["branch_ref"].split("/")[-1]
            g = b.get("concept_gloss")
            g = (g.get("text") if isinstance(g, dict) else g) or ""
            cm = b.get("concept_map") or {}
            d["branches"].append((bid, b))
            if d["kind"] == "echo":
                lines.append(f"- {bid} {g} | {b.get('branch_image_ar', '')}")
            else:
                lines.append(f"- {bid} {g} | {b.get('branch_image_ar', '')} | {cm.get('definition', '')} | "
                             f"{first_phrase(b.get('source_phrase_ar', ''))}")
        lines.append("")
    return lines, roots, key_to_rid


def hft(refs: list[str], surah: int) -> list[str]:
    seen, out = set(), []
    for ref in refs:
        f = V9 / "input" / "v2" / f"s{surah:03d}" / ref.replace(":", "_") / "02_hft.md"
        if not f.exists():
            continue
        name = None
        for line in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r"## (\S+) \[", line)
            if m and "overview" not in line:
                name = m.group(1)
                if name in seen:
                    name = None
                    continue
                seen.add(name)
                out += ["", f"### {name}"]
            elif name and line.startswith("- after:"):
                out.append(line)
            elif name and re.match(r"\s+- \d+:\d+ w[\d,]+", line):
                m2 = re.match(r"\s+- (\d+:\d+) w[\d,]+ \*\*(.+?)\*\* \((\S+ \S+ \S+ B\d+)", line)
                if m2:
                    out[-1] += f" · {m2.group(1)} {m2.group(2)} {m2.group(3)}" if out[-1].startswith("  trace:") else ""
                    if not out[-1].startswith("  trace:"):
                        out.append(f"  trace: {m2.group(1)} {m2.group(2)} {m2.group(3)}")
            elif line.startswith("## "):
                name = None
    if not out:
        return []
    return ["## b. HFT hypotheses (earlier readers' compositions; proposals to test)"] + out + [""]


def definitional(src: P.Sources, lex: Lex, roots: dict, key_to_rid: dict) -> list[str]:
    out = []
    for rid, d in roots.items():
        if d["kind"] == "echo":
            continue
        for bid, b in d.get("branches", []):
            text = f"{b.get('branch_image_ar', '')} {b.get('source_phrase_ar', '')}"
            hits = {key_to_rid[k] for k in lex.roots(text) if k in key_to_rid} - {rid}
            if hits:
                out.append(f"- {root_label(src, rid)} {bid} «{P.clip(first_phrase(b.get('source_phrase_ar', '')) or b.get('branch_image_ar', ''), 90)}» "
                           f"→ {', '.join(root_label(src, h) for h in sorted(hits))}")
    if not out:
        return []
    return ["## d. Definitional links: a branch whose Arabic image or source phrase uses another root of the window", ""] + out + [""]


def staging(src: P.Sources, lex: Lex, roots: dict, key_to_rid: dict, surah: int) -> list[str]:
    """Windows elsewhere in the Quran whose surface carries the branch images of ≥ 3 of the window's roots."""
    rid_keys = defaultdict(set)
    for k, rid in key_to_rid.items():
        rid_keys[rid].add(k)
    fields = []  # (rid, bid, gloss, field keys)
    for rid, d in roots.items():
        if d["kind"] != "identity":
            continue
        for bid, b in d.get("branches", []):
            g = b.get("concept_gloss")
            g = (g.get("text") if isinstance(g, dict) else g) or ""
            keys = lex.roots(b.get("branch_image_ar", ""))
            try:  # the dictionary's own synonym / same-field neighbours widen the field
                nb = json.loads(b.get("neighbor_distinctions") or "[]")
            except (TypeError, json.JSONDecodeError):
                nb = b.get("neighbor_distinctions") if isinstance(b.get("neighbor_distinctions"), list) else []
            for x in nb:
                if x.get("relation_type") in ("synonym", "same_field", "near_synonym"):
                    keys |= lex.rid_keys.get(x.get("neighbor_ref", "").split("/")[0], set())
            keys = {k for k in keys if lex.df.get(k, 0) <= COMMON_DF and k not in FILLER} - rid_keys[rid]
            if keys:
                fields.append((rid, bid, g, keys))
    N = 6236
    refs = [r for r in src.quran if not r.startswith(f"{surah}:") and not r.endswith(":0")]
    by_surah = defaultdict(list)
    for r in refs:
        by_surah[int(r.split(":")[0])].append(r)
    scored = []
    for s, rs in by_surah.items():
        rs.sort(key=lambda x: int(x.split(":")[1]))
        for i in range(0, max(1, len(rs) - STAGE_W + 1)):
            win = rs[i:i + STAGE_W]
            present = set().union(*(lex.ayah_roots[r] for r in win))
            hit = defaultdict(list)
            for rid, bid, g, keys in fields:
                m = keys & present
                if m:
                    hit[rid].append((bid, g, m))
            surface = {rid for rid in roots if roots[rid]["kind"] == "identity" and rid_keys[rid] & present}
            if len(hit) < 3:
                continue
            own = {r for r in surface if lex.df.get(next(iter(rid_keys[r]), ""), N) <= 1500}
            score = (sum(max(max(math.log(N / lex.df[k]) for k in m) for _, _, m in v) for v in hit.values())
                     * (1 + 0.5 * len(own)) / math.sqrt(len(present)))  # dense, not merely long; own roots on the surface
            scored.append((score, win, hit, surface))
    scored.sort(key=lambda x: -x[0])
    out, used = [], set()
    for score, win, hit, surface in scored:
        if any(r in used for r in win):
            continue
        used |= set(win)
        best = []
        for rid, v in sorted(hit.items(), key=lambda x: root_label(src, x[0])):
            bid, g, m = max(v, key=lambda t: max(math.log(N / lex.df[k]) for k in t[2]))
            best.append(f"{root_label(src, rid)} {bid} {g} [{', '.join(P.spaced(k) for k in sorted(m))}]")
        out.append(f"- **{win[0]}–{win[-1].split(':')[1]}** (own roots on the surface: "
                   f"{', '.join(root_label(src, r) for r in sorted(surface)) or '—'}): " + "; ".join(best))
        if len(out) >= STAGE_TOP:
            break
    if not out:
        return []
    return ["## c. Surface staging: Quran passages that tell the window's branch images openly, with other words",
            "", "Each passage lists, per root of this surah, its branch whose image words (in brackets, as roots; widened by",
            "the dictionary's synonym and same-field neighbours) occur on that passage's surface. Candidates only: many",
            "are generic; recall the passage before using it.", ""] + out + [""]


def pairs(refs: list[str], surah: int) -> list[str]:
    seen, out = set(), []
    for ref in refs:
        f = V9 / "input" / "v2" / f"s{surah:03d}" / ref.replace(":", "_") / "03_pairs.md"
        if not f.exists():
            continue
        root = None
        for line in f.read_text(encoding="utf-8").splitlines():
            if line.startswith("## "):
                root = line[3:].split(" (")[0]
            m = re.match(r"\s*- \*\*(B\d+)\*\*", line)
            if m:
                cur = f"{root} {m.group(1)}"
            m = re.match(r"\s*- (near|surah): (.*)", line)
            if m and root:
                key = (cur, m.group(2))
                if key not in seen:
                    seen.add(key)
                    out.append(f"- {cur} ↔ {m.group(2)}")
    if not out:
        return []
    return ["## e. Network pairs (branch images of different ayat that the semantic network links; candidates)", ""] + out + [""]


def build(surah: int, arm: str, with_pairs: bool = False, with_hft: bool = True) -> list[Path]:
    src = P.Sources()
    n = max(int(r.split(":")[1]) for r in src.quran if r.startswith(f"{surah}:"))
    lex = Lex(src)
    made = []
    for lo, hi in windows(surah, n):
        refs = [f"{surah}:{a}" for a in range(lo, hi + 1)]
        name = "all" if (lo, hi) == (1, n) else f"{lo}-{hi}"
        out = V11 / "out" / "arms" / arm / f"s{surah:03d}" / "seeds" / name
        out.mkdir(parents=True, exist_ok=True)
        table, roots, key_to_rid = branch_table(src, refs)
        text = [f"# Seed-pass evidence for surah {surah}, ayat {lo}–{hi} (script, unjudged)", ""]
        text += ["## The window's text", ""] + [f"- {r} {src.quran[r]}" for r in refs] + [""]
        text += table + (hft(refs, surah) if with_hft else []) + staging(src, lex, roots, key_to_rid, surah) + \
            definitional(src, lex, roots, key_to_rid) + (pairs(refs, surah) if with_pairs else [])
        f = out / "seeds_input.md"
        f.write_text("\n".join(text) + "\n", encoding="utf-8")
        made.append(f)
        print(f"{f} ({f.stat().st_size:,} bytes)")
    return made


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("surah", type=int)
    ap.add_argument("--arm", default="S")
    ap.add_argument("--list", action="store_true", help="only print the windows")
    ap.add_argument("--no-hft", action="store_true", help="leave out the HFT hypotheses (arm S0)")
    ap.add_argument("--pairs", action="store_true", help="add the network pairs (e); off by default (size)")
    a = ap.parse_args()
    if a.list:
        src_n = sum(1 for line in P.QURAN_TEXT.read_text(encoding="utf-8").splitlines() if line.startswith(f"{a.surah}|") or line.startswith(f"{a.surah}:"))
        print(windows(a.surah, src_n))
        return
    build(a.surah, a.arm, a.pairs, not a.no_hft)


if __name__ == "__main__":
    main()
