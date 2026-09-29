"""Form-aware construction detector (E0). VERIFICATION ONLY: its calls go to verification records and to the user's
audit sheet, never into any brief, supply or prompt a model reads (user rule: script construction verdicts are
unreliable and must never reach a model).

For every Quranic occurrence of a root that has collocation or non_bare branches, and for each such branch, it says
present / absent / unknown, from:
  * the branch's own dictionary evidence: its lexical units (dictionary furuq_v4 expression_ar), its early-source
    phrases (source_phrase_ar) and its what_is_ar; from each construction statement it reads the head word (the word
    carrying the root: verb form / measure, voice), the preposition after it, content partners, wildcard slots
    (فلان, الشيء, كذا, pronoun suffixes);
  * the occurrence's QAC morphology (measure, voice, pos, lemma) and its grammar attachments (governed prepositions,
    direct objects, iḍāfa, subject, pronoun antecedents), joined through the reviewed QAC bridge.
User rule built in: a derived verb form counts as the construction when the dictionary names that form in bare use
(the form alone, e.g. a masdar or verb of that measure with no partner); a context alone never does, and a bare
Form I statement never licenses (it would make every plain use collocation-bound).

Match levels per construction (the best one is the branch's level at the occurrence):
  3.0 partner      every content partner found among grammatically linked words (or a pronoun's antecedent),
                   with the stated preposition when the statement has one
  2.9 partner-def  same, but the linked word's own dictionary definition (image / what_is) contains the partner
                   word (e.g. a named place whose definition says it is a kind of the partner)
  2.5 partner-win  every content partner found within 4 words, not grammatically linked
  2.0 prep / object  no content partner in the statement; its preposition is governed by the occurrence, and/or its
                   wildcard object slot is filled (direct object, iḍāfa dependent, or passive voice)
  1.0 form         the statement names a derived form in bare use and the occurrence is that form, with no direct
                   object and no preposition that another branch's construction claims
Decision: present if level >= 3 (or >= 2.5 for partner-win); for levels 1-2 present unless another branch of the
same root reaches a strictly higher level with a partner (then absent: the occurrence carries that construction) or
the same level (then unknown: the construction does not discriminate). Level 0: absent when the branch has a
checkable construction and the occurrence has grammar data; unknown otherwise.
"""
import re, sys, collections, functools, json, os
sys.dont_write_bytecode = True
import gdata as G

AR = re.compile(r'[ء-ي]+')
SRC_TAG = re.compile(r'\([^)]*\)')

GLOSS = {'اي', 'اذا', 'اذ', 'وهو', 'وهي', 'هو', 'هي', 'بمعني', 'معناه', 'يعني', 'كانه', 'كانها', 'اراد', 'يريد',
         'تشبيها', 'نقيض', 'ومنه', 'اصله', 'لانه', 'لانها', 'فهو', 'فهي', 'يكون', 'تكون', 'وذلك', 'ذلك', 'وكذلك',
         'ويقال', 'يقال', 'قيل', 'وقيل', 'اصل', 'مثل', 'نحو', 'كما', 'فقد', 'قد', 'ثم', 'حتي', 'اذن', 'ان', 'انه',
         'انها', 'لان', 'وانشد', 'انشد', 'قال', 'وقال', 'قالوا', 'ليس', 'غير', 'الا', 'اما', 'واما', 'سمي', 'يسمي',
         'استعير', 'مصدر', 'اسم', 'جمع', 'وجمعه', 'والجمع', 'الجمع', 'واحده', 'الواحد', 'الواحده', 'يدل', 'تدل',
         'بمنزله', 'كقولك', 'كقولهم', 'يجري', 'مجري', 'مجاز', 'مجازا', 'التي', 'الذي', 'الذين', 'اللذان',
         'اللتان', 'اللاتي', 'اللواتي'}
LEAD = {'يقال', 'ويقال', 'تقول', 'قولهم', 'وقولهم', 'قولك', 'ومنه', 'منه', 'يدخل', 'فيه', 'قد', 'وقد', 'كل', 'من',
        'انه', 'انها', 'لفي', 'سمعت', 'لقيته', 'تركته', 'والمعني', 'ايضا', 'اذا', 'اردت', 'قلت', 'فاذا', 'الامر',
        'العظيم', 'فقد', 'ان', 'في'}
SUBJ_WILD = {'فلان', 'الرجل', 'رجل', 'القوم', 'قوم', 'الانسان', 'المرء', 'احد', 'زيد', 'عمرو', 'الكافر', 'فلانه',
             'المراه', 'الناس'}
OBJ_WILD = {'فلانا', 'الشي', 'شي', 'شييا', 'شيا', 'كذا', 'وكذا', 'بكذا', 'زيدا', 'عمرا', 'الامر', 'امرا', 'امر',
            'احدا', 'غيره', 'غيرك', 'صاحبه'}
FUNC = {'في', 'من', 'علي', 'عن', 'الي', 'ب', 'ل', 'ك', 'مع', 'عند', 'بين', 'لدي', 'دون', 'ما', 'لا', 'لم', 'لن', 'و',
        'ف', 'او', 'ام', 'بل', 'هل', 'قد', 'الذي', 'التي', 'الذين', 'هذا', 'هذه', 'ذلك', 'تلك', 'كل', 'بعض', 'ولا',
        'وما', 'فلا', 'لما', 'مما', 'عما', 'بما', 'فيما', 'انما', 'كان', 'كانت', 'يكون', 'صار', 'هم', 'هن', 'انا',
        'نحن', 'انت', 'له', 'لها', 'لهم', 'لك', 'لي', 'لنا', 'عليه', 'عليها', 'عليهم', 'عليك', 'علي', 'علينا', 'به',
        'بها', 'بهم', 'بك', 'بي', 'منه', 'منها', 'منهم', 'فيه', 'فيها', 'فيهم', 'عنه', 'عنها', 'عنهم', 'عنك', 'اليه',
        'اليها', 'اليهم', 'اليك', 'الي', 'والي', 'وفي', 'وعلي', 'وعن', 'ومن', 'وب', 'وبه'}
PREP_WORDS = {'في': 'في', 'علي': 'علي', 'عن': 'عن', 'الي': 'الي', 'من': 'من', 'مع': 'مع', 'بين': 'بين',
              'عند': 'عند', 'دون': 'دون', 'لدي': 'لدي', 'حتي': 'حتي'}
PRON_SUFF = ('هما', 'كما', 'هم', 'هن', 'كم', 'كن', 'نا', 'ها', 'ه', 'ك', 'ني', 'ي')
GEN_ROOTS = {'ء ل ه', 'ش ي ء', 'ق و ل', 'ك و ن', 'ف ل ن', 'ء م ر', 'ر ج ل', 'غ ي ر', 'ك ل ل', 'ب ع ض', 'ء ح د',
             'ن و س', 'ق و م'}
MEASURES = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII')


def mnorm(m):
    return m if m else 'I'


# --------------------------------------------------------------------------------------------- lexical helpers
def qnorm(s):
    """normalise a QAC (Uthmani) form toward standard spelling: the dagger alif is written as alif (ٰ over
    alif maqsura dropped), then the loose folding."""
    s = (s or '').replace('\u0649\u0670', '\u0649').replace('\u0670', '\u0627')
    return G.norm(s)


def qkey(t):
    return t


def skel(t):
    """devowelled skeleton for orthography-tolerant matching (Uthmani صلوة / standard صلاة)."""
    if len(t) <= 2:
        return t
    return t[0] + ''.join(ch for ch in t[1:] if ch not in 'اوي')


@functools.lru_cache(None)
def surface_lex():
    """(exact lexicon, skeleton lexicon): clitic-stripped Quranic form -> Counter(root)."""
    lex = collections.defaultdict(collections.Counter)
    sk = collections.defaultdict(collections.Counter)
    for d in G.words().values():
        if not d['root']:
            continue
        for f in (d['stem'], d['lemma'], d['surface']):
            for v in variants(qnorm(f)):
                lex[v][d['root']] += 1
                if len(v) >= 3:
                    sk[skel(v)][d['root']] += 1
    return lex, sk


def variants(t):
    """clitic-stripped variants of a normalised token (longest first): conjunction, then a preposition / lam /
    future sin, then the article; then pronoun and inflection suffixes."""
    out = [t]
    for c1 in ('', 'و', 'ف'):
        if not t.startswith(c1):
            continue
        a = t[len(c1):]
        for c2 in ('', 'ب', 'ل', 'ك', 'س'):
            if not a.startswith(c2):
                continue
            b_ = a[len(c2):]
            for c3 in ('', 'ال', 'ل'):
                if not b_.startswith(c3):
                    continue
                x = b_[len(c3):]
                if len(x) >= 2 and x != t:
                    out.append(x)
    for x in list(out):
        for q in PRON_SUFF + ('ات', 'ون', 'ين', 'ان', 'وا', 'تم', 'ت', 'ه', 'ا'):
            if x.endswith(q) and len(x) - len(q) >= 2:
                out.append(x[:-len(q)])
    seen, res = set(), []
    for x in out:
        if x not in seen:
            seen.add(x); res.append(x)
    return res


def _pick(c, exclude):
    tot = sum(c.values())
    rs = {r for r, n in c.items() if n >= 0.25 * tot}
    if exclude:
        rs.discard(exclude)
    return rs


def tok_roots(t, exclude=None):
    lex, sk = surface_lex()
    for v in variants(t):
        if v in lex and len(v) >= 2:
            return _pick(lex[v], exclude)
    for v in variants(t):
        if len(v) >= 3 and skel(v) in sk and len(skel(v)) >= 3:
            return _pick(sk[skel(v)], exclude)
    return set()


def exact_known(u):
    """the token itself (only pronoun suffixes stripped, no proclitic) is a Quranic form"""
    lex, _ = surface_lex()
    if u in lex:
        return True
    return any(u.endswith(q) and u[:-len(q)] in lex for q in PRON_SUFF if len(u) - len(q) >= 3)


def radicals(root):
    return root.split()


def carries_root(t, root):
    """token carries the root: the strong radicals appear in order, compactly (weak radicals may change/drop)."""
    rad = radicals(root)
    strong = []
    for c in rad:
        if c not in 'اويء' and (not strong or strong[-1] != c):
            strong.append(c)                 # geminate roots (ر د د) are written with one letter + shadda
    if len(strong) < 1:
        strong = rad
    if len(strong) == 1:
        # hollow/defective roots with one strong radical: require QAC lexicon evidence
        return root in tok_roots(t)
    s = t
    pos, first, last = 0, -1, -1
    for c in strong:
        j = s.find(c, pos)
        if j < 0:
            return False
        if first < 0:
            first = j
        if last >= 0 and j - last > 3:
            return False
        last = j; pos = j + 1
    if last - first > len(rad) + 2:
        return False
    rs = tok_roots(t)
    if not rs or root in rs:
        return True
    sk = lambda r: [c for c in r.split() if c not in 'اويء']
    return any(sk(r) == sk(root) for r in rs)     # ص ل و / ص ل ي: same strong radicals, weak radical differs


def hnorm(s, qac=False):
    """like the loose folding but keeps an initial hamza on alif (أفعل = Form IV vs ٱفتعل / اطّلع = Form VIII)."""
    s = (s or '')
    if qac:
        s = s.replace('\u0649\u0670', '\u0649').replace('\u0670', '\u0627')
    s = G.DIAC.sub('', s)
    lead = ''
    m = re.match(r'^([وف]?)(آ|ءا|أا)', s)
    if m:
        return m.group(1) + 'آ' + G.norm(s[m.end():])
    m = re.match(r'^([وف]?)([أإ])', s)
    if m:
        lead = m.group(1) + 'أ'
        s = s[m.end():]
    return lead + G.norm(s)


@functools.lru_cache(None)
def root_forms_h():
    """root -> {hamza-preserving skeleton: set((pos, measure, voice))}."""
    out = collections.defaultdict(lambda: collections.defaultdict(set))
    for d in G.words().values():
        if not d['root']:
            continue
        vo = 'PASS' if 'PASS' in d['feats'].split('|') else 'ACT'
        m = mnorm(d['measure'])
        for f in (d['stem'], d['lemma']):
            k = hnorm(f, qac=True)
            if k.startswith('ال') and len(k) > 4:
                k = k[2:]
            out[d['root']][k].add((d['pos'], m, vo if f == d['stem'] else '*'))
    return {r: dict(v) for r, v in out.items()}


@functools.lru_cache(None)
def root_forms():
    """root -> {normalised skeleton: set((pos, measure, voice))} from QAC stems and lemmas of that root."""
    out = collections.defaultdict(lambda: collections.defaultdict(set))
    for d in G.words().values():
        if not d['root']:
            continue
        vo = 'PASS' if 'PASS' in d['feats'].split('|') else 'ACT'
        m = mnorm(d['measure'])
        for f in (d['stem'], d['lemma']):
            k = qnorm(f)
            if k.startswith('ال') and len(k) > 4:
                k = k[2:]
            out[d['root']][k].add((d['pos'], m, vo if f == d['stem'] else '*'))
    return {r: dict(v) for r, v in out.items()}


def pattern_measures(t, root):
    """Fallback measure guess for a head token not attested in QAC (unvocalised), as a set; empty = unknown."""
    rad = radicals(root)
    r1 = rad[0] if rad else ''
    for p in ('وال', 'فال', 'بال', 'ال', 'و', 'ف'):
        if t.startswith(p) and len(t) - len(p) >= 3:
            t = t[len(p):]
            break
    if t.startswith('است') or t.startswith('يست') or t.startswith('تست') or t.startswith('مست') or t.startswith('نست'):
        return {'X', 'VIII'} if r1 == 'س' else {'X'}
    for pre in ('', 'ي', 'ت', 'ن', 'م'):
        if pre and not t.startswith(pre):
            continue
        u = t[len(pre):]
        if u.startswith('ان' + r1) or (pre and u.startswith('ن' + r1) and len(u) >= 4 and pre != 'م'):
            return {'VII'}
    # form VIII: (a/ya/ta/mu)-r1-t-, with assimilation after emphatics / dentals / weak first radical
    viii = {r1 + 'ت'}
    if r1 in 'صضطظ':
        viii.add(r1 + 'ط')
    if r1 in 'دذز':
        viii.add(r1 + 'د')
    if r1 in 'وي':
        viii.add('ت')
    if r1 == 'ط':
        viii.add('ط')
    for pre in ('ا', 'ي', 'ت', 'ن', 'م'):
        if t.startswith(pre) and any(t[1:].startswith(v) for v in viii) and len(t) >= 4:
            return {'VIII'}
    if t.startswith('ت') and len(t) >= 4:
        if t[1] == r1 and len(t) > 2 and t[2] == 'ا':
            return {'VI'}
        if t[1] == r1 or (r1 in 'اوي' and len(t) >= 4):
            if t.endswith('ه') or (len(t) >= 5 and t[-2] == 'ي'):
                return {'II', 'V'}
            return {'V'}
    if t.startswith('مت'):
        return {'V', 'VI'}
    if t.startswith('ا') and len(t) >= 4:
        return {'IV'}
    if t.startswith('م') and len(t) >= 4:
        return {'I', 'II', 'III', 'IV'}
    if len(t) >= 2 and len(t) > 3 and t[1] == 'ا':
        return {'III', 'I'}
    return {'I', 'II'}


def plain_skeleton_measures(t, root):
    """An unvocalised head written with the bare radicals (perfect) or imperfect prefix + radicals cannot show a
    shadda or the IV prefix vowel: فعل = I or II; يفعل = I, II or IV. Returns that set, or None."""
    rad = radicals(root)
    radstr = ''.join(rad)
    strong = ''.join(c for c in rad if c not in 'اويء')
    if len(strong) < 2:
        return None

    nweak = sum(1 for c in rad if c in 'اويء')

    def is_plain(x):
        w = ''.join(ch for ch in x if ch not in 'اوي')
        removed = len(x) - len(w)
        return x == radstr or (w == strong and removed <= nweak)

    for v in variants(t):
        if v[:1] in 'يتن' and v[:1] != rad[0] and len(v) >= 4 and is_plain(v[1:]):
            return {'I', 'II', 'IV'}
        if v[:1] not in 'يتنا' or v[:1] == rad[0]:
            if is_plain(v):
                return {'I', 'II'}
    return None


def verb_like(raw, t, root):
    """the head is (probably) a verb: QAC attests the skeleton as a verb, or it carries an imperfect prefix /
    perfect subject suffix. Used to read a pronoun suffix as an object (verb) or a possessive (noun)."""
    rf = root_forms().get(root, {})
    for v in variants(t):
        if v in rf:
            if any(pos == 'V' for pos, _, _ in rf[v]):
                return True
            if all(pos != 'V' for pos, _, _ in rf[v]):
                return False
    core = t.lstrip('وف')
    if core.startswith('ال'):
        return False
    if core[:1] in 'يتن' and len(core) >= 4:
        return True
    return any(core.endswith(s) for s in ('ته', 'تها', 'تهم', 'تني', 'تك', 'وه', 'وها', 'وهم'))


def head_forms(raw, t, root):
    """(measures set, voice) of a head token. Empty measures = unknown."""
    ms, vo = _head_forms(raw, t, root)
    amb = plain_skeleton_measures(t, root)
    bare_raw = G.DIAC.sub('', raw or '')
    if amb and 'IV' in amb and bare_raw.endswith('ى') and radicals(root)[-1:] in (['ي'], ['و']):
        amb = None                                   # final alif maqsura: a perfect, not an imperfect (تولى)
    if amb and not hnorm(raw).lstrip('وف').startswith(('أ', 'آ')) and set(ms) <= {'I', 'II', 'IV'}:
        ms = set(ms) | amb
    return ms, vo


def _head_forms(raw, t, root):
    th = hnorm(raw)
    if th.startswith('أ') or th[1:2] == 'أ' or th.lstrip('وف').startswith('آ'):
        rfh = root_forms_h().get(root, {})
        hv = [th] + [v for v in variants(th) if v != th]
        if th.startswith('ال') or (raw or '').rstrip('\u064b\u064c\u064d\u064e\u064f\u0650\u0651\u0652').endswith('ة'):
            hv = [th[2:] if th.startswith('ال') else th]
        madda = th.lstrip('وف').startswith('آ') and radicals(root)[:1] == ['ء']
        for v in hv:
            if v in rfh and len(v) >= 2:
                ms = {m for (_, m, _) in rfh[v]}
                if madda:
                    ms |= {'III', 'IV'}              # آفعل: also the III / IV verb (آخذه, آتاه)
                vs = {vo for (_, _, vo) in rfh[v] if vo != '*'}
                return ms, ('PASS' if vs == {'PASS'} else ('ACT' if vs == {'ACT'} else ''))
        core = th.lstrip('وف')
        if core.startswith('آ') and radicals(root)[:1] == ['ء']:
            return {'III', 'IV'}, ''                    # آفعل of a hamza-initial root: III (آخذ) or IV (آمن)
        if core.startswith('أ') and len(core) >= 4 and not core.startswith('أست'):
            voice = 'PASS' if 'ُ' in (raw or '')[:3] else ''
            return {'IV'}, voice
    rf = root_forms().get(root, {})
    vs_ = variants(t)
    if t.startswith('ال') or (raw or '').rstrip('\u064b\u064c\u064d\u064e\u064f\u0650\u0651\u0652').endswith('ة'):
        base = t[2:] if t.startswith('ال') else t
        vs_ = [base]
    for v in vs_:
        if v in rf and len(v) >= 2:
            ms = {m for (_, m, _) in rf[v]}
            vs = {vo for (_, _, vo) in rf[v] if vo != '*'}
            voice = 'PASS' if vs == {'PASS'} else ('ACT' if vs == {'ACT'} else '')
            return ms, voice
    ms = pattern_measures(t, root)
    voice = ''
    if raw and len(raw) > 1 and ('ُ' in raw[:3]):     # vocalised with a damma on the first letter(s): passive
        voice = 'PASS'
    return ms, voice


# ------------------------------------------------------------------------------------ construction statements
def statements(b):
    """The branch's construction statements: (origin, text). Lexical units first, then phrases, then what_is."""
    out = []
    for u in G.lexunits().get((b['root_id'], b['bid']), []):
        if u['kind'] in ('collocation', 'lexical_unit', 'form', 'review') and u['expr']:
            out.append(('lu:' + u['kind'], u['expr']))
    for seg in re.split('[؛;]', b['phrase'] or ''):
        seg = SRC_TAG.sub(' ', seg).strip()
        if seg:
            out.append(('phrase', seg))
    w = b['what'] or ''
    w = re.sub(r'^\s*(يدخل فيه|ويدخل فيه)\s*', '', w)
    for seg in re.split('[،,؛;:]| و(?=[ء-ي]{3,} )', w):
        seg = seg.strip()
        if seg:
            out.append(('what', seg))
    return out


def parse_statement(origin, text, root):
    """-> list of constructions dict(head, measures, voice, preps (set), alts [(prep, roots, stem)] = alternative
       fillers of the one content slot, obj_wild, subj_wild, bare, origin, text).
       Reading of a statement: the head word (carries the root), then up to 5 tokens until a gloss marker; a
       preposition right after the head or before the slot filler is the construction's preposition; the first
       content word is the partner, and و/أو-coordinated content words are alternative partners; a wildcard
       (فلان, الشيء, كذا, a pronoun) fills a slot without naming a partner and, after a preposition, closes the
       statement (what follows is the lexicographer's gloss)."""
    raw_toks = re.findall(r'[\u0621-\u064a\u064b-\u0652\u0670]+', text)
    toks = [G.norm(x) for x in raw_toks]
    first_gloss = next((i for i, t in enumerate(toks) if i > 0 and (t in GLOSS or (t[:1] in 'وف' and t[1:] in GLOSS
                                                                         and len(t) > 3))), len(toks))
    heads = [i for i, t in enumerate(toks) if t and i < first_gloss and carries_root(t, root)]
    clean = origin.startswith('lu')          # lexical units are bare construction statements, no gloss
    cons = []
    last_h = -9
    for n, h in enumerate(heads):
        if h - last_h <= 3:          # cognate masdar or repeated form shortly after the head (توليت الأمر توليا)
            continue
        last_h = h
        end = heads[n + 1] if n + 1 < len(heads) else len(toks)
        head = toks[h]
        ms, voice = head_forms(raw_toks[h], head, root)
        definite_or_tm = head.startswith('ال') or raw_toks[h].endswith('ة') or raw_toks[h].rstrip('\u064b-\u0652').endswith('ة')
        c = dict(head=head, measures=ms, voice=voice, preps=set(), alts=[], obj_wild=False, subj_wild=False,
                 origin=origin, text=text, toks=toks if clean else None, hpos=h)
        rf = root_forms().get(root, {})
        for q in ('هما', 'هم', 'ها', 'ه', 'ني', 'ك'):
            if definite_or_tm or not verb_like(raw_toks[h], head, root):
                break
            if head.endswith(q) and len(head) - len(q) >= 3 and qkey(head) not in rf:
                stem = head[:-len(q)]
                if qkey(stem) in rf or carries_root(stem, root):
                    c['obj_wild'] = True
                break
        # a definite masdar opening the statement followed by a content word = a definition, not a construction
        definitional = (h == 0 or toks[h - 1] in LEAD) and head.startswith('ال')
        pending, k = None, 0
        skipped_generic = []
        for j in range(h + 1, min(end, h + 6)):
            t = toks[j]
            k += 1
            if t in GLOSS or (t[:1] in 'وف' and t[1:] in GLOSS and len(t) > 3):
                break
            if t in PREP_WORDS or (t[:1] == 'و' and t[1:] in PREP_WORDS and c['alts']):
                p = PREP_WORDS[t if t in PREP_WORDS else t[1:]]
                if not c['alts']:
                    c['preps'].add(p)
                pending = p
                continue
            m = re.match(r'^(و?)(علي|عن|من|الي|في|ب|ل|ك)(هما|هم|هن|ها|ه|كم|ك|نا|ني|ي)$', t)
            m2 = re.match(r'^(و?)(ب|ل|ك|في|م|ع)(ما|من)$', t)
            if m2 and not c['alts']:
                p = {'م': 'من', 'ع': 'عن'}.get(m2.group(2), m2.group(2))
                c['preps'].add(p)
                if p != 'ل' and not clean:
                    break
                pending = None
                continue
            if m or t in ('عليه', 'عليها', 'عليهم', 'اليه', 'اليها', 'اليهم', 'علي', 'الي'):
                p = m.group(2) if m else ('علي' if t.startswith('علي') else 'الي')
                if c['alts']:
                    break
                c['preps'].add(p)
                if p != 'ل' and not clean:
                    break                  # a filled prepositional slot closes the statement
                pending = None
                continue
            u, coord = t, False
            if u[:1] in 'وف' and len(u) > 3:
                if u[1:] in OBJ_WILD or u[1:] in SUBJ_WILD or u[1:] in FUNC or u[1:] in PREP_WORDS:
                    u = u[1:]
                elif (c['alts'] or c['obj_wild']) and not exact_known(u):
                    u, coord = u[1:], True
            if c['obj_wild'] and not c['alts'] and pending is None and not clean and u not in PREP_WORDS \
                    and u not in FUNC and not (u[:1] in 'بلك' and len(u) > 3):
                break                      # after a filled object slot, a bare content word is the gloss
            if u == 'او' or u == 'ام':
                pending = None
                continue
            p = pending
            if u[:1] in 'بلك' and len(u) > 3 and u[1:] not in FUNC:
                inner = u[1:]
                if inner.startswith('ال') or inner in OBJ_WILD or inner in SUBJ_WILD or \
                        (tok_roots(inner, root) and not exact_known(u)):
                    p, u = u[0], inner
            if c['alts'] and not coord and not (p and pending is None and u):
                if not (p and p == c['alts'][0][0]):
                    break
            if u in OBJ_WILD or u in SUBJ_WILD:
                if p:
                    if not c['alts']:
                        c['preps'].add(p)
                        if p != 'ل' and not clean:
                            break
                elif u in OBJ_WILD or u.endswith('ا'):
                    c['obj_wild'] = True
                else:
                    c['subj_wild'] = True
                pending = None
                continue
            if u in FUNC or len(u) < 2:
                pending = None
                continue
            if carries_root(u, root):
                pending = None
                continue
            rs_all = tok_roots(u, root)
            if rs_all and rs_all <= GEN_ROOTS:
                skipped_generic.append((p, frozenset(rs_all), u[2:] if u.startswith('ال') and len(u) > 4 else u))
                pending = None
                continue
            if definitional and not c['alts'] and not c['preps'] and p is None:
                break
            rs = rs_all - GEN_ROOTS
            stem = u[2:] if u.startswith('ال') and len(u) > 4 else u
            if not rs and len(stem) < 3:
                pending = None
                continue
            if p and not c['alts']:
                c['preps'].add(p)
            c['alts'].append((p, frozenset(rs), stem))
            pending = None
        # partner before the head, for noun formulas where the root word comes last ('أنف فلان في أسلوب')
        if not c['alts'] and not c['preps'] and origin.startswith('lu') and h > 0:
            for j in range(max(0, h - 3), h):
                t = toks[j]
                if t in FUNC or t in SUBJ_WILD or t in OBJ_WILD or t in LEAD or len(t) < 3:
                    continue
                rs = tok_roots(t, root) - GEN_ROOTS
                stem = t[2:] if t.startswith('ال') and len(t) > 4 else t
                c['alts'].append((None, frozenset(rs), stem))
                break
        if not c['alts'] and clean and skipped_generic and not c['obj_wild']:
            # a formula whose only partner is a common word (أيام الله): matched only through iḍāfa
            p0 = skipped_generic[0]
            c['alts'].append(('idafa', p0[1], p0[2]))
        c['bare'] = not c['alts'] and not c['preps'] and not c['obj_wild']
        cons.append(c)
    return cons


@functools.lru_cache(None)
def constructions(ref):
    b = G.dictionary()['branches'][ref]
    root = b['root']
    out = []
    seen = set()
    for origin, text in statements(b):
        for c in parse_statement(origin, text, root):
            key = (tuple(sorted(c['measures'])), c['voice'], tuple(sorted(c['preps'])),
                   tuple(sorted((p or '', s) for p, _, s in c['alts'])), c['obj_wild'], c['bare'])
            if key in seen:
                continue
            seen.add(key)
            c['branch_ref'] = ref
            out.append(c)
    return out


def checkable(c):
    """a construction the script can check: partner, preposition, object slot, or a bare DERIVED form."""
    if c['alts'] or c['preps'] or c['obj_wild']:
        return True
    return bool(c['measures']) and 'I' not in c['measures']


# ------------------------------------------------------------------------------------------- occurrence context
def pnorm(p):
    p = G.norm(p or '').replace('ـ', '')
    return {'ب': 'ب', 'ل': 'ل', 'ك': 'ك'}.get(p, p)


@functools.lru_cache(maxsize=200000)
def context(ref):
    W = G.words()
    d = W[ref]
    L = G.links().get(ref, [])
    F = G.frames().get(ref)
    ay = G.ayah_words()[(d['s'], d['a'])]
    k0 = ay.index(ref)
    linked = {}          # other ref -> set of (relation, prep)
    gov_preps = collections.defaultdict(set)    # prep -> set(complement refs)
    governed_by = set()
    obj_refs, idafa_deps, subj_refs = set(), set(), set()
    has_obj = False
    for l in L:
        for o in l['other']:
            if o == ref:
                continue
            linked.setdefault(o, set()).add((l['rel'], pnorm(l['prep']) if l['rel'] == 'prep_complement' else ''))
        if l['rel'] == 'prep_complement' and l['role'] == 'head':
            gov_preps[pnorm(l['prep'])].update(o for o in l['other'] if o != ref)
            if not l['other'] or all(o == ref for o in l['other']):
                gov_preps[pnorm(l['prep'])].add('')
        if l['rel'] == 'prep_complement' and l['role'] == 'dependent':
            governed_by.add(pnorm(l['prep']))
        if l['rel'] == 'direct_object' and l['role'] == 'head':
            has_obj = True
            obj_refs.update(o for o in l['other'] if o != ref)
        if l['rel'] == 'idafa' and l['role'] == 'head':
            idafa_deps.update(l['other'])
        if l['rel'] in ('subject',) and l['role'] == 'head':
            subj_refs.update(l['other'])
    if F and F['obj'] in ('explicit', 'clitic', 'both'):
        has_obj = True
        for p in F['preps']:
            gov_preps.setdefault(pnorm(p), set())
    # QAC fallback for an object suffix when grammar has no frame: a second pronoun suffix on a verb
    if d['pos'] == 'V' and not F:
        prons = [s for s in d['suffixes'] if s[0] == 'PRON']
        if len(prons) >= 2 or (prons and G.norm(prons[-1][1]) in ('ه', 'ها', 'هم', 'هما', 'هن', 'ك', 'كم', 'ني')):
            has_obj = True
    # a preposition word right after (for unaligned words)
    nxt = []
    for j in range(k0 + 1, min(len(ay), k0 + 3)):
        x = W[ay[j]]
        if x['pos'] == 'P' or G.norm(x['surface']) in PREP_WORDS:
            nxt.append(PREP_WORDS.get(G.norm(x['lemma'] or x['surface']), G.norm(x['lemma'] or x['surface'])))
        for pp in x['prefixes']:
            if pp[0] == 'P':
                nxt.append(pnorm(pp[1]))
        if x['root']:
            break
    antecedent = set()
    for part, anc, txt in G.antecedents().get(ref, []):
        antecedent.update(anc)
    for o in list(obj_refs):          # object pronoun on the verb itself resolved through the frame's grammar
        if o == ref:
            pass
    window = [ay[j] for j in range(max(0, k0 - 4), min(len(ay), k0 + 5)) if j != k0]
    before = [ay[j] for j in range(max(0, k0 - 8), k0)]
    before_prev = [ay[j] for j in range(max(0, k0 - 6), k0)]
    # second-hop words: the complement / iḍāfa / adjective / apposition / conjunct of a directly linked word
    # (ḍarabnā … min kulli mathalin: the verb links to kulli, kulli to mathalin)
    hop2 = set()
    down = set()
    for l in L:
        if l['role'] == 'head' and l['rel'] in ('prep_complement', 'direct_object', 'idafa', 'adjective',
                                                 'apposition', 'circumstantial', 'accusative_specification'):
            down.update(o for o in l['other'] if o != ref)
    for o in down:
        for l2 in G.links().get(o, []):
            if l2['role'] == 'head' and l2['rel'] in ('prep_complement', 'idafa', 'adjective', 'apposition',
                                                       'conjoined'):
                hop2.update(x for x in l2['other'] if x != ref and x not in linked)
    return dict(d=d, measure=mnorm(d['measure']), voice='PASS' if 'PASS' in d['feats'].split('|') else 'ACT',
                linked=linked, gov_preps=dict(gov_preps), governed_by=governed_by, has_obj=has_obj,
                obj_refs=obj_refs, idafa_deps=idafa_deps, subj_refs=subj_refs, next_preps=set(nxt),
                antecedent=antecedent, window=window, before=before_prev, hop2=hop2, grammar=bool(L or F),
                frame=F)


@functools.lru_cache(maxsize=None)
def word_keys(ref):
    x = G.words()[ref]
    ks = set()
    for f in (x['stem'], x['lemma'], x['surface']):
        n = qnorm(f)
        for v in variants(n):
            if len(v) >= 3:
                ks.add(v)
                ks.add('~' + skel(v))
    return x['root'], frozenset(ks)


@functools.lru_cache(None)
def root_definitions():
    """root -> set of normalised tokens in its first branch's image (definitional join: the first branch in
    dictionary order carries the root's core sense; other branches and the longer what_is made the join noisy)."""
    out = collections.defaultdict(set)
    for b in G.dictionary()['branches'].values():
        if b['bid'] != 'B001':
            continue
        for t in AR.findall(G.norm(b['image'])):
            out[b['root']].add(t)
            if t.startswith('ال') and len(t) > 4:
                out[b['root']].add(t[2:])
    return out


def prep_before(o, prep):
    """surface check: the word carries the preposition as a prefix or the previous word is that preposition."""
    W = G.words()
    x = W[o]
    if prep in ('ب', 'ل', 'ك') and any(pp[0] == 'P' and pnorm(pp[1]) == prep for pp in x['prefixes']):
        return True
    ay = G.ayah_words()[(x['s'], x['a'])]
    k = ay.index(o)
    if k > 0:
        y = W[ay[k - 1]]
        if pnorm(y['lemma'] or y['surface']) == prep or G.norm(y['surface']).lstrip('وف') == prep:
            return True
    return False


def partner_hit(p, refs, need_prep, ctx, surface_prep=False):
    """does partner p=(prep, roots, stem) match one of refs? returns 'root'|'stem'|None.
    need_prep: the stated preposition must link the partner (grammar); surface_prep: or stand right before it."""
    prep, rs, stem = p
    for o in refs:
        if o not in G.words():
            continue
        r, ks = word_keys(o)
        if (rs and r in rs) or stem in ks or (len(stem) >= 3 and ('~' + skel(stem)) in ks and len(skel(stem)) >= 3):
            if prep == 'idafa':
                if not (need_prep and any(rel in ('idafa', 'subject') for rel, _ in ctx['linked'].get(o, set()))):
                    continue
                return 'root' if (rs and r in rs) else 'stem'
            if need_prep and prep:
                rels = ctx['linked'].get(o, set())
                if not any(rp == prep for rel, rp in rels if rel == 'prep_complement'):
                    if not prep_before(o, prep):
                        continue
            elif surface_prep and prep and not prep_before(o, prep):
                continue
            return 'root' if (rs and r in rs) else 'stem'
    return None


def def_hit(p, refs):
    prep, rs, stem = p
    if len(stem) < 3:
        return None
    D = root_definitions()
    for o in refs:
        r = G.words().get(o, {}).get('root')
        if r and (stem in D.get(r, ()) or ('ال' + stem) in D.get(r, ())):
            return r
    return None


def form_ok(c, ctx):
    if c['measures'] and ctx['measure'] not in c['measures']:
        return False
    if c['voice'] == 'PASS' and ctx['voice'] != 'PASS':
        return False
    return True


def specificity(c, ctx):
    """small tie-breaker: a satisfied voice constraint or a single named measure is more specific."""
    s = 0.0
    if c['voice'] == 'PASS' and ctx['voice'] == 'PASS':
        s += 0.1
    if len(c['measures']) == 1 and ctx['measure'] in c['measures']:
        s += 0.05
    return s


WEAK_REASONS = ('prep-lam', 'object-formI', 'prep-other-form', 'subject-pronoun', 'lexeme-unconfirmed')
WINDOW_REASONS = ('partner-win', 'partner-before-pronoun', 'partner-other-form', 'prep-other-form', 'partner-def')


def tok_match(word_ref, tok):
    """a Quran word matches a statement token (clitic- and orthography-tolerant; content forms of 3+ letters)."""
    r, ks = word_keys(word_ref)
    tv = [v for v in variants(tok) if len(v) >= 3]
    return any(v in ks or ('~' + skel(v)) in ks for v in tv)


def surface_is(word_ref, tok):
    """a short function token (preposition) is the word itself or its prefix."""
    x = G.words()[word_ref]
    n = G.norm(x['surface']).lstrip('وف')
    return n == tok or n.startswith(tok) or (tok in ('ب', 'ل', 'ك') and
                                              any(pp[0] == 'P' and pnorm(pp[1]) == tok for pp in x['prefixes']))


# The class of a single-lexeme (non_bare) unit, read from the branch's own image, definition and Turkish gloss. The
# unvocalised skeleton cannot tell أُحُد (the mountain) from أَحَد, أَجَلْ ('yes') from أَجَل, الكَتَم (a plant)
# from نكتم, so a lexeme match must also agree with the QAC part of speech of the occurrence (review M1).
LEX_PROPER = re.compile(r"اسم (?:جبل|مكان|موضع|رجل|امرأة|ماء|بلد|علم|قبيلة|فرس|صنم|واد)|قبيل[ةت]|بطن من|اسمي? قبيلتين|"
                        r"علما ل|موضع|مواضع|أعلام|أسماء|المسمى|بلد ب|جبل ب|ماء ل")
LEX_PROPER_TR = re.compile(r"özel ad|boy ad|boyunun ad|yer ad|kabile|kuyu ad|kişi ad|dağın|put ad|at ad|vadi ad|"
                           r"\badı\b|\badları\b|\badıyla\b|nehri\b", re.I)
LEX_PARTICLE = re.compile(r"(?:^|\s)(?:ال)?(?:حرف|أداة|جواب|ظرف)(?:\s|$)|في الجواب|في التلهف|تعجب|نداء|استفهام|نفي")
LEX_PARTICLE_TR = re.compile(r"bağlaç|edat|ünlem|evet|olumsuzluk|soru |seslenme", re.I)
LEX_THING = re.compile(r"نبات|نبت|شجر|حيوان|طائر|دابة|حجر|أولاد|حبل|سيور|الفصيل")
LEX_THING_TR = re.compile(r"bitki|ağaç|hayvan|kuş|yavru|\bip\b|ipi\b|kayış", re.I)
PARTICLE_POS = {'P', 'NEG', 'ACC', 'COND', 'CONJ', 'SUB', 'INTG', 'CERT', 'RES', 'RET', 'EXP', 'INC', 'EXL', 'AMD',
                'INT', 'FUT', 'ANS', 'EXH', 'SUR', 'AVR', 'T', 'LOC', 'REL', 'DEM', 'PRO', 'VOC', 'EMPH', 'PREV',
                'SUP', 'CAUS', 'EQ', 'IMPN', 'IMPV', 'PRP', 'COM', 'CIRC', 'INL', 'REM', 'RSLT'}


@functools.lru_cache(None)
def lexeme_class(branch_ref):
    b = G.dictionary()['branches'][branch_ref]
    ar = ' '.join([b.get('image') or '', b.get('what') or ''])
    tr = b.get('gloss') or ''
    if LEX_PROPER.search(ar) or LEX_PROPER_TR.search(tr):
        return 'proper'
    if re.search(r"(?:^|\s)(?:ال)?ظرف", ar):
        return 'adverb'
    if LEX_PARTICLE.search(ar) or LEX_PARTICLE_TR.search(tr):
        return 'particle'
    if LEX_THING.search(ar) or LEX_THING_TR.search(tr):
        return 'thing'
    return ''


_VOWEL = {'\u064e': 'a', '\u064f': 'u', '\u0650': 'i', '\u064b': 'a', '\u064c': 'u', '\u064d': 'i'}
_MARKS = re.compile('[\u064b-\u0652]')


def _vowels(t):
    """[(letter, short vowel or '')] of a vocalised word, article removed; long vowels and seats kept as letters."""
    t = re.sub('^[وف]?(?:[اٱ]ل)', '', (t or '').replace('ـ', '').replace('\u0670', 'ا'))
    out = []
    for ch in t:
        if ch in _VOWEL:
            if out:
                out[-1] = (out[-1][0], _VOWEL[ch])
        elif not _MARKS.match(ch) and re.match('[ء-ي]', ch):
            out.append((ch, ''))
    return out


def vowel_conflict(stmt, lemma):
    """True when the dictionary writes the unit with short vowels and they differ from the QAC lemma's at a letter
    where both are marked (جَنَد against جُند, المُدّ against مَدّ). Unvocalised statements never conflict."""
    a, b = _vowels(stmt), _vowels(lemma)
    if not any(v for _, v in a) or len(a) != len(b):
        return False
    return any(va and vb and va != vb for (_, va), (_, vb) in zip(a, b))


@functools.lru_cache(None)
def _branch_tokens(branch_ref):
    b = G.dictionary()['branches'][branch_ref]
    out = set()
    for f in ('image', 'what', 'phrase'):
        for w in re.findall('[ء-ي]+', qnorm(b.get(f) or '')):
            out.add(w[2:] if w.startswith('ال') and len(w) > 4 else w)
    return frozenset(out)


def lexeme_shared(branch_ref, tok):
    """Another branch of the same root names the same lexeme in its own text (ليلة in the night branch as well as in
    'the nearest night'): the lexeme alone cannot choose between them."""
    t = tok[2:] if tok.startswith('ال') and len(tok) > 4 else tok
    forms = {t} | {t[:-len(x)] for x in ('هما', 'كما', 'ها', 'هم', 'هن', 'كم', 'كن', 'نا', 'ه', 'ك')
                   if t.endswith(x) and len(t) - len(x) >= 3}
    rid = G.dictionary()['branches'][branch_ref]['root_id']
    return any(forms & _branch_tokens(o) for o in branches_by_root_id()[rid] if o != branch_ref)


def lexeme_pos_ok(branch_ref, tok, ctx):
    """A single-lexeme unit matches only an occurrence of the same word class: a proper name a QAC proper noun, a
    particle a QAC particle; a unit written with the article never a verb. Returns True, False, or 'unknown' for a
    plant / animal / object name, which a skeleton and a noun tag cannot tell from a common noun (التأويل plant)."""
    pos = ctx['d']['pos']
    cls = lexeme_class(branch_ref)
    if cls == 'proper':
        return pos == 'PN'
    if cls == 'particle':
        return pos in PARTICLE_POS
    if cls == 'adverb':          # QAC tags an adverb governed by a preposition as a noun (مِنْ عِندِ)
        return pos in PARTICLE_POS or pos == 'N'
    if cls == 'thing':
        return 'unknown' if pos == 'N' else False
    if tok.startswith('ال') and pos == 'V':
        return False
    return 'unknown' if lexeme_shared(branch_ref, tok) else True


def formula_level(c, ctx, kind):
    """lexical-unit formulas: the dictionary's own expression stands around the occurrence, token by token, with
    at least one content word besides the root word (أيام الله, من دونه); the verb form must be the stated one.
    A single-token unit of a form-bound (non_bare) branch = the lexeme itself (عند)."""
    toks = c.get('toks')
    if not toks:
        return 0.0
    ay = G.ayah_words()[(ctx['d']['s'], ctx['d']['a'])]
    k0 = ay.index(ctx['d']['ref'])
    h = c['hpos']
    if len(toks) == 1:
        if kind != 'non_bare':
            return 0.0
        # exact lexeme: the occurrence's lemma, or its surface without proclitics, is the named form itself
        lem = qnorm(ctx['d']['lemma'])
        lem = lem[2:] if lem.startswith('ال') and len(lem) > 3 else lem
        t0 = toks[0][2:] if toks[0].startswith('ال') and len(toks[0]) > 3 else toks[0]
        surf = qnorm(ctx['d']['surface'])
        for p in ('وال', 'فال', 'بال', 'كال', 'لل', 'ال', 'و', 'ف', 'ب', 'ل', 'ك'):
            if surf.startswith(p) and len(surf) - len(p) >= 2:
                surf = surf[len(p):]
                break
        if not (lem == t0 or surf == t0):
            return 0.0
        if vowel_conflict(c.get('text') or '', ctx['d']['lemma']):
            return 0.0
        ok = lexeme_pos_ok(c['branch_ref'], toks[0], ctx)
        if ok == 'unknown':
            return 1.1       # a lexeme match the script cannot confirm: reported as unknown (see WEAK_REASONS)
        return 3.0 if ok else 0.0
    if not form_ok(c, ctx):
        return 0.0
    n_content = 0
    for j, t in enumerate(toks):
        if j == h or t in SUBJ_WILD or t in OBJ_WILD:
            continue

        k = k0 + (j - h)
        if k < 0 or k >= len(ay):
            return 0.0
        if t in FUNC or t in PREP_WORDS or len(t) <= 2:
            if not surface_is(ay[k], t):
                return 0.0
            continue
        if not tok_match(ay[k], t):
            return 0.0
        n_content += 1
    return 3.0 if n_content else 0.0


def head_class(c):
    """'noun' or 'verb' for a statement's head word when QAC attests its skeleton under this root with one class
    only, or its spelling shows it (article or ta marbuta: noun); '' when undecided."""
    root = G.dictionary()['branches'][c['branch_ref']]['root']
    h = c.get('head') or ''
    rf = root_forms().get(root, {})
    for v in variants(h):
        if v in rf:
            poss = {pos for pos, _, _ in rf[v]}
            if poss == {'V'}:
                return 'verb'
            if 'V' not in poss:
                return 'noun'
            return ''
    toks = c.get('toks') or []
    raw = toks[c['hpos']] if toks and c.get('hpos') is not None and c['hpos'] < len(toks) else h
    if raw.startswith('ال') or raw.endswith(('ة', 'ه')) and not verb_like(raw, h, root):
        return 'noun'
    return ''


def head_class_clash(c, ctx):
    """The statement's head is a noun and the occurrence a verb (غروب العين 'tear ducts' against تغرب في عين), or
    the head a verb and the occurrence a plain noun (نوّر على فلان against نار): the construction is another word."""
    hc = head_class(c)
    pos = ctx['d']['pos']
    feats = ctx['d']['feats'].split('|')
    deverbal = 'VN' in feats or 'PCPL' in feats
    return (hc == 'noun' and pos == 'V') or (hc == 'verb' and pos in ('N', 'PN') and not deverbal)


def match(c, ctx, kind='collocation'):
    """level, reason for one construction at one occurrence."""
    fl = formula_level(c, ctx, kind)
    if not fl and (c['alts'] or c['preps'] or c['obj_wild']) and head_class_clash(c, ctx):
        return 0.0, ''
    if fl:
        return fl, ('formula' if len(c.get('toks') or []) > 1 else ('lexeme' if fl >= 3.0 else 'lexeme-unconfirmed'))
    same_form = form_ok(c, ctx)
    if not same_form and not (c['alts'] or c['preps'] or c['obj_wild']):
        return 0.0, ''
    if c['voice'] == 'PASS' and ctx['voice'] != 'PASS':
        return 0.0, ''
    linked = set(ctx['linked']) | ctx['antecedent']
    sp = specificity(c, ctx)
    if c['alts']:
        # a stated preposition with a slot of its own (أحاط به علما) must be governed as well
        if c['preps'] and not any(p[0] for p in c['alts']) and not (c['preps'] <= {'ل'}):
            if not any(p in ctx['gov_preps'] or (p in ctx['next_preps'] and not ctx['grammar']) for p in c['preps']):
                return form_named(c, ctx) if same_form else (0.0, '')
        lv, why = 0.0, ''
        if any(partner_hit(p, linked, True, ctx) for p in c['alts']):
            lv, why = 3.0, 'partner'
        elif ctx['d']['pos'] == 'V' and all(p[0] == 'idafa' for p in c['alts']) and not ctx['subj_refs'] \
                and same_form:
            return 1.2, 'subject-pronoun'      # the named subject may be the verb's own pronoun (أوحينا)
        elif any(partner_hit(p, ctx['hop2'], False, ctx, True) for p in c['alts']):
            lv, why = 2.95, 'partner-2hop'
        elif any(def_hit(p, linked) for p in c['alts'] if not p[0] or p[0] in ctx['gov_preps']
                 or p[0] in ctx['governed_by']):
            lv, why = 2.9, 'partner-def'
        elif ctx['frame'] and ctx['frame']['obj'] in ('clitic', 'both') and not ctx['antecedent'] and \
                any(partner_hit(p, ctx['before'], False, ctx) for p in c['alts'] if not p[0]):
            lv, why = 2.5, 'partner-before-pronoun'
        elif any(partner_hit(p, ctx['window'], False, ctx, True) for p in c['alts']):
            lv, why = 2.5, 'partner-win'
        if lv and not same_form:
            # the partner is grammatically linked (with its preposition) but the dictionary states another verb
            # form: a construction-level match; weaker evidence (window / second hop) with another form is none
            if lv >= 3.0:
                return 2.6, 'partner-other-form'
            return 0.0, ''
        if lv:
            return lv + sp, why
        return form_named(c, ctx) if same_form else (0.0, '')
    prep_ok = True
    if c['preps']:
        # the word after is read as the governed preposition only for words without grammar data (وإليه ترجعون
        # after يبسط belongs to the next verb)
        prep_ok = any(p in ctx['gov_preps'] or (p in ctx['next_preps'] and not ctx['grammar']) for p in c['preps'])
    obj_ok = True
    if c['obj_wild']:
        feats = ctx['d']['feats'].split('|')
        deverbal = ctx['d']['pos'] != 'V' and ('VN' in feats or 'PCPL' in feats)
        obj_ok = ctx['has_obj'] or (deverbal and bool(ctx['idafa_deps'])) or \
            (ctx['voice'] == 'PASS' and ctx['d']['pos'] == 'V')
    if c['preps'] or c['obj_wild']:
        if prep_ok and obj_ok:
            weak = c['preps'] and c['preps'] <= {'ل'} and not c['obj_wild']    # dative lam alone: weak frame
            if not same_form:
                if c['preps'] and not c['obj_wild'] and not weak:
                    return 1.5, 'prep-other-form'
                return 0.0, ''
            if weak:
                return 1.2 + sp, 'prep-lam'
            if c['obj_wild'] and not c['preps'] and ctx['measure'] == 'I':
                return 1.2 + sp, 'object-formI'        # a plain transitive Form I use looks the same
            return 2.0 + sp, 'prep' if c['preps'] else 'object'
        if not same_form:
            return 0.0, ''
        return form_named(c, ctx)
    # bare statement: only a DERIVED form named by the dictionary licenses (user rule); an unvocalised head that
    # could also be Form I (shadda / dagger alif not written) does not name a derived form
    if c['measures'] and 'I' not in c['measures'] and ctx['measure'] in c['measures']:
        if ctx['has_obj']:
            return 0.0, ''
        return 1.0 + sp, 'form'
    return 0.0, ''


def form_named(c, ctx):
    """user rule, second half: the dictionary's own statement (what_is or lexical unit) names a derived form; the
    occurrence is that form with a compatible valency (object slot <-> direct object) -> weakest positive level."""
    if not (c['origin'].startswith('lu') or c['origin'] == 'what'):
        return 0.0, ''
    if not c['measures'] or 'I' in c['measures'] or ctx['measure'] not in c['measures']:
        return 0.0, ''
    wants_obj = c['obj_wild'] or any(p[0] is None for p in c['alts'])
    has_obj = ctx['has_obj'] or ctx['voice'] == 'PASS'
    if wants_obj != has_obj and not (wants_obj and ctx['d']['pos'] != 'V'):
        return 0.0, ''
    return 0.9 + specificity(c, ctx), 'form-named'


def best(ref, ctx):
    lv, why, cc = 0.0, '', None
    kind = G.dictionary()['branches'][ref]['kind']
    for c in constructions(ref):
        l, w = match(c, ctx, kind)
        if l > lv:
            lv, why, cc = l, w, c
    return lv, why, cc


@functools.lru_cache(None)
def branches_by_root_id():
    out = collections.defaultdict(list)
    for ref, b in G.dictionary()['branches'].items():
        out[b['root_id']].append(ref)
    for v in out.values():
        v.sort()
    return out


GUARDED = ('collocation', 'non_bare')


def decide(occ, root_id, policy='default'):
    """-> {branch_ref: (call, level, reason, construction text)} for the root's collocation / non_bare branches.
    present: a partner construction (grammatical link, second hop, definition, or window / pronoun look-back);
    for preposition / object-slot / bare-form matches (levels 1-2): present unless another branch of the root
    matches more specifically through grammar (then absent) or equally (then unknown: shared construction)."""
    B = G.dictionary()['branches']
    refs = branches_by_root_id()[root_id]
    ctx = context(occ)
    levels = {r: best(r, ctx) for r in refs}
    out = {}
    for r in refs:
        if B[r]['kind'] not in GUARDED:
            continue
        lv, why, c = levels[r]
        ctext = c['text'] if c else ''
        others = [(levels[o][0], levels[o][1], o) for o in refs if o != r and levels[o][1] not in WINDOW_REASONS]
        top_other = max(others, default=(0.0, '', None))
        if lv >= 2.5 and why in ('partner-win', 'partner-before-pronoun'):
            call = 'unknown'
            why = f'{why}; partner nearby but not grammatically linked'
        elif lv >= 2.5:
            call = 'present'
        elif lv > 0 and why in WEAK_REASONS:
            call = 'unknown'
            why = f'{why}; frame too common to decide by script'
        elif lv > 0:
            if top_other[0] > lv + 1e-9:
                call = 'absent'
                why = f'{why}; outranked by {top_other[2].split("/")[1]} ({top_other[1]})'
            elif abs(top_other[0] - lv) < 1e-9 and policy == 'default':
                call = 'unknown'
                why = f'{why}; shared with {top_other[2].split("/")[1]}'
            else:
                call = 'present'
        else:
            cons = constructions(r)
            if not any(checkable(c) for c in cons):
                call, why = 'unknown', 'no checkable construction (bare Form I or no head word found)'
            elif not ctx['grammar']:
                call, why = 'unknown', 'no grammar data for this word'
            else:
                call, why = 'absent', 'construction not found'
        out[r] = (call, round(lv, 2), why, ctext)
    return out


def all_calls(policy='default'):
    """Every Quranic occurrence x collocation/non_bare branch of its root -> call. Yields tuples."""
    D = G.dictionary()
    B = D['branches']
    roots = sorted({b['root_id'] for b in B.values() if b['kind'] in GUARDED})
    for rid in roots:
        for occ in D['occ'].get(rid, []):
            if occ not in G.words():
                continue
            for r, v in decide(occ, rid, policy).items():
                yield (occ, r) + v


if __name__ == '__main__':
    # show the parsed constructions of some branches (argv: branch refs)
    for ref in sys.argv[1:]:
        b = G.dictionary()['branches'][ref]
        print(ref, b['root'], b['kind'], b['image'])
        for c in constructions(ref):
            print('   ', c['origin'], '|', c['text'][:70], '| head', c['head'], sorted(c['measures']), c['voice'],
                  '| preps', sorted(c['preps']), '| alts', [(p, sorted(rs), s) for p, rs, s in c['alts']],
                  '| obj' if c['obj_wild'] else '', '| bare' if c['bare'] else '')
