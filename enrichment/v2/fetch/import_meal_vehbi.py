#!/usr/bin/env python3
"""MEAL-VEHBI and TAFSIR-VEHBI: Konyalı Mehmed Vehbi (1861-1949), «Hülâsatü'l-Beyân fî Tefsîri'l-Kur'ân» (Latin-script
edition, 15 volumes / 30 cüz; the archive.org item `hulasatul-beyan-fi-tefsiril-kuran-1-16-konyali-mehmed-vehbi`, its
*_djvu.txt OCR, raw/acquired-2026-10-09). Vehbi died 1949: public domain. Edition as stated in the text: Mümin Çevik ve
Ort. Koll. Şti., Beyaz Saray No. 4, Bayazıt, İstanbul, «Dördüncü Baskı» (volume 1 preface dated 16.11.1966).

Layout: after each volume's table of contents the tafsir runs by Arabic blocks. Per block the OCR holds: a lead-in
sentence («…beyan etmek üzere:»), the Arabic (OCR noise), «buyuruyor.», the Turkish translation of the block in
parentheses («(Şu Kur'ân bir kitap ki … şüphe yoktur.)», the closing bracket often read as «|»), then the commentary
(«Yani; …», quotations from Beyzâvî, Râzî, …) and page-foot notes. The publisher prints the translations in bold
(lost in the OCR). A block is a phrase, a verse or several verses (the Arabic carries the verse numbers: lost in the
OCR), so the blocks are tied to verses by a monotone alignment (dynamic programming) over the number of blocks and
verses, scored by lexical similarity to four Ottoman-style Turkish translations in the corpus (MEAL-BILMEN, MEAL-ELMALILI,
MEAL-IZMIRLI, MEAL-ELMALILI-HDKD; their local segments.jsonl are read) and by length. Cells of the alignment: one verse
with up to twenty blocks, or up to ten verses with one block, or 2–3 against 2–3. Tuned on ten short surahs whose
blocks were read by hand: 87% of the verses got the right blocks there; on long surahs the tie is less certain. The
score of every cell is kept in `align`; the
ingestion record lists the low-score cells.

Output: MEAL-VEHBI:S:A (verse or verse group A..A_end: the translation blocks), TAFSIR-VEHBI:S:A (the same cell: the
commentary), TAFSIR-VEHBI:S:intro (the surah's introduction), TAFSIR-VEHBI:frontNNN / backNNN (the volume tables of
contents, the preface, the indexes). Dropped and counted: page headers and page numbers, the Arabic OCR noise.

The besmele is not translated in the book: 1:1 is recorded as missing. The book counts the Fâtiha as seven verses without
the besmele; its blocks are aligned to 1:2–1:7.

  python3 -I -B enrichment/v2/fetch/import_meal_vehbi.py [--dry] [--dump DIR] [--show S]
"""
from __future__ import annotations

import argparse
import bisect
import difflib
import json
import math
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402

SID, TID = "MEAL-VEHBI", "TAFSIR-VEHBI"
RAW = "raw/acquired-2026-10-09/vehbi-hulasatul-beyan.djvu.txt"
REFS = ["MEAL-BILMEN", "MEAL-ELMALILI", "MEAL-IZMIRLI", "MEAL-ELMALILI-HDKD"]  # Ottoman-style translations: closest in wording
TR = re.compile(r"[A-Za-zÇĞİÖŞÜçğıöşüÂÎÛâîû]")
HEADER = re.compile(r"(F[İIi1]\s*TEFS[İI1]R|HUL[ÂA]\w{0,5}[-. ]?[ÜU]?L?\s*BEY|Hul[âa]sat.{0,3}[üu]l\s*Bey|[ÜU]L\s*BEYAN|BEYAN\s*C[üu]z|"
                    r"Imzalı nüshalar|^\W*[0-9]{3,4}\W*$|^\W*(?:[A-ZÇĞİÖŞÜ]+)\s+C[İI]LD[İI]N\s+SONU)")
PAGE_HDR = re.compile(r"^\W*S[üuÜ]re\s*(?P<num>[0-9OlI|]{1,3})?\s*[:;]?\s*(?P<name>[^\n]*?)\s*(?:\W*\w?\W*)F\W{0,3}[İIi]\s?TEFS")
HEADING = re.compile(r"^\W*[0-9]*\s*S[ÜU]\.?R\.?E[-—]?\s?[İIi1l]\s+([A-ZÂÎÛÇŞĞÖÜİ'’ -]{3,}?)\s*\W*$")
OPEN = re.compile(r"^[\(\[\{|“\"']\s*[\(\[|]?\s*(?:[Il1]\s?)?([A-ZÇĞİÖŞÜÂÎÛ][a-zçğıöşüâîû'’-]{2,})")
FNMARK = re.compile(r"^[\(\[]\s*[0-9lLiI|\*]{1,3}\s*[\)\]|J]")
BUYUR = re.compile(r"buyur\w*[.,:;]?")
NAMES = ("fatiha bakara aliimran nisa maide enam araf enfal tevbe yunus hud yusuf rad ibrahim hicr nahl isra kehf meryem taha "
         "enbiya hacc muminun nur furkan suara neml kasas ankebut rum lokman secde ahzab sebe fatir yasin saffat sad zumer "
         "mumin fussilet sura zuhruf duhan casiye ahkaf muhammed fetih hucurat kaf zariyat tur necm kamer rahman vakia "
         "hadid mucadele hasr mumtehine saf cuma munafikun tegabun talak tahrim mulk kalem hakka mearic nuh cin muzzemmil "
         "muddessir kiyame dehr mursel nebe naziat abese tekvir infitar mutaffifin insikak buruc tarik ala gasiye fecr "
         "beled sems leyl duha insirah tin alak kadr beyyine zilzal adiyat karia tekasur asr humeze fil kureys maun "
         "kevser kafirun nasr tebbet ihlas felak nas").split()


def norm(s: str) -> str:
    s = s.lower().replace("ı", "i")
    s = "".join(c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c))
    return re.sub(r"[^a-z]", "", s)


NORM_NAMES = [norm(n) for n in NAMES]


def name_to_sura(name: str) -> int | None:
    n = norm(name)
    if not n:
        return None
    if "imran" in n:
        return 3
    alias = {"hahska": 69, "muhammedaleyhisselam": 47, "dehrinsan": 76, "insan": 76}
    if n in alias:
        return alias[n]
    best, bs = None, 0.0
    for i, nm in enumerate(NORM_NAMES, 1):
        r = difflib.SequenceMatcher(None, n, nm).ratio()
        if r > bs:
            best, bs = i, r
    return best if bs >= 0.72 else None


def garbage(x: str) -> bool:
    """OCR noise of the Arabic: few letters, or fewer than 40% of the tokens plausible Turkish words."""
    s = re.sub(r"[\s\d/:;,.\-–()|]", "", x)
    if not s:
        return True
    if len(TR.findall(s)) / len(s) < 0.55:
        return True
    toks = [t for t in re.findall(r"\S+", x) if not re.fullmatch(r"[\d\W]+", t)]
    if not toks:
        return True
    word = re.compile(r"[«“\"(\[|]*[A-ZÇĞİÖŞÜÂ]?[a-zçğıöşüâîû'’]{2,}(?:-[a-zçğıöşüâîû]+)?[\W]*$")
    ok = sum(1 for t in toks if word.match(t) and len(re.sub(r"\W", "", t)) >= 3 and re.search(r"[aeıioöuüâîû]", t))
    has5 = any(word.match(t) and len(re.sub(r"\W", "", t)) >= 5 and re.search(r"[aeıioöuüâîû]", t) for t in toks)
    return ok / len(toks) < 0.4 and not has5


def join(lines: list[str]) -> str:
    out = ""
    for ln in lines:
        ln = ln.strip()
        if not ln:
            continue
        if out.endswith(("-", "­")) and re.match(r"[a-zçğıöşüâîû]", ln):
            out = out[:-1] + ln
        else:
            out = (out + " " + ln) if out else ln
    return re.sub(r"\s+", " ", out).strip()


def chunks(lines: list[str], size: int = 4000) -> list[str]:
    out, cur, para = [], "", []

    def flush():
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
            flush()
    flush()
    if cur:
        out.append(cur)
    return out


def toc_like(x: str) -> bool:
    s = x.strip()
    return bool(s) and bool(re.search(r"\.{3,}", s) or (len(s) < 80 and re.search(r"\s\d{1,4}\s*$", s)
                                                       and re.search(r"[a-zçğıöşüâîû]{4,}", s) and not garbage(s)))


SHAPES = [(1, k) for k in range(1, 21)] + [(k, 1) for k in range(2, 11)] + [(2, 2), (2, 3), (3, 2)]
PARAMS = {"offset": 0.05, "len": 0.05, "drift": 0.0, "many": 0.10, "stem": 4}  # tuned on 10 short surahs read by hand (87%)


def stems(text: str) -> list[str]:
    import unicodedata as ud
    t = "".join(c for c in ud.normalize("NFD", text.lower().replace("ı", "i")) if not ud.combining(c))
    k = PARAMS["stem"]
    return [w[:k] for w in re.findall(r"[a-z]{3,}", t.replace("'", " ").replace("’", " "))]


def build_refs(counts: dict, issues: list) -> tuple[dict, list, dict]:
    refs: dict[int, list[str]] = {s_: [""] * counts[s_] for s_ in counts}
    used_refs = []
    for rid in REFS:
        path = IC.src_dir(rid) / "segments.jsonl"
        if not path.exists():
            issues.append(f"reference translation {rid} not found locally ({path}): not used for the alignment")
            continue
        used_refs.append(rid)
        for line in path.open(encoding="utf-8"):
            g = json.loads(line)
            if g.get("s") and g.get("a") and g["s"] in counts:
                for q in range(g["a"], min(g["a_end"] or g["a"], counts[g["s"]]) + 1):
                    refs[g["s"]][q - 1] += " " + (g.get("text") or "")
    df: Counter = Counter()
    n_docs = 0
    for s_ in counts:
        for t in refs[s_]:
            df.update(set(stems(t)))
            n_docs += 1
    idf = {w: math.log((n_docs + 1) / (c + 1)) + 0.3 for w, c in df.items()}
    return refs, used_refs, idf


def align(sn: int, verse_nums: list[int], units: list[dict], refs: dict, idf: dict):
    """Monotone alignment of the translation blocks to the verses: cells
    [(first verse index, n verses, first block index, n blocks, similarity)] or None."""
    import numpy as np
    n, m = len(verse_nums), len(units)
    vt = [refs[sn][v - 1] for v in verse_nums]
    bt = [u["meal"] for u in units]
    vocab: dict[str, int] = {}
    vt_s = [stems(t) for t in vt]
    bt_s = [stems(t) for t in bt]
    for ws in vt_s + bt_s:
        for w in ws:
            vocab.setdefault(w, len(vocab))
    D = max(1, len(vocab))

    def mat(sts):
        M = np.zeros((len(sts), D))
        for i, ws in enumerate(sts):
            for w, c in Counter(ws).items():
                M[i, vocab[w]] = (1 + math.log(c)) * idf.get(w, 1.5)
        return M
    Mv, Mb = mat(vt_s), mat(bt_s)
    Cv = np.vstack([np.zeros((1, D)), np.cumsum(Mv, axis=0)])
    Cb = np.vstack([np.zeros((1, D)), np.cumsum(Mb, axis=0)])
    lv = np.concatenate([[0], np.cumsum([len(x) for x in vt_s])]).astype(float)
    lb = np.concatenate([[0], np.cumsum([len(x) for x in bt_s])]).astype(float)
    rho = max(0.5, lb[-1] / max(1.0, lv[-1]))

    def rng(C, d):
        R = C[d:] - C[:-d]
        return R / np.maximum(np.linalg.norm(R, axis=1, keepdims=True), 1e-9)
    rewards = {}
    P = PARAMS
    for dv, db in SHAPES:
        if dv > n or db > m:
            continue
        sim = rng(Cv, dv) @ rng(Cb, db).T
        wv = lv[dv:] - lv[:-dv]
        wb = lb[db:] - lb[:-db]
        pen = np.abs(np.log((wb[None, :] + 2) / (rho * wv[:, None] + 2)))
        ei = np.arange(sim.shape[0])[:, None] + dv
        ej = np.arange(sim.shape[1])[None, :] + db
        drift = np.abs(lb[ej] / max(1.0, lb[-1]) - lv[ei] / max(1.0, lv[-1]))
        many = P["many"] * (min(dv, db) - 1) if min(dv, db) > 1 else 0.0
        rewards[(dv, db)] = (sim - P["offset"] - P["len"] * pen - P["drift"] * drift * (dv + db) / 2.0 - many, sim)
    NEG = -1e18
    f = np.full((n + 1, m + 1), NEG)
    f[0, 0] = 0.0
    choice = np.zeros((n + 1, m + 1), dtype=np.int16)
    shapes = [sh for sh in SHAPES if sh in rewards]
    for i in range(1, n + 1):
        for si, (dv, db) in enumerate(shapes):
            if i < dv:
                continue
            R = rewards[(dv, db)][0][i - dv]
            cand = f[i - dv, 0:m - db + 1] + R
            tgt = f[i, db:m + 1]
            better = cand > tgt
            if better.any():
                f[i, db:m + 1] = np.where(better, cand, tgt)
                ch = choice[i, db:m + 1]
                ch[better] = si
    if f[n, m] <= NEG / 2:
        return None
    cells, i, j = [], n, m
    while i > 0 or j > 0:
        dv, db = shapes[choice[i, j]]
        sim = float(rewards[(dv, db)][1][i - dv, j - db])
        cells.append((i - dv, dv, j - db, db, sim))
        i, j = i - dv, j - db
    cells.reverse()
    return cells


# --- digital edition: surahs whose Arabic carries the verse numbers --------------------------------------------------
# archive.org item 2Bakara_201602 (Konyalı Mehmet Vehbi Efendi, «Hulasat'ül Beyan», surah PDFs with a text layer, the Arabic
# with its verse numbers kept; the same translation text as the djvu OCR). Where a surah PDF is held, its blocks are tied
# to verses by the verse numbers printed in the Arabic instead of by the similarity alignment (the other surahs keep the
# alignment). PDFs are read as data only (pypdf).
PDF_DIR = "raw/ia-2Bakara_201602-2026-10-09"
PDF_SURAHS = {1: "1-fatiha", 2: "2-bakara", 3: "3-ali-imran", 4: "4-nisa", 5: "5-maide", 6: "6-enam", 8: "8-enfal"}
PDF_ARABIC = re.compile(r"[\u0600-\u06FF\uFB50-\uFDFF\uFE70-\uFEFF]")
PDF_MARK = re.compile(r"[\ufd3f\ufd3e\(]\s*(\d{1,3})\s*[\ufd3e\ufd3f\)]")
PDF_BUY = re.compile(r"^buyur\w*[.,:;]?$")


def pdf_text_clean(lines: list[str]) -> str:
    t = ""
    for ln in lines:
        ln = ln.strip()
        if not ln:
            continue
        if t.endswith("-") and ln[:1].islower():
            t += ln  # a line-end hyphen: «vahy-» «i münzel» -> «vahy-i münzel»
        else:
            t = (t + " " + ln) if t else ln
    t = re.sub(r"(?<=[A-Za-zÇĞİÖŞÜçğıöşüÂÎÛâîû])\s+-(?=[a-zçğıöşüâîû])", "-", t)
    return re.sub(r"\s+", " ", t).strip()


def pdf_blocks(path: Path) -> tuple[list[tuple], list[str]]:
    """Events of one surah PDF in reading order: ('M', n, form, line) a verse number in the Arabic; ('B', i0, i1, line)
    a translation block (lines i0..i1, brackets stripped). Also returns the lines."""
    import logging
    import pypdf
    logging.disable(logging.CRITICAL)
    reader = pypdf.PdfReader(path)
    lines = "\n".join(pg.extract_text() or "" for pg in reader.pages).split("\n")
    ev: list[tuple] = []
    recent: list[bool] = []
    after_buy = False

    def grab(i: int, strict: bool) -> int | None:
        for k in range(i, min(len(lines), i + 30)):
            if strict and k > i and (PDF_ARABIC.search(lines[k]) or lines[k].strip().startswith("[") or PDF_MARK.search(lines[k])):
                return None
            if "]" in lines[k]:
                return k
        return None

    i = 0
    while i < len(lines):
        s_ = lines[i].strip()
        if s_.startswith("["):
            k = grab(i, False)
            if k is not None:
                ev.append(("B", i, k))
                i, after_buy = k + 1, False
                continue
        if after_buy and s_:
            k = grab(i, True)
            after_buy = False
            if k is not None and not PDF_ARABIC.search(" ".join(lines[i:k + 1])[:60]) and sum(len(x) for x in lines[i:k + 1]) < 2500:
                ev.append(("B", i, k))
                i = k + 1
                continue
        for m in PDF_MARK.finditer(lines[i]):
            before, after = lines[i][:m.start()], lines[i][m.end():]
            ba, aa = bool(PDF_ARABIC.search(before)), bool(PDF_ARABIC.search(after))
            if not (ba or aa or (not before.strip() and not after.strip())):
                continue  # a number in Turkish prose
            ev.append(("M", int(m.group(1)), "lead" if (not ba and aa) else "trail", i))
        if s_:
            recent = (recent + [bool(PDF_ARABIC.search(s_) or PDF_MARK.search(s_))])[-4:]
        if PDF_BUY.match(s_) and any(recent[-4:-1] or [False]):
            after_buy = True
        i += 1
    return ev, lines


def pdf_cells(sn: int, nv: int, first_verse: int) -> list[dict] | None:
    """Cells {a, b, meal[], comm[]} of surah sn from its PDF, or None when the PDF is not held."""
    stem = PDF_SURAHS.get(sn)
    path = IC.src_dir(SID) / PDF_DIR / f"{stem}.pdf" if stem else None
    if not path or not path.exists():
        return None
    ev, lines = pdf_blocks(path)
    cov_end, hv, last, fresh, prev = first_verse - 1, 0, None, False, None
    blocks: list[dict] = []
    for e in ev:
        if e[0] == "M":
            if hv < e[1] <= hv + 4:
                hv = e[1]  # a stray number (a reference inside the Arabic) never jumps ahead
                fresh = True
            last = e[2]
            continue
        if not fresh and prev is not None and last == "lead":
            a_, b_ = prev  # a further phrase block of the verse whose number opened the Arabic
        elif last == "lead":
            a_, b_ = cov_end + 1, max(hv, cov_end + 1)
            cov_end = b_
        elif hv > cov_end:
            a_, b_ = cov_end + 1, hv
            cov_end = hv
        else:
            a_ = b_ = cov_end + 1  # a phrase block before the number that closes its verse
        fresh = False
        prev = (min(a_, nv), min(b_, nv))
        blocks.append({"a": prev[0], "b": prev[1], "i0": e[1], "i1": e[2]})

    def pre_start(i0: int) -> int:
        j = i0 - 1
        while j >= 0 and (not lines[j].strip() or PDF_ARABIC.search(lines[j]) or PDF_MARK.search(lines[j]) or PDF_BUY.match(lines[j].strip())):
            j -= 1
        return j + 1
    cells: list[dict] = []
    for bi, b in enumerate(blocks):
        txt = pdf_text_clean(lines[b["i0"]:b["i1"] + 1])
        txt = re.sub(r"^\[\s*", "", txt)
        txt = re.sub(r"\s*\].*$", "", txt)
        end_comm = pre_start(blocks[bi + 1]["i0"]) if bi + 1 < len(blocks) else len(lines)
        comm_lines = lines[b["i1"] + 1:max(b["i1"] + 1, end_comm)]
        tail = lines[b["i1"]].split("]", 1)[1] if "]" in lines[b["i1"]] else ""
        comm = pdf_text_clean([tail] + comm_lines)
        if cells and b["a"] <= cells[-1]["b"]:  # the same verse again (a phrase block, then the closing block): one cell
            cells[-1]["meal"].append(txt)
            cells[-1]["comm"].append(comm)
            cells[-1]["a"] = min(cells[-1]["a"], b["a"])
            cells[-1]["b"] = max(cells[-1]["b"], b["b"])
        else:
            cells.append({"a": b["a"], "b": b["b"], "meal": [txt], "comm": [comm]})
    return cells



def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--dump", help="directory for the two segments files of a dry run")
    ap.add_argument("--show", type=int, help="print the blocks (or with --align the aligned cells) of this surah")
    ap.add_argument("--save-blocks", help="write the blocks of all surahs to this pickle file (development)")
    ap.add_argument("--align", action="store_true", help="run the alignment (a dry run otherwise stops after the blocks)")
    a = ap.parse_args()
    counts = IC.ayah_counts()
    L = (IC.src_dir(SID) / RAW).read_text(encoding="utf-8").replace("\f", "\n").split("\n")
    stats: Counter = Counter()
    issues: list[str] = []
    dropped: dict[str, list[str]] = {}

    def drop(cat: str, text: str) -> None:
        stats[f"dropped: {cat}"] += 1
        stats[f"dropped chars: {cat}"] += len(text)
        dropped.setdefault(cat, [])
        if len(dropped[cat]) < 12:
            dropped[cat].append(text.strip()[:70])

    # ---- volumes: front matter (title, tables of contents) and body -----------------------------
    toc_starts = [i for i, l in enumerate(L) if re.search(r"C[İI]LD[İI]N F[İI]HR[İI]ST[İI]", l)]
    index_start = next(i for i, l in enumerate(L) if i > toc_starts[-1] and re.match(r"^\W*[ÖO]?F[İI]HR[İI]ST\W*$", l.strip()))
    body_from = next(i for i, l in enumerate(L) if re.match(r"^\W*B[İI]R[İI]NC[İI] C[ÜU]Z\W*$", l.strip()))
    front_ranges: list[tuple[int, int]] = [(0, body_from)]
    for ts in toc_starts[1:]:
        for i in range(ts + 3, ts + 3000):
            w = [L[j].strip() for j in range(i, i + 7)]
            if all(len(x) >= 50 for x in w[:6]) and not any(toc_like(x) for x in w) and \
                    sum(1 for x in w[:6] if x.endswith("-")) >= 2:
                end_toc = max(j for j in range(ts, i) if toc_like(L[j])) + 1  # the last contents line before the prose
                front_ranges.append((ts, end_toc))
                break
        else:
            issues.append(f"the table of contents starting at line {ts + 1} has no recognisable end")
    in_front = [False] * len(L)
    for s0, s1 in front_ranges:
        for i in range(s0, s1):
            in_front[i] = True
    for i in range(index_start, len(L)):
        in_front[i] = True  # the indexes at the end (back matter)

    # ---- page headers and surah boundaries --------------------------------------------------------
    pts = []  # (line, sura)
    hdr_lines = set()
    for i, l in enumerate(L):
        if in_front[i]:
            continue
        m = PAGE_HDR.match(l)
        if m:
            hdr_lines.add(i)
            num = m.group("num")
            n = int(re.sub(r"[OlI|]", "0", num)) if num and re.sub(r"[OlI|]", "0", num).isdigit() else None
            nm = re.sub(r"[^A-Za-zÂâÎîÛûÇçĞğİıÖöŞşÜü'’ -]", "", m.group("name"))
            s = n if n and 1 <= n <= 114 else name_to_sura(nm)
            if s:
                pts.append((i, s))
    # the longest non-decreasing run of surah numbers
    tails: list[int] = []
    prev = [-1] * len(pts)
    for i, (_, s) in enumerate(pts):
        k = bisect.bisect_right([pts[t][1] for t in tails], s)
        if k == len(tails):
            tails.append(i)
        else:
            tails[k] = i
        prev[i] = tails[k - 1] if k else -1
    chain, i = [], tails[-1]
    while i >= 0:
        chain.append(pts[i])
        i = prev[i]
    chain.reverse()
    stats["page headers with a surah"] = len(pts)
    stats["page headers off the surah sequence (OCR misreads)"] = len(pts) - len(chain)
    first, last = {}, {}
    for ln, s in chain:
        first.setdefault(s, ln)
        last[s] = ln
    heads = []  # real headings: «SURE-İ NAME» followed by the «nâzil olan» line
    for i, l in enumerate(L):
        if in_front[i]:
            continue
        m = HEADING.match(l)
        if m and re.search(r"(n[âa]|ha)zil|s[üu]relerden", " ".join(x for x in L[i + 1:i + 14] if x.strip())):
            heads.append((i, name_to_sura(m.group(1)), m.group(1).strip()))
    intro_lines = [i for i, l in enumerate(L) if not in_front[i] and re.search(r"(n[âa]|ha)zil\s+olan\s+s[üu]r", l)
                   and re.search(r"(Mekke|Medine)", " ".join(L[i:i + 3]))]
    start_of: dict[int, int] = {1: body_from}
    how_of: dict[int, str] = {1: "«BİRİNCİ CÜZ»"}
    prev_start = body_from
    for s in range(2, 115):  # 1. the real headings, in order
        c = [i for i, ss, nm in heads if ss == s and i > prev_start]
        if c:
            start_of[s] = c[0]
            how_of[s] = "heading"
            prev_start = c[0]
    claimed = {i for i in intro_lines for st in start_of.values() if 0 <= i - st <= 8}
    for s in range(2, 115):  # 2. the «nâzil olan sürelerden» line between the neighbours' starts
        if s in start_of:
            continue
        lo = max((v for k, v in start_of.items() if k < s), default=body_from)
        hi = min((v for k, v in start_of.items() if k > s), default=len(L))
        c = [i for i in intro_lines if lo < i < hi and i not in claimed]
        if c:
            start_of[s] = max(c[0] - 3, lo + 1)
            how_of[s] = "intro line"
            claimed.add(c[0])
    for s in range(2, 115):  # 3. the first page header of the surah
        if s in start_of:
            continue
        lo = max((v for k, v in start_of.items() if k < s), default=body_from)
        hi = min((v for k, v in start_of.items() if k > s), default=len(L))
        c = [ln for ln, ss in pts if ss == s and lo < ln < hi]
        start_of[s] = c[0] if c else lo + 1
        how_of[s] = "first page header" if c else "after the previous surah's start"
        issues.append(f"surah {s}: neither heading nor «nâzil olan sürelerden» line found between the neighbouring surahs; "
                      f"its start is taken at the {how_of[s]} (line {start_of[s] + 1})")
    for s in range(1, 115):
        stats[f"surah starts found by: {how_of[s]}"] += 1
    starts_sorted = sorted(start_of.items(), key=lambda kv: kv[1])
    for (s0, l0), (s1, l1) in zip(starts_sorted, starts_sorted[1:]):
        if l1 <= l0:
            issues.append(f"surah starts out of order: {s0} at line {l0 + 1}, {s1} at line {l1 + 1}")
    # ---- per surah: paragraphs, then the blocks --------------------------------------------------
    bounds = {s: (start_of[s], start_of[s + 1] if s < 114 else index_start) for s in range(1, 115)}
    OPENER = re.compile(r"([\(\[|{“\"'])\s*[\(\[|]?\s*(?:[Il1]\s?)?(?=[A-ZÇĞİÖŞÜÂÎÛ](?:[a-zçğıöşüâîû'’-]{1,}|\s))")

    def paragraphs(a0: int, a1: int) -> list[tuple[int, list[str]]]:
        out, cur, st = [], [], a0
        for i in range(a0, a1):
            l = L[i]
            if in_front[i]:
                if cur:
                    out.append((st, cur))
                    cur = []
                continue
            if i in hdr_lines or (HEADER.search(l) and len(l.strip()) < 90):
                drop("page headers and page numbers", l)
                if cur:
                    out.append((st, cur))
                    cur = []
                continue
            if l.strip():
                if not cur:
                    st = i
                cur.append(l.strip())
            elif cur:
                out.append((st, cur))
                cur = []
        if cur:
            out.append((st, cur))
        return out

    def find_meal(t: str, ctx_ok: bool) -> tuple[int, int] | None:
        """(start, end) of a translation block inside a paragraph text: after «buyuruyor.» or at the paragraph start
        (a few noise characters may precede it); end: the closing bracket (OCR: ) | ] J) or the paragraph end."""
        st = None
        m = re.search(r"buyur\w*[.,:;]?\s*(?=[\(\[|{“\"'])", t)
        if m:
            m2 = OPENER.match(t, m.end())
            if m2:
                st = m2.start(1)
        if st is None and ctx_ok:
            for m2 in OPENER.finditer(t[:60]):
                pre = t[:m2.start(1)].strip()
                if len(pre) <= 25 and not re.search(r"[a-zçğıöşüâîû]{4,}", pre) and not FNMARK.match(t[m2.start(1):]):
                    st = m2.start(1)
                    break
        if st is None:
            return None
        depth = 0
        end = len(t)
        for j in range(st, len(t)):
            c = t[j]
            if c == "(":
                depth += 1
            elif c in ")|]J" and j - st >= 12:
                nxt = t[j + 1:j + 4].lstrip()
                after_ok = (not nxt) or re.match(r"[A-ZÇĞİÖŞÜÂÎÛ«“\"(|.]", nxt) or nxt[:1] in "0123456789"
                if c == ")":
                    depth -= 1
                    if depth > 0:
                        continue
                if after_ok or c == "|":
                    end = j + 1
                    break
        return st, end

    blocks_of: dict[int, list[dict]] = {}
    intro_of: dict[int, str] = {}
    for s in range(1, 115):
        a0, a1 = bounds[s]
        ps = paragraphs(a0, a1)
        texts = [join(c) for _, c in ps]
        texts0 = list(texts)
        units = []
        k = 0
        taken_to = -1
        while k < len(ps):
            t = texts[k]
            prev3 = ps[max(0, k - 3):k]
            n_garb = sum(1 for pp in prev3 for l in pp[1] if len(l) >= 3 and garbage(l))
            has_buy = any(BUYUR.search(join(pp[1])) for pp in prev3)
            has_colon = bool(prev3) and join(prev3[-1][1]).rstrip().endswith(":")
            ctx = n_garb >= 1 or has_buy or has_colon
            fm = find_meal(t, ctx) if not FNMARK.match(t) else None
            if fm is None or len(t[fm[0]:fm[1]]) < 20:
                k += 1
                continue
            st, en = fm
            meal = t[st:en]
            k_end = k
            if en >= len(t) and not re.search(r"[)|\]J]\s*$", meal):  # unclosed: runs on into the next paragraphs
                for kk in range(k + 1, min(k + 4, len(ps))):
                    tt = texts[kk]
                    fm2 = re.search(r"[)|\]J]", tt)
                    if re.match(r"(Yani|Zira|Çünkü)", tt):
                        break
                    if fm2 and fm2.end() > 1:
                        meal += " " + tt[:fm2.end()]
                        t_rest = tt[fm2.end():]
                        k_end = kk
                        texts[kk] = t_rest
                        break
                    meal += " " + tt
                    k_end = kk
                    texts[kk] = ""
                else:
                    stats["translation blocks without a closing bracket (kept to the paragraph end)"] += 1
            rest = t[en:] if k_end == k else texts[k_end]
            units.append({"k": k, "pre": t[:st].strip(), "meal": meal, "rest": rest, "k_end": k_end, "line": ps[k][0] + 1,
                          "ctx": (n_garb, has_buy, has_colon, bool(t[:st].strip()))})
            if k_end == k:
                texts[k] = rest
            k = k_end + 1 if k_end != k else k + 1
        # prelude (lead-in sentence, Arabic noise, «buyuruyor.») of every block, then the commentary between blocks
        def prelike(j: int) -> bool:
            tt = texts0[j]
            return garbage(tt) or len(tt) < 12 or (bool(BUYUR.search(tt)) and len(tt) < 40)
        floor = -1
        for ui, u in enumerate(units):
            j = u["k"] - 1
            while j > floor and prelike(j):
                j -= 1
            lead_from = j + 1
            if j > floor and texts0[j].rstrip().endswith(":") and len(texts0[j]) < 600 and not FNMARK.match(texts0[j]):
                u["lead"] = texts0[j]
                j -= 1
                lead_from = j + 1 if False else j + 1
            u["pre_from"] = j + 1
            floor = u["k_end"]
        for ui, u in enumerate(units):
            nxt_pre = units[ui + 1]["pre_from"] if ui + 1 < len(units) else len(ps)
            body = [u["rest"]] if u["rest"] else []
            for j in range(u["k_end"] + 1, nxt_pre):
                tt = texts0[j] if j != u["k_end"] else u["rest"]
                if not tt:
                    continue
                if garbage(tt) and len(tt) < 200:
                    drop("Arabic OCR noise paragraphs (between the blocks)", tt)
                    continue
                body.append(tt)
            u["comm"] = "\n".join(x for x in body if x)
        first_pre = units[0]["pre_from"] if units else len(ps)
        intro_parts = []
        for j in range(0, first_pre):
            tt = texts0[j]
            if garbage(tt) and len(tt) < 200:
                drop("Arabic OCR noise paragraphs (between the blocks)", tt)
                continue
            intro_parts.append(tt)
        intro_of[s] = "\n".join(intro_parts)
        for u in units:
            m_ = u["meal"]
            m_ = re.sub(r"^.{0,60}?buyur\w*[.,:;]?\s*(?=[\(\[|{“\"'])", "", m_)  # noise and «buyuruyor.» before the opener
            m_ = re.sub(r"^[\(\[\{|“\"']\s*[\(\[|]?\s*", "", m_)
            m_ = re.sub(r"\s*[\)\]|J]\s*$", "", m_)
            u["meal"] = re.sub(r"\s+", " ", m_).strip()
        blocks_of[s] = units
        if a.show == -3 and s == 2:
            import random
            random.seed(5)
            for u in random.sample(units, 40):
                print(u["line"], u["ctx"], u["meal"][:100].replace("\n", " "), "...", u["meal"][-25:])
    if a.save_blocks:
        import pickle
        pickle.dump({"blocks_of": blocks_of, "intro_of": intro_of, "stats": dict(stats), "dropped": dropped}, open(a.save_blocks, "wb"))
        return
    if a.show and a.show > 0 and not a.dump and not a.align:
        for i_, u in enumerate(blocks_of[a.show], 1):
            print(f"[{i_}] line {u['line']} lead={u.get('lead', '')[:70]!r}\n    MEAL {u['meal'][:240]!r}\n    COMM {u['comm'][:160]!r} ({len(u['comm'])})")
        print("INTRO", intro_of[a.show][:300])
        return
    if a.show == -3:
        return
    if a.show == -2:
        bad = [(s, len(blocks_of[s]), counts[s]) for s in range(1, 115)]
        print(bad)
        return
    refs, used_refs, idf = build_refs(counts, issues)

    meal_segs: list[dict] = []
    tafs_segs: list[dict] = []
    low: list[str] = []
    missing: list[str] = []
    sims_all = []
    fallback_surahs: list[str] = []
    pdf_surahs: list[int] = []
    for sn in range(1, 115):
        verse_nums = list(range(2, counts[sn] + 1)) if sn == 1 else list(range(1, counts[sn] + 1))
        if sn == 1:
            missing.append("1:1")
        pc = pdf_cells(sn, counts[sn], verse_nums[0])
        if pc is not None:
            pdf_surahs.append(sn)
            for c_ in pc:
                loc = f"{sn}:{c_['a']}"
                g = {"seg": f"{SID}:{loc}", "s": sn, "a": c_["a"], "a_end": c_["b"], "text": " ".join(c_["meal"]).strip(),
                     "blocks": len(c_["meal"]), "align": None, "aligned_by": "verse numbers printed in the Arabic (digital PDF)",
                     "page": None}
                meal_segs.append(g)
                tafs_segs.append({"seg": f"{TID}:{loc}", "s": sn, "a": c_["a"], "a_end": c_["b"],
                                  "text": "\n\n".join(x for x in c_["comm"] if x), "blocks": len(c_["meal"]), "align": None,
                                  "aligned_by": "verse numbers printed in the Arabic (digital PDF)", "page": None})
            continue
        units = blocks_of[sn]
        cells = None
        if units:
            cells = align(sn, verse_nums, units, refs, idf)
        if cells is None:
            issues.append(f"surah {sn}: no alignment path ({len(units)} blocks, {len(verse_nums)} verses): "
                          + ("blocks distributed over the verses by length" if units else "no translation block found"))
            if not units:
                missing.extend(f"{sn}:{v}" for v in verse_nums)
                intro_of[sn] = intro_of.get(sn, "")
                continue
            # proportional fallback: cumulative length of the blocks against the verses
            fallback_surahs.append(str(sn))
            tot = sum(len(u["meal"]) for u in units) or 1
            cells, acc, vi = [], 0, 0
            for ui, u in enumerate(units):
                acc += len(u["meal"])
                target = min(len(verse_nums), max(vi + 1, round(acc / tot * len(verse_nums)))) if ui < len(units) - 1 else len(verse_nums)
                if target > vi:
                    cells.append((vi, target - vi, ui, 1, 0.0))
                    vi = target
                else:
                    cells[-1] = (cells[-1][0], cells[-1][1], cells[-1][2], cells[-1][3] + 1, 0.0)
        for (vi, dv, bj, db, sim) in cells:
            vs = verse_nums[vi:vi + dv]
            us = units[bj:bj + db]
            a0, a1 = vs[0], vs[-1]
            loc = f"{sn}:{a0}"
            meal = " ".join(u["meal"] for u in us).strip()
            tparts = []
            for u in us:
                if u.get("lead"):
                    tparts.append(u["lead"])
                if u["comm"]:
                    tparts.append(u["comm"])
            g = {"seg": f"{SID}:{loc}", "s": sn, "a": a0, "a_end": a1, "text": meal, "blocks": db, "align": round(sim, 3),
                 "page": None}
            meal_segs.append(g)
            tafs_segs.append({"seg": f"{TID}:{loc}", "s": sn, "a": a0, "a_end": a1, "text": "\n\n".join(tparts),
                              "blocks": db, "align": round(sim, 3), "page": None})
            sims_all.append(sim)
            if sim < 0.12 and dv + db > 2:
                low.append(f"{sn}:{a0}" + (f"-{a1}" if a1 > a0 else "") + f" ({db} blocks, sim {sim:.2f})")
    for sn in range(1, 115):
        if intro_of.get(sn, "").strip():
            tafs_segs.append({"seg": f"{TID}:{sn}:intro", "s": sn, "a": 1, "a_end": counts[sn], "head": "surah introduction",
                              "text": intro_of[sn].strip(), "page": None})
    for i_, c in enumerate(chunks([L[i] for i in range(len(L)) if in_front[i] and i < index_start]), 1):
        tafs_segs.append({"seg": f"{TID}:front{i_:03d}", "head": "front matter: title, preface, biography, tables of contents",
                          "text": c, "refs": IC.find_refs(c)})
    for i_, c in enumerate(chunks(L[index_start:]), 1):
        tafs_segs.append({"seg": f"{TID}:back{i_:03d}", "head": "back matter: indexes", "text": c, "refs": IC.find_refs(c)})
    got = Counter()
    for g in meal_segs:
        if g["text"].strip():
            for q in range(g["a"], g["a_end"] + 1):
                got[(g["s"], q)] += 1
    miss_all = missing + [f"{sn}:{q}" for sn in counts for q in range(1, counts[sn] + 1)
                          if not got[(sn, q)] and f"{sn}:{q}" not in missing]
    short = {str(sn): f"{sum(1 for q in range(1, counts[sn] + 1) if got[(sn, q)])}/{counts[sn]}" for sn in counts
             if any(not got[(sn, q)] for q in range(1, counts[sn] + 1))}
    covered = 6236 - len(miss_all)
    stats["translation blocks"] = sum(len(v) for v in blocks_of.values())
    stats["aligned cells"] = len(meal_segs)
    stats["mean cell similarity"] = round(sum(sims_all) / max(1, len(sims_all)), 3)
    stats["low-similarity cells (sim < 0.12, more than one verse or block)"] = len(low)
    print(f"surahs {len(start_of)}; blocks {stats['translation blocks']}; cells {len(meal_segs)}; covered {covered}/6236; "
          f"missing {miss_all[:10]}; mean sim {stats['mean cell similarity']}; low {len(low)}; fallbacks {fallback_surahs}; "
          f"issues {len(issues)} {issues[:4]}")
    if a.show and a.show > 0 and a.align:
        mm = {g["seg"]: g for g in meal_segs}
        tt = {g["seg"]: g for g in tafs_segs}
        for g in meal_segs:
            if g["s"] == a.show:
                print(f"{g['s']}:{g['a']}-{g['a_end']} blocks={g['blocks']} sim={g['align']}  {g['text'][:150]!r}")
    if a.dump:
        d_ = Path(a.dump)
        d_.mkdir(parents=True, exist_ok=True)
        for name, segs_ in ((SID, meal_segs), (TID, tafs_segs)):
            (d_ / f"{name}.jsonl").write_text("".join(json.dumps(g, ensure_ascii=False) + "\n" for g in segs_), encoding="utf-8")
    if a.dry:
        return
    ingestion_common = {
        "script": "enrichment/v2/fetch/import_meal_vehbi.py", "from": IC.inputs(SID, ["vehbi-hulasatul-beyan.djvu"]),
        "method": "archive.org OCR text (djvu.txt); surah starts from the headings / page headers; translation blocks "
                  "(parenthesised, after the Arabic noise and «buyuruyor.»); blocks tied to verses by a monotone "
                  "alignment scored by lexical similarity to " + ", ".join(used_refs) + " and by length; surahs "
                  + ", ".join(map(str, pdf_surahs)) + " (digital surah PDFs of archive.org item 2Bakara_201602, same translation "
                  "text, raw/" + PDF_DIR.split("/", 1)[1] + ") are tied by the verse numbers printed in the Arabic instead",
        "from_pdf": {str(p_.relative_to(IC.src_dir(SID))): IC.C.sha256(p_) for p_ in sorted((IC.src_dir(SID) / PDF_DIR).glob("*.pdf"))},
        "verse_count_mismatch": short,
        "missing": [{"ayah": m_, "reason": ("the book prints the besmele in Arabic and gives it no Turkish translation block "
                                           "(its Fâtiha commentary starts at verse 2)" if m_ == "1:1"
                                           else "no translation block found for this verse"),
                     "checked": ["the archive.org djvu.txt OCR of the 16-volume item", "the digital surah PDF 1-fatiha.pdf of "
                                 "archive.org item 2Bakara_201602 (same translation text; also no translation of the besmele)"]}
                    for m_ in miss_all],
        "issues": issues, "alignment_by_pdf_surahs": pdf_surahs, "counts": dict(stats),
        "dropped_sample": dropped, "low_similarity_cells": low, "alignment_fallback_surahs": fallback_surahs,
        "references_used_for_alignment": used_refs,
    }
    IC.write(SID, meal_segs, dict(ingestion_common), {
        "coverage": f"1-114 ({covered}/6236 ayat)", "locator": "ayah", "kind": "meal",
        "edition": "Latin-script edition of the Hülâsatü'l-Beyân, Mümin Çevik ve Ort. Koll. Şti., Beyaz Saray No. 4, Bayazıt, "
                   "İstanbul, «Dördüncü Baskı» (as printed; volume 1 preface dated 16.11.1966; text as OCR'd on archive.org)",
        "notes": "Public domain: author died 1949. The Turkish translation blocks of Vehbi's tafsir (printed in bold in the "
                 "book, in parentheses in the OCR), tied to verses by alignment: each Arabic block of the book is a phrase, "
                 "a verse or several verses and the OCR lost the Arabic and its verse numbers, so the verse groups (a..a_end) "
                 "are inferred, not printed (see align and the low-similarity list in the ingestion record), except in "
                 "surahs 1-6 and 8, tied by the verse numbers of the Arabic in the digital surah PDFs of archive.org item "
                 "2Bakara_201602 (same translation text; 2026-10-09 review: the OCR alignment there was wrong in 15-30% of "
                 "the verses). The besmele (1:1) is not translated in the book (checked in both copies). OCR quality: running text mostly good; page headers inside "
                 "paragraphs and Arabic noise leave stray fragments. The commentary is in TAFSIR-VEHBI."})
    tmeta = json.loads((IC.src_dir(TID) / "source.json").read_text(encoding="utf-8"))
    IC.write(TID, tafs_segs, dict(ingestion_common), {
        "coverage": f"1-114 ({covered}/6236 ayat)", "locator": "ayah", "kind": "tafsir",
        "notes": "Public domain: author died 1949. The commentary of the Hülâsatü'l-Beyân (Latin-script edition, Mümin Çevik, "
                 "«Dördüncü Baskı»; vol. 2 printed Ahmet Sait Matbaası, İstanbul, 1967), OCR from archive.org, whole text kept: "
                 "TAFSIR-VEHBI:S:A is the commentary of the same verse cell as MEAL-VEHBI:S:A (the lead-in sentence, the "
                 "commentary and the page-foot notes of its blocks; the cell tie is inferred, see MEAL-VEHBI), "
                 "TAFSIR-VEHBI:S:intro the surah's introduction, frontNNN / backNNN the volume contents, preface, biography "
                 "and indexes. Only page headers and the Arabic OCR noise are dropped (counted in the ingestion record)."})
    if a.dry and a.show == -1:
        for s in range(1, 115):
            print(s, start_of[s] + 1)
        return


if __name__ == "__main__":
    main()
