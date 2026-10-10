#!/usr/bin/env python3
"""Enrichment v7 verse digests: build the inputs and spawn files, check the outputs. Launches no model.

A digest records what one source says about the verses its segments are tied to: one line per segment,
one row per claim, each row with a short source-body anchor. Spawn files can be run by native agents or the
scripted runner; the same chunk files serve every model.

  digest.py build RUN (--ayat 100:1 87:6 | --surahs 2 3 | --page PATH --ayah A) --models gpt-6-luna:max --skip-done luna-max --quotes
  digest.py check RUN [--model TAG] [--chunk N]     every segment answered, current anchors and required row fields
  digest.py report RUN                              per-model totals and costs

Every skipped source or segment is printed and listed in RUN/manifest.json.
"""
import argparse
import hashlib
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'enrichment/v5'))
from common import OVERLAY, PART_CHARS, TRANSLATION_OK, connect, contains, dump, rows  # noqa: E402

V7 = ROOT / 'enrichment/v7'
BRIEF = V7 / 'briefs/digest.md'
# In the 264-agent S1/S87–114 run, none of the 18 chunks below 20k rendered characters exceeded the
# user's 120k-token context cap; 77 larger chunks did. Keep future v7 extractor inputs smaller.
DEFAULT_CHUNK_CHARS = 20_000
# Stage 1 kinds. Verse-indexed hadith has a reliable ayah tie and belongs here; untied hadith
# still needs a quotation or explicit-citation match. Poetry, wujuh and grammar retain the word route.
KINDS = ('tafsir', 'tafsir_tr', 'maani', 'nazm', 'isari', 'modern', 'qiraat', 'ulum', 'reference', 'sira', 'hadith')
PROVENANCE_KEYS = ('text_status', 'marker_found', 'align_uncertain', 'align', 'aligned_by',
                   'scan_match', 'scan_match_note', 'ocr_fixes', 'notes_ocr', 'refs', 'quran_quotes',
                   'sahih', 'graded_by', 'duplicate', 'secondary', 'page', 'printed_page')
GUIDE = {
    'tafsir': 'A Qurʾān commentary. Record the author\'s own explanation of each verse, every view it reports with '
              'who holds it, reports and narrations (the authority at the end of the chain, the gist, any grading '
              'the author states), occasions of revelation, linguistic, grammatical, rhetorical, qirāʾa, legal and '
              'theological points, disagreements and the view the author prefers, and links it draws to other verses.',
    'tafsir_tr': 'A Turkish Qurʾān commentary. Record the author\'s explanation, the views he reports and from whom, his '
                 'preferences, his word choices in rendering the verse, and the links he draws to other verses.',
    'maani': 'A maʿānī al-Qurʾān work (language and grammar of the Qurʾān). Record each lexical, grammatical and '
             'syntactic analysis, the variant readings discussed, the authorities and the poetry or Arab usage cited '
             'as evidence (poet and the word witnessed), and which analysis the author prefers.',
    'nazm': 'A work on the coherence (naẓm) of the Qurʾān. Record how the author links the verse to its neighbours, '
            'its passage and the sūra\'s theme, the structure he sees, and the other verses he connects it to.',
    'isari': 'A Sufi (ishārī) commentary. Record the outward explanation the author gives, then each inward (ishārī) '
             'reading, the authorities and Sufi masters he cites, and the spiritual lessons he draws.',
    'modern': 'A modern commentary or study. Record the author\'s reading of the verse, his arguments and evidence, the '
              'classical or modern views he engages, where he departs from them, and the links to other verses.',
    'qiraat': 'A work on the variant readings. Record each reading, its readers, the argument (ḥujja) for it, and the '
              'difference in meaning the author draws.',
    'ulum': 'A work on the Qurʾānic sciences. Record what it says about the verse: rhetoric, inimitability, '
            'abrogation, occasions of revelation, structure, with the authorities cited.',
    'reference': 'A reference work. Record what the entry says about the verse and its terms, with the scholars cited.',
    'hadith': 'A hadith collection, indexed to the verse or reached because its passage quotes the verse (a chapter '
              'heading that opens with the verse, or a report). Record each report, who it goes back to, its gist '
              'and how it bears on the verse, and any grading the collection states; for a chapter heading, also '
              'the theme the compiler files the verse under. Mark it none when the verse words only coincide.',
    'poetry': 'A poetry collection or its commentary, reached because the passage shares the verse\'s words. Record '
              'the poet, the line\'s point, and the commentator\'s gloss when it bears on the verse\'s words; mark it '
              'none when the words only coincide.',
    'wujuh': 'A wujūh wa-naẓāʾir work (the senses of a Qurʾānic word). Record each sense it gives the word in this '
             'verse, the verses it groups with it, and its authorities.',
    'grammar': 'A grammar work, reached because it cites the verse. Record the grammatical point it uses the verse '
               'for and the analysis it gives.',
    'sira': 'A biography of the Prophet or a history. Record the events it ties to the verse, its sources and '
            'reports, and any dating or occasion it gives.',
}

# Row tags (user decision 2026-10-08): every row names the verse words it is about and one type from this list.
TYPES = ('meaning', 'grammar', 'rhetoric', 'readings', 'referent', 'reports', 'sciences', 'interpretation',
         'theology', 'law', 'links', 'inward')
TYPE_GUIDE = {
    'meaning': 'what a word means: lexicon, root, etymology, Arab usage and poetry cited for the sense',
    'grammar': 'syntax, iʿrāb, morphology',
    'rhetoric': 'balāgha: word choice, order, ellipsis, oath form, why this wording',
    'readings': 'variant readings (qirāʾāt) and their arguments',
    'referent': 'who or what the words refer to',
    'reports': 'narrations, occasions of revelation, gradings',
    'sciences': 'place and order of revelation, verse counting, virtues of the sūra, abrogation',
    'interpretation': "the meaning of the verse or phrase: the author's explanation, its point or wisdom",
    'theology': 'creed and kalām',
    'law': 'legal rulings',
    'links': 'coherence with neighbouring verses or the sūra, and connections to other verses',
    'inward': 'ishārī (Sufi) readings',
}
WHOLE = '*'


def run_dir(run):
    return V7 / 'work' / run


_QURAN = None


def quran():
    """Verse text by 'S:A'."""
    global _QURAN
    if _QURAN is None:
        with connect() as con:
            _QURAN = {f'{s}:{a}': t for s, a, t in con.execute("SELECT s, a, text FROM seg JOIN src ON src.id=seg.src "
                                                              "WHERE src.kind='quran' AND a IS NOT NULL")}
    return _QURAN


def _skel(word):
    """A word's letters without vowels and without alif (Uthmani spelling drops some alifs)."""
    return normalize_map(word)[0].replace(' ', '').replace('ا', '')


def verse_tokens(verse):
    """(surface, skeleton) per word of a verse; pause marks are not words."""
    out = []
    for w in quran().get(verse, '').split():
        k = _skel(w)
        if k:
            out.append((w, k))
    return out


def word_position(word, verse):
    """Index of the verse word a tag names, or None. A tag may be a phrase: its first word decides."""
    toks = verse_tokens(verse)
    parts = [_skel(x) for x in (word or '').split() if _skel(x)]
    if not parts:
        return None
    for i, (_, k) in enumerate(toks):
        w = parts[0]
        if w == k or (len(w) >= 2 and w in k) or (len(k) >= 3 and k in w):
            return i
    return None


def tag_problems(r):
    """Problems with one row's words and type (rows of runs built with row tags, and retag outputs)."""
    out = []
    words, typ = r.get('words'), r.get('type')
    if not isinstance(words, list) or not words:
        out.append('"words" must be a non-empty list (verse words, or ["*"] for the whole verse)')
    else:
        for w in words:
            if w == WHOLE:
                continue
            if not any(all(word_position(x, v) is not None for x in str(w).split()) for v in verse_list(r.get('verses'))):
                out.append(f'word «{w}» is not in the text of {", ".join(verse_list(r.get("verses"))) or "its verses"}')
    if typ not in TYPES:
        out.append(f'type «{typ}» is not one of: {", ".join(TYPES)}')
    return out


_EXCERPTS = None
_LEGACY_INPUT_WARNED = set()
UNVERIFIED_OUTPUT_LOCS = set()


def excerpts():
    """run -> locators known or conservatively suspected to have been excerpted.

    Current manifests carry excerpt_locs. If an old run lacks the exact input snapshot, every locator in that
    run is treated as potentially excerpted; an anchor in its output cannot establish full-body coverage.
    """
    global _EXCERPTS
    if _EXCERPTS is None:
        _EXCERPTS = defaultdict(set)
        for manifest in (V7 / 'work').glob('*/manifest.json'):
            man = json.loads(manifest.read_text())
            run = manifest.parent.name
            _EXCERPTS[run].update(man.get('excerpt_locs', []))
            for c in man.get('chunks', []):
                if c.get('source_sha256'):
                    continue
                saved = saved_chunk_segments(manifest.parent, c)
                if saved is None:
                    if any((manifest.parent / 'out').glob(f"*/c{c['chunk']:02d}.jsonl")):
                        _EXCERPTS[run].update(c['locs'])
                else:
                    _EXCERPTS[run].update(loc for loc, (_, excerpt) in saved.items() if excerpt)
    return _EXCERPTS


_UNFINISHED = set()


def unfinished(f):
    """True when the chunk output f (work/RUN/out/TAG/cNN.jsonl) belongs to an agent that started under codex_run and
    has no run.json yet: its file may be partial, so it is not read (printed once per file). Runs without a runs/
    entry for the chunk (native sessions) count as finished."""
    run, tag = f.parts[-4], f.parts[-2]
    d = f.parents[2] / 'runs' / f'v7d_{run}_{tag}_{f.stem}'
    record = d / 'run.json'
    if d.is_dir() and (not record.exists() or not _completed_record(record)):
        if f not in _UNFINISHED:
            _UNFINISHED.add(f)
            print(f'NOTE {f.relative_to(V7)}: its agent has not finished; not read (its notes arrive in a later update)')
        return True
    return False


def _completed_record(path):
    try:
        x = json.loads(path.read_text())
        return x.get('turn_completed') is True and x.get('returncode') == 0
    except (OSError, ValueError):
        return False


def row_tags():
    """Tags from every retag run: row id -> (words, type)."""
    out = {}
    for f in sorted((V7 / 'work').glob('*/retag/out/*/c*.jsonl')):
        for line in f.read_text().splitlines():
            if line.strip():
                try:
                    x = json.loads(line)
                except ValueError:
                    print(f'WARNING {f.relative_to(V7)}: a line is not JSON; skipped')
                    continue
                out.setdefault(x['id'], (x.get('words'), x.get('type')))
    return out


def tag_of(model, effort):
    """Output tag of a model: luna-max, sol-high; claude-haiku-5-5 -> haiku-high, claude-sonnet-5-5 -> sonnet-high."""
    name = model.split('-')[1] if model.startswith('claude-') else model.split('-')[-1]
    return f'{name}-{effort}'


def parse_ayah(text):
    s, a = text.split(':')
    return int(s), int(a)


_VERSE_TOKEN = re.compile(r'(?:(\d+):)?(\d+)(?:\s*-\s*(?:(\d+):)?(\d+))?')
_DASHES = str.maketrans({'–': '-', '—': '-', '‒': '-', '−': '-'})
_WORD_BEFORE = re.compile(r"([^\W\d_][\w'’ʾ.-]*)\W*$")   # the word just before a verse item, if any
_BIBLE = set("""genesis gen exodus exod ex leviticus lev numbers num deuteronomy deut dt joshua josh judges judg ruth
samuel sam kings kgs chronicles chron chr ezra nehemiah neh esther esth job psalm psalms ps psa pss proverbs prov pr
ecclesiastes eccl eccles qoheleth song songs canticles cant isaiah isa jeremiah jer lamentations lam ezekiel ezek
daniel dan hosea hos joel amos obadiah obad jonah micah mic nahum nah habakkuk hab zephaniah zeph haggai hag
zechariah zech malachi mal matthew matt mt mark mk luke lk john jn acts romans rom corinthians cor galatians gal
ephesians eph philippians phil colossians col thessalonians thess timothy tim titus philemon phlm hebrews heb james
jas peter pet pt jude revelation rev apocalypse maccabees macc sirach sir ecclesiasticus tobit tob wisdom wis baruch
bar judith jdt esdras esd torah tanakh gospel bible septuagint lxx talmud mishnah gn lv nm jos jgs jb prv sg jl jon ob
zep zec rv rm revelations""".split())
_GAP = re.compile(r'^[\s,;"\'&]*$')                 # what may stand between two items of one list
RANGE_MAX = 300              # a written range longer than this is taken as a mistake, not expanded
AYAH_MAX = 286               # the longest sūra; a larger ayah number is not a verse


def verse_list(values, rejected=None):
    """Every S:A a row's `verses` or `mentions` value names. Agents mostly write ["87:6"], but also ranges ("105:3-5",
    "25:48–89"), lists in one string ("92:7,10,12", "92:3,5-7"), lists joined into one string, and annotated values
    ("Qur'an 2:255", "Surah Yusuf 12:5", "2:255 (Ayat al-Kursi)"). An ayah number without a surah takes the surah of
    the item before it, only when nothing but separators stands between them. An item right after a Bible book's name
    (_BIBLE: "Luke 1:5", "Acts 14:8-28", "1 Samuel 17") and every item after it in the same value, a range across
    sūras, reversed or longer than RANGE_MAX, an ayah above AYAH_MAX and a number with no surah are not read; when
    `rejected` is a list, each value with such an item, or with nothing read, is appended to it (2026-10-10)."""
    out = []
    for v in values if isinstance(values, list) else [values] if isinstance(values, str) else []:
        text = str(v).translate(_DASHES)
        s, end, got, bad, bible = None, 0, [], False, False
        for m in _VERSE_TOKEN.finditer(text):
            sur, a, sur2, b = m.groups()
            before = text[end:m.start()]
            if not _GAP.match(before):
                s = None                     # free text in between: a bare number after it is not an ayah
            w = _WORD_BEFORE.search(before)
            end = m.end()
            if bible or (w and w.group(1).lower().rstrip('.') in _BIBLE):
                bible, bad = True, True      # a Bible reference: it, and what follows it in this value, is not read
                continue
            s = int(sur) if sur else s
            a, b = int(a), int(b) if b else int(a)
            if s is None or not 1 <= s <= 114 or (sur2 and int(sur2) != s) or a < 1 or b < a or b - a > RANGE_MAX or b > AYAH_MAX:
                bad = True
                continue
            got += [f'{s}:{x}' for x in range(a, b + 1)]
        if (bad or not got) and rejected is not None:
            rejected.append(v)
        out += got
    return list(dict.fromkeys(out))


def gather(ayat):
    """Segments tied to the ayat (index range plus range overlay), stage-1 kinds, text held locally."""
    skipped = []
    with connect() as con:
        src = {i: (k, acc, json.loads(m or '{}')) for i, k, acc, m in con.execute('SELECT id,kind,access,meta FROM src')}
        extra = defaultdict(set)
        if OVERLAY.exists():
            for r in rows(OVERLAY):
                for a in range(r['indexed_end'] + 1, r['a_end'] + 1):
                    extra[r['s'], a].add(r['seg_id'])
        found = {}
        for s, a in ayat:
            hits = con.execute('SELECT id,seg,src,s,a,coalesce(a_end,a),head,text,extra FROM seg WHERE s=? AND a<=? '
                               'AND coalesce(a_end,a)>=?', (s, a, a)).fetchall()
            if extra[s, a]:
                q = ','.join('?' * len(extra[s, a]))
                hits += con.execute(f'SELECT id,seg,src,s,a,coalesce(a_end,a),head,text,extra FROM seg WHERE id IN ({q})',
                                    list(extra[s, a])).fetchall()
            for sid, loc, sr, ss, aa, ae, head, text, metadata in hits:
                kind, access, _ = src[sr]
                why = None
                if kind not in KINDS:
                    why = f'kind {kind}: meal table or a later stage'
                elif access != 'yerel':
                    why = f'access {access}: no local text'
                elif not (text or '').strip():
                    why = 'empty text'
                if why:
                    skipped.append({'ayah': f'{s}:{a}', 'loc': loc, 'src': sr, 'reason': why})
                    continue
                if sid in extra[s, a]:
                    ae = max(ae, a)
                if sid in found:
                    found[sid]['scope'].append(f'{s}:{a}')
                    continue
                found[sid] = {'scope': [f'{s}:{a}'], 'loc': loc, 'src': sr, 'kind': kind, 'verses': f'{ss}:{aa}' + (f'-{ae}' if ae != aa else ''),
                              'head': head or '', 'text': text, 'extra': json.loads(metadata or '{}')}
    return src, [found[k] for k in sorted(found)], skipped


def surah_level(ayat):
    """Segments tied to a surah but to no ayah (introductions, maqṣūd): reserved for the surah page; returned as
    skip records and printed, never dropped silently."""
    out = []
    with connect() as con:
        for s in sorted({s for s, _ in ayat}):
            rows_ = con.execute("SELECT seg.seg, seg.src, length(seg.text) FROM seg JOIN src ON src.id=seg.src "
                                f"WHERE seg.s=? AND seg.a IS NULL AND src.access='yerel' AND src.kind IN ({','.join('?' * len(KINDS))})",
                                (s, *KINDS)).fetchall()
            if rows_:
                print(f"NOTE surah-level S{s}: {len(rows_)} segments, {sum(r[2] for r in rows_):,} characters, "
                      'reserved for the surah page (listed in manifest.json)')
            out += [{'ayah': f'S{s}', 'loc': loc, 'src': sr, 'reason': 'surah-level: reserved for the surah page'}
                    for loc, sr, _ in rows_]
    return out


_ARABIC_DROP = set(chr(c) for c in list(range(0x0610, 0x061B)) + list(range(0x064B, 0x0660)) + list(range(0x06D6, 0x06EE)))
_ARABIC_MAP = {'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٱ': 'ا', 'ٰ': 'ا', 'ى': 'ي', 'ة': 'ه', 'ؤ': 'و', 'ئ': 'ي'}


def normalize_map(text):
    """Arabic letters only, vowel and Quranic marks dropped, alif/yā/hamza forms unified, the dagger alif written out
    (so Uthmani ٱلصَّٰلِحَٰتِ matches الصالحات) except after alif maqṣūra, where it only marks the ى already written
    (so عَلَىٰ matches على; 2026-10-10). Returns the words joined by single spaces and, per character, its index in the
    original text."""
    out, idx, space, prev = [], [], True, ''
    for i, ch in enumerate(text or ''):
        if ch in _ARABIC_DROP or ch in ('ـ', 'ء'):
            continue
        if ch == 'ٰ' and prev == 'ى':
            continue
        prev = ch
        ch = _ARABIC_MAP.get(ch, ch)
        if '\u0621' <= ch <= '\u064A':
            out.append(ch)
            idx.append(i)
            space = False
        elif not space:
            out.append(' ')
            idx.append(i)
            space = True
    return ''.join(out).strip(), idx


QUOTE_KINDS_ONE = ('ulum', 'wujuh', 'modern', 'reference', 'grammar', 'tafsir', 'tafsir_tr', 'maani', 'nazm', 'isari', 'qiraat')
QUOTE_KINDS_THREE = ('hadith', 'sira', 'poetry')
QUOTE_MAX_HITS = 40          # a 1-2 word window in more segments than this is too common alone: its 3-word windows are used
QUOTE_LIMITS = []


def quote_packet(ayat):
    """Segments with no verse key that quote an ayah's own words: windows of 1-3 words that occur in no other ayah
    (1-word windows of at least 4 letters, and only for the kinds in QUOTE_KINDS_ONE; hadith, sīra and poetry need 3
    words). Indexed hadith, sīra and poetry are also searched outside their index range and overlay; gather()
    supplies their indexed verses. Explicit citations with the full normalized verse are a conservative fallback.
    Lexicon, meal and translations are not searched. Window counts and fallback locators are recorded in
    QUOTE_LIMITS."""
    global QUOTE_LIMITS
    QUOTE_LIMITS = []
    with connect() as con:
        quran = {(s, a): normalize_map(t)[0].split() for s, a, t in
                 con.execute("SELECT s, a, text FROM seg JOIN src ON src.id=seg.src WHERE src.kind='quran'")}
        grams = defaultdict(set)
        for v, words in quran.items():
            for n in (1, 2, 3):
                for i in range(len(words) - n + 1):
                    grams[' '.join(words[i:i + n])].add(v)
        kinds = QUOTE_KINDS_ONE + QUOTE_KINDS_THREE
        eligible = (f"(seg.s IS NULL AND src.kind IN ({','.join('?' * len(kinds))}) OR seg.s IS NOT NULL "
                    f"AND seg.a IS NOT NULL AND src.kind IN ({','.join('?' * len(QUOTE_KINDS_THREE))}))")
        segs = con.execute(f"SELECT seg.id,seg.seg,seg.src,src.kind,seg.head,seg.text,seg.extra,seg.s,seg.a,"
                           f"coalesce(seg.a_end,seg.a) FROM seg JOIN src ON src.id=seg.src "
                           f"WHERE src.access='yerel' AND {eligible}", kinds + QUOTE_KINDS_THREE).fetchall()
        # The ref table comes from explicit source citations. It is noisy (indexes and bare references), so a
        # citation is used only when the segment also contains the ayah's entire normalized Arabic text.
        surahs = sorted({s for s, _ in ayat})
        cited = con.execute(f"SELECT ref.s,ref.a,ref.a_end,seg.seg FROM ref JOIN seg ON seg.id=ref.seg_id "
                            f"JOIN src ON src.id=seg.src WHERE ref.s IN ({','.join('?' * len(surahs))}) "
                            f"AND src.access='yerel' AND {eligible}",
                            (*surahs, *kinds, *QUOTE_KINDS_THREE)).fetchall() if surahs else []
        src_kind = {i: k for i, k in con.execute('SELECT id, kind FROM src')}
    keyed = {}                   # locator -> verses reached by its index range and range overlay
    extra = defaultdict(set)
    if OVERLAY.exists():
        for r in rows(OVERLAY):
            extra[r['seg_id']].update((r['s'], x) for x in range(r['indexed_end'] + 1, r['a_end'] + 1))
    for sid, loc, _, _, _, _, _, ss, aa, ae in segs:
        if ss is not None:
            keyed[loc] = {(ss, x) for x in range(aa, ae + 1)} | extra[sid]
    norm = [(loc, sr, kind, head, text, json.loads(metadata or '{}'), ' ' + normalize_map(text)[0] + ' ')
            for _, loc, sr, kind, head, text, metadata, _, _, _ in segs]
    by_loc = {g[0]: g for g in norm}
    citations = defaultdict(set)
    target = set(ayat)
    for s, start, end, loc in cited:
        for a in range(start, end + 1):
            if (s, a) in target and (s, a) not in keyed.get(loc, ()):
                citations[s, a].add(loc)
    out = {}
    def add_hit(g, s, a, route):
        loc, sr, kind, head, body, metadata, _ = g
        if loc in out:
            if f'{s}:{a}' not in out[loc]['scope']:
                out[loc]['scope'].append(f'{s}:{a}')
            return
        key = sorted(keyed.get(loc, ()))
        indexed = (f'; indexed {key[0][0]}:{key[0][1]}'
                   + (f'-{key[-1][1]}' if len(key) > 1 else '')) if key else ''
        out[loc] = {'scope': [f'{s}:{a}'], 'loc': loc, 'src': sr, 'kind': src_kind.get(sr, kind),
                    'verses': f'{s}:{a} ({route}{indexed})', 'head': head or '', 'text': body, 'extra': metadata}
    for s, a in ayat:
        words = quran.get((s, a), [])
        windows = []
        for n in (1, 2, 3):
            for i in range(len(words) - n + 1):
                w = ' '.join(words[i:i + n])
                if grams[w] == {(s, a)} and (n > 1 or len(w) >= 4):
                    windows.append((n, w))
        # Shortest windows first. A longer window is used only when no shorter window inside it was used; a short
        # window too common to mean a quotation is never dropped outright: the longer windows that contain it are
        # tried instead (user, 2026-10-09: nothing dropped). A three-word window has no cap.
        windows.sort(key=lambda x: x[0])
        full = ' ' + ' '.join(words) + ' '
        fallback_eligible = len(words) >= 3 and len(full.strip()) >= 12
        limit = {'ayah': f'{s}:{a}', 'unique_windows': {str(n): sum(k == n for k, _ in windows) for n in (1, 2, 3)},
                 'explicit_ref_candidates': len(citations[s, a]), 'full_verse_fallback_eligible': fallback_eligible,
                 'full_verse_fallback_rule': 'at least 3 normalized Arabic words and 12 normalized characters including spaces',
                 'full_verse_fallback': []}
        QUOTE_LIMITS.append(limit)
        if not windows:
            print(f'NOTE quotes {s}:{a}: no unique 1-3 word window; '
                  + ('only full-verse explicit-citation fallback is available' if fallback_eligible
                     else 'full-verse fallback is ineligible (under 3 normalized words or 12 characters)'))
        elif not any(n == 3 for n, _ in windows):
            fallback_note = ('full-verse explicit-citation fallback only' if fallback_eligible else
                             'full-verse fallback ineligible (under 3 normalized words or 12 characters)')
            print(f'NOTE quotes {s}:{a}: no unique 3-word window for untied hadith, sira or poetry; {fallback_note}')
        print(f"quotes {s}:{a}: {len(windows)} unique window(s): " + ' | '.join(w for _, w in windows))
        used = []
        for n, w in windows:
            covered_by_short = any(m < n and f' {v} ' in f' {w} ' for m, v in used)
            if covered_by_short and n < 3:
                continue
            # A short window covers only QUOTE_KINDS_ONE. Its three-word extension must still search
            # hadith, sira and poetry, which require three words.
            hits = [x for x in norm if f' {w} ' in x[6] and
                    (x[2] in QUOTE_KINDS_THREE if covered_by_short else n >= 3 or x[2] in QUOTE_KINDS_ONE)
                    and (s, a) not in keyed.get(x[0], ())]
            if n < 3 and len(hits) > QUOTE_MAX_HITS:
                print(f"NOTE quotes {s}:{a}: window «{w}» in {len(hits)} segments, too common alone; the longer windows that contain it are used instead")
                continue
            used.append((n, w))
            print(f"quotes {s}:{a}: «{w}» in {len(hits)} segment(s){' (hadith, sīra, poetry only)' if covered_by_short else ''}: "
                  + ', '.join(h[0] for h in hits[:12])
                  + (' …' if len(hits) > 12 else ''))
            for hit in hits:
                add_hit(hit, s, a, 'quoted')
        if fallback_eligible:
            for loc in sorted(citations[s, a]):
                hit = by_loc.get(loc)
                if hit and full in hit[6]:
                    add_hit(hit, s, a, 'explicit citation + full verse')
                    limit['full_verse_fallback'].append(loc)
        if limit['explicit_ref_candidates'] and not limit['full_verse_fallback'] and not windows:
            print(f"NOTE quotes {s}:{a}: {limit['explicit_ref_candidates']} explicit-reference candidate(s) "
                  + ('lacked a verified full-verse match' if fallback_eligible else 'were not searched by the short-verse fallback rule'))
    print(f'quotation packet: {len(out)} segment(s), {sum(len(g["text"]) for g in out.values()):,} characters')
    return list(out.values())


def segment_input(g):
    """Exact segment text delivered in a chunk, including its locator/header overhead."""
    metadata = {k: g.get('extra', {}).get(k) for k in PROVENANCE_KEYS if k in g.get('extra', {})}
    note = ('CORPUS METADATA (provenance/index; not source words or an anchor): '
            + json.dumps(metadata, ensure_ascii=False, sort_keys=True) + '\n') if metadata else ''
    return (f"=== SEGMENT {g['loc']} | source {g['src']} | verses {g['verses']} | {g['head']} ===\n"
            f"{note}{g['text'].strip()}\n\n")


def merge_quote_scope(indexed, quoted):
    """Keep one full input for a locator, including verses reached by both routes."""
    more = [v for v in quoted['scope'] if v not in indexed['scope']]
    if more:
        indexed['scope'] += more
        indexed['verses'] += f" (also quoted: {', '.join(more)})"


def source_fingerprint(head, body, extra):
    """Hash the current passage, heading and provenance delivered to a Tier 1 agent."""
    metadata = {k: extra.get(k) for k in PROVENANCE_KEYS if k in extra}
    value = {'head': head or '', 'text': body or '', 'provenance': metadata}
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def saved_chunk_segments(d, c):
    """Recover exact input bodies and excerpt markers from a complete legacy chunk snapshot, or None."""
    n, count = c['chunk'], c.get('parts', 0)
    if count < 1:
        return None
    pieces = []
    for k in range(count):
        f = d / 'chunks' / f'c{n:02d}.p{k}.txt'
        try:
            raw = f.read_text()
        except OSError:
            return None
        head = f'<<chunk {n} part {k} of 0..{count - 1}>>\n'
        tail = (f'\n<<part {k} ends; continues in part {k + 1}>>\n'
                if k + 1 < count else '\n<<end of chunk>>\n')
        if not raw.startswith(head) or not raw.endswith(tail):
            return None
        pieces.append(raw[len(head):-len(tail)])
    rendered = ''.join(pieces)
    out, cursor = {}, 0
    for i, loc in enumerate(c['locs']):
        marker = f'=== SEGMENT {loc} | source '
        if not rendered.startswith(marker, cursor):
            return None
        end_header = rendered.find(' ===\n', cursor + len(marker))
        if end_header < 0:
            return None
        header = rendered[cursor:end_header]
        start_body = end_header + len(' ===\n')
        next_marker = f"=== SEGMENT {c['locs'][i + 1]} | source " if i + 1 < len(c['locs']) else None
        end_body = rendered.find(next_marker, start_body) if next_marker else len(rendered)
        if end_body < 0 or not rendered[start_body:end_body].endswith('\n\n'):
            return None
        body = rendered[start_body:end_body - 2]
        if body.startswith('CORPUS METADATA ('):
            body = body.split('\n', 1)[1] if '\n' in body else ''
        out[loc] = (body, '[excerpt: characters ' in header)
        cursor = end_body
    return out if cursor == len(rendered) else None


def chunks(segments, chunk_chars=DEFAULT_CHUNK_CHARS):
    """Whole sources packed in kind order by rendered input size; a longer single segment stands alone."""
    by_src = defaultdict(list)
    for g in segments:
        by_src[g['src']].append(g)
    out, cur, size = [], [], 0
    for sr in sorted(by_src, key=lambda s: (by_src[s][0]['kind'], s)):
        n = sum(len(segment_input(g)) for g in by_src[sr])
        if cur and size + n > chunk_chars:
            out.append(cur)
            cur, size = [], 0
        for g in by_src[sr]:
            rendered = len(segment_input(g))
            if cur and size + rendered > chunk_chars:
                out.append(cur)
                cur, size = [], 0
            cur.append(g)
            size += rendered
    if cur:
        out.append(cur)
    return out


def split_original_chunks(segments, original, selected):
    """Keep an existing run's exact segment order, splitting selected chunks once at a segment boundary."""
    by_loc = {g['loc']: g for g in segments}
    old = original['chunks']
    known = {c['chunk'] for c in old}
    unknown = selected - known
    if unknown:
        raise SystemExit(f'unknown chunks to split: {sorted(unknown)}')
    planned = []
    legacy_changed = []
    for c in old:
        try:
            group = [by_loc[loc] for loc in c['locs']]
        except KeyError as e:
            raise SystemExit(f'original segment missing from corpus: {e}') from e
        rendered = [len(segment_input(g)) for g in group]
        if c.get('input_sha256') and hashlib.sha256(''.join(segment_input(g) for g in group).encode()).hexdigest() != c['input_sha256']:
            raise SystemExit(f"original chunk c{c['chunk']:02d} changed in corpus")
        if not c.get('input_sha256') and sum(rendered) != c['chars']:
            legacy_changed.append(c['chunk'])
        if c['chunk'] not in selected:
            planned.append((group, c['chunk'], None))
            continue
        if len(group) < 2:
            raise SystemExit(f"cannot split one-segment chunk c{c['chunk']:02d}")
        half = sum(rendered) / 2
        running = 0
        cuts = []
        for i, size in enumerate(rendered[:-1], 1):
            running += size
            cuts.append((abs(running - half), i))
        cut = min(cuts)[1]
        planned.extend(((group[:cut], c['chunk'], 1), (group[cut:], c['chunk'], 2)))
    if legacy_changed:
        print(f'NOTE {len(legacy_changed)} original chunk(s) predate input hashes and have changed rendered lengths '
              '(new provenance metadata or changed source); review the rebuilt inputs before launch: '
              + ', '.join(f'c{n:02d}' for n in legacy_changed))
    return planned


def source_line(sr, meta, kind):
    bits = [f"{meta.get('title', sr)}", meta.get('author') or '', f"d. {meta['death_ah']} AH" if meta.get('death_ah') else '']
    line = f'{sr}: ' + ', '.join(b for b in bits if b) + f' ({kind})'
    if sr in TRANSLATION_OK:
        line += f'\nTRANSLATION: {TRANSLATION_OK[sr]}'
    return line


def build(a):
    d = run_dir(a.run)
    if d.exists():
        raise SystemExit(f'{d} exists; choose a new run name')
    split_plan = getattr(a, 'split_plan', None)
    if split_plan:
        if a.ayat or a.surahs or a.page or a.skip_done or a.skip_planned:
            raise SystemExit('--split-plan uses the original run\'s ayat and locators; omit other scope and skip options')
        forecast = json.loads(Path(split_plan).read_text())
        original_name = forecast['run']
        original = json.loads((run_dir(original_name) / 'manifest.json').read_text())
        if a.run == original_name:
            raise SystemExit('the split run needs a new run name')
        a.ayat = original['ayat']
        selected = set(forecast['split_chunks'])
    chunk_chars = getattr(a, 'chunk_chars', DEFAULT_CHUNK_CHARS)
    if chunk_chars < 1:
        raise SystemExit('--chunk-chars must be positive')
    if getattr(a, 'surahs', None):
        if a.ayat or a.page:
            raise SystemExit('give one of --ayat, --surahs, or --page with --ayah')
        with connect() as con:
            a.ayat = [f'{s}:{x}' for s, x in con.execute(
                "SELECT s, a FROM seg JOIN src ON src.id=seg.src WHERE src.kind='quran' AND s IN (%s) ORDER BY s, a"
                % ','.join('?' * len(a.surahs)), a.surahs)]
        print(f'surahs {" ".join(map(str, a.surahs))}: {len(a.ayat)} ayat')
    elif bool(a.ayat) == bool(a.page):
        raise SystemExit('give one of --ayat, --surahs, or --page with --ayah')
    if a.page:
        import write  # late import: write imports this module
        a.ayat = write.page_verses(a.page, a.ayah)
        print(f'{a.ayah}: own ayah + {len(a.ayat) - 1} cited verses from {a.page}')
    ayat = [parse_ayah(x) for x in a.ayat]
    src, segments, skipped = gather(ayat)
    skipped += surah_level(ayat)
    if split_plan:
        packet = quote_packet(ayat)
        by_loc = {g['loc']: g for g in segments}
        for g in packet:
            if g['loc'] in by_loc:
                merge_quote_scope(by_loc[g['loc']], g)
            else:
                by_loc[g['loc']] = g
        expected = [loc for c in original['chunks'] for loc in c['locs']]
        if len(expected) != len(set(expected)) or any(loc not in by_loc for loc in expected):
            raise SystemExit('original manifest has duplicate or unavailable locators')
        segments = [by_loc[loc] for loc in expected]
        skipped = original['skipped']
        planned = split_original_chunks(segments, original, selected)
    elif a.skip_done:
        done = {}
        for tag in a.skip_done:
            for f in sorted((V7 / 'work').glob(f'*/out/{tag}/c*.jsonl')):
                if f.parts[-4] in getattr(a, 'skip_done_exclude_run', []):
                    continue
                for loc in valid_output_locs(f):
                    if loc not in excerpts().get(f.parts[-4], set()):
                        done.setdefault(loc, f'{f.parts[-4]}/{tag}')
        for run in getattr(a, 'skip_planned', None) or []:
            pm = json.loads((run_dir(run) / 'manifest.json').read_text())
            print(f'NOTE --skip-planned {run}: reserving every locator in its manifest even if its agents are unfinished; reconcile this run after it completes')
            for c in pm['chunks']:
                for loc in c['locs']:
                    done.setdefault(loc, f'{run} (planned, not finished)')
        cut = {loc for locs in excerpts().values() for loc in locs} - set(done)
        if cut:
            print(f'NOTE {len(cut)} segment locator(s) have excerpt or unverified legacy input provenance; '
                  'any of them in scope is digested from the current full source now')
        kept = []
        for g in segments:
            if g['loc'] in done:
                skipped.append({'ayah': ','.join(g['scope']), 'loc': g['loc'], 'src': g['src'],
                                'reason': f"already digested in {done[g['loc']]}"})
            else:
                kept.append(g)
        segments = kept
    elif a.skip_planned:
        raise SystemExit('--skip-planned requires --skip-done; planned locators cannot be reserved otherwise')
    if getattr(a, 'quotes', False) and not split_plan:
        have = {g['loc']: g for g in segments}
        done_q = done if a.skip_done else {}
        packet = quote_packet(ayat)
        for g in packet:
            if g['loc'] in done_q:
                skipped.append({'ayah': ','.join(g['scope']), 'loc': g['loc'], 'src': g['src'],
                                'reason': f"already digested in {done_q[g['loc']]}"})
            elif g['loc'] in have:        # an indexed segment gathered for one ayah and quoting another of the run
                merge_quote_scope(have[g['loc']], g)
            else:
                segments.append(g)
                have[g['loc']] = g
    with connect() as con:
        verse_text = {f'{s}:{x}': con.execute("SELECT text FROM seg JOIN src ON src.id=seg.src WHERE src.kind='quran' "
                                              'AND s=? AND a=?', (s, x)).fetchone()[0] for s, x in ayat}
    parts_dir = d / 'chunks'
    parts_dir.mkdir(parents=True)
    plan = []
    if not split_plan:
        planned = [(group, None, None) for group in chunks(segments, chunk_chars)]
    for n, (chunk, from_chunk, split_half) in enumerate(planned, 1):
        srcs = list(dict.fromkeys(g['src'] for g in chunk))
        kinds = list(dict.fromkeys(src[s][0] for s in srcs))
        text = ''.join(segment_input(g) for g in chunk)
        parts = [text[i:i + PART_CHARS] for i in range(0, len(text), PART_CHARS)]
        for k, p in enumerate(parts):
            tail = f'\n<<part {k} ends; continues in part {k + 1}>>' if k + 1 < len(parts) else '\n<<end of chunk>>'
            (parts_dir / f'c{n:02d}.p{k}.txt').write_text(f'<<chunk {n} part {k} of 0..{len(parts) - 1}>>\n{p}{tail}\n')
        plan.append({'chunk': n, 'from_chunk': from_chunk, 'split_half': split_half,
                     'sources': srcs, 'kinds': kinds,
                     'scope': list(dict.fromkeys(x for g in chunk for x in g['scope'])),
                     'source_lines': [source_line(s, src[s][2], src[s][0]) for s in srcs],
                     'locs': [g['loc'] for g in chunk], 'chars': len(text), 'parts': len(parts),
                     'input_sha256': hashlib.sha256(text.encode()).hexdigest(),
                     'text_sha256': {g['loc']: hashlib.sha256(g['text'].encode()).hexdigest() for g in chunk},
                     'source_sha256': {g['loc']: source_fingerprint(g['head'], g['text'], g.get('extra', {})) for g in chunk}})
    brief = BRIEF.read_text()
    spawns = []
    for spec in a.models:
        model, effort = spec.split(':')
        tag = tag_of(model, effort)
        for c in plan:
            agent = f'/root/v7d_{a.run}_{tag}_c{c["chunk"]:02d}'
            fill = {'AGENT': agent, 'MODEL': model, 'EFFORT': effort, 'RUN': a.run, 'TAG': tag, 'N': str(c['chunk']),
                    'NN': f'{c["chunk"]:02d}', 'LAST': str(c['parts'] - 1), 'SEGMENTS': str(len(c['locs'])),
                    'NSRC': str(len(c['sources'])), 'SOURCES': '\n'.join(f'- {x}' for x in c['source_lines']),
                    'GUIDES': '\n'.join(f'- **{k}**: {GUIDE[k]}' for k in c['kinds']),
                    'AYAT': '\n'.join(f'- {k}: {verse_text[k]}' for k in c['scope']),
                    'TYPES': '\n'.join(f'- `{k}`: {v}' for k, v in TYPE_GUIDE.items())}
            text = brief
            for k, v in fill.items():
                text = text.replace('{' + k + '}', v)
            f = d / 'spawn' / f'{tag}_c{c["chunk"]:02d}.md'
            f.parent.mkdir(exist_ok=True)
            f.write_text(text)
            spawns.append(str(f.relative_to(ROOT)))
        (d / 'out' / tag).mkdir(parents=True)
    dump(d / 'manifest.json', {'run': a.run, 'ayat': a.ayat, 'models': a.models,
                               'split_plan': split_plan, 'split_from_run': original_name if split_plan else None,
                               'split_chunks': sorted(selected) if split_plan else [],
                               'skip_done_exclude_run': getattr(a, 'skip_done_exclude_run', []),
                               'chunk_chars': chunk_chars, 'row_tags': True, 'strict_fields': True,
                               'excerpt_locs': [],
                               'quotes': bool(getattr(a, 'quotes', False) or split_plan),
                               'quote_limits': QUOTE_LIMITS if (getattr(a, 'quotes', False) or split_plan) else [],
                               'chunks': plan, 'skipped': skipped, 'spawn': spawns})
    total = sum(c['chars'] for c in plan)
    print(f'{len(segments)} segments, {len(plan)} chunks, {total:,} characters, {len(spawns)} spawn files')
    for c in plan:
        print(f"  c{c['chunk']:02d} {len(c['sources']):2d} sources {len(c['locs']):3d} segments {c['chars']:7,} chars: "
              + ' '.join(c['sources']))
    routine = defaultdict(int)
    for s in skipped:
        if '-FULL covers' in s['reason']:
            routine['short edition where the FULL edition covers the verse'] += 1
        elif s['reason'].startswith(('kind meal', 'kind translation', 'kind quran', 'already digested', 'surah-level')):
            routine[s['reason'].split(':')[0].split(' (')[0]] += 1
        else:
            print(f"SKIPPED {s['ayah']} {s['loc']}: {s['reason']}")
    for reason, k in sorted(routine.items()):
        print(f"SKIPPED {k} segment(s): {reason} (each listed in manifest.json)")


def line_problems(loc, x, body, tags=False, strict=False):
    """Problems in one segment's output against the current corpus text."""
    problems = []
    rs = x.get('rows')
    if not isinstance(rs, list):
        return ['"rows" must be a list']
    if not rs and not isinstance(x.get('none'), str):
        problems.append('no rows and no "none" reason')
    elif not rs and not x['none'].strip():
        problems.append('no rows and no "none" reason')
    for j, r in enumerate(rs, 1):
        if not isinstance(r, dict):
            problems.append(f'row {j}: must be an object')
            continue
        missing = [k for k in ('verses', 'speaker', 'stance', 'claim', 'anchor') if not r.get(k)]
        if missing:
            problems.append(f'row {j}: missing {", ".join(missing)}')
        verses = r.get('verses')
        rejected = []
        expanded = verse_list(verses, rejected)
        valid_verses = (isinstance(verses, str) or
                        isinstance(verses, list) and all(isinstance(v, str) for v in verses)) and bool(expanded) and not rejected
        if not valid_verses:
            problems.append(f'row {j}: "verses" must name Quran verses (S:A, ranges or lists)')
        elif strict and any(v not in quran() for v in expanded):
            problems.append(f'row {j}: verse is absent from the Quran index')
        anchor = r.get('anchor')
        if anchor and (not isinstance(anchor, str) or not contains(body, anchor)):
            problems.append(f'row {j}: anchor not found in the current segment: {str(anchor)[:80]}')
        if strict:
            if r.get('stance') not in ('holds', 'prefers', 'reports', 'rejects'):
                problems.append(f'row {j}: stance must be holds, prefers, reports or rejects')
            if not isinstance(r.get('speaker'), str) or not isinstance(r.get('claim'), str):
                problems.append(f'row {j}: speaker and claim must be text')
            elif len(r['claim'].split()) > 40:
                problems.append(f'row {j}: claim exceeds 40 words')
            if isinstance(anchor, str) and not (min(5, len(body.split())) <= len(anchor.split()) <= 25):
                problems.append(f'row {j}: anchor must have 5 to 25 words (or use the whole shorter segment)')
            mentions = r.get('mentions')
            rejected_mentions = []
            mentioned = verse_list(mentions, rejected_mentions)
            if not isinstance(mentions, list) or any(not isinstance(v, str) for v in mentions) or rejected_mentions:
                problems.append(f'row {j}: "mentions" must be a list of Quran verse references')
            elif any(v not in quran() for v in mentioned):
                problems.append(f'row {j}: mentioned verse is absent from the Quran index')
        if tags and valid_verses:
            problems += [f'row {j}: {p}' for p in tag_problems(r)]
    return problems


def valid_output_locs(f):
    """Only finished, structurally valid, current-anchor lines assigned to this run's chunk count as done."""
    if unfinished(f):
        return set()
    d = f.parents[2]
    try:
        man = json.loads((d / 'manifest.json').read_text())
        c = next(x for x in man['chunks'] if f.stem == f"c{x['chunk']:02d}")
        lines = f.read_text().splitlines()
    except (OSError, ValueError, KeyError, StopIteration) as e:
        print(f'WARNING {f.relative_to(V7)}: cannot validate against its manifest ({e}); not counted as done')
        return set()
    expected = set(c['locs'])
    saved = None if c.get('source_sha256') else saved_chunk_segments(d, c)
    if not c.get('source_sha256') and saved is None:
        UNVERIFIED_OUTPUT_LOCS.update(expected)
        if d.name not in _LEGACY_INPUT_WARNED:
            _LEGACY_INPUT_WARNED.add(d.name)
            print(f'NOTE {d.relative_to(V7)}: legacy input snapshots are unavailable or incomplete; '
                  'its output locators remain unresolved and must be rebuilt before counting as complete')
        return set()
    with connect() as con:
        source = {loc: (row[0] or '', row[1] or '', json.loads(row[2] or '{}')) for loc in expected
                  if (row := con.execute('SELECT head,text,extra FROM seg WHERE seg=?', (loc,)).fetchone())}
    valid, duplicate = set(), set()
    for i, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            x = json.loads(line)
        except ValueError:
            print(f'WARNING {f.relative_to(V7)} line {i}: not JSON; not counted as done')
            continue
        if not isinstance(x, dict) or not isinstance(x.get('loc'), str) or x['loc'] not in expected:
            print(f'WARNING {f.relative_to(V7)} line {i}: unknown or malformed locator; not counted as done')
            continue
        loc = x['loc']
        if loc in valid:
            duplicate.add(loc)
        if loc not in source:
            duplicate.add(loc)
            continue
        head, body, extra = source[loc]
        if (loc in man.get('excerpt_locs', []) or
                (c.get('source_sha256') and loc not in c['source_sha256']) or
                (saved is not None and (loc not in saved or saved[loc][1] or saved[loc][0] != body.strip())) or
                (c.get('source_sha256', {}).get(loc) and source_fingerprint(head, body, extra) != c['source_sha256'][loc])):
            duplicate.add(loc)
            print(f'WARNING {f.relative_to(V7)} {loc}: excerpt or source input changed; not counted as done')
            continue
        problems = line_problems(loc, x, body, man.get('row_tags', False), man.get('strict_fields', False))
        if problems:
            duplicate.add(loc)
            print(f'WARNING {f.relative_to(V7)} {loc}: invalid output ({problems[0]}); not counted as done')
        else:
            valid.add(loc)
    return valid - duplicate


def check_chunk(d, tag, c, tags=False, strict=False):
    """Problems in one output file: missing, extra or duplicate segments, bad lines, anchors not verbatim."""
    f = d / 'out' / tag / f"c{c['chunk']:02d}.jsonl"
    if not f.exists():
        return [f'{f.name}: no output file'], 0
    saved = None if c.get('source_sha256') else saved_chunk_segments(d, c)
    if not c.get('source_sha256') and saved is None:
        return [f'{f.name}: legacy input snapshot unavailable; output provenance unresolved, rebuild this chunk'], 0
    with connect() as con:
        source = {loc: (row[0] or '', row[1] or '', json.loads(row[2] or '{}')) for loc in c['locs']
                  if (row := con.execute('SELECT head,text,extra FROM seg WHERE seg=?', (loc,)).fetchone())}
    problems, seen, n_rows = [], [], 0
    for loc in c['locs']:
        if loc not in source:
            problems.append(f'{loc}: missing from current corpus')
            continue
        head, body, extra = source[loc]
        if saved is not None and (loc not in saved or saved[loc][1] or saved[loc][0] != body.strip()):
            problems.append(f'{loc}: excerpt or source text changed since build')
        elif c.get('source_sha256') and loc not in c['source_sha256']:
            problems.append(f'{loc}: missing source provenance hash')
        elif c.get('source_sha256', {}).get(loc) and source_fingerprint(head, body, extra) != c['source_sha256'][loc]:
            problems.append(f'{loc}: source text, heading or provenance changed since build')
    for i, line in enumerate(f.read_text().splitlines(), 1):
        if not line.strip():
            continue
        try:
            x = json.loads(line)
        except ValueError as e:
            problems.append(f'line {i}: not JSON ({e})')
            continue
        loc = x.get('loc') if isinstance(x, dict) else None
        if loc not in c['locs']:
            problems.append(f'line {i}: locator {loc!r} is not in this chunk')
            continue
        seen.append(loc)
        if loc in source:
            problems += [f'{loc}: {p}' for p in line_problems(loc, x, source[loc][1], tags, strict)]
        if isinstance(x.get('rows'), list):
            n_rows += len(x['rows'])
    for loc in c['locs']:
        if loc not in seen:
            problems.append(f'{loc}: segment has no line')
    for loc in {x for x in seen if seen.count(x) > 1}:
        problems.append(f'{loc}: more than one line')
    return problems, n_rows


def check(a):
    d = run_dir(a.run)
    man = json.loads((d / 'manifest.json').read_text())
    tags = [a.model] if a.model else sorted(p.name for p in (d / 'out').iterdir())
    plan = [c for c in man['chunks'] if a.chunk in (None, c['chunk'])]
    if a.chunk is not None:  # the agent's own check: print problems or OK, record nothing
        problems, _ = check_chunk(d, tags[0], plan[0], man.get('row_tags', False), man.get('strict_fields', False))
        print('OK' if not problems else '\n'.join(problems[:60]) + (f'\n... {len(problems) - 60} more' if len(problems) > 60 else ''))
        return
    for tag in tags:
        result = {}
        for c in plan:
            problems, n_rows = check_chunk(d, tag, c, man.get('row_tags', False), man.get('strict_fields', False))
            result[f"c{c['chunk']:02d}"] = {'rows': n_rows, 'problems': problems}
            for p in problems:
                print(f"WARNING {tag} c{c['chunk']:02d}: {p}")
        dump(d / 'out' / tag / 'check.json', result)
        bad = sum(1 for v in result.values() if v['problems'])
        print(f'{tag}: {len(result)} chunks checked, {bad} with problems, {sum(v["rows"] for v in result.values())} rows')


_SESSIONS = None
_SESSION_ROOTS = None


def native_agent_alias(agent):
    """Name used by native spawns, whose task names allow only letters, digits and underscores."""
    parent, name = agent.rsplit('/', 1)
    return parent + '/' + re.sub(r'[^a-z0-9_]', '_', name)


def usage(runs_dir, agent):
    """Usage of one Codex agent: run.json when run_codex.py ran it, else the native session whose agent_path is
    the agent name (agents spawned by a Codex orchestrator). Search both live and archived session transcripts;
    archival preserves the relative path, so a live copy takes precedence. None when neither exists."""
    global _SESSIONS, _SESSION_ROOTS
    r = runs_dir / agent.rsplit('/', 1)[1] / 'run.json'
    if r.exists():
        x = json.loads(r.read_text())
        return {'usd': x.get('usd_equivalent', 0), 'requests': x.get('requests', 0),
                'peak': x.get('max_request_input_tokens') or 0,
                'completed': bool(x.get('turn_completed')) and not x.get('returncode'), 'via': 'run.json'}
    if _SESSIONS is None:
        _SESSIONS = {}
        live_root = Path(os.environ.get('CODEX_SESSIONS_DIR', str(Path.home() / '.codex/sessions')))
        archive_root = Path(os.environ.get('CODEX_SESSIONS_ARCHIVE_DIR', str(ROOT / '.scratch/codex_sessions_archive')))
        roots = [p if p.is_absolute() else ROOT / p for p in (archive_root, live_root)]
        _SESSION_ROOTS = roots
        # Scan live first, then archive. A transcript moved between those scans is still
        # found; its preserved relative path also de-duplicates a copy restored for repair.
        relative_paths = set()
        for base in reversed(roots):
            relative_paths.update(f.relative_to(base) for f in base.glob('*/*/*/*.jsonl'))
        for relative in relative_paths:
            meta = None
            for base in reversed(roots):
                try:
                    with (base / relative).open() as h:
                        meta = json.loads(h.readline()).get('payload', {})
                except (ValueError, OSError):
                    continue
                break
            if meta is None:
                continue
            if meta.get('agent_path'):
                _SESSIONS.setdefault(meta['agent_path'], []).append(relative)
    # Spawn prompts retain their original headers verbatim. Native task names cannot contain
    # the hyphens in those headers, so look for the underscore-only alias as well.
    session_agent = agent if _SESSIONS.get(agent) else native_agent_alias(agent)
    files = _SESSIONS.get(session_agent, [])
    if not files:
        return claude_usage(agent)
    if len(files) > 1:
        print(f'WARNING {agent}: {len(files)} native sessions; costing the latest')
    import account  # enrichment/v5
    relative = sorted(files)[-1]
    rec = None
    # The archive helper may move a completed transcript during this report. Resolve its
    # preserved relative path when costing it, and retry from the other location if moved.
    for base in reversed(_SESSION_ROOTS):
        try:
            rec = account.session(base / relative, session_agent)
        except OSError:
            continue
        if rec is not None:
            break
    if rec is None:
        print(f'WARNING {agent}: native transcript disappeared from live and archive locations')
        return claude_usage(agent)
    return {'usd': rec['usd'], 'requests': rec['requests'], 'peak': rec['max_request_input'],
            'completed': rec['completed'], 'via': 'native session'}


def claude_usage(agent):
    """Usage of a Claude subagent spawned with a spawn file's text: its transcript starts with the header line."""
    sys.path.insert(0, str(ROOT / '_commentary/v16'))
    import agentrun
    key = f'<!-- agent {agent} |'
    hits = []
    for f in agentrun.PROJECTS.glob('*/*/subagents/agent-*.jsonl'):
        try:
            with f.open(encoding='utf-8') as h:
                if key in h.read(20_000):
                    hits.append(f)
        except OSError:
            continue
    if not hits:
        return None
    if len(hits) > 1:
        print(f'WARNING {agent}: {len(hits)} Claude transcripts; costing the latest')
    p = agentrun.parse(sorted(hits, key=lambda f: f.stat().st_mtime)[-1])
    if p['cost_usd'] is None:
        print(f"WARNING {agent}: no rate for {p['model']} in agentrun.RATES; cost counted as 0")
    return {'usd': p['cost_usd'] or 0, 'requests': p['num_messages'], 'peak': p.get('max_context') or 0,
            'completed': p['completed'], 'via': f"Claude transcript ({p['model']})"}


def report(a):
    d = run_dir(a.run)
    man = json.loads((d / 'manifest.json').read_text())
    src_chars = {f"c{c['chunk']:02d}": c['chars'] for c in man['chunks']}
    for tag in sorted(p.name for p in (d / 'out').iterdir()):
        usd = reqs = peak = done = 0
        for c in man['chunks']:
            agent = f"/root/v7d_{a.run}_{tag}_c{c['chunk']:02d}"
            x = usage(d / 'runs', agent)
            if x is None:
                print(f"WARNING {tag} c{c['chunk']:02d}: no run.json and no native session named {agent}")
                continue
            done += 1
            usd += x['usd']
            reqs += x['requests']
            peak = max(peak, x['peak'])
            if not x['completed']:
                print(f"WARNING {tag} c{c['chunk']:02d}: did not complete ({x['via']})")
            if x['peak'] > 120_000:
                print(f"WARNING {tag} c{c['chunk']:02d}: peak request {x['peak']:,} tokens, over the 120k cap")
        out_chars = sum(len(f.read_text()) for f in (d / 'out' / tag).glob('c*.jsonl'))
        chk = d / 'out' / tag / 'check.json'
        rows_n = sum(v['rows'] for v in json.loads(chk.read_text()).values()) if chk.exists() else '?'
        print(f'{tag}: {done}/{len(man["chunks"])} runs, ${usd:.2f} API-equivalent, {reqs} requests, peak {peak:,} tokens, '
              f'{rows_n} rows, digest/source characters {out_chars / max(1, sum(src_chars.values())):.2f}')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('build'); p.add_argument('run'); p.add_argument('--ayat', nargs='+')
    p.add_argument('--surahs', nargs='+', type=int, help='every ayah of these surahs')
    p.add_argument('--page', help="a frozen page: digest its own ayah (--ayah) and every verse it cites")
    p.add_argument('--ayah')
    p.add_argument('--models', nargs='+', required=True)
    p.add_argument('--skip-done', metavar='TAG', nargs='+', help='skip segments already digested by these model tags in any run')
    p.add_argument('--skip-planned', nargs='+', metavar='RUN', help='also skip segments assigned to these built runs (running or not yet run)')
    p.add_argument('--quotes', action='store_true',
                   help='add the quotation packet: segments with no verse key that quote the ayat\'s own words')
    p.add_argument('--skip-done-exclude-run', action='append', default=[], metavar='RUN',
                   help='exclude an active, disjoint run whose output files may be changing')
    p.add_argument('--split-plan', help='forecast JSON: preserve its original run and split only listed chunks')
    p.add_argument('--chunk-chars', type=int, default=DEFAULT_CHUNK_CHARS,
                   help='target rendered input characters per agent chunk (default: %(default)s); a longer single segment stands alone')
    p = sub.add_parser('check'); p.add_argument('run'); p.add_argument('--model'); p.add_argument('--chunk', type=int)
    p = sub.add_parser('report'); p.add_argument('run')
    a = parser.parse_args()
    {'build': build, 'check': check, 'report': report}[a.cmd](a)


if __name__ == '__main__':
    main()
