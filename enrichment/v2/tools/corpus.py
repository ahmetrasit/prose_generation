#!/usr/bin/env python3
"""The enrichment corpus: import what is already local, index everything, look things up.

Every source lives in enrichment/corpus/<ID>/ (source.json + segments.jsonl; see enrichment/corpus/README.md).
Fetchers under enrichment/v2/fetch/ write new sources there; `import-local` writes the sources this machine
already holds (the v1 tafsir slice, hadith, the classical lexica, the project dictionary, the Qur'an text, the
qirāʾāt table). `build` indexes every segments.jsonl into enrichment/corpus/corpus.sqlite (FTS5).

  corpus.py import-local [--only ID,...]
  corpus.py build
  corpus.py sources [--kind tafsir]                 list sources with coverage and access
  corpus.py get TAB:107:3 [MUS:2985 ...] [--from N]  print segments by locator (--from: page a long one)
  corpus.py ayah 107:3 [--kind tafsir,meal]         every segment tied to an ayah (ranges included)
  corpus.py search 'الماعون' [--src TAB-FULL,FARRA] [--kind tafsir] [--surah 107] [--n 10] [--chars 300]
                                                   [--sahih] [--exact] [--no-translations]

Read commands accept --no-translations to omit extra English/Turkish translations while retaining
the primary text, source notes and attribution/grade flags.

Search matches word prefixes by default (Arabic normalised: no tashkīl, unified alef/yā/tāʾ marbūṭa/hamza
carriers; Turkish: case and diacritics folded). Hadith segments carry `sahih` (Bukhārī/Muslim, or every named
grader in the dataset says sahih); `--sahih` keeps only those. Bible/intertext sources are never indexed here.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
import shutil
import sqlite3
import sys
import unicodedata
from datetime import date
from pathlib import Path

PG = Path(__file__).resolve().parents[3]
PROJECTS = PG.parent
CORPUS = PG / "enrichment" / "corpus"
INDEX = CORPUS / "corpus.sqlite"
INDEX_INTERTEXT = CORPUS / "corpus_intertext.sqlite"  # the Bible pass: kind intertext only (--intertext)
INTERTEXT = False
SHOW_TRANSLATIONS = True
V1 = PG / "enrichment" / "v1" / "corpus"
QD = PROJECTS / "quran-data" / "data"
LEX = PROJECTS / "quran-roots" / "_corpus" / "lexicons" / "cache"
CACHE = PG / "enrichment" / "v2" / ".cache"
EXCLUDED_KINDS = {"intertext"}  # the separate non-Islamic pass; never in this index

# ---------------------------------------------------------------- normalisation

_AR_DIAC = re.compile(r"[ؐ-ًؚ-ٰٟۖ-ۭـ]")
_AR_MAP = str.maketrans({"أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ى": "ي", "ة": "ه", "ؤ": "و", "ئ": "ي"})
_TR_MAP = str.maketrans({"ı": "i", "İ": "i", "I": "i"})


def norm(text: str) -> str:
    """One normal form for Arabic, Turkish and English, used both for indexing and for queries."""
    text = unicodedata.normalize("NFKC", text or "")
    text = _AR_DIAC.sub("", text).translate(_AR_MAP).translate(_TR_MAP).lower()
    text = "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c)
                   or "؀" <= c <= "ۿ")
    return re.sub(r"\s+", " ", text)


# ---------------------------------------------------------------- writing sources

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def source_dir(sid: str) -> Path:
    """A source's directory: enrichment/corpus/<ID>/, or a grouped one (ACADEMIC/<ID>/) when that holds its record."""
    d = CORPUS / sid
    if (d / "source.json").exists():
        return d
    grouped = [p.parent for p in CORPUS.glob(f"*/{sid}/source.json") if "raw" not in p.parts]
    return grouped[0] if len(grouped) == 1 else d


def write_source(meta: dict, segments) -> int:
    d = source_dir(meta["id"])
    d.mkdir(parents=True, exist_ok=True)
    n = 0
    tmp = d / "segments.jsonl.tmp"
    with tmp.open("w", encoding="utf-8") as f:
        for seg in segments:
            seg.setdefault("s", None)
            seg.setdefault("a", None)
            seg.setdefault("a_end", seg.get("a"))
            f.write(json.dumps(seg, ensure_ascii=False) + "\n")
            n += 1
    tmp.replace(d / "segments.jsonl")
    meta = {"access": "yerel", "fetched_at": date.today().isoformat(), **meta, "segments": n}
    (d / "source.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return n


def _gunzip(src: Path, name: str) -> Path:
    CACHE.mkdir(parents=True, exist_ok=True)
    dst = CACHE / name
    if not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime:
        opener = gzip.open if src.suffix == ".gz" else None
        if opener:
            with opener(src) as f, dst.open("wb") as g:
                shutil.copyfileobj(f, g)
        else:  # .zst
            import subprocess
            subprocess.run(["zstd", "-dqf", str(src), "-o", str(dst)], check=True)
    return dst


# ---------------------------------------------------------------- importers (sources already on this machine)

V1_TAFSIR = {  # quran-tafsir.net slug -> (ID, author, work, death AH, tradition)
    "tabary": ("TAB", "al-Ṭabarī", "Jāmiʿ al-bayān", 310, "sunni-rivaya"),
    "katheer": ("IBNKATHIR", "Ibn Kathīr", "Tafsīr al-Qurʾān al-ʿaẓīm", 774, "sunni-rivaya"),
    "seoty": ("DURR", "al-Suyūṭī", "al-Durr al-manthūr", 911, "sunni-rivaya"),
    "zamakhshary": ("KASHSHAF", "al-Zamakhsharī", "al-Kashshāf", 538, "mutazili-dirayet"),
    "alrazy": ("RAZI", "Fakhr al-Dīn al-Rāzī", "Mafātīḥ al-ghayb", 606, "sunni-dirayet"),
    "baidawy": ("BAYDAWI", "al-Bayḍāwī", "Anwār al-tanzīl", 685, "sunni-dirayet"),
    "beqaay": ("BIQAI", "al-Biqāʿī", "Naẓm al-durar", 885, "nazm"),
    "qortoby": ("QURTUBI", "al-Qurṭubī", "al-Jāmiʿ li-aḥkām al-Qurʾān", 671, "sunni-dirayet"),
    "atia": ("IBNATIYYA", "Ibn ʿAṭiyya", "al-Muḥarrar al-wajīz", 542, "sunni-dirayet"),
    "hayyan": ("ABUHAYYAN", "Abū Ḥayyān", "al-Baḥr al-muḥīṭ", 745, "sunni-dirayet"),
    "alusy": ("ALUSI", "al-Ālūsī", "Rūḥ al-maʿānī", 1270, "sunni-dirayet"),
    "baghawy": ("BAGHAWI", "al-Baghawī", "Maʿālim al-tanzīl", 516, "sunni-rivaya"),
    "mawardy": ("MAWARDI", "al-Māwardī", "al-Nukat wa-l-ʿuyūn", 450, "sunni-dirayet"),
    "wahidy": ("WAHIDI-QT", "al-Wāḥidī", "al-Wajīz fī tafsīr al-Kitāb al-ʿazīz (per-ayah slice; the site's book list names it)", 468,
               "sunni"),
    "ashour": ("IBNASHUR", "Ibn ʿĀshūr", "al-Taḥrīr wa-l-tanwīr", 1393, "modern-bayani"),
    "nasafy": ("NASAFI", "al-Nasafī", "Madārik al-tanzīl", 710, "sunni-dirayet"),
}


def import_v1_tafsir(only: set[str]) -> None:
    index = {}
    for line in (V1 / "tafsir_index.jsonl").read_text(encoding="utf-8").splitlines():
        r = json.loads(line)
        index[(r["book"], r["surah"], r["ayah"])] = r
    for slug, (sid, author, work, death, trad) in V1_TAFSIR.items():
        if only and sid not in only:
            continue
        files = sorted((V1 / "tafsir" / slug).glob("*_*.txt"),
                       key=lambda p: tuple(int(x) for x in p.stem.split("_")))
        segs, surahs = [], set()
        for p in files:
            s, a = (int(x) for x in p.stem.split("_"))
            surahs.add(s)
            segs.append({"seg": f"{sid}:{s}:{a}", "s": s, "a": a, "text": p.read_text(encoding="utf-8").strip(),
                         "url": index.get((slug, s, a), {}).get("url")})
        n = write_source({"id": sid, "title": work, "author": author, "death_ah": death, "kind": "tafsir",
                          "tradition": trad, "language": "ar", "edition": "quran-tafsir.net per-ayah pages (div.nass)",
                          "locator": "ayah", "coverage": f"surahs {sorted(surahs)} (per-ayah slice)",
                          "urls": [f"https://quran-tafsir.net/{slug}/sura<s>-aya<a>.html"],
                          "files": {"enrichment/v1/corpus/tafsir_index.jsonl": "per-page sha256 of the raw HTML"},
                          "licence": "public web pages; local research copy",
                          "notes": "Per-ayah slice for the surahs in coverage. The page for an ayah can open with the"
                                   " surah introduction. Whole-book text, where fetched, is a separate source (<ID>-FULL)."},
                         segs)
        print(f"{sid}: {n} segments")


HADITH = {"bukhari": ("BUKHARI", "Ṣaḥīḥ al-Bukhārī"), "muslim": ("MUSLIM", "Ṣaḥīḥ Muslim"),
          "abudawud": ("ABUDAWUD", "Sunan Abī Dāwūd"), "tirmidhi": ("TIRMIDHI", "Jāmiʿ al-Tirmidhī"),
          "nasai": ("NASAI", "Sunan al-Nasāʾī"), "ibnmajah": ("IBNMAJAH", "Sunan Ibn Māja"),
          "malik": ("MALIK", "al-Muwaṭṭaʾ")}
_NOT_SAHIH = re.compile(r"isna+d|hasan|da.?e?e?f|weak|munkar|mawdu|shadh|maqtu|mawquf", re.I)


def is_sahih(book: str, grades: list[dict]) -> tuple[bool, list[str]]:
    """Bukhārī/Muslim by collection; otherwise every named grader must say sahih (not 'sahih isnad', not 'hasan sahih')."""
    if book in ("bukhari", "muslim"):
        return True, ["Buhârî" if book == "bukhari" else "Müslim"]
    if not grades:
        return False, []
    names = []
    for g in grades:
        text = (g.get("grade") or "").strip()
        if not re.match(r"^sahih\b", text, re.I) or _NOT_SAHIH.search(text):
            return False, []
        names.append(g.get("name") or "?")
    return True, names


def import_hadith(only: set[str]) -> None:
    db = sqlite3.connect(V1 / "hadith" / "hadith.sqlite")
    for book, (sid, title) in HADITH.items():
        if only and sid not in only:
            continue
        segs, n_sahih = [], 0
        for _, b, num, ref, gr, ara, eng, tur in db.execute("SELECT * FROM h WHERE book=? ORDER BY num", (book,)):
            grades = json.loads(gr) if gr else []
            ok, by = is_sahih(book, grades)
            n_sahih += ok
            num_s = str(int(num)) if num == int(num) else str(num)
            segs.append({"seg": f"{sid}:{num_s}", "text": ara, "en": eng, "tr": tur, "sahih": ok,
                         "graded_by": by, "grades": grades, "reference": json.loads(ref) if ref else None})
        n = write_source({"id": sid, "title": title, "kind": "hadith", "tradition": "sunni-hadith", "language": "ar",
                          "edition": "fawazahmed0/hadith-api editions (ara/eng/tur), fetched 2026-10-02",
                          "locator": "hadith", "coverage": "whole book",
                          "urls": [f"https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/ara-{book}.json"],
                          "licence": "dataset licence (Unlicense); translations as in the dataset",
                          "notes": f"Dataset numbering, not sunnah.com numbering: cite <ID>:<number> and the opening words. "
                                   f"sahih={n_sahih} of {len(segs)} under the project rule (Sahihayn by collection; "
                                   f"other books only when every named grader says sahih)."}, segs)
        print(f"{sid}: {n} segments, {n_sahih} sahih")


CLASSICAL = {"ayn": ("AYN", "Kitāb al-ʿAyn", "al-Khalīl b. Aḥmad", 170),
             "jamhara": ("JAMHARA", "Jamharat al-lugha", "Ibn Durayd", 321),
             "tahdhib": ("TAHDHIB", "Tahdhīb al-lugha", "al-Azharī", 370),
             "sihah": ("SIHAH", "al-Ṣiḥāḥ", "al-Jawharī", 393),
             "maqayis": ("MAQAYIS", "Maqāyīs al-lugha", "Ibn Fāris", 395),
             "mufradat": ("MUFRADAT", "al-Mufradāt fī gharīb al-Qurʾān", "al-Rāghib al-Iṣfahānī", 502)}


def import_classical(only: set[str]) -> None:
    """The six lexica the project dictionary is built from, as routed per root (furuq superset, v4 fallback)."""
    furuq = sqlite3.connect(_gunzip(QD / "lexicon" / "furuq.sqlite.zst", "furuq.sqlite"))
    v4 = sqlite3.connect(_gunzip(QD / "lexicon" / "v4.sqlite.gz", "v4.sqlite"))
    for src, (sid, title, author, death) in CLASSICAL.items():
        if only and sid not in only:
            continue
        segs, seen, used = [], set(), {}
        for db, label in ((furuq, "furuq"), (v4, "v4")):
            for rid, root, head, page, text, route in db.execute(
                    "SELECT root_id, root_norm, headword, page_or_volume_ref, entry_text_clean, route_status "
                    "FROM dictionary_entries WHERE source_id=? ORDER BY root_id, id", (src,)):
                if (rid, text[:200]) in seen or text.strip() in ("", "-"):
                    continue
                seen.add((rid, text[:200]))
                key = root.replace(" ", "")
                used[key] = used.get(key, 0) + 1
                segs.append({"seg": f"{sid}:{key}" + ("" if used[key] == 1 else f"#{used[key]}"),
                             "head": head, "root": root, "root_id": rid, "page": None if page in ("", "-") else page,
                             "route": route, "via": label, "text": text})
        n = write_source({"id": sid, "title": title, "author": author, "death_ah": death, "kind": "lexicon",
                          "tradition": "classical-lexicography", "language": "ar",
                          "edition": "digital text as routed per root by the project dictionary (quran-data lexicon furuq/v4)",
                          "locator": "entry", "coverage": "roots routed by the project dictionary",
                          "urls": [], "files": {"quran-data/data/lexicon/furuq.sqlite.zst": sha256(QD / "lexicon" / "furuq.sqlite.zst"),
                                                "quran-data/data/lexicon/v4.sqlite.gz": sha256(QD / "lexicon" / "v4.sqlite.gz")},
                          "licence": "digital editions as ingested by quran-roots; local research copy",
                          "notes": "route = exact or variant routing of the entry to the root (see the dictionary). Some "
                                   "entries are routed by headword and may belong to a neighbouring root; check the head."},
                         segs)
        print(f"{sid}: {n} segments")


def _lexicon_rows(db: Path, sql: str):
    con = sqlite3.connect(db)
    yield from con.execute(sql)


def import_other_lexica(only: set[str]) -> None:
    sh = LEX / "shards"
    specs = [
        ("LISAN", "Lisān al-ʿArab", "Ibn Manẓūr", 711, "classical-lexicography", "ar",
         [sh / "lisan_compact.sqlite"], "SELECT root_norm, headword, entry_text_clean, lisan_ref FROM lisan_entries"),
        ("LANE", "An Arabic-English Lexicon", "E. W. Lane", None, "orientalist-lexicography", "en",
         sorted(sh.glob("lane_compact__part*.sqlite")),
         "SELECT root_norm, coalesce(lane_headword, wizsk_lane_headword), entry_text_clean, lane_ref FROM lane_entries"),
        ("QAMUS", "al-Qāmūs al-muḥīṭ", "al-Fīrūzābādī", 817, "classical-lexicography", "ar",
         [LEX / "openiti_extra" / "qamus.sqlite"],
         "SELECT root_norm, headword, entry_text_clean, page_or_volume_ref FROM lexicon_entries"),
        ("VASIT", "al-Muʿjam al-wasīṭ", "Majmaʿ al-lugha al-ʿarabiyya", None, "modern-dictionary", "ar",
         [sh / "wizsk_wasith.sqlite"], "SELECT root_norm, headword, entry_text_clean, page_or_volume_ref FROM lexicon_entries"),
        ("MUHIT", "Muḥīṭ al-muḥīṭ", "Buṭrus al-Bustānī", None, "modern-dictionary", "ar",
         sorted(sh.glob("wizsk_muhit__part*.sqlite")),
         "SELECT root_norm, headword, entry_text_clean, page_or_volume_ref FROM lexicon_entries"),
        ("HANSWEHR", "A Dictionary of Modern Written Arabic", "Hans Wehr", None, "modern-dictionary", "en",
         [sh / "wizsk_hanswehr.sqlite"], "SELECT root_norm, headword, entry_text_clean, page_or_volume_ref FROM lexicon_entries"),
    ]
    for sid, title, author, death, trad, lang, dbs, sql in specs:
        if only and sid not in only:
            continue
        segs, used = [], {}
        for db in dbs:
            for root, head, text, ref in _lexicon_rows(db, sql):
                if not (text or "").strip():
                    continue
                key = (root or head or "?").replace(" ", "")
                used[key] = used.get(key, 0) + 1
                segs.append({"seg": f"{sid}:{key}" + ("" if used[key] == 1 else f"#{used[key]}"), "head": head,
                             "root": root, "page": ref or None, "text": text})
        modern = trad == "modern-dictionary"
        n = write_source({"id": sid, "title": title, "author": author, "death_ah": death,
                          "kind": "lexicon", "tradition": trad, "language": lang,
                          "edition": "quran-roots lexicon shards (wizsk / OpenITI digital texts)", "locator": "entry",
                          "coverage": "whole dictionary", "files": {str(p.relative_to(PROJECTS)): sha256(p) for p in dbs},
                          "licence": "digital editions as ingested by quran-roots; local research copy",
                          "notes": ("MODERN dictionary: cite only inside anlam_tarihi as evidence of later drift, never as "
                                    "attestation of a Qur'anic sense." if modern else "")}, segs)
        print(f"{sid}: {n} segments")
    ctx = LEX / "openiti_context.sqlite"
    for sid, src, title, author, death in (("ASAS", "asas_balagha", "Asās al-balāgha", "al-Zamakhsharī", 538),
                                           ("SIBAWAYH", "sibawayh", "al-Kitāb", "Sībawayh", 180)):
        if only and sid not in only:
            continue
        segs = []
        for i, (head, text, path) in enumerate(_lexicon_rows(ctx, f"SELECT section_title, entry_text_clean, section_path "
                                                                   f"FROM audit_corpus_entries WHERE source='{src}' ORDER BY id"), 1):
            segs.append({"seg": f"{sid}:{(head or str(i)).replace(' ', '')}#{i}", "head": head, "text": text, "page": path})
        n = write_source({"id": sid, "title": title, "author": author, "death_ah": death,
                          "kind": "lexicon" if sid == "ASAS" else "grammar", "tradition": "classical", "language": "ar",
                          "edition": "OpenITI text as segmented by quran-roots (openiti_context.sqlite)", "locator": "entry",
                          "coverage": "whole book", "files": {str(ctx.relative_to(PROJECTS)): sha256(ctx)},
                          "licence": "OpenITI; local research copy", "notes": ""}, segs)
        print(f"{sid}: {n} segments")


def import_project(only: set[str]) -> None:
    """PROJE: the project dictionary (Turkish entries transferred from ../dictionary), one segment per branch."""
    if only and "PROJE" not in only:
        return
    tr = QD / "dictionary" / "tr"
    manifest = json.loads((tr / "MANIFEST.json").read_text(encoding="utf-8"))
    segs = []
    for f in sorted(tr.glob("*_entry.json")):
        e = json.loads(f.read_text(encoding="utf-8"))
        for b in e.get("branches", []):
            rid, bid = b["branch_ref"].split("/")[0], b["branch_ref"].split("/")[-1]
            g = b.get("concept_gloss")
            g = (g.get("text") if isinstance(g, dict) else g) or ""
            senses = " · ".join(x.get("target_gloss", "") for x in b.get("lexical_glosses", []) if x.get("target_gloss"))
            segs.append({"seg": f"PROJE:{rid}/{bid}", "root_id": rid, "head": g, "image_ar": b.get("branch_image_ar", ""),
                         "text": f"{g} — {senses}\n{b.get('source_phrase_ar', '')}", "sources": b.get("sources")})
    n = write_source({"id": "PROJE", "title": "Project dictionary (Turkish entries)", "author": "this project",
                      "kind": "lexicon", "tradition": "project", "language": "tr",
                      "edition": f"quran-data/data/dictionary/tr, transferred from ../dictionary at commit {manifest.get('sourceCommit')}",
                      "locator": "entry", "coverage": f"{manifest.get('entryCount')} root entries",
                      "files": {"quran-data/data/dictionary/tr/MANIFEST.json": sha256(tr / "MANIFEST.json")},
                      "licence": "project", "source_commit": manifest.get("sourceCommit"),
                      "notes": "Authoritative dictionary. Locator PROJE:<root_id>/<branch>; the base's inline tags cite "
                               "branches as \"<root letters>,Bnnn\"."}, segs)
    print(f"PROJE: {n} segments")


def import_quran(only: set[str]) -> None:
    if not only or "QURAN" in only:
        segs = []
        for line in (QD / "text" / "quran-uthmani.tsv").read_text(encoding="utf-8").splitlines():
            ref, _, ar = line.partition("|")
            s, a = (int(x) for x in ref.split(":"))
            if a:
                segs.append({"seg": f"QURAN:{s}:{a}", "s": s, "a": a, "text": ar.strip().lstrip("﻿")})
        print("QURAN:", write_source({"id": "QURAN", "title": "al-Qurʾān (Uthmani text)", "kind": "quran", "language": "ar",
                                      "edition": "quran-data/data/text/quran-uthmani.tsv (tanzil Uthmani; basmala is :0)",
                                      "locator": "ayah", "coverage": "1-114", "licence": "tanzil text licence",
                                      "files": {"quran-data/data/text/quran-uthmani.tsv": sha256(QD / "text" / "quran-uthmani.tsv")},
                                      "notes": ""}, segs))
    if not only or "QIRAAT-ER" in only:
        tsv = PROJECTS / "quran" / "_project_corpus" / "qiraat.tsv"
        segs = []
        lines = tsv.read_text(encoding="utf-8").splitlines()
        cols = lines[0].split("\t")
        for line in lines[1:]:
            r = dict(zip(cols, line.split("\t")))
            s, a, w = (int(x) for x in r["tsv_word_ref"].split(":"))
            segs.append({"seg": f"QIRAAT-ER:{s}:{a}:{w}#{r['qiraat_variant_order']}", "s": s, "a": a,
                         "head": r["qiraat_arabic"], "text": f"{r['qiraat_arabic']} ({r['qiraat_transliteration']}) — "
                         f"{r['qiraat_reader_set']}, {r['qiraat_transmission_type']}: {r['qiraat_note']}",
                         "transmission": r["qiraat_transmission_type"]})
        print("QIRAAT-ER:", write_source({"id": "QIRAAT-ER", "title": "Qirāʾāt variants per word", "kind": "qiraat",
                                          "language": "en", "edition": "quran/_project_corpus/qiraat.tsv (from erquran.org)",
                                          "locator": "ayah", "coverage": "variant-bearing words, 1-114",
                                          "files": {"quran/_project_corpus/qiraat.tsv": sha256(tsv)},
                                          "licence": "erquran.org data as extracted by the project",
                                          "notes": "Secondary, single source. Prefer Ibn Mujāhid / ḥujja works for claims."},
                                         segs))


IMPORTERS = [import_v1_tafsir, import_hadith, import_classical, import_other_lexica, import_project, import_quran]


# ---------------------------------------------------------------- index

def sources() -> list[dict]:
    out = []
    # one level, plus grouped pointer records (ACADEMIC/<ID>/source.json); never anything under raw/
    paths = list(CORPUS.glob("*/source.json")) + [p for p in CORPUS.glob("*/*/source.json") if "raw" not in p.parts]
    for p in sorted(paths):
        try:
            out.append(json.loads(p.read_text(encoding="utf-8")))
        except json.JSONDecodeError as e:
            print(f"bad source.json {p}: {e}", file=sys.stderr)
    return out


def flat(v) -> str:
    """Segment fields are usually strings; some sources give notes as lists or objects."""
    if isinstance(v, str):
        return v
    if isinstance(v, list):
        return " ".join(flat(x) for x in v)
    if isinstance(v, dict):
        return " ".join(flat(x) for x in v.values())
    return "" if v is None else str(v)


def running_calls() -> list[str]:
    """Enrichment calls started without a run.log.json (and not confirmed dead): they read this index."""
    work = PG / "enrichment" / "v2" / "work"
    pattern = "s*/ehlikitap.*" if INTERTEXT else "s*/zengin.*"  # each pass reads only its own index
    dirs = sorted(work.glob(pattern)) + ([] if INTERTEXT else sorted(work.glob("s*/okuma.*/*")))  # reading calls
    return [str(d.relative_to(work)) for d in dirs
            if (d / "started.json").exists() and not (d / "run.log.json").exists() and not (d / "dead.json").exists()]


def build(force: bool = False) -> None:
    if running_calls() and not force:
        raise SystemExit(f"enrichment calls are running {running_calls()}: rebuilding the index would change what "
                         f"their validator sees; wait for them (--force only if the user agrees)")
    index = INDEX_INTERTEXT if INTERTEXT else INDEX
    tmp = index.with_suffix(".sqlite.tmp")
    tmp.unlink(missing_ok=True)
    con = sqlite3.connect(tmp)
    con.executescript("""
        CREATE TABLE src(id TEXT PRIMARY KEY, kind TEXT, access TEXT, meta TEXT);
        CREATE TABLE seg(id INTEGER PRIMARY KEY, seg TEXT UNIQUE, src TEXT, s INT, a INT, a_end INT,
                         head TEXT, text TEXT, extra TEXT);
        CREATE INDEX seg_ayah ON seg(s, a, a_end);
        CREATE INDEX seg_src ON seg(src);
        CREATE VIRTUAL TABLE f USING fts5(body, content='', tokenize='unicode61 remove_diacritics 2');
        CREATE TABLE ref(s INT, a INT, a_end INT, seg_id INT);
        CREATE INDEX ref_ayah ON ref(s, a, a_end);
    """)
    total = 0
    for meta in sources():
        kind = meta.get("kind")
        if INTERTEXT:  # the Bible pass index: the intertext sources plus what every pass may cite (Quran, modern, reference)
            if kind not in {"intertext", "quran", "modern", "reference"}:
                continue
        elif kind in EXCLUDED_KINDS:  # the Islamic index never holds intertext
            continue
        con.execute("INSERT INTO src VALUES(?,?,?,?)", (meta["id"], meta.get("kind"), meta.get("access"),
                                                         json.dumps(meta, ensure_ascii=False)))
        path = source_dir(meta["id"]) / "segments.jsonl"
        if not path.exists():
            if meta.get("access") != "hafiza":  # memory pointers have no text by design
                print(f"WARNING: {meta['id']}: no segments.jsonl; not indexed", file=sys.stderr)
            continue
        n = 0
        with path.open(encoding="utf-8") as f:
            for line in f:
                r = json.loads(line)
                extra = {k: v for k, v in r.items() if k not in ("seg", "s", "a", "a_end", "head", "text")}
                try:
                    cur = con.execute("INSERT INTO seg(seg,src,s,a,a_end,head,text,extra) VALUES(?,?,?,?,?,?,?,?)",
                                      (r["seg"], meta["id"], r.get("s"), r.get("a"), r.get("a_end") or r.get("a"),
                                       r.get("head"), r.get("text", ""), json.dumps(extra, ensure_ascii=False)))
                except sqlite3.IntegrityError:
                    print(f"duplicate locator {r['seg']} in {meta['id']}", file=sys.stderr)
                    continue
                # ayat the text cites explicitly ("Q 2:255", "20:125-7"), kept apart from its tie: a reference work
                # or a note is reachable from every ayah it discusses without being tied to it (`corpus.py cites`)
                for ref in r.get("refs") or []:
                    rs, ra, rb = parse_ref(ref)
                    con.execute("INSERT INTO ref VALUES(?,?,?,?)", (rs, ra, rb, cur.lastrowid))
                body = " ".join(flat(r.get(k)) for k in ("head", "text", "en", "tr", "notes") if r.get(k))
                con.execute("INSERT INTO f(rowid, body) VALUES(?,?)", (cur.lastrowid, norm(body)))
                n += 1
        total += n
        print(f"{meta['id']:22} {n:>8}", flush=True)
    con.commit()
    con.close()
    tmp.replace(index)
    print(f"indexed {total} segments -> {index.relative_to(PG)}")


STAMP = CORPUS / "corpus.sqlite.gz.stamp.json"   # versioned: what the committed corpus.sqlite.gz.partNN hold


def fresh() -> int:
    """Is the index current? Every source.json must equal the copy the index stored at build time (a new source,
    a removed one, or a changed record means rebuild), and no segments.jsonl may be newer than the index. Also says
    whether the committed gz parts (STAMP) hold this index. Prints STALE lines; returns 1 when stale."""
    index = INDEX_INTERTEXT if INTERTEXT else INDEX
    if not index.exists():
        print(f"STALE: {index.relative_to(PG)} missing (reassemble the parts: cat corpus.sqlite.gz.part* | gunzip, or build)")
        return 1
    con = sqlite3.connect(index.resolve().as_uri() + "?mode=ro", uri=True)
    stored = {i: json.loads(m) for i, m in con.execute("SELECT id, meta FROM src")}
    built = index.stat().st_mtime
    stale = []
    for meta in sources():
        kind, sid = meta.get("kind"), meta["id"]
        if (INTERTEXT and kind not in {"intertext", "quran", "modern", "reference"}) or \
                (not INTERTEXT and kind in EXCLUDED_KINDS):
            continue
        if sid not in stored:
            stale.append(f"{sid}: source not in the index")
        elif stored.pop(sid) != meta:
            stale.append(f"{sid}: source.json changed since the index was built")
        seg = source_dir(sid) / "segments.jsonl"
        if seg.exists() and seg.stat().st_mtime > built:
            stale.append(f"{sid}: segments.jsonl newer than the index")
    stale += [f"{sid}: in the index, no source.json any more" for sid in stored]
    for x in stale:
        print(f"STALE {x}")
    print(f"{index.relative_to(PG)}: " + ("current" if not stale else f"{len(stale)} problem(s): rebuild with "
                                          "`corpus.py build` (no enrichment calls running)"))
    if not INTERTEXT:
        try:
            st = json.loads(STAMP.read_text()) if STAMP.exists() else None
        except (OSError, ValueError) as e:
            st = f"unreadable ({e})"
        if isinstance(st, dict):
            same = st.get("sqlite_sha256") == sha256(index)
            print(f"committed gz parts ({st.get('built_at')}): " + ("hold this index" if same else
                  "DIFFER from this index (regenerate them with tools/corpus_parts.sh, then sources_sync.py --commit)"))
        else:
            print(f"committed gz parts: stamp {st or 'missing'} (corpus.sqlite.gz.stamp.json); regenerate with "
                  "tools/corpus_parts.sh")
    return 1 if stale else 0


def parse_ref(ref: str) -> tuple[int, int, int]:
    """'2:255' -> (2, 255, 255); '20:125-127' -> (20, 125, 127)."""
    s, rest = ref.split(":")
    a, _, b = rest.partition("-")
    return int(s), int(a), int(b or a)


def connect() -> sqlite3.Connection:
    index = INDEX_INTERTEXT if INTERTEXT else INDEX
    if not index.exists():
        sys.exit(f"no index: run `corpus.py {'--intertext ' if INTERTEXT else ''}build` first")
    return sqlite3.connect(index)


# Every get/ayah/search call prints at most CALL_LIMIT characters of segment text, and everything it prints stays
# under OUT_BYTES bytes (user, 2026-10-05: an agent re-reads all its tool output on every later turn, and Claude
# Code saves an output over ~30,000 BYTES to a file the agent may never read; Arabic is two bytes a character).
# Past the limit a segment is listed only; a cut is always said, with the command for the rest.
CALL_LIMIT = 9_000
OUT_BYTES = 24_000
_used = 0
_unshown: list[str] = []
PREVIEW = False  # search results are previews by design: marked so, never counted as cuts


def show(row, chars: int, start: int = 0) -> None:
    global _used
    seg, src, s, a, a_end, head, text, extra = row
    extra = json.loads(extra or "{}")
    flags = []
    if "sahih" in extra:
        flags.append(f"sahih={extra['sahih']} by={'|'.join(extra.get('graded_by') or []) or '-'}")
    if extra.get("page"):
        flags.append(f"page={extra['page']}")
    # the text's standing, so that an unverified page is never quoted as if checked (user, 2026-10-05)
    if extra.get("text_status"):
        flags.append(f"STATUS: {extra['text_status']}")
    for k, say in (("marker_found", "note marker not found: tie approximate"),
                   ("align_uncertain", "verse alignment uncertain"), ("duplicate", "duplicate of other segments"),
                   ("secondary", "secondary study")):
        if extra.get(k) is (False if k == "marker_found" else True):
            flags.append(say)
    head_line = f"== {seg}" + (f"  [{head}]" if head else "") + ("  " + " ".join(flags) if flags else "")
    room = CALL_LIMIT - _used if CALL_LIMIT else None
    if CALL_LIMIT and _bytes_out() > OUT_BYTES - 3_000:  # leave room for the closing note
        room = 0
    if room is not None and room <= 0:  # listed once, compactly, by close_call()
        _unshown.append(f"{seg}({len(text):,})")
        return
    body = text[start:]
    n = len(body) if not chars else min(chars, len(body))
    if room is not None:
        n = min(n, room)
    shown = body[:n]
    span = f"  [characters {start + 1:,}–{start + n:,} of {len(text):,}]" if (start or n < len(body)) else ""
    print(head_line + span)
    if n < len(body):
        tail = (f" … [preview: `corpus.py get {seg}` for the text]" if PREVIEW else
                f" … [cut: `corpus.py get {seg} --from {start + n}` for the rest]")
    else:
        tail = ""
    print(shown + tail)
    _used += n
    for k in ("en", "tr", "notes"):
        if k in ("en", "tr") and not SHOW_TRANSLATIONS:
            continue
        if extra.get(k):
            v = flat(extra[k])
            v = v if not chars else v[:chars]
            print(f"  {k}: {v}")
            _used += len(v)


class _Counter:
    """stdout that counts the bytes written, so a call can stop before the harness's spill limit."""
    def __init__(self, inner):
        self.inner, self.n = inner, 0

    def write(self, s):
        self.n += len(s.encode("utf-8"))
        return self.inner.write(s)

    def flush(self):
        return self.inner.flush()


def _bytes_out() -> int:
    return getattr(sys.stdout, "n", 0)


def close_call() -> None:
    """The segments past the call's limit, listed once: each locator when few, else per source (count, characters)."""
    if not _unshown:
        return
    if len(_unshown) <= 12:
        listing = " ".join(_unshown)
    else:
        by: dict[str, list[int]] = {}
        for x in _unshown:
            loc, n = x.rsplit("(", 1)
            by.setdefault(loc.split(":")[0], []).append(int(n.rstrip(")").replace(",", "")))
        listing = "; ".join(f"{src} {len(v)} segments {sum(v):,} chars" for src, v in by.items())
    print(f"NOTE: {len(_unshown)} segments not shown (the {CALL_LIMIT:,}-character limit of one call): {listing}. "
          f"Get them in another call; an ayah page's locators and sizes are listed in PACK/ayah/S_A/sources.md")


def cmd_get(locs: list[str], chars: int, start: int = 0) -> None:
    con = connect()
    for loc in locs:
        # the segment and its sub-segments (loc#2 …) by two index lookups; `OR … LIKE` would scan the whole table
        rows = (con.execute("SELECT seg,src,s,a,a_end,head,text,extra FROM seg WHERE seg=?", (loc,)).fetchall()
                + con.execute("SELECT seg,src,s,a,a_end,head,text,extra FROM seg WHERE seg>=? AND seg<? ORDER BY id",
                              (loc + "#", loc + "$")).fetchall())
        if not rows:
            print(f"== {loc}: NOT FOUND")
        for r in rows:
            show(r, chars, start)


def kinds_filter(kinds: str | None) -> tuple[str, list]:
    if not kinds:
        return "", []
    ks = kinds.split(",")
    return f" AND seg.src IN (SELECT id FROM src WHERE kind IN ({','.join('?' * len(ks))}))", ks


def cmd_ayah(ref: str, kinds: str | None, src: str | None, chars: int) -> None:
    con = connect()
    s, a = (int(x) for x in ref.split(":"))
    sql = "SELECT seg,src,s,a,a_end,head,text,extra FROM seg WHERE s=? AND a<=? AND coalesce(a_end,a)>=?"
    args: list = [s, a, a]
    k_sql, k_args = kinds_filter(kinds)
    sql += k_sql
    args += k_args
    if src:
        ids = src.split(",")
        sql += f" AND src IN ({','.join('?' * len(ids))})"
        args += ids
    dups = []
    for r in con.execute(sql + " ORDER BY src, a", args):
        if json.loads(r[7] or "{}").get("duplicate"):
            dups.append(f"{r[0]}({len(r[6] or ''):,})")  # repeats text shown elsewhere: listed, not printed
            continue
        show(r, chars)
    if dups:
        print(f"DUPLICATES not printed (their text is in the segments above): {' '.join(dups)}")
    # segments that cite the ayah without being tied to it: counted here, never silently left out
    cited = cites_rows(con, s, a, src)
    if cited:
        by: dict[str, int] = {}
        for r in cited:
            by[r[1]] = by.get(r[1], 0) + 1
        print(f"CITED ELSEWHERE: {len(cited)} segments not tied to {s}:{a} cite it "
              f"({'; '.join(f'{k} {v}' for k, v in sorted(by.items()))}): `corpus.py cites {s}:{a}` lists them")


def cites_rows(con, s: int, a: int, src: str | None = None) -> list:
    sql = ("SELECT DISTINCT seg.seg,seg.src,seg.s,seg.a,seg.a_end,seg.head,seg.text,seg.extra FROM ref JOIN seg "
           "ON seg.id=ref.seg_id WHERE ref.s=? AND ref.a<=? AND ref.a_end>=? "
           "AND NOT (coalesce(seg.s,0)=? AND seg.a<=? AND coalesce(seg.a_end,seg.a)>=?)")
    args: list = [s, a, a, s, a, a]
    if src:
        ids = src.split(",")
        sql += f" AND seg.src IN ({','.join('?' * len(ids))})"
        args += ids
    return con.execute(sql + " ORDER BY seg.src, seg.id", args).fetchall()


def cmd_cites(ref: str, src: str | None, chars: int) -> None:
    """Every segment that cites the ayah without being tied to it, with a snippet centred on the citation."""
    con = connect()
    s, a = (int(x) for x in ref.split(":"))
    rows = cites_rows(con, s, a, src)
    print(f"{len(rows)} segments cite {s}:{a} (not tied to it)")
    for r in rows:
        text = r[6] or ""
        m = re.search(rf"(?<![\d:]){s}\s*:\s*{a}(?!\d)", text) or re.search(rf"(?<![\d:]){s}\s*:\s*\d", text)
        at = max(0, (m.start() if m else 0) - chars // 2)
        global _used
        if _bytes_out() > OUT_BYTES - 3_000 or (CALL_LIMIT and _used >= CALL_LIMIT):
            _unshown.append(f"{r[0]}({len(text):,})")
            continue
        snippet = text[at:at + chars].replace("\n", " ")
        print(f"== {r[0]}" + (f"  [{r[5]}]" if r[5] else "") + f"  [characters {at + 1:,}–{at + len(snippet):,} of "
              f"{len(text):,}]")
        print(("… " if at else "") + snippet + (f" … [preview: `corpus.py get {r[0]}` for the text]"
                                               if at + len(snippet) < len(text) else ""))
        _used += len(snippet)


def cmd_search(q: str, a) -> None:
    con = connect()
    words = norm(q).split()
    fq = " ".join(f'"{w}"' + ("" if a.exact else "*") for w in words)
    sql = ("SELECT seg.seg,seg.src,seg.s,seg.a,seg.a_end,seg.head,seg.text,seg.extra FROM f JOIN seg ON seg.id=f.rowid "
           "WHERE f MATCH ?")
    args: list = [fq]
    if a.src:
        ids = a.src.split(",")
        sql += f" AND seg.src IN ({','.join('?' * len(ids))})"
        args += ids
    k_sql, k_args = kinds_filter(a.kind)
    sql += k_sql
    args += k_args
    if a.surah:
        sql += " AND seg.s=?"
        args.append(a.surah)
    if a.sahih:
        sql += " AND json_extract(seg.extra,'$.sahih')=1"
    rows = con.execute(sql + " ORDER BY rank LIMIT ?", args + [a.n]).fetchall()
    print(f"{len(rows)} shown (limit {a.n}) for {fq}")
    for r in rows:
        show(r, a.chars)


def cmd_sources(kind: str | None) -> None:
    for m in sources():
        if kind and m.get("kind") != kind:
            continue
        print(f"{m['id']:22} {m.get('kind', ''):12} {m.get('access', ''):7} {str(m.get('segments', '-')):>8}  "
              f"{m.get('author', '') or ''} — {m.get('title', '')}  [{m.get('coverage', '')}]")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-i", "--intertext", action="store_true",
                    help="the Bible pass index (corpus_intertext.sqlite: WLC, SBLGNT, KJV, SEFARIA, CORPUSCORANICUM-INTERTEXT); "
                         "before the subcommand")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("import-local")
    p.add_argument("--only", default="")
    p = sub.add_parser("fresh", help="is the index current with every source? (run before tier 1 and meal builds)")
    p = sub.add_parser("build")
    p.add_argument("--force", action="store_true", help="build even while enrichment calls are running")
    p = sub.add_parser("sources")
    p.add_argument("--kind")
    p = sub.add_parser("get")
    p.add_argument("loc", nargs="+")
    p.add_argument("--chars", type=int, default=0, help="per segment (0: whole, within the call's limit)")
    p.add_argument("--from", dest="start", type=int, default=0, help="start at this character (page a long segment)")
    p = sub.add_parser("ayah")
    p.add_argument("ref")
    p.add_argument("--kind")
    p.add_argument("--src")
    p.add_argument("--chars", type=int, default=600)
    p = sub.add_parser("cites", help="segments that cite an ayah without being tied to it (reference works, notes)")
    p.add_argument("ref")
    p.add_argument("--src")
    p.add_argument("--chars", type=int, default=500)
    p = sub.add_parser("search")
    p.add_argument("q")
    p.add_argument("--src")
    p.add_argument("--kind")
    p.add_argument("--surah", type=int)
    p.add_argument("--n", type=int, default=10)
    p.add_argument("--chars", type=int, default=300)
    p.add_argument("--sahih", action="store_true")
    p.add_argument("--exact", action="store_true")
    for p in (sub.choices["get"], sub.choices["ayah"], sub.choices["search"], sub.choices["cites"]):
        p.add_argument("--no-translations", action="store_true",
                       help="omit extra English/Turkish translations; keep primary text, notes and source flags")
        p.add_argument("--limit", type=int, default=9_000,
                       help="characters of segment text this call prints (default 9,000; output also stays under "
                            "24,000 bytes; 0: no limit, for scripts)")
    a = ap.parse_args()
    global INTERTEXT, CALL_LIMIT, PREVIEW, SHOW_TRANSLATIONS
    INTERTEXT = a.intertext
    CALL_LIMIT = getattr(a, "limit", 9_000)
    PREVIEW = a.cmd in ("search", "ayah", "cites")
    SHOW_TRANSLATIONS = not getattr(a, "no_translations", False)
    if CALL_LIMIT:
        sys.stdout = _Counter(sys.stdout)
    if a.cmd == "import-local":
        only = set(x for x in a.only.split(",") if x)
        for f in IMPORTERS:
            f(only)
    elif a.cmd == "fresh":
        sys.exit(fresh())
    elif a.cmd == "build":
        build(a.force)
    elif a.cmd == "sources":
        cmd_sources(a.kind or ("intertext" if INTERTEXT else None))
    elif a.cmd == "get":
        cmd_get(a.loc, a.chars, a.start)
    elif a.cmd == "ayah":
        cmd_ayah(a.ref, a.kind, a.src, a.chars)
    elif a.cmd == "search":
        cmd_search(a.q, a)
    elif a.cmd == "cites":
        cmd_cites(a.ref, a.src, a.chars)
    if a.cmd in ("get", "ayah", "search", "cites"):
        close_call()


if __name__ == "__main__":
    main()
