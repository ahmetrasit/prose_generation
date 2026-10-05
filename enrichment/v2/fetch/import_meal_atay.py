#!/usr/bin/env python3
"""MEAL-ATAY: Hüseyin Atay, Kur'an-ı Kerim Türkçe Çeviri (2013, his solo translation), from the user's download
(raw/acquired-2026-10-05/atay-kuran-turkce-ceviri-2013.pdf, 654 PDF pages, and the archive's OCR text of it).

The OCR text keeps the words apart (the PDF text layer breaks them: «Alla h») and prints one paragraph per verse,
without verse numbers (they stand in the margin), sometimes two verses in one paragraph or one verse over two. So
the paragraphs of each surah are aligned to its verses by dynamic programming: a paragraph (or two, or three) is
matched with a verse (or up to four) by the character 4-grams it shares with three other Turkish meals of the same
verses (MEAL-DIB1961, Atay's own 1961 Diyanet translation with Kutluay; MEAL-TDV; MEAL-KURANYOLU), the best of the
three counting; where the OCR keeps a verse number at a paragraph's start, it is used as a strong hint.

Also from the book: «2. DÜVE/BAKARA BÖLÜMÜ» headings and the surah's note («Medine döneminde inmiştir. 286
ayettir.») -> S:intro; the page-foot cross-references «2/25 , 3/133 , 9/111 …» (the verse, then its parallels) ->
`parallels` on the verse; the subject index (Dizin) -> MEAL-ATAY:dizin, with refs. The scan repeats the pages of
surahs 92–114 and the index after the index: that second copy is compared with the first and left out (counted,
with its similarity). Dropped and counted: running headers and page numbers.

  python3 -B enrichment/v2/fetch/import_meal_atay.py [--dry]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402

SID, STEM = "MEAL-ATAY", "atay-kuran-turkce-ceviri-2013"
REFS = ["MEAL-DIB1961", "MEAL-TDV", "MEAL-KURANYOLU"]
HEAD = re.compile(r"^\s*(\S{1,4}?)\s*[.,-]?\s+(.*B\s?Ö\s?L\s?Ü\s?M\s?Ü)\s*$")
FOOT = re.compile(r"^\s*(\d{1,3})\s?/\s?(\d{1,3})\s?(?:[,.]|$)")
RUNNING = re.compile(r"(C[üu]z\s*\d.*B[öo]l[üu]m|B[öo]l[üu]m\s*\d.*C[üu]z|^\s*[0-9IVXLC]{1,6}\s*$|^\s*\d{1,3}\s*$)")
STEPS = [(1, 1, 0.0), (1, 2, 0.04), (2, 1, 0.04), (1, 3, 0.08), (3, 1, 0.08), (1, 4, 0.12), (2, 2, 0.06)]


def grams(t: str) -> set[str]:
    t = re.sub(r"[^a-zçğıöşüâîû]", "", t.lower().replace("İ", "i").replace("I", "ı"))
    return {t[i:i + 4] for i in range(len(t) - 3)}


def dice(a: set, b: set) -> float:
    return 2 * len(a & b) / (len(a) + len(b)) if a and b else 0.0


def ref_verses(counts: dict[int, int]) -> dict[str, dict[tuple[int, int], set]]:
    out = {}
    for sid in REFS:
        d: dict[tuple[int, int], set] = {}
        for line in (IC.src_dir(sid) / "segments.jsonl").open(encoding="utf-8"):
            g = json.loads(line)
            if g.get("s") and g.get("a"):
                gs = grams(g.get("text") or "")
                for a in range(g["a"], (g.get("a_end") or g["a"]) + 1):
                    d[(g["s"], a)] = gs
        out[sid] = d
    return out


def align(paras: list[dict], vlist: list[tuple[int, int]], refs: dict) -> list[tuple[int, int, int, int, float]]:
    """(first paragraph, last paragraph, first verse index, last verse index (1-based in vlist), score) for the best
    monotone alignment of the paragraphs with the verse list (one surah, or two when a heading was lost)."""
    m, n = len(paras), len(vlist)
    pg = [p["grams"] for p in paras]
    vg = [[refs[r].get(sa, set()) for r in REFS] for sa in vlist]
    NEG = -1e9
    best = [[NEG] * (n + 1) for _ in range(m + 1)]
    back = [[None] * (n + 1) for _ in range(m + 1)]
    best[0][0] = 0.0
    band = max(40, abs(m - n) + 20)
    for i in range(m + 1):
        for j in range(n + 1):
            if best[i][j] == NEG or abs(i - j) > band:
                continue
            for da, db, pen in STEPS:
                i2, j2 = i + da, j + db
                if i2 > m or j2 > n:
                    continue
                pset = set().union(*pg[i:i2])
                sc = max(dice(pset, set().union(*(vg[k][r] for k in range(j, j2)))) for r in range(len(REFS)))
                hint = paras[i]["hint"]
                if hint is not None:
                    sc += 0.5 if hint == vlist[j][1] else -0.3
                v = best[i][j] + sc - pen
                if v > best[i2][j2]:
                    best[i2][j2], back[i2][j2] = v, (i, j, sc)
    if best[m][n] == NEG:
        return []
    out, i, j = [], m, n
    while i or j:
        pi, pj, sc = back[i][j]
        out.append((pi, i - 1, pj + 1, j, sc))
        i, j = pi, pj
    return out[::-1]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--dump")
    a = ap.parse_args()
    counts = IC.ayah_counts()
    stats: Counter = Counter()
    path = next(IC.src_dir(SID).glob(f"raw/acquired-*/{STEM}.ocr.txt"))
    raw = path.read_text(encoding="utf-8")
    raw = re.sub(r"¬\s*\n\s*", "", raw)  # line-end hyphenation marked «¬»
    lines = raw.split("\n")
    # blocks: front matter, surah k, index; the second copy of 92–114 and the index after the first index is set aside
    surah, mode = 0, "front"
    blocks: dict[int, list[str]] = {}
    covers: dict[int, list[int]] = {}
    front, dizin, dup = [], [], []
    feet: list[tuple[int, int, list[str]]] = []
    for ln in lines:
        x = ln.strip()
        h = HEAD.match(ln)
        if h:
            t = h.group(1).replace("L", "1").replace("l", "1").replace("O", "0").replace("o", "0")
            k = int(t) if t.isdigit() else surah + 1
            if mode == "dizin" or (surah and k <= surah):
                mode = "dup"
            elif mode != "dup":
                if k != surah + 1:
                    stats[f"headings {surah + 1}–{k - 1} not found"] += 1
                    covers[surah] = list(range(surah, k))  # the lost surahs' text is in the block before
                surah, mode = k, "surah"
                blocks[surah] = []
                covers[surah] = [surah]
                continue
        if mode == "dup":
            dup.append(ln)
            continue
        if x == "Dizin" and surah == 114:
            mode = "dizin"
            continue
        if mode == "dizin":
            dizin.append(ln)
            continue
        if mode == "front":
            front.append(ln)
            continue
        if RUNNING.search(x) and len(x) < 70:
            stats["running headers and page numbers dropped"] += 1
            continue
        f = FOOT.match(x)
        if f and re.fullmatch(r"[\d/,\s.\-]+", x):
            refs = re.findall(r"(\d{1,3})\s?/\s?(\d{1,3})", x)
            feet.append((int(f.group(1)), int(f.group(2)), [f"{s}:{v}" for s, v in refs[1:] if IC.valid(int(s), int(v))]))
            stats["cross-reference lines"] += 1
            continue
        blocks[surah].append(ln)
    refs = ref_verses(counts)
    segs, uncertain, issues = [], [], []
    for s in range(1, 115):
        if s not in blocks:
            issues.append(f"surah {s}: no heading found; aligned inside the block of surah {max(k for k in blocks if k < s)}")
            continue
        text = "\n".join(blocks[s])
        paras = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
        intro = []
        # the surah's note and the basmala (verse 1 only in S1) open the block
        while paras and (re.search(r"(döneminde|Mekke'de|Medine'de).{0,40}inmiştir|ayettir\.", paras[0])
                         or (s != 1 and re.match(r"Acıyan.{0,30}Adına", paras[0]))):
            first = paras.pop(0)
            m = re.match(r"(.*?Adına)\s+(.*)$", first)
            if m and s != 1 and m.group(2):
                intro.append(m.group(1))
                paras.insert(0, m.group(2))
            else:
                intro.append(first)
        if s != 1 and paras and re.match(r"Acıyan.{0,30}Adına\s*$", paras[0]):
            intro.append(paras.pop(0))
        items = []
        for p in paras:
            mh = re.match(r"^(\d{1,3})\s+(\S.*)$", p)
            hint = int(mh.group(1)) if mh and 1 <= int(mh.group(1)) <= counts[s] else None
            body = mh.group(2) if hint else p
            items.append({"text": body, "hint": hint, "grams": grams(body)})
        segs.append({"seg": f"{SID}:{s}:intro", "s": s, "a": 1, "a_end": counts[s], "head": "surah heading and note",
                     "text": "\n".join(intro)})
        vlist = [(k, v) for k in covers[s] for v in range(1, counts[k] + 1)]
        path_ = align(items, vlist, refs) if items else []
        if not path_:
            issues.append(f"surah {s}: no alignment ({len(items)} paragraphs, {len(vlist)} verses); kept as one unit")
            segs.append({"seg": f"{SID}:{s}:1", "s": s, "a": 1, "a_end": counts[s], "aligned": False,
                         "text": "\n".join(i["text"] for i in items)})
            continue
        for p0, p1, i0, i1, sc in path_:
            (s0, v0), (s1, v1) = vlist[i0 - 1], vlist[i1 - 1]
            if s1 != s0:  # a unit across a lost heading: keep it on the first surah's last verse
                v1 = counts[s0]
                issues.append(f"{s0}:{v0} unit runs into surah {s1} (lost heading); tied to {s0}:{v0}-{v1}")
            g = {"seg": f"{SID}:{s0}:{v0}", "s": s0, "a": v0, "a_end": v1,
                 "text": " ".join(items[k]["text"] for k in range(p0, p1 + 1)), "align_score": round(sc, 3)}
            if p1 > p0:
                stats["verses printed over two or more paragraphs"] += 1
            if v1 > v0:
                stats["paragraphs holding two or more verses"] += 1
            if sc < 0.15:
                uncertain.append(f"{s}:{v0}" + (f"-{v1}" if v1 > v0 else "") + f" ({sc:.2f})")
                g["align_uncertain"] = True
            segs.append(g)
        stats["paragraphs"] += len(items)
    # parallels from the page feet
    by = {(g["s"], a): g for g in segs if g.get("s") and not g["seg"].endswith("intro")
          for a in range(g["a"], g["a_end"] + 1)}
    for s, v, par in feet:
        g = by.get((s, v))
        if g is None:
            stats["cross-reference lines whose verse is not in the text"] += 1
            continue
        g.setdefault("parallels", [])
        g["parallels"] += [f"{s}:{v} -> " + ", ".join(par)] if g["a_end"] > g["a"] else par
    for g in segs:
        if g.get("parallels") and all("->" not in p for p in g["parallels"]):
            g["parallels"] = sorted(set(g["parallels"]), key=lambda r: tuple(map(int, r.split(":"))))
    dz = "\n".join(x for x in dizin if x.strip())
    segs.append({"seg": f"{SID}:dizin", "head": "subject index (Dizin)", "text": dz,
                 "refs": sorted({f"{s}:{v}" for s, v in re.findall(r"(?<![\d/])(\d{1,3})\s?/\s?(\d{1,3})", dz)
                                 if IC.valid(int(s), int(v))}, key=lambda r: tuple(map(int, r.split(":"))))})
    segs.append({"seg": f"{SID}:front", "head": "front matter (title, contents, preface)",
                 "text": "\n".join(x for x in front if x.strip())})
    # the duplicate copy: how close is it to the first?
    dup_text = re.sub(r"\s+", " ", "\n".join(dup))
    first_tail = re.sub(r"\s+", " ", " ".join(g["text"] for g in segs if g.get("s") and g["s"] >= 92) + " " + dz)
    sim = dice(grams(dup_text), grams(first_tail))
    stats["duplicate scan of 92–114 and the index: characters (kept as MEAL-ATAY:duplicate-scan)"] = len(dup_text)
    segs.append({"seg": f"{SID}:duplicate-scan", "head": "the scan's second copy of surahs 92–114 and the index "
                 f"(similarity to the first copy {sim:.2f}; its OCR keeps verse numbers)", "duplicate": True,
                 "text": "\n".join(x for x in dup if x.strip())})
    covered = Counter()
    for g in segs:
        if g.get("s") and not g["seg"].endswith("intro"):
            covered[g["s"]] += g["a_end"] - g["a"] + 1
    print(f"verse units {sum(1 for g in segs if g.get('s') and not g['seg'].endswith('intro'))}; verses covered "
          f"{sum(covered.values())}/6236; uncertain alignments {len(uncertain)} {uncertain[:12]}")
    print(f"{dict(stats)}; duplicate-copy similarity to the first copy {sim:.2f}; issues {issues[:6]}")
    if a.dry:
        if a.dump:
            Path(a.dump).write_text("".join(json.dumps(g, ensure_ascii=False) + "\n" for g in segs))
        return
    old = json.loads((IC.src_dir(SID) / "source.json").read_text())
    IC.write(SID, segs, {
        "script": "enrichment/v2/fetch/import_meal_atay.py", "from": IC.inputs(SID, [STEM]),
        "method": "archive OCR text; paragraphs aligned to verses by dynamic programming on character 4-grams "
                  f"shared with {', '.join(REFS)} (best of three); OCR verse numbers used as hints",
        "uncertain_alignments": uncertain, "counts": dict(stats), "issues": issues,
        "duplicate_copy_similarity": round(sim, 3),
    }, {"coverage": f"1-114 ({sum(covered.values())}/6236 ayat, aligned)", "locator": "ayah", "kind": "meal",
        "notes": "Ingested 2026-10-05 from the user's download (fetch/import_meal_atay.py). The verse numbers are "
                 "not in the OCR text: verses are aligned (align_score per unit; align_uncertain marks a weak "
                 "match). `parallels`: the book's own cross-references at the page foot. Pointer note before "
                 "ingestion: " + (old.get("notes") or "")})


if __name__ == "__main__":
    main()
