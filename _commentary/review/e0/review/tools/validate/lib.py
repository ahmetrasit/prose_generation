"""E0 link validation: shared read-only loaders.

Every source is read-only. Caches are written only to ./cache (this directory).
Sources:
  - the project dictionary: quran-data/data/dictionary/tr/root_*_entry.json (branch image, what_is, source phrase,
    branch_kind, neighbour relations)
  - early entry texts: dictionary/data/output/root_packets/root_*.json (dictionary_sources[].entry_text_clean) for the
    six early sources only (ayn, maqayis, jamhara, sihah, tahdhib, mufradat)
  - QAC words / lemmas as exported in v15/data/words.tsv and lemmas.tsv (morphology only; no v15 scene data)
  - quran-slm corpus_network directional ranks (E5, NeoAraBERT, character) for the similarity type
  - Qnet v2 branch_keywords.tsv
Code for the lemma/clitic handling follows the Phase 2 C1 prototype (C1-branch-distance/common.py, metrics2.py).
"""
import csv, json, glob, re, os, math, pickle, collections, sys
sys.dont_write_bytecode = True
csv.field_size_limit(1_000_000_000)

P = '/Volumes/OZTURK/_projects'
TR = f'{P}/quran-data/data/dictionary/tr'
PACK = f'{P}/dictionary/data/output/root_packets'
V15 = f'{P}/prose_generation/_commentary/v15/data'
SLM = f'{P}/quran-slm'
QNET = f'{P}/quran-roots/_corpus/activation/Qnet/v2/network/incidence_full/branch_keywords.tsv'
HFT = ('/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/'
       'scratchpad/phase2/K-northstar-critic/hft_na_set.json')
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'cache')
os.makedirs(CACHE, exist_ok=True)
EARLY = ('ayn', 'maqayis', 'jamhara', 'sihah', 'tahdhib', 'mufradat')

DIAC = re.compile('[ؐ-ًؚ-ٰۖ-ۭـ]')


def norm(t):
    t = DIAC.sub('', t or '')
    t = re.sub('[أإآٱ]', 'ا', t)
    return t.replace('ى', 'ي').replace('ة', 'ه').replace('ؤ', 'و').replace('ئ', 'ي')


def skel(t):
    """consonantal skeleton for matching Uthmani against imla'i quotations: no alef/hamza/diacritics"""
    t = DIAC.sub('', t or '')
    t = re.sub('[اأإآٱءىئؤ]', lambda m: {'ى': 'ي', 'ئ': 'ي', 'ؤ': 'و'}.get(m.group(0), ''), t)
    return t.replace('ة', 'ه')


def nroot(r):
    return re.sub('[أإآؤئ]', 'ء', (r or '').strip())


def cached(name, fn):
    p = os.path.join(CACHE, name + '.pkl')
    if os.path.exists(p):
        return pickle.load(open(p, 'rb'))
    v = fn()
    pickle.dump(v, open(p, 'wb'))
    return v


# ------------------------------------------------------------------ Quran words
def _words():
    out = []
    for w in csv.DictReader(open(f'{V15}/words.tsv', encoding='utf-8'), delimiter='\t'):
        roots = [nroot(r) for r in w['roots'].split('|') if r.strip()]
        out.append(dict(s=int(w['surah']), a=int(w['ayah']), w=int(w['w']), surface=w['surface'], roots=roots,
                        lemma=w['lemmas'], pos=w['pos']))
    return out


WORDS = cached('words', _words)
BY_AYAH = collections.defaultdict(list)
for _w in WORDS:
    BY_AYAH[(_w['s'], _w['a'])].append(_w)
AYAT = sorted(BY_AYAH)
NAY = len(AYAT)
AYAT_OF = collections.defaultdict(list)
for _s, _a in AYAT:
    AYAT_OF[_s].append(_a)
AY_ROOTS = {k: frozenset(r for w in ws for r in w['roots']) for k, ws in BY_AYAH.items()}
ROOT_AY = collections.defaultdict(set)
for _k, _rs in AY_ROOTS.items():
    for _r in _rs:
        ROOT_AY[_r].add(_k)
ROOT_DF = {r: len(v) for r, v in ROOT_AY.items()}
LEM_AY = collections.defaultdict(set)
LEM_ROOT = {}
for _w in WORDS:
    if len(_w['roots']) == 1 and _w['lemma'] and '|' not in _w['lemma']:
        LEM_AY[_w['lemma']].add((_w['s'], _w['a']))
        LEM_ROOT[_w['lemma']] = _w['roots'][0]
LEM_DF = {L: len(v) for L, v in LEM_AY.items()}


# ------------------------------------------------------------------ dictionary branches (project dictionary only)
def _branches():
    rid2root = {}
    for r in csv.DictReader(open(f'{V15}/branches.tsv', encoding='utf-8'), delimiter='\t'):
        rid2root[r['root_id']] = nroot(r['root'])
    B = {}
    for f in sorted(glob.glob(f'{TR}/root_*_entry.json')):
        d = json.load(open(f))
        for br in d.get('branches', []):
            m = re.match(r'(root_\d+)/(B\d+)', br.get('branch_ref', ''))
            if not m:
                continue
            rid, bid = m.group(1), m.group(2)
            root = rid2root.get(rid)
            if root is None:
                try:
                    root = nroot(json.load(open(f'{PACK}/{rid}.json'))['root_norm'])
                except Exception:
                    root = rid
            ls = br.get('lexicalization_scope') or {}
            nbs = []
            for nd in br.get('neighbor_distinctions') or []:
                m2 = re.match(r'(root_\d+)/(B\d+)', nd.get('neighbor_ref', ''))
                if m2:
                    nbs.append(((m2.group(1), m2.group(2)), nd.get('relation_type')))
            B[(rid, bid)] = dict(rid=rid, bid=bid, root=root, kind=ls.get('branch_kind'), note=ls.get('note'),
                                 image=br.get('branch_image_ar') or '', what=br.get('what_is_ar') or '',
                                 phrase=br.get('source_phrase_ar') or '', nbs=nbs)
    return B


BR = cached('branches', _branches)
ROOT_BR = collections.defaultdict(list)       # root letters -> branch keys (union over homonymous root ids)
for _k, _b in BR.items():
    ROOT_BR[_b['root']].append(_k)
for _r in ROOT_BR:
    ROOT_BR[_r].sort(key=lambda k: (k[0], int(k[1][1:])))
RID_BR = collections.defaultdict(list)
for _k in BR:
    RID_BR[_k[0]].append(_k)
for _r in RID_BR:
    RID_BR[_r].sort(key=lambda k: int(k[1][1:]))

# neighbour relations, symmetric
REL = collections.defaultdict(dict)
for _k, _b in BR.items():
    for _k2, _t in _b['nbs']:
        if _k2 in BR:
            REL[_k][_k2] = _t
            REL[_k2].setdefault(_k, _t)


# ------------------------------------------------------------------ lemma / surface form index (whole word, clitic stripped)
def _forms():
    lemroot = collections.defaultdict(set)     # normalized form -> roots
    formlem = collections.defaultdict(set)     # normalized form -> single-root lemmas
    for r in csv.DictReader(open(f'{V15}/lemmas.tsv', encoding='utf-8'), delimiter='\t'):
        for f in {norm(r['lemma']), norm(r['lemma'].replace('ٰ', 'ا'))}:
            f = f[2:] if f.startswith('ال') else f
            if len(f) >= 3:
                lemroot[f].add(nroot(r['root']))
                formlem[f].add(r['lemma'])
    for w in WORDS:
        if len(w['roots']) != 1:
            continue
        for f in {norm(w['surface']), norm(w['surface'].replace('ٰ', 'ا'))}:
            forms = {f}
            g = re.sub('^(وال|فال|بال|كال|لل|ال)', '', f)
            if len(g) >= 3:
                forms.add(g)
            h = re.sub('^(و|ف)', '', f)
            if len(h) >= 4:
                forms.add(h)
            for x in forms:
                if len(x) >= 3:
                    lemroot[x].add(w['roots'][0])
                    if w['lemma'] and '|' not in w['lemma']:
                        formlem[x].add(w['lemma'])
    return dict(lemroot), dict(formlem)


LEMF, FORMLEM = cached('forms', _forms)
TOK = re.compile('[ء-ي]+')
PREFIXES = ('وال', 'فال', 'بال', 'كال', 'لل', 'ال', 'و', 'ف', 'ب', 'ل', 'ك')
SUFS = ('ها', 'هم', 'هن', 'كم', 'نا', 'ه', 'ك')


def _tiers(tok):
    pre = [tok[len(p):] for p in PREFIXES if tok.startswith(p) and len(tok) - len(p) >= 3]
    return [[tok], [tok[:-len(x)] for x in SUFS if tok.endswith(x) and len(tok) - len(x) >= 3], pre,
            [c[:-len(x)] for c in pre for x in SUFS if c.endswith(x) and len(c) - len(x) >= 3]]


def token_roots(tok):
    """roots whose Quranic lemma/surface equals the token; the least-stripped matching spelling wins"""
    for tier in _tiers(tok):
        out = set()
        for c in tier:
            out |= LEMF.get(c, set())
        if out:
            return out
    return set()


def token_lemma(tok):
    """the single Quranic lemma the token spells (least-stripped first), else None"""
    for tier in _tiers(tok):
        lems = set()
        for c in tier:
            lems |= FORMLEM.get(c, set())
        if lems:
            return next(iter(lems)) if len(lems) == 1 else None
    return None


STOP_TOK = {norm(x) for x in '''من في على إلى عن أي هو هي الذي التي إذا كل ما لا أو ثم به له بها لها يقال سمي ذلك شيء أصل يدل
واحد معروف اسم أيضا قال وهو وهي كان بعض فهو فلان جمع قيل يقول أنه أن كما حتى مثل غير بين قبل عند هذا هذه ذو ذات لم قد لأن
الواحد يسمى تقول العرب أمر كذا عنه منه فعل يفعل مصدر يكون صار يستعمل يذكر يؤنث كأنه تعني ناس قوم قول لما منسوب إذ إلا
إنما وقد فيه فيها منها عليه إليه وكل يعني أراد معنى كثير قليل حين حيث وقت نحو دون سواء أبو فيما مما عما بما كلما
هم هن وهم وهن فهم فهن أنا نحن أنت أنتم أنتن إياه تلك ذا ذي هؤلاء أولئك الذين اللذان اللتان اللاتي أحد كلها كله بعضهم بعضها
وذلك وكذلك كذلك ذاك إذ إذن لكن لكنه بل ليس ليست لن لو لولا أما إما حيثما متى أين كيف لدى لدن'''.split()}
# generic dictionary vocabulary: words that appear in definitions as scaffolding (used only to MEASURE noise)
GENERIC_TOK = {norm(x) for x in '''الشيء شيء الناس الأمر أمر النفس نفس الحق حق جاء خلاف غيره بينهما بينهم الرجل رجل الإنسان
الأرض يوم عمل قول كلام موضع مكان حال أهل ذات'''.split()}


def is_stop(t):
    return t in STOP_TOK or (t[:1] in 'وف' and t[1:] in STOP_TOK)


def clean_phrase(ph):
    return re.sub(r'\([a-z;_ ]+\)', ' ', ph or '')


# ------------------------------------------------------------------ what each card names (roots and lemmas), per field
def _card_names():
    """key -> dict(roots={root: [(field, token)]}, lemmas={lemma: (field, token)}) from image / what_is / phrase.
    Whole-word, clitic-stripped matches only; function words skipped; the card's own root skipped."""
    out = {}
    for k, b in BR.items():
        roots = collections.defaultdict(list)
        lemmas = {}
        for field, txt in (('image', b['image']), ('what', b['what']), ('phrase', clean_phrase(b['phrase']))):
            for t in TOK.findall(norm(txt)):
                if is_stop(t):
                    continue
                for r in token_roots(t):
                    if r != b['root']:
                        roots[r].append((field, t))
                L = token_lemma(t)
                if L and LEM_ROOT.get(L) and LEM_ROOT[L] != b['root']:
                    lemmas.setdefault(L, (field, t))
        out[k] = dict(roots=dict(roots), lemmas=lemmas)
    return out


NAMES = cached('card_names', _card_names)
CARD_DF = collections.Counter(r for v in NAMES.values() for r in v['roots'])   # how many cards name a root


# ------------------------------------------------------------------ HFT surprise set
def hft_cases():
    """unique (ayah, rid, bid) targets with the union of their HFT activator roots"""
    d = json.load(open(HFT))['all']
    g = collections.OrderedDict()
    for c in d:
        s, a = map(int, c['ayah'].split(':'))
        key = (s, a, c['rid'], c['branch'])
        e = g.setdefault(key, dict(s=s, a=a, rid=c['rid'], bid=c['branch'], root=nroot(c['root']), acts=set(),
                                   widx=set(), n_raw=0))
        e['acts'] |= {nroot(x[0]) for x in c['activators']}
        e['widx'] |= {int(x) for x in (c.get('widx') or [])}
        e['n_raw'] += 1
    out = []
    for e in g.values():
        e['acts'] = sorted(e['acts'] - {e['root']})
        e['widx'] = sorted(e['widx'])
        if e['acts']:
            out.append(e)
    return out


def load_early_texts(rid):
    """{source: entry_text_clean} for the six early sources only"""
    p = f'{PACK}/{rid}.json'
    if not os.path.exists(p):
        return {}
    d = json.load(open(p))
    out = {}
    for s in d.get('dictionary_sources', []):
        sid = s.get('source_id')
        t = s.get('entry_text_clean') or ''
        if sid in EARLY and t and t != '-':
            out[sid] = out.get(sid, '') + ('\n' if sid in out else '') + t
    return out
