"""Build the selected-evidence packet and validate final Turkish synthesis."""

from __future__ import annotations

import copy
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .adjudication import (
    AdjudicationOptions,
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
    preflight_confined_writes,
    pretty_json_bytes,
    sha256_bytes,
    validate_exact_prompt_files,
    write_bytes_confined,
)
from .prepare import PrepareOptions, validate_docket, validate_prepared


PACKET_SCHEMA = "commentary-v3-synthesis-packet-v1"
RESPONSE_SCHEMA = "commentary-v3-synthesis-response-v1"
VALIDATED_SCHEMA = "commentary-v3-synthesis-validated-v1"
PROMPT_MANIFEST_SCHEMA = "commentary-v3-synthesis-prompt-manifest-v1"
KEY_RE = re.compile(r"^[a-z][a-z0-9_-]{2,63}$")
MAX_PARAGRAPHS = 16
MAX_FINDINGS = 48
MAX_FRICTION_NOTES = 12
SYNTHESIS_LIMIT_FIELDS = (
    "max_packet_bytes",
    "max_prompt_bytes",
    "min_prose_chars",
    "max_prose_chars",
    "max_paragraphs",
    "max_findings",
    "max_friction_notes",
)
@dataclass(frozen=True)
class SynthesisOptions:
    max_packet_bytes: int = 300_000
    max_prompt_bytes: int = 375_000
    min_prose_chars: int = 500
    max_prose_chars: int = 24_000
    max_paragraphs: int = 16
    max_findings: int = 48
    max_friction_notes: int = 12

    def validate(self) -> None:
        for name in SYNTHESIS_LIMIT_FIELDS:
            value = getattr(self, name)
            if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                raise ValidationError(f"{name} must be a nonnegative integer")
        if self.max_packet_bytes == 0 or self.max_prompt_bytes == 0:
            raise ValidationError("Packet and prompt byte limits must be positive")
        if self.min_prose_chars > self.max_prose_chars:
            raise ValidationError("min_prose_chars exceeds max_prose_chars")
        if self.max_paragraphs == 0 or self.max_findings == 0:
            raise ValidationError("Paragraph and finding limits must be positive")
        for name, ceiling in (
            ("max_paragraphs", MAX_PARAGRAPHS),
            ("max_findings", MAX_FINDINGS),
            ("max_friction_notes", MAX_FRICTION_NOTES),
        ):
            if getattr(self, name) > ceiling:
                raise ValidationError(f"{name} exceeds hard limit {ceiling}")


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


def _synthesis_limits(options: SynthesisOptions) -> dict[str, int]:
    options.validate()
    return {name: getattr(options, name) for name in SYNTHESIS_LIMIT_FIELDS}


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
    response, _response_raw = load_json_object(response_path)
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
            "every_selected_candidate_requires_complete_branch_lineage": True,
            "unknown_candidates_may_not_be_introduced": True,
            "apparatus_is_rendered_deterministically": True,
        },
    }
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
    replacements = {
        "@@AYAH_REF@@": identity["ayah_ref"],
        "@@SOURCE_SHA256@@": identity["source_canonical_sha256"],
        "@@DOCKET_SHA256@@": identity["docket_payload_sha256"],
        "@@ADJUDICATION_SHA256@@": identity["adjudication_payload_sha256"],
        "@@PACKET_SHA256@@": identity["synthesis_packet_sha256"],
        "@@MIN_PROSE_CHARS@@": str(options.min_prose_chars),
        "@@MAX_PROSE_CHARS@@": str(options.max_prose_chars),
        "@@MAX_PARAGRAPHS@@": str(options.max_paragraphs),
        "@@MAX_FINDINGS@@": str(options.max_findings),
        "@@MAX_FRICTION_NOTES@@": str(options.max_friction_notes),
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
    selected = {item["candidate_id"]: item for item in packet["selections"]}
    packet_supports = {item["support_id"] for item in packet["support_registry"]}
    packet_branches = {item["branch_ref"] for item in packet["branch_registry"]}
    raw_paragraphs = _require_list(response.get("paragraphs"), "synthesis paragraphs")
    if not 1 <= len(raw_paragraphs) <= options.max_paragraphs:
        raise ValidationError("Synthesis paragraph count is outside configured bounds")
    paragraph_fields = {"paragraph_key", "text", "finding_keys"}
    paragraphs_by_key: dict[str, dict[str, Any]] = {}
    raw_paragraph_texts: dict[str, str] = {}
    prose_chars = 0
    declared_finding_keys: list[str] = []
    for index, raw in enumerate(raw_paragraphs):
        paragraph = _require_dict(raw, f"paragraphs[{index}]")
        _exact_keys(paragraph, paragraph_fields, f"paragraphs[{index}]")
        expected_key = f"p{index + 1:02d}"
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
    if not options.min_prose_chars <= prose_chars <= options.max_prose_chars:
        raise ValidationError(
            f"Synthesis prose has {prose_chars} chars; required range is "
            f"{options.min_prose_chars}-{options.max_prose_chars}"
        )
    if len(declared_finding_keys) != len(set(declared_finding_keys)):
        raise ValidationError("A finding may land in only one paragraph")

    finding_fields = {
        "finding_key",
        "title",
        "summary",
        "effect",
        "epistemic_status",
        "candidate_ids",
        "support_ids",
        "branch_refs",
        "paragraph_key",
        "landing_quote",
        "containment_quote",
    }
    raw_findings = _require_list(response.get("findings"), "synthesis findings")
    if not 1 <= len(raw_findings) <= options.max_findings:
        raise ValidationError("Synthesis finding count is outside configured bounds")
    findings: list[dict[str, Any]] = []
    seen_keys: set[str] = set()
    seen_ids: set[str] = set()
    covered_candidates: set[str] = set()
    claim_grounded_candidates: set[str] = set()
    for index, raw in enumerate(raw_findings):
        finding = _require_dict(raw, f"findings[{index}]")
        _exact_keys(finding, finding_fields, f"findings[{index}]")
        key = finding.get("finding_key")
        if not isinstance(key, str) or not KEY_RE.fullmatch(key) or key in seen_keys:
            raise ValidationError(f"Finding {index} has invalid or duplicate finding_key")
        seen_keys.add(key)
        paragraph_key = finding.get("paragraph_key")
        if not isinstance(paragraph_key, str) or paragraph_key not in paragraphs_by_key:
            raise ValidationError(f"Finding {key} references unknown paragraph")
        if key not in paragraphs_by_key[paragraph_key]["finding_keys"]:
            raise ValidationError(f"Finding {key} is not declared by its paragraph")
        title = _text(finding.get("title"), f"finding {key} title")
        summary = _text(finding.get("summary"), f"finding {key} summary")
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
        candidate_ids = _string_list(
            finding.get("candidate_ids"), f"finding {key} candidate_ids", nonempty=True
        )
        if not set(candidate_ids) <= set(selected):
            raise ValidationError(f"Finding {key} cites an unselected candidate")
        support_ids = _string_list(
            finding.get("support_ids"), f"finding {key} support_ids", nonempty=True
        )
        if not set(support_ids) <= packet_supports:
            raise ValidationError(f"Finding {key} cites support outside synthesis packet")
        for candidate_id in candidate_ids:
            if not set(support_ids) & set(selected[candidate_id]["support_ids"]):
                raise ValidationError(
                    f"Finding {key} lacks cited support for candidate {candidate_id}"
                )
        branch_refs = _string_list(
            finding.get("branch_refs"), f"finding {key} branch_refs"
        )
        allowed_branches = {
            ref for candidate_id in candidate_ids for ref in selected[candidate_id]["branch_refs"]
        }
        if not set(branch_refs) <= allowed_branches or not set(branch_refs) <= packet_branches:
            raise ValidationError(f"Finding {key} cites unrelated branch evidence")
        nonlexical = [
            selected[candidate_id]
            for candidate_id in candidate_ids
            if selected[candidate_id]["origin"] != "docket"
            or selected[candidate_id]["source_type"] != "word_analysis"
        ]
        if nonlexical and epistemic_status == "bundle_traceable":
            raise ValidationError(f"Finding {key} understates inferential evidence")
        if any(item.get("confidence") == "exploratory" for item in nonlexical):
            if epistemic_status != "exploratory":
                raise ValidationError(f"Finding {key} must remain exploratory")
        if epistemic_status == "exploratory" and effect == "baseline":
            raise ValidationError(f"Exploratory finding {key} cannot be baseline")
        paragraph_text = paragraphs_by_key[paragraph_key]["text"]
        raw_landing_quote = finding.get("landing_quote")
        landing_quote = _text(raw_landing_quote, f"finding {key} landing_quote")
        if raw_landing_quote not in raw_paragraph_texts[paragraph_key]:
            raise ValidationError(f"Finding {key} landing_quote is absent from prose")
        missing_landing_claims = [
            candidate_id
            for candidate_id in candidate_ids
            if selected[candidate_id]["claim"] not in raw_landing_quote
        ]
        if missing_landing_claims:
            raise ValidationError(
                f"Finding {key} landing_quote lacks exact candidate claims: "
                f"{missing_landing_claims}"
            )
        claim_grounded_candidates.update(candidate_ids)
        raw_containment_quote = finding.get("containment_quote")
        containment_quote = _text(
            raw_containment_quote,
            f"finding {key} containment_quote",
            nullable=True,
        )
        if epistemic_status != "bundle_traceable" and containment_quote is None:
            raise ValidationError(f"Inferential finding {key} lacks prose containment")
        if (
            raw_containment_quote is not None
            and raw_containment_quote not in raw_paragraph_texts[paragraph_key]
        ):
            raise ValidationError(f"Finding {key} containment_quote is absent from prose")
        candidate_contributions = [
            {
                "candidate_id": candidate_id,
                "claim_landing": selected[candidate_id]["claim"],
                "deletion_loss": selected[candidate_id]["selection_basis"][
                    "deletion_loss"
                ],
            }
            for candidate_id in sorted(candidate_ids)
        ]
        semantic = {
            "packet_sha256": packet["identity"]["synthesis_packet_sha256"],
            "title": title,
            "summary": summary,
            "effect": effect,
            "epistemic_status": epistemic_status,
            "candidate_ids": sorted(candidate_ids),
            "support_ids": sorted(support_ids),
            "branch_refs": sorted(branch_refs),
            "paragraph_id": paragraph_key,
            "landing_quote": landing_quote,
            "containment_quote": containment_quote,
            "candidate_contributions": candidate_contributions,
        }
        finding_id = f"find_{canonical_sha256(semantic)[:20]}"
        if finding_id in seen_ids:
            raise ValidationError(f"Semantically duplicate finding: {key}")
        seen_ids.add(finding_id)
        covered_candidates.update(candidate_ids)
        findings.append(
            {
                "finding_id": finding_id,
                "finding_key": key,
                **{field: semantic[field] for field in (
                    "title", "summary", "effect", "epistemic_status", "candidate_ids",
                    "support_ids", "branch_refs", "paragraph_id", "landing_quote",
                    "containment_quote", "candidate_contributions",
                )},
            }
        )
    if set(declared_finding_keys) != seen_keys:
        raise ValidationError("Paragraph finding declarations do not match findings")
    if covered_candidates != set(selected):
        missing = sorted(set(selected) - covered_candidates)
        raise ValidationError(f"Selected candidates lack prose findings: {missing}")
    missing_claim_landings = sorted(set(selected) - claim_grounded_candidates)
    if missing_claim_landings:
        raise ValidationError(
            "Selected candidates lack exact claim prose landings: "
            f"{missing_claim_landings}"
        )
    missing_branch_lineage: dict[str, list[str]] = {}
    for candidate_id, selection in selected.items():
        required = set(selection["branch_refs"])
        cited = {
            branch_ref
            for finding in findings
            if candidate_id in finding["candidate_ids"]
            for branch_ref in finding["branch_refs"]
            if branch_ref in required
        }
        if cited != required:
            missing_branch_lineage[candidate_id] = sorted(required - cited)
    if missing_branch_lineage:
        raise ValidationError(
            "Branch-bearing selections lack complete finding branch lineage: "
            f"{missing_branch_lineage}"
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
    if len(raw_notes) > options.max_friction_notes:
        raise ValidationError("Synthesis friction note count exceeds configured limit")
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
                "summary": _text(note.get("summary"), f"friction note {index} summary"),
                "candidate_ids": sorted(candidate_ids),
                "support_ids": sorted(support_ids),
            }
        )
    return paragraphs, findings, notes


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
    _prompt, prompt_manifest = _render_synthesis_prompt_unbound(
        packet, options=options
    )
    expected_response_identity = {
        **packet["identity"],
        "prompt_sha256": prompt_manifest["identity"]["prompt_sha256"],
    }
    _exact_keys(
        response,
        {"schema_version", "identity", "paragraphs", "findings", "friction_notes"},
        "synthesis response",
    )
    if response.get("schema_version") != RESPONSE_SCHEMA:
        raise ValidationError("Unexpected synthesis response schema_version")
    identity = _require_dict(response.get("identity"), "synthesis response identity")
    _exact_keys(
        identity, set(expected_response_identity), "synthesis response identity"
    )
    if identity != expected_response_identity:
        raise ValidationError("Synthesis response identity does not bind prompt and packet")
    paragraphs, findings, notes = _normalize_synthesis_content(
        response, packet, options=options
    )
    selected_supports = {
        support_id for finding in findings for support_id in finding["support_ids"]
    }
    selected_branches = {
        branch_ref for finding in findings for branch_ref in finding["branch_refs"]
    }
    artifact = {
        "schema_version": VALIDATED_SCHEMA,
        "identity": {
            **expected_response_identity,
            "response_canonical_sha256": canonical_sha256(response),
        },
        "paragraphs": paragraphs,
        "findings": findings,
        "friction_notes": notes,
        "coverage": {
            "selected_candidate_count": len(packet["selections"]),
            "covered_candidate_count": len(
                {candidate_id for finding in findings for candidate_id in finding["candidate_ids"]}
            ),
            "paragraph_count": len(paragraphs),
            "finding_count": len(findings),
            "cited_support_count": len(selected_supports),
            "cited_branch_count": len(selected_branches),
            "friction_note_count": len(notes),
        },
        "limits": _synthesis_limits(options),
    }
    outputs = _render_markdown_outputs_unbound(artifact, packet, docket, adjudication)
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
                "- Sınır: "
                + (
                    f"“{_md_inline(finding['containment_quote'])}”"
                    if finding["containment_quote"]
                    else "yerel paket okumasının kendi sınırı"
                ),
            ]
        )
        for contribution in finding["candidate_contributions"]:
            evidence_lines.append(
                f"- Katki `{contribution['candidate_id']}`: "
                f"iddia “{_md_inline(contribution['claim_landing'])}”; silme kaybi "
                f"“{_md_inline(contribution['deletion_loss'])}”"
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
        support_ids = ", ".join(
            f"`{item}`" for item in candidate["support_ids"]
        ) or "yok"
        branch_refs = ", ".join(
            f"`{item}`" for item in candidate["branch_refs"]
        ) or "yok"
        friction_lines.append(
            f"- `{decision['status']}` `{decision['candidate_id']}` "
            f"({_md_inline(candidate['source_type'])}/{_md_inline(candidate['source_local_id'])}): "
            f"{_md_inline(decision['rationale'])} Destekler: {support_ids}; "
            f"dallar: {branch_refs}."
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
    if artifact.get("schema_version") != VALIDATED_SCHEMA:
        raise ValidationError("Unexpected validated synthesis schema_version")
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
    findings = _require_list(artifact.get("findings"), "validated findings")
    key_by_id = {
        item["finding_id"]: item["finding_key"]
        for item in findings
        if isinstance(item, dict)
    }
    raw_response = {
        "paragraphs": [
            {
                "paragraph_key": item["paragraph_id"],
                "text": item["text"],
                "finding_keys": [key_by_id[finding_id] for finding_id in item["finding_ids"]],
            }
            for item in _require_list(artifact.get("paragraphs"), "validated paragraphs")
        ],
        "findings": [
            {
                "finding_key": item["finding_key"],
                "title": item["title"],
                "summary": item["summary"],
                "effect": item["effect"],
                "epistemic_status": item["epistemic_status"],
                "candidate_ids": item["candidate_ids"],
                "support_ids": item["support_ids"],
                "branch_refs": item["branch_refs"],
                "paragraph_key": item["paragraph_id"],
                "landing_quote": item["landing_quote"],
                "containment_quote": item["containment_quote"],
            }
            for item in findings
        ],
        "friction_notes": artifact.get("friction_notes"),
    }
    paragraphs, normalized_findings, notes = _normalize_synthesis_content(
        raw_response, packet, options=options
    )
    if paragraphs != artifact.get("paragraphs"):
        raise ValidationError("Validated synthesis paragraphs are not normalized")
    if normalized_findings != findings:
        raise ValidationError("Validated synthesis findings are not normalized")
    if notes != artifact.get("friction_notes"):
        raise ValidationError("Validated synthesis friction notes are not normalized")
    expected_coverage = {
        "selected_candidate_count": len(packet["selections"]),
        "covered_candidate_count": len(
            {candidate_id for item in findings for candidate_id in item["candidate_ids"]}
        ),
        "paragraph_count": len(paragraphs),
        "finding_count": len(findings),
        "cited_support_count": len(
            {support_id for item in findings for support_id in item["support_ids"]}
        ),
        "cited_branch_count": len(
            {branch_ref for item in findings for branch_ref in item["branch_refs"]}
        ),
        "friction_note_count": len(notes),
    }
    if artifact.get("coverage") != expected_coverage:
        raise ValidationError("Validated synthesis coverage is inconsistent")
    rendered = _render_markdown_outputs_unbound(
        artifact, packet, docket, adjudication
    )
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
    response, _response_raw = load_json_object(response_path)
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
    response, _response_raw = load_json_object(response_path)
    verification_options = _packet_options(packet, trusted_options)
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
