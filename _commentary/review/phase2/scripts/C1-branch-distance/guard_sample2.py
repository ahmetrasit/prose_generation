"""Risky 'absent' decisions: a signature root occurs somewhere in the same ayah (possible missed constructions)."""
import random, collections, sys
sys.dont_write_bytecode = True
import common as C, guard as G
random.seed(12)
risky = []; tot = 0
for w in C.WORDS:
    for r in w['roots']:
        for i in C.BY_ROOT.get(r, []):
            if C.kind_of(i) != 'collocation': continue
            st, det = G.status(i, w)
            if st != 'absent': continue
            tot += 1
            ayroots = {x for y in C.BY_AYAH[(w['s'], w['a'])] if y['ref'] != w['ref'] for x in y['roots']}
            sigroots = {x for _, _, sg in G.SIG.get((C.RID[i], C.BID[i]), []) for p, rs, t in sg['elems'] for x in rs}
            if sigroots & ayroots: risky.append((w, i, det))
print('absent total', tot, 'absent with a signature root elsewhere in the ayah', len(risky))
def ctx(w):
    ay = C.BY_AYAH[(w['s'], w['a'])]
    return ' '.join(('[' + x['surface'] + ']') if x['ref'] == w['ref'] else x['surface'] for x in ay if abs(x['w'] - w['w']) <= 6)
for w, i, det in random.sample(risky, 30):
    print(f"{w['ref']} {C.DISP[i]} «{C.TEXT[i][0]}» | {det} || {ctx(w)}")
