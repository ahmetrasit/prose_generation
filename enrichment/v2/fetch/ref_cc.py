#!/usr/bin/env python3
"""Corpus Coranicum (BBAW) -> enrichment/corpus/CORPUSCORANICUM/  and  .../CORPUSCORANICUM-INTERTEXT/

  ref_cc.py commentary 1 87-114        chronological-literary commentary per sura (Sinai/Neuwirth et al.)
  ref_cc.py intertexts 1 22 87-114     per-verse intertext lists + full intertext records
  ref_cc.py all 1 22 87-114            both
  ref_cc.py reparse                    rebuild both segments.jsonl from raw/ (no network)

Open JSON API used by the public site (https://corpuscoranicum.de, Vue SPA):
  https://api.corpuscoranicum.de/api/data/commentary/available        -> list of suras with commentary
  https://api.corpuscoranicum.de/api/data/commentary/sura/<n>          -> text_structure + sections
  https://api.corpuscoranicum.de/api/data/intertexts                   -> index (713 entries, first passage only)
  https://api.corpuscoranicum.de/api/data/intertexts/sura/<s>/verse/<v>-> intertexts attached to a verse
  https://api.corpuscoranicum.de/api/data/intertexts/<id>              -> full record (text, translation, notes)
Human-readable pages: https://corpuscoranicum.de/de/verse-navigator/sura/<s>/verse/<v>/commentary
                      https://corpuscoranicum.de/de/verse-navigator/sura/<s>/verse/<v>/intertexts/<id>

INTERTEXTS (Bible / Jewish / Christian / pagan parallels) go ONLY to CORPUSCORANICUM-INTERTEXT
(kind "intertext"), kept apart from the Islamic-literature pass.
"""
from __future__ import annotations

import argparse
import json
import sys

from ref_common import Source, html_to_text

API = "https://api.corpuscoranicum.de/api/data"
SITE = "https://corpuscoranicum.de"
SID, SID_IT = "CORPUSCORANICUM", "CORPUSCORANICUM-INTERTEXT"

AYAS = [7, 286, 200, 176, 120, 165, 206, 75, 129, 109, 123, 111, 43, 52, 99, 128, 111, 110, 98, 135, 112, 78, 118,
        64, 77, 227, 93, 88, 69, 60, 34, 30, 73, 54, 45, 83, 182, 88, 75, 85, 54, 53, 89, 59, 37, 35, 38, 29, 18, 45,
        60, 49, 62, 55, 78, 96, 29, 22, 24, 13, 14, 11, 11, 18, 12, 12, 30, 52, 52, 44, 28, 28, 20, 56, 40, 31, 50,
        40, 46, 42, 29, 19, 36, 25, 22, 17, 19, 26, 30, 20, 15, 21, 11, 8, 8, 19, 5, 8, 8, 11, 11, 8, 3, 9, 5, 4, 7,
        3, 6, 3, 5, 4, 5, 6]
assert len(AYAS) == 114 and sum(AYAS) == 6236

LICENCE = ("BBAW Corpus Coranicum. Impressum (api .../website/language/de/info/impressum, fetched into raw/): "
           "'Alle Rechte vorbehalten. Lizensiert unter einer Creative Commons Namensnennung 3.0 Lizenz' "
           "(i.e. CC BY 3.0 stated, alongside an all-rights-reserved formula); authors' copyright on texts. "
           "Cite as given in how_to_cite. Local research copy only.")

META = {
    "id": SID,
    "title": "Corpus Coranicum — Chronologisch-literaturwissenschaftlicher Kommentar zum Koran",
    "author": "Nicolai Sinai (Frühmekkanische Suren), with Nora K. Schmid, using preparatory work by Angelika Neuwirth; "
              "later parts Dirk Hartwig, Angelika Neuwirth et al. (author line per sura in segments)",
    "death_ah": None,
    "kind": "modern",
    "tradition": "academic (Western historical-critical / literary; Neuwirth school)",
    "language": "de",
    "edition": "online beta ('Betaversion: Stand <date>') served by api.corpuscoranicum.de",
    "access": "yerel",
    "locator": "ayah",
    "licence": LICENCE,
    "notes": "seg CORPUSCORANICUM:<s>:<section> for sura-level sections (datierung = Neuwirth/Nöldeke period, "
             "e.g. 'Mekka I'; literarkritik; aufbau = structure; structure = verse table with rhyme and verse groups) "
             "and CORPUSCORANICUM:<s>:<a>[-<a_end>]:<anmerkung|kommentar>[#k] for verse notes. Methodological "
             "boilerplate (comment_title) is not segmented. CAVEAT: the commentary text itself sometimes quotes Biblical / "
             "Late Antique parallels (e.g. Mt 6:5 at 107:4-7); the structured intertext database is kept separately. Suras without commentary return nothing (see "
             "available_suras). Intertexts are NOT here: see CORPUSCORANICUM-INTERTEXT.",
}
META_IT = {
    "id": SID_IT,
    "title": "Corpus Coranicum — Texte aus der Umwelt des Korans (TUK, intertexts)",
    "author": "various entry authors (per segment), BBAW",
    "death_ah": None,
    "kind": "intertext",
    "tradition": "academic; Late Antique non-Islamic parallels (Hebrew Bible, NT, patristics, pseudepigrapha, "
                 "inscriptions, pre-Islamic poetry)",
    "language": "de",
    "edition": "online database via api.corpuscoranicum.de",
    "access": "yerel",
    "locator": "ayah",
    "licence": LICENCE,
    "notes": "FOR THE SEPARATE INTERTEXT PASS ONLY — must not enter the Islamic-literature enrichment pass. "
             "seg CORPUSCORANICUM-INTERTEXT:<s>:<a>[-<a_end>]:<TUK id>; one segment per (intertext, passage) for "
             "passages in suras whose verse lists were fetched; the same intertext text is repeated for each such "
             "passage. Fields: tuk_id, title, category, supercategory, language, dated, location, source, "
             "entry_author, url.",
}


def nums(items):
    out = []
    for it in items:
        if "-" in it:
            a, b = it.split("-")
            out += range(int(a), int(b) + 1)
        else:
            out.append(int(it))
    return out


def jget(src: Source, path: str, rel: str, refresh=False):
    st, body = src.fetch(f"{API}/{path}", rel, refresh=refresh, headers={"Accept": "application/json"})
    if st != 200:
        return None
    return json.loads(body)["data"]


# ---------------------------------------------------------------- commentary
def available(src, refresh=False):
    return jget(src, "commentary/available", "commentary/available.json", refresh) or []


def vr(a, b):
    return f"{a}" if a == b else f"{a}-{b}"


def parse_commentary(n: int, d: dict) -> list[dict]:
    segs = []
    title = html_to_text(d.get("title") or "")
    author = d.get("author")
    cite = (d.get("how_to_cite") or "").replace("%DATE%", "<date>")
    base = {"s": n, "title": title, "author": author, "cite": cite,
            "url": f"{SITE}/de/verse-navigator/sura/{n}/verse/1/commentary"}
    rows = []
    for v in d.get("text_structure") or []:
        rows.append(f"V.{v['verse']} [Versgruppe {v.get('decade')}, Abschnitt {v.get('section')}, Hauptteil "
                    f"{v.get('main_part')}, Reim {v.get('rhyme')}{', Einschub' if v.get('insert') else ''}] "
                    f"{v.get('de') or ''}")
    if rows:
        segs.append(dict(base, seg=f"{SID}:{n}:structure", a=None, a_end=None,
                         head=f"{title} — Textstruktur (Versgruppen, Reim, Übersetzung)", text="\n".join(rows)))
    for sec in d.get("sections") or []:
        sid = sec.get("id")
        gt = sec.get("general_title") or sid
        st = sec.get("specific_title")
        head = f"{title} — {gt}" + (f": {st}" if st else "")
        wc = html_to_text(sec.get("works_cited") or "")
        if sec.get("content"):
            txt = html_to_text(sec["content"])
            if wc:
                txt += "\n\nLiteratur: " + wc
            segs.append(dict(base, seg=f"{SID}:{n}:{sid}", a=None, a_end=None, head=head, text=txt,
                             section=sid, classification=st))
        seen = {}
        for it in sec.get("verse_content") or []:
            a, b = it.get("verse_start"), it.get("verse_end")
            key = f"{SID}:{n}:{vr(a, b)}:{sid}"
            seen[key] = seen.get(key, 0) + 1
            if seen[key] > 1:
                key += f"#{seen[key]}"
            segs.append(dict(base, seg=key, a=a, a_end=b, head=f"{head} — V. {vr(a, b)}",
                             text=html_to_text(it.get("content") or ""), section=sid))
        if sec.get("verse_content") and wc:
            segs.append(dict(base, seg=f"{SID}:{n}:{sid}:literatur", a=None, a_end=None,
                             head=f"{head} — Literatur", text=wc, section=sid))
    return segs


def do_commentary(src: Source, suras, refresh=False):
    av = set(available(src, refresh))
    src.fetch("https://api.corpuscoranicum.de/api/website/language/de/info/impressum", "site/impressum_de.json",
              refresh=refresh)
    for n in suras:
        if n not in av:
            print(f"S{n}: no commentary published (not in commentary/available)")
            continue
        d = jget(src, f"commentary/sura/{n}", f"commentary/sura_{n:03d}.json", refresh)
        if not d:
            print(f"S{n}: fetch failed", file=sys.stderr)
            continue
        segs = parse_commentary(n, d)
        src.upsert_segments(segs, drop_prefix=f"{SID}:{n}:")
        dat = next((s.get("classification") for s in segs if s.get("section") == "datierung"), None)
        print(f"S{n}: {len(segs)} segments; Datierung: {dat}")
    finalize_commentary(src, av)


def finalize_commentary(src: Source, av=None):
    av = av or set(json.loads(src.read_raw("commentary/available.json"))["data"])
    segs = src.load_segments()
    done = sorted({s["s"] for s in segs})
    chron = {s["s"]: s.get("classification") for s in segs if s.get("section") == "datierung"}
    src.update_source(dict(META, coverage=",".join(map(str, done))), urls=[SITE, f"{API}/commentary/sura/<n>"],
                      extra={"available_suras": sorted(av), "chronology": {str(k): v for k, v in sorted(chron.items())}})


# ---------------------------------------------------------------- intertexts
def it_segments(rec: dict, suras: set) -> list[dict]:
    out = []
    tr = rec.get("translations") or {}
    if isinstance(tr, str):
        tr = {"de": tr}
    parts = [f"{rec.get('title')} — {rec.get('supercategory') or ''} / {rec.get('category') or ''}",
             f"Sprache: {rec.get('language')}; Ort: {rec.get('location')}; datiert: {rec.get('dated')}; "
             f"Autor des Intertexts: {rec.get('intertext_author')}"]
    if rec.get("content"):
        parts.append("Text:\n" + html_to_text(rec["content"]))
    if rec.get("transcription"):
        parts.append("Transkription:\n" + html_to_text(rec["transcription"]))
    for lang in ("de", "en", "fr"):
        if tr.get(lang):
            parts.append(f"Übersetzung ({lang}):\n" + html_to_text(tr[lang]))
    for k, lab in (("notes", "Kommentar"), ("source", "Quelle"), ("translation_source", "Übersetzungsquelle"),
                   ("identified_by", "Identifiziert von"), ("literature", "Literatur")):
        if rec.get(k):
            parts.append(f"{lab}: " + html_to_text(rec[k]))
    text = "\n\n".join(parts)
    for p in rec.get("passages") or []:
        s, e = p["start"], p["end"]
        if s["sura"] not in suras:
            continue
        a_end = e["verse"] if e["sura"] == s["sura"] else None
        out.append({"seg": f"{SID_IT}:{s['sura']}:{vr(s['verse'], a_end or s['verse'])}:{rec['id']}",
                    "s": s["sura"], "a": s["verse"], "a_end": a_end or s["verse"], "page": None,
                    "head": rec.get("title"), "text": text, "tuk_id": rec["id"],
                    "category": rec.get("category"), "supercategory": rec.get("supercategory"),
                    "language": rec.get("language"), "dated": rec.get("dated"), "location": rec.get("location"),
                    "entry_author": rec.get("entry_author"), "updated_at": rec.get("updated_at"),
                    "url": f"{SITE}/de/verse-navigator/sura/{s['sura']}/verse/{s['verse']}/intertexts/{rec['id']}"})
    return out


def do_intertexts(src: Source, suras, refresh=False):
    ids = {}
    for n in suras:
        for v in range(1, AYAS[n - 1] + 1):
            d = jget(src, f"intertexts/sura/{n}/verse/{v}", f"intertexts/verse/{n:03d}_{v:03d}.json", refresh) or []
            for it in d:
                ids.setdefault(it["id"], []).append(f"{n}:{v}")
        print(f"S{n}: verse lists done; intertext ids so far {len(ids)}", file=sys.stderr)
    for i in sorted(ids):
        jget(src, f"intertexts/{i}", f"intertexts/record/{i}.json", refresh)
    rebuild_intertexts(src)


def fetched_suras_it(src: Source) -> set:
    return {int(p.stem.split("_")[0]) for p in (src.raw / "intertexts" / "verse").glob("*.json")}


def rebuild_intertexts(src: Source):
    suras = fetched_suras_it(src)
    ids = set()
    for p in (src.raw / "intertexts" / "verse").glob("*.json"):
        try:
            ids |= {it["id"] for it in json.loads(p.read_bytes())["data"]}
        except Exception as e:  # a broken raw page: its intertexts are missing until it is fetched again
            print(f"WARNING: unreadable intertext page {p}: {type(e).__name__}: {e}", file=sys.stderr)
    segs = []
    for i in sorted(ids):
        p = src.raw / "intertexts" / "record" / f"{i}.json"
        if p.exists():
            segs += it_segments(json.loads(p.read_bytes())["data"], suras)
    segs.sort(key=lambda s: (s["s"], s["a"], s["tuk_id"]))
    src.segments_path().unlink(missing_ok=True)
    src.upsert_segments(segs)
    per = {}
    for s in segs:
        per[s["s"]] = per.get(s["s"], 0) + 1
    print(f"intertext segments: {len(segs)} from {len(ids)} records; per sura {dict(sorted(per.items()))}")
    src.update_source(dict(META_IT, coverage="verse lists fetched for suras " + ",".join(map(str, sorted(suras)))),
                      urls=[f"{API}/intertexts/sura/<s>/verse/<v>", f"{API}/intertexts/<id>"],
                      extra={"segments_per_sura": {str(k): v for k, v in sorted(per.items())},
                             "suras_without_intertexts": sorted(suras - set(per))})


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["commentary", "intertexts", "all", "reparse"])
    ap.add_argument("suras", nargs="*")
    ap.add_argument("--refresh", action="store_true")
    a = ap.parse_args()
    suras = nums(a.suras)
    if a.mode in ("commentary", "all"):
        do_commentary(Source(SID), suras, a.refresh)
    if a.mode in ("intertexts", "all"):
        do_intertexts(Source(SID_IT), suras, a.refresh)
    if a.mode == "reparse":
        src = Source(SID)
        segs = []
        for p in sorted((src.raw / "commentary").glob("sura_*.json")):
            segs += parse_commentary(int(p.stem.split("_")[1]), json.loads(p.read_bytes())["data"])
        src.segments_path().unlink(missing_ok=True)
        src.upsert_segments(segs)
        finalize_commentary(src)
        rebuild_intertexts(Source(SID_IT))


if __name__ == "__main__":
    main()
