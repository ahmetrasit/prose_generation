"""Frame state v2: a collocation-bound branch whose lexical construction is not detected (C2 R5) is 'frame-present'
when a GRAMMATICAL partner of the occurrence (dictionary occurrence_evidence attachments: other_root) is a root the
branch's own definition / early phrase names. Generic; no case rules. Read-only."""
import sys,os,csv,collections,re,json,glob,pickle
sys.dont_write_bytecode=True
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
exec(open(os.path.join(HERE,'frame_rule.py')).read().split('# 1) named loci')[0].replace("W=int(sys.argv[1]) if len(sys.argv)>1 else 4","W=0"))
AP=os.path.join(HERE,'attach.pkl')
if os.path.exists(AP): ATT=pickle.load(open(AP,'rb'))
else:
    ATT=collections.defaultdict(set)
    for f in glob.glob('/Volumes/OZTURK/_projects/quran-data/data/dictionary/tr/*_entry.json'):
        try: d=json.load(open(f))
        except: continue
        for o in (d.get('occurrence_evidence') or {}).get('occurrences',[]):
            al=o.get('alignment') or {}
            for at in al.get('attachments',[]) or []:
                r=C.nroot(at.get('other_root') or '')
                if r: ATT[o['qac_word_ref']].add(r)
    ATT=dict(ATT); pickle.dump(ATT,open(AP,'wb'))
def frame2(ref3,bref):
    if bref not in NR: NR[bref]=named_roots(B[bref])
    return sorted(ATT.get(ref3,set()) & NR[bref])
idx=collections.defaultdict(list)
for r in rows:
    s,a,w=r['ref3'].split(':'); idx[f'{s}:{a}'].append(r)
for ay in ['100:1','4:34','1:4','1:6','1:7','1:5','1:2','29:38','18:96','5:6']:
    for r in idx[ay]:
        b=B[r['branch']]
        st='lexical' if r['present']=='1' else ('FRAME '+','.join(frame2(r['ref3'],r['branch'])) if frame2(r['ref3'],r['branch']) else 'absent')
        if st=='absent' and ay not in ('100:1','4:34','1:4','1:6','1:7'): continue
        if ay=='4:34' and b['root']!='ض ر ب': continue
        print(ay,r['ref3'],b['root'],b['bid'],(b['image'] or '')[:40],'->',st)
dos={}
for r in csv.DictReader(open('/Volumes/OZTURK/_projects/root-dossier/out/activation_map.tsv'),delimiter='\t'):
    if r['role']=='dominant': dos[r['qac_word_ref']]=r['branch_ref']
droots={B[v]['root'] for v in dos.values() if v in B}
tp=fn=fp=tn=tpF=fpF=0; exfp=[]; extp=[]
allF=0; allN=0
for r in rows:
    lex=r['present']=='1'
    if not lex:
        allN+=1
        if frame2(r['ref3'],r['branch']): allF+=1
    d=dos.get(r['ref3'])
    if not d or not d.startswith('root_'): continue
    if B.get(d,{}).get('root')!=B[r['branch']]['root']: continue
    fr=(not lex) and bool(frame2(r['ref3'],r['branch']))
    if d==r['branch']:
        tp+=lex; fn+=(not lex); tpF+=fr
        if fr: extp.append((r['ref3'],B[r['branch']]['root'],B[r['branch']]['bid'],frame2(r['ref3'],r['branch'])))
    else:
        fp+=lex; tn+=(not lex); fpF+=fr
        if fr: exfp.append((r['ref3'],B[r['branch']]['root'],B[r['branch']]['bid'],frame2(r['ref3'],r['branch'])))
print(f'dossier lexical: recall={tp/max(1,tp+fn):.3f} FAR={fp/max(1,fp+tn):.4f} (tp {tp} fn {fn} fp {fp} tn {tn})')
print(f'+frame2: recall={(tp+tpF)/max(1,tp+fn):.3f} FAR={(fp+fpF)/max(1,fp+tn):.4f} (adds tp {tpF}, fp {fpF}); whole Quran: {allF} of {allN} not-detected pairs flip to frame')
print('tp ex',extp[:8]); print('fp ex',exfp[:8])
