#!/usr/bin/env python3
"""MEAL-KARAHANLI-TIEM73-UNLU + REF-KARAHANLI-TIEM73-UNLU-NOTES: the Karakhanid Turkish interlinear Qur'an translation
of manuscript TİEM 73 (Istanbul, Türk ve İslam Eserleri Müzesi no. 73, copied 734 H / 1333-34), complete (all 114
surahs, 452 leaves), in Suat Ünlü's transcribed edition «Karahanlı Türkçesi İlk Türkçe Satır-Arası Transkribeli
Kur'an Türcümesi (TİEM 73) - Türkiye Türkçesi Mealli Karşılaştırmalı Kur'an-ı Kerim», volumes 1-4 (Konya: Selçuklu
Belediyesi, 2018; ISBN 978-605-4886-35-7), with a modern Turkish translation (Şener/Sofuoğlu/Yıldırım, «Yüce Kur'an
ve Açıklamalı-Yorumlu Meâli») printed under each verse. A second edition of the same manuscript beside Kök's
thesis (MEAL-KARAHANLI-TIEM73, surahs 1-20): Ünlü's verse numbers stand at the start of each line, so the verses are
exact where the OCR kept the number.

Input: the OCR text of archive.org item karahanli-kuran-i-kerim (uploader daulet.cubex@gmail.com), files
Karahanlı_Kuran-ı_Kerim_Meali-Cilt_1..4 (_djvu.txt); volumes 7 and 8 (Açıklamalı Sözlük = glossary) go to the
reference source as sections. Fetched by this script into raw/acquired-2026-10-09/.

Page layout in the OCR: per verse a line «N. <Karakhanid transliteration>», the Arabic text (OCR garbage), then the
modern Turkish «N. <Capitalised Turkish>», then footnotes («N text») at the page foot; ornament tokens
(«AYA», «DAN», «p 4» ...) stick to both ends of the lines. Surah starts are found by the intro line «Mekke
döneminde inmiştir. N âyettir.» checked against the surah's verse count (three intro lines are lost: Ra'd, Saba, Duha;
their surahs are cut where the verse numbers restart).

What is kept: Karakhanid verse lines (S:A; a continuation line is added when the first line ends without a full
stop; a verse whose number the OCR lost is taken from the unnumbered Karakhanid-looking lines before the modern
line of that number and flagged `number_lost`); the basmala lines of the surahs (S:head). The modern Turkish
lines, the footnotes, the surah intros and the front/back matter go to the reference source, tied to their verses
where numbered. OCR lines of the Arabic column and running headers are dropped and counted, with a sample.

  python3 -B enrichment/v2/fetch/import_meal_karahanli_unlu.py [--dry] [--debug S]
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402
import turkic_common as T  # noqa: E402

SID, NSID = "MEAL-KARAHANLI-TIEM73-UNLU", "REF-KARAHANLI-TIEM73-UNLU-NOTES"
IDENT = "karahanli-kuran-i-kerim"
URL = f"https://archive.org/details/{IDENT}"
VOLS = [("154f2d", "Karahanlı_Kuran-ı_Kerim_Meali-Cilt_1_djvu.txt"), ("501ce6", "Karahanlı_Kuran-ı_Kerim_Meali-Cilt_2_djvu.txt"),
        ("8867a7", "Karahanlı_Kuran-ı_Kerim_Meali-Cilt_3_djvu.txt"), ("7b0419", "Karahanlı_Kuran-ı_Kerim_Meali-Cilt_4_djvu.txt")]
GLOSS = [("gl7", "Cilt_7_"),
         ("gl8", "Cilt_8_")]

STOP = {"Av", "Yan", "Dan", "Ya", "Ni", "Mi", "Ne", "Za", "Ka", "Wi", "Dy", "Pan", "Yy", "Ye", "Nİ", "İN", "Aİ", "Yİ", "Ka4",
        "Va", "YA", "Pa", "Sa", "Ke", "Di", "Du", "Sö", "Ün", "Ay4", "Wa", "Ni4", "Ya,"}
SYM = {"p", "d", "v", "w", "y", "#", "|", "Y", "N", "W", "V", "A", "K", "Ç", "e", "i"}
KARA = set("anlar kim takı yana ol birle birlä üze üzä tanrı erse ymâ yme ymä anın anıp kılur kılurlar aydı ayturlar bolgay siler "
           "sizni bizni biz yok turur erdi idi bodun kılğay kertgündi kertgünür kertgünmedi ajunka ögdi yarlıkağ bolur tanrıka "
           "anlarka anlarnı silerke ayur ayğıl kılğıl bilür bilgil ymâ ukar ukmaz kıldı kıldılar tegme tegmä nege köni".split())
MODERN = set("ve bir bu için olan ile de da gibi ancak ama çünkü her o onlar ki ise daha çok kimse allah ey sizin kendi ona onu "
             "şöyle diye değil mi mı ya yoksa ise bunun bunlar şu ne olarak ettik eder eden etti ederler olduğunu rabbin sana "
             "size biz'e onların onun dahi bile fakat hiç hiçbir olur olmak".split())
HEAD_LINE = re.compile(r"Karahanlı Türkçesi İ[lk]|Transkribeli Kur|Mealli Karşılaştırmalı|Kur'an Türcümesi")
INTRO = re.compile(r"(\d{1,3})\s*\.?\s*[âa]yettir")
SURAH_HEAD = re.compile(r"s[uüe]r[eâaé]t[uü]|âyet|inmi[şs]|Mekke|Medine")
NUMTOK = re.compile(r"^[^\w]{0,2}(\d{1,3})(?:\.|(?=[a-zçğıöşüâîû]{2}))(\S.*)?$")
LETTERS = "A-Za-zÇĞİÖŞÜçğıöşüÂÎÛâîû"


def is_noise(t: str) -> bool:
    if NUMTOK.match(t):
        return False
    if len(t) > 5:
        return False
    if t in STOP or t in SYM:
        return True
    if re.fullmatch(rf"[^\w{LETTERS}]+", t):
        return True
    if re.search(r"\d", t):
        return True
    if not re.search(r"[a-zçğıöşüâîû]", t):          # no lower-case letter at all: AYA, ZN, W#, DX.
        return True
    if re.fullmatch(r"[a-zçğıöşü]{1,2}[A-ZÇĞİÖŞÜ][a-z0-9]?", t):
        return True
    return False


def clean(line: str) -> str:
    """The line without the ornament tokens of the page margins (both ends); a verse number found within the
    first five tokens makes everything before it margin."""
    toks = line.split()
    toks = [re.sub(r"^[|Il](?=\d{1,2}\.)", "1", t) for t in toks]   # «|8.» is «18.»
    for i, t in enumerate(toks[:5]):
        if NUMTOK.match(t) and i > 0:
            toks = toks[i:]
            break
    i = 0
    while i < len(toks) and is_noise(toks[i]) and i < 6:
        i += 1
    j = len(toks)
    while j > i and is_noise(toks[j - 1]) and len(toks) - j < 6:
        j -= 1
    toks = toks[i:j]
    # after the last full stop only margin tokens can follow: capitalised short tokens («Ya», «Av»)
    for k in range(len(toks) - 1, -1, -1):
        if toks[k].endswith("."):
            tail = toks[k + 1:]
            if 0 < len(tail) <= 2 and all(len(x) <= 4 and x[0].isupper() and not x.endswith(".") for x in tail):
                toks = toks[:k + 1]
            break
    return " ".join(toks)


def score(text: str) -> int:
    ws = re.findall(rf"[{LETTERS}']+", text.lower().replace("i̇", "i"))
    return sum(w in KARA for w in ws) - sum(w in MODERN for w in ws)


def wordlike(text: str) -> bool:
    toks = text.split()
    if not toks:
        return False
    good = [t for t in toks if re.fullmatch(rf"[{LETTERS}'’“”\"(),.;:?!\-–]*[{LETTERS}]{{3,}}[{LETTERS}'’“”\"(),.;:?!\-–]*", t)]
    return len(good) / len(toks) >= 0.5 and len(text) >= 12


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("--debug", type=int)
    a = ap.parse_args()
    counts = IC.ayah_counts()
    raws = [(k, T.ensure_raw(SID, IDENT, name, f"{k}.txt")) for k, name in VOLS + GLOSS]
    vol_lines = {k: T.read_lines(p) for k, p in raws}
    stats: Counter = Counter()
    issues: list[str] = []
    dropped_sample: list[str] = []

    # --- surah anchors: intro lines checked against the verse counts, in order
    cand: list[tuple[str, int, int]] = []
    for k, _ in VOLS:
        L = vol_lines[k]
        for i, l in enumerate(L):
            m = INTRO.search(l)
            if m and re.search(r"(Mekke|Medine|nâzil|inmi)", " ".join(L[max(0, i - 1):i + 1])):
                cand.append((k, i, int(m.group(1))))
    anchors: dict[int, tuple[str, int]] = {}
    s = 1
    for k, i, c in cand:
        for n in range(s, min(s + 4, 115)):
            if counts[n] == c:
                anchors[n] = (k, i)
                s = n + 1
                break
    lost = [n for n in range(1, 115) if n not in anchors]
    print(f"surah intro lines found for {len(anchors)}/114; lost: {lost}")
    # start of each volume's surah text: from its first anchor; the lines before are front matter
    order = [n for n in sorted(anchors)]
    regions: list[tuple[int, str, int, int]] = []  # (first surah, vol, start line, end line)
    for idx, n in enumerate(order):
        k, i = anchors[n]
        nxt = anchors[order[idx + 1]] if idx + 1 < len(order) else None
        end = nxt[1] if nxt and nxt[0] == k else len(vol_lines[k])
        regions.append((n, k, i, end))

    verses: dict[tuple[int, int], dict] = {}      # (s, n) -> Karakhanid verse
    heads: dict[int, list[str]] = {}
    modern: dict[tuple[int, int], list[str]] = {}
    notes: dict[int, list[str]] = {}
    preamble: dict[int, list[str]] = {}
    orphans: dict[int, list[str]] = {}

    def scan(sn: int, k: str, lo: int, hi: int) -> None:
        """One surah's lines: Karakhanid verses, modern lines, footnotes."""
        V = counts[sn]
        L = vol_lines[k]
        last: tuple[str, int] | None = None
        pending: list[str] = []
        seen_num = False
        for i in range(lo, hi):
            raw = L[i]
            if not raw.strip():
                continue
            line = clean(raw)
            if not line:
                stats["lines of ornament tokens only dropped"] += 1
                continue
            if INTRO.search(raw) and not seen_num:
                preamble.setdefault(sn, []).append(line)
                continue
            if HEAD_LINE.search(raw):
                stats["running headers dropped"] += 1
                continue
            m = NUMTOK.match(line.split(" ")[0]) if line else None
            n = None
            body = ""
            if m and 1 <= int(m.group(1)) <= V:
                n = int(m.group(1))
                body = ((m.group(2) or "") + " " + " ".join(line.split(" ")[1:])).strip()
            if n is not None and body:
                kara = body[0].islower() or (not body[0].isupper() and score(body) > 0) or score(body) >= 1
                if kara and (sn, n) not in verses:
                    if pending:
                        orphans.setdefault(sn, []).extend(pending)
                        stats["unnumbered Karakhanid-looking lines before a numbered one, kept as notes"] += len(pending)
                        pending = []
                    verses[(sn, n)] = {"text": body, "line": f"{k}:{i}", "lost": False}
                    last = ("K", n)
                    seen_num = True
                    continue
                # modern line of verse n
                if (sn, n) not in verses and pending:
                    verses[(sn, n)] = {"text": " ".join(pending), "line": f"{k}:{i}", "lost": True}
                    stats["verses whose number the OCR lost, taken from the unnumbered Karakhanid lines before the modern line"] += 1
                elif pending:
                    orphans.setdefault(sn, []).extend(pending)
                    stats["unnumbered Karakhanid-looking lines before a numbered one, kept as notes"] += len(pending)
                pending = []
                modern.setdefault((sn, n), []).append(body)
                last = ("M", n)
                seen_num = True
                continue
            # unnumbered line
            short_tail = (last and last[0] == "K" and not verses[(sn, last[1])]["text"].rstrip().endswith(".")
                          and re.fullmatch(rf"[{LETTERS}'’]{{3,}}\.?", line))
            if not wordlike(line) and not short_tail:
                stats["lines of the Arabic column / ornaments (OCR garbage) dropped"] += 1
                if len(dropped_sample) < 40 and i % 7 == 0:
                    dropped_sample.append(raw.strip()[:80])
                continue
            sc = score(line)
            if short_tail:
                verses[(sn, last[1])]["text"] += " " + line
                stats["Karakhanid continuation lines joined to their verse"] += 1
                continue
            if re.match(r"^\d{1,3}\s+\S", line) and not re.match(r"^\d{1,3}\.", line):
                notes.setdefault(sn, []).append(line)       # footnote: «5 Bu harflere ...»
                last = ("F", 0)
                continue
            if not seen_num:
                preamble.setdefault(sn, []).append(line)
                if sc >= 0 and line[0].islower():
                    heads.setdefault(sn, []).append(line)
                continue
            if sc > 0 and line[0].islower():
                if last and last[0] == "K" and not verses[(sn, last[1])]["text"].rstrip().endswith("."):
                    verses[(sn, last[1])]["text"] += " " + line
                    stats["Karakhanid continuation lines joined to their verse"] += 1
                else:
                    pending.append(line)
                continue
            if last and last[0] == "M":
                modern[(sn, last[1])][-1] += " " + line
            elif not seen_num:
                preamble.setdefault(sn, []).append(line)
                if sc >= 0 and line[0].islower():
                    heads.setdefault(sn, []).append(line)
            else:
                notes.setdefault(sn, []).append(line)
        if pending:
            orphans.setdefault(sn, []).extend(pending)
            stats["unnumbered Karakhanid-looking lines before a numbered one, kept as notes"] += len(pending)

    # --- split a region among its surahs when intro lines were lost, then scan
    for first, k, lo, hi in regions:
        group = [first]
        nxt_first = next((n for n in order if n > first), 115)
        group = list(range(first, nxt_first))
        if len(group) == 1:
            scan(first, k, lo, hi)
            continue
        # K(1)-type resets: lines whose first token is «1.»
        L = vol_lines[k]
        cuts = [lo]
        ones = [i for i in range(lo + 5, hi) if re.match(r"^1\.\s?[a-zçğıöşüâîû]", clean(L[i]))]
        # use the first expected_n-1 ones that come after enough verses of the current surah
        cur = 0
        for i in ones:
            if len(cuts) >= len(group):
                break
            nums = [int(m.group(1)) for j in range(cuts[-1], i)
                    if not INTRO.search(L[j]) and (m := re.match(r"^(\d{1,3})\.\s?[a-zçğıöşüâîû]", clean(L[j])))]
            if nums and max(nums) >= counts[group[len(cuts) - 1]] - 3:
                back = i
                for j in range(i, max(i - 40, cuts[-1]), -1):
                    if re.search(r"s[uüe]r[eâaé]t[uü]", L[j]):
                        back = j
                        break
                cuts.append(back)
        if len(cuts) != len(group):
            issues.append(f"region of surahs {group[0]}-{group[-1]}: found {len(cuts)} of {len(group)} surah starts by verse-number resets")
        cuts.append(hi)
        for idx, sn in enumerate(group[:len(cuts) - 1]):
            scan(sn, k, cuts[idx], cuts[idx + 1])

    # --- coverage
    per_surah: dict[int, list[int]] = {}
    for (sn, n) in verses:
        per_surah.setdefault(sn, []).append(n)
    miss = T.missing_in_range(per_surah, 1, 114)
    present = T.covered(per_surah)
    got = sum(len(set(v)) for v in per_surah.values())
    print(f"issues: {issues}")
    print(f"verses present {got}/6236; surahs with misses {len(miss)}; missing {sum(len(v) for v in miss.values())}")
    print(dict(stats))
    if a.debug:
        sn = a.debug
        print(present.get(str(sn)), miss.get(str(sn)))
        for n in sorted(x for (s_, x) in verses if s_ == sn)[:6]:
            print(n, verses[(sn, n)]["text"][:120])
    lost_nums = sorted(f"{sn}:{n}" for (sn, n), v in verses.items() if v["lost"])
    if a.dry:
        worst = sorted(((len(v), k) for k, v in miss.items()), reverse=True)[:12]
        print("worst:", worst, "number_lost verses:", len(lost_nums))
        return

    # --- segments
    def sq(x: str) -> str:
        return re.sub(r"\s+", " ", x).strip()
    segs: list[dict] = []
    for (sn, n), v in sorted(verses.items()):
        g = {"seg": f"{SID}:{sn}:{n}", "s": sn, "a": n, "a_end": n, "page": v["line"], "text": sq(v["text"])}
        if v["lost"]:
            g["number_lost"] = True
        segs.append(g)
    for sn, ls in sorted(heads.items()):
        segs.append({"seg": f"{SID}:{sn}:head", "s": sn, "a": None, "a_end": None,
                     "head": "surah heading lines / the edition's Karakhanid surah note and basmala (lower-case lines before verse 1)",
                     "text": sq(" ".join(ls))})
    segs.sort(key=lambda g: (g["s"], -1 if g["seg"].endswith(":head") else g["a"]))
    nsegs: list[dict] = []
    for (sn, n), ls in sorted(modern.items()):
        nsegs.append({"seg": f"{NSID}:{sn}:{n}#modern", "s": sn, "a": n, "a_end": n,
                      "head": "modern Turkish translation printed under the interlinear verse (edition's comparison text)",
                      "text": sq(" ".join(ls))})
    for sn in sorted(set(preamble) | set(notes) | set(orphans)):
        V = counts[sn]
        if preamble.get(sn):
            nsegs.append({"seg": f"{NSID}:{sn}:intro", "s": sn, "a": 1, "a_end": V, "head": "surah intro lines before verse 1 (modern note, heading, basmala)",
                          "text": sq(" ".join(preamble[sn]))})
        for kind, bag, label in (("notes", notes, "footnotes and unassigned modern lines of the surah (the OCR does not keep which verse a marker belongs to)"),
                                 ("orphans", orphans, "Karakhanid-looking lines that could not be tied to a verse number")):
            if bag.get(sn):
                for c, (_, _, text) in enumerate(T.chunks(bag[sn], 3500)):
                    nsegs.append({"seg": f"{NSID}:{sn}:{kind}:{c:02d}", "s": sn, "a": 1, "a_end": V, "head": label, "text": text})
    for k, _ in VOLS:
        first = min((i for (n_, kk, i, e) in regions if kk == k), default=len(vol_lines[k]))
        for c, (f, e, text) in enumerate(T.chunks(vol_lines[k][:first], 3500)):
            nsegs.append({"seg": f"{NSID}:front-{k}:{c:03d}", "page": f"{k}:{f}", "head": f"front matter before the first surah of volume file {k}",
                          "text": sq(" ".join(clean(x) or x for x in text.split("\n")))})
    for k, _ in GLOSS:
        for c, (f, e, text) in enumerate(T.chunks(vol_lines[k], 3500)):
            nsegs.append({"seg": f"{NSID}:{k}:{c:04d}", "page": f"{k}:{f}",
                          "head": "volume " + ("7" if k == "gl7" else "8") + ": glossary / concordance (Açıklamalı Sözlük) - OCR as is, margin ornaments included",
                          "text": text})
    raw_files = {str(p.relative_to(IC.CORPUS / SID)): IC.C.sha256(p) for _, p in raws}
    T.ensure_source(SID, {
        "id": SID, "title": "Karahanlı Türkçesi satır-arası Kur'an tercümesi (TİEM 73), Ünlü edition",
        "author": "anonymous (Karakhanid interlinear; copyist Muhammad b. al-Ḥājj Dawlatshāh al-Shīrāzī, 734 H / 1333-34)",
        "translator": "anonymous", "death_ah": None, "kind": "meal", "tradition": "", "language": "tr", "turkic_stage": "Karakhanid",
        "edition": "Suat Ünlü, Karahanlı Türkçesi İlk Türkçe Satır-Arası Transkribeli Kur'an Türcümesi (TİEM 73) - Türkiye Türkçesi Mealli "
                   "Karşılaştırmalı Kur'an-ı Kerim, volumes 1-4 (text) and 7-8 (glossary), Konya: Selçuklu Belediyesi, 2018 "
                   "(vol. 1 ISBN 978-605-4886-36-4); transcription of the whole manuscript with a modern Turkish translation under each verse",
        "edition_editor": "Suat Ünlü", "edition_publisher": "Konya Selçuklu Belediyesi", "edition_year": 2018,
        "manuscript": "Istanbul, Türk ve İslam Eserleri Müzesi (TİEM) 73, 452 leaves, complete (114 surahs)",
        "access": "yerel", "locator": "ayah", "urls": [URL], "uploader": "daulet.cubex@gmail.com", "archive_identifier": IDENT,
        "licence": "scholarly edition; archive.org third-party upload; local research use",
        "panel": False, "cross_witnesses": ["MEAL-KARAHANLI-TIEM73"],
        "notes_parts": {"static": "scholarly edition; archive.org third-party upload; local research use"},
    }, None)
    src = IC.CORPUS / SID / "source.json"
    meta = IC.json.loads(src.read_text(encoding="utf-8"))
    meta["files"] = raw_files
    meta["fetched_at"] = T._dt.datetime.now(T._dt.timezone.utc).isoformat()
    meta["acquisition"] = {"date": T.TODAY, "state": "raw_downloaded", "files": len(raw_files), "ingestion_status": "pending",
                           "note": "OCR texts (djvu.txt) of an archive.org third-party upload; no PDF kept."}
    src.write_text(IC.json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    T.ensure_source(NSID, {
        "id": NSID, "title": "Ünlü TİEM 73 edition: modern Turkish translation, footnotes, front matter, glossary volumes",
        "author": "Suat Ünlü (edition); modern translation by Abdülkadir Şener, Cemal Sofuoğlu, Mustafa Yıldırım", "kind": "reference",
        "tradition": "academic", "language": "tr", "turkic_stage": "Karakhanid",
        "edition": "same edition as MEAL-KARAHANLI-TIEM73-UNLU", "access": "yerel", "locator": "section", "urls": [URL],
        "uploader": "daulet.cubex@gmail.com", "archive_identifier": IDENT,
        "licence": "scholarly edition; archive.org third-party upload; local research use",
        "raw_shared": [f"../{SID}/raw/acquired-{T.TODAY}/"], "panel": False, "files": {},
        "coverage": "all 114 surahs: modern translation lines tied to their verses; footnotes and intros tied to their surah",
    }, None)
    old_mis = {k: [len(set(per_surah.get(int(k), []))), counts[int(k)]] for k in miss}
    ing = {"script": "enrichment/v2/fetch/import_meal_karahanli_unlu.py", "from": raw_files,
           "method": "OCR djvu.txt; Karakhanid verse lines found by verse number, margin ornament tokens stripped, modern lines told apart by case and word lists",
           "edition_range": "surahs 1-114 (the whole manuscript)", "covered": present, "missing": miss,
           "verse_count_mismatch": old_mis, "verses_with_number_lost_in_ocr": lost_nums,
           "intro_lines_lost": [str(x) for x in lost], "issues": issues, "counts": T.tally(stats), "dropped_sample": dropped_sample}
    IC.write(SID, segs, ing, {
        "coverage": f"1-114 ({got}/6236 ayat; {sum(len(v) for v in miss.values())} lost in the OCR, listed in ingestion.missing)",
        "notes": "Whole TİEM 73 manuscript in Ünlü's transcribed edition (Konya 2018), OCR of a scan with heavy page-margin ornaments. "
                 f"{got} of 6,236 verses have their Karakhanid line; {sum(len(v) for v in miss.values())} verses are missing "
                 f"({len(miss)} surahs affected) because their line fell into the OCR garbage of the Arabic column; "
                 f"{len(lost_nums)} verses had their number lost and were placed by position (`number_lost`). "
                 "Special letters of the transliteration (â, ä, ö, ü, ı, ğ, ñ and the ligature signs) are often misread: "
                 "text is OCR as is, not corrected. " + T.NOTE})
    IC.write(NSID, nsegs, {"script": "enrichment/v2/fetch/import_meal_karahanli_unlu.py", "from": raw_files,
                           "method": "modern lines and footnotes of the same pages; glossary volumes as chunks",
                           "counts": T.tally(stats), "issues": []}, {})


if __name__ == "__main__":
    main()
