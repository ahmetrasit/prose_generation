"""OpenITI mARkdown → segments.jsonl (streaming; the book is never held in memory).

  ######OpenITI# … #META#Header#End#   header: the #META# lines are returned for source.json
  ### | … / ### || … / ### ||| …       headings → `head` (the heading path, outermost first)
  # …  (new paragraph), ~~ … (continuation)
  PageV01P023 (also PageEndV01P023)    end-of-page marker: the text before it is on vol 1 p. 23
  ms123                                 milestones: dropped
  %~%                                   hemistich separator → " … "

Segments break at every heading; inside a heading's text they are ~1500-character runs of whole paragraphs
(very long paragraphs are cut at sentence ends). In Qur'an-ordered books a new segment is also started where a
paragraph opens with a Qur'an quotation, so that segments follow the commented ayahs.

Surah/ayah (only when work["qorder"]):
  1. headings: altafsir "[2 - سورة البقرة]" / "[2.1-2]", Shamela "[النور: 29]", "سورة X" headings set the surah;
     an explicit ayah reference in the heading applies to every segment under it;
  2. otherwise, inside the current surah only: Shamela citations "[البقرة: 5]" and quotations ﴿…﴾ {…} «…»
     matched against the Qur'an text (Uthmani file, spelling-neutral skeleton). The first piece of evidence at or
     after the previous segment's ayah gives `a`; `a_end` extends over directly following evidence (gaps ≤ 2).
  3. no evidence → a = null (s stays the current surah when one is established); nothing is guessed.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from openiti_quran import BACKMATTER, Evidence, quran

PAGE = re.compile(r"Page(?:End)?V(\d+)P(\d+)")
PAGE_REAL = re.compile(r"Page(?:End)?V\d+P(?!0+\b)\d+")  # PageV00P000 is a placeholder, not a page
MS = re.compile(r"\bms\d+\b|\bms[A-Z]\w*\d+\b")
FN = re.compile(r"«\d{1,3}»")  # Shamela footnote calls (the notes themselves were removed by OpenITI)
HADITH_NO = re.compile(r"^\s*\[?(\d{1,5})\]?\s*[-–ـ]\s*\S")
QUOTE_OPEN = re.compile(r"^\s*(?:﴿|\{|«|@QB@|و?قوله\s*(?:تبارك وتعالى|تعالى|عز وجل|جل ذكره|جل)?\s*[:：]?\s*[﴿{«(@])")
INLINE_SURA = re.compile(r"\$\s*(?=سور[ةه]\s)")                         # "… PageV01P016 $ سورة البقرة"
RUNNING_HEAD = re.compile(r"Page(?:End)?V\d+P\d+\s+(?=سور[ةه]\s)")     # running title after a page break

TARGET, MAXLEN, MINLEN, PARA_MAX = 1500, 2600, 400, 3200


def clean(t: str) -> str:
    t = re.sub(r"</?[a-zA-Z][^<>]{0,80}>", " ", t)  # stray HTML (</span> in some Shamela headings)
    t = PAGE.sub(" ", t)
    t = MS.sub(" ", t)
    t = FN.sub("", t)
    t = t.replace("@QB@", "﴿").replace("@QE@", "﴾")           # OpenITI Qur'an tags → ornate brackets
    t = t.replace("%~%", " … ")
    t = re.sub(r"\s*%\s*%\s*", " … ", t).replace("%", " ")      # JK poetry: % hemistich % % hemistich %
    t = t.replace("|", " ")                                     # JK print line-break bars
    t = re.sub(r"@", " ", t)                                    # stray @ left from removed tags
    t = re.sub(r"[<>]", " ", t)                                 # JK angle-bracket markup (> > … < <).replace("‏", "").replace("‎", "")
    return re.sub(r"[ \t ]+", " ", t).strip()


def split_long(p: str) -> list[str]:
    """Cut an over-long paragraph at sentence ends (., ؟, !, :) near TARGET."""
    out = []
    while len(p) > PARA_MAX:
        cut = -1
        for m in re.finditer(r"[.؟!:](?=\s)|\s(?=قال|وقال|حدثنا|حدثني|أخبرنا)", p[: TARGET + 600]):
            if m.end() >= TARGET - 600:
                cut = m.end()
                break
        if cut < 0:
            cut = p.rfind(" ", 0, TARGET) + 1 or TARGET
        out.append(p[:cut])
        p = p[cut:]
    out.append(p)
    return out


class Segmenter:
    def __init__(self, work: dict, out, has_pages: bool):
        self.w, self.out, self.has_pages = work, out, has_pages
        self.id = work["id"]
        self.qorder = work.get("qorder")
        self.hadith = work.get("mode") == "hadith"
        self.ev = Evidence(quran()) if self.qorder else None
        self.q = quran() if self.qorder else None
        self.heads: dict[int, str] = {}
        self.acc: list[str] = []
        self.acc_len = 0
        self.queue: list[dict] = []
        self.used: dict[str, int] = {}
        self.n = 0
        self.cur_s = None
        self.prev_a = 0
        self.sec_ref = None
        self.in_surah, self.surah_level = False, 1
        self.miss_streak = 0
        self.refs_by_level: dict[int, tuple] = {}
        self.hadith_no = None
        self.stats = dict(segments=0, with_s=0, with_a=0, a_from_head=0, chars=0)
        self.surahs: set[int] = set()
        self.last = None

    # ------------------------------------------------------------ headings
    def heading(self, line: str):
        self.flush()
        body = line.lstrip("#").strip()
        m = re.match(r"^(\|+)\s*", body)
        level = len(m.group(1)) if m else 1
        body = body[m.end():] if m else body
        body = re.sub(r"^[A-Z]+\|\s*", "", body)  # |EDITOR| etc.
        body = re.sub(r"^(?:AUTO|CHECK)\s+", "", body)  # OpenITI auto-tagged headings
        body = clean(body)
        self.heads = {k: v for k, v in self.heads.items() if k < level}
        self.hadith_no = None
        if body:
            self.heads[level] = body
        if self.qorder:
            self.sec_ref = None
            s = self.ev.surah_heading(body)
            refs = self.ev.explicit(body, heading=True)
            strong = [r for r in refs if r[3]]
            if s and (self.cur_s is None or s > self.cur_s or
                      (s < self.cur_s and re.match(r"^[\[«(]?\s*(?:\d{1,3}\s*-\s*)?(?:تفسير\s+)?سور", body))):
                if s != self.cur_s:
                    self.cur_s, self.prev_a, self.miss_streak = s, 0, 0
                self.in_surah, self.surah_level = True, level
            elif self.in_surah and level <= self.surah_level and BACKMATTER.search(body) and not refs:
                self.in_surah = False  # indexes / appendices after the last surah
            if refs:
                pick = strong[0] if strong else None  # structural markers may also move back (fix a stray jump)
                if pick is None and self.cur_s:
                    pick = next((r for r in refs if r[0] == self.cur_s), None)
                if pick is None and (self.cur_s is None or refs[0][0] >= self.cur_s):
                    pick = refs[0]
                if pick:
                    pick = pick[:3]
                    if pick[0] != self.cur_s:
                        self.cur_s, self.prev_a, self.miss_streak = pick[0], 0, 0
                    self.sec_ref = pick
                    if not self.in_surah:
                        self.in_surah, self.surah_level = True, level
            elif self.cur_s and self.in_surah and not s:
                # a heading that quotes the ayah it introduces ({…} (11), «…», @QB@…@QE@)
                pick = self.choose(self.ev.collect(body, self.cur_s))
                if pick:
                    self.sec_ref = (self.cur_s, *pick)
            # a sub-heading without a reference of its own stays under its parent heading's ayah reference
            self.refs_by_level = {k: v for k, v in self.refs_by_level.items() if k < level}
            if s:
                self.refs_by_level = {}
            if self.sec_ref:
                self.refs_by_level[level] = self.sec_ref
                self.prev_a = self.sec_ref[1]
            elif self.refs_by_level:
                parent = self.refs_by_level[max(self.refs_by_level)]
                if parent[0] == self.cur_s:
                    self.sec_ref = parent

    def running_head(self, text: str):
        """A running title 'سورة X' after a page marker: moves the surah forward only (never back)."""
        if not self.qorder:
            return
        m = re.match(r"سور[ةه]\s+(.{1,40})", text)
        s = self.q.surah_by_name(m.group(1)) if m else None
        if s and (self.cur_s is None or s > self.cur_s):
            self.flush()
            self.cur_s, self.prev_a, self.sec_ref = s, 0, None
            self.in_surah, self.surah_level = True, 1

    # ------------------------------------------------------------ paragraphs
    def feed(self, p: str):
        """Paragraph entry point: splits off inline surah markers ('$ سورة X', running titles) first."""
        cuts = [(m.start(), m.end(), "head") for m in INLINE_SURA.finditer(p)]
        if self.w.get("running_heads"):
            cuts += [(m.end(), m.end(), "run") for m in RUNNING_HEAD.finditer(p)]
        if not cuts:
            return self.para(p)
        pos = 0
        for st, en, kind in sorted(cuts):
            if st > pos:
                self.para(p[pos:st])
            if kind == "head":
                m = re.match(r"(سور[ةه]\s+\S+(?:\s+\S+)?)", p[en:])
                self.heading("### | " + (m.group(1) if m else p[en:en + 30]))
                pos = en + (m.end() if m else 0)
            else:
                self.running_head(p[en:en + 60])
                pos = en
        if pos < len(p):
            self.para(p[pos:])

    def para(self, p: str):
        if not p.strip():
            return
        markers = [m for m in PAGE.findall(p) if int(m[1])]
        body = clean(p)
        if not body:  # a marker-only paragraph closes the page of what precedes it
            if markers:
                if self.acc:
                    self.acc.append(p)
                elif self.last is not None:
                    self.last["markers"].extend(markers)
                    self.resolve()
            return
        if self.hadith:
            m = HADITH_NO.match(body)
            if m:
                self.flush()
                self.hadith_no = m.group(1)
            elif self.acc_len >= 3 * MAXLEN:  # front matter / very long commentary: keep segments bounded
                self.flush()
        elif self.acc_len >= MINLEN and (
                self.acc_len + len(body) > MAXLEN or self.acc_len >= TARGET or
                (self.qorder and self.acc_len >= 600 and QUOTE_OPEN.match(body))):
            self.flush()
        for piece in split_long(p) if len(p) > PARA_MAX and not self.hadith else [p]:
            if self.acc_len >= TARGET and not self.hadith:
                self.flush()
            self.acc.append(piece)
            self.acc_len += len(piece)

    # ------------------------------------------------------------ chunks
    def flush(self):
        if not self.acc:
            return
        raw = "\n".join(self.acc)
        self.acc, self.acc_len = [], 0
        text = "\n".join(x for x in (clean(r) for r in raw.split("\n")) if x)
        markers = [m for m in PAGE.findall(raw) if int(m[1])]
        if not text:
            if markers and self.last is not None:
                self.last["markers"].extend(markers)
                self.resolve()
            return
        head = " › ".join(self.heads[k] for k in sorted(self.heads))
        seg = {"seg": None, "s": None, "a": None, "a_end": None, "page": None,
               "head": head[:300] if head else None, "text": text, "markers": markers}
        if self.hadith:
            seg["hadith_no"] = self.hadith_no
        if self.w.get("mode") == "lexicon" and self.heads:
            seg["entry"] = re.sub(r"\s+", "", self.heads[max(self.heads)])[:40]
        if self.qorder:
            self.assign(seg)
        self.queue.append(seg)
        self.last = seg
        self.resolve()

    def choose(self, evid, lo=None, hi=None):
        """Pick the ayah a segment comments on from its cues (text order).
        1. the first cue with a hit in [prev_a, prev_a + 25] (inside [lo, hi] when a heading gave a range);
        2. else the first strong cue at/after prev_a;
        3. else, when the previous segment also found nothing ahead (we ran past the text after a stray forward
           jump), the first strong cue — or two cues agreeing within 2 ayahs — anywhere in the surah.
        a_end extends over directly following cues (gaps ≤ 2)."""
        lo = self.prev_a if lo is None else lo
        top = hi if hi is not None else 10 ** 4
        win = min(top, lo + 25)
        first = None
        for hits, strong in evid:
            ok = [h for h in hits if lo <= h[0] <= win]
            if ok:
                first = min(ok)
                break
        if not first:
            for hits, strong in evid:
                ok = [h for h in hits if lo <= h[0] <= top]
                if ok and strong:
                    first = min(ok)
                    break
        if not first and evid and self.miss_streak >= 1 and hi is None:
            for k, (hits, strong) in enumerate(evid):
                if strong or any(abs(h[0] - g[0]) <= 2 for h in hits for hh, _ in evid[k + 1:] for g in hh):
                    first = min(hits)
                    break
        if not first:
            if evid:
                self.miss_streak += 1
            return None
        self.miss_streak = 0
        a, a_end = first
        for (x, y) in sorted({h for hits, _ in evid for h in hits if h[0] >= a}):
            if x <= a_end + 2 and y <= top:
                a_end = max(a_end, y)
        return a, a_end

    def assign(self, seg):
        if self.sec_ref:
            s, a, b = self.sec_ref
            seg.update(s=s, a=a, a_end=b)
            self.stats["a_from_head"] += 1
            if b - a >= 2:  # a heading range (e.g. "الآيات 1 الى 54"): narrow it with the segment's own cues
                lo = max(a, self.prev_a) if self.prev_a <= b else a
                cues = self.ev.collect(seg["text"], s) or self.ev.lemma_cues(seg["text"], s, lo, b)
                pick = self.choose(cues, lo=lo, hi=b)
                if pick:
                    seg.update(a=pick[0], a_end=pick[1])
                    self.prev_a = pick[0]
            return
        s = self.cur_s
        if not s or not self.in_surah:
            return
        seg["s"] = s
        cues = self.ev.collect(seg["text"], s) or self.ev.lemma_cues(seg["text"], s, self.prev_a, self.prev_a + 25)
        pick = self.choose(cues)
        if pick:
            seg.update(a=pick[0], a_end=pick[1])
            self.prev_a = pick[0]

    def resolve(self, final=False):
        """Give pages to queued segments and write out the resolved prefix of the queue."""
        if self.has_pages:
            page = None
            for seg in reversed(self.queue):
                if seg["markers"]:
                    page = seg["markers"][0]
                if seg["page"] is None and page is not None:
                    seg["page"] = page
            # a queued segment whose own first marker exists takes it (it starts on that page)
            for seg in self.queue:
                if seg["markers"]:
                    seg["page"] = seg["markers"][0]
        while self.queue and (not self.has_pages or self.queue[0]["page"] is not None or final):
            self.emit(self.queue.pop(0))

    def emit(self, seg):
        self.n += 1
        seg["emitted"] = True
        pg = seg["page"]
        seg = dict(seg)
        seg["page"] = f"v{int(pg[0])}p{int(pg[1])}" if pg else None
        if self.hadith and seg.get("hadith_no"):
            key = seg["hadith_no"]
        elif seg.get("entry"):
            key = seg["entry"]
        elif self.has_pages and pg:
            key = seg["page"]
        elif seg.get("s") and seg.get("a"):
            key = f"{seg['s']}:{seg['a']}" + (f"-{seg['a_end']}" if seg["a_end"] and seg["a_end"] != seg["a"] else "")
        else:
            key = f"n{self.n}"
        k = self.used.get(key, 0) + 1
        self.used[key] = k
        seg["seg"] = f"{self.id}:{key}" + ("" if k == 1 else f"#{k}")
        if seg.get("a") and not seg.get("a_end"):
            seg["a_end"] = seg["a"]
        st = self.stats
        st["segments"] += 1
        st["chars"] += len(seg["text"])
        st["with_s"] += bool(seg.get("s"))
        st["with_a"] += bool(seg.get("a"))
        if seg.get("s"):
            self.surahs.add(seg["s"])
        self.out.write(json.dumps({k: v for k, v in seg.items() if k not in ("markers", "emitted", "entry")},
                                  ensure_ascii=False) + "\n")

    def close(self):
        self.flush()
        self.resolve(final=True)


def ranges(xs: list[int]) -> str:
    out, i = [], 0
    while i < len(xs):
        j = i
        while j + 1 < len(xs) and xs[j + 1] == xs[j] + 1:
            j += 1
        out.append(str(xs[i]) if i == j else f"{xs[i]}-{xs[j]}")
        i = j + 1
    return ",".join(out)


def has_page_markers(path: Path) -> bool:
    with path.open(encoding="utf-8", errors="replace") as f:
        for line in f:
            if PAGE_REAL.search(line):
                return True
    return False


def parse(path: Path, work: dict, out_path: Path) -> tuple[dict, dict]:
    """Segment one OpenITI text file. Returns (header meta, stats)."""
    meta: dict[str, list[str]] = {}
    has_pages = has_page_markers(path)
    tmp = out_path.with_suffix(".jsonl.tmp")
    with path.open(encoding="utf-8", errors="replace") as f, tmp.open("w", encoding="utf-8") as out:
        sg = Segmenter(work, out, has_pages)
        in_header = True
        cur: list[str] = []
        for line in f:
            line = line.rstrip("\n").lstrip("﻿")
            if in_header:
                if line.startswith("#META#Header#End"):
                    in_header = False
                    continue
                elif line.startswith("#META#"):
                    body = line[6:]
                    k, _, v = body.partition("::") if "::" in body else body.partition(":")
                    v = v.strip()
                    if v and v not in ("NODATA", "NOTGIVEN", "NOCODE"):
                        meta.setdefault(k.strip(), []).append(v)
                elif not line.startswith("######OpenITI#") and line.startswith("### "):
                    in_header = False  # file without a header block
                if in_header:
                    continue
            if line.startswith("###") or line.startswith("# |"):
                if cur:
                    sg.feed(" ".join(cur))
                    cur = []
                sg.heading(line)
            elif line.startswith("~~"):
                cur.append(line[2:].strip())
            elif line.startswith("# ") or line == "#":
                if cur:
                    sg.feed(" ".join(cur))
                cur = [line[2:].strip()]
            elif not line.strip():
                if cur:
                    sg.feed(" ".join(cur))
                    cur = []
            else:
                cur.append(line.strip())
        if cur:
            sg.feed(" ".join(cur))
        sg.close()
    tmp.replace(out_path)
    st = sg.stats
    st["has_pages"] = has_pages
    st["surahs"] = ranges(sorted(sg.surahs))
    return {k: " | ".join(v) for k, v in meta.items()}, st
