"""Render and validate the single model adjudication stage."""

from __future__ import annotations

import copy
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .common import (
    BudgetError,
    INPUTS_ROOT,
    OUTPUTS_ROOT,
    V3_ROOT,
    ValidationError,
    canonical_json_bytes,
    canonical_sha256,
    contains_apparatus_id,
    confined_existing_file,
    load_json_object,
    load_json_object_bounded,
    preflight_confined_writes,
    pretty_json_bytes,
    sha256_bytes,
    validate_exact_prompt_files,
    write_bytes_confined,
    write_json_confined,
)
from .prepare import (
    PrepareOptions,
    SUPPORT_ROLE_EVIDENCE,
    SUPPORT_ROLE_NOMINATION,
    SUPPORT_ROLE_OCCURRENCE,
    WORD_TOPIC_SOURCE_POINTER_RE,
    build_prepared_artifacts,
    validate_docket,
    validate_prepared,
)


RESPONSE_SCHEMA = "commentary-v3-adjudication-response-v2"
VALIDATED_SCHEMA = "commentary-v3-adjudication-validated-v2"
PROMPT_MANIFEST_SCHEMA = "commentary-v3-adjudication-prompt-manifest-v2"
REF_RE = re.compile(r"^([1-9][0-9]*):([1-9][0-9]*)$")
PROPOSAL_KEY_RE = re.compile(r"^[a-z][a-z0-9_-]{2,63}$")
NEW_ACTIVATION_REF_RE = re.compile(r"^new:([a-z][a-z0-9_-]{2,63})$")
ACTIVATION_REF_RE = re.compile(
    r"^(?:cand_[0-9a-f]{20}|new:[a-z][a-z0-9_-]{2,63})$"
)
BRANCH_REVIEW_REASON_MIN_CHARS = 24
BRANCH_REVIEW_REASON_MAX_CHARS = 400
CONTACT_QUOTE_MIN_CHARS = 12
CONTACT_QUOTE_MAX_CHARS = 320
CONTACT_CLAIM_MIN_CHARS = 24
CONTACT_CLAIM_MAX_CHARS = 500
SELECTION_BASIS_MIN_CHARS = 24
SELECTION_BASIS_MAX_CHARS = 400
EXCLUSION_RATIONALE_MIN_CHARS = 48
EXCLUSION_RATIONALE_MAX_CHARS = 1_200
SELECTION_SAFETY_CEILING = 512
ADJUDICATION_RESPONSE_SAFETY_CEILING = 32_000_000
CONTACT_MODE_SOURCE_EXPLICIT = "source_explicit"
CONTACT_MODE_BOUNDED_INFERENCE = "bounded_inference"
ACTIVATED_REASON_CODE = "supported_activation"
UNACTIVATED_REASON_CODES = {
    "no_supported_contact",
    "insufficient_evidence",
    "scope_blocked",
    "lexical_overreach",
}
UNACTIVATION_BASIS_KINDS = {"grounding_only", "candidate_evidence_rejected"}
EXCLUSION_REASON_CODES = {
    "unsupported",
    "unsafe",
    "out_of_scope",
    "semantic_duplicate",
}
ELIGIBILITY_TERMS = {
    "trusted", "citable", "compatible", "admissible", "eligible", "provenance",
    "guvenilir", "alintilanabilir", "uyumlu", "uygun", "gecerli",
}
ELIGIBILITY_BOILERPLATE = ELIGIBILITY_TERMS | {
    "a", "aday", "adayi", "adayin", "and", "as", "because", "bu", "bir",
    "carries", "delil", "destek", "evidence", "has", "icin", "ile", "is",
    "it", "kanit", "kaynak", "merely", "only", "or", "olarak", "sadece",
    "sirf", "source", "support", "tasir", "the", "this", "tutulmalidir",
    "ve", "veya", "yalniz", "yorumda", "oldugu",
}


@dataclass(frozen=True)
class AdjudicationOptions:
    max_prompt_bytes: int = 750_000

    def validate(self) -> None:
        if (
            not isinstance(self.max_prompt_bytes, int)
            or isinstance(self.max_prompt_bytes, bool)
            or self.max_prompt_bytes <= 0
        ):
            raise ValidationError("max_prompt_bytes must be a positive integer")


def _require_dict(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValidationError(f"{label} must be an object")
    return value


def _require_list(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        raise ValidationError(f"{label} must be an array")
    return value


def _require_exact_keys(value: dict[str, Any], expected: set[str], label: str) -> None:
    actual = set(value)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise ValidationError(
            f"{label} fields disagree with contract; missing={missing}, extra={extra}"
        )


def _require_text(value: Any, label: str, *, allow_null: bool = False) -> str | None:
    if allow_null and value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{label} must be a nonempty string")
    return " ".join(value.split())


def _require_reader_text(value: Any, label: str) -> str:
    text = _require_text(value, label)
    assert text is not None
    if contains_apparatus_id(text):
        raise ValidationError(
            f"{label} leaks apparatus identifiers into required synthesis prose"
        )
    return text


def _require_string_list(value: Any, label: str) -> list[str]:
    items = _require_list(value, label)
    if any(not isinstance(item, str) or not item for item in items):
        raise ValidationError(f"{label} must contain only nonempty strings")
    if len(set(items)) != len(items):
        raise ValidationError(f"{label} must not contain duplicates")
    return items


def _comparison_words(value: str) -> list[str]:
    folded = unicodedata.normalize(
        "NFKD", value.casefold().replace("ı", "i")
    )
    ascii_folded = "".join(
        character for character in folded if not unicodedata.combining(character)
    )
    return re.findall(r"[a-z0-9\u0621-\u064a]+", ascii_folded)


def _is_eligibility_only(value: str) -> bool:
    words = _comparison_words(value)
    return bool(set(words) & ELIGIBILITY_TERMS) and set(words) <= (
        ELIGIBILITY_BOILERPLATE
    )


def _new_candidate_capacity(selected_existing_count: int) -> int:
    if (
        not isinstance(selected_existing_count, int)
        or isinstance(selected_existing_count, bool)
        or selected_existing_count < 0
    ):
        raise ValidationError("selected_existing_count must be a nonnegative integer")
    capacity = SELECTION_SAFETY_CEILING - selected_existing_count
    if capacity < 0:
        raise BudgetError(
            f"Adjudication selected {selected_existing_count} existing candidates; fail-loud safety "
            f"ceiling is {SELECTION_SAFETY_CEILING}. Nothing was pruned."
        )
    return capacity


def _reader_contribution_key(
    *, claim: str, reader_payoff: str, containment: str, deletion_loss: str
) -> tuple[str, str, str, str]:
    """Identify only byte-equivalent reader contributions, never near matches."""
    return claim, reader_payoff, containment, deletion_loss


def _selection_basis(
    value: Any,
    *,
    label: str,
    expected_kind: str,
    known_candidate_ids: set[str],
    own_candidate_id: str | None = None,
) -> dict[str, Any]:
    basis = _require_dict(value, label)
    _require_exact_keys(
        basis, {"kind", "deletion_loss", "subsumes_candidate_ids"}, label
    )
    if basis.get("kind") != expected_kind:
        raise ValidationError(f"{label} kind must be {expected_kind}")
    deletion_loss = _require_text(basis.get("deletion_loss"), f"{label} deletion_loss")
    if not SELECTION_BASIS_MIN_CHARS <= len(deletion_loss) <= SELECTION_BASIS_MAX_CHARS:
        raise ValidationError(
            f"{label} deletion_loss must contain {SELECTION_BASIS_MIN_CHARS}-"
            f"{SELECTION_BASIS_MAX_CHARS} characters"
        )
    if expected_kind == "distinct" and _is_eligibility_only(deletion_loss):
        raise ValidationError(
            f"{label} deletion_loss may not use provenance eligibility as its basis"
        )
    subsumes = _require_string_list(
        basis.get("subsumes_candidate_ids"), f"{label} subsumes_candidate_ids"
    )
    if set(subsumes) - known_candidate_ids or own_candidate_id in subsumes:
        raise ValidationError(f"{label} subsumes unknown or self candidate IDs")
    if subsumes:
        raise ValidationError(
            f"{label} may not subsume candidates in the exhaustive admission contract"
        )
    return {
        "kind": expected_kind,
        "deletion_loss": deletion_loss,
        "subsumes_candidate_ids": sorted(subsumes),
    }


def _support_quote(
    value: Any,
    *,
    label: str,
    allowed_support_ids: set[str],
    support_registry: dict[str, dict[str, Any]],
) -> dict[str, str]:
    quote_record = _require_dict(value, label)
    _require_exact_keys(quote_record, {"support_id", "quote"}, label)
    support_id = quote_record.get("support_id")
    if not isinstance(support_id, str) or support_id not in allowed_support_ids:
        raise ValidationError(f"{label} cites support outside the selected evidence")
    support = support_registry[support_id]
    if (
        support["trust"] != "trusted"
        or support["citable"] is not True
        or support["role"] != SUPPORT_ROLE_EVIDENCE
    ):
        raise ValidationError(f"{label} must cite trusted candidate evidence")
    quote = _require_text(quote_record.get("quote"), f"{label} quote")
    if not CONTACT_QUOTE_MIN_CHARS <= len(quote) <= CONTACT_QUOTE_MAX_CHARS:
        raise ValidationError(
            f"{label} quote must contain {CONTACT_QUOTE_MIN_CHARS}-"
            f"{CONTACT_QUOTE_MAX_CHARS} characters"
        )
    if quote not in support["text"]:
        raise ValidationError(f"{label} quote is not an exact support excerpt")
    if sum(character.isalpha() for character in quote) < 8:
        raise ValidationError(f"{label} quote lacks explanatory text")
    return {"support_id": support_id, "quote": quote}


def _parse_ayah_ref(value: Any, label: str) -> tuple[int, int]:
    if not isinstance(value, str):
        raise ValidationError(f"{label} must be an ayah ref string")
    match = REF_RE.fullmatch(value)
    if not match:
        raise ValidationError(f"{label} is not an ayah ref: {value!r}")
    return int(match.group(1)), int(match.group(2))


def _artifact_relatives(ayah_ref: str) -> dict[str, Path]:
    surah, ayah = _parse_ayah_ref(ayah_ref, "ayah_ref")
    stem = f"{surah}_{ayah}"
    folder = Path(f"s{surah:03d}")
    return {
        "source": Path("source") / folder / f"{stem}.bundle.json",
        "prepared": Path("prepared") / folder / f"{stem}.prepared.json",
        "docket": Path("adjudication") / folder / f"{stem}.docket.json",
        "prompt": Path("adjudication") / folder / f"{stem}.prompt.md",
        "prompt_manifest": Path("adjudication") / folder / f"{stem}.prompt.json",
        "response": Path("adjudication") / folder / f"{stem}.response.json",
        "validated": Path("adjudication") / folder / f"{stem}.adjudication.json",
    }


def load_docket_for_ayah(
    ayah_ref: str,
    *,
    prepare_options: PrepareOptions | None = None,
) -> tuple[dict[str, Any], Path]:
    expected_options = prepare_options or PrepareOptions()
    expected_options.validate()
    relatives = _artifact_relatives(ayah_ref)
    path = confined_existing_file(INPUTS_ROOT, relatives["docket"])
    docket, _raw = load_json_object(path)
    validate_docket(docket)
    if docket.get("identity", {}).get("ayah_ref") != ayah_ref:
        raise ValidationError("Docket ayah identity disagrees with requested ayah")

    prepared_path = confined_existing_file(INPUTS_ROOT, relatives["prepared"])
    prepared, _prepared_raw = load_json_object(prepared_path)
    source_path = confined_existing_file(INPUTS_ROOT, relatives["source"])
    source, source_raw = load_json_object(source_path)
    validate_prepared(
        prepared,
        docket,
        source_bundle=source,
        source_raw=source_raw,
        options=expected_options,
    )
    source_identity = _require_dict(
        prepared.get("identity", {}).get("source"), "prepared source identity"
    )
    if sha256_bytes(source_raw) != source_identity.get("raw_sha256"):
        raise ValidationError("Source snapshot raw hash disagrees with prepared artifact")
    if canonical_sha256(source) != source_identity.get("canonical_sha256"):
        raise ValidationError(
            "Source snapshot canonical hash disagrees with prepared artifact"
        )
    if source_identity.get("canonical_sha256") != docket["identity"].get(
        "source_canonical_sha256"
    ):
        raise ValidationError("Source snapshot hash disagrees with docket")
    if source_identity.get("ayah_ref") != ayah_ref:
        raise ValidationError("Source snapshot ayah identity disagrees with request")
    if source.get("ayahRef") != ayah_ref:
        raise ValidationError("Source snapshot bundle identity disagrees with request")

    rebuilt_prepared, rebuilt_docket = build_prepared_artifacts(
        source,
        source_path=source_path,
        source_raw=source_raw,
        options=expected_options,
    )
    if rebuilt_docket != docket:
        raise ValidationError("Docket does not deterministically rederive from source")
    if rebuilt_prepared != prepared:
        raise ValidationError(
            "Prepared artifact does not deterministically rederive from source"
        )

    gate = _require_dict(docket.get("adjudication_gate"), "adjudication_gate")
    if not gate.get("ready"):
        detail = "; ".join(gate.get("blockers") or ["unspecified blocker"])
        raise ValidationError(f"Docket is blocked from adjudication: {detail}")
    return docket, path


def _render_adjudication_prompt_unbound(
    docket: dict[str, Any],
    *,
    options: AdjudicationOptions | None = None,
    template: str | None = None,
) -> tuple[str, dict[str, Any]]:
    options = options or AdjudicationOptions()
    options.validate()
    validate_docket(docket)
    gate = _require_dict(docket.get("adjudication_gate"), "adjudication_gate")
    if not gate.get("ready"):
        raise ValidationError("Blocked docket cannot be rendered for adjudication")
    if template is None:
        template_path = V3_ROOT / "prompts" / "adjudication.md"
        try:
            template = template_path.read_text(encoding="utf-8")
        except OSError as exc:
            raise ValidationError(f"Cannot read adjudication prompt template: {exc}") from exc

    identity = _require_dict(docket.get("identity"), "docket identity")
    eligible_candidates = [
        candidate for candidate in docket["candidates"] if candidate["selection_eligible"]
    ]
    mandatory_selected = sum(candidate["mandatory"] for candidate in eligible_candidates)
    maximum_new_candidate_capacity = _new_candidate_capacity(mandatory_selected)
    registered_branch_count = sum(
        len(root["branches"]) for root in docket["branch_registry"]
    ) + len(docket["nominated_branch_registry"])
    neighbor_ref = next(
        (
            ref
            for ref in docket.get("scope", {}).get("pericope", {}).get("refs", [])
            if ref != identity["ayah_ref"]
        ),
        identity["ayah_ref"],
    )
    replacements = {
        "@@AYAH_REF@@": identity["ayah_ref"],
        "@@SOURCE_SHA256@@": identity["source_canonical_sha256"],
        "@@DOCKET_SHA256@@": identity["docket_payload_sha256"],
        "@@MAXIMUM_NEW_CANDIDATE_CAPACITY@@": str(maximum_new_candidate_capacity),
        "@@ELIGIBLE_CANDIDATE_COUNT@@": str(len(eligible_candidates)),
        "@@MANDATORY_SELECTED_COUNT@@": str(mandatory_selected),
        "@@SELECTION_SAFETY_CEILING@@": str(SELECTION_SAFETY_CEILING),
        "@@SUPPORT_REGISTRY_COUNT@@": str(len(docket["support_registry"])),
        "@@REGISTERED_BRANCH_COUNT@@": str(registered_branch_count),
        "@@PERICOPE_NEIGHBOR_REF@@": neighbor_ref,
        "@@DOCKET_JSON@@": canonical_json_bytes(docket).decode("utf-8"),
    }
    prompt = template
    for marker, replacement in replacements.items():
        if marker not in prompt:
            raise ValidationError(f"Adjudication prompt template lacks marker {marker}")
        prompt = prompt.replace(marker, replacement)
    unresolved = sorted(set(re.findall(r"@@[A-Z0-9_]+@@", prompt)))
    if unresolved:
        raise ValidationError(f"Unresolved adjudication prompt markers: {unresolved}")
    prompt_bytes = prompt.encode("utf-8")
    if len(prompt_bytes) > options.max_prompt_bytes:
        raise BudgetError(
            f"Adjudication prompt is {len(prompt_bytes)} bytes; limit is "
            f"{options.max_prompt_bytes}. Nothing was truncated."
        )
    manifest = {
        "schema_version": PROMPT_MANIFEST_SCHEMA,
        "identity": {
            "ayah_ref": identity["ayah_ref"],
            "source_canonical_sha256": identity["source_canonical_sha256"],
            "docket_payload_sha256": identity["docket_payload_sha256"],
            "prompt_sha256": sha256_bytes(prompt_bytes),
        },
        "budget": {
            "prompt_bytes": len(prompt_bytes),
            "estimated_tokens_chars_div_4": (len(prompt) + 3) // 4,
            "candidate_count": len(docket["candidates"]),
            "eligible_candidate_count": len(eligible_candidates),
            "mandatory_selected_count": mandatory_selected,
            "maximum_new_candidate_capacity": maximum_new_candidate_capacity,
            "selection_safety_ceiling": SELECTION_SAFETY_CEILING,
            "new_candidate_capacity_formula": (
                f"{SELECTION_SAFETY_CEILING} - selected_existing_count"
            ),
            "support_registry_count": len(docket["support_registry"]),
            "registered_branch_count": registered_branch_count,
        },
        "contract": {
            "response_schema_version": RESPONSE_SCHEMA,
            "every_selection_eligible_candidate_exactly_once": True,
            "selection_ineligible_candidates_have_no_model_decision": True,
            "every_discovered_candidate_or_loud_overflow": True,
            "every_focus_branch_exactly_once": True,
            "every_nominated_branch_exactly_once": True,
            "selection_safety_ceiling": SELECTION_SAFETY_CEILING,
            "expected_response": str(
                Path("outputs") / _artifact_relatives(identity["ayah_ref"])["response"]
            ),
        },
    }
    return prompt, manifest


def _require_persisted_docket_binding(
    docket: dict[str, Any], *, prepare_options: PrepareOptions | None
) -> None:
    ayah_ref = docket.get("identity", {}).get("ayah_ref")
    if not isinstance(ayah_ref, str):
        raise ValidationError("Source-bound docket lacks a valid ayah identity")
    try:
        persisted, _path = load_docket_for_ayah(
            ayah_ref, prepare_options=prepare_options
        )
    except ValidationError as exc:
        raise ValidationError(
            "Public adjudication handoff requires a persisted, source-rederived docket: "
            f"{exc}"
        ) from exc
    if persisted != docket:
        raise ValidationError(
            "Public adjudication handoff docket differs from its persisted source binding"
        )


def render_adjudication_prompt(
    docket: dict[str, Any],
    *,
    options: AdjudicationOptions | None = None,
    prepare_options: PrepareOptions | None = None,
) -> tuple[str, dict[str, Any]]:
    """Render only after the docket rederives from its retained source snapshot."""
    _require_persisted_docket_binding(docket, prepare_options=prepare_options)
    return _render_adjudication_prompt_unbound(docket, options=options)


def render_adjudication_for_ayah(
    ayah_ref: str,
    *,
    options: AdjudicationOptions | None = None,
    prepare_options: PrepareOptions | None = None,
    write: bool = True,
    force: bool = False,
) -> tuple[str, dict[str, Any], dict[str, str]]:
    docket, docket_path = load_docket_for_ayah(
        ayah_ref, prepare_options=prepare_options
    )
    prompt, manifest = render_adjudication_prompt(
        docket, options=options, prepare_options=prepare_options
    )
    relatives = _artifact_relatives(ayah_ref)
    paths = {
        "docket": str(docket_path),
        "prompt": str(INPUTS_ROOT / relatives["prompt"]),
        "prompt_manifest": str(INPUTS_ROOT / relatives["prompt_manifest"]),
        "expected_response": str(OUTPUTS_ROOT / relatives["response"]),
    }
    if write:
        payloads = {
            relatives["prompt"]: prompt.encode("utf-8"),
            relatives["prompt_manifest"]: pretty_json_bytes(manifest),
        }
        preflight_confined_writes(INPUTS_ROOT, payloads, replace=force)
        for relative in (relatives["prompt"], relatives["prompt_manifest"]):
            write_bytes_confined(
                INPUTS_ROOT,
                relative,
                payloads[relative],
                replace=force,
            )
    return prompt, manifest, paths


def _registered_branches(docket: dict[str, Any]) -> tuple[set[str], set[str]]:
    focus = {
        branch["branch_ref"]
        for root in docket["branch_registry"]
        for branch in root["branches"]
    }
    nominated = {
        branch["branch_ref"] for branch in docket["nominated_branch_registry"]
    }
    return focus, nominated


def _validate_identity(
    response: dict[str, Any],
    docket: dict[str, Any],
    *,
    prompt_sha256: str,
) -> None:
    identity = _require_dict(response.get("identity"), "response identity")
    _require_exact_keys(
        identity,
        {
            "ayah_ref",
            "source_canonical_sha256",
            "docket_payload_sha256",
            "prompt_sha256",
        },
        "response identity",
    )
    expected = docket["identity"]
    for field in ("ayah_ref", "source_canonical_sha256", "docket_payload_sha256"):
        if identity.get(field) != expected.get(field):
            raise ValidationError(f"Response identity {field} does not bind docket")
    if identity.get("prompt_sha256") != prompt_sha256:
        raise ValidationError("Response identity prompt_sha256 does not bind prompt")


def _validate_decisions(
    raw_decisions: Any,
    docket: dict[str, Any],
) -> list[dict[str, Any]]:
    decision_fields = {
        "candidate_id",
        "status",
        "priority",
        "rationale",
        "synthesis_claim",
        "reader_payoff",
        "containment",
        "selection_basis",
        "support_quote",
        "exclusion_basis",
        "support_ids",
        "branch_refs",
    }
    candidates = {
        item["candidate_id"]: item
        for item in docket["candidates"]
        if item["selection_eligible"]
    }
    support_registry = {item["support_id"]: item for item in docket["support_registry"]}
    focus_branches, nominated_branches = _registered_branches(docket)
    registered_branches = focus_branches | nominated_branches
    decisions_by_id: dict[str, dict[str, Any]] = {}
    received_order: list[str] = []
    for index, raw in enumerate(_require_list(raw_decisions, "decisions")):
        decision = _require_dict(raw, f"decisions[{index}]")
        _require_exact_keys(decision, decision_fields, f"decisions[{index}]")
        candidate_id = decision.get("candidate_id")
        if not isinstance(candidate_id, str) or candidate_id not in candidates:
            raise ValidationError(f"Decision references unknown candidate: {candidate_id!r}")
        if candidate_id in decisions_by_id:
            raise ValidationError(f"Candidate has duplicate decisions: {candidate_id}")
        received_order.append(candidate_id)
        candidate = candidates[candidate_id]
        status = decision.get("status")
        if not isinstance(status, str) or status not in (
            "selected",
            "rejected",
            "deferred",
        ):
            raise ValidationError(f"Decision {candidate_id} has invalid status")
        if candidate["mandatory"] and status != "selected":
            raise ValidationError(f"Mandatory candidate was not selected: {candidate_id}")
        rationale = _require_text(decision.get("rationale"), f"decision {candidate_id} rationale")
        if (
            candidate.get("obligation") != "must_integrate"
            and _is_eligibility_only(rationale)
        ):
            raise ValidationError(
                f"Decision {candidate_id} rationale may not state only provenance "
                "eligibility"
            )
        support_ids = _require_string_list(
            decision.get("support_ids"), f"decision {candidate_id} support_ids"
        )
        unknown_supports = set(support_ids) - set(support_registry)
        if unknown_supports:
            raise ValidationError(
                f"Decision {candidate_id} cites unknown supports: {sorted(unknown_supports)}"
            )
        if not set(support_ids) & set(candidate["support_ids"]):
            raise ValidationError(
                f"Decision {candidate_id} must cite at least one candidate-owned support"
            )
        extra_support_ids = set(support_ids) - set(candidate["support_ids"])
        branch_refs = _require_string_list(
            decision.get("branch_refs"), f"decision {candidate_id} branch_refs"
        )
        if not set(branch_refs) <= set(candidate["branch_refs"]):
            raise ValidationError(
                f"Decision {candidate_id} cites branches outside its candidate evidence"
            )
        if not set(branch_refs) <= registered_branches:
            raise ValidationError(f"Decision {candidate_id} cites unregistered branches")

        normalized = {
            "candidate_id": candidate_id,
            "status": status,
            "priority": decision.get("priority"),
            "rationale": rationale,
            "synthesis_claim": decision.get("synthesis_claim"),
            "reader_payoff": decision.get("reader_payoff"),
            "containment": decision.get("containment"),
            "selection_basis": decision.get("selection_basis"),
            "support_quote": decision.get("support_quote"),
            "exclusion_basis": decision.get("exclusion_basis"),
            "support_ids": sorted(support_ids),
            "branch_refs": sorted(branch_refs),
        }
        if status == "selected":
            if decision.get("exclusion_basis") is not None:
                raise ValidationError(
                    f"Selected decision {candidate_id} exclusion_basis must be null"
                )
            priority = decision.get("priority")
            if not isinstance(priority, str) or priority not in (
                "core",
                "supporting",
            ):
                raise ValidationError(f"Selected decision {candidate_id} needs priority")
            for field in ("synthesis_claim", "reader_payoff", "containment"):
                normalized[field] = _require_reader_text(
                    decision.get(field), f"selected decision {candidate_id} {field}"
                )
            basis_kind = (
                "mandatory" if candidate["mandatory"] else "distinct"
            )
            normalized["selection_basis"] = _selection_basis(
                decision.get("selection_basis"),
                label=f"selected decision {candidate_id} selection_basis",
                expected_kind=basis_kind,
                known_candidate_ids=set(candidates),
                own_candidate_id=candidate_id,
            )
            if extra_support_ids:
                raise ValidationError(
                    f"Trusted selection {candidate_id} cites support outside its "
                    "candidate evidence"
                )
            selected_supports = [support_registry[support_id] for support_id in support_ids]
            if any(
                support["trust"] != "trusted"
                or not support["citable"]
                or support["role"] != SUPPORT_ROLE_EVIDENCE
                for support in selected_supports
            ):
                raise ValidationError(
                    f"Selected decision {candidate_id} may expose only trusted, "
                    "citable candidate_evidence support to synthesis"
                )
            normalized["support_quote"] = _support_quote(
                decision.get("support_quote"),
                label=f"selected decision {candidate_id} support_quote",
                allowed_support_ids=set(support_ids),
                support_registry=support_registry,
            )
            unactivated_support_branches = sorted(
                {
                    branch_ref
                    for support in selected_supports
                    for branch_ref in support["branch_refs"]
                }
                - set(branch_refs)
            )
            if unactivated_support_branches:
                raise ValidationError(
                    f"Selected decision {candidate_id} exposes branch-bearing support "
                    "without activating its branches: "
                    f"{unactivated_support_branches}"
                )
        else:
            if extra_support_ids:
                raise ValidationError(
                    f"Non-selected decision {candidate_id} cites unrelated support"
                )
            if decision.get("priority") is not None:
                raise ValidationError(f"Non-selected decision {candidate_id} priority must be null")
            for field in ("synthesis_claim", "reader_payoff", "containment"):
                if decision.get(field) is not None:
                    raise ValidationError(
                        f"Non-selected decision {candidate_id} {field} must be null"
                    )
            if decision.get("selection_basis") is not None:
                raise ValidationError(
                    f"Non-selected decision {candidate_id} selection_basis must be null"
                )
            if branch_refs:
                raise ValidationError(
                    f"Non-selected decision {candidate_id} branch_refs must be empty"
                )
            if not (
                EXCLUSION_RATIONALE_MIN_CHARS
                <= len(rationale)
                <= EXCLUSION_RATIONALE_MAX_CHARS
            ):
                raise ValidationError(
                    f"Non-selected decision {candidate_id} rationale must contain "
                    f"{EXCLUSION_RATIONALE_MIN_CHARS}-"
                    f"{EXCLUSION_RATIONALE_MAX_CHARS} characters"
                )
            excluded_supports = [support_registry[support_id] for support_id in support_ids]
            if any(
                support["trust"] != "trusted"
                or not support["citable"]
                or support["role"] != SUPPORT_ROLE_EVIDENCE
                for support in excluded_supports
            ):
                raise ValidationError(
                    f"Non-selected decision {candidate_id} may cite only trusted, "
                    "citable candidate_evidence support"
                )
            normalized["support_quote"] = _support_quote(
                decision.get("support_quote"),
                label=f"non-selected decision {candidate_id} support_quote",
                allowed_support_ids=set(support_ids),
                support_registry=support_registry,
            )
            if normalized["support_quote"]["quote"] not in rationale:
                raise ValidationError(
                    f"Non-selected decision {candidate_id} rationale must contain "
                    "its exact support quote"
                )
            raw_exclusion = _require_dict(
                decision.get("exclusion_basis"),
                f"non-selected decision {candidate_id} exclusion_basis",
            )
            _require_exact_keys(
                raw_exclusion,
                {"reason_code", "duplicate_of_candidate_ids"},
                f"non-selected decision {candidate_id} exclusion_basis",
            )
            reason_code = raw_exclusion.get("reason_code")
            if not isinstance(reason_code, str) or reason_code not in EXCLUSION_REASON_CODES:
                raise ValidationError(
                    f"Non-selected decision {candidate_id} has invalid exclusion reason"
                )
            duplicate_of = _require_string_list(
                raw_exclusion.get("duplicate_of_candidate_ids"),
                f"non-selected decision {candidate_id} duplicate_of_candidate_ids",
            )
            if candidate_id in duplicate_of or set(duplicate_of) - set(candidates):
                raise ValidationError(
                    f"Non-selected decision {candidate_id} has invalid duplicate targets"
                )
            if reason_code == "semantic_duplicate":
                if not duplicate_of:
                    raise ValidationError(
                        f"Semantic duplicate {candidate_id} needs selected duplicate targets"
                    )
            elif duplicate_of:
                raise ValidationError(
                    f"Non-duplicate decision {candidate_id} cannot cite duplicate targets"
                )
            normalized["exclusion_basis"] = {
                "reason_code": reason_code,
                "duplicate_of_candidate_ids": sorted(duplicate_of),
            }
        decisions_by_id[candidate_id] = normalized

    missing = set(candidates) - set(decisions_by_id)
    extra = set(decisions_by_id) - set(candidates)
    if missing or extra:
        raise ValidationError(
            "Adjudication decision coverage disagrees with selection eligibility: "
            f"missing={sorted(missing)}, extra={sorted(extra)}"
        )
    expected_order = [
        item["candidate_id"]
        for item in docket["candidates"]
        if item["selection_eligible"]
    ]
    if received_order != expected_order:
        raise ValidationError(
            "Adjudication decisions must follow exact selection-eligible docket order"
        )
    normalized_decisions = [
        decisions_by_id[item["candidate_id"]]
        for item in docket["candidates"]
        if item["selection_eligible"]
    ]
    selected_ids = {
        item["candidate_id"]
        for item in normalized_decisions
        if item["status"] == "selected"
    }
    all_selected = [
        item for item in normalized_decisions if item["status"] == "selected"
    ]
    if len(all_selected) > SELECTION_SAFETY_CEILING:
        raise ValidationError(
            "Selected candidate count exceeds the fail-loud safety ceiling "
            f"{SELECTION_SAFETY_CEILING}"
        )
    for item in normalized_decisions:
        exclusion = item["exclusion_basis"]
        if exclusion is None or exclusion["reason_code"] != "semantic_duplicate":
            continue
        targets = exclusion["duplicate_of_candidate_ids"]
        if not set(targets) <= selected_ids:
            raise ValidationError(
                f"Semantic duplicate {item['candidate_id']} must link only selected targets"
            )
        missing_target_claims = [
            target_id
            for target_id in targets
            if decisions_by_id[target_id]["synthesis_claim"] not in item["rationale"]
        ]
        if missing_target_claims:
            raise ValidationError(
                f"Semantic duplicate {item['candidate_id']} rationale must quote the "
                f"exact selected target claims: {missing_target_claims}"
            )
        duplicate_candidate = candidates[item["candidate_id"]]
        covered_branches = {
            branch_ref
            for target_id in targets
            for branch_ref in decisions_by_id[target_id]["branch_refs"]
        }
        if not set(duplicate_candidate["branch_refs"]) <= covered_branches:
            raise ValidationError(
                f"Semantic duplicate {item['candidate_id']} loses branch lineage"
            )
    return normalized_decisions


def _validate_new_candidates(
    raw_candidates: Any,
    docket: dict[str, Any],
    decisions: list[dict[str, Any]],
    *,
    new_candidate_capacity: int,
) -> list[dict[str, Any]]:
    proposal_fields = {
        "proposal_key",
        "title",
        "lane",
        "scope",
        "claim",
        "mechanism",
        "reader_payoff",
        "containment",
        "selection_basis",
        "support_quote",
        "confidence",
        "anchor_refs",
        "support_ids",
        "branch_refs",
    }
    proposals = _require_list(raw_candidates, "new_candidates")
    if len(proposals) > new_candidate_capacity:
        raise ValidationError(
            f"New candidate count {len(proposals)} exceeds fail-loud remaining "
            f"capacity {new_candidate_capacity}"
        )
    identity = docket["identity"]
    focus_ref = identity["ayah_ref"]
    focus_surah, _focus_ayah = _parse_ayah_ref(focus_ref, "focus ayah")
    pericope_refs = set(docket["scope"]["pericope"]["refs"])
    support_registry = {item["support_id"]: item for item in docket["support_registry"]}
    focus_branches, nominated_branches = _registered_branches(docket)
    registered_branches = focus_branches | nominated_branches
    support_owners: dict[str, list[dict[str, Any]]] = {
        support_id: [
            candidate
            for candidate in docket["candidates"]
            if support_id in candidate["support_ids"]
        ]
        for support_id in support_registry
    }
    seen_keys: set[str] = set()
    seen_ids: set[str] = set()
    contribution_owners = {
        _reader_contribution_key(
            claim=decision["synthesis_claim"],
            reader_payoff=decision["reader_payoff"],
            containment=decision["containment"],
            deletion_loss=decision["selection_basis"]["deletion_loss"],
        ): decision["candidate_id"]
        for decision in decisions
        if decision["status"] == "selected"
    }
    decision_status = {item["candidate_id"]: item["status"] for item in decisions}
    normalized: list[dict[str, Any]] = []
    for index, raw in enumerate(proposals):
        proposal = _require_dict(raw, f"new_candidates[{index}]")
        _require_exact_keys(proposal, proposal_fields, f"new_candidates[{index}]")
        key = proposal.get("proposal_key")
        if not isinstance(key, str) or not PROPOSAL_KEY_RE.fullmatch(key):
            raise ValidationError(f"new candidate {index} has invalid proposal_key")
        if key in seen_keys:
            raise ValidationError(f"Duplicate new candidate proposal_key: {key}")
        seen_keys.add(key)
        lane = proposal.get("lane")
        proposal_scope = proposal.get("scope")
        expected_scopes = {
            "micro": {"focus_ayah"},
            "macro": {"pericope"},
            "global": {"surah", "cross_surah"},
        }
        if (
            not isinstance(lane, str)
            or lane not in expected_scopes
            or not isinstance(proposal_scope, str)
            or proposal_scope not in expected_scopes[lane]
        ):
            raise ValidationError(f"New candidate {key} lane/scope combination is invalid")
        confidence = proposal.get("confidence")
        if not isinstance(confidence, str) or confidence not in (
            "strong",
            "moderate",
            "exploratory",
        ):
            raise ValidationError(f"New candidate {key} confidence is invalid")
        text_fields = {
            field: _require_text(proposal.get(field), f"new candidate {key} {field}")
            for field in (
                "title",
                "claim",
                "mechanism",
                "reader_payoff",
                "containment",
            )
        }
        for field in ("claim", "reader_payoff", "containment"):
            text_fields[field] = _require_reader_text(
                proposal.get(field), f"new candidate {key} {field}"
            )
        selection_basis = _selection_basis(
            proposal.get("selection_basis"),
            label=f"new candidate {key} selection_basis",
            expected_kind="distinct",
            known_candidate_ids=set(decision_status),
        )
        anchor_refs = _require_string_list(
            proposal.get("anchor_refs"), f"new candidate {key} anchor_refs"
        )
        parsed_anchors = [
            (_parse_ayah_ref(ref, f"new candidate {key} anchor"), ref)
            for ref in anchor_refs
        ]
        if focus_ref not in anchor_refs:
            raise ValidationError(f"New candidate {key} does not anchor the focus ayah")
        if lane == "micro" and set(anchor_refs) != {focus_ref}:
            raise ValidationError(f"Micro new candidate {key} has non-focus anchors")
        if lane == "macro":
            if not set(anchor_refs) <= pericope_refs or set(anchor_refs) == {focus_ref}:
                raise ValidationError(
                    f"Macro new candidate {key} must use focus plus pericope neighbor anchors"
                )
        if lane == "global" and proposal["scope"] == "surah":
            if any(surah != focus_surah for (surah, _ayah), _ref in parsed_anchors):
                raise ValidationError(f"Surah new candidate {key} crosses surah boundary")

        support_ids = _require_string_list(
            proposal.get("support_ids"), f"new candidate {key} support_ids"
        )
        if set(support_ids) - set(support_registry):
            raise ValidationError(f"New candidate {key} cites unknown supports")
        support_items = [support_registry[support_id] for support_id in support_ids]
        cited_owners = {
            candidate["candidate_id"]: candidate
            for support_id in support_ids
            for candidate in support_owners[support_id]
        }.values()
        if any(
            item["trust"] != "trusted"
            or not item["citable"]
            or item["role"]
            not in (
                SUPPORT_ROLE_OCCURRENCE,
                SUPPORT_ROLE_EVIDENCE,
                SUPPORT_ROLE_NOMINATION,
            )
            for item in support_items
        ):
            raise ValidationError(
                f"New candidate {key} may cite only trusted, citable evidence or "
                "explicit grounding supports"
            )
        if not any(item["role"] == SUPPORT_ROLE_EVIDENCE for item in support_items):
            raise ValidationError(
                f"New candidate {key} lacks candidate_evidence support"
            )
        support_quote = _support_quote(
            proposal.get("support_quote"),
            label=f"new candidate {key} support_quote",
            allowed_support_ids=set(support_ids),
            support_registry=support_registry,
        )
        if not any(
            item["scope"] == "micro"
            and item["role"] == SUPPORT_ROLE_OCCURRENCE
            for item in support_items
        ):
            raise ValidationError(
                f"New candidate {key} lacks QAC focus-occurrence grounding"
            )
        if lane == "macro" and not any(
            item["scope"] == "macro" and item["role"] == SUPPORT_ROLE_EVIDENCE
            for item in support_items
        ):
            raise ValidationError(f"Macro new candidate {key} lacks macro support")
        if lane == "global" and not any(
            item["scope"] == "global" and item["role"] == SUPPORT_ROLE_EVIDENCE
            for item in support_items
        ):
            raise ValidationError(f"Global new candidate {key} lacks global support")

        branch_refs = _require_string_list(
            proposal.get("branch_refs"), f"new candidate {key} branch_refs"
        )
        if not branch_refs or not set(branch_refs) <= registered_branches:
            raise ValidationError(f"New candidate {key} cites unknown or no branches")
        unactivated_support_branches = sorted(
            {
                branch_ref
                for support in support_items
                for branch_ref in support["branch_refs"]
            }
            - set(branch_refs)
        )
        if unactivated_support_branches:
            raise ValidationError(
                f"New candidate {key} exposes branch-bearing support without "
                f"activating its branches: {unactivated_support_branches}"
            )
        if not set(branch_refs) & focus_branches:
            raise ValidationError(f"New candidate {key} lacks a focus-root branch")
        for branch_ref in branch_refs:
            root_id = branch_ref.split("/", 1)[0]
            if branch_ref in focus_branches:
                if not any(
                    support_registry[support_id]["role"] == SUPPORT_ROLE_OCCURRENCE
                    and owner["source_type"] == "qac_morpheme"
                    and owner["kind"] == "focus_root_occurrence"
                    and owner["lane"] == "micro"
                    and owner["trust"] == "trusted"
                    and root_id in owner["root_ids"]
                    and support_id in owner["support_ids"]
                    for support_id in support_ids
                    for owner in support_owners[support_id]
                ):
                    raise ValidationError(
                        f"New candidate {key} focus branch {branch_ref} is not "
                        "grounded by its cited QAC occurrence carrier"
                    )
            elif not any(
                support_registry[support_id]["role"] == SUPPORT_ROLE_NOMINATION
                and branch_ref in support_registry[support_id]["branch_refs"]
                and owner["trust"] == "trusted"
                and branch_ref in owner["branch_refs"]
                and support_id in owner["support_ids"]
                for support_id in support_ids
                for owner in support_owners[support_id]
            ):
                raise ValidationError(
                    f"New candidate {key} nominated branch {branch_ref} is not "
                    "grounded by cited branch_nomination support"
                )
        owner_anchor_refs = {
            match.group(0)
            for owner in cited_owners
            for anchor in owner["anchor_refs"]
            if (match := re.match(r"^[1-9][0-9]*:[1-9][0-9]*", anchor))
        }
        unsupported_anchors = set(anchor_refs) - owner_anchor_refs
        if unsupported_anchors:
            raise ValidationError(
                f"New candidate {key} anchors lack cited candidate support: "
                f"{sorted(unsupported_anchors)}"
            )
        contribution_key = _reader_contribution_key(
            claim=text_fields["claim"],
            reader_payoff=text_fields["reader_payoff"],
            containment=text_fields["containment"],
            deletion_loss=selection_basis["deletion_loss"],
        )
        if contribution_key in contribution_owners:
            raise ValidationError(
                f"New candidate {key} exactly duplicates the reader contribution of "
                f"{contribution_owners[contribution_key]}"
            )
        semantic_payload = {
            "docket_payload_sha256": identity["docket_payload_sha256"],
            "lane": lane,
            "scope": proposal["scope"],
            **text_fields,
            "selection_basis": selection_basis,
            "support_quote": support_quote,
            "confidence": confidence,
            "anchor_refs": sorted(anchor_refs),
            "support_ids": sorted(support_ids),
            "branch_refs": sorted(branch_refs),
        }
        candidate_id = f"new_{canonical_sha256(semantic_payload)[:20]}"
        if candidate_id in seen_ids:
            raise ValidationError(f"Semantically duplicate new candidate: {key}")
        seen_ids.add(candidate_id)
        contribution_owners[contribution_key] = f"new:{key}"
        normalized.append(
            {
                "candidate_id": candidate_id,
                "proposal_key": key,
                "status": "selected",
                "lane": lane,
                "scope": proposal["scope"],
                **text_fields,
                "selection_basis": selection_basis,
                "support_quote": support_quote,
                "confidence": confidence,
                "anchor_refs": sorted(anchor_refs),
                "support_ids": sorted(support_ids),
                "branch_refs": sorted(branch_refs),
            }
        )
    return normalized


def _branch_review_registry(docket: dict[str, Any]) -> list[dict[str, str]]:
    records = [
        {
            "branch_ref": branch["branch_ref"],
            "registry": "focus",
            "descriptor": " ".join(branch["gloss"].split()),
        }
        for root in docket["branch_registry"]
        for branch in root["branches"]
    ]
    records.extend(
        {
            "branch_ref": branch["branch_ref"],
            "registry": "nominated",
            "descriptor": " ".join(
                (branch.get("image_en") or branch.get("image_ar") or "").split()
            ),
        }
        for branch in docket["nominated_branch_registry"]
    )
    if any(not item["descriptor"] for item in records):
        raise ValidationError("Branch review registry contains an empty descriptor")
    return records


def _validate_branch_review(
    raw_review: Any,
    docket: dict[str, Any],
    decisions: list[dict[str, Any]],
    new_candidates: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    expected_records = _branch_review_registry(docket)
    expected_order = [item["branch_ref"] for item in expected_records]
    review = _require_list(raw_review, "branch_review")
    if len(review) != len(expected_order):
        raise ValidationError(
            "Branch review does not cover every focus and nominated branch"
        )

    selected_existing = {
        item["candidate_id"]: item
        for item in decisions
        if item["status"] == "selected"
    }
    docket_candidates = {
        item["candidate_id"]: item for item in docket["candidates"]
    }
    new_by_key = {item["proposal_key"]: item for item in new_candidates}
    registered_branches = set(expected_order)
    focus_branch_refs = {
        branch["branch_ref"]
        for root in docket["branch_registry"]
        for branch in root["branches"]
    }
    support_registry = {
        item["support_id"]: item for item in docket["support_registry"]
    }
    support_owners: dict[str, list[dict[str, Any]]] = {
        support_id: [
            candidate
            for candidate in docket["candidates"]
            if support_id in candidate["support_ids"]
        ]
        for support_id in support_registry
    }
    focus_ref = docket["identity"]["ayah_ref"]
    normalized: list[dict[str, Any]] = []
    activated_branches: set[str] = set()
    bounded_contact_supports: dict[str, tuple[str, str]] = {}
    qac_root_ids_by_ref = {
        morpheme["qac_ref"]: set(
            docket["focus_root_mappings"].get(morpheme["root_ar"], [])
        )
        for morpheme in docket["focus"]["qac_morphemes"]
    }

    def word_owner_root_ids(owner: dict[str, Any]) -> set[str]:
        pointer_match = WORD_TOPIC_SOURCE_POINTER_RE.fullmatch(
            owner["source_pointer"]
        )
        if owner["source_type"] != "word_analysis" or pointer_match is None:
            return set()
        word_index = int(pointer_match.group(1))
        qac_refs = docket["focus"]["word_analysis_qac_refs"][word_index]
        return {
            root_id
            for qac_ref in qac_refs
            for root_id in qac_root_ids_by_ref.get(qac_ref, set())
        }

    def evidence_contacts_branch(branch_ref: str, support_id: str) -> bool:
        """Enforce a source-derived relation, not proposal-authored relabeling."""
        support = support_registry[support_id]
        if branch_ref in support["branch_refs"]:
            return True
        owners = support_owners[support_id]
        if any(
            owner["trust"] == "trusted"
            and branch_ref in owner["branch_refs"]
            and any(
                nomination_id in support_registry
                and support_registry[nomination_id]["role"]
                == SUPPORT_ROLE_NOMINATION
                and support_registry[nomination_id]["trust"] == "trusted"
                and support_registry[nomination_id]["citable"] is True
                and branch_ref in support_registry[nomination_id]["branch_refs"]
                for nomination_id in owner["support_ids"]
            )
            for owner in owners
        ):
            return True
        if branch_ref in focus_branch_refs:
            root_id = branch_ref.split("/", 1)[0]
            return support["source_type"] == "word_analysis" and any(
                support_id in owner["support_ids"]
                and root_id in word_owner_root_ids(owner)
                for owner in owners
            )
        return False

    for index, raw in enumerate(review):
        expected_record = expected_records[index]
        item = _require_dict(raw, f"branch_review[{index}]")
        _require_exact_keys(
            item,
            {
                "branch_ref",
                "registry",
                "status",
                "activation_refs",
                "reason_code",
                "reason",
                "support_ids",
                "contact_evidence",
                "unactivation_basis",
            },
            f"branch_review[{index}]",
        )
        branch_ref = item.get("branch_ref")
        if branch_ref != expected_order[index]:
            raise ValidationError(
                "Branch review must follow the focus then nominated registry order"
            )
        registry = item.get("registry")
        if registry != expected_record["registry"]:
            raise ValidationError(f"Branch review {branch_ref} registry is invalid")
        status = item.get("status")
        if not isinstance(status, str) or status not in (
            "activated",
            "unactivated",
        ):
            raise ValidationError(f"Branch review {branch_ref} has invalid status")
        reason = _require_text(item.get("reason"), f"branch review {branch_ref} reason")
        if not BRANCH_REVIEW_REASON_MIN_CHARS <= len(reason) <= BRANCH_REVIEW_REASON_MAX_CHARS:
            raise ValidationError(
                f"Branch review {branch_ref} reason must contain "
                f"{BRANCH_REVIEW_REASON_MIN_CHARS}-"
                f"{BRANCH_REVIEW_REASON_MAX_CHARS} characters"
            )
        descriptor = expected_record["descriptor"]
        if descriptor not in reason or branch_ref not in reason:
            raise ValidationError(
                f"Branch review {branch_ref} reason must quote its canonical ref and "
                f"registered descriptor: {descriptor!r}"
            )
        activation_refs = _require_string_list(
            item.get("activation_refs"),
            f"branch review {branch_ref} activation_refs",
        )
        if status == "activated" and not activation_refs:
            raise ValidationError(
                f"Activated branch review {branch_ref} lacks a candidate reference"
            )
        if status == "unactivated" and activation_refs:
            raise ValidationError(
                f"Unactivated branch review {branch_ref} cites a candidate"
            )

        reason_code = item.get("reason_code")
        if status == "activated" and reason_code != ACTIVATED_REASON_CODE:
            raise ValidationError(
                f"Activated branch review {branch_ref} has invalid reason_code"
            )
        if status == "unactivated" and (
            not isinstance(reason_code, str)
            or reason_code not in UNACTIVATED_REASON_CODES
        ):
            raise ValidationError(
                f"Unactivated branch review {branch_ref} has invalid reason_code"
            )
        support_ids = _require_string_list(
            item.get("support_ids"), f"branch review {branch_ref} support_ids"
        )
        if not support_ids:
            raise ValidationError(
                f"Branch review {branch_ref} must cite at least one support"
            )
        if set(support_ids) - set(support_registry):
            raise ValidationError(
                f"Branch review {branch_ref} cites an unknown support"
            )
        if any(
            not support_registry[support_id]["citable"]
            or support_registry[support_id]["trust"] != "trusted"
            for support_id in support_ids
        ):
            raise ValidationError(
                f"Branch review {branch_ref} cites untrusted or uncitable support"
            )
        if registry == "focus":
            root_id = branch_ref.split("/", 1)[0]
            if not any(
                support_registry[support_id]["role"] == SUPPORT_ROLE_OCCURRENCE
                and owner["lane"] == "micro"
                and root_id in owner["root_ids"]
                and any(
                    anchor == focus_ref or anchor.startswith(f"{focus_ref}:")
                    for anchor in owner["anchor_refs"]
                )
                for support_id in support_ids
                for owner in support_owners[support_id]
            ):
                raise ValidationError(
                    f"Branch review {branch_ref} lacks focus-root occurrence grounding"
                )
        elif not any(
            support_registry[support_id]["role"] == SUPPORT_ROLE_NOMINATION
            and branch_ref in support_registry[support_id]["branch_refs"]
            and owner["trust"] == "trusted"
            and branch_ref in owner["branch_refs"]
            for support_id in support_ids
            for owner in support_owners[support_id]
        ):
            raise ValidationError(
                f"Branch review {branch_ref} lacks its nominated-branch grounding"
            )

        raw_unactivation_basis = item.get("unactivation_basis")
        if status == "activated":
            if raw_unactivation_basis is not None:
                raise ValidationError(
                    f"Activated branch review {branch_ref} has an unactivation basis"
                )
            unactivation_basis = None
        else:
            basis = _require_dict(
                raw_unactivation_basis,
                f"branch review {branch_ref} unactivation_basis",
            )
            _require_exact_keys(
                basis,
                {"kind", "candidate_ids", "support_ids"},
                f"branch review {branch_ref} unactivation_basis",
            )
            basis_kind = basis.get("kind")
            if (
                not isinstance(basis_kind, str)
                or basis_kind not in UNACTIVATION_BASIS_KINDS
            ):
                raise ValidationError(
                    f"Branch review {branch_ref} has an invalid unactivation basis kind"
                )
            basis_candidate_ids = _require_string_list(
                basis.get("candidate_ids"),
                f"branch review {branch_ref} unactivation candidate_ids",
            )
            basis_support_ids = _require_string_list(
                basis.get("support_ids"),
                f"branch review {branch_ref} unactivation support_ids",
            )
            if not basis_candidate_ids:
                raise ValidationError(
                    f"Branch review {branch_ref} unactivation basis must cite at "
                    "least one docket candidate"
                )
            if not basis_support_ids:
                raise ValidationError(
                    f"Branch review {branch_ref} unactivation basis must cite at "
                    "least one support"
                )
            if set(basis_candidate_ids) - set(docket_candidates):
                raise ValidationError(
                    f"Branch review {branch_ref} unactivation basis cites an unknown "
                    "docket candidate"
                )
            if set(basis_support_ids) != set(support_ids):
                raise ValidationError(
                    f"Branch review {branch_ref} unactivation basis must account for "
                    "every branch-review support"
                )
            basis_candidates = [
                docket_candidates[candidate_id] for candidate_id in basis_candidate_ids
            ]
            if any(
                not any(
                    support_id in candidate["support_ids"]
                    for candidate in basis_candidates
                )
                for support_id in basis_support_ids
            ) or any(
                not set(candidate["support_ids"]) & set(basis_support_ids)
                for candidate in basis_candidates
            ):
                raise ValidationError(
                    f"Branch review {branch_ref} unactivation basis support ownership "
                    "is invalid"
                )
            root_id = branch_ref.split("/", 1)[0]
            if registry == "focus":
                grounding_role = SUPPORT_ROLE_OCCURRENCE
                grounding_present = any(
                    support_registry[support_id]["role"] == grounding_role
                    and candidate["source_type"] == "qac_morpheme"
                    and candidate["kind"] == "focus_root_occurrence"
                    and root_id in candidate["root_ids"]
                    and support_id in candidate["support_ids"]
                    for support_id in basis_support_ids
                    for candidate in basis_candidates
                )
            else:
                grounding_role = SUPPORT_ROLE_NOMINATION
                grounding_present = any(
                    support_registry[support_id]["role"] == grounding_role
                    and branch_ref in support_registry[support_id]["branch_refs"]
                    and branch_ref in candidate["branch_refs"]
                    and support_id in candidate["support_ids"]
                    for support_id in basis_support_ids
                    for candidate in basis_candidates
                )
            if not grounding_present:
                raise ValidationError(
                    f"Branch review {branch_ref} unactivation basis lacks exact registry "
                    "grounding"
                )
            if basis_kind == "grounding_only":
                if reason_code != "no_supported_contact" or any(
                    support_registry[support_id]["role"] != grounding_role
                    for support_id in basis_support_ids
                ):
                    raise ValidationError(
                        f"Branch review {branch_ref} grounding-only basis contains "
                        "non-grounding evidence or an incompatible reason"
                    )
            else:
                evidence_support_ids = [
                    support_id
                    for support_id in basis_support_ids
                    if support_registry[support_id]["role"] == SUPPORT_ROLE_EVIDENCE
                ]
                if reason_code not in (
                    "insufficient_evidence",
                    "scope_blocked",
                    "lexical_overreach",
                ) or not any(
                    evidence_contacts_branch(branch_ref, support_id)
                    for support_id in evidence_support_ids
                ):
                    raise ValidationError(
                        f"Branch review {branch_ref} rejected-evidence basis lacks "
                        "branch-related candidate evidence or has an incompatible reason"
                    )
            unactivation_basis = {
                "kind": basis_kind,
                "candidate_ids": sorted(basis_candidate_ids),
                "support_ids": sorted(basis_support_ids),
            }

        candidates_by_activation: dict[str, dict[str, Any]] = {}
        for activation_ref in activation_refs:
            if activation_ref in selected_existing:
                candidate = selected_existing[activation_ref]
            else:
                match = NEW_ACTIVATION_REF_RE.fullmatch(activation_ref)
                if not match or match.group(1) not in new_by_key:
                    raise ValidationError(
                        f"Branch review {branch_ref} cites an unknown or unselected "
                        f"activation: {activation_ref}"
                    )
                candidate = new_by_key[match.group(1)]
            if branch_ref not in candidate["branch_refs"]:
                raise ValidationError(
                    f"Branch review {branch_ref} activation {activation_ref} does not "
                    "carry that branch"
                )
            if not set(support_ids) & set(candidate["support_ids"]):
                raise ValidationError(
                    f"Branch review {branch_ref} lacks support for activation "
                    f"{activation_ref}"
                )
            candidates_by_activation[activation_ref] = candidate

        raw_contact_evidence = _require_list(
            item.get("contact_evidence"),
            f"branch review {branch_ref} contact_evidence",
        )
        if status == "unactivated" and raw_contact_evidence:
            raise ValidationError(
                f"Unactivated branch review {branch_ref} has contact evidence"
            )
        if status == "activated" and len(raw_contact_evidence) != len(activation_refs):
            raise ValidationError(
                f"Activated branch review {branch_ref} needs one contact record per "
                "activation"
            )
        normalized_contacts: list[dict[str, Any]] = []
        seen_contact_refs: set[str] = set()
        for contact_index, raw_contact in enumerate(raw_contact_evidence):
            contact = _require_dict(
                raw_contact,
                f"branch review {branch_ref} contact_evidence[{contact_index}]",
            )
            _require_exact_keys(
                contact,
                {
                    "activation_ref",
                    "support_id",
                    "quote",
                    "contact_mode",
                    "contact_claim",
                },
                f"branch review {branch_ref} contact_evidence[{contact_index}]",
            )
            activation_ref = contact.get("activation_ref")
            if not isinstance(activation_ref, str) or not ACTIVATION_REF_RE.fullmatch(
                activation_ref
            ):
                raise ValidationError(
                    f"Branch review {branch_ref} contact activation_ref is invalid"
                )
            if (
                activation_ref not in candidates_by_activation
                or activation_ref in seen_contact_refs
            ):
                raise ValidationError(
                    f"Branch review {branch_ref} contact activation is missing or duplicate"
                )
            seen_contact_refs.add(activation_ref)
            candidate = candidates_by_activation[activation_ref]
            support_id = contact.get("support_id")
            if (
                support_id not in support_ids
                or support_id not in candidate["support_ids"]
                or support_registry[support_id]["role"] != SUPPORT_ROLE_EVIDENCE
            ):
                raise ValidationError(
                    f"Branch review {branch_ref} contact for {activation_ref} lacks "
                    "candidate-owned evidence-role support"
                )
            quote = _require_text(
                contact.get("quote"),
                f"branch review {branch_ref} contact quote",
            )
            if not CONTACT_QUOTE_MIN_CHARS <= len(quote) <= CONTACT_QUOTE_MAX_CHARS:
                raise ValidationError(
                    f"Branch review {branch_ref} contact quote must contain "
                    f"{CONTACT_QUOTE_MIN_CHARS}-{CONTACT_QUOTE_MAX_CHARS} characters"
                )
            if quote not in support_registry[support_id]["text"]:
                raise ValidationError(
                    f"Branch review {branch_ref} contact quote is not an exact support excerpt"
                )
            if sum(character.isalpha() for character in quote) < 8:
                raise ValidationError(
                    f"Branch review {branch_ref} contact quote lacks explanatory text"
                )
            contact_mode = contact.get("contact_mode")
            contact_claim = _require_text(
                contact.get("contact_claim"),
                f"branch review {branch_ref} contact claim",
            )
            if not CONTACT_CLAIM_MIN_CHARS <= len(contact_claim) <= CONTACT_CLAIM_MAX_CHARS:
                raise ValidationError(
                    f"Branch review {branch_ref} contact claim must contain "
                    f"{CONTACT_CLAIM_MIN_CHARS}-{CONTACT_CLAIM_MAX_CHARS} characters"
                )
            if branch_ref not in contact_claim or descriptor not in contact_claim:
                raise ValidationError(
                    f"Branch review {branch_ref} contact claim must bind the exact "
                    "branch ref and registered descriptor"
                )
            if activation_ref in selected_existing:
                provenance = docket_candidates[activation_ref]
                if contact_mode != CONTACT_MODE_SOURCE_EXPLICIT:
                    raise ValidationError(
                        f"Existing activation {activation_ref} must use "
                        f"{CONTACT_MODE_SOURCE_EXPLICIT} contact"
                    )
                if (
                    provenance["source_type"] != "cross_run_publication"
                    or support_registry[support_id]["source_type"]
                    != "cross_run_publication"
                    or support_registry[support_id]["json_pointer"]
                    != provenance["source_pointer"]
                    or branch_ref not in support_registry[support_id]["branch_refs"]
                ):
                    raise ValidationError(
                        f"Existing activation {activation_ref} lacks a structured "
                        "publication anchor for this branch"
                    )
            else:
                if contact_mode != CONTACT_MODE_BOUNDED_INFERENCE:
                    raise ValidationError(
                        f"Recovered activation {activation_ref} must use "
                        f"{CONTACT_MODE_BOUNDED_INFERENCE} contact"
                    )
                if contact_claim not in candidate["mechanism"]:
                    raise ValidationError(
                        f"Recovered activation {activation_ref} contact claim must be "
                        "an exact clause of its proposal mechanism"
                    )
                if not evidence_contacts_branch(branch_ref, support_id):
                    raise ValidationError(
                        f"Recovered activation {activation_ref} relabels evidence with "
                        f"no source-derived relation to {branch_ref}"
                    )
                prior_contact = bounded_contact_supports.get(support_id)
                if prior_contact is not None:
                    raise ValidationError(
                        f"Recovered activation {activation_ref} reuses one generic "
                        "evidence support across recovered activations"
                    )
                bounded_contact_supports[support_id] = (activation_ref, branch_ref)
            normalized_contacts.append(
                {
                    "candidate_id": candidate["candidate_id"],
                    "support_id": support_id,
                    "quote": quote,
                    "contact_mode": contact_mode,
                    "contact_claim": contact_claim,
                }
            )
        if seen_contact_refs != set(activation_refs):
            raise ValidationError(
                f"Branch review {branch_ref} contact evidence does not cover activations"
            )

        if status == "activated":
            activated_branches.add(branch_ref)
        normalized.append(
            {
                "branch_ref": branch_ref,
                "registry": registry,
                "status": status,
                "candidate_ids": sorted(
                    candidate["candidate_id"]
                    for candidate in candidates_by_activation.values()
                ),
                "reason_code": reason_code,
                "reason": reason,
                "support_ids": sorted(support_ids),
                "unactivation_basis": unactivation_basis,
                "contact_evidence": sorted(
                    normalized_contacts, key=lambda contact: contact["candidate_id"]
                ),
            }
        )

    selected_branches = {
        branch_ref
        for item in [*selected_existing.values(), *new_candidates]
        for branch_ref in item["branch_refs"]
        if branch_ref in registered_branches
    }
    if activated_branches != selected_branches:
        raise ValidationError(
            "Activated branch review does not match all selected branch lineage"
        )
    return normalized


def _raw_branch_review(
    branch_review: list[dict[str, Any]],
    new_candidates: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    proposal_by_id = {
        item["candidate_id"]: item["proposal_key"] for item in new_candidates
    }
    return [
        {
            "branch_ref": item["branch_ref"],
            "registry": item["registry"],
            "status": item["status"],
            "activation_refs": [
                (
                    f"new:{proposal_by_id[candidate_id]}"
                    if candidate_id in proposal_by_id
                    else candidate_id
                )
                for candidate_id in item["candidate_ids"]
            ],
            "reason_code": item["reason_code"],
            "reason": item["reason"],
            "support_ids": item["support_ids"],
            "unactivation_basis": item["unactivation_basis"],
            "contact_evidence": [
                {
                    "activation_ref": (
                        f"new:{proposal_by_id[contact['candidate_id']]}"
                        if contact["candidate_id"] in proposal_by_id
                        else contact["candidate_id"]
                    ),
                    "support_id": contact["support_id"],
                    "quote": contact["quote"],
                    "contact_mode": contact["contact_mode"],
                    "contact_claim": contact["contact_claim"],
                }
                for contact in item["contact_evidence"]
            ],
        }
        for item in branch_review
    ]


def _adjudication_payload_hash(artifact: dict[str, Any]) -> str:
    payload = copy.deepcopy(artifact)
    payload.get("identity", {}).pop("adjudication_payload_sha256", None)
    return canonical_sha256(payload)


def _adjudication_coverage(
    docket: dict[str, Any],
    decisions: list[dict[str, Any]],
    new_candidates: list[dict[str, Any]],
    branch_review: list[dict[str, Any]],
) -> dict[str, Any]:
    decision_map = {item["candidate_id"]: item for item in decisions}
    focus_review = [item for item in branch_review if item["registry"] == "focus"]
    nominated_review = [
        item for item in branch_review if item["registry"] == "nominated"
    ]

    def grouped(field: str, values: list[str]) -> dict[str, dict[str, int]]:
        result: dict[str, dict[str, int]] = {}
        for value in values:
            candidates = [item for item in docket["candidates"] if item[field] == value]
            new_in_group = [item for item in new_candidates if item.get(field) == value]
            result[value] = {
                "candidate_count": len(candidates),
                "eligible_count": sum(item["selection_eligible"] for item in candidates),
                "ineligible_count": sum(
                    not item["selection_eligible"] for item in candidates
                ),
                "selected_existing_count": sum(
                    decision_map[item["candidate_id"]]["status"] == "selected"
                    for item in candidates
                    if item["selection_eligible"]
                ),
                "selected_new_count": len(new_in_group),
                "rejected_count": sum(
                    decision_map[item["candidate_id"]]["status"] == "rejected"
                    for item in candidates
                    if item["selection_eligible"]
                ),
                "deferred_count": sum(
                    decision_map[item["candidate_id"]]["status"] == "deferred"
                    for item in candidates
                    if item["selection_eligible"]
                ),
            }
        return result

    eligible = [item for item in docket["candidates"] if item["selection_eligible"]]
    selected_existing = [item for item in decisions if item["status"] == "selected"]
    source_types = sorted({item["source_type"] for item in docket["candidates"]})
    return {
        "docket_candidate_count": len(docket["candidates"]),
        "eligible_candidate_count": len(eligible),
        "ineligible_candidate_count": len(docket["candidates"]) - len(eligible),
        "decision_count": len(decisions),
        "selected_existing_count": len(selected_existing),
        "selected_new_count": len(new_candidates),
        "rejected_count": sum(item["status"] == "rejected" for item in decisions),
        "deferred_count": sum(item["status"] == "deferred" for item in decisions),
        "by_lane": grouped("lane", ["micro", "macro", "global"]),
        "by_source_type": grouped("source_type", source_types),
        "focus_branch_count": len(focus_review),
        "reviewed_focus_branch_count": len(focus_review),
        "activated_focus_branch_count": sum(
            item["status"] == "activated" for item in focus_review
        ),
        "unactivated_focus_branch_count": sum(
            item["status"] == "unactivated" for item in focus_review
        ),
        "nominated_branch_count": len(nominated_review),
        "reviewed_nominated_branch_count": len(nominated_review),
        "activated_nominated_branch_count": sum(
            item["status"] == "activated" for item in nominated_review
        ),
        "unactivated_nominated_branch_count": sum(
            item["status"] == "unactivated" for item in nominated_review
        ),
    }


def _validate_adjudication_response_unbound(
    response: dict[str, Any],
    docket: dict[str, Any],
    *,
    options: AdjudicationOptions | None = None,
) -> dict[str, Any]:
    options = options or AdjudicationOptions()
    options.validate()
    validate_docket(docket)
    if not docket["adjudication_gate"]["ready"]:
        raise ValidationError("Blocked docket cannot be adjudicated")
    _prompt, prompt_manifest = _render_adjudication_prompt_unbound(
        docket, options=options
    )
    prompt_sha256 = prompt_manifest["identity"]["prompt_sha256"]
    _require_exact_keys(
        response,
        {
            "schema_version",
            "identity",
            "decisions",
            "new_candidates",
            "discovery_complete",
            "branch_review",
        },
        "adjudication response",
    )
    if response.get("schema_version") != RESPONSE_SCHEMA:
        raise ValidationError("Unexpected adjudication response schema_version")
    if response.get("discovery_complete") is not True:
        raise BudgetError(
            "Adjudication reported incomplete discovery; increase the fail-loud "
            "safety ceiling before rerunning"
        )
    _validate_identity(response, docket, prompt_sha256=prompt_sha256)
    decisions = _validate_decisions(response.get("decisions"), docket)
    selected_existing = [
        item["candidate_id"] for item in decisions if item["status"] == "selected"
    ]
    new_candidate_capacity = _new_candidate_capacity(len(selected_existing))
    new_candidates = _validate_new_candidates(
        response.get("new_candidates"),
        docket,
        decisions,
        new_candidate_capacity=new_candidate_capacity,
    )
    if len(selected_existing) + len(new_candidates) > SELECTION_SAFETY_CEILING:
        raise ValidationError(
            "Selected candidate count exceeds the fail-loud safety ceiling "
            f"{SELECTION_SAFETY_CEILING}"
        )
    branch_review = _validate_branch_review(
        response.get("branch_review"), docket, decisions, new_candidates
    )
    focus_review = [item for item in branch_review if item["registry"] == "focus"]
    nominated_review = [
        item for item in branch_review if item["registry"] == "nominated"
    ]
    artifact = {
        "schema_version": VALIDATED_SCHEMA,
        "identity": {
            "ayah_ref": docket["identity"]["ayah_ref"],
            "source_canonical_sha256": docket["identity"]["source_canonical_sha256"],
            "docket_payload_sha256": docket["identity"]["docket_payload_sha256"],
            "prompt_sha256": prompt_sha256,
            "response_canonical_sha256": canonical_sha256(response),
        },
        "decisions": decisions,
        "new_candidates": new_candidates,
        "discovery_complete": True,
        "branch_review": branch_review,
        "selection": {
            "selected_existing_candidate_ids": selected_existing,
            "selected_new_candidate_ids": [item["candidate_id"] for item in new_candidates],
            "rejected_candidate_ids": [
                item["candidate_id"] for item in decisions if item["status"] == "rejected"
            ],
            "deferred_candidate_ids": [
                item["candidate_id"] for item in decisions if item["status"] == "deferred"
            ],
            "ineligible_candidate_ids": [
                item["candidate_id"]
                for item in docket["candidates"]
                if not item["selection_eligible"]
            ],
        },
        "coverage": _adjudication_coverage(
            docket, decisions, new_candidates, branch_review
        ),
        "limits": {
            "new_candidate_capacity": new_candidate_capacity,
            "selection_safety_ceiling": SELECTION_SAFETY_CEILING,
        },
    }
    artifact["identity"]["adjudication_payload_sha256"] = _adjudication_payload_hash(
        artifact
    )
    _validate_adjudication_artifact_unbound(artifact, docket, options=options)
    return artifact


def validate_adjudication_response(
    response: dict[str, Any],
    docket: dict[str, Any],
    *,
    options: AdjudicationOptions | None = None,
    prepare_options: PrepareOptions | None = None,
) -> dict[str, Any]:
    """Validate a response only against a persisted, source-rederived docket."""
    _require_persisted_docket_binding(docket, prepare_options=prepare_options)
    return _validate_adjudication_response_unbound(
        response, docket, options=options
    )


def _validate_adjudication_artifact_unbound(
    artifact: dict[str, Any],
    docket: dict[str, Any],
    *,
    options: AdjudicationOptions | None = None,
) -> None:
    trusted_options = options or AdjudicationOptions()
    trusted_options.validate()
    if artifact.get("schema_version") != VALIDATED_SCHEMA:
        raise ValidationError("Unexpected validated adjudication schema_version")
    _require_exact_keys(
        artifact,
        {
            "schema_version",
            "identity",
            "decisions",
            "new_candidates",
            "discovery_complete",
            "branch_review",
            "selection",
            "coverage",
            "limits",
        },
        "validated adjudication",
    )
    if artifact.get("discovery_complete") is not True:
        raise ValidationError("Validated adjudication discovery must be complete")
    identity = _require_dict(artifact.get("identity"), "adjudication identity")
    _require_exact_keys(
        identity,
        {
            "ayah_ref",
            "source_canonical_sha256",
            "docket_payload_sha256",
            "prompt_sha256",
            "response_canonical_sha256",
            "adjudication_payload_sha256",
        },
        "adjudication identity",
    )
    for field in (
        "prompt_sha256",
        "response_canonical_sha256",
        "adjudication_payload_sha256",
    ):
        if not isinstance(identity.get(field), str) or not re.fullmatch(
            r"[0-9a-f]{64}", identity[field]
        ):
            raise ValidationError(f"Validated adjudication {field} is invalid")
    for field in ("ayah_ref", "source_canonical_sha256", "docket_payload_sha256"):
        if identity.get(field) != docket.get("identity", {}).get(field):
            raise ValidationError(f"Validated adjudication {field} does not bind docket")
    expected_hash = identity.get("adjudication_payload_sha256")
    if expected_hash != _adjudication_payload_hash(artifact):
        raise ValidationError("Validated adjudication payload hash mismatch")
    decisions = _require_list(artifact.get("decisions"), "adjudication decisions")
    if [item.get("candidate_id") for item in decisions] != [
        item["candidate_id"]
        for item in docket["candidates"]
        if item["selection_eligible"]
    ]:
        raise ValidationError("Validated adjudication decision order/coverage drifted")
    revalidated_decisions = _validate_decisions(decisions, docket)
    if revalidated_decisions != decisions:
        raise ValidationError("Validated adjudication decisions are not normalized")
    new_candidates = _require_list(
        artifact.get("new_candidates"), "adjudication new_candidates"
    )
    limits = _require_dict(artifact.get("limits"), "adjudication limits")
    if set(limits) != {"new_candidate_capacity", "selection_safety_ceiling"}:
        raise ValidationError("Validated adjudication limits fields are invalid")
    new_candidate_capacity = limits.get("new_candidate_capacity")
    if (
        not isinstance(new_candidate_capacity, int)
        or isinstance(new_candidate_capacity, bool)
        or not 0 <= new_candidate_capacity <= SELECTION_SAFETY_CEILING
    ):
        raise ValidationError("Validated new_candidate_capacity is invalid")
    selected_existing_count = sum(
        item.get("status") == "selected" for item in decisions
    )
    if new_candidate_capacity != _new_candidate_capacity(selected_existing_count):
        raise ValidationError(
            "Validated new_candidate_capacity does not match selected decisions"
        )
    if limits.get("selection_safety_ceiling") != SELECTION_SAFETY_CEILING:
        raise ValidationError("Validated selection_safety_ceiling is invalid")
    raw_new_candidates: list[dict[str, Any]] = []
    normalized_fields = {
        "proposal_key",
        "title",
        "lane",
        "scope",
        "claim",
        "mechanism",
        "reader_payoff",
        "containment",
        "selection_basis",
        "support_quote",
        "confidence",
        "anchor_refs",
        "support_ids",
        "branch_refs",
    }
    for index, item in enumerate(new_candidates):
        normalized = _require_dict(item, f"adjudication new_candidates[{index}]")
        if set(normalized) != normalized_fields | {"candidate_id", "status"}:
            raise ValidationError("Validated new candidate fields are invalid")
        if normalized.get("status") != "selected":
            raise ValidationError("Validated new candidate must be selected")
        raw_new_candidates.append(
            {field: normalized[field] for field in normalized_fields}
        )
    revalidated_new = _validate_new_candidates(
        raw_new_candidates,
        docket,
        decisions,
        new_candidate_capacity=new_candidate_capacity,
    )
    if revalidated_new != new_candidates:
        raise ValidationError("Validated new candidates are not normalized")
    _prompt, prompt_manifest = _render_adjudication_prompt_unbound(
        docket,
        options=trusted_options,
    )
    if identity["prompt_sha256"] != prompt_manifest["identity"]["prompt_sha256"]:
        raise ValidationError("Validated adjudication does not bind current prompt")
    branch_review = _require_list(
        artifact.get("branch_review"), "adjudication branch_review"
    )
    revalidated_branch_review = _validate_branch_review(
        _raw_branch_review(branch_review, new_candidates),
        docket,
        decisions,
        new_candidates,
    )
    if revalidated_branch_review != branch_review:
        raise ValidationError("Validated branch review is not normalized")
    selection = _require_dict(artifact.get("selection"), "adjudication selection")
    _require_exact_keys(
        selection,
        {
            "selected_existing_candidate_ids",
            "selected_new_candidate_ids",
            "rejected_candidate_ids",
            "deferred_candidate_ids",
            "ineligible_candidate_ids",
        },
        "adjudication selection",
    )
    expected_selected = [
        item["candidate_id"] for item in decisions if item.get("status") == "selected"
    ]
    expected_rejected = [
        item["candidate_id"] for item in decisions if item.get("status") == "rejected"
    ]
    expected_deferred = [
        item["candidate_id"] for item in decisions if item.get("status") == "deferred"
    ]
    if len(expected_selected) + len(new_candidates) > SELECTION_SAFETY_CEILING:
        raise ValidationError("Validated selection exceeds fail-loud safety ceiling")
    if selection.get("selected_existing_candidate_ids") != expected_selected:
        raise ValidationError("Validated selected-existing index is inconsistent")
    if selection.get("selected_new_candidate_ids") != [
        item.get("candidate_id") for item in new_candidates
    ]:
        raise ValidationError("Validated selected-new index is inconsistent")
    if selection.get("rejected_candidate_ids") != expected_rejected:
        raise ValidationError("Validated rejected index is inconsistent")
    if selection.get("deferred_candidate_ids") != expected_deferred:
        raise ValidationError("Validated deferred index is inconsistent")
    expected_ineligible = [
        item["candidate_id"]
        for item in docket["candidates"]
        if not item["selection_eligible"]
    ]
    if selection.get("ineligible_candidate_ids") != expected_ineligible:
        raise ValidationError("Validated ineligible index is inconsistent")
    coverage = _require_dict(artifact.get("coverage"), "adjudication coverage")
    expected_coverage = _adjudication_coverage(
        docket, decisions, new_candidates, branch_review
    )
    if coverage != expected_coverage:
        raise ValidationError("Validated adjudication coverage is inconsistent")


def validate_adjudication_for_ayah(
    ayah_ref: str,
    *,
    options: AdjudicationOptions | None = None,
    prepare_options: PrepareOptions | None = None,
    write: bool = True,
    force: bool = False,
) -> tuple[dict[str, Any], dict[str, str]]:
    docket, docket_path = load_docket_for_ayah(
        ayah_ref, prepare_options=prepare_options
    )
    relatives = _artifact_relatives(ayah_ref)
    response_path = confined_existing_file(OUTPUTS_ROOT, relatives["response"])
    response, _raw = load_json_object_bounded(
        response_path, max_bytes=ADJUDICATION_RESPONSE_SAFETY_CEILING
    )
    effective_options = options or AdjudicationOptions()
    prompt, prompt_manifest = render_adjudication_prompt(
        docket,
        options=effective_options,
        prepare_options=prepare_options,
    )
    validate_exact_prompt_files(
        INPUTS_ROOT,
        relatives["prompt"],
        relatives["prompt_manifest"],
        expected_prompt=prompt,
        expected_manifest=prompt_manifest,
        label="Adjudication",
    )
    artifact = validate_adjudication_response(
        response,
        docket,
        options=effective_options,
        prepare_options=prepare_options,
    )
    paths = {
        "docket": str(docket_path),
        "response": str(response_path),
        "validated": str(OUTPUTS_ROOT / relatives["validated"]),
    }
    if write:
        write_json_confined(
            OUTPUTS_ROOT,
            relatives["validated"],
            artifact,
            replace=force,
        )
    return artifact, paths
