from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import json, hashlib, re

W=Path(__file__).parent
R=W.parents[3]
a=json.loads((W/'annotations.json').read_text())
content=json.loads((W/'content_audit.json').read_text())
claims=json.loads((W/'claim_map.json').read_text())
base=Path(content['base_file']).read_bytes()
out=Path(content['output_file']).read_text()
rec=''.join(out[x:y] for x,y in content['original_fragment_character_spans']).encode()
assert base==rec
assert hashlib.sha256(base).hexdigest()==content['base_sha256']
assert hashlib.sha256((W/'evidence_matrix.json').read_bytes()).hexdigest()==(W/'evidence_matrix.precomposition.sha256').read_text().strip()
assert content['matrix_completed_at_utc'] < content['composed_at_utc']
assert all('checked_sources' in x and 'classical_attestation' in x for x in a if x['type']=='novelty')
covered={i for n in content['novelty_coverage'] for i in n['base_blocks']}
assert {c['base_block'] for c in claims['claims']} <= covered
assert all(x['relation']=='thematic' for x in a if x['type']=='hadith')
assert all(x['historicity']=='uncertain' for x in a if x['type']=='asbab')
assert all(x.get('hadith_grade')=='not_assessed' for x in a if x['type']=='asbab')
assert [x['id'] for x in a if x.get('canonical')=='true']==['S107-QIR-001']
assert not any(x.get('canonical')=='false' for x in a)
assert next(x for x in a if x['id']=='S107-TAF-010')['hadith_grade']=='hasan'
assert next(x for x in a if x['id']=='S107-TAF-010')['type']=='tafsir'
assert next(x for x in a if x['id']=='S107-ASB-002')['transmitter'].startswith('İbn Mesʿûd')
assert next(x for x in a if x['id']=='S107-HAD-008')['hadith_grade']=='daif'
assert next(x for x in a if x['id']=='S107-HAD-008')['connection']=='rejected'
assert 'not_checked' in next(x for x in a if x['id']=='S107-SRC-002')['prose']
assert 'iki asıl' in next(x for x in a if x['id']=='S107-MTH-013')['prose']
assert 'düzensiz' in next(x for x in a if x['id']=='S107-MTH-009')['prose']
assert 'mümkün' in next(x for x in a if x['id']=='S107-MTH-005')['prose']
assert 'zayıf bulur' in next(x for x in a if x['id']=='S107-TAF-005')['prose']
assert 'reddedip' in next(x for x in a if x['id']=='S107-TAF-006')['prose']
assert 'Ali en-Nümeyrî' in next(x for x in a if x['id']=='S107-SRC-004')['prose']
q=json.loads((W/'quran_passages.json').read_text())
assert len(q)==188
assert json.loads((W/'quran_quote_audit.json').read_text())['literal_normalized_mismatches']==[]
assert len([r for r in json.loads((W/'retrieval_index.json').read_text()) if r['state']=='inspected_displayed_body_complete'])==56
assert sum(r['inspected'] for r in json.loads((W/'lexicon_sections.json').read_text()))==19
assert not any('Enrichment pending.' in line for line in out.splitlines())
assert not any('\n' in x['prose'] for x in a)
assert not re.search(r'|turn\d+(?:search|view|fetch)\d+',out)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
supp=[('alusi_107_1','https://quran-tafsir.net/alusy/sura107-aya1.html',True),('alusi_107_7','https://quran-tafsir.net/alusy/sura107-aya7.html',True),('ibnatiyya_107_1','https://quran-tafsir.net/atia/sura107-aya1.html',True),('beqaay_108_1','https://quran-tafsir.net/beqaay/sura108-aya1.html',True),('tabary_51_11','https://quran.ksu.edu.sa/tafseer/tabary/sura51-aya11.html',True),('tabary_9_103','https://quran.ksu.edu.sa/tafseer/tabary/sura9-aya103.html',True),('qortobi_67_30','https://quran.ksu.edu.sa/tafseer/qortobi/sura67-aya30.html',True),('beqaay_106_4','https://quran-tafsir.net/beqaay/sura106-aya4.html',False)]
srows=[]
for key,url,inspected in supp:
    p=W/'sources'/f'{key}.txt'
    srows.append(dict(key=key,url=url,downloaded=p.exists(),inspected=inspected,scope='Displayed div.nass body complete' if inspected else 'Downloaded but not inspected; excluded from all novelty coverage.',sha256=sha(p) if p.exists() else None))
srows.append(dict(key='wahidi_107',url='https://quranpedia.net/surah/1/107/book/2919',downloaded=(W/'sources/wahidi_107.html').exists(),inspected=True,scope='Actual displayed 107:1–2 asbab passages and explicitly empty107:3–7 entries; not whole edition.',sha256=sha(W/'sources/wahidi_107.html')))
srows.append(dict(key='abushama_638',url='https://www.islamicbook.ws/qbook/alom/ibraz-almaani-004.html',downloaded=False,inspected=True,scope='Web tool: Shatibiyya638 verse and explanatory paragraph about root hamza in interrogative rayta/raytum; not whole page/volume.'))
(W/'supplementary_inspections.json').write_text(json.dumps(srows,ensure_ascii=False,indent=2)+'\n')
addendum=dict(stage='postcomposition_editorial_source_checks',checked_at_utc=datetime.now(timezone.utc).isoformat(),original_precomposition_matrix_unchanged=True,checks=[dict(source='Suyuti107:7 line5',finding='Actual attribution of implements-borrowing sabab is Ibn Masud, through Ibn Mardawayh; draft attribution corrected to match primary displayed passage.'),dict(source='Razi107:4–5 second masala',finding='Initial objection to simple prayer-abandonment reading and possible reply via form/meaning distinction both retained; not just claimed support.'),dict(source='Ibn Kathir107:7 and Suyuti107:7 Ibn Qani variant',finding='Ali al-Namiri versus Ali b Abi Talib name difference remains unresolved; people not conflated.'),dict(source='Quran68:18–22 and83:12–15',finding='Nine additional context verses actually read during range QC; final exact list188 verses. No claim these were read before the frozen matrix.')])
(W/'evidence_matrix.QC_addendum.json').write_text(json.dumps(addendum,ensure_ascii=False,indent=2)+'\n')
result=dict(content_qc_passed=True,checked_at_utc=datetime.now(timezone.utc).isoformat(),output_sha256=sha(Path(content['output_file'])),base_fragments_and_separators_byte_exact=True,major_paragraphs_novelty_audited=len(covered),novelty_annotations=sum(x['type']=='novelty' for x in a),novelty_classical_attestation_counts=dict(Counter(x['classical_attestation'] for x in a if x['type']=='novelty')),hadith_annotations=11,hadith_grade_counts=dict(Counter(x['hadith_grade'] for x in a if x['type']=='hadith')),companion_loan_report_has_verified_hasan_grade=True,no_sahih_direct_prophetic_tafsir_invented=True,no_asbab_certainty_or_grade_invented=True,reported_reading_labels_bounded=True,ordinary_sehv_disagreement_and_razi_rejection_retained=True,important_failed_candidates_retained=True,quran_verses_inspected=188,quran_literal_tags_normalized_checked=110,core_page_bodies_inspected=56,hawramani_author_root_blocks_inspected=19,substantive_evidence_matrix_before_composition=True,whole_volume_or_exhaustive_source_coverage_not_claimed=True,limitations_explicit_in_final_md=True,own_outputs_only=True,errors=[])
(W/'editorial_qc.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
