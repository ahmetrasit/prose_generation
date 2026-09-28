import json, os, re, collections
D=os.path.dirname(__file__)
rows=json.load(open(os.path.join(D,'files.json')))
counts={}
for line in open('/Volumes/OZTURK/_projects/quran-slm/resources/source/quran_ayah_counts.tsv'):
    p=line.strip().split('\t')
    if p[0].isdigit(): counts[int(p[0])]=int(p[1])
# per analysis per ayah
per=collections.defaultdict(lambda: collections.defaultdict(set))
for layer,rel,f,sz in rows:
    parts=rel.split(os.sep)
    if layer in('input','raw','editorial','middle','concise','output') and len(parts)>=3:
        aid=parts[0]; ay=parts[2]
        per[aid][ay].add((layer,re.sub(r'^\d+_\d+\.','S_A.',f)))
keys={'in_disc':('input','macro.discovery.prompt.md'),'disc3':None,'scope3':None,'ledger3':None,
 'canon':('raw','S_A.prose.tr.md'),'edit':('editorial','S_A.prose.editorial.tr.md'),'inv':('editorial','S_A.invitation.tr.md'),
 'mid':('middle','S_A.prose.middle.tr.md'),'midclaims':('middle','S_A.middle.claims.json'),'midprompt':('input','middle-layer.prompt.md')}
out=[]
print('aid\tn_ayahdirs\tin_disc\tdisc3\tscope3\tcanon\tedit\tinv\tmid\tmidclaims')
for aid in sorted(per):
    ays=per[aid]
    c=collections.Counter()
    for ay,fs in ays.items():
        for k,v in keys.items():
            if v and v in fs: c[k]+=1
        if all(('raw',f'{l}.discovery.json') in fs for l in ('micro','macro','global')): c['disc3']+=1
        if all(('raw',f'{l}.scope.tr.md') in fs for l in ('micro','macro','global')) or all(('raw',f'{l}.prose.tr.md') in fs for l in ('micro','macro','global')): c['scope3']+=1
    print('\t'.join([aid,str(len(ays))]+[str(c[k]) for k in ['in_disc','disc3','scope3','canon','edit','inv','mid','midclaims']]))
