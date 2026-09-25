#!/usr/bin/env python3
"""Check every {ar:...} tag of a reading against its sources, in one call.

For each tag:
  exact      the Arabic occurs verbatim (NFC) in the package or the Quran text
  fixable    it occurs once diacritics, Quranic marks, tatweel and alef/ya variants are ignored;
             --fix rewrites the tag with the exact source form
  missing    not found anywhere: correct the quote or drop the tag
  wrong-ayah the tag is followed closely (≤40 chars, same sentence) by (S:A) citations and none of
             those ayat contains it (checked only for quotes that occur somewhere in the Quran text)

Usage: python3 _commentary/v9/verify_ar.py READING PACKAGE_DIR [--fix]
Exit status 1 when a missing or wrong-ayah tag remains.
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

QURAN_TEXT = Path(__file__).resolve().parents[3] / "quran-data" / "data" / "text" / "quran-uthmani.tsv"
TAG_RE = re.compile(r"\{\s*ar\s*:\s*(?P<ar>[^{},\n]*?)\s*,\s*tr\s*:")
CITE_RE = re.compile(r"\((\d{1,3}):(\d{1,3})\)")
_FOLD = str.maketrans({"ٱ": "ا", "أ": "ا", "إ": "ا", "آ": "ا", "ى": "ي", "ـ": None})


def _dropped(ch: str) -> bool:
    return unicodedata.category(ch) in ("Mn", "Cf") or ch in "ـۥۦۣ۞۩"


def loose(text: str) -> tuple[str, list[int]]:
    """Folded text plus, for each folded character, its index in the NFC original."""
    out, idx, prev_space = [], [], False
    for i, ch in enumerate(text):
        if _dropped(ch):
            continue
        if ch.isspace():
            if prev_space:
                continue
            ch, prev_space = " ", True
        else:
            prev_space = False
        ch = ch.translate(_FOLD)
        if ch:
            out.append(ch)
            idx.append(i)
    return "".join(out), idx


def exact_span(orig: str, idx: list[int], start: int, end: int) -> str:
    a, b = idx[start], idx[end - 1] + 1
    while b < len(orig) and _dropped(orig[b]):
        b += 1
    return orig[a:b]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("reading")
    ap.add_argument("package")
    ap.add_argument("--fix", action="store_true")
    args = ap.parse_args()

    reading_path = Path(args.reading)
    text = unicodedata.normalize("NFC", reading_path.read_text(encoding="utf-8"))
    sources = [unicodedata.normalize("NFC", p.read_text(encoding="utf-8"))
               for p in sorted(Path(args.package).glob("*.md"))]
    quran = {}
    for line in QURAN_TEXT.read_text(encoding="utf-8-sig").splitlines():  # "S:A|text"
        ref, _, ayah = line.partition("|")
        if ayah:
            quran[ref.strip()] = unicodedata.normalize("NFC", ayah.lstrip("\ufeff"))
    sources.append("\n".join(quran.values()))
    blob = "\n".join(sources)
    blob_loose, blob_idx = loose(blob)
    quran_loose = {k: loose(v)[0] for k, v in quran.items()}

    counts = {"exact": 0, "fixed": 0, "fixable": 0, "missing": 0, "wrong-ayah": 0}
    problems, replacements = [], []
    for m in TAG_RE.finditer(text):
        ar = m.group("ar").strip()
        line_no = text.count("\n", 0, m.start()) + 1
        ar_loose = loose(ar)[0].strip()
        new_ar = ar
        if ar in blob:
            counts["exact"] += 1
        else:
            pos = blob_loose.find(ar_loose) if ar_loose else -1
            if pos < 0:
                counts["missing"] += 1
                problems.append(f"line {line_no}: missing  {ar}")
                continue
            new_ar = exact_span(blob, blob_idx, pos, pos + len(ar_loose)).replace("\n", " ۝ ")
            if new_ar == ar:  # spans ayat joined with ۝
                counts["exact"] += 1
            elif args.fix:
                counts["fixed"] += 1
                replacements.append((m.start("ar"), m.end("ar"), new_ar))
            else:
                counts["fixable"] += 1
                problems.append(f"line {line_no}: fixable  {ar}  →  {new_ar}")
        # citation check: (S:A) refs that follow the tag closely (within 40 chars, no sentence end between)
        tail = text[text.index("}", m.end()) + 1:]
        stop = min([x for x in (tail.find("{ar:"), tail.find("\n"), tail.find(". ")) if x >= 0] or [len(tail)])
        near = CITE_RE.search(tail[:stop])
        cite = near if near and near.start() <= 40 else None
        if cite and any(ar_loose in q for q in quran_loose.values()):
            refs = [f"{c.group(1)}:{c.group(2)}" for c in CITE_RE.finditer(tail[near.start():stop])]
            if not any(ar_loose in quran_loose.get(r, "") for r in refs):
                counts["wrong-ayah"] += 1
                problems.append(f"line {line_no}: wrong-ayah  {ar}  cited {', '.join(refs)}")

    if replacements:
        for a, b, new in reversed(replacements):
            text = text[:a] + new + text[b:]
        reading_path.write_text(text, encoding="utf-8")

    print(" ".join(f"{k}={v}" for k, v in counts.items()))
    for p in problems:
        print(p)
    return 1 if counts["missing"] or counts["wrong-ayah"] else 0


if __name__ == "__main__":
    sys.exit(main())
