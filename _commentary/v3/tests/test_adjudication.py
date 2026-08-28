from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


V3_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(V3_ROOT))

from tests.test_prepare import fixture_bundle  # noqa: E402
from v3lib.adjudication import (  # noqa: E402
    AdjudicationOptions,
    RESPONSE_SCHEMA,
    _render_adjudication_prompt_unbound as render_adjudication_prompt,
    _validate_adjudication_artifact_unbound as validate_adjudication_artifact,
    _validate_adjudication_response_unbound as validate_adjudication_response,
    load_docket_for_ayah,
    render_adjudication_prompt as render_source_bound_adjudication_prompt,
    validate_adjudication_response as validate_source_bound_adjudication_response,
)
from v3lib.common import (  # noqa: E402
    BudgetError,
    ValidationError,
    canonical_json_bytes,
    canonical_sha256,
    contains_apparatus_id,
    pretty_json_bytes,
    sha256_bytes,
)
from v3lib.prepare import (  # noqa: E402
    PrepareOptions,
    _stable_id,
    build_prepared_artifacts,
    validate_docket,
)


def fixture_bundle_for_docket(*, legacy_hft: bool = False) -> dict:
    bundle = fixture_bundle(valid_hft=legacy_hft)
    bundle["channel_subchannels_anchored_here"][0]["ayah_refs"].append("29:41")
    bundle["channel_subchannels_anchored_here"][0]["ayah_anchors"] += "; ب ي ت 29:41"
    for word_ref, surface, root_ar, root_id in (
        ("29:38:2", "yol", "س ب ل", "root_000672"),
        ("29:38:3", "gorenler", "ب ص ر", "root_000121"),
    ):
        if any(
            word.get("aligned_qac_word_ref") == word_ref
            for word in bundle["word_analysis"]["words"]
        ):
            continue
        bundle["word_analysis"]["words"].append(
            {
                "aligned_qac_word_ref": word_ref,
                "surface_display": surface,
                "root_display": root_ar,
                "gloss_range": surface,
                "root_gloss_range": root_ar,
                "prose": f"{surface} focus evidence",
                "topics": [
                    {
                        "topic_id": f"{word_ref}:ground-{root_id}",
                        "headline": f"{surface} local grounding",
                        "status": "used",
                        "reader_payoff": "local grounding",
                        "reason": "focus morphology",
                        "commentary_obligation": "ledger_only",
                        "representative_source_ids": ["Q1"],
                    }
                ],
            }
        )
    bundle["word_morpheme_spans"] = [
        {
            "word_index": index,
            "surface_ar": word["surface_display"],
            "word_ids": [f"word-{index}"],
            "qac_refs": [
                row["qac_ref"]
                for row in bundle["qac_morphemes"]
                if row["qac_word_ref"] == word["aligned_qac_word_ref"]
            ],
            "morpheme_ids": [
                f"morpheme-{row['qac_ref']}"
                for row in bundle["qac_morphemes"]
                if row["qac_word_ref"] == word["aligned_qac_word_ref"]
            ],
            "aligned_qac_word_ref_upstream": word["aligned_qac_word_ref"],
            "morpheme_skip_count": 0,
        }
        for index, word in enumerate(bundle["word_analysis"]["words"])
    ]
    return bundle


def fixture_docket(*, legacy_hft: bool = False) -> dict:
    bundle = fixture_bundle_for_docket(legacy_hft=legacy_hft)
    _prepared, docket = build_prepared_artifacts(
        bundle,
        source_path=Path("fixture.json"),
        options=PrepareOptions(
            hft_policy="quarantine" if not legacy_hft else "strict",
            allow_legacy_hft_response=legacy_hft,
        ),
    )
    return docket


def response_for_docket(
    docket: dict,
    *,
    include_new: bool = False,
    options: AdjudicationOptions | None = None,
) -> dict:
    options = options or AdjudicationOptions()
    support_registry = {
        item["support_id"]: item for item in docket["support_registry"]
    }
    decisions = []
    for candidate in docket["candidates"]:
        selected = candidate["obligation"] == "must_integrate"
        evidence_supports = [
            support_id
            for support_id in candidate["support_ids"]
            if support_registry[support_id]["role"] == "candidate_evidence"
            and support_registry[support_id]["trust"] == "trusted"
            and support_registry[support_id]["citable"]
        ]
        selected_supports = evidence_supports or [candidate["support_ids"][0]]
        claim_label = f"{candidate['title']} {candidate['candidate_id'][-8:]}"
        decisions.append(
            {
                "candidate_id": candidate["candidate_id"],
                "status": "selected" if selected else "rejected",
                "priority": "core" if selected else None,
                "rationale": "Yerel delil karari.",
                "synthesis_claim": (
                    f"{claim_label} yerel ve sinirli iddiayi kurar."
                    if selected
                    else None
                ),
                "reader_payoff": "Okur baglantiyi gorur." if selected else None,
                "containment": "Sozluk anlami yerine gecmez." if selected else None,
                "selection_basis": (
                    {
                        "kind": "mandatory",
                        "deletion_loss": (
                            f"{claim_label} silinirse ona ozgu yerel yorum sonucu "
                            "metinden tamamen kaybolur."
                        ),
                        "subsumes_candidate_ids": [],
                    }
                    if selected
                    else None
                ),
                "support_ids": selected_supports,
                "branch_refs": [] if selected else list(candidate["branch_refs"]),
            }
        )
    new_candidates = []
    if include_new:
        rooted_supports = []
        for root_id in ("root_000672", "root_000121"):
            owner = next(item for item in docket["candidates"] if root_id in item["root_ids"])
            rooted_supports.append(
                next(
                    support_registry[support_id]
                    for support_id in owner["support_ids"]
                    if support_registry[support_id]["scope"] == "micro"
                )
            )
        macro_owner = next(
            item
            for item in docket["candidates"]
            if item["lane"] == "macro" and "29:41" in item["anchor_refs"]
        )
        macro_supports = [
            support_registry[support_id]
            for support_id in macro_owner["support_ids"]
            if support_registry[support_id]["scope"] == "macro"
            and support_registry[support_id]["role"] == "candidate_evidence"
        ]
        def root_topic_support(root_id: str) -> dict:
            qac_roots = {
                candidate["source_local_id"]: set(candidate["root_ids"])
                for candidate in docket["candidates"]
                if candidate["source_type"] == "qac_morpheme"
            }
            owner = next(
                candidate
                for candidate in docket["candidates"]
                if candidate["source_type"] == "word_analysis"
                and root_id
                in {
                    mapped_root
                    for qac_ref in docket["focus"]["word_analysis_qac_refs"][
                        int(candidate["source_pointer"].split("/")[3])
                    ]
                    for mapped_root in qac_roots.get(qac_ref, set())
                }
            )
            return next(
                support_registry[support_id]
                for support_id in owner["support_ids"]
                if "/topics/" in support_registry[support_id]["json_pointer"]
            )

        local_supports = {
            root_id: root_topic_support(root_id)
            for root_id in ("root_000672", "root_000121")
        }
        branch_descriptors = {
            branch["branch_ref"]: branch["gloss"]
            for root in docket["branch_registry"]
            for branch in root["branches"]
        }
        contact_claims = {
            "root_000672/B010": (
                "root_000672/B010 "
                f"{branch_descriptors['root_000672/B010']}: yol imgesi komsu "
                "yapisal gorunurluk ile sinirli bir temas kurar."
            ),
            "root_000121/B001": (
                "root_000121/B001 "
                f"{branch_descriptors['root_000121/B001']}: gorme imgesi komsu "
                "barinak yapisinin gorunurlugu ile sinirli bir temas kurar."
            ),
        }
        contact_supports = {
            "root_000672/B010": local_supports["root_000672"]["support_id"],
            "root_000121/B001": local_supports["root_000121"]["support_id"],
        }
        new_candidates.append(
            {
                "proposal_key": "webbed_sight",
                "title": "Agsi gorus ve yol",
                "lane": "macro",
                "scope": "pericope",
                "claim": "Yolun kesilmesi gorme paradoksuyla sinirli bir yankiya girer.",
                "mechanism": " ".join(contact_claims.values()),
                "reader_payoff": "Okur bilerek sapmanin gorsel baskisini fark eder.",
                "containment": "Sabil goz hastaligi diye cevrilmez; bu yalniz yankidir.",
                "selection_basis": {
                    "kind": "distinct",
                    "deletion_loss": (
                        "Bu onerme silinirse yol, gorme ve komsu barinak arasindaki "
                        "agsi yapisal yankinin tamami kaybolur."
                    ),
                    "subsumes_candidate_ids": [],
                },
                "confidence": "exploratory",
                "anchor_refs": ["29:38", "29:41"],
                "support_ids": [
                    rooted_supports[0]["support_id"],
                    rooted_supports[1]["support_id"],
                    local_supports["root_000672"]["support_id"],
                    local_supports["root_000121"]["support_id"],
                    macro_supports[0]["support_id"],
                ],
                "branch_refs": ["root_000672/B010", "root_000121/B001"],
            }
        )
    activated: dict[str, list[str]] = {}
    for decision in decisions:
        if decision["status"] != "selected":
            continue
        for branch_ref in decision["branch_refs"]:
            activated.setdefault(branch_ref, []).append(decision["candidate_id"])
    for proposal in new_candidates:
        for branch_ref in proposal["branch_refs"]:
            activated.setdefault(branch_ref, []).append(
                f"new:{proposal['proposal_key']}"
            )
    support_owners = {
        support_id: [
            candidate
            for candidate in docket["candidates"]
            if support_id in candidate["support_ids"]
        ]
        for support_id in support_registry
    }
    decision_by_id = {item["candidate_id"]: item for item in decisions}
    proposal_by_key = {item["proposal_key"]: item for item in new_candidates}

    def occurrence_support(branch_ref: str) -> str:
        root_id = branch_ref.split("/", 1)[0]
        for support_id in support_registry:
            support = support_registry[support_id]
            if support["trust"] != "trusted" or not support["citable"]:
                continue
            if support["role"] != "focus_occurrence":
                continue
            if any(
                owner["lane"] == "micro"
                and root_id in owner["root_ids"]
                and any(
                    anchor == docket["identity"]["ayah_ref"]
                    or anchor.startswith(f"{docket['identity']['ayah_ref']}:")
                    for anchor in owner["anchor_refs"]
                )
                for owner in support_owners[support_id]
            ):
                return support_id
        raise AssertionError(f"fixture lacks review support for {branch_ref}")

    def activation_candidate(activation_ref: str) -> dict:
        if activation_ref.startswith("new:"):
            return proposal_by_key[activation_ref.split(":", 1)[1]]
        return decision_by_id[activation_ref]

    def contact_record(activation_ref: str, branch_ref: str, descriptor: str) -> dict:
        candidate = activation_candidate(activation_ref)
        if activation_ref.startswith("new:"):
            support_id = contact_supports[branch_ref]
            contact_mode = "bounded_inference"
            contact_claim = contact_claims[branch_ref]
        else:
            support_id = next(
                support_id
                for support_id in candidate["support_ids"]
                if support_registry[support_id]["role"] == "candidate_evidence"
                and support_registry[support_id]["trust"] == "trusted"
                and support_registry[support_id]["citable"]
            )
            contact_mode = "source_explicit"
            contact_claim = (
                f"{branch_ref} {descriptor}: yapilandirilmis yayin ankraji bu "
                "dali acikca tasir."
            )
        text = support_registry[support_id]["text"]
        return {
            "activation_ref": activation_ref,
            "support_id": support_id,
            "quote": text[: min(len(text), 120)],
            "contact_mode": contact_mode,
            "contact_claim": contact_claim,
        }

    review_records = [
        {
            "branch_ref": branch["branch_ref"],
            "registry": "focus",
            "descriptor": branch["gloss"],
        }
        for root in docket["branch_registry"]
        for branch in root["branches"]
    ] + [
        {
            "branch_ref": branch["branch_ref"],
            "registry": "nominated",
            "descriptor": branch.get("image_en") or branch.get("image_ar"),
        }
        for branch in docket["nominated_branch_registry"]
    ]

    def review_supports(record: dict, contacts: list[dict]) -> list[str]:
        if record["registry"] == "focus":
            grounding = occurrence_support(record["branch_ref"])
        else:
            grounding = next(
                support_id
                for candidate in docket["candidates"]
                if record["branch_ref"] in candidate["branch_refs"]
                for support_id in candidate["support_ids"]
                if support_registry[support_id]["role"] == "branch_nomination"
                and support_registry[support_id]["trust"] == "trusted"
                and support_registry[support_id]["citable"]
            )
        return sorted({grounding, *(item["support_id"] for item in contacts)})

    def unactivation_basis(record: dict, support_ids: list[str]) -> dict:
        if record["registry"] == "focus":
            root_id = record["branch_ref"].split("/", 1)[0]
            candidate_ids = {
                owner["candidate_id"]
                for support_id in support_ids
                if support_registry[support_id]["role"] == "focus_occurrence"
                for owner in support_owners[support_id]
                if root_id in owner["root_ids"]
            }
        else:
            candidate_ids = {
                owner["candidate_id"]
                for support_id in support_ids
                if support_registry[support_id]["role"] == "branch_nomination"
                for owner in support_owners[support_id]
                if record["branch_ref"] in owner["branch_refs"]
            }
        return {
            "kind": "grounding_only",
            "candidate_ids": sorted(candidate_ids),
            "support_ids": support_ids,
        }

    branch_review = []
    for record in review_records:
        activation_refs = activated.get(record["branch_ref"], [])
        contacts = [
            contact_record(item, record["branch_ref"], record["descriptor"])
            for item in activation_refs
        ]
        support_ids = review_supports(record, contacts)
        branch_review.append(
            {
                "branch_ref": record["branch_ref"],
                "registry": record["registry"],
                "status": "activated" if activation_refs else "unactivated",
                "activation_refs": activation_refs,
                "reason_code": (
                    "supported_activation"
                    if activation_refs
                    else "no_supported_contact"
                ),
                "reason": (
                    f"{record['branch_ref']} {record['descriptor']}: Secili kanit bu dala ozgu yapisal "
                    "temasi sinirli bicimde kurar."
                    if activation_refs
                    else f"{record['branch_ref']} {record['descriptor']}: Paket bu yan dali "
                    "odak veya komsu imgeyle gerekceli bicimde etkinlestirmez."
                ),
                "support_ids": support_ids,
                "unactivation_basis": (
                    None
                    if activation_refs
                    else unactivation_basis(record, support_ids)
                ),
                "contact_evidence": contacts,
            }
        )
    _prompt, manifest = render_adjudication_prompt(docket, options=options)
    return {
        "schema_version": RESPONSE_SCHEMA,
        "identity": {
            "ayah_ref": docket["identity"]["ayah_ref"],
            "source_canonical_sha256": docket["identity"]["source_canonical_sha256"],
            "docket_payload_sha256": docket["identity"]["docket_payload_sha256"],
            "prompt_sha256": manifest["identity"]["prompt_sha256"],
        },
        "decisions": decisions,
        "new_candidates": new_candidates,
        "branch_review": branch_review,
    }


def select_optional_decision(
    response: dict,
    candidate_id: str,
    *,
    suffix: str,
    claim: str | None = None,
    deletion_loss: str | None = None,
    subsumes_candidate_ids: list[str] | None = None,
) -> dict:
    decision = next(
        item for item in response["decisions"] if item["candidate_id"] == candidate_id
    )
    decision.update(
        status="selected",
        priority="supporting",
        synthesis_claim=claim or f"{suffix} icin ayri ve sinirli yorum sonucu.",
        reader_payoff=f"Okur {suffix} katkisini ayri olarak gorur.",
        containment=f"{suffix} yerel anlami degistirmez.",
        selection_basis={
            "kind": "distinct",
            "deletion_loss": deletion_loss
            or f"{suffix} silinirse ona ozgu yorum sonucu metinden tamamen kaybolur.",
            "subsumes_candidate_ids": subsumes_candidate_ids or [],
        },
        branch_refs=[],
    )
    return decision


class AdjudicationTests(unittest.TestCase):
    def test_adjudication_limits_require_exact_integer_types(self) -> None:
        for options in (
            AdjudicationOptions(max_prompt_bytes=True),
            AdjudicationOptions(max_prompt_bytes=1.5),
            AdjudicationOptions(max_new_candidates=True),
            AdjudicationOptions(max_new_candidates=1.5),
        ):
            with self.subTest(options=options):
                with self.assertRaisesRegex(ValidationError, "integer"):
                    options.validate()

    @unittest.skipUnless(
        (V3_ROOT / "inputs/adjudication/s029/29_38.docket.json").exists(),
        "generated real S29 v3 docket not present",
    )
    def test_real_s29_docket_renders_current_contract(self) -> None:
        docket, _path = load_docket_for_ayah(
            "29:38", prepare_options=PrepareOptions(hft_policy="quarantine")
        )
        prompt, manifest = render_adjudication_prompt(docket)
        self.assertTrue(docket["adjudication_gate"]["ready"])
        self.assertEqual(manifest["budget"]["candidate_count"], 69)
        self.assertIn("root_000672/B010", prompt)
        self.assertIn("root_001046/B011", prompt)
        self.assertIn("apply a deletion test", prompt)
        self.assertIn("active_motifs", prompt)
        self.assertIn("not a record of everything that is plausible", prompt)

    @unittest.skipUnless(
        (V3_ROOT / "inputs/adjudication/s029/29_39.docket.json").exists(),
        "generated real S29:39 v3 docket not present",
    )
    def test_real_s29_39_artifact_is_current_and_explicitly_authorized(self) -> None:
        docket, _path = load_docket_for_ayah(
            "29:39",
            prepare_options=PrepareOptions(
                hft_policy="quarantine",
                allow_incomplete_branch_coverage=True,
            ),
        )
        roots = {
            candidate["source_local_id"]: candidate["root_ids"]
            for candidate in docket["candidates"]
            if candidate["source_local_id"]
            in {"29:39:10:arrival-frame", "29:39:17:governed-domain"}
        }
        self.assertEqual(
            roots,
            {
                "29:39:10:arrival-frame": [],
                "29:39:17:governed-domain": [],
            },
        )
        qac_carrier_roots = {
            root_id
            for candidate in docket["candidates"]
            if candidate["source_type"] == "qac_morpheme"
            for root_id in candidate["root_ids"]
        }
        self.assertIn("root_000281", qac_carrier_roots)
        self.assertIn("root_000025", qac_carrier_roots)
        self.assertFalse(docket["scope"]["branch_coverage"]["complete"])
        self.assertTrue(
            docket["adjudication_gate"][
                "incomplete_branch_coverage_authorized"
            ]
        )

    def test_load_rebinds_docket_to_prepared_and_source_snapshot(self) -> None:
        bundle = fixture_bundle()
        raw = pretty_json_bytes(bundle)
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            source_raw=raw,
            options=PrepareOptions(hft_policy="quarantine"),
        )
        with tempfile.TemporaryDirectory(dir=V3_ROOT) as temp_dir:
            inputs_root = Path(temp_dir)
            relatives = {
                "source": Path("source/s029/29_38.bundle.json"),
                "prepared": Path("prepared/s029/29_38.prepared.json"),
                "docket": Path("adjudication/s029/29_38.docket.json"),
            }
            for relative, payload in (
                (relatives["source"], raw),
                (relatives["prepared"], pretty_json_bytes(prepared)),
                (relatives["docket"], pretty_json_bytes(docket)),
            ):
                path = inputs_root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(payload)

            with patch("v3lib.adjudication.INPUTS_ROOT", inputs_root):
                policy = PrepareOptions(hft_policy="quarantine")
                loaded, _path = load_docket_for_ayah(
                    "29:38", prepare_options=policy
                )
                self.assertEqual(loaded["identity"], docket["identity"])
                source_bound_prompt, _manifest = (
                    render_source_bound_adjudication_prompt(
                        docket, prepare_options=policy
                    )
                )
                unbound_prompt, _manifest = render_adjudication_prompt(docket)
                self.assertEqual(source_bound_prompt, unbound_prompt)
                response = response_for_docket(docket)
                self.assertEqual(
                    validate_source_bound_adjudication_response(
                        response, docket, prepare_options=policy
                    )["identity"]["ayah_ref"],
                    "29:38",
                )

                forged = copy.deepcopy(docket)
                support = next(
                    item
                    for item in forged["support_registry"]
                    if item["role"] == "candidate_evidence"
                )
                old_support_id = support["support_id"]
                support["text"] = "Injected evidence absent from the retained source."
                support["support_id"] = _stable_id(
                    "sup",
                    {
                        "source_type": support["source_type"],
                        "source_local_id": support["source_local_id"],
                        "scope": support["scope"],
                        "json_pointer": support["json_pointer"],
                        "role": support["role"],
                        "citable": support["citable"],
                        "trust": support["trust"],
                        "branch_refs": support["branch_refs"],
                        "text_sha256": sha256_bytes(
                            support["text"].encode("utf-8")
                        ),
                    },
                )
                for candidate in forged["candidates"]:
                    if old_support_id not in candidate["support_ids"]:
                        continue
                    candidate["support_ids"] = [
                        support["support_id"] if value == old_support_id else value
                        for value in candidate["support_ids"]
                    ]
                    candidate["candidate_id"] = _stable_id(
                        "cand",
                        {
                            "ayah_ref": forged["identity"]["ayah_ref"],
                            "lane": candidate["lane"],
                            "source_type": candidate["source_type"],
                            "source_local_id": candidate["source_local_id"],
                            "source_pointer": candidate["source_pointer"],
                            "kind": candidate["kind"],
                            "title": candidate["title"],
                            "mandatory": candidate["mandatory"],
                            "obligation": candidate["obligation"],
                            "scope": candidate["scope"],
                            "trust": candidate["trust"],
                            "branch_refs": candidate["branch_refs"],
                            "root_ids": candidate["root_ids"],
                            "unresolved_branch_citations": candidate[
                                "unresolved_branch_citations"
                            ],
                            "anchor_refs": candidate["anchor_refs"],
                            "support_ids": candidate["support_ids"],
                        },
                    )
                forged_payload = copy.deepcopy(forged)
                forged_payload["identity"].pop("docket_payload_sha256")
                forged["identity"]["docket_payload_sha256"] = canonical_sha256(
                    forged_payload
                )
                with self.assertRaisesRegex(
                    ValidationError, "differs from its persisted source binding"
                ):
                    render_source_bound_adjudication_prompt(
                        forged, prepare_options=policy
                    )
                with self.assertRaisesRegex(
                    ValidationError, "differs from its persisted source binding"
                ):
                    validate_source_bound_adjudication_response(
                        response, forged, prepare_options=policy
                    )

                stale = copy.deepcopy(docket)
                stale["branch_registry"][0]["branches"][0]["boundary"] = "changed"
                payload = copy.deepcopy(stale)
                payload["identity"].pop("docket_payload_sha256")
                stale["identity"]["docket_payload_sha256"] = canonical_sha256(payload)
                (inputs_root / relatives["docket"]).write_bytes(
                    pretty_json_bytes(stale)
                )
                with self.assertRaisesRegex(ValidationError, "bind docket"):
                    load_docket_for_ayah("29:38", prepare_options=policy)

                coordinated = copy.deepcopy(docket)
                coordinated["candidates"][0]["title"] = "forged title"
                payload = copy.deepcopy(coordinated)
                payload["identity"].pop("docket_payload_sha256")
                coordinated["identity"]["docket_payload_sha256"] = canonical_sha256(
                    payload
                )
                coordinated_prepared = copy.deepcopy(prepared)
                coordinated_prepared["artifacts"][
                    "docket_payload_sha256"
                ] = coordinated["identity"]["docket_payload_sha256"]
                coordinated_prepared["budget"]["docket_bytes"] = len(
                    canonical_json_bytes(coordinated)
                )
                coordinated_prepared["budget"][
                    "estimated_tokens_chars_div_4"
                ] = (len(canonical_json_bytes(coordinated)) + 3) // 4
                (inputs_root / relatives["docket"]).write_bytes(
                    pretty_json_bytes(coordinated)
                )
                (inputs_root / relatives["prepared"]).write_bytes(
                    pretty_json_bytes(coordinated_prepared)
                )
                with self.assertRaisesRegex(
                    ValidationError, "identity hash|rederive from source"
                ):
                    load_docket_for_ayah("29:38", prepare_options=policy)

                (inputs_root / relatives["docket"]).write_bytes(
                    pretty_json_bytes(docket)
                )
                (inputs_root / relatives["prepared"]).write_bytes(
                    pretty_json_bytes(prepared)
                )
                (inputs_root / relatives["source"]).write_bytes(
                    json.dumps(bundle, ensure_ascii=False, indent=2).encode("utf-8")
                )
                with self.assertRaisesRegex(ValidationError, "raw hash"):
                    load_docket_for_ayah("29:38", prepare_options=policy)

                (inputs_root / relatives["source"]).write_bytes(raw)
                forged_path = copy.deepcopy(prepared)
                forged_path["identity"]["source"]["path"] = "/forged/source.json"
                (inputs_root / relatives["prepared"]).write_bytes(
                    pretty_json_bytes(forged_path)
                )
                with self.assertRaisesRegex(ValidationError, "rederive from source"):
                    load_docket_for_ayah("29:38", prepare_options=policy)

    def test_handoff_policy_cannot_be_promoted_by_artifact_edits(self) -> None:
        bundle = fixture_bundle()
        bundle["root_lexicon"]["root_000121"]["dictionary_entry"] = None
        raw = pretty_json_bytes(bundle)
        authorized_policy = PrepareOptions(
            hft_policy="quarantine",
            allow_incomplete_branch_coverage=True,
        )
        prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            source_raw=raw,
            options=authorized_policy,
        )
        with tempfile.TemporaryDirectory(dir=V3_ROOT) as temp_dir:
            inputs_root = Path(temp_dir)
            for relative, payload in (
                (Path("source/s029/29_38.bundle.json"), raw),
                (
                    Path("prepared/s029/29_38.prepared.json"),
                    pretty_json_bytes(prepared),
                ),
                (
                    Path("adjudication/s029/29_38.docket.json"),
                    pretty_json_bytes(docket),
                ),
            ):
                path = inputs_root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(payload)
            with patch("v3lib.adjudication.INPUTS_ROOT", inputs_root):
                with self.assertRaisesRegex(ValidationError, "rederive from source"):
                    load_docket_for_ayah(
                        "29:38",
                        prepare_options=PrepareOptions(hft_policy="quarantine"),
                    )
                loaded, _path = load_docket_for_ayah(
                    "29:38", prepare_options=authorized_policy
                )
                self.assertTrue(loaded["adjudication_gate"]["ready"])

    def test_prompt_is_bound_compact_and_contains_no_diagnostic_quarantine(self) -> None:
        docket = fixture_docket()
        prompt, manifest = render_adjudication_prompt(docket)
        self.assertNotIn("@@", prompt)
        self.assertIn(docket["identity"]["docket_payload_sha256"], prompt)
        self.assertIn(canonical_json_bytes(docket).decode("utf-8"), prompt)
        self.assertNotIn("outlier_webbed_path", prompt)
        self.assertIn(
            "support prose need not repeat them", prompt
        )
        self.assertIn('qualifier such as "where attested"', prompt)
        self.assertIn("does not establish occurrence", prompt)
        self.assertEqual(manifest["budget"]["candidate_count"], len(docket["candidates"]))

    def test_prompt_budget_fails_without_truncation(self) -> None:
        with self.assertRaises(BudgetError):
            render_adjudication_prompt(
                fixture_docket(),
                options=AdjudicationOptions(max_prompt_bytes=100),
            )

    def test_malformed_model_discriminators_raise_validation_errors(self) -> None:
        docket = fixture_docket()
        for field, value in (
            ("candidate_id", []),
            ("status", {}),
            ("priority", []),
        ):
            with self.subTest(field=field):
                response = response_for_docket(docket)
                response["decisions"][0][field] = value
                with self.assertRaises(ValidationError):
                    validate_adjudication_response(response, docket)

        for value in (None, [], {}, False, 0, ""):
            with self.subTest(contact_activation_ref=value):
                response = response_for_docket(docket, include_new=True)
                activated = next(
                    item
                    for item in response["branch_review"]
                    if item["status"] == "activated"
                )
                activated["contact_evidence"][0]["activation_ref"] = value
                with self.assertRaises(ValidationError):
                    validate_adjudication_response(response, docket)

        for padding in (" ", "\t", "\u00a0"):
            with self.subTest(contact_activation_padding=repr(padding)):
                response = response_for_docket(docket, include_new=True)
                activated = next(
                    item
                    for item in response["branch_review"]
                    if item["status"] == "activated"
                )
                contact = activated["contact_evidence"][0]
                contact["activation_ref"] = (
                    padding + contact["activation_ref"] + padding
                )
                with self.assertRaisesRegex(ValidationError, "activation_ref is invalid"):
                    validate_adjudication_response(response, docket)

    def test_complete_response_normalizes_and_hashes_new_candidate(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket, include_new=True)
        first = validate_adjudication_response(response, docket)
        second = validate_adjudication_response(copy.deepcopy(response), docket)
        self.assertEqual(first, second)
        self.assertEqual(first["coverage"]["decision_count"], len(docket["candidates"]))
        self.assertEqual(first["coverage"]["selected_new_count"], 1)
        self.assertRegex(first["new_candidates"][0]["candidate_id"], r"^new_[0-9a-f]{20}$")
        validate_adjudication_artifact(first, docket)

        base_proposal = response["new_candidates"][0]
        distinct_claims = [
            "Yol engeli gorme fiilinin bilincli taniklik gerilimini belirginlestirir.",
            "Ag imgesi hareket alaninin kirilgan barinak yapisini one cikarir.",
            "Calisma kokunun rota yan dali eylemin sonucunu mekana tasir.",
            "Komsu ev benzetmesi yol seciminin dayanak sorununu gorunur kilar.",
            "Goren ozne ile kapanan gecit arasinda ironik bir erisim farki dogar.",
            "Toplumsal engelleme sahnesi bireysel basiret iddiasini sinar.",
            "Yolun islenmisligi sapmanin kendiliginden olmadigini ima eder.",
            "Barinak zayifligi gorunen guven ile gercek dayaniklilik arasini acar.",
            "Ard arda gelen imgeler eylem rota ve algiyi tek hesapta bulusturur.",
        ]
        response["new_candidates"] = [
            {
                **copy.deepcopy(base_proposal),
                "proposal_key": f"proposal_{index}",
                "title": f"Proposal {index}",
                "claim": distinct_claims[index],
                "selection_basis": {
                    **copy.deepcopy(base_proposal["selection_basis"]),
                    "deletion_loss": (
                        f"Bu {index} numarali onerme silinirse "
                        f"{distinct_claims[index].casefold()} sonucu yorumdan kaybolur."
                    ),
                },
            }
            for index in range(9)
        ]
        with self.assertRaisesRegex(ValidationError, "exceeds limit"):
            validate_adjudication_response(response, docket)
        expanded_options = AdjudicationOptions(max_new_candidates=9)
        _prompt, expanded_manifest = render_adjudication_prompt(
            docket, options=expanded_options
        )
        response["identity"]["prompt_sha256"] = expanded_manifest["identity"][
            "prompt_sha256"
        ]
        expanded_refs = [f"new:proposal_{index}" for index in range(9)]
        for item in response["branch_review"]:
            if item["status"] == "activated":
                original_contact = item["contact_evidence"][0]
                item["activation_refs"] = expanded_refs
                item["contact_evidence"] = [
                    {
                        **original_contact,
                        "activation_ref": activation_ref,
                    }
                    for activation_ref in expanded_refs
                ]
        with self.assertRaisesRegex(ValidationError, "generic evidence support"):
            validate_adjudication_response(
                response,
                docket,
                options=expanded_options,
            )
        response_schema = json.loads(
            (V3_ROOT / "schemas/adjudication-response.schema.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(response_schema["properties"]["new_candidates"]["maxItems"], 20)

        mutated = copy.deepcopy(first)
        must_decision = next(
            item
            for item in mutated["decisions"]
            if next(
                candidate
                for candidate in docket["candidates"]
                if candidate["candidate_id"] == item["candidate_id"]
            )["obligation"]
            == "must_integrate"
        )
        must_decision.update(
            status="rejected",
            priority=None,
            synthesis_claim=None,
            reader_payoff=None,
            containment=None,
            selection_basis=None,
        )
        payload = copy.deepcopy(mutated)
        payload["identity"].pop("adjudication_payload_sha256")
        mutated["identity"]["adjudication_payload_sha256"] = canonical_sha256(payload)
        with self.assertRaisesRegex(ValidationError, "must_integrate"):
            validate_adjudication_artifact(mutated, docket)

        mutated = copy.deepcopy(first)
        mutated["selection"]["rejected_candidate_ids"] = []
        payload = copy.deepcopy(mutated)
        payload["identity"].pop("adjudication_payload_sha256")
        mutated["identity"]["adjudication_payload_sha256"] = canonical_sha256(payload)
        with self.assertRaisesRegex(ValidationError, "rejected index"):
            validate_adjudication_artifact(mutated, docket)

    def test_validated_adjudication_limit_is_caller_bound(self) -> None:
        docket = fixture_docket()
        options = AdjudicationOptions(max_new_candidates=9)
        response = response_for_docket(docket)
        _prompt, manifest = render_adjudication_prompt(docket, options=options)
        response["identity"]["prompt_sha256"] = manifest["identity"][
            "prompt_sha256"
        ]
        artifact = validate_adjudication_response(
            response, docket, options=options
        )
        with self.assertRaisesRegex(ValidationError, "caller-bound policy"):
            validate_adjudication_artifact(artifact, docket)
        validate_adjudication_artifact(artifact, docket, options=options)

    def test_response_binds_exact_prompt_and_partitions_focus_branches(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket, include_new=True)
        artifact = validate_adjudication_response(response, docket)
        expected_branches = [
            branch["branch_ref"]
            for root in docket["branch_registry"]
            for branch in root["branches"]
        ] + [
            branch["branch_ref"] for branch in docket["nominated_branch_registry"]
        ]
        self.assertEqual(
            [item["branch_ref"] for item in artifact["branch_review"]],
            expected_branches,
        )
        self.assertEqual(
            artifact["coverage"]["reviewed_focus_branch_count"],
            sum(len(root["branches"]) for root in docket["branch_registry"]),
        )
        activated = {
            item["branch_ref"]
            for item in artifact["branch_review"]
            if item["status"] == "activated"
        }
        self.assertEqual(
            activated, {"root_000672/B010", "root_000121/B001"}
        )

        stale_prompt = copy.deepcopy(response)
        stale_prompt["identity"]["prompt_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValidationError, "does not bind prompt"):
            validate_adjudication_response(stale_prompt, docket)

        incomplete = copy.deepcopy(response)
        incomplete["branch_review"].pop()
        with self.assertRaisesRegex(ValidationError, "every focus and nominated branch"):
            validate_adjudication_response(incomplete, docket)

        reordered = copy.deepcopy(response)
        reordered["branch_review"][0], reordered["branch_review"][1] = (
            reordered["branch_review"][1],
            reordered["branch_review"][0],
        )
        with self.assertRaisesRegex(ValidationError, "registry order"):
            validate_adjudication_response(reordered, docket)

    def test_activated_branch_contact_requires_exact_candidate_evidence(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket, include_new=True)
        target = next(
            item for item in response["branch_review"] if item["status"] == "activated"
        )
        target["contact_evidence"][0]["quote"] = "Bu alinti destekte yoktur."
        with self.assertRaisesRegex(ValidationError, "exact support excerpt"):
            validate_adjudication_response(response, docket)

    def test_nomination_and_occurrence_do_not_establish_branch_contact(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket, include_new=True)
        supports = {
            support["support_id"]: support for support in docket["support_registry"]
        }
        target = next(
            item for item in response["branch_review"] if item["status"] == "activated"
        )
        ineligible = next(
            support
            for support in supports.values()
            if support["role"] in {"focus_occurrence", "branch_nomination"}
            and support["support_id"] in target["support_ids"]
        )
        target["contact_evidence"][0].update(
            support_id=ineligible["support_id"],
            quote=ineligible["text"][: min(len(ineligible["text"]), 120)],
        )
        with self.assertRaisesRegex(ValidationError, "evidence-role support"):
            validate_adjudication_response(response, docket)

    def test_selected_occurrence_carrier_cannot_enter_synthesis(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket)
        carrier = next(
            item for item in docket["candidates"] if item["source_type"] == "qac_morpheme"
        )
        select_optional_decision(
            response,
            carrier["candidate_id"],
            suffix="occurrence_only",
        )
        with self.assertRaisesRegex(ValidationError, "candidate_evidence"):
            validate_adjudication_response(response, docket)

    def test_prose_bound_selected_fields_reject_apparatus_ids(self) -> None:
        docket = fixture_docket()
        for field, leak in (
            ("synthesis_claim", " root_000672/B010"),
            ("reader_payoff", " cand_00000000000000000000"),
            ("reader_payoff", " Sup_00000000000000000000"),
            ("containment", " B1"),
            ("containment", " B010"),
            ("containment", " B1234"),
            (
                "synthesis_claim",
                ' cand<span style="display:none">x</span>_00000000000000000000',
            ),
            ("reader_payoff", " cand<?x>_00000000000000000000"),
            ("containment", " cand[]()_00000000000000000000"),
            (
                "synthesis_claim",
                r" [c](#x)[and](#y)\_00000000000000000000",
            ),
            (
                "synthesis_claim",
                r" [c][x][and][y]\_00000000000000000000",
            ),
            (
                "reader_payoff",
                " cand&amp;amp;amp;amp;amp;amp;#95;00000000000000000000",
            ),
            ("containment", " B٠١٠"),
            ("containment", " B०१०"),
        ):
            with self.subTest(field=field):
                response = response_for_docket(docket)
                selected = next(
                    item for item in response["decisions"] if item["status"] == "selected"
                )
                selected[field] += leak
                with self.assertRaisesRegex(ValidationError, "apparatus identifiers"):
                    validate_adjudication_response(response, docket)

        for embedded in ("AB010", "B010x", "xB0\u200d10"):
            with self.subTest(embedded=embedded):
                self.assertFalse(contains_apparatus_id(embedded))
        for obfuscated in (
            "B0\u200d10",
            "cand_abcdef\u200dabcdef",
            "Ｂ０１０",
            "ｒｏｏｔ＿０００６７２／Ｂ０１０",
            r"cand\_00000000000000000000",
            "cand&#95;00000000000000000000",
            "cand<span></span>_00000000000000000000",
            "cand**_**00000000000000000000",
            "B٠١٠",
            "B०१०",
        ):
            with self.subTest(obfuscated=obfuscated):
                self.assertTrue(contains_apparatus_id(obfuscated))
        deeply_encoded = "cand&#95;00000000000000000000"
        for _ in range(40):
            deeply_encoded = deeply_encoded.replace("&", "&amp;", 1)
        self.assertTrue(contains_apparatus_id(deeply_encoded))

    def test_prose_bound_new_candidate_fields_reject_apparatus_ids(self) -> None:
        docket = fixture_docket()
        for field, leak in (
            ("claim", " root_000672/B010"),
            ("reader_payoff", " new:bounded_route"),
            ("containment", " B010"),
            ("claim", r" cand\_00000000000000000000"),
            ("reader_payoff", " cand&#95;00000000000000000000"),
            ("containment", " cand<span></span>_00000000000000000000"),
            (
                "claim",
                ' cand<span aria-hidden="true">x</span>_00000000000000000000',
            ),
            ("reader_payoff", " cand<!x>_00000000000000000000"),
            ("containment", " cand[]()_00000000000000000000"),
            ("containment", r" [c][x][and][y]\_00000000000000000000"),
            ("reader_payoff", " B٠١٠"),
        ):
            with self.subTest(field=field):
                response = response_for_docket(docket, include_new=True)
                response["new_candidates"][0][field] += leak
                with self.assertRaisesRegex(ValidationError, "apparatus identifiers"):
                    validate_adjudication_response(response, docket)

    def test_raw_model_schemas_avoid_adapter_unsupported_keywords(self) -> None:
        unsupported = {"oneOf", "uniqueItems"}

        def found_keywords(value: object) -> set[str]:
            if isinstance(value, dict):
                return (set(value) & unsupported) | set().union(
                    *(found_keywords(item) for item in value.values()), set()
                )
            if isinstance(value, list):
                return set().union(
                    *(found_keywords(item) for item in value), set()
                )
            return set()

        for filename in (
            "adjudication-response.schema.json",
            "synthesis-response.schema.json",
        ):
            with self.subTest(filename=filename):
                schema = json.loads((V3_ROOT / "schemas" / filename).read_text())
                self.assertEqual(found_keywords(schema), set())

    def test_selected_candidate_must_activate_every_branch_on_exposed_support(self) -> None:
        bundle = fixture_bundle_for_docket()
        bundle["channel_subchannels_anchored_here"][0]["scene_or_process"] += (
            " root_000672/B001"
        )
        _prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        supports = {
            item["support_id"]: item for item in docket["support_registry"]
        }
        candidate = next(
            item
            for item in docket["candidates"]
            if item["source_type"] == "channel"
            and any(
                "root_000672/B001" in supports[support_id]["branch_refs"]
                for support_id in item["support_ids"]
            )
        )
        branch_support = next(
            support_id
            for support_id in candidate["support_ids"]
            if "root_000672/B001" in supports[support_id]["branch_refs"]
            and supports[support_id]["role"] == "candidate_evidence"
        )
        response = response_for_docket(docket)
        decision = select_optional_decision(
            response,
            candidate["candidate_id"],
            suffix="branch_bearing_channel",
        )
        decision["support_ids"] = [branch_support]
        self.assertEqual(decision["branch_refs"], [])
        with self.assertRaisesRegex(
            ValidationError, "branch-bearing support without activating"
        ):
            validate_adjudication_response(response, docket)

    def test_new_candidate_must_activate_every_branch_on_exposed_support(self) -> None:
        bundle = fixture_bundle_for_docket()
        bundle["channel_subchannels_anchored_here"][0]["scene_or_process"] += (
            " root_000672/B001"
        )
        _prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        supports = {
            item["support_id"]: item for item in docket["support_registry"]
        }
        branch_support = next(
            support_id
            for candidate in docket["candidates"]
            if candidate["source_type"] == "channel"
            for support_id in candidate["support_ids"]
            if "root_000672/B001" in supports[support_id]["branch_refs"]
            and supports[support_id]["role"] == "candidate_evidence"
        )
        response = response_for_docket(docket, include_new=True)
        proposal = response["new_candidates"][0]
        self.assertNotIn("root_000672/B001", proposal["branch_refs"])
        replaced = next(
            support_id
            for support_id in proposal["support_ids"]
            if supports[support_id]["scope"] == "macro"
            and supports[support_id]["role"] == "candidate_evidence"
        )
        proposal["support_ids"] = sorted(
            branch_support if support_id == replaced else support_id
            for support_id in proposal["support_ids"]
        )
        with self.assertRaisesRegex(
            ValidationError, "branch-bearing support without activating"
        ):
            validate_adjudication_response(response, docket)

    def test_new_candidate_support_and_branch_floods_are_rejected(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket, include_new=True)
        response["new_candidates"][0]["support_ids"] = [
            item["support_id"] for item in docket["support_registry"]
        ]
        with self.assertRaisesRegex(ValidationError, "supports; limit"):
            validate_adjudication_response(response, docket)

        bundle = fixture_bundle_for_docket()
        sbl_branches = bundle["root_lexicon"]["root_000672"]["dictionary_entry"][
            "branches"
        ]
        for branch_id in ("B011", "B012", "B013", "B014", "B015"):
            sbl_branches.append(
                {
                    **copy.deepcopy(sbl_branches[0]),
                    "branch_ref": f"root_000672/{branch_id}",
                    "concept_gloss": {"text": f"bounded branch {branch_id}"},
                }
            )
        _prepared, expanded = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        response = response_for_docket(expanded, include_new=True)
        response["new_candidates"][0]["branch_refs"] = [
            branch["branch_ref"]
            for root in expanded["branch_registry"]
            if root["root_id"] == "root_000672"
            for branch in root["branches"]
        ][:7]
        with self.assertRaisesRegex(ValidationError, "branches; limit"):
            validate_adjudication_response(response, expanded)

    def test_new_candidate_rejects_legacy_support_leakage(self) -> None:
        docket = fixture_docket(legacy_hft=True)
        response = response_for_docket(docket, include_new=True)
        legacy_support = next(
            item["support_id"]
            for item in docket["support_registry"]
            if item["trust"] == "legacy_unbound"
        )
        response["new_candidates"][0]["support_ids"][-1] = legacy_support
        with self.assertRaisesRegex(ValidationError, "trusted, citable evidence"):
            validate_adjudication_response(response, docket)

    def test_generic_existing_candidate_cannot_activate_a_branch(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket)
        candidate = next(
            item
            for item in docket["candidates"]
            if item["source_type"] == "channel" and item["branch_refs"]
        )
        decision = select_optional_decision(
            response,
            candidate["candidate_id"],
            suffix="generic_channel",
        )
        branch_ref = candidate["branch_refs"][0]
        decision["branch_refs"] = [branch_ref]
        supports = {
            item["support_id"]: item for item in docket["support_registry"]
        }
        contact_support = decision["support_ids"][0]
        target = next(
            item for item in response["branch_review"] if item["branch_ref"] == branch_ref
        )
        descriptor = next(
            branch["gloss"]
            for root in docket["branch_registry"]
            for branch in root["branches"]
            if branch["branch_ref"] == branch_ref
        )
        target.update(
            status="activated",
            activation_refs=[candidate["candidate_id"]],
            reason_code="supported_activation",
            reason=(
                f"{branch_ref} {descriptor}: generic kanal delili dali "
                "etkinlestirmeye calisir."
            ),
            support_ids=sorted({*target["support_ids"], contact_support}),
            unactivation_basis=None,
            contact_evidence=[
                {
                    "activation_ref": candidate["candidate_id"],
                    "support_id": contact_support,
                    "quote": supports[contact_support]["text"][:120],
                    "contact_mode": "source_explicit",
                    "contact_claim": (
                        f"{branch_ref} {descriptor}: generic kanal metni dal "
                        "temasi olarak ileri surulur."
                    ),
                }
            ],
        )
        with self.assertRaisesRegex(ValidationError, "structured publication anchor"):
            validate_adjudication_response(response, docket)

    def test_bounded_inference_cannot_reuse_one_support_for_many_branches(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket, include_new=True)
        activated = [
            item for item in response["branch_review"] if item["status"] == "activated"
        ]
        first_contact = activated[0]["contact_evidence"][0]
        second_contact = activated[1]["contact_evidence"][0]
        second_contact["support_id"] = first_contact["support_id"]
        second_contact["quote"] = first_contact["quote"]
        activated[1]["support_ids"] = sorted(
            {*activated[1]["support_ids"], first_contact["support_id"]}
        )
        with self.assertRaisesRegex(
            ValidationError, "generic evidence support|source-derived relation"
        ):
            validate_adjudication_response(response, docket)

    def test_bounded_inference_cannot_relabel_unrelated_candidate_evidence(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket, include_new=True)
        target = next(
            item
            for item in response["branch_review"]
            if item["branch_ref"] == "root_000672/B010"
        )
        contact = target["contact_evidence"][0]
        old_support_id = contact["support_id"]
        unrelated_owner = next(
            candidate
            for candidate in docket["candidates"]
            if candidate["source_type"] == "word_analysis"
            and candidate["anchor_refs"] == ["29:38:1"]
        )
        supports = {item["support_id"]: item for item in docket["support_registry"]}
        unrelated_support = next(
            supports[support_id]
            for support_id in unrelated_owner["support_ids"]
            if "/topics/" in supports[support_id]["json_pointer"]
        )
        proposal = response["new_candidates"][0]
        proposal["support_ids"] = sorted(
            unrelated_support["support_id"] if item == old_support_id else item
            for item in proposal["support_ids"]
        )
        target["support_ids"] = sorted(
            unrelated_support["support_id"] if item == old_support_id else item
            for item in target["support_ids"]
        )
        contact["support_id"] = unrelated_support["support_id"]
        contact["quote"] = unrelated_support["text"][:120]
        with self.assertRaisesRegex(ValidationError, "source-derived relation"):
            validate_adjudication_response(response, docket)

    def test_bounded_inference_uses_morpheme_spans_not_upstream_word_number(self) -> None:
        bundle = fixture_bundle_for_docket()
        bundle["word_morpheme_spans"] = [
            {
                "word_index": index,
                "surface_ar": word["surface_display"],
                "word_ids": [f"word-{index}"],
                "qac_refs": [
                    row["qac_ref"]
                    for row in bundle["qac_morphemes"]
                    if row["qac_word_ref"] == word["aligned_qac_word_ref"]
                ],
                "morpheme_ids": [
                    f"morpheme-{row['qac_ref']}"
                    for row in bundle["qac_morphemes"]
                    if row["qac_word_ref"] == word["aligned_qac_word_ref"]
                ],
                "aligned_qac_word_ref_upstream": word["aligned_qac_word_ref"],
                "morpheme_skip_count": 0,
            }
            for index, word in enumerate(bundle["word_analysis"]["words"])
        ]
        sbl_word = next(
            word
            for word in bundle["word_analysis"]["words"]
            if word.get("root_display") == "س ب ل"
        )
        sbl_index = bundle["word_analysis"]["words"].index(sbl_word)
        sbl_word["aligned_qac_word_ref"] = "29:38:1"
        bundle["word_morpheme_spans"][sbl_index][
            "aligned_qac_word_ref_upstream"
        ] = "29:38:1"
        _prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("misaligned-fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        artifact = validate_adjudication_response(
            response_for_docket(docket, include_new=True), docket
        )
        activated = {
            item["branch_ref"]
            for item in artifact["branch_review"]
            if item["status"] == "activated"
        }
        self.assertIn("root_000672/B010", activated)

    def test_bounded_inference_maps_a_repeated_root_at_its_exact_qac_ref(self) -> None:
        bundle = fixture_bundle_for_docket()
        bundle["qac_morphemes"].append(
            {
                "qac_ref": "29:38:4:1",
                "qac_word_ref": "29:38:4",
                "surface_ar": "سَبِيلًا",
                "lemma_ar": "سَبِيل",
                "root_ar": "س ب ل",
                "pos": "N",
                "morpheme_role": "STEM",
                "morph_features": "N",
            }
        )
        bundle["word_analysis"]["words"].append(
            {
                "aligned_qac_word_ref": "29:38:4",
                "surface_display": "ikinci yol",
                "root_display": "yanlis kok etiketi",
                "gloss_range": "ikinci yol",
                "root_gloss_range": "yanlis kok etiketi",
                "prose": "Ikinci yol kullanimina ait odak delili.",
                "topics": [
                    {
                        "topic_id": "29:38:4:second-sbl",
                        "headline": "ikinci yol kullanimi",
                        "status": "used",
                        "reader_payoff": "Ikinci kullanim ayri gorulur.",
                        "reason": "Exact span ikinci QAC kokunu baglar.",
                        "commentary_obligation": "ledger_only",
                        "representative_source_ids": ["Q2"],
                    }
                ],
            }
        )
        bundle["word_morpheme_spans"].append(
            {
                "word_index": 3,
                "surface_ar": "سَبِيلًا",
                "word_ids": ["word-3"],
                "qac_refs": ["29:38:4:1"],
                "morpheme_ids": ["morpheme-3"],
                "aligned_qac_word_ref_upstream": "29:38:4",
                "morpheme_skip_count": 0,
            }
        )
        _prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("repeated-root-fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        response = response_for_docket(docket, include_new=True)
        supports = {item["support_id"]: item for item in docket["support_registry"]}
        second_owner = next(
            candidate
            for candidate in docket["candidates"]
            if candidate["source_pointer"]
            == "/word_analysis/words/3/topics/0"
        )
        second_support = next(
            supports[support_id]
            for support_id in second_owner["support_ids"]
            if supports[support_id]["json_pointer"]
            == "/word_analysis/words/3/topics/0"
        )
        target = next(
            item
            for item in response["branch_review"]
            if item["branch_ref"] == "root_000672/B010"
        )
        old_support_id = target["contact_evidence"][0]["support_id"]
        proposal = response["new_candidates"][0]
        proposal["support_ids"] = sorted(
            second_support["support_id"] if item == old_support_id else item
            for item in proposal["support_ids"]
        )
        target["support_ids"] = sorted(
            second_support["support_id"] if item == old_support_id else item
            for item in target["support_ids"]
        )
        target["contact_evidence"][0]["support_id"] = second_support["support_id"]
        target["contact_evidence"][0]["quote"] = second_support["text"][:120]
        validate_adjudication_response(response, docket)

    def test_word_span_cannot_union_morphemes_from_different_qac_words(self) -> None:
        bundle = fixture_bundle_for_docket()
        bundle["word_morpheme_spans"][1]["qac_refs"] = [
            "29:38:2:1",
            "29:38:3:1",
        ]
        bundle["word_morpheme_spans"][1]["morpheme_ids"] = [
            "cross-word-1",
            "cross-word-2",
        ]
        bundle["word_morpheme_spans"][2] = None
        with self.assertRaisesRegex(ValidationError, "invalid or reused QAC lineage"):
            build_prepared_artifacts(
                bundle,
                source_path=Path("cross-word-span.json"),
                options=PrepareOptions(hft_policy="quarantine"),
            )

        docket = fixture_docket()
        forged = copy.deepcopy(docket)
        forged["focus"]["word_analysis_qac_refs"][1] = [
            "29:38:2:1",
            "29:38:3:1",
        ]
        forged["focus"]["word_analysis_qac_refs"][2] = []
        payload = copy.deepcopy(forged)
        payload["identity"].pop("docket_payload_sha256")
        forged["identity"]["docket_payload_sha256"] = canonical_sha256(payload)
        with self.assertRaisesRegex(ValidationError, "QAC lineage is invalid"):
            validate_docket(forged)

    def test_bounded_inference_contact_support_is_single_use_across_proposals(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket, include_new=True)
        first = response["new_candidates"][0]
        second = copy.deepcopy(first)
        second.update(
            proposal_key="webbed_sight_two",
            title="Gorunen kesinti ve ikinci yanki",
            claim="Yol kesintisi ikinci ve ayri bir gorunurluk gerilimi kurar.",
            reader_payoff="Okur kesintinin ikinci gorsel basincini ayri olarak fark eder.",
            containment="Bu ikinci yanki yerel sozu baska bir sozluk anlamina cevirmez.",
            branch_refs=["root_000672/B010"],
        )
        descriptor = next(
            branch["gloss"]
            for root in docket["branch_registry"]
            for branch in root["branches"]
            if branch["branch_ref"] == "root_000672/B010"
        )
        second["mechanism"] = (
            f"root_000672/B010 {descriptor}: ikinci temas yapisal baskiyi "
            "ayri ve sinirli bicimde kurar."
        )
        second["selection_basis"]["deletion_loss"] = (
            "Bu ikinci onerme silinirse gorunurluk geriliminin ayri yapisal "
            "katmani metinden kaybolur."
        )
        response["new_candidates"].append(second)

        target = next(
            item
            for item in response["branch_review"]
            if item["branch_ref"] == "root_000672/B010"
        )
        reused = copy.deepcopy(target["contact_evidence"][0])
        reused["activation_ref"] = "new:webbed_sight_two"
        reused["contact_claim"] = second["mechanism"]
        target["activation_refs"].append("new:webbed_sight_two")
        target["contact_evidence"].append(reused)
        with self.assertRaisesRegex(ValidationError, "generic evidence support"):
            validate_adjudication_response(response, docket)

    def test_optional_selection_requires_interpretive_deletion_basis(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket)
        candidate = next(
            item
            for item in docket["candidates"]
            if item["obligation"] != "must_integrate"
            and item["source_type"] == "word_analysis"
            and not item["branch_refs"]
        )
        select_optional_decision(
            response,
            candidate["candidate_id"],
            suffix="yerel_aday",
            deletion_loss=(
                "Bu aday güvenilir ve citable oldugu icin yorumda tutulmalidir."
            ),
        )
        with self.assertRaisesRegex(ValidationError, "provenance eligibility"):
            validate_adjudication_response(response, docket)

    def test_optional_rationale_cannot_be_provenance_only(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket)
        candidates = {
            item["candidate_id"]: item for item in docket["candidates"]
        }
        decision = next(
            item
            for item in response["decisions"]
            if candidates[item["candidate_id"]]["obligation"] != "must_integrate"
        )
        decision["rationale"] = "Bu aday yalnız güvenilir ve uyumlu destek taşır."
        with self.assertRaisesRegex(ValidationError, "provenance eligibility"):
            validate_adjudication_response(response, docket)

    def test_distinct_optional_cannot_restate_mandatory_claim(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket)
        mandatory_claim = next(
            item["synthesis_claim"]
            for item in response["decisions"]
            if item["status"] == "selected"
        )
        candidate = next(
            item
            for item in docket["candidates"]
            if item["obligation"] != "must_integrate"
            and item["source_type"] == "word_analysis"
            and not item["branch_refs"]
        )
        select_optional_decision(
            response,
            candidate["candidate_id"],
            suffix="mandatory_repeat",
            claim=mandatory_claim.upper().replace(" ", "  "),
        )
        with self.assertRaisesRegex(ValidationError, "duplicate synthesis claims"):
            validate_adjudication_response(response, docket)

    def test_optional_selection_rejects_duplicate_claims_and_deletion_losses(self) -> None:
        docket = fixture_docket()
        optional = [
            item
            for item in docket["candidates"]
            if item["obligation"] != "must_integrate"
            and item["source_type"] == "word_analysis"
            and not item["branch_refs"]
        ]
        response = response_for_docket(docket)
        for index, candidate in enumerate(optional[:2]):
            select_optional_decision(
                response,
                candidate["candidate_id"],
                suffix=f"aday_{index}",
                claim="Ayni sinirli yorum sonucu.",
            )
        with self.assertRaisesRegex(ValidationError, "duplicate synthesis claims"):
            validate_adjudication_response(response, docket)

        response = response_for_docket(docket)
        repeated_loss = (
            "Bu iki adaydan biri silinirse ayni yorum sonucu metinden kaybolur."
        )
        for index, candidate in enumerate(optional[:2]):
            select_optional_decision(
                response,
                candidate["candidate_id"],
                suffix=f"aday_{index}",
                claim=(
                    "Ilk aday eylemin yerel sonucunu belirginlestirir."
                    if index == 0
                    else "Ikinci aday komsu rota imgesinin yapisini acar."
                ),
                deletion_loss=repeated_loss,
            )
        with self.assertRaisesRegex(ValidationError, "duplicate deletion losses"):
            validate_adjudication_response(response, docket)

    def test_selected_candidate_cannot_subsume_another_selection(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket)
        mandatory_id = next(
            item["candidate_id"]
            for item in docket["candidates"]
            if item["obligation"] == "must_integrate"
        )
        candidate = next(
            item
            for item in docket["candidates"]
            if item["obligation"] != "must_integrate"
            and item["source_type"] == "word_analysis"
            and not item["branch_refs"]
        )
        select_optional_decision(
            response,
            candidate["candidate_id"],
            suffix="subsumption",
            subsumes_candidate_ids=[mandatory_id],
        )
        with self.assertRaisesRegex(ValidationError, "subsumes selected candidates"):
            validate_adjudication_response(response, docket)

    def test_selected_candidate_handoff_has_a_hard_limit(self) -> None:
        bundle = fixture_bundle_for_docket()
        topics = bundle["word_analysis"]["words"][0]["topics"]
        for index in range(62):
            topics.append(
                {
                    "topic_id": f"29:38:1:optional-{index}",
                    "headline": f"Optional reading {index}",
                    "status": "used",
                    "reader_payoff": f"Distinct payoff {index}.",
                    "reason": f"Distinct local reason {index}.",
                    "commentary_obligation": "ledger_only",
                    "representative_source_ids": [f"Q{index}"],
                }
            )
        _prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(
                hft_policy="quarantine", max_optional_candidates=80
            ),
        )
        response = response_for_docket(docket)
        for index, candidate in enumerate(docket["candidates"]):
            if (
                candidate["obligation"] != "must_integrate"
                and candidate["source_type"] == "word_analysis"
            ):
                select_optional_decision(
                    response,
                    candidate["candidate_id"],
                    suffix=f"secim_{index}",
                )
        with self.assertRaisesRegex(ValidationError, "hard synthesis handoff limit"):
            validate_adjudication_response(response, docket)

    def test_nominated_branches_are_reviewed_and_contact_grounded(self) -> None:
        bundle = fixture_bundle_for_docket()
        bundle["branch_inventories"] = {
            "full_context_packet": {
                "source_file": "fixture-branches.json",
                "branch_inventories": [
                    {
                        "root": "ب ي ت",
                        "branches": [
                            {
                                "branch_id": "B007",
                                "image_en": "woven shelter",
                                "scope_en": "shelter imagery where attested",
                                "variants": [
                                    {
                                        "root_id": "root_009999",
                                        "image_en": "woven shelter",
                                        "scope_en": "shelter imagery where attested",
                                    }
                                ],
                            }
                        ],
                    }
                ],
            }
        }
        bundle["channel_subchannels_anchored_here"][0]["active_motifs"] = (
            "a shelter `quranic:root_009999:B007/m01`"
        )
        _prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(
                hft_policy="quarantine", max_support_per_candidate=6
            ),
        )
        self.assertEqual(
            [item["branch_ref"] for item in docket["nominated_branch_registry"]],
            ["root_009999/B007"],
        )
        response = response_for_docket(docket, include_new=True)
        proposal = response["new_candidates"][0]
        proposal["branch_refs"].append("root_009999/B007")
        supports = {
            item["support_id"]: item for item in docket["support_registry"]
        }
        used_contact_supports = {
            contact["support_id"]
            for item in response["branch_review"]
            for contact in item["contact_evidence"]
            if contact["activation_ref"] == "new:webbed_sight"
        }
        contact_support = next(
            support["support_id"]
            for support in supports.values()
            if support["role"] == "candidate_evidence"
            and support["scope"] == "macro"
            and not support["branch_refs"]
            and support["support_id"] not in used_contact_supports
        )
        nominated = next(
            item
            for item in response["branch_review"]
            if item["branch_ref"] == "root_009999/B007"
        )
        nomination_support = next(
            support_id
            for support_id in nominated["support_ids"]
            if supports[support_id]["role"] == "branch_nomination"
        )
        proposal["support_ids"] = sorted(
            {*proposal["support_ids"], contact_support, nomination_support}
        )
        contact_claim = (
            "root_009999/B007 woven shelter: komsu barinak imgesi secili "
            "onerideki yapisal temasa sinirli olarak katilir."
        )
        proposal["mechanism"] += " " + contact_claim
        nominated.update(
            status="activated",
            activation_refs=["new:webbed_sight"],
            reason_code="supported_activation",
            reason=(
                "root_009999/B007 woven shelter: Komsu barinak imgesi secili "
                "onerideki yapisal temasa sinirli olarak katilir."
            ),
            support_ids=sorted(
                {nomination_support, contact_support}
            ),
            unactivation_basis=None,
            contact_evidence=[
                {
                    "activation_ref": "new:webbed_sight",
                    "support_id": contact_support,
                    "quote": supports[contact_support]["text"][:120],
                    "contact_mode": "bounded_inference",
                    "contact_claim": contact_claim,
                }
            ],
        )
        artifact = validate_adjudication_response(response, docket)
        self.assertEqual(artifact["coverage"]["reviewed_nominated_branch_count"], 1)
        self.assertEqual(artifact["coverage"]["activated_nominated_branch_count"], 1)

        incomplete = copy.deepcopy(response)
        incomplete["branch_review"].pop()
        with self.assertRaisesRegex(ValidationError, "focus and nominated branch"):
            validate_adjudication_response(incomplete, docket)

    def test_branch_activation_requires_selected_candidate_lineage(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket)
        target = next(
            item
            for item in response["branch_review"]
            if item["branch_ref"] == "root_000672/B010"
        )
        target["reason"] = "not selected"
        with self.assertRaisesRegex(ValidationError, "24-400"):
            validate_adjudication_response(response, docket)

        response = response_for_docket(docket)
        target = next(
            item
            for item in response["branch_review"]
            if item["branch_ref"] == "root_000672/B010"
        )
        target["reason"] = (
            "Paket bu yan dali odak veya komsu imgeyle gerekceli bicimde "
            "etkinlestirmez."
        )
        with self.assertRaisesRegex(ValidationError, "registered descriptor"):
            validate_adjudication_response(response, docket)

        response = response_for_docket(docket)
        target = next(
            item
            for item in response["branch_review"]
            if item["branch_ref"] == "root_000672/B010"
        )
        target_gloss = next(
            branch["gloss"]
            for root in docket["branch_registry"]
            for branch in root["branches"]
            if branch["branch_ref"] == target["branch_ref"]
        )
        target.update(
            status="activated",
            activation_refs=["new:missing_proposal"],
            reason_code="supported_activation",
            reason=(
                f"{target['branch_ref']} {target_gloss}: Eksik bir oneriyi "
                "etkinlestirmeye calisir."
            ),
            unactivation_basis=None,
        )
        with self.assertRaisesRegex(ValidationError, "unknown or unselected"):
            validate_adjudication_response(response, docket)

    def test_unactivated_branch_requires_a_source_owned_basis(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket)
        target = next(
            item
            for item in response["branch_review"]
            if item["branch_ref"] == "root_000672/B010"
        )

        missing = copy.deepcopy(response)
        next(
            item
            for item in missing["branch_review"]
            if item["branch_ref"] == target["branch_ref"]
        )["unactivation_basis"] = None
        with self.assertRaisesRegex(ValidationError, "unactivation_basis must be an object"):
            validate_adjudication_response(missing, docket)

        generic = copy.deepcopy(response)
        generic_target = next(
            item
            for item in generic["branch_review"]
            if item["branch_ref"] == target["branch_ref"]
        )
        descriptor = next(
            branch["gloss"]
            for root in docket["branch_registry"]
            for branch in root["branches"]
            if branch["branch_ref"] == target["branch_ref"]
        )
        generic_target["reason"] = (
            f"{descriptor}: Paket bu dali desteklenen bir temas olarak etkinlestirmez."
        )
        with self.assertRaisesRegex(ValidationError, "canonical ref"):
            validate_adjudication_response(generic, docket)

        root_word_ref = next(
            candidate["anchor_refs"][0]
            for candidate in docket["candidates"]
            if candidate["source_type"] == "qac_morpheme"
            and "root_000672" in candidate["root_ids"]
        )
        evidence_owner = next(
            candidate
            for candidate in docket["candidates"]
            if candidate["source_type"] == "word_analysis"
            and candidate["anchor_refs"] == [root_word_ref]
        )
        evidence_support = next(
            support
            for support in docket["support_registry"]
            if support["support_id"] in evidence_owner["support_ids"]
            and "/topics/" in support["json_pointer"]
        )
        grounding_candidate_ids = target["unactivation_basis"]["candidate_ids"]
        target["support_ids"] = sorted(
            {*target["support_ids"], evidence_support["support_id"]}
        )
        target["reason_code"] = "insufficient_evidence"
        target["reason"] = (
            f"{target['branch_ref']} {descriptor}: {evidence_support['text'][:80]} "
            "metni bu yan dala ozgu temasi kurmaya yetmez."
        )[:400]
        target["unactivation_basis"] = {
            "kind": "candidate_evidence_rejected",
            "candidate_ids": sorted(
                {*grounding_candidate_ids, evidence_owner["candidate_id"]}
            ),
            "support_ids": target["support_ids"],
        }
        artifact = validate_adjudication_response(response, docket)
        normalized = next(
            item
            for item in artifact["branch_review"]
            if item["branch_ref"] == target["branch_ref"]
        )
        self.assertEqual(
            normalized["unactivation_basis"]["kind"],
            "candidate_evidence_rejected",
        )

    def test_response_must_cover_every_candidate_exactly_once(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket)
        response["decisions"].pop()
        with self.assertRaisesRegex(ValidationError, "omitted"):
            validate_adjudication_response(response, docket)

        response = response_for_docket(docket)
        response["decisions"].append(copy.deepcopy(response["decisions"][0]))
        with self.assertRaisesRegex(ValidationError, "duplicate"):
            validate_adjudication_response(response, docket)

    def test_must_integrate_cannot_be_rejected(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket)
        selected = next(item for item in response["decisions"] if item["status"] == "selected")
        selected.update(
            status="rejected",
            priority=None,
            synthesis_claim=None,
            reader_payoff=None,
            containment=None,
            selection_basis=None,
        )
        with self.assertRaisesRegex(ValidationError, "must_integrate"):
            validate_adjudication_response(response, docket)

    def test_unknown_support_and_candidate_branch_injection_fail(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket)
        response["decisions"][0]["support_ids"] = ["sup_00000000000000000000"]
        with self.assertRaisesRegex(ValidationError, "unknown supports"):
            validate_adjudication_response(response, docket)

        response = response_for_docket(docket)
        response["decisions"][0]["branch_refs"] = ["root_000672/B010"]
        with self.assertRaisesRegex(ValidationError, "outside its candidate"):
            validate_adjudication_response(response, docket)

    def test_branch_nomination_may_be_selected_without_activation(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket)
        candidate = next(item for item in docket["candidates"] if item["branch_refs"])
        decision = next(
            item for item in response["decisions"] if item["candidate_id"] == candidate["candidate_id"]
        )
        decision.update(
            status="selected",
            priority="supporting",
            synthesis_claim="Dal deliline bagli sinirli okuma.",
            reader_payoff="Okur dal mekanizmasini gorur.",
            containment="Dal yerel anlami degistirmez.",
            selection_basis={
                "kind": "distinct",
                "deletion_loss": (
                    "Bu aday silinirse dal mekanizmasinin ayri yorum katkisi "
                    "metinden kaybolur."
                ),
                "subsumes_candidate_ids": [],
            },
            branch_refs=[],
        )
        artifact = validate_adjudication_response(response, docket)
        normalized = next(
            item
            for item in artifact["decisions"]
            if item["candidate_id"] == candidate["candidate_id"]
        )
        self.assertEqual(normalized["branch_refs"], [])

    def test_structured_publication_anchor_can_activate_existing_branch(self) -> None:
        bundle = fixture_bundle_for_docket()
        bundle["v12_cross_run_publication"] = {
            "ayah_ref": "29:38",
            "findings": [
                {
                    "text": "Worked-road publication finding.",
                    "grade": "strong",
                    "anchors": [["29:38:1", "root_001046", ["B011"]]],
                }
            ],
        }
        _prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        response = response_for_docket(docket)
        publication = next(
            item
            for item in docket["candidates"]
            if item["source_type"] == "cross_run_publication"
        )
        decision = select_optional_decision(
            response,
            publication["candidate_id"],
            suffix="structured_publication",
        )
        branch_ref = "root_001046/B011"
        decision["branch_refs"] = [branch_ref]
        support_id = decision["support_ids"][0]
        support = next(
            item for item in docket["support_registry"] if item["support_id"] == support_id
        )
        descriptor = next(
            branch["gloss"]
            for root in docket["branch_registry"]
            for branch in root["branches"]
            if branch["branch_ref"] == branch_ref
        )
        target = next(
            item for item in response["branch_review"] if item["branch_ref"] == branch_ref
        )
        target.update(
            status="activated",
            activation_refs=[publication["candidate_id"]],
            reason_code="supported_activation",
            reason=(
                f"{branch_ref} {descriptor}: yapilandirilmis yayin ankraji dali "
                "acikca tasir."
            ),
            support_ids=sorted({*target["support_ids"], support_id}),
            unactivation_basis=None,
            contact_evidence=[
                {
                    "activation_ref": publication["candidate_id"],
                    "support_id": support_id,
                    "quote": support["text"][:120],
                    "contact_mode": "source_explicit",
                    "contact_claim": (
                        f"{branch_ref} {descriptor}: yapilandirilmis yayin ankraji "
                        "bu dali acikca tasir."
                    ),
                }
            ],
        )
        artifact = validate_adjudication_response(response, docket)
        activated = next(
            item for item in artifact["branch_review"] if item["branch_ref"] == branch_ref
        )
        self.assertEqual(activated["status"], "activated")
        self.assertEqual(
            activated["contact_evidence"][0]["contact_mode"], "source_explicit"
        )

    def test_legacy_selection_is_audit_only(self) -> None:
        docket = fixture_docket(legacy_hft=True)
        response = response_for_docket(docket)
        hft_candidate = next(item for item in docket["candidates"] if item["source_type"] == "hft")
        decision = next(
            item for item in response["decisions"] if item["candidate_id"] == hft_candidate["candidate_id"]
        )
        decision.update(
            status="selected",
            priority="supporting",
            synthesis_claim="Sinirli HFT iddiasi.",
            reader_payoff="Okur yerel gerilimi gorur.",
            containment="Tek basina kanit sayilmaz.",
            selection_basis={
                "kind": "distinct",
                "deletion_loss": (
                    "Bu aday silinirse HFT iliskisinin sinirli yorum sonucu "
                    "metinden kaybolur."
                ),
                "subsumes_candidate_ids": [],
            },
            branch_refs=[],
        )
        with self.assertRaisesRegex(ValidationError, "audit-only"):
            validate_adjudication_response(response, docket)

    def test_mandatory_claims_are_also_deduplicated(self) -> None:
        bundle = fixture_bundle_for_docket()
        second = copy.deepcopy(bundle["word_analysis"]["words"][1]["topics"][0])
        second.update(
            topic_id="29:38:2:second-mandatory",
            headline="Second mandatory local reading",
            commentary_obligation="must_integrate",
        )
        bundle["word_analysis"]["words"][1]["topics"].append(second)
        _prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        response = response_for_docket(docket)
        selected = [item for item in response["decisions"] if item["status"] == "selected"]
        selected[1]["synthesis_claim"] = selected[0]["synthesis_claim"]
        selected[1]["selection_basis"]["deletion_loss"] = selected[0][
            "selection_basis"
        ]["deletion_loss"]
        with self.assertRaisesRegex(ValidationError, "duplicate synthesis claims"):
            validate_adjudication_response(response, docket)

    def test_new_candidate_scope_and_grounding_are_enforced(self) -> None:
        docket = fixture_docket()
        response = response_for_docket(docket, include_new=True)
        proposal = response["new_candidates"][0]
        proposal["anchor_refs"] = ["29:38", "29:45"]
        with self.assertRaisesRegex(ValidationError, "pericope neighbor"):
            validate_adjudication_response(response, docket)

        response = response_for_docket(docket, include_new=True)
        response["new_candidates"][0]["branch_refs"] = ["root_999999/B999"]
        with self.assertRaisesRegex(ValidationError, "unknown or no branches"):
            validate_adjudication_response(response, docket)

    def test_blocked_docket_cannot_render(self) -> None:
        bundle = fixture_bundle()
        bundle["root_lexicon"]["root_000121"]["dictionary_entry"] = None
        _prepared, docket = build_prepared_artifacts(
            bundle,
            source_path=Path("fixture.json"),
            options=PrepareOptions(hft_policy="quarantine"),
        )
        self.assertFalse(docket["adjudication_gate"]["ready"])
        with self.assertRaisesRegex(ValidationError, "Blocked docket"):
            render_adjudication_prompt(docket)


if __name__ == "__main__":
    unittest.main()
