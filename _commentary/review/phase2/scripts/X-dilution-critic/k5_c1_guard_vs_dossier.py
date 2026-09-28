# K5: C1's construction guard (guard.status) scored against root-dossier plain branches, as C2 scored its own guard.
# A dossier 'dominant' row whose branch is collocation-bound = the construction is present by definition (true placement).
# C1 pushes 'absent' as "echo only (construction absent here)"; window/prep-only/unknown stay live.
import sys, os, csv, collections
sys.dont_write_bytecode = True
C1='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/C1-branch-distance'
sys.path.insert(0, C1); os.chdir(C1)
import common as C, guard as G
GRAM = {('root_001533','B012'), ('root_000502','B003')}   # C2's two grammatical constructions (nafs 'self', min duni)
W = {w['ref']: w for w in C.WORDS}
dos = []
for r in csv.DictReader(open(C.P + '/root-dossier/out/activation_map.tsv', encoding='utf-8'), delimiter='\t'):
    if r['role'] != 'dominant' or not r['branch_ref'].startswith('root_'): continue
    ref3 = ':'.join(r['qac_word_ref'].split(':')[:3])
    dos.append((ref3, r['branch_ref'].split('/')[0], r['branch_ref'].split('/')[1]))
cnt = collections.Counter(); ex = []
for ref3, rid, b in dos:
    w = W.get(ref3)
    if not w: continue
    for i in C.BY_RID.get(rid, []):
        if C.kind_of(i) != 'collocation': continue
        st, _ = G.status(i, w)
        true = (C.BID[i] == b)
        g = (rid, C.BID[i]) in GRAM
        for sub in (('all',) + (() if g else ('excl_gram',))):
            cnt[(sub, true, st)] += 1
        if true and st == 'absent' and not g and len(ex) < 10: ex.append((ref3, C.DISP[i], w['surface']))
for sub in ('all', 'excl_gram'):
    T = {st: v for (s, t, st), v in cnt.items() if s == sub and t}
    F = {st: v for (s, t, st), v in cnt.items() if s == sub and not t}
    nt = sum(T.values()); nf = sum(F.values())
    print(f"[{sub}] true placements {nt}: " + ', '.join(f"{k} {v} ({v/nt:.0%})" for k, v in sorted(T.items())))
    print(f"[{sub}] other-branch occurrences {nf}: " + ', '.join(f"{k} {v} ({v/nf:.1%})" for k, v in sorted(F.items())))
print('examples of true placements C1 marks echo-only (absent):')
for e in ex: print(' -', e)
