"""Experiment isolation and source-preservation checks; no model calls."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import composition as C
import experiment as EX
import synthesis as S


class CompositionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / 'v14'
        self.root.mkdir()
        self.ref = '24:35'
        self.source = self.root / 'out-evidence'
        self.arm = self.root / 'out-composition'
        old = EX.ayah_dir(self.source, self.ref)
        old.mkdir(parents=True)
        self.out = EX.ayah_dir(self.arm, self.ref)
        snapshot = self.root / 'baseline.manifest.json'
        snapshot.write_text('{"files":{"out-old/frozen":"original"}}')
        self.root_patch = patch.object(EX, 'ROOT', self.root)
        self.snapshot_patch = patch.object(EX, 'SNAPSHOT', snapshot)
        self.root_patch.start(); self.snapshot_patch.start()
        self.addCleanup(self.root_patch.stop); self.addCleanup(self.snapshot_patch.stop)
        self.addCleanup(self.tmp.cleanup)
        (self.root / 'prompts').mkdir()
        (self.root / 'prompts/compose.md').write_text('Compose an explanation from evidence.')
        (self.root / 'prompts/write_composition.md').write_text('Write prose only.')
        act = ('F1 | local | branches: ن و ر B001 | image: a chosen explanation\n'
               'F2 | fragment | image: IRRELEVANT_RESEARCH_MATERIAL\n')
        qeq = 'F1 | contradicts | 24:36 | ACTUAL_COUNTER_EVIDENCE\nA1 | axis | 24:34 | OTHER_AXIS\n'
        data = S.inventory(self.ref, act, qeq, '')
        files = {
            'act.md': act, 'qeq.md': qeq, 'synthesis.json': json.dumps(data),
            'inputs/ayah.md': 'Focus text and morphology', 'inputs/window_text.md': '24:35|exact focus',
            'inputs/dictionary.md': '### ن و ر — focus\n- B001 light | مصدر النور | definition | exact phrase\n',
            'inputs/branches.md': '- ض و ء B001 light | exact other branch\n',
            'inputs/concordance.md': '## ن و ر — 3 uses\n### lemma\n- source use\n',
            'inputs/variants.md': 'No supplied variants.'}
        hashes = {}
        for name, content in files.items():
            path = old / name
            path.parent.mkdir(exist_ok=True)
            path.write_text(content)
            hashes[str(path.relative_to(self.source))] = S.sha(path)
        (self.source / 'inputs').mkdir()
        corpus = self.source / 'inputs/quran.tsv'
        corpus.write_text('24:34|exact previous\n24:35|exact focus\n24:36|exact next\n')
        hashes['inputs/quran.tsv'] = S.sha(corpus)
        # These files exist beside the archive but must never enter generation.
        (old / '24_35.reading.tr.md').write_text('TARGET_BASELINE_NEVER_SEE')
        (old / 'review.json').write_text('TARGET_EVALUATION_NEVER_SEE')
        (self.source / 'inputs/write.md').write_text('OLD_ACCOUNT_CONTRACT_NEVER_SEE')
        hashes['inputs/write.md'] = S.sha(self.source / 'inputs/write.md')
        (self.source / 'experiment.json').write_text(json.dumps({'refs':[self.ref], 'source_mode':'lookup',
            'files':hashes, 'quran_source':{'path':str(corpus), 'sha256':S.sha(corpus)}}))
        self.plan = {'schema':1, 'ref':self.ref, 'explanation':'An integrated causal explanation.',
                     'reader_change':'A consequential change in understanding.', 'source_items':['F1'],
                     'branches':['ن و ر B001'], 'quran_refs':['24:35'],
                     'concordance_roots':['ن و ر'], 'limits':[]}

    def prepare(self):
        return C.prepare(self.arm, self.source, self.ref)

    def compose(self):
        self.prepare()
        C.start(self.arm, self.ref, 'synth', 'test-sol', 'max')
        return C.ingest(self.arm, self.ref, 'synth', json.dumps(self.plan))

    def test_full_research_retained_without_baseline_review_or_old_contract_leak(self):
        manifest = self.prepare()
        packet = (self.out / 'synth.input.md').read_text()
        for sentinel in ['TARGET_BASELINE_NEVER_SEE','TARGET_EVALUATION_NEVER_SEE','OLD_ACCOUNT_CONTRACT_NEVER_SEE']:
            self.assertNotIn(sentinel, packet)
        for sentinel in ['IRRELEVANT_RESEARCH_MATERIAL','ACTUAL_COUNTER_EVIDENCE','OTHER_AXIS']:
            self.assertIn(sentinel, packet)
        self.assertEqual(manifest['research_items'], 4)
        for name in manifest['copied_source_files']:
            self.assertEqual(S.sha(self.arm / name), S.sha(self.source / name))

    def test_writer_receives_selected_evidence_and_counterevidence_archive_keeps_everything(self):
        self.assertEqual(self.compose()['state'], 'done')
        packet = (self.out / 'write.input.md').read_text()
        self.assertIn('An integrated causal explanation.', packet)
        self.assertIn('ACTUAL_COUNTER_EVIDENCE', packet)
        self.assertIn('exact phrase', packet)
        self.assertNotIn('IRRELEVANT_RESEARCH_MATERIAL', packet)
        self.assertNotIn('OTHER_AXIS', packet)
        dispositions = C.read(self.out / 'research.disposition.json')['items']
        self.assertEqual(len(dispositions), 4)
        self.assertFalse(dispositions['F2']['selected_by_composer'])
        self.assertIn('IRRELEVANT_RESEARCH_MATERIAL', dispositions['F2']['record'])

    def test_unknown_selection_stops_dependent_writer_without_repair(self):
        self.plan['branches'] = ['ن و ر B999']
        result = self.compose()
        self.assertEqual(result['state'], 'failed')
        self.assertFalse((self.out / 'write.input.md').exists())
        with self.assertRaisesRegex(ValueError, 'Synthesis must finish'):
            C.start(self.arm, self.ref, 'write', 'test-astra', 'max')
        with self.assertRaises(FileExistsError):
            C.start(self.arm, self.ref, 'synth', 'test-sol', 'max')

    def test_changed_frozen_source_or_prepared_input_is_rejected(self):
        self.prepare()
        (self.out / 'synth.input.md').write_text('modified packet')
        with self.assertRaisesRegex(ValueError, 'Frozen evidence changed'):
            C.start(self.arm, self.ref, 'synth', 'test-sol', 'max')

    def test_changed_composition_after_writer_claim_is_rejected(self):
        self.compose()
        C.start(self.arm, self.ref, 'write', 'test-astra', 'max')
        (self.out / 'composition.json').write_text('{}')
        with self.assertRaisesRegex(ValueError, 'Composition changed'):
            C.ingest(self.arm, self.ref, 'write', 'Prose.')

    def test_lookup_reads_only_frozen_sources_and_logs_each_stage(self):
        self.compose()
        C.start(self.arm, self.ref, 'write', 'test-astra', 'max')
        found = C.lookup(self.arm, self.ref, 'write', 'items', 'F2')
        self.assertIn('IRRELEVANT_RESEARCH_MATERIAL', found)
        found = C.lookup(self.arm, self.ref, 'write', 'quran', '24:35', 1)
        self.assertIn('exact previous', found)
        self.assertIn('exact next', found)
        self.assertEqual(len((self.out / 'write.lookups.jsonl').read_text().splitlines()), 2)
        with self.assertRaises(ValueError):
            C.lookup(self.arm, self.ref, 'write', 'items', '../../review.json')
        with self.assertRaisesRegex(ValueError, 'active generation'):
            C.lookup(self.arm, self.ref, 'synth', 'items', 'F1')

    def test_one_prose_only_generation_no_claim_of_semantic_coverage(self):
        self.compose()
        C.start(self.arm, self.ref, 'write', 'test-astra', 'max')
        result = C.ingest(self.arm, self.ref, 'write', 'Finished commentary.\n')
        self.assertEqual(result['state'], 'review-needed')
        self.assertEqual((self.out / '24_35.reading.tr.md').read_text(), 'Finished commentary.\n')
        self.assertFalse((self.out / 'synthesis.account.json').exists())
        with self.assertRaises(ValueError):
            C.ingest(self.arm, self.ref, 'write', 'Replacement commentary.')


if __name__ == '__main__':
    unittest.main()
