"""Shared helpers for the importers of the user's downloads (import_*.py; Task B in HYBRID_PLAN.md).

Input: the page cache of fetch/pdf_pages.py (raw/pages/<pdf stem>.jsonl, one line per PDF page) or an OCR file.
Output: segments.jsonl beside the source's source.json (corpus/README.md contract), and source.json updated in place:
access becomes `yerel` and an `ingestion` record says the script, the inputs (sha256), the counts and every
quality caveat. Nothing a page holds is dropped without being counted in that record (no silent losses: user,
2026-10-05).
"""
from __future__ import annotations

import datetime as _dt
import json
import re
import sqlite3
import sys
from pathlib import Path

V2 = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(V2 / "tools"))
import corpus as C  # noqa: E402

CORPUS = C.CORPUS


def src_dir(sid: str) -> Path:
    return C.source_dir(sid)


def pages(sid: str, stem: str) -> list[dict]:
    path = src_dir(sid) / "raw" / "pages" / f"{stem}.jsonl"
    if not path.exists():
        sys.exit(f"{path} missing: run fetch/pdf_pages.py on {sid} first")
    return [json.loads(x) for x in path.open(encoding="utf-8")]


_COUNTS: dict[int, int] | None = None


def ayah_counts() -> dict[int, int]:
    """Ayat per surah, from the QURAN source in the index."""
    global _COUNTS
    if _COUNTS is None:
        con = sqlite3.connect(C.INDEX)
        _COUNTS = {s: n for s, n in con.execute("SELECT s, max(a) FROM seg WHERE src='QURAN' GROUP BY s")}
        if len(_COUNTS) != 114:
            sys.exit("the index has no complete QURAN source")
    return _COUNTS


def valid(s: int, a: int, b: int | None = None) -> bool:
    n = ayah_counts().get(s)
    return bool(n) and 1 <= a <= n and (b is None or a <= b <= n)


# "2:255", "Q 2:255", "20:125-7", "20:125–127", "2:3.5" is not taken (a list form, too ambiguous)
REF = re.compile(r"(?<![\d:.,/])(\d{1,3})\s?:\s?(\d{1,3})(?:\s?[-–]\s?(\d{1,3}))?(?![\d:])")


# a Bible book (name or usual abbreviation) right before a reference: not the Qurʾān
BIBLE = re.compile(
    r"\b(?:Gen(?:esis)?|Exod(?:us)?|Ex|Lev(?:iticus)?|Num(?:bers)?|Deut(?:eronomy)?|Josh(?:ua)?|Judg(?:es)?|Ruth|"
    r"Sam(?:uel)?|Kgs|Kings|Chr(?:on(?:icles)?)?|Ezra|Neh(?:emiah)?|Esth(?:er)?|Job|Ps(?:alms?|s)?|Prov(?:erbs)?|"
    r"Eccl(?:esiastes)?|Qoh(?:eleth)?|Song|Cant|Isa(?:iah)?|Jer(?:emiah)?|Lam(?:entations)?|Ezek(?:iel)?|Dan(?:iel)?|"
    r"Hos(?:ea)?|Joel|Amos|Obad(?:iah)?|Jonah|Mic(?:ah)?|Nah(?:um)?|Hab(?:akkuk)?|Zeph(?:aniah)?|Hag(?:gai)?|"
    r"Zech(?:ariah)?|Mal(?:achi)?|Matt?(?:hew)?|Mk|Mark|Lk|Luke|Jn|John|Acts|Rom(?:ans)?|Cor(?:inthians)?|"
    r"Gal(?:atians)?|Eph(?:esians)?|Phil(?:ippians)?|Col(?:ossians)?|Thess(?:alonians)?|Tim(?:othy)?|Tit(?:us)?|"
    r"Philem(?:on)?|Heb(?:rews)?|Jas|James|Pet(?:er)?|Jude|Rev(?:elation)?|Sir(?:ach)?|Tob(?:it)?|Macc(?:abees)?|"
    r"Wis(?:dom)?|Bar(?:uch)?|Enoch|Jub(?:ilees)?)\.?\s*$")


# further ayat of the same surah after a reference: «q 6:59, 63 and 97», «(6:12 and 54)», «7:156–57, 160»
MORE = re.compile(r"\s?(?:,|and|&)\s?(\d{1,3})(?:\s?[-–]\s?(\d{1,3}))?(?![\d:])")


def _end(a: str, b: str | None) -> int | None:
    if b is None:
        return None
    n = int(b)
    if n < int(a) and len(b) < len(a):  # "125-7" = 125-127
        n = int(a[:len(a) - len(b)] + b)
    return n


def find_refs(text: str) -> list[str]:
    """The ayat a text cites as surah:ayah (ranges kept, and the further ayat listed after one: «6:59, 63 and 97»),
    validated against the surah lengths; in text order, each once."""
    out: list[str] = []

    def add(s: int, a: int, b: int | None) -> None:
        if not valid(s, a, b if b is not None and b >= a else None):
            return
        r = f"{s}:{a}" + (f"-{b}" if b is not None and b > a else "")
        if r not in out:
            out.append(r)
    for m in REF.finditer(text):
        if BIBLE.search(text[max(0, m.start() - 24):m.start()]):  # «Rev 1:1», «Genesis 2–3», «1 Kings 19:1»
            continue
        s, a = int(m.group(1)), int(m.group(2))
        add(s, a, _end(m.group(2), m.group(3)))
        pos = m.end()
        while True:
            mm = MORE.match(text, pos)
            if not mm:
                break
            add(s, int(mm.group(1)), _end(mm.group(1), mm.group(2)))
            pos = mm.end()
    return out


def write(sid: str, segments: list[dict], ingestion: dict, meta_updates: dict | None = None) -> None:
    """segments.jsonl (locators must be unique) and source.json (access yerel + the ingestion record)."""
    d = src_dir(sid)
    seen: set[str] = set()
    for g in segments:
        if g["seg"] in seen:
            sys.exit(f"duplicate locator {g['seg']}: refusing to write {sid}")
        seen.add(g["seg"])
        g.setdefault("s", None)
        g.setdefault("a", None)
        g.setdefault("a_end", g.get("a"))
    tmp = d / "segments.jsonl.tmp"
    with tmp.open("w", encoding="utf-8") as f:
        for g in segments:
            f.write(json.dumps(g, ensure_ascii=False) + "\n")
    tmp.replace(d / "segments.jsonl")
    meta = json.loads((d / "source.json").read_text(encoding="utf-8"))
    meta.update(meta_updates or {})
    meta["access"] = "yerel"
    meta["segments"] = len(segments)
    tied = sum(1 for g in segments if g.get("s") is not None)
    with_refs = sum(1 for g in segments if g.get("refs"))
    ingestion = {"date": _dt.date.today().isoformat(), **ingestion, "segments": len(segments),
                 "tied_to_ayah": tied, "with_cited_ayat": with_refs,
                 "characters": sum(len(g.get("text") or "") for g in segments)}
    meta["ingestion"] = ingestion
    if isinstance(meta.get("acquisition"), dict):
        meta["acquisition"]["ingestion_status"] = "ingested"
    (d / "source.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{sid}: wrote {len(segments)} segments ({tied} tied to ayat, {with_refs} citing ayat, "
          f"{ingestion['characters']:,} characters) -> {(d / 'segments.jsonl').relative_to(C.PG)}")


def inputs(sid: str, stems: list[str]) -> dict:
    """The input files of an ingestion with their sha256 (the PDF the page cache came from)."""
    d = src_dir(sid)
    out = {}
    for stem in stems:
        for p in sorted(d.glob(f"raw/acquired-*/{stem}.*")):
            out[str(p.relative_to(d))] = C.sha256(p)
    return out
