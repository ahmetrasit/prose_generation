import json,collections,csv,re,sys
exec(open('k6_guards_vs_dossier.py').read().split("BROW=")[0])
rows=[r for r in csv.DictReader(open('/Volumes/OZTURK/_projects/root-dossier/out/activation_map.tsv',encoding='utf-8'),delimiter='\t') if r['role']=='dominant' and r['branch_ref'].startswith('root_')]
tp=[r for r in rows if BI.get(r['branch_ref'],{}).get('kind')=='collocation']
print(len(tp), collections.Counter(r['branch_ref'] for r in tp).most_common(12))
import random; random.seed(3)
for r in random.sample(tp,6):
    b=r['branch_ref']; v=BI[b]; ay=r['verse_ref']
    print('\n',r['qac_word_ref'],v['root'],b,v['gloss'][:50]); print('  src:',(v.get('src_ar') or '')[:200])
    print('  occ atts:',[ (q,atts) for q,s,atts in occ_by.get((b.split('/')[0],ay),[])][:3])
