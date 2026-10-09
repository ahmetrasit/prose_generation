#!/usr/bin/env python3
"""Sefaria texts on demand for the Bible pass (kind intertext, gelenek tevrat): Tanakh commentary, Targum, Talmud,
midrash, by reference, into enrichment/bible/corpus/SEFARIA/.

  bible_sefaria.py text "Genesis 22:2" "Targum Jonathan on Genesis 22:2" "Genesis Rabbah 56:1"
  bible_sefaria.py related "Genesis 22:2" --types targum,midrash,talmud,commentary --n 12

`related` lists Sefaria's links for a Tanakh verse, keeps the given link types (at most --n per type), and fetches
each linked text. Locators: SEFARIA:<ref with spaces as _ and : as .>, e.g. SEFARIA:Targum_Jonathan_on_Genesis.22.2,
SEFARIA:Genesis_Rabbah.56.1. Every fetched text keeps its Sefaria version title and licence in the segment (per
version licences differ; the source.json says so). Run before a page call: the agents have no network.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from enrichment.bible.fetch.ref_common import Source  # noqa: E402

API = "https://www.sefaria.org/api"
META = {"id": "SEFARIA", "title": "Sefaria library: Tanakh commentary, Targum, Talmud, midrash (texts fetched by reference)",
        "author": "various; Sefaria (texts and translations per version)", "death_ah": None, "kind": "intertext",
        "gelenek": ["tevrat"], "tradition": "Jewish (Tanakh, Targum, Talmud, midrash, classical commentary)", "language": "he|en",
        "edition": "Sefaria API v3 (texts) and related (links); the version title per segment", "access": "yerel",
        "locator": "sefaria-ref", "licence": "per version, as Sefaria states it (CC-BY, CC-BY-SA, CC0, public domain); "
        "recorded in each segment's `licence`; local research copy",
        "notes": "FOR THE BIBLE PASS ONLY. Fetched on demand, reference by reference; coverage is whatever has been asked for. "
                 "The agents have no network: fetch before the call (bible_sefaria.py related <Tanakh ref> for a verse's "
                 "Targum/midrash/Talmud/commentary). Hebrew text `text`, English translation `en` when Sefaria has one.",
        "coverage": "on demand"}
TYPES = {"targum": "Targum", "midrash": "Midrash", "talmud": "Talmud", "commentary": "Commentary", "mishnah": "Mishnah",
         "halakhah": "Halakhah", "kabbalah": "Kabbalah", "liturgy": "Liturgy", "apocrypha": "Second Temple"}


def loc(ref: str) -> str:
    """SEFARIA:<work with spaces as _>.<chapter>.<verse>: "Onkelos Genesis 22:2" -> SEFARIA:Onkelos_Genesis.22.2,
    "Berakhot 60b" -> SEFARIA:Berakhot.60b, "Genesis Rabbah 56:1" -> SEFARIA:Genesis_Rabbah.56.1."""
    r = re.sub(r"\s+(\d+[a-b]?(?::\d+)*)$", r".\1", ref.strip())
    return "SEFARIA:" + re.sub(r"\s+", "_", r).replace(":", ".")


def flat(x) -> str:
    if isinstance(x, list):
        return " ".join(flat(y) for y in x)
    return re.sub(r"<[^>]+>", "", str(x or "")).strip()


def fetch_text(src: Source, ref: str) -> dict | None:
    q = urllib.parse.quote(ref.strip().replace(" ", "_"))
    rel = f"texts/{q}.json"
    st, body = src.fetch(f"{API}/v3/texts/{q}?version=primary&version=translation", rel)
    if st in (400, 404):  # Sefaria answers 400 for a reference it cannot parse: unavailable here, a gap
        if st == 400:
            print(f'NOTE: {ref}: Sefaria cannot parse this reference (400); recorded as a gap', file=sys.stderr)
        return None
    if st != 200 or not body:
        raise ValueError(f'FETCH FAILED: {ref} ({st})')
    try:
        d = json.loads(body)
    except json.JSONDecodeError as exc:
        raise ValueError(f'FETCH FAILED: {ref}: not JSON') from exc
    if d.get('error'):
        raise ValueError(f'FETCH FAILED: {ref}: {d["error"]}')
    he, en, lic, vt = "", "", [], []
    for v in d.get("versions") or []:
        t = flat(v.get("text"))
        if not t:
            continue
        if v.get("language") == "he" and not he:
            he = t
        elif v.get("language") == "en" and not en:
            en = t
        vt.append(f"{v.get('versionTitle')} ({v.get('language')})")
        if v.get("license"):
            lic.append(str(v.get("license")))
    if not he and not en:
        print(f"WARNING: {ref}: no text in the response", file=sys.stderr)
        return None
    cats = d.get("categories") or []
    return {"seg": loc(d.get("ref") or ref), "s": None, "a": None, "a_end": None, "page": None,
            "head": d.get("ref") or ref, "text": he or en, **({"en": en} if he and en else {}),
            "text_language": 'he' if he else 'en', "translation_aid": not bool(he),
            "ref": d.get("ref"), "heRef": d.get("heRef"), "book": d.get("book"), "categories": cats,
            "primary_category": d.get("primary_category"), "versions": vt, "licence": " | ".join(dict.fromkeys(lic))}


def cmd_text(refs: list[str]) -> dict:
    src, segs = Source("SEFARIA"), []
    report = {'requested': refs, 'resolved': {}, 'missing': [], 'errors': []}
    for r in refs:
        try:
            seg = fetch_text(src, r)
        except Exception as e:
            report['errors'].append({'ref': r, 'error': str(e)})
            print(f'FETCH FAILED: {r}: {e}', file=sys.stderr)
            continue
        if seg:
            segs.append(seg)
            print(f"{seg['seg']}  [{', '.join(seg['versions'])}]")
            report['resolved'][r] = seg['seg']
        else:
            report['missing'].append(r)
    if segs:
        src.upsert_segments(segs)
    src.update_source(META, urls=[f"{API}/v3/texts/<ref>", f"{API}/related/<ref>"])
    print(f"{len(segs)} of {len(refs)} fetched")
    return report


def cmd_related(ref: str, types: list[str], n: int) -> dict:
    src = Source("SEFARIA")
    q = urllib.parse.quote(ref.strip().replace(" ", "_"))
    st, body = src.fetch(f"{API}/related/{q}", f"related/{q}.json")
    if st != 200 or not body:
        raise ValueError(f"FETCH FAILED: related {ref} ({st})")
    data = json.loads(body)
    if data.get('error'):
        raise ValueError(f'FETCH FAILED: related {ref}: {data["error"]}')
    links = data.get("links") or []
    want = {TYPES[t] for t in types}
    picked, per = [], {}
    for l in links:
        cat = l.get("category")
        if cat not in want or not l.get('ref'):
            continue
        if per.get(cat, 0) >= n:
            continue
        per[cat] = per.get(cat, 0) + 1
        picked.append(l.get("ref"))
    print(f"{ref}: {len(links)} links, {len(picked)} kept ({', '.join(f'{k} {v}' for k, v in per.items())})")
    return cmd_text(list(dict.fromkeys(picked)))


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("text"); p.add_argument("refs", nargs="+")
    p = sub.add_parser("related"); p.add_argument("ref"); p.add_argument("--types", default="targum,midrash,talmud,commentary")
    p.add_argument("--n", type=int, default=8, help="links kept per type")
    for parser in sub.choices.values():
        parser.add_argument('--report', type=Path, help='write the structured retrieval result')
    a = ap.parse_args()
    if a.cmd == "text":
        report = cmd_text(a.refs)
    else:
        bad = [t for t in a.types.split(",") if t not in TYPES]
        if bad:
            raise SystemExit(f"unknown link types {bad}; known: {', '.join(TYPES)}")
        report = cmd_related(a.ref, a.types.split(","), a.n)
    if a.report:
        a.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    if report['errors'] or report['missing']:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
