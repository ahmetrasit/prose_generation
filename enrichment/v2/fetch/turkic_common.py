"""Shared helpers of the early Turkic interlinear importers (import_meal_karahanli_*.py, import_meal_eat_*.py ...).

The editions come from archive.org third-party uploads whose OCR text (the item's *_djvu.txt) is the only input.
This module downloads that file into the source's raw/ folder (network only to archive.org), writes the
source.json of a new source, and holds the small text helpers every importer needs. Nothing is dropped without
being counted by the importer that calls these helpers.
"""
from __future__ import annotations

import datetime as _dt
import json
import re
import sys
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402

C = IC.C
TODAY = "2026-10-09"
NOTE = "scholarly edition; archive.org third-party upload; local research use"


def ensure_raw(sid: str, ident: str, pick: str, local: str) -> Path:
    """The item's *_djvu.txt whose name contains `pick`, under raw/acquired-<date>/<local>; downloaded when absent."""
    d = IC.src_dir(sid) if (IC.CORPUS / sid / "source.json").exists() else IC.CORPUS / sid
    out = d / f"raw/acquired-{TODAY}" / local
    if out.exists():
        return out
    out.parent.mkdir(parents=True, exist_ok=True)
    meta = json.load(urllib.request.urlopen(f"https://archive.org/metadata/{ident}", timeout=60))
    names = [f["name"] for f in meta["files"] if f["name"].endswith("_djvu.txt") and pick in f["name"]]
    if len(names) != 1:
        sys.exit(f"{ident}: expected one djvu.txt containing {pick!r}, found {names}")
    url = f"https://archive.org/download/{ident}/" + urllib.parse.quote(names[0])
    urllib.request.urlretrieve(url, out)
    print(f"downloaded {url} -> {out}")
    return out


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8", errors="replace").replace("\r", "").split("\n")


def ensure_source(sid: str, meta: dict, raw: Path | None) -> None:
    """Create or refresh the source's source.json (identity and provenance; the ingestion record is added by IC.write)."""
    d = IC.CORPUS / sid
    d.mkdir(parents=True, exist_ok=True)
    p = d / "source.json"
    old = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
    new = {**old, **meta}
    if raw is not None:
        new["files"] = {str(raw.relative_to(d)): C.sha256(raw)}
        new["fetched_at"] = _dt.datetime.now(_dt.timezone.utc).isoformat()
        new["acquisition"] = {"date": TODAY, "state": "raw_downloaded", "files": 1, "bytes": raw.stat().st_size,
                              "ingestion_status": (old.get("acquisition") or {}).get("ingestion_status", "pending"),
                              "note": "OCR text (djvu.txt) of an archive.org third-party upload; no PDF kept."}
    p.write_text(json.dumps(new, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def chunks(lines: list[str], limit: int = 3500) -> list[tuple[int, int, str]]:
    """Paragraphs (blank-line separated) packed into chunks of at most `limit` characters: (first line, last line, text)."""
    out: list[tuple[int, int, str]] = []
    cur: list[str] = []
    first = 0
    size = 0
    for i, l in enumerate(lines):
        s = l.strip()
        if not s:
            if size >= limit:
                out.append((first, i, "\n".join(cur)))
                cur, size = [], 0
            continue
        if not cur:
            first = i
        cur.append(s)
        size += len(s) + 1
        if size >= limit * 2:  # a paragraph without blank lines: cut between lines, never inside one
            out.append((first, i, "\n".join(cur)))
            cur, size = [], 0
    if cur:
        out.append((first, len(lines) - 1, "\n".join(cur)))
    return out


SLASH3 = re.compile(r"(?<![\d/])(\d{3})\s?/\s?(\d{3})(?![\d])")


def code_refs(text: str) -> list[str]:
    """«002/022», «001/006-1w1»: surah/ayah locators of the editions' notes and indexes, validated."""
    out: list[str] = []
    for m in SLASH3.finditer(text):
        s, a = int(m.group(1)), int(m.group(2))
        r = f"{s}:{a}"
        if IC.valid(s, a) and r not in out:
            out.append(r)
    return out


def covered(per_surah: dict[int, list[int]]) -> dict[str, str]:
    """{'2': '1-20,22-286', ...}: the verses present per surah as compact ranges."""
    res: dict[str, str] = {}
    for s in sorted(per_surah):
        v = sorted(set(per_surah[s]))
        rng: list[str] = []
        i = 0
        while i < len(v):
            j = i
            while j + 1 < len(v) and v[j + 1] == v[j] + 1:
                j += 1
            rng.append(str(v[i]) if i == j else f"{v[i]}-{v[j]}")
            i = j + 1
        res[str(s)] = ",".join(rng)
    return res


def missing_in_range(per_surah: dict[int, list[int]], lo_s: int, hi_s: int) -> dict[str, list[int]]:
    """Verses of surahs lo_s..hi_s (the edition's range) that no segment carries."""
    counts = IC.ayah_counts()
    out: dict[str, list[int]] = {}
    for s in range(lo_s, hi_s + 1):
        have = set(per_surah.get(s, []))
        m = [a for a in range(1, counts[s] + 1) if a not in have]
        if m:
            out[str(s)] = m
    return out


def ranges(nums: list[int]) -> str:
    return covered({0: nums})["0"]


def tally(c: Counter) -> dict:
    return {k: v for k, v in sorted(c.items())}


# ---------------------------------------------------------------- aligning an unnumbered text to a numbered one
import unicodedata as _ud
import zlib as _zlib

_FOLD = str.maketrans({"ı": "i", "İ": "i", "â": "a", "ä": "a", "ö": "o", "ü": "u", "ğ": "g", "ş": "s", "ç": "c", "î": "i", "û": "u",
                       "ñ": "n", "ŋ": "n", "é": "e", "ê": "e", "ô": "o", "ë": "e", "ñ": "n"})


def fold(x: str) -> str:
    """Letters only, lower case, Turkish/Arabic-transliteration diacritics folded: the comparison form of a word."""
    x = _ud.normalize("NFD", x.lower().replace("i̇", "i"))
    x = "".join(c for c in x if not _ud.combining(c)).translate(_FOLD)
    return re.sub(r"[^a-z]", "", x)


def _bits(x: str) -> int:
    v = 0
    if len(x) < 3:
        return (1 << (_zlib.crc32(x.encode()) % 8192)) if x else 0
    for i in range(len(x) - 2):
        v |= 1 << (_zlib.crc32(x[i:i + 3].encode()) % 8192)
    return v


def align_to_oracle(words: list[str], oracle: list[str | None], max_ratio: float = 4.0) -> tuple[list[int], list[float]] | None:
    """Cut `words` (the unnumbered text, in order) into len(oracle) runs, run j resembling oracle[j] (a numbered text of
    the same passage: another translation or edition) most: dynamic programme over word positions with the cut point of
    run j kept near where the oracle's share of characters puts it, run length at most `max_ratio` times the expected
    one; similarity = Dice over character trigrams (bit sets). A verse whose oracle is None scores 0.4. Returns the end
    index of every run and its similarity, or None when no cut exists."""
    N, m = len(words), len(oracle)
    if N < m or m == 0:
        return None
    wb = [_bits(fold(w)) for w in words]
    ob = [_bits("".join(fold(w) for w in o.split())) if o else None for o in oracle]
    oc = [b.bit_count() if b is not None else 0 for b in ob]
    lens = [sum(len(fold(w)) for w in o.split()) if o else 0 for o in oracle]
    known = [x for x in lens if x]
    if not known:
        return None
    avg = sum(known) / len(known)
    lens = [x or avg for x in lens]
    tot = sum(lens)
    cum, acc = [], 0.0
    for x in lens:
        acc += x
        cum.append(acc / tot)
    W = max(30, int(0.05 * N))
    window = []
    for j in range(m):
        e = round(N * cum[j])
        window.append((max(j + 1, e - W), min(N - (m - 1 - j), e + W)) if j < m - 1 else (N, N))
    NEG = -1e9
    prev: dict[int, float] = {0: 0.0}
    backs: list[dict[int, int]] = []
    for j in range(m):
        lo, hi = window[j]
        exp_words = max(3.0, N * lens[j] / tot)
        maxlen = int(exp_words * max_ratio) + 12
        cur: dict[int, float] = {}
        bk: dict[int, int] = {}
        for p, val in prev.items():
            acc = 0
            top = min(hi, p + maxlen)
            for i in range(p + 1, top + 1):
                acc |= wb[i - 1]
                if i < lo:
                    continue
                if ob[j] is None:
                    sc = 0.4
                else:
                    c = acc.bit_count()
                    sc = 2 * (acc & ob[j]).bit_count() / (c + oc[j]) if c else 0.0
                v2 = val + sc
                if v2 > cur.get(i, NEG):
                    cur[i] = v2
                    bk[i] = p
        if not cur:
            return None
        backs.append(bk)
        prev = cur
    if N not in prev:
        return None
    ends, sims = [], []
    i = N
    for j in range(m - 1, -1, -1):
        p = backs[j][i]
        acc = 0
        for t in wb[p:i]:
            acc |= t
        c = acc.bit_count()
        sims.append(0.4 if ob[j] is None else (2 * (acc & ob[j]).bit_count() / (c + oc[j]) if c else 0.0))
        ends.append(i)
        i = p
    return ends[::-1], sims[::-1]
