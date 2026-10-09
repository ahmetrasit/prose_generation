#!/usr/bin/env python3
"""MEAL-DOGRUL: Ömer Rıza Doğrul, «Tanrı Buyruğu (Kur'an-ı Kerim'in Tercüme ve Tefsir-i Şerifi)», third printing
(Üçüncü Basılış), Istanbul, Ahmet Halit Yaşaroğlu Kitapçılık ve Kâğıtçılık T.L.Ş., Bilgi Basım ve Yayınevi, no. 729,
1955. Doğrul died 1952: public domain. Source: the archive.org item
tanri-buyrugu-kuran-i-kerimin-tercume-ve-tefsir-i-serifi-omer-riza-dogrul, its *_djvu.txt (OCR; raw/acquired-2026-10-09).

Layout of the OCR text: a long front matter (introduction); then per surah «SÜRE: n» / «NAME SÜRESİ» / «(Mekkede nâzil
olmuştur. N âyettir.)», the surah's introduction («Konusu: …»), «Meal-i Kerimi:», the besmele, and the verses inline
(«87 Biz, Musaya Kitap verdik, … 88 Onlar derler ki; …», groups «6,7» / «9-10» as printed, «1 — …» in the Fâtiha);
footnote markers «(83)» in the verses; the footnotes (the tafsir) are printed at the page foot as paragraphs «(83) …»,
those of a page continuing at the next page after its verses. Page headers «Süre: 2| Bakara Süresi 39» and the OCR
noise of the Arabic text boxes are dropped and counted. «BÖLÜM :1 — …» headings inside the verse text go to the next
verse's `head`.

Segments: MEAL-DOGRUL:S:A (verse or verse group A..A_end; `printed` the numbers as printed; footnotes in `notes`),
MEAL-DOGRUL:S:intro (the surah's introduction and its own footnotes), MEAL-DOGRUL:frontNNN / backNNN (front and back
matter in ~4,000-character pieces, nothing dropped).

Numbering: Doğrul does not count the besmele as Fâtiha's first verse: his 1–5 are 1:2–1:6 of the project's numbering,
his 6–7 together are 1:7. They are stored as 1:1 (besmele), 1:2..1:6 and 1:7 (a group), the printed numbers in `printed`.

  python3 -I -B enrichment/v2/fetch/import_meal_dogrul.py [--dry] [--dump out.jsonl]
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402

SID = "MEAL-DOGRUL"
RAW = "raw/acquired-2026-10-09/dogrul-tanri-buyrugu.djvu.txt"
SHIFT = {1: 1}  # surah -> offset of the printed verse numbers (the besmele is not numbered by Doğrul)

NUM_EV = re.compile(r"S[ÜU]RE\s?[:;]\s?(\d{1,3})")
NAME_EV = re.compile(r"S[ÜU]RES[İI!'’]*\W*$")
HEADER = re.compile(r"S[üuûö]r[eo]s[iı]\W*\d+\W*$|^\W*\d+\W*[A-Za-zÂâ'’ ]{3,25}S[üuûö]r[eo]s[iı]\W*$|^\W*(?:S[üuö]re|Sure)\s*[:\-—]?\s*[\dI7l!]{0,3}\s*[|)\]!1Il/ ]|TANRI\s*BUYRU|TERCÜME\s*ve\s*TEFS")
PAGENO = re.compile(r"^\W*\d{3,4}\W*$")
FN = re.compile(r"^(?:[(\[{]\s?([0-9OoIil]{0,3})\s?[)\]1l|]?|([0-9OoIil]{1,3})\s?[)\]])\s+(?=\S)")
BOLUM = re.compile(r"^BÖLÜM\s?[:;.]?\s?[\dIl]+\s?[—–-]")
MEAL = re.compile(r"\bMe\w{1,3}[-.]?[ijlı1]\s*[Kk]er\w{2,3}\b")
BESMELE = re.compile(r"^\W*Bismi'?\s?ll", re.I)
MARK = re.compile(r"\((\s?[0-9OoIil]{1,3}\s?)[\)1l]")
END_PUNCT = re.compile(r"[.?!:»”\")]\s*\d{0,3}\s*[)\]]?\s*$")
TR = re.compile(r"[A-Za-zÇĞİÖŞÜçğıöşüÂÎÛâîû]")


def digits(s: str) -> int | None:
    t = re.sub(r"\s", "", s).translate(str.maketrans("OoIil", "00111"))
    return int(t) if t.isdigit() else None


WORD = re.compile(r"[«“\"(\[]*[A-ZÇĞİÖŞÜÂ]?[a-zçğıöşüâîû'’]{2,}(?:-[a-zçğıöşüâîû]+)?[\W]*$")


def garbage(p: str) -> bool:
    """OCR noise of the Arabic text boxes: few letters, or fewer than half of the tokens plausible Turkish words."""
    s = re.sub(r"[\s\d/:;,.\-–()]", "", p)
    if not s:
        return True
    if len(TR.findall(s)) / len(s) < 0.55:
        return True
    toks = [t for t in re.findall(r"\S+", p) if not re.fullmatch(r"[\d\W]+", t)]
    if toks:
        ok = sum(1 for t in toks if WORD.match(t) and len(re.sub(r"\W", "", t)) >= 3 and re.search(r"[aeıioöuüâîû]", t))
        has5 = any(WORD.match(t) and len(re.sub(r"\W", "", t)) >= 5 and re.search(r"[aeıioöuüâîû]", t) for t in toks)
        return ok / len(toks) < 0.4 and not has5
    return False


def join(lines: list[str]) -> str:
    out = ""
    for ln in lines:
        ln = re.sub(r"(?:\s+\|)+$|^\|\s+", "", ln.strip())  # the column bar of the scan
        if not ln:
            continue
        if out.endswith(("-", "­")) and re.match(r"[a-zçğıöşüâîû]", ln):
            out = out[:-1] + ln
        else:
            out = (out + " " + ln) if out else ln
    return re.sub(r"\s+", " ", out).strip()


FUZZ = {"5": "[539S]", "3": "[35]", "6": "[68]", "8": "[86B]", "0": "[0Oo6]", "1": "[1lIiıİ|!7]", "7": "[71]", "9": "[945]",
        "4": "[49]", "2": "[2Z]"}


GEN = re.compile(r"(?:(?<=\s)|^|(?<=[”\"’'.)]))[.,*'\"|“«(\-–]{0,2}(\d[0-9OoIilı|!]{0,3}|[lIiıİ|!][0-9]{1,2}|[lIiıİ|!]{1,2})((?:\s?[,\-–.]\s?[0-9OoIilı|!]{1,3})*)\s?[—–.,:;-]?"
                 r"(?:(?:\s+|(?=[A-ZÇĞİÖŞÜÂ«“\"(]))(?=[^\s\d:/.,;)])|\s*$)")
TWINS = {("5", "3"), ("3", "5"), ("5", "9"), ("9", "5"), ("9", "4"), ("4", "9"), ("6", "8"), ("8", "6"), ("0", "6"), ("6", "0"),
         ("1", "7"), ("7", "1"), ("2", "7"), ("7", "2"), ("8", "3"), ("3", "8"), ("0", "8"), ("8", "0"), ("1", "4"), ("4", "1"), ("2", "9"), ("9", "2"), ("3", "9"), ("9", "3"), ("6", "5"), ("5", "6")}


LETTER_DIGITS = str.maketrans("OoIilıİ|!", "001111111")


def val_of(m: re.Match) -> int | None:
    g = m.group(1).translate(LETTER_DIGITS)
    if g.isdigit():
        if not m.group(1).isdigit() and len(m.group(1)) == 1 and m.start() > 1:
            return None  # a single letter read as 1 only at the start of a paragraph
        return int(g)
    return None


def m_end(m: re.Match) -> int:
    v = val_of(m) or 0
    e = v
    for x in re.findall(r"[0-9OoIilı|!]{1,3}", m.group(2) or ""):
        t = x.translate(LETTER_DIGITS)
        if not t.isdigit():
            continue
        if int(t) == e + 1:
            e = int(t)
        elif e < int(t) <= v + 12 and re.search(r"[,\-–]", m.group(2) or ""):
            e = int(t)  # «6,7», «9-10»: a plain range
    return e


def ctx_ok(text: str, m: re.Match) -> bool:
    pre = text[:m.start()].rstrip()
    return not pre or bool(re.search(r"[.?!:;)»”\"’,\]]$", pre))


def weak_ok(text: str, m: re.Match) -> bool:
    return bool(re.match(r"[«“\"(]?[A-ZÇĞİÖŞÜÂÎÛ]", text[m.end():]))


def twin(raw: str, miss: int) -> bool:
    t = str(miss)
    if raw.isdigit() and len(raw) == len(t) + 1 and any(raw[:i] + raw[i + 1:] == t for i in range(len(raw))):
        return True  # an extra stroke read as a digit: «1728» for 128
    if not raw.isdigit() or len(raw) != len(t) or raw == t:
        return False
    d = [(x, y) for x, y in zip(raw, t) if x != y]
    return len(d) <= 2 and all(pr in TWINS for pr in d)


def token_re(n: int, fuzzy: bool = False) -> re.Pattern:
    d = "".join((FUZZ if fuzzy else {"1": "[1lIiıİ|!]", "0": "[0Oo]"}).get(c, c) for c in str(n))
    return re.compile(rf"(?:(?<=\s)|^)[.,*'\"|]?({d}{'[ıi]?' if n == 1 else ''})((?:\s?[,\-–]\s?\d{{1,3}})*)\s?[—–.-]?(?:\s+|(?=[«“\"(]))(?=[^\s\d:/.,;)])")


def chunks(lines: list[str], size: int = 4000) -> list[str]:
    out, cur = [], ""
    para: list[str] = []

    def flush_para():
        nonlocal cur
        if para:
            t = "\n".join(para)
            if cur and len(cur) + len(t) > size:
                out.append(cur)
                cur = ""
            cur += ("\n\n" if cur else "") + t
            para.clear()
    for ln in lines:
        if ln.strip():
            para.append(ln.rstrip())
        else:
            flush_para()
    flush_para()
    if cur:
        out.append(cur)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--dump")
    ap.add_argument("--runs", action="store_true", help="print the missing verses as runs per surah")
    ap.add_argument("--show", type=int, help="print the units of this surah")
    a = ap.parse_args()
    counts = IC.ayah_counts()
    raw = (IC.src_dir(SID) / RAW).read_text(encoding="utf-8").replace("\f", "\n")
    L = raw.split("\n")
    stats: Counter = Counter()
    issues: list[str] = []
    dropped: dict[str, list[str]] = {}

    def drop(cat: str, text: str) -> None:
        stats[f"dropped: {cat}"] += 1
        stats[f"dropped chars: {cat}"] += len(text)
        dropped.setdefault(cat, [])
        if len(dropped[cat]) < 12:
            dropped[cat].append(text.strip()[:70])

    # ---- surah heading events ------------------------------------------------------------------
    start = next(i for i, x in enumerate(L) if re.match(r"^SÜRE\s?:\s?1\b", x))
    end = next(i for i, x in enumerate(L) if i > start + 60000 and "FÂTİHA SÜRESİ" in x and re.search(r"\d", x))
    events: list[tuple[int, int | None]] = []  # (line, number or None)
    for i in range(start, end):
        x = L[i].strip()
        if BOLUM.match(x):
            continue
        mn = NUM_EV.search(x)
        letters = [c for c in x if c.isalpha()]
        upper = bool(letters) and sum(c.isupper() for c in letters) / len(letters) > 0.6
        if mn and len(x) < 40:
            events.append((i, int(mn.group(1))))
        elif NAME_EV.search(x) and len(x) < 60 and (upper or "Fussilet" in x):
            events.append((i, None))
    ev_lines = {i for i, _ in events}
    merged: list[tuple[int, int | None]] = []
    for i, n in events:
        if merged and i - merged[-1][0] <= 8:
            if merged[-1][1] is None and n is not None:
                merged[-1] = (merged[-1][0], n)
            continue
        merged.append((i, n))
    ev_at: dict[int, int] = {}
    last = 0
    for i, n in merged:
        if n is None or n == last + 1:
            s = last + 1
        elif last < n <= last + 3:
            issues.append(f"surah heading numbers jump {last} -> {n} (line {i + 1}): {n - last - 1} heading(s) not found")
            s = n
        else:
            issues.append(f"surah heading «{L[i].strip()}» (line {i + 1}) read as {last + 1}")
            s = last + 1
        ev_at[i] = s
        last = s
    if last != 114:
        issues.append(f"surah headings found up to {last}")

    # ---- paragraphs ----------------------------------------------------------------------------
    items: list[tuple[str, object]] = []  # ("sura", s) | ("p", [lines])
    cur: list[str] = []
    for i in range(start, end):
        if i in ev_lines:
            if cur:
                items.append(("p", cur))
                cur = []
            if i in ev_at:
                items.append(("sura", ev_at[i]))
            continue
        x = L[i].strip()
        special = bool(x) and ((MEAL.search(x) and len(x) < 40) or (BESMELE.match(x) and len(x) < 40) or
                               (BOLUM.match(x) and len(x) < 90) or (i - 1 >= 0 and BOLUM.match(L[i - 1].strip()) and
                                                                    x.upper() == x and len(x) < 30))
        if special:  # own paragraph: the OCR text has no blank line around these
            if cur:
                items.append(("p", cur))
            items.append(("p", [L[i]]))
            cur = []
        elif x:
            cur.append(L[i])
        elif cur:
            items.append(("p", cur))
            cur = []
    if cur:
        items.append(("p", cur))

    intros: dict[int, dict] = {}
    vlog: dict[int, list[tuple[str, str]]] = {}  # surah -> [("p" | "head", text)] of the verse region, in order
    feet: list[dict] = []
    s = 0
    mode = "pre"
    foot: dict | None = None
    foot_mode = False
    last_val = 0

    def new_foot(para: str) -> None:
        nonlocal foot
        m = FN.match(para)
        k = digits(m.group(1) or m.group(2) or "") if m else None
        foot = {"k": k, "text": para[m.end():] if m else para, "s": s, "mode": mode}
        feet.append(foot)

    def head_val(p: str) -> int | None:
        """The verse number a paragraph starts with, if any."""
        m = GEN.match(p)
        return val_of(m) if m else None

    has_meal: dict[int, bool] = {}
    cur_s = 0
    for kind, val in items:
        if kind == "sura":
            cur_s = val  # type: ignore[assignment]
        elif cur_s and any(MEAL.search(x) and len(x.strip()) < 40 for x in val):  # type: ignore[union-attr]
            has_meal[cur_s] = True

    for kind, val in items:
        if kind == "sura":
            s = val  # type: ignore[assignment]
            mode, foot_mode, last_val = "intro", False, 0  # `foot` is kept: a footnote may run on past the heading
            intros[s] = {"parts": [], "notes": [], "s": s}
            vlog[s] = []
            continue
        lines = val  # type: ignore[assignment]
        if len(lines) >= 2:  # noise lines inside a paragraph (the scan has no blank line around the Arabic boxes)
            keep = []
            for x in lines:
                if len(x.strip()) >= 10 and len(x.split()) >= 3 and garbage(x):
                    drop("noise of the Arabic text boxes (single lines inside paragraphs)", x)
                else:
                    keep.append(x)
            lines = keep or lines
        p = re.sub(r"^[|*\s]+", "", join(lines))
        if not p:
            continue
        body0 = [len(x.strip()) for x in lines[:-1]]
        wide = bool(body0) and sum(1 for x in body0 if x >= 69) / len(body0) >= 0.5  # footnote type: longer lines
        if s == 0:
            drop("text before the first surah heading", p)
            continue
        if (HEADER.search(p) and len(p) < 80) or PAGENO.match(p):
            drop("running headers and page numbers", p)
            foot_mode = False
            continue
        if MEAL.search(p) and len(p) < 40:
            if mode == "intro":
                mode = "verses"
            continue
        if garbage(p):
            drop("noise of the Arabic text boxes", p)
            continue
        if FN.match(p) and len(p) > 8 and re.search(r"[A-Za-zÇĞİÖŞÜçğıöşüÂâîû']{4,}", p[FN.match(p).end():FN.match(p).end() + 40]):
            new_foot(p)
            foot_mode = True
            continue
        if mode == "intro" and not has_meal.get(s) and BESMELE.match(p) and len(p) < 40:
            mode = "verses"  # no «Meal-i Kerimi» line in the OCR: the besmele opens the verses
            stats["surahs whose verses start at the besmele (no «Meal-i Kerimi» line in the OCR)"] += 1
            drop("besmele lines (the Arabic besmele transliterated)", p)
            continue
        if mode == "intro":
            hv = head_val(p)
            if hv == 1 and re.match(r"\s*[A-ZÇĞİÖŞÜÂÎÛ«“\"(]", p[GEN.match(p).end():]) and \
                    max(len(x.strip()) for x in lines) <= 68:  # verse type is larger: shorter lines
                mode = "verses"  # surah without a «Meal-i Kerimi» line
                issues.append(f"surah {s}: no «Meal-i Kerimi» line; verses taken from the first «1 …» paragraph")
            else:
                if foot_mode and foot is not None:
                    foot["text"] += " " + p
                else:
                    intros[s]["parts"].append(p)
                continue
        # ---- verse region
        if foot is not None and not wide:
            k = 0
            while k < len(lines) - 2 and len(lines[k].strip()) >= 73 and all(len(x.strip()) <= 68 for x in lines[k + 1:k + 3]):
                k += 1
            if k == 0 and foot["text"].rstrip().endswith("-") and lines[0].strip()[:1].islower() and len(lines) > 1 \
                    and not GEN.match(lines[0].strip()):
                k = 1  # the end of a footnote that broke across the page: the first line, lower case after a hyphen
            if k:
                foot["text"] += " " + join(lines[:k])
                stats["footnote lines found at the top of a verse paragraph (moved to their footnote)"] += k
                lines = lines[k:]
                p = re.sub(r"^[|*\s]+", "", join(lines))
        hv = head_val(p)
        if foot_mode and ((hv is not None and last_val < hv <= last_val + 3) or (len(lines) >= 3 and not wide)):
            foot_mode = False  # a verse paragraph: the footnote region has ended (page header lost)
            stats["footnote regions closed by the next verse paragraph"] += 1
        if wide and not (hv is not None and last_val < hv <= last_val + 3):
            foot_mode = True
            stats["footnote continuation paragraphs recognised by their line width"] += 1
        if foot_mode:
            if foot is not None:
                foot["text"] += " " + p
            else:
                feet.append(foot := {"k": None, "text": p, "s": s, "mode": mode})
            continue
        if BOLUM.match(p) and len(p) < 120:
            vlog[s].append(("head", p))
            continue
        if BESMELE.match(p) and len(p) < 40:
            drop("besmele lines (the Arabic besmele transliterated)", p)
            continue
        p = re.sub(r"(?<=[.?!'’”])(\d{2,3})(?=[A-ZÇĞİÖŞÜ])", r" \1 ", p)  # «olur'83Herşeyin»
        vlog[s].append(("p", p))
        for m in GEN.finditer(p):
            v = val_of(m)
            if v and last_val < v <= last_val + 3 and ctx_ok(p, m):
                last_val = max(m_end(m), last_val)

    # ---- verses: the chain of verse numbers of each surah ---------------------------------------
    verses: dict[tuple[int, int], dict] = {}
    markers: list[dict] = []
    grouped: list[str] = []
    lost_numbers: list[str] = []
    book_over: list[str] = []

    def build_units(sn: int) -> list[dict]:
        """Units {a, a_end, text, head, printed} of one surah from its verse-region paragraphs."""
        log = vlog.get(sn, [])
        n_all = counts[sn]
        cands = []  # (pi, start, end_pos, value, end_value, strong, raw)
        for pi, (kd, text) in enumerate(log):
            if kd != "p":
                continue
            for m in GEN.finditer(text):
                v = val_of(m)
                if not v or v < 1 or v > n_all + 12:
                    continue
                ctx, cap = ctx_ok(text, m), weak_ok(text, m)
                q = 1.0 if ctx and cap else 0.8 if ctx else 0.6 if cap else 0.35
                cands.append({"pi": pi, "st": m.start(), "en": m.end(), "v": v, "e": m_end(m), "q": q,
                              "raw": m.group(1)})
        all_c = cands
        cands = [c for c in cands if c["v"] <= n_all + 5 and c["q"] >= 0.6]  # the book may number more verses
        # longest increasing chain (by quality)
        best, prev = [], []
        for j, c in enumerate(cands):
            b, pj = c["q"], -1
            for i in range(j):
                ci = cands[i]
                if ci["e"] < c["v"] <= ci["e"] + 60 and best[i] + c["q"] > b:
                    b, pj = best[i] + c["q"], i
            best.append(b)
            prev.append(pj)
        chain: list[dict] = []
        if cands:
            j = max(range(len(cands)), key=lambda x: (best[x], -x))
            while j >= 0:
                chain.append(cands[j])
                j = prev[j]
            chain.reverse()
        # OCR twins: a missing number whose digits are read wrongly between two chain tokens
        out_chain: list[dict] = []
        for idx, c in enumerate(chain + [None]):
            lo = out_chain[-1] if out_chain else None
            nxt_v = c["v"] if c else n_all + 1
            prev_e = lo["e"] if lo else 0
            if nxt_v > prev_e + 1:
                lo_pos = (lo["pi"], lo["en"]) if lo else (-1, -1)
                hi_pos = (c["pi"], c["st"]) if c else (10 ** 9, 0)
                for miss in range(prev_e + 1, nxt_v):
                    for t in all_c:
                        pos = (t["pi"], t["st"])
                        if lo_pos < pos < hi_pos and t not in chain and t not in out_chain and (t["v"] == miss or twin(t["raw"], miss)) \
                                and (not out_chain or pos > (out_chain[-1]["pi"], out_chain[-1]["en"])):
                            t = dict(t, v=miss, e=miss, twin=t["raw"] if t["v"] != miss else None)
                            out_chain.append(t)
                            lo_pos = (t["pi"], t["en"])
                            break
            if c:
                out_chain.append(c)
        chain = out_chain
        units: list[dict] = []
        if not chain:
            return units
        # text between tokens
        def piece(p0: tuple[int, int], p1: tuple[int, int]) -> tuple[str, str | None]:
            parts, head = [], None
            for pi in range(p0[0], min(p1[0], len(log) - 1) + 1):
                kd, text = log[pi]
                if kd == "head":
                    head = head or text
                    continue
                a0 = p0[1] if pi == p0[0] else 0
                a1 = p1[1] if pi == p1[0] else len(text)
                seg = text[a0:a1].strip()
                if seg:
                    parts.append(seg)
            return " ".join(parts), head
        first = chain[0]
        pre_text, _ = piece((0, 0), (first["pi"], first["st"]))
        if first["v"] > 1:
            units.append({"a": 1, "a_end": first["v"] - 1, "text": pre_text, "head": None,
                          "printed": f"({1}-{first['v'] - 1}: numbers lost)", "lostgap": True})
        elif pre_text:
            intros[sn]["parts"].append(pre_text)
            stats["verse-region text before verse 1 added to the surah's introduction"] += 1
        for idx, c in enumerate(chain):
            nxt = chain[idx + 1] if idx + 1 < len(chain) else None
            if nxt is None and c["e"] < n_all and n_all - c["e"] <= 3:
                nxt = {"v": n_all + 1, "pi": 10 ** 9, "st": 0}  # the last verse numbers are lost: group them here
            p0 = (c["pi"], c["en"])
            if nxt:
                p1 = (nxt["pi"], nxt["st"])
            else:
                p1 = (len(log) - 1, len(log[-1][1]) if log else 0)
            text, _ = piece(p0, p1)
            # a head paragraph just before this token
            head = None
            for pi in range(((chain[idx - 1]["pi"]) if idx else 0), c["pi"] + 1):
                if pi < len(log) and log[pi][0] == "head" and (idx == 0 or pi >= chain[idx - 1]["pi"]):
                    head = log[pi][1]
            a_end = c["e"]
            printed = str(c["v"]) if c["e"] == c["v"] else f"{c['v']}-{c['e']}"
            if c.get("twin"):
                printed = f"({c['twin']} read as {c['v']})"
                stats["verse numbers read through an OCR digit confusion"] += 1
            u = {"a": c["v"], "a_end": a_end, "text": text, "head": head, "printed": printed}
            if nxt and nxt["v"] > a_end + 1:
                u["a_end"] = nxt["v"] - 1
                u["printed"] += f" (+{a_end + 1}-{nxt['v'] - 1}: numbers lost)" if nxt["v"] - 1 > a_end + 1 else \
                    f" (+{a_end + 1}: number lost)"
                u["lostgap"] = True
            units.append(u)
        return units

    def line_mode(sn: int) -> list[dict]:
        """The short surahs print their verses one per line without numbers, a few with «7.» / «10. … 11. …»."""
        paras = [t for kd, t in vlog.get(sn, []) if kd == "p"]
        n_all = counts[sn]
        units: list[dict] = []
        i_, pend, junk = 1, [], []

        def flush(upto: int) -> None:
            nonlocal i_, pend
            if upto < i_:
                junk.extend(pend)
                pend = []
                return
            if pend and len(pend) == upto - i_ + 1:
                for off, t_ in enumerate(pend):
                    units.append({"a": i_ + off, "a_end": i_ + off, "text": t_, "head": None,
                                  "printed": f"(unnumbered line {i_ + off})"})
            elif pend:
                units.append({"a": i_, "a_end": upto, "text": " ".join(pend), "head": None,
                              "printed": f"(unnumbered lines, {len(pend)} paragraphs for verses {i_}-{upto}; not separable)"})
                grouped.append(f"{sn}:{i_}" + (f"-{upto}" if upto > i_ else ""))
                issues.append(f"{sn}:{i_}-{upto}: printed as {len(pend)} unnumbered paragraphs; stored as one group")
            else:
                issues.append(f"{sn}:{i_}-{upto}: no text found")
            i_ = upto + 1
            pend = []

        conf = {3: 5, 5: 3, 6: 8, 8: 6, 1: 7, 7: 1}

        def anchors(t_: str, want: int) -> list[tuple[re.Match, int]]:
            out, w = [], want
            for m_ in re.finditer(r"(?:(?<=\s)|^)[.,*]?(\d{1,3})\s?[.)]\s+(?=\S)", t_):
                k_ = int(m_.group(1))
                if k_ == w or (conf.get(k_) == w and out) or (k_ > w and not out and k_ <= n_all and m_.start() <= 2):
                    out.append((m_, w if k_ != w and conf.get(k_) == w else k_))
                    w = out[-1][1] + 1
            return out
        for t_ in paras:
            ms = anchors(t_, i_)
            if ms and ms[0][0].start() <= 2:
                flush(ms[0][1] - 1)
                for ci, (m_, k) in enumerate(ms):
                    seg_end = ms[ci + 1][0].start() if ci + 1 < len(ms) else len(t_)
                    units.append({"a": k, "a_end": k, "text": t_[m_.end():seg_end].strip(), "head": None, "printed": str(k)})
                    i_ = k + 1
            else:
                pend.append(t_)
        if i_ <= n_all:
            flush(n_all)
        else:
            junk.extend(pend)
        if junk:
            stats["unnumbered paragraphs after the verses (commentary continuation), kept as an unmarked note"] += len(junk)
            if units:
                units[-1]["junk"] = " ".join(junk)
        stats["surahs whose verses are printed without numbers"] += 1
        return units

    for sn in range(1, 115):
        if sn not in intros:
            continue
        units = build_units(sn)
        got_n = sum(u["a_end"] - u["a"] + 1 for u in units if not u.get("lostgap")) + \
            sum(1 for u in units if u.get("lostgap"))
        if counts[sn] <= 15 and sn > 1 and len(units) < counts[sn] - 1 and vlog.get(sn):
            issues.append(f"surah {sn}: {len(units)} numbered units for {counts[sn]} verses; read line by line")
            units = line_mode(sn)
        for u in units:
            a0, a1 = u["a"], u["a_end"]
            if a0 > counts[sn]:  # the book numbers more verses than the project's count: kept with the last one
                book_over.append(f"{sn}:{a0}" + (f"-{a1}" if a1 > a0 else ""))
                a0, a1 = counts[sn], counts[sn]
            a1 = min(a1, counts[sn])
            if sn in SHIFT:
                a0, a1 = min(a0 + SHIFT[sn], counts[sn]), min(a1 + SHIFT[sn], counts[sn])
            if u.get("lostgap") and u["a"] != u["a_end"]:
                lost_numbers.append(f"{sn}:{u['a']}-{u['a_end']}" if u["a_end"] > u["a"] else f"{sn}:{u['a']}")
            key = (sn, a0)
            if key in verses:  # Fâtiha 6 and 7 together are 1:7
                x = verses[key]
                x["parts"].append(f"[{u['printed']}] " + u["text"])
                x["printed"] += "," + u["printed"]
                x["a_end"] = max(x["a_end"], a1)
            else:
                verses[key] = {"parts": [u["text"]] if u["text"] else [], "notes": [], "s": sn, "a": a0, "a_end": a1,
                               "printed": u["printed"], "head": u.get("head")}
            if u.get("junk"):
                verses[key]["notes"].append("[unmarked] " + u["junk"])
            if u.get("lostgap"):
                verses[key]["lostgap"] = True

    # ---- Fâtiha's besmele (1:1) -----------------------------------------------------------------
    bes = next((x.strip() for x in L[start:start + 400] if re.match(r"^Esirgeyen, bağışlayan Tanrı adıy", x.strip())), None)
    if bes:
        verses[(1, 1)] = {"parts": [bes], "notes": [], "s": 1, "a": 1, "a_end": 1, "printed": "besmele",
                          "head": "besmele line of the Fâtiha page"}
    else:
        issues.append("1:1: the besmele translation line was not found")

    # ---- footnotes: tied to their markers in document order ---------------------------------------
    for sn in range(1, 115):
        if sn in intros:
            for t in intros[sn]["parts"]:
                for m in MARK.finditer(t):
                    markers.append({"k": digits(m.group(1)), "unit": intros[sn], "s": sn, "done": False})
        for key in sorted(k for k in verses if k[0] == sn):
            for t in verses[key]["parts"]:
                for m in MARK.finditer(t):
                    markers.append({"k": digits(m.group(1)), "unit": verses[key], "s": sn, "done": False})
    for f in feet:
        cand = [mk for mk in markers if not mk["done"] and f["s"] - 1 <= mk["s"] <= f["s"]]
        hit = next((mk for mk in cand if mk["k"] == f["k"]), None) if f["k"] is not None else None
        if hit is None and cand:
            hit = ([mk for mk in cand if mk["s"] == f["s"]] or cand)[0]
            stats["footnotes tied by position (marker number unreadable or unmatched)"] += 1
        tgt = None
        if hit is not None:
            hit["done"] = True
            tgt = hit["unit"]
            lab = hit["k"] if hit["k"] is not None else f["k"]
        else:
            tgt = max((verses[k] for k in verses if k[0] == f["s"]), key=lambda x: x["a"], default=intros.get(f["s"]))
            lab = None
            stats["footnotes without a marker (tied to the surah's last verse, or its introduction)"] += 1
        if tgt is not None:
            tgt["notes"].append((f"[{lab}] " if lab is not None else "[unmarked] ") +
                                re.sub(r" +", " ", f["text"]).strip())
    # page-foot text of surahs without any verse unit: nothing to tie to

    # ---- segments -------------------------------------------------------------------------------
    segs: list[dict] = []
    for i, c in enumerate(chunks(L[:start]), 1):
        segs.append({"seg": f"{SID}:front{i:03d}", "head": "front matter (introduction)", "text": c,
                     "refs": IC.find_refs(c)})
    for sn, x in sorted(intros.items()):
        g = {"seg": f"{SID}:{sn}:intro", "s": sn, "a": 1, "a_end": counts[sn], "head": "surah introduction",
             "text": " ".join(x["parts"]).strip()}
        if x["notes"]:
            g["notes"] = "\n".join(x["notes"])
        segs.append(g)
    got: Counter = Counter()
    for (sn, a0), x in sorted(verses.items()):
        t = re.sub(r"\s+", " ", " ".join(x["parts"])).strip()
        if not t:
            issues.append(f"{sn}:{a0}-{x['a_end']}: the verse unit has no text in the OCR (number found, text lost)")
            continue
        g = {"seg": f"{SID}:{sn}:{a0}", "s": sn, "a": a0, "a_end": x["a_end"], "printed": x["printed"], "text": t}
        if x.get("head"):
            g["head"] = x["head"]
        if x["notes"]:
            g["notes"] = "\n".join(x["notes"])
        segs.append(g)
        for q in range(a0, x["a_end"] + 1):
            got[(sn, q)] += 1
    for i, c in enumerate(chunks(L[end:]), 1):
        segs.append({"seg": f"{SID}:back{i:03d}", "head": "back matter (contents table and index of topics)", "text": c,
                     "refs": IC.find_refs(c)})
    stated = {}
    for sn, x in intros.items():
        mm = re.search(r"(\d{1,3})\s*[âa]yettir", " ".join(x["parts"]))
        if mm:
            stated[sn] = int(mm.group(1))
    differs = {str(k): f"book {v}, project {counts[k]}" for k, v in sorted(stated.items()) if v != counts[k]}
    stats["front matter lines kept"] = start
    stats["back matter lines kept"] = len(L) - end
    missing = [f"{sn}:{q}" for sn in counts for q in range(1, counts[sn] + 1) if not got[(sn, q)]]
    short: dict[str, str] = {}
    for sn in counts:
        have = sum(1 for q in range(1, counts[sn] + 1) if got[(sn, q)])
        if have != counts[sn]:
            first = next(q for q in range(1, counts[sn] + 1) if not got[(sn, q)])
            short[str(sn)] = f"{have}/{counts[sn]} (first missing {sn}:{first})"

    def order(g: dict):
        n = g["seg"]
        if ":front" in n:
            return (0, 0, 0, n)
        if ":back" in n:
            return (2, 0, 0, n)
        return (1, g["s"], -1 if n.endswith("intro") else g["a"], n)
    segs.sort(key=order)
    covered = 6236 - len(missing)
    print(f"surah headings {len(ev_at)}; intros {len(intros)}; verse units {len(verses)}; verses covered {covered}/6236; "
          f"surahs short {len(short)}: {dict(list(short.items())[:15])}")
    if a.runs:
        runs: dict[int, list] = {}
        for m_ in missing:
            sn_, an_ = map(int, m_.split(":"))
            r_ = runs.setdefault(sn_, [])
            if r_ and r_[-1][1] == an_ - 1:
                r_[-1][1] = an_
            else:
                r_.append([an_, an_])
        for sn_, r_ in runs.items():
            print(sn_, " ".join(f"{x}" if x == y else f"{x}-{y}" for x, y in r_))
    if a.show:
        for k in sorted(k for k in verses if k[0] == a.show):
            x = verses[k]
            print(f"{k[0]}:{k[1]}-{x['a_end']} [{x['printed']}] {' '.join(x['parts'])[:160]!r} notes={len(x['notes'])}")
    print(f"footnotes {len(feet)}; stats {dict(stats)}; issues {len(issues)} {issues[:6]}")
    if a.dump:
        Path(a.dump).write_text("".join(IC.json.dumps(g, ensure_ascii=False) + "\n" for g in segs), encoding="utf-8")
    if a.dry:
        return
    IC.write(SID, segs, {
        "script": "enrichment/v2/fetch/import_meal_dogrul.py", "from": IC.inputs(SID, ["dogrul-tanri-buyrugu.djvu"]),
        "method": "archive.org OCR text (djvu.txt); surah headings in order; verses by sequential numbers; page-foot "
                  "footnotes tied by marker",
        "verse_count_mismatch": short, "missing": missing, "grouped_not_separable": grouped, "verse_numbers_lost_in_ocr_text_kept_as_group": lost_numbers,
        "book_numbers_beyond_project_count": book_over, "surah_headers_with_other_ayah_count": differs, "issues": issues, "counts": dict(stats),
        "dropped_sample": dropped,
    }, {"coverage": f"1-114 ({covered}/6236 ayat)", "locator": "ayah", "kind": "meal",
        "notes": "Public domain: author died 1952. OCR (archive.org djvu text) of the third printing (1955), read from "
                 "raw/acquired-2026-10-09; segments are the book's own verse units: verse groups as printed "
                 "(«6,7», «4-5»), `printed` keeps the numbers as printed, the page-foot tafsir footnotes are in `notes` "
                 "of the verse they are marked at. "
                 f"{len(lost_numbers)} verse units lost a verse number in the OCR: the unit then covers the verse "
                 "before and the lost one (listed in the ingestion record under verse_numbers_lost_in_ocr_text_kept_as_group). "
                 "The book's verse numbering differs from the project's Hafs count in surahs "
                 + ", ".join(differs) + " (see surah_headers_with_other_ayah_count; some of these differences are OCR misreads "
                 "of the printed count); there the units carry the book's numbers, numbers beyond the project's count are "
                 "kept with its last verse. Fâtiha is stored with the besmele as 1:1 (the book does not number it). "
                 "OCR quality: good running text, but diacritics are partly lost (ü/u, â/a), hyphenated line ends are joined, "
                 "and stray fragments of the Arabic text boxes remain here and there."
                 + (f" Verses without text: {', '.join(missing)}." if missing else " No verse without text.")})


if __name__ == "__main__":
    main()
