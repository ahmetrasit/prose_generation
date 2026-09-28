# K7: A's digest as a records->prose handover. Per digest (all 909 v5 ayat): number of atomized item lines per
# section (a line starting "- ", plus C2 titles split on " | "), and the popularity labels it carries
# ("[N readings]" on every A/B branch line, lines sorted by that count).
import glob, re, statistics, collections
DG='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/A-v5-step/out/digests'
tot=[]; per=collections.defaultdict(list); lowshare=[]; sorted_ok=0; nd=0; coll_low=[]
for p in sorted(glob.glob(DG+'/*.digest.md')):
    t=open(p,encoding='utf-8').read(); nd+=1
    secs=re.split(r'\n(?=## )',t); n=0
    for s in secs:
        m=re.match(r'## ([A-Z]\d?)\.',s)
        if not m: continue
        k=m.group(1)
        if k=='C2':
            c=len(s.split(':',1)[1].split(' | ')) if ':' in s else 0
        else:
            c=sum(1 for l in s.split('\n') if l.startswith('- '))
        per[k].append(c); n+=c
        if k in ('A','B'):
            cnts=[int(x) for x in re.findall(r'\[(\d+) readings\]',s)]
            if cnts:
                lowshare.append(sum(1 for x in cnts if x<=2)/len(cnts))
                if cnts==sorted(cnts,reverse=True): sorted_ok+=1
    tot.append(n)
q=lambda v,f: sorted(v)[int(f*(len(v)-1))]
print('digests',nd)
print(f'atomized items per digest: median {statistics.median(tot)}, p10 {q(tot,.1)}, p90 {q(tot,.9)}, max {max(tot)}')
for k in sorted(per): print(f'  {k}: median {statistics.median(per[k])}, p90 {q(per[k],.9)}')
print(f'A/B sections sorted by descending [N readings]: {sorted_ok} of {len(lowshare)} sections')
print(f'share of A/B branch lines labelled [1-2 readings]: median {statistics.median(lowshare):.2f}')
for ay in ('1_6','18_86','18_96','100_1','5_6'):
    p=f'{DG}/{ay}.digest.md'
    t=open(p,encoding='utf-8').read(); print(ay,'items',sum(1 for l in t.split('\n') if l.startswith('- ')))
