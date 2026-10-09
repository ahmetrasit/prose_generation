"""Offline tests for the 2026-10-09 additions: Hebrew root layer, Semitic root verdicts, r13 ayah packs,
configurable reader pairs and the codex exec discovery route. No models, no network."""
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import unittest

from enrichment.bible import discovery as D, discovery_exec as DX, discovery_native as N, hebrew as H
from enrichment.bible import image_enrich as I, pack as P, verdicts as VR, agentrun as AR
from enrichment.bible import test_workflow as W


class SemiticTest(W.BibleWorkflowTest):
    def test_sound_correspondences_cover_weak_and_split_letters(self):
        keys = {(lang, k) for lang, k, _ in H.candidates('ع ص ر')}
        self.assertIn(('heb', 'עצר'), keys)
        keys = {k for lang, k, _ in H.candidates('ث ل ج') if lang == 'heb'}
        self.assertIn('שלג', keys)                       # ث → ש in Hebrew
        self.assertIn(('arc', 'תלג'), {(l, k) for l, k, _ in H.candidates('ث ل ج')})   # ث → ת in Aramaic
        keys = {k for lang, k, _ in H.candidates('و ل د') if lang == 'heb'}
        self.assertIn('ילד', keys)                       # initial و → י
        keys = {k for lang, k, _ in H.candidates('ب ك ي') if lang == 'heb'}
        self.assertIn('בכה', keys)                       # final weak → ה
        self.assertEqual(H.ar_letters('أَمَرَ'), ['ء', 'م', 'ر'])
        with self.assertRaises(SystemExit):
            H.ar_letters('ا')

    def test_cognates_keep_only_lexicon_roots_and_label_their_basis(self):
        rows = H.cognates('ح م د')
        self.assertEqual([(r['key'], r['basis']) for r in rows], [('חמד', 'BDB cites an Arabic cognate')])
        self.assertIn('no Hebrew or Aramaic root', '\n'.join(H.cmd_cognates('ق ط ع')))
        self.assertIn('חמד', H.table(['ح م د']))

    def test_lemma_mapping_reports_prefix_only_and_ambiguous_lemmas(self):
        entries = {'a': dict(aug='a'), 'b': dict(aug='b'), 'c': dict(aug=None)}
        by = {('heb', '1254'): ['a', 'b'], ('heb', '430'): ['c'], ('arc', '560'): ['c']}
        self.assertEqual(H.lemma_entries('c/1254 b', 'HC/Vqw3ms', by, entries), (['b'], 'exact'))
        self.assertEqual(H.lemma_entries('430', 'HNcmpa', by, entries), (['c'], 'exact'))
        self.assertEqual(H.lemma_entries('l', 'HR/Sp3mp', by, entries), ([], 'prefix'))
        self.assertEqual(H.lemma_entries('1254', 'HVqp3ms', by, entries)[1], 'ambiguous')
        self.assertEqual(H.lemma_entries('560', 'AVqp3ms', by, entries), (['c'], 'exact'))

    def test_roots_cited_by_a_frozen_text_are_found(self):
        text = 'bir {ar:x, source:"ع ص ر,B006"} ve {ar:y, source:"خ س ر,B002"} ve {ar:z, source:"103:1"}'
        self.assertEqual(H.roots_in(text), ['خ س ر', 'ع ص ر'])

    def test_every_root_needs_one_decision(self):
        d = self.root/'call'
        d.mkdir()
        para = {1, 2}
        self.assertEqual(VR.check_roots(d, [], {}, para), [])
        self.assertIn('missing root_verdicts.jsonl', VR.check_roots(d, ['ع ص ر'], {}, para)[0])
        rows = [dict(root='ع ص ر', decision='used', hebrew=['עצר'], reason='r', paragraphs=[1], annotations=['X'])]
        (d/'root_verdicts.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in rows))
        errs = VR.check_roots(d, ['ع ص ر', 'خ س ر'], {}, para)
        self.assertTrue(any('annotation X was absent' in e for e in errs))
        self.assertTrue(any('1 Arabic roots have no decision: خ س ر' in e for e in errs))
        rows = [dict(root='ع ص ر', decision='false_friend', hebrew=['עצר'], reason='r', paragraphs=[], annotations=[]),
                dict(root='خ س ر', decision='maybe', hebrew=[], reason='', paragraphs=[9], annotations=[])]
        (d/'root_verdicts.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in rows))
        errs = VR.check_roots(d, ['ع ص ر', 'خ س ر'], {}, para)
        self.assertEqual(len(errs), 3)                   # bad decision, empty reason, bad paragraph

    def test_tool_grammars_allow_hebrew_lookups_only(self):
        d = (self.home/'work/x').resolve()
        self.assertTrue(AR.allowed_command(f'python3 {self.home}/hebrew.py root עצר', d))
        self.assertTrue(AR.allowed_command(f"python3 {self.home}/hebrew.py cognates 'ع ص ر'", d))
        self.assertFalse(AR.allowed_command(f'python3 {self.home}/hebrew.py build', d))
        self.assertFalse(I.allowed_command(f'python3 {I.E.V2}/hebrew.py build', d))
        self.assertTrue(I.allowed_command(f'python3 {I.E.V2}/hebrew.py word WLC:Gen.1.1', d))
        self.assertTrue(I.allowed_patch(f'*** Begin Patch\n*** Add File: {d}/root_verdicts.jsonl\n+x\n*** End Patch', d))

    def test_r13_ayah_pack_takes_the_frozen_reading_not_the_augment(self):
        v16 = self.root/'_commentary/v16/out'
        (v16/'s001/images.r13.x').mkdir(parents=True)
        (v16/'s001/images.r13.x/images.md').write_text(W.SURAH)
        reading = v16/'1_1/DM.r13.images.r13.x'
        (reading/'augment.augment9.opus').mkdir(parents=True)
        (reading/'1_1.reading.tr.md').write_text('# Ayah\n\nBirinci paragraf burada durur.\n')
        (reading/'augment.augment9.opus/1_1.reading.tr.md').write_text(W.AYAH)
        self.assertEqual(P.r13_reading(v16, 1, 1), reading/'1_1.reading.tr.md')
        with redirect_stdout(io.StringIO()):
            P.build(1, force=True, ayah_base='r13')
        base = json.loads((self.home/'work/s001/pack/base.json').read_text())
        self.assertEqual(base['ayah_base'], 'r13')
        self.assertNotIn('augment', base['ayat']['1:1']['path'])
        self.assertEqual(W.R.target_page(1, '1:1')[1], '# Ayah\n\nBirinci paragraf burada durur.\n')
        with self.assertRaisesRegex(ValueError, 'cannot be combined'):
            P.build(1, force=True, from_pack=self.upstream, ayah_base='r13')

    def test_reader_pair_is_fixed_per_attempt(self):
        self.assertEqual(D.readers(1, 'test'), ('luna', 'terra'))
        root = D.discovery_dir(1, 'pair')
        root.mkdir(parents=True)
        W.save(root/'readers.json', {'readers': ['luna', 'sol']})
        self.assertEqual(D.readers(1, 'pair'), ('luna', 'sol'))
        t = D.targets_of(1)[0]
        for m in ('luna', 'sol'):
            self.completed_discovery(t, m, rows='', run_tag='pair')
        with self.assertRaisesRegex(ValueError, 'both Luna and Sol'):
            D.merge(1, [t], 'pair', ['luna'])
        W.save(root/'readers.json', {'readers': ['luna', 'luna']})
        with self.assertRaises(ValueError):
            D.readers(1, 'pair')

    def test_codex_exec_followup_proof_is_the_second_turn_user_message(self):
        ev = [dict(type='session_meta', timestamp='0', payload=dict(id='t')),
              dict(type='event_msg', timestamp='1', payload=dict(type='task_started')),
              dict(type='response_item', timestamp='2', payload=dict(type='message', role='user',
                   content=[dict(type='input_text', text='first')])),
              dict(type='event_msg', timestamp='3', payload=dict(type='task_started')),
              dict(type='response_item', timestamp='4', payload=dict(type='message', role='user',
                   content=[dict(type='input_text', text='Exact followup\n')]))]
        session = dict(runner='codex-exec', agent_id='t', agent_path='/root/x')
        self.assertEqual(N.followup_proof(session, ev, 'Exact followup'),
                         [dict(call_id='codex-exec-resume', encrypted=False, matches=True)])
        self.assertEqual(N.followup_proof(session, ev[:3], 'Exact followup'), [])

    def test_exec_policy_flags_reads_outside_the_call(self):
        d = (self.home/'work/x').resolve()
        def call(cmd, phase=1):
            return dict(name='exec', phase=phase, call_id='c',
                        arguments='const r = await tools.exec_command({cmd:' + json.dumps(cmd) + '});\ntext(r.output);')
        ok = [call(f'cat {d}/prompt.md'), call(f"cat > {d}/list.tsv <<'EOF'\nweak\ttevrat\tmotif\tWLC:Gen.1.1\ta/b\tx\nEOF"),
              call(f"cat > {d}/followup.tsv <<'EOF'\nEOF", 2)]
        self.assertEqual(DX.policy(d, ok)[0], [])
        bad = [call('cat /etc/passwd'), call(f'python3 {self.home}/corpus.py get WLC:Gen.1.1'),
               call('curl https://example.com'), dict(name='spawn_agent', arguments='{}', call_id='z', phase=1)]
        self.assertEqual(len(DX.policy(d, bad)[0]), 5)    # curl also names a path-like URL


def load_tests(loader, tests, pattern):
    """Only the tests defined here (the inherited workflow tests run in test_workflow)."""
    names = [n for n in SemiticTest.__dict__ if n.startswith('test_')]
    return unittest.TestSuite(SemiticTest(n) for n in sorted(names))
