"""Script harvest for one ayah: the compact push file a synthesis call would read, plus the full pull table.
Order only, nothing filtered: every branch of every word is listed; neighbour activations are ordered by a typed
union and each carries its path; collocation-bound branches whose construction is absent are listed apart
(construction-scoped), never silently dropped.  Usage: python3 harvest.py 29:38 [29:38 ...]"""
import sys, os, json, collections, math
sys.dont_write_bytecode = True
import common as C, metrics as M, guard as G
OUT = os.path.join(C.HERE, 'harvest'); os.makedirs(OUT, exist_ok=True)
TYPES = ['mention_shared', 'xref', 'bridge', 'clause_max', 'slm_neo', 'scene_other', 'dict_rel', 'dict_contrast', 'sound']
LABEL = dict(mention_shared='shared component', xref='definition names the other word', bridge='Quran pairs them',
             clause_max='similar clause', slm_neo='similar card', scene_other='scene, other role', dict_rel='dictionary neighbour',
             dict_contrast='dictionary contrast', sound='sound echo')
# per-type floors: a type "fires" only above its floor (floors are the 90th percentile of that metric over random
# cross-root pairs, computed once below) -- this orders, it removes nothing from the pull table
def floors():
    import random
    random.seed(3); v = collections.defaultdict(list)
    for _ in range(4000):
        a, b = random.randrange(C.N), random.randrange(C.N)
        if C.ROOTKEY[a] == C.ROOTKEY[b]: continue
        for t in TYPES: v[t].append(M.METRICS[t](a, b))
    out = {}
    for t, xs in v.items():
        xs = sorted(xs); q = xs[int(0.9 * len(xs))]
        out[t] = max(q, 1e-9)
    return out
FL = C.cached('floors', floors)

def ayah_words(s, a): return [w for w in C.BY_AYAH[(s, a)] if w['roots']]

def na_table(s, a, window=3):
    """every (branch of a focus word) x (other word in the window) with each type's score; returns rows"""
    focus = ayah_words(s, a)
    ctx = [w for k in C.window(s, a, window) for w in ayah_words(*k)]
    rows = []
    for x in focus:
        rx = x['roots'][0]
        for c in C.BY_ROOT.get(rx, []):
            stc = G.status(c, x)[0]
            for y in ctx:
                if y['roots'][0] == rx: continue
                best = {}
                for yb in C.BY_ROOT.get(y['roots'][0], []):
                    for t in TYPES:
                        v = M.METRICS[t](c, yb)
                        if v > best.get(t, (0, None))[0]: best[t] = (v, yb)
                fired = {t: vb for t, vb in best.items() if vb[0] > FL[t] or (t in ('xref', 'dict_rel', 'dict_contrast', 'sound') and vb[0] > 0)}
                if fired:
                    rows.append(dict(x=x['ref'], c=c, status=stc, y=y['ref'], ysurf=y['surface'], same_ayah=(y['s'], y['a']) == (s, a),
                                     fired={t: (round(v / FL[t], 2), yb) for t, (v, yb) in fired.items()}))
    return rows

def xrefs_out(s, a, scope='quran'):
    """definition of a focus word's branch names a Quranic lexeme: where that lexeme occurs (same surah first)"""
    out = []
    for x in ayah_words(s, a):
        for c in C.BY_ROOT.get(x['roots'][0], []):
            for r, toks in M.MENTS[c].items():
                ays = sorted(M.ROOT_AY.get(r, ()))
                if not ays or len(ays) > 30: continue          # frequent roots: not a pointer (listed in pull)
                same = [k for k in ays if k[0] == s and k != (s, a)]
                out.append((x['ref'], c, r, toks[0][1], same, len(ays)))
    return out

def fmt(s, a):
    words = ayah_words(s, a)
    rows = na_table(s, a)
    lines = [f"# script harvest {s}:{a} (order only; nothing removed; full tables in {s:03d}_{a:03d}.pull.json)", '']
    lines.append('## words and all their branches (kind; construction where bound)')
    for w in words:
        bl = []
        for c in C.BY_ROOT.get(w['roots'][0], []):
            st, det = G.status(c, w)
            tag = '' if st == 'free' else {'present_strict': ' [construction present]', 'present_window': ' [construction nearby?]',
                                            'possible_prep_only': ' [construction?]', 'unknown': ' [bound; unverified]', 'absent': ' [bound: absent here]'}[st]
            bl.append(f"{C.BID[c]} {C.TEXT[c][0]}{tag}")
        lines.append(f"- {w['ref']} {w['surface']} ({w['roots'][0]}): " + ' · '.join(bl))
    lines.append('')
    lines.append('## neighbour activations (branch <- activating word: typed paths; strongest first; one line per branch)')
    STRONG = {'mention_shared', 'xref', 'bridge', 'scene_other', 'dict_rel', 'dict_contrast', 'sound'}
    best = {}
    for r in rows:
        if r['status'] == 'absent': continue
        types = set(r['fired'])
        n_strong = len(types & STRONG)
        if n_strong == 0: continue                       # similarity-only: pull table
        if not r['same_ayah'] and len(types) < 2: continue
        key = r['c']
        score = (r['same_ayah'], len(types), max(v for v, _ in r['fired'].values()))
        best.setdefault(key, []).append((score, r))
    per_word = collections.defaultdict(list)
    for c, lst in best.items():
        lst.sort(key=lambda x: x[0], reverse=True)
        per_word[lst[0][1]['x']].append((lst[0][0], lst[0][1], [x[1]['ysurf'] for x in lst[1:4]]))
    for w in words:
        lst = sorted(per_word.get(w['ref'], []), key=lambda x: x[0], reverse=True)
        if not lst: continue
        lines.append(f"### {w['ref']} {w['surface']}")
        for score, r, also in lst:
            paths = []
            for t, (v, yb) in sorted(r['fired'].items(), key=lambda kv: (kv[0] not in STRONG, -kv[1][0])):
                ex = M.EXPLAIN.get(t)
                p = ex(r['c'], yb) if ex and t in STRONG else ''
                paths.append(f"{LABEL[t]}: {p}" if p else LABEL[t])
            yb0 = next(iter(r['fired'].values()))[1]
            lines.append(f"- {C.BID[r['c']]} {C.TEXT[r['c']][0]} <- {r['ysurf']} {r['y']} ({C.DISP[yb0]}): " + ' | '.join(paths[:3])
                         + (f" (also: {', '.join(also)})" if also else ''))
    lines.append('')
    xo = xrefs_out(s, a)
    xs = [x for x in xo if x[4]]
    if xs:
        lines.append('## definitions that name a lexeme found elsewhere in the surah')
        for ref, c, r, tok, same, n in xs:
            lines.append(f"- {C.DISP[c]} {C.TEXT[c][0]} names «{tok}» ({r}): {', '.join(f'{k[0]}:{k[1]}' for k in same[:8])}{' ...' if len(same) > 8 else ''} ({n} ayat in the Quran)")
        lines.append('')
    blocked = [(w, c, G.status(c, w)[1]) for w in words for c in C.BY_ROOT.get(w['roots'][0], []) if G.status(c, w)[0] == 'absent']
    if blocked:
        lines.append('## construction-scoped branches (the sense belongs to a construction absent here; not activatable here)')
        lines.append('- ' + ' · '.join(f"{C.DISP[c]} «{C.TEXT[c][0]}» needs: {det.split(';')[0]}" for w, c, det in blocked))
    push = '\n'.join(lines) + '\n'
    pull = dict(na_rows=[dict(r, c=C.DISP[r['c']], fired={t: [v, C.DISP[yb]] for t, (v, yb) in r['fired'].items()}) for r in rows],
                xrefs=[(ref, C.DISP[c], r, tok, [f'{k[0]}:{k[1]}' for k in same], n) for ref, c, r, tok, same, n in xo])
    return push, pull

if __name__ == '__main__':
    sizes = {}
    for ref in sys.argv[1:]:
        s, a = map(int, ref.split(':'))
        push, pull = fmt(s, a)
        p1 = os.path.join(OUT, f'{s:03d}_{a:03d}.push.md'); p2 = os.path.join(OUT, f'{s:03d}_{a:03d}.pull.json')
        open(p1, 'w').write(push); json.dump(pull, open(p2, 'w'), ensure_ascii=False)
        sizes[ref] = dict(push_chars=len(push), push_bytes=len(push.encode()), pull_bytes=os.path.getsize(p2), na_rows=len(pull['na_rows']), xrefs=len(pull['xrefs']))
        print(ref, sizes[ref])
    json.dump(sizes, open(os.path.join(OUT, 'sizes.json'), 'w'), indent=1)
