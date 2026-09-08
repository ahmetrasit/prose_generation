"""Real-source regressions for accepted overlaps and forged/stale bundle joins."""

import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch

from _commentary import qac_analysis_bridge as bridge


class AcceptedAnalysisBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not (bridge.DEFAULT_DATA_ROOT / bridge.BRIDGE_PATH).is_file():
            raise unittest.SkipTest("Requires the frozen quran-data bridge release")
        cls.source = bridge.get_bridge()
        cls.bundle = json.loads((bridge.ROOT / "bundles/s029/29_38.ayah.json").read_text())
        cls.bundle["word_morpheme_spans"], cls.bundle["coverage"]["word_morpheme_spans"] = cls.source.align(
            cls.bundle["word_analysis"], cls.bundle["qac_morphemes"])

    def test_whole_expression_and_pronoun_share_the_verified_occurrence(self):
        refs = bridge.validate_bundle(self.bundle, source_ref="29:38")
        self.assertEqual(refs[12], ["29:38:9:1", "29:38:9:2"])
        self.assertEqual(refs[13], ["29:38:9:2"])
        self.assertTrue(all(refs))
        self.assertEqual(len(refs), 23)

    def test_preparation_delivers_every_topic_and_the_exact_pronoun_link(self):
        from _commentary.v5 import workflow
        original = workflow._build_scope_prompt
        received = {}

        def inspect_prompt(layout, lane, packet):
            prompt = original(layout, lane, packet)
            decoded = json.loads(prompt.rsplit("<lane_packet_json>\n", 1)[1].split(
                "\n</lane_packet_json>", 1)[0])
            for candidate in decoded["candidate_inventory"]:
                if candidate["source_type"] == "word_analysis":
                    received[candidate["source_local_id"]] = candidate
            return prompt

        args = workflow._parser().parse_args(["prepare", "--ayah", "29:38", "--check-only"])
        refs, args.composition = workflow._resolve_request(args)
        args.ayah = refs[0]
        with patch.object(workflow, "_build_scope_prompt", inspect_prompt):
            self.assertEqual(workflow.prepare(args)["status"], "checked")
        expected = {t["topic_id"] for w in self.bundle["word_analysis"]["words"] for t in w["topics"]}
        self.assertEqual(set(received), expected)
        self.assertEqual(received["29:38:14:pronoun-chain"]["word_alignment"], {
            "analysis_ref": "29:38:14", "qac_refs": ["29:38:9:2"], "status": "accepted"})

    def test_bridge_tag_does_not_authorize_an_arbitrary_reused_morpheme(self):
        altered = copy.deepcopy(self.bundle)
        altered["word_morpheme_spans"][13]["qac_refs"] = ["29:38:11:2"]
        with self.assertRaisesRegex(ValueError, "differ from the accepted bridge"):
            bridge.validate_bundle(altered, source_ref="29:38")

    def test_sparse_analysis_ids_preserve_all_late_topics(self):
        from _commentary.v5 import workflow
        source = bridge.ROOT / "bundles/s005-pericopes/p01_001-011/5_3.ayah.json"
        args = workflow._parser().parse_args([
            "prepare", "--ayah", "5:3", "--source-bundle", str(source),
            "--context-bundles-dir", str(source.parent), "--check-only",
            "--analysis-id", "bridge-sparse-ids", "--segment", "package=5:1-11",
        ])
        refs, args.composition = workflow._resolve_request(args)
        args.ayah = refs[0]
        bundle, docket = workflow._load_focus_inputs(
            args, Path(args.context_bundles_dir), Path(args.member_bundles_dir))
        self.assertEqual(len(bundle["word_analysis"]["words"]), 67)
        self.assertEqual(docket["focus"]["word_analysis_refs"][-1], "5:3:80")
        expected = {t["topic_id"] for w in bundle["word_analysis"]["words"] for t in w["topics"]}
        received = {c["source_local_id"] for c in docket["candidates"] if c["source_type"] == "word_analysis"}
        self.assertEqual(len(expected), 102)
        self.assertEqual(received, expected)

    def test_dropping_a_resolved_entry_cannot_hide_behind_coverage(self):
        altered = copy.deepcopy(self.bundle)
        altered["word_morpheme_spans"][13] = None
        with self.assertRaisesRegex(ValueError, "differ from the accepted bridge"):
            bridge.validate_bundle(altered, source_ref="29:38")

    def test_compact_packets_keep_all_restored_sparse_topics_and_exact_links(self):
        from _commentary.v5 import workflow
        cases = (
            ("5:3", "s005-pericopes/p01_001-011", "5:1-11", 102),
            ("12:31", "s012-pericopes/p02_019-035", "12:19-35", 106),
            ("24:31", "s024-pericopes/p01_001-034", "24:1-34", 80),
        )
        for ref, package, segment, count in cases:
            with self.subTest(ref=ref):
                directory = bridge.ROOT / "bundles" / package
                source = json.loads((directory / (ref.replace(":", "_") + ".ayah.json")).read_text())
                expected = {
                    topic["topic_id"]: {
                        "analysis_ref": f"{ref}:{word['critical_w']}",
                        "qac_refs": list(span["qac_refs"]) if span else [],
                        "status": "accepted" if span else "excluded-source-defect",
                    }
                    for word, span in zip(source["word_analysis"]["words"], source["word_morpheme_spans"])
                    for topic in word["topics"]
                }
                packets = {}
                render = workflow._build_scope_prompt

                def capture(layout, lane, packet):
                    prompt = render(layout, lane, packet)
                    packets[lane] = json.loads(prompt.rsplit("<lane_packet_json>\n", 1)[1].split(
                        "\n</lane_packet_json>", 1)[0])
                    return prompt

                args = workflow._parser().parse_args([
                    "prepare", "--ayah", ref, "--context-bundles-dir", str(directory),
                    "--analysis-id", "compact-bridge-check", "--segment", "package=" + segment,
                    "--check-only",
                ])
                refs, args.composition = workflow._resolve_request(args)
                args.ayah = refs[0]
                with patch.object(workflow, "_build_scope_prompt", capture):
                    self.assertEqual(workflow.prepare(args)["status"], "checked")
                received = {
                    c["source_local_id"]: c["word_alignment"]
                    for c in packets["micro"]["candidate_inventory"]
                    if c["source_type"] == "word_analysis"
                }
                self.assertEqual(len(expected), count)
                self.assertEqual(received, expected)
                for lane in ("macro", "global"):
                    self.assertFalse(any(c["source_type"] == "word_analysis"
                                         for c in packets[lane]["candidate_inventory"]))
                for packet in packets.values():
                    self.assertNotIn("context_evidence", packet)
                    self.assertNotIn("review_inventory", packet)

    def test_stale_provenance_is_rejected_even_with_correct_edges(self):
        altered = copy.deepcopy(self.bundle)
        altered["coverage"]["word_morpheme_spans"]["bridge"]["source_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "provenance or coverage is stale"):
            bridge.validate_bundle(altered, source_ref="29:38")

    def test_changed_source_analysis_and_morphology_are_rejected(self):
        altered = copy.deepcopy(self.bundle)
        altered["word_analysis"]["words"][13]["prose"] += " altered"
        with self.assertRaisesRegex(ValueError, "released source"):
            bridge.validate_bundle(altered, source_ref="29:38")
        altered = copy.deepcopy(self.bundle)
        altered["qac_morphemes"][0]["surface_ar"] = "altered"
        with self.assertRaisesRegex(ValueError, "canonical QAC"):
            bridge.validate_bundle(altered, source_ref="29:38")

    def test_reviewed_source_exclusion_keeps_its_analysis_and_reason(self):
        record = self.source._analysis(17)["17:28"]
        qac = [dict(row) for row in self.source.qac.execute(
            "SELECT * FROM qac_morphemes WHERE surah=17 AND ayah=28 ORDER BY word_index,morpheme_index")]
        original = copy.deepcopy(record)
        spans, coverage = self.source.align(record, qac)
        self.assertEqual(record, original)
        gap, = coverage["unresolved"]
        self.assertEqual(gap["analysis_ref"], "17:28:12")
        self.assertEqual(gap["status"], "excluded-source-defect")
        self.assertTrue(gap["reason"])
        self.assertIsNone(spans[gap["word_index"]])


if __name__ == "__main__":
    unittest.main()
