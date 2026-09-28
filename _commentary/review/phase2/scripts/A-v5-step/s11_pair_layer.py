# F7 candidate layer: all cross-word branch pairs inside one ayah ranked by quran-slm fused affinity
# (ordering only, never a filter). Reports rank of watch pairs among all pairs of the ayah.
import sys, os, collections
sys.argv=['x']; exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'s06_intra_ayah_coherence.py')).read().split("if __name__=='__main__':")[0])
import numpy as np
def pairs(ref, extra=()):
    roots=[r for r in dict.fromkeys(QRA[ref]) if r in by_rootkey]
    for e in extra:
        roots+= [r for r in dict.fromkeys(QRA[e]) if r in by_rootkey and r not in roots]
    P=[]
    for i,X in enumerate(roots):
        for Y in roots[i+1:]:
            A=by_rootkey[X]; Bb=by_rootkey[Y]; S=fused(A,Bb)
            for ia in range(len(A)):
                for ib in range(len(Bb)):
                    if S[ia,ib]>0: P.append((float(S[ia,ib]),lab[A[ia]],lab[Bb[ib]]))
    P.sort(reverse=True); return P
cases={'29:38':[('س ب ل B010','ص د د B013'),('س ب ل B010','ب ص ر B001'),('س ب ل B010','ز ي ن B002'),('ص د د B013','ز ي ن B002'),('ص د د B013','ب ص ر B001')],
       '1:7':[('ض ل ل B005','ن ع م B005')],
       '1:6':[('ق و م B012','ه د ي B008'),('ص ر ط B002','ه د ي B008')],
       '5:6':[('ر ف ق B004','ي د ي B001'),('ك ع ب B001','ر ج ل B001'),('ر ف ق B002','س ف ر B001')],
       '100:1':[('ع د و B002','ض ب ح B002')],
       '18:96':[('ن ف خ B001','ن و ر B002')]}
for ref,watch in cases.items():
    P=pairs(ref); idx={(a,b):k+1 for k,(s,a,b) in enumerate(P)}; idx.update({(b,a):k+1 for k,(s,a,b) in enumerate(P)})
    print(f'### {ref}: {len(P)} cross-word branch pairs')
    for w in watch: print('   ',w,'rank',idx.get(w))
    print('    top10:',' | '.join(f'{a}~{b}' for s,a,b in P[:10]))
