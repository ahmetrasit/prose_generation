"""Candidate typed link types, as PATH EXISTENCE between a dictionary branch T (key (rid, bid)) and a word's root r in
ayah X.  Each type function returns None (no path) or a short "element" (what the path goes through, used only to
measure noise).  Every type is script-only and read-only.

Scope of each type (what it can discriminate):
  branch->root   : depends on T itself (can tell branches of one root apart)
  root->root     : depends on T only through its root (lift against 'another branch of the same root' is 1 by
                   construction)
  branch-only    : depends on T and X but not on the partner word (lift against 'another word of the ayah' is 1)
"""
import math, collections, csv, pickle, os, sys, random
import numpy as np
sys.dont_write_bytecode = True
import lib

EXCL_ROOTS = {'ء ل ه'}          # the divine name is never a pointer target (as in C1)

# ------------------------------------------------------------------ definitional pointer
NM_ANY, NM_PHRASE, NM_IMGWHAT, NM_TOK = {}, {}, {}, {}
for k, v in lib.NAMES.items():
    NM_ANY[k] = set(v['roots']) - EXCL_ROOTS
    NM_PHRASE[k] = {r for r, occ in v['roots'].items() if any(f == 'phrase' for f, _ in occ)} - EXCL_ROOTS
    NM_IMGWHAT[k] = {r for r, occ in v['roots'].items() if any(f in ('image', 'what') for f, _ in occ)} - EXCL_ROOTS
    NM_TOK[k] = {r: occ[0][1] for r, occ in v['roots'].items()}
NM_LEM = {k: {L for L in v['lemmas']} for k, v in lib.NAMES.items()}


def _ptr(T, r, cap=None, fields='any', cardcap=None):
    s = {'any': NM_ANY, 'phrase': NM_PHRASE, 'imgwhat': NM_IMGWHAT}[fields].get(T, ())
    if r not in s:
        return None
    if cap is not None and lib.ROOT_DF.get(r, 0) > cap:
        return None
    if cardcap is not None and lib.CARD_DF.get(r, 0) > cardcap:
        return None
    return NM_TOK[T].get(r, r)


def _ptr_phrase_only(T, r, cap=None):
    if r in NM_PHRASE.get(T, ()) and r not in NM_IMGWHAT.get(T, ()):
        if cap is None or lib.ROOT_DF.get(r, 0) <= cap:
            return NM_TOK[T].get(r, r)
    return None


def _ptr_rev(T, r, cap=None):
    """some branch of the partner root names T's root (root->root)"""
    rt = lib.BR[T]['root']
    if rt in EXCL_ROOTS or (cap is not None and lib.ROOT_DF.get(rt, 0) > cap):
        return None
    for b in lib.ROOT_BR.get(r, ()):
        if rt in NM_ANY.get(b, ()):
            return NM_TOK[b].get(rt, rt)
    return None


AY_LEMS = {k: collections.defaultdict(set) for k in lib.BY_AYAH}
for w in lib.WORDS:
    for rr in w['roots']:
        if w['lemma']:
            AY_LEMS[(w['s'], w['a'])][rr].add(w['lemma'])


def _ptr_lemma(T, r, X):
    """T's card spells the exact lemma of the partner word in this ayah"""
    hit = NM_LEM.get(T, set()) & AY_LEMS[X].get(r, set())
    return next(iter(hit)) if hit else None


# ------------------------------------------------------------------ rare-lemma bridge
_sig = {}


def lem_root_sig(L, r):
    """-log10 binomial tail that lemma L co-occurs with root r in >= k ayat (C1 metrics2 significance)"""
    key = (L, r)
    if key in _sig:
        return _sig[key]
    A, B = lib.LEM_AY.get(L, set()), lib.ROOT_AY.get(r, set())
    k = len(A & B); n = len(A); q = len(B) / lib.NAY
    if k == 0 or q >= 1:
        v = 0.0
    else:
        logs = [math.lgamma(n + 1) - math.lgamma(j + 1) - math.lgamma(n - j + 1) + j * math.log(q) + (n - j) * math.log(1 - q)
                for j in range(k, n + 1)]
        m = max(logs)
        v = max(0.0, -(m + math.log(sum(math.exp(x - m) for x in logs))) / math.log(10))
    _sig[key] = v
    return v


def _bridge(T, r, X, cap=30, sig=None, rev=False):
    """T's card names a rare lemma L (in <= cap ayat) that the Quran puts beside root r in another ayah.
    rev=True: a branch of r names a rare lemma that the Quran puts beside T's root (root->root)."""
    rt = lib.BR[T]['root']
    if not rev:
        srcs, other = [T], r
    else:
        srcs, other = lib.ROOT_BR.get(r, ()), rt
    for b in srcs:
        for L in NM_LEM.get(b, ()):
            if lib.LEM_DF.get(L, 0) > cap:
                continue
            lr = lib.LEM_ROOT.get(L)
            if lr in (rt, r) or lr in EXCL_ROOTS:
                continue
            wit = lib.LEM_AY[L] & lib.ROOT_AY.get(other, set())
            wit.discard(X)
            if not wit:
                continue
            if sig is not None and lem_root_sig(L, other) < sig:
                continue
            return L
    return None


def _bridge_supply(T, r, X, cap=30, root_cap=400, min_wit=2, min_share=0.5):
    """The rule the E0 supply ships (supply_config.json 'bridge'): T's card names a lemma L in at most cap ayat,
    partner root r in at most root_cap ayat, and the Quran puts L beside r in at least min_wit ayat and in at least
    min_share of L's ayat, the focus ayah X removed from both counts (review M3)."""
    rt = lib.BR[T]['root']
    if lib.ROOT_DF.get(r, 0) > root_cap:
        return None
    for L in NM_LEM.get(T, ()):
        n = lib.LEM_DF.get(L, 0)
        if n == 0 or n > cap:
            continue
        lr = lib.LEM_ROOT.get(L)
        if lr in (rt, r) or lr in EXCL_ROOTS:
            continue
        ayl = lib.LEM_AY[L] - {X}
        k = len(ayl & lib.ROOT_AY.get(r, set()))
        if ayl and k >= min_wit and k / len(ayl) >= min_share:
            return L
    return None


# ------------------------------------------------------------------ dictionary neighbour relation
CONTRAST = {'antonym', 'polarity_pair'}
SYN = {'near_synonym', 'synonym'}


def _nb(T, r, types=None):
    rel = lib.REL.get(T, {})
    for b in lib.ROOT_BR.get(r, ()):
        t = rel.get(b)
        if t and (types is None or t in types):
            return t
    return None


# ------------------------------------------------------------------ root co-occurrence (ayah, +-3 window), formula
SURAH_OF_POS = {}
W3_AY = collections.defaultdict(set)     # root -> ayat Z such that root occurs within +-3 ayat of Z (same surah)
for s, alist in lib.AYAT_OF.items():
    for a in alist:
        for b in alist:
            if abs(a - b) <= 3:
                for rr in lib.AY_ROOTS[(s, b)]:
                    W3_AY[rr].add((s, a))


def _local(X, k=3):
    s, a = X
    return {(s, b) for b in lib.AYAT_OF[s] if abs(b - a) <= k}


_pmi_c = {}


def pmi_ayah(rt, r, X):
    key = (rt, r, X)
    if key not in _pmi_c:
        A = lib.ROOT_AY.get(rt, set()); B = lib.ROOT_AY.get(r, set())
        nA = len(A) - (X in A); nB = len(B) - (X in B)
        c = len(A & B) - (X in A and X in B)
        n = lib.NAY - 1
        _pmi_c[key] = (math.log(c * n / (nA * nB)) if c > 0 and nA and nB else -9.0, c)
    return _pmi_c[key]


_pmi_w = {}


def pmi_win(rt, r, X):
    """rt in ayah Z and r within +-3 of Z, all Z outside +-3 of X"""
    key = (rt, r, X)
    if key not in _pmi_w:
        loc = _local(X)
        A = lib.ROOT_AY.get(rt, set()) - loc
        B = W3_AY.get(r, set()) - loc
        n = lib.NAY - len(loc)
        c = len(A & B)
        _pmi_w[key] = (math.log(c * n / (len(A) * len(B))) if c > 0 and A and B else -9.0, c)
    return _pmi_w[key]


def _cooc(T, r, X, kind='ayah', thr=1.0, cmin=2):
    rt = lib.BR[T]['root']
    v, c = (pmi_ayah if kind == 'ayah' else pmi_win)(rt, r, X)
    return f'pmi={v:.2f},c={c}' if (c >= cmin and v > thr) else None


def _formula(T, r, X, k=5, need_pmi=False):
    """the two roots meet in at most k ayat in the whole Quran, and at least once outside this ayah"""
    rt = lib.BR[T]['root']
    both = lib.ROOT_AY.get(rt, set()) & lib.ROOT_AY.get(r, set())
    n = len(both | {X})              # ayat where the pair meets, counting this one
    if n > k or len(both - {X}) < 1:
        return None
    if need_pmi and pmi_ayah(rt, r, X)[0] <= 0:
        return None
    return f'n={n}'


# ------------------------------------------------------------------ quran-slm fused similarity
import json as _json
CAT = _json.load(open(f'{lib.SLM}/artifacts/corpus_network/catalog.json'))['cards']
NCARD = len(CAT)
GI = {(c['source_root_id'], c['branch_id']): c['global_index'] for c in CAT}


def _mm(p):
    return np.memmap(p, dtype='<u2', mode='r', shape=(NCARD, NCARD))


E5 = _mm(f'{lib.SLM}/artifacts/corpus_network/e5_directional_rank.u16le')
CH = _mm(f'{lib.SLM}/artifacts/corpus_network/character_directional_rank.u16le')
NEO = _mm(f'{lib.SLM}/artifacts/corpus_ensemble/neoarabert_directional_rank.u16le')


def _rrf(R, a, b):
    ra, rb = float(R[a, b]), float(R[b, a])
    if ra == 0 or rb == 0:
        return 0.0
    return 0.5 * (1 / (10 + ra) + 1 / (10 + rb))


_fz = {}


def fused(a, b):
    k = (a, b) if a < b else (b, a)
    if k not in _fz:
        _fz[k] = 0.35 * _rrf(E5, a, b) + 0.35 * _rrf(NEO, a, b) + 0.3 * _rrf(CH, a, b)
    return _fz[k]


def _floor(q):
    p = os.path.join(lib.CACHE, 'slm_floor.pkl')
    if os.path.exists(p):
        F = pickle.load(open(p, 'rb'))
    else:
        rnd = random.Random(5); v = []
        roots = [c['surface_root_key'] for c in CAT]
        while len(v) < 20000:
            a, b = rnd.randrange(NCARD), rnd.randrange(NCARD)
            if roots[a] != roots[b]:
                v.append(fused(a, b))
        v.sort()
        F = {x: v[int(x / 100 * len(v))] for x in (90, 95, 99)}
        pickle.dump(F, open(p, 'wb'))
    return F[q]


SLM_P99 = _floor(99)
SLM_P95 = _floor(95)


def _slm_best(T, r):
    a = GI.get(T)
    if a is None:
        return None, None
    best, bb = -1.0, None
    for b in lib.ROOT_BR.get(r, ()):
        j = GI.get(b)
        if j is None:
            continue
        v = fused(a, j)
        if v > best:
            best, bb = v, b
    return (best, bb) if bb else (None, None)


_pr = {}


def _slm_pair(T, r, top=10):
    """T's best partner branch of r ranks within the top pairs of (branches of T's root) x (branches of r)"""
    best, bb = _slm_best(T, r)
    if best is None:
        return None
    key = (T[0], r)
    if key not in _pr:
        vals = []
        for t2 in lib.RID_BR[T[0]]:
            a = GI.get(t2)
            if a is None:
                continue
            for b in lib.ROOT_BR.get(r, ()):
                j = GI.get(b)
                if j is not None:
                    vals.append(fused(a, j))
        vals.sort(reverse=True)
        _pr[key] = vals
    vals = _pr[key]
    rank = sum(1 for x in vals if x > best) + 1
    return f'{bb[1]} rank {rank}/{len(vals)}' if rank <= top else None


def _slm_floor(T, r, q=99):
    best, bb = _slm_best(T, r)
    if best is None:
        return None
    return f'{bb[1]}' if best >= (SLM_P99 if q == 99 else SLM_P95) else None


# ------------------------------------------------------------------ Qnet keyword overlap
def _qnet():
    kw = collections.defaultdict(set)
    for row in csv.DictReader(open(lib.QNET, encoding='utf-8'), delimiter='\t'):
        kw[(row['root_id'], row['branch_id'])].add((row['keyword'], row['keyword_type']))
    return dict(kw)


QKW = lib.cached('qnet_kw', _qnet)
QDF = collections.Counter(w for v in QKW.values() for w in {x for x, _ in v})


def _qnet_ov(T, r, maxdf=None, core=False):
    mine = QKW.get(T, set())
    if core:
        mine = {x for x in mine if x[1] == 'core'}
    words = {w for w, _ in mine if maxdf is None or QDF[w] <= maxdf}
    if not words:
        return None
    for b in lib.ROOT_BR.get(r, ()):
        other = QKW.get(b, set())
        if core:
            other = {x for x in other if x[1] == 'core'}
        sh = words & {w for w, _ in other}
        if sh:
            return min(sh, key=lambda w: QDF[w])
    return None


# ------------------------------------------------------------------ early-source co-citation
COC = [c for c in pickle.load(open(os.path.join(lib.CACHE, 'cocite.pkl'), 'rb')) if c['verified']]
CC_ROOT = collections.defaultdict(set)          # rid -> ayat cited anywhere in its early entries
CC_BR = collections.defaultdict(set)            # (rid, bid) -> ayat cited under that branch
CC_QROOT = collections.defaultdict(set)         # (rid, X) -> roots of the quoted words of X
CC_QROOT_BR = collections.defaultdict(set)      # (rid, bid, X) -> roots of the quoted words of X
for c in COC:
    X = c['ayah']
    CC_ROOT[c['rid']].add(X)
    qr = set()
    for j in c['qpos'] or []:
        if j < len(lib.BY_AYAH[X]):
            qr |= set(lib.BY_AYAH[X][j]['roots'])
    CC_QROOT[(c['rid'], X)] |= qr
    if c['bid']:
        CC_BR[(c['rid'], c['bid'])].add(X)
        CC_QROOT_BR[(c['rid'], c['bid'], X)] |= qr


def _cc_here(T, r, X, branch=True):
    s = CC_BR.get(T, ()) if branch else CC_ROOT.get(T[0], ())
    return 'cited' if X in s else None


def _cc_quote(T, r, X, branch=False):
    s = CC_QROOT_BR.get((T[0], T[1], X), ()) if branch else CC_QROOT.get((T[0], X), ())
    return 'quoted' if r in s else None


def _cc_else(T, r, X, branch=True):
    s = CC_BR.get(T, ()) if branch else CC_ROOT.get(T[0], ())
    for Y in s:
        if Y != X and r in lib.AY_ROOTS.get(Y, ()):
            return f'{Y[0]}:{Y[1]}'
    return None


# ------------------------------------------------------------------ registry
# name: (family, scope, function(T, r, X))
TYPES = collections.OrderedDict()


def reg(name, family, scope, fn):
    TYPES[name] = (family, scope, fn)


reg('ptr', 'pointer', 'branch->root', lambda T, r, X: _ptr(T, r))
reg('ptr_card400', 'pointer', 'branch->root', lambda T, r, X: _ptr(T, r, cardcap=400))
reg('ptr_df1000', 'pointer', 'branch->root', lambda T, r, X: _ptr(T, r, cap=1000))
reg('ptr_df300', 'pointer', 'branch->root', lambda T, r, X: _ptr(T, r, cap=300))
reg('ptr_df100', 'pointer', 'branch->root', lambda T, r, X: _ptr(T, r, cap=100))
reg('ptr_df30', 'pointer', 'branch->root', lambda T, r, X: _ptr(T, r, cap=30))
reg('ptr_imgwhat', 'pointer', 'branch->root', lambda T, r, X: _ptr(T, r, fields='imgwhat'))
reg('ptr_imgwhat_df300', 'pointer', 'branch->root', lambda T, r, X: _ptr(T, r, cap=300, fields='imgwhat'))
reg('ptr_phrase', 'pointer', 'branch->root', lambda T, r, X: _ptr(T, r, fields='phrase'))
reg('ptr_phrase_only', 'pointer', 'branch->root', lambda T, r, X: _ptr_phrase_only(T, r))
reg('ptr_phrase_only_df300', 'pointer', 'branch->root', lambda T, r, X: _ptr_phrase_only(T, r, cap=300))
reg('ptr_lemma', 'pointer', 'branch->root', lambda T, r, X: _ptr_lemma(T, r, X))
reg('ptr_rev', 'pointer', 'root->root', lambda T, r, X: _ptr_rev(T, r))
reg('ptr_rev_df300', 'pointer', 'root->root', lambda T, r, X: _ptr_rev(T, r, cap=300))
reg('bridge30', 'bridge', 'branch->root', lambda T, r, X: _bridge(T, r, X, cap=30))
reg('bridge100', 'bridge', 'branch->root', lambda T, r, X: _bridge(T, r, X, cap=100))
reg('bridge30_sig2', 'bridge', 'branch->root', lambda T, r, X: _bridge(T, r, X, cap=30, sig=2.0))
reg('bridge100_sig2', 'bridge', 'branch->root', lambda T, r, X: _bridge(T, r, X, cap=100, sig=2.0))
reg('bridge30_rev', 'bridge', 'root->root', lambda T, r, X: _bridge(T, r, X, cap=30, rev=True))
reg('bridge_supply', 'bridge', 'branch->root', lambda T, r, X: _bridge_supply(T, r, X))
reg('nb_any', 'neighbour', 'branch->root', lambda T, r, X: _nb(T, r))
reg('nb_synonym', 'neighbour', 'branch->root', lambda T, r, X: _nb(T, r, SYN))
reg('nb_near_neighbor', 'neighbour', 'branch->root', lambda T, r, X: _nb(T, r, {'near_neighbor'}))
reg('nb_same_field', 'neighbour', 'branch->root', lambda T, r, X: _nb(T, r, {'same_field'}))
reg('nb_thematic', 'neighbour', 'branch->root', lambda T, r, X: _nb(T, r, {'thematic', 'other'}))
reg('nb_contrast', 'contrast', 'branch->root', lambda T, r, X: _nb(T, r, CONTRAST))
reg('cooc_ayah_pmi0', 'cooccurrence', 'root->root', lambda T, r, X: _cooc(T, r, X, 'ayah', 0.0))
reg('cooc_ayah_pmi1', 'cooccurrence', 'root->root', lambda T, r, X: _cooc(T, r, X, 'ayah', 1.0))
reg('cooc_ayah_pmi2', 'cooccurrence', 'root->root', lambda T, r, X: _cooc(T, r, X, 'ayah', 2.0))
reg('cooc_win3_pmi0', 'cooccurrence', 'root->root', lambda T, r, X: _cooc(T, r, X, 'win', 0.0))
reg('cooc_win3_pmi1', 'cooccurrence', 'root->root', lambda T, r, X: _cooc(T, r, X, 'win', 1.0))
reg('cooc_win3_pmi2', 'cooccurrence', 'root->root', lambda T, r, X: _cooc(T, r, X, 'win', 2.0))
reg('formula_k3', 'formula', 'root->root', lambda T, r, X: _formula(T, r, X, 3))
reg('formula_k5', 'formula', 'root->root', lambda T, r, X: _formula(T, r, X, 5))
reg('formula_k10', 'formula', 'root->root', lambda T, r, X: _formula(T, r, X, 10))
reg('formula_k5_pmi', 'formula', 'root->root', lambda T, r, X: _formula(T, r, X, 5, need_pmi=True))
reg('slm_pair10', 'similarity', 'branch->root', lambda T, r, X: _slm_pair(T, r, 10))
reg('slm_pair3', 'similarity', 'branch->root', lambda T, r, X: _slm_pair(T, r, 3))
reg('slm_p99', 'similarity', 'branch->root', lambda T, r, X: _slm_floor(T, r, 99))
reg('slm_p95', 'similarity', 'branch->root', lambda T, r, X: _slm_floor(T, r, 95))
reg('qnet_any', 'qnet', 'branch->root', lambda T, r, X: _qnet_ov(T, r))
reg('qnet_df50', 'qnet', 'branch->root', lambda T, r, X: _qnet_ov(T, r, maxdf=50))
reg('qnet_df200', 'qnet', 'branch->root', lambda T, r, X: _qnet_ov(T, r, maxdf=200))
reg('qnet_core', 'qnet', 'branch->root', lambda T, r, X: _qnet_ov(T, r, core=True))
reg('qnet_core_df50', 'qnet', 'branch->root', lambda T, r, X: _qnet_ov(T, r, maxdf=50, core=True))
reg('cc_here_branch', 'cocitation', 'branch-only', lambda T, r, X: _cc_here(T, r, X, True))
reg('cc_here_root', 'cocitation', 'root-only', lambda T, r, X: _cc_here(T, r, X, False))
reg('cc_quote_root', 'cocitation', 'root->root', lambda T, r, X: _cc_quote(T, r, X, False))
reg('cc_quote_branch', 'cocitation', 'branch->root', lambda T, r, X: _cc_quote(T, r, X, True))
reg('cc_else_branch', 'cocitation', 'branch->root', lambda T, r, X: _cc_else(T, r, X, True))
reg('cc_else_root', 'cocitation', 'root->root', lambda T, r, X: _cc_else(T, r, X, False))
