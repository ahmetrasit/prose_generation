#!/usr/bin/env python3
"""Bible texts for the separate Bible pass (gelenek tevrat / incil): three open bulk sources, one directory each under
enrichment/bible/corpus/, kind `intertext` (never in the Islamic index; indexed by `corpus.py --intertext build`).

  bible_text.py wlc        Hebrew Bible, Westminster Leningrad Codex (openscriptures/morphhb OSIS XML, CC BY 4.0)
  bible_text.py sblgnt     Greek New Testament, SBLGNT (LogosBible/SBLGNT, CC BY 4.0)
  bible_text.py kjv        King James Version with the Apocrypha (ebible.org eng-kjv, public domain), the English aid
  bible_text.py all

Locators are OSIS: WLC:Gen.22.2, SBLGNT:Matt.6.5, KJV:Gen.22.2 (schema.json, kaynak). One segment per verse; the
WLC text is pointed, with the consonantal form in `consonantal` for searching. Downloads are cached in raw/ and never
fetched twice (ref_common.Source). Nothing here reaches the Islamic pass.
"""
from __future__ import annotations

import io
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from enrichment.bible.fetch.ref_common import Source  # noqa: E402

WLC_BOOKS = ["Gen", "Exod", "Lev", "Num", "Deut", "Josh", "Judg", "Ruth", "1Sam", "2Sam", "1Kgs", "2Kgs", "1Chr", "2Chr",
             "Ezra", "Neh", "Esth", "Job", "Ps", "Prov", "Eccl", "Song", "Isa", "Jer", "Lam", "Ezek", "Dan", "Hos", "Joel",
             "Amos", "Obad", "Jonah", "Mic", "Nah", "Hab", "Zeph", "Hag", "Zech", "Mal"]
SBLGNT_BOOKS = ["Matt", "Mark", "Luke", "John", "Acts", "Rom", "1Cor", "2Cor", "Gal", "Eph", "Phil", "Col", "1Thess",
                "2Thess", "1Tim", "2Tim", "Titus", "Phlm", "Heb", "Jas", "1Pet", "2Pet", "1John", "2John", "3John", "Jude", "Rev"]
NAMES = {"Gen": "Genesis", "Exod": "Exodus", "Lev": "Leviticus", "Num": "Numbers", "Deut": "Deuteronomy", "Josh": "Joshua",
         "Judg": "Judges", "Ruth": "Ruth", "1Sam": "1 Samuel", "2Sam": "2 Samuel", "1Kgs": "1 Kings", "2Kgs": "2 Kings",
         "1Chr": "1 Chronicles", "2Chr": "2 Chronicles", "Ezra": "Ezra", "Neh": "Nehemiah", "Esth": "Esther", "Job": "Job",
         "Ps": "Psalms", "Prov": "Proverbs", "Eccl": "Ecclesiastes", "Song": "Song of Songs", "Isa": "Isaiah", "Jer": "Jeremiah",
         "Lam": "Lamentations", "Ezek": "Ezekiel", "Dan": "Daniel", "Hos": "Hosea", "Joel": "Joel", "Amos": "Amos", "Obad": "Obadiah",
         "Jonah": "Jonah", "Mic": "Micah", "Nah": "Nahum", "Hab": "Habakkuk", "Zeph": "Zephaniah", "Hag": "Haggai", "Zech": "Zechariah",
         "Mal": "Malachi", "Matt": "Matthew", "Mark": "Mark", "Luke": "Luke", "John": "John", "Acts": "Acts", "Rom": "Romans",
         "1Cor": "1 Corinthians", "2Cor": "2 Corinthians", "Gal": "Galatians", "Eph": "Ephesians", "Phil": "Philippians",
         "Col": "Colossians", "1Thess": "1 Thessalonians", "2Thess": "2 Thessalonians", "1Tim": "1 Timothy", "2Tim": "2 Timothy",
         "Titus": "Titus", "Phlm": "Philemon", "Heb": "Hebrews", "Jas": "James", "1Pet": "1 Peter", "2Pet": "2 Peter",
         "1John": "1 John", "2John": "2 John", "3John": "3 John", "Jude": "Jude", "Rev": "Revelation",
         "Tob": "Tobit", "Jdt": "Judith", "EsthGr": "Esther (Greek)", "Wis": "Wisdom", "Sir": "Sirach", "Bar": "Baruch",
         "PrAzar": "Prayer of Azariah", "Sus": "Susanna", "Bel": "Bel and the Dragon", "1Macc": "1 Maccabees", "2Macc": "2 Maccabees",
         "1Esd": "1 Esdras", "2Esd": "2 Esdras", "PrMan": "Prayer of Manasseh", "AddPs": "Psalm 151", "EpJer": "Letter of Jeremiah"}
# ebible USFM codes -> OSIS
USFM = {"GEN": "Gen", "EXO": "Exod", "LEV": "Lev", "NUM": "Num", "DEU": "Deut", "JOS": "Josh", "JDG": "Judg", "RUT": "Ruth",
        "1SA": "1Sam", "2SA": "2Sam", "1KI": "1Kgs", "2KI": "2Kgs", "1CH": "1Chr", "2CH": "2Chr", "EZR": "Ezra", "NEH": "Neh",
        "EST": "Esth", "JOB": "Job", "PSA": "Ps", "PRO": "Prov", "ECC": "Eccl", "SOL": "Song", "SNG": "Song", "ISA": "Isa",
        "JER": "Jer", "LAM": "Lam", "EZE": "Ezek", "EZK": "Ezek", "DAN": "Dan", "HOS": "Hos", "JOE": "Joel", "JOL": "Joel",
        "AMO": "Amos", "OBA": "Obad", "JON": "Jonah", "MIC": "Mic", "NAH": "Nah", "HAB": "Hab", "ZEP": "Zeph", "HAG": "Hag",
        "ZEC": "Zech", "MAL": "Mal", "MAT": "Matt", "MAR": "Mark", "MRK": "Mark", "LUK": "Luke", "JOH": "John", "JHN": "John",
        "ACT": "Acts", "ROM": "Rom", "1CO": "1Cor", "2CO": "2Cor", "GAL": "Gal", "EPH": "Eph", "PHI": "Phil", "PHP": "Phil",
        "COL": "Col", "1TH": "1Thess", "2TH": "2Thess", "1TI": "1Tim", "2TI": "2Tim", "TIT": "Titus", "PHM": "Phlm", "HEB": "Heb",
        "JAM": "Jas", "JAS": "Jas", "1PE": "1Pet", "2PE": "2Pet", "1JO": "1John", "2JO": "2John", "3JO": "3John", "1JN": "1John",
        "2JN": "2John", "3JN": "3John", "JUD": "Jude", "REV": "Rev", "TOB": "Tob", "JDT": "Jdt", "ESG": "EsthGr", "WIS": "Wis",
        "SIR": "Sir", "BAR": "Bar", "PRA": "PrAzar", "SUS": "Sus", "BEL": "Bel", "1MA": "1Macc", "2MA": "2Macc", "1ES": "1Esd",
        "4ES": "2Esd", "2ES": "2Esd", "PRM": "PrMan", "LJE": "EpJer", "PS2": "AddPs"}
NS = {"o": "http://www.bibletechnologies.net/2003/OSIS/namespace"}
HEB_POINTS = re.compile(r"[֑-ֽֿ-ׇ]")  # cantillation and vowels; keeps letters and maqaf


def wlc_verse(v) -> dict:
    """The written (ketiv) stream, with qere/other notes kept separately.

    Word positions are one-based; a note's after_word is zero at verse start.
    Never recursively collect words: note/rdg/w belongs to the apparatus.
    """
    tokens, notes, word_number = [], [], 0
    for child in v:
        tag = child.tag.rsplit('}', 1)[-1]
        if tag == 'note':
            readings = [{"type": r.get("type"),
                         "text": ' '.join(''.join(w.itertext()).replace('/', '') for w in r.iter(f"{{{NS['o']}}}w")),
                         "words": [{**w.attrib, "text": ''.join(w.itertext()).replace('/', '')}
                                   for w in r.iter(f"{{{NS['o']}}}w")]}
                        for r in child.iter(f"{{{NS['o']}}}rdg")]
            notes.append({"after_word": word_number, "type": child.get("type"), "readings": readings,
                          "xml": ET.tostring(child, encoding='unicode').strip()})
        elif tag in ('w', 'seg'):
            text = ''.join(child.itertext()).replace('/', '')
            if tag == 'w':
                word_number += 1
            tokens.append({"kind": tag, **child.attrib, "text": text,
                           **({"position": word_number} if tag == 'w' else {})})
        else:
            raise ValueError(f"{v.get('osisID')}: unexpected verse child {tag}")
    text = ' '.join(t['text'] for t in tokens)
    text = re.sub(r'\s*־\s*', '־', text)
    text = re.sub(r'\s+׃', '׃', text).strip()
    return {"text": text, "consonantal": HEB_POINTS.sub('', text), "tokens": tokens,
            "text_reading": "ketiv", "variant_notes": notes,
            "gelenek": ["tevrat"], "nusha": ["masoretik"], "versification": "Bible.MT"}


def wlc() -> None:
    META = {"id": "WLC", "title": "Hebrew Bible, Westminster Leningrad Codex (Open Scriptures Hebrew Bible, OSIS)",
                         "author": "Masoretic text; Open Scriptures (morphology and XML)", "death_ah": None, "kind": "intertext",
                         "gelenek": ["tevrat"], "tradition": "Hebrew Bible (Masoretic)", "language": "he",
                         "edition": "openscriptures/morphhb, wlc/*.xml (WLC 4.20)", "access": "yerel", "locator": "osis",
                         "licence": "CC BY 4.0 (Open Scriptures Hebrew Bible); local research copy",
                         "notes": "FOR THE BIBLE PASS ONLY. seg WLC:<OSIS book>.<chapter>.<verse>; text pointed (vowels, "
                                  "cantillation), `consonantal` without points; the text is the written/ketiv stream. "
                                  "Qere and other notes are separate in variant_notes, with word positions; punctuation "
                                  "and original word attributes are retained in tokens. Verse numbering is the Hebrew one (differs from English in "
                                  "Psalms headings and some chapter breaks).",
                         "coverage": "whole Hebrew Bible, 39 books",
                         "urls": ["https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/<Book>.xml"]}
    src, segs, n = Source("WLC"), [], 0
    failures = []
    for book in WLC_BOOKS:
        st, body = src.fetch(f"https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/{book}.xml", f"wlc/{book}.xml")
        if st != 200 or not body:
            print(f"FETCH FAILED: WLC {book}", file=sys.stderr)
            failures.append(book)
            continue
        root = ET.fromstring(body)
        for v in root.iter(f"{{{NS['o']}}}verse"):
            osis = v.get("osisID")
            if not osis:
                continue
            b, c, vs = osis.split(".")
            segs.append({"seg": f"WLC:{osis}", "s": None, "a": None, "a_end": None, "page": None,
                     "head": f"{NAMES.get(b, b)} {c}:{vs}", **wlc_verse(v),
                     "book": b, "chapter": int(c), "verse": int(vs)})
            n += 1
    if failures:
        raise SystemExit(f"WLC incomplete ({', '.join(failures)}); previous segments left intact")
    src.upsert_segments(segs, drop_prefix="WLC:")
    src.update_source(META, urls=META["urls"])
    print(f"WLC: {n} verses")


def sblgnt() -> None:
    META = {"id": "SBLGNT", "title": "The Greek New Testament: SBL Edition", "author": "ed. Michael W. Holmes; Society of Biblical Literature / Logos",
                            "death_ah": None, "kind": "intertext", "gelenek": ["incil"], "tradition": "New Testament (Greek)",
                            "language": "el", "edition": "LogosBible/SBLGNT data/sblgnt/text", "access": "yerel", "locator": "osis",
                            "licence": "CC BY 4.0 (SBLGNT); local research copy",
                            "notes": "FOR THE BIBLE PASS ONLY. seg SBLGNT:<OSIS book>.<chapter>.<verse>.",
                            "coverage": "whole New Testament, 27 books",
                            "urls": ["https://raw.githubusercontent.com/LogosBible/SBLGNT/master/data/sblgnt/text/<Book>.txt"]}
    src, segs, n = Source("SBLGNT"), [], 0
    failures = []
    for book in SBLGNT_BOOKS:
        st, body = src.fetch(f"https://raw.githubusercontent.com/LogosBible/SBLGNT/master/data/sblgnt/text/{book}.txt", f"sblgnt/{book}.txt")
        if st != 200 or not body:
            print(f"FETCH FAILED: SBLGNT {book}", file=sys.stderr)
            failures.append(book)
            continue
        for line in body.decode("utf-8").splitlines():
            m = re.match(r"(\S+) (\d+):(\d+)\t(.*)", line)
            if not m:
                continue
            b, c, vs, text = m.group(1), m.group(2), m.group(3), m.group(4).strip()
            segs.append({"seg": f"SBLGNT:{b}.{c}.{vs}", "s": None, "a": None, "a_end": None, "page": None,
                     "head": f"{NAMES.get(b, b)} {c}:{vs}", "text": text, "book": b, "chapter": int(c), "verse": int(vs)})
            n += 1
    if failures:
        raise SystemExit(f"SBLGNT incomplete ({', '.join(failures)}); previous segments left intact")
    src.upsert_segments(segs, drop_prefix='SBLGNT:')
    src.update_source(META, urls=META["urls"])
    print(f"SBLGNT: {n} verses")


def kjv() -> None:
    META = {"id": "KJV", "title": "King James Version (1769 text) with the Apocrypha", "author": "1611 translators; eBible.org edition",
                         "death_ah": None, "kind": "intertext", "gelenek": ["tevrat", "incil"], "tradition": "English Bible (Protestant canon + Apocrypha)",
                         "language": "en", "edition": "ebible.org eng-kjv, verse-per-line text", "access": "yerel", "locator": "osis",
                         "licence": "public domain; local research copy",
                         "notes": "FOR THE BIBLE PASS ONLY, as the English reading aid beside WLC and SBLGNT; never the text quoted as "
                                  "the scripture itself when the Hebrew or Greek is in the corpus. seg KJV:<OSIS book>.<chapter>.<verse>; "
                                  "[brackets] are the translators' supplied words.",
                         "coverage": "66 books and the Apocrypha", "urls": ["https://ebible.org/Scriptures/eng-kjv_vpl.zip"]}
    src, segs = Source("KJV"), []
    st, body = src.fetch("https://ebible.org/Scriptures/eng-kjv_vpl.zip", "kjv/eng-kjv_vpl.zip")
    if st != 200 or not body:
        raise SystemExit('FETCH FAILED: KJV zip; previous segments left intact')
    z = zipfile.ZipFile(io.BytesIO(body))
    txt = z.read("eng-kjv_vpl.txt").decode("utf-8")
    n, unknown = 0, set()
    for line in txt.splitlines():
        m = re.match(r"(\S+) (\d+):(\d+) (.*)", line)
        if not m:
            continue
        code, c, vs, text = m.groups()
        b = USFM.get(code)
        if not b:
            unknown.add(code)
            continue
        segs.append({"seg": f"KJV:{b}.{c}.{vs}", "s": None, "a": None, "a_end": None, "page": None,
                 "head": f"{NAMES.get(b, b)} {c}:{vs}", "text": text.strip(), "book": b, "chapter": int(c), "verse": int(vs)})
        n += 1
    src.upsert_segments(segs)
    src.update_source(META, urls=META["urls"])
    print(f"KJV: {n} verses" + (f"; NOTE: unknown book codes skipped: {', '.join(sorted(unknown))}" if unknown else ""))


def main() -> None:
    what = sys.argv[1:] or ["all"]
    if "all" in what:
        what = ["wlc", "sblgnt", "kjv"]
    for w in what:
        {"wlc": wlc, "sblgnt": sblgnt, "kjv": kjv}[w]()


if __name__ == "__main__":
    main()
