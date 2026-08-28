"""Build the selected-evidence packet and validate final Turkish synthesis."""

from __future__ import annotations

import copy
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .adjudication import (
    ADJUDICATION_RESPONSE_SAFETY_CEILING,
    AdjudicationOptions,
    SELECTION_SAFETY_CEILING,
    _validate_adjudication_artifact_unbound,
    load_docket_for_ayah,
    render_adjudication_prompt,
    validate_adjudication_response,
)
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
)
from .prepare import PrepareOptions, validate_docket, validate_prepared


PACKET_SCHEMA = "commentary-v3-synthesis-packet-v2"
RESPONSE_SCHEMA = "commentary-v3-synthesis-response-v2"
VALIDATED_SCHEMA = "commentary-v3-synthesis-validated-v2"
PROMPT_MANIFEST_SCHEMA = "commentary-v3-synthesis-prompt-manifest-v2"
KEY_RE = re.compile(r"^[a-z][a-z0-9_-]{2,63}$")
MAX_PARAGRAPHS = SELECTION_SAFETY_CEILING
MAX_FINDINGS = SELECTION_SAFETY_CEILING
MAX_FRICTION_NOTES = SELECTION_SAFETY_CEILING
ANNOTATION_SAFETY_CEILING = 1_000_000
SYNTHESIS_LIMIT_FIELDS = (
    "max_packet_bytes",
    "max_prompt_bytes",
    "max_response_bytes",
    "max_annotation_chars",
    "min_prose_chars",
    "max_prose_chars",
    "max_rendered_output_bytes",
)
VALIDATED_PARAGRAPH_FIELDS = {"paragraph_id", "text", "finding_ids"}
VALIDATED_FINDING_FIELDS = {
    "finding_id",
    "finding_key",
    "title",
    "summary",
    "effect",
    "epistemic_status",
    "candidate_ids",
    "support_ids",
    "branch_refs",
    "paragraph_id",
    "landing_quote",
    "candidate_contributions",
}


@dataclass(frozen=True)
class SynthesisOptions:
    max_packet_bytes: int = 4_000_000
    max_prompt_bytes: int = 5_000_000
    max_response_bytes: int = 32_000_000
    max_annotation_chars: int = 1_000_000
    min_prose_chars: int = 500
    max_prose_chars: int = 1_000_000
    max_rendered_output_bytes: int = 64_000_000

    def validate(self) -> None:
        for name in SYNTHESIS_LIMIT_FIELDS:
            value = getattr(self, name)
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                raise ValidationError(f"{name} must be a nonnegative integer")
        if any(
            getattr(self, field) == 0
            for field in (
                "max_packet_bytes",
                "max_prompt_bytes",
                "max_response_bytes",
                "max_annotation_chars",
                "max_rendered_output_bytes",
            )
        ):
            raise ValidationError("Synthesis safety maxima must be positive")
        if self.min_prose_chars > self.max_prose_chars:
            raise ValidationError("min_prose_chars exceeds max_prose_chars")
        if self.max_annotation_chars > ANNOTATION_SAFETY_CEILING:
            raise ValidationError(
                "max_annotation_chars exceeds the fail-loud infrastructure ceiling"
            )


def _require_dict(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValidationError(f"{label} must be an object")
    return value


def _require_list(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        raise ValidationError(f"{label} must be an array")
    return value


def _exact_keys(value: dict[str, Any], fields: set[str], label: str) -> None:
    if set(value) != fields:
        raise ValidationError(
            f"{label} fields disagree with contract; "
            f"missing={sorted(fields - set(value))}, extra={sorted(set(value) - fields)}"
        )


def _text(value: Any, label: str, *, nullable: bool = False) -> str | None:
    if nullable and value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{label} must be a nonempty string")
    return " ".join(value.split())


def _string_list(value: Any, label: str, *, nonempty: bool = False) -> list[str]:
    items = _require_list(value, label)
    if nonempty and not items:
        raise ValidationError(f"{label} must not be empty")
    if any(not isinstance(item, str) or not item for item in items):
        raise ValidationError(f"{label} must contain only nonempty strings")
    if len(set(items)) != len(items):
        raise ValidationError(f"{label} contains duplicates")
    return items


def _annotation_text(value: Any, label: str, *, options: SynthesisOptions) -> str:
    if isinstance(value, str) and len(value) > options.max_annotation_chars:
        raise BudgetError(
            f"{label} has {len(value)} raw characters; configured annotation maximum "
            f"is {options.max_annotation_chars}. Nothing was truncated."
        )
    rendered = _text(value, label)
    if len(rendered) > options.max_annotation_chars:
        raise BudgetError(
            f"{label} has {len(rendered)} characters; configured annotation maximum "
            f"is {options.max_annotation_chars}. Nothing was truncated."
        )
    return rendered


def _enforce_response_budget(
    response: dict[str, Any],
    options: SynthesisOptions,
    *,
    raw_bytes: bytes | None = None,
) -> None:
    canonical_bytes = len(canonical_json_bytes(response))
    if canonical_bytes > options.max_response_bytes:
        raise BudgetError(
            f"Synthesis response is {canonical_bytes} canonical bytes; configured "
            f"maximum is {options.max_response_bytes}. Nothing was truncated."
        )
    if raw_bytes is not None and len(raw_bytes) > options.max_response_bytes:
        raise BudgetError(
            f"Synthesis response source is {len(raw_bytes)} bytes; configured maximum "
            f"is {options.max_response_bytes}. Nothing was truncated."
        )


def _enforce_rendered_output_budget(
    outputs: dict[str, bytes], options: SynthesisOptions
) -> None:
    total_bytes = sum(len(payload) for payload in outputs.values())
    if total_bytes > options.max_rendered_output_bytes:
        raise BudgetError(
            f"Rendered synthesis outputs total {total_bytes} bytes; configured maximum "
            f"is {options.max_rendered_output_bytes}. Nothing was truncated."
        )


def _overlapping_occurrence_starts(
    text: str, substring: str, *, stop_after: int = 2
) -> list[int]:
    starts: list[int] = []
    search_from = 0
    while len(starts) < stop_after:
        start = text.find(substring, search_from)
        if start < 0:
            break
        starts.append(start)
        search_from = start + 1
    return starts


def _synthesis_limits(options: SynthesisOptions) -> dict[str, int]:
    options.validate()
    return {name: getattr(options, name) for name in SYNTHESIS_LIMIT_FIELDS}


def _minimum_distinct_landing_chars(selections: list[dict[str, Any]]) -> int:
    return sum(len(selection["claim"]) for selection in selections)


def _require_synthesis_options(
    options: SynthesisOptions | None,
) -> SynthesisOptions:
    if options is None:
        raise ValidationError(
            "Caller-bound SynthesisOptions are required; packet-declared limits "
            "are not trusted policy"
        )
    options.validate()
    return options


def _options_from_limits(value: Any, label: str) -> SynthesisOptions:
    limits = _require_dict(value, label)
    _exact_keys(limits, set(SYNTHESIS_LIMIT_FIELDS), label)
    options = SynthesisOptions(**limits)
    options.validate()
    return options


def _packet_options(
    packet: dict[str, Any], options: SynthesisOptions | None = None
) -> SynthesisOptions:
    trusted = _require_synthesis_options(options)
    bound = _options_from_limits(packet.get("limits"), "synthesis packet limits")
    if _synthesis_limits(trusted) != _synthesis_limits(bound):
        raise ValidationError("Synthesis options do not match packet-bound limits")
    return trusted


def _artifact_relatives(ayah_ref: str) -> dict[str, Path]:
    if not isinstance(ayah_ref, str):
        raise ValidationError("Ayah ref must be a string")
    match = re.fullmatch(r"([1-9][0-9]*):([1-9][0-9]*)", ayah_ref)
    if not match:
        raise ValidationError(f"Invalid ayah ref: {ayah_ref!r}")
    surah, ayah = int(match.group(1)), int(match.group(2))
    stem = f"{surah}_{ayah}"
    folder = Path(f"s{surah:03d}")
    return {
        "source": Path("source") / folder / f"{stem}.bundle.json",
        "prepared": Path("prepared") / folder / f"{stem}.prepared.json",
        "adjudication": Path("adjudication") / folder / f"{stem}.adjudication.json",
        "adjudication_response": Path("adjudication") / folder / f"{stem}.response.json",
        "adjudication_prompt": Path("adjudication") / folder / f"{stem}.prompt.md",
        "adjudication_prompt_manifest": Path("adjudication") / folder / f"{stem}.prompt.json",
        "packet": Path("synthesis") / folder / f"{stem}.packet.json",
        "prompt": Path("synthesis") / folder / f"{stem}.prompt.md",
        "prompt_manifest": Path("synthesis") / folder / f"{stem}.prompt.json",
        "response": Path("synthesis") / folder / f"{stem}.response.json",
        "validated": Path("synthesis") / folder / f"{stem}.synthesis.json",
        "prose": folder / f"{stem}.prose.tr.md",
        "evidence": folder / f"{stem}.evidence.tr.md",
        "index": folder / f"{stem}.index.tr.md",
        "friction": folder / f"{stem}.friction.tr.md",
    }


def load_adjudication_for_ayah(
    ayah_ref: str,
    docket: dict[str, Any],
    *,
    options: AdjudicationOptions | None = None,
    prepare_options: PrepareOptions | None = None,
) -> tuple[dict[str, Any], Path]:
    trusted_options = options or AdjudicationOptions()
    trusted_options.validate()
    docket_identity = _require_dict(docket.get("identity"), "docket identity")
    if docket_identity.get("ayah_ref") != ayah_ref:
        raise ValidationError(
            "Requested adjudication ayah does not match the supplied docket identity"
        )
    relative = _artifact_relatives(ayah_ref)["adjudication"]
    path = confined_existing_file(OUTPUTS_ROOT, relative)
    artifact, _raw = load_json_object(path)
    _validate_adjudication_artifact_unbound(
        artifact, docket, options=trusted_options
    )
    prompt, prompt_manifest = render_adjudication_prompt(
        docket,
        options=trusted_options,
        prepare_options=prepare_options,
    )
    relatives = _artifact_relatives(ayah_ref)
    validate_exact_prompt_files(
        INPUTS_ROOT,
        relatives["adjudication_prompt"],
        relatives["adjudication_prompt_manifest"],
        expected_prompt=prompt,
        expected_manifest=prompt_manifest,
        label="Adjudication",
    )
    response_path = confined_existing_file(
        OUTPUTS_ROOT, relatives["adjudication_response"]
    )
    response, _response_raw = load_json_object_bounded(
        response_path, max_bytes=ADJUDICATION_RESPONSE_SAFETY_CEILING
    )
    rebuilt = validate_adjudication_response(
        response,
        docket,
        options=trusted_options,
        prepare_options=prepare_options,
    )
    if rebuilt != artifact:
        raise ValidationError(
            "Validated adjudication does not match its bound raw response"
        )
    return artifact, path


def _branch_map(docket: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for root in docket["branch_registry"]:
        for branch in root["branches"]:
            result[branch["branch_ref"]] = {
                "branch_ref": branch["branch_ref"],
                "registry": "focus",
                "root_id": root["root_id"],
                "root_ar": root.get("root_ar"),
                "status": branch.get("status"),
                "branch_kind": branch.get("branch_kind"),
                "gloss": branch.get("gloss"),
                "boundary": branch.get("boundary"),
            }
    for branch in docket["nominated_branch_registry"]:
        result[branch["branch_ref"]] = {
            "branch_ref": branch["branch_ref"],
            "registry": "nominated",
            "root_id": branch["branch_ref"].split("/", 1)[0],
            "root_ar": branch.get("root_ar"),
            "status": None,
            "branch_kind": None,
            "gloss": branch.get("image_en") or branch.get("image_ar"),
            "boundary": branch.get("scope_en") or branch.get("scope_ar"),
        }
    return result


def _packet_payload_hash(packet: dict[str, Any]) -> str:
    payload = copy.deepcopy(packet)
    payload.get("identity", {}).pop("synthesis_packet_sha256", None)
    return canonical_sha256(payload)


def _build_synthesis_packet_unbound(
    docket: dict[str, Any],
    adjudication: dict[str, Any],
    *,
    options: SynthesisOptions | None = None,
    adjudication_options: AdjudicationOptions | None = None,
    _validate_result: bool = True,
) -> dict[str, Any]:
    options = _require_synthesis_options(options)
    validate_docket(docket)
    trusted_adjudication_options = adjudication_options or AdjudicationOptions()
    trusted_adjudication_options.validate()
    _validate_adjudication_artifact_unbound(
        adjudication, docket, options=trusted_adjudication_options
    )
    candidate_map = {item["candidate_id"]: item for item in docket["candidates"]}
    decision_map = {item["candidate_id"]: item for item in adjudication["decisions"]}
    new_map = {item["candidate_id"]: item for item in adjudication["new_candidates"]}
    support_map = {item["support_id"]: item for item in docket["support_registry"]}
    branches = _branch_map(docket)
    selected_ids = (
        adjudication["selection"]["selected_existing_candidate_ids"]
        + adjudication["selection"]["selected_new_candidate_ids"]
    )
    if not selected_ids:
        raise ValidationError("Synthesis requires at least one selected candidate")
    if len(selected_ids) > MAX_FINDINGS:
        raise BudgetError(
            f"Synthesis has {len(selected_ids)} selected candidates; fail-loud "
            f"finding ceiling is {MAX_FINDINGS}. Nothing was compressed."
        )
    selections: list[dict[str, Any]] = []
    cited_support_ids: set[str] = set()
    cited_branch_refs: set[str] = set()
    for candidate_id in selected_ids:
        if candidate_id in candidate_map:
            candidate = candidate_map[candidate_id]
            decision = decision_map[candidate_id]
            support_ids = decision["support_ids"]
            branch_refs = decision["branch_refs"]
            selection = {
                "candidate_id": candidate_id,
                "origin": "docket",
                "priority": decision["priority"],
                "lane": candidate["lane"],
                "scope": candidate["scope"],
                "kind": candidate["kind"],
                "source_type": candidate["source_type"],
                "source_local_id": candidate["source_local_id"],
                "title": candidate["title"],
                "trust": candidate["trust"],
                "confidence": None,
                "claim": decision["synthesis_claim"],
                "mechanism": decision["rationale"],
                "reader_payoff": decision["reader_payoff"],
                "containment": decision["containment"],
                "selection_basis": decision["selection_basis"],
                "support_quote": decision["support_quote"],
                "anchor_refs": candidate["anchor_refs"],
                "root_ids": candidate["root_ids"],
                "support_ids": support_ids,
                "branch_refs": branch_refs,
            }
        else:
            candidate = new_map[candidate_id]
            support_ids = candidate["support_ids"]
            branch_refs = candidate["branch_refs"]
            selection = {
                "candidate_id": candidate_id,
                "origin": "adjudicator_new",
                "priority": "supporting",
                "lane": candidate["lane"],
                "scope": candidate["scope"],
                "kind": "recovered_surprise",
                "source_type": "adjudicator_new",
                "source_local_id": candidate["proposal_key"],
                "title": candidate["title"],
                "trust": "trusted_grounded_inference",
                "confidence": candidate["confidence"],
                "claim": candidate["claim"],
                "mechanism": candidate["mechanism"],
                "reader_payoff": candidate["reader_payoff"],
                "containment": candidate["containment"],
                "selection_basis": candidate["selection_basis"],
                "support_quote": candidate["support_quote"],
                "anchor_refs": candidate["anchor_refs"],
                "root_ids": sorted({ref.split("/", 1)[0] for ref in branch_refs}),
                "support_ids": support_ids,
                "branch_refs": branch_refs,
            }
        cited_support_ids.update(support_ids)
        cited_branch_refs.update(branch_refs)
        selections.append(selection)
    packet = {
        "schema_version": PACKET_SCHEMA,
        "identity": {
            "ayah_ref": docket["identity"]["ayah_ref"],
            "source_canonical_sha256": docket["identity"]["source_canonical_sha256"],
            "docket_payload_sha256": docket["identity"]["docket_payload_sha256"],
            "adjudication_payload_sha256": adjudication["identity"][
                "adjudication_payload_sha256"
            ],
        },
        "scope": {
            "pericope": docket["scope"]["pericope"],
            "readiness_mode": docket["adjudication_gate"]["mode"],
            "warnings": docket["adjudication_gate"]["warnings"],
        },
        "focus": docket["focus"],
        "selections": selections,
        "support_registry": [support_map[item] for item in sorted(cited_support_ids)],
        "branch_registry": [branches[item] for item in sorted(cited_branch_refs)],
        "limits": _synthesis_limits(options),
        "contract": {
            "every_selected_candidate_requires_a_prose_landing": True,
            "every_selected_candidate_requires_an_exact_claim_landing": True,
            "reader_payoff_and_containment_are_preserved_in_apparatus": True,
            "every_selected_candidate_requires_exactly_one_finding": True,
            "findings_must_follow_selection_order": True,
            "finding_supports_and_branches_must_be_complete": True,
            "candidate_landings_must_not_overlap": True,
            "every_selected_candidate_requires_complete_branch_lineage": True,
            "unknown_candidates_may_not_be_introduced": True,
            "apparatus_is_rendered_deterministically": True,
            "required_finding_count": len(selections),
            "minimum_distinct_landing_chars": _minimum_distinct_landing_chars(
                selections
            ),
            "paragraph_safety_ceiling": MAX_PARAGRAPHS,
            "friction_safety_ceiling": MAX_FRICTION_NOTES,
        },
    }
    minimum_prose_chars = max(
        options.min_prose_chars,
        packet["contract"]["minimum_distinct_landing_chars"],
    )
    if minimum_prose_chars > options.max_prose_chars:
        raise BudgetError(
            f"Exact synthesis landings require at least {minimum_prose_chars} prose "
            f"characters; configured maximum is {options.max_prose_chars}. Nothing "
            "was compressed."
        )
    packet["identity"]["synthesis_packet_sha256"] = _packet_payload_hash(packet)
    packet_bytes = canonical_json_bytes(packet)
    if len(packet_bytes) > options.max_packet_bytes:
        raise BudgetError(
            f"Synthesis packet is {len(packet_bytes)} bytes; limit is "
            f"{options.max_packet_bytes}. Nothing was truncated."
        )
    if _validate_result:
        _validate_synthesis_packet_unbound(
            packet,
            docket,
            adjudication,
            options=options,
            adjudication_options=trusted_adjudication_options,
        )
    return packet


def _validate_synthesis_packet_unbound(
    packet: dict[str, Any],
    docket: dict[str, Any],
    adjudication: dict[str, Any],
    *,
    options: SynthesisOptions | None = None,
    adjudication_options: AdjudicationOptions | None = None,
) -> None:
    trusted_adjudication_options = adjudication_options or AdjudicationOptions()
    trusted_adjudication_options.validate()
    _validate_adjudication_artifact_unbound(
        adjudication, docket, options=trusted_adjudication_options
    )
    if packet.get("schema_version") != PACKET_SCHEMA:
        raise ValidationError("Unexpected synthesis packet schema_version")
    identity = _require_dict(packet.get("identity"), "synthesis packet identity")
    expected_identity = {
        "ayah_ref": docket["identity"]["ayah_ref"],
        "source_canonical_sha256": docket["identity"]["source_canonical_sha256"],
        "docket_payload_sha256": docket["identity"]["docket_payload_sha256"],
        "adjudication_payload_sha256": adjudication["identity"][
            "adjudication_payload_sha256"
        ],
    }
    for field, expected in expected_identity.items():
        if identity.get(field) != expected:
            raise ValidationError(f"Synthesis packet {field} does not bind inputs")
    if identity.get("synthesis_packet_sha256") != _packet_payload_hash(packet):
        raise ValidationError("Synthesis packet payload hash mismatch")
    bound_options = _packet_options(packet, options)
    if len(canonical_json_bytes(packet)) > bound_options.max_packet_bytes:
        raise BudgetError(
            "Synthesis packet exceeds its packet-bound byte limit. Nothing was truncated."
        )
    expected_packet = _build_synthesis_packet_unbound(
        docket,
        adjudication,
        options=bound_options,
        adjudication_options=trusted_adjudication_options,
        _validate_result=False,
    )
    if packet != expected_packet:
        raise ValidationError(
            "Synthesis packet does not match docket/adjudication derivation"
        )
    selections = _require_list(packet.get("selections"), "synthesis selections")
    selected_ids = [item.get("candidate_id") for item in selections if isinstance(item, dict)]
    expected_selected = (
        adjudication["selection"]["selected_existing_candidate_ids"]
        + adjudication["selection"]["selected_new_candidate_ids"]
    )
    if selected_ids != expected_selected or len(set(selected_ids)) != len(selected_ids):
        raise ValidationError("Synthesis packet selection order/coverage drifted")
    support_ids = {
        item.get("support_id")
        for item in _require_list(packet.get("support_registry"), "packet supports")
        if isinstance(item, dict)
    }
    support_map = {
        item["support_id"]: item
        for item in packet["support_registry"]
    }
    branch_refs = {
        item.get("branch_ref")
        for item in _require_list(packet.get("branch_registry"), "packet branches")
        if isinstance(item, dict)
    }
    referenced_supports: set[str] = set()
    referenced_branches: set[str] = set()
    required_fields = {
        "candidate_id",
        "origin",
        "priority",
        "lane",
        "scope",
        "kind",
        "source_type",
        "source_local_id",
        "title",
        "trust",
        "confidence",
        "claim",
        "mechanism",
        "reader_payoff",
        "containment",
        "selection_basis",
        "support_quote",
        "anchor_refs",
        "root_ids",
        "support_ids",
        "branch_refs",
    }
    for index, selection in enumerate(selections):
        item = _require_dict(selection, f"selections[{index}]")
        _exact_keys(item, required_fields, f"selections[{index}]")
        item_supports = set(_string_list(item["support_ids"], "selection supports", nonempty=True))
        item_branches = set(_string_list(item["branch_refs"], "selection branches"))
        if not item_supports <= support_ids or not item_branches <= branch_refs:
            raise ValidationError("Synthesis selection references unregistered evidence")
        unactivated_support_branches = sorted(
            {
                branch_ref
                for support_id in item_supports
                for branch_ref in support_map[support_id]["branch_refs"]
            }
            - item_branches
        )
        if unactivated_support_branches:
            raise ValidationError(
                f"Synthesis selection {item['candidate_id']} exposes branch-bearing "
                "support without activated lineage: "
                f"{unactivated_support_branches}"
            )
        referenced_supports.update(item_supports)
        referenced_branches.update(item_branches)
    if referenced_supports != support_ids or referenced_branches != branch_refs:
        raise ValidationError("Synthesis packet contains unreferenced support/branch records")


def _render_synthesis_prompt_unbound(
    packet: dict[str, Any],
    *,
    options: SynthesisOptions | None = None,
    template: str | None = None,
) -> tuple[str, dict[str, Any]]:
    options = _packet_options(packet, options)
    if template is None:
        try:
            template = (V3_ROOT / "prompts" / "synthesis.md").read_text(encoding="utf-8")
        except OSError as exc:
            raise ValidationError(f"Cannot read synthesis prompt template: {exc}") from exc
    identity = packet["identity"]
    effective_min_prose_chars = max(
        options.min_prose_chars,
        packet["contract"]["minimum_distinct_landing_chars"],
    )
    replacements = {
        "@@AYAH_REF@@": identity["ayah_ref"],
        "@@SOURCE_SHA256@@": identity["source_canonical_sha256"],
        "@@DOCKET_SHA256@@": identity["docket_payload_sha256"],
        "@@ADJUDICATION_SHA256@@": identity["adjudication_payload_sha256"],
        "@@PACKET_SHA256@@": identity["synthesis_packet_sha256"],
        "@@MIN_PROSE_CHARS@@": str(effective_min_prose_chars),
        "@@MAX_PROSE_CHARS@@": str(options.max_prose_chars),
        "@@PARAGRAPH_SAFETY_CEILING@@": str(MAX_PARAGRAPHS),
        "@@REQUIRED_FINDING_COUNT@@": str(len(packet["selections"])),
        "@@FRICTION_SAFETY_CEILING@@": str(MAX_FRICTION_NOTES),
        "@@PACKET_JSON@@": canonical_json_bytes(packet).decode("utf-8"),
    }
    prompt = template
    for marker, replacement in replacements.items():
        if marker not in prompt:
            raise ValidationError(f"Synthesis prompt template lacks marker {marker}")
        prompt = prompt.replace(marker, replacement)
    unresolved = sorted(set(re.findall(r"@@[A-Z0-9_]+@@", prompt)))
    if unresolved:
        raise ValidationError(f"Unresolved synthesis prompt markers: {unresolved}")
    prompt_bytes = prompt.encode("utf-8")
    if len(prompt_bytes) > options.max_prompt_bytes:
        raise BudgetError(
            f"Synthesis prompt is {len(prompt_bytes)} bytes; limit is "
            f"{options.max_prompt_bytes}. Nothing was truncated."
        )
    manifest = {
        "schema_version": PROMPT_MANIFEST_SCHEMA,
        "identity": {
            **identity,
            "prompt_sha256": sha256_bytes(prompt_bytes),
        },
        "budget": {
            "packet_bytes": len(canonical_json_bytes(packet)),
            "prompt_bytes": len(prompt_bytes),
            "estimated_tokens_chars_div_4": (len(prompt) + 3) // 4,
            "selected_candidate_count": len(packet["selections"]),
            "required_finding_count": len(packet["selections"]),
            "minimum_distinct_landing_chars": packet["contract"][
                "minimum_distinct_landing_chars"
            ],
            "effective_min_prose_chars": effective_min_prose_chars,
        },
        "limits": _synthesis_limits(options),
        "contract": {
            "response_schema_version": RESPONSE_SCHEMA,
            "expected_response": str(
                Path("outputs") / _artifact_relatives(identity["ayah_ref"])["response"]
            ),
        },
    }
    return prompt, manifest


def _load_source_bound_synthesis_context(
    packet: dict[str, Any],
    *,
    options: SynthesisOptions | None,
    adjudication_options: AdjudicationOptions | None,
    prepare_options: PrepareOptions | None,
) -> tuple[dict[str, Any], dict[str, Any], SynthesisOptions]:
    trusted_options = _packet_options(packet, options)
    identity = _require_dict(packet.get("identity"), "synthesis packet identity")
    ayah_ref = identity.get("ayah_ref")
    if not isinstance(ayah_ref, str):
        raise ValidationError("Source-bound synthesis packet lacks an ayah identity")
    try:
        docket, _docket_path = load_docket_for_ayah(
            ayah_ref, prepare_options=prepare_options
        )
        adjudication, _adjudication_path = load_adjudication_for_ayah(
            ayah_ref,
            docket,
            options=adjudication_options,
            prepare_options=prepare_options,
        )
    except ValidationError as exc:
        raise ValidationError(
            "Public synthesis handoff requires persisted, source-rederived inputs: "
            f"{exc}"
        ) from exc
    _validate_synthesis_packet_unbound(
        packet,
        docket,
        adjudication,
        options=trusted_options,
        adjudication_options=adjudication_options,
    )
    return docket, adjudication, trusted_options


def render_synthesis_prompt(
    packet: dict[str, Any],
    *,
    options: SynthesisOptions | None = None,
    adjudication_options: AdjudicationOptions | None = None,
    prepare_options: PrepareOptions | None = None,
) -> tuple[str, dict[str, Any]]:
    """Render only after the packet rederives from retained source inputs."""
    _docket, _adjudication, trusted_options = (
        _load_source_bound_synthesis_context(
            packet,
            options=options,
            adjudication_options=adjudication_options,
            prepare_options=prepare_options,
        )
    )
    return _render_synthesis_prompt_unbound(packet, options=trusted_options)


def render_synthesis_for_ayah(
    ayah_ref: str,
    *,
    options: SynthesisOptions | None = None,
    adjudication_options: AdjudicationOptions | None = None,
    prepare_options: PrepareOptions | None = None,
    write: bool = True,
    force: bool = False,
) -> tuple[dict[str, Any], str, dict[str, Any], dict[str, str]]:
    trusted_options = _require_synthesis_options(options)
    docket, docket_path = load_docket_for_ayah(
        ayah_ref, prepare_options=prepare_options
    )
    adjudication, adjudication_path = load_adjudication_for_ayah(
        ayah_ref,
        docket,
        options=adjudication_options,
        prepare_options=prepare_options,
    )
    packet = _build_synthesis_packet_unbound(
        docket,
        adjudication,
        options=trusted_options,
        adjudication_options=adjudication_options,
    )
    prompt, manifest = render_synthesis_prompt(
        packet,
        options=trusted_options,
        adjudication_options=adjudication_options,
        prepare_options=prepare_options,
    )
    relatives = _artifact_relatives(ayah_ref)
    paths = {
        "docket": str(docket_path),
        "adjudication": str(adjudication_path),
        "packet": str(INPUTS_ROOT / relatives["packet"]),
        "prompt": str(INPUTS_ROOT / relatives["prompt"]),
        "prompt_manifest": str(INPUTS_ROOT / relatives["prompt_manifest"]),
        "expected_response": str(OUTPUTS_ROOT / relatives["response"]),
    }
    if write:
        payloads = {
            relatives["packet"]: pretty_json_bytes(packet),
            relatives["prompt"]: prompt.encode("utf-8"),
            relatives["prompt_manifest"]: pretty_json_bytes(manifest),
        }
        preflight_confined_writes(INPUTS_ROOT, payloads, replace=force)
        for relative in ("packet", "prompt", "prompt_manifest"):
            write_bytes_confined(
                INPUTS_ROOT,
                relatives[relative],
                payloads[relatives[relative]],
                replace=force,
            )
    return packet, prompt, manifest, paths


def _normalize_synthesis_content(
    response: dict[str, Any],
    packet: dict[str, Any],
    *,
    options: SynthesisOptions,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    selections = packet["selections"]
    selected = {item["candidate_id"]: item for item in selections}
    selected_order = [item["candidate_id"] for item in selections]
    packet_supports = {item["support_id"] for item in packet["support_registry"]}
    packet_branches = {item["branch_ref"] for item in packet["branch_registry"]}
    raw_paragraphs = _require_list(response.get("paragraphs"), "synthesis paragraphs")
    if not 1 <= len(raw_paragraphs) <= MAX_PARAGRAPHS:
        raise ValidationError("Synthesis paragraph count exceeds fail-loud safety bounds")
    paragraph_fields = {"paragraph_key", "text", "finding_keys"}
    paragraphs_by_key: dict[str, dict[str, Any]] = {}
    raw_paragraph_texts: dict[str, str] = {}
    prose_chars = 0
    declared_finding_keys: list[str] = []
    for index, raw in enumerate(raw_paragraphs):
        paragraph = _require_dict(raw, f"paragraphs[{index}]")
        _exact_keys(paragraph, paragraph_fields, f"paragraphs[{index}]")
        expected_key = f"p{index + 1:03d}"
        if paragraph.get("paragraph_key") != expected_key:
            raise ValidationError(f"Paragraph keys must be sequential; expected {expected_key}")
        raw_prose = paragraph.get("text")
        prose = _text(raw_prose, f"paragraph {expected_key} text")
        if contains_apparatus_id(prose):
            raise ValidationError(f"Paragraph {expected_key} leaks apparatus identifiers")
        finding_keys = _string_list(
            paragraph.get("finding_keys"),
            f"paragraph {expected_key} finding_keys",
            nonempty=True,
        )
        prose_chars += len(prose)
        declared_finding_keys.extend(finding_keys)
        paragraphs_by_key[expected_key] = {
            "paragraph_id": expected_key,
            "text": prose,
            "finding_keys": finding_keys,
        }
        raw_paragraph_texts[expected_key] = raw_prose
    minimum_prose_chars = max(
        options.min_prose_chars,
        packet["contract"]["minimum_distinct_landing_chars"],
    )
    if not minimum_prose_chars <= prose_chars <= options.max_prose_chars:
        raise ValidationError(
            f"Synthesis prose has {prose_chars} chars; required range is "
            f"{minimum_prose_chars}-{options.max_prose_chars}"
        )
    published_prose = "\n\n".join(
        paragraph["text"] for paragraph in paragraphs_by_key.values()
    )
    if len(declared_finding_keys) != len(set(declared_finding_keys)):
        raise ValidationError("A finding may land in only one paragraph")

    finding_fields = {
        "finding_key",
        "title",
        "summary",
        "effect",
        "epistemic_status",
        "candidate_id",
        "support_ids",
        "branch_refs",
        "paragraph_key",
        "landing_quote",
    }
    raw_findings = _require_list(response.get("findings"), "synthesis findings")
    if len(raw_findings) != len(selections):
        raise ValidationError(
            "Synthesis must emit exactly one finding per selected candidate"
        )
    if len(raw_findings) > MAX_FINDINGS:
        raise BudgetError("Synthesis finding count exceeds fail-loud safety ceiling")
    findings: list[dict[str, Any]] = []
    seen_keys: set[str] = set()
    seen_ids: set[str] = set()
    landing_ranges: dict[str, list[tuple[int, int, str]]] = {
        key: [] for key in paragraphs_by_key
    }
    for index, raw in enumerate(raw_findings):
        finding = _require_dict(raw, f"findings[{index}]")
        _exact_keys(finding, finding_fields, f"findings[{index}]")
        key = finding.get("finding_key")
        expected_key = f"f{index + 1:03d}"
        if key != expected_key or not KEY_RE.fullmatch(expected_key):
            raise ValidationError(
                f"Findings must follow exact selection order; expected {expected_key}"
            )
        if key in seen_keys:
            raise ValidationError(f"Finding {index} has a duplicate finding_key")
        seen_keys.add(key)
        expected_candidate_id = selected_order[index]
        candidate_id = finding.get("candidate_id")
        if candidate_id != expected_candidate_id:
            raise ValidationError(
                f"Finding {key} must carry only selected candidate "
                f"{expected_candidate_id} in exact selection order"
            )
        selection = selected[candidate_id]
        paragraph_key = finding.get("paragraph_key")
        if not isinstance(paragraph_key, str) or paragraph_key not in paragraphs_by_key:
            raise ValidationError(f"Finding {key} references unknown paragraph")
        if key not in paragraphs_by_key[paragraph_key]["finding_keys"]:
            raise ValidationError(f"Finding {key} is not declared by its paragraph")
        title = _annotation_text(
            finding.get("title"), f"finding {key} title", options=options
        )
        summary = _annotation_text(
            finding.get("summary"), f"finding {key} summary", options=options
        )
        effect = finding.get("effect")
        if not isinstance(effect, str) or effect not in (
            "baseline",
            "supports_primary",
            "shifts_primary",
        ):
            raise ValidationError(f"Finding {key} effect is invalid")
        epistemic_status = finding.get("epistemic_status")
        if not isinstance(epistemic_status, str) or epistemic_status not in (
            "bundle_traceable",
            "inference",
            "exploratory",
        ):
            raise ValidationError(f"Finding {key} epistemic_status is invalid")
        support_ids = _string_list(
            finding.get("support_ids"), f"finding {key} support_ids", nonempty=True
        )
        if support_ids != selection["support_ids"]:
            raise ValidationError(
                f"Finding {key} must retain the candidate's complete support set"
            )
        if not set(support_ids) <= packet_supports:
            raise ValidationError(f"Finding {key} cites support outside synthesis packet")
        branch_refs = _string_list(
            finding.get("branch_refs"), f"finding {key} branch_refs"
        )
        if branch_refs != selection["branch_refs"]:
            raise ValidationError(
                f"Finding {key} must retain the candidate's complete branch set"
            )
        if not set(branch_refs) <= packet_branches:
            raise ValidationError(f"Finding {key} cites unregistered branch evidence")
        direct = (
            selection["origin"] == "docket"
            and selection["source_type"] == "word_analysis"
        )
        if not direct and epistemic_status == "bundle_traceable":
            raise ValidationError(f"Finding {key} understates inferential evidence")
        if selection.get("confidence") == "exploratory":
            if epistemic_status != "exploratory":
                raise ValidationError(f"Finding {key} must remain exploratory")
        if epistemic_status == "exploratory" and effect == "baseline":
            raise ValidationError(f"Exploratory finding {key} cannot be baseline")
        raw_landing_quote = finding.get("landing_quote")
        landing_quote = _text(raw_landing_quote, f"finding {key} landing_quote")
        raw_paragraph = raw_paragraph_texts[paragraph_key]
        if raw_landing_quote not in raw_paragraph:
            raise ValidationError(f"Finding {key} landing_quote is absent from prose")
        raw_occurrences = _overlapping_occurrence_starts(
            raw_paragraph, raw_landing_quote
        )
        if len(raw_occurrences) != 1:
            raise ValidationError(
                f"Finding {key} landing_quote must occur exactly once in prose"
            )
        published_occurrences = _overlapping_occurrence_starts(
            published_prose, landing_quote
        )
        if len(published_occurrences) != 1:
            raise ValidationError(
                f"Finding {key} normalized landing_quote must occur exactly once "
                "in the complete published prose"
            )
        if selection["claim"] not in raw_landing_quote:
            raise ValidationError(
                f"Finding {key} landing_quote lacks the exact candidate claim"
            )
        published_paragraph = paragraphs_by_key[paragraph_key]["text"]
        paragraph_occurrences = _overlapping_occurrence_starts(
            published_paragraph, landing_quote
        )
        if len(paragraph_occurrences) != 1:
            raise ValidationError(
                f"Finding {key} normalized landing_quote does not resolve uniquely "
                "inside its published paragraph"
            )
        start = paragraph_occurrences[0]
        landing_ranges[paragraph_key].append(
            (start, start + len(landing_quote), key)
        )
        candidate_contributions = [
            {
                "candidate_id": candidate_id,
                "claim_landing": selection["claim"],
                "reader_payoff_landing": selection["reader_payoff"],
                "containment_landing": selection["containment"],
                "mechanism": selection["mechanism"],
                "deletion_loss": selection["selection_basis"]["deletion_loss"],
                "support_quote": selection["support_quote"],
            }
        ]
        semantic = {
            "packet_sha256": packet["identity"]["synthesis_packet_sha256"],
            "title": title,
            "summary": summary,
            "effect": effect,
            "epistemic_status": epistemic_status,
            "candidate_ids": [candidate_id],
            "support_ids": support_ids,
            "branch_refs": branch_refs,
            "paragraph_id": paragraph_key,
            "landing_quote": landing_quote,
            "candidate_contributions": candidate_contributions,
        }
        finding_id = f"find_{canonical_sha256(semantic)[:20]}"
        if finding_id in seen_ids:
            raise ValidationError(f"Semantically duplicate finding: {key}")
        seen_ids.add(finding_id)
        findings.append(
            {
                "finding_id": finding_id,
                "finding_key": key,
                **{field: semantic[field] for field in (
                    "title", "summary", "effect", "epistemic_status", "candidate_ids",
                    "support_ids", "branch_refs", "paragraph_id", "landing_quote",
                    "candidate_contributions",
                )},
            }
        )
    expected_finding_keys = [f"f{index + 1:03d}" for index in range(len(selections))]
    if declared_finding_keys != expected_finding_keys:
        raise ValidationError(
            "Paragraph finding declarations must preserve exact selection order"
        )
    for paragraph_key, ranges in landing_ranges.items():
        ordered = sorted(ranges)
        for previous, current in zip(ordered, ordered[1:]):
            if previous[1] > current[0]:
                raise ValidationError(
                    f"Candidate prose landings overlap in {paragraph_key}: "
                    f"{previous[2]}, {current[2]}"
                )
    finding_id_by_key = {item["finding_key"]: item["finding_id"] for item in findings}
    paragraphs = [
        {
            "paragraph_id": item["paragraph_id"],
            "text": item["text"],
            "finding_ids": [finding_id_by_key[key] for key in item["finding_keys"]],
        }
        for item in paragraphs_by_key.values()
    ]

    friction_fields = {"kind", "summary", "candidate_ids", "support_ids"}
    raw_notes = _require_list(response.get("friction_notes"), "friction_notes")
    if len(raw_notes) > MAX_FRICTION_NOTES:
        raise BudgetError("Synthesis friction notes exceed fail-loud safety ceiling")
    notes: list[dict[str, Any]] = []
    for index, raw in enumerate(raw_notes):
        note = _require_dict(raw, f"friction_notes[{index}]")
        _exact_keys(note, friction_fields, f"friction_notes[{index}]")
        kind = note.get("kind")
        if not isinstance(kind, str) or kind not in (
            "live_alternative",
            "scope_limit",
            "evidence_gap",
            "production",
        ):
            raise ValidationError(f"Friction note {index} kind is invalid")
        candidate_ids = _string_list(note.get("candidate_ids"), "friction candidate_ids")
        support_ids = _string_list(note.get("support_ids"), "friction support_ids")
        if not set(candidate_ids) <= set(selected) or not set(support_ids) <= packet_supports:
            raise ValidationError("Friction note cites evidence outside synthesis packet")
        if candidate_ids:
            for candidate_id in candidate_ids:
                if support_ids and not set(support_ids) & set(selected[candidate_id]["support_ids"]):
                    raise ValidationError("Friction note support does not ground its candidate")
        notes.append(
            {
                "kind": kind,
                "summary": _annotation_text(
                    note.get("summary"),
                    f"friction note {index} summary",
                    options=options,
                ),
                "candidate_ids": sorted(candidate_ids),
                "support_ids": sorted(support_ids),
            }
        )
    return paragraphs, findings, notes


def _synthesis_coverage(
    packet: dict[str, Any],
    paragraphs: list[dict[str, Any]],
    findings: list[dict[str, Any]],
    notes: list[dict[str, Any]],
) -> dict[str, Any]:
    def grouped(field: str) -> dict[str, dict[str, int]]:
        values = (
            ["micro", "macro", "global"]
            if field == "lane"
            else sorted({selection[field] for selection in packet["selections"]})
        )
        result: dict[str, dict[str, int]] = {}
        for value in values:
            candidate_ids = {
                selection["candidate_id"]
                for selection in packet["selections"]
                if selection[field] == value
            }
            grouped_findings = [
                finding
                for finding in findings
                if finding["candidate_ids"][0] in candidate_ids
            ]
            result[value] = {
                "selected_candidate_count": len(candidate_ids),
                "finding_count": len(grouped_findings),
                "cited_support_count": len(
                    {
                        support_id
                        for finding in grouped_findings
                        for support_id in finding["support_ids"]
                    }
                ),
                "cited_branch_count": len(
                    {
                        branch_ref
                        for finding in grouped_findings
                        for branch_ref in finding["branch_refs"]
                    }
                ),
            }
        return result

    return {
        "selected_candidate_count": len(packet["selections"]),
        "covered_candidate_count": len(findings),
        "exact_one_to_one_finding_count": len(findings),
        "paragraph_count": len(paragraphs),
        "finding_count": len(findings),
        "cited_support_count": len(
            {support_id for item in findings for support_id in item["support_ids"]}
        ),
        "cited_branch_count": len(
            {branch_ref for item in findings for branch_ref in item["branch_refs"]}
        ),
        "friction_note_count": len(notes),
        "by_lane": grouped("lane"),
        "by_source_type": grouped("source_type"),
    }


def _synthesis_payload_hash(artifact: dict[str, Any]) -> str:
    payload = copy.deepcopy(artifact)
    payload.get("identity", {}).pop("synthesis_payload_sha256", None)
    return canonical_sha256(payload)


def _output_hashes(outputs: dict[str, bytes]) -> dict[str, dict[str, Any]]:
    return {
        name: {"bytes": len(payload), "sha256": sha256_bytes(payload)}
        for name, payload in sorted(outputs.items())
    }


def _validate_synthesis_response_unbound(
    response: dict[str, Any],
    packet: dict[str, Any],
    docket: dict[str, Any],
    adjudication: dict[str, Any],
    *,
    options: SynthesisOptions | None = None,
    adjudication_options: AdjudicationOptions | None = None,
) -> tuple[dict[str, Any], dict[str, bytes]]:
    options = _packet_options(packet, options)
    _validate_synthesis_packet_unbound(
        packet,
        docket,
        adjudication,
        options=options,
        adjudication_options=adjudication_options,
    )
    _enforce_response_budget(response, options)
    _prompt, prompt_manifest = _render_synthesis_prompt_unbound(
        packet, options=options
    )
    expected_response_identity = {
        **packet["identity"],
        "prompt_sha256": prompt_manifest["identity"]["prompt_sha256"],
    }
    _exact_keys(
        response,
        {
            "schema_version",
            "identity",
            "paragraphs",
            "findings",
            "friction_complete",
            "friction_notes",
        },
        "synthesis response",
    )
    if response.get("schema_version") != RESPONSE_SCHEMA:
        raise ValidationError("Unexpected synthesis response schema_version")
    if response.get("friction_complete") is not True:
        raise BudgetError(
            "Synthesis reported incomplete friction discovery; increase the "
            "fail-loud safety ceiling before rerunning"
        )
    identity = _require_dict(response.get("identity"), "synthesis response identity")
    _exact_keys(
        identity, set(expected_response_identity), "synthesis response identity"
    )
    if identity != expected_response_identity:
        raise ValidationError("Synthesis response identity does not bind prompt and packet")
    paragraphs, findings, notes = _normalize_synthesis_content(
        response, packet, options=options
    )
    artifact = {
        "schema_version": VALIDATED_SCHEMA,
        "identity": {
            **expected_response_identity,
            "response_canonical_sha256": canonical_sha256(response),
        },
        "paragraphs": paragraphs,
        "findings": findings,
        "friction_complete": True,
        "friction_notes": notes,
        "coverage": _synthesis_coverage(packet, paragraphs, findings, notes),
        "limits": _synthesis_limits(options),
    }
    outputs = _render_markdown_outputs_unbound(artifact, packet, docket, adjudication)
    _enforce_rendered_output_budget(outputs, options)
    artifact["outputs"] = _output_hashes(outputs)
    artifact["identity"]["synthesis_payload_sha256"] = _synthesis_payload_hash(artifact)
    _validate_synthesis_artifact_unbound(
        artifact,
        packet,
        docket,
        adjudication,
        options=options,
        adjudication_options=adjudication_options,
    )
    return artifact, outputs


def validate_synthesis_response(
    response: dict[str, Any],
    packet: dict[str, Any],
    docket: dict[str, Any],
    adjudication: dict[str, Any],
    *,
    options: SynthesisOptions | None = None,
    adjudication_options: AdjudicationOptions | None = None,
    prepare_options: PrepareOptions | None = None,
) -> tuple[dict[str, Any], dict[str, bytes]]:
    """Validate only against the packet's persisted source-derived lineage."""
    persisted_docket, persisted_adjudication, trusted_options = (
        _load_source_bound_synthesis_context(
            packet,
            options=options,
            adjudication_options=adjudication_options,
            prepare_options=prepare_options,
        )
    )
    if docket != persisted_docket or adjudication != persisted_adjudication:
        raise ValidationError(
            "Public synthesis validation inputs differ from persisted source binding"
        )
    return _validate_synthesis_response_unbound(
        response,
        packet,
        persisted_docket,
        persisted_adjudication,
        options=trusted_options,
        adjudication_options=adjudication_options,
    )


def _md_inline(value: Any) -> str:
    return str(value).replace("\n", " ").replace("`", "'")


def _render_markdown_outputs_unbound(
    artifact: dict[str, Any],
    packet: dict[str, Any],
    docket: dict[str, Any],
    adjudication: dict[str, Any],
) -> dict[str, bytes]:
    prose = "\n\n".join(item["text"] for item in artifact["paragraphs"]) + "\n"
    support_map = {item["support_id"]: item for item in packet["support_registry"]}
    branch_map = {item["branch_ref"]: item for item in packet["branch_registry"]}
    review_branch_map = _branch_map(docket)
    docket_support_map = {
        item["support_id"]: item for item in docket["support_registry"]
    }
    branch_review = adjudication["branch_review"]
    review_support_map = {
        support_id: docket_support_map[support_id]
        for support_id in {
            support_id
            for item in branch_review
            for support_id in item["support_ids"]
        }
    }
    candidate_map = {item["candidate_id"]: item for item in packet["selections"]}
    finding_map = {item["finding_id"]: item for item in artifact["findings"]}

    evidence_lines = [
        "Bu kanıt yüzeyi, prose bulgularını doğrulanmış v3 aday, destek ve dal kimliklerine bağlar.",
        "`bundle_traceable` doğrudan paket okumasını, `inference` bounded sentezi, `exploratory` ise keşifsel rezonansı gösterir.",
        "",
        "## Bulgular",
    ]
    for finding in artifact["findings"]:
        evidence_lines.extend(
            [
                "",
                f"### `{finding['finding_id']}` — {_md_inline(finding['title'])}",
                f"- Prose landing: “{_md_inline(finding['landing_quote'])}”",
                f"- Okuma: {_md_inline(finding['summary'])}",
                f"- Statü/etki: `{finding['epistemic_status']}` / `{finding['effect']}`",
                "- Adaylar: " + ", ".join(f"`{item}`" for item in finding["candidate_ids"]),
                "- Destekler: " + ", ".join(f"`{item}`" for item in finding["support_ids"]),
                "- Dallar: "
                + (", ".join(f"`{item}`" for item in finding["branch_refs"]) or "yok"),
            ]
        )
        for contribution in finding["candidate_contributions"]:
            evidence_lines.append(
                f"- Katkı `{contribution['candidate_id']}`: iddia "
                f"“{_md_inline(contribution['claim_landing'])}”; okur getirisi "
                f"“{_md_inline(contribution['reader_payoff_landing'])}”; sınır "
                f"“{_md_inline(contribution['containment_landing'])}”; mekanizma "
                f"“{_md_inline(contribution['mechanism'])}”; silme kaybı "
                f"“{_md_inline(contribution['deletion_loss'])}”; doğrudan dayanak "
                f"`{contribution['support_quote']['support_id']}` "
                f"“{_md_inline(contribution['support_quote']['quote'])}”"
            )
    cited_support_ids = sorted(
        {support_id for item in artifact["findings"] for support_id in item["support_ids"]}
    )
    evidence_lines.extend(["", "## Atıf yapılan destekler"])
    for support_id in cited_support_ids:
        support = support_map[support_id]
        evidence_lines.append(
            f"- `{support_id}` [{support['scope']}; {support['trust']}; "
            f"{support['role']}; "
            f"{_md_inline(support['source_type'])}/{_md_inline(support['source_local_id'])}] "
            f"{_md_inline(support['text'])}"
        )
    cited_branch_refs = sorted(
        {branch_ref for item in artifact["findings"] for branch_ref in item["branch_refs"]}
    )
    evidence_lines.extend(["", "## Atıf yapılan dallar"])
    if not cited_branch_refs:
        evidence_lines.append("- Dal atfı gerektiren kabul edilmiş bulgu yoktur.")
    for branch_ref in cited_branch_refs:
        branch = branch_map[branch_ref]
        evidence_lines.append(
            f"- `{branch_ref}` [{branch['registry']}; {_md_inline(branch.get('root_ar'))}] "
            f"{_md_inline(branch.get('gloss'))}; sınır: {_md_inline(branch.get('boundary'))}"
        )
    evidence_lines.extend(
        [
            "",
            "## Kapsam",
            f"- Seçilen aday: {artifact['coverage']['selected_candidate_count']}; "
            f"prose içinde karşılanan: {artifact['coverage']['covered_candidate_count']}.",
            f"- Bulgu: {artifact['coverage']['finding_count']}; paragraf: "
            f"{artifact['coverage']['paragraph_count']}.",
            f"- Adjudication modu: `{packet['scope']['readiness_mode']}`.",
        ]
    )
    evidence = "\n".join(evidence_lines) + "\n"

    findings_for_candidate: dict[str, list[dict[str, Any]]] = {
        candidate_id: [
            finding for finding in artifact["findings"] if candidate_id in finding["candidate_ids"]
        ]
        for candidate_id in candidate_map
    }
    index_lines: list[str] = []
    for candidate_id in [item["candidate_id"] for item in packet["selections"]]:
        candidate = candidate_map[candidate_id]
        linked = findings_for_candidate[candidate_id]
        summaries = " / ".join(_md_inline(item["summary"]) for item in linked)
        tags = " ".join(
            f"[{item['epistemic_status']}] [{item['effect']}]" for item in linked
        )
        finding_ids = ",".join(item["finding_id"] for item in linked)
        index_lines.append(
            f"- `{_md_inline(candidate['source_local_id'])}` (`{candidate_id}` -> "
            f"`{finding_ids}`) — {summaries} {tags}"
        )
    index = "\n".join(index_lines) + "\n"

    docket_candidates = {item["candidate_id"]: item for item in docket["candidates"]}
    friction_lines = ["# Sürtünme ve kapsam kaydı"]
    for warning in packet["scope"]["warnings"]:
        friction_lines.append(f"- Kapsam uyarısı: {_md_inline(warning)}")
    for note in artifact["friction_notes"]:
        refs = ", ".join(f"`{item}`" for item in note["candidate_ids"])
        suffix = f" ({refs})" if refs else ""
        friction_lines.append(
            f"- `{note['kind']}`: {_md_inline(note['summary'])}{suffix}"
        )
    friction_lines.extend(["", "## Dal taraması"])
    if not branch_review:
        friction_lines.append("- İncelenecek odak veya aday gösterilmiş dal yoktur.")
    for item in branch_review:
        branch = review_branch_map[item["branch_ref"]]
        candidate_ids = ", ".join(
            f"`{candidate_id}`" for candidate_id in item["candidate_ids"]
        )
        suffix = f" ({candidate_ids})" if candidate_ids else ""
        support_ids = ", ".join(
            f"`{support_id}`" for support_id in item["support_ids"]
        )
        friction_lines.append(
            f"- `{item['branch_ref']}` [{item['registry']}] `{item['status']}`/"
            f"`{item['reason_code']}` [{_md_inline(branch.get('gloss'))}; "
            f"sinir: {_md_inline(branch.get('boundary'))}]: "
            f"{_md_inline(item['reason'])}{suffix} "
            f"Destekler: {support_ids}."
        )
        basis = item["unactivation_basis"]
        if basis is not None:
            basis_candidates = ", ".join(
                f"`{candidate_id}`" for candidate_id in basis["candidate_ids"]
            )
            basis_supports = ", ".join(
                f"`{support_id}`" for support_id in basis["support_ids"]
            )
            friction_lines.append(
                f"- Etkinlestirmeme temeli `{basis['kind']}`; adaylar: "
                f"{basis_candidates}; destekler: {basis_supports}."
            )
        for contact in item["contact_evidence"]:
            friction_lines.append(
                f"- Temas `{contact['candidate_id']}` / "
                f"`{contact['support_id']}` / `{contact['contact_mode']}`: "
                f"{_md_inline(contact['contact_claim'])}; "
                f"“{_md_inline(contact['quote'])}”"
            )
    friction_lines.extend(["", "## Dal taramasi destekleri"])
    for support_id in sorted(review_support_map):
        support = review_support_map[support_id]
        friction_lines.append(
            f"- `{support_id}` [{support['scope']}; {support['trust']}; "
            f"{support['role']}; "
            f"{_md_inline(support['source_type'])}/"
            f"{_md_inline(support['source_local_id'])}] "
            f"{_md_inline(support['text'])}"
        )
    friction_lines.extend(["", "## Adjudication'da dışarıda kalanlar"])
    excluded_decisions = [
        item for item in adjudication["decisions"] if item["status"] != "selected"
    ]
    if not excluded_decisions:
        friction_lines.append("- Dışarıda bırakılan docket adayı yoktur.")
    for decision in excluded_decisions:
        candidate = docket_candidates[decision["candidate_id"]]
        friction_lines.extend(
            [
                f"### `{decision['status']}` `{decision['candidate_id']}`",
                f"- Kaynak: `{_md_inline(candidate['source_type'])}` / "
                f"`{_md_inline(candidate['source_local_id'])}`.",
                f"- Gerekçe: {_md_inline(decision['rationale'])}",
                "- Tam normalize karar kaydı:",
                f"    {canonical_json_bytes(decision).decode('utf-8')}",
                "- Tam docket aday kaydı:",
                f"    {canonical_json_bytes(candidate).decode('utf-8')}",
                "- Kararın tam destek kayıtları:",
            ]
        )
        for support_id in decision["support_ids"]:
            friction_lines.append(
                f"    {canonical_json_bytes(docket_support_map[support_id]).decode('utf-8')}"
            )

    ineligible_ids = set(adjudication["selection"]["ineligible_candidate_ids"])
    ineligible_candidates = [
        candidate
        for candidate in docket["candidates"]
        if candidate["candidate_id"] in ineligible_ids
    ]
    friction_lines.extend(["", "## Seçime uygun olmayan docket adayları"])
    if not ineligible_candidates:
        friction_lines.append("- Seçime uygun olmayan docket adayı yoktur.")
    for candidate in ineligible_candidates:
        friction_lines.extend(
            [
                f"### `{candidate['candidate_id']}`",
                "- Tam docket aday kaydı:",
                f"    {canonical_json_bytes(candidate).decode('utf-8')}",
                "- Adayın tam destek kayıtları:",
            ]
        )
        for support_id in candidate["support_ids"]:
            friction_lines.append(
                f"    {canonical_json_bytes(docket_support_map[support_id]).decode('utf-8')}"
            )
    friction_lines.extend(
        [
            "",
            "## Density audit",
            f"- Seçilen mevcut aday: {len(adjudication['selection']['selected_existing_candidate_ids'])}.",
            f"- Seçilen yeni aday: {len(adjudication['selection']['selected_new_candidate_ids'])}.",
            f"- Reddedilen: {adjudication['coverage']['rejected_count']}; ertelenen: "
            f"{adjudication['coverage']['deferred_count']}.",
            f"- Odak dal taraması: "
            f"{adjudication['coverage']['reviewed_focus_branch_count']}/"
            f"{adjudication['coverage']['focus_branch_count']}; etkinleşen: "
            f"{adjudication['coverage']['activated_focus_branch_count']}; "
            f"etkinleşmeyen: "
            f"{adjudication['coverage']['unactivated_focus_branch_count']}.",
            f"- Aday gösterilmiş dal taraması: "
            f"{adjudication['coverage']['reviewed_nominated_branch_count']}/"
            f"{adjudication['coverage']['nominated_branch_count']}; etkinleşen: "
            f"{adjudication['coverage']['activated_nominated_branch_count']}; "
            f"etkinleşmeyen: "
            f"{adjudication['coverage']['unactivated_nominated_branch_count']}.",
            f"- Prose landing kapsamı: {artifact['coverage']['covered_candidate_count']}/"
            f"{artifact['coverage']['selected_candidate_count']}.",
        ]
    )
    friction = "\n".join(friction_lines) + "\n"
    return {
        "prose": prose.encode("utf-8"),
        "evidence": evidence.encode("utf-8"),
        "index": index.encode("utf-8"),
        "friction": friction.encode("utf-8"),
    }


def _raw_response_from_validated_artifact(
    artifact: dict[str, Any],
) -> dict[str, Any]:
    findings = _require_list(artifact.get("findings"), "validated findings")
    key_by_id: dict[str, str] = {}
    raw_findings: list[dict[str, Any]] = []
    for index, raw in enumerate(findings):
        finding = _require_dict(raw, f"validated findings[{index}]")
        _exact_keys(
            finding,
            VALIDATED_FINDING_FIELDS,
            f"validated findings[{index}]",
        )
        finding_id = _text(
            finding.get("finding_id"), f"validated findings[{index}] finding_id"
        )
        finding_key = _text(
            finding.get("finding_key"), f"validated findings[{index}] finding_key"
        )
        if finding_id in key_by_id:
            raise ValidationError("Validated synthesis contains duplicate finding IDs")
        key_by_id[finding_id] = finding_key
        candidate_ids = _string_list(
            finding.get("candidate_ids"),
            f"validated findings[{index}] candidate_ids",
            nonempty=True,
        )
        if len(candidate_ids) != 1:
            raise ValidationError(
                f"Validated findings[{index}] must carry exactly one candidate ID"
            )
        raw_findings.append(
            {
                "finding_key": finding_key,
                "title": finding.get("title"),
                "summary": finding.get("summary"),
                "effect": finding.get("effect"),
                "epistemic_status": finding.get("epistemic_status"),
                "candidate_id": candidate_ids[0],
                "support_ids": finding.get("support_ids"),
                "branch_refs": finding.get("branch_refs"),
                "paragraph_key": finding.get("paragraph_id"),
                "landing_quote": finding.get("landing_quote"),
            }
        )

    paragraphs = _require_list(artifact.get("paragraphs"), "validated paragraphs")
    raw_paragraphs: list[dict[str, Any]] = []
    for index, raw in enumerate(paragraphs):
        paragraph = _require_dict(raw, f"validated paragraphs[{index}]")
        _exact_keys(
            paragraph,
            VALIDATED_PARAGRAPH_FIELDS,
            f"validated paragraphs[{index}]",
        )
        finding_ids = _string_list(
            paragraph.get("finding_ids"),
            f"validated paragraphs[{index}] finding_ids",
            nonempty=True,
        )
        unknown_ids = [
            finding_id for finding_id in finding_ids if finding_id not in key_by_id
        ]
        if unknown_ids:
            raise ValidationError(
                f"Validated paragraphs[{index}] references unknown finding IDs: "
                f"{unknown_ids}"
            )
        raw_paragraphs.append(
            {
                "paragraph_key": paragraph.get("paragraph_id"),
                "text": paragraph.get("text"),
                "finding_keys": [key_by_id[finding_id] for finding_id in finding_ids],
            }
        )

    return {
        "paragraphs": raw_paragraphs,
        "findings": raw_findings,
        "friction_complete": artifact.get("friction_complete"),
        "friction_notes": artifact.get("friction_notes"),
    }


def _validate_synthesis_artifact_unbound(
    artifact: dict[str, Any],
    packet: dict[str, Any],
    docket: dict[str, Any],
    adjudication: dict[str, Any],
    *,
    options: SynthesisOptions | None = None,
    adjudication_options: AdjudicationOptions | None = None,
) -> None:
    options = _packet_options(packet, options)
    _validate_synthesis_packet_unbound(
        packet,
        docket,
        adjudication,
        options=options,
        adjudication_options=adjudication_options,
    )
    _exact_keys(
        artifact,
        {
            "schema_version",
            "identity",
            "paragraphs",
            "findings",
            "friction_complete",
            "friction_notes",
            "coverage",
            "limits",
            "outputs",
        },
        "validated synthesis",
    )
    if artifact.get("schema_version") != VALIDATED_SCHEMA:
        raise ValidationError("Unexpected validated synthesis schema_version")
    if artifact.get("friction_complete") is not True:
        raise ValidationError("Validated synthesis friction discovery is incomplete")
    identity = _require_dict(artifact.get("identity"), "synthesis identity")
    expected_identity_fields = set(packet["identity"]) | {
        "prompt_sha256",
        "response_canonical_sha256",
        "synthesis_payload_sha256",
    }
    _exact_keys(identity, expected_identity_fields, "synthesis identity")
    for field, expected in packet["identity"].items():
        if identity.get(field) != expected:
            raise ValidationError(f"Validated synthesis {field} does not bind packet")
    for field in (
        "prompt_sha256",
        "response_canonical_sha256",
        "synthesis_payload_sha256",
    ):
        if not isinstance(identity.get(field), str) or not re.fullmatch(
            r"[0-9a-f]{64}", identity[field]
        ):
            raise ValidationError(f"Validated synthesis {field} is invalid")
    if identity["synthesis_payload_sha256"] != _synthesis_payload_hash(artifact):
        raise ValidationError("Validated synthesis payload hash mismatch")
    limits = _require_dict(artifact.get("limits"), "synthesis limits")
    if limits != packet.get("limits") or limits != _synthesis_limits(options):
        raise ValidationError("Validated synthesis limits do not match packet-bound limits")
    _prompt, prompt_manifest = _render_synthesis_prompt_unbound(
        packet, options=options
    )
    if identity["prompt_sha256"] != prompt_manifest["identity"]["prompt_sha256"]:
        raise ValidationError("Validated synthesis does not bind current prompt")
    raw_response = _raw_response_from_validated_artifact(artifact)
    findings = _require_list(artifact.get("findings"), "validated findings")
    paragraphs, normalized_findings, notes = _normalize_synthesis_content(
        raw_response, packet, options=options
    )
    if paragraphs != artifact.get("paragraphs"):
        raise ValidationError("Validated synthesis paragraphs are not normalized")
    if normalized_findings != findings:
        raise ValidationError("Validated synthesis findings are not normalized")
    if notes != artifact.get("friction_notes"):
        raise ValidationError("Validated synthesis friction notes are not normalized")
    expected_coverage = _synthesis_coverage(packet, paragraphs, findings, notes)
    if artifact.get("coverage") != expected_coverage:
        raise ValidationError("Validated synthesis coverage is inconsistent")
    rendered = _render_markdown_outputs_unbound(
        artifact, packet, docket, adjudication
    )
    _enforce_rendered_output_budget(rendered, options)
    if artifact.get("outputs") != _output_hashes(rendered):
        raise ValidationError("Validated synthesis output hashes are inconsistent")


def validate_synthesis_artifact(
    artifact: dict[str, Any],
    packet: dict[str, Any],
    docket: dict[str, Any],
    adjudication: dict[str, Any],
    *,
    options: SynthesisOptions | None = None,
    adjudication_options: AdjudicationOptions | None = None,
    prepare_options: PrepareOptions | None = None,
) -> None:
    persisted_docket, persisted_adjudication, trusted_options = (
        _load_source_bound_synthesis_context(
            packet,
            options=options,
            adjudication_options=adjudication_options,
            prepare_options=prepare_options,
        )
    )
    if docket != persisted_docket or adjudication != persisted_adjudication:
        raise ValidationError(
            "Public synthesis validation inputs differ from persisted source binding"
        )
    _validate_synthesis_artifact_unbound(
        artifact,
        packet,
        persisted_docket,
        persisted_adjudication,
        options=trusted_options,
        adjudication_options=adjudication_options,
    )
    ayah_ref = packet["identity"]["ayah_ref"]
    prompt, prompt_manifest = _render_synthesis_prompt_unbound(
        packet, options=trusted_options
    )
    relatives = _artifact_relatives(ayah_ref)
    validate_exact_prompt_files(
        INPUTS_ROOT,
        relatives["prompt"],
        relatives["prompt_manifest"],
        expected_prompt=prompt,
        expected_manifest=prompt_manifest,
        label="Synthesis",
    )
    response_path = confined_existing_file(
        OUTPUTS_ROOT, relatives["response"]
    )
    response, response_raw = load_json_object_bounded(
        response_path, max_bytes=trusted_options.max_response_bytes
    )
    _enforce_response_budget(response, trusted_options, raw_bytes=response_raw)
    rebuilt_artifact, _rebuilt_outputs = _validate_synthesis_response_unbound(
        response,
        packet,
        persisted_docket,
        persisted_adjudication,
        options=trusted_options,
        adjudication_options=adjudication_options,
    )
    if rebuilt_artifact != artifact:
        raise ValidationError(
            "Validated synthesis artifact does not match the persisted raw response derivation"
        )


def validate_synthesis_for_ayah(
    ayah_ref: str,
    *,
    options: SynthesisOptions | None = None,
    adjudication_options: AdjudicationOptions | None = None,
    prepare_options: PrepareOptions | None = None,
    write: bool = True,
    force: bool = False,
) -> tuple[dict[str, Any], dict[str, bytes], dict[str, str]]:
    trusted_options = _require_synthesis_options(options)
    docket, docket_path = load_docket_for_ayah(
        ayah_ref, prepare_options=prepare_options
    )
    adjudication, adjudication_path = load_adjudication_for_ayah(
        ayah_ref,
        docket,
        options=adjudication_options,
        prepare_options=prepare_options,
    )
    relatives = _artifact_relatives(ayah_ref)
    packet_path = confined_existing_file(INPUTS_ROOT, relatives["packet"])
    packet, _raw = load_json_object(packet_path)
    effective_options = _packet_options(packet, trusted_options)
    _validate_synthesis_packet_unbound(
        packet,
        docket,
        adjudication,
        options=effective_options,
        adjudication_options=adjudication_options,
    )
    response_path = confined_existing_file(OUTPUTS_ROOT, relatives["response"])
    response, response_raw = load_json_object_bounded(
        response_path, max_bytes=effective_options.max_response_bytes
    )
    _enforce_response_budget(response, effective_options, raw_bytes=response_raw)
    prompt, prompt_manifest = render_synthesis_prompt(
        packet,
        options=effective_options,
        adjudication_options=adjudication_options,
        prepare_options=prepare_options,
    )
    validate_exact_prompt_files(
        INPUTS_ROOT,
        relatives["prompt"],
        relatives["prompt_manifest"],
        expected_prompt=prompt,
        expected_manifest=prompt_manifest,
        label="Synthesis",
    )
    artifact, outputs = validate_synthesis_response(
        response,
        packet,
        docket,
        adjudication,
        options=effective_options,
        adjudication_options=adjudication_options,
        prepare_options=prepare_options,
    )
    paths = {
        "docket": str(docket_path),
        "adjudication": str(adjudication_path),
        "packet": str(packet_path),
        "response": str(response_path),
        "validated": str(OUTPUTS_ROOT / relatives["validated"]),
        **{
            name: str(OUTPUTS_ROOT / relatives[name])
            for name in ("prose", "evidence", "index", "friction")
        },
    }
    if write:
        payloads = {
            relatives[name]: outputs[name]
            for name in ("prose", "evidence", "index", "friction")
        }
        payloads[relatives["validated"]] = pretty_json_bytes(artifact)
        preflight_confined_writes(OUTPUTS_ROOT, payloads, replace=force)
        for name in ("prose", "evidence", "index", "friction", "validated"):
            write_bytes_confined(
                OUTPUTS_ROOT,
                relatives[name],
                payloads[relatives[name]],
                replace=force,
            )
    return artifact, outputs, paths


def verify_final_outputs_for_ayah(
    ayah_ref: str,
    *,
    options: SynthesisOptions | None = None,
    adjudication_options: AdjudicationOptions | None = None,
    prepare_options: PrepareOptions | None = None,
) -> dict[str, Any]:
    trusted_options = _require_synthesis_options(options)
    docket, _docket_path = load_docket_for_ayah(
        ayah_ref, prepare_options=prepare_options
    )
    relatives = _artifact_relatives(ayah_ref)
    prepared_path = confined_existing_file(INPUTS_ROOT, relatives["prepared"])
    prepared, _prepared_raw = load_json_object(prepared_path)
    source_path = confined_existing_file(INPUTS_ROOT, relatives["source"])
    source_bundle, source_raw = load_json_object(source_path)
    validate_prepared(
        prepared,
        docket,
        source_bundle=source_bundle,
        source_raw=source_raw,
        options=prepare_options or PrepareOptions(),
    )
    source_identity = prepared["identity"]["source"]
    if sha256_bytes(source_raw) != source_identity.get("raw_sha256"):
        raise ValidationError("Source snapshot raw hash does not match prepared identity")
    if canonical_sha256(source_bundle) != source_identity.get("canonical_sha256"):
        raise ValidationError(
            "Source snapshot canonical hash does not match prepared identity"
        )
    if source_bundle.get("ayahRef") != ayah_ref:
        raise ValidationError("Source snapshot ayah identity disagrees with requested ayah")
    adjudication, _adjudication_path = load_adjudication_for_ayah(
        ayah_ref,
        docket,
        options=adjudication_options,
        prepare_options=prepare_options,
    )
    packet_path = confined_existing_file(INPUTS_ROOT, relatives["packet"])
    packet, _raw = load_json_object(packet_path)
    _validate_synthesis_packet_unbound(
        packet,
        docket,
        adjudication,
        options=trusted_options,
        adjudication_options=adjudication_options,
    )
    artifact_path = confined_existing_file(OUTPUTS_ROOT, relatives["validated"])
    artifact, _artifact_raw = load_json_object(artifact_path)
    validate_synthesis_artifact(
        artifact,
        packet,
        docket,
        adjudication,
        options=trusted_options,
        adjudication_options=adjudication_options,
        prepare_options=prepare_options,
    )
    response_path = confined_existing_file(OUTPUTS_ROOT, relatives["response"])
    verification_options = _packet_options(packet, trusted_options)
    response, _response_raw = load_json_object_bounded(
        response_path, max_bytes=verification_options.max_response_bytes
    )
    prompt, prompt_manifest = render_synthesis_prompt(
        packet,
        options=verification_options,
        adjudication_options=adjudication_options,
        prepare_options=prepare_options,
    )
    validate_exact_prompt_files(
        INPUTS_ROOT,
        relatives["prompt"],
        relatives["prompt_manifest"],
        expected_prompt=prompt,
        expected_manifest=prompt_manifest,
        label="Synthesis",
    )
    rebuilt_artifact, rebuilt_outputs = validate_synthesis_response(
        response,
        packet,
        docket,
        adjudication,
        options=verification_options,
        adjudication_options=adjudication_options,
        prepare_options=prepare_options,
    )
    if rebuilt_artifact != artifact:
        raise ValidationError("Validated synthesis does not match its raw response")
    expected_outputs = _render_markdown_outputs_unbound(
        artifact, packet, docket, adjudication
    )
    if expected_outputs != rebuilt_outputs:
        raise ValidationError("Rebuilt synthesis outputs are inconsistent")
    verified: dict[str, dict[str, Any]] = {}
    for name, expected in expected_outputs.items():
        path = confined_existing_file(OUTPUTS_ROOT, relatives[name])
        actual = path.read_bytes()
        if actual != expected:
            raise ValidationError(f"Final {name} output does not match synthesis artifact")
        verified[name] = {"path": str(path), "bytes": len(actual), "sha256": sha256_bytes(actual)}
    return {
        "ayah_ref": ayah_ref,
        "source_snapshot": {
            "path": str(source_path),
            "bytes": len(source_raw),
            "raw_sha256": source_identity["raw_sha256"],
            "canonical_sha256": source_identity["canonical_sha256"],
        },
        "readiness": {
            "mode": packet["scope"]["readiness_mode"],
            "warnings": packet["scope"]["warnings"],
        },
        "synthesis_payload_sha256": artifact["identity"]["synthesis_payload_sha256"],
        "coverage": artifact["coverage"],
        "outputs": verified,
    }
