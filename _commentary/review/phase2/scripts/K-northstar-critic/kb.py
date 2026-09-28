# branch lookup: root letters -> branches with kind, note, image, phrase (read-only)
import json,glob,csv,sys,pickle,os
TR='/Volumes/OZTURK/_projects/quran-data/data/dictionary/tr'
V15='/Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/branches.tsv'
CACHE=os.path.join(os.path.dirname(__file__),'kb.pkl')
def load():
    if os.path.exists(CACHE): return pickle.load(open(CACHE,'rb'))
    rid2root={}
    for r in csv.DictReader(open(V15),delimiter='\t'):
        rid2root[r['root_id']]=r['root']
    B={}
    for f in glob.glob(TR+'/*_entry.json'):
        try: d=json.load(open(f))
        except: continue
        for b in d['branches']:
            ref=b['branch_ref']; rid,bid=ref.split('/')
            ls=b.get('lexicalization_scope') or {}
            B[ref]=dict(root=rid2root.get(rid,rid),rid=rid,bid=bid,kind=ls.get('branch_kind'),note=ls.get('note'),
                        image=b.get('branch_image_ar'),what=b.get('what_is_ar'),phrase=b.get('source_phrase_ar'),
                        gloss=(b.get('concept_gloss') or {}) )
    pickle.dump(B,open(CACHE,'wb'))
    return B
if __name__=='__main__':
    B=load()
    roots=sys.argv[1:]
    for ref,b in sorted(B.items()):
        if b['root'] in roots:
            ph=b['phrase']; ph=json.dumps(ph,ensure_ascii=False)[:260] if not isinstance(ph,str) else ph[:260]
            print(f"{b['root']} {b['bid']} [{b['kind']}] {b['image']} || {ph} || note: {(b['note'] or '')[:160]}")
