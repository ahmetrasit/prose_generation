from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import build_channel_bundle as builder  # noqa: E402
import check_channel_bundle  # noqa: E402
import check_channel_plan  # noqa: E402
import instantiate_channel  # noqa: E402


class CombinedChannelBundleTests(unittest.TestCase):
    def test_absent_review_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            bundles = Path(tmp) / "bundles"
            directory = bundles / "s108"
            directory.mkdir(parents=True)
            (directory / "108.surah.json").write_text(
                json.dumps({"surah_scope": {}}), encoding="utf-8"
            )
            with patch.object(builder, "BUNDLES", bundles):
                with self.assertRaisesRegex(SystemExit, "absent channel review"):
                    builder.build(108)

    def test_review_preserves_synthesis_and_standalone_channels(self) -> None:
        review = {
            "parent_channels": [
                {
                    "name": "group",
                    "semantic_invariant": "invariant",
                    "surface_relation": "relation",
                    "surprising_reach": "reach",
                    "subchannels": [
                        {
                            "key": "A",
                            "name": "sub",
                            "reading_type": "mixed",
                            "scene_or_process": "redundant scene",
                            "active_motifs": "trace `ع ص ر:B001/m01`",
                            "ayah_anchors": "1:1 word",
                            "synthesis": "reviewed synthesis",
                            "ayah_refs": ["1:1"],
                        }
                    ],
                },
                {
                    "name": "standalone",
                    "subchannels": [],
                    "reading_type": "latent/lexical",
                    "scene_or_process": "redundant scene",
                    "active_motifs": "trace `ع ص ر:B001/m01`",
                    "ayah_anchors": "1:1 word",
                    "synthesis": "standalone synthesis",
                    "ayah_refs": [],
                },
            ]
        }
        normalized = builder.normalize_review(review, 1)
        grouped = normalized["parent_channels"][0]["subchannels"][0]
        standalone = normalized["parent_channels"][1]
        self.assertEqual(grouped["synthesis"], "reviewed synthesis")
        self.assertNotIn("scene_or_process", grouped)
        self.assertNotIn("ayah_anchors", grouped)
        self.assertEqual(standalone["synthesis"], "standalone synthesis")
        self.assertEqual(standalone["ayah_refs"], ["1:1"])

    def test_s87_bundle_has_compact_combined_shape(self) -> None:
        data = builder.build(87)
        self.assertEqual(
            set(data),
            {
                "schemaVersion",
                "bundleType",
                "surah",
                "reviewedChannels",
                "text",
                "anchorInventory",
                "motifAnchorMap",
                "primaryFloor",
                "primaryBranchMap",
                "coverage",
            },
        )
        self.assertEqual(data["bundleType"], "combined-channel-commentary")
        self.assertEqual(
            data["coverage"]["reviewedChannels"]["commentaryAuthorityStatus"],
            "reviewed-for-commentary",
        )
        self.assertEqual(
            sum(
                not parent["subchannels"]
                for parent in data["reviewedChannels"]["parent_channels"]
            ),
            4,
        )
        self.assertEqual(check_channel_bundle.validate_data(data, 87), [])

    def test_every_review_citation_has_compiled_mapping(self) -> None:
        data = builder.build(87)
        errors = check_channel_bundle.validate_data(data, 87)
        self.assertFalse(
            any("has no motif mapping" in error for error in errors), errors
        )

    def test_repeated_root_is_recurrence_not_identity_ambiguity(self) -> None:
        fixture = {
            "branch_inventories": {
                "default": {
                    "branch_inventories": [
                        {
                            "root": "ع ص ر",
                            "branches": [
                                {"variants": [{"root_id": "root_000001"}]}
                            ],
                        }
                    ]
                }
            },
            "qac_morphemes": [
                {
                    "qac_ref": "1:1:1:1",
                    "root_ar": "ع ص ر",
                    "surface_ar": "عصر",
                },
                {
                    "qac_ref": "1:1:2:1",
                    "root_ar": "ع ص ر",
                    "surface_ar": "عصر",
                },
            ],
        }
        with tempfile.TemporaryDirectory() as tmp:
            bundles = Path(tmp) / "bundles"
            directory = bundles / "s001"
            directory.mkdir(parents=True)
            (directory / "1_1.ayah.json").write_text(
                json.dumps(fixture), encoding="utf-8"
            )
            with patch.object(builder, "BUNDLES", bundles):
                anchors, ambiguous = builder.build_anchor_inventory(
                    1, [1], {builder.norm_root("ع ص ر")}, set()
                )
        self.assertEqual(len(anchors), 2)
        self.assertEqual(len(ambiguous), 0)
        self.assertEqual(
            {item["anchorId"] for item in anchors},
            {"a001-0001", "a001-0002"},
        )
        self.assertTrue(
            all(
                item["recurrenceRefs"]
                == ["1:1:1:1", "1:1:2:1"]
                for item in anchors
            )
        )

    def test_build_is_deterministic(self) -> None:
        self.assertEqual(builder.build(103), builder.build(103))

    def test_instantiator_reads_only_layer2_prose(self) -> None:
        bundle = builder.build(103)
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            bundle_path = directory / "103.channel.json"
            bundle_path.write_text(json.dumps(bundle), encoding="utf-8")
            for ayah in (1, 2, 3):
                (directory / f"103_{ayah}.prose.fixture.md").write_text(
                    f"Prose {ayah}.", encoding="utf-8"
                )
                (directory / f"103_{ayah}.evidence.fixture.md").write_text(
                    "must not be loaded", encoding="utf-8"
                )
            prompt, manifest = instantiate_channel.assemble(
                103,
                "tr",
                "2026-07-28",
                bundle_path,
                directory,
                "fixture",
            )
        kinds = [item["kind"] for item in manifest["sources"]]
        self.assertEqual(kinds.count("layer2-prose"), 3)
        self.assertFalse(any("evidence" in kind for kind in kinds))
        self.assertEqual(manifest["lane"], "combined-layer3-layer2.5")
        self.assertEqual(manifest["deferred"], [])
        self.assertEqual(len(manifest["expectedArtifacts"]), 8)
        self.assertIn("103.surah.channels.reviewed.json", prompt)
        self.assertNotIn("must not be loaded", prompt)


def combined_plan(bundle: dict) -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        bundle_path = Path(tmp) / "bundle.json"
        bundle_path.write_text(json.dumps(bundle), encoding="utf-8")
        allowed, errors = check_channel_plan.bundle_members(bundle_path)
    if errors:
        raise AssertionError(errors)
    selected = []
    seen_ayahs = set()
    for qac_ref, root_id, branch_id in sorted(allowed):
        ayah_ref = ":".join(qac_ref.split(":")[:2])
        if ayah_ref in seen_ayahs:
            continue
        selected.append((ayah_ref, qac_ref, root_id, branch_id))
        seen_ayahs.add(ayah_ref)
        if len(selected) == 2:
            break
    if len(selected) != 2:
        raise AssertionError("fixture needs exact members in two ayahs")

    members = []
    for index, (ayah_ref, qac_ref, root_id, branch_id) in enumerate(selected, 1):
        members.append(
            {
                "memberId": f"member-{index}",
                "ayahRef": ayah_ref,
                "qacMorphemeRef": qac_ref,
                "rootId": root_id,
                "branchId": branch_id,
                "primaryStatus": "non-primary",
                "surface_tr": f"member {index}",
                "contribution_tr": f"contribution {index}",
                "evidenceRefs": ["compiled-bundle"],
            }
        )
    floor = bundle["primaryFloor"]
    if floor["status"] == "authored":
        basis = {
            "status": "authored",
            "sourcePath": floor["sourcePath"],
            "sourceSha256": floor["sourceSha256"],
            "apparatusStatus": "typed-primary-floor",
        }
    else:
        basis = {
            "status": "arabic-only-inference",
            "apparatusStatus": "writer-primary-inference",
        }
    source_coverage = []
    for parent in bundle["reviewedChannels"]["parent_channels"]:
        if parent["subchannels"]:
            refs = [
                f"{parent['key']}/{subchannel['key']}"
                for subchannel in parent["subchannels"]
            ]
        else:
            refs = [parent["key"]]
        source_coverage.extend(
            {
                "sourceRef": source_ref,
                "disposition": "integrated",
                "channelIds": ["test-channel"],
            }
            for source_ref in refs
        )
    return {
        "schemaVersion": "surah-channel-plan-v1",
        "surah": bundle["surah"],
        "reviewState": "reviewed",
        "sourceLane": "combined",
        "primaryFloorBasis": basis,
        "sourceCoverage": source_coverage,
        "channels": [
            {
                "channelId": "test-channel",
                "name_tr": "Test",
                "statement_tr": "Test statement",
                "reviewDecision": "accepted",
                "wholeSurahRelation": "supports-primary",
                "wholeSurahShift_tr": "Whole-surah shift.",
                "sourceCandidates": [
                    {"sourceType": "network-v3", "sourceRef": "reviewed"}
                ],
                "members": members,
                "maturityStatus": "reviewed",
                "maturityByAyah": [
                    {
                        "ayahRef": members[0]["ayahRef"],
                        "state": "latent",
                        "newMemberIds": ["member-1"],
                        "recalledMemberIds": [],
                        "cumulativeImage_tr": "one",
                    },
                    {
                        "ayahRef": members[1]["ayahRef"],
                        "state": "complete",
                        "newMemberIds": ["member-2"],
                        "recalledMemberIds": ["member-1"],
                        "focusAyahRelation": "supports-primary",
                        "focusAyahShift_tr": "relation",
                        "cumulativeImage_tr": "complete",
                    },
                ],
                "rejectedMotifs": [],
            }
        ],
        "review": {
            "reviewerId": "upstream-network-v3-review",
            "reviewedAt": "2026-07-28",
            "summary_tr": "Reviewed upstream.",
        },
    }


class CombinedPlanValidationTests(unittest.TestCase):
    def validate_fixture(
        self, data: dict, bundle: dict | None
    ) -> list[str]:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            plan_path = directory / "plan.json"
            plan_path.write_text(json.dumps(data), encoding="utf-8")
            bundle_path = None
            if bundle is not None:
                bundle_path = directory / "bundle.json"
                bundle_path.write_text(json.dumps(bundle), encoding="utf-8")
            return check_channel_plan.validate(
                plan_path, "reviewed", bundle_path
            )

    def test_combined_plan_requires_bundle(self) -> None:
        bundle = builder.build(103)
        errors = self.validate_fixture(combined_plan(bundle), None)
        self.assertTrue(any("requires the source channel bundle" in e for e in errors))

    def test_exact_combined_members_validate(self) -> None:
        bundle = builder.build(103)
        self.assertEqual(self.validate_fixture(combined_plan(bundle), bundle), [])

    def test_unmapped_branch_is_rejected(self) -> None:
        bundle = builder.build(103)
        plan = combined_plan(bundle)
        plan["channels"][0]["members"][0]["branchId"] = "B999"
        errors = self.validate_fixture(plan, bundle)
        self.assertTrue(
            any("does not resolve to an exact reviewed" in error for error in errors)
        )

    def test_missing_reviewed_source_coverage_is_rejected(self) -> None:
        bundle = builder.build(103)
        plan = combined_plan(bundle)
        plan["sourceCoverage"].pop()
        errors = self.validate_fixture(plan, bundle)
        self.assertTrue(any("must account for every reviewed source" in e for e in errors))

    def test_combined_plan_cannot_defer_maturity(self) -> None:
        bundle = builder.build(103)
        plan = combined_plan(bundle)
        plan["channels"][0]["maturityStatus"] = "deferred-to-review"
        errors = self.validate_fixture(plan, bundle)
        self.assertTrue(any("maturityStatus=reviewed" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
