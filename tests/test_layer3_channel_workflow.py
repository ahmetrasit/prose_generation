from __future__ import annotations

import importlib
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "_channel" / "layer3" / "scripts"
LAYER3_MODULE_NAMES = ("common", "validate", "build_packet", "finalize", "instantiate")
saved_modules = {
    name: sys.modules.pop(name)
    for name in LAYER3_MODULE_NAMES
    if name in sys.modules
}
sys.path.insert(0, str(SCRIPTS))
try:
    layer3_common = importlib.import_module("common")
    layer3_validate = importlib.import_module("validate")
    layer3_build = importlib.import_module("build_packet")
    layer3_finalize = importlib.import_module("finalize")
    layer3_instantiate = importlib.import_module("instantiate")
finally:
    sys.path.remove(str(SCRIPTS))
    for module_name in LAYER3_MODULE_NAMES:
        sys.modules.pop(module_name, None)
    sys.modules.update(saved_modules)


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
        write(
            self.quran_data
            / "data"
            / "analysis"
            / "channels"
            / "network-v3"
            / "s042"
            / "review"
            / "reader_a_pilot.md",
            "### 1. Test system\n\n"
            "#### Subchannel A. Linked motion\n\n"
            "- Ayah anchors: 42:1 first signal; 42:2 second signal\n"
            "- Active motifs: `test:B001/m01`; `test:B002/m01`\n",
        )
        self.write_layer2_set(1, "a", "supports-primary")
        self.write_layer2_set(2, "b", "shifts-primary")

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp)

    def write_layer2_set(self, ayah: int, key: str, relation: str) -> None:
        write(
            self.layer2 / f"42_{ayah}.prose.editorial.test.md",
            f"reader-facing editorial prose {ayah}\n",
        )
        write(
            self.layer2 / f"42_{ayah}.evidence.editorial.test.md",
            "## Preserved rejected readings\n\n"
            f"- Boundary for ayah {ayah}.\n\n"
            "## Coverage note\n\n"
            "ok\n",
        )
        write(
            self.layer2 / f"42_{ayah}.index.editorial.test.md",
            f"- `surprise:local-{key}` - local resonance {key} [{relation}] [inference]\n",
        )
        write(
            self.layer2 / f"42_{ayah}.friction.editorial.test.md",
            "No friction.\n",
        )

    def packet(self) -> dict[str, object]:
        return layer3_build.build_packet(
            surah=42,
            language="tr",
            layer2_dir=self.layer2,
            layer2_label="editorial.test",
            quran_data=self.quran_data,
            latent_activation=self.latent,
            primary_floor_path=self.tmp / "floor.json",
        )

    def hypotheses(self, packet: dict[str, object]) -> dict[str, object]:
        return {
            "schemaVersion": "layer3-discovery-hypotheses-v3",
            "packetId": packet["packetId"],
            "sourceSetHash": packet["sourceSetHash"],
            "surah": 42,
            "language": "tr",
            "hypotheses": [
                {
                    "hypothesisId": "cross-care",
                    "readerName": "tasiyan bakim",
                    "imageSystem": "iki hareketi birbirine tasiyan bir bakim duzeni",
                    "systemBoundary": "yalniz ayni hareketi tasiyan iki somut katki dahildir",
                    "proposedOperation": "iki hareket birbirini okutur",
                    "readerShift": {
                        "before": "iki ayet ayridir",
                        "hinge": "yerel rezonanslar birlikte calisir",
                        "after": "iki ayet tek bir hareket gibi gorunur",
                    },
                    "memberSignals": [
                        {
                            "ayahRef": "42:1",
                            "concreteContribution": "ilk hareket tasinir",
                            "activationCardRefs": ["activation:network-p01-a"],
                        },
                        {
                            "ayahRef": "42:2",
                            "concreteContribution": "ikinci hareket karsilar",
                            "activationCardRefs": ["activation:network-p01-a"],
                        },
                    ],
                    "activationCardRefs": ["activation:network-p01-a"],
                }
            ],
            "activationCardCoverage": [
                {
                    "activationRef": "activation:network-p01-a",
                    "hypothesisIds": ["cross-care"],
                    "searchNote": "iki ayette ayni tasima sistemi sinandi",
                }
            ],
        }

    def briefs(self, packet: dict[str, object]) -> dict[str, object]:
        return {
            "schemaVersion": "layer3-channel-briefs-v3",
            "briefId": f"{packet['runId']}-briefs-v3",
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
                    "imageSystem": "iki hareketi tasiyan ortak bakim duzeni",
                    "systemBoundary": "ayni tasima hareketine katilmayan genel bakim konulari disarida kalir",
                    "inputRefs": [
                        "hypothesis:cross-care",
                        "resonance:42:1:local-a",
                        "resonance:42:2:local-b",
                    ],
                    "surfaceFloorRefs": ["primary-floor#42:1", "primary-floor#42:2"],
                    "surfaceFloor": "ilk ve ikinci zemin ayakta kalir",
                    "memberLandings": [
                        {
                            "memberId": "care-first",
                            "ayahRef": "42:1",
                            "concreteContribution": "ilk hareket bakimla tasinir",
                            "inputRefs": [
                                "hypothesis:cross-care",
                                "resonance:42:1:local-a",
                            ],
                            "evidenceRefs": [
                                "finding:42:1:001",
                                "resonance:42:1:local-a",
                                "activation:network-p01-a",
                            ],
                            "primaryRelation": "supports-primary",
                        },
                        {
                            "memberId": "care-second",
                            "ayahRef": "42:2",
                            "concreteContribution": "ikinci hareket bakimi ileri tasir",
                            "inputRefs": ["resonance:42:2:local-b"],
                            "evidenceRefs": [
                                "finding:42:2:001",
                                "resonance:42:2:local-b",
                            ],
                            "primaryRelation": "shifts-primary",
                        },
                    ],
                    "hinges": [
                        {
                            "hingeId": "care-hinge",
                            "imageMovement": "ilk tasima ikinci harekette devam eder",
                            "contribution": "yerel rezonanslar iki ayeti baglar",
                            "inputRefs": [
                                "hypothesis:cross-care",
                                "resonance:42:1:local-a",
                                "resonance:42:2:local-b",
                            ],
                            "memberIds": ["care-first", "care-second"],
                            "ayahRefs": ["42:1", "42:2"],
                            "evidenceRefs": [
                                "finding:42:1:001",
                                "resonance:42:1:local-a",
                                "finding:42:2:001",
                                "resonance:42:2:local-b",
                                "activation:network-p01-a",
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
                    "preludePromise": "iki harekette tasinan bakimi fark etmeye hazirlar",
                    "postludePayoff": "bakimin iki ayeti tek isleyen sistem yaptigini tamamlar",
                }
            ],
            "nonChannelDispositions": [],
        }

    def composition(
        self,
        packet: dict[str, object],
        briefs: dict[str, object],
        *,
        phase: str = "editorial",
    ) -> dict[str, object]:
        draft_id = f"{packet['runId']}-composition-draft-v2"
        return {
            "schemaVersion": "layer3-surah-composition-v2",
            "compositionId": (
                draft_id
                if phase == "draft"
                else f"{packet['runId']}-composition-v2"
            ),
            "phase": phase,
            "revisionOf": None if phase == "draft" else draft_id,
            "packetId": packet["packetId"],
            "briefId": briefs["briefId"],
            "sourceSetHash": packet["sourceSetHash"],
            "surah": 42,
            "language": "tr",
            "prelude": (
                "Iki ayet birlikte ilerler. "
                "Bakim, iki hareket arasinda tasinan somut bir duzen olarak gorunebilir."
            ),
            "postlude": (
                "Ilk zemin ile ikinci zemin birlikte okunur. "
                "Ilk ayette bakim ilk hareketi tasir. "
                "Ikinci ayette ayni bakim hareketi ileri goturur. "
                "Iki somut hareket birbirine baglaninca bakim iki ayeti karsilikli okutur; "
                "okuyucu daginik satirlar yerine tek bir isleyen sistem gorur."
            ),
            "evidenceMap": {
                "primaryGroundings": [
                    {
                        "surface": "prelude",
                        "span": "Iki ayet birlikte ilerler.",
                        "sourceRefs": ["primary-floor#42:1", "primary-floor#42:2"],
                    },
                    {
                        "surface": "postlude",
                        "span": "Ilk zemin ile ikinci zemin birlikte okunur.",
                        "sourceRefs": ["primary-floor#42:1", "primary-floor#42:2"],
                    }
                ],
                "preludeChannelPromises": [
                    {
                        "channelId": "care-channel",
                        "span": "Bakim, iki hareket arasinda tasinan somut bir duzen olarak gorunebilir.",
                        "evidenceRefs": [
                            "finding:42:1:001",
                            "resonance:42:1:local-a",
                            "activation:network-p01-a",
                        ],
                    }
                ],
                "postludeChannelLandings": [
                    {
                        "channelId": "care-channel",
                        "operationSpan": "bakim iki ayeti karsilikli okutur",
                        "gainSpan": "okuyucu daginik satirlar yerine tek bir isleyen sistem gorur",
                        "evidenceRefs": [
                            "finding:42:1:001",
                            "resonance:42:1:local-a",
                            "finding:42:2:001",
                            "resonance:42:2:local-b",
                            "activation:network-p01-a",
                        ],
                    }
                ],
                "postludeMemberLandings": [
                    {
                        "memberId": "care-first",
                        "span": "Ilk ayette bakim ilk hareketi tasir.",
                        "evidenceRefs": [
                            "finding:42:1:001",
                            "resonance:42:1:local-a",
                            "activation:network-p01-a",
                        ],
                    },
                    {
                        "memberId": "care-second",
                        "span": "Ikinci ayette ayni bakim hareketi ileri goturur.",
                        "evidenceRefs": [
                            "finding:42:2:001",
                            "resonance:42:2:local-b",
                        ],
                    },
                ],
                "postludeHingeLandings": [
                    {
                        "hingeId": "care-hinge",
                        "span": "Iki somut hareket birbirine baglaninca",
                        "evidenceRefs": [
                            "finding:42:1:001",
                            "resonance:42:1:local-a",
                            "finding:42:2:001",
                            "resonance:42:2:local-b",
                            "activation:network-p01-a",
                        ],
                    }
                ],
            },
            "friction": [],
        }

    def test_packet_requires_complete_layer2_handoff(self) -> None:
        (self.layer2 / "42_2.friction.editorial.test.md").unlink()

        with self.assertRaises(SystemExit) as caught:
            self.packet()

        self.assertIn("no complete Layer-2", str(caught.exception))

    def test_packet_rejects_malformed_surprise_rows(self) -> None:
        write(
            self.layer2 / "42_1.index.editorial.test.md",
            "- `surprise:local-a` - missing relation [inference]\n",
        )

        with self.assertRaises(SystemExit) as caught:
            self.packet()

        self.assertIn("must carry exactly one", str(caught.exception))

    def test_packet_accepts_grounded_surprise_rows(self) -> None:
        write(
            self.layer2 / "42_1.index.editorial.test.md",
            "- `delta-grounded` - grounded finding [supports-primary]\n"
            "- `surprise:local-a` - grounded local resonance [supports-primary]\n",
        )

        packet = self.packet()
        ayah = packet["layer2Handoff"]["ayahs"][0]

        self.assertEqual(ayah["findings"][0]["primaryRelation"], "supports-primary")
        self.assertFalse(ayah["findings"][1]["inference"])
        self.assertEqual(
            ayah["localResonances"][0]["resonanceRef"],
            "resonance:42:1:local-a",
        )

    def test_packet_rejects_non_editorial_layer2_sets(self) -> None:
        for ayah in (1, 2):
            for kind in ("prose", "evidence", "index", "friction"):
                shutil.copyfile(
                    self.layer2 / f"42_{ayah}.{kind}.editorial.test.md",
                    self.layer2 / f"42_{ayah}.{kind}.test.md",
                )

        with self.assertRaises(SystemExit) as caught:
            layer3_build.build_packet(
                surah=42,
                language="tr",
                layer2_dir=self.layer2,
                layer2_label="test",
                quran_data=self.quran_data,
                latent_activation=self.latent,
                primary_floor_path=self.tmp / "floor.json",
            )

        self.assertIn("requires the reader-facing editorial", str(caught.exception))

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

        self.assertIn("layer3-discovery-input-v3", prompt)
        self.assertIn("ilk zemin", prompt)
        self.assertNotIn("local resonance a", prompt)
        self.assertNotIn("Boundary for ayah", prompt)
        self.assertNotIn("reader-facing editorial prose 1", prompt)

    def test_discovery_requires_exact_activation_card_coverage(self) -> None:
        packet = self.packet()
        hypotheses = self.hypotheses(packet)
        hypotheses["activationCardCoverage"] = []

        errors = layer3_validate.validate_hypotheses(hypotheses, packet)

        self.assertTrue(any("account exactly once" in error for error in errors))

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
        listed_only["channels"][0]["memberLandings"][1]["inputRefs"] = [
            "hypothesis:cross-care"
        ]
        errors = layer3_validate.validate_briefs(listed_only, packet, hypotheses)
        self.assertTrue(any("every channel inputRef" in error for error in errors))

    def test_briefs_require_hypothesis_activation_refs(self) -> None:
        packet = self.packet()
        hypotheses = self.hypotheses(packet)
        briefs = self.briefs(packet)

        for container in (
            briefs["channels"][0]["memberLandings"][0],
            briefs["channels"][0]["hinges"][0],
        ):
            container["evidenceRefs"] = [
                ref
                for ref in container["evidenceRefs"]
                if ref != "activation:network-p01-a"
            ]

        errors = layer3_validate.validate_briefs(briefs, packet, hypotheses)

        self.assertTrue(
            any("activationCardRefs in evidenceRefs" in error for error in errors)
        )

    def test_briefs_require_exact_resonance_finding_pairs(self) -> None:
        write(
            self.layer2 / "42_1.index.editorial.test.md",
            "- `42:1:ordinary` - ordinary finding\n"
            "- `surprise:local-a` - local resonance a [supports-primary] [inference]\n",
        )
        packet = self.packet()
        hypotheses = self.hypotheses(packet)
        briefs = self.briefs(packet)
        for container in (
            briefs["channels"][0]["memberLandings"][0],
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

    def test_compose_projects_only_admitted_member_prose_and_edit_reuses_draft(self) -> None:
        packet = self.packet()
        hypotheses = self.hypotheses(packet)
        briefs = self.briefs(packet)
        packet_path = self.write_artifact("packet.json", packet)
        hypotheses_path = self.write_artifact("hypotheses.json", hypotheses)
        briefs_path = self.write_artifact("briefs.json", briefs)

        compose_prompt = layer3_instantiate.assemble(
            stage="compose",
            surah=42,
            packet_path=packet_path,
            hypotheses_path=hypotheses_path,
            briefs_path=briefs_path,
        )
        self.assertIn("reader-facing editorial prose 1", compose_prompt)
        self.assertIn("reader-facing editorial prose 2", compose_prompt)
        self.assertIn("surah-composition.draft.tr.json", compose_prompt)

        draft = self.composition(packet, briefs, phase="draft")
        edit_prompt = layer3_instantiate.assemble(
            stage="edit",
            surah=42,
            packet_path=packet_path,
            hypotheses_path=hypotheses_path,
            briefs_path=briefs_path,
            draft_path=self.write_artifact("draft.json", draft),
        )
        self.assertIn("layer3-surah-composition-v2", edit_prompt)
        self.assertIn(draft["compositionId"], edit_prompt)

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
                (out_dir / "42.surah-reading.prelude.tr.md").read_text(encoding="utf-8"),
                (out_dir / "42.surah-reading.postlude.tr.md").read_text(encoding="utf-8"),
                composition,
            ),
            [],
        )

        broken = json.loads(json.dumps(composition))
        broken["evidenceMap"]["postludeHingeLandings"] = []
        errors = layer3_validate.validate_composition(broken, packet, briefs)
        self.assertTrue(any("every admitted hinge" in error for error in errors))

        duplicate_span = json.loads(json.dumps(composition))
        duplicate_span["evidenceMap"]["postludeChannelLandings"][0]["gainSpan"] = duplicate_span[
            "evidenceMap"
        ]["postludeChannelLandings"][0]["operationSpan"]
        errors = layer3_validate.validate_composition(duplicate_span, packet, briefs)
        self.assertTrue(any("operationSpan and gainSpan must be distinct" in error for error in errors))

        incomplete_refs = json.loads(json.dumps(composition))
        incomplete_refs["evidenceMap"]["postludeHingeLandings"][0]["evidenceRefs"].pop()
        errors = layer3_validate.validate_composition(incomplete_refs, packet, briefs)
        self.assertTrue(any("must include every hinge evidenceRef" in error for error in errors))

        wrong_phase = self.composition(packet, briefs, phase="draft")
        errors = layer3_validate.validate_composition(
            wrong_phase,
            packet,
            briefs,
            required_phase="editorial",
        )
        self.assertTrue(any("expected 'editorial'" in error for error in errors))
        with self.assertRaises(SystemExit):
            layer3_finalize.write_publication(
                composition=wrong_phase,
                packet=packet,
                briefs=briefs,
                out_dir=self.tmp / "draft-published",
            )

    def test_composition_rejects_reused_evidence_spans(self) -> None:
        packet = self.packet()
        briefs = self.briefs(packet)
        composition = self.composition(packet, briefs)
        composition["evidenceMap"]["preludeChannelPromises"][0]["span"] = (
            "Iki ayet birlikte ilerler."
        )

        errors = layer3_validate.validate_composition(composition, packet, briefs)

        self.assertTrue(
            any("prelude evidence spans: duplicate value" in error for error in errors)
        )

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
