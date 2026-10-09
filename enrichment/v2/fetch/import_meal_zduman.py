#!/usr/bin/env python3
"""MEAL-ZDUMAN + TAFSIR-ZDUMAN: Prof. Dr. M. Zeki Duman, Beyânu'l-Hak (Kur'an-ı Kerim'in Nüzul Sırasına Göre Tefsiri),
Ankara 2016 (3 volumes), from the archive.org OCR text of the «Only Text» edition of the 3 volumes
(raw/acquired-2026-10-09/zduman-beyanu-l-hak-only-text.djvu.txt); the scan's own OCR
(zduman-beyanu-l-hak-orjinal.djvu.txt, 2016 «orjinal», 227 MB scan) is kept as raw but not parsed: its meal columns
are Arabic-column garbage, only the commentary is readable and it has the same text as the Only Text file.

The book is in revelation order (Fâtiha is placed 5th, Alak 1st, Nasr last); each surah opens with a heading
«96/1- Alak Suresi» (mushaf/revelation number; a few are printed the other way round), an introduction, and then
PASSAGES (pasaj): the meal of a passage as one quoted paragraph («Kovulmuş Şeytandan … Başlarım» in front of the
first one), a line «Tefsir», and the passage's numbered notes «1- …», «2- …». The meal paragraphs carry NO verse
numbers in this edition. Every passage is tied to its mushaf verses by aligning its words to the surah's verses in
seven other Turkish meals (monotone partition of the surah into its passages, best total fit, first passage from
verse 1, last up to the last verse); the boundaries whose fit is weak are listed in the ingestion record
(uncertain_boundaries). Fâtiha counts the basmala as its verse 1 (the book says «Besmele ile birlikte yedi ayet»).

Segments, MEAL-ZDUMAN: S:A (the passage's meal, a..a_end = its verses; the formula line in `formula`).
TAFSIR-ZDUMAN: S:intro (surah heading and introduction), S:A#tN (note N of the passage, tied to its verses),
S:A#pre (text of the passage's commentary before its first numbered note), S:A#fn (page footnotes printed in the
passage's region, markers not placed), S:front (title, biography, the lists, the Giriş essay).
Dropped and counted: page-number lines, running headers, the TOC lines in the front matter are kept as front matter.

  python3 -I enrichment/v2/fetch/import_meal_zduman.py [--dry] [--dump PREFIX]
"""
from __future__ import annotations

import argparse
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402
from import_meal_akdemir import slash_refs  # noqa: E402  («Bakara: 2/62; Maide: 5/69»)

MEAL, TAFSIR = "MEAL-ZDUMAN", "TAFSIR-ZDUMAN"
STEM = "zduman-beyanu-l-hak-only-text"
RAW2 = "zduman-beyanu-l-hak-orjinal"
REFS = ["DIB", "BULAC", "ATAY", "CAKIR", "HAYRAT", "ATES", "ALIMIHR"]
OD = str.maketrans("OlIS", "0115")
HEAD = re.compile(r"^\s*([0-9OlIS]{1,3})\s?/\s?([0-9OlIS]{1,3})\s?[-–—.:]?\s*(\S.{0,45})?$")
ITEM = re.compile(r"^\s*([0-9OlI]{1,2})\s?[-–—]\s+(\S.*)$")
LABEL = re.compile(r"^Kovulmu[sş] [SŞ]eytandan.*Ba[sş]lar[ıi]m\.*\s*$")
META_COMMON = {
    "kind": "meal", "tradition": "", "language": "tr", "access": "hafiza", "locator": "ayah", "panel": False,
    "author": "M. Zeki Duman", "translator": "M. Zeki Duman",
    "edition": "Beyânu'l-Hak (Kur'an-ı Kerim'in Nüzul Sırasına Göre Tefsiri), Prof. Dr. M. Zeki Duman, Ankara 2016 "
               "(title page: «ANKARA 2016»; earlier printings Fecr Yayınevi, Ankara, 1st 2006, 2nd 2008); 3 volumes",
    "licence": "In copyright; archive.org upload by a third party; local research use only.",
    "urls": [
        "https://archive.org/details/zeki-duman-beyanu-i-hak-orjinal-3-cilt-2016-bsk",
        "https://archive.org/details/beyanul-hak-kuran-i-kerimin-nuzul-sirasina-gore-tefsiri-1-2-m.-zeki-duman",
    ],
    "provenance": {
        "archive_org_items": {
            "zeki-duman-beyanu-i-hak-orjinal-3-cilt-2016-bsk": "uploader soydemir2005@hotmail.com; files: Only Text (3 Cilt) djvu.txt (parsed), Orjinal 3 Cilt 2016 djvu.txt (raw only)",
            "beyanul-hak-kuran-i-kerimin-nuzul-sirasina-gore-tefsiri-1-2-m.-zeki-duman": "uploader hanifisar@gmail.com; 1-2 cilt, same text as the Orjinal file (not used)",
        },
    },
}
META = {
    MEAL: {**META_COMMON, "id": MEAL, "title": "Beyânu'l-Hak: Kur'an-ı Kerim'in Nüzul Sırasına Göre Tefsiri (meal)",
           "notes": "archive.org upload by a third party; in copyright; local research use."},
    TAFSIR: {**META_COMMON, "id": TAFSIR, "kind": "tafsir", "title": "Beyânu'l-Hak: Kur'an-ı Kerim'in Nüzul Sırasına Göre Tefsiri (tefsir)",
             "raw_shared": ["../MEAL-ZDUMAN/raw/acquired-2026-10-09/"],
             "notes": "archive.org upload by a third party; in copyright; local research use."},
}


def ensure(sid: str) -> Path:
    d = IC.src_dir(sid)
    if not (d / "source.json").exists():
        d.mkdir(parents=True, exist_ok=True)
        (d / "source.json").write_text(IC.json.dumps(META[sid], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return d


def num(s: str) -> int | None:
    t = re.sub(r"\s", "", s).translate(OD)
    return int(t) if t.isdigit() else None


# ---------------------------------------------------------------------------------------------- reading the book


def paragraphs(lines: list[str], lo: int, hi: int) -> list[dict]:
    """Blocks of consecutive non-blank lines in lines[lo:hi]."""
    out, cur = [], None
    for i in range(lo, hi):
        if lines[i].strip() == "Tefsir" or LABEL.match(lines[i].strip()):  # their own blocks, blank line or not
            if cur is not None:
                cur["hi"] = i
                out.append(cur)
                cur = None
            out.append({"lo": i, "hi": i + 1, "lines": [lines[i].strip()]})
        elif lines[i].strip():
            if cur is None:
                cur = {"lo": i, "lines": []}
            cur["lines"].append(lines[i].strip())
        elif cur is not None:
            cur["hi"] = i
            out.append(cur)
            cur = None
    if cur is not None:
        cur["hi"] = hi
        out.append(cur)
    return out


def is_footnote(p: dict) -> bool:
    """A page footnote block: its first token is a marker (≤4 characters, no lowercase letter, not «12-»), then text."""
    first = p["lines"][0].split(None, 1)
    if len(first) < 2:
        return False
    t = first[0]
    if len(t) > 4 or re.search(r"[a-zçğıöşü]", t) or t.endswith(("-", "–", "—")) or t in ("Tefsir",):
        return False
    return bool(re.search(r"\d+\s?[/:]\s?\d+|Bkz|s\.\s?\d|\bC\.|cilt|Sahih|Buhari|Müslim|Tirmizi|İbn|Taberi|Râzi|Razi", p["lines"][0] + " ".join(p["lines"][1:2]))) or len(p["lines"]) <= 2


def find_regions(lines: list[str], counts: dict[int, int], issues: list[str]) -> list[dict]:
    cands = []
    for i, x in enumerate(lines):
        m = HEAD.match(x)
        if not m:
            continue
        nxt = " ".join([y for y in lines[i + 1:i + 12] if y.strip()][:5])
        if not re.search(r"(?i)\bsure|Mekk|Meden", nxt) or not re.search(r"Peygamber|ayet|Mekk|Meden", nxt):
            continue
        a, b = num(m.group(1)), num(m.group(2))
        g = re.search(r"(?:Ebu|Ebü|Bekir)[^.]{0,90}?göre\s+([0-9OlIS]{1,3})\.?", nxt)
        cands.append({"line": i, "a": a, "b": b, "name": (m.group(3) or "").strip(), "g": num(g.group(1)) if g else None})
    pick: dict[int, dict] = {}
    for c in cands:
        if c["g"] in (c["a"], c["b"]) and c["g"] not in pick:
            c["mushaf"] = c["g"]
            pick[c["g"]] = c
    missing = set(range(1, 115)) - set(pick)
    for c in cands:
        if "mushaf" in c:
            continue
        opts = [v for v in {c["a"], c["b"], c["g"]} if v in missing]
        if len(opts) == 1:
            c["mushaf"] = opts[0]
            pick[opts[0]] = c
            missing.discard(opts[0])
        else:
            issues.append(f"heading at line {c['line'] + 1} ({c['a']}/{c['b']} {c['name']}): surah number not resolved {opts}")
    regs = sorted((c for c in cands if "mushaf" in c), key=lambda c: c["line"])
    for r, nx in zip(regs, regs[1:] + [None]):
        r["end"] = nx["line"] if nx else len(lines)
    if len(regs) != 114 or set(c["mushaf"] for c in regs) != set(range(1, 115)):
        issues.append(f"surah headings found {len(regs)}; missing {sorted(set(range(1, 115)) - set(c['mushaf'] for c in regs))}")
    return regs


def split_region(lines: list[str], r: dict, issues: list[str], stats: Counter) -> dict:
    """The passages of one surah: [{'meal': text, 'formula', 'items': [(n, text)], 'pre', 'fn': [...]}]."""
    paras = paragraphs(lines, r["line"], r["end"])
    tef = []  # index of the paragraph «Tefsir» that opens a passage (the next line is the note «1-»)
    for k, p in enumerate(paras):
        if p["lines"][0] == "Tefsir":
            body = p["lines"][1:] or (paras[k + 1]["lines"] if k + 1 < len(paras) else [])
            if body and re.match(r"^\s*[1lI]\s?[-–—.]", body[0]):
                tef.append(k)
    passages = []
    for n, k in enumerate(tef):
        j = k - 1
        fn_before, stack = [], []
        while j > 0 and is_footnote(paras[j]) and len(fn_before) < 6:
            fn_before.append(paras[j])
            j -= 1
        stack.insert(0, paras[j])
        # a meal that starts «“»; when the paragraph before «Tefsir» does not, the meal was cut by a page: go up
        guard = 0
        while not stack[0]["lines"][0].lstrip().startswith(("“", '"', "«")) and j > 0 and guard < 4:
            j -= 1
            if paras[j]["lines"][0] == "Tefsir":
                j += 1
                break
            if is_footnote(paras[j]):
                fn_before.append(paras[j])
                continue
            guard += 1
            stack.insert(0, paras[j])
        if not stack[0]["lines"][0].lstrip().startswith(("“", '"', "«")):
            issues.append(f"surah {r['mushaf']}: passage {n + 1}: the meal paragraph does not start with a quote (line {stack[0]['lo'] + 1}); its beginning may be misfiled in the previous commentary")
        formula = None
        flag = not stack[0]["lines"][0].lstrip().startswith(("“", '"', "«"))
        if j > 0 and LABEL.match(paras[j - 1]["lines"][0]):
            formula = paras[j - 1]["lines"][0].strip().rstrip(".")
            j -= 1
        passages.append({"flag": flag, "tef": k, "meal_lo": j, "meal_paras": stack, "formula": formula, "fn_before": fn_before})
    for pa in passages:
        ls = [x for p in pa["meal_paras"] for x in p["lines"]]
        # a meal run into the paragraph of the last note (no blank line between): cut after that note's last line
        # that ends a sentence, where a quoted line begins
        last_item = max((i for i, x in enumerate(ls) if ITEM.match(x)), default=None)
        if last_item is not None:
            for i in range(last_item + 1, len(ls)):
                if ls[i].lstrip().startswith(("“", '"', "«")) and re.search(r"[.!?:;,”\"»][\s*\"”“'’\d]*$", ls[i - 1]):
                    pa["spill"] = ls[:i]
                    ls = ls[i:]
                    stats["meal cut off from a note running into it (no blank line)"] += 1
                    break
        pa["meal"] = " ".join(ls)
    # regions of text
    first = passages[0]["meal_lo"] if passages else len(paras)
    intro_paras = paras[:first]
    for n, pa in enumerate(passages):
        end = passages[n + 1]["meal_lo"] if n + 1 < len(passages) else len(paras)
        pa["comm"] = paras[pa["tef"]:end]
    for n, pa in enumerate(passages):
        if pa.get("spill"):
            (passages[n - 1]["comm"] if n else intro_paras).append({"lo": pa["meal_paras"][0]["lo"], "hi": 0, "lines": pa["spill"]})
    out = {"intro": intro_paras, "passages": passages}
    return out


def comm_items(comm: list[dict], issues: list[str], where: str, stats: Counter) -> tuple[str, list[tuple[int, str]], list[str]]:
    """A passage's commentary -> (text before note 1, [(n, text)], footnote lines)."""
    pre, items, fns = [], [], []
    last, cur = 0, None
    for p in comm:
        if is_footnote(p) and not (p["lines"][0] == "Tefsir"):
            fns.extend(p["lines"])
            continue
        for x in p["lines"]:
            if x == "Tefsir":
                stats["«Tefsir» lines inside a commentary (page layout)"] += 1
                continue
            m = ITEM.match(x)
            n = num(m.group(1)) if m else None
            if m and n == last + 1:
                cur = [m.group(2)]
                items.append((n, cur))
                last = n
            elif cur is not None:
                cur.append(x)
            else:
                pre.append(x)
    return " ".join(pre).strip(), [(n, " ".join(t)) for n, t in items], fns


# ---------------------------------------------------------------------------------------------- aligning passages


def tokens(text: str) -> list[str]:
    t = text.lower().replace("İ", "i").replace("I", "ı").translate(str.maketrans("âîûÂÎÛ", "aiuaiu"))
    return re.findall(r"[a-zçğıöşü]{3,}", t.replace("i̇", "i"))


def stems(text: str) -> set[str]:
    return {w[:5] for w in tokens(text)}


LAMBDA = 6.0  # weight of the length prior (log-ratio of the passage's words to the words of its verses)


LEN: dict = {}


def load_refs(counts: dict[int, int]):
    refs = []
    for m in REFS:
        p = IC.src_dir(f"MEAL-{m}") / "segments.jsonl"
        d: dict[tuple[int, int], set[str]] = {}
        for line in p.open(encoding="utf-8"):
            g = IC.json.loads(line)
            if g.get("s") and g.get("a") and "#" not in g["seg"] and not g["seg"].endswith(("intro", "notes")):
                st = stems(g.get("text") or "")
                for a in range(g["a"], (g.get("a_end") or g["a"]) + 1):
                    d.setdefault((g["s"], a), set()).update(st)
        refs.append(d)
        for g in (IC.json.loads(l) for l in p.open(encoding="utf-8")):
            if g.get("s") and g.get("a") and "#" not in g["seg"] and not g["seg"].endswith(("intro", "notes")):
                k = (g["s"], g["a"])
                n = len(tokens(g.get("text") or "")) / ((g.get("a_end") or g["a"]) - g["a"] + 1)
                for a in range(g["a"], (g.get("a_end") or g["a"]) + 1):
                    LEN[(m, g["s"], a)] = n
    df: Counter = Counter()
    for d in refs:
        for st in d.values():
            df.update(st)
    nverse = sum(counts.values())
    idf = {s: math.log(nverse * len(refs) / (1 + c)) for s, c in df.items()}
    return refs, idf


def align(surah: int, n: int, passages: list[str], refs, idf, issues: list[str], unc: list[str]) -> list[tuple[int, int]]:
    """Monotone partition of verses 1..n into len(passages) contiguous parts, best total fit."""
    K = len(passages)
    if K == 1:
        return [(1, n)]
    if K > n:
        issues.append(f"surah {surah}: {K} passages for {n} verses: partition impossible; every passage tied to the whole surah")
        return [(1, n)] * K
    P = [stems(t) for t in passages]
    S = [[0.0] * (n + 1) for _ in range(K)]
    for v in range(1, n + 1):
        for k in range(K):
            tot = 0.0
            for d in refs:
                sv = d.get((surah, v), set())
                den = sum(idf.get(s, 0.0) for s in sv)
                if den > 0:
                    tot += sum(idf.get(s, 0.0) for s in sv & P[k]) / den
            S[k][v] = tot / len(refs)
    z = [[0.0] * (n + 1) for _ in range(K)]
    for v in range(1, n + 1):
        for k in range(K):
            z[k][v] = S[k][v] - max(S[o][v] for o in range(K) if o != k)
    pre = [[0.0] * (n + 1) for _ in range(K)]
    for k in range(K):
        for v in range(1, n + 1):
            pre[k][v] = pre[k][v - 1] + z[k][v]
    NEG = -1e18
    Rv = [0.0] * (n + 1)  # words of the verse in the other meals (mean)
    for v in range(1, n + 1):
        Rv[v] = sum(LEN.get((m, surah, v), 0.0) for m in REFS) / len(REFS)
    Rp = [0.0] * (n + 1)
    for v in range(1, n + 1):
        Rp[v] = Rp[v - 1] + Rv[v]
    Lk = [max(1, len(tokens(t))) for t in passages]
    c = sum(Lk) / max(1.0, Rp[n])

    def pen(k: int, i: int, j: int) -> float:
        return LAMBDA * math.log((Lk[k] + 5) / (c * (Rp[j] - Rp[i]) + 5)) ** 2
    f = [[NEG] * (n + 1) for _ in range(K + 1)]
    back = [[0] * (n + 1) for _ in range(K + 1)]
    f[0][0] = 0.0
    for k in range(1, K + 1):
        for j in range(k, n - (K - k) + 1):
            best, bi = NEG, 0
            for i in range(k - 1, j):
                if f[k - 1][i] > NEG:
                    val = f[k - 1][i] + pre[k - 1][j] - pre[k - 1][i] - pen(k - 1, i, j)
                    if val > best:
                        best, bi = val, i
            f[k][j], back[k][j] = best, bi
    bounds, j = [], n
    for k in range(K, 0, -1):
        i = back[k][j]
        bounds.append((i + 1, j))
        j = i
    bounds.reverse()

    def total(b):
        return sum(pre[k][e] - pre[k][s - 1] - pen(k, s - 1, e) for k, (s, e) in enumerate(b))
    base = total(bounds)
    for k in range(K - 1):
        e = bounds[k][1]
        deltas = []
        for ne in (e - 1, e + 1):
            if bounds[k][0] <= ne < bounds[k + 1][1] and ne >= bounds[k][0] and ne + 1 <= bounds[k + 1][1]:
                b2 = list(bounds)
                b2[k] = (bounds[k][0], ne)
                b2[k + 1] = (ne + 1, bounds[k + 1][1])
                deltas.append(base - total(b2))
        margin = min(deltas) if deltas else 9.9
        if margin < 0.25:
            unc.append(f"{surah}:{e}|{e + 1} (passage {k + 1}|{k + 2}; fit margin {margin:.2f})")
    return bounds


# ---------------------------------------------------------------------------------------------- main


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--dump")
    a = ap.parse_args()
    counts = IC.ayah_counts()
    dm, dt = ensure(MEAL), ensure(TAFSIR)
    path = dm / "raw" / "acquired-2026-10-09" / f"{STEM}.djvu.txt"
    lines = path.read_text(encoding="utf-8").split("\n")
    issues: list[str] = []
    stats: Counter = Counter()
    unc: list[str] = []
    regs = find_regions(lines, counts, issues)
    refs, idf = load_refs(counts)
    msegs, tsegs = [], []
    stats["surah headings"] = len(regs)
    front = "\n".join(x.rstrip() for x in lines[:min(r["line"] for r in regs)] if x.strip())
    for r in sorted(regs, key=lambda c: c["mushaf"]):
        s = r["mushaf"]
        parts = split_region(lines, r, issues, stats)
        pas = parts["passages"]
        for pa in pas:
            pa["pre"], pa["items"], pa["fns"] = comm_items(pa["comm"], issues, f"{s}", stats)
            pa["fns"] = [x for p in pa["fn_before"] for x in p["lines"]] + pa["fns"]
        if not pas:
            issues.append(f"surah {s}: no passage found (no «Tefsir» line followed by note 1-): the whole region kept as the surah introduction")
        bounds = align(s, counts[s], [pa["meal"] for pa in pas], refs, idf, issues, unc) if pas else []
        intro = "\n".join(" ".join(p["lines"]) for p in parts["intro"] if not is_footnote(p) and not LABEL.match(p["lines"][0]))
        ifn = [x for p in parts["intro"] if is_footnote(p) for x in p["lines"]]
        head = lines[r["line"]].strip()
        tsegs.append({"seg": f"{TAFSIR}:{s}:intro", "s": s, "a": 1, "a_end": counts[s], "head": f"{head} (surah introduction)",
                      "text": intro, **({"notes": "\n".join(ifn)} if ifn else {})})
        for pa, (b0, b1) in zip(pas, bounds):
            key = f"{s}:{b0}"
            g = {"seg": f"{MEAL}:{key}", "s": s, "a": b0, "a_end": b1, "text": pa["meal"],
                 "group": f"{b0}-{b1} (one passage; the edition prints no verse numbers: range fitted to the surah's verses)"}
            if pa["formula"]:
                g["formula"] = pa["formula"]
            if pa["flag"]:
                g["meal_start_uncertain"] = True
            msegs.append(g)
            if pa["pre"]:
                tsegs.append({"seg": f"{TAFSIR}:{key}#pre", "s": s, "a": b0, "a_end": b1, "text": pa["pre"],
                              "head": "commentary before the first numbered note"})
            for n, t in pa["items"]:
                tsegs.append({"seg": f"{TAFSIR}:{key}#t{n}", "s": s, "a": b0, "a_end": b1, "text": t, "head": f"note {n}"})
            if pa["fns"]:
                tsegs.append({"seg": f"{TAFSIR}:{key}#fn", "s": s, "a": b0, "a_end": b1, "marker_found": False,
                              "head": "page footnotes printed in this passage's commentary (markers not placed)",
                              "text": "\n".join(pa["fns"])})
            stats["passages"] += 1
            stats["numbered notes"] += len(pa["items"])
    for g in tsegs:
        refs_ = slash_refs((g.get("text") or "") + " " + (g.get("notes") or ""))
        if refs_:
            g["refs"] = refs_
    tsegs.append({"seg": f"{TAFSIR}:front", "head": "title page, author, lists, preface and the Giriş essay", "text": front})
    cover = Counter()
    for g in msegs:
        for v in range(g["a"], g["a_end"] + 1):
            cover[(g["s"], v)] += 1
    missing = [f"{s}:{v}" for s in counts for v in range(1, counts[s] + 1) if (s, v) not in cover]
    short = {s: (sum(1 for (ss, _) in cover if ss == s), counts[s]) for s in counts if sum(1 for (ss, _) in cover if ss == s) != counts[s]}
    print(f"surah regions {len(regs)}; passages {stats['passages']}; verses covered {len(cover)}/6236; missing {len(missing)}; "
          f"surahs not matching {short}; notes {stats['numbered notes']}; uncertain boundaries {len(unc)}; issues {len(issues)}")
    print({k: v for k, v in stats.items()}, issues[:12])
    if a.dump:
        for nm, sg in (("meal", msegs), ("tafsir", tsegs)):
            Path(f"{a.dump}{nm}.jsonl").write_text("".join(IC.json.dumps(g, ensure_ascii=False) + "\n" for g in sg))
    if a.dry:
        print("uncertain:", unc[:30])
        return
    common = {"script": "enrichment/v2/fetch/import_meal_zduman.py", "from": IC.inputs(MEAL, [STEM, RAW2]),
              "method": "archive.org OCR text (Only Text edition); passages = «Tefsir» followed by note 1-; meal paragraph "
                        "before it; passage verse ranges fitted by word alignment to seven other meals",
              "verse_count_mismatch": {str(k): v for k, v in short.items()}, "missing": missing, "issues": issues,
              "counts": dict(stats), "uncertain_boundaries": unc}
    old_m = IC.json.loads((dm / "source.json").read_text())
    IC.write(MEAL, msegs, {**common}, {
        "coverage": f"1-114 ({len(cover)}/6236 ayat)", "notes": old_m["notes"] + (
            f" Ingested {IC._dt.date.today().isoformat()} (fetch/import_meal_zduman.py): {stats['passages']} passages, each the meal "
            f"of a revelation-order passage; the edition prints no verse numbers, so each passage's verse range was fitted by word "
            f"alignment to seven other meals ({len(unc)} boundaries are weakly determined: ingestion.uncertain_boundaries). "
            + (f"{len(missing)} verses are not covered: {', '.join(missing[:40])}." if missing else "All 6236 verses are covered."))})
    old_t = IC.json.loads((dt / "source.json").read_text())
    tied = IC.json.loads(IC.json.dumps(common))
    tied["from"] = {k: v for k, v in IC.inputs(MEAL, [STEM, RAW2]).items()}
    IC.write(TAFSIR, tsegs, tied, {
        "coverage": "1-114 (every surah: introduction and the notes of every passage)",
        "notes": old_t["notes"] + (f" Ingested {IC._dt.date.today().isoformat()} (fetch/import_meal_zduman.py): {stats['numbered notes']} numbered notes "
                                   f"tied to their passage's verse range (see MEAL-ZDUMAN for how the ranges were fitted).")})


if __name__ == "__main__":
    main()
