# K3: what D's phrase policy (push the early phrase only when memory_score<=1) withholds, on D's own labels.
# memory_score = [idx<=3] + [n_sources>=4] + [hft_any+v12>=10]  (D r3/policy_eval.py definition, as stated in the proposal)
import csv, collections
R='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/D-knowledge-supply/r3/recall_manual.tsv'
rows=[r for r in csv.DictReader(open(R),delimiter='\t') if r['plain']!='1']
def sc(r): return int(int(r['idx'])<=3)+int(int(r['n_sources'])>=4)+int(int(r['hft_any'] or 0)+int(r['v12'] or 0)>=10)
c=collections.Counter()
for r in rows:
    s=sc(r); cold=r['cold']=='1'; fed=r['fed']=='1'
    push = s<=1
    c['n']+=1; c[('push',push)]+=1
    if fed and not cold: c[('fedonly',push)]+=1
    if not cold: c[('notcold',push)]+=1
    if fed: c[('fed',push)]+=1
print('latent candidates',c['n'],'pushed',c[('push',True)],'index-only',c[('push',False)])
print('fed-only (dictionary arm reached, memory did not): pushed',c[('fedonly',True)],'index-only',c[('fedonly',False)])
print('fed (any): pushed',c[('fed',True)],'index-only',c[('fed',False)])
print('not recalled by memory: pushed',c[('notcold',True)],'index-only',c[('notcold',False)])
