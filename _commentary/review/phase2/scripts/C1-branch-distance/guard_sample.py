"""Print a random sample of guard decisions (other roots than ḍaraba) for manual checking."""
import random, collections, sys
sys.dont_write_bytecode = True
import common as C, guard as G
random.seed(11)
by = collections.defaultdict(list)
for w in C.WORDS:
    for r in w['roots']:
        if r == 'ض ر ب': continue
        for i in C.BY_ROOT.get(r, []):
            if C.kind_of(i) == 'collocation':
                st, det = G.status(i, w)
                by[st].append((w, i, det))
def ctx(w):
    ay = C.BY_AYAH[(w['s'], w['a'])]
    return ' '.join(('[' + x['surface'] + ']') if x['ref'] == w['ref'] else x['surface'] for x in ay if abs(x['w'] - w['w']) <= 5)
for st, n in (('present_strict', 30), ('present_window', 15), ('absent', 25)):
    print('=====', st, len(by[st]))
    for w, i, det in random.sample(by[st], n):
        print(f"{w['ref']} {C.DISP[i]} «{C.TEXT[i][0]}» | {det} || {ctx(w)}")
