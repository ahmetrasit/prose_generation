from pathlib import Path
import json,hashlib,re
from collections import Counter
W=Path('enrichment/v1/work/107_astra_high');O=Path('enrichment/v1/out/107/107_enriched.astra-high.md');B=Path('_commentary/v16/out/s107/images.r13.map3.nohft.tool.tool/images.md')
a=json.loads((W/'annotation_records.json').read_text());nov=[x for x in a if x['type']=='novelty'];out=O.read_text();base=B.read_text()
parts=out.split('\n\n## Kaynak kayıtları')[0].split('\n\n');restored='\n\n'.join(x for x in parts if not x.startswith('<!--') and not x.startswith('{id:'))+'\n'
coverage={
 'seeing':['001','002','023'],'cloth':['003','004'],'sehv':['005'],'suha':['006','017'],'hands':['007','018'],
 'house':['008','009','020'],'water':['010','020'],'fire':['011','012','018','019'],'debt':['013','014','021'],
 'outward':['015','016','021'],'quran':['002','009','012','014','016','018','019','021'],'structure':['022']}
for v in coverage.values():
 for n in v:assert any(d['id']=='S107-NOV-'+n for d in nov)
corpus={name:{'passages':'S107:1–7 digital verse-labelled pages, fully inspected','files':[str(p.relative_to(W)) for p in sorted((W/'sources').glob(slug+'_[1-7].txt'))]} for name,slug in [('Tabari','tabary'),('IbnKathir','katheer'),('Zamakhshari','zamakhshary'),('Razi','alrazy'),('Baydawi','baidawy'),('Suyuti','seoty'),('Biqai','beqaay')]}
corpus['Razi']['qualification']='107:4 and107:5 duplicate same section;107:2 continues in107:3. Intro107:1 m1–4;4–5 m1–3;6;7 four opinions/alignment/closing prayer.'
corpus['Baydawi']['qualification']='107:4 header only; relevant linkage in107:3.'
corpus['Suyuti']['qualification']='107:3 header only; cannot infer absent printed material.'
corpus['extra']=['Qurtubi107:1 and107:7 fully; Qurtubi67:30 fully','Wahidi107 records871/871m','IbnAshur107:1 page introduction and commentary fully','Tabari9:103 fully','Razi108:1 ONLY first latifa','AbuShama Ibraaz638 ONLY commentary on arayt','21 indexed lexical source entries listed in source registry, bounded as specified there; Maqayis سهو and معن web entries fully','11 individually opened hadiths, grading attributed to source; no independent isnad grading','Original Quran references and additional references saved in two inspected source files']
issues=[
 {'base_claim':'Musallin fire/ritual unity','evidence':'Maqayis صلى explicitly two origins; Raghib صلا DOES preserve unnamed fire-removal derivation','resolution':'Echo-root comparison constrained; old partial antecedent preserved'},
 {'base_claim':'Outward prayer gives poor sakana via9:103','evidence':'Tabari9:103 and Bukhari1497: Prophet prays for donors; tranquility recipient donor','resolution':'Flagged locally, base untouched'},
 {'base_claim':'Suha and shelf necessary sehv derivation','evidence':'Maqayis سهو: Suha possible; sehwa anomalous','resolution':'Qualifiers preserved'},
 {'base_claim':'Lift/drop opposite meanings regular same-root inference','evidence':'Maqayis دع excludes imitative calls from analogy; حض two origins','resolution':'Rejection/constraint annotations'},
 {'base_claim':'Maun/maeen one definite root','evidence':'Raghib عين and Qurtubi67:30 preserve alternatives','resolution':'Disputed derivation'},
 {'base_claim':'Verse7 small debt unpaid','evidence':'Received tafsir withheld tool/zakat/benefit, not explicitly unpaid borrowed debt','resolution':'Metaphorical ledger bounded'},
 {'base_claim':'No classical precursor to social prayer reversal','evidence':'Razi107:7 explicit prayer-for-God displayed-to-people / human-help withheld reversal','resolution':'Explicit core anchor and partial novelty'},
 {'base_claim':'No classical fire-prayer or74 precursor','evidence':'Raghib صلا fire derivation and107/74 juxtaposition','resolution':'Partial novelty; Raghib universal musallin remark constrained by70:22'},
 {'source_conflict':'Razi107:4 discussion numbering','resolution':'Corrected source_ref to second/third faces within m1 after rereading'},
 {'source_conflict':'Qurtubi107:7 etymology numbering','resolution':'Corrected alternative عون to tenth opinion; historical usage fourth'},
 {'source_conflict':'Biqai Enfal snippet verse number and count-based history','resolution':'Corrected added citation scope8:3–4; rejected numerical history as independent evidence'},
 {'source_conflict':'Named sabab subjects and chronology','resolution':'Competing names and Makki/Madani/split reception retained without invented isnad resolution'},
 {'source_conflict':'Saad marfu/mawquf; AbuBarza; Qurra report; water/salt/fire','resolution':'Source criticism and grades attributed, weaker reports not merged into authenticated evidence'}]
audit={
 'output':str(O.resolve()),'sha256':hashlib.sha256(O.read_bytes()).hexdigest(),'base_sha256':hashlib.sha256(B.read_bytes()).hexdigest(),
 'precomposition_matrix':{'file':'evidence_matrix.json','substantive_rows':len(json.loads((W/'evidence_matrix.json').read_text())),'created_before_annotation_composition':True},
 'exact_base_reconstruction':restored==base,'unique_annotation_prose':len({d['prose'] for d in a})==len(a),'no_inline_insertion':True,
 'types':dict(Counter(x['type'] for x in a)),'novelty_statuses':dict(Counter(x['classical_attestation'] for x in nov)),
 'novelty_coverage':coverage,'source_content_review':issues,'checked_corpus':corpus,
 'deduplication':'Repeated IbnAbbas public/private-prayer/tool reports treated as one received cluster with attested_in; maun lexical meanings grouped; distinct sabab and hadith reports kept distinct. Repeated synthesis paragraphs receive separate scope-limited novelty audits, not duplicated evidence claims.',
 'limitations':['No printed-volume audit','No independent full isnad study','Qurtubi107:2–6 not_checked','Non-target Quran passage tafsir generally not_checked except named extras','Modern scholarly literature not_checked; IbnAshur107:1 only','Absent S107_comprehensive_reference_v2.md not invented','Structural validator alone does not establish source accuracy'],
 'scope_respected':'Only exclusive output and own work directory written; no competing work/output read; no original edited; no agents delegated',
 'completed':True}
assert audit['exact_base_reconstruction'] and audit['unique_annotation_prose']
(W/'source_content_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'exact_base_reconstruction':True,'novelty_networks':len(coverage),'matrix_rows':audit['precomposition_matrix']['substantive_rows'],'review_items':len(issues),'output_sha256':audit['sha256']},ensure_ascii=False))
