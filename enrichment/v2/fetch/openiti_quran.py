"""Qur'an lookup for the OpenITI segmenter: surah names, orthographic skeletons, quotation matching.

The reference text is quran-data/data/text/quran-uthmani.tsv ("s:a|text"; the basmala of surahs 2-114 except 9
is :0, 1:1 is the basmala of al-Fātiḥa; ayah numbers are the standard Kufan count, not shifted).

Matching works on a *skeleton*: diacritics, Qur'anic marks, tatweel and every alif/hamza are removed, the alef,
yāʾ, tāʾ marbūṭa and hamza-carrier variants are unified, spaces are dropped. That makes the Uthmani spelling
(ٱلْكِتَٰبُ, يَٰٓأَيُّهَا, إِبْرَٰهِۦمَ, ٱلصَّلَوٰةَ) meet the imlāʾī spelling of printed books (الكتاب, يا أيها, إبراهيم,
الصلاة). A quotation is looked up as a substring of the concatenated skeleton of one surah; the hit gives the
ayah (and, for quotations that run over an ayah boundary, the last ayah).
"""
from __future__ import annotations

import bisect
import re
from functools import lru_cache
from pathlib import Path

QURAN_TSV = Path("/Volumes/aro/projects/quran-data/data/text/quran-uthmani.tsv")

# 114 surahs: canonical name first, then names under which classical books head or cite them.
SURAH_NAMES = {
    1: "الفاتحة|فاتحة الكتاب|أم القرآن|أم الكتاب|الحمد", 2: "البقرة", 3: "آل عمران", 4: "النساء", 5: "المائدة",
    6: "الأنعام", 7: "الأعراف", 8: "الأنفال", 9: "التوبة|براءة", 10: "يونس", 11: "هود", 12: "يوسف", 13: "الرعد",
    14: "إبراهيم", 15: "الحجر", 16: "النحل", 17: "الإسراء|بني إسرائيل|سبحان", 18: "الكهف", 19: "مريم", 20: "طه",
    21: "الأنبياء", 22: "الحج", 23: "المؤمنون|المؤمنين", 24: "النور", 25: "الفرقان", 26: "الشعراء", 27: "النمل",
    28: "القصص", 29: "العنكبوت", 30: "الروم", 31: "لقمان", 32: "السجدة|ألم تنزيل|الم تنزيل|ألم السجدة|الم السجدة",
    33: "الأحزاب", 34: "سبأ", 35: "فاطر|الملائكة", 36: "يس|يسن", 37: "الصافات", 38: "ص", 39: "الزمر",
    40: "غافر|المؤمن", 41: "فصلت|حم السجدة", 42: "الشورى|حم عسق", 43: "الزخرف", 44: "الدخان", 45: "الجاثية",
    46: "الأحقاف", 47: "محمد|القتال", 48: "الفتح", 49: "الحجرات", 50: "ق", 51: "الذاريات", 52: "الطور",
    53: "النجم", 54: "القمر|اقتربت", 55: "الرحمن", 56: "الواقعة", 57: "الحديد", 58: "المجادلة|المجادلة",
    59: "الحشر", 60: "الممتحنة", 61: "الصف", 62: "الجمعة", 63: "المنافقون|المنافقين", 64: "التغابن",
    65: "الطلاق", 66: "التحريم", 67: "الملك|تبارك", 68: "القلم|ن|نون|ن والقلم", 69: "الحاقة",
    70: "المعارج|سأل سائل", 71: "نوح", 72: "الجن", 73: "المزمل", 74: "المدثر", 75: "القيامة",
    76: "الإنسان|الدهر|هل أتى|هل أتى على الإنسان", 77: "المرسلات", 78: "النبأ|عم|عم يتساءلون",
    79: "النازعات", 80: "عبس", 81: "التكوير|إذا الشمس كورت|كورت", 82: "الانفطار|إذا السماء انفطرت|انفطرت",
    83: "المطففين|التطفيف|ويل للمطففين", 84: "الانشقاق|إذا السماء انشقت|انشقت", 85: "البروج", 86: "الطارق",
    87: "الأعلى|سبح|سبح اسم ربك", 88: "الغاشية|هل أتاك", 89: "الفجر", 90: "البلد", 91: "الشمس", 92: "الليل",
    93: "الضحى", 94: "الشرح|الانشراح|ألم نشرح", 95: "التين", 96: "العلق|اقرأ", 97: "القدر",
    98: "البينة|لم يكن", 99: "الزلزلة|الزلزال|إذا زلزلت", 100: "العاديات", 101: "القارعة",
    102: "التكاثر|ألهاكم", 103: "العصر", 104: "الهمزة", 105: "الفيل|ألم تر", 106: "قريش|لإيلاف",
    107: "الماعون|أرأيت|الدين", 108: "الكوثر", 109: "الكافرون|الكافرين|قل يا أيها الكافرون",
    110: "النصر|إذا جاء نصر الله", 111: "المسد|تبت|اللهب|أبي لهب", 112: "الإخلاص|قل هو الله أحد|الصمد",
    113: "الفلق", 114: "الناس",
}

# ---------------------------------------------------------------- normalisation

_DIAC = re.compile(r"[ؐ-ًؚ-ٟۖ-ۜ۟-ۤۧ-ۭـࣰ-ࣿ]")
_MAP = str.maketrans({"أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ى": "ي", "ة": "ه", "ؤ": "و", "ئ": "ي", "ء": "",
                      "ی": "ي", "ک": "ك", "ھ": "ه"})


def norm(text: str) -> str:
    """Readable normal form (keeps alifs and spaces): for names and headings."""
    text = text.replace("ٰ", "ا")
    text = _DIAC.sub("", text).replace("ۥ", "").replace("ۦ", "")
    text = text.translate(_MAP)
    return re.sub(r"\s+", " ", text).strip()


def skeleton(text: str, uthmani: bool = False) -> str:
    """Spelling-neutral consonantal skeleton without spaces (see module doc)."""
    if uthmani:
        marks = "[\u064B-\u065F\u06D6-\u06ED]*"
        text = re.sub("وٰ(?=" + marks + "[ةا])", "ا", text)  # ٱلصَّلَوٰة → الصلاة, ٱلرِّبَوٰا۟ → الربا (not سموات)
        text = re.sub("ىٰ(?=" + marks + "[ء-ي])", "ا", text)  # ٱلتَّوْرَىٰة → التوراة (not عَلَىٰ)
        text = re.sub("ۦ(?=[ء-ي])", "ي", text)  # إِبْرَٰهِۦمَ → إبراهيم
    text = _DIAC.sub("", text).replace("ٰ", "").replace("ۥ", "").replace("ۦ", "")
    text = text.translate(_MAP)
    text = re.sub(r"[^ء-ي]", "", text)
    return text.replace("ا", "")


# ---------------------------------------------------------------- Qur'an tables

class Quran:
    def __init__(self, path: Path = QURAN_TSV):
        self.ayahs: dict[int, list[tuple[int, str]]] = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            ref, _, txt = line.partition("|")
            if ":" not in ref:
                continue
            s, a = (int(x) for x in ref.split(":"))
            if a == 0:
                continue
            self.ayahs.setdefault(s, []).append((a, txt.lstrip("﻿")))
        self.count = {s: len(v) for s, v in self.ayahs.items()}
        # per-surah concatenated skeleton + start offsets
        self.concat: dict[int, str] = {}
        self.starts: dict[int, list[int]] = {}
        for s, rows in self.ayahs.items():
            parts, starts, pos = [], [], 0
            for a, t in rows:
                sk = skeleton(t, uthmani=True)
                starts.append(pos)
                parts.append(sk)
                pos += len(sk)
            self.concat[s] = "".join(parts)
            self.starts[s] = starts
        # name lookup: normalised name -> surah, longest names first
        names = []
        for s, alts in SURAH_NAMES.items():
            for n in alts.split("|"):
                names.append((norm(n), s))
        self.names = sorted(set(names), key=lambda x: -len(x[0]))

    def valid(self, s: int, a: int) -> bool:
        return 1 <= s <= 114 and 1 <= a <= self.count[s]

    def surah_by_name(self, text: str) -> int | None:
        """Surah whose name begins `text` (text already stripped of 'سورة'); whole-word match."""
        t = norm(text).strip(" «»()[]{}\"'.:،-")
        for n, s in self.names:
            if t == n or (t.startswith(n) and len(t) > len(n) and not ("ء" <= t[len(n)] <= "ي")):
                return s
            # cited without the article: 'سورة بقرة' is rare; accept only for long names
            if n.startswith("ال") and len(n) > 5 and (t == n[2:] or t.startswith(n[2:] + " ")):
                return s
        return None

    def ayah_at(self, s: int, pos: int) -> int:
        return bisect.bisect_right(self.starts[s], pos)  # 1-based ayah number

    @lru_cache(maxsize=200000)
    def find(self, s: int, quote_sk: str) -> tuple[tuple[int, int], ...]:
        """All (a, a_end) where the quotation skeleton occurs in surah s."""
        out, c, i = [], self.concat.get(s, ""), 0
        if not quote_sk or not c:
            return ()
        while True:
            i = c.find(quote_sk, i)
            if i < 0:
                break
            a = self.ayah_at(s, i)
            a2 = self.ayah_at(s, i + len(quote_sk) - 1)
            out.append((a, a2))
            i += 1
            if len(out) > 20:
                break
        return tuple(out)


@lru_cache(maxsize=1)
def quran() -> Quran:
    return Quran()


# ---------------------------------------------------------------- evidence in a piece of text

_NAME_ALT = None


def _names_alt() -> str:
    global _NAME_ALT
    if _NAME_ALT is None:
        alts = set()
        for alts_s in SURAH_NAMES.values():
            for n in alts_s.split("|"):
                alts.add(re.escape(n))
                alts.add(re.escape(norm(n)))
        _NAME_ALT = "|".join(sorted(alts, key=len, reverse=True))
    return _NAME_ALT


QUOTE = re.compile(r"﴿([^﴾]{2,600})﴾|\{([^{}]{2,600})\}|«([^«»]{2,400})»|@QB@(.{2,600}?)@QE@")
PAREN = re.compile(r"\(([^()]{4,300})\)")                               # (…) — Qur'an quotes in some editions
DQUOTE = re.compile(r'"([^"\n]{4,300})"|“([^”\n]{4,300})”')            # "…" — lemmas in some editions
NUMREF = re.compile(r"\((\d{1,3})\s*/\s*(\d{1,3})\)")                 # (105/ 1) — s/a cross-reference
AYNUM = re.compile(r"\((\d{1,3})(?:\s*[-–]\s*(\d{1,3}))?\)"            # lemma (23) / (2- 3) — editor's ayah number
                   r"|(?<=[﴾}»])\s*(\d{1,3})(?:\s*[-–]\s*(\d{1,3}))?(?![\d/:])")  # ﴿…﴾ 214 (Ibn Mujāhid)
ALTAFSIR_HEAD = re.compile(r"\[(\d{1,3})\.(\d{1,3})(?:\s*-\s*(\d{1,3}))?\]")  # ### || [2.1-2]
ALTAFSIR_SURA = re.compile(r"\[(\d{1,3})\s*-\s*سورة")                      # ### | [1 - سورة الفاتحة]
SURA_WORD = re.compile(r"(?:^|[\s«(\[{\"'$])(?:تفسير\s+|ومن\s+)?(?:سور[ةه]|السورة التي [تي]ذكر فيها)\s+(.{1,40})")
SURA_NUM = re.compile(r"سور[ةه][^\d\n]{1,40}?[(\[]\s*(\d{1,3})\s*[)\]]")
# Shamela section headings: "[سورة سبإ (34) : الآيات 1 الى 54]" · "[سورة البقرة (2) : آية 255]" · "(83) : الآيات 1 الى 36]"
SECTION_RANGE = re.compile(r"\((\d{1,3})\)\s*:\s*(?:الآيات|الآية|آية|آيه)\s*(\d{1,3})(?:\s*(?:الى|إلى|-)\s*(\d{1,3}))?")
BACKMATTER = re.compile(r"فهرس|الفهارس|المصادر|المراجع|المحتويات|ملحق|^\(?\s*[ء-ي]\s*\)?$")


class Evidence:
    """Explicit references and quotation hits found in a string."""

    def __init__(self, q: Quran):
        self.q = q
        names = _names_alt()
        # [البقرة: 255] (البقرة: 255) [البقرة/ 61] [سورة البقرة، الآية 255] [البقرة: 1 - 5]
        self.ref = re.compile(r"[\[(]\s*(?:سورة\s+)?(" + names + r")\s*[:/،,]\s*(?:الآية|الآيات|آية)?\s*(\d{1,3})"
                              r"(?:\s*[-–]\s*(\d{1,3}))?\s*[\])]")
        # سورة بني إسرائيل آية 83 (unbracketed)
        self.ref2 = re.compile(r"سورة\s+(" + names + r")\s*[،,]?\s*(?:الآية|آية)\s*(\d{1,3})")
        # heading that is just "البقرة: 259" / "[البقرة: 259]" / "النور : ( 1 - 2 ) سورة أنزلناها …" (JK texts)
        self.headref = re.compile(r"^\s*\[?\s*(?:سورة\s+)?(" + names + r")\s*[:/]\s*\(?\s*(\d{1,3})"
                                  r"(?:\s*[-–]\s*(\d{1,3}))?\s*\)?")

    def explicit(self, text: str, heading: bool = False) -> list[tuple[int, int, int, bool]]:
        """[(s, a, a_end, strong)] in text order. strong = a structural marker (altafsir [s.a], a heading that
        starts with 'name: n', a Shamela section range); weak = an in-text citation [name: n], (s/ a)."""
        out = []
        for m in ALTAFSIR_HEAD.finditer(text):
            s, a = int(m.group(1)), int(m.group(2))
            b = int(m.group(3)) if m.group(3) else a
            if self.q.valid(s, a) and self.q.valid(s, b) and b >= a:
                out.append((m.start(), s, a, b, True))
        pats = [(self.ref, False), (self.ref2, False)] + ([(self.headref, True)] if heading else [])
        for pat, strong in pats:
            for m in pat.finditer(text):
                s = self.q.surah_by_name(m.group(1))
                if not s:
                    continue
                a = int(m.group(2))
                b = int(m.group(3)) if len(m.groups()) > 2 and m.group(3) else a
                if self.q.valid(s, a):
                    out.append((m.start(), s, a, b if self.q.valid(s, b) and b >= a else a, strong))
        for m in NUMREF.finditer(text):
            s, a = int(m.group(1)), int(m.group(2))
            if self.q.valid(s, a):
                out.append((m.start(), s, a, a, False))
        if heading:
            for m in SECTION_RANGE.finditer(text):
                s, a = int(m.group(1)), int(m.group(2))
                b = int(m.group(3)) if m.group(3) else a
                if 1 <= s <= 114 and self.q.valid(s, a):
                    out.append((m.start(), s, a, b if self.q.valid(s, b) and b >= a else a, True))
        seen, res = set(), []
        for x in sorted(out):
            if x[1:4] not in seen:
                seen.add(x[1:4])
                res.append(x[1:])
        return res

    def collect(self, text: str, s: int) -> list[tuple[tuple[tuple[int, int], ...], bool]]:
        """In-surah cues in text order: (candidate (a, a_end) hits, strong). Strong cues: explicit citations of
        surah s, editor's ayah numbers verified against the preceding words, long quotations with a single hit;
        weak cues: other matched quotations (﴿﴾ {} «» @QB@, and (…) in editions that bracket the Qur'an so)."""
        ev = []
        for m in ALTAFSIR_HEAD.finditer(text):
            if int(m.group(1)) == s and self.q.valid(s, int(m.group(2))):
                a = int(m.group(2))
                b = int(m.group(3)) if m.group(3) and self.q.valid(s, int(m.group(3))) else a
                ev.append((m.start(), ((a, max(a, b)),), True))
        for pat in (self.ref, self.ref2):
            for m in pat.finditer(text):
                if self.q.surah_by_name(m.group(1)) == s and self.q.valid(s, int(m.group(2))):
                    a = int(m.group(2))
                    b = int(m.group(3)) if len(m.groups()) > 2 and m.group(3) and self.q.valid(s, int(m.group(3))) else a
                    ev.append((m.start(), ((a, max(a, b)),), True))
        for m in NUMREF.finditer(text):
            if int(m.group(1)) == s and self.q.valid(s, int(m.group(2))):
                ev.append((m.start(), ((int(m.group(2)), int(m.group(2))),), True))
        for m in QUOTE.finditer(text):
            frag = next(g for g in m.groups() if g is not None)
            sk = skeleton(frag)
            if len(sk) >= 5:
                hits = self.q.find(s, sk)
                if hits:
                    ev.append((m.start(), hits, len(sk) >= 20 and len(hits) == 1))
        for m in list(PAREN.finditer(text)) + list(DQUOTE.finditer(text)):
            sk = skeleton(next(g for g in m.groups() if g is not None))
            if len(sk) >= 8:
                hits = self.q.find(s, sk)
                if hits:
                    ev.append((m.start(), hits, False))
        for m in AYNUM.finditer(text):
            g1, g2 = (m.group(1), m.group(2)) if m.group(1) else (m.group(3), m.group(4))
            n = int(g1)
            n2 = int(g2) if g2 else n
            if not self.q.valid(s, n) or n2 < n or not self.q.valid(s, n2):
                continue
            words = re.sub(r"[()«»{}\[\]﴿﴾.…:،]", " ", text[max(0, m.start() - 90):m.start()]).split()
            for k in (4, 3, 2):
                sk = skeleton(" ".join(words[-k:]))
                if len(sk) >= 4 and any(a <= n2 and b >= n for a, b in self.q.find(s, sk)):
                    ev.append((m.start(), ((n, n2),), True))
                    break
        return [(h, st) for _, h, st in sorted(ev, key=lambda x: x[0])]

    def lemma_cues(self, text: str, s: int, lo: int, hi: int) -> list[tuple[tuple[tuple[int, int], ...], bool]]:
        """Unbracketed lemmas: the opening words of each paragraph (up to 'أي', ':' …) matched inside surah s and
        kept only when the hit lies in [lo, hi] (a heading range or the reading window). Weak cues."""
        out = []
        for line in text.split("\n"):
            head = re.split(r"\s(?:أي|يعني|يقول|قال|معناه|يريد)\s|[:،؛.(«{﴿]", line.strip(), maxsplit=1)[0]
            words = head.split()[:6]
            if len(words) < 2:
                continue
            sk = skeleton(" ".join(words))
            if len(sk) < 9:
                continue
            hits = tuple(h for h in self.q.find(s, sk) if lo <= h[0] <= hi)
            if hits:
                out.append((hits, False))
        return out

    def quotes(self, text: str, s: int) -> list:
        return self.collect(text, s)

    def surah_heading(self, head: str) -> int | None:
        """Surah number named by a heading ('سورة البقرة', '[2 - سورة البقرة]', '«سورة أرأيت» (107)',
        'فاتحة الكتاب')."""
        m = ALTAFSIR_SURA.search(head)
        if m and 1 <= int(m.group(1)) <= 114:
            return int(m.group(1))
        m = SURA_WORD.search(head)
        if m:
            s = self.q.surah_by_name(m.group(1))
            if s:
                return s
        m = SURA_NUM.search(head)  # name not recognised: trust a number only when it is the only cue
        if m and 1 <= int(m.group(1)) <= 114:
            return int(m.group(1))
        t = norm(head).strip(" «»()[]{}\"'.:،-")
        m = re.search(r"\(?\s*(\d{1,3})\s*\)?$", t)
        num = int(m.group(1)) if m else None
        t = t[:m.start()].strip(" «»()[]{}\"'.:،-") if m else t
        for n, s in self.q.names:
            if t == n and len(n) > 2 and (num is None or num == s):
                return s
        return None
