"""Offline regression checks; these tests never call a model."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import experiment as EX
import synthesis as S
import review as R


class SynthesisTests(unittest.TestCase):
    def test_adjacent_tags_and_bare_references(self):
        self.assertEqual(S.passages('24:35 [same-word] [staging], 24:36'),
                         {'24:35': ['same-word', 'staging'], '24:36': []})
        self.assertEqual(S.passages('24:35:1'), {})

    def test_prose_source_tags_and_ranges_are_cited_but_word_ids_are_not(self):
        self.assertEqual(S.prose_passages('source:24:35} (24:36–38; 24:39-24:40) word 24:41:2'),
                         {'24:35', '24:36', '24:37', '24:38', '24:39', '24:40'})
        data = self.data()
        check = S.check_account(data, 'A source illuminates the scene. {source:24:36} (24:37–38)', {
            'bundles': [], 'deferred': [{'items': 'remaining', 'destination': 'review', 'reason': 'test'}]})
        self.assertEqual(check['unused_passage_candidates'], {})

    def test_wrapped_network_and_duplicate_records(self):
        parsed = S.records('I1 | image | members: 24:35:1\n  | movement: light moves\nunplaced: 24:35 F2')
        self.assertIn('movement: light moves', parsed['I1'])
        with self.assertRaises(ValueError):
            S.records('F1 | a\nF1 | b')

    def test_disclosure_ranges_and_repeated_role_order(self):
        self.assertEqual(S.roles('meet 24:33; develop 24:34, 24:35; assemble 24:36–24:37', '24:35'), ['develop'])
        self.assertEqual(S.roles('24:35 touch (word); 24:36 assemble', '24:35'), ['touch'])

    def data(self):
        return S.inventory('24:35',
            'F1 | chain | words: 24:35:1 | branches: ن و ر B001 | image: source and light\n'
            'F2 | loss | image: a lexical loss\nF3 | fragment | image: unfinished fragment',
            'F1 | contradicts | 24:36 [same-word] [staging] | a real constraint\n'
            'A1 | axis | 24:37 | a separate axis',
            'I1 | image | members: 24:35:1 ن و ر B001 (source) [24:35 F1]; 24:36:2 (receiver) [24:36 F2]'
            ' | movement: light reaches its receiver | meets: I2 at 24:35:1 — a shared source'
            ' | purpose: receiving light | disclosure: 24:35 touch; 24:36 assemble')

    def test_all_findings_axes_counterevidence_and_meetings_are_preserved(self):
        data = self.data()
        self.assertEqual(set(data['items']), {'F1', 'F2', 'F3', 'E_F1', 'A1', 'I1', 'I1_M1'})
        self.assertEqual(data['passages']['24:36']['tags'], ['same-word', 'staging'])
        # A different ayah's F2 must not become this ayah's image member.
        self.assertNotIn('F2', data['groups'][0]['items'])
        self.assertIn('source', S.render(data))
        self.assertIn('receiver', data['items']['I1']['text'])

    def test_coverage_claim_is_not_semantic_success(self):
        check = S.check_account(self.data(), 'A source lights a receiver in this passage.', {
            'bundles': [{'id': 'B1', 'items': ['F1'], 'level': 'mentioned',
                         'evidence': 'A source lights a receiver', 'payoff': 'a claim'}]})
        self.assertFalse(check['structurally_valid'])
        self.assertIn('F3', check['unreported'])
        self.assertEqual(check['semantic_acceptance'], 'pending independent review')
        forwarded = S.handforward(self.data(), check)
        self.assertIn('F1: mentioned', forwarded)
        self.assertIn('F3: unreported', forwarded)
        self.assertIn('E_F1: unreported', forwarded)

    def test_nonverbatim_and_unknown_evidence_cannot_pass(self):
        check = S.check_account(self.data(), 'This is the actual passage from the commentary.', {
            'bundles': [{'id': 'B1', 'items': ['F99'], 'level': 'connected',
                         'evidence': 'a fabricated quotation that is long enough', 'payoff': 'claim'}],
            'deferred': [{'items': 'remaining', 'destination': 'surah', 'reason': 'held'}]})
        self.assertFalse(check['structurally_valid'])
        self.assertEqual(check['decisions']['F1']['level'], 'deferred')


class FrozenExperimentTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.patch = patch.object(EX, 'ROOT', self.root)
        self.patch.start()
        self.snapshot = self.root / 'baseline.manifest.json'
        self.snapshot.write_text(json.dumps({'files': {'out-v2/example': 'hash'}}))
        self.patch2 = patch.object(EX, 'SNAPSHOT', self.snapshot)
        self.patch2.start()
        (self.root/'prompts').mkdir()
        (self.root/'prompts/write.md').write_text('Synthesis brief. Do not read evaluation material.')
        for a in (35, 36):
            ref=f'24:{a}'
            src=EX.ayah_dir(self.root/'out-v2',ref)
            work=EX.ayah_dir(self.root/'work',ref)
            src.mkdir(parents=True); work.mkdir(parents=True)
            (src/'act.md').write_text('F1 | local | image: a concrete reading')
            (src/'qeq.md').write_text('F1 | supports | 24:34 | source statement')
            for step in ('act','qeq'):
                (src/f'{step}.status.json').write_text('{"state":"done"}')
            (src/'branches.md').write_text('branch sources')
            (src/f'24_{a}.reading.tr.md').write_text(f'TARGET BASELINE {a}')
            for name in ('ayah.md','dictionary.md','concordance.md'):
                (work/name).write_text(name+' canonical input')
            (work/'window').write_text('work/s024/window_1-40')
        window=self.root/'work/s024/window_1-40'
        window.mkdir(); (window/'window_text.md').write_text('window text')
        self.arm=self.root/'out-trial'

    def tearDown(self):
        self.patch2.stop(); self.patch.stop(); self.tmp.cleanup()

    def test_frozen_content_and_no_target_or_eval_leak(self):
        EX.prepare(self.arm,self.root/'out-v2',['24:35'])
        packet,_=EX.packet(self.arm,'24:35')
        self.assertNotIn('TARGET BASELINE 35',packet)
        data=EX.ayah_dir(self.arm,'24:35')/'act.md'
        data.write_text(data.read_text()+' altered')
        with self.assertRaisesRegex(ValueError,'Frozen evidence changed'):
            EX.packet(self.arm,'24:35')

    def test_sequential_context_uses_candidate_and_never_baseline_fallback(self):
        EX.prepare(self.arm,self.root/'out-v2',['24:35','24:36'])
        with self.assertRaisesRegex(ValueError,'waiting for'):
            EX.packet(self.arm,'24:36')
        EX.export(self.arm,'24:35')
        EX.claim(self.arm,'24:35','test-model','max')
        body=' '.join(['The commentary develops a connected explanation.']*70)
        account={'bundles':[], 'deferred':[{'items':'remaining','destination':'surah','reason':'test deferral'}]}
        EX.ingest(self.arm,'24:35',body+'\n===== SYNTHESIS =====\n'+json.dumps(account))
        packet,receipt=EX.packet(self.arm,'24:36')
        self.assertIn(body,packet)
        self.assertNotIn('TARGET BASELINE 35',packet)
        self.assertEqual(receipt['earlier_prose'][0]['kind'],'earlier candidate, awaiting semantic review')
        self.assertEqual(json.loads((EX.ayah_dir(self.arm,'24:35')/'write.status.json').read_text())['state'],'review-needed')

    def test_never_twice_and_immutable_export(self):
        EX.prepare(self.arm,self.root/'out-v2',['24:35'])
        EX.export(self.arm,'24:35')
        EX.claim(self.arm,'24:35','test','max')
        with self.assertRaises(ValueError): EX.claim(self.arm,'24:35','test','max')
        with self.assertRaises(ValueError): EX.export(self.arm,'24:35')
        with self.assertRaises(ValueError): EX.prepare(self.root/'out-v2',self.root/'out-v2',['24:35'])

    def test_changed_predecessor_invalidates_export(self):
        EX.prepare(self.arm,self.root/'out-v2',['24:36'])
        EX.export(self.arm,'24:36')
        prior=self.arm/'context/s024/24_35.reading.tr.md'
        prior.write_text('changed previous text')
        with self.assertRaises(ValueError): EX.claim(self.arm,'24:36','test','max')

    def test_claimed_input_cannot_change_during_external_generation(self):
        EX.prepare(self.arm,self.root/'out-v2',['24:35'])
        EX.export(self.arm,'24:35')
        path=EX.claim(self.arm,'24:35','test','max')
        path.write_text('changed after model started')
        with self.assertRaisesRegex(ValueError,'changed during generation'):
            EX.ingest(self.arm,'24:35','any response')


class AcceptanceTests(unittest.TestCase):
    def test_regression_cannot_be_offset_by_an_improvement_and_hashes_are_binding(self):
        with tempfile.TemporaryDirectory() as tmp:
            arm = Path(tmp)
            out = EX.ayah_dir(arm, '24:35')
            out.mkdir(parents=True)
            body = 'This exact passage connects the source and its receiver.'
            reading = out / '24_35.reading.tr.md'
            reading.write_text(body)
            data = S.inventory('24:35', 'F1 | local | image: a relation', '', '')
            EX.dump(out/'synthesis.json', data)
            EX.dump(out/'synthesis.account.json', {'bundles': [{'id':'B1','items':['F1'], 'level':'connected',
                     'evidence':body, 'payoff':'source reaches receiver'}], 'deferred':[]})
            criteria = arm / 'cases.json'
            criteria.write_text('{}')
            rows = [{'id':'preserve', 'verdict':'regressed', 'evidence':body, 'notes':'lost an important relationship'},
                    {'id':'improve', 'verdict':'improved', 'evidence':body, 'notes':'a separate gain'}]
            report={'ref':'24:35','reviewer':'independent reviewer','candidate_sha256':S.sha(reading),
                    'cases_sha256':S.sha(criteria),'rows':rows}
            EX.dump(out/'review.json',report)
            with patch.object(EX,'verify',return_value={}), patch.object(R,'CASES',criteria), \
                 patch.object(R,'cases_for',return_value=[{'id':'preserve','mode':'preserve'}, {'id':'improve','mode':'improve'}]), \
                 patch.object(R,'source_check',return_value={'ok':True}):
                self.assertFalse(R.assess(arm,'24:35')['eligible'])
                report['rows'][0]['verdict']='preserved'
                EX.dump(out/'review.json',report)
                self.assertTrue(R.assess(arm,'24:35')['eligible'])
                reading.write_text(body+' Added after review.')
                self.assertFalse(R.assess(arm,'24:35')['eligible'])


if __name__ == '__main__':
    unittest.main()
