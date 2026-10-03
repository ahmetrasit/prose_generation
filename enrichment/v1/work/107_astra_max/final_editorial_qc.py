from pathlib import Path
from collections import Counter
import json, re, hashlib

W=Path(__file__).parent
OUT=Path('/Volumes/aro/projects/prose_generation/enrichment/v1/out/107/107_enriched.astra-max.md')
BASE=Path('/Volumes/aro/projects/prose_generation/_commentary/v16/out/s107/images.r13.map3.nohft.tool.tool/images.md')
a=json.loads((W/'annotations.json').read_text())
matrix=json.loads((W/'evidence_matrix.json').read_text())
ids={x['id'] for x in a}
coverage={
 'C01':[], 'C02':[1], 'C03':[2], 'C04':[3], 'C05':[4], 'C06':[5],
 'C07':[6], 'C08':[7], 'C09':[8], 'C10':[9], 'C11':[10], 'C12':[11],
 'C13':[], 'C14':[12], 'C15':[13,24], 'C16':[], 'C17':[], 'C18':[14],
 'C19':[15,24], 'C20':[16], 'C21':[17], 'C22':[], 'C23':[18,23],
 'C24':[19,24], 'C25':[20,25], 'C26':[21,25], 'C27':[22], 'C28':[26],
 'C29':[], 'C30':[], 'C31':[]
}
out=[]
for claim in matrix['claims']:
 ns=[f'S107-NOV-{i:03d}' for i in coverage[claim['id']]]
 assert all(i in ids for i in ns)
 synth='project_synthesis' in claim['classes']
 assert not synth or ns,(claim['id'],'missing major synthesis audit')
 local=[x['id'] for x in a if x['after_base_block'] in claim['paragraphs']]
 assert local,(claim['id'],'no local explanation')
 out.append({'claim_id':claim['id'],'claim':claim['claim'],'novelty_ids':ns,'local_annotation_ids':local,'disposition':'novelty audited' if ns else 'received meaning or evidence layer; not claimed as new'})
body=OUT.read_text(); base=BASE.read_text()
blocks=re.split(r'\n\s*\n',base.strip())
cursor=0
for b in blocks:
 pos=body.index(b,cursor); cursor=pos+len(b)
assert Counter(x['prose'] for x in a).most_common(1)[0][1]==1
cross_refs={s for x in a for s in re.findall(r'S107-[A-Z]+-\d{3}',x['prose'])}
assert cross_refs<=ids
assert all('107:' in x['ayah'] and '\n' not in x['prose'] for x in a)
all_tags=re.findall(r'\{[^{}]*\}',base)
assert all(body.count(t)>=base.count(t) for t in set(all_tags))
for x in a:
 for scope in x['ayah'].split('|'):
  m=re.fullmatch(r'107:(\d+)(?:-(\d+))?',scope); assert m and 1<=int(m[1])<=int(m[2] or m[1])<=7
checks=[
 {'topic':'seeing and mirror','result':'two-way showing has explicit Razi/Zamakhshari antecedent; literal mirror combination bounded; form III versus VI and ayah6 versus final7 corrected in annotations'},
 {'topic':'false cloth and interrupted act','result':'Raghib cloth text and Razi counterfeit prayer both preserved; IbnFaris milk uncertainty stated; no hidden literal cloth/camel asserted'},
 {'topic':'orphan and Suha','result':'IbnFaris solitary definition separated from named alternative etymologies; Suha tentative derivation stated; no sky object in surah claimed'},
 {'topic':'push and encourage','result':'Maqayis two roots in حضض and nonanalogical cries in دعع retained; direct52:13 antecedent preserved'},
 {'topic':'house','result':'old maun vessels and Razi neighbor oven explicit; sahwa irregularity noted; composite home is project image'},
 {'topic':'water','result':'Wahidi23:50 explicit m-n/main/rights/maun antecedent and opposing ayn derivation both retained; no whole Igfal inspection claimed'},
 {'topic':'fire','result':'IbnFaris two originals and original project ECHO mapping stated; prayer-from-burning derivation rejected; weak water/salt/fire report kept weak'},
 {'topic':'debt','result':'din/dayn actual lexicon family retained;107 account not translated commercial debt; ariya versus zakat distinction stated'},
 {'topic':'outward prayer','result':'9:103 Prophet-to-givers dua distinguished from107 ritual; Bukhari1497 thematic; classical Razi rights inversion explicit'},
 {'topic':'nazm','result':'Biqai start/end and neighboring surahs explicit; Razi108 first latifa only; no unity-to-chronology inference'},
 {'topic':'readings','result':'Ulaymi named received readers checked; unclassified companion/other variants remain reported; unstated vocalization of يدعو removed'},
 {'topic':'hadith','result':'13 primary collection records verified; 11 thematic hadith blocks, companion evidence separate; direct tafsir chain objections preserved; no grade invented for ungraded reports'},
 {'topic':'historical scope','result':'contested Makkī/Madanī/split and conditional17th ordering; specific sabab alternatives and camel-count variation retained'},
 {'topic':'deduplication','result':'later report repetition combined; late synthesis paragraphs point to existing novelty records; no duplicate prose records'}
]
report={
 'output':str(OUT),'annotation_count':len(a),'source_count':len(json.loads((W/'source_records.json').read_text())),
 'major_claims':len(out),'project_syntheses_all_have_novelty_audit':True,
 'novelty_count':sum(x['type']=='novelty' for x in a),
 'novelty_attestation_counts':dict(Counter(x['classical_attestation'] for x in a if x['type']=='novelty')),
 'base_blocks_preserved':len(blocks),'base_tags_preserved':len(all_tags),
 'all_annotation_cross_references_resolve':True,'duplicate_annotation_prose':False,
 'base_sha256':hashlib.sha256(BASE.read_bytes()).hexdigest(),'output_sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),
 'source_review':checks,'claim_coverage':out,
 'limitations':matrix['not_checked'],
 'review_type':'source and claim review by the same independent worker; structural checker also run separately',
 'editorial_qc_passed':True
}
(W/'editorial_qc.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in {'source_review','claim_coverage','limitations'}},ensure_ascii=False,indent=2))
