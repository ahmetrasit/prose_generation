"""Regressions reproduced from the 29:38/100:1 source formats."""

import copy
import gzip
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from _commentary.v5 import packet_evidence as evidence
from _commentary.v5 import workflow


class ReferenceRepairTests(unittest.TestCase):
    def test_real_channel_occurrence_list_keeps_every_context(self):
        source = (
            "ء ي ي 29:35,44; ع ل م 29:28,32,41-43; "
            "ب ي ن 29:35,38-39; ب ص ر 29:38; ت ر ك 29:35."
        )
        expected = [f"29:{a}" for a in (28, 32, 35, 38, 39, 41, 42, 43, 44)]
        self.assertEqual(workflow._extract_quran_refs(source), expected)
        self.assertEqual(workflow._extract_quran_refs(json.dumps({"text": source})), expected)

    def test_ranges_coordinates_and_corpus_bounds(self):
        self.assertEqual(workflow._extract_quran_refs("29:41–29:43,44"),
                         ["29:41", "29:42", "29:43", "29:44"])
        self.assertEqual(workflow._extract_quran_refs("29:38:22:1"), ["29:38"])
        self.assertEqual(workflow._extract_quran_refs("1:7-2:2,5"), ["1:7", "2:1", "2:2", "2:5"])
        self.assertEqual(workflow._extract_quran_refs("115:1; 29:70; 1:0; 9:0"), [])

    def test_hft_moves_with_its_current_ownership_and_counts(self):
        packets = {lane: {
            "scope": {"pericope": {"refs": ["29:38", "29:41"]},
                      "hft": {"assigned_record_count": int(lane == "macro")}},
            "candidate_inventory": [], "support_registry": [],
            "branch_registry": [], "connection_registry": [],
            "hft_evidence": {"assigned_records": []},
        } for lane in workflow.LANES}
        packets["macro"]["candidate_inventory"] = [{
            "candidate_id": "c1", "source_local_id": "hft:1", "source_type": "hft",
            "hft_ref": "h1", "anchor_refs": ["29:41"], "support_ids": ["s1"],
        }]
        packets["macro"]["support_registry"] = [{
            "support_id": "s1", "source_local_id": "hft:1", "scope": "macro",
            "payload": {"mechanism": "A wider contact at 29:41."},
        }]
        packets["macro"]["hft_evidence"]["assigned_records"] = [
            {"hft_ref": "h1", "owning_lane": "macro"}]
        composition = workflow.compositions.composition_from_cli(
            "split", ["focus=29:38", "other=29:41"], ["29:38"])
        workflow._normalize_and_route_lane_packets(packets, {"ayahRef": "29:38"}, composition)
        for lane, packet in packets.items():
            expected = int(lane == "global")
            self.assertEqual(len(packet["candidate_inventory"]), expected)
            self.assertEqual(packet["scope"]["hft"]["assigned_record_count"], expected)
            self.assertEqual(packet["hft_evidence"]["assigned_record_count"], expected)
            self.assertEqual(packet["hft_evidence"]["lane_counts"][lane], expected)
        record = packets["global"]["hft_evidence"]["assigned_records"][0]
        self.assertEqual(record["owning_lane"], "global")
        self.assertEqual(record["upstream_owning_lane"], "macro")


class SemanticRepairTests(unittest.TestCase):
    def test_caution_inference_and_published_claims_are_accounted_for(self):
        candidate = {"candidate_id": "c1", "support_ids": ["s1", "s2", "s3"]}
        supports = {
            "s1": {"support_id": "s1", "payload": {
                "rendering_caution": "Does not resolve the participle to a beneficent referent.",
                "why_still_valid": "The appeal-for-redress branch supplies the carrier.",
                "abductive_moves": [{"inference": "A social reversal remains possible."}],
            }},
            "s2": {"support_id": "s2", "text": json.dumps({"text": "Published local claim."})},
            "s3": {"support_id": "s3", "payload": ["A discarded branch remains counterevidence."]},
        }
        obligations = workflow._candidate_semantic_obligations(candidate, supports)
        self.assertEqual({o["kind"] for o in obligations}, {
            "rendering_caution", "why_still_valid", "abductive_moves", "candidate_text", "hft_claim"})
        self.assertEqual(len({o["obligation_ref"] for o in obligations}), 5)

    def test_prompt_keeps_complete_records_without_string_lookups(self):
        detail = {"lexical_item": "a red-veined eye film resembling woven webbing",
                  "boundary": "A separate same-root lexical item; not the meaning of the focus form."}
        packet = {"branches": [{"id": "B010", "detail": detail},
                               {"id": "B011", "detail": detail}],
                  "support": [detail, {"quoted_boundary": detail["boundary"]}]}
        original = copy.deepcopy(packet)
        prompt = workflow._build_scope_prompt(workflow.layout_for("29:38"), "micro", packet)
        rendered = prompt.split("<lane_packet_json>\n", 1)[1].split("\n</lane_packet_json>", 1)[0]
        decoded = json.loads(rendered)
        self.assertEqual(decoded, original)
        self.assertEqual(packet, original)
        self.assertNotIn("$v5_ref", prompt)
        self.assertNotIn("shared_evidence", decoded)

    def test_historical_compact_packets_can_still_be_decoded(self):
        packet = {"branch": {"$v5_ref": 1}, "shared_evidence": [
            {"ref": 1, "value": {"lexical_item": "eye film", "boundary": {"$v5_ref": 2}}},
            {"ref": 2, "value": "A separate same-root item, not the focus meaning."},
        ]}
        self.assertEqual(evidence.expand_packet(packet), {"branch": {
            "lexical_item": "eye film", "boundary": "A separate same-root item, not the focus meaning."}})


class ContextEvidenceTests(unittest.TestCase):
    def test_exact_arabic_and_typed_target_survive_without_a_target_bundle(self):
        connection = sqlite3.connect(":memory:")
        columns = ",".join(f"{key} TEXT" for key in evidence.MORPHEME_COLUMNS)
        connection.execute(f"CREATE TABLE qac_morphemes ({columns},surah INT,ayah INT,word_index INT,morpheme_index INT)")
        row = ("7:201:12:1", "مُّبْصِرُونَ", "مُبْصِر", "ب ص ر", "N", "STEM",
               "STEM|POS:N|ACT|PCPL|(IV)|LEM:muboSir|ROOT:bSr|MP|NOM", 7, 201, 12, 1)
        connection.execute("INSERT INTO qac_morphemes VALUES (?,?,?,?,?,?,?,?,?,?,?)", row)
        packet = {"review_inventory": {"context_refs": ["7:201"]},
                  "connection_registry": [{"target_ref": "7:201", "qualification": {}}]}
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "qac.sqlite.gz"
            path.write_bytes(gzip.compress(connection.serialize()))
            evidence.attach_context_evidence({"global": packet},
                {"7:201": {"arabic_uthmani": "فَإِذَا هُم مُبْصِرُونَ"}}, path, Path(temporary) / "cache")
        connection.close()
        self.assertEqual(packet["context_evidence"][0]["morphemes"], [list(row[:7])])
        self.assertEqual(packet["context_evidence_coverage"]["missing_morphology_refs"], [])
        self.assertTrue(packet["connection_registry"][0]["qualification"]["target_morphology_supplied"])

    def test_unavailable_morphology_is_reported_without_erasing_arabic(self):
        packet = {"review_inventory": {"context_refs": ["7:201"]}}
        with tempfile.TemporaryDirectory() as temporary:
            evidence.attach_context_evidence({"global": packet},
                {"7:201": {"arabic_uthmani": "مُبْصِرُونَ"}}, Path(temporary) / "missing.gz")
        self.assertEqual(packet["context_evidence"][0]["arabic_uthmani"], "مُبْصِرُونَ")
        self.assertEqual(packet["context_evidence_coverage"]["missing_morphology_refs"], ["7:201"])

    def test_corrupt_morphology_is_reported_without_erasing_arabic(self):
        packet = {"review_inventory": {"context_refs": ["7:201"]}}
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "corrupt.gz"
            # Valid gzip header followed by an invalid DEFLATE block type.
            path.write_bytes(bytes.fromhex("1f8b0800000000000003") + b"\x07" + b"\x00" * 8)
            evidence.attach_context_evidence({"global": packet},
                {"7:201": {"arabic_uthmani": "مُبْصِرُونَ"}}, path, Path(temporary) / "cache")
        self.assertEqual(packet["context_evidence"][0]["arabic_uthmani"], "مُبْصِرُونَ")
        self.assertEqual(packet["context_evidence_coverage"]["missing_morphology_refs"], ["7:201"])
        self.assertIn("could not be projected", packet["context_evidence_coverage"]["morphology_error"])

    def test_focus_morphology_covers_self_references_and_its_prefatory_alias(self):
        packet = {
            "identity": {"ayah_ref": "29:0", "linguistic_source_ref": "1:1"},
            "focus": {"qac_morphemes": [{"qac_ref": "1:1:1:1"}]},
            "review_inventory": {"context_refs": []},
            "connection_registry": [{"target_ref": "29:0"}, {"target_ref": "1:1"}],
        }
        with tempfile.TemporaryDirectory() as temporary:
            evidence.attach_context_evidence({"micro": packet}, {}, Path(temporary) / "missing.gz")
        self.assertEqual(packet["context_evidence"], [])
        for connection in packet["connection_registry"]:
            self.assertTrue(connection["qualification"]["target_morphology_supplied"])


if __name__ == "__main__":
    unittest.main()
