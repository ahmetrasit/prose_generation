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
        # operational reads added for S103: own preview listing, checker help, print-only multi-address sed
        self.assertTrue(I.allowed_command(f'ls -l {d}/preview', d))
        self.assertTrue(I.allowed_command(f'python3 {I.E.V2}/image_enrich.py check --help', d))
        self.assertTrue(I.allowed_command(f"sed -n '/BC-aa/p; /S103-TEV-MTF-006/p' {d}/verdicts.jsonl", d))
        self.assertFalse(I.allowed_command(f"sed -n '/x/w /tmp/o' {d}/verdicts.jsonl", d))
        self.assertFalse(I.allowed_command(f"sed -n '/x/p; e rm -rf x' {d}/verdicts.jsonl", d))
        self.assertFalse(I.allowed_command(f"sed -n '/x/p' /etc/passwd", d))
        self.assertFalse(I.allowed_command(f'ls -l {d.parent}', d))

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
        # readers often wrap the tools in their own JavaScript (variables, string building, Promise.all)
        js = [dict(name='exec', phase=1, call_id='j1', arguments='const p=' + json.dumps(str(d/'package.md'))
                   + '; const r=await tools.exec_command({cmd:"sed -n \'1,40p\' "+JSON.stringify(p)});text(r.output);'),
              dict(name='exec', phase=1, call_id='j2', arguments='const patch=' + json.dumps(
                  f'*** Begin Patch\n*** Add File: {d}/list.tsv\n+weak\ttevrat\tmotif\tWLC:Gen.1.1\tb\tx\n*** End Patch')
                   + '; text(await tools.apply_patch(patch));')]
        self.assertEqual(DX.policy(d, js), ([], []))
        sneaky = [dict(name='exec', phase=1, call_id='j3', arguments='const p="/Users/x/secret.md"; '
                       'const r=await tools.exec_command({cmd:"cat "+p});'),
                  dict(name='exec', phase=1, call_id='j4', arguments='await tools.web_search({q:"x"});')]
        self.assertEqual(len(DX.policy(d, sneaky)[0]), 2)

    def review_call_dir(self):
        from unittest.mock import patch
        from enrichment.bible import review as RV
        self.stack.enter_context(patch.object(RV, 'HERE', self.home))
        self.stack.enter_context(patch.object(RV, 'PG', self.root))
        d = (self.home/'work/s001/ehlikitap.1_1.opus.high').resolve()
        d.mkdir(parents=True)
        tsv = self.home/'work/s001/discovery/t/1_1.merged.tsv'
        tsv.parent.mkdir(parents=True)
        tsv.write_text('x')
        W.save(d/'started.json', dict(surah=1, bible_inputs={str(tsv.relative_to(self.root)): 'h'}))
        return RV, d, tsv

    def test_operator_review_classifies_mechanically(self):
        RV, d, tsv = self.review_call_dir()
        scratch = '/private/tmp/claude-502/-x/sess/scratchpad'
        persisted = str(Path.home()/'.claude/projects/p/s/tool-results/b1.txt')
        calls = [
            dict(id='1', name='Bash', input=dict(command=f'cat {tsv} | head -5; wc -l {d}/annotations.jsonl')),
            dict(id='2', name='Bash', input=dict(command=f'grep -n x {tsv}'), result=f'Output saved to {persisted}'),
            dict(id='3', name='Read', input=dict(file_path=persisted)),
            dict(id='4', name='Write', input=dict(file_path=f'{scratch}/h.py',
                 content=f"import csv, json, sys\nrows=list(open(sys.argv[1]))\nopen('{d}/verdicts.jsonl','w')")),
            dict(id='5', name='Bash', input=dict(command=f'python3 -I {scratch}/h.py {tsv}')),
            dict(id='6', name='Bash', input=dict(command=f"sed -i '' 's#a#b#' {d}/annotations.jsonl")),
            dict(id='7', name='Bash', input=dict(command='cat /etc/passwd')),
            dict(id='8', name='Read', input=dict(file_path=str(Path.home()/'.claude/projects/p/s/tool-results/b9.txt'))),
            dict(id='9', name='Write', input=dict(file_path=f'{scratch}/bad.py', content="import subprocess\n")),
            dict(id='10', name='Bash', input=dict(command=f'python3 -I {scratch}/bad.py')),
            dict(id='11', name='Bash', input=dict(command=f'python3 -I -c "open(\'{tsv}\',\'w\')"')),
            dict(id='12', name='Bash', input=dict(command=f'cat {tsv} > {d}/copy.tsv')),
            dict(id='13', name='Write', input=dict(file_path=f'{d}/operator-review.json', content='{}')),
        ]
        rows, used = RV.walk(d, calls)
        kinds = [(r['kind'], r['auto']) for r in rows]
        self.assertEqual(kinds[:6], [('read', True), ('read', True), ('own_output', True), ('helper', False),
                                     ('helper', False), ('own_edit', True)])
        # writing a script is harmless; running the unsafe one is what fails
        self.assertEqual([r['kind'] for r in rows[6:]], [None, None, 'helper', None, None, None, None])
        self.assertIn(str(Path(f'{scratch}/h.py')), used)
        with self.assertRaisesRegex(ValueError, 'unclassifiable'):
            RV.write(d, calls, 'operator', str(tsv))

    def test_operator_review_binds_each_call_by_hash(self):
        RV, d, tsv = self.review_call_dir()
        scratch = '/private/tmp/claude-502/-x/sess/scratchpad'
        calls = [dict(id='1', name='Write', input=dict(file_path=f'{scratch}/h.py', content='import json\n')),
                 dict(id='2', name='Bash', input=dict(command=f'python3 -I {scratch}/h.py {tsv}'))]
        from unittest.mock import patch
        with patch.object(AR, 'old_rule_allows', lambda d, c: False):
            rev = RV.write(d, calls, 'operator', str(tsv))
            self.assertEqual(len(rev['calls']), 2)
            self.assertTrue((d/rev['helper_copies'][0]['copy']).exists())
            self.assertEqual(RV.covered(d, calls)[0], {0, 1})
            changed = [calls[0], dict(calls[1], input=dict(command=f'python3 -I {scratch}/h.py /etc/passwd'))]
            ok, problems = RV.covered(d, changed)
            self.assertEqual(ok, {0})
            self.assertTrue(problems)
            with self.assertRaisesRegex(ValueError, 'never overwrite'):
                RV.write(d, calls, 'operator', str(tsv))

    def test_ayah_lookup_output_counts_as_opened_evidence(self):
        calls = [dict(name='Bash', input=dict(command='python3 /x/corpus.py --intertext ayah 1:1 --chars 1500'),
                      result='== CC:1:1:note  [head]\nText of the note\n== QURAN:1:1\nبسم\n', is_error=False),
                 dict(name='Bash', input=dict(command='python3 /x/corpus.py --intertext get WLC:Gen.1.1'),
                      result='== WLC:Gen.1.1\nבראשית\n', is_error=False)]
        shown = set()
        requested, opened = VR.lookup_audit(calls, shown)
        self.assertEqual((requested, opened, shown), ({'WLC:Gen.1.1'}, {'WLC:Gen.1.1'}, {'CC:1:1:note', 'QURAN:1:1'}))


def load_tests(loader, tests, pattern):
    """Only the tests defined here (the inherited workflow tests run in test_workflow)."""
    names = [n for n in SemiticTest.__dict__ if n.startswith('test_')]
    return unittest.TestSuite(SemiticTest(n) for n in sorted(names))
