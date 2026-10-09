#!/usr/bin/env python3
"""MEAL-OCELIK + TAFSIR-OCELIK: Prof. Dr. Ömer Çelik, Hakk'ın Dâveti, Kur'ân-ı Kerîm Meâli ve Tefsîri (Erkam
Yayınları, İstanbul 1434 / 2013; title page of vol. 1: «İSTANBUL 1434 / 2013», «Baskı Tarihi: İstanbul / 2013»;
5 volumes), from the archive.org OCR text of all five volumes in one file
(raw/acquired-2026-10-09/ocelik-hakkin-daveti-1-5.djvu.txt) and, for gaps only, the five volume files of the second
upload (ocelik-hakkin-daveti-aydin-0N.djvu.txt, uploader «Lami Aydın»; the same OCR, without the page numbers).

Layout: «N. NAME SÛRESİ», the surah's introduction (Mekke/Medine, number of âyets, «Konusu», «Fazileti»), then, for each
passage, a title, the Arabic text (OCR garbage), the basmala line «Rahmân Rahim Allah'ın ismiyle…» (first passage) and the
verses «N. text», EACH VERSE FOLLOWED BY ITS COMMENTARY (paragraphs, word studies, footnotes at the page foot, the
running page numbers). So the meal is one segment per verse and the commentary is tied to that verse.
A verse line «N. text» is accepted when N is the next verse number and its text is the best match, among the lines
printed with that number, for the verse in seven other Turkish meals (a commentary list «1. Fâtihatü'l-Kitâb: …» looks
alike); a monotone choice over the whole surah.

Segments, MEAL-OCELIK: S:A (the verse, section title in `head`; the basmala line in `formula` of verse 1).
TAFSIR-OCELIK: S:intro, S:A#c (commentary after verse A, up to the next verse), S:front.
Dropped and counted: page-number lines, Arabic-column garbage lines (samples kept), repeated surah headings.

  python3 -I enrichment/v2/fetch/import_meal_ocelik.py [--dry] [--dump PREFIX]
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402
from import_meal_akdemir import slash_refs  # noqa: E402,F401
from import_meal_eliacik import noisy  # noqa: E402
from import_meal_zduman import load_refs, stems  # noqa: E402

MEAL, TAFSIR = "MEAL-OCELIK", "TAFSIR-OCELIK"
STEM = "ocelik-hakkin-daveti-1-5"
ALT = [f"ocelik-hakkin-daveti-aydin-0{i}" for i in range(1, 6)]
OD = str.maketrans("OlIiıS", "011155")
N = r"[0-9OlIiıS]{1,3}"
HEADING = re.compile(rf"^\s*({N})\s?[.\-]\s?([^\d]{{2,34}}?)\s*S[ÛÜU]RES[İI]\W*$")
VERSE = re.compile(rf"^[\W_]{{0,3}}({N})(?:\.[.,]?\s*(?=[a-zçğıöşü])|(?:\.[.,]?\s*|\s+(?=[“\"A-ZÇĞİÖŞÜ«]))(?=[A-ZÇĞİÖŞÜÂ\"“'(\[…‘0«]))(\S.*)$")
VERSE0 = re.compile(r"^\s{0,3}[.,;:\-]\s+(?=[A-ZÇĞİÖŞÜÂ\"“'(\[…‘«])(\S.*)$")  # the number was lost by the OCR
PAGENO = re.compile(r"^\s*[\d]{1,4}\s*$")
BASMALA = re.compile(r"^\s*Rahm[âa]n(\s+ve)?\s+Rah[iî]m\s+Allah.{0,3}[ıi]n\s+ismiyle")

META = {
    "kind": "meal", "tradition": "", "language": "tr", "access": "hafiza", "locator": "ayah", "panel": False,
    "author": "Ömer Çelik", "translator": "Ömer Çelik",
    "edition": "Erkam Yayınları, İstanbul 1434 / 2013 (title page of volume 1: «İSTANBUL 1434 / 2013»; «Baskı Tarihi: İstanbul / 2013»; "
               "ISBN 978-9944-83-956-3); 5 volumes",
    "licence": "In copyright (Erkam Yayınları); archive.org upload by a third party; local research use only.",
    "urls": [
        "https://archive.org/details/hakkin-daveti-kuran-i-kerim-meali-ve-tefsiri-1-5-omer-celik",
        "https://archive.org/details/hakkin-daveti-kuran-i-kerim-mealive-tefsiri-02",
    ],
    "provenance": {
        "archive_org_items": {
            "hakkin-daveti-kuran-i-kerim-meali-ve-tefsiri-1-5-omer-celik": "uploader hanifisar@gmail.com; all 5 volumes in one djvu.txt (parsed)",
            "hakkin-daveti-kuran-i-kerim-mealive-tefsiri-02": "uploader gunaydin.selami@gmail.com (creator «Lami Aydın», 2024-07-30); volumes 1-5 as separate files (gap fill only)",
        },
    },
    "notes": "archive.org upload by a third party; in copyright; local research use.",
}
METAS = {MEAL: {**META, "id": MEAL, "title": "Hakk'ın Dâveti: Kur'ân-ı Kerîm Meâli ve Tefsîri (meâl)"},
         TAFSIR: {**META, "id": TAFSIR, "kind": "tafsir", "title": "Hakk'ın Dâveti: Kur'ân-ı Kerîm Meâli ve Tefsîri (tefsir)",
                  "raw_shared": ["../MEAL-OCELIK/raw/acquired-2026-10-09/"]}}


def ensure(sid: str) -> Path:
    d = IC.src_dir(sid)
    if not (d / "source.json").exists():
        d.mkdir(parents=True, exist_ok=True)
        (d / "source.json").write_text(IC.json.dumps(METAS[sid], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return d


def num(s: str) -> int | None:
    t = re.sub(r"\s", "", s).translate(OD)
    return int(t) if t.isdigit() else None


def garbage(x: str) -> bool:
    """A line of the Arabic text or a drawn frame, as the OCR read it: nearly every token is noise."""
    toks = x.split()
    if not toks:
        return False
    bad = sum(1 for t in toks if noisy(t))
    return bad / len(toks) >= 0.8 and len(x) > 3


def read_regions(lines: list[str], counts: dict[int, int], issues: list[str], stats: Counter) -> list[dict]:
    """Surah regions in order: heading line numbers (number == previous + 1)."""
    regs, cur = [], 0
    for i, x in enumerate(lines):
        m = HEADING.match(x)
        if not m:
            continue
        n = num(m.group(1))
        if n == cur + 1:
            regs.append({"s": n, "line": i, "name": m.group(2).strip()})
            cur = n
    for r, nx in zip(regs, regs[1:] + [None]):
        r["end"] = nx["line"] if nx else len(lines)
    if [r["s"] for r in regs] != list(range(1, 115)):
        miss = sorted(set(range(1, 115)) - {r["s"] for r in regs})
        issues.append(f"surah headings found {len(regs)}; missing {miss}")
    return regs


def candidates(lines: list[str], lo: int, hi: int, counts_s: int) -> dict[int, list[dict]]:
    """{verse number: [lines]}; key 0 = lines printed without a (readable) number."""
    out: dict[int, list[dict]] = {}
    for i in range(lo, hi):
        m = VERSE.match(lines[i])
        m0 = None if m else VERSE0.match(lines[i])
        if not m and not m0:
            continue
        n = num(m.group(1)) if m else 0
        if n is None or n > counts_s:
            continue
        para = [(m or m0).group(2 if m else 1)]
        j = i + 1
        while j < hi and lines[j].strip() and len(para) < 8 and not VERSE.match(lines[j]) and not VERSE0.match(lines[j]):
            para.append(lines[j].strip())
            j += 1
        out.setdefault(n, []).append({"line": i, "end": j, "text": re.sub(r"\s+", " ", " ".join(para)).strip(), "numbered": bool(m)})
    return out


def cos(a: set[str], b: set[str], idf: dict[str, float]) -> float:
    inter = sum(idf.get(s, 0.0) for s in a & b)
    na = sum(idf.get(s, 0.0) for s in a)
    nb = sum(idf.get(s, 0.0) for s in b)
    return inter / ((na * nb) ** 0.5) if na > 0 and nb > 0 else 0.0


SENT = re.compile(r"(?<=[.!?…”»])\s+")


def trim(s: int, v: int, text: str, refs, idf) -> tuple[str, str]:
    """The verse's paragraph may run into the commentary (no blank line): keep the sentences that best fit the verse in the
    other meals; the rest goes to the verse's commentary."""
    parts = SENT.split(text)
    if len(parts) < 2:
        return text, ""
    best, bk = -1.0, len(parts)
    for k in range(1, len(parts) + 1):
        pre = " ".join(parts[:k])
        if k < len(parts) and (pre.count("“") > pre.count("”") or pre.count("«") > pre.count("»")):
            continue  # inside a quotation: the verse goes on
        st = stems(pre)
        sc = sum(cos(d.get((s, v), set()), st, idf) for d in refs) / len(refs)
        if sc > best - 0.01:  # a longer prefix stays as long as the fit does not fall
            best, bk = max(best, sc), k
    return " ".join(parts[:bk]), " ".join(parts[bk:])


def choose(s: int, cands: dict[int, list[dict]], n: int, refs, idf) -> dict[int, dict]:
    """One line per verse number, increasing in position, best total fit to the verse in the other meals."""
    def fit(v: int, c: dict) -> float:
        st = stems(c["text"])
        sc = [cos(d.get((s, v), set()), st, idf) for d in refs]
        return sum(sc) / len(sc)
    NONE = -0.05
    prev = [{"pos": -1, "score": 0.0, "pick": None, "back": None}]
    layers = []
    for v in range(1, n + 1):
        opts = [{"c": c, "f": fit(v, c)} for c in cands.get(v, [])]
        if v >= 100:  # «14.» for 114 and 115: the OCR dropped the hundreds digit
            opts += [{"c": c, "f": fit(v, c)} for c in cands.get(v % 100, []) if fit(v, c) >= 0.2]
        opts += [{"c": c, "f": fit(v, c) - 0.02} for c in cands.get(0, []) if fit(v, c) >= 0.06]  # unnumbered lines
        cur = []
        for o in opts:
            best = None
            for p in prev:
                if p["pos"] < o["c"]["line"] and (best is None or p["score"] > best["score"]):
                    best = p
            if best is not None:
                cur.append({"pos": o["c"]["line"], "score": best["score"] + o["f"], "pick": o["c"], "back": best, "f": o["f"]})
        # the verse not found: the best previous state, no position change
        bp = max(prev, key=lambda p: p["score"])
        cur.append({"pos": bp["pos"], "score": bp["score"] + NONE, "pick": None, "back": bp})
        layers.append(cur)
        prev = cur
    st = max(prev, key=lambda p: p["score"])
    picks: dict[int, dict] = {}
    for v in range(n, 0, -1):
        if st["pick"] is not None:
            picks[v] = {**st["pick"], "fit": st["f"]}
        st = st["back"]
    return picks


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--dump")
    a = ap.parse_args()
    counts = IC.ayah_counts()
    dm, dt = ensure(MEAL), ensure(TAFSIR)
    raw = dm / "raw" / "acquired-2026-10-09"
    lines_all = (raw / f"{STEM}.djvu.txt").read_text(encoding="utf-8").split("\n")
    issues: list[str] = []
    stats: Counter = Counter()
    sample: dict[str, list[str]] = {}

    def drop(cat: str, x: str) -> None:
        stats[f"dropped: {cat}"] += 1
        s = sample.setdefault(cat, [])
        if len(s) < 8:
            s.append(x.strip()[:70])

    refs, idf = None, None
    from import_meal_zduman import load_refs as _lr
    refs, idf = _lr(counts)
    regs = read_regions(lines_all, counts, issues, stats)
    lines_alt: list[str] = []
    for stem in ALT:
        lines_alt += (raw / f"{stem}.djvu.txt").read_text(encoding="utf-8").split("\n")
    regs_alt = {r["s"]: r for r in read_regions(lines_alt, counts, [], Counter())}
    msegs, tsegs, missing, tied_all = [], [], [], []
    front = "\n".join(x.rstrip() for x in lines_all[:regs[0]["line"]] if x.strip())
    for r in regs:
        s, n = r["s"], counts[r["s"]]
        # clean copy of the region: page numbers and garbage lines out (counted), blank lines kept
        seg_lines = []
        for x in lines_all[r["line"]:r["end"]]:
            if PAGENO.match(x):
                drop("page numbers", x)
                continue
            if x.strip() and garbage(x) and not VERSE.match(x):
                drop("Arabic-column garbage lines", x)
                continue
            seg_lines.append(x)
        cands = candidates(seg_lines, 0, len(seg_lines), n)
        picks = choose(s, cands, n, refs, idf)
        miss = [v for v in range(1, n + 1) if v not in picks]
        # a verse printed without any readable number: the line between its neighbours that fits it best
        for v in list(miss):
            lo_ = max((picks[u]["end"] for u in picks if u < v), default=0)
            hi_ = min((picks[u]["line"] for u in picks if u > v), default=len(seg_lines))
            best = None
            for i in range(lo_, min(hi_, lo_ + 14)):
                x = seg_lines[i].strip()
                if len(x) < 12 or garbage(x) or PAGENO.match(x):
                    continue
                txt = x
                sc = sum(cos(d.get((s, v), set()), stems(txt), idf) for d in refs) / len(refs)
                if best is None or sc > best[0]:
                    best = (sc, i)
            if best and best[0] >= 0.15:
                i = best[1]
                j = i + 1
                while j < hi_ and seg_lines[j].strip() and j - i < 6 and not VERSE.match(seg_lines[j]):
                    j += 1
                picks[v] = {"line": i, "end": j, "text": re.sub(r"\s+", " ", " ".join(x.strip() for x in seg_lines[i:j])), "fit": best[0], "unnumbered": True}
                stats["verses found without a readable number"] += 1
                miss.remove(v)
        order_tmp = sorted(picks)
        alt_picks: dict[int, dict] = {}
        if miss and s in regs_alt:
            ra = regs_alt[s]
            sl = [x for x in lines_alt[ra["line"]:ra["end"]] if not (PAGENO.match(x) or (x.strip() and garbage(x) and not VERSE.match(x)))]
            pa_ = choose(s, candidates(sl, 0, len(sl), n), n, refs, idf)
            for v in list(miss):
                if v in pa_:
                    alt_picks[v] = {**pa_[v], "alt": True}
                    stats["verses filled from the second upload"] += 1
                    miss.remove(v)
        if miss:
            issues.append(f"{s}: verse lines not found for {miss[:20]}{'…' if len(miss) > 20 else ''}")
            # their text is most likely inside the paragraph of the verse before (the OCR ran lines together): tied there
            gone = set(miss)
            for v in sorted(miss):
                u = max((x for x in list(picks) + list(alt_picks) if x < v), default=None)
                if u is not None and all(w in gone for w in range(u + 1, v + 1)):
                    unit = picks[u] if u in picks else alt_picks[u]
                    unit["a_end"] = max(unit.get("a_end", u), v)
                    unit.setdefault("tied", []).append(f"{s}:{v}")
                    tied_all.append(f"{s}:{v}")
                    miss.remove(v)
        order = sorted(picks)  # (verses filled from the second upload carry no comment: its neighbours' comment lines stay where they were)
        first_line = picks[order[0]]["line"] if order else len(seg_lines)
        # intro: heading to the first verse; the passage title and the basmala line are cut from its tail
        intro = [x.strip() for x in seg_lines[:first_line] if x.strip()]
        titles: dict[int, str] = {}
        formula = None
        # comment of each verse: from the end of its paragraph to the next verse line
        for k, v in enumerate(order):
            p = picks[v]
            nxt = picks[order[k + 1]]["line"] if k + 1 < len(order) else len(seg_lines)
            body = [x.strip() for x in seg_lines[p["end"]:nxt] if x.strip()]
            # the next passage's title and basmala line sit at the end of this comment
            if k + 1 < len(order):
                while body and BASMALA.match(body[-1]):
                    formula_next = body.pop()
                    drop("basmala lines", formula_next)
                    titles.setdefault(order[k + 1], "")
                if body and len(body[-1]) <= 70 and not re.search(r"[.!?:;,]$", body[-1]) and not re.match(r"^\d", body[-1]) and sum(1 for x in body if True) > 1:
                    titles[order[k + 1]] = body.pop()
            p["comment"] = body
        # intro tail
        while intro and BASMALA.match(intro[-1]):
            formula = intro.pop()
            drop("basmala lines", formula)
        if intro and len(intro[-1]) <= 70 and order and not re.search(r"[.!?:;,]$", intro[-1]) and len(intro) > 2:
            titles[order[0]] = intro.pop()
        tsegs.append({"seg": f"{TAFSIR}:{s}:intro", "s": s, "a": 1, "a_end": n, "head": f"{s}. {r['name']} SÛRESİ: introduction",
                      "text": " ".join(intro)})
        for v in order:
            p = picks[v]
            p["text"], spill = trim(s, v, p["text"], refs, idf) if not p.get("tied") else (p["text"], "")
            if spill:
                p["comment"] = [spill] + p["comment"]
                stats["verse paragraphs cut where the commentary begins (no blank line)"] += 1
        # blocks: verses printed one after the other; the commentary after the block belongs to all its verses
        blocks, cur_b = [], []
        for v in order:
            cur_b.append(v)
            if picks[v]["comment"]:
                blocks.append(cur_b)
                cur_b = []
        if cur_b:
            blocks.append(cur_b)
        for v in sorted(set(order) | set(alt_picks)):
            p = picks[v] if v in picks else alt_picks[v]
            g = {"seg": f"{MEAL}:{s}:{v}", "s": s, "a": v, "a_end": p.get("a_end", v), "text": p["text"]}
            if p.get("tied"):
                g["verses_without_own_line"] = p["tied"]
            if titles.get(v):
                tk = titles[v].split()
                if sum(1 for w in tk if noisy(w)) / len(tk) <= 0.3 and len(titles[v]) >= 6:
                    g["head"] = titles[v]
                else:
                    drop("garbage lines taken for a passage title", titles[v])
            if p.get("unnumbered"):
                g["number_unreadable_in_ocr"] = True
            if p.get("alt"):
                g["from_second_upload"] = True
            if order and v == order[0] and formula:
                g["formula"] = formula
            if p.get("fit", 1) < 0.08:
                g["low_fit_to_reference_meals"] = round(p["fit"], 3)
                stats["verses with a low fit to the reference meals"] += 1
            msegs.append(g)
        for b in blocks:
            body = picks[b[-1]]["comment"]
            if body:
                tsegs.append({"seg": f"{TAFSIR}:{s}:{b[0]}#c", "s": s, "a": b[0], "a_end": b[-1], "text": "\n".join(body),
                              **({"group": f"{b[0]}-{b[-1]} (the commentary printed after these verses)"} if len(b) > 1 else {})})
        missing += [f"{s}:{v}" for v in miss]
    for g in tsegs:
        rf = list(dict.fromkeys(slash_refs(g["text"]) + IC.find_refs(g["text"])))  # «(A'râf 7/156)», «7:156»
        if rf:
            g["refs"] = rf
    tsegs.append({"seg": f"{TAFSIR}:front", "head": "title pages, preface and front matter", "text": front})
    got = Counter()
    for g in msegs:
        got[g["s"]] += g["a_end"] - g["a"] + 1
    short = {s: (got[s], counts[s]) for s in counts if got[s] != counts[s]}
    print(f"surahs {len(regs)}; verses {sum(g['a_end'] - g['a'] + 1 for g in msegs)}/6236 ({len(msegs)} segments); tied {tied_all}; missing {len(missing)}; surahs not matching {len(short)} "
          f"{dict(list(short.items())[:20])}; issues {len(issues)} {issues[:10]}")
    print(dict(stats))
    if a.dump:
        for nm, sg in (("meal", msegs), ("tafsir", tsegs)):
            Path(f"{a.dump}{nm}.jsonl").write_text("".join(IC.json.dumps(g, ensure_ascii=False) + "\n" for g in sg))
    if a.dry:
        print("missing:", missing[:80])
        return
    common = {"script": "enrichment/v2/fetch/import_meal_ocelik.py", "from": IC.inputs(MEAL, [STEM] + ALT),
              "method": "archive.org OCR text; verse lines «N. text» chosen per surah as the best monotone fit to the verse in "
                        "seven other meals; each verse's commentary = the lines up to the next verse",
              "verse_count_mismatch": {str(k): v for k, v in short.items()}, "missing": missing, "number_lost_in_ocr_text_tied_to_previous_unit": tied_all, "issues": issues,
              "counts": dict(stats), "dropped_sample": sample}
    old = IC.json.loads((dm / "source.json").read_text())
    IC.write(MEAL, msegs, common, {"coverage": f"1-114 ({sum(g['a_end'] - g['a'] + 1 for g in msegs)}/6236 ayat)", "notes": old["notes"] + (
        f" Ingested {IC._dt.date.today().isoformat()} (fetch/import_meal_ocelik.py) from the OCR text of the five volumes: {sum(g['a_end'] - g['a'] + 1 for g in msegs)}/6236 verses ({len(tied_all)} of them tied into the verse before: their number and line are lost in the OCR)"
        + (f"; not found: {', '.join(missing[:40])}" if missing else "") + ". OCR noise from the Arabic text is dropped line by line "
        "(counted in ingestion.counts, samples kept); inline OCR noise may remain.")})
    oldt = IC.json.loads((dt / "source.json").read_text())
    IC.write(TAFSIR, tsegs, common, {"coverage": "1-114 (commentary tied to the verse it follows)", "notes": oldt["notes"] + (
        f" Ingested {IC._dt.date.today().isoformat()} (fetch/import_meal_ocelik.py): the commentary after each verse, the surah introductions.")})


if __name__ == "__main__":
    main()
