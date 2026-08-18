from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "_channel" / "layer3" / "scripts"
sys.path.insert(0, str(SCRIPTS))

import build_packet as layer3_build  # noqa: E402
import common as layer3_common  # noqa: E402
import finalize as layer3_finalize  # noqa: E402
import instantiate as layer3_instantiate  # noqa: E402
import validate as layer3_validate  # noqa: E402


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, value: object) -> None:
    write(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")


class Layer3WorkflowTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="layer3-test-"))
        self.quran_data = self.tmp / "qd"
        self.latent = self.tmp / "latent_activation"
        self.layer2 = self.tmp / "layer2"
        write(
            self.quran_data / "data" / "text" / "quran-uthmani.tsv",
            "42:0|basmala\n42:1|first arabic\n42:2|second arabic\n",
        )
        write_json(
            self.tmp / "floor.json",
            {
                "schemaVersion": "translation-layer-v1",
                "language": "tr",
                "surah": 42,
                "ayat": [
                    {"ayahRef": "42:1", "translation": {"text": "ilk zemin"}},
                    {"ayahRef": "42:2", "translation": {"text": "ikinci zemin"}},
                ],
            },
        )
        self.write_layer2_set(1, "a", "supports-primary")
        self.write_layer2_set(2, "b", "shifts-primary")

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp)

    def write_layer2_set(self, ayah: int, key: str, relation: str) -> None:
        write(self.layer2 / f"42_{ayah}.prose.test.md", f"prose {ayah}\n")
        write(
            self.layer2 / f"42_{ayah}.evidence.test.md",
            "## Preserved rejected readings\n\n"
            f"- Boundary for ayah {ayah}.\n\n"
            "## Coverage note\n\n"
            "ok\n",
        )
        write(
            self.layer2 / f"42_{ayah}.index.test.md",
            f"- `surprise:local-{key}` - local resonance {key} [{relation}] [inference]\n",
        )
        write(self.layer2 / f"42_{ayah}.friction.test.md", "No friction.\n")

    def packet(self) -> dict[str, object]:
        return layer3_build.build_packet(
            surah=42,
            language="tr",
            layer2_dir=self.layer2,
            layer2_label="test",
            quran_data=self.quran_data,
            latent_activation=self.latent,
            primary_floor_path=self.tmp / "floor.json",
        )

    def hypotheses(self, packet: dict[str, object]) -> dict[str, object]:
        return {
            "schemaVersion": "layer3-discovery-hypotheses-v2",
            "packetId": packet["packetId"],
            "sourceSetHash": packet["sourceSetHash"],
            "surah": 42,
            "language": "tr",
            "hypotheses": [
                {
                    "hypothesisId": "cross-care",
                    "proposedOperation": "iki hareket birbirini okutur",
                    "readerShift": {
                        "before": "iki ayet ayridir",
                        "hinge": "yerel rezonanslar birlikte calisir",
                        "after": "iki ayet tek bir hareket gibi gorunur",
                    },
                    "rhetoricalReach": [
                        {"movement": "ilk hareket", "ayahRefs": ["42:1"]},
                        {"movement": "ikinci hareket", "ayahRefs": ["42:2"]},
                    ],
                    "activationCardRefs": [],
                }
            ],
        }

    def briefs(self, packet: dict[str, object]) -> dict[str, object]:
        return {
            "schemaVersion": "layer3-channel-briefs-v2",
            "briefId": f"{packet['runId']}-briefs-v2",
            "packetId": packet["packetId"],
            "sourceSetHash": packet["sourceSetHash"],
            "surah": 42,
            "language": "tr",
            "primaryArgument": {
                "thesis": "zemin korunur",
                "development": "iki ayet birlikte ilerler",
                "surfaceFloorRefs": ["primary-floor#42:1", "primary-floor#42:2"],
            },
            "requiredReviewInputRefs": [
                "hypothesis:cross-care",
                "resonance:42:1:local-a",
                "resonance:42:2:local-b",
            ],
            "channels": [
                {
                    "channelId": "care-channel",
                    "readerName": "birlikte bakim",
                    "inputRefs": [
                        "hypothesis:cross-care",
                        "resonance:42:1:local-a",
                        "resonance:42:2:local-b",
                    ],
                    "surfaceFloorRefs": ["primary-floor#42:1", "primary-floor#42:2"],
                    "surfaceFloor": "ilk ve ikinci zemin ayakta kalir",
                    "hinges": [
                        {
                            "hingeId": "care-hinge",
                            "contribution": "yerel rezonanslar iki ayeti baglar",
                            "inputRefs": [
                                "hypothesis:cross-care",
                                "resonance:42:1:local-a",
                                "resonance:42:2:local-b",
                            ],
                            "ayahRefs": ["42:1", "42:2"],
                            "evidenceRefs": [
                                "finding:42:1:001",
                                "resonance:42:1:local-a",
                                "finding:42:2:001",
                                "resonance:42:2:local-b",
                            ],
                            "claimPolicy": {
                                "scope": "bounded",
                                "permittedForm": "rezonans olarak soyle",
                                "counterpressureRefs": ["boundary:42:1:01"],
                                "prohibitedClaims": ["yasak iddia"],
                            },
                        }
                    ],
                    "crossAyahOperation": "iki ayet karsilikli okunur",
                    "readerShift": {
                        "before": "ayri dururlar",
                        "after": "birbirini tasirlar",
                    },
                    "indispensableGain": "ikisini birlikte okuma imkani dogar",
                }
            ],
            "nonChannelDispositions": [],
        }

    def composition(self, packet: dict[str, object], briefs: dict[str, object]) -> dict[str, object]:
        return {
            "schemaVersion": "layer3-surah-composition-v1",
            "compositionId": f"{packet['runId']}-composition-v1",
            "packetId": packet["packetId"],
            "briefId": briefs["briefId"],
            "sourceSetHash": packet["sourceSetHash"],
            "surah": 42,
            "language": "tr",
            "prose": (
                "Ilk zemin ve ikinci zemin birlikte okunur. "
                "Yerel rezonanslar iki ayeti birbirine baglar. "
                "Bu bag, iki ayeti karsilikli okutur ve okuyucuya yeni birlik kazandirir."
            ),
            "evidenceMap": {
                "primaryClaims": [
                    {
                        "claimId": "primary-floor",
                        "ayahRefs": ["42:1", "42:2"],
                        "span": "Ilk zemin ve ikinci zemin birlikte okunur.",
                        "sourceRefs": ["primary-floor#42:1", "primary-floor#42:2"],
                    }
                ],
                "channelLandings": [
                    {
                        "channelId": "care-channel",
                        "operationSpan": "Bu bag, iki ayeti karsilikli okutur",
                        "gainSpan": "okuyucuya yeni birlik kazandirir",
                        "evidenceRefs": [
                            "finding:42:1:001",
                            "resonance:42:1:local-a",
                            "finding:42:2:001",
                            "resonance:42:2:local-b",
                        ],
                    }
                ],
                "hingeLandings": [
                    {
                        "hingeId": "care-hinge",
                        "span": "Yerel rezonanslar iki ayeti birbirine baglar.",
                        "evidenceRefs": [
                            "finding:42:1:001",
                            "resonance:42:1:local-a",
                            "finding:42:2:001",
                            "resonance:42:2:local-b",
                        ],
                    }
                ],
            },
            "friction": [],
        }

    def test_packet_requires_complete_layer2_handoff(self) -> None:
        (self.layer2 / "42_2.friction.test.md").unlink()

        with self.assertRaises(SystemExit) as caught:
            self.packet()

        self.assertIn("no complete Layer-2", str(caught.exception))

    def test_packet_rejects_malformed_surprise_rows(self) -> None:
        write(
            self.layer2 / "42_1.index.test.md",
            "- `surprise:local-a` - missing relation [inference]\n",
        )

        with self.assertRaises(SystemExit) as caught:
            self.packet()

        self.assertIn("must carry exactly one", str(caught.exception))

    def test_packet_and_discovery_prompt_are_layer2_blind(self) -> None:
        packet = self.packet()

        self.assertEqual(layer3_validate.validate_packet(packet), [])
        prompt = layer3_instantiate.assemble(
            stage="discover",
            surah=42,
            packet_path=self.write_artifact("packet.json", packet),
            hypotheses_path=None,
            briefs_path=None,
        )

        self.assertIn("layer3-discovery-input-v2", prompt)
        self.assertIn("ilk zemin", prompt)
        self.assertNotIn("local resonance a", prompt)
        self.assertNotIn("Boundary for ayah", prompt)
        self.assertNotIn("prose 1", prompt)

    def test_briefs_allow_many_to_many_and_require_complete_accounting(self) -> None:
        packet = self.packet()
        hypotheses = self.hypotheses(packet)
        briefs = self.briefs(packet)

        self.assertEqual(layer3_validate.validate_hypotheses(hypotheses, packet), [])
        self.assertEqual(layer3_validate.validate_briefs(briefs, packet, hypotheses), [])

        broken = json.loads(json.dumps(briefs))
        broken["channels"][0]["inputRefs"].remove("resonance:42:2:local-b")
        broken["channels"][0]["hinges"][0]["inputRefs"].remove("resonance:42:2:local-b")

        errors = layer3_validate.validate_briefs(broken, packet, hypotheses)
        self.assertTrue(any("every discovery hypothesis and local resonance" in error for error in errors))

        listed_only = json.loads(json.dumps(briefs))
        listed_only["channels"][0]["hinges"][0]["inputRefs"].remove(
            "resonance:42:2:local-b"
        )
        errors = layer3_validate.validate_briefs(listed_only, packet, hypotheses)
        self.assertTrue(any("every channel inputRef" in error for error in errors))

    def test_briefs_require_exact_resonance_finding_pairs(self) -> None:
        write(
            self.layer2 / "42_1.index.test.md",
            "- `42:1:ordinary` - ordinary finding\n"
            "- `surprise:local-a` - local resonance a [supports-primary] [inference]\n",
        )
        packet = self.packet()
        hypotheses = self.hypotheses(packet)
        briefs = self.briefs(packet)
        for container in (
            briefs["channels"][0]["hinges"][0],
        ):
            container["evidenceRefs"] = [
                "finding:42:1:002" if ref == "finding:42:1:001" else ref
                for ref in container["evidenceRefs"]
            ]

        self.assertEqual(layer3_validate.validate_briefs(briefs, packet, hypotheses), [])

        broken = json.loads(json.dumps(briefs))
        broken["channels"][0]["hinges"][0]["evidenceRefs"] = [
            "finding:42:1:001" if ref == "finding:42:1:002" else ref
            for ref in broken["channels"][0]["hinges"][0]["evidenceRefs"]
        ]
        errors = layer3_validate.validate_briefs(broken, packet, hypotheses)
        self.assertTrue(any("exact paired findingRef" in error for error in errors))

    def test_boundary_extraction_keeps_real_table_and_sentence_forms(self) -> None:
        evidence = """\
| Prosedeki ifade | Bundle dayanağı | İzlenebilirlik ve sınır |
| --- | --- | --- |
| Yerel okuma | `x` | Karşı sınır `root_000001/B004`; bu dal proseye taşınmadı. |

Kapsam notu: ordinary coverage.

Bu kapsam satırı taşınmadı kelimesini içerse bile kapsamdır.
"""

        self.assertEqual(
            layer3_build.extract_layer2_boundaries(evidence),
            [
                "| Yerel okuma | `x` | Karşı sınır `root_000001/B004`; bu dal proseye taşınmadı. |"
            ],
        )

    def test_composition_and_finalizer_require_visible_landings(self) -> None:
        packet = self.packet()
        hypotheses = self.hypotheses(packet)
        briefs = self.briefs(packet)
        composition = self.composition(packet, briefs)

        self.assertEqual(layer3_validate.validate_composition(composition, packet, briefs), [])
        out_dir = self.tmp / "published"
        paths = layer3_finalize.write_publication(
            composition=composition,
            packet=packet,
            briefs=briefs,
            out_dir=out_dir,
        )
        for path in paths:
            self.assertTrue(path.exists())

        evidence = json.loads((out_dir / "42.surah-reading.evidence.tr.json").read_text(encoding="utf-8"))
        self.assertEqual(
            layer3_validate.validate_publication_evidence(
                evidence,
                (out_dir / "42.surah-reading.tr.md").read_text(encoding="utf-8"),
                composition,
            ),
            [],
        )

        broken = json.loads(json.dumps(composition))
        broken["evidenceMap"]["hingeLandings"] = []
        errors = layer3_validate.validate_composition(broken, packet, briefs)
        self.assertTrue(any("every admitted hinge" in error for error in errors))

        duplicate_span = json.loads(json.dumps(composition))
        duplicate_span["evidenceMap"]["channelLandings"][0]["gainSpan"] = duplicate_span[
            "evidenceMap"
        ]["channelLandings"][0]["operationSpan"]
        errors = layer3_validate.validate_composition(duplicate_span, packet, briefs)
        self.assertTrue(any("operationSpan and gainSpan must be distinct" in error for error in errors))

        incomplete_refs = json.loads(json.dumps(composition))
        incomplete_refs["evidenceMap"]["hingeLandings"][0]["evidenceRefs"].pop()
        errors = layer3_validate.validate_composition(incomplete_refs, packet, briefs)
        self.assertTrue(any("must include every evidenceRef from the hinge" in error for error in errors))

    def test_custom_source_roots_keep_absolute_paths(self) -> None:
        custom_root = self.tmp / "custom-quran-data"
        source = custom_root / "data" / "text" / "quran.tsv"
        write(source, "42:1|first arabic\n")

        label = layer3_common.portable_path(source, quran_data=custom_root)

        self.assertEqual(label, str(source.resolve()))
        self.assertEqual(layer3_common.resolve_portable_path(label), source.resolve())

    def write_artifact(self, name: str, value: object) -> Path:
        path = self.tmp / name
        write_json(path, value)
        return path


if __name__ == "__main__":
    unittest.main()
