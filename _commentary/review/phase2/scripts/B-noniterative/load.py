"""Shared read-only loaders for the B-noniterative Phase 2 scripts.

Sources (read-only):
  prose_generation/_commentary/v15/data/{quran,words,lemmas,branches}.tsv   (built by v15 build.py base)
  quran-data/data/dictionary/tr/root_*_entry.json                            (branch_kind = lexicalization_scope)
  quran-data/data/grammar/contextual/collocation_profiles_v2.tsv
"""
import csv, json, glob, re, os, functools, sys
csv.field_size_limit(sys.maxsize)

PG = "/Volumes/OZTURK/_projects/prose_generation"
QD = "/Volumes/OZTURK/_projects/quran-data"
V15D = f"{PG}/_commentary/v15/data"
OUT = os.path.dirname(os.path.abspath(__file__))

AR_DIAC = re.compile(r"[ؐ-ًؚ-ٰٟۖ-ۭـ]")


def norm(s: str) -> str:
    """Loose Arabic folding: strip diacritics/tatweel, unify alef/hamza/ya/ta marbuta forms."""
    s = AR_DIAC.sub("", s)
    s = s.replace("ٱ", "ا").replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")
    s = s.replace("ؤ", "و").replace("ئ", "ي").replace("ى", "ي").replace("ة", "ه").replace("ء", "")
    return s


def nroot(r: str) -> str:
    """Root key normalisation (dictionary writes ح م ء, grammar writes ح م أ)."""
    return r.replace("أ", "ء").replace("إ", "ء").replace("ؤ", "ء").replace("ئ", "ء").replace("آ", "ء").strip()


@functools.lru_cache(None)
def quran():
    return {r["ref"]: r["text"] for r in csv.DictReader(open(f"{V15D}/quran.tsv", encoding="utf-8"), delimiter="\t")}


@functools.lru_cache(None)
def words():
    rows = list(csv.DictReader(open(f"{V15D}/words.tsv", encoding="utf-8"), delimiter="\t"))
    by_ayah = {}
    for r in rows:
        by_ayah.setdefault(f"{r['surah']}:{r['ayah']}", []).append(r)
    return rows, by_ayah


@functools.lru_cache(None)
def root_index():
    """root -> list of refs S:A:W (all rooted words)."""
    rows, _ = words()
    idx = {}
    for r in rows:
        for root in (r["roots"] or "").split("|"):
            root = nroot(root)
            if root:
                idx.setdefault(root, []).append(r["ref"])
    return idx


@functools.lru_cache(None)
def branches():
    """(root, B) -> row dict, Quranic-attested + furuq, from v15 branches.tsv."""
    out = {}
    for r in csv.DictReader(open(f"{V15D}/branches.tsv", encoding="utf-8"), delimiter="\t"):
        out[(nroot(r["root"]), r["branch"])] = r
    return out


@functools.lru_cache(None)
def branches_by_root():
    d = {}
    for (root, b), r in branches().items():
        d.setdefault(root, []).append(r)
    for v in d.values():
        v.sort(key=lambda r: r["branch"])
    return d


@functools.lru_cache(None)
def branch_kind():
    """(root_id, 'Bnnn') -> (branch_kind, note) from the Turkish dictionary entries."""
    out = {}
    for f in glob.glob(f"{QD}/data/dictionary/tr/root_*_entry.json"):
        d = json.load(open(f, encoding="utf-8"))
        for b in d.get("branches", []):
            rid, bn = b["branch_ref"].split("/")
            ls = b.get("lexicalization_scope") or {}
            out[(rid, bn)] = (ls.get("branch_kind", "missing"), ls.get("note", ""),
                              b.get("source_phrase_ar", ""), b.get("branch_image_ar", ""), b.get("what_is_ar", ""))
    return out


def kind_of(row):
    return branch_kind().get((row["root_id"], row["branch"]), ("missing", "", "", "", ""))


@functools.lru_cache(None)
def collocations():
    d = {}
    for r in csv.DictReader(open(f"{QD}/data/grammar/contextual/collocation_profiles_v2.tsv", encoding="utf-8"),
                            delimiter="\t"):
        d.setdefault(nroot(r["root_arabic"]), []).append(r)
    return d


def surah_len(s: int) -> int:
    q = quran()
    n = 0
    while f"{s}:{n+1}" in q:
        n += 1
    return n


def ayah_roots(ref):
    _, by = words()
    out = []
    for w in by.get(ref, []):
        for root in (w["roots"] or "").split("|"):
            root = nroot(root)
            if root and root not in out:
                out.append(root)
    return out


def est_tokens(chars: int) -> int:
    """Rough token estimate for mixed Arabic/Turkish/English markdown: ~2.6 chars per token
    (calibrated below in cost_model.py against recorded claude -p input_tokens for v9 cold/dict arms)."""
    return int(chars / 2.6)
