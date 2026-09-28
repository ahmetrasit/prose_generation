# K3b: which branches does D's phrase policy (memory_score>=2 -> index line only) leave without their early phrase,
# among those memory did NOT recall (cold=0)? Position, sources, activation history, and the dictionary gloss.
import csv, collections, json
R='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/D-knowledge-supply/r3/recall_manual.tsv'
rows=[r for r in csv.DictReader(open(R),delimiter='\t') if r['plain']!='1']
def sc(r): return int(int(r['idx'])<=3)+int(int(r['n_sources'])>=4)+int(int(r['hft_any'] or 0)+int(r['v12'] or 0)>=10)
io=[r for r in rows if sc(r)>=2 and r['cold']!='1']
print('latent, not recalled by memory, index-only:',len(io))
print('  by position:',collections.Counter('B001' if int(r['idx'])==1 else ('B002-3' if int(r['idx'])<=3 else 'B004+') for r in io))
print('  fed arm reached them:',sum(r['fed']=='1' for r in io))
fo=[r for r in io if r['fed']=='1']
print('fed-only index-only by position:',collections.Counter('B001' if int(r['idx'])==1 else ('B002-3' if int(r['idx'])<=3 else 'B004+') for r in fo))
print('columns:',list(rows[0].keys()))
for r in fo: print('  ',r.get('ayah'),r.get('root'),r.get('branch'),'idx',r['idx'],'src',r['n_sources'],'hft',r['hft_any'],'v12',r['v12'])
