#!/usr/bin/env python3
"""MEAL-MOZTURK: Mustafa Öztürk, Kur'an-ı Kerim Meali: Anlam ve Yorum Merkezli Çeviri (Ankara Okulu Yayınları, 2nd
printing, December 2014), from the user's PDF (raw/acquired-2026-10-09/ozturk-kuran-meali.pdf, 695 PDF pages, Adobe
ClearScan OCR text layer; from PDF page 31 on, the printed page number equals the PDF page). Run
fetch/pdf_pages.py MEAL-MOZTURK first.

Layout: each surah opens «88/ĞAŞİYE SURESİ» (digits and letters garbled by OCR), an introduction paragraph («Mekke
döneminde vahyedilmiştir … Toplam 26 ayettir»), the basmala, then verses or verse groups «12 - 1 6. text» (the OCR splits
and garbles digits: «1 70.», «ı.», «24 1 -242.»). Öztürk renders several verses as one paragraph and numbers it as a
group («3-4.»): kept as printed (a..a_end). His own explanations stand in [square brackets] in the text. Footnotes
("dipnot") are numbered from 1 in every surah, printed under the verses of the same page («5. Bu ayetteki …»); their
marker in the text is a number glued after a word or punctuation («artırsın!5», «söylenirler. 6 İyi»). On some pages
a column of Arabic text, whose OCR is garbage, lies beside the Turkish column and its noise is interleaved with Turkish
lines.

Segments: MEAL-MOZTURK:S:A (verse group A..A_end, markers [n] in the text, footnotes in `notes`),
MEAL-MOZTURK:S:intro (heading, introduction, basmala), MEAL-MOZTURK:pNNN (front matter: copyright, contents, the
publisher's preface "Yeni Baskıya Mukaddime" and the author's "Sunuş"). Dropped and counted (see the ingestion record):
running headers, page numbers, margin «Cüz N» lines, ornament brackets «[26]», Arabic-column lines, and noise tokens
inside lines that mix Turkish and Arabic noise (a sample of each is kept).

  python3 -I -B enrichment/v2/fetch/import_meal_ozturk.py [--dry] [--dump FILE]
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402

SID, STEM = "MEAL-MOZTURK", "ozturk-kuran-meali"
DEBUG_NOTES = bool(__import__("os").environ.get("DEBUG_NOTES"))
DEBUG = {int(p) for p in __import__("os").environ.get("DEBUG_PAGES", "").split(",") if p}
FIRST_NUMBERED_PAGE = 31  # from here the printed page number equals the PDF page
DIG = str.maketrans({"s": "?", "S": "?", "B": "?", "ı": "1", "l": "1", "I": "1", "L": "1", "O": "0", "o": "0"})
N3 = r"[0-9ıIlLOoSsB?](?:\s?[0-9ıIlLOoSsB?]){0,2}"
N3B = N3
LET = "A-Za-zÇĞİÖŞÜçğıöşüÂÎÛâîûÔô"
HEAD = re.compile(rf"^(?:\W|[A-Za-z](?=\s)){{0,3}}\s*({N3})\s?/\s?(.{{2,45}})$")
VERSE = re.compile(rf"^\W{{0,2}}({N3})(?:\s?[-–]\s?({N3B}))?(?:\s[a-z])?\s?[.·:,]\s*(.*)$")
INLINE = re.compile(rf"(?:^|(?<=[\s.!?:;,\"”)\]'’\-]))({N3})(?:\s?[-–]\s?({N3B}))?\s?[.·:,]\s+(?=[A-ZÇĞİÖŞÜ\[(\"“‘])")
NOTEWORDS = re.compile(r"(Bu |Bkz|Burada|Ayette|Ayetteki|Yukarıdaki|Bu\b)")
NOTERM = re.compile(rf"^\W{{0,2}}({N3})\s+((?:[A-ZÇĞİÖŞÜ\[(\"“‘]).*)$")
NOTE_START = re.compile(rf"^\W{{0,2}}({N3})\s?[.·:]\s+(.*)$")
HEADER_WORDS = re.compile(r"S[üu]resi|C[üu]z|Kur'an-ı Kerim Meali|Sunuş|Mukaddime")
HEADER_REST = re.compile(r"S[üu]resi|C[üu]z|Kur'an-ı Kerim Meali|Sunuş|Yeni Baskıya Mukaddime|[\d\s/\[\]()|.\-–]")
CUZ = re.compile(r"^\s*C[üu]z\s*[\d\s]{1,5}$")
BRACKET = re.compile(r"^\s*[\[(]\s*[\dılIO\s]{1,6}\s*[\])]\s*$")
TOKEN_CORE = re.compile(rf"^[^{LET}\d]*([{LET}'’\-/]*[{LET}][{LET}'’\-/.]*)?[^{LET}\d]*$")
VOWEL = re.compile(r"[aeıioöuüâîûAEIİOÖUÜÂÎÛôÔ]")
HASNOTE_END = re.compile(r"[.!?)\"”’]\s*$")


def title_like(xs: str) -> bool:
    """«88/ĞAŞİYE SURESİ», however garbled: number, slash, mostly capitals, ending in SURESİ."""
    m = HEAD.match(xs)
    if not m or not re.search(r"(?i)R\W{0,2}E\s?S\s?[iİIl]\s*$", xs):
        return False
    letters = [c for c in xs if c.isalpha()]
    return sum(c.isupper() for c in letters) >= 0.3 * max(1, len(letters))


def num(s: str) -> int | None:
    t = re.sub(r"\s", "", s).translate(DIG)
    return int(t) if t.isdigit() else None


def build_vocab(pages: list[dict]) -> set[str]:
    """Words that occur at least twice in lines with no noise character: the book's own Turkish vocabulary."""
    cnt: Counter = Counter()
    for r in pages:
        if r["page"] < FIRST_NUMBERED_PAGE:
            continue
        for x in r["text"].split("\n"):
            if "�" in x or len(x.split()) < 4:
                continue
            for t in x.split():
                m = re.fullmatch(rf"[^{LET}]*([{LET}'’]+)[^{LET}]*", t)
                if m:
                    cnt[m.group(1).lower()] += 1
    return {w for w, n in cnt.items() if n >= 3 and len(w) >= 2}


class Cleaner:
    def __init__(self, vocab: set[str]):
        self.vocab = vocab

    def kind(self, t: str, lead: bool = False) -> str:
        """good: a Turkish-looking word; neutral: digits and punctuation; noise: anything else."""
        if re.search(r"[^A-Za-zÇĞİÖŞÜçğıöşüÂÎÛâîûÔô0-9.,;:!?()\[\]\"'“”‘’\-–—/·…*\xad]", t):
            return "noise"
        edge = re.sub(rf"^[^{LET}\d]+|[^{LET}\d]+$", "", t)
        if re.fullmatch(r"[0-9ılIOLoSsB?]{1,3}(?:[-–][0-9ılIOLoSsB?]{1,3})?", edge) and re.search(r"\d", edge):
            return "neutral"  # «7-s.» for 7-8
        if not edge or edge.isdigit() or re.fullmatch(r"[0-9ılIOLoSsB?]{1,3}", edge) and (any(c.isdigit() for c in edge) or lead):
            return "neutral"  # digits, punctuation, a digit read as a letter («ı», «8ı»)
        if re.search(r"[;:\[\]()<>{}|]", edge):
            return "noise"
        core = re.sub(rf"[^{LET}]", "", edge)
        if not core:
            return "neutral"  # «3-4.», «12/5»
        if len(core) == 1:
            if edge == core and core in "oaeOAE":
                return "good"
            return "neutral" if edge == core else "noise"  # a split-off letter («Musa'n m»), «b.» in «Ahmed b. X»
        if core.lower() in self.vocab:
            return "good"
        if len(core) == 2 and edge == core:
            return "neutral"  # a split-off syllable («ük» in «Y ük»)
        if len(core) >= 3 and VOWEL.search(core):
            return "good"
        return "noise"

    CLOSERS = (".", "!", "?", ")", "]", '"', "”", ",", ";", ":", "...", "?!", "!?")

    def tail_cut(self, toks: list[str]) -> int:
        """Where the Arabic residue at a line's end begins (len(toks) if none): the trailing run of tokens that are no
        words (punctuation only, or at most two characters with punctuation, or a lone letter), at least three of them;
        closing marks and short digit tokens inside such a run go with it."""
        e = len(toks)  # a run of tokens with no letter or digit at the end: residue if long, or if it holds a non-closing mark
        while e > 0 and not re.search(r"[A-Za-zÇĞİÖŞÜçğıöşüÂÎÛâîûÔô0-9]", toks[e - 1]):
            e -= 1
        if len(toks) - e >= 3 or any(t not in self.CLOSERS for t in toks[e:]):
            return e
        k, junk, seen = len(toks), 0, False
        while k > 0:
            t = toks[k - 1]
            core = re.sub(r"[^A-Za-zÇĞİÖŞÜçğıöşüÂÎÛâîûÔô0-9]", "", t)
            if t in self.CLOSERS:
                pass
            elif not core or (len(core) <= 2 and not core.isdigit() and (t != core or core not in "oOaAeE")
                              and core.lower() not in ("de", "da", "mi", "mı", "mu", "mü", "ki", "ne", "ya", "ve", "bu", "şu", "ey")):
                junk += 1
                seen = True
            elif core.isdigit() and len(core) <= 2 and seen:
                junk += 1
            else:
                break
            k -= 1
        return k if junk >= 3 else len(toks)

    def clean(self, x: str) -> tuple[str, int, list[str], int]:
        """-> (kept text, noise tokens removed, removed tokens, vocabulary words lost when a line was dropped whole).
        A line with no noise token is kept as it is. A line with noise tokens is an Arabic-column line unless it holds
        an anchor: a run of three consecutive tokens that are words of the book's vocabulary (digits and punctuation do
        not break a run). With an anchor, the runs of non-noise tokens holding a vocabulary word (or two other
        Turkish-looking words) are kept and the noise tokens around them removed; without, the line is dropped whole."""
        toks = x.split()
        kinds = [self.kind(t, i < 3) for i, t in enumerate(toks)]
        for i, t in enumerate(toks[:-1]):  # «İ man», «B unun»: a capital split off its word is OCR spacing, not noise
            if kinds[i] == "noise" and len(re.sub(rf"[^{LET}]", "", t)) == 1 and t[:1].isupper() \
                    and re.match(rf"[^{LET}]*[a-zçğıöşü]", toks[i + 1]):
                kinds[i] = "neutral"
        if "noise" not in kinds:
            k = self.tail_cut(toks)  # Arabic residue at the line's end
            if k == 0:
                return "", 0, toks, 0  # a line of residue only
            if k < len(toks):
                return " ".join(toks[:k]), len(toks) - k, toks[k:], 0
            return x.strip(), 0, [], 0
        inv = [k == "good" and re.sub(rf"[^{LET}]", "", t).lower() in self.vocab for t, k in zip(toks, kinds)]  # vocabulary words
        out, removed, kept_vocab = [], [], 0
        i = 0
        stray = lambda t: bool(re.fullmatch(rf"[{LET}]{{1,2}}", t)) and t.lower() not in self.vocab  # noqa: E731
        while i <= len(toks):
            j = i
            while j < len(toks) and kinds[j] != "noise":
                j += 1
            lo, hi = i, j  # the run toks[lo:hi]; stray letters next to the noise they came with are trimmed
            while lo < hi and i > 0 and stray(toks[lo]):
                lo += 1
            while hi > lo and j < len(toks) and stray(toks[hi - 1]):
                hi -= 1
            seg = toks[lo:hi]
            nv = sum(1 for t, v in zip(seg, inv[lo:hi]) if v and len(re.sub(rf"[^{LET}]", "", t)) >= 3)
            ng = sum(1 for k, t in zip(kinds[lo:hi], seg) if k == "good" and len(re.sub(rf"[^{LET}]", "", t)) >= 4)
            if seg and (nv >= 2 or nv + ng >= 2 or (nv >= 1 and len(seg) >= 2)):
                out.extend(seg)
                removed.extend(toks[i:lo] + toks[hi:j])
                kept_vocab += sum(inv[lo:hi])
            else:
                removed.extend(toks[i:j])
            if j < len(toks):
                removed.append(toks[j])
            i = j + 1
        if kept_vocab < 2:
            return "", 0, toks, sum(1 for t, v in zip(toks, inv) if v and len(re.sub(rf"[^{LET}]", "", t)) >= 3)
        k = self.tail_cut(out)  # junk left at the line's end by the Arabic residue
        if 0 < k < len(out):
            removed.extend(out[k:])
            out = out[:k]
        return " ".join(out), len(removed), removed, 0


def kinds_of(t: str, c: Cleaner) -> str:
    return c.kind(t)


def join_lines(parts: list[str], vocab: set[str]) -> str:
    """Lines to text: a soft hyphen at a line end joins the word; a plain hyphen joins it when the joined word is in the
    book's vocabulary (else the hyphen is kept, a compound), anything else is separated by a space."""
    out = ""
    for p in parts:
        p = p.strip()
        if not p:
            continue
        if not out:
            out = p
        elif out.endswith("\xad"):
            out = out[:-1] + p
        elif out[-1:] == "-" and out[-2:-1].isalpha():
            m1 = re.search(rf"([{LET}'’]+)-$", out[-40:])
            m2 = re.match(rf"([{LET}'’]+)", p)
            if m1 and m2 and (m1.group(1) + m2.group(1)).lower() in vocab:
                out = out[:-1] + p
            else:
                out = out + p
        else:
            out = out + " " + p
    return re.sub(r"\s+", " ", out.replace("\xad", "")).strip()


def marker_re(n: int) -> re.Pattern:
    """The footnote marker n in verse text: a number glued after a word («sakınanlardır.2»), or after punctuation with a
    space («söylenirler. 6 İyi»); after punctuation the OCR's ı/l for 1 and O for 0 are read as digits."""
    plain = "".join(f"{c}\\s?" for c in str(n)).rstrip("\\s?")
    var = "".join(f"{'[1ıl]' if c == '1' else '[0Oo]' if c == '0' else c}\\s?" for c in str(n)).rstrip("\\s?")
    return re.compile(rf"(?:(?<=[.,;:!?)\]\"”’'])\s?({plain})|(?<=[.!?)\]\"”])\s?({var})|(?<=[{LET}])({plain}))(?=[\s.,;:!?)\]\"”]|$)")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--dump")
    a = ap.parse_args()
    counts = IC.ayah_counts()
    pages = IC.pages(SID, STEM)
    vocab = build_vocab(pages)
    cl = Cleaner(vocab)
    stats: Counter = Counter()
    issues: list[str] = []
    sample: dict[str, list[str]] = {k: [] for k in ("header", "page number", "cüz", "bracket", "arabic line", "noise tokens",
                                                     "mixed line lost", "removed words")}

    def drop(cat: str, text: str, n: int = 1) -> None:
        stats[f"{cat} dropped"] += n
        if len(sample[cat]) < 12:
            sample[cat].append(text.strip()[:70])

    verses: dict[tuple[int, int], dict] = {}
    intros: dict[int, dict] = {}
    other: dict[int, list[str]] = {}
    notes: dict[int, dict[int, dict]] = {}  # surah -> note number -> {text, page, unit}
    surah, verse = 0, 0
    unit = None
    recent: list[dict] = []  # the units of the current surah, in order
    covered: set[int] = set()  # verse numbers the units of the current surah cover
    mode, cur_note, note_next = "verse", None, 1
    page_last_note_open = False
    carry = None

    def close_surah(s: int, v: int, page: int) -> None:
        if s and v < counts[s]:
            issues.append(f"{s}:{v + 1}-{counts[s]} not found before the next surah or the end (p{page})")

    def marker_seen(n: int) -> bool:
        if not surah or unit is None:
            return False
        rx = marker_re(n)
        return any(rx.search(p) for u in recent[-25:] for p in u["parts"])

    for r in pages:
        page = r["page"]
        raw = [x for x in r["text"].split("\n") if x.strip()]
        kept: list[str] = []
        for i, x in enumerate(raw):
            xs = x.strip()
            is_title = title_like(xs)
            if (i < 3 and len(xs) < 80 and not is_title and HEADER_WORDS.search(xs)
                    and len(HEADER_REST.sub("", xs).strip()) <= 24):
                drop("header", xs)
                continue
            if page >= FIRST_NUMBERED_PAGE and re.fullmatch(r"[\d\sılIO]{1,7}", xs) and num(xs) == page:
                drop("page number", xs)
                continue
            if CUZ.match(xs):
                drop("cüz", xs)
                continue
            if BRACKET.match(xs):
                drop("bracket", xs)
                continue
            if is_title:
                kept.append(xs)  # a surah heading (all capitals, which the noise filter would not trust)
                continue
            if page < FIRST_NUMBERED_PAGE:
                kept.append(xs)  # front matter: only headers are dropped; the text is kept as printed
                continue
            xs, nmarks = re.subn(r"\s*\[\s?[!\dılIO]{1,3}\s?[\dılIO\s]{0,4}\]", "", xs)
            if nmarks:
                stats["margin page marks «[143]» inside lines dropped"] += nmarks
            text, nnoise, removed, lost = cl.clean(xs)
            if not text:
                drop("arabic line", xs)
                stats["arabic-column characters dropped"] += len(xs)
                if lost >= 3:
                    drop("mixed line lost", xs)
                    issues.append(f"p{page}: a line with {lost} Turkish-looking words was dropped as Arabic noise: {xs[:60]!r}")
                continue
            if nnoise:
                stats["noise tokens dropped (Arabic residue inside Turkish lines)"] += nnoise
                for t in removed:
                    if len(re.sub(rf"[^{LET}]", "", t)) >= 4:
                        stats["removed tokens with 4+ letters (possible real words)"] += 1
                        if len(sample["removed words"]) < 40:
                            sample["removed words"].append(f"p{page}: {t[:30]}")
                    elif len(sample["noise tokens"]) < 25:
                        sample["noise tokens"].append(t[:30])
            kept.append(text)

        mode, cur_note = "verse", None
        if carry and carry[0] == surah:
            mode, cur_note = "note", carry[1]  # the note went on over the page break
        carry = None
        for x in kept:
            m_head = HEAD.match(x)
            if m_head and page >= FIRST_NUMBERED_PAGE or (m_head and surah == 0):
                n_head = num(m_head.group(1))
                name = m_head.group(2)
                if n_head == surah + 1 and title_like(x):
                    close_surah(surah, verse, page)
                    surah, verse, unit, mode, cur_note, note_next = n_head, 0, None, "verse", None, 1
                    intros[surah] = unit = {"parts": [x], "page": page}
                    recent = [unit]
                    covered = set()
                    notes[surah] = {}
                    continue
            if surah == 0:
                other.setdefault(page, []).append(x)
                continue
            # a number at the line start: verse, footnote, or text
            mv = VERSE.match(x)
            def plausible(m) -> int | None:
                """The verse number the line opens with, if it is the next verse (or a believable skip, or a one-digit
                OCR misreading of the next number); else None."""
                if not m or not surah:
                    return None
                n1_, n2_ = num(m.group(1)), (num(m.group(2)) if m.group(2) else None)
                if not n1_:  # a letter read for a digit («S6» for 36): matches the expected number if the rest agrees
                    ds0, es0 = re.sub(r"\s", "", m.group(1)).translate(DIG), str(verse + 1)
                    if "?" in ds0 and len(ds0) == len(es0) and all(c in ("?", e) for c, e in zip(ds0, es0)) and verse < counts[surah]:
                        return verse + 1
                    return None
                if n2_ and not n1_ < n2_ <= counts[surah]:
                    return None
                rest_ = m.group(3).strip()
                # digits only, and text that opens like a verse (not a lowercase continuation): a skip is believable
                clean_ = bool(re.fullmatch(r"[\d\s]+", m.group(1))) and not re.match(r"[a-zçğıöşü]", rest_)
                if n1_ <= counts[surah] and (n1_ == verse + 1 or (clean_ and verse < n1_ <= verse + 8 and (verse >= 1 or n1_ <= 3))):
                    return n1_
                if clean_ and max(1, verse - 8) <= n1_ < verse and n1_ not in covered and (not n2_ or n2_ not in covered) and \
                        not (NOTE_START.match(x) and NOTEWORDS.match(NOTE_START.match(x).group(2))):
                    return n1_  # a verse printed out of order by the text layer
                ds, es = re.sub(r"\s", "", m.group(1)).translate(DIG), str(verse + 1)
                nn_ = NOTE_START.match(x)
                if (not n2_ and verse < counts[surah] and len(ds) == len(es) >= 2 and note_next + 3 < int(ds) < verse + 1 and sum(a_ != b_ for a_, b_ in zip(ds, es)) == 1
                        and not (nn_ and (num(nn_.group(1)) == note_next or NOTEWORDS.match(nn_.group(2))))
                        and re.match(r"[^\n]{0,6}?[.·:,]\s*[\[(\"“‘A-ZÇĞİÖŞÜ]", x)):
                    return verse + 1
                return None
            nm0 = NOTE_START.match(x)
            note_like = bool(nm0 and num(nm0.group(1)) is not None and (
                num(nm0.group(1)) == note_next or (note_next <= num(nm0.group(1)) <= note_next + 3
                                                   and NOTEWORDS.match(nm0.group(2)))))
            if plausible(mv) is None and not note_like and surah and verse < counts[surah]:
                mv = None
                for cand in INLINE.finditer(x):  # a verse number inside a line, after Arabic residue
                    g1, st = cand.group(1), cand.start()
                    for cut in range(len(g1)):  # «1 11 .» for 11: leading residue digits are dropped
                        if num(g1[cut:]) == verse + 1 and not cand.group(2):
                            st += cut
                            break
                    else:
                        cut = None
                    if cut is not None and st > 0:
                        before = x[:st].strip()
                        before = re.sub(r"(?<=[.!?\"”)\]])\s*(?:[,'’‘·•_:;\-]{1,3}\s*)+$", "", before)
                        stats["verse numbers found inside a line (after Arabic residue)"] += 1
                        if before:
                            if mode == "note" and cur_note is not None:
                                notes[surah][cur_note]["parts"].append(before)
                            elif unit is not None:
                                unit["parts"].append(before)
                        x = x[st:]
                        mv = VERSE.match(x)
                        break
                if not mv:
                    mt = NOTERM.match(x)
                    if mt and num(mt.group(1)) == verse + 1 and len(re.sub(r"\s", "", mt.group(1))) >= 2:
                        stats["verse numbers read without their full stop"] += 1
                        x = mt.group(1) + ". " + mt.group(2)
                        mv = VERSE.match(x)
                mb = re.fullmatch(rf"({N3})((?:\s+\S{{1,2}}){{0,3}})", x)
                if not mv and mb and num(mb.group(1)) == verse + 1:  # «21 b h 1»: the number, its text on the next line
                    stats["verse numbers alone on a line"] += 1
                    x = mb.group(1) + "."
                    mv = VERSE.match(x)
            decided = None
            if mv:
                n1 = num(mv.group(1))
                n2 = num(mv.group(2)) if mv.group(2) else None
                n_eff = plausible(mv)
                is_verse = n_eff is not None
                nm = NOTE_START.match(x)
                nn = num(nm.group(1)) if nm else None
                nbody = nm.group(2) if nm else ""
                nw = bool(NOTEWORDS.match(nbody))
                is_note = False
                if nn is not None and not n2:
                    if is_verse and verse == 0:
                        is_note = False
                    elif is_verse:  # the number fits both: a footnote only if its marker is in the text and it reads like one
                        is_note = nn == note_next and nw and marker_seen(nn)
                        if nn == note_next:
                            issues.append(f"{surah}:{nn} p{page}: «{x[:40]}» fits verse {nn} and footnote {nn}; taken as "
                                          f"{'footnote' if is_note else 'verse'}")
                    else:
                        is_note = (nn == note_next and (marker_seen(nn) or mode == "note" or nw)) or (
                            note_next < nn <= note_next + 3 and nw)
                        if is_note and nn != note_next:
                            issues.append(f"{surah}: footnotes {note_next}-{nn - 1} not seen before footnote {nn} (p{page})")
                if is_note:
                    is_verse = False
                if is_verse:
                    decided = "verse"
                elif is_note:
                    decided = "note"
            if DEBUG and page in DEBUG:
                print(f"  p{page} s{surah} v{verse} n{note_next} mode={mode} -> {decided} | {x[:70]!r}")
            if decided == "verse":
                n1 = n_eff
                n2 = num(mv.group(2)) if mv.group(2) else None
                if n1 != num(mv.group(1)):
                    stats["verse numbers misread by one digit, taken in sequence"] += 1
                    issues.append(f"{surah}:{n1} p{page}: printed number read by OCR as «{re.sub(chr(92) + "s", "", mv.group(1))}», taken as verse {n1}")
                if n1 < verse + 1:
                    issues.append(f"{surah}:{n1} p{page}: printed after verse {verse} (column order of the text layer); kept as verse {n1}")
                end = n2 if n2 else n1
                if mv.group(2) and not n2:  # «7-s.»: the group's last number is unreadable; the usual pair
                    end = min(n1 + 1, counts[surah])
                    issues.append(f"{surah}:{n1} p{page}: group end printed «{mv.group(2)}» unreadable; taken as {n1}-{end}")
                unit = verses[(surah, n1)] = {"a_end": end, "parts": [], "page": page}
                recent.append(unit)
                covered.update(range(n1, end + 1))
                verse = max(verse, end)
                mode, cur_note = "verse", None
                if mv.group(3).strip():
                    unit["parts"].append(mv.group(3).strip())
                continue
            if decided == "note":
                body = NOTE_START.match(x).group(2)
                nn = num(NOTE_START.match(x).group(1))
                notes[surah][nn] = {"parts": [body], "page": page, "unit": unit, "verse": verse}
                cur_note, mode, note_next = nn, "note", nn + 1
                continue
            if mode == "note" and cur_note is not None:
                notes[surah][cur_note]["parts"].append(x)
            elif unit is not None:
                unit["parts"].append(x)
            else:
                other.setdefault(page, []).append(x)
        # a note whose last line is incomplete may continue on the next page
        last_ = notes[surah][cur_note]["parts"][-1] if mode == "note" and cur_note is not None else ""
        page_last_note_open = bool(last_ and not HASNOTE_END.search(last_))
        carry = (surah, cur_note) if page_last_note_open and re.search(r"[-\xad,;]\s*$", last_) else None
        if carry:
            stats["notes that run on to the next page (line ends in a hyphen or comma)"] += 1
        if page_last_note_open:
            stats["notes ending a page without a full stop"] += 1
            if DEBUG_NOTES:
                print(f"  NOTE-OPEN p{page}: {notes[surah][cur_note]['parts'][-1][-70:]!r}")
    close_surah(surah, verse, 0)

    # footnote markers: placed in the unit text, in order, per surah
    segs = []
    unplaced = 0
    for s in sorted(notes):
        order = sorted(((k, u) for k, u in verses.items() if k[0] == s), key=lambda kv: kv[0][1])
        units = [intros[s]] + [u for _, u in order]
        pos = 0  # marker search resumes at the unit of the last placed marker
        for n in sorted(notes[s]):
            rx = marker_re(n)
            placed = False
            for ui in range(pos, len(units)):
                u = units[ui]
                for pi, p in enumerate(u["parts"]):
                    mm = rx.search(p)
                    if mm and (ui, pi) >= (pos, 0):
                        u["parts"][pi] = p[:mm.start()] + f" [{n}]" + p[mm.end():]
                        u.setdefault("notes", []).append(n)
                        pos, placed = ui, True
                        break
                if placed:
                    break
            nt = notes[s][n]
            if not placed:
                unplaced += 1
                u = nt["unit"] or intros[s]
                u.setdefault("notes", []).append(n)
                issues.append(f"{s}: footnote {n} (p{nt['page']}): marker not found in the text; tied to the verse unit above it")
        stats["footnotes"] += len(notes[s])
        # footnote numbering must be continuous
        nums = sorted(notes[s])
        if nums and nums != list(range(1, nums[-1] + 1)):
            miss = sorted(set(range(1, nums[-1] + 1)) - set(nums))
            issues.append(f"{s}: footnote numbers missing {miss[:12]}")
    stats["footnotes without a marker in the text"] = unplaced

    # verses whose numbers the text layer lacks (printed only in Arabic letters, or lost): tied to the unit above
    # (its text then holds theirs) or, at a surah's start, kept as an empty unit; every one is listed in the issues
    for s in sorted(counts):
        have = sorted((a0, u) for (s_, a0), u in verses.items() if s_ == s)
        cov = set()
        for a0, u in have:
            cov.update(range(a0, u["a_end"] + 1))
        miss = [n for n in range(1, counts[s] + 1) if n not in cov]
        i = 0
        while i < len(miss):
            j = i
            while j + 1 < len(miss) and miss[j + 1] == miss[j] + 1:
                j += 1
            m0, m1 = miss[i], miss[j]
            prev = [(a0, u) for a0, u in have if u["a_end"] == m0 - 1]
            if prev:
                prev[0][1]["a_end"] = m1
                issues.append(f"{s}:{m0}{'-' + str(m1) if m1 > m0 else ''}: no printed number in the text layer; "
                              f"tied to the unit {s}:{prev[0][0]} above it (its text holds theirs)")
            else:
                verses[(s, m0)] = {"a_end": m1, "parts": [], "page": intros[s]["page"], "empty": True}
                issues.append(f"{s}:{m0}{'-' + str(m1) if m1 > m0 else ''}: no text in the text layer (read as Arabic "
                              f"letters or lost); kept as an empty unit")
            i = j + 1
    got: Counter = Counter()
    for (s, a0), u in verses.items():
        got[s] += u["a_end"] - a0 + 1
    short = {s: (got[s], counts[s]) for s in counts if got[s] != counts[s]}
    for s, (g, c) in short.items():
        issues.append(f"surah {s}: verses covered {g} of {c}")

    def notes_text(u: dict, s: int) -> str:
        return "\n".join(f"[{n}] " + join_lines(notes[s][n]["parts"], vocab) for n in sorted(set(u.get("notes", []))))

    for s, u in sorted(intros.items()):
        g = {"seg": f"{SID}:{s}:intro", "s": s, "a": 1, "a_end": counts[s], "page": f"pdf{u['page']}",
             "head": "surah heading, introduction and basmala", "text": join_lines(u["parts"], vocab)}
        if u.get("notes"):
            g["notes"] = notes_text(u, s)
        segs.append(g)
    for (s, a0), u in sorted(verses.items()):
        g = {"seg": f"{SID}:{s}:{a0}", "s": s, "a": a0, "a_end": u["a_end"], "page": f"pdf{u['page']}",
             "text": join_lines(u["parts"], vocab)}
        if u.get("notes"):
            g["notes"] = notes_text(u, s)
        segs.append(g)
    for pg, ls in sorted(other.items()):
        text = "\n".join(ls).strip()
        if text:
            segs.append({"seg": f"{SID}:p{pg:03d}", "page": f"pdf{pg}", "head": "front matter", "text": text,
                         "refs": IC.find_refs(text)})
    segs.sort(key=lambda g: (g.get("s") or 0, -1 if g["seg"].endswith("intro") else (g.get("a") or 0), g["seg"]))
    for g in segs:
        if g.get("s") and not g["text"]:
            issues.append(f"{g['seg']}: empty text")
    longest = max((len(g["text"]), g["seg"]) for g in segs if g.get("s"))
    print(f"surahs {len(intros)}; verse units {len(verses)}; verses covered {sum(got.values())}/6236; surahs not "
          f"matching {len(short)} {dict(list(short.items())[:12])}; longest unit {longest}")
    print(f"{dict(stats)}; issues {len(issues)}")
    for i in issues[:int(__import__("os").environ.get("NISS", "60"))]:
        print("  ISSUE", i)
    if a.dump:
        Path(a.dump).write_text("".join(IC.json.dumps(g, ensure_ascii=False) + "\n" for g in segs))
    if a.dry:
        return
    if short or not segs:
        sys.exit("verse coverage is not complete: refusing to write (fix the parser; no gaps accepted)")
    old = IC.json.loads((IC.src_dir(SID) / "source.json").read_text())
    IC.write(SID, segs, {
        "script": "enrichment/v2/fetch/import_meal_ozturk.py", "from": IC.inputs(SID, [STEM]),
        "method": "PDF text layer (pypdf via fetch/pdf_pages.py); verse groups in order; footnotes by marker; "
                  "Arabic-column noise removed token by token",
        "verse_count_mismatch": {str(k): v for k, v in short.items()}, "issues": issues, "counts": dict(stats),
        "dropped_sample": {k: v for k, v in sample.items() if v},
    }, {"coverage": f"1-114 ({sum(got.values())}/6236 ayat)", "locator": "ayah", "kind": "meal",
        "edition": "Ankara Okulu Yayınları, 2nd printing, December 2014 (first printing October 2014); ISBN "
                   "978-9944-162-82-1; 695-page PDF (copyright page: PDF page 2; the translation starts on PDF page 31)",
        "licence": "copyrighted; ingested from the user's own PDF for local research use",
        "acquisition": {"date": "2026-10-09", "state": "raw_downloaded", "ingestion_status": "ingested", "files": 1,
                        "pdfs": 1, "origin": "the user's own PDF (Downloads), copied into raw/acquired-2026-10-09"},
        "files": {f"raw/acquired-2026-10-09/{STEM}.pdf": IC.inputs(SID, [STEM]).get(
            f"raw/acquired-2026-10-09/{STEM}.pdf")},
        "notes": "Ingested 2026-10-09 from the user's own PDF (fetch/import_meal_ozturk.py). The text is OCR (Adobe "
                 "ClearScan layer): some letters are wrong («hfila» for hâlâ, «Aynca» for Ayrıca, «çevıilmek» for çevrilmek) and some words "
                 "are letter-spaced («O'nda n», «İ man»); care is needed when quoted. Verse groups are Öztürk's own (a..a_end); his bracketed explanations [..] are part of "
                 "the meal; footnotes (dipnot) are attached to their verse unit as [n]. Pointer note before "
                 "ingestion: " + (old.get("notes") or "").split("Pointer note before ingestion: ")[-1]})


if __name__ == "__main__":
    main()
