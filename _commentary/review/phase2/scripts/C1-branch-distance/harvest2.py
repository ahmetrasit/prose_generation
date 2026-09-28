"""Script harvest v2: the compact per-ayah PUSH a synthesis call would read, and the complete PULL table.

Ordering only; nothing is removed.  Per content word, every branch of its root is scored by NEIGHBOUR ACTIVATION
(max over the other words of the ayah and of the +-3 window, over all their branches that are senses there) for each
path type; one ordered list per ayah by reciprocal-rank fusion of the types (union_rrf).  The push shows per word the
4 best branches plus any branch with a pointer-grade path (rare definitional cross-reference, a lemma the Quran pairs
with the activating word, a dictionary contrast), each with its activating word and its typed paths in words.
The dictionary guard is a label and an order, not a filter: a collocation-bound branch whose construction is absent
here is shown only on an 'echo' line (the phrase it belongs to), never as a sense of the word here.
Also: definitional pointers to other ayat (a branch names a rare Quranic lemma), same-root recurrence for rare roots,
and a construction-grouped concordance for mid-frequency roots (for loaded words).
Usage: python3 harvest2.py 29:38 1:6 ..."""
import sys, os, json, collections, math, re
sys.dont_write_bytecode = True
import numpy as np
import common as C, metrics as M, guard as G, metrics2 as M2

OUT = os.path.join(C.HERE, 'harvest2'); os.makedirs(OUT, exist_ok=True)
TYPES = ['slm_neo', 'clause_max', 'mention_shared', 'xref_idf', 'bridge_dir', 'scene_other', 'dict_rel', 'dict_contrast']
LABEL = dict(slm_neo='similar card', clause_max='similar clause', mention_shared='shared component', xref_idf='definition names the word',
             bridge_dir='Quran pairs them', scene_other='scene, other role', dict_rel='dictionary neighbour', dict_contrast='dictionary contrast')
WINDOW = 3
PUSH_K = 3
EXTRA_CONV = 5          # a branch outside the top 3 is still pushed with paths when >= 5 kinds converge on one word
ORDER = 'convergence'   # or 'union_floor' (reciprocal-rank fusion of floor-gated types)
CONV = {}
INNER = {}
BRIDGE_P99 = 4.66       # 99th percentile of bridge_dir over random cross-root pairs (measured)
POINTER_DF = 30          # a named lemma in at most this many ayat is a pointer
RARE_ROOT_DF = 12        # same-root recurrence listed in full for roots in at most this many ayat
CONC_ROOT_DF = 40        # construction-grouped concordance for roots in at most this many ayat
KIND_TAG = {'bare': 'bare', 'mixed_non_bare': 'mixed', 'non_bare': 'non-bare', 'collocation': 'coll', 'unresolved': 'unres.', None: '?'}


def ayah_words(s, a):
    return [w for w in C.BY_AYAH[(s, a)] if w['roots'] and w['roots'][0] in C.BY_ROOT]


_pm = {}
def pair_mat(t, rx, ry):
    k = (t, rx, ry)
    if k not in _pm:
        f = M.METRICS[t]
        _pm[k] = np.array([[f(a, b) for b in C.BY_ROOT[ry]] for a in C.BY_ROOT[rx]], dtype=np.float64)
    return _pm[k]


_st = {}
def status(i, w):
    k = (i, w['ref'])
    if k not in _st: _st[k] = G.status(i, w)
    return _st[k]


def harvest(s, a):
    focus = ayah_words(s, a)
    ctx = [w for k in C.window(s, a, WINDOW) for w in ayah_words(*k)]
    cands = []                       # (word, card)
    best = {}                        # (word ref, card) -> {type: (value, y card, y word)}
    for x in focus:
        rx = x['roots'][0]; cx = C.BY_ROOT[rx]
        for t in TYPES:
            bv = np.zeros(len(cx)); by = [None] * len(cx)
            for y in ctx:
                ry = y['roots'][0]
                if ry == rx or y['ref'] == x['ref']: continue
                ok = [j for j, yb in enumerate(C.BY_ROOT[ry]) if status(yb, y)[0] != 'absent']
                if not ok: continue
                if t == 'bridge_dir' and len(M2.ROOT_AY.get(ry, ())) > 400:
                    continue                     # a very frequent activator root (الله, أرض, يوم ...) pairs with everything
                m = pair_mat(t, rx, ry)[:, ok]
                # same-ayah activators count fully, window activators at 0.8 (order only)
                wgt = 1.0 if (y['s'], y['a']) == (s, a) else 0.8
                mv = m.max(axis=1) * wgt; am = m.argmax(axis=1)
                for j in range(len(cx)):
                    if mv[j] > bv[j]:
                        bv[j] = mv[j]; by[j] = (C.BY_ROOT[ry][ok[am[j]]], y)
            for j, c in enumerate(cx):
                best.setdefault((x['ref'], c), {})[t] = (bv[j], by[j])
        for c in cx: cands.append((x, c))
    # union_rrf over all candidates of the ayah
    u = collections.defaultdict(float)
    for t in TYPES:
        f = M2.FLOORS.get(t, 0.0)
        vals = sorted({best[(x['ref'], c)][t][0] for x, c in cands if best[(x['ref'], c)][t][0] > f}, reverse=True)
        pos = {v: k for k, v in enumerate(vals)}
        for x, c in cands:
            v = best[(x['ref'], c)][t][0]
            if v > f: u[(x['ref'], c)] += 1.0 / (2 + pos[v])
    for x, c in cands:                           # similarity breaks ties
        u[(x['ref'], c)] += 1e-3 * best[(x['ref'], c)]['slm_neo'][0]
    if ORDER == 'convergence':
        # convergence (conv_eval.py): the most independent path types (each above its random-pair 95th percentile)
        # tying the branch to ONE activating word; same-ayah activators first; similarity breaks ties
        F95 = C.cached('floors95', lambda: None)
        for x in focus:
            rx = x['roots'][0]; cx = C.BY_ROOT[rx]
            conv = np.zeros(len(cx)); act = [None] * len(cx)
            inner = np.zeros(len(cx)); iact = [None] * len(cx)
            for y in ctx:
                ry = y['roots'][0]
                if ry == rx or y['ref'] == x['ref']: continue
                ok = [j for j, yb in enumerate(C.BY_ROOT[ry]) if status(yb, y)[0] != 'absent']
                if not ok: continue
                cnt = np.zeros(len(cx))
                for t in TYPES:
                    if t == 'bridge_dir' and len(M2.ROOT_AY.get(ry, ())) > 400: continue
                    cnt += pair_mat(t, rx, ry)[:, ok].max(axis=1) > F95[t]
                cnt += 0.25 if (y['s'], y['a']) == (s, a) else 0.0
                same = (y['s'], y['a']) == (s, a)
                for j in range(len(cx)):
                    if cnt[j] > conv[j]: conv[j] = cnt[j]; act[j] = y
                    if same and cnt[j] > inner[j]: inner[j] = cnt[j]; iact[j] = y
            for j, c in enumerate(cx):
                CONV[(x['ref'], c)] = (int(conv[j]), act[j])
                INNER[(x['ref'], c)] = (int(inner[j]), iact[j])
                u[(x['ref'], c)] = conv[j] + 10 * best[(x['ref'], c)]['slm_neo'][0]
    return focus, cands, best, u


def pointer_paths(x, c, b):
    out = []
    v, yy = b['xref_idf']
    if v > 0 and yy:
        n = len(M2.ROOT_AY.get(C.ROOTKEY[yy[0]], ())) if C.ROOTKEY[yy[0]] in M.MENTS[c] else len(M2.ROOT_AY.get(C.ROOTKEY[c], ()))
        if n <= POINTER_DF // 3: out.append('xref_idf')
    v, yy = b['bridge_dir']
    if v >= BRIDGE_P99 and yy: out.append('bridge_dir')
    v, yy = b['dict_contrast']
    if v > 0 and yy: out.append('dict_contrast')
    return out


def short(t, c, yb, yw, s, a):
    """one compact path in words"""
    where = yw['surface'] + ('' if (yw['s'], yw['a']) == (s, a) else f" {yw['s']}:{yw['a']}")
    if t == 'xref_idf':
        r = C.ROOTKEY[yb]
        if r in M.MENTS[c]:
            return f"names «{M.MENTS[c][r][0][1]}» = {where} ({len(M2.ROOT_AY.get(r, ()))} ayat)"
        return f"{C.DISP[yb]} names this word ← {where}"
    if t == 'bridge_dir':
        v, L, wit = M2._bridge_dir(c, yb)
        return f"Quran pairs «{M2.CARD_LEM[c][L]}» with {where} ({', '.join(f'{x}:{y}' for x, y in wit[:3])}{'…' if len(wit) > 3 else ''})"
    if t == 'scene_other':
        ta, tb = M.TAGK.get(c, set()), M.TAGK.get(yb, set())
        sc = sorted({f for f, r in ta} & {f for f, r in tb})
        f = sc[0] if sc else '?'
        return f"scene {f}: {'/'.join(sorted(r for g, r in ta if g == f))} + {'/'.join(sorted(r for g, r in tb if g == f))} ← {where}"
    if t in ('dict_rel', 'dict_contrast'):
        return f"dictionary {M.REL.get(c, {}).get(yb)} of {C.DISP[yb]} ← {where}"
    if t == 'mention_shared':
        sh = sorted(set(M.MENTS[c]) & set(M.MENTS[yb]), key=lambda r: C.MDF[r])
        return f"both name «{M.MENTS[c][sh[0]][0][1]}» ← {where}" if sh else f"shared component ← {where}"
    return f"{LABEL[t]} {C.DISP[yb]} «{C.TEXT[yb][0][:24]}» ← {where}"


def act_paths(x, c, y, F95):
    """types above their 95th percentile between branch c of x and the senses of y, best first by priority"""
    rx, ry = x['roots'][0], y['roots'][0]
    j = C.BY_ROOT[rx].index(c)
    ok = [k for k, yb in enumerate(C.BY_ROOT[ry]) if status(yb, y)[0] != 'absent']
    out = []
    for t in TYPES:
        if t == 'bridge_dir' and len(M2.ROOT_AY.get(ry, ())) > 400: continue
        row = pair_mat(t, rx, ry)[j, ok]
        if len(row) and row.max() > F95[t]:
            out.append((t, C.BY_ROOT[ry][ok[int(row.argmax())]]))
    return out


PRIO = {'xref_idf': 0, 'bridge_dir': 1, 'dict_contrast': 2, 'scene_other': 3, 'dict_rel': 4, 'slm_neo': 5, 'clause_max': 6, 'mention_shared': 7}


def line_for(x, c, b, s, a):
    st, det = status(c, x)
    kind = KIND_TAG.get(C.kind_of(c), '?')
    nsrc = len(C.CAT[c].get('dictionary_source_families') or [])
    tag = kind + (' present' if st.startswith('present') else '') + ('; 1 src' if nsrc <= 1 else '')
    F95 = C.cached('floors95', lambda: None)
    k, act = CONV.get((x['ref'], c), (0, None))
    paths = []
    if act is not None and k >= 2:
        ap = sorted(act_paths(x, c, act, F95), key=lambda tb: PRIO[tb[0]])
        paths = [short(t, c, yb, act, s, a) for t, yb in ap if not (t == 'mention_shared' and M.METRICS[t](c, yb) < 5.0)][:2]
    ki, iact = INNER.get((x['ref'], c), (0, None))
    if iact is not None and ki >= 2 and (act is None or iact['ref'] != act['ref']):   # the best activator inside the ayah
        ap = sorted(act_paths(x, c, iact, F95), key=lambda tb: PRIO[tb[0]])
        ap = [short(t, c, yb, iact, s, a) for t, yb in ap if not (t == 'mention_shared' and M.METRICS[t](c, yb) < 5.0)][:1]
        if ap: paths.append(f"in the ayah, {ki} kinds: " + ap[0])
    for t in sorted(pointer_paths(x, c, b), key=lambda t: PRIO[t]):     # pointer-grade paths from any window word
        v, yy = b[t]
        if yy is not None and (act is None or yy[1]['ref'] != act['ref']):
            paths.append(short(t, c, yy[0], yy[1], s, a)); break
    head = f" {k} kinds ← {act['surface']}{'' if (act['s'], act['a']) == (s, a) else ' ' + str(act['s']) + ':' + str(act['a'])}:" if act is not None and k >= 2 else ''
    return f"  - {C.BID[c]} «{C.TEXT[c][0]}» [{tag}]{head} " + (' | '.join(paths) if paths else '')


def concordance(root):
    """Quranic occurrences of a root grouped by lemma + construction (relation, preposition, partner root)"""
    groups = collections.defaultdict(list)
    rids = {C.RID[i] for i in C.BY_ROOT[root]}
    for w in C.WORDS:
        if root not in w['roots']: continue
        o = C.OCC.get(w['ref'], {})
        ats = [at for r in rids for at in (o.get(r) or {}).get('ats', [])]
        parts = {f"{at[2] or at[0]}{(' ' + at[3]) if at[3] else ''}" for at in ats if at[1] == 'head' and at[0] in ('prep_complement', 'direct_object', 'idafa', 'adjective')}
        parts |= {f"after {at[2]}" for at in ats if at[1] != 'head' and at[0] == 'prep_complement' and at[2]}
        sig = ' + '.join(sorted(parts)) or '-'
        groups[(C.norm(w['lemma']), sig)].append(f"{w['s']}:{w['a']}")
    return groups


def fmt(s, a):
    focus, cands, best, u = harvest(s, a)
    L = [f"# {s}:{a} script harvest (order only; complete lists: {s:03d}_{a:03d}.pull.json)", '']
    pushed = set(); echoes = []
    for x in focus:
        cx = C.BY_ROOT[x['roots'][0]]
        live = [c for c in cx if status(c, x)[0] != 'absent']
        ranked = sorted(live, key=lambda c: -u.get((x['ref'], c), 0.0))
        top = ranked[:PUSH_K]
        extra = [c for c in ranked[PUSH_K:] if pointer_paths(x, c, best[(x['ref'], c)]) or CONV.get((x['ref'], c), (0, None))[0] >= EXTRA_CONV]
        L.append(f"## w{x['w']} {x['surface']} ({x['roots'][0]}; {len(cx)} branches)")
        for c in top + extra:
            L.append(line_for(x, c, best[(x['ref'], c)], s, a)); pushed.add((x['ref'], c))
        rest = [c for c in ranked if c not in top and c not in extra]
        if rest:                                  # every other live branch stays visible, in order, without paths
            L.append('  - then: ' + ' · '.join(f"{C.BID[c]} «{C.TEXT[c][0]}»" for c in rest))
        ab = [c for c in cx if status(c, x)[0] == 'absent']
        if ab:
            L.append('  - echo only (construction absent here): ' + ' · '.join(
                f"{C.BID[c]} «{C.TEXT[c][0]}» (phrase: {status(c, x)[1].split(';')[0]})" for c in ab))
    # pointers: a branch of a focus word names a rare Quranic lemma found elsewhere
    ptr = []
    for x in focus:
        for c in C.BY_ROOT[x['roots'][0]]:
            if status(c, x)[0] == 'absent': continue
            for Lm, tok in M2.CARD_LEM.get(c, {}).items():
                ays = sorted(M2.LEM_AY.get(Lm, ()))
                ays = [k for k in ays if k != (s, a)]
                same = [k for k in ays if k[0] == s]
                if 0 < len(ays) <= POINTER_DF // 3 and same:
                    ptr.append((len(ays), f"- {C.DISP[c]} names «{tok}» ({Lm}): " + ', '.join(f'{k[0]}:{k[1]}' for k in (same + [k for k in ays if k[0] != s])[:6])
                                + (' ...' if len(ays) > 6 else '') + (f"  [same surah: {len(same)}]" if same else '')))
    ptr.sort()
    if ptr:
        L += ['', '## pointers: a branch definition names a rare Quranic word that occurs elsewhere in this surah'] + [p for _, p in ptr[:12]]
        if len(ptr) > 12: L.append(f"- ... {len(ptr) - 12} more in the pull file")
    # same-root recurrence (rare roots) and construction-grouped concordance (mid-frequency roots)
    rec = []
    seen_r = set()
    for x in focus:
        r = x['roots'][0]; df = len(M2.ROOT_AY.get(r, ()))
        if r in seen_r: continue
        seen_r.add(r)
        if df <= CONC_ROOT_DF:
            g = concordance(r)
            parts = [f"{lem} [{sig}] ×{len(refs)}: {', '.join(refs[:5])}{' ...' if len(refs) > 5 else ''}" for (lem, sig), refs in sorted(g.items(), key=lambda kv: -len(kv[1]))]
            rec.append(f"- {r} ({df} ayat): " + ' ; '.join(parts))
    if rec:
        L += ['', f'## Quranic uses of the rarer roots here, grouped by lemma and construction (roots in <= {CONC_ROOT_DF} ayat)'] + rec
    push = '\n'.join(L) + '\n'
    pull = dict(ayah=f'{s}:{a}', window=WINDOW,
                rows=[dict(word=x['ref'], surface=x['surface'], card=C.DISP[c], image=C.TEXT[c][0], kind=C.kind_of(c),
                           guard=status(c, x)[0], union=round(u.get((x['ref'], c), 0.0), 4), pushed=(x['ref'], c) in pushed,
                           paths={t: [round(float(v), 4), C.DISP[yy[0]], yy[1]['ref']] for t, (v, yy) in best[(x['ref'], c)].items() if v > 0 and yy})
                      for x, c in cands],
                pointers=[p for _, p in ptr])
    return push, pull, pushed


if __name__ == '__main__':
    sizes = {}
    for ref in sys.argv[1:]:
        s, a = map(int, ref.split(':'))
        push, pull, pushed = fmt(s, a)
        p1 = os.path.join(OUT, f'{s:03d}_{a:03d}.push.md'); p2 = os.path.join(OUT, f'{s:03d}_{a:03d}.pull.json')
        open(p1, 'w').write(push); json.dump(pull, open(p2, 'w'), ensure_ascii=False)
        sizes[ref] = dict(push_chars=len(push), push_lines=push.count('\n'), pull_bytes=os.path.getsize(p2), candidates=len(pull['rows']), pushed=len(pushed),
                          est_push_tokens=int(len(push) / 2.2))
        print(ref, sizes[ref], flush=True)
    json.dump(sizes, open(os.path.join(OUT, 'sizes.json'), 'w'), indent=1)
