"""Shared pieces for the root-filter evaluation: QAC roots, page paragraphs and their roots, note-to-root matching.
No model is called. Run from the repository root."""
import json
import re
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'enrichment/v7'))
import write  # noqa: E402  page(): paragraphs and cited verses
from digest import normalize_map  # noqa: E402

INDEX = ROOT / 'enrichment/v8/work/luna-test-95_1/index.sqlite'
QAC = HERE / 'qac.sqlite'
PAGES = {a: ROOT / f"_commentary/v16/out/{a.replace(':', '_')}/DM.r13.images.r13.map3.nohft.tool.tool.tool/"
            f"{a.replace(':', '_')}.reading.tr.md" for a in ('103:1', '1:3', '95:1')}
STOP_FREQ = 500            # roots with this many QAC occurrences or more are "common" (Allah, qāla, kāna, rabb, ...)
AUGMENT = set('اتسمنويهلء')   # ḥurūf al-ziyāda (سألتمونيها) after normalisation, plus hamza
WEAK = set('ويا')
QUOTE = re.compile(r'\{ar:(.*?), tr:.*?source:("[^"]*"|\d+:\d+)\}', re.S)
TAG = re.compile(r'\{source:("[^"]*"|\d+:\d+)\}')
PREFIXES = ('وبال', 'وال', 'فال', 'بال', 'كال', 'لل', 'ال', 'وب', 'ول', 'فب', 'فل', 'وك', 'و', 'ف', 'ب', 'ل', 'ك', 'س')
SUFFIXES = ('هما', 'كما', 'تما', 'هم', 'هن', 'كم', 'كن', 'نا', 'ها', 'ون', 'ين', 'ات', 'وا', 'ه', 'ك', 'ي', 'ت', 'ن')


def norm(s):
    """normalize_map (vowels off, alif/hamza forms unified, dagger alif written) and then alif dropped."""
    return normalize_map(s)[0]


def skel(w):
    return w.replace('ا', '')


def root_key(r):
    """'ع ص ر' / 'عصر' / 'ء ت ي' → normalised 3-4 letter key (hamza kept as ء)."""
    return r.replace(' ', '').replace('أ', 'ء').replace('ا', 'ء') if r else ''


# ---------------------------------------------------------------- QAC
class Qac:
    def __init__(self):
        con = sqlite3.connect(QAC)
        self.words = defaultdict(list)        # 'S:A' -> [(skeleton, core skeleton, {roots})]
        self.forms = defaultdict(set)         # root -> skeletons of its words (whole word, core, lemma)
        self.form_roots = defaultdict(set)    # skeleton -> roots (for non-Qurʾān Arabic in a paragraph)
        self.freq = defaultdict(int)
        self.verses_of = defaultdict(set)     # root -> verses where it occurs
        rows = con.execute('SELECT surah, ayah, word_index, morpheme_role, surface_ar, lemma_ar, root_join_key '
                           'FROM qac_morphemes ORDER BY surah, ayah, word_index, morpheme_index')
        cur, buf = None, []
        for s, a, w, role, surf, lem, rk in list(rows) + [(None,) * 7]:
            if (s, a, w) != cur and buf:
                v = f'{cur[0]}:{cur[1]}'
                whole = skel(norm(''.join(b[1] for b in buf)).replace(' ', ''))
                core = skel(norm(''.join(b[1] for b in buf if b[0] != 'PREFIX')).replace(' ', ''))
                roots = {b[3] for b in buf if b[3]}
                self.words[v].append((whole, core, roots))
                for r in roots:
                    self.verses_of[r].add(v)
                    for f in (whole, core) + tuple(skel(norm(b[2]).replace(' ', '')) for b in buf if b[3] == r):
                        if len(f) >= 3:
                            self.forms[r].add(f)
                            self.form_roots[f].add(r)
                buf = []
            if s is None:
                break
            cur = (s, a, w)
            buf.append((role, surf, lem, root_key(rk)))
            if rk:
                self.freq[root_key(rk)] += 1

    def verse_roots(self, v):
        return set().union(*(r for _, _, r in self.words.get(v, []))) if self.words.get(v) else set()


def variants(tok):
    """Token skeleton plus the skeletons left after stripping one clitic prefix and/or one suffix."""
    out = {tok}
    for p in PREFIXES:
        if tok.startswith(p) and len(tok) - len(p) >= 3:
            out.add(tok[len(p):])
    for t in list(out):
        for x in SUFFIXES:
            if t.endswith(x) and len(t) - len(x) >= 3:
                out.add(t[:-len(x)])
    return {skel(t) for t in out if len(skel(t)) >= 3}


def pattern_match(word, root, translit=False):
    """Root letters in order inside the word; every other letter an augment letter; weak letters and hamza may be
    absent or written as alif/wāw/yāʾ; a doubled last radical may be written once."""
    letters = list(root)
    if len(letters) == 3 and letters[1] == letters[2]:
        alts = [letters, letters[:2]]
    else:
        alts = [letters]
    for L in alts:
        strong = sum(1 for c in L if c not in WEAK and c != 'ء')
        if strong < 2 or len(word) > len(L) + 5:
            continue
        if _pm(word, 0, L, 0, 0, translit):
            return True
    return False


def _pm(w, i, L, j, extra, tr=False):
    if j == len(L):
        return all(c in AUGMENT for c in w[i:]) and extra + len(w) - i <= 5
    c = L[j]
    ok = {c}
    if c == 'ء' or c in WEAK:
        ok = {'ا', 'و', 'ي', 'ء'} | ({'ع'} if tr else set())   # a transliteration may write hamza as '
        if _pm(w, i, L, j + 1, extra, tr):          # weak radical or hamza not written
            return True
    for k in range(i, len(w)):
        if w[k] in ok and _pm(w, k + 1, L, j + 1, extra + (k - i), tr):
            return True
        if w[k] not in AUGMENT:
            return False
    return False


# ---------------------------------------------------------------- transliterations in English claims
TR_MARK = re.compile(r"[āīūʿʾḥṣḍṭẓʿ‘’`']")
DIGRAPH = [('kh', 'خ'), ('gh', 'غ'), ('sh', 'ش'), ('th', 'ث'), ('dh', 'ذ')]
SINGLE = {'ʿ': 'ع', '‘': 'ع', '`': 'ع', "'": 'ع', '’': 'ع', 'ʾ': 'ء', 'ḥ': 'ح', 'h': 'ه', 'ṣ': 'ص', 's': 'س', 'ḍ': 'ض',
          'd': 'د', 'ṭ': 'ط', 't': 'ت', 'ẓ': 'ظ', 'z': 'ز', 'q': 'ق', 'k': 'ك', 'j': 'ج', 'b': 'ب', 'f': 'ف', 'l': 'ل',
          'm': 'م', 'n': 'ن', 'r': 'ر', 'w': 'و', 'y': 'ي', 'ā': 'ا', 'ī': 'ي', 'ū': 'و', 'g': 'ج', 'x': 'خ'}


FOLD = str.maketrans({'ص': 'س', 'ط': 'ت', 'ض': 'د', 'ح': 'ه', 'ظ': 'ز', 'ذ': 'ز', 'ث': 'س'})


def fold(s):
    """Transliterations in claims are not always dotted (ya'sirun for yaʿṣirūn): compare emphatics folded."""
    return s.translate(FOLD)


def translit_tokens(claim):
    """Arabic consonant skeletons of the transliterated words in an English claim (only words with a
    transliteration mark: macron, dot below, ʿ or ʾ or an apostrophe inside the word)."""
    out = []
    for t in re.findall(r"[A-Za-zāīūʿʾḥṣḍṭẓĀĪŪḤṢḌṬẒ‘’`'-]+", claim or ''):
        t = t.lower().strip("'’‘-")
        if not TR_MARK.search(t) or re.search(r"['’]s$", t):
            continue
        t = re.sub(r'^(a[lnrstdz]-|wa-|bi-|li-|fa-)', '', t)
        for a, b in DIGRAPH:
            t = t.replace(a, b)
        s = ''.join(SINGLE.get(ch, '') for ch in t)
        s = re.sub(r'(.)\1', r'\1', s).replace('ا', '')
        if len(s) >= 3:
            out.append(s)
    return out


# ---------------------------------------------------------------- page paragraphs and their roots
def paragraphs(ayah, qac, dict_words=False):
    """{p: dict(text, cites, roots, quotes, src)}. roots: QAC roots of the words of every Qurʾān quotation (matched
    against the quoted verse's QAC words), the root of every dictionary tag; with dict_words also the QAC roots of
    the other Arabic words inside dictionary quotations (looked up by form over the whole Qurʾān)."""
    text, paras, _, cites = write.page(str(PAGES[ayah]), ayah)
    out = {}
    for p, (lo, hi) in paras.items():
        t = text[lo:hi]
        roots, why, unmatched = set(), defaultdict(set), []
        for m in QUOTE.finditer(t):
            ar, src = m[1], m[2].strip('"')
            if re.fullmatch(r'\d+:\d+', src):
                vw = qac.words.get(src, [])
                for tok in norm(ar).split():
                    k = skel(tok)
                    hit = [r for w, c, r in vw if k == w or k == c or (len(k) >= 3 and (k in w or w in k) and len(w) >= 3)]
                    if hit:
                        for rs in hit[:1]:
                            for r in rs:
                                roots.add(r)
                                why[r].add(src)
                    elif len(k) >= 3:
                        unmatched.append((src, tok))
            else:
                r = root_key(src.split(',')[0])
                roots.add(r)
                why[r].add('dict')
                if dict_words:
                    for tok in norm(ar).split():
                        for v in variants(tok):
                            for r2 in qac.form_roots.get(v, ()):
                                roots.add(r2)
                                why[r2].add('dict-word')
        for m in TAG.finditer(t):
            src = m[1].strip('"')
            if not re.fullmatch(r'\d+:\d+', src):
                r = root_key(src.split(',')[0])
                roots.add(r)
                why[r].add('dict')
        out[p] = {'text': t, 'cites': cites[p], 'roots': roots, 'why': dict(why), 'unmatched': unmatched}
    return out


# ---------------------------------------------------------------- notes
def notes_on(verses):
    con = sqlite3.connect(INDEX)
    con.row_factory = sqlite3.Row
    q = ','.join('?' * len(verses))
    rows = {}
    for r in con.execute(f'SELECT * FROM notes WHERE verse IN ({q})', list(verses)):
        d = rows.setdefault(r['id'], dict(r) | {'verses': set()})
        d['verses'].add(r['verse'])
    return rows


def all_verses_of(ids):
    con = sqlite3.connect(INDEX)
    out = defaultdict(set)
    for i in ids:
        for (v,) in con.execute('SELECT verse FROM notes WHERE id=?', (i,)):
            out[i].add(v)
    return out


def line(r):
    who = r['src'] + (f" d.{r['death']}" if r['death'] else '')
    sp = '' if r['speaker'] == 'author' else f" · {r['speaker']}"
    return f"[{r['id']}] {who}{sp} · {r['stance']} · {r['claim']} «{r['anchor']}»"


ARABIC_CH = re.compile(r'[؀-ۿ]')


def tokens_est(s):
    """Token estimate: Arabic letters at 2.0 chars/token, everything else at 4.0 chars/token."""
    a = len(ARABIC_CH.findall(s))
    return a / 2.0 + (len(s) - a) / 4.0


class NoteRoots:
    """Per note: the roots it carries, by three detectors.
    lex:  an Arabic token of the anchor or claim (after clitic stripping) equals a QAC form of the root;
    pat:  an Arabic token fits the root's letters with only augment letters around them (catches non-Qurʾānic
          derivatives such as عصارة, اعتصار, معصر);
    tr:   a transliterated word of the English claim fits the root's letters (yaʿṣirūn, ʿaṣr).
    tag:  simulated retag: the words of the note's own verse(s) that the note names (Arabic or transliterated),
          and their QAC roots; notes naming none are 'untagged' (they would get '*' or a word only a model finds)."""

    def __init__(self, qac):
        self.qac = qac

    def arabic_tokens(self, r):
        toks = norm((r['an'] or '') + ' ' + (r['cn'] or '')).split()
        return toks

    def match(self, r, roots, how):
        toks = self.arabic_tokens(r)
        hit = set()
        if 'lex' in how or 'pat' in how:
            for t in toks:
                vs = variants(t)
                for root in roots:
                    if root in hit:
                        continue
                    if 'lex' in how and vs & self.qac.forms.get(root, set()):
                        hit.add(root)
                    elif 'pat' in how and any(pattern_match(v, root) for v in vs | {skel(t)} if len(v) >= 3):
                        hit.add(root)
        if 'tr' in how:
            for s in translit_tokens(r['claim']):
                for root in roots:
                    if root not in hit and pattern_match(fold(s), fold(root), True):
                        hit.add(root)
        return hit

    def tag(self, r, verses, common=frozenset()):
        """Simulated verse-word tag: verse words named in the note: the word itself (anchor/claim Arabic), another
        Qurʾānic form of its root unless the root is common (عصره for يعصرون), or a transliteration in the claim."""
        toks = [v for t in self.arabic_tokens(r) for v in variants(t) | {skel(t)}]
        tset = set(toks)
        tr = translit_tokens(r['claim'])
        words, roots = [], set()
        for v in verses:
            for w, c, rs in self.qac.words.get(v, []):
                if not rs:
                    continue
                named = (w in tset or c in tset or any(len(c) >= 3 and (c in t) and len(t) <= len(c) + 3 for t in tset)
                         or any(rr not in common and tset & self.qac.forms.get(rr, set()) for rr in rs))
                if not named and tr:
                    named = any(any(pattern_match(fold(s), fold(rr), True) for rr in rs)
                                and len(s) <= len(c) + 3 for s in tr)
                if named:
                    words.append((v, c))
                    roots |= rs
        return words, roots
