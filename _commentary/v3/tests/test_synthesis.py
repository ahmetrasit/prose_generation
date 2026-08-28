from __future__ import annotations

import copy
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


V3_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(V3_ROOT))

import v3lib.adjudication as adjudication_module  # noqa: E402
import v3lib.synthesis as synthesis_module  # noqa: E402
from tests.test_adjudication import (  # noqa: E402
    fixture_bundle_for_docket,
    fixture_docket,
    response_for_docket,
)
from v3lib.adjudication import (  # noqa: E402
    AdjudicationOptions,
    _render_adjudication_prompt_unbound as render_adjudication_prompt,
    _validate_adjudication_response_unbound as validate_adjudication_response,
    validate_adjudication_for_ayah,
)
from v3lib.common import (  # noqa: E402
    BudgetError,
    ValidationError,
    canonical_json_bytes,
    canonical_sha256,
    pretty_json_bytes,
    write_bytes_confined,
    write_json_confined,
)
from v3lib.prepare import PrepareOptions, build_prepared_artifacts  # noqa: E402
from v3lib.synthesis import (  # noqa: E402
    RESPONSE_SCHEMA,
    SynthesisOptions,
    _build_synthesis_packet_unbound,
    _render_synthesis_prompt_unbound,
    _validate_synthesis_artifact_unbound,
    _validate_synthesis_response_unbound,
    load_adjudication_for_ayah,
    _render_markdown_outputs_unbound as render_markdown_outputs,
    render_synthesis_prompt as render_source_bound_synthesis_prompt,
    validate_synthesis_artifact as validate_source_bound_synthesis_artifact,
    validate_synthesis_for_ayah,
    _validate_synthesis_packet_unbound,
    validate_synthesis_response as validate_source_bound_synthesis_response,
    verify_final_outputs_for_ayah,
)


DEFAULT_SYNTHESIS_OPTIONS = SynthesisOptions()


def _fixture_options(
    packet: dict, options: SynthesisOptions | None
) -> SynthesisOptions:
    return options or SynthesisOptions(**packet["limits"])


def build_synthesis_packet(
    docket: dict,
    adjudication: dict,
    *,
    options: SynthesisOptions | None = None,
    **kwargs,
) -> dict:
    return _build_synthesis_packet_unbound(
        docket,
        adjudication,
        options=options or DEFAULT_SYNTHESIS_OPTIONS,
        **kwargs,
    )


def render_synthesis_prompt(
    packet: dict,
    *,
    options: SynthesisOptions | None = None,
    **kwargs,
):
    return _render_synthesis_prompt_unbound(
        packet,
        options=_fixture_options(packet, options),
        **kwargs,
    )


def validate_synthesis_packet(
    packet: dict,
    docket: dict,
    adjudication: dict,
    *,
    options: SynthesisOptions | None = None,
    **kwargs,
) -> None:
    _validate_synthesis_packet_unbound(
        packet,
        docket,
        adjudication,
        options=_fixture_options(packet, options),
        **kwargs,
    )


def validate_synthesis_response(
    response: dict,
    packet: dict,
    docket: dict,
    adjudication: dict,
    *,
    options: SynthesisOptions | None = None,
    **kwargs,
):
    return _validate_synthesis_response_unbound(
        response,
        packet,
        docket,
        adjudication,
        options=_fixture_options(packet, options),
        **kwargs,
    )


def validate_synthesis_artifact(
    artifact: dict,
    packet: dict,
    docket: dict,
    adjudication: dict,
    *,
    options: SynthesisOptions | None = None,
    **kwargs,
) -> None:
    _validate_synthesis_artifact_unbound(
        artifact,
        packet,
        docket,
        adjudication,
        options=_fixture_options(packet, options),
        **kwargs,
    )


REAL_S29_FILES = [
    V3_ROOT / "inputs/source/s029/29_38.bundle.json",
    V3_ROOT / "inputs/prepared/s029/29_38.prepared.json",
    V3_ROOT / "inputs/adjudication/s029/29_38.docket.json",
    V3_ROOT / "outputs/adjudication/s029/29_38.response.json",
    V3_ROOT / "outputs/synthesis/s029/29_38.response.json",
    V3_ROOT / "outputs/synthesis/s029/29_38.synthesis.json",
]


def packet_fixture(*, include_new: bool = True) -> tuple[dict, dict, dict]:
    docket = fixture_docket()
    adjudication = validate_adjudication_response(
        response_for_docket(docket, include_new=include_new), docket
    )
    packet = build_synthesis_packet(docket, adjudication)
    return docket, adjudication, packet


def response_for_packet(packet: dict) -> dict:
    paragraphs = []
    findings = []
    for index, selection in enumerate(packet["selections"], start=1):
        paragraph_key = f"p{index:02d}"
        finding_key = f"reading_{index:02d}"
        landing = selection["claim"]
        containment = "Bu yanki kelimenin yerel anlaminin yerine gecmez."
        text = (
            f"{landing} Secilen delil, soz dizimi ile okuyucu getirisini ayni "
            "hareket icinde bulusturur; once temel hukmu belirler, sonra bu hukmun "
            "hangi ayrinti sayesinde daha keskin duyuldugunu gosterir. Okur, "
            "kelimelerin yalniz sonuc bildirmedigini, sonuca goturen algi ve "
            "degerlendirme duzenini de tasidigini fark eder. Bu aciklama ayetin "
            "kendi yuzeyine bagli kalir ve komsu malzemeyi ancak yerel bag kurulmus "
            f"oldugunda kullanir. {containment} Boylece yorum, duz anlami korurken "
            "okunabilir bir ek basinc ve somut bir dusunce hareketi kazandirir."
        )
        direct = (
            selection["origin"] == "docket"
            and selection["source_type"] == "word_analysis"
        )
        exploratory = selection.get("confidence") == "exploratory"
        status = "bundle_traceable" if direct else (
            "exploratory" if exploratory else "inference"
        )
        paragraphs.append(
            {
                "paragraph_key": paragraph_key,
                "text": text,
                "finding_keys": [finding_key],
            }
        )
        findings.append(
            {
                "finding_key": finding_key,
                "title": f"Yerel okuma {index}",
                "summary": selection["claim"],
                "effect": "baseline" if direct else "shifts_primary",
                "epistemic_status": status,
                "candidate_ids": [selection["candidate_id"]],
                "support_ids": [selection["support_ids"][0]],
                "branch_refs": list(selection["branch_refs"]),
                "paragraph_key": paragraph_key,
                "landing_quote": landing,
                "containment_quote": None if direct else containment,
            }
        )
    _prompt, manifest = render_synthesis_prompt(packet)
    return {
        "schema_version": RESPONSE_SCHEMA,
        "identity": copy.deepcopy(manifest["identity"]),
        "paragraphs": paragraphs,
        "findings": findings,
        "friction_notes": [],
    }


class SynthesisTests(unittest.TestCase):
    def test_unbound_handoff_helpers_are_private(self) -> None:
        self.assertFalse(hasattr(synthesis_module, "build_synthesis_packet"))
        self.assertFalse(hasattr(synthesis_module, "validate_synthesis_packet"))
        self.assertFalse(hasattr(synthesis_module, "render_markdown_outputs"))
        self.assertFalse(
            hasattr(adjudication_module, "validate_adjudication_artifact")
        )

    def test_public_synthesis_apis_require_caller_bound_policy(self) -> None:
        docket, adjudication, packet = packet_fixture()
        response = response_for_packet(packet)
        artifact, _outputs = validate_synthesis_response(
            response, packet, docket, adjudication
        )
        calls = (
            lambda: _build_synthesis_packet_unbound(docket, adjudication),
            lambda: _validate_synthesis_packet_unbound(
                packet, docket, adjudication
            ),
            lambda: render_source_bound_synthesis_prompt(packet),
            lambda: validate_source_bound_synthesis_response(
                response, packet, docket, adjudication
            ),
            lambda: validate_source_bound_synthesis_artifact(
                artifact, packet, docket, adjudication
            ),
        )
        for call in calls:
            with self.subTest(call=call), self.assertRaisesRegex(
                ValidationError, "Caller-bound SynthesisOptions"
            ):
                call()

    def test_malformed_model_discriminators_raise_validation_errors(self) -> None:
        docket, adjudication, packet = packet_fixture()
        for field, value in (
            ("paragraph_key", []),
            ("effect", {}),
            ("epistemic_status", []),
        ):
            with self.subTest(field=field):
                response = response_for_packet(packet)
                response["findings"][0][field] = value
                with self.assertRaises(ValidationError):
                    validate_synthesis_response(
                        response, packet, docket, adjudication
                    )

    def test_selected_only_packet_is_deterministic_and_compact(self) -> None:
        bundle = fixture_bundle_for_docket()
        duplicate_word = copy.deepcopy(bundle["word_analysis"]["words"][1])
        duplicate_word["prose"] = "Ikinci bagimsiz yol-koku odak delili."
        duplicate_word["topics"][0]["topic_id"] = "29:38:2:review-only-grounding"
        bundle["word_analysis"]["words"].append(duplicate_word)
        bundle["word_morpheme_spans"].append(None)
        _prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        adjudication = validate_adjudication_response(
            response_for_docket(docket, include_new=True), docket
        )
        first = build_synthesis_packet(docket, adjudication)
        second = build_synthesis_packet(docket, adjudication)
        self.assertEqual(first, second)
        self.assertEqual(len(first["selections"]), 2)
        self.assertTrue(
            all(item["selection_basis"]["deletion_loss"] for item in first["selections"])
        )
        self.assertLess(len(str(first)), len(str(docket)))
        self.assertNotIn("branch_review", first)
        self.assertNotIn("branch_review_support_registry", first)
        review_response = response_for_docket(docket, include_new=True)
        selected_support_ids = {
            support_id
            for decision in review_response["decisions"]
            if decision["status"] == "selected"
            for support_id in decision["support_ids"]
        } | {
            support_id
            for proposal in review_response["new_candidates"]
            for support_id in proposal["support_ids"]
        }
        docket_supports = {
            item["support_id"]: item for item in docket["support_registry"]
        }
        support_owners = {
            support_id: [
                candidate
                for candidate in docket["candidates"]
                if support_id in candidate["support_ids"]
            ]
            for support_id in docket_supports
        }
        review_entry, review_only_support = next(
            (entry, support_id)
            for entry in review_response["branch_review"]
            if entry["status"] == "unactivated"
            for support_id, support in docket_supports.items()
            if support_id not in selected_support_ids
            and support["citable"]
            and support["trust"] == "trusted"
            and support["role"] == "focus_occurrence"
            and any(
                owner["lane"] == "micro"
                and entry["branch_ref"].split("/", 1)[0] in owner["root_ids"]
                and any(
                    anchor == docket["identity"]["ayah_ref"]
                    or anchor.startswith(f"{docket['identity']['ayah_ref']}:")
                    for anchor in owner["anchor_refs"]
                )
                for owner in support_owners[support_id]
            )
        )
        review_entry["support_ids"] = [review_only_support]
        review_adjudication = validate_adjudication_response(review_response, docket)
        review_packet = build_synthesis_packet(docket, review_adjudication)
        prompt, _manifest = render_synthesis_prompt(review_packet)
        self.assertNotIn(
            review_only_support,
            {item["support_id"] for item in review_packet["support_registry"]},
        )
        _artifact, review_outputs = validate_synthesis_response(
            response_for_packet(review_packet),
            review_packet,
            docket,
            review_adjudication,
        )
        friction = review_outputs["friction"]
        review_support = docket_supports[review_only_support]
        self.assertIn(review_support["text"].encode(), friction)
        self.assertIn(review_support["source_type"].encode(), friction)
        self.assertIn(review_support["source_local_id"].encode(), friction)
        self.assertIn(review_entry["branch_ref"].encode(), friction)
        validate_synthesis_packet(first, docket, adjudication)

        mutated = copy.deepcopy(first)
        mutated["selections"][0]["claim"] = "Recomputed-hash packet mutation"
        payload = copy.deepcopy(mutated)
        payload["identity"].pop("synthesis_packet_sha256")
        mutated["identity"]["synthesis_packet_sha256"] = canonical_sha256(payload)
        with self.assertRaisesRegex(ValidationError, "does not match"):
            validate_synthesis_packet(mutated, docket, adjudication)

    def test_synthesis_handoff_rejects_artifact_controlled_adjudication_limit(self) -> None:
        docket = fixture_docket()
        adjudication_options = AdjudicationOptions(max_new_candidates=9)
        response = response_for_docket(docket)
        _prompt, manifest = render_adjudication_prompt(
            docket, options=adjudication_options
        )
        response["identity"]["prompt_sha256"] = manifest["identity"][
            "prompt_sha256"
        ]
        adjudication = validate_adjudication_response(
            response, docket, options=adjudication_options
        )
        with self.assertRaisesRegex(ValidationError, "caller-bound policy"):
            build_synthesis_packet(docket, adjudication)
        packet = build_synthesis_packet(
            docket,
            adjudication,
            adjudication_options=adjudication_options,
        )
        validate_synthesis_packet(
            packet,
            docket,
            adjudication,
            adjudication_options=adjudication_options,
        )

    def test_prompt_binds_packet_and_obeys_budget(self) -> None:
        docket, adjudication, packet = packet_fixture()
        prompt, manifest = render_synthesis_prompt(packet)
        self.assertNotIn("@@", prompt)
        self.assertIn(packet["identity"]["synthesis_packet_sha256"], prompt)
        self.assertEqual(manifest["budget"]["selected_candidate_count"], 2)
        limited_options = SynthesisOptions(max_prompt_bytes=100)
        limited_packet = build_synthesis_packet(
            docket, adjudication, options=limited_options
        )
        with self.assertRaises(BudgetError):
            render_synthesis_prompt(limited_packet)

    def test_custom_limits_round_trip_and_tamper_is_rejected(self) -> None:
        docket, adjudication, _packet = packet_fixture()
        options = SynthesisOptions(
            max_packet_bytes=301_000,
            max_prompt_bytes=376_000,
            min_prose_chars=400,
            max_prose_chars=23_000,
            max_paragraphs=15,
            max_findings=47,
            max_friction_notes=11,
        )
        packet = build_synthesis_packet(docket, adjudication, options=options)
        _prompt, manifest = render_synthesis_prompt(packet)
        artifact, _outputs = validate_synthesis_response(
            response_for_packet(packet), packet, docket, adjudication
        )
        expected_limits = {
            field: getattr(options, field)
            for field in (
                "max_packet_bytes",
                "max_prompt_bytes",
                "min_prose_chars",
                "max_prose_chars",
                "max_paragraphs",
                "max_findings",
                "max_friction_notes",
            )
        }
        self.assertEqual(packet["limits"], expected_limits)
        self.assertEqual(manifest["limits"], expected_limits)
        self.assertEqual(artifact["limits"], expected_limits)
        validate_synthesis_packet(
            packet, docket, adjudication, options=options
        )
        with self.assertRaisesRegex(ValidationError, "packet-bound limits"):
            render_synthesis_prompt(packet, options=SynthesisOptions())

        mutated_packet = copy.deepcopy(packet)
        mutated_packet["limits"]["max_prompt_bytes"] += 1
        mutated_packet["identity"]["synthesis_packet_sha256"] = canonical_sha256(
            {
                **mutated_packet,
                "identity": {
                    key: value
                    for key, value in mutated_packet["identity"].items()
                    if key != "synthesis_packet_sha256"
                },
            }
        )
        with self.assertRaisesRegex(ValidationError, "packet-bound limits"):
            validate_synthesis_packet(
                mutated_packet, docket, adjudication, options=options
            )

        mutated = copy.deepcopy(artifact)
        mutated["limits"]["max_prompt_bytes"] += 1
        payload = copy.deepcopy(mutated)
        payload["identity"].pop("synthesis_payload_sha256")
        mutated["identity"]["synthesis_payload_sha256"] = canonical_sha256(payload)
        with self.assertRaisesRegex(ValidationError, "packet-bound limits"):
            validate_synthesis_artifact(mutated, packet, docket, adjudication)

    def test_valid_response_renders_four_traceable_outputs(self) -> None:
        docket, adjudication, packet = packet_fixture()
        response = response_for_packet(packet)
        artifact, outputs = validate_synthesis_response(
            response, packet, docket, adjudication
        )
        self.assertEqual(set(outputs), {"prose", "evidence", "index", "friction"})
        self.assertNotIn(b"cand_", outputs["prose"])
        self.assertIn(b"cand_", outputs["evidence"])
        self.assertIn(b"root_000672/B010", outputs["evidence"])
        self.assertIn(b"Adjudication'da", outputs["friction"])
        self.assertIn(b"dal taramas", outputs["friction"])
        self.assertIn(b"root_000672/B010", outputs["friction"])
        self.assertIn(adjudication["branch_review"][0]["reason"].encode(), outputs["friction"])
        contact = next(
            contact
            for item in adjudication["branch_review"]
            for contact in item["contact_evidence"]
        )
        self.assertIn(contact["quote"].encode(), outputs["friction"])
        self.assertIn(b"candidate_evidence", outputs["evidence"])
        contribution = artifact["findings"][0]["candidate_contributions"][0]
        self.assertEqual(
            contribution["deletion_loss"],
            packet["selections"][0]["selection_basis"]["deletion_loss"],
        )
        self.assertIn(contribution["deletion_loss"].encode(), outputs["evidence"])
        self.assertEqual(artifact["coverage"]["covered_candidate_count"], 2)
        validate_synthesis_artifact(artifact, packet, docket, adjudication)
        self.assertEqual(
            outputs, render_markdown_outputs(artifact, packet, docket, adjudication)
        )

    def test_synthesis_response_binds_exact_prompt(self) -> None:
        docket, adjudication, packet = packet_fixture()
        response = response_for_packet(packet)
        response["identity"]["prompt_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValidationError, "prompt and packet"):
            validate_synthesis_response(response, packet, docket, adjudication)

    def test_synthesis_options_cannot_exceed_schema_caps(self) -> None:
        for options, field in (
            (SynthesisOptions(max_paragraphs=17), "max_paragraphs"),
            (SynthesisOptions(max_findings=49), "max_findings"),
            (SynthesisOptions(max_friction_notes=13), "max_friction_notes"),
        ):
            with self.assertRaisesRegex(ValidationError, field):
                options.validate()

    def test_every_selected_candidate_requires_a_landing(self) -> None:
        docket, adjudication, packet = packet_fixture()
        response = response_for_packet(packet)
        response["findings"].pop()
        response["paragraphs"].pop()
        with self.assertRaisesRegex(ValidationError, "lack prose findings"):
            validate_synthesis_response(response, packet, docket, adjudication)

    def test_claim_landing_and_complete_branch_lineage_are_mandatory(self) -> None:
        docket, adjudication, packet = packet_fixture()
        response = response_for_packet(packet)
        selection = packet["selections"][0]
        generic = "Bu genel cumle aday iddiasini tasimaz."
        response["paragraphs"][0]["text"] = response["paragraphs"][0]["text"].replace(
            selection["claim"], generic
        )
        response["findings"][0]["landing_quote"] = generic
        with self.assertRaisesRegex(ValidationError, "lacks exact candidate claims"):
            validate_synthesis_response(response, packet, docket, adjudication)

        response = response_for_packet(packet)
        branch_index = next(
            index
            for index, item in enumerate(packet["selections"])
            if len(item["branch_refs"]) > 1
        )
        response["findings"][branch_index]["branch_refs"].pop()
        with self.assertRaisesRegex(ValidationError, "complete finding branch lineage"):
            validate_synthesis_response(response, packet, docket, adjudication)

    def test_unselected_candidate_and_unowned_support_are_rejected(self) -> None:
        docket, adjudication, packet = packet_fixture()
        response = response_for_packet(packet)
        excluded_id = next(
            item["candidate_id"]
            for item in adjudication["decisions"]
            if item["status"] != "selected"
        )
        response["findings"][0]["candidate_ids"] = [excluded_id]
        with self.assertRaisesRegex(ValidationError, "unselected"):
            validate_synthesis_response(response, packet, docket, adjudication)

        response = response_for_packet(packet)
        first_supports = set(packet["selections"][0]["support_ids"])
        other_support = next(
            support_id
            for selection in packet["selections"][1:]
            for support_id in selection["support_ids"]
            if support_id not in first_supports
        )
        response["findings"][0]["support_ids"] = [other_support]
        with self.assertRaisesRegex(ValidationError, "lacks cited support"):
            validate_synthesis_response(response, packet, docket, adjudication)

    def test_exact_landing_containment_and_provenance_rules(self) -> None:
        docket, adjudication, packet = packet_fixture()
        response = response_for_packet(packet)
        response["findings"][0]["landing_quote"] = "prose icinde yok"
        with self.assertRaisesRegex(ValidationError, "absent from prose"):
            validate_synthesis_response(response, packet, docket, adjudication)

        response = response_for_packet(packet)
        response["findings"][0]["landing_quote"] = response["findings"][0][
            "landing_quote"
        ].replace(" ", "  ", 1)
        with self.assertRaisesRegex(ValidationError, "absent from prose"):
            validate_synthesis_response(response, packet, docket, adjudication)

        for leak in (
            " cand_00000000000000000000",
            " Sup_00000000000000000000",
            " new:bounded_route",
            " root_000672/B010",
            " B1",
            " B010",
            " B1234",
            " B0\u200d10",
            " Ｂ０１０",
            r" cand\_00000000000000000000",
            " cand&#95;00000000000000000000",
            " cand<span></span>_00000000000000000000",
            " cand**_**00000000000000000000",
            ' cand<span hidden>x</span>_00000000000000000000',
            " cand<?xml?>_00000000000000000000",
            " cand[]()_00000000000000000000",
            r" [c](#x)[and](#y)\_00000000000000000000",
            r" [c][x][and][y]\_00000000000000000000",
            " cand&amp;amp;amp;amp;amp;amp;#95;00000000000000000000",
            " B٠١٠",
            " B०१०",
        ):
            with self.subTest(leak=leak):
                response = response_for_packet(packet)
                response["paragraphs"][0]["text"] += leak
                with self.assertRaisesRegex(ValidationError, "apparatus identifiers"):
                    validate_synthesis_response(response, packet, docket, adjudication)

        response = response_for_packet(packet)
        response["findings"][1]["containment_quote"] = None
        with self.assertRaisesRegex(ValidationError, "lacks prose containment"):
            validate_synthesis_response(response, packet, docket, adjudication)

    def test_artifact_semantics_survive_recomputed_hash_attack(self) -> None:
        docket, adjudication, packet = packet_fixture()
        artifact, _outputs = validate_synthesis_response(
            response_for_packet(packet), packet, docket, adjudication
        )
        mutated = copy.deepcopy(artifact)
        excluded_id = next(
            item["candidate_id"]
            for item in adjudication["decisions"]
            if item["status"] != "selected"
        )
        mutated["findings"][0]["candidate_ids"] = [excluded_id]
        payload = copy.deepcopy(mutated)
        payload["identity"].pop("synthesis_payload_sha256")
        mutated["identity"]["synthesis_payload_sha256"] = canonical_sha256(payload)
        with self.assertRaisesRegex(ValidationError, "unselected"):
            validate_synthesis_artifact(mutated, packet, docket, adjudication)

        mutated = copy.deepcopy(artifact)
        mutated["findings"][0]["candidate_contributions"][0]["deletion_loss"] = (
            "Forged deletion consequence that is not selection-bound."
        )
        payload = copy.deepcopy(mutated)
        payload["identity"].pop("synthesis_payload_sha256")
        mutated["identity"]["synthesis_payload_sha256"] = canonical_sha256(payload)
        with self.assertRaisesRegex(ValidationError, "findings are not normalized"):
            validate_synthesis_artifact(mutated, packet, docket, adjudication)

    def test_synthesis_publication_repairs_missing_completion_marker(self) -> None:
        docket, adjudication, _packet = packet_fixture()
        synthesis_options = SynthesisOptions(
            max_packet_bytes=301_000,
            max_prompt_bytes=376_000,
            min_prose_chars=400,
            max_prose_chars=23_000,
            max_paragraphs=15,
            max_findings=47,
            max_friction_notes=11,
        )
        packet = build_synthesis_packet(
            docket, adjudication, options=synthesis_options
        )
        adjudication_response = response_for_docket(docket, include_new=True)
        adjudication_prompt, adjudication_manifest = render_adjudication_prompt(docket)
        synthesis_response = response_for_packet(packet)
        synthesis_prompt, synthesis_manifest = render_synthesis_prompt(packet)
        source_bundle = fixture_bundle_for_docket()
        source_raw = pretty_json_bytes(source_bundle)
        prepared, rebuilt_docket = build_prepared_artifacts(
            source_bundle,
            source_path=Path("fixture.json"),
            source_raw=source_raw,
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertEqual(canonical_json_bytes(rebuilt_docket), canonical_json_bytes(docket))
        with tempfile.TemporaryDirectory(dir=V3_ROOT) as temp_dir:
            temporary = Path(temp_dir)
            inputs_root = temporary / "inputs"
            outputs_root = temporary / "outputs"
            write_json_confined(
                inputs_root,
                Path("source/s029/29_38.bundle.json"),
                source_bundle,
            )
            write_json_confined(
                inputs_root,
                Path("prepared/s029/29_38.prepared.json"),
                prepared,
            )
            write_json_confined(
                inputs_root,
                Path("adjudication/s029/29_38.docket.json"),
                docket,
            )
            write_json_confined(
                outputs_root,
                Path("adjudication/s029/29_38.response.json"),
                adjudication_response,
            )
            write_bytes_confined(
                inputs_root,
                Path("adjudication/s029/29_38.prompt.md"),
                adjudication_prompt.encode("utf-8"),
            )
            write_json_confined(
                inputs_root,
                Path("adjudication/s029/29_38.prompt.json"),
                adjudication_manifest,
            )
            write_json_confined(
                outputs_root,
                Path("adjudication/s029/29_38.adjudication.json"),
                adjudication,
            )
            write_json_confined(
                outputs_root,
                Path("adjudication/s029/29_39.adjudication.json"),
                adjudication,
            )
            write_json_confined(
                inputs_root,
                Path("synthesis/s029/29_38.packet.json"),
                packet,
            )
            write_bytes_confined(
                inputs_root,
                Path("synthesis/s029/29_38.prompt.md"),
                synthesis_prompt.encode("utf-8"),
            )
            write_json_confined(
                inputs_root,
                Path("synthesis/s029/29_38.prompt.json"),
                synthesis_manifest,
            )
            write_json_confined(
                outputs_root,
                Path("synthesis/s029/29_38.response.json"),
                synthesis_response,
            )
            with (
                patch("v3lib.adjudication.INPUTS_ROOT", inputs_root),
                patch("v3lib.adjudication.OUTPUTS_ROOT", outputs_root),
                patch("v3lib.synthesis.INPUTS_ROOT", inputs_root),
                patch("v3lib.synthesis.OUTPUTS_ROOT", outputs_root),
            ):
                prepare_options = PrepareOptions(hft_policy="quarantine")
                with self.assertRaisesRegex(
                    ValidationError, "does not match the supplied docket identity"
                ):
                    load_adjudication_for_ayah(
                        "29:39",
                        docket,
                        prepare_options=prepare_options,
                    )
                adjudication_response_path = (
                    outputs_root / "adjudication/s029/29_38.response.json"
                )
                original_adjudication_response = adjudication_response_path.read_bytes()
                malformed_adjudication_response = copy.deepcopy(adjudication_response)
                malformed_adjudication_response["decisions"][0]["candidate_id"] = []
                adjudication_response_path.write_bytes(
                    pretty_json_bytes(malformed_adjudication_response)
                )
                with self.assertRaises(ValidationError):
                    validate_adjudication_for_ayah(
                        "29:38",
                        prepare_options=prepare_options,
                        write=False,
                    )
                adjudication_response_path.write_bytes(original_adjudication_response)
                bound_prompt, bound_manifest = render_source_bound_synthesis_prompt(
                    packet,
                    options=synthesis_options,
                    prepare_options=prepare_options,
                )
                self.assertEqual(bound_prompt, synthesis_prompt)
                self.assertEqual(bound_manifest, synthesis_manifest)
                forged_packet = copy.deepcopy(packet)
                forged_packet["support_registry"][0]["text"] = (
                    "Injected synthesis evidence absent from retained source."
                )
                forged_payload = copy.deepcopy(forged_packet)
                forged_payload["identity"].pop("synthesis_packet_sha256")
                forged_packet["identity"]["synthesis_packet_sha256"] = (
                    canonical_sha256(forged_payload)
                )
                with self.assertRaisesRegex(
                    ValidationError,
                    "does not match docket/adjudication derivation",
                ):
                    render_source_bound_synthesis_prompt(
                        forged_packet,
                        options=synthesis_options,
                        prepare_options=prepare_options,
                    )
                first, _outputs, paths = validate_synthesis_for_ayah(
                    "29:38",
                    options=synthesis_options,
                    prepare_options=prepare_options,
                )
                synthesis_response_path = (
                    outputs_root / "synthesis/s029/29_38.response.json"
                )
                original_synthesis_response = synthesis_response_path.read_bytes()
                malformed_synthesis_response = copy.deepcopy(synthesis_response)
                malformed_synthesis_response["findings"][0]["paragraph_key"] = []
                synthesis_response_path.write_bytes(
                    pretty_json_bytes(malformed_synthesis_response)
                )
                with self.assertRaises(ValidationError):
                    validate_synthesis_for_ayah(
                        "29:38",
                        options=synthesis_options,
                        prepare_options=prepare_options,
                        write=False,
                    )
                synthesis_response_path.write_bytes(original_synthesis_response)
                verify_final_outputs_for_ayah(
                    "29:38",
                    options=synthesis_options,
                    prepare_options=prepare_options,
                )
                handoff_files = (
                    inputs_root / "adjudication/s029/29_38.prompt.md",
                    inputs_root / "adjudication/s029/29_38.prompt.json",
                    inputs_root / "synthesis/s029/29_38.prompt.md",
                    inputs_root / "synthesis/s029/29_38.prompt.json",
                )
                for handoff_path in handoff_files:
                    original = handoff_path.read_bytes()
                    handoff_path.write_bytes(original + b"\n")
                    with self.assertRaisesRegex(
                        ValidationError, "prompt (file|manifest) is not current"
                    ):
                        verify_final_outputs_for_ayah(
                            "29:38",
                            options=synthesis_options,
                            prepare_options=prepare_options,
                        )
                    handoff_path.write_bytes(original)
                marker = Path(paths["validated"])
                marker_bytes = marker.read_bytes()
                marker.unlink()
                self.assertFalse(marker.exists())
                second, _outputs, _paths = validate_synthesis_for_ayah(
                    "29:38",
                    options=synthesis_options,
                    prepare_options=prepare_options,
                )
            self.assertEqual(second, first)
            self.assertEqual(marker.read_bytes(), marker_bytes)

    @unittest.skipUnless(all(path.exists() for path in REAL_S29_FILES), "real S29 run absent")
    def test_real_s29_complete_lineage_and_surprise_regression(self) -> None:
        result = verify_final_outputs_for_ayah(
            "29:38",
            options=DEFAULT_SYNTHESIS_OPTIONS,
            prepare_options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertEqual(result["coverage"]["selected_candidate_count"], 46)
        self.assertEqual(set(result["outputs"]), {"prose", "evidence", "index", "friction"})

        prose = (V3_ROOT / "outputs/s029/29_38.prose.tr.md").read_text(encoding="utf-8")
        evidence = (V3_ROOT / "outputs/s029/29_38.evidence.tr.md").read_text(
            encoding="utf-8"
        )
        index = (V3_ROOT / "outputs/s029/29_38.index.tr.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("işlek rotaya erişimin bozulması", prose)
        self.assertIn("29:41'deki örümcek evi", prose)
        self.assertIn("A:Cutting the Worked Road", index)
        self.assertIn("A:Fitted Dwelling Structure", index)
        self.assertIn("root_001046/B011", evidence)
        self.assertNotIn("root_000672/B010", evidence)


if __name__ == "__main__":
    unittest.main()
