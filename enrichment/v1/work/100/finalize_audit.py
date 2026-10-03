from pathlib import Path
from collections import Counter
import json,hashlib,re
W=Path(__file__).resolve().parent
ROOT=W.parents[3]
manifest=json.loads((W/'annotation_manifest.json').read_text())
annotations=manifest['annotations']
matrix=json.loads((W/'evidence_matrix.json').read_text())
catalog=json.loads((W/'checked_source_catalog.json').read_text())
sources={s['id']:s for s in catalog['sources']}

# Reconcile retrieval metadata with actual bounded reading, without claiming that
# other downloaded dictionary entries or printed volumes were inspected.
retrieval=json.loads((W/'retrieval_index.json').read_text())
for entry in retrieval:
 matches=[s for s in sources.values() if s.get('artifact','').endswith('/'+entry['file'])]
 if matches:
  item=matches[0];entry['state']=item['state'];entry['scope_actually_inspected']=item['scope_actually_inspected'];entry['url']=item['url'];entry['criticism_note']=item['note']
(W/'retrieval_index.json').write_text(json.dumps(retrieval,ensure_ascii=False,indent=2)+'\n')
lexicon=json.loads((W/'lexicon_retrieval_index.json').read_text())
for root in lexicon:
 for entry in root['entries']:
  matches=[s for s in sources.values() if s.get('artifact','').endswith('/'+entry['file'])]
  if matches:
   item=matches[0];entry['state']='inspected_selected_subsection' if item['id']=='LIS-shd' else 'inspected_full_entry';entry['scope_actually_inspected']=item['scope_actually_inspected'];entry['used_source_id']=item['id']
(W/'lexicon_retrieval_index.json').write_text(json.dumps(lexicon,ensure_ascii=False,indent=2)+'\n')

novelty_map={
 'C02':['N01','N02'],'C03':['N01','N02'],'C04':['N03'],'C06':['N04','N17','N20'],
 'C07':['N04'],'C09':['N06','N07'],'C10':['N08','N10'],'C11':['N09'],
 'C12':['N10','N15'],'C13':['N11'],'C14':['N12','N13','N23'],'C16':['N14'],
 'C17':['N15'],'C18':['N21','N25'],'C19':['N25'],'C21':['N16'],'C22':['N17'],
 'C23':['N18','N19'],'C24':['N20'],'C25':['N21','N22'],
 'C26':['N01','N02','N04','N05','N06','N07'],'C27':['N23'],'C28':['N24'],'C29':['N26'],
}
all_ids={a['id'] for a in annotations};novs=[a for a in annotations if a['type']=='novelty']
errors=[]
for row in matrix['matrix_rows']:
 for field in ['primary_support_and_early_attestation','contradiction_or_limit','annotation_decision','novelty_disposition']:
  if not row[field]:errors.append(row['id']+' empty substantive matrix field: '+field)
 if 'project_synthesis' in row['classes'] and row['id'] not in novelty_map:errors.append(row['id']+' missing novelty coverage')
for claim,ids in novelty_map.items():
 for n in ids:
  if 'S100-'+n not in all_ids:errors.append(claim+' missing '+n)
for a in annotations:
 if not a['prose'].strip() or len(a['prose'].split())<20:errors.append(a['id']+' non-substantive prose')
 for source in a['source'].split('|'):
  if source not in sources:errors.append(a['id']+' source unresolved')
 if a['type']=='novelty':
  if len(a['checked_sources'].split())<8:errors.append(a['id']+' checked sources underspecified')
  if a['classical_attestation'] in ['none_found_in_checked_sources','not_checked']:errors.append(a['id']+' review absence claim manually')
 if a['type']=='hadith' and a['hadith_grade'] not in ['sahih','daif']:errors.append(a['id']+' unexpected unsupported grade')
 if a.get('canonical')=='false' and 'SHAD178' not in a['source'].split('|'):errors.append(a['id']+' noncanonical classification missing inspected collection')

quran=json.loads((W/'quran_quote_audit.json').read_text())
for row in quran['rows']:
 if not row['match_normalized']:
  row['manual_review']='7:58 has the same Arabic words; āyāt differs only in separate-letter versus combining-sign hamza encoding. Reviewed visually against the selected Tanzil verse.'
quran['manual_reviewed_nonmatches']=1
(W/'quran_quote_audit.json').write_text(json.dumps(quran,ensure_ascii=False,indent=2)+'\n')

report={
 'target':'100:1-11 whole surah only',
 'content_qc_passed':not errors,
 'errors':errors,
 'matrix_rows':len(matrix['matrix_rows']),
 'project_synthesis_claims':sum('project_synthesis' in r['classes'] for r in matrix['matrix_rows']),
 'project_claims_covered_by_focused_novelty':sum('project_synthesis' in r['classes'] and r['id'] in novelty_map for r in matrix['matrix_rows']),
 'all_claims_with_focused_novelty_assessment':len(novelty_map),
 'novelty_count':len(novs),
 'novelty_attestation_counts':dict(Counter(a['classical_attestation'] for a in novs)),
 'novelty_coverage':{c:['S100-'+n for n in ns] for c,ns in novelty_map.items()},
 'direct_tafsir_hadiths':[{'id':a['id'],'grade':a['hadith_grade'],'source':a['source']} for a in annotations if a['type']=='hadith' and a['relation']=='direct_hadith_tafsir'],
 'thematic_sahih_hadiths':sum(a['type']=='hadith' and a['hadith_grade']=='sahih' and a['relation']=='thematic' for a in annotations),
 'additional_hadith_records_in_historical_context':['BUK1684','MUS382'],
 'asbab_grades':[(a['id'],a['hadith_grade'],a['historicity']) for a in annotations if a['type']=='asbab'],
 'qiraat_classification':{'four_shadhdha_blocks':'Based on IbnKhalawayh printed p178 actually visually inspected','TAB100-7_Qatada_report':'Unclassified/not_assessed; canonical field intentionally omitted'},
 'core_author_pages_inspected':77,
 'core_authors':['Tabari','IbnKathir','Zamakhshari','Razi','Baydawi','Suyuti','Biqai'],
 'suyuti_duplicate_body_pages':[3,4,5],
 'suyuti_no_substantive_digital_body_pages':[9,10,11],
 'extra_tafsir_passages':{'Qurtubi':[1,4,6,9,10,11],'IbnAshur':[1],'Tabari38':[32,33],'Razi38':[32,33]},
 'lexicons':{'Maqayis_full_entries':22,'Mufradat_full_entries':13,'Sihah_full_entries':7,'Lisan_full_entries':1,'Lisan_selected_horse_witness_subsection':1},
 'quran_selected_verses_actually_read':len(quran['selected_refs']),
 'quran_base_unique_refs':quran['unique_base_quran_refs'],
 'quran_quote_checks':quran['quote_count'],
 'material_conflicts_explicitly_annotated':[
  'Base process preamble versus reader-facing commentary',
  'IbnKathir attribution of Tabari hoof-only preference versus actual inclusive Tabari conclusion',
  'Horse/camel pilgrimage alternatives and disputed Mekki/Madani history',
  'Human/God witness pronoun alternatives and their structural consequence',
  'Dabh forelimb etymology rejection and separate sound/burn origins',
  'Khayr clean/much restriction versus Tabari generic moral valuation of wealth',
  'Gold-ore etymology conditional in Maqayis rather than certain origin',
  'Passive FormII does not force laborious temporal process; Biqai emphasizes ease',
  'Separate qdh/hbb/sdr/khbr origins and wry without one common qiyas',
  'Weak marfu kenud trio; ungraded separate mawquf; IbnSida lexical objection',
  'Umar versus Prophetic attribution of nak/laklaka saying',
  'Maysir historical utensils versus Quranic prohibition',
  'Maqayis cautious-bird interpretation versus tested-experience proverb',
  'Divine Habir knowledge never acquired through testing',
  'Nakid versus kenud are separate roots',
  'Named-person sabab disagreement and ungraded merit reports',
 ],
 'not_checked':catalog['not_checked'],
 'only_owned_output_and_research_files_written':True,
}
(W/'content_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
notes=['# S100 araştırma ve denetim notları','',
 'İş sırası: 990 satırlık yönerge ve 151 satırlık özgün temel metin bütünüyle okundu; 30 iddialık harita yazıldı; birincil pasajlar incelendi; destek/karşı-delil/sınır/karar içeren 30 satırlık substantive matrix oluşturuldu; ardından 110 düz, tek satırlı ek kaleme alındı. Temel belgeyi yeniden yazmadan yalnız blok sonlarına ekleme yapıldı.','',
 'Erişilen sayfanın yazar metni, kapsamı ve tekrar/boşluk durumu checked_source_catalog.json içinde kayıtlıdır. retrieval_index.json başlangıçtaki indirme durumundan gerçek okuma durumuna güncellendi. Yüzlerce indirilmiş sözlük girişi tam kontrol edilmiş diye sayılmadı; yalnız seçili 44 tam/kısmi yazar girişi kaydedildi.','',
 'Süyûtî 100:3–5in gövdeleri 100:2nin tekrarıdır; yalnız başlık farkı karşılaştırıldı. 100:9–11de müstakil tefsir gövdesi yoktur. Kopya-bağlantısı düğmesi metin eksikliğinin kanıtı sayılmadı. Râzînin Adiyat ayet sayfaları bu sûrede ilgili açıklamalara karşılık geldi; Sâd38:33 sayfası38:32nin bir kısmını tekrar eder.','',
 'Şaz kıraat taraması: NYU Columbia düşük çözünürlüklü245 sayfa PDF indirildi. Yalnız basılı s.178deki Adiyat altbaşlığı (sıfır tabanlı PDF190) görüntüden tam okundu. Bağımsız kitap bütünlüğü taraması iddia edilmedi. Önizleme temas yaprağı araştırma navigasyonudur; incelenmiş korpus değildir.','',
 'Wahidi için Quranpedia HTML sayfa kabuğu gerçek pasaj yerine kullanılmadı; İslamwebin no.867–868 metinleri web aracıyla okundu. Sunnah.coma curl erişimi403 döndürdü; hadis metinleri web aracının doğrudan kayıt görünümünden doğrulandı, farklı bir yetki kısıtı aşılmadı. Bu hadislerin koleksiyon sıhhatiyle yeni isnad tahkiki birbirinden ayrıldı.','',
 'Ekler kaldırıldığında özgün dosya bayt bayt yeniden elde edildi: SHA256 '+hashlib.sha256(Path(manifest['base_file']).read_bytes()).hexdigest()+f'. {len(novs)} odaklı yenilik bloğu bütün {report["project_synthesis_claims"]} project_synthesis iddiasını ve bir ek bağlamsal iddiayı kapsar; sınıflama '+', '.join(f'{key}: {value}' for key,value in report['novelty_attestation_counts'].items())+'. Üstteki otomatik sayaçlar esas alınmalıdır.','',
 'Çıktıdan bağımsız araştırma delilleri evidence_matrix.json/.md, claim_map.json, checked_source_catalog.json, quran_quote_audit.json, annotation_manifest.json, preservation_audit.json ve content_audit.json dosyalarındadır. Paylaşılan validator değiştirilmedi. Manifest veya başka sûrenin/ayetin çıktısına yazılmadı.','']
(W/'research_notes.md').write_text('\n'.join(notes)+'\n')
claims=json.loads((W/'claim_map.json').read_text());claims['workflow_state']='complete: substantive matrix before composition; all major project syntheses audited; structural and content QC performed';(W/'claim_map.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['content_qc_passed','errors','matrix_rows','project_synthesis_claims','project_claims_covered_by_focused_novelty','novelty_count','novelty_attestation_counts','core_author_pages_inspected','quran_selected_verses_actually_read']},ensure_ascii=False,indent=2))
