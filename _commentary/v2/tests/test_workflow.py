from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

V2_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = V2_ROOT.parent.parent
sys.path.insert(0, str(V2_ROOT / "scripts"))

import validate  # noqa: E402
import workflow  # noqa: E402


def finding(ayah_ref: str, index: int, disposition: str = "carry") -> dict:
    item = {
        "findingId": f"{ayah_ref}:finding-{index}",
        "disposition": disposition,
        "kind": "context-activation",
        "relation": "shifts-primary",
        "supportLevel": "contextual-inference",
        "localAnchors": [
            {
                "surface_ar": "لفظ",
                "surface_tr": "lafiz",
                "function_tr": "Yerel hareketi kurar.",
                "evidenceRefs": [f"anchor-{index}"],
            }
        ],
        "primaryReading_tr": "Birincil okuma.",
        "readingBefore_tr": "Ilk okuma.",
        "readingAfter_tr": "Etkinlesmis okuma.",
        "proseClaim_tr": f"Bulgu {index}.",
        "readerPayoff_tr": f"Okur kazanimi {index}.",
        "sourceClaimRefs": [f"source-{index}"],
        "evidenceRefs": [f"evidence-{index}"],
        "activationTriggers": [
            {
                "ayahRef": ayah_ref,
                "effect_tr": "Okumayi keskinlestirir.",
                "evidenceRefs": [f"trigger-{index}"],
            }
        ],
        "counterEvidence": [],
        "channelTags": ["test-channel"],
    }
    if disposition == "blocked":
        item["blockingEvidence"] = [f"blocked-{index}"]
    return item


def ledger(surah: int, ayah: int, count: int) -> dict:
    ref = f"{surah}:{ayah}"
    findings = [finding(ref, index) for index in range(1, count + 1)]
    return {
        "schemaVersion": "commentary-v2-layer2-discovery-v1",
        "surah": surah,
        "ayahRef": ref,
        "language": "tr",
        "primaryFloor_tr": "Birincil zemin.",
        "sourceObligations": [
            {
                "sourceRef": item["sourceClaimRefs"][0],
                "disposition": "carry",
                "findingRefs": [item["findingId"]],
            }
            for item in findings
        ],
        "findings": findings,
        "coverageNote_tr": "",
    }


def editorial_plan(
    ledgers: list[dict],
    ledger_paths: list[Path] | None = None,
    pericope_id: str = "test-pericope",
) -> dict:
    surah = ledgers[0]["surah"]
    ayah_refs = [item["ayahRef"] for item in ledgers]
    source_ledgers = []
    for index, item in enumerate(ledgers):
        digest = (
            validate.sha256_path(ledger_paths[index])
            if ledger_paths is not None
            else "0" * 64
        )
        source_ledgers.append({"ayahRef": item["ayahRef"], "sha256": digest})
    ayah_plans = []
    coverage = []
    for item in ledgers:
        refs = [
            finding_item["findingId"]
            for finding_item in item["findings"]
            if finding_item["disposition"] == "carry"
        ]
        placement_id = f"movement-{item['ayahRef'].split(':')[1]}"
        ayah_plans.append(
            {
                "ayahRef": item["ayahRef"],
                "primaryFloor_tr": item["primaryFloor_tr"],
                "governingMovement_tr": "Butun bulgulari tasiyan hareket.",
                "placements": [
                    {
                        "placementId": placement_id,
                        "movementRole": "development",
                        "findingRefs": refs,
                        "synthesisRefs": [],
                        "paragraphPurpose_tr": "Bulgulari birlikte gelistirir.",
                        "localReturn_tr": "Yerel anlama geri doner.",
                    }
                ],
                "standaloneRequirement_tr": "Ayah tek basina anlasilabilir kalir.",
                "layer3HandoffIds": [],
            }
        )
        for finding_item in item["findings"]:
            disposition = (
                "represented"
                if finding_item["disposition"] == "carry"
                else "upstream-blocked"
            )
            row = {
                "findingRef": finding_item["findingId"],
                "sourceAyahRef": item["ayahRef"],
                "disposition": disposition,
            }
            if disposition == "represented":
                row.update(
                    {
                        "ownerAyahRef": item["ayahRef"],
                        "placementId": placement_id,
                    }
                )
            else:
                row["reason_tr"] = "Kesif asamasinda engellendi."
            coverage.append(row)
    return {
        "schemaVersion": "commentary-v2-pericope-editorial-plan-v1",
        "surah": surah,
        "pericopeId": pericope_id,
        "ayahRefs": ayah_refs,
        "sourceLedgers": source_ledgers,
        "ayahPlans": ayah_plans,
        "findingCoverage": coverage,
        "editorialSyntheses": [],
    }


def channel_registry(
    ledgers: list[dict],
    ledger_paths: list[Path],
    pericope_id: str = "test-pericope",
    candidate_id: str = "test-channel",
) -> dict:
    members = []
    for index, item in enumerate(ledgers, 1):
        finding_item = item["findings"][0]
        members.append(
            {
                "memberId": f"member-{index}",
                "findingRef": finding_item["findingId"],
                "ayahRef": item["ayahRef"],
                "localAnchor_tr": finding_item["localAnchors"][0]["surface_tr"],
                "contribution_tr": finding_item["proseClaim_tr"],
                "evidenceRefs": finding_item["evidenceRefs"],
            }
        )
    return {
        "schemaVersion": "commentary-v2-channel-registry-v1",
        "surah": ledgers[0]["surah"],
        "pericopeId": pericope_id,
        "sourceLedgers": [
            {
                "ayahRef": item["ayahRef"],
                "sha256": validate.sha256_path(path),
            }
            for item, path in zip(ledgers, ledger_paths)
        ],
        "channels": [
            {
                "candidateId": candidate_id,
                "name_tr": "Test kanali",
                "invariant_tr": "Iki ayah boyunca ayni hareket gelisir.",
                "reasoningChain_tr": [
                    "Ilk ayah hareketi baslatir.",
                    "Ikinci ayah hareketi donusturur.",
                ],
                "members": members,
                "counterEvidence": [],
                "crossPericopeStatus": "self-contained",
            }
        ],
    }


class UncappedCoverageTests(unittest.TestCase):
    def test_dense_ayah_with_many_findings_is_valid(self) -> None:
        dense = ledger(2, 282, 120)
        self.assertEqual(validate.validate_ledger_data(dense), [])
        plan = editorial_plan([dense])
        self.assertEqual(validate.validate_plan_data(plan, [dense]), [])

    def test_missing_one_dense_finding_fails_coverage(self) -> None:
        dense = ledger(2, 282, 80)
        plan = editorial_plan([dense])
        missing_ref = dense["findings"][-1]["findingId"]
        plan["findingCoverage"] = [
            row for row in plan["findingCoverage"] if row["findingRef"] != missing_ref
        ]
        errors = validate.validate_plan_data(plan, [dense])
        self.assertTrue(any("missing findings" in error for error in errors))

    def test_plan_hashes_bind_exact_ledger_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "2_282.ledger.json"
            dense = ledger(2, 282, 2)
            path.write_text(json.dumps(dense), encoding="utf-8")
            plan = editorial_plan([dense])
            errors = validate.validate_plan_data(plan, [dense], [path])
            self.assertTrue(any("hashes do not match" in error for error in errors))

    def test_schemas_define_no_array_caps(self) -> None:
        def walk(value):
            if isinstance(value, dict):
                self.assertNotIn("maxItems", value)
                for child in value.values():
                    walk(child)
            elif isinstance(value, list):
                for child in value:
                    walk(child)

        for path in (V2_ROOT / "shared" / "schemas").glob("*.json"):
            walk(json.loads(path.read_text(encoding="utf-8")))


class ReconciliationTests(unittest.TestCase):
    def test_reconciliation_accounts_for_every_pericope_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            ledgers = [ledger(100, ayah, 1) for ayah in (1, 2, 3, 4)]
            ledger_paths = []
            for ayah, item in zip((1, 2, 3, 4), ledgers):
                path = directory / f"100_{ayah}.ledger.json"
                path.write_text(json.dumps(item), encoding="utf-8")
                ledger_paths.append(path)
            first = channel_registry(
                ledgers[:2],
                ledger_paths[:2],
                pericope_id="first",
                candidate_id="motion-trace",
            )
            second = channel_registry(
                ledgers[2:],
                ledger_paths[2:],
                pericope_id="second",
                candidate_id="hidden-trace",
            )
            first_path = directory / "first.channel-registry.json"
            second_path = directory / "second.channel-registry.json"
            first_path.write_text(json.dumps(first), encoding="utf-8")
            second_path.write_text(json.dumps(second), encoding="utf-8")

            result_registry = {
                "schemaVersion": "commentary-v2-channel-registry-v1",
                "surah": 100,
                "pericopeId": "whole-surah",
                "sourceLedgers": first["sourceLedgers"] + second["sourceLedgers"],
                "channels": [
                    {
                        "candidateId": "surah-trace",
                        "name_tr": "Surah izi",
                        "invariant_tr": "Hareket iz birakir.",
                        "reasoningChain_tr": ["Ilk iz.", "Ikinci iz."],
                        "members": (
                            first["channels"][0]["members"]
                            + second["channels"][0]["members"]
                        ),
                        "counterEvidence": [],
                        "crossPericopeStatus": "self-contained",
                    }
                ],
            }
            reconciliation = {
                "schemaVersion": "commentary-v2-registry-reconciliation-v1",
                "surah": 100,
                "sourceRegistries": [
                    {
                        "pericopeId": "first",
                        "sha256": validate.sha256_path(first_path),
                    },
                    {
                        "pericopeId": "second",
                        "sha256": validate.sha256_path(second_path),
                    },
                ],
                "candidateCoverage": [
                    {
                        "sourcePericopeId": "first",
                        "sourceCandidateId": "motion-trace",
                        "disposition": "merged",
                        "resultCandidateIds": ["surah-trace"],
                        "reason_tr": "Ayni iz mekanizmasi.",
                    },
                    {
                        "sourcePericopeId": "second",
                        "sourceCandidateId": "hidden-trace",
                        "disposition": "merged",
                        "resultCandidateIds": ["surah-trace"],
                        "reason_tr": "Ayni iz mekanizmasi.",
                    },
                ],
            }
            errors = validate.validate_reconciliation_data(
                reconciliation,
                [(first_path, first), (second_path, second)],
                result_registry,
            )
            self.assertEqual(errors, [])


class InstantiationTests(unittest.TestCase):
    def config(self, output_root: Path) -> dict:
        return {
            "schemaVersion": "commentary-v2-run-v1",
            "runId": "test-run",
            "surah": 100,
            "language": "tr",
            "outputRoot": str(output_root),
            "ayahSources": {
                "100:1": ["bundles/s100/100_1.ayah.json"],
                "100:2": ["bundles/s100/100_2.ayah.json"],
            },
            "pericopes": [{"id": "test-pericope", "ayahs": [1, 2]}],
        }

    def test_discovery_and_compiler_are_hermetic_and_ledger_first(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = self.config(root)
            written = workflow.instantiate_discovery(
                config, selected_ayah=1, run_date="2026-07-29"
            )
            prompt = written[0].read_text(encoding="utf-8")
            self.assertIn("Hermeticity rule", prompt)
            self.assertIn("layer2-discovery-ledger.schema.json", prompt)

            _, discovery_outputs = workflow.stage_paths(root, "discovery")
            discovery_outputs.mkdir(parents=True)
            ledgers = [ledger(100, 1, 3), ledger(100, 2, 4)]
            for ayah, item in zip((1, 2), ledgers):
                (discovery_outputs / f"100_{ayah}.ledger.json").write_text(
                    json.dumps(item, ensure_ascii=False), encoding="utf-8"
                )

            written = workflow.instantiate_compiler(
                config,
                pericope_id="test-pericope",
                run_date="2026-07-29",
                include_memos=False,
            )
            compiler_prompt = written[0].read_text(encoding="utf-8")
            self.assertIn('"findingId":"100:1:finding-1"', compiler_prompt)
            self.assertNotIn("discovery-memo", compiler_prompt)

    def test_layer2_author_gets_only_its_ledger_and_plan_slice(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = self.config(root)
            _, discovery_outputs = workflow.stage_paths(root, "discovery")
            discovery_outputs.mkdir(parents=True)
            ledger_paths = []
            ledgers = [ledger(100, 1, 2), ledger(100, 2, 2)]
            for ayah, item in zip((1, 2), ledgers):
                path = discovery_outputs / f"100_{ayah}.ledger.json"
                path.write_text(json.dumps(item, ensure_ascii=False), encoding="utf-8")
                ledger_paths.append(path)

            _, compiler_outputs = workflow.stage_paths(root, "compiler")
            compiler_outputs.mkdir(parents=True)
            plan = editorial_plan(ledgers, ledger_paths)
            plan_path = compiler_outputs / "test-pericope.editorial-plan.json"
            plan_path.write_text(json.dumps(plan, ensure_ascii=False), encoding="utf-8")

            written = workflow.instantiate_layer2(
                config,
                pericope_id="test-pericope",
                selected_ayah=1,
                run_date="2026-07-29",
            )
            manifest = json.loads(written[1].read_text(encoding="utf-8"))
            kinds = [item["kind"] for item in manifest["sources"]]
            self.assertEqual(kinds.count("discovery-ledger"), 1)
            self.assertEqual(kinds.count("editorial-plan-slice"), 1)
            self.assertNotIn("channel-registry", kinds)

    def test_layer3_uses_registry_without_layer2_prose_by_default(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = self.config(root)
            _, discovery_outputs = workflow.stage_paths(root, "discovery")
            discovery_outputs.mkdir(parents=True)
            ledger_paths = []
            ledgers = [ledger(100, 1, 2), ledger(100, 2, 2)]
            for ayah, item in zip((1, 2), ledgers):
                path = discovery_outputs / f"100_{ayah}.ledger.json"
                path.write_text(json.dumps(item, ensure_ascii=False), encoding="utf-8")
                ledger_paths.append(path)

            _, compiler_outputs = workflow.stage_paths(root, "compiler")
            compiler_outputs.mkdir(parents=True)
            plan = editorial_plan(ledgers, ledger_paths)
            (compiler_outputs / "test-pericope.editorial-plan.json").write_text(
                json.dumps(plan, ensure_ascii=False), encoding="utf-8"
            )
            registry = channel_registry(ledgers, ledger_paths)
            (compiler_outputs / "test-pericope.channel-registry.json").write_text(
                json.dumps(registry, ensure_ascii=False), encoding="utf-8"
            )

            written = workflow.instantiate_layer3(
                config,
                pericope_id="test-pericope",
                run_date="2026-07-29",
                include_layer2_prose=False,
            )
            manifest = json.loads(written[1].read_text(encoding="utf-8"))
            kinds = [item["kind"] for item in manifest["sources"]]
            self.assertEqual(kinds.count("channel-registry"), 1)
            self.assertNotIn("layer2-edited-prose", kinds)

    def test_multi_pericope_reconciliation_and_surah_layer3(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = {
                "schemaVersion": "commentary-v2-run-v1",
                "runId": "multi-run",
                "surah": 100,
                "language": "tr",
                "outputRoot": str(root),
                "ayahSources": {
                    f"100:{ayah}": [f"bundles/s100/100_{ayah}.ayah.json"]
                    for ayah in (1, 2, 3, 4)
                },
                "pericopes": [
                    {"id": "first", "ayahs": [1, 2]},
                    {"id": "second", "ayahs": [3, 4]},
                ],
            }
            _, discovery_outputs = workflow.stage_paths(root, "discovery")
            discovery_outputs.mkdir(parents=True)
            ledgers = [ledger(100, ayah, 1) for ayah in (1, 2, 3, 4)]
            ledger_paths = []
            for ayah, item in zip((1, 2, 3, 4), ledgers):
                path = discovery_outputs / f"100_{ayah}.ledger.json"
                path.write_text(json.dumps(item), encoding="utf-8")
                ledger_paths.append(path)

            _, compiler_outputs = workflow.stage_paths(root, "compiler")
            compiler_outputs.mkdir(parents=True)
            registries = []
            for pericope_id, subset, paths in (
                ("first", ledgers[:2], ledger_paths[:2]),
                ("second", ledgers[2:], ledger_paths[2:]),
            ):
                plan = editorial_plan(subset, paths, pericope_id)
                (compiler_outputs / f"{pericope_id}.editorial-plan.json").write_text(
                    json.dumps(plan), encoding="utf-8"
                )
                registry = channel_registry(
                    subset,
                    paths,
                    pericope_id,
                    f"{pericope_id}-channel",
                )
                (
                    compiler_outputs / f"{pericope_id}.channel-registry.json"
                ).write_text(json.dumps(registry), encoding="utf-8")
                registries.append(registry)

            written = workflow.instantiate_reconciler(
                config, run_date="2026-07-29"
            )
            manifest = json.loads(written[1].read_text(encoding="utf-8"))
            self.assertEqual(
                [item["kind"] for item in manifest["sources"]].count(
                    "channel-registry"
                ),
                2,
            )

            _, reconciler_outputs = workflow.stage_paths(root, "reconciler")
            reconciler_outputs.mkdir(parents=True, exist_ok=True)
            reconciled_members = []
            for index, member in enumerate(
                registries[0]["channels"][0]["members"]
                + registries[1]["channels"][0]["members"],
                1,
            ):
                reconciled_members.append(
                    {**member, "memberId": f"whole-member-{index}"}
                )
            reconciled = {
                "schemaVersion": "commentary-v2-channel-registry-v1",
                "surah": 100,
                "pericopeId": "whole-surah",
                "sourceLedgers": (
                    registries[0]["sourceLedgers"]
                    + registries[1]["sourceLedgers"]
                ),
                "channels": [
                    {
                        "candidateId": "whole-channel",
                        "name_tr": "Butun kanal",
                        "invariant_tr": "Butun ayahlarda iz surer.",
                        "reasoningChain_tr": ["Ilk pericope.", "Ikinci pericope."],
                        "members": reconciled_members,
                        "counterEvidence": [],
                        "crossPericopeStatus": "self-contained",
                    }
                ],
            }
            reconciled_path = (
                reconciler_outputs / "whole-surah.channel-registry.json"
            )
            reconciled_path.write_text(json.dumps(reconciled), encoding="utf-8")
            written = workflow.instantiate_layer3_surah(
                config,
                run_date="2026-07-29",
                include_layer2_prose=False,
            )
            manifest = json.loads(written[1].read_text(encoding="utf-8"))
            self.assertEqual(manifest["unit"], "whole-surah")


if __name__ == "__main__":
    unittest.main()
