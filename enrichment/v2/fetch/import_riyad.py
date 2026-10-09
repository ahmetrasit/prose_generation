#!/usr/bin/env python3
"""RIYAD: al-Nawawī, Riyāḍ al-Ṣāliḥīn (Arabic), with its structure: books (kitāb), chapters (bāb), the Qurʾān verses
each chapter opens with, and the numbered hadiths (1-1896).

Source: OpenITI version 0676Nawawi.RiyadSalihin.Shamela0012014-ara1 (the RELEASE primary; Shamela book 12014 =
ed. Shuʿayb al-Arnaʾūṭ, Muʾassasat al-Risāla, Beirut, 3rd ed. 1419/1998), fetched from
raw.githubusercontent.com/OpenITI/0700AH. (sunnah.com answers 403 to scripts; the other open Riyāḍ datasets were
incomplete, see source.json notes.) Run `--fetch` once to download the raw file into
enrichment/corpus/RIYAD/raw/acquired-2026-10-09/.

File structure (OpenITI mARkdown): `### | كتاب …` a book (the first book, al-Muqaddimāt, has no heading and the
author's preface is `### | [مقدمة المؤلف]`), `### || N- باب …` chapter N (1-372), `### ||| k/N-` hadith N (k is
the number inside the chapter, often mistyped; N is the book-wide number), `# ` opens a paragraph, `~~` continues it;
`PageV01P526` and `ms002` are page/milestone marks (stripped, counted).

Segments (locators):
  RIYAD:0.0        the author's preface (with its verses)
  RIYAD:<b>.<c>    chapter head: book b (1 = al-Muqaddimāt … 19 = al-Manthūrāt wa-l-Mulaḥ), chapter c (book-wide
                   number 1-372): the title and everything before the chapter's first hadith (the opening verses
                   and al-Nawawī's remarks on them). `refs` = the verses cited as «[sūra: n]» (validated); s/a/a_end
                   = the first cited verse (range) so the pipeline finds the chapter by verse.
  RIYAD:<n>        hadith n: text, `book`, `chapter`, `hadith_no`, `attribution` (the collections al-Nawawī names,
                   as printed) and `collections` (normalised); `refs` = verses cited inside it. A verse quoted at
                   the end of a book (after its last hadith) stays in that hadith's text and refs.
Every irregularity (hadith header numbering, unresolved verse refs, chapters without verses, numbers missing) is
printed and written to the ingestion record.

  python3 -B enrichment/v2/fetch/import_riyad.py [--fetch] [--dry] [--dump FILE]
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import sys
import urllib.request
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402

SID = "RIYAD"
URI = "0676Nawawi.RiyadSalihin.Shamela0012014-ara1"
RAW_DIR = "raw/acquired-2026-10-09"
BASE = "https://raw.githubusercontent.com/OpenITI/0700AH/master/data/0676Nawawi/0676Nawawi.RiyadSalihin/"
FILES = [URI + ".mARkdown", URI + ".yml"]
# second open dataset, used only to restore hadiths the OpenITI file lacks and to cross-check
OSA_URL = "https://raw.githubusercontent.com/osamayy/riyad-salihin/HEAD/riyad-salihin.json"
OSA_FILE = "osamayy-riyad-salihin.json"
UA = {"User-Agent": "Mozilla/5.0 (research corpus fetch; prose_generation enrichment)"}

SURAHS = ("الفاتحة البقرة آل_عمران النساء المائدة الأنعام الأعراف الأنفال التوبة يونس هود يوسف الرعد إبراهيم الحجر النحل "
          "الإسراء الكهف مريم طه الأنبياء الحج المؤمنون النور الفرقان الشعراء النمل القصص العنكبوت الروم لقمان السجدة "
          "الأحزاب سبأ فاطر يس الصافات ص الزمر غافر فصلت الشورى الزخرف الدخان الجاثية الأحقاف محمد الفتح الحجرات ق "
          "الذاريات الطور النجم القمر الرحمن الواقعة الحديد المجادلة الحشر الممتحنة الصف الجمعة المنافقون التغابن "
          "الطلاق التحريم الملك القلم الحاقة المعارج نوح الجن المزمل المدثر القيامة الإنسان المرسلات النبأ النازعات "
          "عبس التكوير الانفطار المطففين الانشقاق البروج الطارق الأعلى الغاشية الفجر البلد الشمس الليل الضحى الشرح "
          "التين العلق القدر البينة الزلزلة العاديات القارعة التكاثر العصر الهمزة الفيل قريش الماعون الكوثر الكافرون "
          "النصر المسد الإخلاص الفلق الناس").split()
ALIASES = {"الذريات": 51, "الانشراح": 94, "المطففون": 83, "الزلزال": 99, "غافر": 40, "المؤمن": 40, "الدهر": 76,
           "بني_إسرائيل": 17, "حم_السجدة": 41, "التوبه": 9, "ن": 68, "عم": 78}
_TASH = re.compile(r"[ً-ْٰـ]")


def norm(s: str) -> str:
    s = _TASH.sub("", s.replace("_", " ")).strip()
    s = re.sub(r"^سورة\s*", "", s)
    s = s.translate(str.maketrans("أإآٱةىؤئ", "ااااهيوي"))
    return re.sub(r"\s+", "", s)


def _strip_al(s: str) -> str:
    return s[2:] if s.startswith("ال") else s


NAME = {}
for i, n in enumerate(SURAHS, 1):
    NAME[norm(n)] = i
    NAME[_strip_al(norm(n))] = i
for n, i in ALIASES.items():
    NAME[norm(n)] = i
    NAME[_strip_al(norm(n))] = i
assert len(SURAHS) == 114

BRACKET = re.compile(r"\[([^\[\]]{1,70})\]")
# the edition mistypes some brackets: «} [النساء:36 [.», «} البقرة:132-133]»: also read what follows a closing brace
AFTER_BRACE = re.compile(r"\}\s*\[?\s*([^\[\]{}]{1,40}?)\s*[\[\]]")
# «[البينة: 5]», «[الذريات56, 57]», «[الأحزاب: 70-71]», «[النحل من الآية 125]»
REFSPEC = re.compile(r"^\s*(?P<name>[^\d:：]+?)\s*[:：]?\s*(?P<nums>\d[\d\s,،\-–و]*?)\s*[,،]*\s*$")
NUMSEG = re.compile(r"(\d{1,3})(?:\s*[-–]\s*(\d{1,3}))?")

COLLECTIONS = [  # (printed form, canonical)
    ("البخاري", "Bukhari"), ("مسلم", "Muslim"), ("أبو داود", "Abu Dawud"), ("أبي داود", "Abu Dawud"),
    ("الترمذي", "Tirmidhi"), ("النسائي", "Nasai"), ("ابن ماجه", "Ibn Majah"), ("ابن ماجة", "Ibn Majah"),
    ("مالك", "Malik"), ("الموطأ", "Malik"), ("أحمد", "Ahmad"), ("الدارمي", "Darimi"), ("البيهقي", "Bayhaqi"),
    ("الدارقطني", "Daraqutni"), ("ابن حبان", "Ibn Hibban"), ("الحاكم", "Hakim"), ("ابن خزيمة", "Ibn Khuzayma"),
    ("الطبراني", "Tabarani"), ("أبو يعلى", "Abu Yala"), ("ابن السني", "Ibn al-Sunni"), ("الحميدي", "Humaydi"),
    ("البزار", "Bazzar"), ("ابن أبي الدنيا", "Ibn Abi al-Dunya"), ("الشافعي", "Shafii")]
ATTR = re.compile(r"(?:متفق (?:على صحته|عليه)|رواه|رواها|رواهما|رواهن|أخرجه)[^.؛\n]{0,200}")

BOOK_HEAD = re.compile(r"^### \| (.*\S)\s*$")
CHAP_HEAD = re.compile(r"^### \|\| (\d+)\s*[-–]?\s*(.*\S)?\s*$")
HAD_HEAD = re.compile(r"^### \|\|\| (.*)$")
MARKS = re.compile(r"\s*\b(?:PageV\d+P\d+|ms\d+)\b")


def fetch() -> None:
    d = IC.src_dir(SID) / RAW_DIR
    d.mkdir(parents=True, exist_ok=True)
    if not (d / OSA_FILE).exists():
        data = urllib.request.urlopen(urllib.request.Request(OSA_URL, headers=UA), timeout=120).read()
        (d / OSA_FILE).write_bytes(data)
        print(f"fetched {OSA_FILE}: {len(data):,} bytes")
    for f in FILES:
        dest = d / f
        if dest.exists():
            print(f"have {dest.name}")
            continue
        data = urllib.request.urlopen(urllib.request.Request(BASE + f, headers=UA), timeout=120).read()
        dest.write_bytes(data)
        print(f"fetched {f}: {len(data):,} bytes sha256 {hashlib.sha256(data).hexdigest()[:16]}")


inferred: list = []
mistyped: list = []


def surah_refs(text: str, unresolved: list) -> list[str]:
    """Verses cited as «[sūra: n]» in the text, validated; unresolved bracket refs are recorded (never dropped)."""
    out: list[str] = []
    found = {m.start(1): m for m in BRACKET.finditer(text)}
    for m in AFTER_BRACE.finditer(text):
        if m.start(1) not in found and not any(abs(m.start(1) - k) < 3 for k in found):
            body = m.group(1)
            if re.search(r"\d", body) and REFSPEC.match(body) and not re.search(r"[.!؟]", body):
                found[m.start(1)] = m
                mistyped.append(body)
    for _, m in sorted(found.items()):
        body = m.group(1)
        if not re.search(r"\d", body):
            continue
        body2 = re.sub(r"من\s+الآية|الآية", " ", body)
        sp = REFSPEC.match(body2)
        if not sp:
            unresolved.append(("unparsed", body))
            continue
        name = norm(sp.group("name")).rstrip("،,")
        s = NAME.get(name) or NAME.get(_strip_al(name)) or NAME.get("ا" + name)
        if not s and not name:  # «[الآية: 41]»: the sūra named just before in the same text
            prior = re.findall(r"سورة\s+([^\s{}\[\]،,.:]+)", text[:m.start()])
            if prior:
                pn = norm(prior[-1])
                s = NAME.get(pn) or NAME.get(_strip_al(pn))
                if s:
                    inferred.append((body, f"sūra {s} from «سورة {prior[-1]}» earlier in the text"))
        if not s:
            unresolved.append(("unknown surah", body))
            continue
        for nm in NUMSEG.finditer(sp.group("nums")):
            a = int(nm.group(1))
            b = int(nm.group(2)) if nm.group(2) else None
            if not IC.valid(s, a, b if b is not None and b >= a else None):
                unresolved.append(("invalid verse", body))
                continue
            r = f"{s}:{a}" + (f"-{b}" if b is not None and b > a else "")
            if r not in out:
                out.append(r)
    return out


def first_tie(refs: list[str]) -> tuple[int | None, int | None, int | None]:
    if not refs:
        return None, None, None
    s, rest = refs[0].split(":")
    a, _, b = rest.partition("-")
    return int(s), int(a), int(b or a)


def parse(raw: Path, report: Counter, flags: dict) -> list[dict]:
    lines = raw.read_text(encoding="utf-8").split("\n")
    # blocks: (kind, header info, paragraphs)
    blocks: list[dict] = []
    cur = None
    started = False
    for ln in lines:
        if ln.startswith("#META#") or ln.startswith("######OpenITI#") or not ln.strip():
            continue
        if ln.startswith("###"):
            started = True
            m = HAD_HEAD.match(ln)
            if m:
                cur = {"kind": "hadith", "head": m.group(1), "paras": []}
            elif ln.startswith("### ||"):
                m = CHAP_HEAD.match(ln)
                if not m:
                    flags["unparsed_headers"].append(ln)
                    continue
                cur = {"kind": "chapter", "no": int(m.group(1)), "title": (m.group(2) or "").strip(), "paras": []}
            else:
                m = BOOK_HEAD.match(ln)
                title = m.group(1) if m else ln
                cur = {"kind": "preface" if "مقدمة المؤلف" in title else "book", "title": title, "paras": []}
            blocks.append(cur)
            continue
        if not started:
            continue
        if ln.startswith("# "):
            cur["paras"].append(ln[2:].strip())
        elif ln.startswith("~~"):
            if cur["paras"]:
                cur["paras"][-1] += " " + ln[2:].strip()
            else:
                cur["paras"].append(ln[2:].strip())
        else:
            # a bare line: page mark («PageV01P526») or stray text
            if re.fullmatch(r"\s*(?:PageV\d+P\d+|ms\d+)(?:\s+(?:PageV\d+P\d+|ms\d+))*\s*", ln):
                report["page marks (own line)"] += 1
            else:
                report["bare lines kept"] += 1
                cur["paras"].append(ln.strip())

    def clean(paras: list[str]) -> str:
        out = []
        for p in paras:
            n = len(MARKS.findall(p))
            report["page/milestone marks stripped"] += n
            p = re.sub(r"\s+", " ", MARKS.sub(" ", p)).strip()
            if p:
                out.append(p)
        return "\n".join(out)

    # a `### ||| N-` block that only holds a «باب …» title is a chapter heading typed one level too deep
    fixed = []
    for b in blocks:
        if b["kind"] == "hadith" and b["paras"] and b["paras"][0].startswith("باب ") and len(b["paras"]) == 1:
            flags["chapter_heading_typed_as_hadith"].append((b["head"], b["paras"][0][:60]))
            prev = fixed[-1] if fixed else None
            if prev and prev["kind"] == "chapter" and difflib.SequenceMatcher(
                    None, prev["title"], b["paras"][0]).ratio() > 0.85:
                flags["duplicate_chapter_heading_dropped"].append((prev["no"], prev["title"], b["paras"][0]))
                continue  # the same title again right after the proper heading, no hadith between: a repeated line
            b = {"kind": "chapter", "no": None, "title": b["paras"][0], "paras": []}
        fixed.append(b)
    blocks = fixed
    # printed hadith numbers: a jump is believed only when the next two headers continue from it (a genuine skip
    # in the edition's numbering); an isolated odd number is a typo and the sequence number is used
    hads = [b for b in blocks if b["kind"] == "hadith"]
    printed = []
    for b in hads:
        ints = [int(x) for x in re.findall(r"\d+", b["head"])]
        printed.append(ints)
    expect = 1
    for i, b in enumerate(hads):
        ints = printed[i]
        nxt = [(printed[j][-1] if printed[j] else None) for j in (i + 1, i + 2) if j < len(hads)]
        if expect in ints:
            n = expect
            if ints[-1] != expect:
                flags["hadith_header_ambiguous"].append((b["head"], expect))
        elif ints and expect < ints[-1] <= expect + 3 and nxt == [ints[-1] + 1, ints[-1] + 2][:len(nxt)]:
            n = ints[-1]
            flags["number_skipped_in_edition"].append(f"{expect}-{n - 1} absent: header after hadith {expect - 1} "
                                                      f"prints {n}")
        else:
            n = expect
            flags["hadith_header_typo"].append((b["head"].strip(), expect))
        b["n"] = n
        expect = n + 1
    # chapter numbers: a chapter heading typed as a hadith takes the next chapter number
    segs: list[dict] = []
    book_no, book_title, chap_no, chap_title = 1, "كتاب المقدمات", 0, ""
    book_titles = {1: book_title}
    unresolved: list = []
    nums_seen: list[int] = []
    pending: dict | None = None  # chapter head waiting for its text (it is complete when blocks end)
    for b in blocks:
        k = b["kind"]
        if k == "preface":
            text = clean(b["paras"])
            refs = surah_refs(text, unresolved)
            s, a, ae = first_tie(refs)
            segs.append({"seg": f"{SID}:0.0", "kind": "preface", "head": "مقدمة المؤلف", "book": 0, "chapter": 0,
                         "text": text, "refs": refs, "s": s, "a": a, "a_end": ae})
        elif k == "book":
            book_no += 1
            book_title = b["title"]
            book_titles[book_no] = book_title
            if clean(b["paras"]):
                flags["book_head_text"].append((book_no, clean(b["paras"])[:80]))
        elif k == "chapter":
            chap_no = b["no"] if b["no"] is not None else chap_no + 1
            chap_title = b["title"]
            intro = clean(b["paras"])
            text = (f"{chap_title}\n{intro}").strip()
            refs = surah_refs(intro, unresolved)
            title_refs = surah_refs(chap_title, unresolved)
            for r in title_refs:
                if r not in refs:
                    refs.append(r)
            s, a, ae = first_tie(refs)
            if not refs:
                flags["chapters_without_verses"].append(f"{book_no}.{chap_no}")
            segs.append({"seg": f"{SID}:{book_no}.{chap_no}", "kind": "chapter", "head": chap_title,
                         "book": book_no, "book_title": book_title, "chapter": chap_no, "text": text,
                         "refs": refs, "s": s, "a": a, "a_end": ae})
        else:  # hadith
            n = b["n"]
            nums_seen.append(n)
            text = clean(b["paras"])
            refs = surah_refs(text, unresolved)
            attrs = [m.group(0).strip() for m in ATTR.finditer(text)]
            coll = []
            for printed, canon in COLLECTIONS:
                if any(printed in x for x in attrs) and canon not in coll:
                    coll.append(canon)
            if any(x.startswith("متفق") for x in attrs):
                for c in ("Bukhari", "Muslim"):
                    if c not in coll:
                        coll.append(c)
            if not attrs:
                flags["hadith_without_attribution"].append(n)
            if not text:
                flags["empty_hadith"].append(n)
            segs.append({"seg": f"{SID}:{n}", "kind": "hadith", "hadith_no": n, "book": book_no,
                         "book_title": book_title, "chapter": chap_no, "head": chap_title, "text": text,
                         "attribution": " | ".join(attrs), "collections": coll, "refs": refs})
    # hadiths whose header is absent from the OpenITI file: restored from the osamayy dataset (and flagged)
    osa = raw.parent / OSA_FILE
    present = set(nums_seen)
    for n in range(1, 1897):
        if n in present:
            continue
        text = None
        if osa.exists():
            for rec in json.loads(osa.read_text(encoding="utf-8")):
                m = re.search(r"(?m)^\s*%d\s*[-–]\s*(.*)$" % n, rec["content"])
                if m:
                    text = re.sub(r"\s+", " ", m.group(1)).strip()
                    break
        pos = next((i for i, g in enumerate(segs) if g["seg"] == f"{SID}:{n - 1}"), None)
        if text is None or pos is None:
            flags["restore_failed"].append(n)
            continue
        prev = segs[pos]
        refs = surah_refs(text, unresolved)
        attrs = [m.group(0).strip() for m in ATTR.finditer(_TASH.sub("", text))]
        coll = []
        for printed, canon in COLLECTIONS:
            if any(printed in x for x in attrs) and canon not in coll:
                coll.append(canon)
        if any(x.startswith("متفق") for x in attrs):
            coll = list(dict.fromkeys(coll + ["Bukhari", "Muslim"]))
        segs.insert(pos + 1, {"seg": f"{SID}:{n}", "kind": "hadith", "hadith_no": n, "book": prev["book"],
                              "book_title": prev["book_title"], "chapter": prev["chapter"], "head": prev["head"],
                              "text": _TASH.sub("", text), "attribution": " | ".join(attrs), "collections": coll,
                              "refs": refs, "fill_source": "osamayy/riyad-salihin (diacritics stripped); the "
                              "OpenITI file has no header or text for this number"})
        flags["restored_from_osamayy"].append(n)
        nums_seen.append(n)
    flags["unresolved_refs"] = unresolved
    flags["books"] = book_titles
    flags["hadith_numbers"] = nums_seen
    return segs


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fetch", action="store_true", help="download the raw OpenITI file first")
    ap.add_argument("--dry", action="store_true", help="parse and report; write nothing")
    ap.add_argument("--dump", help="write the segments to this file for inspection")
    args = ap.parse_args()
    if args.fetch:
        fetch()
    d = IC.src_dir(SID)
    if not args.dry and not (d / "source.json").exists():  # IC.write updates source.json in place
        d.mkdir(parents=True, exist_ok=True)
        (d / "source.json").write_text(json.dumps({"id": SID}) + "\n", encoding="utf-8")
    raw = d / RAW_DIR / FILES[0]
    if not raw.exists():
        sys.exit(f"{raw} missing: run with --fetch")
    report: Counter = Counter()
    flags: dict = {k: [] for k in ("unparsed_headers", "book_head_text", "chapters_without_verses",
                                   "hadith_header_ambiguous", "hadith_header_typo", "number_skipped_in_edition",
                                   "chapter_heading_typed_as_hadith", "duplicate_chapter_heading_dropped",
                                   "restored_from_osamayy", "restore_failed",
                                   "hadith_without_attribution", "empty_hadith")}
    segs = parse(raw, report, flags)
    nums = flags.pop("hadith_numbers")
    books = flags.pop("books")
    unresolved = flags.pop("unresolved_refs")
    chapters = [g for g in segs if g["kind"] == "chapter"]
    hadiths = [g for g in segs if g["kind"] == "hadith"]
    missing = [n for n in range(1, 1897) if n not in set(nums)]
    dupes = sorted(n for n, c in Counter(nums).items() if c > 1)
    chap_nums = [g["chapter"] for g in chapters]
    chap_missing = [n for n in range(1, 373) if n not in set(chap_nums)]
    ch_verses = sum(len(g["refs"]) for g in chapters)
    # braces-quoted verses outnumbering the verse refs found: listed, so a missing tie is never silent
    quoted_no_ref = [f"{g['seg']} ({len(re.findall(r'[{][^{}]+[}]', g['text']))} quoted, {len(g['refs'])} refs)"
                     for g in chapters if len(re.findall(r"[{][^{}]+[}]", g["text"])) > len(g["refs"])]
    print(f"books {len(books)}: " + "; ".join(f"{k}={v[:30]}" for k, v in books.items()))
    print(f"chapters {len(chapters)} (missing numbers {chap_missing}); chapters with verses "
          f"{sum(1 for g in chapters if g['refs'])}, verse refs on chapters {ch_verses}")
    print(f"hadiths {len(hadiths)}; numbers 1-1896 missing {missing}; duplicated {dupes}; "
          f"with cited verses {sum(1 for g in hadiths if g['refs'])}")
    print(f"mistyped brackets read: {mistyped}")
    print(f"chapters with more quoted verses than refs: {len(quoted_no_ref)} {quoted_no_ref[:20]}")
    print(f"unresolved bracket refs {len(unresolved)}: {unresolved[:20]}; inferred {inferred}")
    for k, v in flags.items():
        print(f"{k}: {len(v)}" + (f"  {v[:12]}" if v else ""))
    print("report:", dict(report))
    cat = Counter(c for g in hadiths for c in g["collections"])
    print("collections named:", dict(cat.most_common()))
    if args.dump:
        with open(args.dump, "w", encoding="utf-8") as f:
            for g in segs:
                f.write(json.dumps(g, ensure_ascii=False) + "\n")
    if args.dry:
        print("dry run: nothing written")
        return
    sha = IC.inputs(SID, [URI, OSA_FILE.rsplit(".", 1)[0]])
    notes = ("OpenITI Shamela0012014 (ed. Shuʿayb al-Arnaʾūṭ, Muʾassasat al-Risāla, 3rd ed. 1419/1998). Hadith "
             "numbers are al-Nawawī's book-wide 1-1896 as in this edition (the sunnah.com numbering of the same "
             "work follows the same sequence; cite RIYAD:<n> and the opening words). Book numbers: 1 = "
             "al-Muqaddimāt (it has no heading in the file; the 18 headed books follow, 2-19). Chapter segment "
             "RIYAD:<b>.<c> carries the title and the opening verses/remarks; `refs` are the verses cited as "
             "[sūra: n], s/a/a_end = the first cited verse (range). The chapter list in this edition is al-Nawawī's "
             "(372 chapters). The final hadith of a book may carry a closing verse in its text. Attribution = the "
             "collections al-Nawawī names after each hadith, as printed (`attribution`, `collections`). "
             "Cross-checked against the incomplete open datasets osamayy/riyad-salihin and "
             "CheeseWithSauce/HadithsJSONFormat (sunnah.com copy); sunnah.com itself returns 403 to scripts.")
    IC.write(SID, segs, {
        "script": "enrichment/v2/fetch/import_riyad.py",
        "from": sha,
        "method": "OpenITI mARkdown headers: book, chapter and hadith headings; verse refs parsed from «[sūra: n]»",
        "books": len(books), "chapters": len(chapters), "hadiths": len(hadiths),
        "hadith_numbers_missing": missing, "hadith_numbers_duplicated": dupes, "chapter_numbers_missing": chap_missing,
        "chapters_with_verses": sum(1 for g in chapters if g["refs"]), "chapter_verse_refs": ch_verses,
        "chapters_without_verses": flags["chapters_without_verses"],
        "hadiths_with_cited_verses": sum(1 for g in hadiths if g["refs"]),
        "unresolved_bracket_refs": unresolved, "inferred_bracket_refs": inferred, "refs_read_from_mistyped_brackets": mistyped,
        "chapters_with_unreferenced_quotes": quoted_no_ref, "irregularities": {k: v for k, v in flags.items()
                                                                   if k != "chapters_without_verses"},
        "stripped": dict(report),
        "collections_named": dict(cat.most_common()),
    }, {
        "id": SID, "title": "Riyāḍ al-Ṣāliḥīn", "author": "al-Nawawī", "death_ah": 676, "kind": "hadith",
        "tradition": "sunni-hadith", "language": "ar", "locator": "hadith",
        "edition": "OpenITI Shamela0012014 = ed. Shuʿayb al-Arnaʾūṭ, Muʾassasat al-Risāla, Beirut, 3rd ed. "
                   "1419/1998 (RELEASE 2025-1-9; OpenITI commit as fetched 2026-10-09)",
        "coverage": "whole book: preface, 19 books, 372 chapters, hadiths 1-1896",
        "urls": [BASE + FILES[0], "https://shamela.ws/book/12014"],
        "licence": "OpenITI text (open corpus, CC BY-NC-SA 4.0 as stated by OpenITI); the underlying edition's rights "
                   "are the publisher's; local research copy only",
        "files": sha, "notes": notes,
        "acquisition": {"date": "2026-10-09", "state": "raw_downloaded", "ingestion_status": "ingested",
                        "files": len(sha), "source": "OpenITI/0700AH on GitHub"},
    })


if __name__ == "__main__":
    main()
