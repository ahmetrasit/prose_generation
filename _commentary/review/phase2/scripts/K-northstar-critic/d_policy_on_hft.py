"""D's static memory_score on the independent HFT neighbour-activation outlier branches (all 3,398 cases, named
surahs excluded): share whose early phrase D would push (score<=1) vs index line only. The HFT feature makes this
partly circular (an outlier adds >=1 HFT activation), so also shown without that feature. Read-only."""
import csv,json,os,collections
HERE=os.path.dirname(os.path.abspath(__file__))
D='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/D-knowledge-supply/branches.tsv'
T={r['branch_ref']:r for r in csv.DictReader(open(D),delimiter='\t')}
S=json.load(open(os.path.join(HERE,'hft_na_set.json')))
c=collections.Counter(); c2=collections.Counter(); kinds=collections.Counter()
for x in S['all']:
    r=T.get(f"{x['rid']}/{x['branch']}")
    if not r: c['missing']+=1; continue
    pos=int(r['idx'])<=3; src=int(r['n_sources'])>=4; act=int(r['hft_any'])+int(r['v12'])>=10
    s=pos+src+act; c['pushed' if s<=1 else 'index_only']+=1
    s2=pos+src; c2['pushed' if s2<=1 else 'index_only']+=1
    kinds[r['branch_kind']]+=1
print('with HFT feature',dict(c)); print('without HFT feature',dict(c2)); print('kinds',dict(kinds))
