"""Regression checks for lossless discovery packaging and handoff provenance."""
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import augment_surah as A
import check_discovery as C
import discover as D


class DiscoveryChecks(unittest.TestCase):
    def test_all_s1_members_and_branches_survive(self):
        _, source, _ = D.B.surah_inputs(1)
        sections = D.sections(source.read_text())
        self.assertEqual(len(sections), 14)
        for section in sections:
            source_items = D.KAYNAK.search(source.read_text()[section['start']:section['end']])
            if source_items:
                self.assertEqual(len(section['members']), len(source_items.group(1).split(';')))
        for k in (4, 5):
            self.assertIn('ر ح م', sections[k-1]['roots'])
            self.assertTrue({'1:1', '1:3'} <= set(sections[k-1]['ayat']))
        guidance = next(m for m in sections[0]['members'] if m['root'] == 'ه د ي')
        self.assertEqual(guidance['branch'], 'B001, B002, B003')
        with self.assertRaises(ValueError):
            D.sections('## Test\nKaynaklar: malformed\n')

    def test_missing_empty_and_blank_note_are_distinct(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'list.tsv'
            self.assertTrue(C.check(path, 1, {'2:1': 'الم'})['schema_errors'])
            path.write_text('')
            self.assertFalse(C.check(path, 1, {'2:1': 'الم'})['schema_errors'])
            path.write_text('strong\t2:1\troot\t\n')
            self.assertTrue(C.check(path, 1, {'2:1': 'الم'})['schema_errors'])

    def test_wrong_ayah_quote_and_orthography(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'list.tsv'
            path.write_text('strong\t79:18\tscene\tوَأَهْدِيَكَ إِلَىٰ رَبِّكَ فَتَخْشَىٰ\n'
                            'strong\t26:63\tscene\tطَرِيقًا فِي الْبَحْرِ يَبَسًا\n'
                            'strong\t6:153\tscene\tهَٰذَا صِرَاطِي مُسْتَقِيمًا فَاتَّبِعُوهُ\n')
            flags = C.check(path, 1, D.M.verses())['arabic_findings']
            self.assertEqual([r['ref'] for r in flags], ['79:18', '26:63'])
            self.assertIn('79:19', flags[0]['matching_refs'])
            self.assertIn('20:77', flags[1]['matching_refs'])

    def test_merge_uses_snapshot_and_rejects_bad_runs(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(D, 'discovery_dir', return_value=Path(tmp)):
            root = Path(tmp)
            initial = '\nstrong\t2:1\troot\tFirst\n'
            extra = 'medium\t2:2\ttheme\tSecond\n'
            log = {'status': 'ok', 'turn2': {'completed': True}, 'append_only': True,
                   'tool_audit_reviewed': True, 'turn1_rows': 1}
            for model in D.MODELS:
                d = root/'sec1'/model
                d.mkdir(parents=True)
                (d/'turn1.list.tsv').write_text(initial)
                (d/'list.tsv').write_text(initial+extra)
                (d/'run.log.json').write_text(json.dumps(log))
            def merge():
                with contextlib.redirect_stdout(io.StringIO()):
                    D.merge(1, [{'k': 1, 'title': 'test'}], {'2:1': 'الم', '2:2': 'ذلك'}, 'test')
            merge()
            rows = A.section_list(1, 1, root/'sec1.merged.tsv')
            self.assertEqual([(r['ref'], r['luna_turn']) for r in rows], [('2:1', '1'), ('2:2', '2')])
            target = root/'sec1/luna/list.tsv'
            for invalid in (initial+extra+extra, extra, initial+'bad\n'):
                target.write_text(invalid)
                with self.assertRaises(ValueError): merge()
            target.write_text(initial+extra)
            (root/'sec1/luna/run.log.json').write_text(json.dumps({**log, 'status': 'partial'}))
            with self.assertRaises(ValueError): merge()

    def test_explicit_handoff_and_invalid_tier(self):
        with self.assertRaises(ValueError): A.section_list(1, 1)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)/'sec1.merged.tsv'
            path.write_text('ref\ttier\tluna_label\tluna_turn\tterra_label\tterra_turn\tbases\texplanations\n'
                            '2:1\tunknown\tstrong\t1\t\t\troot\tExample\n')
            with self.assertRaises(ValueError): A.section_list(1, 1, path)
        for tag in ('../bad', '/tmp', 'a/b'):
            with self.assertRaises(ValueError): D.discovery_dir(1, tag)


if __name__ == '__main__':
    unittest.main()
