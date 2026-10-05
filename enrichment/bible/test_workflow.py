"""Offline regression tests for the isolated Bible pathway.

All work happens in temporary directories. No models, web requests or shared
enrichment artifacts are written.
"""
from contextlib import ExitStack, closing, redirect_stdout, redirect_stderr
import csv
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from xml.etree import ElementTree as ET

from enrichment.bible import agentrun as AR, blocks as B, corpus as C
from enrichment.bible import discovery as D, discovery_native as N, enrich as E
from enrichment.bible import intertext as I, pack as P, render as R, validate as V
from enrichment.bible.fetch import bible_text as BT, bible_sefaria as SF, ref_common as RC

CODE = Path(__file__).resolve().parent
AYAH = '# Ayah\n\nBirinci paragraf burada durur.\n\n<!-- v16:augment extra para=1 -->\nÖnceden eklenmiş değişmez açıklama.\n'
SURAH = ('# Surah\n\n## Birinci imge\n\nBirinci paragraf burada durur.\n\n'
         'Kaynaklar: 1:1 kelime ح م د B1\n\n## İkinci imge\n\nİkinci paragraf burada durur.\n\n'
         'Kaynaklar: 1:1 kelime ح م د B2\n')
ROW = 'strong\ttevrat\tparalel\tWLC:Gen.1.1\tcreation\tA distinct narrative reason\n'


def save(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False))


class BibleWorkflowTest(unittest.TestCase):
    def setUp(self):
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        self.root = Path(self.stack.enter_context(tempfile.TemporaryDirectory())).resolve()
        self.home = self.root / 'enrichment/bible'
        self.home.mkdir(parents=True)
        self.corpus = self.home / 'corpus'
        for module, fields in [
            (C, dict(HERE=self.home, PG=self.root, CORPUS=self.corpus,
                     INDEX=self.corpus/'corpus.sqlite', INDEX_INTERTEXT=self.corpus/'corpus.sqlite')),
            (E, dict(V2=self.home, PG=self.root, WORK=self.home/'work', OUT=self.home/'out',
                     PROMPTS=CODE/'prompts', LEDGER=self.home/'work/ledger.jsonl',
                     ERRATA=self.home/'errata.jsonl', ISLAMIC_OUT=self.root/'enrichment/v2/out')),
            (R, dict(V2=self.home)), (V, dict(V2=self.home)), (P, dict(HERE=self.home, PG=self.root)),
            (D, dict(HERE=self.home, ROOT_PG=self.root, INDEX=self.corpus/'corpus.sqlite')),
            (AR, dict(HERE=self.home, ROOT=self.root, PROJECTS=self.root/'transcripts')),
            (RC, dict(CORPUS=self.corpus)),
        ]:
            for key, value in fields.items():
                self.stack.enter_context(patch.object(module, key, value))
        self.stack.enter_context(patch.object(RC, 'http_get', side_effect=AssertionError('network forbidden in tests')))
        for name in ('SCHEMA.md', 'SCHEMA_BIBLE_CARD.md'):
            (self.home/name).write_bytes((CODE/name).read_bytes())
        sources = {
            'WLC': [dict(seg='WLC:Gen.1.1', text='בְּרֵאשִׁית בָּרָא אֱלֹהִים', book='Gen',
                         text_reading='ketiv', variant_notes=[])],
            'SBLGNT': [dict(seg='SBLGNT:Matt.1.1', text='Βίβλος γενέσεως Ἰησοῦ Χριστοῦ', book='Matt')],
            'KJV': [dict(seg='KJV:Gen.1.1', text='In the beginning', book='Gen'),
                    dict(seg='KJV:Matt.1.1', text='The book of the generation', book='Matt')],
            'QURAN': [dict(seg='QURAN:1:1', s=1, a=1, text='بِسْمِ اللَّهِ')],
        }
        for sid, records in sources.items():
            save(self.corpus/sid/'source.json', dict(id=sid, kind='quran' if sid=='QURAN' else 'intertext',
                                                   access='yerel', title=sid))
            (self.corpus/sid/'segments.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in records))
        upstream = self.root/'readonly-pack'
        (upstream/'base').mkdir(parents=True)
        (upstream/'base/surah.md').write_text(SURAH)
        (upstream/'base/1_1.md').write_text(AYAH)
        self.upstream = upstream
        save(upstream/'base.json', dict(surah=dict(path='_commentary/v16/out/s001/images.r13.x/images.md',
                                                 sha256=E.sha(SURAH)),
            ayat={'1:1':dict(path='_commentary/v16/out/1_1/DM.r13.images.r13.x/augment.augment9.opus/1_1.reading.tr.md',
                            sha256=E.sha(AYAH))}))
        save(upstream/'pack.json', dict(ayat=1))
        with redirect_stdout(io.StringIO()):
            C.build()
            P.build(1, from_pack=upstream)

    def record(self, **changes):
        return dict(dict(id='S001-TEV-PRL-001', gelenek='tevrat', tur='paralel', ayet='1:1',
                         islev='destek', iliski='tematik', durum='acik', kat='ek',
                         metin='Tekvin metnindeki başlangıç anlatısı burada anılan yaratılışla karşılaştırılabilir.',
                         kaynak='WLC:Gen.1.1', paragraf=1, capa='Birinci paragraf burada',
                         bag='benzerlik', tarihleme='kuran_oncesi', nusha='masoretik'), **changes)

    def handoff(self, target='1:1'):
        root=D.discovery_dir(1,'test')
        root.mkdir(parents=True,exist_ok=True)
        path=root/(target.replace(':','_')+'.merged.tsv')
        base=R.target_page(1,target)[2]
        D.write_handoff(path,[],base['sha256'],{})
        save(root.parent/'selected.json',{target:str(path.relative_to(root.parent))})
        save(root/'prefetch.json',dict(complete=True,lists={path.name:C.sha256(path)},candidates=[],source_hashes={}))
        return path

    def call(self, records):
        self.handoff()
        d=E.call_dir(1,'1:1')
        d.mkdir(parents=True)
        (d/'annotations.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records))
        inputs=E.bible_inputs(1,'1:1')
        started=dict(bible_inputs=inputs,base_sha256=E.sha(AYAH),
                     pack_sha256=C.sha256(E.wd(1)/'pack/pack.json'))
        return d,started

    def completed_discovery(self,t,model='luna',rows=ROW):
        d=D.tdir(1,t['target'],'test')/model
        d.mkdir(parents=True,exist_ok=True)
        for name,text in [('list.tsv',rows),('turn1.list.tsv',rows),('prompt.md','brief'),('package.md',t['prose'])]:
            (d/name).write_text(text)
        log=dict(status='ok',append_only=True,tool_audit_reviewed=True,turn2=dict(completed=True),
                 base_sha256=t['base_sha256'],target=t['target'],runner='agent',model=D.MODELS[model],effort=D.EFFORT)
        for filename,field in [('list.tsv','list_sha256'),('turn1.list.tsv','turn1_sha256'),
                               ('prompt.md','prompt_sha256'),('package.md','package_sha256')]:
            log[field]=C.sha256(d/filename)
        save(d/'run.log.json',log)
        return d

    def test_hebrew_and_greek_search_use_original_text(self):
        for query,sid,want in [('בראשית','WLC','WLC:Gen.1.1'),('βιβλος','SBLGNT','SBLGNT:Matt.1.1')]:
            with closing(C.connect()) as con:
                rows=con.execute('SELECT seg FROM f JOIN seg ON seg.id=f.rowid WHERE f MATCH ? AND src=?',
                                 (C.norm(query),sid)).fetchall()
            self.assertEqual(rows,[(want,)])

    def test_wlc_notes_are_separate_and_positioned(self):
        xml=f'''<verse xmlns="{BT.NS['o']}" osisID="Ezek.1.8"><w lemma="x">וידו</w>
            <note type="variant"><rdg type="qere"><w>וִידֵי</w></rdg></note>
            <w>אדם</w><seg type="x-maqqef">־</seg><w>יד</w><seg>׃</seg></verse>'''
        result=BT.wlc_verse(ET.fromstring(xml))
        self.assertEqual(result['text'],'וידו אדם־יד׃')
        self.assertNotIn('וִידֵי',result['text'])
        self.assertEqual(result['variant_notes'][0]['after_word'],1)
        self.assertEqual(result['variant_notes'][0]['readings'][0]['text'],'וִידֵי')

    def test_index_rejects_old_wlc_without_overwriting_index(self):
        before=C.sha256(C.INDEX)
        path=self.corpus/'WLC/segments.jsonl'
        path.write_text(json.dumps(dict(seg='WLC:Gen.1.1',text='mixed'))+'\n')
        with self.assertRaisesRegex(ValueError,'mixed-variant'),redirect_stdout(io.StringIO()): C.build()
        self.assertEqual(C.sha256(C.INDEX),before)

    def test_bible_namespace_and_wrong_tradition(self):
        self.assertEqual(V.check_records(1,'1:1',[self.record()])[1],[])
        for change in [dict(id='S001-PRL-001'),dict(id='S001-TEV-PAR-001'),dict(kaynak='SBLGNT:Matt.1.1'),
                       dict(kaynak='KJV:Matt.1.1')]:
            self.assertTrue(V.check_records(1,'1:1',[self.record(**change)])[1],change)

    def test_new_testament_record_and_segment_classification(self):
        r=self.record(id='S001-INC-MTF-001',tur='motif',gelenek='incil',kaynak='SBLGNT:Matt.1.1',nusha='yunanca_ahit')
        self.assertEqual(V.check_records(1,'1:1',[r])[1],[])
        self.assertEqual(I.metadata('KJV',{'book':'Matt','seg':'KJV:Matt.1.1'})['gelenek'],['incil'])
        self.assertTrue(I.metadata('CORPUSCORANICUM-INTERTEXT',{'category':'unknown'})['background_only'])

    def test_translation_alone_and_wrong_witness_do_not_pass(self):
        self.assertTrue(V.check_records(1,'1:1',[self.record(kaynak='KJV:Gen.1.1')])[1])
        self.assertTrue(V.check_records(1,'1:1',[self.record(nusha='pesitta')])[1])
        self.assertEqual(V.check_records(1,'1:1',[self.record(kaynak='KJV:Gen.1.1|WLC:Gen.1.1')])[1],[])

    def test_prompt_names_only_available_bible_inputs(self):
        prompt=E.build_prompt(1,'1:1',E.call_dir(1,'1:1'))
        self.assertIn('numbered/1_1.md',prompt)
        self.assertNotIn('numbered/1_1.ehlikitap.md',prompt)
        self.assertNotIn('enrichment/v2',prompt)
        self.assertNotIn('PACK/ayah/',prompt)
        self.assertIn('SCHEMA_BIBLE_CARD.md',prompt)

    def test_discovery_uses_augment9_and_rejects_ambiguous_references(self):
        self.assertIn('Önceden eklenmiş',D.targets_of(1)[0]['prose'])
        path=self.root/'list.tsv'
        path.write_text(ROW.replace('WLC:Gen.1.1','Gen.1.1'))
        self.assertTrue(D.parse_rows(path)[1])
        path.write_text(ROW.replace('WLC:Gen.1.1','WLC:Gen.1.999'))
        self.assertTrue(D.parse_rows(path)[1])
        path.write_text('')
        self.assertEqual(D.parse_rows(path),([],[]))
        self.assertTrue(D.parse_rows(self.root/'absent.tsv')[1])

    def test_followup_preserves_first_turn_and_distinct_reasons(self):
        d=self.root/'followup'; d.mkdir()
        (d/'list.tsv').write_text(ROW); (d/'turn1.list.tsv').write_text(ROW)
        second=ROW.replace('strong','medium').replace('A distinct narrative reason','Another useful reason')
        (d/'followup.tsv').write_text(ROW+second)
        result=N.consolidate(d)
        self.assertEqual(result['unique_additions'],1)
        self.assertEqual((d/'list.tsv').read_text(),ROW+second)
        (d/'list.tsv').write_text('')
        with self.assertRaisesRegex(ValueError,'changed'): N.consolidate(d)

    def test_failed_or_modified_discovery_cannot_merge(self):
        t=D.targets_of(1)[0]; d=self.completed_discovery(t)
        log=json.loads((d/'run.log.json').read_text());log['status']='error';save(d/'run.log.json',log)
        with self.assertRaisesRegex(ValueError,'completed'): D.merge(1,[t],'test',['luna'])
        self.completed_discovery(t)
        (d/'list.tsv').write_text('')
        with self.assertRaisesRegex(ValueError,'changed'): D.merge(1,[t],'test',['luna'])
        self.assertFalse((d.parent.parent/'1_1.merged.tsv').exists())

    def test_sections_aggregate_to_surah_handoff(self):
        targets=[t for t in D.targets_of(1) if t['target'].startswith('sec')]
        for t in targets:
            for model in ('luna','terra'): self.completed_discovery(t,model)
        with redirect_stdout(io.StringIO()): paths=D.merge(1,targets,'test')
        path=next(p for p in paths if p.name=='surah.merged.tsv')
        rows=list(csv.DictReader(io.StringIO(path.read_text()),delimiter='\t'))
        self.assertEqual(len(rows),2)
        self.assertEqual(len(json.loads(rows[0]['evidence'])),2)
        self.assertEqual(E.discovery_list(1,'surah'),path)

    def test_discovery_merge_keeps_multiple_link_kinds(self):
        t=D.targets_of(1)[0]
        self.completed_discovery(t,rows=ROW+ROW.replace('paralel','motif').replace('creation','formula'))
        with redirect_stdout(io.StringIO()): paths=D.merge(1,[t],'test',['luna'])
        row=next(csv.DictReader(io.StringIO(paths[0].read_text()),delimiter='\t'))
        self.assertEqual(row['kinds'],'motif|paralel')
        self.assertEqual(len(json.loads(row['evidence'])),2)

    def test_pack_rebuild_guards_page_and_discovery_calls(self):
        for relative in ('ehlikitap.1_1.opus.high','discovery/test/1_1/luna'):
            d=E.wd(1)/relative;save(d/'started.json',{})
            with self.assertRaisesRegex(ValueError,'active'): P.build(1,force=True,from_pack=self.upstream)
            save(d/'dead.json',{})

    def test_changed_numbered_input_blocks_spawn(self):
        self.handoff()
        p=E.wd(1)/'pack/numbered/1_1.md';p.write_text(p.read_text()+'changed')
        with self.assertRaisesRegex(ValueError,'pack input changed'): E.bible_inputs(1,'1:1')

    def test_stale_source_or_prefetch_blocks_spawn(self):
        p=self.handoff()
        report=p.parent/'prefetch.json';data=json.loads(report.read_text());data['complete']=False;save(report,data)
        with self.assertRaisesRegex(ValueError,'prefetch'): E.bible_inputs(1,'1:1')
        self.handoff()
        src=self.corpus/'SBLGNT/segments.jsonl';src.write_text(src.read_text()+'\n')
        with self.assertRaisesRegex(ValueError,'rebuild'): E.bible_inputs(1,'1:1')

    def test_input_drift_after_start_blocks_acceptance(self):
        d,start=self.call([self.record()])
        path=E.discovery_list(1,'1:1');path.write_text(path.read_text()+'\n')
        self.assertFalse(E.finish(1,'1:1',d,started=start)['ok'])
        self.assertFalse(E.accepted(1,'1:1'))

    def test_all_dropped_fails_and_deliberate_empty_needs_reason(self):
        d,start=self.call([self.record(id='bad')])
        result=E.finish(1,'1:1',d,started=start)
        self.assertFalse(result['ok']);self.assertEqual(result['dropped'],1)
        (d/'annotations.jsonl').write_text('')
        self.assertFalse(E.finish(1,'1:1',d,started=start)['ok'])
        save(d/'gaps.json',dict(no_findings_reason='No verified parallel in the checked texts.'))
        self.assertTrue(E.finish(1,'1:1',d,started=start)['ok'])

    def test_accepted_snapshot_survives_raw_edits_but_rejects_tampering(self):
        d,start=self.call([self.record()])
        self.assertTrue(E.finish(1,'1:1',d,started=start)['ok'])
        (d/'annotations.jsonl').write_text('broken raw annotation')
        with redirect_stdout(io.StringIO()): self.assertTrue(E.merge_page(1,'1:1'))
        out=E.OUT/'s001/1_1.ehlikitap.md'
        saved=json.loads(out.with_suffix('.json').read_text())
        snapshot=self.root/saved['accepted_annotations']; snapshot.write_text(snapshot.read_text()+'\n')
        with redirect_stdout(io.StringIO()): self.assertFalse(E.merge_page(1,'1:1'))

    def test_complete_handoff_accepts_both_languages_after_augment(self):
        greek=self.record(id='S001-INC-MTF-001',gelenek='incil',tur='motif',
                          kaynak='SBLGNT:Matt.1.1',nusha='yunanca_ahit')
        d,start=self.call([self.record(),greek])
        result=E.finish(1,'1:1',d,started=start)
        self.assertTrue(result['ok']);self.assertEqual(result['kept'],2)
        page=(E.OUT/'s001/1_1.ehlikitap.md').read_text()
        self.assertLess(page.index('Önceden eklenmiş'),page.index('S001-TEV-PRL-001'))
        self.assertLess(page.index('S001-TEV-PRL-001'),page.index('S001-INC-MTF-001'))
        self.assertFalse(E.finish(1,'1:1',d,started=start)['ok'])

    def test_merge_rejects_duplicate_ids_across_accepted_layers(self):
        d,start=self.call([self.record()]);E.finish(1,'1:1',d,started=start)
        page=E.OUT/'s001/1_1.ehlikitap.md'
        other=E.ISLAMIC_OUT/'s001/1_1.md';other.parent.mkdir(parents=True)
        other.write_bytes(page.read_bytes());other.with_suffix('.json').write_bytes(page.with_suffix('.json').read_bytes())
        with redirect_stdout(io.StringIO()) as output:
            self.assertFalse(E.merge_page(1,'1:1'))
        self.assertIn('duplicate IDs',output.getvalue())

    def test_merge_rejects_changed_accepted_page_or_base(self):
        d,start=self.call([self.record()]);E.finish(1,'1:1',d,started=start)
        page=E.OUT/'s001/1_1.ehlikitap.md';page.write_text(page.read_text()+'alteration')
        with redirect_stdout(io.StringIO()): self.assertFalse(E.merge_page(1,'1:1'))
        p=E.wd(1)/'pack/base/1_1.md';p.write_text(p.read_text()+'changed')
        with self.assertRaisesRegex(ValueError,'base bytes'): R.target_page(1,'1:1')

    def test_merge_reads_accepted_islamic_page_without_writing_it(self):
        r=dict(id='S001-KNT-001',gelenek='islami',tur='kaynak_notu',ayet='1:1',islev='destek',
               iliski='tematik',durum='acik',kat='ek',metin='Eski kabul edilmiş açıklama.',kaynak='OLD:1',
               paragraf=1,capa='Birinci paragraf burada')
        page=E.ISLAMIC_OUT/'s001/1_1.md';page.parent.mkdir(parents=True)
        original,_=R.render_page(AYAH,[r],'<!-- accepted -->',None,{'OLD':dict(title='Old source')})
        page.write_text(original)
        ann=self.root/'old-call/annotations.jsonl';ann.parent.mkdir();ann.write_text(json.dumps(r)+'\n')
        save(page.with_suffix('.json'),dict(page_sha256=C.sha256(page),base=R.target_page(1,'1:1')[2],
                                           annotations=str(ann),kept=1))
        digest=C.sha256(page)
        with redirect_stdout(io.StringIO()): self.assertTrue(E.merge_page(1,'1:1'))
        self.assertEqual(C.sha256(page),digest)
        self.assertIn('Old source',(E.OUT/'s001/1_1.merged.md').read_text())

    def test_missing_transcript_and_outside_tool_use_fail(self):
        d,start=self.call([])
        start.update(surah=1,target='1:1',model_id='claude-opus-5-5',effort='high')
        with redirect_stdout(io.StringIO()): AR.prepare(d,'brief',start)
        self.assertTrue(AR.finish(d)['is_error'])
        calls=[dict(name='Read',input=dict(file_path=str(E.ISLAMIC_OUT/'s001/1_1.md'))),
               dict(name='Write',input=dict(file_path=str(d.with_name(d.name+'-other')/'annotations.jsonl')))]
        self.assertEqual(len(AR.tool_use_outside_rule(d,'annotations.jsonl',calls)),2)
        self.assertTrue(AR.allowed_command(f'python3 {self.home}/corpus.py search בראשית --src WLC',d))
        self.assertFalse(AR.allowed_command(f'python3 {self.home}/corpus.py build',d))

    def test_source_mutation_guard(self):
        d=E.call_dir(1,'1:1');save(d/'started.json',{})
        with self.assertRaisesRegex(ValueError,'active'): RC.Source('WLC')
        with self.assertRaisesRegex(SystemExit,'running'): C.build()
        with self.assertRaisesRegex(ValueError,'active'): D.prefetch([],2)
        with self.assertRaisesRegex(ValueError,'active'): D.merge(1,[],'test')

    def test_prefetch_records_failure_and_missing_witness(self):
        path=self.handoff()
        rows=[dict(ref='WLC:Gen.1.1',tier='strong',tradition='tevrat',kinds='paralel',basis='x',
                   explanations='reason',target='1:1',evidence='[]'),
              dict(ref='Unknown homily',tier='weak',tradition='incil',kinds='motif',basis='y',
                   explanations='reason',target='1:1',evidence='[]')]
        D.write_handoff(path,rows,E.sha(AYAH),{})
        with patch.object(SF,'cmd_related',side_effect=TimeoutError('offline')),redirect_stdout(io.StringIO()):
            report=D.prefetch([path],2)
        self.assertFalse(report['complete'])
        self.assertEqual(len(report['errors']),1)
        self.assertIn('Unknown homily',report['missing'])

    def test_sefaria_distinguishes_empty_text_and_service_failure(self):
        with patch.object(RC.Source,'fetch',return_value=(503,b'error')),redirect_stdout(io.StringIO()),redirect_stderr(io.StringIO()):
            report=SF.cmd_text(['Genesis 1:1'])
        self.assertEqual(len(report['errors']),1)
        with patch.object(RC.Source,'fetch',return_value=(200,b'{"versions":[]}')),redirect_stdout(io.StringIO()),redirect_stderr(io.StringIO()):
            report=SF.cmd_text(['Genesis 1:1'])
        self.assertEqual(report['errors'],[]);self.assertEqual(report['missing'],['Genesis 1:1'])

    def test_transient_http_error_is_retried_without_reusing_failed_cache(self):
        src=RC.Source('SEFARIA')
        with patch.object(RC,'http_get',side_effect=[(503,b'error','url'),(200,b'{}','url')]) as fetch:
            self.assertEqual(src.fetch('url','retry.json',quiet=True)[0],503)
            self.assertEqual(src.fetch('url','retry.json',quiet=True)[0],200)
            self.assertEqual(src.fetch('url','retry.json',quiet=True)[0],200)
        self.assertEqual(fetch.call_count,2)


if __name__=='__main__':
    unittest.main()
