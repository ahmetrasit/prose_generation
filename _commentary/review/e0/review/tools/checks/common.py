"""Shared, read-only loaders and matchers for check.py, lint.py and scorecard.py (E0 checks).

Sources (read-only, raw project data; nothing from earlier pipeline packets):
  quran-data/data/text/quran-uthmani.tsv                         Quran text (S:A|text)
  quran-data/data/dictionary/tr/root_*_entry.json                dictionary branches (branch_ref, branch_kind, scope note,
                                                                 image, what_is, source_phrase_ar with source tags) and
                                                                 occurrence evidence (which root each Quran word carries)
  dictionary/data/output/root_packets/root_*.json                full early entries (dictionary_sources[].entry_text_clean)
                                                                 of the six early sources, and lexical senses per branch
  quran-roots/_corpus/lexicons/cache/openiti_context.sqlite      Majaz al-Quran, direct text (quran_specialized_entries,
                                                                 source 'majaz_quran')
  study/_project_corpus/qiraat.tsv                               variant readings
  root-dossier/out/activation_map.tsv                            the [plain] branch per Quran word (role 'dominant')

Late compilations (Lisan, Lane, al-Qamus) are never read. The derived index is cached in ./cache (rebuilt when a
source directory changes: file count, total size, newest mtime).
"""
from __future__ import annotations

import bisect
import csv
import glob
import gzip
import json
import os
import pickle
import re
import sqlite3
import sys
from functools import lru_cache
from pathlib import Path

csv.field_size_limit(sys.maxsize)

HERE = Path(__file__).resolve().parent
CACHE = HERE / "cache"
PROJ = Path("/Volumes/OZTURK/_projects")
SRC = {
    "quran": PROJ / "quran-data/data/text/quran-uthmani.tsv",
    "tr_entries": PROJ / "quran-data/data/dictionary/tr",
    "root_packets": PROJ / "dictionary/data/output/root_packets",
    "majaz": PROJ / "quran-roots/_corpus/lexicons/cache/openiti_context.sqlite",
    "qiraat": PROJ / "study/_project_corpus/qiraat.tsv",
    "activation_map": PROJ / "root-dossier/out/activation_map.tsv",
    "furuq": PROJ / "quran-slm/resources/source/furuq_full_branches_ar.tsv",  # root letters for ids without a packet
}
EARLY_SOURCES = ("ayn", "maqayis", "jamhara", "sihah", "tahdhib", "mufradat")
BOUND_KINDS = ("collocation", "non_bare")  # "yalin anlama genellenmez": the sense lives only in its construction/unit
CACHE_VERSION = 4

# ------------------------------------------------------------------------------------------------ Arabic folding

ARABIC_CHARS = "؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿"
ARABIC_RUN = re.compile(f"[{ARABIC_CHARS}]+(?:[  ،،]+[{ARABIC_CHARS}]+)*")
ARABIC_LETTER = re.compile("[ء-يٱ-ۓ]")
_DIAC = re.compile("[ؐ-ًؚ-ٟۖ-ۭـ]")
_AL = str.maketrans({"ٱ": "ا", "أ": "ا", "إ": "ا", "آ": "ا", "ى": "ي", "ة": "ه", "ؤ": "و", "ئ": "ي", "ء": "",
                     "ی": "ي", "ک": "ك", "﻿": ""})
_NONLETTER = re.compile("[^ء-ي ]+")


def fold(s: str, dagger: str = "drop") -> str:
    """Letters only, diacritics removed, alif/hamza/ya/ta-marbuta unified, hamza dropped, single spaces.
    dagger='drop' removes the superscript alif (ٱلرَّحْمَٰنِ -> الرحمن); dagger='alif' writes it as a full alif and folds
    Uthmani waw/ya + dagger to alif (ٱلصَّلَوٰةِ -> الصلاه, ٱلصِّرَٰطَ -> الصراط), matching classical spelling."""
    s = s or ""
    if dagger == "alif":
        s = re.sub("[وى][ً-ٟۖ-ۭ]*ٰ", "ا", s)
        s = s.replace("ٰ", "ا")
    else:
        s = s.replace("ٰ", "")
    s = _DIAC.sub("", s).translate(_AL)
    s = _NONLETTER.sub(" ", s)
    return re.sub(r"\s+", " ", s).strip()


def fold_variants(s: str) -> list[str]:
    out = []
    for d in ("drop", "alif"):
        f = fold(s, d)
        if f and f not in out:
            out.append(f)
    return out


def skeleton(folded: str) -> str:
    """Consonantal skeleton of a folded string (long vowels removed): the loose fallback only."""
    return re.sub("[اوي]", "", folded)


def nroot(r: str) -> str:
    """Root letters with spaces, hamza seats unified to ء."""
    r = re.sub("[أإؤئآ]", "ء", (r or "").replace("ٱ", "ا"))
    return " ".join(r.replace(" ", ""))


# ------------------------------------------------------------------------------------------------ refs and text

REF = re.compile(r"(?<![\d.:/])(\d{1,3}):(\d{1,3})(?::(\d{1,3}))?(?:\s*[-–]\s*(\d{1,3})(?![\d:]))?(?![\d])")


def parse_ref(ref: str) -> tuple[int, int]:
    s, a = ref.split(":")[:2]
    return int(s), int(a)


def refs_in(text: str, quran: dict | None = None) -> set[str]:
    """Valid S:A refs (S:A:W folded to S:A; S:A-B ranges expanded when B > A, at most 40 ayat)."""
    quran = quran if quran is not None else quran_text()
    out = set()
    for m in REF.finditer(text):
        s, a = int(m.group(1)), int(m.group(2))
        if f"{s}:{a}" not in quran:
            continue
        out.add(f"{s}:{a}")
        if m.group(4) and not m.group(3):
            b = int(m.group(4))
            if a < b <= a + 40:
                out |= {f"{s}:{x}" for x in range(a + 1, b + 1) if f"{s}:{x}" in quran}
    return out


TAG = re.compile(r"\{\{ar:([^}|]*)(?:\|[^}]*)?\}\}|\{ar:([^,}]*)(?:,[^}]*)?\}")


def tags(text: str) -> list[tuple[int, int, str]]:
    """(start, end, arabic) for every {ar:…, tr:…, gloss:…} and {{ar:…}} tag."""
    return [(m.start(), m.end(), (m.group(1) if m.group(1) is not None else m.group(2)).strip())
            for m in TAG.finditer(text)]


def line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def sentences(text: str) -> list[tuple[int, int]]:
    """(start, end) spans of sentences: split after . ! ? … followed by space, and at newlines. Tags are opaque."""
    masked = TAG.sub(lambda m: "x" * (m.end() - m.start()), text)
    spans, start = [], 0
    for m in re.finditer(r"(?<=[.!?…])[\"”’»)]*\s+|\n+", masked):
        end = m.start()
        if masked[start:end].strip():
            spans.append((start, end))
        start = m.end()
    if masked[start:].strip():
        spans.append((start, len(text)))
    return spans


def sentence_at(spans: list[tuple[int, int]], pos: int) -> int:
    i = bisect.bisect_right([s for s, _ in spans], pos) - 1
    return max(i, 0)


def words(text: str) -> list[str]:
    return text.split()


def paragraphs(text: str) -> list[str]:
    """Blank-line separated blocks that are not headings."""
    return [p for p in re.split(r"\n\s*\n", text) if p.strip() and not p.strip().startswith("#")]


def est_tokens(text: str) -> int:
    """The cost critic's calibrated formula (X-cost-critic c01): 4581 + 1.151 x Arabic chars + 0.366 x other chars."""
    ar = len(re.findall(f"[{ARABIC_CHARS}]", text))
    return int(4581 + 1.151 * ar + 0.366 * (len(text) - ar))


# Negation / disclaimer frames. NEG_E2 is byte-identical to experiments/e2_score.py (for continuity with EXPERIMENTS.md).
NEG_E2 = re.compile(r"\b(değil(?:dir|dir\.)?|sayılmaz|anlamına gelmez|demek değildir|söylemez|gerektirmez)\b", re.I)
DISCLAIMERS = {
    "değil": r"\bdeğil(?:dir)?\b",
    "değil,": r"\bdeğil,",
    "sayılmaz": r"\bsayılmaz\b",
    "anlamına gelmez": r"\banlamına gelm(?:ez|iyor)\b",
    "demek değildir": r"\bdemek değildir\b",
    "söylemez": r"\bsöylem(?:ez|iyor)\b",
    "gerektirmez": r"\bgerektirmez\b",
    "iddia etmez": r"\biddia etmez\b",
    "kanıtlamaz": r"\bkanıtlamaz\b",
    "taşımaz": r"\btaşımaz\b",
    "eşitleme": r"\beşitleme\w*",
    "kesin değildir": r"\bkesin değildir\b",
}
NOT_ONLY = re.compile(r"\b(yalnızca|sadece|salt|yalnız)\b[^.!?]{0,80}\bdeğil", re.I)


def negation(text: str) -> dict:
    w = len(text.split())
    n = len(NEG_E2.findall(text))
    br = {k: len(re.findall(rx, text, re.I)) for k, rx in DISCLAIMERS.items()}
    return {"neg_e2_count": n, "neg_e2_per_1000": round(1000 * n / w, 2) if w else None,
            "breakdown": {k: v for k, v in br.items() if v}, "not_only_frames": len(NOT_ONLY.findall(text))}


# ------------------------------------------------------------------------------------------------ Quran

@lru_cache(maxsize=1)
def quran_text() -> dict[str, str]:
    out = {}
    for line in SRC["quran"].read_text(encoding="utf-8").splitlines():
        line = line.replace("﻿", "")
        if "|" not in line:
            continue
        ref, t = line.split("|", 1)
        s, a = ref.split(":")
        if a != "0":
            out[f"{int(s)}:{int(a)}"] = t.strip()
    return out


@lru_cache(maxsize=None)
def surah_len(s: int) -> int:
    q = quran_text()
    n = 0
    while f"{s}:{n + 1}" in q:
        n += 1
    return n


def window(ref: str, radius: int = 7) -> list[str]:
    s, a = parse_ref(ref)
    return [f"{s}:{x}" for x in range(max(1, a - radius), min(surah_len(s), a + radius) + 1)]


# ------------------------------------------------------------------------------------------------ corpus search

PROCLITICS = {"و", "ف", "ب", "ل", "ك", "س", "ا", "ال", "وال", "فال", "بال", "كال", "لل", "ولل", "فلل", "وب", "ول", "فب",
              "فل", "وك", "فك", "اف", "او", "ول", "وس", "فس", "لي"}
ENCLITICS = {"ه", "ها", "هم", "هما", "هن", "ك", "كم", "كما", "كن", "ي", "ني", "نا", "ا"}
SEP = "\n"


class Corpus:
    """Units of folded text joined by newlines; find(q) returns (unit index, level) with token-boundary checks.
    level 'exact' = whole tokens; 'clitic' = a proclitic before or a pronoun enclitic after the quoted tokens."""

    def __init__(self, units: list[str]):
        self.text = SEP.join(units) + SEP
        self.starts, pos = [], 0
        for u in units:
            self.starts.append(pos)
            pos += len(u) + 1

    def unit(self, pos: int) -> int:
        return bisect.bisect_right(self.starts, pos) - 1

    def unit_text(self, u: int) -> str:
        end = self.starts[u + 1] - 1 if u + 1 < len(self.starts) else len(self.text) - 1
        return self.text[self.starts[u]:end]

    def find(self, q: str, limit: int = 5000):
        t, out, i = self.text, [], 0
        if not q:
            return out
        while len(out) < limit:
            i = t.find(q, i)
            if i < 0:
                break
            j = i + len(q)
            ls = t.rfind(" ", 0, i) + 1
            ls = max(ls, t.rfind(SEP, 0, i) + 1)
            pre = t[ls:i]
            re_ = min(x for x in (t.find(" ", j), t.find(SEP, j), len(t)) if x >= 0)
            post = t[j:re_]
            if (pre == "" or pre in PROCLITICS) and (post == "" or post in ENCLITICS):
                out.append((self.unit(i), "exact" if pre == "" and post == "" else "clitic"))
            i += 1
        return out


def _parts(quote_folded: str) -> list[str]:
    return [p.strip() for p in re.split(r"\s*(?:\.\.\.|…)\s*", quote_folded) if p.strip()]


def search_units(corpus: Corpus, quote: str, loose_corpus: Corpus | None = None) -> dict[int, str]:
    """unit index -> best level for a raw quotation (ellipses split it into parts that must share one unit)."""
    raw_parts = [p for p in re.split(r"\s*(?:\.\.\.|…)\s*", quote) if p.strip()]
    best: dict[int, str] = {}
    rank = {"exact": 0, "clitic": 1, "article": 2, "loose": 3}
    per_part = []
    for rp in raw_parts:
        hits: dict[int, str] = {}
        for v in fold_variants(rp):
            cands = [(v, None)]
            first = v.split(" ")[0]
            for art in ("وال", "فال", "بال", "ال"):
                if first.startswith(art) and len(first) - len(art) >= 2:
                    cands.append((v[len(art):], "article"))
                    break
            for q, forced in cands:
                if len(q.replace(" ", "")) < 2:
                    continue
                for u, lvl in corpus.find(q):
                    lvl = forced or lvl
                    if u not in hits or rank[lvl] < rank[hits[u]]:
                        hits[u] = lvl
        if not hits and loose_corpus is not None:
            v = skeleton(fold(rp, "drop"))
            if len(v.replace(" ", "")) >= 4 or (len(v.split()) >= 2 and len(v.replace(" ", "")) >= 3):
                for u, _ in loose_corpus.find(v):
                    hits.setdefault(u, "loose")
        per_part.append(hits)
    if not per_part:
        return best
    common = set(per_part[0])
    for h in per_part[1:]:
        common &= set(h)
    for u in common:
        best[u] = max((h[u] for h in per_part), key=lambda l: rank[l])
    return best


def _tok_match(t: str, q: str) -> bool:
    if t == q:
        return True
    if t.endswith(q) and t[:-len(q)] in PROCLITICS:
        return True
    return t.startswith(q) and t[len(q):] in ENCLITICS


def gapped_units(corpus: Corpus, quote: str, max_gap: int = 4, limit: int = 300) -> dict[int, str]:
    """Units holding every token of a quotation of 3+ tokens in order, with at most max_gap other tokens between two
    quoted tokens (a silent elision: 'حافظت على الرجل إذا حفظته' for '… على الرجل محافظة وحفاظا إذا حفظته …')."""
    out: dict[int, str] = {}
    for v in fold_variants(quote):
        toks = v.split()
        if len(toks) < 3:
            continue
        key = max(toks, key=len)
        for u, _ in corpus.find(key, limit=limit):
            if u in out:
                continue
            ut = corpus.unit_text(u).split()
            for i, t in enumerate(ut):
                if not _tok_match(t, toks[0]):
                    continue
                j, ok = i, True
                for q in toks[1:]:
                    for k in range(j + 1, min(len(ut), j + 2 + max_gap)):
                        if _tok_match(ut[k], q):
                            j = k
                            break
                    else:
                        ok = False
                        break
                if ok:
                    out[u] = "gapped"
                    break
    return out


ROOT_NAME = re.compile(r"^[ء-يٱ](?:\s*[-‐–\s]\s*[ء-يٱ]){1,4}$")


def root_name(text: str) -> str | None:
    """'ق و م' / 'ق-و-م' (letters spaced or hyphenated) -> 'ق و م'; else None."""
    t = _DIAC.sub("", text.replace("ٰ", "")).strip()
    if not ROOT_NAME.match(t):
        return None
    return nroot(re.sub(r"[\s\-‐–]", "", t))


# ------------------------------------------------------------------------------------------------ cached index

def _dir_sig(path: Path, pattern: str) -> list:
    files = glob.glob(str(path / pattern))
    tot, newest = 0, 0.0
    for f in files:
        st = os.stat(f)
        tot += st.st_size
        newest = max(newest, st.st_mtime)
    return [len(files), tot, round(newest, 1)]


def _file_sig(path: Path) -> list:
    st = os.stat(path)
    return [st.st_size, round(st.st_mtime, 1)]


def source_signature() -> dict:
    return {"version": CACHE_VERSION,
            "quran": _file_sig(SRC["quran"]),
            "tr_entries": _dir_sig(SRC["tr_entries"], "root_*_entry.json"),
            "root_packets": _dir_sig(SRC["root_packets"], "root_*.json"),
            "majaz": _file_sig(SRC["majaz"]),
            "qiraat": _file_sig(SRC["qiraat"]),
            "activation_map": _file_sig(SRC["activation_map"]),
            "furuq": _file_sig(SRC["furuq"])}


def _segments(phrase: str) -> list[tuple[str, list[str]]]:
    """Split a source_phrase_ar into (segment, source tags); a tag '(a;b)' closes the group of segments before it."""
    out, pending = [], []
    for seg in re.split("؛", phrase or ""):
        seg = seg.strip()
        if not seg:
            continue
        m = re.search(r"\(([a-z_;\- ]+)\)\s*$", seg)
        if m:
            srcs = [x.strip() for x in m.group(1).split(";") if x.strip()]
            pending.append(seg[:m.start()].strip())
            out += [(p, srcs) for p in pending]
            pending = []
        else:
            pending.append(seg)
    out += [(p, []) for p in pending]
    return out


def build_index(verbose: bool = True) -> dict:
    """Read the raw sources once and keep only what the checks need."""
    if verbose:
        print("building E0 check index from the raw sources (one-off, ~1-2 min) ...", file=sys.stderr)
    packets = {}
    for f in sorted(glob.glob(str(SRC["root_packets"] / "root_*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        rid = d.get("root_envelope_id") or Path(f).stem
        early = {}
        for s in d.get("dictionary_sources", []) or []:
            sid, t = s.get("source_id"), (s.get("entry_text_clean") or "").strip()
            if sid in EARLY_SOURCES and t and t != "-":
                early.setdefault(sid, []).append(t)
        lex = []
        for ls in d.get("lexical_senses", []) or []:
            lex.append({"branch_ids": (ls.get("branch_ids") or "").split(";"),
                        "expression_ar": ls.get("expression_ar") or "", "sense_ar": ls.get("sense_ar") or "",
                        "source_phrase_ar": ls.get("source_phrase_ar") or ""})
        packets[rid] = {"root": nroot(d.get("root_norm") or ""), "early": {k: "\n".join(v) for k, v in early.items()},
                        "lex": lex}
    with open(SRC["furuq"], encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            rid = r.get("source_root_id") or ""
            if rid and rid not in packets and r.get("surface_root"):
                packets[rid] = {"root": nroot(r["surface_root"]), "early": {}, "lex": []}
    branches, word_root = [], {}
    for f in sorted(glob.glob(str(SRC["tr_entries"] / "root_*_entry.json"))):
        d = json.load(open(f, encoding="utf-8"))
        rid = d["root_envelope_id"]
        root = packets.get(rid, {}).get("root", "")
        for b in d.get("branches", []):
            ls = b.get("lexicalization_scope") or {}
            cg = b.get("concept_gloss") or {}
            branches.append({
                "branch_ref": b["branch_ref"], "root_id": rid, "root": root, "branch": b["branch_ref"].split("/")[1],
                "branch_kind": ls.get("branch_kind") or "", "scope_note": ls.get("note") or "",
                "image_ar": b.get("branch_image_ar") or "", "what_is_ar": b.get("what_is_ar") or "",
                "what_is_not_ar": b.get("what_is_not_ar") or "", "source_phrase_ar": b.get("source_phrase_ar") or "",
                "sources": b.get("sources") or [], "tr_concept": cg.get("text") or "",
                "tr_glosses": [g.get("target_gloss") for g in b.get("lexical_glosses") or [] if g.get("target_gloss")]})
        for o in (d.get("occurrence_evidence") or {}).get("occurrences", []) or []:
            w = o.get("qac_word_ref")
            if w:
                word_root.setdefault(w, [])
                if rid not in word_root[w]:
                    word_root[w].append(rid)
    plain = {}
    with open(SRC["activation_map"], encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r.get("role") == "dominant" and (r.get("branch_ref") or "").startswith("root_"):
                w = ":".join(r["qac_word_ref"].split(":")[:3])
                plain.setdefault(w, [])
                if r["branch_ref"] not in plain[w]:
                    plain[w].append(r["branch_ref"])
    con = sqlite3.connect(f"file:{SRC['majaz']}?mode=ro", uri=True)
    majaz = [{"id": i, "marker": m or "", "heading": h or "", "text": t or ""} for i, m, h, t in con.execute(
        "select id, ayah_marker, section_title, entry_text_clean from quran_specialized_entries "
        "where source='majaz_quran' order by id")]
    con.close()
    qiraat = []
    with open(SRC["qiraat"], encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            qiraat.append({"word_ref": r["tsv_word_ref"], "arabic": r["qiraat_arabic"],
                           "readers": r.get("qiraat_reader_set", ""), "note": (r.get("qiraat_note") or "")[:200]})
    return {"signature": source_signature(), "packets": packets, "branches": branches, "word_root": word_root,
            "plain": plain, "majaz": majaz, "qiraat": qiraat}


@lru_cache(maxsize=1)
def index() -> dict:
    CACHE.mkdir(parents=True, exist_ok=True)
    p = CACHE / "index.pkl.gz"
    sig = source_signature()
    if p.exists():
        try:
            with gzip.open(p, "rb") as fh:
                d = pickle.load(fh)
            if d.get("signature") == sig:
                return d
        except Exception:
            pass
    d = build_index()
    with gzip.open(p, "wb") as fh:
        pickle.dump(d, fh, protocol=pickle.HIGHEST_PROTOCOL)
    (CACHE / "signature.json").write_text(json.dumps(sig, indent=1) + "\n", encoding="utf-8")
    return d


@lru_cache(maxsize=1)
def branch_by_ref() -> dict[str, dict]:
    return {b["branch_ref"]: b for b in index()["branches"]}


@lru_cache(maxsize=1)
def branch_by_letters() -> dict[str, str]:
    """'ح م م B001' -> 'root_000001/B001'."""
    return {f"{b['root']} {b['branch']}": b["branch_ref"] for b in index()["branches"] if b["root"]}


@lru_cache(maxsize=1)
def root_letters() -> dict[str, str]:
    return {rid: p["root"] for rid, p in index()["packets"].items()}


def ayah_roots(ref: str) -> list[str]:
    """root ids carried by the words of an ayah (dictionary occurrence evidence), in word order."""
    s, a = parse_ref(ref)
    out = []
    wr = index()["word_root"]
    for w in range(1, 200):
        k = f"{s}:{a}:{w}"
        if k not in wr:
            if w > 3 and f"{s}:{a}:{w + 1}" not in wr and f"{s}:{a}:{w + 2}" not in wr:
                break
            continue
        for r in wr[k]:
            if r not in out:
                out.append(r)
    return out


def plain_branches(ref: str) -> set[str]:
    """Branch refs the root dossier marks [plain] (role 'dominant') at the words of an ayah."""
    s, a = parse_ref(ref)
    return {b for w, bs in index()["plain"].items() if w.startswith(f"{s}:{a}:") for b in bs}


# ---- corpora built lazily from the index

@lru_cache(maxsize=1)
def quran_corpora():
    q = quran_text()
    refs = list(q)
    drop = Corpus([fold(q[r], "drop") for r in refs])
    alif = Corpus([fold(q[r], "alif") for r in refs])
    loose = Corpus([skeleton(fold(q[r], "drop")) for r in refs])
    return refs, drop, alif, loose


@lru_cache(maxsize=1)
def dict_corpus():
    """One unit per dictionary text field: (branch_ref, field, source tags)."""
    units, meta = [], []
    for b in index()["branches"]:
        for fld in ("image_ar", "what_is_ar", "what_is_not_ar"):
            if b[fld]:
                units.append(fold(b[fld]))
                meta.append((b["branch_ref"], fld, []))
        for seg, srcs in _segments(b["source_phrase_ar"]):
            units.append(fold(seg))
            meta.append((b["branch_ref"], "source_phrase_ar", srcs))
    for rid, p in index()["packets"].items():
        for ls in p["lex"]:
            refs = [f"{rid}/{x}" for x in ls["branch_ids"] if x]
            if not refs:
                continue
            for fld in ("expression_ar", "sense_ar"):
                if ls[fld]:
                    units.append(fold(ls[fld]))
                    meta.append((refs[0], "lexical_" + fld, []))
            for seg, srcs in _segments(ls["source_phrase_ar"]):
                units.append(fold(seg))
                meta.append((refs[0], "lexical_source_phrase", srcs))
    return Corpus(units), meta


@lru_cache(maxsize=1)
def early_corpus():
    units, meta = [], []
    for rid, p in index()["packets"].items():
        for sid, t in p["early"].items():
            units.append(fold(t))
            meta.append((rid, sid))
    return Corpus(units), meta


@lru_cache(maxsize=1)
def majaz_corpus():
    m = index()["majaz"]
    return Corpus([fold(e["text"]) for e in m]), m


@lru_cache(maxsize=1)
def qiraat_index() -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    for r in index()["qiraat"]:
        for v in fold_variants(r["arabic"]):
            out.setdefault(v, []).append(r)
    return out


def sha256(path: Path | str) -> str:
    import hashlib
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()
