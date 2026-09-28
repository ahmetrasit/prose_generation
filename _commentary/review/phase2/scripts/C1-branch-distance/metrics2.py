"""Second-generation typed proximities (script only), added on top of metrics.py.

  xref_idf     (M4, definitional cross-reference): card a names a Quranic lexeme of b's root (or b names a's root),
               weighted by the rarity of the named root in the Quran (log #ayat / #ayat with the root).  A rare named
               root (عنكبوت: 1 ayah) is a pointer; a frequent one (عين) is not.
  bridge_lemma (new, 'the Quran pairs them'): a LEMMA named by card a co-occurs in some ayah with b's root; PMI over
               ayat, lemma-level and only for forms that map to ONE Quranic lemma (so حمر 'red' is not read as حمير
               'donkeys'); the witness ayat are the explanatory path (غشاوة is beside أبصار in 2:7 and 45:23).
               Symmetric: max of both directions.
Every function returns a float (higher = closer); *_explain returns the path in words."""
import csv, collections, math, re, sys
sys.dont_write_bytecode = True
import common as C, metrics as M

NAY = len(C.BY_AYAH)
ROOT_AY = collections.defaultdict(set)
LEM_AY = collections.defaultdict(set)
LEM_ROOT = {}
for w in C.WORDS:
    for r in w['roots']:
        ROOT_AY[r].add((w['s'], w['a']))
    if len(w['roots']) == 1 and w['lemma'] and '|' not in w['lemma']:
        LEM_AY[w['lemma']].add((w['s'], w['a']))
        LEM_ROOT[w['lemma']] = w['roots'][0]

# normalized form -> lemmas (from lemma spellings and every surface spelling)
FORM_LEM = collections.defaultdict(set)
for r in csv.DictReader(open(f'{C.V15}/lemmas.tsv', encoding='utf-8'), delimiter='\t'):
    for f in {C.norm(r['lemma']), C.norm(r['lemma'].replace('ٰ', 'ا'))}:
        f = f[2:] if f.startswith('ال') else f
        if len(f) >= 3:
            FORM_LEM[f].add(r['lemma'])
for w in C.WORDS:
    if len(w['roots']) != 1 or not w['lemma'] or '|' in w['lemma']:
        continue
    for f in {C.norm(w['surface']), C.norm(w['surface'].replace('ٰ', 'ا'))}:
        forms = {f}
        g = re.sub('^(وال|فال|بال|كال|لل|ال)', '', f)
        if len(g) >= 3: forms.add(g)
        h = re.sub('^(و|ف)', '', f)
        if len(h) >= 4: forms.add(h)
        for x in forms:
            if len(x) >= 3: FORM_LEM[x].add(w['lemma'])


def token_lemma(t):
    """the single Quranic lemma a dictionary token spells; least-stripped spelling first; else None"""
    sufs = ('ها', 'هم', 'هن', 'كم', 'نا', 'ه', 'ك')
    pre = [t[len(p):] for p in C.PREFIXES if t.startswith(p) and len(t) - len(p) >= 3]
    tiers = [[t], [t[:-len(x)] for x in sufs if t.endswith(x) and len(t) - len(x) >= 3], pre,
             [c[:-len(x)] for c in pre for x in sufs if c.endswith(x) and len(c) - len(x) >= 3]]
    for tier in tiers:
        lems = set()
        for c in tier:
            lems |= FORM_LEM.get(c, set())
        if lems:
            return next(iter(lems)) if len(lems) == 1 else None
    return None


LEMMA_DF_MAX = 300      # a lemma in more ayat than this (كان, قال ...) is not a pointer


def _card_lemmas():
    out = {}
    for i, (img, wi, ph) in C.TEXT.items():
        d = {}
        for field, txt in (('image', img), ('def', wi), ('phrase', re.sub(r'\([a-z;_ ]+\)', ' ', ph))):
            for t in C.TOK.findall(C.norm(txt)):
                if t in C.STOP_TOK or (t[:1] in 'وف' and t[1:] in C.STOP_TOK):
                    continue
                L = token_lemma(t)
                if L and LEM_ROOT.get(L) and LEM_ROOT[L] != C.ROOTKEY[i] and LEM_ROOT[L] != 'ء ل ه' \
                        and len(LEM_AY.get(L, ())) <= LEMMA_DF_MAX:
                    d.setdefault(L, t)
        out[i] = d
    return out


CARD_LEM = C.cached('card_lemmas', _card_lemmas)


def root_idf(r):
    return math.log(NAY / max(1, len(ROOT_AY.get(r, ()))))


def xref_idf(a, b):
    ra, rb = C.ROOTKEY[a], C.ROOTKEY[b]
    v = 0.0
    if rb in M.MENTS[a]: v = max(v, root_idf(rb))
    if ra in M.MENTS[b]: v = max(v, root_idf(ra))
    return v


def _pmi_lem_root(L, r):
    """significance that lemma L co-occurs with root r in ayat more often than chance: -log10 of the binomial tail
    P(X >= k), X ~ Bin(#ayat of L, share of ayat with r).  One chance co-occurrence of a rare lemma scores low;
    غشاوة beside أبصار in both of its 2 ayat scores high.  (Named _pmi_ for history; it is not PMI.)"""
    A, B = LEM_AY.get(L, set()), ROOT_AY.get(r, set())
    inter = A & B
    if not inter: return 0.0, ()
    n, k, q = len(A), len(inter), len(B) / NAY
    if q >= 1: return 0.0, tuple(sorted(inter))
    logs = [math.lgamma(n + 1) - math.lgamma(j + 1) - math.lgamma(n - j + 1) + j * math.log(q) + (n - j) * math.log(1 - q) for j in range(k, n + 1)]
    m = max(logs)
    logp = m + math.log(sum(math.exp(x - m) for x in logs))
    return max(0.0, -logp / math.log(10)), tuple(sorted(inter))


def _bridge_dir(a, b):
    rb = C.ROOTKEY[b]; best = (0.0, None, ())
    for L, tok in CARD_LEM.get(a, {}).items():
        if LEM_ROOT.get(L) == rb:
            continue
        v, wit = _pmi_lem_root(L, rb)
        if v > best[0]: best = (v, L, wit)
    return best


_bcache = {}
def bridge_lemma(a, b):
    k = (a, b) if a < b else (b, a)
    if k not in _bcache:
        _bcache[k] = max(_bridge_dir(a, b)[0], _bridge_dir(b, a)[0])
        if len(_bcache) > 3_000_000: _bcache.clear()
    return _bcache[k]


def bridge_lemma_explain(a, b):
    x, y = _bridge_dir(a, b), _bridge_dir(b, a)
    if x[0] >= y[0] and x[1]:
        src, L, wit, other = a, x[1], x[2], C.ROOTKEY[b]
    elif y[1]:
        src, L, wit, other = b, y[1], y[2], C.ROOTKEY[a]
    else:
        return ''
    return (f"{C.DISP[src]} names «{CARD_LEM[src][L]}» ({L}), which the Quran puts beside {other} in "
            + ', '.join(f'{s}:{a_}' for s, a_ in wit[:4]) + (' ...' if len(wit) > 4 else ''))


def xref_idf_explain(a, b):
    ra, rb = C.ROOTKEY[a], C.ROOTKEY[b]
    out = []
    if rb in M.MENTS[a]: out.append(f"{C.DISP[a]} names «{M.MENTS[a][rb][0][1]}» ({rb}, {len(ROOT_AY.get(rb, ()))} ayat)")
    if ra in M.MENTS[b]: out.append(f"{C.DISP[b]} names «{M.MENTS[b][ra][0][1]}» ({ra}, {len(ROOT_AY.get(ra, ()))} ayat)")
    return '; '.join(out)


def bridge_dir(a, b):
    """directional: a's card names a lemma that the Quran puts beside b's ROOT (depends on b only through its root, so
    it activates a branch of X from a neighbouring word Y whatever Y's sense is)"""
    return _bridge_dir(a, b)[0]


def bridge_dir_explain(a, b):
    v, L, wit = _bridge_dir(a, b)
    if not L: return ''
    return (f"{C.DISP[a]} names «{CARD_LEM[a][L]}» ({L}), which the Quran puts beside {C.ROOTKEY[b]} in "
            + ', '.join(f'{s}:{a_}' for s, a_ in wit[:4]) + (' ...' if len(wit) > 4 else ''))


M.METRICS['bridge_dir'] = bridge_dir
M.EXPLAIN['bridge_dir'] = bridge_dir_explain
M.METRICS['xref_idf'] = xref_idf
M.METRICS['bridge_lemma'] = bridge_lemma
M.EXPLAIN['xref_idf'] = xref_idf_explain
M.EXPLAIN['bridge_lemma'] = bridge_lemma_explain

def _floors():
    """90th percentile of each metric over 4,000 random cross-root card pairs: a type 'fires' only above it"""
    import random
    random.seed(3); v = collections.defaultdict(list)
    names = ['slm_fused', 'slm_neo', 'clause_max', 'mention_shared', 'xref', 'xref_idf', 'bridge', 'bridge_lemma', 'bridge_dir', 'scene_other', 'scene_same', 'dict_rel', 'dict_contrast']
    for _ in range(4000):
        p, q = random.randrange(C.N), random.randrange(C.N)
        if C.ROOTKEY[p] == C.ROOTKEY[q]: continue
        for t in names: v[t].append(M.METRICS[t](p, q))
    return {t: sorted(xs)[int(0.9 * len(xs))] for t, xs in v.items()}


FLOORS = C.cached('floors_m2', _floors)


if __name__ == '__main__':
    sab = [i for i in C.BY_ROOT['س ب ل'] if C.BID[i] == 'B010'][0]
    print('eye-film lemmas named:', CARD_LEM[sab])
    for r in ('ب ص ر', 'ز ي ن', 'ع ن ك ب', 'و ه ن', 'ب ي ت'):
        bs = C.BY_ROOT[r]
        best = max(bs, key=lambda j: bridge_lemma(sab, j))
        print(r, 'bridge_lemma', round(bridge_lemma(sab, best), 2), bridge_lemma_explain(sab, best), '| xref_idf', round(max(xref_idf(sab, j) for j in bs), 2))
