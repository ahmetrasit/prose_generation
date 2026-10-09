#!/usr/bin/env python3
"""MEAL-EAT-SIVAS-DELICE + REF-EAT-SIVAS-DELICE-NOTES: the Old Anatolian Turkish interlinear Qur'an translation of the
Sivas manuscript (Sivas Kongre ve Etnografya Müzesi E.Y. 84/176, XV century), leaves 105b-170b only = Mâ'ide 5:1 to
A'râf 7:133, in İbrahim Delice's master's thesis «Eski Anadolu Türkçesi İle Yazılmış Satırarası Bir Kur'an Tercümesi
(Gramer - Metin - Çeviri - Sözlük) (105b-170b)» (Cumhuriyet Üniversitesi, Sosyal Bilimler Enstitüsü, Sivas 1992;
supervisor Yrd. Doç. Dr. Bilal Yücel). The other published part of the same manuscript is MEAL-EAT-SIVAS-KUTUKCU
(535b-616b).

Input: the OCR text of archive.org item EskiAnadoluTrkkesiIleYazYlmSatrarasBirKuranTercmesi (uploader
empireofhassaan@hotmail.com), fetched into raw/acquired-2026-10-09/.

The «Metin ve Günümüz Türkiye Türkçesi» part alternates two kinds of pages:
  - the transcription of a leaf (a lone «112b» opens it): the manuscript's lines are numbered «(1)» ... «(11)»,
    the verses are separated by « / » (no verse numbers), the footnotes follow («106a/4 word: ... -metin-»);
  - the modern Turkish translation of the same stretch: entries «(112b/1-6) text /33/» whose bracket gives the leaf and
    lines the verse occupies and whose last token is the verse number.
Segments: the manuscript text split at the « / » separators into units, the units numbered as the verses of
their surah (the surah starts at the manuscript's own heading «şuret ul-en'âm ... âyet» and basmala), checked against
the modern entries: where the number of units of a surah does not equal the verses it covers, the units between two
agreeing anchors are stored as a group a..a_end. The modern translation and the footnotes go to the reference source,
the translation tied to its verses.

  python3 -B enrichment/v2/fetch/import_meal_eat_sivas_delice.py [--dry]
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

SID, NSID = "MEAL-EAT-SIVAS-DELICE", "REF-EAT-SIVAS-DELICE-NOTES"
IDENT = "EskiAnadoluTrkkesiIleYazYlmSatrarasBirKuranTercmesi"
URL = f"https://archive.org/details/{IDENT}"
FOLIO = re.compile(r"^\s*(\d{3})\s?([ab])\s*$")
PAGE_NO = re.compile(r"^\s*[-–—]\s*\d{1,3}\s*[-–—]?\s*$|^\s*\d{1,3}\s*$")
MOD_START = re.compile(r"^\s*\(\s*(?:(\d{3}\s?[ab])\s?[/l1]\s?)?([\dlIbt]{1,2})(?:\s?-\s?(?:(\d{3}\s?[ab])\s?/\s?)?[^)]{0,10})?\s*[)J]")
MOD_END = re.compile(r"/\s?([\dIl]{1,3})\s?/\s*$")
FOOT = re.compile(r"^\s*\d{3}[ab]\s?/\s?\d{1,2}\b")
SURAH_HEAD = re.compile(r"[sş]uret?\s*u?\s*[l1']{0,2}\s*[-' ]?\s*(?:ul)?")
HEAD_MS = re.compile(r"\(\s*\d{1,2}\s*[);]\s*[sş]uret\s*u?\s*l?\s*-?\s*([a-zçğıöşü'â]+)", re.I)
BISM = re.compile(r"bi?s[mr]+i?l+[aâ]hi?\s?'?r-?ra[hf]mani?\s?'?r-?ra[hn]?[iî]m", re.I)
LINE_MARK = re.compile(r"\(\s*([\dlIb*;]{1,3})\s*[)J>]")
FIX = str.maketrans({"l": "1", "I": "1", "b": "6"})
SURAHS = [5, 6, 7]
STARTS = {5: "MAÎDE SURESİ", 6: "EN'AM", 7: "A'RAF"}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    counts = IC.ayah_counts()
    raw = T.ensure_raw(SID, IDENT, "Anadolu_Tukcesi_Ile_Yazilmish", "delice_105b-170b_djvu.txt")
    L = T.read_lines(raw)
    stats: Counter = Counter()
    issues: list[str] = []
    r0 = next(i for i, l in enumerate(L) if FOLIO.match(l) and l.strip() == "105b")
    r1 = next((i for i in range(r0, len(L)) if re.match(r"^\s*-A-\s*$", L[i])), len(L))

    # ---- walk the text part: the kind of each line (old text of a leaf / modern translation) by structure, then by wording
    OLD = re.compile(r"\b(dakı|dagı|da£ı|pes|bayık|bayı£|anlar|anlarun|anlarnun|çalab\w*|yalavâ?c\w*|eyit\w*|eyide\w*|ol-kim|şol|tafirı|"
                     r"tanrı|dutıcı\w*|oldılar|eyledi\w*|iy|kim|ya[ ']?n[iîl]|virin\w*|getür\w*|şakın\w*|ögret\w*|işit\w*)\b", re.I)
    NEW = re.compile(r"\b(ve|bir|bu|için|olan|Allah|edin|değil|ise|onlar|gibi|şüphesiz|ki|de|da|ama|eğer|çok|her|ancak|etti|ettik)\b")
    folio = ""
    items: list[tuple[str, str]] = []                # ("folio", id) | ("line", text)
    mod_entries: list[dict] = []
    foot_notes: list[tuple[str, str]] = []
    cur: dict | None = None
    cur_fol = "105b"
    modern_lines: list[str] = []
    DASHED = re.compile(r"^\s*[-–—]\s*\d{1,3}\s*[-–—]\s*$")

    def close_entry() -> None:
        nonlocal cur
        if cur is not None:
            mod_entries.append(cur)
            cur = None

    # line-level state machine: a modern entry opens at «(coordinate) ...» and closes at «/n/»; a lone leaf id opens old text
    # that runs to the next entry, dashed page number or footnote block; inside an open entry, a leaf id suspends it
    state = "ms"            # ms: old text | mod: inside a modern entry | msx: old text interrupting an open entry
    DASHED_ = re.compile(r"^\s*[-–—]\s*\d{1,3}\s*[-–—]\s*$")
    for i in range(r0, r1):
        s_ = L[i].strip()
        if not s_ or s_ == "• • •":
            continue
        if DASHED_.match(s_):
            stats["thesis page numbers dropped"] += 1
            if state == "msx":
                state = "mod"
            continue
        if PAGE_NO.match(s_) and not FOLIO.match(s_):
            stats["lone figures dropped"] += 1
            continue
        fm = FOLIO.match(s_)
        if fm:
            folio = fm.group(1) + fm.group(2)
            items.append(("folio", folio))
            state = "msx" if state in ("mod", "msx") else "ms"
            continue
        if FOOT.match(s_):
            foot_notes.append((folio, s_))
            continue
        coord = MOD_START.match(s_)
        explicit = bool(coord and re.match(r"^\(\s*(?:\d{3}\s?[ab]|[\dlIbt]{1,2}\s?-)", s_))
        old_sc, new_sc = len(OLD.findall(s_)), len(NEW.findall(s_))
        if state == "mod":
            if explicit and cur is not None and not MOD_END.search(cur["text"]):
                close_entry()
            if coord and explicit and cur is None:
                pass
        if state in ("ms", "msx") and coord and (explicit or new_sc > old_sc) and not (old_sc > new_sc + 1):
            state = "mod"
            close_entry()
        elif state == "mod" and cur is not None and old_sc >= new_sc + 2 and len(re.findall(r"\(\s*[\dlIb*;]{1,2}\s*[)J>]", s_)) >= 1:
            state = "msx"          # old text interrupting the entry (a leaf printed in the middle)
        if state in ("ms", "msx"):
            items.append(("line", s_))
            continue
        modern_lines.append(s_)
        if coord and (cur is None or explicit):
            close_entry()
            f0, l0, f1 = coord.group(1), coord.group(2), coord.group(3)
            if f0:
                cur_fol = re.sub(r"\s", "", f0)
            ln = l0.translate(FIX)
            cur = {"folio": cur_fol, "line": int(ln) if ln.isdigit() else None, "text": s_[coord.end():].strip(), "src": i, "n": None}
            if f1:
                cur_fol = re.sub(r"\s", "", f1)
        elif cur is not None:
            cur["text"] += " " + s_
        else:
            stats["modern lines outside any entry, kept in the reference source"] += 1
            foot_notes.append((folio, "[modern page, no entry] " + s_))
            continue
        me = MOD_END.search(cur["text"]) or re.search(r"/\s?([\dIl]{1,3})\s?/", cur["text"])
        if me:
            n = me.group(1).translate(FIX)
            cur["n"] = int(n) if n.isdigit() else None
            cur["text"] = (cur["text"][:me.start()] + " " + cur["text"][me.end():]).strip()
            close_entry()
            state = "ms"
    close_entry()
    # ---- leaf blocks of the old text (a leaf id opens one); split where a surah heading falls inside
    blocks: list[dict] = []
    for kind_, t in items:
        if kind_ == "folio":
            blocks.append({"leaf": t, "lines": []})
        elif blocks:
            blocks[-1]["lines"].append(t)
        else:
            blocks.append({"leaf": "", "lines": [t]})
    leaf_seq: list[str] = []
    for b_ in blocks:
        txt = ""
        for ln_ in b_["lines"]:
            if txt.endswith("-") and not txt.endswith("--"):
                txt = txt[:-1] + (" " + ln_ if ln_.startswith("(") else ln_)
            else:
                txt = (txt + " " + ln_).strip()
        b_["text"] = re.sub(r"\s+", " ", txt).strip()
        leaf_seq.append(b_["leaf"])
    fold_tr = str.maketrans({"ı": "i", "İ": "i", "ğ": "g", "ş": "s", "Ş": "s", "ç": "c", "ö": "o", "ü": "u", "â": "a", "î": "i", "û": "u", "'": "", "’": ""})
    sn_cur = 5
    pieces: list[dict] = []          # (surah, leaf, text) in reading order
    for bi, b_ in enumerate(blocks):
        txt = b_["text"]
        cuts_ = []
        for m_ in re.finditer(r"[sşŞ]uret", txt, re.I):
            span = txt[m_.start():m_.start() + 40].lower().translate(fold_tr)
            for sn, rx in ((6, r"e\s?n\s?\w?\s?a\s?m"), (7, r"a\s?\W?\s?r\s?a\s?f")):
                if sn == sn_cur + 1 and re.search(rx, span):
                    cuts_.append((m_.start(), sn))
        pos = 0
        for cpos, sn in cuts_:
            if txt[pos:cpos].strip():
                pieces.append({"s": sn_cur, "leaf": b_["leaf"], "text": txt[pos:cpos].strip(), "block": bi})
            sn_cur, pos = sn, cpos
        if txt[pos:].strip():
            pieces.append({"s": sn_cur, "leaf": b_["leaf"], "text": txt[pos:].strip(), "block": bi})
    # modern entries -> surah by number resets; verse n lies from its printed start leaf to the start leaf of verse n+1
    leaf_ord: dict[str, int] = {}
    for lf in leaf_seq:
        if lf and lf not in leaf_ord:
            leaf_ord[lf] = len(leaf_ord)
    ents: list[dict] = []
    sn_, prev_n = 5, 0
    for e_ in mod_entries:
        n_ = e_.get("n")
        if not n_:
            continue
        if n_ <= prev_n - 10 and sn_ < 7:
            sn_ += 1
        prev_n = n_
        ents.append({"s": sn_, "n": n_, "leaf": e_["folio"], "text": e_["text"]})
    verse_leaf = {(e["s"], e["n"]): leaf_ord.get(e["leaf"]) for e in ents}
    ords_by_s: dict[int, list[tuple[int, int]]] = {5: [], 6: [], 7: []}
    for (sn, n), o in sorted(verse_leaf.items()):
        if o is not None:
            ords_by_s[sn].append((n, o))
    ledger: dict[tuple[int, str], dict] = {}
    for pc in pieces:
        o = leaf_ord.get(pc["leaf"])
        key = (pc["s"], pc["leaf"], pc["block"])
        vs = []
        lst = ords_by_s[pc["s"]]
        for idx, (n, on) in enumerate(lst):
            nxt = lst[idx + 1][1] if idx + 1 < len(lst) else max(leaf_ord.get(q["leaf"], on) for q in pieces if q["s"] == pc["s"])
            if o is not None and on <= o <= max(nxt, on):
                vs.append(n)
        pc["verses"] = vs
    # verses of the leaves without any modern entry: between their neighbours
    last_hi = {5: 0, 6: 0, 7: 0}
    for pc in pieces:
        vs = pc["verses"]
        if vs:
            pc["lo"], pc["hi"], pc["inferred"] = min(vs), max(vs), False
            last_hi[pc["s"]] = pc["hi"]
        else:
            pc["lo"], pc["hi"], pc["inferred"] = None, None, True
    for idx, pc in enumerate(pieces):
        if pc["inferred"]:
            prev_ = next((q for q in reversed(pieces[:idx]) if q["s"] == pc["s"] and q["hi"]), None)
            nxt_ = next((q for q in pieces[idx + 1:] if q["s"] == pc["s"] and q["lo"]), None)
            lo = prev_["hi"] if prev_ else 1
            hi = nxt_["lo"] if nxt_ else lo
            pc["lo"], pc["hi"] = lo, max(hi, lo)
    # the last piece of each surah runs to the surah's last verse (the edition ends at 7:133)
    ends_ = {5: counts[5], 6: counts[6], 7: 133}
    for sn in (5, 6, 7):
        last_pc = [q for q in pieces if q["s"] == sn][-1]
        if last_pc["hi"] < ends_[sn]:
            last_pc["hi"] = ends_[sn]
            last_pc["completed"] = True
    print("leaf pieces:", len(pieces), "with printed verse numbers:", sum(1 for q in pieces if not q["inferred"]))
    per_surah: dict[int, list[int]] = {}
    for pc in pieces:
        per_surah.setdefault(pc["s"], []).extend(range(pc["lo"], pc["hi"] + 1))
    ranges_ = ends_
    miss = {str(sn): [x for x in range(1, ranges_[sn] + 1) if x not in set(per_surah.get(sn, []))] for sn in (5, 6, 7)}
    miss = {k: v for k, v in miss.items() if v}
    print("verses covered by a leaf:", {sn: len(set(per_surah.get(sn, []))) for sn in (5, 6, 7)}, "missing", miss)
    if a.dry:
        print(dict(stats))
        return
    segs: list[dict] = []
    seen_ids: Counter = Counter()
    for pc in pieces:
        base = f"{SID}:{pc['s']}:{pc['lo']}#{pc['leaf'] or 'noleaf'}"
        seen_ids[base] += 1
        sid_ = base if seen_ids[base] == 1 else f"{base}.{seen_ids[base]}"
        g = {"seg": sid_, "s": pc["s"], "a": pc["lo"], "a_end": pc["hi"], "page": pc["leaf"],
             "head": f"old text of leaf {pc['leaf'] or '?'} (a leaf segment: verses {pc['lo']}-{pc['hi']} begin or continue on it)",
             "text": f"[{pc['leaf']}] " + pc["text"] if pc["leaf"] else pc["text"], "leaf_segment": True}
        flags = []
        if pc["inferred"]:
            flags.append("verse range inferred from the neighbouring leaves (no modern entry names this leaf)")
        if pc.get("completed"):
            flags.append("range end completed to the surah's last verse")
        if flags:
            g["flags"] = flags
        segs.append(g)
    got_total = sum(len(set(v)) for v in per_surah.values())
    total = sum(ends_.values())
    present = T.covered({sn: per_surah.get(sn, []) for sn in (5, 6, 7)})
    nsegs: list[dict] = []
    modern_ids: Counter = Counter()
    for e in ents:
        modern_ids[(e["s"], e["n"])] += 1
        nsegs.append({"seg": f"{NSID}:{e['s']}:{e['n']}#modern" + (f".{modern_ids[(e['s'], e['n'])]}" if modern_ids[(e["s"], e["n"])] > 1 else ""), "s": e["s"], "a": e["n"], "a_end": e["n"],
                      "head": "modern Turkish translation printed in the edition (Delice)", "text": e["text"]})
    for n, (lf, t) in enumerate(foot_notes):
        nsegs.append({"seg": f"{NSID}:note:{n:03d}", "page": lf, "head": f"edition's footnote or stray modern line (leaf {lf})", "text": t})
    for name, lo, hi, label in (("front", 0, r0, "thesis front matter, introduction, grammar"),
                                ("back", r1, len(L), "glossary (Sözlük), bibliography, summaries")):
        for n, (f, e, text) in enumerate(T.chunks(L[lo:hi], 3500)):
            nsegs.append({"seg": f"{NSID}:{name}:{n:04d}", "page": f"line{lo + f}", "head": label, "text": text})
    T.ensure_source(SID, {
        "id": SID, "title": "Eski Anadolu Türkçesi satır-arası Kur'an tercümesi, Sivas manuscript, leaves 105b-170b (Delice)",
        "author": "anonymous (XV century)", "translator": "anonymous", "death_ah": None, "kind": "meal", "tradition": "",
        "language": "tr", "turkic_stage": "Old Anatolian Turkish",
        "edition": "İbrahim Delice, Eski Anadolu Türkçesi İle Yazılmış Satırarası Bir Kur'an Tercümesi (Gramer - Metin - Çeviri - Sözlük) "
                   "(105b-170b), master's thesis, Cumhuriyet Üniversitesi, Sosyal Bilimler Enstitüsü, Sivas 1992 "
                   "(supervisor Yrd. Doç. Dr. Bilal Yücel)",
        "edition_editor": "İbrahim Delice", "edition_publisher": "Cumhuriyet Üniversitesi (master's thesis)", "edition_year": 1992,
        "manuscript": "Sivas Kongre ve Etnografya Müzesi E.Y. 84/176 (622 leaves; this edition: 105b-170b); the other part "
                      "is MEAL-EAT-SIVAS-KUTUKCU (535b-616b)",
        "access": "yerel", "locator": "ayah", "urls": [URL], "uploader": "empireofhassaan@hotmail.com", "archive_identifier": IDENT,
        "licence": "scholarly edition; archive.org third-party upload; local research use", "panel": False, "cross_witnesses": [],
    }, raw)
    T.ensure_source(NSID, {
        "id": NSID, "title": "Delice, Sivas interlinear thesis: modern translation, notes, grammar, glossary",
        "author": "İbrahim Delice", "kind": "reference", "tradition": "academic", "language": "tr", "turkic_stage": "Old Anatolian Turkish",
        "edition": "same thesis as MEAL-EAT-SIVAS-DELICE", "access": "yerel", "locator": "section", "urls": [URL],
        "uploader": "empireofhassaan@hotmail.com", "archive_identifier": IDENT,
        "licence": "scholarly edition; archive.org third-party upload; local research use",
        "raw_shared": [f"../{SID}/{raw.relative_to(IC.CORPUS / SID)}"], "panel": False, "files": {},
    }, None)
    ing = {"script": "enrichment/v2/fetch/import_meal_eat_sivas_delice.py",
           "from": {str(raw.relative_to(IC.CORPUS / SID)): IC.C.sha256(raw)},
           "method": "OCR djvu.txt; old text by manuscript leaf (leaf ids open it); verse ranges of a leaf from the modern entries' printed leaf references",
           "edition_range": "leaves 105b-170b = Mâ'ide 5:1 to A'râf 7:133 (surahs 5, 6 complete; 7 up to verse 133 of 206)",
           "covered": present, "missing": miss, "verse_count_mismatch": {k: [len(set(per_surah.get(int(k), []))), ends_[int(k)]] for k in miss},
           "leaf_segments": len(pieces), "leaves_found_in_ocr": len(set(leaf_seq) - {""}), "leaves_expected": 132,
           "issues": ["old-text verse separators «/» are not one per verse (145 units for 120 verses in Mâ'ide), so verses are not cut inside a leaf"],
           "counts": T.tally(stats), "dropped_sample": []}
    IC.write(SID, segs, ing, {
        "coverage": f"5:1-7:133 by leaf ({got_total}/{total} verses lie on a stored leaf; 7:134-206 are outside the edition)",
        "notes": "Partial: leaves 105b-170b of the Sivas manuscript only. The OCR of the scan is poor; the old text is stored LEAF by LEAF "
                 "(segment = one manuscript leaf, a..a_end = the verses that begin or continue on it, read from the modern entries' printed "
                 "leaf references; adjacent leaves share the verse they split). No verse is cut inside a leaf: the edition's verse separators "
                 "do not give one verse per mark. Manuscript line numbers (n) stay in the text; leaf ids are the OCR readings (about a third of the 132 leaves have no readable id and are merged into the leaf before; a few ids are misread). " + T.NOTE})
    IC.write(NSID, nsegs, {"script": "enrichment/v2/fetch/import_meal_eat_sivas_delice.py",
                           "from": {str(raw.relative_to(IC.CORPUS / SID)): IC.C.sha256(raw)}, "counts": T.tally(stats), "issues": []}, {})


if __name__ == "__main__":
    main()
