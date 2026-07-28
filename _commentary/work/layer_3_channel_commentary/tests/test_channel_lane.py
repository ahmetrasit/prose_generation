from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

WORK_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WORK_ROOT / "scripts"))

import build_channel_bundle as builder  # noqa: E402
import check_channel_bundle  # noqa: E402
import check_channel_integration  # noqa: E402
import check_channel_overlays  # noqa: E402
import instantiate_channel  # noqa: E402
import render_channel_preview  # noqa: E402


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ChannelBundleTests(unittest.TestCase):
    def test_s87_bundle_is_compact_and_grounded(self) -> None:
        data = builder.build(87)
        self.assertEqual(data["bundleType"], "combined-channel-commentary")
        self.assertEqual(
            data["coverage"]["reviewedChannels"]["reviewStatus"], "reviewed"
        )
        self.assertEqual(data["primaryBranchMap"]["status"], "complete")
        self.assertTrue(data["primaryBranchMap"]["entries"])
        self.assertEqual(check_channel_bundle.validate_data(data, 87), [])

    def test_review_synthesis_and_standalone_source_are_preserved(self) -> None:
        source = {
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
                            "active_motifs": "trace `ع ص ر:B001/m01`",
                            "synthesis": "source synthesis",
                            "ayah_refs": ["1:1"],
                        }
                    ],
                },
                {
                    "name": "standalone",
                    "subchannels": [],
                    "reading_type": "latent/lexical",
                    "active_motifs": "trace `ع ص ر:B001/m01`",
                    "synthesis": "standalone synthesis",
                    "ayah_refs": ["1:1"],
                },
            ]
        }
        normalized = builder.normalize_review(source, 1)
        self.assertEqual(
            normalized["parent_channels"][0]["subchannels"][0]["synthesis"],
            "source synthesis",
        )
        self.assertEqual(
            normalized["parent_channels"][1]["synthesis"],
            "standalone synthesis",
        )

    def test_root_id_citations_compile_like_arabic_root_citations(self) -> None:
        review = {
            "parent_channels": [
                {
                    "key": "P01",
                    "subchannels": [
                        {
                            "key": "x",
                            "active_motifs": (
                                "quranic:root_000001:B002/m01 and "
                                "`ع ص ر:B003/m02`"
                            ),
                            "ayah_refs": ["1:1"],
                        }
                    ],
                }
            ]
        }
        anchors = [
            {
                "anchorId": "a001-0001",
                "ayahRef": "1:1",
                "qacMorphemeRef": "1:1:1:1",
                "root_ar": "ع ص ر",
                "rootId": "root_000001",
                "rootOccurrenceStatus": "resolved",
            }
        ]
        mapping = builder.build_motif_anchor_map(review, anchors)
        self.assertEqual(
            mapping["root_000001"]["B002"]["m01"]["anchorIds"],
            ["a001-0001"],
        )
        self.assertEqual(
            mapping["ع ص ر"]["B003"]["m02"]["anchorIds"],
            ["a001-0001"],
        )

    def test_recurrence_is_not_root_ambiguity(self) -> None:
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
                {"qac_ref": "1:1:1:1", "root_ar": "ع ص ر", "surface_ar": "عصر"},
                {"qac_ref": "1:1:2:1", "root_ar": "ع ص ر", "surface_ar": "عصر"},
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
        self.assertEqual(ambiguous, [])
        self.assertTrue(
            all(item["rootOccurrenceStatus"] == "resolved" for item in anchors)
        )
        self.assertTrue(all(len(item["recurrenceRefs"]) == 2 for item in anchors))

    def test_build_is_deterministic(self) -> None:
        self.assertEqual(builder.build(103), builder.build(103))


def integration_fixture(bundle: dict, bundle_path: Path) -> dict:
    _, allowed, statuses, source_refs, errors = (
        check_channel_integration.load_bundle(bundle_path)
    )
    if errors:
        raise AssertionError(errors)
    triples = sorted(
        allowed,
        key=lambda item: (
            int(item[0].split(":")[1]),
            statuses[item] != "non-primary",
            item,
        ),
    )
    selected = None
    for first in triples:
        for second in triples:
            if first[0].split(":")[:2] == second[0].split(":")[:2]:
                continue
            pair = sorted((first, second), key=lambda item: int(item[0].split(":")[1]))
            if any(statuses[item] == "non-primary" for item in pair):
                selected = pair
                break
        if selected:
            break
    if selected is None:
        raise AssertionError("fixture needs two ayahs and a non-primary member")

    members = []
    for index, triple in enumerate(selected, 1):
        qac, root_id, branch_id = triple
        ayah_ref = ":".join(qac.split(":")[:2])
        members.append(
            {
                "memberId": f"member-{index}",
                "ayahRef": ayah_ref,
                "qacMorphemeRef": qac,
                "rootId": root_id,
                "branchId": branch_id,
                "primaryStatus": statuses[triple],
                "surface_tr": f"member {index}",
                "contribution_tr": f"contribution {index}",
                "evidenceRefs": ["compiled-bundle"],
            }
        )
    floor = bundle["primaryFloor"]
    basis = (
        {
            "status": "authored",
            "sourcePath": floor["sourcePath"],
            "sourceSha256": floor["sourceSha256"],
            "apparatusStatus": "canonical-translation-floor",
        }
        if floor["status"] == "authored"
        else {
            "status": "arabic-only-inference",
            "apparatusStatus": "writer-primary-inference",
        }
    )
    first_source = sorted(source_refs)[0]
    coverage = [
        (
            {
                "sourceRef": source_ref,
                "disposition": "integrated",
                "channelIds": ["traveler-image"],
            }
            if source_ref == first_source
            else {
                "sourceRef": source_ref,
                "disposition": "apparatus-only",
                "channelIds": [],
                "reason_tr": "Bu kompozisyonda ayrıca görünür kılınmadı.",
            }
        )
        for source_ref in sorted(source_refs)
    ]
    return {
        "schemaVersion": "surah-channel-integration-v1",
        "surah": bundle["surah"],
        "sourceLane": "combined-layer3-layer2.5",
        "sourceBundle": str(bundle_path),
        "sourceBundleSha256": sha(bundle_path),
        "primaryFloorBasis": basis,
        "channels": [
            {
                "channelId": "traveler-image",
                "name_tr": "Yolcu imgesi",
                "statement_tr": "İki ayet boyunca oluşan ikincil imge.",
                "wholeSurahRelation": "shifts-primary",
                "wholeSurahShift_tr": "Dua bir yolculuk olarak görünür.",
                "sourceChannels": [first_source],
                "members": members,
                "maturityStatus": "derived",
                "maturityByAyah": [
                    {
                        "ayahRef": members[0]["ayahRef"],
                        "state": "latent",
                        "newMemberIds": ["member-1"],
                        "recalledMemberIds": [],
                        "cumulativeImage_tr": "İlk iz.",
                    },
                    {
                        "ayahRef": members[1]["ayahRef"],
                        "state": "complete",
                        "newMemberIds": ["member-2"],
                        "recalledMemberIds": ["member-1"],
                        "focusAyahRelation": "shifts-primary",
                        "focusAyahShift_tr": "İki iz bir yolculuk kurar.",
                        "cumulativeImage_tr": "Yolculuk tamamlanır.",
                    },
                ],
            }
        ],
        "sourceCoverage": coverage,
    }


class IntegrationTests(unittest.TestCase):
    def make_fixture(self, directory: Path) -> tuple[dict, Path, dict, Path]:
        bundle = builder.build(103)
        bundle_path = directory / "103.channel.json"
        bundle_path.write_text(
            json.dumps(bundle, ensure_ascii=False), encoding="utf-8"
        )
        integration = integration_fixture(bundle, bundle_path)
        integration_path = directory / "103.surah.channels.integrated.json"
        integration_path.write_text(
            json.dumps(integration, ensure_ascii=False), encoding="utf-8"
        )
        return bundle, bundle_path, integration, integration_path

    def test_integration_validates_without_review_fields(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _, bundle_path, _, integration_path = self.make_fixture(Path(tmp))
            self.assertEqual(
                check_channel_integration.validate(
                    integration_path, bundle_path
                ),
                [],
            )

    def test_review_vocabulary_is_forbidden(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _, bundle_path, integration, integration_path = self.make_fixture(
                Path(tmp)
            )
            integration["reviewState"] = "reviewed"
            integration["channels"][0]["reviewDecision"] = "accepted"
            integration_path.write_text(json.dumps(integration), encoding="utf-8")
            errors = check_channel_integration.validate(
                integration_path, bundle_path
            )
            self.assertTrue(any("forbidden fields" in error for error in errors))

    def test_primary_status_is_mechanical(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _, bundle_path, integration, integration_path = self.make_fixture(
                Path(tmp)
            )
            member = integration["channels"][0]["members"][0]
            member["primaryStatus"] = (
                "primary"
                if member["primaryStatus"] != "primary"
                else "non-primary"
            )
            integration_path.write_text(json.dumps(integration), encoding="utf-8")
            errors = check_channel_integration.validate(
                integration_path, bundle_path
            )
            self.assertTrue(any("primaryStatus must be" in error for error in errors))

    def test_every_reviewed_source_must_be_accounted_for(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _, bundle_path, integration, integration_path = self.make_fixture(
                Path(tmp)
            )
            integration["sourceCoverage"].pop()
            integration_path.write_text(json.dumps(integration), encoding="utf-8")
            errors = check_channel_integration.validate(
                integration_path, bundle_path
            )
            self.assertTrue(
                any("must account for every reviewed source" in error for error in errors)
            )


class OverlayAndInstantiationTests(unittest.TestCase):
    def test_instantiator_loads_prose_only_and_authors_seven_files(self) -> None:
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
                103, "tr", "2026-07-28", bundle_path, directory, "fixture"
            )
        self.assertEqual(
            [item["kind"] for item in manifest["sources"]].count("layer2-prose"),
            3,
        )
        self.assertEqual(len(manifest["expectedArtifacts"]), 7)
        self.assertIn("103.surah.channels.integrated.json", prompt)
        self.assertNotIn("103.surah.channels.reviewed.json", prompt)
        self.assertNotIn("must not be loaded", prompt)
        self.assertNotIn(
            "103.ayah-channel-overlays.preview.md",
            manifest["expectedArtifacts"],
        )

    def test_overlay_hashes_and_deterministic_renderer(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            bundle = builder.build(103)
            bundle_path = directory / "103.channel.json"
            bundle_path.write_text(json.dumps(bundle), encoding="utf-8")
            integration = integration_fixture(bundle, bundle_path)
            integration_path = directory / "103.surah.channels.integrated.json"
            integration_path.write_text(
                json.dumps(integration, ensure_ascii=False), encoding="utf-8"
            )
            members = integration["channels"][0]["members"]
            base_paths = {}
            ayah_refs = [
                item["ayahRef"]
                for item in bundle["text"]
                if not item["ayahRef"].endswith(":0")
            ]
            for index, ayah_ref in enumerate(ayah_refs, 1):
                path = directory / f"{ayah_ref.replace(':', '_')}.prose.md"
                path.write_text(
                    f"Primary paragraph {index}.\n\nGround phrase {index}.",
                    encoding="utf-8",
                )
                base_paths[ayah_ref] = path
            member_two_index = ayah_refs.index(members[1]["ayahRef"]) + 1
            overlay = {
                "schemaVersion": "ayah-channel-overlays-v1",
                "surah": 103,
                "sourceIntegration": str(integration_path),
                "sourceIntegrationSha256": sha(integration_path),
                "baseLayer2Directory": str(directory),
                "ayahs": [],
                "coverage": {
                    "integratedChannelIds": ["traveler-image"],
                    "insertedChannelIds": ["traveler-image"],
                    "omitted": [],
                },
            }
            for ayah_ref in ayah_refs:
                insertions = []
                if ayah_ref == members[1]["ayahRef"]:
                    insertions.append(
                        {
                            "insertionId": "traveler-arrives",
                            "channelId": "traveler-image",
                            "stage": "complete",
                            "placement": {
                                "afterParagraph": 2,
                                "afterPhrase": (
                                    f"Ground phrase {member_two_index}."
                                ),
                            },
                            "newMemberIds": ["member-2"],
                            "recalledMemberIds": ["member-1"],
                            "focusAyahRelation": "shifts-primary",
                            "focusAyahShift_tr": "İki iz birleşir.",
                            "prose_tr": (
                                "İkinci iz, ilkini bir yolculuğa dönüştürür."
                            ),
                        }
                    )
                path = base_paths[ayah_ref]
                overlay["ayahs"].append(
                    {
                        "ayahRef": ayah_ref,
                        "baseProse": str(path),
                        "baseProseSha256": sha(path),
                        "insertions": insertions,
                    }
                )
            overlay_path = directory / "103.ayah-channel-overlays.json"
            overlay_path.write_text(
                json.dumps(overlay, ensure_ascii=False), encoding="utf-8"
            )
            self.assertEqual(
                check_channel_overlays.validate(
                    overlay_path, integration_path
                ),
                [],
            )
            first = render_channel_preview.render(
                overlay_path, integration_path
            )
            second = render_channel_preview.render(
                overlay_path, integration_path
            )
            self.assertEqual(first, second)
            self.assertIn("layer-2.5 id=traveler-arrives", first)
            self.assertIn("İkinci iz", first)

            overlay["ayahs"][0]["baseProseSha256"] = "0" * 64
            overlay_path.write_text(json.dumps(overlay), encoding="utf-8")
            errors = check_channel_overlays.validate(
                overlay_path, integration_path
            )
            self.assertTrue(any("baseProseSha256" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
