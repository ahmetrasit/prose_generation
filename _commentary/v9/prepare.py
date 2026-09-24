"""Render a V9 ayah package: small markdown files an agent reads whole.

Pilot scope: one numbered focus ayah with its whole host surah as context.
Sources are read directly; nothing is summarised by a model.

  bundle      bundles/sNNN/S_A.ayah.json         (word analysis, HFT, QAC, walks)
  dictionary  quran-data/data/dictionary/tr/     (Turkish branch entries)
  QAC         quran-slm resources qac_root_ayah  (root -> word surfaces per ayah)
  network     quran-slm surah_networks_global_ensemble/sNNN (branch affinities)
  inter-ayah  quran-data .../inter-ayah/reciprocal/focus_S_A_cutoff_100.tsv
  text        quran-data/data/text/quran-uthmani.tsv
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

import numpy as np

PG = Path(__file__).resolve().parents[2]
PROJECTS = PG.parent
QD = PROJECTS / "quran-data" / "data"
QS = PROJECTS / "quran-slm"
DICT_DIR = QD / "dictionary" / "tr"
QURAN_TEXT = QD / "text" / "quran-uthmani.tsv"
RECIPROCAL_DIR = QD / "analysis" / "inter-ayah" / "reciprocal"
QAC_ROOT_AYAH = QS / "resources" / "source" / "qac_root_ayah.tsv"
NETWORK_DIR = QS / "artifacts" / "surah_networks_global_ensemble"

csv.field_size_limit(10**9)


# ---------------------------------------------------------------- sources

def load_quran_text() -> dict[str, str]:
    text = {}
    for line in QURAN_TEXT.read_text(encoding="utf-8").splitlines():
        ref, _, ar = line.partition("|")
        text[ref.strip()] = ar.strip().lstrip("﻿")
    return text


def load_qac_surfaces(surahs: set[int]) -> dict[tuple[str, str], dict[str, str]]:
    """(root_norm, ayah_ref) -> {word_index: surface}."""
    out: dict[tuple[str, str], dict[str, str]] = {}
    with QAC_ROOT_AYAH.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            if int(row["surah"]) not in surahs:
                continue
            idx = row["word_indices"].split(";")
            surf = row["surfaces_ar"].split(";")
            out[(row["root_norm"], row["ayah_ref"])] = dict(zip(idx, surf))
    return out


_dict_cache: dict[str, dict] = {}
_root_names: dict[str, str] = {}


def root_name(root_id: str) -> str:
    """Arabic root letters for a dictionary root id (from the quran-slm branch snapshot)."""
    if not _root_names:
        with (QS / "resources" / "source" / "corpus_branches_ar.tsv").open(encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                _root_names.setdefault(row["source_root_id"], row["surface_root"])
    return _root_names.get(root_id, "")


def dictionary_entry(root_id: str) -> dict:
    if root_id not in _dict_cache:
        path = DICT_DIR / f"{root_id}_entry.json"
        _dict_cache[root_id] = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    return _dict_cache[root_id]


def branch_entry(root_id: str, branch_id: str) -> dict:
    for b in dictionary_entry(root_id).get("branches", []):
        if b.get("branch_ref", "").endswith("/" + branch_id):
            return b
    return {}


def gloss(b: dict) -> str:
    g = b.get("concept_gloss")
    return (g.get("text") if isinstance(g, dict) else g) or ""


def clip(s: str, n: int) -> str:
    s = " ".join((s or "").split())
    return s if len(s) <= n else s[: n - 1] + "…"


# ---------------------------------------------------------------- sections

def section_ayah(ref: str, bundle: dict, quran: dict[str, str]) -> str:
    lines = [f"# {ref} — focus", "", quran[ref], ""]
    tr = (bundle.get("v12_cross_run_publication") or {}).get("baseline", {}).get("text")
    if tr:
        lines += ["Anchor translation (canonical reading, reference only):", "", tr, ""]
    lines += ["## Words (QAC)", "", "| w | surface | lemma | root | features |", "|---|---|---|---|---|"]
    for m in bundle["qac_morphemes"]:
        if m.get("morpheme_role") == "STEM":
            w = m["qac_word_ref"].split(":")[-1]
            feats = clip(m.get("morph_features", "").replace("STEM|", ""), 60)
            lines.append(f"| {w} | {m['surface_ar']} | {m.get('lemma_ar','')} | {m.get('root_ar','')} | {feats} |")
    lines += ["", "## Word notes (precomputed word analysis; support, not obligations)", ""]
    for w in bundle["word_analysis"]["words"]:
        topics = "; ".join(t["headline"] for t in w.get("topics", []) if t.get("status") != "dropped")
        surf = w.get("surface_display", "").replace("{{ar:", "").replace("}}", "").split(" (")[0]
        lines.append(f"- {w['aligned_qac_word_ref']} {surf}: {clip(w.get('gloss_range',''), 220)}"
                     + (f" — topics: {topics}" if topics else ""))
    return "\n".join(lines) + "\n"


def section_dictionary(root_ids: list[str]) -> str:
    lines = ["# Dictionary — every branch of every focus root", "",
             "One line per branch: gloss | Arabic image | definition | facets | not | source phrase.",
             "Full entries (neighbour distinctions, occurrences) via lookup.py.", ""]
    for rid in root_ids:
        e = dictionary_entry(rid)
        if not e:
            lines += [f"## {rid} — no dictionary entry", ""]
            continue
        prof = e.get("root_profile") or {}
        lines += [f"## {root_name(rid)} ({rid}) — {len(e.get('branches', []))} branches", "",
                  clip(prof.get("summary", ""), 400), ""]
        for b in e.get("branches", []):
            cm = b.get("concept_map") or {}
            facets = " / ".join(f.get("statement", "") for f in cm.get("facets", []))
            lines.append(
                f"- **{b['branch_ref'].split('/')[-1]}** {gloss(b)} | {b.get('branch_image_ar','')} | "
                f"{clip(cm.get('definition',''), 260)} | facets: {clip(facets, 300)} | "
                f"not: {clip(b.get('what_is_not_ar',''), 120)} | src: {clip(b.get('source_phrase_ar',''), 220)}")
        lines.append("")
    return "\n".join(lines) + "\n"


def resolve_trace_step(step: dict, qac: dict) -> str:
    ref = step.get("source_ref", "")
    root = step.get("root", "")
    words = qac.get((root, ref), {})
    idxs = step.get("source_word_indices") or []
    surf = " ".join(words.get(i, f"w{i}?") for i in idxs) or "?"
    b = branch_entry(step.get("mapped_root_id", ""), step.get("branch_id", ""))
    return (f"  - {ref} w{','.join(idxs)} **{surf}** ({root} {step.get('branch_id')}: "
            f"{gloss(b) or '—'} / {b.get('branch_image_ar','—')}) — {step.get('role','')}")


def section_hft(bundle: dict, qac: dict) -> str:
    lines = ["# HFT — precomputed activation hypotheses (whole-surah window)", "",
             "Each record: changed reading, mechanism, and every trace step resolved to the actual word.", ""]
    readers = (bundle.get("v12_focus_trace_hermetic") or {}).get("readers", {})
    for rid, r in readers.items():
        for kind in ("baseline_models", "context_deltas", "surprising_valid_outliers"):
            for rec in r.get(kind, []) or []:
                cr = rec.get("changed_reading") or {}
                lines += [f"## {rec.get('model_id') or rec.get('delta_id') or rec.get('outlier_id')} "
                          f"[{kind.rstrip('s')}, {rec.get('confidence','?')}]", "",
                          f"- before: {cr.get('before','')}",
                          f"- after: {cr.get('after','')}",
                          f"- mechanism: {rec.get('mechanism','')}"]
                if rec.get("containment"):
                    lines.append(f"- containment: {rec['containment']}")
                lines.append("- trace:")
                lines += [resolve_trace_step(s, qac) for s in rec.get("activation_trace", [])]
                lines.append("")
        summ = r.get("summary") or {}
        if summ:
            lines += ["## HFT reader overview", ""]
            for k, v in summ.items():
                vals = v if isinstance(v, list) else [v]
                for x in vals:
                    lines.append(f"- {k}: {x}")
            lines.append("")
    return "\n".join(lines) + "\n"


def section_pairs(surah: int, ayah: int, qac: dict, window: int, k_near: int, k_same: int, k_far: int) -> str:
    net = NETWORK_DIR / f"s{surah:03d}"
    cat = json.loads((net / "catalog.json").read_text(encoding="utf-8"))
    A = np.load(net / "affinity.npy", mmap_mode="r")
    B = cat["branches"]

    def rid(b):  # quranic:root_000672:B010
        return b["node_id"].split(":")[1]

    def top(row, pool, own_root, k):
        seen, out = set(), []
        for b in sorted(pool, key=lambda b: -row[b["index"]]):
            if b["root"] == own_root or b["root"] in seen:
                continue
            seen.add(b["root"])
            out.append(b)
            if len(out) == k:
                break
        return out

    def partner(b, ayat):
        be = branch_entry(rid(b), b["branch_id"])
        words = []
        for a in ayat:
            w = qac.get((b["root"], f"{surah}:{a}"), {})
            if w:
                words.append(f"{surah}:{a} {' '.join(w.values())}")
        return (f"{b['root']} {b['branch_id']} {gloss(be) or '—'} / {be.get('branch_image_ar','—')}"
                f" ← {'; '.join(words) or '?'}")

    focus = [b for b in B if ayah in b["ayahs"]]
    same = [b for b in B if ayah in b["ayahs"]]
    near = [b for b in B if any(abs(a - ayah) <= window and a != ayah for a in b["ayahs"])]
    far = [b for b in B if any(abs(a - ayah) > window for a in b["ayahs"])]

    lines = ["# Branch-image pairs (quran-slm surah network; top by distinct partner root)", "",
             f"For every branch of every focus root: partners in the same ayah (top {k_same}), "
             f"within ±{window} ayat (top {k_near}), and elsewhere in the surah (top {k_far}).",
             "A pair is a candidate only; judge whether it opens a reading.", ""]
    by_root = defaultdict(list)
    for f in focus:
        by_root[f["root"]].append(f)
    n = 0
    for root, fs in by_root.items():
        lines += [f"## {root}", ""]
        for f in sorted(fs, key=lambda b: b["branch_id"]):
            fe = branch_entry(rid(f), f["branch_id"])
            row = np.asarray(A[f["index"]])
            lines.append(f"- **{f['branch_id']}** {gloss(fe) or '—'} / {fe.get('branch_image_ar','—')}")
            for label, pool, k, ayat_of in (
                ("same", same, k_same, lambda b: [ayah]),
                ("near", near, k_near, lambda b: [a for a in b["ayahs"] if abs(a - ayah) <= window and a != ayah]),
                ("far", far, k_far, lambda b: [a for a in b["ayahs"] if abs(a - ayah) > window][:3]),
            ):
                for p in top(row, pool, f["root"], k):
                    lines.append(f"  - {label}: {partner(p, ayat_of(p))}")
                    n += 1
        lines.append("")
    lines.insert(4, f"Pairs listed: {n}.")
    return "\n".join(lines) + "\n"


def section_surah(surah: int, ayah: int, quran: dict[str, str]) -> str:
    lines = [f"# Surah {surah} — full text (context)", ""]
    a = 0
    while f"{surah}:{a + 1}" in quran:
        a += 1
        ref = f"{surah}:{a}"
        mark = " ◀ focus" if a == ayah else ""
        lines.append(f"- {ref}{mark} {quran[ref]}")
    return "\n".join(lines) + "\n"


def section_inter_ayah(ref: str, quran: dict[str, str]) -> str:
    s, a = ref.split(":")
    path = RECIPROCAL_DIR / f"focus_{s}_{a}_cutoff_100.tsv"
    rows = list(csv.DictReader(path.open(encoding="utf-8"), delimiter="\t"))
    by_target = defaultdict(list)
    for r in rows:
        by_target[r["target_ref"]].append(r)
    lines = [f"# Inter-ayah rows (reciprocal) — {len(rows)} records, {len(by_target)} target ayat", "",
             "Labels are earlier review judgements, not decisions. Neighbouring ayat are given for context.", ""]
    for i, (t, rs) in enumerate(by_target.items(), 1):
        ts, ta = t.split(":")
        lines.append(f"## {i}. {t}")
        for r in rs:
            if r["record_type"] == "directional_review":
                lines.append(f"- review {ref}→{t}: {r['focus_direction_label']} — {r['source_note']}")
            else:
                lines.append(f"- from {r['source_focus_ref']}→{ref} ({r['record_type'].replace('reciprocal_','')}, "
                             f"{r['source_direction_label']}): {r['source_note']}")
        for n in (int(ta) - 1, int(ta), int(ta) + 1):
            nref = f"{ts}:{n}"
            if nref in quran and n > 0:
                lines.append(f"  - {'**' + nref + '**' if n == int(ta) else nref} {quran[nref]}")
        lines.append("")
    return "\n".join(lines) + "\n"


def section_leads(bundle: dict) -> str:
    lines = ["# Other precomputed leads (not available for every surah)", ""]
    for name, walk in (bundle.get("v12_reader_walks") or {}).items():
        if isinstance(walk, dict):
            for k, v in walk.items():
                if k.endswith("_md") and v:
                    lines += [f"## walk {name}: {k}", "", v.strip(), ""]
    for name, walk in (bundle.get("v12_reader_walks_wide") or {}).items():
        if isinstance(walk, dict):
            for k, v in walk.items():
                if k.endswith("_md") and v:
                    lines += [f"## wide walk {name}: {k}", "", v.strip(), ""]
    pub = bundle.get("v12_cross_run_publication") or {}
    for f in pub.get("findings", []) or []:
        lines += [f"## published finding", "", json.dumps(f, ensure_ascii=False), ""]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- driver

def prepare(ref: str, bundles: Path, out: Path, window: int, k_near: int, k_same: int, k_far: int) -> dict:
    surah, ayah = (int(x) for x in ref.split(":"))
    bundle = json.loads((bundles / f"s{surah:03d}" / f"{surah}_{ayah}.ayah.json").read_text(encoding="utf-8"))
    quran = load_quran_text()
    targets = {surah}
    qac = load_qac_surfaces(targets)
    root_ids = sorted((bundle.get("root_lexicon") or {}).keys())

    out.mkdir(parents=True, exist_ok=True)
    files = {
        "00_ayah.md": section_ayah(ref, bundle, quran),
        "01_dictionary.md": section_dictionary(root_ids),
        "02_hft.md": section_hft(bundle, qac),
        "03_pairs.md": section_pairs(surah, ayah, qac, window, k_near, k_same, k_far),
        "04_surah.md": section_surah(surah, ayah, quran),
        "05_inter_ayah.md": section_inter_ayah(ref, quran),
        "06_leads.md": section_leads(bundle),
    }
    report = {}
    for name, text in files.items():
        (out / name).write_text(text, encoding="utf-8")
        size = len(text.encode("utf-8"))
        report[name] = {"bytes": size, "approx_tokens": size // 4}
    return report


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ayah", required=True)
    ap.add_argument("--bundles", default=str(PG / "bundles"))
    ap.add_argument("--out", required=True)
    ap.add_argument("--window", type=int, default=3)
    ap.add_argument("--k-near", type=int, default=3)
    ap.add_argument("--k-same", type=int, default=3)
    ap.add_argument("--k-far", type=int, default=2)
    a = ap.parse_args()
    print(json.dumps(prepare(a.ayah, Path(a.bundles), Path(a.out), a.window, a.k_near, a.k_same, a.k_far),
                     indent=1))


if __name__ == "__main__":
    main()
