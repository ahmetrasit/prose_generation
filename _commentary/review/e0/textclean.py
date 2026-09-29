"""Text cleaning shared by the E0 supply builder and the E0 checks (one definition, so both agree).

- strip_edition_footnotes: the printed Ṣiḥāḥ carries its editor's footnotes inside the OpenITI text. Some quote late
  works (Lisān, Tāj al-ʿArūs, al-Qāmūs, Ibn Barrī's glosses on al-Jawharī) or manuscript variants. That is late
  material inside an "early" entry, so the note is replaced by a visible marker. A note is recognised only by a
  footnote number followed, in the same OpenITI segment, by an editorial cue; a segment that opens with Ibn Barrī or is
  signed by the Būlāq editor ("قاله نصر") is the editor's as a whole.
- strip_openiti_markers: page markers (PageV01P193), manuscript markers (ms0159), line joins (~~), Quran-quote markers
  (@QB@ / @QE@) and page numbers (@359@).
"""
from __future__ import annotations

import re

FOOTNOTE_MARK = "[edition footnote omitted]"
_SEG = re.compile(r"(\s#\s)")
_NUM = re.compile(r"\(\d{1,2}\)")
_J = r"\s*(?:~~\s*)?"  # an OpenITI line join may sit between the words of a cue
_CUE = re.compile(rf"(?:و?ف[يى]{_J}(?:اللسان|القاموس|المخطوط[ةه]?)|ابن{_J}بر[يى](?![ا-ي])|بعض{_J}النسخ|"
                  rf"لسان{_J}العرب{_J}وتاج|تاج{_J}العروس|المخطوطات)")
_BARRI_OPEN = re.compile(rf"^\s*(?:#\s*)?قال{_J}ابن{_J}بر[يى](?![ا-ي])")
# a whole segment is the editor's when it is signed by the Bulaq editor Nasr al-Hurini ("قاله نصر"). A segment opening
# with "=" is not: OpenITI uses it for ordinary text continued after a page break.
_EDITOR_SEGMENT = re.compile(rf"قاله{_J}نصر")


def strip_edition_footnotes(text: str, source_id: str) -> str:
    if source_id != "sihah" or not text:
        return text
    parts = _SEG.split(text)
    out = []
    for p in parts:
        if _SEG.fullmatch(p) or not p:
            out.append(p)
            continue
        if _EDITOR_SEGMENT.search(p):
            out.append(FOOTNOTE_MARK)
            continue
        c = _CUE.search(p)
        if not c:
            out.append(p)
            continue
        if _BARRI_OPEN.match(p):
            out.append(FOOTNOTE_MARK)
            continue
        nums = [m for m in _NUM.finditer(p) if m.start() < c.start()]
        if nums:
            # the note runs from its number to the end of the segment
            out.append(p[:nums[-1].start()].rstrip() + (" " if p[:nums[-1].start()].strip() else "") + FOOTNOTE_MARK)
        else:
            out.append(p)
    return "".join(out)


_MARKERS = [(re.compile(r"PageV\d+P\d+"), " "), (re.compile(r"\bms\d+\b"), " "), (re.compile(r"@Q[BE]@"), " "),
            (re.compile(r"@\d+@"), " "), (re.compile(r"~~"), " ")]


def strip_openiti_markers(text: str) -> str:
    for rx, rep in _MARKERS:
        text = rx.sub(rep, text)
    return re.sub(r"[ \t]{2,}", " ", text)


def clean_early(text: str, source_id: str) -> str:
    return strip_openiti_markers(strip_edition_footnotes(text or "", source_id)).strip()
