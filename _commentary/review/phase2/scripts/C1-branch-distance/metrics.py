"""Candidate branch-pair proximities (all script-only, read-only data).
Each metric m(a, b) -> float (higher = closer); `explain(a, b)` returns the typed paths.
  slm_fused / slm_neo / slm_char / slm_e5 : current quran-slm ranks (reference)
  clause_max  (M3) : max cosine over micro-motifs (image, definition clauses, classical phrase units), E5-small vectors
                     computed by quran-slm in July (artifacts/s1_ar3_v1/embeddings), mapped back by clause_map.py
  mention_shared (M4): IDF-weighted Quranic roots named by BOTH cards (shared component: water, eye, road ...)
  xref (M4): card a names a Quranic lexeme of b's root, or b names a's (definitional cross-reference)
  dict_rel : the dictionary's own neighbour_distinctions (typed: near_synonym, antonym, polarity_pair ...)
  scene_other / scene_same (M2): Luna scene tags, same scene with a different / the same role, IDF-weighted
  bridge (new): a root named by card a co-occurs in some ayah with b's root (PMI); the witness ayah is the path
  sound : paronomasia -- a token in card a whose consonants match b's root with one radical changed or permuted
"""
import numpy as np, json, math, collections, re, sys, os
sys.dont_write_bytecode = True
import common as C

# ---------------- M3 micro-motif vectors ----------------
def _motifs():
    cm = json.load(open(os.path.join(C.HERE, 'clause_map.json')))
    E = C.SLM + '/artifacts/s1_ar3_v1/embeddings/'
    cl = np.load(E + 'what_is_ar_clauses.passage.cdf675821d0ac88aae7a.npz')['embeddings']
    su = np.load(E + 'source_phrase_ar_units.passage.5a178a5098c0b51a2d97.npz')['embeddings']
    im = np.load(E + 'branch_image_ar.image.ffe0f6f77dd986a86b6f.npz')['embeddings']
    order = [json.loads(l)['node_id'] for l in open(C.SLM + '/artifacts/s1_ar3_v1/nodes/global_nodes.jsonl')]
    rows = collections.defaultdict(list); texts = collections.defaultdict(list)
    for k, n in enumerate(order):
        if n in C.NODE: rows[C.NODE[n]].append(im[k]); texts[C.NODE[n]].append('img')
    for k, n in enumerate(cm['clause_owner']):
        if n in C.NODE: rows[C.NODE[n]].append(cl[k]); texts[C.NODE[n]].append(cm['clause_text'][k])
    for k, n in enumerate(cm['unit_owner']):
        if n in C.NODE: rows[C.NODE[n]].append(su[k]); texts[C.NODE[n]].append(cm['unit_text'][k])
    card = np.load(C.SLM + '/artifacts/corpus_network/e5_embeddings.npy')
    M, T = {}, {}
    for i in range(C.N):
        if rows.get(i):
            M[i] = np.vstack(rows[i]).astype(np.float32); T[i] = texts[i]
        else:
            M[i] = card[i:i + 1].astype(np.float32); T[i] = ['card']
    return M, T
MOT, MOTT = C.cached('motifs', _motifs)
# Clause cosines of E5 cluster high (0.75-0.95); centre by the corpus mean motif to sharpen
_allm = np.vstack([MOT[i] for i in range(C.N)])
MU = _allm.mean(0)
MOTC = {}
for i in range(C.N):
    x = MOT[i] - MU
    MOTC[i] = x / np.maximum(np.linalg.norm(x, axis=1, keepdims=True), 1e-6)
del _allm

def clause_max(a, b):
    if C.ROOTKEY[a] == C.ROOTKEY[b]: return 0.0
    return float((MOTC[a] @ MOTC[b].T).max())
def clause_top2(a, b):
    if C.ROOTKEY[a] == C.ROOTKEY[b]: return 0.0
    s = np.sort((MOTC[a] @ MOTC[b].T).ravel())[::-1]
    return float(s[:2].mean())
def clause_explain(a, b):
    S = MOTC[a] @ MOTC[b].T
    k = np.unravel_index(S.argmax(), S.shape)
    return f"clause {MOTT[a][k[0]][:40]} ~ {MOTT[b][k[1]][:40]} ({S[k]:.2f})"

# ---------------- M4 mentions ----------------
NCARD = C.N
def idf(r): return math.log(NCARD / (1 + C.MDF[r]))
MENTS = {i: C.ment(i) for i in range(C.N)}
def mention_shared(a, b):
    sh = set(MENTS[a]) & set(MENTS[b]) - {C.ROOTKEY[a], C.ROOTKEY[b]}
    return sum(idf(r) for r in sh)
def xref(a, b):
    """a's card names b's root or b's card names a's root"""
    return (1.0 if C.ROOTKEY[b] in MENTS[a] else 0.0) + (1.0 if C.ROOTKEY[a] in MENTS[b] else 0.0)
def mention_explain(a, b):
    out = []
    for r in set(MENTS[a]) & set(MENTS[b]) - {C.ROOTKEY[a], C.ROOTKEY[b]}:
        out.append(f"both name {MENTS[a][r][0][1]} ({r})")
    if C.ROOTKEY[b] in MENTS[a]: out.append(f"{C.DISP[a]} names «{MENTS[a][C.ROOTKEY[b]][0][1]}»")
    if C.ROOTKEY[a] in MENTS[b]: out.append(f"{C.DISP[b]} names «{MENTS[b][C.ROOTKEY[a]][0][1]}»")
    return '; '.join(out)

# ---------------- dictionary neighbour relations ----------------
REL = collections.defaultdict(dict)
for (k, lst) in C.NB.items():
    a = C.GI.get(k)
    if a is None: continue
    for k2, t in lst:
        b = C.GI.get(k2)
        if b is None: continue
        REL[a][b] = t; REL[b].setdefault(a, t)
RELW = {'antonym': 1.0, 'polarity_pair': 1.0, 'near_synonym': 0.8, 'synonym': 0.8, 'near_neighbor': 0.7, 'same_field': 0.6, 'thematic': 0.6, 'other': 0.4}
def dict_rel(a, b):
    t = REL.get(a, {}).get(b)
    return RELW.get(t, 0.5) if t else 0.0
def dict_contrast(a, b):
    return 1.0 if REL.get(a, {}).get(b) in ('antonym', 'polarity_pair') else 0.0

# ---------------- M2 Luna scenes ----------------
def scene_key(fr):
    # added scenes ('new:...'/'new....') are merged to their domain + first word so near-duplicates meet
    if fr.startswith('new'):
        x = re.sub(r'^new[:.]', '', fr)
        parts = re.split(r'[._:-]', x)
        return 'new.' + '.'.join(parts[:2])
    return fr
TAGK = {i: {(scene_key(f), r) for f, r in v} for i, v in C.TAGS.items()}
SDF = collections.Counter(s for v in TAGK.values() for s in {f for f, r in v})
def sidf(s): return math.log(C.N / (1 + SDF[s]))
ABSTRACT = ('moral.', 'divine.')
def scene_other(a, b):
    ta, tb = TAGK.get(a, set()), TAGK.get(b, set())
    sa = {f for f, r in ta}; sb = {f for f, r in tb}
    tot = 0.0
    for s in sa & sb:
        if s.startswith(ABSTRACT): continue
        ra = {r for f, r in ta if f == s}; rb = {r for f, r in tb if f == s}
        if ra != rb and not (ra & rb): tot += sidf(s)
    return tot / math.sqrt(max(1, len(sa)) * max(1, len(sb)))
def scene_same(a, b):
    ta, tb = TAGK.get(a, set()), TAGK.get(b, set())
    sh = {f for f, r in ta & tb if not f.startswith(ABSTRACT)}
    return sum(sidf(s) for s in sh) / math.sqrt(max(1, len(ta)) * max(1, len(tb)))
def scene_explain(a, b):
    ta, tb = TAGK.get(a, set()), TAGK.get(b, set())
    out = []
    for s in {f for f, r in ta} & {f for f, r in tb}:
        out.append(f"{s}: {'/'.join(sorted(r for f, r in ta if f == s))} + {'/'.join(sorted(r for f, r in tb if f == s))}")
    return '; '.join(out[:3])

# ---------------- bridge: named root co-occurs with b's root in an ayah ----------------
AY_ROOTS = {k: {r for w in ws for r in w['roots']} for k, ws in C.BY_AYAH.items()}
ROOT_AY = collections.defaultdict(set)
for k, rs in AY_ROOTS.items():
    for r in rs: ROOT_AY[r].add(k)
NAY = len(AY_ROOTS)
def pmi(r1, r2):
    A, B = ROOT_AY.get(r1, set()), ROOT_AY.get(r2, set())
    if not A or not B: return 0.0, None
    inter = A & B
    if not inter: return 0.0, None
    v = math.log(len(inter) * NAY / (len(A) * len(B)))
    return max(0.0, v), min(inter)
def bridge(a, b):
    """max over roots m named by a (not b's root) of PMI(m, root(b)) -- the Quran puts a's named object next to b's word"""
    rb = C.ROOTKEY[b]; best = 0.0
    for m in MENTS[a]:
        if m == rb or m == C.ROOTKEY[a]: continue
        v, _ = pmi(m, rb)
        best = max(best, v)
    return best
def bridge_explain(a, b):
    rb = C.ROOTKEY[b]; best = (0, None, None)
    for m in MENTS[a]:
        if m == rb: continue
        v, ay = pmi(m, rb)
        if v > best[0]: best = (v, m, ay)
    if not best[1]: return ''
    return f"{C.DISP[a]} names «{MENTS[a][best[1]][0][1]}» ({best[1]}), which the Quran puts beside {rb} in {best[2][0]}:{best[2][1]}"

# ---------------- sound echo (paronomasia) ----------------
ROOTSET = set(C.BY_ROOT)
def skeleton(tok):
    t = re.sub(r'^(وال|فال|بال|كال|لل|ال)', '', tok)
    return [c for c in t if c not in 'اويىةه']
def sound(a, b):
    """a token of card a (image/definition) shares b's two outer radicals in order with one change (e.g. شين ~ شيطان)"""
    rb = C.ROOTKEY[b].split()
    if len(rb) != 3 or rb[1] in 'اويء': return 0.0     # a weak middle radical makes every C-C token an 'echo'
    img, wi, _ = C.TEXT.get(a, ('', '', ''))
    rs = [c for c in rb if c not in 'اوي'] or rb
    for t in C.TOK.findall(C.norm(img)):
        if C.token_roots(t) or t in C.STOP_TOK: continue            # a real lemma: handled by mentions
        sk = skeleton(t)
        if len(sk) < 2: continue
        if sk[0] == rb[0] and sk[-1] == rb[-1] and len(sk) <= 3:
            return 1.0
    return 0.0

METRICS = dict(slm_fused=C.s_fused, slm_neo=C.s_neo, slm_char=C.s_char, slm_e5=C.s_e5,
               clause_max=clause_max, clause_top2=clause_top2, mention_shared=mention_shared, xref=xref,
               dict_rel=dict_rel, dict_contrast=dict_contrast, scene_other=scene_other, scene_same=scene_same,
               bridge=bridge, sound=sound)
EXPLAIN = dict(slm_fused=lambda a, b: f"similar cards (slm {C.s_fused(a, b):.3f})", clause_max=clause_explain,
               mention_shared=mention_explain, xref=mention_explain, dict_rel=lambda a, b: f"dictionary neighbour: {REL.get(a, {}).get(b)}",
               scene_other=scene_explain, scene_same=scene_explain, bridge=bridge_explain,
               sound=lambda a, b: f"sound echo between {C.DISP[a]} wording and {C.ROOTKEY[b]}")
