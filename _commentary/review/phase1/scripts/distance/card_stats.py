import csv, json, glob, collections, numpy as np
csv.field_size_limit(10**9)
rows=list(csv.DictReader(open('/Volumes/OZTURK/_projects/quran-slm/resources/source/corpus_branches_ar.tsv',encoding='utf-8'),delimiter='\t'))
L=np.array([len(r['branch_image_ar'])+len(r['what_is_ar'])+len(r['source_phrase_ar']) for r in rows])
Li=np.array([len(r['branch_image_ar']) for r in rows]); Lw=np.array([len(r['what_is_ar']) for r in rows]); Ls=np.array([len(r['source_phrase_ar']) for r in rows])
print('cards',len(rows),'total chars median',np.median(L),'p90',np.percentile(L,90),'max',L.max())
print('image median',np.median(Li),'what_is median',np.median(Lw),'source_phrase median',np.median(Ls), 'share of chars in source phrases', Ls.sum()/L.sum())
q=np.array([r['source_phrase_ar'].count('(') for r in rows]); print('dictionary citations per card median',np.median(q),'p90',np.percentile(q,90))
print('cards > 1500 chars', (L>1500).sum(), '> 2000', (L>2000).sum())
# Luna scenes per card
tags=collections.defaultdict(set)
for f in glob.glob('/Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/frames/out/*.json'):
    for it in json.load(open(f))['items']:
        for fr in it['frames']: tags[it['key']].add(fr['frame'])
k=[len(v) for v in tags.values()]
print('Luna scenes per branch:', collections.Counter(k))
