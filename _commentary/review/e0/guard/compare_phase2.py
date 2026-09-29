"""Score the Phase 2 construction heuristics on exactly the same label rows as the new detector (eval_dossier.py):
  A  = A-v5-step s03 cue (verbatim copy inside X-dilution-critic/k6_guards_vs_dossier.py, a_cue)
  B  = B-noniterative construction.licensed_v2
  C2 = C2-loaded-parallels construction.present(signature, occ_context, 'R5')
The prototype code and caches live in the Phase 2 scratchpad; this script only imports and calls them.
A heuristic that has no verdict for a branch (not in its branch table) counts as 'absent' (as in Phase 2).
Writes compare_phase2.json.
"""
import sys, os, json, collections, importlib
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SP = ('/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/'
      'scratchpad/phase2')
sys.path.insert(0, HERE)
import gdata as G
import eval_dossier as E


def load_A_B():
    cwd = os.getcwd()
    os.chdir(SP + '/X-dilution-critic')
    ns = {}
    src = open('k6_guards_vs_dossier.py').read().split('cnt=collections.Counter()')[0]
    exec(compile(src, 'k6_head', 'exec'), ns)
    os.chdir(cwd)
    return ns


def load_C2():
    cwd = os.getcwd()
    d = SP + '/C2-loaded-parallels'
    os.chdir(d)
    sys.path.insert(0, d)
    for m in ('common', 'construction'):
        sys.modules.pop(m, None)
    C = importlib.import_module('common')
    K = importlib.import_module('construction')
    br = C.trcache()['br']
    r2i, i2r = C.root_ids()
    os.chdir(cwd)
    sys.path.remove(d)
    return C, K, br, i2r


def main():
    res_new, rows = E.run(names=('all', 'excl_gram', 'main', 'dev', 'test'))
    ns = load_A_B()
    C, K, br, i2r = load_C2()
    sigcache, ctxcache = {}, {}

    def verdict_A(occ, ref):
        if ref not in ns['BI']:
            return 'absent'
        ay = ':'.join(occ.split(':')[:2])
        return 'present' if ns['a_cue'](ref, ay) == 'present' else 'absent'

    def verdict_B(occ, ref):
        rid, bn = ref.split('/')
        row = ns['BROW'].get((rid, bn))
        try:
            return 'present' if (row and ns['BC'].licensed_v2(occ, row)) else 'absent'
        except Exception:
            return 'absent'

    def verdict_C2(occ, ref):
        info = br.get(ref)
        root = i2r.get(ref.split('/')[0])
        if not info or not root:
            return 'absent'
        if ref not in sigcache:
            sigcache[ref] = K.signature(root, info)
        if (occ, root) not in ctxcache:
            ctxcache[(occ, root)] = K.occ_context(occ, root)
        ok, _ = K.present(sigcache[ref], ctxcache[(occ, root)], 'R5')
        return 'present' if ok else 'absent'

    B = G.dictionary()['branches']
    out = {'new_detector': res_new}
    for name, fn in (('A', verdict_A), ('B', verdict_B), ('C2', verdict_C2)):
        cwd = os.getcwd()
        os.chdir(SP + ('/C2-loaded-parallels' if name == 'C2' else '/X-dilution-critic'))
        vs = [fn(r['occ'], r['branch']) for r in rows]
        os.chdir(cwd)
        out[name] = {}
        for sub in ('all', 'excl_gram', 'main', 'dev', 'test'):
            T = [v for r, v in zip(rows, vs) if r['kind'] == 'true' and E.subset(r['branch'], sub)]
            if sub in ('dev', 'test'):
                O = [v for r, v in zip(rows, vs) if r['kind'] == 'other' and E.subset(r['placed'], sub)]
            else:
                O = [v for r, v in zip(rows, vs) if r['kind'] == 'other' and
                     (E.subset(r['placed'], sub) if B[r['placed']]['kind'] == 'collocation' else True)]
            out[name][sub] = dict(true_placements=len(T), recall_present=round(T.count('present') / len(T), 3),
                                  missed=round(1 - T.count('present') / len(T), 3), other=len(O),
                                  false_activation_present=round(O.count('present') / len(O), 4))
    json.dump(out, open(os.path.join(HERE, 'compare_phase2.json'), 'w'), ensure_ascii=False, indent=1)
    for sub in ('all', 'excl_gram', 'main', 'dev', 'test'):
        n = res_new[sub]
        print(f"{sub:9s} n={n['true_placements']:4d}  NEW recall {n['recall_present']:.3f} absent {n['false_absent']:.3f} "
              f"unknown {n['unknown']:.3f} FA {n['false_activation_present']:.4f} | " +
              ' | '.join(f"{h} recall {out[h][sub]['recall_present']:.3f} FA {out[h][sub]['false_activation_present']:.4f}"
                         for h in ('A', 'B', 'C2')))


if __name__ == '__main__':
    main()
