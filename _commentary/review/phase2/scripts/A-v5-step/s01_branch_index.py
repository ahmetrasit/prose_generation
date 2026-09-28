# Build branch_ref -> {root letters, kind, gloss, image_ar, what_is_ar, what_is_not_ar, source phrase, sources, error profile}
# from the project's own dictionary (quran-data/data/dictionary/tr). Read-only.
import json, glob, os, csv, collections, sys
OUT=os.path.join(os.path.dirname(__file__),'out')
csv.field_size_limit(10**9)
roots={}
for r in csv.DictReader(open('/Volumes/OZTURK/_projects/quran-slm/resources/source/quranic_branches_ar.tsv',encoding='utf-8'),delimiter='\t'):
    roots[r['source_root_id']]=r['surface_root']
idx={}; kinds=collections.Counter(); occ={}
for p in sorted(glob.glob('/Volumes/OZTURK/_projects/quran-data/data/dictionary/tr/root_*_entry.json')):
    d=json.load(open(p,encoding='utf-8'))
    rid=d['root_envelope_id']
    oe=d.get('occurrence_evidence') or {}
    # construction evidence per occurrence: attachments (relation, other_surface, other_root, prep_base)
    occs=[]
    for o in oe.get('occurrences',[]):
        al=(o.get('alignment') or {})
        atts=[(a.get('relation'),a.get('other_surface'),a.get('other_root'),a.get('prep_base'),a.get('focus_role')) for a in (al.get('attachments') or [])]
        occs.append((o.get('qac_ref'),o.get('ayah_ref'),o.get('lemma_ar'),o.get('surface_ar'),atts))
    occ[rid]={'n_words':(oe.get('summary') or {}).get('word_count'),'n_ayat':(oe.get('summary') or {}).get('ayah_count'),'occ':occs}
    for b in d['branches']:
        ls=b.get('lexicalization_scope') or {}
        k=ls.get('branch_kind','missing'); kinds[k]+=1
        cg=b.get('concept_gloss') or {}
        idx[b['branch_ref']]={'root':roots.get(rid,rid),'kind':k,'scope_note':ls.get('note'),
            'gloss':cg.get('text'),'image_ar':b.get('branch_image_ar'),'what_is_ar':b.get('what_is_ar'),
            'what_is_not_ar':b.get('what_is_not_ar'),'src_ar':b.get('source_phrase_ar'),'sources':b.get('sources'),
            'loses':(cg.get('error_profile') or {}).get('loses'),'adds':(cg.get('error_profile') or {}).get('adds'),
            'status':(b.get('identity_judgment') or {}).get('status'),
            'tr_glosses':[(g.get('text'),(g.get('error_profile') or {}).get('fit'),(g.get('error_profile') or {}).get('loses'),(g.get('error_profile') or {}).get('adds'),(g.get('error_profile') or {}).get('collision')) for g in (b.get('contextual_glosses') or []) if (g.get('error_profile') or {}).get('fit') not in (None,'none')]}
json.dump(idx,open(os.path.join(OUT,'branch_index.json'),'w'),ensure_ascii=False)
json.dump(occ,open(os.path.join(OUT,'root_occ.json'),'w'),ensure_ascii=False)
print('branches',len(idx),'roots',len(occ)); print(kinds)
