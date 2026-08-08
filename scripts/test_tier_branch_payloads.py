#!/usr/bin/env python3

import copy
import tempfile
import unittest
from pathlib import Path

import tier_branch_payloads as tiering


def branch(root_id, branch_id, *, image="صورة", what="تعريف"):
    return {
        "branch_ref": f"{root_id}/{branch_id}",
        "branch_image_ar": image,
        "what_is_ar": what,
        "what_is_not_ar": "مرفوض",
        "identity_judgment": {
            "status": "distinct",
            "rationale": "keep on explicit branches",
            "boundary_note": "remove everywhere",
        },
        "lexicalization_scope": {
            "branch_kind": "mixed_non_bare",
            "note": "keep on explicit branches",
        },
        "source_phrase_ar": "عبارة المصدر",
        "concept_gloss": {"text": f"concept {root_id}/{branch_id}"},
        "contextual_glosses": [{"text": "context"}],
        "lexical_glosses": [{"text": "lexical"}],
        "concept_map": {"definition": "definition fallback"},
    }


def root_record(root_id, role, branches):
    return {
        "root_ar": "ر ف ع",
        "qac_roots_ar": ["ر ف ع"],
        "root_id": root_id,
        "root_mapping_role": role,
        "root_mapping_roles": [role],
        "qac_root_mappings": [{"root_mapping_role": role}],
        "dictionary_entry": {"branches": branches, "non_branch": "unchanged"},
        "dictionary_source_file": f"quran-data/{root_id}.json",
        "gloss": {
            "branches": [
                {
                    "branch_ref": item["branch_ref"],
                    "concept_gloss": {"text": f"reviewed {item['branch_ref']}"},
                    "contextual_glosses": [{"text": "reviewed context"}],
                    "extra": "keep only when explicit",
                }
                for item in branches
            ],
            "non_branch": "unchanged",
        },
        "gloss_source_file": f"quran-data/{root_id}.gloss.json",
    }


def valid_bundle():
    first = [
        branch("root_000001", "B001"),
        branch("root_000001", "B003"),
        branch("root_000001", "B004", image="", what=""),
        branch("root_000001", "B007"),
    ]
    second = [branch("root_000002", "B007")]
    return {
        "bundle_type": "ayah",
        "ayahRef": "12:1",
        "coverage": {
            "word_analysis": {"present": True},
            "v12_focus_trace_hermetic": {"present": True},
            "v12_reader_walks": {"present": False},
            "v12_reader_walks_wide": {"present": False},
            "v12_cross_run_publication": {"present": False},
            "channel_review": {"present": False},
            "inter_ayah": {"present": False},
            "butuncul_okuma": {"present": False},
            "branch_inventories": {"present": True},
            "root_lexicon": {"present": True},
        },
        "root_lexicon": {
            "root_000001": root_record("root_000001", "dominant", first),
            "root_000002": root_record("root_000002", "non_dominant", second),
        },
        "branch_inventories": {
            "full_context_packet": {
                "branch_inventories": [{
                    "root": "ر ف ع",
                    "branches": [{
                        "branch_id": "B007",
                        "variants": [
                            {"root_id": "root_000001"},
                            {"root_id": "root_000002"},
                        ],
                    }],
                }],
            },
        },
        "word_analysis": {"words": [], "must_remain": "yes"},
        "qac_morphemes": [],
        "word_morpheme_spans": [],
        "v12_focus_trace_hermetic": {
            "readers": {
                "reader_a": {
                    "activation_trace": [{
                        "mapped_root_id": "root_000001",
                        "branch_id": "B003",
                    }],
                },
            },
        },
        "v12_reader_walks": {},
        "v12_reader_walks_wide": {},
        "v12_cross_run_publication": {},
        "channel_subchannels_anchored_here": [],
        "inter_ayah_rows": [],
        "butuncul_okuma_line": None,
        "unrelated": {"must": ["remain", "byte-for-byte equivalent"]},
    }


def without_projected_surfaces(bundle):
    result = copy.deepcopy(bundle)
    result.get("coverage", {}).get("root_lexicon", {}).pop("branch_policy", None)
    for root in result["root_lexicon"].values():
        if root.get("dictionary_entry") is not None:
            root["dictionary_entry"]["branches"] = "BRANCHES"
        if root.get("gloss") is not None:
            root["gloss"]["branches"] = "BRANCHES"
    return result


class TierBranchPayloadTests(unittest.TestCase):
    def test_tiers_preserve_roots_refs_and_every_nonbranch_field(self):
        source = valid_bundle()
        tiered, policy = tiering.tier_bundle(source)

        self.assertEqual(without_projected_surfaces(source), without_projected_surfaces(tiered))
        self.assertEqual(set(source["root_lexicon"]), set(tiered["root_lexicon"]))
        self.assertEqual(policy["dictionary_branches_dropped"], 0)

        branches = {
            item["branch_ref"]: item
            for root in tiered["root_lexicon"].values()
            for item in root["dictionary_entry"]["branches"]
        }
        explicit = branches["root_000001/B003"]
        self.assertEqual(explicit["payload_tier"], "explicit_interest")
        self.assertIn("source_phrase_ar", explicit)
        self.assertIn("lexical_glosses", explicit)
        self.assertNotIn("what_is_not_ar", explicit)
        self.assertNotIn("boundary_note", explicit["identity_judgment"])

        safety = branches["root_000001/B001"]
        self.assertEqual(safety["payload_tier"], "local_low_branch_safety")
        self.assertNotIn("source_phrase_ar", safety)

        compact = branches["root_000001/B004"]
        self.assertEqual(compact["payload_tier"], "compact_rest")
        self.assertEqual(compact["semantic_fallback"], "reviewed root_000001/B004")

        glosses = {
            item["branch_ref"]: item
            for root in tiered["root_lexicon"].values()
            for item in root["gloss"]["branches"]
        }
        self.assertEqual(
            set(glosses),
            {
                item["branch_ref"]
                for root in source["root_lexicon"].values()
                for item in root["gloss"]["branches"]
            },
        )
        self.assertEqual(
            set(glosses["root_000001/B004"]),
            {"branch_ref", "payload_tier"},
        )

    def test_general_scanner_handles_root_forms_and_promotes_ambiguous_targets(self):
        source = valid_bundle()
        maps = tiering.build_resolution_maps(source)
        ledger = tiering.InterestLedger()
        tiering.collect_text_citations(
            "test",
            (
                "quranic:root_000001:B003/m01; root_000001/B004; "
                "ر ف ع B007"
            ),
            maps,
            ledger,
        )
        self.assertEqual(
            ledger.refs,
            {
                "root_000001/B003",
                "root_000001/B004",
                "root_000001/B007",
                "root_000002/B007",
            },
        )
        self.assertEqual(len(ledger.ambiguous), 1)
        self.assertEqual(ledger.ambiguous[0]["resolution"], "promote_all_candidates")

    def test_missing_required_source_field_fails(self):
        source = valid_bundle()
        del source["word_analysis"]
        with self.assertRaisesRegex(tiering.TieringError, "missing required bundle field"):
            tiering.tier_bundle(source)

    def test_coverage_payload_contradiction_fails(self):
        source = valid_bundle()
        source["coverage"]["v12_reader_walks"]["present"] = True
        with self.assertRaisesRegex(tiering.TieringError, "present is true"):
            tiering.tier_bundle(source)

    def test_malformed_structured_hft_anchor_fails(self):
        source = valid_bundle()
        source["v12_focus_trace_hermetic"]["readers"]["reader_a"][
            "activation_trace"
        ][0].pop("branch_id")
        with self.assertRaisesRegex(tiering.TieringError, "invalid_or_missing_branch_id"):
            tiering.tier_bundle(source)

    def test_branch_without_any_semantic_payload_fails(self):
        source = valid_bundle()
        target = source["root_lexicon"]["root_000001"]
        dictionary_branch = target["dictionary_entry"]["branches"][2]
        dictionary_branch["concept_gloss"] = {}
        dictionary_branch["concept_map"] = {}
        target["gloss"]["branches"][2]["concept_gloss"] = {}
        with self.assertRaisesRegex(tiering.TieringError, "has no branch_image_ar"):
            tiering.tier_bundle(source)

    def test_missing_input_file_is_a_hard_cli_error(self):
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "missing.json"
            with self.assertRaisesRegex(SystemExit, "does not exist"):
                tiering.main([str(missing), "--check"])


if __name__ == "__main__":
    unittest.main()
