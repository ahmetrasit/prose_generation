import csv,sqlite3,re,collections,sys
csv.field_size_limit(10**9)
P='/Volumes/OZTURK/_projects/'
DI=re.compile(r'[ً-ْٰـۖ-ۭ]')
def norm(s):
    s=DI.sub('',s or ''); s=re.sub('[أإآٱ]','ا',s); s=s.replace('ى','ي').replace('ة','ه').replace('ؤ','و').replace('ئ','ي')
    return s
surahs=[int(x) for x in sys.argv[1].split(',')]
rows=[r for r in csv.DictReader(open(P+'quran-slm/resources/source/qac_root_ayah.tsv',encoding='utf-8'),delimiter='\t') if int(r['surah']) in surahs]
roots=set(r['root_norm'] for r in rows)
# forms per root in window: lemmas + surfaces, normalized, stripped of prefixes al-/w-/f-/b-/l-
forms=collections.defaultdict(set)
for r in rows:
    for f in (r['lemmas_ar'].split('|')+r['surfaces_ar'].split('|')):
        for x in re.split(r'[;,\s]+',f):
            n=norm(x)
            n=re.sub(r'^(وال|فال|بال|لل|ال|و|ف)','',n) if len(n)>4 else n
            if len(n)>=3: forms[r['root_norm']].add(n)
c=sqlite3.connect(P+'dictionary/data/working/furuq_v4.sqlite')
hits=[]
for rid,bid,rn,img,wi in c.execute("select root_id,branch_id,root_norm,branch_image_ar,what_is_ar from branch_images where origin_corpus='quranic'"):
    if rn not in roots: continue
    prose=norm((img or '')+' '+(wi or ''))
    toks=set(re.findall(r'[ء-ي]+',prose))
    toks|={re.sub(r'^(وال|فال|بال|لل|ال|و|ف|ب|ل)','',t) for t in toks}
    for rb in roots:
        if rb==rn: continue
        m=forms[rb]&toks
        if m: hits.append((rn,bid,rb,sorted(m)[:3],(img or '')[:50]))
print('window roots',len(roots),'hits',len(hits))
for h in hits: print(h)
