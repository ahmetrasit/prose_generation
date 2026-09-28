"""Shared read-only loaders for the C1 branch-distance experiments (Phase 2).
All sources are read-only; caches go to this scratch directory only.

Reconstructed 2026-09-28 from the compiled earlier version of this module (common_prev.cpython-314.pyc.bak,
disassembly in old/dis_common.txt) after the source was overwritten; same API, plus STOP_TOK (used by metrics.sound).
"""
import csv, json, glob, re, os, math, pickle, collections, sqlite3, sys
import numpy as np
sys.dont_write_bytecode = True
csv.field_size_limit(1000000000)

P = '/Volumes/OZTURK/_projects'
SLM = f'{P}/quran-slm'
V15 = f'{P}/prose_generation/_commentary/v15/data'
QD = f'{P}/quran-data/data'
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'cache')
os.makedirs(CACHE, exist_ok=True)

DIAC = re.compile('[ؐ-ًؚ-ٰٟۖ-ۭـ]')


def norm(t):
    t = DIAC.sub('', t or '')
    t = re.sub('[أإآٱ]', 'ا', t)
    return t.replace('ى', 'ي').replace('ة', 'ه').replace('ؤ', 'و').replace('ئ', 'ي')


def nroot(r):
    r = (r or '').strip()
    return re.sub('[أإآؤئ]', 'ء', r)


def cached(name, fn):
    p = os.path.join(CACHE, name + '.pkl')
    if os.path.exists(p):
        return pickle.load(open(p, 'rb'))
    v = fn()
    pickle.dump(v, open(p, 'wb'))
    return v


# ------------------------------------------------------------------ catalog (quran-slm Quran cards)
CAT = json.load(open(f'{SLM}/artifacts/corpus_network/catalog.json'))['cards']
N = len(CAT)
GI = {(c['source_root_id'], c['branch_id']): c['global_index'] for c in CAT}
NODE = {c['node_id']: c['global_index'] for c in CAT}
ROOTKEY = [nroot(c['surface_root_key']) for c in CAT]
RID = [c['source_root_id'] for c in CAT]
BID = [c['branch_id'] for c in CAT]
BNUM = [int(c['branch_id'][1:]) for c in CAT]
DISP = [f'{ROOTKEY[i]} {BID[i]}' for i in range(N)]
BY_ROOT = collections.defaultdict(list)
for c in CAT:
    BY_ROOT[nroot(c['surface_root_key'])].append(c['global_index'])
BY_RID = collections.defaultdict(list)
for c in CAT:
    BY_RID[c['source_root_id']].append(c['global_index'])


def _mm(p):
    return np.memmap(p, dtype='<u2', mode='r', shape=(N, N))


E5 = _mm(f'{SLM}/artifacts/corpus_network/e5_directional_rank.u16le')
CH = _mm(f'{SLM}/artifacts/corpus_network/character_directional_rank.u16le')
NEO = _mm(f'{SLM}/artifacts/corpus_ensemble/neoarabert_directional_rank.u16le')


def rrf(R, a, b):
    ra, rb = float(R[a, b]), float(R[b, a])
    if ra == 0 or rb == 0:
        return 0.0
    return 0.5 * (1 / (10 + ra) + 1 / (10 + rb))


def s_fused(a, b): return 0.35 * rrf(E5, a, b) + 0.35 * rrf(NEO, a, b) + 0.3 * rrf(CH, a, b)
def s_neo(a, b): return rrf(NEO, a, b)
def s_char(a, b): return rrf(CH, a, b)
def s_e5(a, b): return rrf(E5, a, b)


# ------------------------------------------------------------------ card texts
def _texts():
    out = {}
    for r in csv.DictReader(open(f'{SLM}/resources/source/corpus_branches_ar.tsv', encoding='utf-8'), delimiter='\t'):
        if r['node_id'] not in NODE:
            continue
        out[NODE[r['node_id']]] = (r['branch_image_ar'] or '', r['what_is_ar'] or '', r['source_phrase_ar'] or '')
    return out


TEXT = cached('texts', _texts)


# ------------------------------------------------------------------ Turkish dictionary: branch_kind, neighbours, aligned occurrences
def _dict():
    kind, nb, what_not = {}, collections.defaultdict(list), {}
    occ = {}
    for f in glob.glob(f'{QD}/dictionary/tr/root_*_entry.json'):
        d = json.load(open(f))
        for br in d.get('branches', []):
            m = re.match(r'(root_\d+)/(B\d+)', br.get('branch_ref', ''))
            if not m:
                continue
            key = (m.group(1), m.group(2))
            kind[key] = (br.get('lexicalization_scope') or {}).get('branch_kind')
            for nd in br.get('neighbor_distinctions') or []:
                m2 = re.match(r'(root_\d+)/(B\d+)', nd.get('neighbor_ref', ''))
                if not m2:
                    continue
                nb[key].append(((m2.group(1), m2.group(2)), nd.get('relation_type')))
        for o in (d.get('occurrence_evidence') or {}).get('occurrences', []):
            al = o.get('alignment') or {}
            ats = [(a.get('relation'), a.get('focus_role'), norm(a.get('prep_base') or '').replace('ـ', ''),
                    nroot(a.get('other_root')), a.get('other_surface') or '')
                   for a in (al.get('attachments') or [])]
            occ.setdefault(o['qac_word_ref'], {})[re.search(r'(root_\d+)', os.path.basename(f)).group(1)] = dict(
                status=al.get('status'), lemma=o.get('lemma_ar'), stem=o.get('stem_ar'), pos=o.get('pos'), ats=ats)
    return kind, dict(nb), occ


KIND, NB, OCC = cached('dict', _dict)


def kind_of(i):
    return KIND.get((RID[i], BID[i]))


# ------------------------------------------------------------------ Quran words (v15 words.tsv: QAC words with gateway roots)
def _words():
    W = list(csv.DictReader(open(f'{V15}/words.tsv', encoding='utf-8'), delimiter='\t'))
    out = []
    for w in W:
        roots = [nroot(r) for r in w['roots'].split('|') if r.strip()]
        out.append(dict(s=int(w['surah']), a=int(w['ayah']), w=int(w['w']), ref=w['ref'], surface=w['surface'],
                        roots=roots, lemma=w['lemmas'], pos=w['pos']))
    return out


WORDS = cached('words', _words)
BY_AYAH = collections.defaultdict(list)
for w in WORDS:
    BY_AYAH[(w['s'], w['a'])].append(w)
AYAT_OF = collections.defaultdict(list)
for s, a in sorted(BY_AYAH):
    AYAT_OF[s].append(a)


def window(s, a, k):
    return [(s, x) for x in AYAT_OF[s] if abs(x - a) <= k]


# ------------------------------------------------------------------ lexicon: normalized Quranic lemma/surface forms -> roots
def _lemforms():
    lem = collections.defaultdict(set)
    for r in csv.DictReader(open(f'{V15}/lemmas.tsv', encoding='utf-8'), delimiter='\t'):
        for f in {norm(r['lemma']), norm(r['lemma'].replace('ٰ', 'ا'))}:
            if f.startswith('ال'):
                f = f[2:]
            if len(f) >= 3:
                lem[f].add(nroot(r['root']))
    for w in WORDS:
        if len(w['roots']) != 1:
            continue
        for f in {norm(w['surface']), norm(w['surface'].replace('ٰ', 'ا'))}:
            forms = {f}
            g = re.sub('^(وال|فال|بال|كال|لل|ال)', '', f)
            if len(g) >= 3:
                forms.add(g)                     # article-type prefix stripped
            h = re.sub('^(و|ف)', '', f)
            if len(h) >= 4:
                forms.add(h)                     # a lone conjunction stripped only when four letters remain
            for x in forms:
                if len(x) >= 3:
                    lem[x].add(w['roots'][0])
    return dict(lem)


LEMF = cached('lemforms', _lemforms)
TOK = re.compile('[ء-ي]+')
PREFIXES = ('وال', 'فال', 'بال', 'كال', 'لل', 'ال', 'و', 'ف', 'ب', 'ل', 'ك')


def token_roots(tok):
    """roots whose Quranic lemma/surface equals the token; the LEAST-stripped spelling that matches wins
    (بعيده is بعيد + ه, not ب + عيد + ه); returns set"""
    sufs = ('ها', 'هم', 'هن', 'كم', 'نا', 'ه', 'ك')
    pre = [tok[len(p):] for p in PREFIXES if tok.startswith(p) and len(tok) - len(p) >= 3]
    tiers = [[tok],
             [tok[:-len(x)] for x in sufs if tok.endswith(x) and len(tok) - len(x) >= 3],
             pre,
             [c[:-len(x)] for c in pre for x in sufs if c.endswith(x) and len(c) - len(x) >= 3]]
    for tier in tiers:
        out = set()
        for c in tier:
            out |= LEMF.get(c, set())
        if out:
            return out
    return set()


# function words a paronomasia check must skip (normalized forms)
STOP_TOK = {norm(x) for x in '''من في على إلى عن أي هو هي الذي التي إذا كل ما لا أو ثم به له بها لها يقال سمي ذلك شيء أصل يدل
واحد معروف اسم أيضا قال وهو وهي كان بعض فهو فلان جمع قيل يقول أنه أن كما حتى مثل غير بين قبل عند هذا هذه ذو ذات لم قد لأن
الواحد يسمى تقول العرب أمر كذا عنه منه فعل يفعل مصدر يكون صار يستعمل يذكر يؤنث كأنه تعني ناس قوم قول لما منسوب إذ إلا
إنما وقد فيه فيها منها عليه إليه وكل يعني أراد معنى كثير قليل حين حيث وقت نحو دون سواء أبو فيما مما عما بما كلما
هم هن وهم وهن فهم فهن أنا نحن أنت أنتم أنتن إياه تلك ذا ذي هؤلاء أولئك الذين اللذان اللتان اللاتي أحد كلها كله بعضهم بعضها
وذلك وكذلك كذلك ذاك إذ إذن لكن لكنه بل ليس ليست لن لو لولا أما إما حيثما متى أين كيف لدى لدن'''.split()}



def _mentions():
    """card -> {root: [(field, token)]}: tokens in the card's image / definition / phrases that equal a Quranic lemma of another root"""
    M = {}
    for i, (img, wi, ph) in TEXT.items():
        d = collections.defaultdict(list)
        for field, txt in (('image', img), ('def', wi), ('phrase', re.sub(r'\([a-z;_ ]+\)', ' ', ph))):
            for t in TOK.findall(norm(txt)):
                if t in STOP_TOK or (t[:1] in 'وف' and t[1:] in STOP_TOK):
                    continue                     # function words (وفي is 'and in', not a form of و ف ي)
                for r in token_roots(t):
                    if r != ROOTKEY[i]:
                        d[r].append((field, t))
        M[i] = dict(d)
    return M


MENT = cached('mentions', _mentions)
MDF = collections.Counter(r for v in MENT.values() for r in v)
STOP_DF = 400


def ment(i):
    return {r: v for r, v in MENT.get(i, {}).items() if MDF[r] <= STOP_DF and r not in ('ء ل ه',)}


# ------------------------------------------------------------------ v15 Luna scene tags
def _tags():
    k2i = collections.defaultdict(list)
    for c in CAT:
        k2i[f"{nroot(c['surface_root_key'])} {c['branch_id']}"].append(c['global_index'])
    tags = collections.defaultdict(set)
    for f in glob.glob(f'{V15}/frames/out/*.json'):
        for it in json.load(open(f))['items']:
            key = it['key'].split()
            k = nroot(' '.join(key[:-1])) + ' ' + key[-1]
            for i in k2i.get(k, []):
                for fr in it['frames']:
                    tags[i].add((fr['frame'], fr['role']))
    return dict(tags)


TAGS = cached('tags', _tags)


def rank_of(scores, target):
    v = scores[target]
    better = sum(1 for x in scores.values() if x > v)
    ties = sum(1 for x in scores.values() if x == v) - 1
    return better + 1 + ties / 2
