#!/usr/bin/env python3
"""Confident OCR repair for the OCR-imported modern-Turkish corpus sources.

    python3 enrichment/v2/fetch/ocr_fix.py SOURCE_ID [--dry] [--samples N] [--only RULE,RULE] [--skip RULE,RULE]

Reads corpus/<ID>/segments.jsonl and corrects OCR damage only where the repair is certain:

  header   running page/volume headers left inside the text («Sayfa:142 Cüz:4», «6418 HULÂSAT-ÜL BEYAN Cüz: 30»)
  noise    leftover Arabic-noise punctuation runs («, , , , ,»)
  hyphen   hyphenation leftovers («aslın- da» -> «aslında»), only when the joined word is attested
  join     letter-spaced / split words («O'nda n», «İ man», «zam an lar»): the joined form is attested in the
           clean Turkish meals and the spaced sequence never occurs there
  sub      one known OCR confusion (rı->n, ı->r, fi->â, ...) turns a non-word into an attested word, with a
           clear winner among the candidates
  case     stray capitals inside a word («kİ», «İŞte»), when the lower-cased form is attested

«Attested» is measured on a clean vocabulary: every born-digital Turkish meal of the corpus (all MEAL-* sources
except the OCR ones and the interlinears), plus the headwords of NISANYAN, TDK and KUBBEALTI.

Every changed segment keeps its original as `text_ocr` (and `notes_ocr`), and `ocr_fixes` lists
[[from, to, rule], ...]. Re-running starts from `text_ocr`, so the tool is idempotent. source.json gets an
`ocr_corrections` record in its ingestion block and a sentence in notes. Nothing else is touched: Arabic,
transliteration, verse numbers, author spelling and punctuation stay as imported.
"""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import glob
import json
import random
import re
import sys
from pathlib import Path

PG = Path(__file__).resolve().parents[3]
CORPUS = PG / "enrichment" / "corpus"

OCR_SOURCES = {"MEAL-AKDEMIR", "MEAL-MOZTURK", "MEAL-ELIACIK", "MEAL-ZDUMAN", "TAFSIR-ZDUMAN", "MEAL-OCELIK",
               "TAFSIR-OCELIK", "MEAL-DOGRUL", "MEAL-VEHBI", "TAFSIR-VEHBI", "RIYAD-TR"}
# Not in the clean vocabulary: the other OCR imports and the Middle Turkic / Old Anatolian interlinears.
NOT_CLEAN = ("EAT", "KARAHANLI", "ATAY", "HAMIDULLAH", "HDKD")
TR_DICTS = ("NISANYAN", "TDK", "KUBBEALTI")
FIELDS = ("text", "notes")
RULES = ("header", "noise", "hyphen", "join", "sub", "case")

TOK = re.compile(r"[^\W\d_]+(?:['’ʼ´][^\W\d_]+)*['’ʼ´]?")
MIDCAP = re.compile(r"[a-zçğıöşüâîû] (Ş[^\W\d_]*(?:['’][^\W\d_]+)?)")
APOS = re.compile(r"['’ʼ´]")


def tr_lower(s: str) -> str:
    return s.replace("I", "ı").replace("İ", "i").lower()


def key(w: str) -> str:
    return tr_lower(APOS.sub("", w))


FOLD = str.maketrans("âîû", "aiu")


def fold(k: str) -> str:
    return k.translate(FOLD)


# ---------------------------------------------------------------------------------------------------------------
# per-source patterns for running headers and noise (regex -> removed, surrounding whitespace collapsed)
HEADERS: dict[str, list[str]] = {
    "MEAL-ELIACIK": [r"\bSayfa\s*:\s*\d{1,3}\b", r"\bCüz\s*:\s*[0-9lIO]{1,3}\b"],
    "MEAL-AKDEMIR": [r"(?:[A-ZÂÎÛŞÇĞÖÜİ][\w'’-]*\s+){1}S\s?[ûu]\s?resi[.,]\s*Cüz\s*\d{1,2}[.,]?(?:\s*S[ûuü]re\s*\d{1,3})?"],
    "MEAL-MOZTURK": [r"\bCüz\s+\d{1,2}[oO]?(?:\s*-\s*\d(?:\s?\d)?)?(?![\w])"],
    "MEAL-VEHBI": [r"(?:\S{0,3}\d{3,4}\s+)?HUL[ÂA]S[^\n]{0,40}?\b[Cc]\S{0,3}z\s*[:;]+\s*\d{1,2}\b"],
    "TAFSIR-VEHBI": [r"(?:\S{0,3}\d{3,4}\s+)?HUL[ÂA]S[^\n]{0,40}?\b[Cc]\S{0,3}z\s*[:;]+\s*\d{1,2}\b"],
}
NOISE = re.compile(r"(?<!\S)(?:[,;:.'’]{1,2}(?:\s+|$)){3,}")

SUFFIX_FRAGMENTS = set("nda nde dan den tan ten lar ler nın nin nun nün ını ini unu ünü ına ine una üne yla yle "
                       "ında inde unda ünde ndan nden larında lerinde ları leri ın in un ün da de ta te mış miş "
                       "muş müş dır dir dür tır tir ki ya ye na ne ıyla iyle".split())

SPACED_SOURCES = {"MEAL-AKDEMIR"}
NOT_WORDS = SUFFIX_FRAGMENTS - set("ki da de ya ye ne na ta te".split())

# (ocr, true) single-step confusions, applied at one or two places of an unknown word. Lower-case letters only.
SUBS = [("n", "rı"), ("n", "ri"), ("ı", "r"), ("ı", "i"), ("l", "ı"), ("l", "i"), ("ı", "l"),
        ("fi", "â"), ("fı", "â"), ("a", "â"), ("rn", "m"), ("m", "ın"), ("m", "in"), ("c", "ç"), ("t", "r"),
        ("s", "ş"), ("g", "ğ"), ("n", "r"), ("ü", "û"), ("ğ", "â")]
WEIGHT = {("n", "r"): 1.6}  # rı->n is the usual scan error; r->n alone is rare, so it only competes
# the typical scan/OCR confusions: a word repaired only by these may be accepted without verse confirmation
CORE = {("n", "rı"), ("n", "ri"), ("ı", "r"), ("m", "ın"), ("m", "in"), ("fi", "â"), ("fı", "â")}
# every other confusion (diacritic drops, ı/i/l swaps, ...) is used in a source only when that source shows it
# systematically: at least SYSTEMATIC distinct words repaired by it and confirmed by the other meals
SYSTEMATIC = 15
# confusions that a source's own ingestion record / sample shows (û printed, ü read; â printed, ğ read)
SOURCE_OPS = {"MEAL-OCELIK": {("ü", "û"), ("ğ", "â")}, "TAFSIR-OCELIK": {("ü", "û"), ("ğ", "â")},
              "MEAL-ZDUMAN": {("ü", "û")}, "TAFSIR-ZDUMAN": {("ü", "û")}, "MEAL-ELIACIK": {("ü", "û")},
              "MEAL-MOZTURK": {("ü", "û")}}


# ---------------------------------------------------------------------------------------------------------------
def segments_path(sid: str) -> Path:
    return CORPUS / sid / "segments.jsonl"


def is_clean_source(sid: str) -> bool:
    return sid.startswith("MEAL-") and sid not in OCR_SOURCES and not any(b in sid for b in NOT_CLEAN)


def load_rows(sid: str) -> list[dict]:
    return [json.loads(l) for l in segments_path(sid).open(encoding="utf-8")]


class Vocab:
    """Clean-corpus counts: V total, D number of sources; spaced n-gram counts for the candidate joins."""

    def __init__(self) -> None:
        self.V: collections.Counter = collections.Counter()
        self.D: collections.Counter = collections.Counter()
        self.heads: set[str] = set()
        self.midcap: collections.Counter = collections.Counter()
        for f in sorted(glob.glob(str(CORPUS / "MEAL-*" / "segments.jsonl"))):
            sid = Path(f).parent.name
            if not is_clean_source(sid):
                continue
            seen = set()
            for line in open(f, encoding="utf-8"):
                t = json.loads(line).get("text") or ""
                ks = [key(w) for w in TOK.findall(t)]
                self.V.update(ks)
                for m in MIDCAP.finditer(t):
                    self.midcap[key(m.group(1))] += 1
                seen.update(ks)
            self.D.update(seen)
        for d in TR_DICTS:
            p = segments_path(d)
            if not p.exists():
                continue
            for line in open(p, encoding="utf-8"):
                r = json.loads(line)
                for h in (r.get("head"), r.get("query")):
                    for w in TOK.findall(h or ""):
                        self.heads.add(key(w))

    def known(self, k: str) -> bool:
        return self.D[k] >= 3 or k in self.heads

    def strong(self, k: str) -> bool:
        return (self.D[k] >= 5 and self.V[k] >= 20) or (k in self.heads and self.V[k] >= 5)

    def scan(self, grams: set[tuple], cand_keys: set[str]):
        """One pass over the clean meals: counts of the spaced n-grams, and per verse which candidate keys occur."""
        ng: collections.Counter = collections.Counter()
        verse: dict = collections.defaultdict(lambda: collections.defaultdict(set))
        firsts = {g[0] for g in grams}
        maxn = max((len(g) for g in grams), default=2)
        for f in sorted(glob.glob(str(CORPUS / "MEAL-*" / "segments.jsonl"))):
            src = Path(f).parent.name
            if not is_clean_source(src):
                continue
            for line in open(f, encoding="utf-8"):
                r = json.loads(line)
                ks = [key(w) for w in TOK.findall(r.get("text") or "")]
                for i, k in enumerate(ks):
                    if k in firsts:
                        for n in range(2, maxn + 1):
                            g = tuple(ks[i:i + n])
                            if len(g) == n and g in grams:
                                ng[g] += 1
                s_, a_ = r.get("s"), r.get("a")
                if s_ is not None and a_ is not None:
                    e = r.get("a_end") or a_
                    if e - a_ <= 12:
                        hit = cand_keys.intersection(fold(k) for k in ks)
                        if hit:
                            for x in range(a_, e + 1):
                                for h in hit:
                                    verse[(s_, x)][h].add(src)
        return ng, verse


# ---------------------------------------------------------------------------------------------------------------
class Fixer:
    def __init__(self, sid: str, vocab: Vocab, rules=RULES) -> None:
        self.sid, self.v, self.rules = sid, vocab, set(rules)
        self.ng: collections.Counter = collections.Counter()
        self.verse_keys: dict = {}
        self.sub_cache: dict = {}
        self.ambiguous = 0
        self.ops_allowed = None  # None: every confusion (learning pass)
        self.pair_n: collections.Counter = collections.Counter()
        self.pair_att: collections.Counter = collections.Counter()
        self.unconfirmed: collections.Counter = collections.Counter()
        self.by_rule_b: collections.Counter = collections.Counter()

    # -- regex rules -------------------------------------------------------------------------------------------
    def regex_rule(self, text: str, pats, rule: str, fixes: list) -> str:
        for p in pats:
            def rep(m):
                fixes.append([m.group(0), "", rule])
                return " "
            text = re.sub(p, rep, text)
        return re.sub(r"[ \t]{2,}", " ", re.sub(r" +([,.;:!?])", r" \1", text)) if fixes else text

    def noise(self, text: str, fixes: list) -> str:
        def rep(m):
            s = m.group(0)
            if s.count(",") + s.count(";") < 2:
                return s
            fixes.append([s.strip(), "", "noise"])
            return ""
        return NOISE.sub(rep, text)

    # -- joins (space and hyphen leftovers) ---------------------------------------------------------------------
    # A run is a chain of word tokens separated by one space, or by «- » / «-\n» before a lower-case piece. It is
    # tiled by dynamic programming into groups; a group of 2+ tokens is joined when the joined form is attested
    # and the spaced sequence never occurs in the clean meals. The joins of a run are applied only when no token
    # next to a joined group stays a fragment (a neighbouring stray letter means the tiling is a guess).
    GAPS = (" ", "- ", "-\n", "-\r\n")
    MAXG = 12

    def join_ok_key(self, k: str) -> bool:
        if k in SUFFIX_FRAGMENTS or len(k) < 2 or (len(k) == 2 and not (self.sid in SPACED_SOURCES and self.v.V[k] >= 3000)):
            return False
        if not (self.v.known(k) and self.v.V[k] >= 5):
            return False
        return len(k) > 4 or self.v.V[k] >= 200

    def single_ok(self, w: str) -> bool:
        k = key(w)
        if k in NOT_WORDS:
            return False
        return (self.v.known(k) and (len(k) >= 2 or k == "o")) or (not self.v.known(k) and len(k) >= 4)

    def single_cost(self, w: str) -> int:
        """Cost of leaving a token as it is inside a tiling: 0 a word, 1 an unattested longer token (a name, or a
        word the clean meals lack), 2 a fragment."""
        k = key(w)
        if k in NOT_WORDS:
            return 2
        if self.v.known(k):
            return 0 if (len(k) >= 2 or k == "o") else 2
        return 1 if len(k) >= 4 else 2

    def stray(self, w: str) -> bool:
        """A single left-over token that looks like a fragment: not a word, or a 1-2 letter token that is not a
        common function word."""
        k = key(w)
        return self.single_cost(w) >= 1 or (len(k) <= 2 and self.v.V[k] < 3000)

    def runs(self, text: str):
        toks = [(m.start(), m.end(), m.group()) for m in TOK.finditer(text)]
        run = []
        for t in toks:
            if t[0] > 0 and text[t[0] - 1] in "'’ʼ´-" and not (text[t[0] - 1] == "-" and t[0] > 1 and text[t[0] - 2] == " "):
                if len(run) > 1:
                    yield run
                run = []  # a suffix after an apostrophe or izafet hyphen (neşr-i din) belongs to the word before it
                continue
            if run:
                gap = text[run[-1][1]:t[0]]
                if gap in self.GAPS and (gap == " " or t[2][:1].islower()):
                    run.append(t)
                    continue
                if len(run) > 1:
                    yield run
            run = [t]
        if len(run) > 1:
            yield run

    def run_groups(self, text: str, run):
        """Candidate multi-token groups (i, j) of a run whose joined form is attested."""
        n = len(run)
        for i in range(n):
            joined = run[i][2]
            for j in range(i + 1, min(n, i + self.MAXG)):
                joined += run[j][2]
                if self.join_ok_key(key(joined)):
                    yield i, j + 1, joined

    def collect_ngrams(self, rows) -> set[tuple]:
        grams = set()
        for r in rows:
            for f in FIELDS:
                t = r.get(f + "_ocr", r.get(f))
                if isinstance(t, str):
                    for run in self.runs(t):
                        for i, j, _ in self.run_groups(t, run):
                            grams.add(tuple(key(x[2]) for x in run[i:j]))
        return grams

    def piece_evidence(self, pieces) -> bool:
        """A space join needs a case-consistent group with a piece that cannot be a word by itself: a single letter
        or an unattested piece. In a source whose OCR spaced the letters out systematically (SPACED_SOURCES) a
        piece of at most two letters is enough."""
        ws = [x[2] for x in pieces]
        if not (all(w.isupper() for w in ws) or not any(c.isupper() for w in ws[1:] for c in w)):
            return False  # mixed case inside the group: noise or a real phrase, not a split word
        vowels = "aeıioöuüâîû"
        if any(len(key(w)) == 1 and (key(w) not in vowels or (w.isupper() and w is ws[0])) for w in ws) \
                or any(not self.v.known(key(w)) for w in ws):
            return True
        return self.sid in SPACED_SOURCES and any(len(key(w)) <= 2 for w in ws)

    def group_ok(self, pk: tuple, joined: str) -> bool:
        c = self.ng.get(pk, 0)
        return c * 200 <= self.v.V[key(joined)]

    def joins(self, text: str, fixes: list, want: set) -> str:
        edits = []
        for run in self.runs(text):
            n = len(run)
            groups = {}
            for i, j, joined in self.run_groups(text, run):
                pk = tuple(key(x[2]) for x in run[i:j])
                if self.group_ok(pk, joined):
                    hy = any(text[run[q][1]:run[q + 1][0]].startswith("-") for q in range(i, j - 1))
                    if not hy and not self.piece_evidence(run[i:j]):
                        continue
                    if hy and len(key(joined)) < 5:
                        continue
                    if ("hyphen" if hy else "join") in want:
                        groups.setdefault(i, []).append((j, joined, hy))
            if not groups:
                continue
            INF = (10 ** 6, 10 ** 6, 10 ** 6)
            best = [INF] * (n + 1)
            ways = [0] * (n + 1)
            how: list = [None] * (n + 1)
            best[0], ways[0] = (0, 0, 0), 1
            for i in range(n):
                if best[i] == INF:
                    continue
                c = (best[i][0] + self.single_cost(run[i][2]), best[i][1], best[i][2] + 1)
                if c < best[i + 1]:
                    best[i + 1], how[i + 1], ways[i + 1] = c, (i, None), ways[i]
                elif c == best[i + 1]:
                    ways[i + 1] += ways[i]
                for j, joined, hy in groups.get(i, []):
                    c = (best[i][0], best[i][1] + (j - i), best[i][2] + 1)
                    if c < best[j]:
                        best[j], how[j], ways[j] = c, (i, (joined, hy)), ways[i]
                    elif c == best[j]:
                        ways[j] += ways[i]
            if ways[n] != 1:
                self.ambiguous += 1
                continue  # two equally good tilings (Alla h ile): not certain, leave the run alone
            path, k = [], n
            while k > 0:
                i, g = how[k]
                path.append((i, k, g))
                k = i
            path.reverse()
            for idx, (i, k, g) in enumerate(path):
                if g is None:
                    continue
                bad = False
                for nb in (idx - 1, idx + 1):
                    if 0 <= nb < len(path) and path[nb][2] is None and self.stray(run[path[nb][0]][2]):
                        bad = True
                if bad and self.v.V[key(g[0])] < 2000:
                    continue
                edits.append((run[i][0], run[k - 1][1], g[0], "hyphen" if g[1] else "join"))
        out, pos = [], 0
        for s, e, joined, rule in sorted(edits):
            out.append(text[pos:s])
            out.append(joined)
            fixes.append([text[s:e], joined, rule])
            pos = e
        out.append(text[pos:])
        return "".join(out)

    # -- substitutions -----------------------------------------------------------------------------------------
    def sub_candidates(self, w: str):
        """{candidate: (cost, ops)}: one or two confusions applied to the word."""
        res: dict = {}

        def step(s: str, ops: tuple, start: int) -> None:
            for ocr, true in SUBS:
                i = s.find(ocr, start)
                while i != -1:
                    t = s[:i] + true + s[i + len(ocr):]
                    o2 = ops + ((ocr, true),)
                    cost = sum(WEIGHT.get(o, 1) for o in o2)
                    if t not in res or res[t][0] > cost:
                        res[t] = (cost, o2)
                    if len(ops) == 0:
                        step(t, o2, i + len(true))
                    i = s.find(ocr, i + 1)

        step(w, (), 0)
        return res

    def sub(self, w: str):
        ck = (w, None if self.ops_allowed is None else len(self.ops_allowed))
        if ck not in self.sub_cache:
            self.sub_cache[ck] = self._sub(w)
        return self.sub_cache[ck]

    def _sub(self, w: str):
        """(candidate, key, ops) for an unknown word with one clear repair by known confusions, else None."""
        short_ok = len(w) == 3 and "ü" in w and ("ü", "û") in SOURCE_OPS.get(self.sid, ())
        if (len(w) < 4 and not short_ok) or w.isupper() or w[:1] in ("ı", "ğ"):
            return None
        k = key(w)
        if self.v.known(k) or (w[:1].islower() and APOS.search(w[1:-1] if len(w) > 2 else "")):
            return None  # (an inner apostrophe in a lower-case word is an Arabic ayn/hamza: sa'y, ma'rüf)
        best: dict[int, list] = {}
        for cand, (cost, ops) in self.sub_candidates(w).items():
            ck = key(cand)
            if self.v.strong(ck):
                best.setdefault(cost, []).append((self.v.V[ck], cand, ops))
        for cost in sorted(best):
            lst = sorted(best[cost], reverse=True)
            if len(lst) == 1 and any(o[0] in ("fi", "fı") for o in lst[0][2]):
                # hfila: fi->â also lost the second circumflex (hâlâ): take the one with the extra a->â when it is far
                # more common than the one-step reading
                for cand2, (c2, ops2) in self.sub_candidates(w).items():
                    k2 = key(cand2)
                    if c2 == cost + 1 and ("a", "â") in ops2 and self.v.strong(k2) and \
                            self.v.V[k2] >= 10 * lst[0][0] and all(o in lst[0][2] or o == ("a", "â") for o in ops2):
                        lst = [(self.v.V[k2], cand2, ops2)]
                        break
            if len(lst) == 1 or lst[0][0] >= 10 * lst[1][0]:
                ops_ = lst[0][2]
                circ = any(o[0] in ("fi", "fı") for o in ops_)  # hfila -> hâlâ: the lost second circumflex comes with it
                if self.ops_allowed is not None and not all(
                        o in self.ops_allowed or (circ and o == ("a", "â")) for o in ops_):
                    return None
                return lst[0][1], key(lst[0][1]), lst[0][2]
            return None
        return None

    def sub_cands_of(self, rows) -> set[str]:
        out = set()
        for r in rows:
            for f in FIELDS:
                t = r.get(f + "_ocr", r.get(f))
                if isinstance(t, str):
                    for w in TOK.findall(t):
                        c = self.sub(w)
                        if c:
                            out.add(fold(c[1]))
        return out

    def verse_attested(self, row: dict, ck: str) -> bool:
        s, a = row.get("s"), row.get("a")
        if s is None or a is None:
            return False
        e = row.get("a_end") or a
        if e - a > 12:
            return False
        srcs = set()
        for x in range(a, e + 1):
            srcs |= self.verse_keys.get((s, x), {}).get(fold(ck), set())
        return len(srcs) >= 2

    def learn(self, rows) -> None:
        pre = []
        for r in rows:
            for f in FIELDS:
                t = r.get(f + "_ocr", r.get(f))
                if isinstance(t, str):
                    pre.append((r, self.pre(t, [])))
        # 1. which confusions does this source show systematically?
        self.ops_allowed = None
        types: dict = collections.defaultdict(set)
        for r, t in pre:
            for w in TOK.findall(t):
                c = self.sub(w)
                if c and self.verse_attested(r, c[1]):
                    for o in c[2]:
                        types[o].add((w, c[0]))
        self.ops_allowed = set(CORE) | SOURCE_OPS.get(self.sid, set()) | {
            o for o, ts in types.items() if len(ts) >= SYSTEMATIC}
        self.systematic = {o: len(ts) for o, ts in types.items() if o not in CORE}
        # 2. per (word, repair) pair: how often do the other meals confirm it?
        for r, t in pre:
            for w in TOK.findall(t):
                c = self.sub(w)
                if c:
                    self.pair_n[(w, c[0])] += 1
                    if self.verse_attested(r, c[1]):
                        self.pair_att[(w, c[0])] += 1

    def accept_sub(self, row: dict, w: str, cand: str, ck: str, ops: tuple) -> bool:
        if self.verse_attested(row, ck):
            return True
        if ops and all(o in SOURCE_OPS.get(self.sid, ()) for o in ops):
            self.by_rule_b[(w, cand)] += 1
            return True  # the source's own, systematic confusion, with a unique attested repair
        # one typical scan confusion turns an unattested word into a very common one (Aynca -> Ayrıca)
        if len(ops) == 1 and ops[0] in CORE and len(w) >= 5 and self.v.V[ck] >= 1000 and self.v.D[ck] >= 40:
            self.by_rule_b[(w, cand)] += 1
            return True
        # a long word turned into a very common one by one typical scan confusion
        if len(w) >= 6 and self.v.V[ck] >= 200 and self.v.D[ck] >= 15:
            self.by_rule_b[(w, cand)] += 1
            return True
        # fi/fı read for the circumflex â (hfila -> hâlâ): a sequence that does not occur in Turkish words
        if any(o[0] in ("fi", "fı") for o in ops) and cand.count("â") > w.count("â") \
                and not re.search(r"f[iı]", cand.lower()) and (len(w) >= 5 or self.v.V[ck] >= 2000):
            self.by_rule_b[(w, cand)] += 1
            return True
        att, n = self.pair_att[(w, cand)], self.pair_n[(w, cand)]
        return att >= 3 and att * 2 >= n

    def subs(self, text: str, fixes: list, row: dict) -> str:
        def rep(m):
            w = m.group()
            c = self.sub(w)
            if not c:
                return w
            t, ck, ops = c
            if w.endswith("m") and not APOS.search(w) and re.match(r" [a-zçğıöşü]", text[m.end():m.end() + 2]):
                return w  # a detached «m» before a lower-case piece is a split word, not an ın->m confusion
            if not self.accept_sub(row, w, t, ck, ops):
                self.unconfirmed[(w, t)] += 1
                return w
            fixes.append([w, t, "sub"])
            return t
        return TOK.sub(rep, text)

    # -- stray capitals ----------------------------------------------------------------------------------------
    @staticmethod
    def lower_neighbours(text: str, start: int, end: int) -> bool:
        """True when the word before and the word after (same sentence, no punctuation) start in lower case: a
        capital in between is then a misread letter, not a name or a title-case heading."""
        before = re.search(r"(\S+) $", text[max(0, start - 40):start])
        after = re.match(r" (\S+)", text[end:end + 40])
        if not before or not after:
            return False
        return before.group(1)[0].islower() and before.group(1)[-1].isalpha() and after.group(1)[0].islower()

    def case(self, text: str, fixes: list) -> str:
        def rep(m):
            w = m.group()
            body = w[1:]
            # a stray capital inside a word (kİ, İŞte)
            if len(w) >= 2 and any(c.isupper() for c in body) and not w.isupper():
                low = w[0] + tr_lower(body)
                if key(low) != key(w) and self.v.strong(key(low)):
                    fixes.append([w, low, "case"])
                    return low
            # «Ş» for «ş» after a lower-case word: only for words that are never capitalised mid-sentence
            if w[0] == "Ş" and len(w) >= 3 and self.lower_neighbours(text, m.start(), m.end()):
                k = key(w)
                low = "ş" + w[1:]
                if self.v.strong(k) and self.v.midcap[k] * 50 <= self.v.V[k] and not w.isupper():
                    fixes.append([w, low, "case"])
                    return low
            return w
        return TOK.sub(rep, text)

    # -- driver ------------------------------------------------------------------------------------------------
    def pre(self, text: str, fixes: list) -> str:
        if "header" in self.rules and self.sid in HEADERS:
            text = self.regex_rule(text, HEADERS[self.sid], "header", fixes)
        if "noise" in self.rules:
            text = self.noise(text, fixes)
        want = {r for r in ("hyphen", "join") if r in self.rules}
        if want:
            text = self.joins(text, fixes, want)
        return text

    def fix(self, text: str, row: dict) -> tuple[str, list]:
        fixes: list = []
        text = self.pre(text, fixes)
        if "sub" in self.rules:
            text = self.subs(text, fixes, row)
        if "case" in self.rules:
            text = self.case(text, fixes)
        return text, fixes


def context(text: str, frm: str, to: str, width: int = 40) -> str:
    i = text.find(to) if to else -1
    if i < 0:
        return text[:80].replace("\n", " ")
    return text[max(0, i - width):i + len(to) + width].replace("\n", " ")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--samples", type=int, default=30)
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--only")
    ap.add_argument("--skip")
    args = ap.parse_args()
    sid = args.source
    if sid not in OCR_SOURCES:
        sys.exit(f"{sid}: not an OCR-imported modern-Turkish source ({', '.join(sorted(OCR_SOURCES))})")
    rules = [r for r in RULES if (not args.only or r in args.only.split(",")) and r not in (args.skip or "").split(",")]
    rows = load_rows(sid)
    vocab = Vocab()
    fx = Fixer(sid, vocab, rules)
    grams = fx.collect_ngrams(rows) if {"join", "hyphen"} & set(rules) else set()
    cands = fx.sub_cands_of(rows) if "sub" in rules else set()
    fx.ng, fx.verse_keys = vocab.scan(grams, cands)
    if "sub" in rules:
        fx.learn(rows)
        print(f"{sid}: confusions beyond the core set seen systematically (distinct confirmed words): "
              f"{ {a + '>' + b: n for (a, b), n in fx.systematic.items()} }")

    changed, per_rule, samples = 0, collections.Counter(), []
    pairs: collections.Counter = collections.Counter()
    out_rows = []
    for r in rows:
        new = dict(r)
        any_change = False
        all_fixes = []
        for f in FIELDS:
            orig = r.get(f + "_ocr", r.get(f))
            if not isinstance(orig, str):
                continue
            t, fixes = fx.fix(orig, r)
            if fixes and t != orig:
                new[f + "_ocr"], new[f] = orig, t
                all_fixes += fixes
                any_change = True
            else:
                new.pop(f + "_ocr", None)
                new[f] = orig
        if any_change:
            new["ocr_fixes"] = all_fixes
            changed += 1
            for a, b, rule in all_fixes:
                per_rule[rule] += 1
                pairs[(rule, a, b)] += 1
                samples.append((rule, a, b, r["seg"], context(new.get("text", ""), a, b)))
        else:
            new.pop("ocr_fixes", None)
        out_rows.append(new)

    print(f"{sid}: {changed}/{len(rows)} segments changed; fixes per rule: {dict(per_rule)}; "
          f"space-join runs left alone as ambiguous: {fx.ambiguous}")
    random.seed(7)
    by_rule = collections.defaultdict(list)
    for s in samples:
        by_rule[s[0]].append(s)
    for rule in RULES:
        lst = by_rule.get(rule, [])
        if not lst:
            continue
        print(f"\n--- {rule}: {len(lst)}; top pairs")
        for (ru, x, y), n in [kv for kv in pairs.most_common() if kv[0][0] == rule][:args.top]:
            print(f"  {n:5d}  {x!r} -> {y!r}")
        print(f"--- {rule}: random samples")
        for s in random.sample(lst, min(args.samples, len(lst))):
            print(f"  {s[3]}: {s[1]!r} -> {s[2]!r} | {s[4]}")
    if fx.by_rule_b:
        print(f"\n--- sub accepted without verse/pair confirmation (typical-confusion criterion): {sum(fx.by_rule_b.values())}")
        for (x, y), n in fx.by_rule_b.most_common(args.top):
            print(f"  {n:5d}  {x!r} -> {y!r}")
    if fx.unconfirmed:
        print(f"\n--- sub candidates left alone (no verse/pair confirmation): {sum(fx.unconfirmed.values())} occurrences")
        for (x, y), n in fx.unconfirmed.most_common(args.top):
            print(f"  {n:5d}  {x!r} -> {y!r}")
    if args.dry:
        return
    write(sid, out_rows, rules, changed, per_rule, samples, {
        "confusions_used_beyond_core": sorted(a + ">" + b for a, b in (fx.ops_allowed or set()) if (a, b) not in CORE),
        "sub_candidates_left_alone_unconfirmed": sum(fx.unconfirmed.values()),
        "space_join_runs_left_alone_ambiguous": fx.ambiguous})


def write(sid, out_rows, rules, changed, per_rule, samples, extra=None) -> None:
    d = CORPUS / sid
    tmp = d / "segments.jsonl.tmp"
    with tmp.open("w", encoding="utf-8") as f:
        for r in out_rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    tmp.replace(d / "segments.jsonl")
    meta = json.loads((d / "source.json").read_text(encoding="utf-8"))
    random.seed(11)
    pick = random.sample(samples, min(30, len(samples)))
    meta.setdefault("ingestion", {})["ocr_corrections"] = {
        "date": dt.date.today().isoformat(), "script": "enrichment/v2/fetch/ocr_fix.py",
        "rules": {r: RULE_TEXT[r] for r in rules}, "fixes_per_rule": dict(per_rule),
        "segments_changed": changed, **(extra or {}),
        "samples": [{"seg": s[3], "from": s[1], "to": s[2], "rule": s[0]} for s in pick],
        "original": "each changed segment keeps its imported text in text_ocr (notes_ocr) and the list ocr_fixes"}
    sentence = ("OCR repair (ocr_fix.py): only certain corrections, originals kept in text_ocr/ocr_fixes; "
                "see ingestion.ocr_corrections.")
    notes = meta.get("notes") or ""
    if "OCR repair (ocr_fix.py)" not in notes:
        meta["notes"] = (notes.rstrip() + " " + sentence).strip()
    (d / "source.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{sid}: wrote {len(out_rows)} segments, {changed} changed")


RULE_TEXT = {
    "header": "running page/volume headers left inside the text removed (per-source patterns)",
    "noise": "leftover Arabic-noise punctuation runs (3+ commas/semicolons in a row) removed",
    "hyphen": "hyphenation leftover 'xx- yy' joined when the joined word is attested in the clean meals",
    "join": "letter-spaced / split words joined when the joined form is attested and the spaced sequence never occurs in the clean meals",
    "sub": "non-word turned into an attested word by one known OCR confusion (rı->n, ı->r, fi->â, ...) with a clear winner",
    "case": "stray capital inside a word lower-cased when the lower-cased form is attested",
}

if __name__ == "__main__":
    main()
