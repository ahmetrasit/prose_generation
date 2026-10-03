import json, re, hashlib, sys
sys.path.insert(0,'/Volumes/aro/projects/prose_generation/enrichment/v1')
import validate_output as v
from pathlib import Path
R=Path('/Volumes/aro/projects/prose_generation')
base=R/'_commentary/v16/out/s107/images.r13.map3.nohft.tool.tool/images.md'
out=R/'enrichment/v1/out/107/107_enriched.sonnet-5-5.md'
rep=v.validate(base,out,107)
text=out.read_text(encoding='utf-8')
blocks=[v.parse_block(l) for l in text.split('\n') if l.startswith('{id:')]
ids=[b['id'] for b in blocks]
meal=[b for b in blocks if b['id'].startswith('S107-MEAL-')]
reg=set(re.findall(r'^- \*\*([^*]+)\*\*',text.split('\n## Kaynak kayıtları')[1],re.M))
used=set()
for b in blocks: used|=set(b['source'].split('|'))
nov=[b for b in blocks if b['type']=='novelty']
audit={
 "output_file": str(out), "output_sha256": rep['output_sha256'], "base_sha256": rep['base_sha256'],
 "validator": {"errors": rep['errors'], "warnings": rep['warnings'], "structural_qc_passed": rep['structural_qc_passed']},
 "base_paragraph_blocks_total": rep['base_blocks'], "base_blocks_preserved_exactly_in_order": rep['base_blocks_preserved_exactly_in_order'],
 "base_prose_paragraphs": rep['base_prose_paragraphs'], "original_headings_preserved": rep['original_headings'],
 "original_inline_tags": rep['original_inline_tags'], "original_inline_tags_preserved_in_order": rep['original_inline_tags_preserved_in_order'],
 "annotation_count": rep['annotation_count'], "annotations_by_type": rep['annotations_by_type'],
 "translation_review_blocks": len(meal), "translation_review_block_ids": [b['id'] for b in meal],
 "novelty_claims": len(nov), "novelty_by_classical_attestation": {k: sum(1 for b in nov if b['classical_attestation']==k) for k in sorted({b['classical_attestation'] for b in nov})},
 "every_novelty_block_has_checked_sources": all(b.get('checked_sources') for b in nov),
 "rejected_candidate_blocks": [b['id'] for b in blocks if b['role']=='rejected_candidate'],
 "contested_or_uncertain_historical_reports": {"blocks": [b['id'] for b in blocks if b.get('historicity') in ('contested','uncertain')], "named_competing_sabab_candidates": ["al-As b. Wa'il","Abu Sufyan b. Harb","al-Walid b. al-Mughira","Abu Jahl","'Amr b. 'A'idh","an unnamed stingy hypocrite","'Abdullah b. Ubayy (Hibatullah's half-Medinan view)"], "makki_madani_positions": 4},
 "hadith_blocks_by_grade": {k: sum(1 for b in blocks if b['type']=='hadith' and b.get('hadith_grade')==k) for k in ('sahih','hasan','daif','mawdu','not_assessed')},
 "unique_annotation_ids": len(ids)==len(set(ids)),
 "source_count": rep['source_count'], "all_source_ids_resolve": not (used-reg), "registry_ids_unused": sorted(reg-used),
 "translations_retrieved": ["Diyanet Isleri Baskanligi (current; official site verified)","Diyanet (old, aggregator label)","Mehmet Okuyan","Yasar Nuri Ozturk (two web variants)","Elmalili Hamdi Yazir (original + simplified)","Omer Nasuhi Bilmen","Suleyman Ates","Hayrat Nesriyat","Abdulbaki Golpinarli","Ali Bulac","Diyanet Vakfi","Suleymaniye Vakfi","Mustafa Islamoglu","Muhammed Esed (Turkish rendering)","Hasan Basri Cantay","Gultekin Onan","Ismail Hakki Izmirli","'Ibni Kesir' label on acikkuran.com (translator unverified)"],
 "translations_partially_retrieved": ["Edip Yuksel (search-result summary only; pages 403/500; low confidence)"],
 "translations_not_retrieved": ["Celal Yildirim (no page text obtained; nothing attributed)"],
 "unresolved_items": [
  "Primary hadith collection pages (sunnah.com etc.) returned 403; hadith data come via Ibn Kathir, Suyuti, Qurtubi quotations; Muslim 'tilka salat al-munafiq' graded only by collection inclusion (numbering 622/623 differs by source).",
  "Alusi read for 107:1 and 107:7 only, Ibn Atiyya for 107:1 only, Wahidi for 107:1-2 only; remaining pages not read.",
  "Turkish meal texts came through a page-summarising fetch tool; Ozturk and Suleymaniye Vakfi have two web variants whose editions could not be identified; the 'Lanet olsun' (Ozturk) and 'didinip duran' (Suleymaniye) renderings are flagged conditionally.",
  "Whether 'Ata b. Dinar' (Tabari, Ibn Kathir) or 'Ata b. Yasar' (Suyuti text) is correct for the 'an/fi' remark was not resolved.",
  "Base-file lexicon quotations were not re-verified except Maqayis sahw, da', hadd; two source-notes (S107-MET-004, S107-MET-005) record Maqayis qualifications of the base's da' da' and hadd/hadid associations; base prose left untouched.",
  "Classical text was read from cached copies of ayah pages (work/107_sonnet_5_5/sources, copied from the shared earlier source cache) and not re-downloaded; the earlier run's retrieval_index.json (URL list only) was consulted for page URLs; no annotation, matrix or output of other runs was read.",
  "Tension between 'hypocrite' identification and the Makki majority view is recorded as low-confidence inference (S107-MET-001), not resolved.",
  "Ids have gaps (e.g. no NOV-003, TAF-003/004/012) because planned blocks were merged; ids remain unique."
 ]
}
Path('audit_summary.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:audit[k] for k in ['annotation_count','annotations_by_type','novelty_claims','novelty_by_classical_attestation','translation_review_blocks','source_count','all_source_ids_resolve','unique_annotation_ids','hadith_blocks_by_grade','contested_or_uncertain_historical_reports']},ensure_ascii=False,indent=1))
