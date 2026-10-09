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
