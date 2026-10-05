"""Offline regression tests for the isolated Bible pathway.

All work happens in temporary directories. No models, web requests or shared
enrichment artifacts are written.
"""
from contextlib import ExitStack, closing, redirect_stdout, redirect_stderr
import csv
import io
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch
from xml.etree import ElementTree as ET

from enrichment.bible import agentrun as AR, blocks as B, corpus as C
from enrichment.bible import discovery as D, discovery_native as N, enrich as E
from enrichment.bible import check_discovery as DC, discovery_repair as DR, discovery_report as REPORT, verdicts as VR
from enrichment.bible import discovery_first_repair as FR
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
        targets=[t for t in D.targets_of(1) if t['target']==target or (target=='surah' and t['target'].startswith('sec'))]
        for t in targets:
            for model in D.MODELS: self.completed_discovery(t,model,rows='')
        with redirect_stdout(io.StringIO()): paths=D.merge(1,targets,'test')
        path=next(p for p in paths if p.name==target.replace(':','_')+'.merged.tsv')
        root=path.parent
        save(root/'prefetch.json',dict(complete=True,lists={path.name:C.sha256(path)},candidates=[],source_hashes={}))
        return path

    def call(self, records):
        self.handoff()
        d=E.call_dir(1,'1:1')
        d.mkdir(parents=True)
        (d/'annotations.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records))
        save(d/'gaps.json',dict(missing_sources=[],not_found=[],unresolved=[]))
        grouped={}
        for r in records: grouped.setdefault(r['kaynak'],[]).append(r)
        verdicts=[dict(connection_id=None,origin='research',ref=loc,status='accepted',reason='Verified connection.',
                       paragraphs=[r['paragraf'] for r in rs],evidence=loc.split('|'),annotations=[r['id'] for r in rs])
                  for loc,rs in grouped.items()]
        (d/'verdicts.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in verdicts))
        self.tool_gets(d,{loc for r in records for loc in r['kaynak'].split('|')})
        inputs=E.bible_inputs(1,'1:1')
        started=dict(bible_inputs=inputs,base_sha256=E.sha(AYAH),
                     pack_sha256=C.sha256(E.wd(1)/'pack/pack.json'))
        return d,started

    def tool_gets(self,d,refs):
        save(d/'tool_calls.json',[dict(name='Bash',input=dict(command=f'python3 {self.home}/corpus.py get {ref}'),
                                      result=f'== {ref}\nOriginal source text\n',is_error=False) for ref in refs])

    def completed_discovery(self,t,model='luna',rows=ROW,followup='',run_tag='test'):
        d=D.tdir(1,t['target'],run_tag)/model
        d.mkdir(parents=True,exist_ok=True)
        for name,text in [('list.tsv',rows),('turn1.list.tsv',rows),('prompt.md','brief'),('package.md',t['prose']),
                          ('followup.tsv',followup),('spawn.md','Independent inputs only'),('followup.txt','Exact followup')]:
            (d/name).write_text(text)
        inp={k:t[k] for k in ('target','base_path','base_sha256','inputs')}
        save(d/'input.json',inp)
        start=dict(**inp,runner='agent',model=D.MODELS[model],effort=D.EFFORT,protocol=D.PROTOCOL,
                   run_tag=run_tag,agent_path=f'/root/test_{model}')
        for filename,field in [('input.json','input_sha256'),('spawn.md','spawn_sha256'),('followup.txt','followup_text_sha256'),
                               ('prompt.md','prompt_sha256'),('package.md','package_sha256')]:
            start[field]=C.sha256(d/filename)
        save(d/'started.json',start)
        save(d/'turn1.json',dict(rows=len(rows.splitlines()),completed_at='1',sha256=C.sha256(d/'turn1.list.tsv')))
        session=dict(agent_path=start['agent_path'],agent_id=f'test_{model}',transcript='fixture')
        save(d/'session.json',session);save(d/'tool_calls.json',[])
        done=[dict(timestamp='1'),dict(timestamp='2')]
        contexts=[dict(model=D.MODELS[model],effort=D.EFFORT)]*2
        N.finish_run(d,start,session,[],done,contexts,{},[dict(matches=True,encrypted=False)],[])
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
        self.completed_discovery(t,'terra')
        log=json.loads((d/'run.log.json').read_text());log['status']='error';save(d/'run.log.json',log)
        with self.assertRaisesRegex(ValueError,'completed'): D.merge(1,[t],'test')
        self.completed_discovery(t)
        (d/'list.tsv').write_text('')
        with self.assertRaisesRegex(ValueError,'changed'): D.merge(1,[t],'test')
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
        self.completed_discovery(t,'terra',rows='')
        with redirect_stdout(io.StringIO()): paths=D.merge(1,[t],'test')
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
        (d/'verdicts.jsonl').write_text('')
        save(d/'tool_calls.json',[])
        self.assertFalse(E.finish(1,'1:1',d,started=start)['ok'])
        save(d/'gaps.json',dict(missing_sources=[],not_found=[],unresolved=[],
                                no_findings_reason='No verified parallel in the checked texts.'))
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

    def test_discovery_package_preserves_lexical_members_and_scope(self):
        ayah,sec1,sec2=D.targets_of(1)
        package=D.package(1,ayah,{'1:1':'بسم الله'})
        self.assertIn('ح م د\tB1\tBirinci imge',package)
        self.assertIn('ح م د\tB2\tİkinci imge',package)
        self.assertIn('Önceden eklenmiş',package)
        self.assertEqual([m['branch'] for m in sec1['members']],['B1'])
        self.assertEqual([m['branch'] for m in sec2['members']],['B2'])

    def test_single_reader_merge_is_refused(self):
        t=D.targets_of(1)[0];self.completed_discovery(t)
        with self.assertRaisesRegex(ValueError,'both Luna and Terra'): D.merge(1,[t],'test',['luna'])
        with self.assertRaises(FileNotFoundError): D.merge(1,[t],'test')

    def test_distinct_reasons_survive_repeats_and_receive_separate_ids(self):
        t=D.targets_of(1)[0]
        second=ROW.replace('paralel','motif').replace('A distinct narrative reason','A formula connection')
        d=self.completed_discovery(t,followup=ROW.replace('strong','weak')+second+second)
        self.completed_discovery(t,'terra',rows=second)
        cons=json.loads((d/'consolidation.json').read_text())
        self.assertEqual(cons['raw_proposal_rows'],3)
        self.assertEqual(cons['unique_additions'],1)
        self.assertEqual([r['retained']['phase'] for r in cons['repeated_proposals']],[1,2])
        self.assertEqual((d/'list.tsv').read_text(),ROW+second)
        with redirect_stdout(io.StringIO()): path=D.merge(1,[t],'test')[0]
        expected=VR.candidates(path)
        self.assertEqual(len(expected),2)
        meta=json.loads(path.with_suffix('.json').read_text())
        self.assertEqual(len(meta['findings'][0]['repeats']),2)

    def test_raw_followup_and_review_hashes_are_rechecked_at_merge(self):
        t=D.targets_of(1)[0]
        d=self.completed_discovery(t);self.completed_discovery(t,'terra')
        for filename in ('followup.tsv','validation.json','followup.txt','session.events.jsonl'):
            with self.subTest(filename=filename):
                original=(d/filename).read_bytes()
                (d/filename).write_bytes(original+b'\n')
                with self.assertRaisesRegex(ValueError,'changed'): D.merge(1,[t],'test')
                (d/filename).write_bytes(original)

    def test_changed_lexical_source_blocks_discovery(self):
        t=D.targets_of(1)[0];d=self.completed_discovery(t)
        path=E.wd(1)/'pack/base/surah.md';path.write_text(SURAH+'\n')
        with self.assertRaisesRegex(ValueError,'inputs changed'): D.checked_run(d,t)

    def test_legacy_run_is_not_silently_upgraded(self):
        t=D.targets_of(1)[0];d=self.completed_discovery(t)
        log=json.loads((d/'run.log.json').read_text());log.pop('protocol');save(d/'run.log.json',log)
        with self.assertRaisesRegex(ValueError,'legacy'): D.checked_run(d,t)

    def test_missing_followup_is_not_an_empty_success(self):
        t=D.targets_of(1)[0];d=self.completed_discovery(t)
        (d/'followup.tsv').unlink()
        with self.assertRaisesRegex(ValueError,'missing deliverable'): N.consolidation_plan(d)

    def test_wording_review_checks_hebrew_greek_and_qere_separately(self):
        with closing(sqlite3.connect(C.INDEX)) as con:
            con.execute('UPDATE seg SET extra=? WHERE seg=?',
                        (json.dumps(dict(variant_notes=[dict(after_word=1,readings=[dict(text='וידי',type='qere')])])),
                         'WLC:Gen.1.1'))
            con.commit()
        path=self.root/'wording.tsv'
        path.write_text(ROW.replace('A distinct narrative reason','בראשית ברא; qere וידי')+
                        'medium\tincil\tmotif\tSBLGNT:Matt.1.1\tformula\tβιβλος γενεσεως; uncertain πατηρ\n')
        report=DC.check(path)
        self.assertEqual(report['schema_errors'],[])
        self.assertEqual(len(report['findings']),2)
        self.assertEqual(report['findings'][0]['variant_matches'][0]['reading']['type'],'qere')
        self.assertEqual(report['findings'][1]['language'],'Greek')
        self.assertIn('no semantic',report['limits'])

    def test_explicit_mixed_attempt_selection_preserves_provenance(self):
        targets=[t for t in D.targets_of(1) if t['target'].startswith('sec')]
        attempts={'sec1':'first','sec2':'second'}
        for t in targets:
            for model in D.MODELS: self.completed_discovery(t,model,run_tag=attempts[t['target']])
        with redirect_stdout(io.StringIO()): paths=D.merge(1,targets,'combined',attempts=attempts)
        path=next(p for p in paths if p.name=='surah.merged.tsv')
        self.assertTrue(D.verify_handoff(path,1,'surah'))
        meta=json.loads(path.with_suffix('.json').read_text())
        self.assertEqual({r['run_tag'] for r in meta['provenance']},{'first','second'})

    def test_report_surfaces_partial_runs_and_does_not_launch_or_merge(self):
        t=D.targets_of(1)[0]
        self.completed_discovery(t,followup=ROW)
        bad=self.completed_discovery(t,'terra',followup=ROW.replace('Gen.1.1','Gen.1.999'))
        report=REPORT.report(1,'test',[t])
        self.assertFalse(report['ready_for_merge'])
        self.assertEqual(report['jobs'][0]['initial'],1)
        self.assertEqual(len(report['jobs'][0]['repeats']),1)
        self.assertEqual(report['jobs'][1]['status'],'partial')
        self.assertIn('unknown verse',report['jobs'][1]['consolidation_error'])
        self.assertFalse(report['opus_started']);self.assertEqual(report['model_calls'],0)
        self.assertFalse((bad.parent.parent/'1_1.merged.tsv').exists())

    def repair_fixture(self):
        t=D.targets_of(1)[0]
        raw=ROW.replace('Gen.1.1','Gen.1.999')
        d=self.completed_discovery(t,followup=raw)
        changes=[dict(line=1,before=raw.strip().split('\t'),after=ROW.strip().split('\t'),
                      reason='Reference typo; the preserved explanation names the available verse.')]
        return t,d,raw,changes

    def test_recorded_repair_preserves_failed_run_raw_grades_and_first_turn(self):
        t,d,raw,changes=self.repair_fixture()
        failed=(d/'run.log.json').read_bytes()
        DR.propose(d,changes)
        with self.assertRaisesRegex(ValueError,'approval'): DR.accept(d,'')
        DR.accept(d,'User approved the displayed one-line reference correction.')
        self.assertEqual((d/'followup.tsv').read_text(),raw)
        self.assertEqual((d/'turn1.list.tsv').read_text(),ROW)
        self.assertEqual((d/'run.failed.log.json').read_bytes(),failed)
        self.assertEqual(len(D.checked_run(d,t)),1)
        log=json.loads((d/'run.log.json').read_text())
        self.assertEqual(log['status'],'accepted')
        self.assertEqual(log['consolidation']['repeated_proposals'][0]['retained']['phase'],1)
        self.assertEqual(log['repair']['model_calls'],0)
        (d/'run.failed.log.json').write_bytes(failed+b'\n')
        with self.assertRaisesRegex(ValueError,'changed'): D.checked_run(d,t)

    def test_repair_cannot_regrade_rewrite_or_hide_protocol_failures(self):
        t,d,raw,changes=self.repair_fixture()
        for field,value in ((0,'weak'),(5,'A newly invented explanation')):
            candidate=json.loads(json.dumps(changes));candidate[0]['after'][field]=value
            with self.assertRaisesRegex(ValueError,'preserve'): DR.repaired_bytes(raw.encode(),candidate)
        log=json.loads((d/'run.log.json').read_text());log['protocol_findings']=['retrieval during follow-up']
        save(d/'run.log.json',log)
        with self.assertRaisesRegex(ValueError,'protocol'): DR.propose(d,changes)

    def test_unrecorded_proposed_repair_change_is_refused(self):
        _,d,_,changes=self.repair_fixture()
        DR.propose(d,changes)
        (d/'followup.repair.proposed.tsv').write_text(ROW.replace('strong','weak'))
        with self.assertRaisesRegex(ValueError,'unrecorded'): DR.accept(d,'Approval of original proposal')
        self.assertFalse((d/'run.failed.log.json').exists())

    def test_changed_followup_message_blocks_finish_provenance(self):
        t=D.targets_of(1)[0];d=self.completed_discovery(t)
        (d/'followup.txt').write_text('Unapproved extra instructions')
        start=json.loads((d/'started.json').read_text())
        self.assertFalse(N.inputs_unchanged(d,start))

    def discovered_page(self):
        d,start=self.call([self.record()])
        t=D.targets_of(1)[0]
        for model in D.MODELS: self.completed_discovery(t,model,rows=ROW)
        with redirect_stdout(io.StringIO()): path=D.merge(1,[t],'test')[0]
        save(path.parent/'prefetch.json',dict(complete=True,lists={path.name:C.sha256(path)},candidates=[],source_hashes={}))
        start['bible_inputs']=E.bible_inputs(1,'1:1')
        cid=next(iter(VR.candidates(path)))
        verdict=dict(connection_id=cid,ref='WLC:Gen.1.1',status='accepted',reason='Specific original-text connection.',
                     paragraphs=[1],evidence=['WLC:Gen.1.1'],annotations=[self.record()['id']])
        (d/'verdicts.jsonl').write_text(json.dumps(verdict)+'\n')
        return d,start,path,verdict

    def test_candidate_verdict_and_evidence_are_required_for_acceptance(self):
        d,start,path,verdict=self.discovered_page()
        (d/'verdicts.jsonl').write_text('')
        result=E.finish(1,'1:1',d,started=start)
        self.assertFalse(result['ok']);self.assertIn('1 discovery connections have no verdict',result['verdict_errors'])
        (d/'verdicts.jsonl').write_text(json.dumps(verdict)+'\n')
        self.assertTrue(E.finish(1,'1:1',d,started=start)['ok'])

    def test_unopened_or_translation_only_evidence_cannot_verify_candidate(self):
        d,start,path,verdict=self.discovered_page()
        save(d/'tool_calls.json',[])
        report=VR.check(d,path,AYAH,[self.record()])
        self.assertTrue(any('not opened' in e for e in report['errors']))
        self.assertTrue(VR.check(d,path,AYAH,[self.record()],require_opened=False)['ok'])
        verdict['evidence']=['KJV:Gen.1.1']
        self.tool_gets(d,verdict['evidence'])
        (d/'verdicts.jsonl').write_text(json.dumps(verdict)+'\n')
        report=VR.check(d,path,AYAH,[self.record()])
        self.assertTrue(any('original-language' in e for e in report['errors']))

    def test_lookup_commands_without_shown_text_do_not_count_as_evidence(self):
        refs,opened=VR.lookup_audit([dict(name='Bash',input=dict(command='python3 enrichment/bible/corpus.py get WLC:Gen.1.1'),
                                       result='NOTE: 1 segment not shown: WLC:Gen.1.1(80)')])
        self.assertEqual(refs,{'WLC:Gen.1.1'});self.assertEqual(opened,set())
        _,opened=VR.lookup_audit([dict(name='Bash',input=dict(command='python3 enrichment/bible/corpus.py get WLC:Gen.1.1'),
                                     result='== WLC:Gen.1.1: NOT FOUND\n')])
        self.assertEqual(opened,set())

    def test_every_extra_lookup_needs_a_verdict(self):
        d,_,path,_=self.discovered_page()
        self.tool_gets(d,['WLC:Gen.1.1','SBLGNT:Matt.1.1'])
        report=VR.check(d,path,AYAH,[self.record()])
        self.assertEqual(report['lookups_without_verdicts'],['SBLGNT:Matt.1.1'])
        extra=dict(connection_id=None,origin='research',ref='SBLGNT:Matt.1.1',status='rejected',
                   reason='Context only, no independent connection.',paragraphs=[],evidence=['SBLGNT:Matt.1.1'],annotations=[])
        with (d/'verdicts.jsonl').open('a') as stream: stream.write(json.dumps(extra)+'\n')
        self.assertTrue(VR.check(d,path,AYAH,[self.record()])['ok'])

    def test_unresolved_verdict_requires_a_specific_gap(self):
        d,start,path,verdict=self.discovered_page()
        verdict.update(status='unresolved',annotations=[],evidence=[],paragraphs=[],reason='Witness question remains unresolved.')
        (d/'annotations.jsonl').write_text('')
        (d/'verdicts.jsonl').write_text(json.dumps(verdict)+'\n')
        self.assertFalse(VR.check(d,path,AYAH,[])['ok'])
        save(d/'gaps.json',dict(missing_sources=[],not_found=[],unresolved=['WLC:Gen.1.1: witness question'],
                                no_findings_reason='The candidate remains unresolved.'))
        self.assertTrue(E.finish(1,'1:1',d,started=start)['ok'])

    def test_verdict_cannot_point_to_a_dropped_annotation(self):
        d,_,path,_=self.discovered_page()
        report=VR.check(d,path,AYAH,[])
        self.assertTrue(any('absent or dropped' in e for e in report['errors']))

    def test_empty_page_must_still_judge_all_candidates(self):
        d,start,path,verdict=self.discovered_page()
        (d/'annotations.jsonl').write_text('')
        (d/'verdicts.jsonl').write_text('')
        save(d/'gaps.json',dict(missing_sources=[],not_found=[],unresolved=[],no_findings_reason='No independent addition.'))
        self.assertFalse(E.finish(1,'1:1',d,started=start)['ok'])
        verdict.update(status='rejected',annotations=[],paragraphs=[],reason='The proposed connection is too broad after checking the verse.')
        (d/'verdicts.jsonl').write_text(json.dumps(verdict)+'\n')
        self.assertTrue(E.finish(1,'1:1',d,started=start)['ok'])

    def test_verdict_snapshots_are_immutable_and_checked_on_merge(self):
        d,start,_,_=self.discovered_page()
        self.assertTrue(E.finish(1,'1:1',d,started=start)['ok'])
        page=E.OUT/'s001/1_1.ehlikitap.md'
        manifest=json.loads(page.with_suffix('.json').read_text())
        self.assertEqual(set(manifest['verdict_artifacts']),{'verdicts.jsonl','gaps.json','verdict_report.json'})
        (d/'verdicts.jsonl').write_text('raw call changed later')
        with redirect_stdout(io.StringIO()): self.assertTrue(E.merge_page(1,'1:1'))
        snapshot=self.root/manifest['verdict_artifacts']['verdicts.jsonl']['path']
        snapshot.write_text(snapshot.read_text()+'\n')
        with redirect_stdout(io.StringIO()): self.assertFalse(E.merge_page(1,'1:1'))

    def test_selection_drift_during_page_call_blocks_acceptance(self):
        d,start,_,_=self.discovered_page()
        save(E.wd(1)/'discovery/selected.json',{})
        result=E.finish(1,'1:1',d,started=start)
        self.assertFalse(result['ok']);self.assertIn('input changed',result['check'])

    def test_page_author_reads_handoff_but_not_reader_transcripts(self):
        d,start,path,_=self.discovered_page()
        start.update(surah=1,target='1:1')
        save(d/'started.json',start)
        transcript=D.tdir(1,'1:1','test')/'luna/session.events.jsonl'
        calls=[dict(name='Read',input=dict(file_path=str(path))),
               dict(name='Read',input=dict(file_path=str(path.with_suffix('.json')))),
               dict(name='Read',input=dict(file_path=str(transcript)))]
        outside=AR.tool_use_outside_rule(d,'annotations.jsonl',calls)
        self.assertEqual(len(outside),1);self.assertIn('session.events.jsonl',outside[0])

    def test_native_model_and_delivery_failures_are_recorded_and_block_repair(self):
        t=D.targets_of(1)[0];d=self.completed_discovery(t)
        start=json.loads((d/'started.json').read_text())
        session=json.loads((d/'session.json').read_text())
        row=N.finish_run(d,start,session,[],[dict(timestamp='1'),dict(timestamp='2')],
                         [dict(model='wrong',effort='low')],{},[],[])
        self.assertEqual(row['status'],'partial')
        self.assertIn('unexpected model/effort',row['protocol_findings'])
        self.assertIn('missing/incorrect same-session follow-up delivery',row['protocol_findings'])
        with self.assertRaisesRegex(ValueError,'completed'): D.checked_run(d,t)

    def test_prefetch_gaps_cannot_disappear_from_a_page(self):
        d,_,path,_=self.discovered_page()
        prefetch=json.loads((path.parent/'prefetch.json').read_text())
        prefetch['missing']=['Ephrem, Hymns on Paradise 5:6'];save(path.parent/'prefetch.json',prefetch)
        report=VR.check(d,path,AYAH,[self.record()])
        self.assertTrue(any('prefetch gap' in e for e in report['errors']))

    def test_native_cli_lifecycle_with_two_recorded_turns(self):
        t=D.targets_of(1)[0]
        d=D.tdir(1,'1:1','cli')/'luna';d.mkdir(parents=True)
        (d/'prompt.md').write_text('Independent discovery brief')
        (d/'package.md').write_text(D.package(1,t,{'1:1':'بسم الله'}))
        save(d/'input.json',{k:t[k] for k in ('target','base_path','base_sha256','inputs')})
        def run(phase,*extra):
            argv=['discovery_native.py',phase,'--surah','1','--target','1:1','--run-tag','cli','--model','luna',*extra]
            with patch('sys.argv',argv),redirect_stdout(io.StringIO()): N.main()
        run('start','--task','bible_cli_luna')
        (d/'list.tsv').write_text(ROW)
        session=dict(agent_path='/root/bible_cli_luna',agent_id='cli-luna',transcript='fixture')
        save(d/'session.json',session)
        contexts=[dict(model=D.MODELS['luna'],effort='max')]
        first=[dict(timestamp='1')]
        with patch.object(N.N,'events_for',return_value=(session,[],first,contexts,{})):
            run('snapshot')
        (d/'followup.tsv').write_text('')
        with patch.object(N.N,'events_for',return_value=(session,[],first+[dict(timestamp='2')],contexts*2,{})), \
             patch.object(N,'followup_proof',return_value=[dict(matches=True,encrypted=False)]):
            run('audit')
            run('finish','--reviewed')
        self.assertEqual(D.checked_run(d,t)[0]['ref'],'WLC:Gen.1.1')
        with self.assertRaisesRegex(SystemExit,'already finished'): run('finish','--reviewed')

    def test_unambiguous_book_names_resolve_without_changing_raw_rows(self):
        path=self.root/'aliases.tsv'
        raw=ROW.replace('WLC:Gen.1.1','WLC:Genesis.1.1')
        path.write_text(raw)
        rows,bad=D.parse_rows(path)
        self.assertEqual(bad,[])
        self.assertEqual(rows[0]['ref'],'WLC:Gen.1.1')
        self.assertEqual(rows[0]['raw_ref'],'WLC:Genesis.1.1')
        self.assertEqual(path.read_text(),raw)
        report=DC.check(path)
        self.assertEqual(report['findings'][0]['kind'],'reference_alias')
        self.assertEqual(report['findings'][0]['raw_ref'],'WLC:Genesis.1.1')
        self.assertEqual(D.BOOK_CODES['james'],'Jas')
        self.assertEqual(D.BOOK_CODES['hosea'],'Hos')
        self.assertEqual({k:D.BOOK_CODES[k] for k in ('is','jon','philem')},
                         {'is':'Isa','jon':'Jonah','philem':'Phlm'})

    def test_book_name_resolution_never_changes_edition_or_verse_numbering(self):
        path=self.root/'aliases.tsv'
        for ref in ('WLC:Genesis.1.999','WLC:Unknown.1.1','SBLGNT:Genesis.1.1'):
            path.write_text(ROW.replace('WLC:Gen.1.1',ref))
            self.assertTrue(D.parse_rows(path)[1],ref)

    def test_alias_repeat_keeps_first_bytes_and_records_raw_spellings(self):
        t=D.targets_of(1)[0]
        raw=ROW.replace('WLC:Gen.1.1','WLC:Genesis.1.1')
        d=self.completed_discovery(t,rows=raw,followup=ROW)
        rows=D.checked_run(d,t)
        self.assertEqual(len(rows),1)
        self.assertEqual((d/'list.tsv').read_text(),raw)
        cons=json.loads((d/'consolidation.json').read_text())
        self.assertEqual(cons['repeated_proposals'][0]['retained']['row']['raw_ref'],'WLC:Genesis.1.1')

    def first_repair_fixture(self):
        t=D.targets_of(1)[0];d=D.tdir(1,'1:1','first-repair')/'luna';d.mkdir(parents=True)
        (d/'prompt.md').write_text('Independent discovery brief')
        (d/'package.md').write_text(D.package(1,t,{'1:1':'بسم الله'}))
        save(d/'input.json',{k:t[k] for k in ('target','base_path','base_sha256','inputs')})
        def run(phase,*extra):
            argv=['discovery_native.py',phase,'--surah','1','--target','1:1',
                  '--run-tag','first-repair','--model','luna',*extra]
            with patch('sys.argv',argv),redirect_stdout(io.StringIO()): N.main()
        run('start','--task','bible_first_repair')
        raw=ROW.replace('Gen.1.1','Gen.1.999');(d/'list.tsv').write_text(raw)
        session=dict(agent_path='/root/bible_first_repair',agent_id='repair-luna',transcript='fixture')
        save(d/'session.json',session)
        event_data=(session,[],[dict(timestamp='1')],[dict(model=D.MODELS['luna'],effort='max')],{})
        self.stack.enter_context(patch.object(N.N,'events_for',return_value=event_data))
        self.proof=self.stack.enter_context(patch.object(N,'followup_proof',return_value=[]))
        changes=[dict(line=1,before=raw.strip().split('\t'),after=ROW.strip().split('\t'),reason='Exact approved locator correction')]
        return t,d,run,raw,changes,event_data

    def finish_first_repaired(self,d,run,event_data,followup=ROW):
        run('snapshot');(d/'followup.tsv').write_text(followup)
        session,events,done,contexts,usage=event_data
        with patch.object(N.N,'events_for',return_value=(session,events,done+[dict(timestamp='2')],contexts*2,usage)), \
             patch.object(N,'followup_proof',return_value=[dict(matches=True,encrypted=False)]):
            run('audit')
            if followup==ROW: run('finish','--reviewed')
            else:
                with self.assertRaises(SystemExit): run('finish','--reviewed')

    def test_first_turn_repair_preserves_raw_and_replays_through_merge(self):
        t,d,run,raw,changes,event_data=self.first_repair_fixture()
        FR.propose(d,changes);FR.accept(d,'User approved this exact first-turn repair',True)
        self.assertEqual((d/'list.tsv').read_text(),raw)
        self.finish_first_repaired(d,run,event_data)
        self.assertEqual((d/'turn1.list.tsv').read_text(),raw)
        self.assertEqual((d/'turn1.original.tsv').read_text(),raw)
        self.assertEqual((d/'list.tsv').read_text(),ROW)
        self.assertEqual(len(D.checked_run(d,t)),1)
        log=json.loads((d/'run.log.json').read_text())
        self.assertEqual(log['consolidation']['initial_file'],'turn1.accepted.tsv')
        self.assertEqual(len(log['consolidation']['repeated_proposals']),1)
        self.completed_discovery(t,'terra',run_tag='first-repair')
        with redirect_stdout(io.StringIO()): path=D.merge(1,[t],'first-repair')[0]
        self.assertEqual(json.loads(path.with_suffix('.json').read_text())['findings'][0]['first_turn_repair']['changes'],changes)
        self.assertTrue(REPORT.report(1,'first-repair',[t])['ready_for_merge'])
        for name in FR.ARTIFACTS:
            original=(d/name).read_bytes();(d/name).write_bytes(original+b'\n')
            with self.assertRaisesRegex(ValueError,'changed'): D.checked_run(d,t)
            (d/name).write_bytes(original)

    def test_first_turn_repair_requires_exact_approval_and_tool_review(self):
        _,d,_,raw,changes,_=self.first_repair_fixture();FR.propose(d,changes)
        with self.assertRaisesRegex(ValueError,'approval'): FR.accept(d,'',True)
        with self.assertRaisesRegex(ValueError,'audit'): FR.accept(d,'User approved',False)
        self.assertEqual((d/'list.tsv').read_text(),raw)
        self.assertFalse((d/'turn1.accepted.tsv').exists())

    def test_first_turn_repair_rejects_late_delivery_and_wrong_model(self):
        _,d,_,_,changes,data=self.first_repair_fixture()
        session,events,done,contexts,usage=data
        with patch.object(N.N,'events_for',return_value=(session,events,done*2,contexts,usage)):
            with self.assertRaisesRegex(ValueError,'one completed'): FR.propose(d,changes)
        with patch.object(N.N,'events_for',return_value=(session,events,done,[dict(model='wrong',effort='max')],usage)):
            with self.assertRaisesRegex(ValueError,'model'): FR.propose(d,changes)
        self.proof.return_value=[dict(matches=True)]
        with self.assertRaisesRegex(ValueError,'already delivered'): FR.propose(d,changes)

    def test_first_turn_schema_swap_cannot_change_meaning_or_grade(self):
        raw=ROW.replace('\ttevrat\tparalel\t','\tparalel\ttevrat\t')
        changes=[dict(line=1,before=raw.strip().split('\t'),after=ROW.strip().split('\t'),reason='Columns transposed')]
        self.assertEqual(DR.repaired_bytes(raw.encode(),changes,allow_schema_swap=True),ROW.encode())
        with self.assertRaisesRegex(ValueError,'preserve'): DR.repaired_bytes(raw.encode(),changes)
        for column,value in ((0,'weak'),(2,'motif'),(4,'different basis'),(5,'different explanation')):
            bad=json.loads(json.dumps(changes));bad[0]['after'][column]=value
            with self.assertRaisesRegex(ValueError,'preserve'):
                DR.repaired_bytes(raw.encode(),bad,allow_schema_swap=True)

    def test_first_turn_repair_refuses_unrecorded_proposal_change(self):
        _,d,_,_,changes,_=self.first_repair_fixture();FR.propose(d,changes)
        (d/'turn1.repair.proposed.tsv').write_text(ROW.replace('strong','weak'))
        with self.assertRaisesRegex(ValueError,'unrecorded'): FR.accept(d,'Approval of original proposal',True)

    def test_first_turn_repair_keeps_followup_repair_provenance(self):
        t,d,run,raw,changes,data=self.first_repair_fixture()
        FR.propose(d,changes);FR.accept(d,'First correction approved',True)
        self.finish_first_repaired(d,run,data,followup=raw)
        DR.propose(d,changes);DR.accept(d,'Follow-up correction approved separately')
        self.assertEqual(len(D.checked_run(d,t)),1)
        self.assertEqual((d/'turn1.list.tsv').read_text(),raw)
        self.assertEqual((d/'followup.tsv').read_text(),raw)

    def test_recorded_witness_label_repair_is_explicit_and_edition_bound(self):
        t=D.targets_of(1)[0];raw=ROW.replace('\ttevrat\t','\tincil\t')
        d=self.completed_discovery(t,followup=raw)
        changes=[dict(line=1,before=raw.strip().split('\t'),after=ROW.strip().split('\t'),reason='WLC requires tevrat')]
        with self.assertRaisesRegex(ValueError,'preserve'): DR.repaired_bytes(raw.encode(),changes)
        DR.propose(d,changes,allow_witness_tradition=True)
        DR.accept(d,'User approved the displayed edition-derived label correction')
        self.assertEqual(len(D.checked_run(d,t)),1)
        self.assertEqual((d/'followup.tsv').read_text(),raw)
        for field,value in ((0,'weak'),(2,'motif'),(3,'SBLGNT:Matt.1.1'),(5,'Different explanation')):
            altered=json.loads(json.dumps(changes));altered[0]['after'][field]=value
            with self.assertRaisesRegex(ValueError,'preserve'):
                DR.repaired_bytes(raw.encode(),altered,allow_witness_tradition=True)
        reversed_change=[dict(line=1,before=changes[0]['after'],after=changes[0]['before'],reason='Wrong tradition')]
        with self.assertRaisesRegex(ValueError,'preserve'):
            DR.repaired_bytes(ROW.encode(),reversed_change,allow_witness_tradition=True)

    def test_followup_column_swap_is_recorded_and_replayed(self):
        t=D.targets_of(1)[0];raw=ROW.replace('\ttevrat\tparalel\t','\tparalel\ttevrat\t')
        d=self.completed_discovery(t,followup=raw)
        changes=[dict(line=1,before=raw.strip().split('\t'),after=ROW.strip().split('\t'),reason='Exact transposed columns')]
        DR.propose(d,changes,allow_schema_swap=True)
        DR.accept(d,'User approved this displayed follow-up column swap')
        self.assertEqual(len(D.checked_run(d,t)),1)
        record=json.loads((d/'repair.accepted.json').read_text())
        self.assertTrue(record['allow_schema_swap'])
        self.assertEqual((d/'followup.tsv').read_text(),raw)


if __name__=='__main__':
    unittest.main()
