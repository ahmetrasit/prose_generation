#!/usr/bin/env python3
"""Books imported one segment per page (Task B, HYBRID_PLAN.md): the user's downloads whose structure is the page
(monographs, dictionaries without a reliable entry layout). Run fetch/pdf_pages.py on the source first.

  python3 -B enrichment/v2/fetch/import_pages.py NOLDEKE-GDQ [--dry]
  sources: NOLDEKE-GDQ JEFFERY-FOREIGN SINAI-KEYTERMS CUYPERS-COMPOSITION ZAMMIT-COMPARATIVE ISLAHI-TADABBUR

Per page: the text (from the PDF text layer, or from the archive's OCR file cut at the PDF page boundaries when that
OCR is the same as the text layer but keeps its spaces: Jeffery); the locator <ID>:p<printed page> (volumes:
v<vol>p<page>) when the page's printed number is read and agrees with a neighbour's, else <ID>:pdf<n> (v<vol>pdf<n>);
`head` = the running header; `refs` = the ayat it cites in the book's own citation style; Iṣlāḥī's pages are tied
to the surah their running header names. Repairs (counted in the ingestion record): Nöldeke's text layer puts every
word on its own line (rejoined) and marks line-end hyphenation with «¬» (rejoined); nothing else is changed.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402

ROMAN = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100}


def roman(s: str) -> int | None:
    s = s.lower()
    if not re.fullmatch(r"c{0,1}(?:xc|xl|l?x{0,3})(?:ix|iv|v?i{0,3})", s) or not s:
        return None
    total, prev = 0, 0
    for ch in reversed(s):
        v = ROMAN[ch]
        total += -v if v < prev else v
        prev = max(prev, v)
    return total


def refs_sur(text: str) -> list[str]:
    """German style (Nöldeke): «Sur. 21,5. 37,35. 52,30», «Süra 2,100», «Sure 96, 1—5»."""
    out = []
    for m in re.finditer(r"S[uüū]r(?:a|e)?\.?\s*(\d{1,3})\s*,\s*(\d{1,3})(?:\s*[-—–]\s*(\d{1,3}))?"
                         r"((?:\s*[.;]\s*\d{1,3}\s*,\s*\d{1,3}(?:\s*[-—–]\s*\d{1,3})?)*)", text):
        items = [(m.group(1), m.group(2), m.group(3))] + re.findall(
            r"(\d{1,3})\s*,\s*(\d{1,3})(?:\s*[-—–]\s*(\d{1,3}))?", m.group(4) or "")
        for s, a, b in items:
            s, a = int(s), int(a)
            b = IC._end(str(a), b) if b else None
            if IC.valid(s, a, b if b and b >= a else None):
                r = f"{s}:{a}" + (f"-{b}" if b and b > a else "")
                if r not in out:
                    out.append(r)
    return out


def refs_roman(text: str) -> list[str]:
    """Jeffery: a line of references only, «xxxviii, 36.», «ii, 7; xvii, 49, 98.»"""
    out = []
    for ln in text.split("\n"):
        if not re.fullmatch(r"\s*(?:[ivxlc]{1,8}\s*,\s*\d{1,3}(?:\s*[-–]\s*\d{1,3})?(?:\s*,\s*\d{1,3})*\s*[;.,]?\s*)+",
                            ln):
            continue
        for sm, rest in re.findall(r"([ivxlc]{1,8})\s*,\s*([\d,\s\-–]+)", ln):
            s = roman(sm)
            if not s or s > 114:
                continue
            for a, b in re.findall(r"(\d{1,3})(?:\s*[-–]\s*(\d{1,3}))?", rest):
                a = int(a)
                b = IC._end(str(a), b) if b else None
                if IC.valid(s, a, b if b and b >= a else None):
                    r = f"{s}:{a}" + (f"-{b}" if b and b > a else "")
                    if r not in out:
                        out.append(r)
    return out


def refs_islahi(text: str, surah: int | None) -> list[str]:
    out = IC.find_refs(text)
    if surah:
        for m in re.finditer(r"\bVerses?\s*\(?\s*(\d{1,3})(?:\s*[-–]\s*(\d{1,3}))?\s*\)?", text):
            a = int(m.group(1))
            b = IC._end(m.group(1), m.group(2)) if m.group(2) else None
            if IC.valid(surah, a, b if b and b >= a else None):
                r = f"{surah}:{a}" + (f"-{b}" if b and b > a else "")
                if r not in out:
                    out.append(r)
    return out


SOURCES = {
    "NOLDEKE-GDQ": {"stems": ["noldeke-gdq-vol-1", "noldeke-gdq-vol-2", "noldeke-gdq-vol-3"], "words": True,
                    "refs": "sur", "edition": "Th. Nöldeke, Geschichte des Qorāns, 2nd ed. (Schwally, Bergsträsser, "
                    "Pretzl), Leipzig 1909–1938, three volumes (archive.org scans, their OCR text layer)",
                    "caveat": "OCR of a Fraktur-free Antiqua print: German good; Arabic quotations in the text layer "
                              "are garbage (Latin OCR of Arabic script) and must not be quoted"},
    "JEFFERY-FOREIGN": {"stems": ["jeffery-foreign-1938"], "ocr": True, "refs": "roman",
                        "edition": "A. Jeffery, The Foreign Vocabulary of the Qurʾān, Baroda 1938 (archive.org scan "
                                   "and OCR)",
                        "caveat": "OCR: English good; Arabic, Syriac, Hebrew script quotations are garbage"},
    "SINAI-KEYTERMS": {"stems": ["sinai-key-terms-2023"], "refs": "colon",
                       "edition": "N. Sinai, Key Terms of the Qur'an: A Critical Dictionary, Princeton 2023 (PDF)"},
    "CUYPERS-COMPOSITION": {"stems": ["cuypers-composition-2015"], "refs": "colon",
                            "edition": "M. Cuypers, The Composition of the Qur'an: Rhetorical Analysis, London 2015 "
                                       "(PDF)"},
    "ZAMMIT-COMPARATIVE": {"stems": ["zammit-comparative-lexical-study"], "refs": "colon",
                           "edition": "M. R. Zammit, A Comparative Lexical Study of Qurʾānic Arabic, Leiden 2002 (PDF)",
                           "caveat": "the comparative tables are laid out in columns; the text layer reads them row "
                                     "by row across two entries (page text kept as extracted)"},
    "ISLAHI-TADABBUR": {"stems": ["tadabbur-e-quran-vol-3-surah-anam-06", "tadabbur-e-quran-vol-3-surah-araf-07",
                                  "tadabbur-e-quran-vol-3-surah-anfal-08",
                                  "tadabbur-e-quran-vol-4-surah-yunus-10-surah-maryam-19",
                                  "tadabbur-e-quran-vol-5-english", "tadabbur-e-quran-vol-6-2",
                                  "tadabbur-e-quran-vol-7-english", "tadabbur-e-quran-vol-8-english",
                                  "tadabbur-e-quran-vol-9-english"],
                        "refs": "islahi", "surah_header": True,
                        "edition": "A. A. Iṣlāḥī, Tadabbur-i Qurʾān, English translation (M. S. Kayani et al.), "
                                   "the PDF files with a text layer: surahs 6–8, 10–19 and vols 5–9",
                        "caveat": "English only; the Arabic quotations' text layer is often scrambled (presentation "
                                  "forms, control characters). Not yet imported: surah 9 (no text layer) and surahs "
                                  "1–5 (Urdu vols 1–2): OCR_NEEDED.md"},
}


def ocr_pages(sid: str, stem: str, rows: list[dict], stats: Counter) -> dict[int, str]:
    """The archive OCR file cut at the PDF page boundaries: each page's first non-space characters are found in the
    OCR (same OCR, the text layer only lost the spaces); a page not found keeps its text-layer text."""
    path = next(IC.src_dir(sid).glob(f"raw/acquired-*/{stem}.ocr.txt"))
    ocr = path.read_text(encoding="utf-8")
    pos_of = [i for i, ch in enumerate(ocr) if not ch.isspace()]
    flat = "".join(ocr[i] for i in pos_of)
    anchors, at = [], 0
    for r in rows:
        k = re.sub(r"\s", "", r["text"])
        if len(k) < 20:
            continue
        i = flat.find(k[:30], at)
        if i >= 0:
            anchors.append((r["page"], i, len(k)))
            at = i
    out = {}
    for j, (p, i, n) in enumerate(anchors):
        end = anchors[j + 1][1] if j + 1 < len(anchors) else len(flat)
        out[p] = ocr[pos_of[i]:pos_of[end - 1] + 1 if end - 1 < len(pos_of) else len(ocr)]
        stats["pages from the OCR file"] += 1
        if abs((end - i) - n) > max(40, n * 0.05):
            stats["pages whose OCR length differs from the text layer by >5%"] += 1
    return out


def printed_numbers(texts: dict[int, str]) -> dict[int, int]:
    """A page's printed number: a number standing alone at the top (first 3 lines) or bottom (last 2 lines) whose
    offset (PDF page minus number) is the most common offset among the candidates of the pages around it (±6), and
    shared by at least one neighbour; else none (the page is cited by its PDF page)."""
    cand: dict[int, set[int]] = {}
    for p, t in texts.items():
        ls = [x.strip() for x in t.split("\n") if x.strip()]
        c = set()
        for x in ls[:3] + ls[-2:]:
            if len(x) < 90:
                c.update(int(m.group(1)) for m in re.finditer(r"(?<![\d.,:/])(\d{1,4})(?![\d.,:/])", x))
        cand[p] = c
    out = {}
    for p, c in cand.items():
        votes = Counter(q - n for q in range(p - 6, p + 7) if q != p for n in cand.get(q, ()))
        best = [(votes[p - n], n) for n in c if votes[p - n] >= 1]
        if best:
            v, n = max(best)
            if v >= 1 and all(votes[p - m] < v for m in c if m != n):  # no tie
                out[p] = n
    return out


SURAH_NAMES = {
    "fatihah": 1, "fatiha": 1, "baqarah": 2, "baqara": 2, "alimran": 3, "imran": 3, "nisa": 4, "maidah": 5,
    "maida": 5, "anam": 6, "araf": 7, "anfal": 8, "tawbah": 9, "taubah": 9, "baraah": 9, "yunus": 10, "hud": 11,
    "yusuf": 12, "rad": 13, "ibrahim": 14, "hijr": 15, "nahl": 16, "baniisrail": 17, "isra": 17, "kahf": 18,
    "maryam": 19, "taha": 20, "anbiya": 21, "hajj": 22, "muminun": 23, "muminoon": 23, "nur": 24, "furqan": 25,
    "shuara": 26, "naml": 27, "qasas": 28, "ankabut": 29, "rum": 30, "luqman": 31, "sajdah": 32, "ahzab": 33,
    "saba": 34, "fatir": 35, "yasin": 36, "yaseen": 36, "saffat": 37, "sad": 38, "zumar": 39, "mumin": 40,
    "ghafir": 40, "hamimsajdah": 41, "hamimalsajdah": 41, "mumtahinah": 60, "abas": 80, "suad": 38, "nashrah": 94, "fussilat": 41, "shura": 42, "zukhruf": 43, "dukhan": 44, "jathiyah": 45,
    "ahqaf": 46, "muhammad": 47, "fath": 48, "hujurat": 49, "qaf": 50, "dhariyat": 51, "tur": 52, "najm": 53,
    "qamar": 54, "rahman": 55, "waqiah": 56, "hadid": 57, "mujadalah": 58, "hashr": 59, "mumtahanah": 60,
    "saff": 61, "jumuah": 62, "munafiqun": 63, "taghabun": 64, "talaq": 65, "tahrim": 66, "mulk": 67, "qalam": 68,
    "haqqah": 69, "maarij": 70, "nuh": 71, "jinn": 72, "muzzammil": 73, "muddaththir": 74, "muddathir": 74,
    "qiyamah": 75, "dahr": 76, "insan": 76, "mursalat": 77, "naba": 78, "naziat": 79, "abasa": 80, "takwir": 81,
    "infitar": 82, "mutaffifin": 83, "tatfif": 83, "inshiqaq": 84, "buruj": 85, "tariq": 86, "ala": 87,
    "ghashiyah": 88, "fajr": 89, "balad": 90, "shams": 91, "layl": 92, "lail": 92, "duha": 93, "sharh": 94,
    "inshirah": 94, "alamnashrah": 94, "tin": 95, "alaq": 96, "qadr": 97, "bayyinah": 98, "zilzal": 99,
    "zalzalah": 99, "adiyat": 100, "qariah": 101, "takathur": 102, "asr": 103, "humazah": 104, "fil": 105,
    "quraysh": 106, "quraish": 106, "maun": 107, "kawthar": 108, "kauthar": 108, "kafirun": 109, "nasr": 110,
    "lahab": 111, "masad": 111, "ikhlas": 112, "falaq": 113, "nas": 114,
}


def fold(s: str) -> str:
    import unicodedata
    s = unicodedata.normalize("NFD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = re.sub(r"[‘’ʿʾ'`´\-\s@]", "", s.lower())  # «S@āffāt»: «@» is a dot-below the text layer lost
    return s.replace("ḥ", "h")


def surah_in_header(lines: list[str]) -> int | None:
    """«Tadabbur-i-Qur’ān Vol.7: Sūrah Jāthiyah», «Vol.3: al-An‘ām (6)», «2 | Sūrah al-A‘lā»: the number in brackets,
    else the name after «Sūrah» (or after «Vol.N:») looked up, longest name first."""
    for x in lines:
        m = re.search(r"\((\d{1,3})\)", x)
        if m and 1 <= int(m.group(1)) <= 114 and ("Vol" in x or "rah" in x):
            return int(m.group(1))
        f = fold(x)
        m = re.search(r"surah(.*)$", f) or re.search(r"vol\.?\d+\)?:+(.*)$", f)
        if m:
            raw = m.group(1)
            for rest in (raw, raw[2:] if raw.startswith("al") else None):  # «al-ʿAlaq» = alalaq, «ʿAbasa» = abasa
                if rest is None:
                    continue
                for name in sorted(SURAH_NAMES, key=len, reverse=True):
                    if rest.startswith(name):
                        return SURAH_NAMES[name]
    return None


UNRELIABLE_HEADER = {"tadabbur-e-quran-vol-6-2"}  # its running header reads «Sūrah Sajdah» on every page (29–39)


def islahi_surahs(stem: str, texts: dict[int, str], stats: Counter) -> dict[int, int]:
    """Each page's surah in an Iṣlāḥī file. Votes: the surah named in a page's first lines (running header, or a
    heading «Sūrah X (N)»; the running header is skipped in UNRELIABLE_HEADER files). The longest run of votes that
    never goes backwards is kept (a table of contents or a cross-reference drops out, counted); a surah starts at its
    first kept vote, or earlier at a «Central Theme and Relationship with the Previous Sūrah» page after the last vote
    of the surah before; a surah with no vote between two kept ones is placed at such a «Central Theme» page when
    there is one (else its pages stay with the surah before: counted)."""
    votes: list[tuple[int, int]] = []
    marks: list[int] = []
    for p in sorted(texts):
        ls = [x.strip() for x in texts[p].split("\n") if x.strip()]
        zone = ls[1:8] if stem in UNRELIABLE_HEADER else ls[:4]
        zone = [x for x in zone if len(x) < 90]
        s = surah_in_header(zone) if stem not in UNRELIABLE_HEADER else next(
            (surah_in_header([x]) for x in zone if re.match(r"^S ?[ūu] ?r ?a ?h\b", x) and surah_in_header([x])), None)
        if s:
            votes.append((p, s))
        if any(re.match(r"(Central Theme|Theme and Relation)", x) for x in ls):
            if not marks or p - marks[-1] > 3:
                marks.append(p)
    # longest non-decreasing run of votes (by page order)
    n = len(votes)
    best, prev = [1] * n, [-1] * n
    for i in range(n):
        for j in range(i):
            if votes[j][1] <= votes[i][1] and best[j] + 1 > best[i]:
                best[i], prev[i] = best[j] + 1, j
    kept, i = [], max(range(n), key=lambda k: best[k]) if n else -1
    while i >= 0:
        kept.append(votes[i])
        i = prev[i]
    kept.reverse()
    stats["surah votes dropped (contents, cross-references)"] += n - len(kept)
    starts: dict[int, int] = {}  # surah -> first page
    last_page: dict[int, int] = {}
    for p, s in kept:
        starts.setdefault(s, p)
        last_page[s] = p
    order = sorted(starts)
    for k, s in enumerate(order[1:], 1):
        before = order[k - 1]
        missing = list(range(before + 1, s))
        free = [m for m in marks if last_page[before] < m <= starts[s]]
        # the marks between the surah before and this one: the missing surahs' openings first, in order, and the
        # last one this surah's opening
        for x, m in zip(missing, free):
            starts[x] = m
            stats["surahs placed at a «Central Theme» page (no vote)"] += 1
        for x in missing[len(free):]:
            stats[f"surah {x} not found in the file (its pages stay with the surah before)"] += 1
        if len(free) > len(missing):
            starts[s] = free[-1]
    if order:
        last = order[-1]
        after = [m for m in marks if m > last_page[last]]
        for k, m in enumerate(after, 1):  # surahs after the last one named (no header of their own)
            if last + k <= 114:
                starts[last + k] = m
                stats["surahs placed at a «Central Theme» page after the last named one"] += 1
        first = order[0]
        cand = [m for m in marks if m <= starts[first]]
        if cand:
            starts[first] = cand[-1]
    res: dict[int, int] = {}
    seq = sorted((p, s) for s, p in starts.items())
    for p in sorted(texts):
        cur = [s for q, s in seq if q <= p]
        if cur:
            res[p] = cur[-1]
    return res


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", choices=sorted(SOURCES))
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--dump")
    a = ap.parse_args()
    sid, cfg = a.source, SOURCES[a.source]
    stats: Counter = Counter()
    segs: list[dict] = []
    multi = len(cfg["stems"]) > 1
    counts = IC.ayah_counts()
    for vi, stem in enumerate(cfg["stems"], 1):
        rows = IC.pages(sid, stem)
        texts = {r["page"]: r["text"] for r in rows}
        if cfg.get("ocr"):
            texts.update(ocr_pages(sid, stem, rows, stats))
        if cfg.get("words"):
            for p, t in texts.items():
                n = t.count("¬")
                t = re.sub(r"¬\s*\n?\s*", "", t)
                stats["«¬» line-end hyphens rejoined"] += n
                texts[p] = re.sub(r"\s*\n\s*", " ", t).strip()
        nums = printed_numbers(texts) if not cfg.get("words") else printed_numbers(
            {p: "\n".join(re.findall(r"\S+", t)[:6] + re.findall(r"\S+", t)[-3:]) for p, t in texts.items()})
        prefix = f"v{vi}" if multi and sid != "ISLAHI-TADABBUR" else ""
        page_surah = islahi_surahs(stem, texts, stats) if cfg.get("surah_header") else {}
        sec_surah, sec = None, None
        for p in sorted(texts):
            t = texts[p].strip()
            if not t:
                stats["empty pages"] += 1
                continue
            if sid == "ISLAHI-TADABBUR":
                loc = f"{sid}:{stem.replace('tadabbur-e-quran-', '')}:p{p}"
            elif p in nums:
                loc = f"{sid}:{prefix}p{nums[p]}"
            else:
                loc = f"{sid}:{prefix}pdf{p}"
            first = next((x.strip() for x in t.split("\n")[:3]
                          if x.strip() and not x.strip().startswith("©") and not x.strip().isdigit()), "") \
                if not cfg.get("words") else ""
            g = {"seg": loc, "page": f"{stem}:pdf{p}", "head": re.sub(r"\s*\d+\s*$|^\s*\d+\s*", "", first)[:120],
                 "text": t}
            if p in nums:
                g["printed_page"] = nums[p]
            style = cfg["refs"]
            if style == "sur":
                g["refs"] = refs_sur(t)
            elif style == "roman":
                g["refs"] = refs_roman(t)
            elif style == "islahi":
                s = page_surah.get(p)
                if s and s != sec_surah:
                    sec_surah, sec = s, None
                # the section a page belongs to: «Section I: Verses (1-7)», «Verses (9-13):» headings; the page is
                # tied to the section it continues and every section that starts on it; before the first section
                # (introduction, central theme) to the whole surah
                heads = [(int(x), IC._end(x, y or None) or int(x)) for x, y in re.findall(
                    r"(?m)^\s*(?:Section [IVXL]+:\s*)?Verses?\s*\(?\s*(\d{1,3})(?:\s*[-–]\s*(\d{1,3}))?\s*\)?\s*:?",
                    t)] if s else []
                heads = [(x, y) for x, y in heads if IC.valid(s, x, y if y >= x else None)]
                if s and len(heads) >= 3:  # the introduction's outline of the sections («Verses (1-7): …» ×n)
                    heads, sec = [], None
                    stats["outline pages (3+ section headings) tied to the whole surah"] += 1
                if s:
                    keep_sec = sec and not (heads and heads[0][0] <= sec[0])  # a restart ends the old section
                    span = ([sec] if keep_sec else []) + heads
                    if span:
                        g.update({"s": s, "a": min(x for x, _ in span), "a_end": max(y for _, y in span)})
                        stats["pages tied to their section's verses"] += 1
                    else:
                        g.update({"s": s, "a": 1, "a_end": counts[s]})
                        stats["pages tied to the whole surah (before its first section)"] += 1
                    if heads:
                        sec = heads[-1]
                else:
                    stats["pages before the file's first surah header (not tied)"] += 1
                g["refs"] = refs_islahi(t, s)
            else:
                g["refs"] = IC.find_refs(t)
            segs.append(g)
    dup = [k for k, c in Counter(g["seg"] for g in segs).items() if c > 1]
    for g in segs:
        if g["seg"] in dup:
            g["seg"] = g["seg"].rsplit(":", 1)[0] + ":" + g["page"].replace(":", "-")
            stats["printed number shared by two pages: PDF page used"] += 1
    print(f"{sid}: {len(segs)} pages; {dict(stats)}; with refs {sum(1 for g in segs if g.get('refs'))}, "
          f"refs {sum(len(g.get('refs') or []) for g in segs)}; by printed page "
          f"{sum(1 for g in segs if 'printed_page' in g)}")
    if a.dry:
        if a.dump:
            Path(a.dump).write_text("".join(IC.json.dumps(g, ensure_ascii=False) + "\n" for g in segs))
        return
    old = IC.json.loads((IC.src_dir(sid) / "source.json").read_text())
    IC.write(sid, segs, {
        "script": f"enrichment/v2/fetch/import_pages.py {sid}", "from": IC.inputs(sid, cfg["stems"]),
        "method": ("archive OCR file cut at the PDF pages" if cfg.get("ocr") else "PDF text layer (pypdf via "
                   "fetch/pdf_pages.py)") + "; one segment per page; refs in the book's citation style",
        "repairs": dict(stats), "quality": cfg.get("caveat", "text layer good"),
    }, {"locator": "page", "edition": cfg["edition"],
        "coverage": "whole book by page; cited ayat in refs (`corpus.py cites S:A`)" + (
            "; pages tied to the surah of their running header" if cfg.get("surah_header") else ""),
        "licence": "copyrighted or public domain as the edition; local research copy only (user, 2026-10-05: "
                   "licence is no barrier for local analysis)",
        "notes": f"Ingested 2026-10-05 from the user's download (fetch/import_pages.py {sid}). "
                 + (cfg.get("caveat", "") + ". ") + "Pointer note before ingestion: " + (old.get("notes") or "")})


if __name__ == "__main__":
    main()
