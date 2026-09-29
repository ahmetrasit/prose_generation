#!/usr/bin/env python3
"""check.py: a verification record for one finished commentary (script only; never edits the commentary; the record
goes to the user and to the scorecard, never into anything a model reads).

  python3 check.py <commentary.md> --ref S:A [--out record.json] [--quiet]

What it records:
  1. Every Arabic quotation in a tag ({ar:…, tr:…, gloss:…} or {{ar:…}}) resolved to a source, in this order:
       quran        the Quran text: the focus ayah, its window (±7), its surah, then anywhere (which ayah or ayat)
       dictionary   a dictionary branch text (quran-data TR entries: image, what_is, source phrase with its source tag,
                    and the root packets' lexical senses) - branch_ref, root, source tag, branch_kind; the summary
                    splits early-source phrases from the dictionary's own Arabic definitions (image/what_is), which
                    the dictionary pipeline wrote
       qiraat       a variant reading of a word (study qiraat.tsv)
       early_entry  the full early entry text of one of the six early sources (root packets' entry_text_clean)
       majaz        Majaz al-Quran, quoted directly (openiti_context.sqlite, source majaz_quran)
       unsourced    none of the above (memory, a late source, or an error)
     Matching folds diacritics and Uthmani spelling; 'level' says how: exact tokens, clitic (a proclitic or pronoun
     suffix differs), article (the quote adds or drops al-), loose (consonant skeleton; Quran only, last resort).
     'also' lists the other source types the same quotation matches.
  2. Arabic outside tags (in quotation marks, italics, backticks or bare), flagged and resolved the same way.
  3. [bellek] marks: the marked sentence, its checkable items (Arabic, refs) and whether each is attested in the
     project sources (Quran, dictionary, early entries, Majaz, qiraat). Unsourced Arabic without a mark is listed.
  4. Every cited branch (a quotation resolved to a dictionary branch of a root in the ayah or its window) with its
     branch_kind and scope note, and whether the prose frames it as an echo (markers: yankı, kalıp, söz öbeği,
     ifadede; extended markers reported separately) in its sentence, next to it, or not at all ('no echo marker':
     it may be stated as the word's sense here, or cited as a lexical unit; the user reads the sentence). For the
     record only: the script does not decide whether the construction is present.
  5. Negation/disclaimer rate (the E2 regex, frozen) with a breakdown.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import common as C

ECHO_CORE = {"yankı": r"yankı\w*", "kalıp": r"kalı[pb]\w*", "söz öbeği": r"söz öbe[ğk]\w*",
             "ifadede": r"ifade(?:de|sinde|lerde|lerinde)\b"}
ECHO_EXTENDED = {"deyim": r"deyim\w*", "tabir": r"tabir\w*", "terkip": r"terkib\w*|terkip\w*",
                 "kuruluş": r"kuruluş\w*", "birleşim": r"birleşim\w*", "deyiş": r"deyiş\w*",
                 "sözünde": r"sözünde\b|sözlerinde\b", "yapıda": r"yapı(?:da|sında|lar(?:ın)?da)\b",
                 "ile birlikte kullan": r"ile (?:birlikte )?kullanıl\w*", "ancak ... ile": r"(?:ancak|yalnızca)\s+\S+\s+ile\b"}
BELLEK = re.compile(r"\[\s*bellek[^\]]*\]", re.I)
QUOTE_OPEN = "\"“«‘'„"
ATTESTED = {"quran", "dictionary", "qiraat", "early_entry", "majaz"}
NOT_QUOTATIONS = {"root_name", "too_short"}  # a root cited by its letters; a single letter or particle


class Resolver:
    def __init__(self, focus: str):
        self.focus = focus
        self.s, self.a = C.parse_ref(focus)
        self.win = set(C.window(focus))
        self.refs, self.q_drop, self.q_alif, self.q_loose = C.quran_corpora()
        self.focus_roots = set(C.ayah_roots(focus))
        self.win_roots = {r for x in self.win for r in C.ayah_roots(x)}
        self.letters = C.root_letters()
        self.bb = C.branch_by_ref()
        self.root_ids = {v: k for k, v in C.root_letters().items() if v}
        self.memo: dict[str, dict] = {}

    # --- per source (gapped=True: only the elision-tolerant fallback)
    def quran(self, quote: str, gapped: bool = False) -> list[dict]:
        hits: dict[int, str] = {}
        rank = {"exact": 0, "clitic": 1, "article": 2, "gapped": 3, "loose": 4}
        for corp in (self.q_drop, self.q_alif):
            found = C.gapped_units(corp, quote) if gapped else C.search_units(corp, quote)
            for u, lvl in found.items():
                if u not in hits or rank[lvl] < rank[hits[u]]:
                    hits[u] = lvl
        if not hits and not gapped:  # consonant-skeleton fallback: only the focus, its window and its surah
            for u, lvl in C.search_units(self.q_drop, quote, loose_corpus=self.q_loose).items():
                if C.parse_ref(self.refs[u])[0] == self.s:
                    hits[u] = lvl
        out = []
        for u, lvl in hits.items():
            ref = self.refs[u]
            s, a = C.parse_ref(ref)
            where = "focus" if ref == self.focus else "window" if ref in self.win else "surah" if s == self.s else "other"
            out.append({"ref": ref, "where": where, "level": lvl})
        order = {"focus": 0, "window": 1, "surah": 2, "other": 3}
        strength = {"exact": 0, "clitic": 0, "article": 1, "gapped": 2, "loose": 3}
        out.sort(key=lambda h: (strength[h["level"]], order[h["where"]], rank[h["level"]], C.parse_ref(h["ref"])))
        return out

    def dictionary(self, quote: str, gapped: bool = False) -> list[dict]:
        corp, meta = C.dict_corpus()
        seen, out = set(), []
        rank = {"exact": 0, "clitic": 1, "article": 2, "gapped": 3}
        found = C.gapped_units(corp, quote) if gapped else C.search_units(corp, quote)
        for u, lvl in found.items():
            bref, fld, srcs = meta[u]
            key = (bref, fld, tuple(srcs))
            if key in seen:
                continue
            seen.add(key)
            rid = bref.split("/")[0]
            where = "focus" if rid in self.focus_roots else "window" if rid in self.win_roots else "other"
            b = self.bb.get(bref, {})
            out.append({"branch_ref": bref, "root": self.letters.get(rid, ""), "branch": bref.split("/")[1],
                        "field": fld, "source_tags": srcs, "branch_kind": b.get("branch_kind", ""),
                        "where": where, "level": lvl})
        order = {"focus": 0, "window": 1, "other": 2}
        fpri = {"source_phrase_ar": 0, "lexical_source_phrase": 1, "lexical_expression_ar": 2, "lexical_sense_ar": 2,
                "image_ar": 3, "what_is_ar": 3, "what_is_not_ar": 4}
        out.sort(key=lambda h: (rank.get(h["level"], 4), order[h["where"]], fpri.get(h["field"], 5), h["branch_ref"]))
        return out

    def early(self, quote: str, gapped: bool = False) -> list[dict]:
        corp, meta = C.early_corpus()
        out = []
        found = C.gapped_units(corp, quote) if gapped else C.search_units(corp, quote)
        for u, lvl in found.items():
            rid, sid = meta[u]
            where = "focus" if rid in self.focus_roots else "window" if rid in self.win_roots else "other"
            out.append({"root_id": rid, "root": self.letters.get(rid, ""), "source": sid, "where": where, "level": lvl})
        order = {"focus": 0, "window": 1, "other": 2}
        out.sort(key=lambda h: (order[h["where"]], h["root_id"], h["source"]))
        return out

    def majaz(self, quote: str, gapped: bool = False) -> list[dict]:
        corp, entries = C.majaz_corpus()
        found = C.gapped_units(corp, quote) if gapped else C.search_units(corp, quote)
        return [{"entry_id": entries[u]["id"], "ayah_marker": entries[u]["marker"], "heading": entries[u]["heading"][:80],
                 "mapped_ref": entries[u].get("ref"), "surah": entries[u].get("surah"), "level": lvl}
                for u, lvl in sorted(found.items())]

    def qiraat(self, quote: str, gapped: bool = False) -> list[dict]:
        if gapped:
            return []
        idx = C.qiraat_index()
        out = []
        for v in C.fold_variants(quote):
            for r in idx.get(v, []):
                out.append({"word_ref": r["word_ref"], "readers": r["readers"], "arabic": r["arabic"]})
        pre = f"{self.s}:{self.a}:"
        out.sort(key=lambda r: (not r["word_ref"].startswith(pre), r["word_ref"]))
        return out

    # --- decision
    def _one(self, quote: str, gapped: bool) -> dict:
        """Pick the source by match strength first (exact/clitic > article > gapped > loose), then by source and
        place: Quran near (focus, window, surah) > dictionary branch of a focus/window root > variant reading at the
        focus > Quran elsewhere > any dictionary branch > any variant reading > early entry > Majaz. A multi-word
        quotation that is Quran text anywhere goes to the Quran before the dictionary."""
        q = self.quran(quote, gapped)
        d = self.dictionary(quote, gapped)
        e = self.early(quote, gapped)
        m = self.majaz(quote, gapped)
        v = self.qiraat(quote, gapped)
        strength = {"exact": 0, "clitic": 0, "article": 1, "gapped": 2, "loose": 3}
        multiword = len(C.fold(quote).split()) >= 2
        cands = []  # (strength, priority, source, hits)
        for g in sorted({strength[h["level"]] for h in q + d + e + m} | ({0} if v else set())):
            qg = [h for h in q if strength[h["level"]] == g]
            dg = [h for h in d if strength[h["level"]] == g]
            eg = [h for h in e if strength[h["level"]] == g]
            mg = [h for h in m if strength[h["level"]] == g]
            vg = v if g == 0 else []
            qn = [h for h in qg if h["where"] in ("focus", "window", "surah")]
            dn = [h for h in dg if h["where"] in ("focus", "window")]
            vf = [h for h in vg if h["word_ref"].startswith(f"{self.s}:{self.a}:")]
            order = [(0, "quran", qn), (1, "dictionary", dn), (2, "qiraat", vf), (3, "quran", qg),
                     (4, "dictionary", dg), (5, "qiraat", vg), (6, "early_entry", eg), (7, "majaz", mg)]
            if multiword:  # a multi-word Quran passage is cited from the Quran, even where a branch quotes it too
                order = [order[0], order[3], order[1], order[2]] + order[4:]
            for pri, src, hs in order:
                if hs:
                    cands.append((g, pri, src, hs))
                    break
            if cands:
                break
        if cands:
            _, _, src, top = cands[0]
        else:
            src, top = "unsourced", []
        detail = {}
        if src == "quran":
            detail = {"refs": [h["ref"] for h in top[:6]], "n_ayat": len(top), "where": top[0]["where"]}
        elif src == "dictionary":
            detail = {"branches": top[:6], "n_matches": len(top)}
        elif src == "early_entry":
            detail = {"entries": top[:8], "n_matches": len(top)}
        elif src == "majaz":
            detail = {"entries": top[:4], "n_matches": len(top)}
        elif src == "qiraat":
            detail = {"variants": top[:4]}
        also = {}
        if src != "quran" and q:
            also["quran"] = {"refs": [h["ref"] for h in q[:4]], "n_ayat": len(q), "level": q[0]["level"]}
        if src != "dictionary" and d:
            also["dictionary"] = [f"{h['root']} {h['branch']} ({h['branch_ref']}) {h['field']}" +
                                  (f" [{';'.join(h['source_tags'])}]" if h["source_tags"] else "") for h in d[:4]]
        if src != "early_entry" and e:
            also["early_entry"] = sorted({f"{h['root']} {h['source']}" for h in e})[:8]
        if src != "majaz" and m:
            also["majaz"] = [h["entry_id"] for h in m[:4]]
        if src != "qiraat" and v:
            also["qiraat"] = [h["word_ref"] for h in v[:4]]
        return {"source": src, "level": top[0].get("level") if top else None, "detail": detail, "also": also}

    def resolve(self, quote: str) -> dict:
        """Root names and single letters first; then strict matching; then pieces (split at ؛ or the ayah-end sign),
        each resolved on its own; then the gapped (silent-elision) fallback."""
        if quote in self.memo:
            return self.memo[quote]
        rn = C.root_name(quote)
        if rn:
            rid = self.root_ids.get(rn)
            res = {"source": "root_name", "level": None,
                   "detail": {"root": rn, "root_id": rid, "in_dictionary": bool(rid)}, "also": {}}
        elif len(C.fold(quote).replace(" ", "")) < 2:
            res = {"source": "too_short", "level": None, "detail": {}, "also": {}}
        else:
            res = self._one(quote, gapped=False)
            if res["source"] == "unsourced" and re.search("[؛۝]", quote):
                pieces = [p.strip() for p in re.split("[؛۝]", quote) if C.fold(p)]
                sub = [self._one(p, False) for p in pieces]
                sub = [x if x["source"] != "unsourced" else self._one(p, True) for p, x in zip(pieces, sub)]
                if sub and all(x["source"] in ATTESTED for x in sub):
                    res = {"source": sub[0]["source"], "level": "pieces",
                           "detail": {"pieces": [{"piece": p, **x} for p, x in zip(pieces, sub)],
                                      **{k: v for k, v in sub[0]["detail"].items()}}, "also": {}}
            if res["source"] == "unsourced":
                g = self._one(quote, gapped=True)
                if g["source"] != "unsourced":
                    res = g
        self.memo[quote] = res
        return res


def outside_tags(text: str) -> list[dict]:
    masked = C.TAG.sub(lambda m: " " * (m.end() - m.start()), text)
    out = []
    for m in C.ARABIC_RUN.finditer(masked):
        run = m.group(0).strip()
        if len(C.ARABIC_LETTER.findall(run)) < 2:
            continue
        before = masked[max(0, m.start() - 3):m.start()].rstrip()
        after = masked[m.end():m.end() + 3].lstrip()
        if before and before[-1] in QUOTE_OPEN:
            ctx = "quotation marks"
        elif before.endswith("*") or after.startswith("*"):
            ctx = "italics"
        elif before.endswith("`") or after.startswith("`"):
            ctx = "backticks"
        elif masked[max(0, m.start() - 1):m.start()] == "(" or before.endswith("("):
            ctx = "parentheses"
        else:
            ctx = "bare"
        out.append({"start": m.start(), "end": m.end(), "line": C.line_of(text, m.start()), "text": run, "context": ctx})
    return out


def _early_phrase(q: dict) -> bool:
    """True if a dictionary match is an early-source phrase (source_phrase_ar or a lexical sense's phrase, with a
    source tag); False if it matches only the dictionary's own Arabic definition (image, what_is, lexical sense),
    which the dictionary pipeline wrote and no early source states in those words."""
    hs = q["detail"].get("branches", []) + [p for x in q["detail"].get("pieces", []) for p in x.get("detail", {}).get("branches", [])]
    return any(h["field"] in ("source_phrase_ar", "lexical_source_phrase") or h.get("source_tags") for h in hs)


def markers(s: str, table: dict) -> list[str]:
    return [k for k, rx in table.items() if re.search(rx, s, re.I)]


def check(path: Path, focus: str) -> dict:
    text = path.read_text(encoding="utf-8")
    R = Resolver(focus)
    spans = C.sentences(text)
    sent_text = lambda i: text[spans[i][0]:spans[i][1]] if 0 <= i < len(spans) else ""
    marks = [(m.start(), m.group(0)) for m in BELLEK.finditer(text)]
    mark_sents = set()
    for pos, _ in marks:
        i = C.sentence_at(spans, pos)
        if pos - spans[i][0] <= 3 and i > 0:
            i -= 1
        mark_sents.add(i)

    quotations = []
    for n, (st, en, ar) in enumerate(C.tags(text), 1):
        r = R.resolve(ar)
        si = C.sentence_at(spans, st)
        quotations.append({"n": n, "line": C.line_of(text, st), "quote": ar, **r, "sentence_index": si,
                           "bellek_marked": si in mark_sents})
    outside = []
    for o in outside_tags(text):
        r = R.resolve(o["text"])
        si = C.sentence_at(spans, o["start"])
        outside.append({"line": o["line"], "text": o["text"], "context": o["context"], **r, "sentence_index": si,
                        "bellek_marked": si in mark_sents})

    # [bellek] marks
    bellek = []
    for pos, raw in marks:
        i = C.sentence_at(spans, pos)
        if pos - spans[i][0] <= 3 and i > 0:
            i -= 1
        s = sent_text(i)
        items = [{"kind": "tag", "arabic": q["quote"], "source": q["source"], "attested": q["source"] in ATTESTED}
                 for q in quotations if q["sentence_index"] == i]
        items += [{"kind": "arabic outside tags", "arabic": o["text"], "source": o["source"],
                   "attested": o["source"] in ATTESTED} for o in outside if o["sentence_index"] == i]
        refs = sorted(C.refs_in(s), key=C.parse_ref)
        translit = re.findall(r"\*([^*\n]{2,40})\*", s)
        ar = [x for x in items if x["source"] not in NOT_QUOTATIONS]
        if not ar:
            status = "no Arabic item (not checkable by script)"
        elif all(x["attested"] for x in ar):
            status = "attested"
        elif any(x["attested"] for x in ar):
            status = "partly attested"
        else:
            status = "not attested in the project sources"
        bellek.append({"line": C.line_of(text, pos), "mark": raw, "sentence": s.strip()[:600], "items": items,
                       "refs": refs, "italic_transliterations": translit, "status": status})
    unsourced_unmarked = [{"line": q["line"], "quote": q["quote"]} for q in quotations
                          if q["source"] == "unsourced" and not q["bellek_marked"]]
    unsourced_unmarked += [{"line": o["line"], "quote": o["text"], "outside_tags": True} for o in outside
                           if o["source"] == "unsourced" and not o["bellek_marked"]]

    # cited branches and echo framing (record only)
    cited, seen = [], set()
    for q in quotations + [dict(o, quote=o["text"], n=None) for o in outside]:
        if q["source"] != "dictionary":
            continue
        for h in q["detail"]["branches"]:
            if h["where"] not in ("focus", "window"):
                continue
            key = (h["branch_ref"], q["line"])
            if key in seen:
                continue
            seen.add(key)
            b = C.branch_by_ref().get(h["branch_ref"], {})
            si = q["sentence_index"]
            here = sent_text(si)
            core_here = markers(here, ECHO_CORE)
            core_near = markers(sent_text(si - 1) + " " + sent_text(si + 1), ECHO_CORE)
            ext_here = markers(here, ECHO_EXTENDED)
            framing = ("echo marker in the sentence" if core_here else
                       "echo marker in a neighbouring sentence" if core_near else
                       "no echo marker")
            cited.append({"branch_ref": h["branch_ref"], "root": h["root"], "branch": h["branch"],
                          "branch_kind": h["branch_kind"], "bound": h["branch_kind"] in C.BOUND_KINDS,
                          "root_in": h["where"], "scope_note": b.get("scope_note", ""), "image_ar": b.get("image_ar", ""),
                          "quote": q["quote"], "line": q["line"], "framing": framing,
                          "echo_markers": core_here or core_near, "extended_markers_in_sentence": ext_here,
                          "sentence": here.strip()[:500]})
    bound = [c for c in cited if c["bound"]]

    by_source: dict[str, int] = {}
    for q in quotations:
        by_source[q["source"]] = by_source.get(q["source"], 0) + 1
    n = len(quotations)
    checkable = [q for q in quotations if q["source"] not in NOT_QUOTATIONS]
    sourced = sum(1 for q in checkable if q["source"] in ATTESTED)
    out_q = [o for o in outside if o["source"] not in NOT_QUOTATIONS]
    words = len(text.split())
    summary = {
        "words": words, "tags": n, "tags_checkable": len(checkable), "tags_sourced": sourced,
        "share_sourced": round(sourced / len(checkable), 3) if checkable else None, "by_source": by_source,
        "levels": {k: sum(1 for q in checkable if q["level"] == k) for k in
                   sorted({str(q["level"]) for q in checkable if q["level"]})},
        "dictionary_early_phrase": sum(1 for q in checkable if q["source"] == "dictionary" and _early_phrase(q)),
        "dictionary_definition_only": sum(1 for q in checkable if q["source"] == "dictionary" and not _early_phrase(q)),
        "arabic_outside_tags": len(outside),
        "arabic_outside_tags_quotations": len(out_q),
        "arabic_outside_tags_quotations_sourced": sum(1 for o in out_q if o["source"] in ATTESTED),
        "arabic_outside_tags_root_names": sum(1 for o in outside if o["source"] == "root_name"),
        "arabic_outside_tags_by_context": {k: sum(1 for o in outside if o["context"] == k)
                                           for k in sorted({o["context"] for o in outside})},
        "bellek_marks": len(bellek),
        "bellek_status": {k: sum(1 for b in bellek if b["status"] == k) for k in sorted({b["status"] for b in bellek})},
        "unsourced_unmarked": len(unsourced_unmarked),
        "cited_branches": len({c["branch_ref"] for c in cited}),
        "cited_bound_branches": len({c["branch_ref"] for c in bound}),
        "bound_citations_with_echo_marker": sum(1 for c in bound if c["framing"].startswith("echo")),
        "bound_citations_without_echo_marker": sum(1 for c in bound if c["framing"] == "no echo marker"),
        "bound_citations_extended_marker_only": sum(1 for c in bound if c["framing"] == "no echo marker"
                                                    and c["extended_markers_in_sentence"]),
        "negation": C.negation(text),
    }
    return {
        "record": "E0 check.py verification record (for the user and the scorecard; never a model input)",
        "file": str(path), "file_sha256": C.sha256(path), "ref": focus,
        "tool_sha256": {p: C.sha256(C.HERE / p) for p in ("check.py", "common.py")},
        "index_signature": C.index()["signature"],
        "summary": summary, "quotations": quotations, "arabic_outside_tags": outside, "bellek": bellek,
        "unsourced_unmarked": unsourced_unmarked, "cited_branches": cited,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("commentary")
    ap.add_argument("--ref", required=True, help="focus ayah S:A")
    ap.add_argument("--out", help="write the JSON record here (default: stdout)")
    ap.add_argument("--quiet", action="store_true", help="with --out: do not print the summary")
    a = ap.parse_args()
    rec = check(Path(a.commentary), a.ref)
    js = json.dumps(rec, ensure_ascii=False, indent=1)
    if a.out:
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        Path(a.out).write_text(js + "\n", encoding="utf-8")
        if not a.quiet:
            s = rec["summary"]
            print(f"{a.ref} {a.commentary}: {s['tags']} tags, {s['tags_sourced']}/{s['tags_checkable']} sourced "
                  f"{s['by_source']}; {s['arabic_outside_tags_quotations']} Arabic quotations outside tags "
                  f"(+{s['arabic_outside_tags_root_names']} root names); {s['bellek_marks']} [bellek] {s['bellek_status']}; "
                  f"{s['unsourced_unmarked']} unsourced unmarked; bound branches cited {s['cited_bound_branches']} "
                  f"(echo marker {s['bound_citations_with_echo_marker']}, none {s['bound_citations_without_echo_marker']}); "
                  f"neg/1000 {s['negation']['neg_e2_per_1000']}")
    else:
        print(js)
    return 0


if __name__ == "__main__":
    sys.exit(main())
