#!/usr/bin/env python3
"""Numbering divergence of a meal source: tie its verse units to the canonical ayat by text (2026-10-09 review).

Some hosts and books number a translation differently from the Hafs count the project uses (a verse omitted or
merged by the translator, a verse split in two, a row printed twice), so from some verse on every unit sits on the
number of its neighbour. A monotone alignment (dynamic programming) of the units against the same ayat in other Turkish
meals puts them where their text belongs: several units may share one ayah (the work splits it), a unit may cover several
ayat (the work joins them), ayat may stay empty (the work lacks them: reported as gaps), near-duplicate units are dropped
(reported). A surah is changed only when the moved units fit their new ayat clearly better than their printed ones.

  realign(sid, sn, units, nv) -> None | dict(units=[...], moved, gain, dropped=[...], gaps=[...])
A unit is a dict with s, a, a_end, text (and any other keys: kept on the first unit of a merged ayah).
"""
from __future__ import annotations

import json
import math
import re
import unicodedata
from pathlib import Path

CORPUS = Path(__file__).resolve().parents[2] / "corpus"
REFS = ["MEAL-DIB", "MEAL-ELMALILI", "MEAL-BILMEN", "MEAL-YAKIT", "MEAL-OCELIK", "MEAL-IZMIRLI", "MEAL-ATAY",
        "MEAL-CAKIR", "MEAL-HAYRAT", "MEAL-ESED", "MEAL-DEMIRYENT", "MEAL-BAYRAKLI"]
MIN_GAIN, MIN_MOVED = 1.0, 3
W_WIDTH, W_GAP, W_SHARE = 0.3, 0.2, 0.15
_R: dict = {}


def toks(t: str) -> set[str]:
    t = t.lower().replace("ı", "i")
    t = "".join(c for c in unicodedata.normalize("NFD", t) if not unicodedata.combining(c))
    t = t.replace("ş", "s").replace("ç", "c").replace("ğ", "g")
    return {w[:5] for w in re.findall(r"[a-z]{4,}", t)}


def cosine(a: set, b: set) -> float:
    return len(a & b) / math.sqrt(len(a) * len(b)) if a and b else 0.0


def refs(exclude: str) -> dict:
    for r in REFS:
        if r in _R:
            continue
        d: dict = {}
        path = CORPUS / r / "segments.jsonl"
        if not path.exists():
            continue
        for line in path.open(encoding="utf-8"):
            x = json.loads(line)
            if x.get("s") and x["seg"].rsplit(":", 1)[-1].isdigit():
                for q in range(x["a"], x["a_end"] + 1):
                    d.setdefault(x["s"], {}).setdefault(q, []).append(x["text"])
        _R[r] = {s: {q: toks(" ".join(ts)) for q, ts in v.items()} for s, v in d.items()}
    return {k: v for k, v in _R.items() if k != exclude}


def realign(sid: str, sn: int, units: list[dict], nv: int, maxw: int = 3, maxgap: int = 3) -> dict | None:
    units = sorted(units, key=lambda u: (u["a"], u["a_end"]))
    m = len(units)
    if m < 8:
        return None
    rf = refs(sid)
    ts = [toks(u["text"]) for u in units]
    wt = [min(len(t), 25) / 25 for t in ts]
    cache: dict = {}

    def sc(i: int, p: int, q: int) -> float:
        k = (i, p, q)
        if k not in cache:
            best = 0.0
            for d in rf.values():
                dd = d.get(sn, {})
                un: set = set()
                for v in range(p, q + 1):
                    un |= dd.get(v, set())
                best = max(best, cosine(ts[i], un))
            cache[k] = best * wt[i]
        return cache[k]

    def ident(u: dict) -> tuple[int, int]:
        return min(u["a"], nv), min(u["a_end"], nv)
    NEG = -1e9
    dp: list[dict] = [dict() for _ in range(m)]
    back: list[dict] = [dict() for _ in range(m)]
    for p in range(1, maxgap + 2):
        for q in range(p, min(p + maxw - 1, nv) + 1):
            dp[0][(p, q)] = sc(0, p, q) - W_WIDTH * (q - p) - W_GAP * (p - 1) + (0.05 if (p, q) == ident(units[0]) else 0)
            back[0][(p, q)] = None
    for i in range(1, m):
        for (p0, q0), s0 in dp[i - 1].items():
            for p in range(max(1, q0), min(q0 + maxgap + 2, nv + 1)):
                gap = max(0, p - q0 - 1)
                for q in range(p, min(p + maxw - 1, nv) + 1):
                    v = (s0 + sc(i, p, q) - W_WIDTH * (q - p) - (W_SHARE if p == q0 else 0) - W_GAP * gap
                         + (0.05 if (p, q) == ident(units[i]) else 0))
                    if v > dp[i].get((p, q), NEG):
                        dp[i][(p, q)] = v
                        back[i][(p, q)] = (p0, q0)
    cands = [(v - W_GAP * (nv - k[1]), k) for k, v in dp[m - 1].items() if nv - k[1] <= maxgap + 1]
    if not cands:
        return None
    _, k = max(cands)
    path = [k]
    for i in range(m - 1, 0, -1):
        k = back[i][k]
        path.append(k)
    path.reverse()
    moved = [(i, u) for i, (u, pq) in enumerate(zip(units, path)) if ident(u) != pq]
    gain = sum(sc(i, *path[i]) - sc(i, *ident(u)) for i, u in moved)
    if len(moved) < MIN_MOVED or gain < MIN_GAIN:
        return None
    # merge units that share an ayah; drop near-duplicates (a row the host printed twice)
    out: list[dict] = []
    dropped: list[str] = []
    for i, (u, (p, q)) in enumerate(zip(units, path)):
        u = dict(u)
        u["book_a"], u["book_a_end"] = u["a"], u["a_end"]
        u["a"], u["a_end"] = p, q
        if out and p <= out[-1]["a_end"]:
            prev = out[-1]
            if cosine(ts[i], toks(prev["text"])) >= 0.55 or cosine(ts[i], toks(" ".join(prev.get("_parts", [prev["text"]])))) >= 0.55:
                dropped.append(f"{sn}:{u['book_a']}" + (f"-{u['book_a_end']}" if u["book_a_end"] > u["book_a"] else "")
                               + f" (near-duplicate of the unit on {sn}:{prev['a']})")
                continue
            prev["text"] = (prev["text"] + " " + u["text"]).strip()
            prev["a_end"] = max(prev["a_end"], q)
            prev.setdefault("_parts", []).append(u["text"])
            prev["book_a_end"] = u["book_a_end"]
        else:
            out.append(u)
    covered = set()
    for u in out:
        covered.update(range(u["a"], u["a_end"] + 1))
    gaps = [f"{sn}:{q}" for q in range(1, nv + 1) if q not in covered]
    for u in out:
        u.pop("_parts", None)
    return {"units": out, "moved": len(moved), "gain": round(gain, 1), "dropped": dropped, "gaps": gaps}
