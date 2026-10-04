#!/usr/bin/env python3
"""Stage 0 (paket): the reference pack for one surah, built by script, read by every agent stage.

  python3 enrichment/v2/pack.py --surah 107 [--force]

Writes enrichment/v2/work/sNNN/pack/:
  base/surah.md, base/S_A.md      the frozen v16 outputs (surah images, never augmented; ayah readings after
                                  augment9 (Opus), copied; an ayah without augment9 has no base and no ayah page
                                  until it has run and the pack is rebuilt)
  base.json                       their paths and sha256
  numbered/surah.md, S_A.md       the same with prose paragraphs numbered [¶n] (v16 augment's numbering; augment9
                                  additions unnumbered, under their paragraph): what the agent reads; records
                                  anchor by paragraph number plus a confirming phrase
A rebuild (--force) is refused while a call of the surah is running. Finished calls are unaffected: each records
the sha256 of its page's base, and acceptance refuses a page whose base has changed since its call.
  binding.json                    every word of every ayah -> QAC lemma/root keys -> dictionary root ids
                                  (identity, documented alternatives, echo) via v9's gateway: the only word->root
                                  binding the workflow uses
  ayah/S_A/words.md               words, morphemes and the elements a faithful translation must carry
  ayah/S_A/dictionary.md          the v16 dictionary section (every branch of every root, early phrases whole)
  ayah/S_A/usage.md               every Qur'anic occurrence of each content lemma (refs), surah occurrences
  ayah/S_A/meals.md               the panel meals, the relay pair (Asad EN / Esed TR), Arberry, then the reference set
  ayah/S_A/sources.md             every corpus locator tied to this ayah, by source (texts via tools/corpus.py get)
  ayah/S_A/turkish.md             Turkish word history for the key words of the panel meals at this ayah (Nişanyan,
                                  TDK, Kubbealtı entries already in the corpus); words still to fetch are listed in
                                  pack.json turkish.fetch_candidates (fetch/ref_loanword.py, then rebuild)
  roots/<root_id>.md              per bound root: project branches + the six classical lexica's entries in full,
                                  locators for Lisān, Lane, Asās, Qāmūs, Tāj
  check/                          v16 check.py records for the base files (tag verification); problems listed in
                                  errata_candidates.json for the audit stage
  pack.json                       manifest: inputs, hashes, dictionary commit, corpus state, gaps
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sqlite3
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

V2 = Path(__file__).resolve().parent
PG = V2.parents[1]
PROJECTS = PG.parent
V16 = PG / "_commentary" / "v16"
CHECK = PG / "_commentary" / "review" / "e0" / "checks" / "check.py"  # the checker v16 runs (v16.py CHECK)
sys.path.insert(0, str(V16))
sys.path.insert(0, str(V2 / "tools"))
import dictionary as D  # noqa: E402  (v16 dictionary; imports v9/prepare as D.P)
import corpus as C  # noqa: E402
sys.path.insert(0, str(V2))
import render as R  # noqa: E402

DICT_REPO = PROJECTS / "dictionary"
TR_MANIFEST = PROJECTS / "quran-data" / "data" / "dictionary" / "tr" / "MANIFEST.json"
CLASSICAL_IDS = ["AYN", "JAMHARA", "TAHDHIB", "SIHAH", "MAQAYIS", "MUFRADAT"]
POINTER_LEXICA = ["LISAN", "LANE", "ASAS", "QAMUS", "TAJ"]
RELAY = ["ASAD-EN", "MEAL-ESED", "ARBERRY"]


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def work_dir(s: int) -> Path:
    return V2 / "work" / f"s{s:03d}"


# ---------------------------------------------------------------- base selection

def surah_base(s: int) -> Path:
    cands = [p for p in (V16 / "out" / f"s{s:03d}").glob("images.r13.*/images.md") if "session-limit" not in str(p)]
    if len(cands) != 1:
        raise SystemExit(f"S{s}: expected one r13 surah images.md, found {[str(c.relative_to(PG)) for c in cands]}; "
                         f"pass --surah-base")
    return cands[0]


AYAH_AUGMENT = R.AYAH_AUGMENT  # v16 production augment (v16 RUNBOOK, 2026-10-04); augment2/3 are superseded


def ayah_base(s: int, a: int) -> Path | None:
    """The final v16 ayah reading: the r13 reading after augment9 (Opus). None while augment9 has not run: an ayah
    page is never built on a bare or superseded reading (the page would then miss or contradict v16's own additions)."""
    name = f"{s}_{a}"
    hits = [p for p in (V16 / "out" / name).glob(f"DM.r13.images.r13.*/{AYAH_AUGMENT}/{name}.reading.tr.md")
            if "session-limit" not in str(p)]
    if len(hits) > 1:
        raise SystemExit(f"{s}:{a}: several augment9 readings {[str(h.relative_to(PG)) for h in hits]}")
    return hits[0] if hits else None


def running_calls(s: int) -> list[str]:
    """Call directories of the surah that started and have no run.log.json yet (running or interrupted)."""
    return [d.name for d in sorted(work_dir(s).glob("zengin.*"))
            if (d / "started.json").exists() and not (d / "run.log.json").exists() and not (d / "dead.json").exists()]


# ---------------------------------------------------------------- morphology -> expected elements

PREFIX = {"f:CONJ": "fa- (and so / then)", "f:REM": "fa- (resumption: so)", "f:RSLT": "fa- (result: so, therefore)",
          "f:SUP": "fa- (supplementary)", "f:CAUS": "fa- (cause: for)", "w:CONJ": "wa- (and)", "w:P": "wa- (oath: by)",
          "w:CIRC": "wa- (circumstantial: while)", "w:COM": "wa- (with)", "w:REM": "wa- (resumption)",
          "bi+": "bi- (preposition: with, by, in)", "l:P": "li- (preposition: for, to)", "l:PRP": "li- (purpose: so that)",
          "l:EMPH": "la- (emphasis: truly)", "l:IMPV": "li- (imperative: let …)", "ka+": "ka- (like, as)",
          "Al+": "al- (definite article; Turkish has none — definiteness must be carried otherwise or is lost)",
          "sa+": "sa- (future: will soon)", "A:INTG": "a- (question)", "A:EQ": "a- (equalisation: whether)",
          "ya+": "yā (vocative: O)", "ta+": "ta- (oath: by)"}
POS = {"N": "noun", "PN": "proper noun", "ADJ": "adjective", "V": "verb", "P": "preposition", "PRON": "pronoun",
       "DEM": "demonstrative", "REL": "relative pronoun", "NEG": "negation", "ACC": "inna-type particle (emphasis)",
       "EMPH": "emphatic particle", "CONJ": "conjunction", "INTG": "interrogative", "COND": "conditional",
       "T": "time adverb", "LOC": "location adverb", "RES": "restriction (only)", "EXP": "exception (except)",
       "AMD": "amendment (but)", "VOC": "vocative", "SUB": "subordinating (that)", "CERT": "certainty (qad)",
       "FUT": "future particle", "PRO": "prohibition", "INL": "Qur'anic initials", "ANS": "answer particle",
       "SUP": "supplemental", "RET": "retraction", "IMPN": "imperative verbal noun", "INC": "inceptive",
       "SUR": "surprise", "AVR": "aversion", "EXL": "explanation", "EQ": "equalisation", "PREV": "preventive",
       "INT": "interpretation", "CAUS": "cause", "COM": "comitative", "CIRC": "circumstantial", "RSLT": "result",
       "REM": "resumption", "EXH": "exhortation", "PRP": "purpose", "IMPV": "imperative particle"}
FEAT = {"PASS": "PASSIVE voice", "IMPF": "imperfect (ongoing/future)", "PERF": "perfect (completed)",
        "IMPV": "imperative", "MOOD:SUBJ": "subjunctive", "MOOD:JUS": "jussive", "NOM": "nominative",
        "ACC": "accusative", "GEN": "genitive", "INDEF": "indefinite", "ACT PCPL": "active participle",
        "PASS PCPL": "passive participle", "VN": "verbal noun"}
PRON = {"1S": "my/me", "1P": "our/us", "2MS": "your (m.s.)", "2FS": "your (f.s.)", "2D": "your (dual)",
        "2MP": "your (m.pl.)", "2FP": "your (f.pl.)", "3MS": "his/him/its", "3FS": "her/its", "3D": "their (dual)",
        "3MP": "their/them (m.pl.)", "3FP": "their/them (f.pl.)"}
NUM = {"S": "singular", "D": "DUAL", "P": "PLURAL"}


def describe(feat: str) -> list[str]:
    parts = feat.split("|")
    out = []
    if parts[0] == "PREFIX":
        key = parts[1].rstrip("+")
        out.append(PREFIX.get(parts[1], PREFIX.get(key, f"prefix {parts[1]}")))
    elif parts[0] == "SUFFIX":
        for p in parts[1:]:
            if p.startswith("PRON:"):
                out.append(f"attached pronoun {p[5:]} = {PRON.get(p[5:], p[5:])}")
            else:
                out.append(f"suffix {p}")
    else:
        for p in parts[1:]:
            if p.startswith("POS:"):
                out.append(POS.get(p[4:], p[4:]))
            elif p.startswith(("LEM:", "ROOT:", "SP:")):
                continue
            elif p in FEAT:
                out.append(FEAT[p])
            elif re.fullmatch(r"\((I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII)\)", p):
                out.append(f"verb form {p}")
            elif re.fullmatch(r"[123]?[MF]?[SDP]", p):
                person = {"1": "1st person ", "2": "2nd person ", "3": "3rd person "}.get(p[0], "")
                rest = p[1:] if p[0] in "123" else p
                gender = {"M": "masc. ", "F": "fem. "}.get(rest[:1], "")
                out.append(f"{person}{gender}{NUM.get(rest[-1], rest[-1])}".strip())
            elif p in ("NOM", "ACC", "GEN"):
                out.append(FEAT[p])
            else:
                out.append(p)
    return out


def words_md(src, ref: str) -> str:
    s, a = (int(x) for x in ref.split(":"))
    lines = [f"# {ref} — words and the elements a faithful translation must carry", "",
             src.quran.get(ref, ""), "",
             "Per word: QAC morphemes with their features in plain terms. These are the checks for the meal review: a "
             "translation keeps, drops or substitutes each element (a preposition, an attached pronoun, number, "
             "definiteness, voice, emphasis, a conjunction). Turkish may force a change; say so when it does.", ""]
    for w in src.words(ref):
        rows = src.qac.execute("SELECT surface_ar, morph_features, lemma_ar, root_ar FROM qac_morphemes "
                               "WHERE qac_word_ref=? ORDER BY morpheme_index", (w["ref"],)).fetchall()
        lines.append(f"## w{w['w']} {w['surface']}  ({w['ref']}; lemma {w['lemmas'] or '—'}; root "
                     f"{' / '.join(D.P.spaced(k) for k in w['roots'].split(';') if k) or '—'})")
        for surf, feat, lemma, root in rows:
            lines.append(f"- {surf}: " + "; ".join(describe(feat)))
        lines.append("")
    return "\n".join(lines)


def usage_md(src, ref: str) -> str:
    s = int(ref.split(":")[0])
    lines = [f"# {ref} — Qur'anic usage of each content lemma", "",
             "Every occurrence of the lemma (refs; QAC). Use it for vucuh, ayet_ayet and for checking a meal's "
             "consistency across the Qur'an (tools/corpus.py get QURAN:S:A or MEAL-X:S:A for the texts).", ""]
    seen = set()
    for w in src.words(ref):
        keys = [k for k in w["roots"].split(";") if k]
        for key in keys:
            lemma = (w["lemmas"].split(";") or [""])[-1]
            if (key, lemma) in seen or not lemma:
                continue
            seen.add((key, lemma))
            occ = src.usage(key, lemma)
            lem_counts = list(src.qac.execute(
                "SELECT lemma_ar, count(*) FROM qac_morphemes WHERE root_join_key=? AND lemma_ar!='' "
                "GROUP BY lemma_ar ORDER BY 2 DESC", (key,)))
            in_surah = [f"{os_}:{oa}" for os_, oa, _ in occ if os_ == s]
            lines.append(f"## {w['surface']} (w{w['w']}) — lemma {lemma}, root {D.P.spaced(key)}: {len(occ)} ayat")
            lines.append("- root's lemmas in the Qur'an: " + ", ".join(f"{l} {c}" for l, c in lem_counts))
            lines.append(f"- in this surah: {', '.join(in_surah) or '—'}")
            if len(occ) == 1:
                lines.append("- hapax: occurs only here")
            lines.append("- all: " + ", ".join(f"{os_}:{oa} {sf}" for os_, oa, sf in occ))
            lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------- corpus-backed files

def corpus_con() -> sqlite3.Connection | None:
    return sqlite3.connect(C.INDEX) if C.INDEX.exists() else None


def source_meta(con) -> dict[str, dict]:
    return {r[0]: json.loads(r[1]) for r in con.execute("SELECT id, meta FROM src")} if con else {}


def meals_md(con, metas: dict, ref: str) -> str:
    s, a = (int(x) for x in ref.split(":"))
    lines = [f"# {ref} — translations", "",
             "Panel meals first (16; `lineage` marks shared lineage, counted as one witness for consensus), then the "
             "relay pair (Asad's English and the Turkish Esed made from it) and Arberry as a literal English control, "
             "then the reference set. Brackets and parentheses are as published. A merged verse group shows its range.",
             ""]
    if not con:
        return "\n".join(lines + ["(corpus index missing: run tools/corpus.py build)"])
    rows = con.execute("SELECT seg, src, a, a_end, text, extra FROM seg WHERE s=? AND a<=? AND coalesce(a_end,a)>=? "
                       "AND src IN (SELECT id FROM src WHERE kind IN ('meal','translation'))", (s, a, a)).fetchall()
    by = {r[1]: r for r in rows}
    panel = sorted(i for i, m in metas.items() if m.get("panel"))
    relay = [i for i in RELAY if i in metas]
    rest = sorted(i for i, m in metas.items() if m.get("kind") in ("meal", "translation") and i not in panel and i not in relay)
    for title, ids in (("## Panel", panel), ("## Relay and control", relay), ("## Reference set", rest)):
        lines += [title, ""]
        for i in ids:
            m = metas[i]
            tag = " ".join(x for x in (f"lineage={m['lineage']}" if m.get("lineage") else "",
                                       f"relay={m['relay']}" if m.get("relay") else "",
                                       "access=hafiza" if m.get("access") == "hafiza" else "") if x)
            r = by.get(i)
            if not r:
                lines.append(f"- **{i}** ({m.get('author') or m.get('title')}){' ' + tag if tag else ''}: — not available")
                continue
            rng = f" [{s}:{r[2]}-{r[3]}]" if r[3] and r[3] != r[2] else ""
            notes = json.loads(r[5] or "{}").get("notes")
            lines.append(f"- **{i}** ({m.get('author') or m.get('title')}){' ' + tag if tag else ''}{rng}: {r[4]}"
                         + (f"\n  notes: {notes}" if notes else ""))
        lines.append("")
    return "\n".join(lines)


TR_DICTS = ("NISANYAN", "TDK", "KUBBEALTI")
TR_SUFFIXES = sorted("larından lerinden larını lerini larına lerine ların lerin ları leri ından inden undan ünden "
                     "dan den tan ten nın nin nun nün ını ini unu ünü ına ine una üne lar ler yla yle ın in un ün "
                     "da de ta te ı i u ü a e".split(), key=len, reverse=True)
TR_STOP = set(("ve ki bu şu o bir için gibi olan onlar onları onlara kim ne mi mı da de ile değil olsun işte artık "
               "öyle hem ise eden edenler olanlar kimse kimseler kimsedir odur onu ona onun yani hiç hep çok daha en "
               "sonra önce kadar vardır yoktur olur olduğu ettiği eder ederler yapan yapanlar şunlar şunlara "
               "kendi kendileri kişi kişiler kimdir").split())


def tr_lower(s: str) -> str:
    """Lower-case the Turkish way and fold circumflexes (miskîni ~ miskin, zekât ~ zekat)."""
    return s.replace("I", "ı").replace("İ", "i").lower().translate(str.maketrans("âîû", "aiu"))


def tr_stem(tok: str) -> str:
    changed = True
    while changed and len(tok) > 4:
        changed = False
        for suf in TR_SUFFIXES:
            if tok.endswith(suf) and len(tok) - len(suf) >= 3:
                tok, changed = tok[: -len(suf)], True
                break
    return tok


def turkish_md(con, metas: dict, ref: str) -> tuple[str, list[str], list[str]]:
    """(turkish.md, matched headwords, fetch candidates) for one ayah, from the panel meals' words."""
    s, a = (int(x) for x in ref.split(":"))
    panel = [i for i, m in metas.items() if m.get("panel")]
    texts = [r[0] for r in con.execute(
        f"SELECT text FROM seg WHERE s=? AND a<=? AND coalesce(a_end,a)>=? AND src IN ({','.join('?' * len(panel))})",
        (s, a, a, *panel))] if con and panel else []
    entries = {}  # headword -> {dict: seg}
    for src_id in TR_DICTS:
        for seg, head in (con.execute("SELECT seg, head FROM seg WHERE src=?", (src_id,)) if con else []):
            h = re.sub(r"\d+$", "", tr_lower(seg.split(":", 1)[1].split("#")[0])).strip("-")
            entries.setdefault(h, {}).setdefault(src_id, seg)
    hits, stems = {}, {}
    for text in texts:
        toks = set(re.findall(r"[a-zçğıöşüâîû]+", tr_lower(text)))
        seen = set()
        for tok in toks:
            for h in entries:
                if len(h) >= 3 and tok.startswith(h) and len(tok) - len(h) <= 7 and h not in seen:
                    hits[h] = hits.get(h, 0) + 1
                    seen.add(h)
            st = tr_stem(tok)
            if len(st) >= 4 and st not in TR_STOP and tok not in TR_STOP:
                stems[st] = stems.get(st, 0) + 1
    matched = sorted((h for h, n in hits.items() if n >= 2), key=lambda h: -hits[h])
    covered = lambda st: any(st.startswith(h) or h.startswith(st) for h in entries)
    candidates = sorted((st for st, n in stems.items() if n >= max(2, len(texts) // 2) and not covered(st)),
                        key=lambda st: -stems[st])[:10]
    lines = [f"# {ref} — Turkish word history", "",
             "Key words of the panel meals at this ayah that have entries in the Turkish dictionaries of the corpus "
             "(how many panel meals use the word in brackets). Use them for anlam_tarihi (Turkish drift) and for meal "
             "kayma findings; cite NISANYAN:/TDK:/KUBBEALTI: locators.", ""]
    for h in matched:
        lines += [f"## {h} [{hits[h]} meals]", ""]
        for src_id, seg in entries[h].items():
            row = con.execute("SELECT text FROM seg WHERE seg=?", (seg,)).fetchone()
            body = (row[0] if row else "").strip()
            lines += [f"**{seg}**", body[:900] + (" …" if len(body) > 900 else ""), ""]
    if not matched:
        lines.append("(no key word of the panel meals has an entry yet)")
    if candidates:
        lines += ["", "Not yet in the corpus (fetch before the run if they matter): " + ", ".join(candidates)]
    return "\n".join(lines) + "\n", matched, candidates


def sources_md(con, metas: dict, ref: str) -> str:
    s, a = (int(x) for x in ref.split(":"))
    lines = [f"# {ref} — corpus locators for this ayah", "",
             "Every segment tied to this ayah (or a range containing it), grouped by kind. Read them with "
             "`python3 enrichment/v2/tools/corpus.py get <locator>`; search whole books with `corpus.py search`.", ""]
    if not con:
        return "\n".join(lines + ["(corpus index missing)"])
    rows = con.execute("SELECT seg, src, length(text) FROM seg WHERE s=? AND a<=? AND coalesce(a_end,a)>=? "
                       "ORDER BY src, a", (s, a, a)).fetchall()
    groups: dict[str, list] = {}
    for seg, sid, n in rows:
        groups.setdefault(metas.get(sid, {}).get("kind", "?"), []).append(f"{seg} ({n:,} chars)")
    for kind in sorted(groups):
        lines += [f"## {kind}", ""] + [f"- {x}" for x in groups[kind]] + [""]
    have = set(r[1] for r in rows)
    missing = sorted(i for i, m in metas.items() if m.get("locator") == "ayah" and m.get("access") != "hafiza"
                     and m.get("kind") in ("tafsir", "tafsir_tr", "meal") and i not in have)
    if missing:
        lines += ["## Not available for this ayah", "", ", ".join(missing), ""]
    pointers = sorted(i for i, m in metas.items() if m.get("access") == "hafiza")
    if pointers:
        lines += ["## Memory-only pointers (no local text; anything cited from them is model memory)", "",
                  ", ".join(pointers), ""]
    return "\n".join(lines)


def root_md(src, con, rid: str) -> str:
    name = src.root_name.get(rid, rid)
    lines = [f"# {name} ({rid})", "", "## Project dictionary (authoritative)", ""]
    lines += D.dict_lines(src, rid)
    key = name.replace(" ", "")
    if con:
        lines += ["## The six classical lexica, as routed to this root (full entries)", ""]
        for sid in CLASSICAL_IDS:
            rows = con.execute("SELECT seg, head, text, extra FROM seg WHERE src=? AND (json_extract(extra,'$.root_id')=? "
                               "OR seg=? OR seg LIKE ?)", (sid, rid, f"{sid}:{key}", f"{sid}:{key}#%")).fetchall()
            for seg, head, text, extra in rows:
                route = json.loads(extra or "{}").get("route", "")
                lines += [f"### {seg} [{head}] route={route}", "", text.strip(), ""]
            if not rows:
                lines += [f"### {sid}: no entry routed to this root", ""]
        lines += ["## Further lexica (read with corpus.py get)", ""]
        for sid in POINTER_LEXICA:
            locs = [r[0] for r in con.execute("SELECT seg FROM seg WHERE src=? AND (seg=? OR seg LIKE ?)",
                                              (sid, f"{sid}:{key}", f"{sid}:{key}#%"))]
            lines.append(f"- {sid}: {', '.join(locs) if locs else '—'}")
        lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------- checks

def run_check(path: Path, ref: str, out: Path) -> dict:
    out.parent.mkdir(parents=True, exist_ok=True)
    p = subprocess.run([sys.executable, "-B", str(CHECK), str(path), "--ref", ref, "--out", str(out), "--quiet"],
                       cwd=CHECK.parent, capture_output=True, text=True)
    if p.returncode or not out.exists():
        return {"error": (p.stdout + p.stderr)[-2000:]}
    return json.loads(out.read_text(encoding="utf-8"))


def problems(check: dict, label: str) -> list[dict]:
    out = []
    if check.get("error"):  # the checker itself failed: say so, never an empty list
        out.append({"file": label, "status": "check failed", "quote": check["error"]})
    for r in check.get("sources", []) or []:
        if r.get("status") not in ("ok", "declared"):
            out.append({"file": label, **{k: r.get(k) for k in ("line", "quote", "declared", "kind", "status", "found_in")}})
    for r in check.get("arabic_outside_tags", []) or []:
        out.append({"file": label, "status": "arabic outside tags", **(r if isinstance(r, dict) else {"quote": r})})
    seen = {(r.get("line"), r.get("quote")) for r in out}
    for r in check.get("unsourced_unmarked", []) or []:  # Arabic the checker found in no source and no bellek mark
        r = r if isinstance(r, dict) else {"quote": r}
        if (r.get("line"), r.get("quote")) not in seen:  # check.py also lists outside-tag items here
            out.append({"file": label, "status": "unsourced, unmarked", **r})
    return out


# ---------------------------------------------------------------- main

def dictionary_state() -> dict:
    m = json.loads(TR_MANIFEST.read_text(encoding="utf-8"))
    head = subprocess.run(["git", "-C", str(DICT_REPO), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    return {"transfer_commit": m.get("sourceCommit"), "dictionary_head": head, "match": m.get("sourceCommit") == head,
            "entries": m.get("entryCount"), "branches": m.get("branchCount")}


def write_numbered(pk: Path) -> None:
    """numbered/<page>.md: the base with its prose paragraphs numbered [¶n], as the agent reads it for anchoring."""
    (pk / "numbered").mkdir(exist_ok=True)
    for f in sorted((pk / "base").glob("*.md")):
        (pk / "numbered" / f.name).write_text(R.numbered(f.read_text(encoding="utf-8")), encoding="utf-8")


def build(s: int, force: bool, surah_base_path: Path | None) -> Path:
    """Every guard runs before anything is touched; an existing pack is kept aside and restored if the build fails."""
    pk = work_dir(s) / "pack"
    prev = pk.with_name("pack.prev")
    if pk.exists() and not force:
        raise SystemExit(f"{pk.relative_to(PG)} exists; --force rebuilds it (never while a stage is running)")
    if running_calls(s):
        raise SystemExit(f"S{s}: calls started without a run.log.json {running_calls(s)}: a rebuild would change "
                         f"their pack under them; wait for them, or, if the process is gone, "
                         f"`enrich.py confirm-dead --surah {s} --dir <dir>` first")
    if prev.exists():
        raise SystemExit(f"{prev.relative_to(PG)} exists (an earlier rebuild was interrupted): compare it with "
                         f"{pk.name}/ and remove the one that is not wanted first")
    dstate = dictionary_state()
    if not dstate["match"]:
        raise SystemExit(f"dictionary transfer {dstate['transfer_commit']} != ../dictionary HEAD {dstate['dictionary_head']}: "
                         f"sync quran-data (scripts/dictionary/sync_turkish_entries.py) first")
    con = corpus_con()
    if con is None:  # every meals/sources/turkish file would say "index missing": refuse instead
        raise SystemExit(f"corpus index {C.INDEX} missing: run tools/corpus.py build first")
    sb = surah_base_path or surah_base(s)
    if pk.exists():
        pk.rename(prev)
    try:
        out = _build(s, pk, sb, dstate, con)
    except BaseException:
        if pk.exists():
            shutil.rmtree(pk)
        if prev.exists():
            prev.rename(pk)
            print(f"WARNING: S{s}: rebuild failed; the previous pack is restored", file=sys.stderr, flush=True)
        raise
    if prev.exists():
        shutil.rmtree(prev)
    return out


def _build(s: int, pk: Path, sb: Path, dstate: dict, con) -> Path:
    (pk / "base").mkdir(parents=True)
    src = D.P.Sources()
    metas = source_meta(con)
    n_ayat = sum(1 for k in src.quran if k.startswith(f"{s}:") and not k.endswith(":0"))
    refs = [f"{s}:{a}" for a in range(1, n_ayat + 1)]

    shutil.copyfile(sb, pk / "base" / "surah.md")
    base = {"surah": {"path": str(sb.relative_to(PG)), "sha256": sha(sb)}, "ayat": {}}
    for ref in refs:
        a = int(ref.split(":")[1])
        p = ayah_base(s, a)
        if p:
            bad = R.marker_mismatches(p.read_text(encoding="utf-8"))
            if bad:  # an addition under the wrong paragraph would put enrichment blocks after the wrong text
                raise SystemExit(f"{p.relative_to(PG)}: v16 augment markers do not match their paragraphs: {bad}")
            shutil.copyfile(p, pk / "base" / f"{s}_{a}.md")
            base["ayat"][ref] = {"path": str(p.relative_to(PG)), "sha256": sha(p)}
        else:
            base["ayat"][ref] = None
    (pk / "base.json").write_text(json.dumps(base, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_numbered(pk)

    binding, roots, turkish = {}, [], {}
    for ref in refs:
        rows = []
        for w in src.words(ref):
            r = src.word_roots(w)
            rows.append({"w": w["w"], "qac_word_ref": w["ref"], "surface": w["surface"], "lemmas": w["lemmas"],
                         "pos": w["pos"], "root_keys": r["keys"],
                         "identity": [{"root_id": x, "root": src.root_name.get(x, x)} for x in r["identity"]],
                         "alternatives": [{"root_id": x, "root": src.root_name.get(x, x), "why": why} for x, why in r["alternatives"]],
                         "echo": [{"root_id": x, "root": src.root_name.get(x, x), "why": why} for x, why in r["echo"]]})
            roots += r["identity"] + [x for x, _ in r["alternatives"]]
        binding[ref] = rows
        d = pk / "ayah" / ref.replace(":", "_")
        d.mkdir(parents=True)
        (d / "words.md").write_text(words_md(src, ref), encoding="utf-8")
        (d / "dictionary.md").write_text(D.section(src, ref, "r2"), encoding="utf-8")
        (d / "usage.md").write_text(usage_md(src, ref), encoding="utf-8")
        (d / "meals.md").write_text(meals_md(con, metas, ref), encoding="utf-8")
        (d / "sources.md").write_text(sources_md(con, metas, ref), encoding="utf-8")
        tmd, matched, cands = turkish_md(con, metas, ref)
        (d / "turkish.md").write_text(tmd, encoding="utf-8")
        turkish[ref] = {"matched": matched, "fetch_candidates": cands}
    (pk / "binding.json").write_text(json.dumps(binding, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (pk / "roots").mkdir()
    for rid in dict.fromkeys(roots):
        (pk / "roots" / f"{rid}.md").write_text(root_md(src, con, rid), encoding="utf-8")

    errata = []
    chk = run_check(pk / "base" / "surah.md", f"{s}:1", pk / "check" / "surah.json")
    errata += problems(chk, "surah.md")
    for ref in refs:
        p = pk / "base" / f"{ref.replace(':', '_')}.md"
        if p.exists():
            errata += problems(run_check(p, ref, pk / "check" / f"{ref.replace(':', '_')}.json"), p.name)
    (pk / "errata_candidates.json").write_text(json.dumps(errata, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    failed = [e["file"] for e in errata if e.get("status") == "check failed"]
    if failed:
        print(f"WARNING: S{s}: check.py failed on {failed} (see errata_candidates.json)", flush=True)
    unbound = [(ref, w["surface"]) for ref, ws in binding.items() for w in ws if w["root_keys"] and not w["identity"]]
    kinds = {}
    for i, m in metas.items():
        kinds.setdefault(m.get("kind"), []).append(i)
    manifest = {
        "surah": s, "ayat": n_ayat, "built_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "base": base, "dictionary": dstate,
        "corpus": {"index": str(C.INDEX.relative_to(PG)), "index_mtime": C.INDEX.stat().st_mtime if C.INDEX.exists() else None,
                   "sources_by_kind": {k: sorted(v) for k, v in sorted(kinds.items(), key=lambda x: str(x[0]))},
                   "pointers_hafiza": sorted(i for i, m in metas.items() if m.get("access") == "hafiza")},
        "binding": {"words": sum(len(v) for v in binding.values()), "roots": len(set(roots)), "unbound": unbound},
        "errata_candidates": len(errata), "check_failed": failed,
        "turkish": {"per_ayah": turkish,
                    "fetch_candidates": sorted({c for v in turkish.values() for c in v["fetch_candidates"]})},
        "missing_ayah_bases": [r for r, v in base["ayat"].items() if not v],
        "files": {str(p.relative_to(pk)): sha(p) for p in sorted(pk.rglob("*")) if p.is_file() and p.name != "pack.json"},
    }
    (pk / "pack.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"S{s}: pack {pk.relative_to(PG)}: {n_ayat} ayat, {manifest['binding']['words']} words, "
          f"{manifest['binding']['roots']} roots, {len(unbound)} unbound, {len(errata)} errata candidates, "
          f"missing ayah bases {manifest['missing_ayah_bases'] or 'none'}")
    return pk


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--surah", type=int, required=True)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--surah-base", type=Path)
    a = ap.parse_args()
    build(a.surah, a.force, a.surah_base)


if __name__ == "__main__":
    main()
