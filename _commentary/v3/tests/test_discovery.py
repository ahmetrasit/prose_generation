from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path


V3_ROOT = Path(__file__).resolve().parent.parent

import sys

sys.path.insert(0, str(V3_ROOT))

from tests.test_prepare import fixture_bundle  # noqa: E402
from v3lib.common import (  # noqa: E402
    BudgetError,
    ScopeError,
    ValidationError,
    canonical_json_bytes,
    canonical_sha256,
    load_json_object_bounded,
    parse_json_object_bytes,
    pretty_json_bytes,
)
from v3lib.discovery import (  # noqa: E402
    DiscoveryOptions,
    build_context_manifest,
    build_discovery_packets,
    build_lane_store,
    build_rehydration_request,
    fulfill_rehydration_request,
    rehydrate_packet_records,
    source_snapshot,
    validate_context_manifest,
    validate_discovery_packets,
    validate_lane_store,
    validate_rehydration_response,
)


def shifted_bundle(bundle: dict, *, ayah: int) -> dict:
    encoded = json.dumps(bundle, ensure_ascii=False)
    shifted = json.loads(encoded.replace("29:38", f"29:{ayah}"))
    shifted["ayah"] = ayah
    return shifted


def snapshot(bundle: dict, name: str) -> dict:
    return source_snapshot(
        bundle,
        raw=pretty_json_bytes(bundle),
        source_path=Path(name),
    )


def rehash_store(store: dict) -> None:
    record_id_changes: dict[str, str] = {}
    for record in store["records"]:
        old_id = record["record_id"]
        envelope = {key: value for key, value in record.items() if key != "record_id"}
        record["record_id"] = f"rec_{canonical_sha256(envelope)[:24]}"
        record_id_changes[old_id] = record["record_id"]
    for atom in store["atoms"]:
        for edge in atom["evidence_refs"]:
            edge["record_id"] = record_id_changes.get(edge["record_id"], edge["record_id"])
        envelope = {key: value for key, value in atom.items() if key != "atom_id"}
        atom["atom_id"] = f"atom_{canonical_sha256(envelope)[:24]}"
    store["records"].sort(key=lambda item: item["record_id"])
    store["atoms"].sort(key=lambda item: item["atom_id"])
    store["coverage"] = {
        "record_count": len(store["records"]),
        "atom_count": len(store["atoms"]),
        "record_ids_sha256": canonical_sha256(
            [item["record_id"] for item in store["records"]]
        ),
        "atom_ids_sha256": canonical_sha256(
            [item["atom_id"] for item in store["atoms"]]
        ),
        "exact_payloads_only": True,
    }
    store["identity"].pop("store_payload_sha256", None)
    store["identity"]["store_payload_sha256"] = canonical_sha256(store)


def rehash_packet(packet: dict) -> None:
    record_ids = [record["record_id"] for record in packet["records"]]
    atom_ids = [atom["atom_id"] for atom in packet["atoms"]]
    coverage_root = canonical_sha256(
        {"ordered_record_ids": record_ids, "ordered_atom_ids": atom_ids}
    )
    packet["identity"]["coverage_root_sha256"] = coverage_root
    packet["coverage"] = {
        "ordered_record_ids": record_ids,
        "ordered_atom_ids": atom_ids,
        "record_count": len(record_ids),
        "atom_count": len(atom_ids),
        "coverage_root_sha256": coverage_root,
        "exact_payloads_only": True,
    }
    packet["identity"].pop("packet_payload_sha256", None)
    packet["identity"]["packet_payload_sha256"] = canonical_sha256(packet)


def rehash_manifest(manifest: dict, packets: list[dict]) -> None:
    manifest["identity"]["packet_payload_sha256s"] = [
        packet["identity"]["packet_payload_sha256"] for packet in packets
    ]
    manifest["identity"].pop("packet_set_payload_sha256", None)
    manifest["identity"]["packet_set_payload_sha256"] = canonical_sha256(manifest)


class DiscoveryTests(unittest.TestCase):
    def setUp(self) -> None:
        first = fixture_bundle()
        first["pericope"]["ayah_from"] = 38
        first["pericope"]["ayah_to"] = 39
        first["word_morpheme_spans"] = []
        for index, row in enumerate(first["qac_morphemes"]):
            first["word_morpheme_spans"].append(
                {
                    "word_index": index,
                    "surface_ar": row["surface_ar"],
                    "word_ids": [f"word-{index}"],
                    "qac_refs": [row["qac_ref"]],
                    "morpheme_ids": [f"morpheme-{index}"],
                    "aligned_qac_word_ref_upstream": first["word_analysis"]["words"][
                        index
                    ]["aligned_qac_word_ref"],
                    "morpheme_skip_count": 0,
                }
            )
        first["channel_subchannels_anchored_here"][0]["ayah_refs"] = [
            "29:38",
            "29:39",
        ]
        first["root_lexicon"]["root_000672"]["dictionary_entry"]["branches"][1][
            "concept_map"
        ] = {
            "definition": "A web-like film over the eye.",
            "facets": [{"role": "core", "statement": "Veiling by a fine mesh."}],
        }
        first["inter_ayah_rows"] = [
            {"label": "strong", "ref": "29:39", "note": "Nearby contact."},
            {"label": "strong", "ref": "29:61", "note": "Distant contact."},
        ]
        first["branch_inventories"] = {
            "full_context_packet": {
                "source_file": "fixture",
                "branch_inventories": [
                    {
                        "root": "س ب ل",
                        "branches": [
                            {
                                "branch_id": "B010",
                                "image_en": "web-like eye film",
                                "variants": [
                                    {
                                        "root_id": "root_000672",
                                        "source_path": "fixture",
                                        "image_en": "web-like eye film",
                                    }
                                ],
                            }
                        ],
                    }
                ],
            }
        }
        first["v12_reader_walks"] = {
            "reader_a": {
                "activated_readings_md": (
                    "Retained preamble.\n"
                    "1. **A retained hypothesis.** Web and sight.\n"
                    "2. **A second hypothesis.** Worked road."
                ),
                "retrospective_surprises_md": "- **Later contact.** 29:61.",
            }
        }
        second = shifted_bundle(first, ayah=39)
        second["channel_subchannels_anchored_here"][0]["ayah_refs"] = [
            "29:38",
            "29:39",
        ]
        second["root_lexicon"]["root_000672"]["dictionary_entry"]["branches"][1][
            "concept_map"
        ]["definition"] = "A distinct 29:39 source variant."
        self.sources = [snapshot(first, "29_38.json"), snapshot(second, "29_39.json")]

    def test_context_requires_exact_pericope_source_coverage(self) -> None:
        context = build_context_manifest(self.sources, focus_ayah_ref="29:38")
        validate_context_manifest(context, self.sources)
        self.assertEqual(context["scope"]["refs"], ["29:38", "29:39"])
        with self.assertRaisesRegex(ValidationError, "exactly cover"):
            build_context_manifest(self.sources[:1], focus_ayah_ref="29:38")

    def test_snapshot_binds_parsed_raw_bytes_and_rejects_duplicate_keys(self) -> None:
        with self.assertRaisesRegex(ValidationError, "does not equal"):
            source_snapshot(
                self.sources[0]["bundle"],
                raw=self.sources[1]["raw"],
                source_path=Path("mismatch.json"),
            )
        bool_bundle = copy.deepcopy(self.sources[0]["bundle"])
        bool_bundle["identity_probe"] = True
        integer_bundle = copy.deepcopy(bool_bundle)
        integer_bundle["identity_probe"] = 1
        with self.assertRaisesRegex(ValidationError, "does not equal"):
            source_snapshot(
                integer_bundle,
                raw=pretty_json_bytes(bool_bundle),
                source_path=Path("bool-vs-int.json"),
            )
        with self.assertRaisesRegex(ValidationError, "duplicate JSON object key"):
            source_snapshot(
                {},
                raw=b'{"ayahRef":"29:38","ayahRef":"29:39"}',
                source_path=Path("duplicate.json"),
            )

    def test_required_fields_and_unrecorded_root_gaps_fail_closed(self) -> None:
        missing_field = copy.deepcopy(self.sources[0]["bundle"])
        missing_field.pop("qac_morphemes")
        malformed_sources = [snapshot(missing_field, "missing.json"), self.sources[1]]
        with self.assertRaisesRegex(ValidationError, "qac_morphemes must be an array"):
            build_lane_store(
                malformed_sources, lane="micro", focus_ayah_ref="29:38"
            )

        gap_bundle = copy.deepcopy(self.sources[0]["bundle"])
        gap_bundle["root_lexicon"].pop("root_001046")
        gap_bundle["coverage"] = {
            "root_lexicon": {
                "per_root": {
                    "ع م ل": {
                        "root_id": None,
                        "root_ids": [],
                        "root_mapping": {
                            "mapping_status": "no_frozen_rooted_surface_match"
                        },
                        "dictionary_present": False,
                    }
                }
            }
        }
        gap_sources = [snapshot(gap_bundle, "gap.json"), self.sources[1]]
        store = build_lane_store(
            gap_sources, lane="micro", focus_ayah_ref="29:38"
        )
        gaps = [record for record in store["records"] if record["role"] == "root_grounding_gap"]
        self.assertEqual(len(gaps), 1)
        self.assertTrue(
            any(
                edge["record_id"] == gaps[0]["record_id"]
                for atom in store["atoms"]
                for edge in atom["evidence_refs"]
            )
        )
        gap_atoms = [
            atom
            for atom in store["atoms"]
            if any(
                edge["record_id"] == gaps[0]["record_id"]
                for edge in atom["evidence_refs"]
            )
        ]
        self.assertTrue(gap_atoms)
        self.assertTrue(all(atom["hypothesis"] for atom in gap_atoms))
        contradictory = copy.deepcopy(gap_bundle)
        contradictory["coverage"]["root_lexicon"]["per_root"]["ع م ل"][
            "root_mapping"
        ]["mapping_status"] = "matched"
        with self.assertRaisesRegex(ValidationError, "not explicit"):
            build_lane_store(
                [snapshot(contradictory, "contradictory-gap.json"), self.sources[1]],
                lane="micro",
                focus_ayah_ref="29:38",
            )
        gap_bundle.pop("coverage")
        with self.assertRaisesRegex(ValidationError, "lack exact root records"):
            build_lane_store(
                [snapshot(gap_bundle, "unrecorded-gap.json"), self.sources[1]],
                lane="micro",
                focus_ayah_ref="29:38",
            )

    def test_malformed_nested_collections_raise_controlled_errors(self) -> None:
        malformed = copy.deepcopy(self.sources[0]["bundle"])
        malformed["word_morpheme_spans"][0]["qac_refs"] = [[]]
        with self.assertRaisesRegex(ValidationError, "qac refs must be strings"):
            build_lane_store(
                [snapshot(malformed, "nested-list.json"), self.sources[1]],
                lane="micro",
                focus_ayah_ref="29:38",
            )
        missing_ref = copy.deepcopy(self.sources[0]["bundle"])
        missing_ref["inter_ayah_rows"] = [{"note": "missing ref"}]
        with self.assertRaisesRegex(ValidationError, "canonical ayah ref"):
            build_lane_store(
                [snapshot(missing_ref, "missing-ref.json"), self.sources[1]],
                lane="global",
                focus_ayah_ref="29:38",
            )
        with self.assertRaisesRegex(ValidationError, "exactly equal ordered pericope"):
            build_lane_store(
                self.sources,
                lane="macro",
                focus_ayah_ref="29:38",
                target_refs=[[]],
            )

    def test_qac_span_and_channel_lineage_fail_closed(self) -> None:
        qac_mismatch = copy.deepcopy(self.sources[0]["bundle"])
        qac_mismatch["qac_morphemes"][0]["qac_word_ref"] = "29:38:2"
        with self.assertRaisesRegex(ValidationError, "disagrees with its QAC word"):
            build_lane_store(
                [snapshot(qac_mismatch, "qac-mismatch.json"), self.sources[1]],
                lane="micro",
                focus_ayah_ref="29:38",
            )

        cross_word = copy.deepcopy(self.sources[0]["bundle"])
        cross_word["word_morpheme_spans"][0]["qac_refs"] = [
            "29:38:1:1",
            "29:38:2:1",
        ]
        cross_word["word_morpheme_spans"][0]["morpheme_ids"] = ["m0", "m1"]
        with self.assertRaisesRegex(ValidationError, "crosses substantive"):
            build_lane_store(
                [snapshot(cross_word, "cross-word.json"), self.sources[1]],
                lane="micro",
                focus_ayah_ref="29:38",
            )

        reused = copy.deepcopy(self.sources[0]["bundle"])
        reused["word_morpheme_spans"][1]["qac_refs"] = ["29:38:1:1"]
        with self.assertRaisesRegex(ValidationError, "invalid or reused QAC lineage"):
            build_lane_store(
                [snapshot(reused, "reused-span.json"), self.sources[1]],
                lane="micro",
                focus_ayah_ref="29:38",
            )

        misaligned = copy.deepcopy(self.sources[0]["bundle"])
        misaligned["word_morpheme_spans"][0][
            "aligned_qac_word_ref_upstream"
        ] = "29:38:2"
        with self.assertRaisesRegex(ValidationError, "word-analysis row"):
            build_lane_store(
                [snapshot(misaligned, "misaligned-span.json"), self.sources[1]],
                lane="micro",
                focus_ayah_ref="29:38",
            )

        malformed_channel = copy.deepcopy(self.sources[0]["bundle"])
        malformed_channel["channel_subchannels_anchored_here"][0]["ayah_refs"] = "29:38"
        with self.assertRaisesRegex(ValidationError, "ayah_refs must be an array"):
            build_lane_store(
                [snapshot(malformed_channel, "malformed-channel.json"), self.sources[1]],
                lane="macro",
                focus_ayah_ref="29:38",
            )

        outside_channel = copy.deepcopy(self.sources[0]["bundle"])
        outside_channel["channel_subchannels_anchored_here"][0]["ayah_refs"] = [
            "29:38",
            "29:61",
        ]
        with self.assertRaisesRegex(ValidationError, "outside its pericope"):
            build_lane_store(
                [snapshot(outside_channel, "outside-channel.json"), self.sources[1]],
                lane="macro",
                focus_ayah_ref="29:38",
            )

    def test_pericope_width_is_bounded_before_materialization(self) -> None:
        huge = copy.deepcopy(self.sources[0]["bundle"])
        huge["pericope"]["ayah_from"] = 1
        huge["pericope"]["ayah_to"] = 1_000_000
        with self.assertRaisesRegex(ScopeError, "hard limit is 512"):
            build_context_manifest(
                [snapshot(huge, "huge.json")], focus_ayah_ref="29:38"
            )

    def test_nonmacro_target_overrides_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValidationError, "only for the reusable macro"):
            build_lane_store(
                self.sources,
                lane="micro",
                focus_ayah_ref="29:38",
                target_refs=["29:38"],
            )

    def test_pathological_json_depth_is_a_controlled_validation_error(self) -> None:
        raw = b'{"x":' + (b"[" * 2_000) + b"0" + (b"]" * 2_000) + b"}"
        with self.assertRaises(ValidationError):
            parse_json_object_bytes(raw, label="deep.json")

    def test_micro_store_preserves_complete_nested_branch_payload(self) -> None:
        store = build_lane_store(
            self.sources,
            lane="micro",
            focus_ayah_ref="29:38",
        )
        validate_lane_store(store, self.sources)
        root_records = [
            record for record in store["records"] if record["role"] == "root_lexicon"
        ]
        web = next(
            record
            for record in root_records
            if record["payload"].get("root_id") == "root_000672"
        )
        branch = web["payload"]["dictionary_entry"]["branches"][1]
        self.assertEqual(
            branch["concept_map"]["facets"][0]["statement"],
            "Veiling by a fine mesh.",
        )
        web_atom = next(
            atom
            for atom in store["atoms"]
            if atom["branch_refs"] == ["root_000672/B010"]
        )
        self.assertEqual(web_atom["evidence_refs"][0]["record_id"], web["record_id"])

        mutated_sources = copy.deepcopy(self.sources)
        mutated_sources[0]["bundle"]["root_lexicon"]["root_000672"][
            "dictionary_entry"
        ]["branches"][1]["concept_map"]["facets"][0]["statement"] = "Changed"
        mutated_sources[0] = snapshot(
            mutated_sources[0]["bundle"], "29_38.json"
        )
        mutated = build_lane_store(
            mutated_sources,
            lane="micro",
            focus_ayah_ref="29:38",
        )
        mutated_web = next(
            record
            for record in mutated["records"]
            if record["role"] == "root_lexicon"
            and record["payload"].get("root_id") == "root_000672"
        )
        self.assertNotEqual(web["record_id"], mutated_web["record_id"])

    def test_macro_packet_set_is_lossless_and_atom_exhaustive(self) -> None:
        options = DiscoveryOptions(
            max_record_bytes=200_000,
            max_packet_bytes=120_000,
            max_store_bytes=2_000_000,
        )
        store = build_lane_store(
            self.sources,
            lane="macro",
            focus_ayah_ref="29:38",
            target_refs=["29:38", "29:39"],
            options=options,
        )
        packets, manifest = build_discovery_packets(
            store, self.sources, options=options
        )
        validate_discovery_packets(
            store, self.sources, packets, manifest, options=options
        )
        self.assertGreater(len(packets), 1)
        self.assertTrue(manifest["coverage"]["all_atoms_assigned_once"])
        self.assertTrue(manifest["coverage"]["all_records_visible"])
        packet_atom_ids = [
            atom["atom_id"] for packet in packets for atom in packet["atoms"]
        ]
        self.assertEqual(
            sorted(packet_atom_ids), sorted(atom["atom_id"] for atom in store["atoms"])
        )
        exact_records = {record["record_id"]: record for record in store["records"]}
        for packet in packets:
            for record in packet["records"]:
                self.assertEqual(record, exact_records[record["record_id"]])

        forged = copy.deepcopy(packets)
        forged[0]["records"][0]["payload"] = "projected"
        payload = copy.deepcopy(forged[0])
        payload["identity"].pop("packet_payload_sha256")
        from v3lib.common import canonical_sha256

        forged[0]["identity"]["packet_payload_sha256"] = canonical_sha256(payload)
        with self.assertRaisesRegex(ValidationError, "do not exactly rederive"):
            validate_discovery_packets(
                store, self.sources, forged, manifest, options=options
            )

    def test_macro_requires_full_scope_and_quarantines_hft_inventory(self) -> None:
        with self.assertRaisesRegex(ValidationError, "exactly equal ordered pericope"):
            build_lane_store(
                self.sources,
                lane="macro",
                focus_ayah_ref="29:38",
                target_refs=["29:38"],
            )
        store = build_lane_store(
            self.sources, lane="macro", focus_ayah_ref="29:38"
        )
        inventories = [
            record for record in store["records"] if record["role"] == "branch_inventories"
        ]
        self.assertTrue(inventories)
        self.assertTrue(all(record["hypothesis"] and not record["citable"] for record in inventories))
        inventory_ids = {record["record_id"] for record in inventories}
        inventory_atoms = [
            atom
            for atom in store["atoms"]
            if any(edge["record_id"] in inventory_ids for edge in atom["evidence_refs"])
        ]
        self.assertTrue(inventory_atoms)
        self.assertTrue(all(atom["hypothesis"] for atom in inventory_atoms))
        self.assertTrue(
            any(atom["kind"] == "hft_branch_inventory_branch" for atom in inventory_atoms)
        )

    def test_every_record_has_atoms_and_all_edges_resolve(self) -> None:
        for lane in ("micro", "macro", "global"):
            with self.subTest(lane=lane):
                store = build_lane_store(
                    self.sources, lane=lane, focus_ayah_ref="29:38"
                )
                validate_lane_store(store, self.sources)
                covered = {
                    edge["record_id"]
                    for atom in store["atoms"]
                    for edge in atom["evidence_refs"]
                }
                self.assertEqual(
                    covered, {record["record_id"] for record in store["records"]}
                )
        macro = build_lane_store(
            self.sources, lane="macro", focus_ayah_ref="29:38"
        )
        self.assertTrue(any(atom["kind"] == "morpheme" for atom in macro["atoms"]))
        self.assertTrue(any(atom["kind"] == "morpheme_span" for atom in macro["atoms"]))

    def test_recomputed_store_forgeries_are_rejected(self) -> None:
        store = build_lane_store(
            self.sources, lane="global", focus_ayah_ref="29:38"
        )
        pointer_forgery = copy.deepcopy(store)
        target_atom = next(
            atom for atom in pointer_forgery["atoms"] if atom["kind"] == "morpheme"
        )
        target_atom["evidence_refs"][0]["pointer"] = "/999999"
        rehash_store(pointer_forgery)
        with self.assertRaisesRegex(ValidationError, "does not resolve"):
            validate_lane_store(pointer_forgery, self.sources)

        trust_forgery = copy.deepcopy(store)
        hypothesis = next(record for record in trust_forgery["records"] if record["hypothesis"])
        hypothesis["citable"] = True
        rehash_store(trust_forgery)
        with self.assertRaisesRegex(ValidationError, "cannot be citable"):
            validate_lane_store(trust_forgery, self.sources)

        type_forgery = copy.deepcopy(store)
        type_forgery["coverage"]["exact_payloads_only"] = 1
        type_forgery["identity"].pop("store_payload_sha256")
        type_forgery["identity"]["store_payload_sha256"] = canonical_sha256(type_forgery)
        with self.assertRaisesRegex(ValidationError, "coverage is inconsistent"):
            validate_lane_store(type_forgery, self.sources)

    def test_reader_segments_use_exact_spans_and_include_preamble(self) -> None:
        store = build_lane_store(
            self.sources, lane="global", focus_ayah_ref="29:38"
        )
        walk_record = next(
            record for record in store["records"] if record["role"] == "v12_reader_walks"
        )
        edges = [
            edge
            for atom in store["atoms"]
            for edge in atom["evidence_refs"]
            if edge["record_id"] == walk_record["record_id"] and "span" in edge
        ]
        self.assertGreaterEqual(len(edges), 4)
        self.assertTrue(all("#" not in edge["pointer"] for edge in edges))
        activated = [
            edge for edge in edges if edge["pointer"].endswith("activated_readings_md")
        ]
        self.assertEqual(min(edge["span"]["start"] for edge in activated), 0)
        inter_record = next(
            record for record in store["records"] if record["role"] == "inter_ayah_row"
        )
        inter_atoms = [
            atom
            for atom in store["atoms"]
            if any(edge["record_id"] == inter_record["record_id"] for edge in atom["evidence_refs"])
        ]
        self.assertEqual(inter_atoms[0]["anchor_refs"], ["29:38", "29:61"])

    def test_packet_metadata_and_local_evidence_are_not_rehashable(self) -> None:
        options = DiscoveryOptions(
            max_record_bytes=200_000,
            max_packet_bytes=120_000,
            max_store_bytes=2_000_000,
        )
        store = build_lane_store(
            self.sources,
            lane="macro",
            focus_ayah_ref="29:38",
            options=options,
        )
        packets, manifest = build_discovery_packets(
            store, self.sources, options=options
        )
        forged_packets = copy.deepcopy(packets)
        forged_manifest = copy.deepcopy(manifest)
        forged_packets[0]["identity"]["focus_ayah_ref"] = "29:999"
        forged_packets[0]["record_catalog"] = []
        forged_packets[0]["contract"]["hypotheses_are_not_evidence"] = False
        rehash_packet(forged_packets[0])
        rehash_manifest(forged_manifest, forged_packets)
        with self.assertRaisesRegex(ValidationError, "do not exactly rederive"):
            validate_discovery_packets(
                store,
                self.sources,
                forged_packets,
                forged_manifest,
                options=options,
            )

        type_forged_packets = copy.deepcopy(packets)
        type_forged_packets[0]["contract"]["atomic_dispositions_required"] = 1
        with self.assertRaisesRegex(ValidationError, "do not exactly rederive"):
            validate_discovery_packets(
                store,
                self.sources,
                type_forged_packets,
                manifest,
                options=options,
            )

        moved_packets = copy.deepcopy(packets)
        moved_manifest = copy.deepcopy(manifest)
        source_index = next(
            index
            for index, packet in enumerate(moved_packets)
            if any(atom["kind"] == "root_branch" for atom in packet["atoms"])
        )
        moved_atom = next(
            atom
            for atom in moved_packets[source_index]["atoms"]
            if atom["kind"] == "root_branch"
        )
        evidence_id = moved_atom["evidence_refs"][0]["record_id"]
        destination_index = next(
            index
            for index, packet in enumerate(moved_packets)
            if index != source_index
            and evidence_id not in {record["record_id"] for record in packet["records"]}
        )
        moved_packets[source_index]["atoms"].remove(moved_atom)
        moved_packets[destination_index]["atoms"].append(moved_atom)
        moved_packets[destination_index]["atoms"].sort(key=lambda item: item["atom_id"])
        rehash_packet(moved_packets[source_index])
        rehash_packet(moved_packets[destination_index])
        rehash_manifest(moved_manifest, moved_packets)
        with self.assertRaisesRegex(ValidationError, "do not exactly rederive"):
            validate_discovery_packets(
                store,
                self.sources,
                moved_packets,
                moved_manifest,
                options=options,
            )

    def test_rehydration_is_exact_and_content_bound(self) -> None:
        options = DiscoveryOptions(
            max_record_bytes=200_000,
            max_packet_bytes=120_000,
            max_store_bytes=2_000_000,
        )
        store = build_lane_store(
            self.sources,
            lane="macro",
            focus_ayah_ref="29:38",
            options=options,
        )
        packets, manifest = build_discovery_packets(
            store, self.sources, options=options
        )
        requester = packets[0]
        local_ids = {record["record_id"] for record in requester["records"]}
        requested_id = next(
            record["record_id"] for record in store["records"] if record["record_id"] not in local_ids
        )
        request = build_rehydration_request(
            store,
            self.sources,
            packets,
            manifest,
            requester_packet_sha256=requester["identity"]["packet_payload_sha256"],
            record_ids=[requested_id],
            options=options,
        )
        response = fulfill_rehydration_request(
            store,
            self.sources,
            packets,
            manifest,
            request,
            options=options,
        )
        validate_rehydration_response(
            store,
            self.sources,
            packets,
            manifest,
            request,
            response,
            options=options,
        )
        rehydrated = rehydrate_packet_records(
            store,
            self.sources,
            packets,
            manifest,
            request,
            requester,
            response,
            options=options,
        )
        self.assertIn(requested_id, {record["record_id"] for record in rehydrated})
        forged = copy.deepcopy(response)
        forged["records"][0]["payload"] = "projected"
        forged["coverage"]["records_payload_sha256"] = canonical_sha256(forged["records"])
        forged["identity"].pop("response_payload_sha256")
        forged["identity"]["response_payload_sha256"] = canonical_sha256(forged)
        with self.assertRaisesRegex(ValidationError, "not exact store material"):
            validate_rehydration_response(
                store,
                self.sources,
                packets,
                manifest,
                request,
                forged,
                options=options,
            )

    def test_global_hypotheses_are_visible_but_non_citable(self) -> None:
        store = build_lane_store(
            self.sources,
            lane="global",
            focus_ayah_ref="29:38",
        )
        hypothesis_records = [record for record in store["records"] if record["hypothesis"]]
        self.assertTrue(hypothesis_records)
        self.assertTrue(all(not record["citable"] for record in hypothesis_records))
        hypothesis_atoms = [atom for atom in store["atoms"] if atom["hypothesis"]]
        self.assertTrue(hypothesis_atoms)
        packets, manifest = build_discovery_packets(store, self.sources)
        validate_discovery_packets(store, self.sources, packets, manifest)

    def test_budgets_fail_instead_of_projecting_records(self) -> None:
        options = DiscoveryOptions(max_record_bytes=100, max_store_bytes=1_000)
        with self.assertRaisesRegex(BudgetError, "Nothing was projected or truncated"):
            build_lane_store(
                self.sources,
                lane="micro",
                focus_ayah_ref="29:38",
                options=options,
            )

    def test_record_and_store_budgets_measure_complete_wire_objects(self) -> None:
        baseline = build_lane_store(
            self.sources,
            lane="micro",
            focus_ayah_ref="29:38",
        )
        record_limit = max(
            len(canonical_json_bytes(record)) for record in baseline["records"]
        )
        store_limit = len(canonical_json_bytes(baseline))
        exact = DiscoveryOptions(
            max_record_bytes=record_limit,
            max_store_bytes=store_limit,
        )
        bounded = build_lane_store(
            self.sources,
            lane="micro",
            focus_ayah_ref="29:38",
            options=exact,
        )
        self.assertLessEqual(
            max(len(canonical_json_bytes(record)) for record in bounded["records"]),
            record_limit,
        )
        self.assertLessEqual(len(canonical_json_bytes(bounded)), store_limit)

        with self.assertRaisesRegex(BudgetError, "Exact evidence record"):
            build_lane_store(
                self.sources,
                lane="micro",
                focus_ayah_ref="29:38",
                options=DiscoveryOptions(
                    max_record_bytes=record_limit - 1,
                    max_store_bytes=store_limit,
                ),
            )
        with self.assertRaisesRegex(BudgetError, "Discovery store is"):
            build_lane_store(
                self.sources,
                lane="micro",
                focus_ayah_ref="29:38",
                options=DiscoveryOptions(max_store_bytes=store_limit - 1),
            )

    def test_bounded_loader_accepts_huge_limit_without_overflow(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "small.json"
            path.write_bytes(b"{}")
            value, raw = load_json_object_bounded(path, max_bytes=10**100)
            self.assertEqual(value, {})
            self.assertEqual(raw, b"{}")


if __name__ == "__main__":
    unittest.main()
