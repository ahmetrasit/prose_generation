#!/usr/bin/env python3
"""Validate Commentary v2 configurations and authored JSON artifacts.

The repository intentionally does not require a third-party JSON Schema runtime.
The schemas guide model output; these semantic checks enforce the cross-artifact
rules that JSON Schema cannot express.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable

V2_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = V2_ROOT.parent.parent

AYAH_RE = re.compile(r"^([1-9][0-9]{0,2}):([1-9][0-9]{0,2})$")
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FINDING_RE = re.compile(
    r"^[1-9][0-9]{0,2}:[1-9][0-9]{0,2}:[a-z0-9]+(?:-[a-z0-9]+)*$"
)
EDITORIAL_SYNTHESIS_RE = re.compile(r"^editorial:[a-z0-9]+(?:-[a-z0-9]+)*$")
AUTHOR_SYNTHESIS_RE = re.compile(r"^author:[a-z0-9]+(?:-[a-z0-9]+)*$")
SHA_RE = re.compile(r"^[a-f0-9]{64}$")


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ValueError(f"cannot read {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def require_object(
    value: Any,
    where: str,
    required: set[str],
    allowed: set[str],
    errors: list[str],
) -> bool:
    if not isinstance(value, dict):
        errors.append(f"{where}: expected object")
        return False
    missing = sorted(required - value.keys())
    extra = sorted(value.keys() - allowed)
    if missing:
        errors.append(f"{where}: missing fields {missing}")
    if extra:
        errors.append(f"{where}: unknown fields {extra}")
    return not missing and not extra


def require_nonempty(value: Any, where: str, errors: list[str]) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{where}: expected non-empty string")


def require_array(value: Any, where: str, errors: list[str]) -> list[Any]:
    if not isinstance(value, list):
        errors.append(f"{where}: expected array")
        return []
    return value


def duplicate_values(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return sorted(duplicates)


def validate_ayah_ref(value: Any, surah: int, where: str, errors: list[str]) -> int | None:
    match = AYAH_RE.fullmatch(value) if isinstance(value, str) else None
    if not match:
        errors.append(f"{where}: invalid ayah reference {value!r}")
        return None
    if int(match.group(1)) != surah:
        errors.append(f"{where}: ayah reference belongs to another surah")
    return int(match.group(2))


def validate_run_config_data(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    allowed = {
        "schemaVersion",
        "runId",
        "surah",
        "language",
        "outputRoot",
        "defaultAyahSourcePattern",
        "governingSources",
        "ayahSources",
        "pericopes",
    }
    required = {"schemaVersion", "runId", "surah", "language", "pericopes"}
    require_object(data, "config", required, allowed, errors)
    if data.get("schemaVersion") != "commentary-v2-run-v1":
        errors.append("config.schemaVersion: expected commentary-v2-run-v1")
    run_id = data.get("runId")
    if not isinstance(run_id, str) or not ID_RE.fullmatch(run_id):
        errors.append("config.runId: use lowercase ASCII kebab-case")
    surah = data.get("surah")
    if not isinstance(surah, int) or isinstance(surah, bool) or not 1 <= surah <= 114:
        errors.append("config.surah: expected integer 1 through 114")
        surah = 0
    require_nonempty(data.get("language"), "config.language", errors)
    if "outputRoot" in data:
        require_nonempty(data.get("outputRoot"), "config.outputRoot", errors)
    if "defaultAyahSourcePattern" in data:
        pattern = data.get("defaultAyahSourcePattern")
        require_nonempty(pattern, "config.defaultAyahSourcePattern", errors)
        if isinstance(pattern, str) and "{ayah}" not in pattern:
            errors.append("config.defaultAyahSourcePattern: must contain {ayah}")

    governing = data.get("governingSources", [])
    if governing is not None:
        items = require_array(governing, "config.governingSources", errors)
        values = [item for item in items if isinstance(item, str)]
        if len(values) != len(items) or any(not item.strip() for item in values):
            errors.append("config.governingSources: every path must be non-empty")
        if duplicate_values(values):
            errors.append("config.governingSources: duplicate paths")

    ayah_sources = data.get("ayahSources", {})
    if ayah_sources is not None and not isinstance(ayah_sources, dict):
        errors.append("config.ayahSources: expected object")
        ayah_sources = {}
    for ref, paths in ayah_sources.items():
        number = validate_ayah_ref(ref, surah, f"config.ayahSources[{ref!r}]", errors)
        if number is None:
            continue
        values = require_array(paths, f"config.ayahSources[{ref!r}]", errors)
        if not values:
            errors.append(f"config.ayahSources[{ref!r}]: at least one source is required")
        if any(not isinstance(item, str) or not item.strip() for item in values):
            errors.append(f"config.ayahSources[{ref!r}]: invalid source path")

    pericopes = require_array(data.get("pericopes"), "config.pericopes", errors)
    if not pericopes:
        errors.append("config.pericopes: at least one pericope is required")
    pericope_ids: list[str] = []
    owned_ayahs: dict[int, str] = {}
    for index, pericope in enumerate(pericopes):
        where = f"config.pericopes[{index}]"
        if not require_object(pericope, where, {"id", "ayahs"}, {"id", "ayahs"}, errors):
            continue
        pericope_id = pericope.get("id")
        if not isinstance(pericope_id, str) or not ID_RE.fullmatch(pericope_id):
            errors.append(f"{where}.id: use lowercase ASCII kebab-case")
            continue
        pericope_ids.append(pericope_id)
        ayahs = require_array(pericope.get("ayahs"), f"{where}.ayahs", errors)
        if not ayahs:
            errors.append(f"{where}.ayahs: at least one ayah is required")
        valid: list[int] = []
        for ayah in ayahs:
            if not isinstance(ayah, int) or isinstance(ayah, bool) or ayah < 1:
                errors.append(f"{where}.ayahs: invalid ayah number {ayah!r}")
                continue
            valid.append(ayah)
            if ayah in owned_ayahs:
                errors.append(
                    f"{where}.ayahs: ayah {surah}:{ayah} already belongs to "
                    f"pericope {owned_ayahs[ayah]!r}"
                )
            else:
                owned_ayahs[ayah] = pericope_id
        if duplicate_values([str(item) for item in valid]):
            errors.append(f"{where}.ayahs: duplicate ayah numbers")
    duplicates = duplicate_values(pericope_ids)
    if duplicates:
        errors.append(f"config.pericopes: duplicate ids {duplicates}")

    if not data.get("defaultAyahSourcePattern") and not ayah_sources:
        errors.append(
            "config: provide defaultAyahSourcePattern or explicit ayahSources"
        )
    missing_sources = [
        f"{surah}:{ayah}"
        for ayah in sorted(owned_ayahs)
        if not data.get("defaultAyahSourcePattern")
        and f"{surah}:{ayah}" not in ayah_sources
    ]
    if missing_sources:
        errors.append(f"config.ayahSources: missing {missing_sources}")
    return errors


def validate_ledger_data(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    allowed = {
        "schemaVersion",
        "surah",
        "ayahRef",
        "language",
        "primaryFloor_tr",
        "sourceObligations",
        "findings",
        "coverageNote_tr",
    }
    required = allowed
    require_object(data, "ledger", required, allowed, errors)
    if data.get("schemaVersion") != "commentary-v2-layer2-discovery-v1":
        errors.append("ledger.schemaVersion: unexpected value")
    surah = data.get("surah")
    if not isinstance(surah, int) or isinstance(surah, bool) or not 1 <= surah <= 114:
        errors.append("ledger.surah: expected integer 1 through 114")
        surah = 0
    ayah_number = validate_ayah_ref(data.get("ayahRef"), surah, "ledger.ayahRef", errors)
    require_nonempty(data.get("language"), "ledger.language", errors)
    require_nonempty(data.get("primaryFloor_tr"), "ledger.primaryFloor_tr", errors)
    if not isinstance(data.get("coverageNote_tr"), str):
        errors.append("ledger.coverageNote_tr: expected string")

    findings = require_array(data.get("findings"), "ledger.findings", errors)
    finding_by_id: dict[str, dict[str, Any]] = {}
    finding_allowed = {
        "findingId",
        "disposition",
        "kind",
        "relation",
        "supportLevel",
        "localAnchors",
        "primaryReading_tr",
        "readingBefore_tr",
        "readingAfter_tr",
        "proseClaim_tr",
        "readerPayoff_tr",
        "sourceClaimRefs",
        "evidenceRefs",
        "activationTriggers",
        "counterEvidence",
        "channelTags",
        "blockingEvidence",
    }
    finding_required = {
        "findingId",
        "disposition",
        "kind",
        "relation",
        "supportLevel",
        "localAnchors",
        "primaryReading_tr",
        "proseClaim_tr",
        "readerPayoff_tr",
        "sourceClaimRefs",
        "evidenceRefs",
        "activationTriggers",
        "counterEvidence",
        "channelTags",
    }
    valid_kinds = {
        "ayah-function",
        "grammar",
        "sound-form",
        "local-resonance",
        "context-activation",
        "counterpressure",
        "surprising-outlier",
    }
    valid_relations = {
        "primary-floor",
        "supports-primary",
        "shifts-primary",
        "parallel-pressure",
    }
    valid_support = {
        "direct",
        "local-inference",
        "contextual-inference",
        "remote-lexical",
        "synthetic",
    }
    for index, finding in enumerate(findings):
        where = f"ledger.findings[{index}]"
        if not require_object(
            finding, where, finding_required, finding_allowed, errors
        ):
            if not isinstance(finding, dict):
                continue
        finding_id = finding.get("findingId")
        if not isinstance(finding_id, str) or not FINDING_RE.fullmatch(finding_id):
            errors.append(f"{where}.findingId: invalid value {finding_id!r}")
            continue
        if ayah_number is not None and not finding_id.startswith(
            f"{surah}:{ayah_number}:"
        ):
            errors.append(f"{where}.findingId: must be owned by ledger ayah")
        if finding_id in finding_by_id:
            errors.append(f"{where}.findingId: duplicate {finding_id!r}")
        finding_by_id[finding_id] = finding
        disposition = finding.get("disposition")
        if disposition not in {"carry", "blocked"}:
            errors.append(f"{where}.disposition: invalid value")
        if disposition == "blocked":
            blocking = require_array(
                finding.get("blockingEvidence"), f"{where}.blockingEvidence", errors
            )
            if not blocking:
                errors.append(f"{where}.blockingEvidence: blocked finding needs evidence")
        elif "blockingEvidence" in finding:
            errors.append(f"{where}.blockingEvidence: carry finding cannot be blocked")
        if finding.get("kind") not in valid_kinds:
            errors.append(f"{where}.kind: invalid value")
        if finding.get("relation") not in valid_relations:
            errors.append(f"{where}.relation: invalid value")
        if finding.get("supportLevel") not in valid_support:
            errors.append(f"{where}.supportLevel: invalid value")
        for field in ("primaryReading_tr", "proseClaim_tr", "readerPayoff_tr"):
            require_nonempty(finding.get(field), f"{where}.{field}", errors)
        anchors = require_array(finding.get("localAnchors"), f"{where}.localAnchors", errors)
        if not anchors:
            errors.append(f"{where}.localAnchors: at least one local anchor is required")
        for anchor_index, anchor in enumerate(anchors):
            awhere = f"{where}.localAnchors[{anchor_index}]"
            if not isinstance(anchor, dict):
                errors.append(f"{awhere}: expected object")
                continue
            for field in ("surface_ar", "surface_tr", "function_tr"):
                require_nonempty(anchor.get(field), f"{awhere}.{field}", errors)
            evidence = require_array(anchor.get("evidenceRefs"), f"{awhere}.evidenceRefs", errors)
            if not evidence:
                errors.append(f"{awhere}.evidenceRefs: at least one reference is required")
        for field in ("sourceClaimRefs", "evidenceRefs"):
            values = require_array(finding.get(field), f"{where}.{field}", errors)
            if not values:
                errors.append(f"{where}.{field}: at least one reference is required")
            if any(not isinstance(item, str) or not item.strip() for item in values):
                errors.append(f"{where}.{field}: references must be non-empty strings")
        triggers = require_array(
            finding.get("activationTriggers"), f"{where}.activationTriggers", errors
        )
        for trigger_index, trigger in enumerate(triggers):
            twhere = f"{where}.activationTriggers[{trigger_index}]"
            if not isinstance(trigger, dict):
                errors.append(f"{twhere}: expected object")
                continue
            validate_ayah_ref(trigger.get("ayahRef"), surah, f"{twhere}.ayahRef", errors)
            require_nonempty(trigger.get("effect_tr"), f"{twhere}.effect_tr", errors)
            refs = require_array(trigger.get("evidenceRefs"), f"{twhere}.evidenceRefs", errors)
            if not refs:
                errors.append(f"{twhere}.evidenceRefs: at least one reference is required")
        for field in ("counterEvidence", "channelTags"):
            require_array(finding.get(field), f"{where}.{field}", errors)

    obligations = require_array(
        data.get("sourceObligations"), "ledger.sourceObligations", errors
    )
    seen_obligations: list[str] = []
    for index, obligation in enumerate(obligations):
        where = f"ledger.sourceObligations[{index}]"
        if not isinstance(obligation, dict):
            errors.append(f"{where}: expected object")
            continue
        source_ref = obligation.get("sourceRef")
        require_nonempty(source_ref, f"{where}.sourceRef", errors)
        if isinstance(source_ref, str):
            seen_obligations.append(source_ref)
        disposition = obligation.get("disposition")
        if disposition not in {"carry", "blocked"}:
            errors.append(f"{where}.disposition: invalid value")
        refs = require_array(obligation.get("findingRefs"), f"{where}.findingRefs", errors)
        if disposition == "carry" and not refs:
            errors.append(f"{where}.findingRefs: carry obligation must map to a finding")
        for ref in refs:
            if ref not in finding_by_id:
                errors.append(f"{where}.findingRefs: unknown finding {ref!r}")
            elif disposition == "carry" and finding_by_id[ref].get("disposition") != "carry":
                errors.append(f"{where}.findingRefs: carry obligation maps to blocked finding")
        if disposition == "blocked":
            blocking = require_array(
                obligation.get("blockingEvidence"),
                f"{where}.blockingEvidence",
                errors,
            )
            if not blocking:
                errors.append(f"{where}.blockingEvidence: blocked obligation needs evidence")
    duplicates = duplicate_values(seen_obligations)
    if duplicates:
        errors.append(f"ledger.sourceObligations: duplicate source refs {duplicates}")
    return errors


def ledger_index(
    ledgers: Iterable[dict[str, Any]],
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]], list[str]]:
    by_ayah: dict[str, dict[str, Any]] = {}
    findings: dict[str, dict[str, Any]] = {}
    errors: list[str] = []
    for ledger in ledgers:
        ayah_ref = ledger.get("ayahRef")
        if not isinstance(ayah_ref, str):
            continue
        if ayah_ref in by_ayah:
            errors.append(f"duplicate ledger for {ayah_ref}")
        by_ayah[ayah_ref] = ledger
        for finding in ledger.get("findings", []):
            if not isinstance(finding, dict):
                continue
            finding_id = finding.get("findingId")
            if not isinstance(finding_id, str):
                continue
            if finding_id in findings:
                errors.append(f"duplicate finding id across ledgers: {finding_id}")
            findings[finding_id] = finding
    return by_ayah, findings, errors


def validate_plan_data(
    data: dict[str, Any],
    ledgers: Iterable[dict[str, Any]] | None = None,
    ledger_paths: Iterable[Path] | None = None,
) -> list[str]:
    errors: list[str] = []
    if data.get("schemaVersion") != "commentary-v2-pericope-editorial-plan-v1":
        errors.append("plan.schemaVersion: unexpected value")
    surah = data.get("surah")
    if not isinstance(surah, int) or isinstance(surah, bool) or not 1 <= surah <= 114:
        errors.append("plan.surah: expected integer 1 through 114")
        surah = 0
    pericope_id = data.get("pericopeId")
    if not isinstance(pericope_id, str) or not ID_RE.fullmatch(pericope_id):
        errors.append("plan.pericopeId: invalid id")
    ayah_refs = require_array(data.get("ayahRefs"), "plan.ayahRefs", errors)
    if not ayah_refs:
        errors.append("plan.ayahRefs: at least one ayah is required")
    for index, ref in enumerate(ayah_refs):
        validate_ayah_ref(ref, surah, f"plan.ayahRefs[{index}]", errors)
    if duplicate_values([ref for ref in ayah_refs if isinstance(ref, str)]):
        errors.append("plan.ayahRefs: duplicate references")

    source_ledgers = require_array(
        data.get("sourceLedgers"), "plan.sourceLedgers", errors
    )
    source_ledger_refs: list[str] = []
    source_ledger_hashes: dict[str, str] = {}
    for index, item in enumerate(source_ledgers):
        where = f"plan.sourceLedgers[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{where}: expected object")
            continue
        ref = item.get("ayahRef")
        validate_ayah_ref(ref, surah, f"{where}.ayahRef", errors)
        digest = item.get("sha256")
        if not isinstance(digest, str) or not SHA_RE.fullmatch(digest):
            errors.append(f"{where}.sha256: invalid SHA-256")
        if isinstance(ref, str):
            source_ledger_refs.append(ref)
            if isinstance(digest, str):
                source_ledger_hashes[ref] = digest
    if duplicate_values(source_ledger_refs):
        errors.append("plan.sourceLedgers: duplicate ayah references")
    if set(source_ledger_refs) != set(
        ref for ref in ayah_refs if isinstance(ref, str)
    ):
        errors.append("plan.sourceLedgers: must match plan.ayahRefs")

    ayah_plans = require_array(data.get("ayahPlans"), "plan.ayahPlans", errors)
    plan_by_ayah: dict[str, dict[str, Any]] = {}
    placement_lookup: dict[tuple[str, str], dict[str, Any]] = {}
    placement_findings: dict[str, list[tuple[str, str]]] = {}
    placement_syntheses: dict[str, list[tuple[str, str]]] = {}
    for index, ayah_plan in enumerate(ayah_plans):
        where = f"plan.ayahPlans[{index}]"
        if not isinstance(ayah_plan, dict):
            errors.append(f"{where}: expected object")
            continue
        ayah_ref = ayah_plan.get("ayahRef")
        validate_ayah_ref(ayah_ref, surah, f"{where}.ayahRef", errors)
        if isinstance(ayah_ref, str):
            if ayah_ref in plan_by_ayah:
                errors.append(f"{where}.ayahRef: duplicate plan for {ayah_ref}")
            plan_by_ayah[ayah_ref] = ayah_plan
        for field in ("primaryFloor_tr", "governingMovement_tr", "standaloneRequirement_tr"):
            require_nonempty(ayah_plan.get(field), f"{where}.{field}", errors)
        placements = require_array(ayah_plan.get("placements"), f"{where}.placements", errors)
        if not placements:
            errors.append(f"{where}.placements: at least one placement is required")
        seen_placements: list[str] = []
        for placement_index, placement in enumerate(placements):
            pwhere = f"{where}.placements[{placement_index}]"
            if not isinstance(placement, dict):
                errors.append(f"{pwhere}: expected object")
                continue
            placement_id = placement.get("placementId")
            if not isinstance(placement_id, str) or not ID_RE.fullmatch(placement_id):
                errors.append(f"{pwhere}.placementId: invalid id")
                continue
            seen_placements.append(placement_id)
            placement_lookup[(str(ayah_ref), placement_id)] = placement
            require_nonempty(
                placement.get("paragraphPurpose_tr"),
                f"{pwhere}.paragraphPurpose_tr",
                errors,
            )
            require_nonempty(
                placement.get("localReturn_tr"), f"{pwhere}.localReturn_tr", errors
            )
            finding_refs = require_array(
                placement.get("findingRefs"), f"{pwhere}.findingRefs", errors
            )
            synthesis_refs = require_array(
                placement.get("synthesisRefs"), f"{pwhere}.synthesisRefs", errors
            )
            for ref in finding_refs:
                if isinstance(ref, str):
                    placement_findings.setdefault(ref, []).append(
                        (str(ayah_ref), placement_id)
                    )
            for ref in synthesis_refs:
                if isinstance(ref, str):
                    placement_syntheses.setdefault(ref, []).append(
                        (str(ayah_ref), placement_id)
                    )
        duplicates = duplicate_values(seen_placements)
        if duplicates:
            errors.append(f"{where}.placements: duplicate ids {duplicates}")
        require_array(ayah_plan.get("layer3HandoffIds"), f"{where}.layer3HandoffIds", errors)
    if set(plan_by_ayah) != set(ref for ref in ayah_refs if isinstance(ref, str)):
        errors.append("plan.ayahPlans: must contain exactly one plan for every ayahRef")

    syntheses = require_array(
        data.get("editorialSyntheses"), "plan.editorialSyntheses", errors
    )
    synthesis_by_id: dict[str, dict[str, Any]] = {}
    for index, synthesis in enumerate(syntheses):
        where = f"plan.editorialSyntheses[{index}]"
        if not isinstance(synthesis, dict):
            errors.append(f"{where}: expected object")
            continue
        synthesis_id = synthesis.get("synthesisId")
        if not isinstance(synthesis_id, str) or not EDITORIAL_SYNTHESIS_RE.fullmatch(
            synthesis_id
        ):
            errors.append(f"{where}.synthesisId: invalid id")
            continue
        if synthesis_id in synthesis_by_id:
            errors.append(f"{where}.synthesisId: duplicate {synthesis_id}")
        synthesis_by_id[synthesis_id] = synthesis
        owner = synthesis.get("ownerAyahRef")
        if owner not in plan_by_ayah:
            errors.append(f"{where}.ownerAyahRef: owner is outside the pericope")
        components = require_array(
            synthesis.get("componentFindingRefs"),
            f"{where}.componentFindingRefs",
            errors,
        )
        if len(components) < 2:
            errors.append(f"{where}.componentFindingRefs: need at least two findings")
        if synthesis_id not in placement_syntheses:
            errors.append(f"{where}: synthesis is not assigned to a placement")
        elif not any(ayah == owner for ayah, _ in placement_syntheses[synthesis_id]):
            errors.append(f"{where}: synthesis is not placed in its owner ayah")

    for ref in placement_syntheses:
        if ref not in synthesis_by_id:
            errors.append(f"plan placements: unknown synthesis ref {ref}")

    coverage = require_array(data.get("findingCoverage"), "plan.findingCoverage", errors)
    coverage_by_ref: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(coverage):
        where = f"plan.findingCoverage[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{where}: expected object")
            continue
        ref = item.get("findingRef")
        if not isinstance(ref, str) or not FINDING_RE.fullmatch(ref):
            errors.append(f"{where}.findingRef: invalid id")
            continue
        if ref in coverage_by_ref:
            errors.append(f"{where}.findingRef: duplicate coverage row")
        coverage_by_ref[ref] = item
        disposition = item.get("disposition")
        if disposition not in {"represented", "upstream-blocked"}:
            errors.append(f"{where}.disposition: invalid value")
        source_ayah = item.get("sourceAyahRef")
        validate_ayah_ref(source_ayah, surah, f"{where}.sourceAyahRef", errors)
        if disposition == "represented":
            owner = item.get("ownerAyahRef")
            placement_id = item.get("placementId")
            if owner != source_ayah:
                errors.append(
                    f"{where}.ownerAyahRef: Layer 2 finding must remain with its source ayah"
                )
            if (str(owner), str(placement_id)) not in placement_lookup:
                errors.append(f"{where}: owner placement does not exist")
            if ref not in placement_findings:
                errors.append(f"{where}: represented finding is absent from placements")
            elif (str(owner), str(placement_id)) not in placement_findings[ref]:
                errors.append(f"{where}: coverage placement does not contain finding")
        elif not str(item.get("reason_tr", "")).strip():
            errors.append(f"{where}.reason_tr: upstream-blocked finding needs a reason")

    if ledgers is not None:
        ledger_list = list(ledgers)
        by_ayah, findings, index_errors = ledger_index(ledger_list)
        errors.extend(index_errors)
        if set(by_ayah) != set(ref for ref in ayah_refs if isinstance(ref, str)):
            errors.append("plan.ayahRefs: do not match supplied ledger ayahs")
        if data.get("surah") and any(
            ledger.get("surah") != data.get("surah") for ledger in ledger_list
        ):
            errors.append("plan.surah: supplied ledger belongs to another surah")
        if set(coverage_by_ref) != set(findings):
            missing = sorted(set(findings) - set(coverage_by_ref))
            extra = sorted(set(coverage_by_ref) - set(findings))
            if missing:
                errors.append(f"plan.findingCoverage: missing findings {missing}")
            if extra:
                errors.append(f"plan.findingCoverage: unknown findings {extra}")
        for ref, finding in findings.items():
            row = coverage_by_ref.get(ref)
            if row is None:
                continue
            expected = (
                "represented"
                if finding.get("disposition") == "carry"
                else "upstream-blocked"
            )
            if row.get("disposition") != expected:
                errors.append(
                    f"plan.findingCoverage[{ref}]: expected {expected} from discovery"
                )
            if finding.get("disposition") == "carry":
                source_ayah = ref.rsplit(":", 1)[0]
                for owner, _ in placement_findings.get(ref, []):
                    if owner != source_ayah:
                        errors.append(
                            f"plan placements: finding {ref} moved to another ayah"
                        )
            elif ref in placement_findings:
                errors.append(f"plan placements: blocked finding {ref} entered a placement")
        for synthesis_id, synthesis in synthesis_by_id.items():
            for ref in synthesis.get("componentFindingRefs", []):
                if ref not in findings:
                    errors.append(
                        f"plan.editorialSyntheses[{synthesis_id}]: unknown finding {ref}"
                    )
                elif findings[ref].get("disposition") != "carry":
                    errors.append(
                        f"plan.editorialSyntheses[{synthesis_id}]: blocked component {ref}"
                    )
        for ref in placement_findings:
            if ref not in findings:
                errors.append(f"plan placements: unknown finding ref {ref}")
        if ledger_paths is not None:
            path_list = list(ledger_paths)
            if len(path_list) != len(ledger_list):
                errors.append("plan.sourceLedgers: ledger/path count mismatch")
            else:
                actual_hashes = {
                    ledger.get("ayahRef"): sha256_path(path)
                    for ledger, path in zip(ledger_list, path_list)
                }
                if source_ledger_hashes != actual_hashes:
                    errors.append(
                        "plan.sourceLedgers: hashes do not match supplied ledger files"
                    )
    return errors


def validate_registry_data(
    data: dict[str, Any],
    ledgers: Iterable[dict[str, Any]] | None = None,
    plan_path: Path | None = None,
    ledger_paths: Iterable[Path] | None = None,
) -> list[str]:
    errors: list[str] = []
    if data.get("schemaVersion") != "commentary-v2-channel-registry-v1":
        errors.append("registry.schemaVersion: unexpected value")
    surah = data.get("surah")
    if not isinstance(surah, int) or isinstance(surah, bool) or not 1 <= surah <= 114:
        errors.append("registry.surah: expected integer 1 through 114")
        surah = 0
    if not isinstance(data.get("pericopeId"), str) or not ID_RE.fullmatch(
        data.get("pericopeId", "")
    ):
        errors.append("registry.pericopeId: invalid id")
    source_ledgers = require_array(
        data.get("sourceLedgers"), "registry.sourceLedgers", errors
    )
    source_ledger_refs: list[str] = []
    for index, item in enumerate(source_ledgers):
        where = f"registry.sourceLedgers[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{where}: expected object")
            continue
        ref = item.get("ayahRef")
        validate_ayah_ref(ref, surah, f"{where}.ayahRef", errors)
        if isinstance(ref, str):
            source_ledger_refs.append(ref)
        digest = item.get("sha256")
        if not isinstance(digest, str) or not SHA_RE.fullmatch(digest):
            errors.append(f"{where}.sha256: invalid SHA-256")
    if duplicate_values(source_ledger_refs):
        errors.append("registry.sourceLedgers: duplicate ayah references")

    finding_map: dict[str, dict[str, Any]] = {}
    if ledgers is not None:
        ledger_list = list(ledgers)
        ledger_by_ayah, finding_map, index_errors = ledger_index(ledger_list)
        errors.extend(index_errors)
        if set(source_ledger_refs) != set(ledger_by_ayah):
            errors.append("registry.sourceLedgers: do not match supplied ledger ayahs")
        if ledger_paths is not None:
            path_list = list(ledger_paths)
            actual_hashes = {
                ledger.get("ayahRef"): sha256_path(path)
                for ledger, path in zip(ledger_list, path_list)
            }
            declared_hashes = {
                item.get("ayahRef"): item.get("sha256")
                for item in source_ledgers
                if isinstance(item, dict)
            }
            if len(path_list) != len(ledger_list):
                errors.append("registry.sourceLedgers: ledger/path count mismatch")
            elif declared_hashes != actual_hashes:
                errors.append(
                    "registry.sourceLedgers: hashes do not match supplied ledger files"
                )
    if plan_path is not None:
        try:
            plan = load_json(plan_path)
        except ValueError as exc:
            errors.append(f"registry editorial plan: {exc}")
        else:
            plan_refs = {
                item.get("ayahRef")
                for item in plan.get("sourceLedgers", [])
                if isinstance(item, dict)
            }
            if set(source_ledger_refs) != plan_refs:
                errors.append("registry.sourceLedgers: do not match editorial plan")

    channels = require_array(data.get("channels"), "registry.channels", errors)
    channel_ids: list[str] = []
    for index, channel in enumerate(channels):
        where = f"registry.channels[{index}]"
        if not isinstance(channel, dict):
            errors.append(f"{where}: expected object")
            continue
        candidate_id = channel.get("candidateId")
        if not isinstance(candidate_id, str) or not ID_RE.fullmatch(candidate_id):
            errors.append(f"{where}.candidateId: invalid id")
            continue
        channel_ids.append(candidate_id)
        for field in ("name_tr", "invariant_tr"):
            require_nonempty(channel.get(field), f"{where}.{field}", errors)
        chain = require_array(
            channel.get("reasoningChain_tr"), f"{where}.reasoningChain_tr", errors
        )
        if not chain:
            errors.append(f"{where}.reasoningChain_tr: at least one step is required")
        members = require_array(channel.get("members"), f"{where}.members", errors)
        if len(members) < 2:
            errors.append(f"{where}.members: a channel needs at least two members")
        member_ids: list[str] = []
        member_ayahs: set[str] = set()
        for member_index, member in enumerate(members):
            mwhere = f"{where}.members[{member_index}]"
            if not isinstance(member, dict):
                errors.append(f"{mwhere}: expected object")
                continue
            member_id = member.get("memberId")
            if not isinstance(member_id, str) or not ID_RE.fullmatch(member_id):
                errors.append(f"{mwhere}.memberId: invalid id")
            else:
                member_ids.append(member_id)
            ref = member.get("findingRef")
            ayah_ref = member.get("ayahRef")
            validate_ayah_ref(ayah_ref, surah, f"{mwhere}.ayahRef", errors)
            if isinstance(ayah_ref, str):
                member_ayahs.add(ayah_ref)
            require_nonempty(member.get("localAnchor_tr"), f"{mwhere}.localAnchor_tr", errors)
            require_nonempty(
                member.get("contribution_tr"), f"{mwhere}.contribution_tr", errors
            )
            evidence = require_array(
                member.get("evidenceRefs"), f"{mwhere}.evidenceRefs", errors
            )
            if not evidence:
                errors.append(f"{mwhere}.evidenceRefs: at least one reference is required")
            if finding_map:
                finding = finding_map.get(ref)
                if finding is None:
                    errors.append(f"{mwhere}.findingRef: unknown finding {ref!r}")
                elif finding.get("disposition") != "carry":
                    errors.append(f"{mwhere}.findingRef: blocked finding cannot be a member")
                elif isinstance(ref, str) and ref.rsplit(":", 1)[0] != ayah_ref:
                    errors.append(f"{mwhere}: findingRef and ayahRef disagree")
        duplicates = duplicate_values(member_ids)
        if duplicates:
            errors.append(f"{where}.members: duplicate member ids {duplicates}")
        if len(member_ayahs) < 2:
            errors.append(f"{where}.members: a channel must cross at least two ayahs")
        require_array(channel.get("counterEvidence"), f"{where}.counterEvidence", errors)
        if channel.get("crossPericopeStatus") not in {
            "self-contained",
            "may-continue",
            "known-continuation",
        }:
            errors.append(f"{where}.crossPericopeStatus: invalid value")
    duplicates = duplicate_values(channel_ids)
    if duplicates:
        errors.append(f"registry.channels: duplicate candidate ids {duplicates}")
    return errors


def validate_layer2_result_data(
    data: dict[str, Any],
    result_path: Path | None = None,
    ledger: dict[str, Any] | None = None,
    ledger_path: Path | None = None,
    plan: dict[str, Any] | None = None,
    plan_path: Path | None = None,
) -> list[str]:
    errors: list[str] = []
    if data.get("schemaVersion") != "commentary-v2-layer2-editorial-result-v1":
        errors.append("result.schemaVersion: unexpected value")
    surah = data.get("surah")
    if not isinstance(surah, int) or isinstance(surah, bool):
        errors.append("result.surah: invalid value")
        surah = 0
    ayah_ref = data.get("ayahRef")
    validate_ayah_ref(ayah_ref, surah, "result.ayahRef", errors)
    for field in ("sourceLedgerSha256", "sourcePlanSha256"):
        value = data.get(field)
        if not isinstance(value, str) or not SHA_RE.fullmatch(value):
            errors.append(f"result.{field}: invalid SHA-256")
    if ledger_path is not None and data.get("sourceLedgerSha256") != sha256_path(ledger_path):
        errors.append("result.sourceLedgerSha256: does not match ledger")
    if plan_path is not None and data.get("sourcePlanSha256") != sha256_path(plan_path):
        errors.append("result.sourcePlanSha256: does not match plan")

    represented = require_array(
        data.get("representedFindingRefs"), "result.representedFindingRefs", errors
    )
    represented_set = {item for item in represented if isinstance(item, str)}
    if len(represented_set) != len(represented):
        errors.append("result.representedFindingRefs: duplicate or invalid refs")
    represented_syntheses = require_array(
        data.get("representedSynthesisRefs"),
        "result.representedSynthesisRefs",
        errors,
    )
    synthesis_set = {
        item for item in represented_syntheses if isinstance(item, str)
    }
    if len(synthesis_set) != len(represented_syntheses):
        errors.append("result.representedSynthesisRefs: duplicate or invalid refs")

    new_syntheses = require_array(data.get("newSyntheses"), "result.newSyntheses", errors)
    new_ids: set[str] = set()
    for index, synthesis in enumerate(new_syntheses):
        where = f"result.newSyntheses[{index}]"
        if not isinstance(synthesis, dict):
            errors.append(f"{where}: expected object")
            continue
        synthesis_id = synthesis.get("synthesisId")
        if not isinstance(synthesis_id, str) or not AUTHOR_SYNTHESIS_RE.fullmatch(
            synthesis_id
        ):
            errors.append(f"{where}.synthesisId: invalid author synthesis id")
            continue
        if synthesis_id in new_ids:
            errors.append(f"{where}.synthesisId: duplicate")
        new_ids.add(synthesis_id)
        components = require_array(
            synthesis.get("componentFindingRefs"),
            f"{where}.componentFindingRefs",
            errors,
        )
        if len(components) < 2:
            errors.append(f"{where}.componentFindingRefs: need at least two findings")
        evidence = require_array(
            synthesis.get("evidenceRefs"), f"{where}.evidenceRefs", errors
        )
        if not evidence:
            errors.append(f"{where}.evidenceRefs: at least one reference is required")
    if not new_ids.issubset(synthesis_set):
        errors.append("result.representedSynthesisRefs: missing new author synthesis")

    checks = data.get("standaloneCheck")
    if not isinstance(checks, dict):
        errors.append("result.standaloneCheck: expected object")
    else:
        for field in (
            "primaryReachable",
            "outsideAyahWordsGrounded",
            "surahThesisAbsent",
            "allPlannedFindingsRepresented",
        ):
            if checks.get(field) is not True:
                errors.append(f"result.standaloneCheck.{field}: must be true")

    outputs = data.get("outputs")
    if not isinstance(outputs, dict):
        errors.append("result.outputs: expected object")
    else:
        for field in ("prose", "evidence", "index", "friction"):
            require_nonempty(outputs.get(field), f"result.outputs.{field}", errors)
            if result_path is not None and isinstance(outputs.get(field), str):
                declared = Path(outputs[field])
                candidates = (
                    [declared]
                    if declared.is_absolute()
                    else [result_path.parent / declared, REPO_ROOT / declared]
                )
                existing = next((path for path in candidates if path.is_file()), None)
                if existing is None:
                    errors.append(
                        f"result.outputs.{field}: file does not exist: "
                        + " or ".join(str(path) for path in candidates)
                    )
                elif not existing.read_text(encoding="utf-8").strip():
                    errors.append(f"result.outputs.{field}: file is empty: {existing}")

    if ledger is not None:
        carried = {
            finding["findingId"]
            for finding in ledger.get("findings", [])
            if isinstance(finding, dict) and finding.get("disposition") == "carry"
        }
        if represented_set != carried:
            missing = sorted(carried - represented_set)
            extra = sorted(represented_set - carried)
            if missing:
                errors.append(f"result.representedFindingRefs: missing {missing}")
            if extra:
                errors.append(f"result.representedFindingRefs: unknown {extra}")
    if plan is not None:
        plan_refs: set[str] = set()
        plan_syntheses: set[str] = set()
        for ayah_plan in plan.get("ayahPlans", []):
            if not isinstance(ayah_plan, dict) or ayah_plan.get("ayahRef") != ayah_ref:
                continue
            for placement in ayah_plan.get("placements", []):
                if not isinstance(placement, dict):
                    continue
                plan_refs.update(placement.get("findingRefs", []))
                plan_syntheses.update(placement.get("synthesisRefs", []))
        if not plan_refs.issubset(represented_set):
            errors.append(
                "result.representedFindingRefs: does not cover the ayah plan"
            )
        if not plan_syntheses.issubset(synthesis_set):
            errors.append(
                "result.representedSynthesisRefs: does not cover the ayah plan"
            )
    return errors


def validate_layer3_result_data(
    data: dict[str, Any],
    registry: dict[str, Any] | None = None,
    registry_path: Path | None = None,
    result_path: Path | None = None,
) -> list[str]:
    errors: list[str] = []
    if data.get("schemaVersion") != "commentary-v2-layer3-result-v1":
        errors.append("result.schemaVersion: unexpected value")
    source_sha = data.get("sourceRegistrySha256")
    if not isinstance(source_sha, str) or not SHA_RE.fullmatch(source_sha):
        errors.append("result.sourceRegistrySha256: invalid SHA-256")
    if registry_path is not None and source_sha != sha256_path(registry_path):
        errors.append("result.sourceRegistrySha256: does not match registry")
    outputs = data.get("outputs")
    if not isinstance(outputs, dict):
        errors.append("result.outputs: expected object")
    else:
        for field in ("prose", "evidence", "friction"):
            require_nonempty(outputs.get(field), f"result.outputs.{field}", errors)
            if result_path is not None and isinstance(outputs.get(field), str):
                declared = Path(outputs[field])
                candidates = (
                    [declared]
                    if declared.is_absolute()
                    else [result_path.parent / declared, REPO_ROOT / declared]
                )
                existing = next((path for path in candidates if path.is_file()), None)
                if existing is None:
                    errors.append(
                        f"result.outputs.{field}: file does not exist: "
                        + " or ".join(str(path) for path in candidates)
                    )
                elif not existing.read_text(encoding="utf-8").strip():
                    errors.append(f"result.outputs.{field}: file is empty: {existing}")
    channels = require_array(data.get("channels"), "result.channels", errors)
    result_channel_ids: set[str] = set()
    used_candidates: set[str] = set()
    for index, channel in enumerate(channels):
        where = f"result.channels[{index}]"
        if not isinstance(channel, dict):
            errors.append(f"{where}: expected object")
            continue
        channel_id = channel.get("channelId")
        if not isinstance(channel_id, str) or not ID_RE.fullmatch(channel_id):
            errors.append(f"{where}.channelId: invalid id")
        elif channel_id in result_channel_ids:
            errors.append(f"{where}.channelId: duplicate")
        else:
            result_channel_ids.add(channel_id)
        source_ids = require_array(
            channel.get("sourceCandidateIds"), f"{where}.sourceCandidateIds", errors
        )
        if not source_ids:
            errors.append(f"{where}.sourceCandidateIds: at least one is required")
        used_candidates.update(item for item in source_ids if isinstance(item, str))
        member_refs = require_array(
            channel.get("memberFindingRefs"), f"{where}.memberFindingRefs", errors
        )
        if len(member_refs) < 2:
            errors.append(f"{where}.memberFindingRefs: need at least two findings")
        ayahs = require_array(channel.get("ayahSequence"), f"{where}.ayahSequence", errors)
        if len(set(item for item in ayahs if isinstance(item, str))) < 2:
            errors.append(f"{where}.ayahSequence: channel must cross two ayahs")

    coverage = require_array(
        data.get("candidateCoverage"), "result.candidateCoverage", errors
    )
    coverage_by_id: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(coverage):
        where = f"result.candidateCoverage[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{where}: expected object")
            continue
        candidate_id = item.get("candidateId")
        if not isinstance(candidate_id, str) or not ID_RE.fullmatch(candidate_id):
            errors.append(f"{where}.candidateId: invalid id")
            continue
        if candidate_id in coverage_by_id:
            errors.append(f"{where}.candidateId: duplicate")
        coverage_by_id[candidate_id] = item
        if item.get("disposition") not in {
            "accepted",
            "merged",
            "revised",
            "rejected",
        }:
            errors.append(f"{where}.disposition: invalid value")
        require_nonempty(item.get("reason_tr"), f"{where}.reason_tr", errors)
        result_ids = item.get("resultChannelIds", [])
        if not isinstance(result_ids, list):
            errors.append(f"{where}.resultChannelIds: expected array")
        elif item.get("disposition") != "rejected" and not result_ids:
            errors.append(f"{where}.resultChannelIds: accepted candidate needs a result")
        elif any(channel_id not in result_channel_ids for channel_id in result_ids):
            errors.append(f"{where}.resultChannelIds: unknown result channel")

    if registry is not None:
        registry_ids = {
            channel["candidateId"]
            for channel in registry.get("channels", [])
            if isinstance(channel, dict) and isinstance(channel.get("candidateId"), str)
        }
        if set(coverage_by_id) != registry_ids:
            missing = sorted(registry_ids - set(coverage_by_id))
            extra = sorted(set(coverage_by_id) - registry_ids)
            if missing:
                errors.append(f"result.candidateCoverage: missing {missing}")
            if extra:
                errors.append(f"result.candidateCoverage: unknown {extra}")
        unknown_used = used_candidates - registry_ids
        if unknown_used:
            errors.append(f"result.channels: unknown source candidates {sorted(unknown_used)}")
    return errors


def validate_reconciliation_data(
    data: dict[str, Any],
    source_registries: Iterable[tuple[Path, dict[str, Any]]] | None = None,
    result_registry: dict[str, Any] | None = None,
) -> list[str]:
    errors: list[str] = []
    if data.get("schemaVersion") != "commentary-v2-registry-reconciliation-v1":
        errors.append("reconciliation.schemaVersion: unexpected value")
    surah = data.get("surah")
    if not isinstance(surah, int) or isinstance(surah, bool) or not 1 <= surah <= 114:
        errors.append("reconciliation.surah: expected integer 1 through 114")
        surah = 0
    source_rows = require_array(
        data.get("sourceRegistries"), "reconciliation.sourceRegistries", errors
    )
    declared_sources: dict[str, str] = {}
    for index, row in enumerate(source_rows):
        where = f"reconciliation.sourceRegistries[{index}]"
        if not isinstance(row, dict):
            errors.append(f"{where}: expected object")
            continue
        pericope_id = row.get("pericopeId")
        digest = row.get("sha256")
        if not isinstance(pericope_id, str) or not ID_RE.fullmatch(pericope_id):
            errors.append(f"{where}.pericopeId: invalid id")
            continue
        if pericope_id in declared_sources:
            errors.append(f"{where}.pericopeId: duplicate")
        if not isinstance(digest, str) or not SHA_RE.fullmatch(digest):
            errors.append(f"{where}.sha256: invalid SHA-256")
        declared_sources[pericope_id] = str(digest)

    source_candidates: set[tuple[str, str]] = set()
    if source_registries is not None:
        actual_sources: dict[str, str] = {}
        for path, registry in source_registries:
            pericope_id = registry.get("pericopeId")
            if not isinstance(pericope_id, str):
                continue
            actual_sources[pericope_id] = sha256_path(path)
            if registry.get("surah") != surah:
                errors.append(
                    f"reconciliation source {pericope_id}: belongs to another surah"
                )
            for channel in registry.get("channels", []):
                if isinstance(channel, dict) and isinstance(
                    channel.get("candidateId"), str
                ):
                    source_candidates.add((pericope_id, channel["candidateId"]))
        if declared_sources != actual_sources:
            errors.append(
                "reconciliation.sourceRegistries: hashes do not match source files"
            )

    result_ids = {
        channel.get("candidateId")
        for channel in (result_registry or {}).get("channels", [])
        if isinstance(channel, dict) and isinstance(channel.get("candidateId"), str)
    }
    coverage = require_array(
        data.get("candidateCoverage"), "reconciliation.candidateCoverage", errors
    )
    covered: set[tuple[str, str]] = set()
    for index, row in enumerate(coverage):
        where = f"reconciliation.candidateCoverage[{index}]"
        if not isinstance(row, dict):
            errors.append(f"{where}: expected object")
            continue
        pericope_id = row.get("sourcePericopeId")
        candidate_id = row.get("sourceCandidateId")
        key = (str(pericope_id), str(candidate_id))
        if key in covered:
            errors.append(f"{where}: duplicate source candidate coverage")
        covered.add(key)
        if pericope_id not in declared_sources:
            errors.append(f"{where}.sourcePericopeId: unknown pericope")
        if not isinstance(candidate_id, str) or not ID_RE.fullmatch(candidate_id):
            errors.append(f"{where}.sourceCandidateId: invalid id")
        if row.get("disposition") not in {"represented", "merged"}:
            errors.append(f"{where}.disposition: invalid value")
        result_candidates = require_array(
            row.get("resultCandidateIds"), f"{where}.resultCandidateIds", errors
        )
        if not result_candidates:
            errors.append(f"{where}.resultCandidateIds: at least one is required")
        if result_registry is not None:
            unknown = set(result_candidates) - result_ids
            if unknown:
                errors.append(
                    f"{where}.resultCandidateIds: unknown candidates {sorted(unknown)}"
                )
        require_nonempty(row.get("reason_tr"), f"{where}.reason_tr", errors)
    if source_registries is not None and covered != source_candidates:
        missing = sorted(source_candidates - covered)
        extra = sorted(covered - source_candidates)
        if missing:
            errors.append(f"reconciliation.candidateCoverage: missing {missing}")
        if extra:
            errors.append(f"reconciliation.candidateCoverage: unknown {extra}")
    return errors


def load_ledger_dir(path: Path) -> tuple[list[dict[str, Any]], list[Path]]:
    if not path.is_dir():
        raise ValueError(f"ledger directory does not exist: {path}")
    paths = sorted(path.glob("*.ledger.json"))
    if not paths:
        raise ValueError(f"no *.ledger.json files in {path}")
    return [load_json(item) for item in paths], paths


def print_result(errors: list[str]) -> int:
    if not errors:
        print("ok")
        return 0
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "kind",
        choices=[
            "config",
            "ledger",
            "plan",
            "registry",
            "reconciliation",
            "layer2-result",
            "layer3-result",
        ],
    )
    parser.add_argument("path", type=Path)
    parser.add_argument("--ledger-dir", type=Path)
    parser.add_argument("--ledger", type=Path)
    parser.add_argument("--plan", type=Path)
    parser.add_argument("--registry", type=Path)
    parser.add_argument("--source-registry", type=Path, action="append")
    args = parser.parse_args()
    try:
        data = load_json(args.path)
        if args.kind == "config":
            errors = validate_run_config_data(data)
        elif args.kind == "ledger":
            errors = validate_ledger_data(data)
        elif args.kind == "plan":
            loaded = load_ledger_dir(args.ledger_dir) if args.ledger_dir else None
            errors = validate_plan_data(
                data,
                loaded[0] if loaded else None,
                loaded[1] if loaded else None,
            )
        elif args.kind == "registry":
            loaded = load_ledger_dir(args.ledger_dir) if args.ledger_dir else None
            errors = validate_registry_data(
                data,
                loaded[0] if loaded else None,
                args.plan,
                loaded[1] if loaded else None,
            )
        elif args.kind == "reconciliation":
            sources = (
                [(path, load_json(path)) for path in args.source_registry]
                if args.source_registry
                else None
            )
            result_registry = load_json(args.registry) if args.registry else None
            errors = validate_reconciliation_data(data, sources, result_registry)
        elif args.kind == "layer2-result":
            ledger = load_json(args.ledger) if args.ledger else None
            plan = load_json(args.plan) if args.plan else None
            errors = validate_layer2_result_data(
                data,
                args.path,
                ledger,
                args.ledger,
                plan,
                args.plan,
            )
        else:
            registry = load_json(args.registry) if args.registry else None
            errors = validate_layer3_result_data(
                data, registry, args.registry, args.path
            )
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return print_result(errors)


if __name__ == "__main__":
    raise SystemExit(main())
