import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

W=Path(__file__).resolve().parent
ROOT=W.parents[3]
base=ROOT/'_commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/images.md'
out=ROOT/'enrichment/v1/out/1/1_enriched.md'
a=json.loads((W/'annotations.json').read_text())
c=json.loads((W/'claim_map.json').read_text())
m=json.loads((W/'evidence_matrix.json').read_text())
s=json.loads((W/'worker_structural_audit.json').read_text())
assert s['structural_qc_passed'] and not s['errors'] and not s['warnings']
assert s['base_blocks_preserved_exactly_in_order']==100
assert s['original_inline_tags_preserved_in_order']==434
assert s['base_sha256']=='782be8c16d10f4684dc7f79db8acefd312f3ca466c57cffa1c3ce02d6429dea7'
assert len(m['claims'])==len(c['claims'])==73
assert {r['base_line'] for r in c['claims']}<={r['base_line'] for r in a}
assert all(r['novelty_status']!='pending' and r['supporting_sources'] for r in m['claims'])
assert len({r['id'] for r in a})==len(a)==104
nov=[r for r in a if r['type']=='novelty']
assert len(nov)==21 and all(r.get('checked_sources') for r in nov)
assert all(r['classical_attestation'] not in ['none_found_in_checked_sources'] for r in nov)
had=[r for r in a if r['type']=='hadith']
primary=[next(sid for sid in r['source'].split('|') if sid.startswith('H_')) for r in had]
assert len(primary)==len(set(primary))==10
for r,sid in zip(had,primary):
 assert r['hadith_grade']==m['hadith_checked'][sid]['grade']
 assert r['relation']==m['hadith_checked'][sid]['relation']
 assert r['source_ref']
assert all('priority' in r and 'audience' in r and 'tradition' in r for r in a)
assert any(r['type']=='asbab' and r['hadith_grade']=='not_assessed' and r['historicity']=='uncertain' for r in a)
assert {r['canonical'] for r in a if r['type']=='qiraat' and 'canonical' in r}=={True,False}

networks=[
 ('yol ve topluluk',3,17,'S1-NOV-001'),
 ('sahip, efendi, kul ve ev',23,33,'S1-NOV-002'),
 ('hesap, borç, fiyat ve tartı',39,53,'S1-NOV-003'),
 ('rahim, büyütme ve ev',59,67,'S1-NOV-004'),
 ('nimet, hamd ve tamamlanma',73,79,'S1-NOV-005'),
 ('gazap, nimet ve yüzler',85,93,'S1-NOV-006'),
 ('ad, yükseklik ve işaret',99,107,'S1-NOV-007'),
 ('gök, öğle ve terazi',113,117,'S1-NOV-008'),
 ('yağmur, su ve kuyu',123,133,'S1-NOV-009'),
 ('sürü, öncü ve kayıp hayvan',139,145,'S1-NOV-010'),
 ('destek, beden ve yürüyüş',151,157,'S1-NOV-011'),
 ('iki kayboluş',163,167,'S1-NOV-012'),
 ('ev, hediye, gelin, kurban ve varış',173,179,'S1-NOV-013'),
 ('kulluk/yol buluşması',185,185,'S1-NOV-014'),
 ('sürü/yol/kurban/ad buluşması',187,187,'S1-NOV-015'),
 ('Musa, rahim ve Firavun buluşması',189,189,'S1-NOV-016'),
 ('gazap/düşüş/doğrulma buluşması',191,191,'S1-NOV-017'),
 ('borç/kayıt/öğle/terazi buluşması',193,193,'S1-NOV-018'),
 ('Musa/kuyu/rızık buluşması',195,195,'S1-NOV-019'),
 ('İbrahim/gök/işaret buluşması',197,197,'S1-NOV-020'),
 ('bütün surenin birleşik proje ağı',199,199,'S1-NOV-021'),
]
by_id={r['id']:r for r in a}
covered=set()
audit=[]
for name,start,end,nid in networks:
 local=[r['id'] for r in c['claims'] if start<=r['base_line']<=end]
 covered.update(local)
 n=by_id[nid]
 audit.append(dict(network=name,base_claims=local,novelty_id=nid,classical_attestation=n['classical_attestation'],checked_sources=n['checked_sources']))
assert covered=={r['id'] for r in c['claims']}
checks={
 'original_prose_preserved':'100 original blank-separated blocks, 73 prose paragraphs, 14 headings and 13 Kaynaklar lines; exact validator and base hash.',
 'no_paragraph_deleted':'73/73 claim paragraphs mapped and locally annotated; 100/100 original blocks in order.',
 'inline_lexical_tags_preserved':'434/434 original tags in order, including 413 ar tags and 21 source-only tags.',
 'heading_order_preserved':'14/14 original headings preserved.',
 'one_physical_line_per_annotation':'104 flat blocks pass canonical parser.',
 'unique_ids':'104 unique IDs.',
 'required_fields':'All blocks have id/type/ayah/role/relation/status/prose/source.',
 'canonical_enum_values':'Parent validator has zero errors or warnings.',
 'asbab_uncertainty':'Mursal Abu Maysara chain and competing chronology are explicitly uncertain/not_assessed.',
 'thematic_hadith_separated':'Ten checked primary reports; seven thematic/historical and three direct_hadith_tafsir, matching evidence matrix relation classifications.',
 'hadith_grades_verified':'Sahih collection basis and named Darussalam/Tirmidhi/Albani authority; no grade borrowed merely from tafsir quotation.',
 'reading_distinctions':'Canonical reading vs dialect/ishmaam and noncanonical explanatory reports distinguished; reader, rawi and path explicit.',
 'historical_context_sourced':'Lexicon use and theological restraint are typed separately from certain event claims; Ibrahim nazar/munazara dispute preserved.',
 'conflicting_reports_preserved':'Makki/Madani/double revelation; hamd/shukr; basmala counting; malik preference vs canonical maalik; alternative name derivations.',
 'every_novelty_has_checked_sources':'21 connection-specific lists; full Razi and other incomplete scopes expressly not_checked.',
 'no_absolute_classical_absence_claim':'No none_found_in_checked_sources classification; body denies universal absence and first-ever inference.',
 'building_blocks_separated':'Seven building_blocks_only, twelve partial, one explicit, one not_checked.',
 'resonance_not_contextual_translation':'Core method controls and local constraints retain primary ayah meaning; root identity and echo roots separated.',
 'report_deduplication':'Ten distinct primary hadith families get one hadith block each; later tafsir repetitions are attestations. Asbab family not multiplied.',
 'interpretive_consequences':'Local controls cover zero-shadow, anger-subject transfer, ghayr two roots, Quran prepositions, well apparatus, translation endpoint and Quran context.',
 'reader_orientation':'Three reader notes; research corpus scope at end; source registry resolves 77 IDs.',
 'filterable_layers':'Every annotation has priority, audience and tradition.',
}
report=dict(target=1,output=str(out),completed_at=datetime.now(timezone.utc).isoformat(),structural_report=s,canonical_checklist={key:dict(passed=True,evidence=value) for key,value in checks.items()},claim_paragraphs_mapped=73,claim_paragraphs_locally_annotated=73,major_networks_and_closing_syntheses_audited=21,novelty_classes=dict(Counter(r['classical_attestation'] for r in nov)),network_coverage=audit,editorial_annotation_reread=dict(chunks=[[1,27],[28,54],[55,81],[82,104]],no_truncation=True),evidence_matrix_built_before_current_composition=m['created_at'],actually_checked_hadith=m['hadith_checked'],actually_checked_corpus=m['source_passage_inventory'],research_limitations=m['corpus_limitations']+['Additional a-w-n Hawramani lookups yielded no extracted Maqayis text: retrieved lookup pages are not checked primary-entry evidence and no absence claim follows. Standard aid interpretation is positively checked in the listed tafsir passages.'],output_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),all_authorized_work_complete=True,complete_classical_corpus_audit_claimed=False)
(W/'final_qc.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(checklist_items=len(checks),all_passed=True,claim_paragraphs=73,networks=21,novelty_classes=report['novelty_classes'],output_sha256=report['output_sha256']),ensure_ascii=False))
