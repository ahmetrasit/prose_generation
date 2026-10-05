"""Offline tests for independent image authors and evidence-preserving assembly."""
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import unittest
from unittest.mock import patch

from enrichment.bible import image_enrich as I, discovery as D, enrich as E, render as R
from enrichment.bible import test_workflow as W
SURAH, save = W.SURAH, W.save


class BibleImageTest(W.BibleWorkflowTest):
    def prepare_images(self):
        self.handoff('surah')
        with redirect_stdout(io.StringIO()):
            I.prepare(1, 'image-test')
        return I.run_dir(1, 'image-test')

    def outputs(self, d, paragraph=1):
        record = self.record(paragraf=paragraph, capa='Birinci paragraf burada' if paragraph==1 else 'İkinci paragraf burada')
        I.save_jsonl(d/'annotations.jsonl', [record])
        I.save_jsonl(d/'verdicts.jsonl', [dict(connection_id=None,origin='research',ref='WLC:Gen.1.1',
            status='accepted',reason='A checked parallel in this paragraph.',paragraphs=[paragraph],
            evidence=['WLC:Gen.1.1'],annotations=[record['id']])])
        save(d/'gaps.json',dict(missing_sources=[],not_found=[],unresolved=[]))
        self.tool_gets(d, ['WLC:Gen.1.1'])

    def test_image_layout_keeps_global_numbers_and_covers_base(self):
        layout=I.image_layout(SURAH)
        self.assertEqual([s['paragraphs'] for s in layout], [[1],[2]])
        self.assertIn('[¶2] İkinci', layout[1]['numbered'])
        with self.assertRaisesRegex(ValueError,'cover every'):
            I.image_layout('Introductory unassigned prose.\n\n'+SURAH)

    def test_image_snapshot_names_unfetched_gaps_honestly(self):
        report=I.local_sources({'a':{'ref':'WLC:Gen.1.1'},'b':{'ref':'Didache 1.1'}})
        self.assertFalse(report['network_attempted'])
        self.assertFalse(report['coverage_complete'])
        self.assertEqual(report['missing'],['Didache 1.1'])
        with self.assertRaisesRegex(ValueError,'canonical'):
            I.local_sources({'a':{'ref':'WLC:Gen.100.1'}})

    def test_image_authors_lock_corpus_and_preserve_default_opus(self):
        root=self.prepare_images()
        from enrichment.bible import corpus as C, pack as P
        self.assertTrue(C.running_calls())
        self.assertTrue(P.running_calls(1))
        self.assertEqual(E.DEFAULT_MODEL, 'opus')
        self.assertEqual(I.frozen_ok(root/'sec1')['paragraphs'],[1])
        with self.assertRaisesRegex(ValueError,'already exists'):
            I.prepare(1,'image-test')

    def test_image_scope_and_actual_opened_evidence_are_required(self):
        root=self.prepare_images(); d=root/'sec1'
        self.outputs(d)
        self.assertTrue(I.check(d)['ok'])
        self.assertFalse(I.check(d,final=True,calls=[])['ok'])
        self.assertTrue(I.check(d,final=True,calls=json.loads((d/'tool_calls.json').read_text()))['ok'])
        self.outputs(d,paragraph=2)
        report=I.check(d)
        self.assertTrue(any('outside assigned image' in x for x in report['errors']))

    def test_image_inputs_cannot_be_changed_after_prepare(self):
        root=self.prepare_images(); d=root/'sec1'
        (d/'base.md').write_text('Changed')
        with self.assertRaisesRegex(ValueError,'image input changed'):
            I.frozen_ok(d)

    def test_image_tool_wrappers_cannot_hide_extra_commands(self):
        inp={'cmd':'cat /some/file','workdir':str(E.PG)}
        wrapper='const r = await tools.exec_command('+json.dumps(inp)+');\ntext(r.output);'
        self.assertEqual(I.unwrap_call('exec',wrapper),('exec_command',inp))
        with self.assertRaisesRegex(ValueError,'unsupported orchestration'):
            I.unwrap_call('exec',wrapper+'await tools.exec_command({"cmd":"curl example.com"});')
        d=(self.home/'work/test').resolve()
        self.assertFalse(I.allowed_command('python3 -c "print(1)"',d))
        self.assertFalse(I.allowed_command(f'cat {d}/notes.md; curl example.com',d))
        self.assertTrue(I.allowed_command(f'python3 {self.home}/corpus.py --intertext get WLC:Gen.1.1',d))
        self.assertTrue(I.allowed_patch(f'*** Begin Patch\n*** Add File: {d}/notes.md\n+x\n*** End Patch',d))
        self.assertFalse(I.allowed_patch(f'*** Begin Patch\n*** Add File: {d}/base.md\n+x\n*** End Patch',d))

    def test_image_initial_prompt_read_accepts_only_literal_bootstrap_syntax(self):
        raw='const r=await tools.exec_command({cmd:"cat prompt.md",max_output_tokens:30000});text(r.output)'
        self.assertEqual(I.unwrap_call('exec',raw,bootstrap=True)[1]['cmd'],'cat prompt.md')
        with self.assertRaises(ValueError): I.unwrap_call('exec',raw)
        with self.assertRaises(ValueError): I.bootstrap_object('{cmd: getCommand()}')
        with self.assertRaises(ValueError): I.bootstrap_object('{cmd:"cat a",cmd:"curl x"}')
        with self.assertRaises(ValueError): I.bootstrap_object('{cmd:"cat a" + "foo"}')

    def test_image_own_preview_and_clock_do_not_authorize_external_tools(self):
        d=(self.home/'work/own').resolve()
        self.assertTrue(I.allowed_command(f"sed -n '1,40p' {d}/preview/surah.md",d))
        self.assertFalse(I.allowed_command(f'cat {d.parent}/other/preview/surah.md',d))
        self.assertTrue(I.allowed_command(f'ls -la {d}',d))
        self.assertFalse(I.allowed_command(f'ls -la {d.parent}',d))
        self.assertFalse(I.allowed_command(f'ls -R {d}',d))
        self.assertEqual(I.unwrap_call('exec','const r = await tools.clock__curr_time({}); text(r.current_time);'),('clock',{}))
        with self.assertRaises(ValueError):
            I.unwrap_call('exec','const r = await tools.clock__curr_time({}); text(r.current_time); await tools.web__run({});')

    def test_image_resumption_requires_exact_failed_history_and_delivery(self):
        root=self.prepare_images();d=root/'sec1'
        failed=dict(type='task_complete',turn_id='failed-turn',error={'message':'capacity'})
        events=[dict(type='event_msg',payload=failed)]
        done=[events[0],dict(type='event_msg',payload={'type':'task_complete','turn_id':'ok-turn'})]
        self.assertTrue(I.audit_turns(d,{},events,done)[0])
        (d/'resume-message.txt').write_text('Continue unchanged.\n')
        save(d/'resume.json',dict(authorized_by='User resume',failures=[failed],successful_turns_before=0,
            model=I.MODEL,effort=I.EFFORT,agent_path=I.read_json(d/'started.json')['agent_path'],
            message='Continue unchanged.',message_sha256=D.digest(d/'resume-message.txt')))
        with patch('enrichment.bible.discovery_native.followup_proof',return_value=[{'matches':True}]):
            errors,history=I.audit_turns(d,{},events,done)
            self.assertEqual(errors,[])
            self.assertEqual(history['successful_completions'],1)
            self.assertEqual(history['unfinished_attempts'],[failed])
            self.assertTrue(I.audit_turns(d,{},events,done+[done[-1]])[0])
        with patch('enrichment.bible.discovery_native.followup_proof',return_value=[]):
            self.assertTrue(I.audit_turns(d,{},events,done)[0])

    def test_image_assembly_remaps_ids_and_preserves_per_section_evidence(self):
        root=self.prepare_images()
        for n in (1,2):
            d=root/f'sec{n}';self.outputs(d,n)
            calls=json.loads((d/'tool_calls.json').read_text())
            self.assertTrue(I.check(d,final=True,calls=calls)['ok'])
            save(d/'run.log.json',dict(status='ok',artifacts={p.name:D.digest(p) for p in d.iterdir() if p.is_file()}))
        result=I.assemble(1,'image-test')
        self.assertEqual(result['annotations'],2)
        rows=R.load(root/'annotations.jsonl')
        self.assertEqual([r['id'] for r in rows],['S001-TEV-PRL-001','S001-TEV-PRL-002'])
        verdicts=R.load(root/'verdicts.jsonl')
        self.assertEqual(len(verdicts),2)
        self.assertEqual([v['scope'] for v in verdicts],['sec1','sec2'])
        self.assertEqual([v['annotations'][0] for v in verdicts],[r['id'] for r in rows])
        self.assertTrue((E.OUT/'s001/surah.ehlikitap.md').exists())
        with self.assertRaisesRegex(ValueError,'already assembled'):
            I.assemble(1,'image-test')

    def test_image_assembly_rejects_changed_or_failed_parts(self):
        root=self.prepare_images()
        save(root/'sec1/run.log.json',dict(status='failed',artifacts={}))
        with self.assertRaisesRegex(ValueError,'failed image'):
            I.assemble(1,'image-test')

    def test_image_assembly_cannot_borrow_evidence_from_another_author(self):
        root=self.prepare_images()
        for n in (1,2):
            d=root/f'sec{n}';self.outputs(d,n)
            if n==2: save(d/'tool_calls.json',[])
            save(d/'run.log.json',dict(status='ok',artifacts={p.name:D.digest(p) for p in d.iterdir() if p.is_file()}))
        with self.assertRaisesRegex(ValueError,'sec2: image no longer passes'):
            I.assemble(1,'image-test')


if __name__=='__main__': unittest.main()
