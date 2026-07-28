from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "_translation" / "v1" / "tools"
sys.path.insert(0, str(TOOLS))

import build_anchor_input  # noqa: E402
import assemble  # noqa: E402
import build_bundle  # noqa: E402
import check_anchors  # noqa: E402
import check_output  # noqa: E402
import instantiate  # noqa: E402


def synthetic_v3_from_v4(v4_seed: dict) -> dict:
    return {
        "schemaVersion": "primary-anchor-seed-v3",
        "surah": v4_seed["surah"],
        "anchors": [
            {
                "qacMorphemeRef": anchor["qacMorphemeRef"],
                "rootId": anchor["primary"]["rootId"],
                "branchIds": list(anchor["primary"]["branchIds"]),
                "lexicalUnitIds": [],
                "consideredNotPrimary": [],
            }
            for anchor in v4_seed["anchors"]
        ],
        "unresolved": copy.deepcopy(v4_seed["unresolved"]),
    }


class TranslationV1Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.anchor_input = build_anchor_input.build_anchor_input(87)
        cls.v4_seed = json.loads(
            (
                ROOT
                / "_translation"
                / "v1"
                / "source"
                / "s087.primary-anchors.json"
            ).read_text(encoding="utf-8")
        )
        if cls.v4_seed.get("schemaVersion") != "primary-anchor-seed-v4":
            raise AssertionError("canonical S87 anchor seed must be v4")
        cls.legacy_seed = synthetic_v3_from_v4(cls.v4_seed)
        cls.translation_input = build_bundle.build_bundle(87, "tr")

    def test_anchor_input_is_compact_exhaustive_and_turkish_assisted(self) -> None:
        data = self.anchor_input
        self.assertEqual(data["schemaVersion"], "anchor-input-v2")
        self.assertEqual(data["coverage"]["rootedStems"], 53)
        self.assertEqual(data["coverage"]["branches"], 429)
        self.assertEqual(
            data["assistance"]["ordinaryTurkishBaseline"]["language"],
            "tr",
        )
        roster = json.loads(
            (
                ROOT.parent
                / "latent_activation"
                / "_status"
                / "v12_cross_run"
                / "s087"
                / "ayah_roster.v3.json"
            ).read_text(encoding="utf-8")
        )
        baseline_source = data["assistance"]["ordinaryTurkishBaseline"]
        self.assertEqual(
            baseline_source,
            {
                "protocol": "v12-cross-run-ayah-roster-v3",
                "language": "tr",
                "hashScope": "frozen-baseline-bundle",
                "baselineBundleSha256": roster["baseline_sha256"],
            },
        )
        self.assertEqual(data["ayat"][0]["ayahRef"], "1:1")
        self.assertTrue(data["ayat"][0]["ordinaryTurkishBaseline"]["targetTokens"])

        for root_id, root in data["roots"].items():
            self.assertEqual(root["rootId"], root_id)
            for branch in root["branches"]:
                self.assertEqual(set(branch), {"branchId", "what_is_ar"})
        for ayah in data["ayat"]:
            for stem in ayah["rootedStems"]:
                self.assertEqual(
                    set(stem["rootResolution"]),
                    {"mappingStatus", "targets"},
                )
                self.assertTrue(stem["rootResolution"]["targets"])
                self.assertTrue(
                    all(
                        set(target) == {"rootId", "rootNormAr"}
                        and target["rootNormAr"]
                        for target in stem["rootResolution"]["targets"]
                    )
                )

        split_stem = next(
            stem
            for ayah in data["ayat"]
            for stem in ayah["rootedStems"]
            if stem["qacMorphemeRef"] == "87:11:2:2"
        )
        self.assertEqual(
            split_stem["rootResolution"]["targets"],
            [
                {"rootId": "root_000808", "rootNormAr": "ش ق و"},
                {"rootId": "root_000809", "rootNormAr": "ش ق ي"},
            ],
        )

    def test_baseline_alignment_reports_missing_and_foreign_word_refs(self) -> None:
        baseline = {
            "targetTokens": [
                {
                    "text": "örnek",
                    "qacWordRefs": ["87:1:1", "87:1:9"],
                }
            ]
        }
        with self.assertRaises(build_anchor_input.RequiredSourceMissing) as raised:
            build_anchor_input.validate_exact_baseline_alignment(
                "87:1",
                baseline,
                {"87:1:1", "87:1:2"},
            )
        self.assertIn("missing=['87:1:2']", str(raised.exception))
        self.assertIn("foreign=['87:1:9']", str(raised.exception))

    def test_baseline_provenance_ignores_publication_findings(self) -> None:
        roster = json.loads(
            (
                ROOT.parent
                / "latent_activation"
                / "_status"
                / "v12_cross_run"
                / "s087"
                / "ayah_roster.v3.json"
            ).read_text(encoding="utf-8")
        )
        publication = json.loads(
            (
                ROOT.parent
                / "quran-data"
                / "data"
                / "analysis"
                / "ayah-activation"
                / "v12-cross-run"
                / "tr"
                / "87_ayah_findings_publication.json"
            ).read_text(encoding="utf-8")
        )
        changed_findings = copy.deepcopy(publication)
        changed_findings["ayat"][0]["findings"].append(
            {"synthetic": "finding-only change"}
        )

        with mock.patch.object(
            build_anchor_input,
            "read_json",
            return_value=publication,
        ):
            original = build_anchor_input.ordinary_turkish_baselines(87, roster)
        with mock.patch.object(
            build_anchor_input,
            "read_json",
            return_value=changed_findings,
        ):
            changed = build_anchor_input.ordinary_turkish_baselines(87, roster)
        self.assertEqual(changed, original)

    def test_generated_input_json_uses_compact_utf8_serialization(self) -> None:
        value = {"text": "Türkçe", "nested": {"value": 1}}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "input.json"
            build_bundle.write_compact_json(path, value)
            encoded = path.read_bytes()
        self.assertEqual(
            encoded,
            '{"text":"Türkçe","nested":{"value":1}}\n'.encode("utf-8"),
        )

    def test_v4_seed_validates_root_scoped_primary_and_resonance(self) -> None:
        seed = self.v4_seed
        self.assertEqual(check_anchors.check(self.anchor_input, seed), [])

        invalid = copy.deepcopy(seed)
        invalid["anchors"][0]["resonances"] = [
            {"rootId": "root_999999", "branchIds": ["B001"]}
        ]
        errors = check_anchors.check(self.anchor_input, invalid)
        self.assertTrue(any("not among" in error for error in errors))

    def test_stage1_consumes_v4_primary_shape(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "s087.primary-anchors.json"
            path.write_text(
                json.dumps(self.v4_seed, ensure_ascii=False),
                encoding="utf-8",
            )
            rebuilt = build_bundle.build_bundle(87, "tr", anchor_path=path)
        legacy_cards = [
            (card.get("rootId"), card.get("branchIds"))
            for ayah in self.translation_input["ayat"]
            for card in ayah["cards"]
        ]
        v4_cards = [
            (card.get("rootId"), card.get("branchIds"))
            for ayah in rebuilt["ayat"]
            for card in ayah["cards"]
        ]
        self.assertEqual(v4_cards, legacy_cards)

    def test_legacy_seed_remains_structurally_usable_with_v2_input(self) -> None:
        self.assertEqual(self.legacy_seed["schemaVersion"], "primary-anchor-seed-v3")
        self.assertTrue(
            all(
                set(anchor)
                == {
                    "qacMorphemeRef",
                    "rootId",
                    "branchIds",
                    "lexicalUnitIds",
                    "consideredNotPrimary",
                }
                and anchor["lexicalUnitIds"] == []
                and anchor["consideredNotPrimary"] == []
                for anchor in self.legacy_seed["anchors"]
            )
        )
        self.assertEqual(
            check_anchors.check(self.anchor_input, self.legacy_seed),
            [],
        )

    def test_translation_input_exposes_only_selected_turkish_branches(self) -> None:
        data = self.translation_input
        self.assertEqual(data["schemaVersion"], "translation-input-v2")
        self.assertEqual(build_bundle.validate_translation_input(data), [])

        rooted = 0
        evidence_refs = []
        for ayah in data["ayat"]:
            for card in ayah["cards"]:
                self.assertNotIn("candidateGlossSources", card)
                self.assertNotIn("rootResolution", card)
                self.assertNotIn("qacWordRef", card)
                self.assertNotIn("glossId", card)
                self.assertNotIn("glossSource", card)
                if "rootId" not in card:
                    self.assertNotIn("evidenceRef", card)
                    continue
                rooted += 1
                evidence_refs.append(card["evidenceRef"])
                selected = set(card["branchIds"])
                source = data["selectedBranchEvidence"][card["evidenceRef"]]
                self.assertNotIn("evidenceLanguage", source)
                self.assertNotIn("lexicalSenses", source)
                for field in ("branchCores", "contextualSenses"):
                    self.assertTrue(
                        all(
                            item["branchId"] in selected
                            for item in source[field]
                        )
                    )
        self.assertEqual(rooted, 53)
        self.assertEqual(set(evidence_refs), set(data["selectedBranchEvidence"]))
        self.assertLess(len(set(evidence_refs)), rooted)

    def test_stage1_registry_supports_multiple_selected_branches(self) -> None:
        self.assertEqual(
            build_bundle.selected_evidence_ref(
                "root_001210",
                ["B003", "B001"],
            ),
            "root_001210/B001+B003",
        )
        with self.assertRaises(ValueError):
            build_bundle.selected_evidence_ref(
                "root_001210",
                ["B001", "B001"],
            )

        multi_seed = copy.deepcopy(self.v4_seed)
        anchor = next(
            item
            for item in multi_seed["anchors"]
            if item["qacMorphemeRef"] == "1:1:1:2"
        )
        anchor["primary"]["branchIds"] = ["B005", "B006"]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "s087.primary-anchors.json"
            path.write_text(
                json.dumps(multi_seed, ensure_ascii=False),
                encoding="utf-8",
            )
            rebuilt = build_bundle.build_bundle(87, "tr", anchor_path=path)
        card = next(
            card
            for ayah in rebuilt["ayat"]
            for card in ayah["cards"]
            if card["qacMorphemeRef"] == "1:1:1:2"
        )
        self.assertEqual(card["evidenceRef"], "root_000745/B005+B006")
        self.assertEqual(
            {
                item["branchId"]
                for item in rebuilt["selectedBranchEvidence"][
                    card["evidenceRef"]
                ]["branchCores"]
            },
            {"B005", "B006"},
        )
        self.assertEqual(build_bundle.validate_translation_input(rebuilt), [])

    def test_evidence_language_defaults_to_target_and_preserves_bridge(self) -> None:
        target = build_bundle.compact_gloss_source(
            {
                "evidenceLanguage": "tr",
                "branchCores": [],
                "contextualSenses": [],
            },
            "tr",
        )
        bridge = build_bundle.compact_gloss_source(
            {
                "evidenceLanguage": "en",
                "branchCores": [],
                "contextualSenses": [],
            },
            "tr",
        )
        self.assertNotIn("evidenceLanguage", target)
        self.assertEqual(bridge["evidenceLanguage"], "en")

        bridge_bundle = copy.deepcopy(self.translation_input)
        first_source = next(iter(bridge_bundle["selectedBranchEvidence"].values()))
        first_source["evidenceLanguage"] = "en"
        self.assertEqual(
            build_bundle.validate_translation_input(bridge_bundle),
            [],
        )
        first_source["evidenceLanguage"] = "tr"
        self.assertTrue(
            any(
                "matching targetLanguage must be omitted" in error
                for error in build_bundle.validate_translation_input(bridge_bundle)
            )
        )

    def test_translation_input_validator_rejects_removed_fields(self) -> None:
        invalid = copy.deepcopy(self.translation_input)
        rooted = next(
            card
            for ayah in invalid["ayat"]
            for card in ayah["cards"]
            if "rootId" in card
        )
        rooted["qacWordRef"] = "87:1:1"
        source = invalid["selectedBranchEvidence"][rooted["evidenceRef"]]
        source["lexicalSenses"] = []
        errors = build_bundle.validate_translation_input(invalid)
        self.assertTrue(any("qacWordRef" in error for error in errors))
        self.assertTrue(any("lexicalSenses is forbidden" in error for error in errors))

    def test_gloss_error_profiles_preserve_every_supported_field(self) -> None:
        evidence = build_bundle.gloss_evidence(
            {
                "text": "örnek",
                "facet_ids": ["F001"],
                "error": {
                    "fit": "narrowing",
                    "preserves": "çekirdek",
                    "loses_facet_ids": ["F002"],
                    "loses": "ayrıntı",
                    "adds": "fazlalık",
                    "collision": "yakın anlam",
                    "reason": "gerekçe",
                },
            }
        )
        self.assertEqual(
            evidence["errorProfile"],
            {
                "fit": "narrowing",
                "preserves": "çekirdek",
                "losesFacetIds": ["F002"],
                "loses": "ayrıntı",
                "adds": "fazlalık",
                "collision": "yakın anlam",
                "reason": "gerekçe",
            },
        )

    def test_assemble_derives_agent_hidden_ids_and_preserves_s87_wording(self) -> None:
        authored = json.loads(
            (
                ROOT
                / "_translation"
                / "v1"
                / "authored"
                / "tr"
                / "s087.authored.json"
            ).read_text(encoding="utf-8")
        )
        assembled = assemble.assemble(
            self.translation_input,
            authored,
            "tr",
            87,
            {
                "quranDataReleaseId": self.translation_input["quranDataReleaseId"],
                "anchorsSha256": "test",
                "bundleSha256": "test",
                "authoredSha256": "test",
                "assemblerVersion": "test",
            },
        )
        self.assertEqual(
            check_output.check(self.translation_input, assembled, 87, "tr"),
            [],
        )
        first_rooted = next(
            card
            for ayah in assembled["ayat"]
            for card in ayah["cards"]
            if "rootId" in card
        )
        ref = first_rooted["qacMorphemeRef"]
        self.assertEqual(first_rooted["qacWordRef"], ref.rsplit(":", 1)[0])
        self.assertEqual(
            first_rooted["occurrenceGloss"]["glossId"],
            f"tr:v1:{ref}",
        )
        self.assertEqual(
            [ayah["translation"]["text"] for ayah in assembled["ayat"]],
            [authored["ayat"][ayah["ayahRef"]]["text"] for ayah in assembled["ayat"]],
        )

    def test_instantiated_artifact_paths_have_one_surah_prefix(self) -> None:
        anchor_prompt, anchor_manifest = instantiate.build_prompt(
            instantiate.STAGES["anchors"],
            87,
            None,
            "2026-07-28",
        )
        self.assertEqual(
            anchor_manifest["output_artifact"],
            "_translation/v1/source/s087.primary-anchors.json",
        )
        self.assertIn(
            "`_translation/v1/source/s087.primary-anchors.json`",
            anchor_prompt,
        )

        _, translation_manifest = instantiate.build_prompt(
            instantiate.STAGES["translation"],
            87,
            "tr",
            "2026-07-28",
        )
        self.assertEqual(
            translation_manifest["output_artifact"],
            "_translation/v1/authored/tr/s087.authored.json",
        )


if __name__ == "__main__":
    unittest.main()
