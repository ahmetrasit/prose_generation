#!/usr/bin/env python3
"""Candidate worklists for the four V9 discovery lines. Scripts retrieve generously; Luna judges.

  local    one item per word of the ayah: QAC identity, the word analysis (every topic with its status, including
           narrowed and dropped ones), the dictionary branches of its roots (gloss + image), variant readings
           (study/_project_corpus/qiraat.tsv, mapped to QAC words)
  usage    one item per content root of the ayah: its whole root family in the Quran (QAC), grouped by lemma and
           form, each occurrence with its ayah text; roots with many occurrences are shown by lemma counts plus the
           focus lemma's occurrences
  surah    the surrounding passage (±7), each focus root's other occurrences in the surah, each HFT record
  related  coherent passages (target ±1): every inter-ayah target (earlier labels shown as hints, never as
           decisions), passages naming the ayah's people, formula families (other ayat sharing ≥2 focus roots)

Output: lines/work/S_A/<line>_<n>.md (bundles ≤ BUNDLE_BYTES) and items.tsv.
Usage: python3 _commentary/v9/lines/candidates.py 18:86
"""
from __future__ import annotations

import csv
import difflib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

V9 = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(V9))
import prepare as P  # noqa: E402

QIRAAT = P.PROJECTS / "study" / "_project_corpus" / "qiraat.tsv"
BUNDLE_BYTES = 40_000
ROOT_FULL_MAX = 60      # a root family with at most this many occurrences is listed in full
LEMMA_LIST_MAX = 40     # otherwise the focus lemma's occurrences, up to this many
PEOPLE_MAX = 60         # a name in more ayat than this is not a people anchor (Allah, Shaytan …)
ROOT_DF_MAX = 400       # formula families use content roots in at most this many ayat
NEAR = 7

DIAC = re.compile(r"[ؐ-ًؚ-ٟۖ-ۭـٰ]")


def skel(t: str) -> str:
    return DIAC.sub("", t or "").translate(str.maketrans("ٱأإآىة", "اااايه"))


def clip(s: str, n: int) -> str:
    s = " ".join((s or "").split())
    return s if len(s) <= n else s[: n - 1] + "…"


def ayah_refs(src, surah: int) -> list[str]:
    return P.ayah_refs(surah, src)


def build(ref: str) -> None:
    src = P.Sources()
    s, a = (int(x) for x in ref.split(":"))
    sa = f"{s}_{a}"
    bundle = json.loads((P.PG / "bundles" / f"s{s:03d}" / f"{sa}.ayah.json").read_text(encoding="utf-8"))
    out = V9 / "lines" / "work" / sa
    out.mkdir(parents=True, exist_ok=True)
    words = src.words(ref)
    content = [w for w in words if w["roots"]]
    items: dict[str, list[tuple[str, str]]] = defaultdict(list)  # line → [(id, text)]

    # ---------------------------------------------------------------- local
    wa = {w.get("aligned_qac_word_ref"): w for w in (bundle.get("word_analysis") or {}).get("words", [])}
    variants = defaultdict(list)
    if QIRAAT.exists():
        with QIRAAT.open(encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                wr = row["tsv_word_ref"]
                if wr.startswith(f"{s}:{a}:"):
                    variants[wr].append(row)
    word_of_variant = {}
    for wr, rows in variants.items():  # map the study word numbering to QAC words by skeleton similarity
        cand = skel(rows[0]["qiraat_arabic"])
        best = max(words, key=lambda w: difflib.SequenceMatcher(None, cand, skel(w["surface"])).ratio())
        word_of_variant[wr] = best["w"]
    var_by_w = defaultdict(list)
    for wr, rows in variants.items():
        var_by_w[word_of_variant[wr]] += rows
    for w in words:
        lines = [f"### L{w['w']:02d} word {w['w']}: {w['surface']} — lemma {w['lemmas'] or '—'}, root "
                 f"{P.spaced(w['roots']) if w['roots'] else '—'}, pos {w['pos']}"]
        x = wa.get(w["ref"])
        if x:
            lines.append(f"- analysis: {clip(x.get('gloss_range', ''), 300)}")
            lines.append(f"- analysis prose: {clip(x.get('prose', ''), 700)}")
            for t in x.get("topics", []):
                lines.append(f"  - topic [{t.get('status', '?')}]: {clip(t.get('headline', ''), 200)}")
        for v in var_by_w.get(w["w"], []):
            lines.append(f"- variant reading: {v['qiraat_arabic']} ({v['qiraat_transliteration']}; "
                         f"{v['qiraat_transmission_type']}): {clip(v['qiraat_note'], 300)}")
        rr = src.word_roots(w) if w["roots"] else {"identity": [], "alternatives": [], "echo": []}
        for kind, rids in (("root", rr["identity"]), ("documented alternative", [x[0] for x in rr["alternatives"]]),
                           ("echo root (sound family, not identity)", [x[0] for x in rr["echo"]])):
            for rid in rids:
                br = [f"{n.split(':')[2]} {src.gloss(n) or '—'} / {src.image(n) or '—'}" for n in src.branches_of.get(rid, [])]
                if br:
                    lines.append(f"- {kind} {src.root_name.get(rid, rid)} branches: " + "; ".join(br))
        items["local"].append((f"L{w['w']:02d}", "\n".join(lines)))

    # ---------------------------------------------------------------- usage
    seen_keys = set()
    for w in content:
        for key in (k for k in w["roots"].split(";") if k):
            if key in seen_keys:
                continue
            seen_keys.add(key)
            occ = list(src.qac.execute(
                "select distinct surah, ayah, surface_ar, lemma_ar, pos, measure from qac_morphemes "
                "where root_join_key=? and morpheme_role='STEM' order by surah, ayah", (key,)))
            by_lemma = defaultdict(list)
            for os_, oa, surf, lem, pos, meas in occ:
                by_lemma[(lem, pos, meas)].append((f"{os_}:{oa}", surf))
            n_ayat = len({r for grp in by_lemma.values() for r, _ in grp})
            focus_lemma = w["lemmas"].split(";")[-1]
            lines = [f"### U-{key} root {P.spaced(key)} (focus word {w['surface']}, lemma {focus_lemma}) — "
                     f"{len(occ)} occurrences in {n_ayat} ayat"]
            lines.append("- forms: " + "; ".join(f"{lem or '—'} {pos}{(' ' + meas) if meas else ''}: {len(v)}"
                                               for (lem, pos, meas), v in sorted(by_lemma.items(), key=lambda kv: -len(kv[1]))))
            show = []
            if len(occ) <= ROOT_FULL_MAX:
                show = sorted(by_lemma.items(), key=lambda kv: (kv[0][0] != focus_lemma, -len(kv[1])))
            else:
                show = [(k, v) for k, v in by_lemma.items() if k[0] == focus_lemma]
                lines.append(f"- frequent root: only the focus lemma's occurrences are listed (up to {LEMMA_LIST_MAX})")
            co = Counter()
            for (lem, pos, meas), occs in show:
                lines.append(f"- {lem or '—'} ({pos}{(' form ' + meas) if meas else ''}):")
                for r, surf in occs[:LEMMA_LIST_MAX]:
                    here = " ◀ focus" if r == ref else (" [same surah]" if r.startswith(f"{s}:") else "")
                    lines.append(f"  - {r}{here} {surf} | {clip(src.quran.get(r, ''), 220)}")
                    if r != ref:
                        for ww in src.words(r):
                            for k2 in ww["roots"].split(";"):
                                if k2 and k2 != key:
                                    co[k2] += 1
            shared = [f"{P.spaced(k)} ({c})" for k, c in co.most_common(14) if c >= 2]
            if shared:
                lines.append("- roots co-occurring across the listed ayat: " + ", ".join(shared))
            items["usage"].append((f"U-{key}", "\n".join(lines)))

    # ---------------------------------------------------------------- surah
    refs = ayah_refs(src, s)
    near = [r for r in refs if abs(int(r.split(":")[1]) - a) <= NEAR and r != ref]
    items["surah"].append(("S-near", "### S-near the surrounding passage (±7)\n" +
                           "\n".join(f"- {r} {src.quran[r]}" for r in near)))
    for key in sorted(seen_keys):
        occ = sorted({f"{os_}:{oa}" for os_, oa in src.qac.execute(
            "select distinct surah, ayah from qac_morphemes where root_join_key=? and surah=?", (key, s))} - {ref},
            key=lambda r: int(r.split(":")[1]))
        if occ:
            items["surah"].append((f"S-{key}", f"### S-{key} root {P.spaced(key)} elsewhere in the surah ({len(occ)})\n" +
                                   "\n".join(f"- {r} {clip(src.quran[r], 260)}" for r in occ[:25])))
    for rd in ((bundle.get("v12_focus_trace_hermetic") or {}).get("readers") or {}).values():
        for kind in ("baseline_models", "context_deltas", "surprising_valid_outliers"):
            for rec in rd.get(kind) or []:
                name = rec.get("model_id") or rec.get("delta_id") or rec.get("outlier_id")
                cr = rec.get("changed_reading") or {}
                steps = "; ".join(f"{st.get('source_ref')} w{','.join(map(str, st.get('source_word_indices') or []))}"
                                  f" {st.get('root', '')} {st.get('branch_id', '')}: {clip(st.get('role', ''), 140)}"
                                  for st in rec.get("activation_trace") or [])
                items["surah"].append((f"S-hft-{name}", f"### S-hft-{name} ({kind.rstrip('s')})\n- after: "
                                       f"{cr.get('after', '')}\n- mechanism: {clip(rec.get('mechanism', ''), 500)}\n"
                                       f"- trace: {steps}"))

    # ---------------------------------------------------------------- related passages
    def passage(r: str, span: int = 1) -> str:
        ts, ta = (int(x) for x in r.split(":"))
        out_ = []
        for n in range(ta - span, ta + span + 1):
            rr = f"{ts}:{n}"
            if rr in src.quran and n > 0 and rr != ref:
                out_.append(f"  - {'**' + rr + '**' if n == ta else rr} {src.quran[rr]}")
        return "\n".join(out_)

    rows = list(csv.DictReader((P.RECIPROCAL_DIR / f"focus_{s}_{a}_cutoff_100.tsv").open(encoding="utf-8"), delimiter="\t"))
    hints = defaultdict(list)
    for r in rows:
        lab = r["focus_direction_label"] if r["record_type"] == "directional_review" else r["source_direction_label"]
        hints[r["target_ref"]].append(f"{lab}: {clip(r['source_note'], 200)}")
    done = set()
    for t in sorted(hints, key=lambda r: tuple(map(int, r.split(":")))):
        items["related"].append((f"R-{t}", f"### R-{t} inter-ayah target\n- earlier labels (hints only): " +
                                 " | ".join(hints[t][:3]) + "\n" + passage(t)))
        done.add(t)
    pn = {l for w in words if "PN" in w["pos"].split(";") for l in w["lemmas"].split(";") if l}
    for lemma in sorted(pn):
        prefs = sorted({f"{x}:{y}" for x, y in src.qac.execute(
            "select distinct surah, ayah from qac_morphemes where lemma_ar=?", (lemma,))} - {ref},
            key=lambda r: tuple(map(int, r.split(":"))))
        if len(prefs) <= PEOPLE_MAX:
            for t in prefs:
                if t not in done:
                    items["related"].append((f"R-{t}", f"### R-{t} passage naming {lemma}\n" + passage(t)))
                    done.add(t)
    df = {}
    content_keys = [k for k in seen_keys]
    for key in content_keys:
        df[key] = src.qac.execute("select count(distinct surah||':'||ayah) from qac_morphemes where root_join_key=?",
                                  (key,)).fetchone()[0]
    keys = [k for k in content_keys if df[k] <= ROOT_DF_MAX]
    shared = defaultdict(set)
    for key in keys:
        for x, y in src.qac.execute("select distinct surah, ayah from qac_morphemes where root_join_key=?", (key,)):
            r = f"{x}:{y}"
            if r != ref and r not in done:
                shared[r].add(key)
    groups = defaultdict(list)
    for r, ks in shared.items():
        if len(ks) >= 2:
            groups[tuple(sorted(ks))].append(r)
    for sig, rs in sorted(groups.items(), key=lambda kv: (-len(kv[0]), -len(kv[1]))):
        rs.sort(key=lambda r: tuple(map(int, r.split(":"))))
        body = "\n".join(passage(r, 0) for r in rs[:4])
        items["related"].append((f"R-f-{'-'.join(sig)}", f"### R-f-{'-'.join(sig)} formula family "
                                 f"({' + '.join(P.spaced(k) for k in sig)}; {len(rs)} ayat: {', '.join(rs[:10])})\n" + body))

    # ---------------------------------------------------------------- write bundles
    tsv = []
    for line, its in items.items():
        n, cur, size = 1, [], 0
        for iid, text in its:
            if cur and size + len(text.encode()) > BUNDLE_BYTES:
                (out / f"{line}_{n}.md").write_text(f"# {line}_{n}.md — {len(cur)} items\n\n" + "\n\n".join(cur) + "\n", encoding="utf-8")
                n, cur, size = n + 1, [], 0
            cur.append(text)
            size += len(text.encode())
            tsv.append(f"{iid}\t{line}_{n}.md")
        if cur:
            (out / f"{line}_{n}.md").write_text(f"# {line}_{n}.md — {len(cur)} items\n\n" + "\n\n".join(cur) + "\n", encoding="utf-8")
    (out / "items.tsv").write_text("\n".join(tsv) + "\n", encoding="utf-8")
    ctx = V9 / "luna" / "work" / sa / "context.md"
    if ctx.exists():
        (out / "context.md").write_text(ctx.read_text(encoding="utf-8"), encoding="utf-8")
    counts = Counter(t.split("\t")[1].split("_")[0] for t in tsv)
    files = sorted(p.name for p in out.glob("*_*.md"))
    print(f"{ref}: items {dict(counts)}; bundles {files}")


if __name__ == "__main__":
    build(sys.argv[1])
