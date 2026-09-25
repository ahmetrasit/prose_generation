"""Render a V9 ayah package (v2): small markdown files an agent reads whole.

Context is the whole host surah (no pericopes) plus the Fatiha lens.
Sources are read directly; nothing is summarised by a model.

  bundle      bundles/sNNN/S_A.ayah.json              (HFT, word analysis, leads)
  QAC         quran-data/data/morphology/qac.sqlite.gz (words, lemmas, roots, counts)
  roots       quran-data/data/bridges/qac-dictionary-root-resolutions.json (identity)
              quran-data/data/bridges/qac-dictionary-word-root-analyses.json (word-scoped alternatives)
              quran-data/data/bridges/qac-furuq-v4-root-map.sqlite.gz (observed targets -> echo roots)
  dictionary  quran-data/data/dictionary/tr/           (Turkish branch entries)
  cards       quran-slm resources/source/corpus_branches_ar.tsv (Arabic branch cards)
  network     quran-slm artifacts corpus_network + corpus_ensemble (global directional ranks)
  inter-ayah  quran-data .../inter-ayah/reciprocal/focus_S_A_cutoff_100.tsv
  text        quran-data/data/text/quran-uthmani.tsv
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import math
import re
import shutil
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

PG = Path(__file__).resolve().parents[2]
PROJECTS = PG.parent
QD = PROJECTS / "quran-data" / "data"
QS = PROJECTS / "quran-slm"
CACHE = Path(__file__).resolve().parent / ".cache"
DICT_DIR = QD / "dictionary" / "tr"
QURAN_TEXT = QD / "text" / "quran-uthmani.tsv"
RECIPROCAL_DIR = QD / "analysis" / "inter-ayah" / "reciprocal"
GATEWAY = QD / "bridges" / "qac-dictionary-root-resolutions.json"
WORD_ALTS = QD / "bridges" / "qac-dictionary-word-root-analyses.json"
ROOTMAP_GZ = QD / "bridges" / "qac-furuq-v4-root-map.sqlite.gz"
QAC_GZ = QD / "morphology" / "qac.sqlite.gz"
CARDS_TSV = QS / "resources" / "source" / "corpus_branches_ar.tsv"
NET = QS / "artifacts" / "corpus_network"
NEO = QS / "artifacts" / "corpus_ensemble"

WINDOW = 7          # near window for pairs and bridges (ayat)
K_SAME, K_NEAR, K_FAR, K_FATIHA = 3, 3, 2, 3
BRIDGES_MAX = 60
CONCEPT_TARGETS = 10  # concept paths kept per focus root, richest first
RARE_LEMMA = 20     # usage profile lists every occurrence at or below this count

csv.field_size_limit(10**9)


def clip(s: str, n: int) -> str:
    s = " ".join((s or "").split())
    return s if len(s) <= n else s[: n - 1] + "…"


def spaced(join_key: str) -> str:
    return " ".join(join_key)


# ---------------------------------------------------------------- sources

def _gunzip(src: Path, name: str) -> Path:
    CACHE.mkdir(exist_ok=True)
    dst = CACHE / name
    if not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime:
        with gzip.open(src) as f, dst.open("wb") as g:
            shutil.copyfileobj(f, g)
    return dst


class Sources:
    def __init__(self) -> None:
        self.quran = {}
        for line in QURAN_TEXT.read_text(encoding="utf-8").splitlines():
            ref, _, ar = line.partition("|")
            self.quran[ref.strip()] = ar.strip().lstrip("﻿")
        self.qac = sqlite3.connect(_gunzip(QAC_GZ, "qac.sqlite"))
        self.rootmap = sqlite3.connect(_gunzip(ROOTMAP_GZ, "rootmap.sqlite"))
        gw = json.loads(GATEWAY.read_text(encoding="utf-8"))
        self.gateway = {r["qacRootJoinKey"]: r for r in gw["roots"]}
        self.word_alts = json.loads(WORD_ALTS.read_text(encoding="utf-8"))["records"]
        self.cards = {}
        self.root_name = {}
        with CARDS_TSV.open(encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                self.cards[row["node_id"]] = row
                self.root_name.setdefault(row["source_root_id"], row["surface_root"])
        cat = json.loads((NET / "catalog.json").read_text(encoding="utf-8"))["cards"]
        self.net_ids = [c["node_id"] for c in cat]
        self.net_ix = {k: i for i, k in enumerate(self.net_ids)}
        self.branches_of = defaultdict(list)  # root_id -> [node_id] in network order
        for c in cat:
            if c["origin_corpus"] == "quranic":
                self.branches_of[c["source_root_id"]].append(c["node_id"])
        n = len(cat)
        self.ranks = [
            (0.35, np.memmap(NET / "e5_directional_rank.u16le", dtype="<u2", mode="r", shape=(n, n))),
            (0.35, np.memmap(NEO / "neoarabert_directional_rank.u16le", dtype="<u2", mode="r", shape=(n, n))),
            (0.30, np.memmap(NET / "character_directional_rank.u16le", dtype="<u2", mode="r", shape=(n, n))),
        ]
        self._dict = {}
        self._rows = {}

    # -- dictionary
    def entry(self, root_id: str) -> dict:
        if root_id not in self._dict:
            p = DICT_DIR / f"{root_id}_entry.json"
            self._dict[root_id] = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
        return self._dict[root_id]

    def branch(self, node_id: str) -> dict:
        _, rid, bid = node_id.split(":")
        for b in self.entry(rid).get("branches", []):
            if b.get("branch_ref", "").endswith("/" + bid):
                return b
        return {}

    def gloss(self, node_id: str) -> str:
        g = self.branch(node_id).get("concept_gloss")
        return (g.get("text") if isinstance(g, dict) else g) or ""

    def image(self, node_id: str) -> str:
        return self.branch(node_id).get("branch_image_ar") or self.cards.get(node_id, {}).get("branch_image_ar", "")

    def label(self, node_id: str) -> str:
        _, rid, bid = node_id.split(":")
        return f"{self.root_name.get(rid, rid)} {bid} {self.gloss(node_id) or '—'} / {self.image(node_id) or '—'}"

    # -- QAC words and roots
    def words(self, ref: str) -> list[dict]:
        s, a = (int(x) for x in ref.split(":"))
        cur = self.qac.execute(
            "select qac_word_ref, word_index, surface_ar, root_join_keys, lemmas_ar, pos_tags "
            "from qac_words where surah=? and ayah=? order by word_index", (s, a))
        return [dict(zip(("ref", "w", "surface", "roots", "lemmas", "pos"), r)) for r in cur]

    def word_roots(self, word: dict) -> dict:
        """Gateway identity roots, word-scoped alternatives and echo roots for one QAC word."""
        ident, alts, echo = [], [], []
        keys = [k for k in word["roots"].split(";") if k]
        for key in keys:
            row = self.gateway.get(key)
            if row:
                ident += row["rootIds"]
                echo += [(t, "withheld observed target") for t in row["withheldTargetIds"]
                         if t not in [e[0] for e in echo]]
            for rid, occ in self.rootmap.execute(
                    "select furuq_root_id, occurrences from qac_furuq_targets "
                    "where qac_root_join_key=? and is_dominant=0", (key,)):
                if rid not in (row or {}).get("rootIds", []) and rid not in [e[0] for e in echo]:
                    echo.append((rid, f"non-dominant observed target ({occ} occ.)"))
            for rec in self.word_alts:
                sel = rec["selector"]
                if sel["qacRootJoinKey"] != key:
                    continue
                refs = [r[0] for r in self.qac.execute(
                    "select qac_ref from qac_morphemes where qac_word_ref=?", (word["ref"],))]
                lem_hit = "qacLemma" in sel and sel["qacLemma"] in word["lemmas"].split(";")
                ref_hit = "qacRef" in sel and sel["qacRef"] in refs
                if lem_hit or ref_hit:
                    for an in rec["analyses"]:
                        if an["standing"] != "primary" and an.get("dictionaryRootId"):
                            alts.append((an["dictionaryRootId"], an.get("attributionTr", "")))
        echo = [(r, why) for r, why in echo if r not in ident and r not in [a[0] for a in alts]]
        return {"keys": keys, "identity": list(dict.fromkeys(ident)), "alternatives": alts, "echo": echo}

    def ayah_branches(self, ref: str, include_echo: bool = False) -> list[tuple[str, dict]]:
        out = []
        for w in self.words(ref):
            r = self.word_roots(w)
            roots = r["identity"] + [a[0] for a in r["alternatives"]] + ([e[0] for e in r["echo"]] if include_echo else [])
            for rid in dict.fromkeys(roots):
                for nid in self.branches_of.get(rid, []):
                    out.append((nid, w))
        return out

    # -- network affinity (rows only; symmetric reciprocal-rank fusion)
    def _row(self, node_id: str) -> list[np.ndarray]:
        if node_id not in self._rows:
            i = self.net_ix[node_id]
            self._rows[node_id] = [np.asarray(m[i]).astype(np.float32) for _, m in self.ranks]
        return self._rows[node_id]

    def affinity(self, a: str, pool: list[str]) -> np.ndarray:
        ra = self._row(a)
        idx = np.array([self.net_ix[p] for p in pool])
        out = np.zeros(len(pool), dtype=np.float32)
        for k, (w, _) in enumerate(self.ranks):
            r_ab = ra[k][idx]
            r_ba = np.asarray(self.ranks[k][1][idx, self.net_ix[a]]).astype(np.float32)
            aff = 0.5 * (1 / (10 + r_ab) + 1 / (10 + r_ba))
            aff[r_ab == 0] = 0
            out += w * aff
        return out

    def usage(self, key: str, lemma: str) -> list[tuple]:
        return list(self.qac.execute(
            "select distinct surah, ayah, surface_ar from qac_morphemes where root_join_key=? and lemma_ar=? "
            "order by surah, ayah", (key, lemma)))


def root_of(node_id: str) -> str:
    return node_id.split(":")[1]


def top_fast(src: Sources, a: str, pool: list[str], k: int, shortlist: int = 60) -> list[tuple[str, float]]:
    """Shortlist by forward ranks (one row read), then exact symmetric affinity; one result per root."""
    pool = [p for p in dict.fromkeys(pool) if p in src.net_ix and root_of(p) != root_of(a)]
    if not pool:
        return []
    fwd = src._row(a)
    idx = np.array([src.net_ix[p] for p in pool])
    score = sum(np.where(fwd[i][idx] == 0, 0, w / (10 + fwd[i][idx])) for i, (w, _) in enumerate(src.ranks))
    cand = [pool[i] for i in np.argsort(-score)[:shortlist]]
    aff = src.affinity(a, cand)
    seen, out = set(), []
    for i in np.argsort(-aff):
        if root_of(cand[i]) in seen:
            continue
        seen.add(root_of(cand[i]))
        out.append((cand[i], float(aff[i])))
        if len(out) == k:
            break
    return out


def top_distinct(src: Sources, a: str, pool: list[tuple[str, str]], k: int) -> list[tuple[str, str, float]]:
    """pool: (node_id, where). Top-k by affinity, one per partner root, excluding a's root."""
    pool = list({n: (n, where) for n, where in reversed(pool)
                 if root_of(n) != root_of(a) and n in src.net_ix}.values())[::-1]
    if not pool:
        return []
    aff = src.affinity(a, [n for n, _ in pool])
    seen, out = set(), []
    for i in np.argsort(-aff):
        n, where = pool[i]
        if root_of(n) in seen:
            continue
        seen.add(root_of(n))
        out.append((n, where, float(aff[i])))
        if len(out) == k:
            break
    return out


# ---------------------------------------------------------------- sections

def section_ayah(src: Sources, ref: str, bundle: dict) -> str:
    lines = [f"# {ref} — focus", "", src.quran[ref], ""]
    tr = (bundle.get("v12_cross_run_publication") or {}).get("baseline", {}).get("text")
    if tr:
        lines += ["Anchor translation (canonical reading, reference only):", "", tr, ""]
    lines += ["## Words (QAC; roots via quran-data gateway)", "", "| w | surface | lemma | root | pos |", "|---|---|---|---|---|"]
    for w in src.words(ref):
        lines.append(f"| {w['w']} | {w['surface']} | {w['lemmas']} | {' / '.join(spaced(k) for k in w['roots'].split(';') if k)} | {w['pos']} |")
    lines += ["", "## Word notes (precomputed word analysis; support, not obligations)", ""]
    for w in (bundle.get("word_analysis") or {}).get("words", []):
        topics = "; ".join(t["headline"] for t in w.get("topics", []) if t.get("status") != "dropped")
        surf = w.get("surface_display", "").replace("{{ar:", "").replace("}}", "").split(" (")[0]
        lines.append(f"- {w['aligned_qac_word_ref']} {surf}: {clip(w.get('gloss_range', ''), 220)}"
                     + (f" — topics: {topics}" if topics else ""))
    return "\n".join(lines) + "\n"


def dict_lines(src: Sources, rid: str) -> list[str]:
    e = src.entry(rid)
    if not e:
        return [f"- ({rid}) no Turkish dictionary entry", ""]
    prof = e.get("root_profile") or {}
    lines = [clip(prof.get("summary", ""), 400), ""]
    for b in e.get("branches", []):
        cm = b.get("concept_map") or {}
        facets = " / ".join(f.get("statement", "") for f in cm.get("facets", []))
        g = b.get("concept_gloss")
        g = (g.get("text") if isinstance(g, dict) else g) or ""
        lines.append(
            f"- **{b['branch_ref'].split('/')[-1]}** {g} | {b.get('branch_image_ar', '')} | "
            f"{clip(cm.get('definition', ''), 260)} | facets: {clip(facets, 300)} | "
            f"not: {clip(b.get('what_is_not_ar', ''), 120)} | src: {clip(b.get('source_phrase_ar', ''), 220)}")
    return lines + [""]


def section_dictionary(src: Sources, ref: str) -> str:
    lines = ["# Dictionary — every branch of every focus root", "",
             "One line per branch: gloss | Arabic image | definition | facets | not | source phrase.",
             "Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this",
             "exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.", ""]
    done = set()
    analysed = [(w, src.word_roots(w)) for w in src.words(ref)]
    for w, r in analysed:
        for rid in r["identity"]:
            if rid in done:
                continue
            done.add(rid)
            lines += [f"## {src.root_name.get(rid, rid)} ({rid}) — identity root of {w['surface']} (w{w['w']})", ""]
            lines += dict_lines(src, rid)
    for w, r in analysed:
        for rid, why in r["alternatives"]:
            if rid in done:
                continue
            done.add(rid)
            lines += [f"## {src.root_name.get(rid, rid)} ({rid}) — documented alternative for {w['surface']}: {clip(why, 160)}", ""]
            lines += dict_lines(src, rid)
    for w, r in analysed:
        for rid, why in r["echo"]:
            if rid in done:
                continue
            done.add(rid)
            lines += [f"## ECHO {src.root_name.get(rid, rid)} ({rid}) — for {w['surface']} (w{w['w']}): {why}; not identity", ""]
            lines += dict_lines(src, rid)
    return "\n".join(lines) + "\n"


def resolve_trace_step(src: Sources, step: dict) -> str:
    ref = step.get("source_ref", "")
    idxs = [str(i) for i in step.get("source_word_indices") or []]
    words = {str(w["w"]): w["surface"] for w in src.words(ref)} if ref else {}
    surf = " ".join(words.get(i, f"w{i}?") for i in idxs) or "?"
    nid = f"quranic:{step.get('mapped_root_id', '')}:{step.get('branch_id', '')}"
    return f"  - {ref} w{','.join(idxs)} **{surf}** ({step.get('root', '')} {step.get('branch_id')}: " \
           f"{src.gloss(nid) or '—'} / {src.image(nid) or '—'}) — {step.get('role', '')}"


def section_hft(src: Sources, bundle: dict) -> str:
    lines = ["# HFT — precomputed activation hypotheses (whole-surah window)", "",
             "Each record: changed reading, mechanism, and every trace step resolved to the actual word.",
             "Note: HFT used an older root map; a trace step on a root the gateway now withholds is an echo, not identity.", ""]
    readers = (bundle.get("v12_focus_trace_hermetic") or {}).get("readers", {})
    for r in readers.values():
        for kind in ("baseline_models", "context_deltas", "surprising_valid_outliers"):
            for rec in r.get(kind, []) or []:
                cr = rec.get("changed_reading") or {}
                name = rec.get("model_id") or rec.get("delta_id") or rec.get("outlier_id")
                lines += [f"## {name} [{kind.rstrip('s')}, {rec.get('confidence', '?')}]", "",
                          f"- before: {cr.get('before', '')}", f"- after: {cr.get('after', '')}",
                          f"- mechanism: {rec.get('mechanism', '')}"]
                if rec.get("containment"):
                    lines.append(f"- containment: {rec['containment']}")
                lines.append("- trace:")
                lines += [resolve_trace_step(src, s) for s in rec.get("activation_trace", [])]
                lines.append("")
        summ = r.get("summary") or {}
        if summ:
            lines += ["## HFT reader overview", ""]
            for k, v in summ.items():
                for x in (v if isinstance(v, list) else [v]):
                    lines.append(f"- {k}: {x}")
            lines.append("")
    return "\n".join(lines) + "\n"


def ayah_refs(surah: int, src: Sources) -> list[str]:
    out, a = [], 1
    while f"{surah}:{a}" in src.quran:
        out.append(f"{surah}:{a}")
        a += 1
    return out


def section_pairs(src: Sources, ref: str, focus: list[tuple[str, dict]], surah_ctx: dict) -> str:
    s, a = (int(x) for x in ref.split(":"))
    same = [(n, f"{ref} {w['surface']}") for n, w in focus]
    near = [(n, f"{r} {w['surface']}") for r, bl in surah_ctx.items() if r != ref and abs(int(r.split(':')[1]) - a) <= WINDOW for n, w in bl]
    far = [(n, f"{r} {w['surface']}") for r, bl in surah_ctx.items() if abs(int(r.split(':')[1]) - a) > WINDOW for n, w in bl]
    near.sort(key=lambda x: abs(int(x[1].split()[0].split(":")[1]) - a))  # a repeated branch is labelled
    far.sort(key=lambda x: abs(int(x[1].split()[0].split(":")[1]) - a))   # by its nearest occurrence
    lines = ["# Branch-image pairs (global network, gateway roots; top by distinct partner root)", "",
             f"For every branch of every focus root: partners in the same ayah (top {K_SAME}), within ±{WINDOW} ayat "
             f"(top {K_NEAR}), and elsewhere in the surah (top {K_FAR}). A pair is a candidate only; judge whether it opens a reading.", ""]
    by_root = defaultdict(list)
    for n, w in focus:
        by_root[root_of(n)].append((n, w))
    count = 0
    for rid, items in by_root.items():
        surfaces = ", ".join(dict.fromkeys(w["surface"] for _, w in items))
        lines += [f"## {src.root_name.get(rid, rid)} ({surfaces})", ""]
        for n in dict.fromkeys(nn for nn, _ in items):
            lines.append(f"- **{n.split(':')[-1]}** {src.gloss(n) or '—'} / {src.image(n) or '—'}")
            for lab, pool, k in (("same", same, K_SAME), ("near", near, K_NEAR), ("far", far, K_FAR)):
                for p, where, _ in top_distinct(src, n, pool, k):
                    lines.append(f"  - {lab}: {src.label(p)} ← {where}")
                    count += 1
        lines.append("")
    lines.insert(4, f"Pairs listed: {count}.")
    return "\n".join(lines) + "\n"


def section_bridges(src: Sources, ref: str, focus: list[tuple[str, dict]], surah_ctx: dict) -> str:
    a = int(ref.split(":")[1])
    ctx = [(n, r, w) for r, bl in surah_ctx.items() if r != ref and abs(int(r.split(':')[1]) - a) <= WINDOW for n, w in bl]
    ids = [n for n, _, _ in ctx]
    top = {}
    for i, (n, r, _) in enumerate(ctx):
        pool = [(m, j) for j, (m, rr, _) in enumerate(ctx) if rr != r]
        best = top_distinct(src, n, [(m, str(j)) for m, j in pool], 2)
        top[i] = {int(j) for _, j, _ in best}
    mutual = {(min(i, j), max(i, j)) for i in top for j in top[i] if i in top.get(j, set())}
    focus_ids = list(dict.fromkeys(n for n, _ in focus))
    scored = []
    for i, j in mutual:
        link = []
        for end in (i, j):
            aff = src.affinity(ids[end], focus_ids)
            k = int(np.argmax(aff))
            link.append((float(aff[k]), focus_ids[k]))
        best = max(link)
        scored.append((best[0], i, j, best[1]))
    scored.sort(reverse=True)
    lines = [f"# Bridges — context↔context links within ±{WINDOW} (mutual top-2, different ayat)", "",
             f"{len(mutual)} mutual bridges; the {min(BRIDGES_MAX, len(scored))} most linked to a focus branch are listed.",
             "Each line: bridge (A ⇄ B) and the focus branch it connects to most (a two-step path).", ""]
    for s_, i, j, fb in scored[:BRIDGES_MAX]:
        (ni, ri, wi), (nj, rj, wj) = ctx[i], ctx[j]
        lines.append(f"- {ri} {wi['surface']} {src.label(ni)} ⇄ {rj} {wj['surface']} {src.label(nj)}"
                     f"  ‖ focus: {src.label(fb)}")
    return "\n".join(lines) + "\n"


def section_usage(src: Sources, ref: str) -> str:
    lines = ["# Concordance and usage profiles (Quranic induction over each focus word)", "",
             "Per focus word: occurrences of its root in this surah; Quran-wide lemma counts; for rare lemmas, every",
             f"occurrence (≤{RARE_LEMMA}) with the roots that co-occur across them; hapax flags; near-synonym contrasts.", ""]
    s = int(ref.split(":")[0])
    for w in src.words(ref):
        keys = [k for k in w["roots"].split(";") if k]
        if not keys:
            continue
        for key in keys:
            lemma = w["lemmas"].split(";")[-1]
            lines.append(f"## {w['surface']} (w{w['w']}) — root {spaced(key)}, lemma {lemma}")
            in_surah = list(src.qac.execute(
                "select distinct ayah, surface_ar from qac_morphemes where root_join_key=? and surah=? order by ayah", (key, s)))
            lines.append(f"- in surah {s}: " + "; ".join(f"{s}:{a} {sf}" for a, sf in in_surah))
            lem_counts = list(src.qac.execute(
                "select lemma_ar, count(*) from qac_morphemes where root_join_key=? and lemma_ar!='' group by lemma_ar order by 2 desc", (key,)))
            lines.append("- Quran lemmas: " + ", ".join(f"{l} {c}" for l, c in lem_counts))
            occ = src.usage(key, lemma)
            if len(occ) == 1:
                lines.append(f"- **hapax**: lemma {lemma} occurs only here.")
            if 1 < len(occ) <= RARE_LEMMA:
                co = Counter()
                lines.append(f"- every occurrence of {lemma} ({len(occ)}):")
                for os_, oa, sf in occ:
                    r = f"{os_}:{oa}"
                    lines.append(f"  - {r} {sf} | {clip(src.quran.get(r, ''), 160)}")
                    for ww in src.words(r):
                        for k2 in ww["roots"].split(";"):
                            if k2 and k2 != key:
                                co[k2] += 1
                shared = [f"{spaced(k2)} ({c})" for k2, c in co.most_common() if c >= 2][:12]
                if shared:
                    lines.append("  - roots co-occurring in ≥2 of these ayat: " + ", ".join(shared))
            ident = src.word_roots(w)["identity"]
            if ident and len(occ) <= RARE_LEMMA:
                contrasts = []
                for rid in ident[:1]:
                    for n in src.branches_of.get(rid, [])[:2]:
                        pool = [(m, "") for m in src.net_ids if m.startswith("quranic:")]
                        for p, _, _ in top_distinct(src, n, pool, 3):
                            prid = root_of(p)
                            pkey = src.root_name.get(prid, "").replace(" ", "")
                            cnt = src.qac.execute("select count(*) from qac_morphemes where root_join_key=?", (pkey,)).fetchone()[0]
                            refs = [f"{a}:{b}" for a, b in src.qac.execute(
                                "select distinct surah, ayah from qac_morphemes where root_join_key=? limit 8", (pkey,))]
                            contrasts.append(f"{src.label(p)} — Quran {cnt} occ.: {', '.join(refs)}")
                if contrasts:
                    lines.append("- near-synonym contrast (nearest branches of other roots):")
                    lines += [f"  - {c}" for c in dict.fromkeys(contrasts)]
            lines.append("")
    return "\n".join(lines) + "\n"


_DIAC = re.compile(r"[ؐ-ًؚ-ٰٟۖ-ۭـ]")
_STOP = set("""من في على الى إلى عن ما الذي التي اي أي شيء كل اذا إذا ان أن به له هو هي وهو يقال قيل سمي يدخل فيه ولا
لا ليس او أو ثم قد كان يكون الا إلا هذا ذلك غير بعض بين عند حتى مثل معنى اصل أصل واحد يدل منه فهو فهي عليه اليه إليه
الشيء اذ إذ كذا قال قالوا بها لها فيها منها عنه عنها وقد وما ومن وهي وفي ذو ذات""".split())


def concept_tokens(text: str) -> set[str]:
    text = _DIAC.sub("", re.sub(r"\([^)]*\)", " ", text or ""))
    out = set()
    for t in re.findall(r"[ء-ي]+", text):
        for p in ("وبال", "فبال", "وال", "بال", "فال", "كال", "لل", "ال"):
            if t.startswith(p) and len(t) - len(p) >= 3:
                t = t[len(p):]
                break
        if t.endswith("ة") and len(t) > 3:
            t = t[:-1]
        if t.endswith("ا") and len(t) > 3:
            t = t[:-1]
        if len(t) >= 3 and t not in _STOP:
            out.add(t)
    return out


_GENERIC = set("""قال كان جعل امر شيء قوم رجل الله اله ناس انسان فعل عمل اخذ اتي جاء راي علم قول يوم ارض سماء
نفس حق كتاب بعض كل احد مثل خير شر اهل عبد رب ملك دين كفر امن
اسم معروف حال بعد جمع وكل حين حيث لما قدر وقت ذكر اخر كثير قليل قل نسب حسن وصف معني اصل""".split())  # definitional filler


def _lemma_form(t: str, lemmas: set[str]) -> str:
    n = _norm(t)
    if n not in lemmas and t[0] in "لبكفو" and len(t) >= 4 and _norm(t[1:]) in lemmas:
        return _norm(t[1:])
    return n


def _norm(t: str) -> str:
    t = _DIAC.sub("", t).replace("ٱ", "ا").replace("أ", "ا").replace("إ", "ا").replace("آ", "ا").replace("ى", "ي")
    return t[:-1] if t.endswith("ة") else t


def section_concepts(src: Sources, ref: str, focus: list, surah_ctx: dict, targets: list[str]) -> str:
    """Shared-concept threads: Quranic content words shared by branch definitions of different roots.

    A token counts only if it is itself a Quranic lemma (drops lexicographic boilerplate). Threads are ranked by
    lift: how over-represented the concept is in this ayah's scope relative to the whole card catalogue.
    """
    lemmas = {_norm(l) for (l,) in src.qac.execute("select distinct lemma_ar from qac_morphemes where lemma_ar!=''")}
    lemmas -= _GENERIC
    df = Counter()
    card_tokens = {}
    for nid, c in src.cards.items():
        toks = {t for t in (_lemma_form(x, lemmas) for x in concept_tokens(
            " ".join((c["branch_image_ar"], c["what_is_ar"], c["source_phrase_ar"])))) if t in lemmas}
        card_tokens[nid] = toks
        df.update(toks)
    n_cards = len(src.cards)
    a = int(ref.split(":")[1])
    scope = [("focus", ref, n, w) for n, w in focus]
    for r, bl in surah_ctx.items():
        if r != ref and abs(int(r.split(":")[1]) - a) <= WINDOW:
            scope += [("near", r, n, w) for n, w in bl]
    for r in ["1:%d" % i for i in range(1, 8)]:
        scope += [("fatiha", r, n, w) for n, w in src.ayah_branches(r)]
    for r in targets:
        scope += [("target", r, n, w) for n, w in src.ayah_branches(r)]
    seen_scope = set()
    unique_scope = []
    for x in scope:
        if (x[0], x[1], x[2]) not in seen_scope:
            seen_scope.add((x[0], x[1], x[2]))
            unique_scope.append(x)
    scope = unique_scope
    # Concept paths: focus branch -> (image) inter-ayah target branch -> (shared concept) nearby-ayah branch.
    targets_b = {}
    for kind, r, n, w in scope:
        if kind == "target":
            targets_b.setdefault(n, (r, w))
    near_by_token = defaultdict(list)
    for kind, r, n, w in scope:
        if kind == "near":
            for t in card_tokens.get(n, ()):
                near_by_token[t].append((r, n, w))
    lines = ["# Shared-concept links (components shared by branch definitions)", "",
             "Not image pairs: a concept word (e.g. ليل night, عين eye, نسج weaving) that two branches' definitions share.",
             "Grouped by focus root. Each line: focus branch → its image partner in an inter-ayah target ayah ⇒ concept",
             "words that partner shares with branches in nearby ayat (focus → target → nearby). The richest",
             f"{CONCEPT_TARGETS} lines per root are kept.", ""]
    total = 0
    by_root = defaultdict(list)
    for n, _w in focus:
        if n not in by_root[root_of(n)]:
            by_root[root_of(n)].append(n)
    for rid, branches in by_root.items():
        best_via = {}  # target branch -> (affinity, focus branch)
        for f in branches:
            for tnode, aff in top_fast(src, f, list(targets_b), 6):
                if aff > best_via.get(tnode, (-1, None))[0]:
                    best_via[tnode] = (aff, f)
        rows = []
        for tnode, (_aff, f) in sorted(best_via.items(), key=lambda kv: (-kv[1][0], kv[0])):
            cands = []
            for t in card_tokens.get(tnode, ()):
                if df[t] > 800 or any(is_root_form(t, src.root_name.get(root_of(x), "")) for x in (tnode, f)):
                    continue
                hits, roots_seen = [], set()
                for r, n, w in sorted(near_by_token.get(t, []), key=lambda x: (abs(int(x[0].split(":")[1]) - a), x[0], x[1])):
                    if root_of(n) in roots_seen or root_of(n) in (root_of(f), root_of(tnode)):
                        continue
                    if is_root_form(t, src.root_name.get(root_of(n), "")):
                        continue
                    roots_seen.add(root_of(n))
                    hits.append(f"{r} {w['surface']} {src.root_name.get(root_of(n), '')} {n.split(':')[2]}")
                    if len(hits) == 5:
                        break
                if hits:
                    cands.append((math.log(n_cards / df[t]), t, hits))
            cands.sort(key=lambda x: (-x[0], x[1]))
            if cands:
                tr_, tw = targets_b[tnode]
                links = "; ".join(f"[{t}] " + ", ".join(h) for _, t, h in cands[:7])
                score = sum(x[0] for x in cands[:7])
                rows.append((score, f"  - {f.split(':')[2]} ({src.gloss(f) or '—'}) → {tr_} {tw['surface']} {short(src, tnode)} ⇒ {links}"))
        rows = [r for _, r in sorted(rows, key=lambda x: (-x[0], x[1]))[:CONCEPT_TARGETS]]
        if rows:
            word = ", ".join(dict.fromkeys(w["surface"] for n, w in focus if root_of(n) == rid))
            lines.append(f"- **{src.root_name.get(rid, rid)} ({word})**")
            lines += rows
            total += len(rows)
    lines.insert(6, f"Paths listed: {total}.")
    return "\n".join(lines) + "\n"


def short(src: Sources, node_id: str) -> str:
    _, rid, bid = node_id.split(":")
    return f"{src.root_name.get(rid, rid)} {bid} {src.image(node_id) or src.gloss(node_id) or '—'}"


def is_root_form(token: str, root_name: str) -> bool:
    """True when the token looks like a form of the given root (its strong radicals in order, at most one
    letter apart)."""
    strong = [c for c in root_name.replace(" ", "") if c not in "اويىءأإآؤئ"]
    strong = [c for i, c in enumerate(strong) if i == 0 or c != strong[i - 1]]
    if len(strong) < 2:
        return False
    return re.search(".?".join(strong), token) is not None


def section_fatiha(src: Sources, ref: str, focus: list) -> str:
    lines = ["# Fatiha lens (recited in every salah; standing context)", ""]
    fat = []
    for i in range(1, 8):
        r = f"1:{i}"
        lines.append(f"- {r} {src.quran[r]}")
        fat += [(n, f"{r} {w['surface']}") for n, w in src.ayah_branches(r)]
    lines += ["", f"## Focus branches × Fatiha branches (top {K_FATIHA} by distinct root)", ""]
    for n in dict.fromkeys(nn for nn, _ in focus):
        tops = top_distinct(src, n, fat, K_FATIHA)
        if tops:
            lines.append(f"- **{src.label(n)}**")
            lines += [f"  - {src.label(p)} ← {where}" for p, where, _ in tops]
    return "\n".join(lines) + "\n"


def section_surah(src: Sources, ref: str) -> str:
    s = int(ref.split(":")[0])
    lines = [f"# Surah {s} — full text (context; no pericope)", ""]
    for r in ayah_refs(s, src):
        lines.append(f"- {r}{' ◀ focus' if r == ref else ''} {src.quran[r]}")
    return "\n".join(lines) + "\n"


def section_inter_ayah(src: Sources, ref: str) -> tuple[str, list[str]]:
    s, a = ref.split(":")
    rows = list(csv.DictReader((RECIPROCAL_DIR / f"focus_{s}_{a}_cutoff_100.tsv").open(encoding="utf-8"), delimiter="\t"))
    by_target = defaultdict(list)
    for r in rows:
        by_target[r["target_ref"]].append(r)
    focus_keys = {k for w in src.words(ref) for k in w["roots"].split(";") if k}

    def signature(t):
        keys = {k for w in src.words(t) for k in w["roots"].split(";") if k}
        return tuple(sorted(keys & focus_keys))

    groups = defaultdict(list)
    for t in by_target:
        sig = signature(t)
        groups[sig if len(sig) >= 3 else ("single", t)].append(t)
    for sig in [g for g, ts in groups.items() if g[0] != "single" and len(ts) < 2]:
        for t in groups.pop(sig):
            groups[("single", t)].append(t)

    def row_lines(t, rs):
        out = []
        for r in rs:
            if r["record_type"] == "directional_review":
                out.append(f"- review {ref}→{t}: {r['focus_direction_label']} — {r['source_note']}")
            else:
                out.append(f"- from {r['source_focus_ref']}→{ref} ({r['record_type'].replace('reciprocal_', '')}, "
                           f"{r['source_direction_label']}): {r['source_note']}")
        return out

    def text_lines(t, neighbours=True):
        ts, ta = t.split(":")
        neighbours = neighbours and any(
            (r["focus_direction_label"] if r["record_type"] == "directional_review" else r["source_direction_label"])
            == "strong" for r in by_target[t])
        rng = (int(ta) - 1, int(ta), int(ta) + 1) if neighbours else (int(ta),)
        return [f"  - {'**' + f'{ts}:{n}' + '**' if n == int(ta) else f'{ts}:{n}'} {src.quran[f'{ts}:{n}']}"
                for n in rng if f"{ts}:{n}" in src.quran and n > 0]

    lines = [f"# Inter-ayah rows (reciprocal) — {len(rows)} records, {len(by_target)} target ayat", "",
             "Labels are earlier review judgements, not decisions. Targets that share ≥3 focus roots are grouped as",
             "one formula: the first member carries neighbouring ayat, the rest only their own text. Only targets with a strong",
             "row carry neighbouring ayat.", ""]
    i = 0
    for sig, ts in sorted(groups.items(), key=lambda kv: (kv[0][0] == "single", -len(kv[1]))):
        if sig[0] != "single":
            lines.append(f"## Formula group ({' + '.join(spaced(k) for k in sig)}) — {len(ts)} targets")
            for n, t in enumerate(ts):
                i += 1
                lines.append(f"### {i}. {t}")
                lines += row_lines(t, by_target[t]) + text_lines(t, neighbours=(n == 0))
            lines.append("")
        else:
            t = ts[0]
            i += 1
            lines.append(f"## {i}. {t}")
            lines += row_lines(t, by_target[t]) + text_lines(t) + [""]
    return "\n".join(lines) + "\n", list(by_target)


def section_people(src: Sources, ref: str, targets: list[str]) -> str:
    """Every other ayah naming the same people (QAC proper nouns of the focus ayah); shared focus roots are
    shown as a hint, not used as a filter."""
    s, a = (int(x) for x in ref.split(":"))
    q = src.qac.execute
    focus_keys = {k for (k,) in q("select distinct root_join_key from qac_morphemes where surah=? and ayah=? "
                                  "and root_join_key!=''", (s, a))}
    lines = ["# Same people elsewhere (every ayah naming a proper noun of the focus ayah)", "",
             "Every other ayah that names a person or people of the focus ayah, with any other focus roots it shares",
             "(a hint only). Rows marked [inter-ayah] are already in 09_inter_ayah.md; the others appear only here.", ""]
    seen_pn = set()
    for lemma, own, surface in q("select lemma_ar, root_join_key, surface_ar from qac_morphemes where surah=? and "
                                 "ayah=? and pos='PN' order by word_index", (s, a)):
        if lemma in seen_pn:
            continue
        seen_pn.add(lemma)
        refs = sorted({(x, y) for x, y in q("select distinct surah, ayah from qac_morphemes where pos='PN' and "
                                              "lemma_ar=?", (lemma,)) if (x, y) != (s, a)})
        rows = []
        for x, y in refs:
            hits = [(w, k) for w, k in q("select surface_ar, root_join_key from qac_morphemes where surah=? and "
                                         "ayah=? and root_join_key!=''", (x, y)) if k in focus_keys and k != own]
            r = f"{x}:{y}"
            shared = ", ".join(dict.fromkeys(f"{w} ({spaced(k)})" for w, k in hits)) or "no other focus root"
            mark = " [inter-ayah]" if r in targets else ""
            rows.append(f"- **{r}**{mark} — shares {shared}\n  - {src.quran.get(r, '')}")
        if rows:
            lines += [f"## {surface} ({lemma}) — {len(rows)} ayat", ""] + rows + [""]
    return "\n".join(lines) + "\n"


def section_leads(bundle: dict) -> str:
    lines = ["# Other precomputed leads (not available for every surah)", ""]
    for key in ("v12_reader_walks", "v12_reader_walks_wide"):
        for name, walk in (bundle.get(key) or {}).items():
            if isinstance(walk, dict):
                for k, v in walk.items():
                    if k.endswith("_md") and v:
                        lines += [f"## {key} {name}: {k}", "", v.strip(), ""]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- driver

def prepare(ref: str, bundles: Path, out: Path) -> dict:
    surah, ayah = (int(x) for x in ref.split(":"))
    bundle = json.loads((bundles / f"s{surah:03d}" / f"{surah}_{ayah}.ayah.json").read_text(encoding="utf-8"))
    src = Sources()
    focus = src.ayah_branches(ref, include_echo=True)
    surah_ctx = {r: src.ayah_branches(r) for r in ayah_refs(surah, src)}
    inter_text, targets = section_inter_ayah(src, ref)
    out.mkdir(parents=True, exist_ok=True)
    files = {
        "00_ayah.md": section_ayah(src, ref, bundle),
        "01_dictionary.md": section_dictionary(src, ref),
        "02_hft.md": section_hft(src, bundle),
        "03_pairs.md": section_pairs(src, ref, focus, surah_ctx),
        "04_bridges.md": section_bridges(src, ref, focus, surah_ctx),
        "05_usage.md": section_usage(src, ref),
        "06_concepts.md": section_concepts(src, ref, focus, surah_ctx, targets),
        "07_fatiha.md": section_fatiha(src, ref, focus),
        "08_surah.md": section_surah(src, ref),
        "09_inter_ayah.md": inter_text,
        "10_leads.md": section_leads(bundle),
        "11_people.md": section_people(src, ref, targets),
    }
    report = {}
    for name, text in files.items():
        (out / name).write_text(text, encoding="utf-8")
        report[name] = len(text.encode("utf-8"))
    return report


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ayah", required=True)
    ap.add_argument("--bundles", default=str(PG / "bundles"))
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    print(json.dumps(prepare(a.ayah, Path(a.bundles), Path(a.out)), indent=1))


if __name__ == "__main__":
    main()
