#!/usr/bin/env python3
"""Render experimental prose-first v3 authoring prompts without running agents.

This is deliberately a prompt transport helper, not a prose validator. It
projects the complete candidate docket into isolated lane packets, inlines each
packet into one hermetic prompt, and later composes reconciliation, lane-prose,
and canonical merge prompts from explicit response files. It remains separate
from the legacy ``workflow.py`` path until the prose prompts have been proven.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


V3_ROOT = Path(__file__).resolve().parent
REPO_ROOT = V3_ROOT.parents[1]
PROMPTS_ROOT = V3_ROOT / "prompts"
DEFAULT_INTER_AYAH_DIR = (
    REPO_ROOT.parent / "quran-data" / "data" / "analysis" / "inter-ayah"
)
DEFAULT_QURAN_TEXT = (
    REPO_ROOT.parent / "quran-data" / "data" / "text" / "quran-uthmani.tsv"
)
LANES = ("micro", "macro", "global")
HFT_RECORD_FIELDS = (
    ("baseline_models", "baseline_model", "model_id"),
    ("context_deltas", "context_delta", "model_id"),
    ("surprising_valid_outliers", "surprising_outlier", "outlier_id"),
)
INTER_AYAH_LABELS = {
    "strong",
    "medium",
    "weak",
    "no value",
    "contrast",
    "reject",
}
MEANINGFUL_INTER_AYAH_LABELS = INTER_AYAH_LABELS - {"no value", "reject"}
INTER_AYAH_FILE_RE = re.compile(
    r"focus_([1-9][0-9]*)_([1-9][0-9]*)_cutoff_100\.tsv"
)
MARKER_RE = re.compile(r"@@[A-Z0-9_]+@@")
ALLOWED_RUN_ROOTS = (
    Path("/private/tmp").resolve(),
    (V3_ROOT / "runs" / "authoring").resolve(),
)


def _load_object(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Cannot load JSON object {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise SystemExit(f"Expected a JSON object at {path}")
    return value


def _canonical_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _sha256_json(value: Any) -> str:
    return _sha256_bytes(_canonical_json(value).encode("utf-8"))


def _pretty_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"


def _ayah_parts(ayah_ref: str) -> tuple[int, int, str, str]:
    match = re.fullmatch(r"([1-9][0-9]*):([1-9][0-9]*)", ayah_ref)
    if not match:
        raise SystemExit(f"Invalid ayah reference: {ayah_ref!r}")
    surah, ayah = int(match.group(1)), int(match.group(2))
    return surah, ayah, f"s{surah:03d}", f"{surah}_{ayah}"


def _default_docket(ayah_ref: str) -> Path:
    _surah, _ayah, folder, stem = _ayah_parts(ayah_ref)
    return V3_ROOT / "inputs" / "adjudication" / folder / f"{stem}.docket.json"


def _default_source_bundle(ayah_ref: str) -> Path:
    _surah, _ayah, folder, stem = _ayah_parts(ayah_ref)
    return V3_ROOT / "inputs" / "source" / folder / f"{stem}.bundle.json"


def _stable_source_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT.parent))
    except ValueError:
        return path.name


def _quran_text_evidence(
    source_path: Path,
) -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
    try:
        source_path = source_path.resolve(strict=True)
        lines = source_path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise SystemExit(f"Cannot read Quran text source {source_path}: {exc}") from exc
    if not source_path.is_file():
        raise SystemExit(f"Quran text source is not a file: {source_path}")

    stable_path = _stable_source_path(source_path)
    evidence: dict[str, dict[str, Any]] = {}
    for line_number, line in enumerate(lines, 1):
        if not line:
            continue
        parts = line.split("|", 1)
        if len(parts) != 2:
            raise SystemExit(
                f"Malformed Quran text row at {source_path}:{line_number}"
            )
        ayah_ref, arabic = parts[0].strip(), parts[1].lstrip("\ufeff").strip()
        if not re.fullmatch(
            r"[1-9][0-9]*:(?:0|[1-9][0-9]*)", ayah_ref
        ) or not arabic:
            raise SystemExit(
                f"Malformed Quran text identity at {source_path}:{line_number}"
            )
        if ayah_ref in evidence:
            raise SystemExit(f"Duplicate Quran text ayah reference: {ayah_ref}")
        row = {
            "ayah_ref": ayah_ref,
            "arabic_uthmani": arabic,
            "source_pointer": f"{stable_path}#L{line_number}",
        }
        row["source_row_sha256"] = _sha256_json(row)
        evidence[ayah_ref] = row
    if not evidence:
        raise SystemExit(f"Quran text source is empty: {source_path}")
    return evidence, {
        "source_id": "quran-data/quran-uthmani",
        "source_path": stable_path,
        "source_sha256": _sha256_bytes(source_path.read_bytes()),
        "ayah_count": len(evidence),
    }


def _reciprocal_connection_evidence(
    focus_ref: str, source_dir: Path
) -> tuple[dict[str, list[dict[str, Any]]], dict[str, Any]]:
    try:
        source_dir = source_dir.resolve(strict=True)
    except OSError as exc:
        raise SystemExit(
            f"Cannot resolve reciprocal inter-ayah source directory {source_dir}: {exc}"
        ) from exc
    if not source_dir.is_dir():
        raise SystemExit(f"Reciprocal inter-ayah source is not a directory: {source_dir}")

    focus_surah = focus_ref.split(":", 1)[0]
    by_origin: dict[str, list[dict[str, Any]]] = {}
    scanned_documents = 0
    matched_rows = 0
    for path in sorted(source_dir.glob("focus_*_cutoff_100.tsv")):
        match = INTER_AYAH_FILE_RE.fullmatch(path.name)
        if match is None:
            continue
        scanned_documents += 1
        origin_ref = f"{int(match.group(1))}:{int(match.group(2))}"
        if origin_ref == focus_ref:
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except OSError as exc:
            raise SystemExit(f"Cannot read reciprocal source {path}: {exc}") from exc
        for line_number, line in enumerate(lines, 1):
            if not line:
                continue
            parts = line.split("\t", 2)
            if len(parts) != 3:
                continue
            label, target_ref, note = parts
            label = label.strip()
            target_ref = target_ref.strip()
            if label not in INTER_AYAH_LABELS and target_ref in INTER_AYAH_LABELS:
                label, target_ref = target_ref, label
            if target_ref != focus_ref:
                continue
            if label not in INTER_AYAH_LABELS:
                raise SystemExit(
                    f"Reciprocal row has an invalid label at {path}:{line_number}"
                )
            if label not in MEANINGFUL_INTER_AYAH_LABELS:
                continue
            stable_path = _stable_source_path(path)
            row_payload = {
                "origin_ref": origin_ref,
                "origin_label": label,
                "origin_note": note,
                "origin_pointer": f"{stable_path}#L{line_number}",
            }
            row_payload["origin_row_sha256"] = _sha256_json(row_payload)
            by_origin.setdefault(origin_ref, []).append(row_payload)
            matched_rows += 1

    if scanned_documents == 0:
        raise SystemExit(
            f"No reciprocal inter-ayah source documents found in {source_dir}"
        )
    for origin_ref in by_origin:
        by_origin[origin_ref].sort(
            key=lambda item: (
                item["origin_label"],
                item["origin_note"],
                item["origin_pointer"],
            )
        )
    return dict(sorted(by_origin.items())), {
        "source_id": "quran-data/inter-ayah-cutoff-100",
        "source_directory": _stable_source_path(source_dir),
        "scanned_document_count": scanned_documents,
        "meaningful_incoming_origin_count": len(by_origin),
        "meaningful_incoming_row_count": matched_rows,
        "meaningful_incoming_cross_surah_origin_count": sum(
            origin_ref.split(":", 1)[0] != focus_surah for origin_ref in by_origin
        ),
        "meaningful_incoming_same_surah_origin_count": sum(
            origin_ref.split(":", 1)[0] == focus_surah for origin_ref in by_origin
        ),
    }


def _read_prompt(name: str) -> str:
    path = PROMPTS_ROOT / name
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise SystemExit(f"Cannot read prompt template {path}: {exc}") from exc


def _render(template: str, replacements: dict[str, str], *, label: str) -> str:
    template_markers = set(MARKER_RE.findall(template))
    replacement_markers = set(replacements)
    if template_markers != replacement_markers:
        raise SystemExit(
            f"{label} marker contract disagrees; "
            f"missing={sorted(template_markers - replacement_markers)}, "
            f"extra={sorted(replacement_markers - template_markers)}"
        )
    rendered = template
    for marker, replacement in replacements.items():
        rendered = rendered.replace(marker, replacement)
    return rendered


def _resolve_run_dir(path: Path) -> Path:
    resolved = path.expanduser().resolve()
    for allowed_root in ALLOWED_RUN_ROOTS:
        try:
            relative = resolved.relative_to(allowed_root)
        except ValueError:
            continue
        if relative.parts:
            return resolved
    allowed = ", ".join(str(item) for item in ALLOWED_RUN_ROOTS)
    raise SystemExit(f"--run-dir must be a child of one of: {allowed}")


def _write(run_dir: Path, path: Path, text: str) -> None:
    resolved = path.resolve(strict=False)
    try:
        resolved.relative_to(run_dir)
    except ValueError as exc:
        raise SystemExit(f"Refusing write outside run directory: {path}") from exc
    if path.is_symlink():
        raise SystemExit(f"Refusing to replace symlink: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        path.parent.resolve().relative_to(run_dir)
    except ValueError as exc:
        raise SystemExit(f"Refusing write through escaped parent: {path}") from exc
    if path.exists():
        if not path.is_file():
            raise SystemExit(f"Refusing to replace non-file: {path}")
        if path.read_text(encoding="utf-8") == text:
            return
        raise SystemExit(f"Refusing to replace changed generated file: {path}")
    path.write_text(text, encoding="utf-8")


def _ensure_directory(run_dir: Path, path: Path) -> None:
    resolved = path.resolve(strict=False)
    try:
        resolved.relative_to(run_dir)
    except ValueError as exc:
        raise SystemExit(f"Refusing directory outside run directory: {path}") from exc
    if path.is_symlink():
        raise SystemExit(f"Refusing symlink directory: {path}")
    if path.exists() and not path.is_dir():
        raise SystemExit(f"Refusing non-directory path: {path}")
    path.mkdir(parents=True, exist_ok=True)
    try:
        path.resolve().relative_to(run_dir)
    except ValueError as exc:
        raise SystemExit(f"Refusing escaped directory: {path}") from exc


def _payload_hash_with_identity_field_removed(
    value: dict[str, Any], field: str
) -> str:
    payload = json.loads(_canonical_json(value))
    payload.get("identity", {}).pop(field, None)
    return _sha256_json(payload)


def _request_sha256(stage: str, inputs: dict[str, str]) -> str:
    return _sha256_json({"stage": stage, "inputs": inputs})


def _json_pointer_get(value: Any, pointer: str) -> Any:
    if not isinstance(pointer, str) or (pointer and not pointer.startswith("/")):
        raise SystemExit(f"Invalid source JSON pointer: {pointer!r}")
    current = value
    if not pointer:
        return current
    for raw_token in pointer[1:].split("/"):
        if re.search(r"~(?:[^01]|$)", raw_token):
            raise SystemExit(f"Invalid source JSON pointer escape: {pointer!r}")
        token = raw_token.replace("~1", "/").replace("~0", "~")
        if isinstance(current, dict) and token in current:
            current = current[token]
        elif isinstance(current, list) and re.fullmatch(r"0|[1-9][0-9]*", token):
            index = int(token)
            if index >= len(current):
                raise SystemExit(f"Source JSON pointer does not resolve: {pointer}")
            current = current[index]
        else:
            raise SystemExit(f"Source JSON pointer does not resolve: {pointer}")
    return current


ARABIC_ROOT_EQUIVALENTS = str.maketrans(
    {"آ": "ء", "أ": "ء", "إ": "ء", "ؤ": "ء", "ئ": "ء", "ى": "ي"}
)


def _normalized_ar(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    return re.sub(r"[\sـ]", "", value.translate(ARABIC_ROOT_EQUIVALENTS))


def _branch_semantic_detail(source_branch: Any) -> dict[str, Any]:
    if not isinstance(source_branch, dict):
        return {}
    detail: dict[str, Any] = {}
    for field in (
        "branch_image_ar",
        "what_is_ar",
        "what_is_not_ar",
        "image_ar",
        "image_en",
        "scope_ar",
        "scope_en",
        "source_phrase_ar",
        "neighbor_coverage_note",
        "source_note",
    ):
        value = source_branch.get(field)
        if isinstance(value, str) and value.strip():
            detail[field] = value.strip()

    # These source-side contrasts and attested gloss families can preserve the
    # difference between a vivid branch image and a merely neighboring sense.
    # Keep them losslessly available to discovery agents instead of projecting
    # only one compact branch gloss.
    for field in (
        "contextual_glosses",
        "lexical_glosses",
        "excluded_glosses",
        "neighbor_distinctions",
        "sources",
    ):
        value = source_branch.get(field)
        if isinstance(value, (list, dict)) and value:
            detail[field] = value

    identity = source_branch.get("identity_judgment")
    if isinstance(identity, dict):
        for source_field, target_field in (
            ("rationale", "identity_rationale"),
            ("boundary_note", "boundary_detail"),
        ):
            value = identity.get(source_field)
            if isinstance(value, str) and value.strip():
                detail[target_field] = value.strip()

    lexicalization = source_branch.get("lexicalization_scope")
    if isinstance(lexicalization, dict):
        note = lexicalization.get("note")
        if isinstance(note, str) and note.strip():
            detail["lexicalization_note"] = note.strip()

    concept_map = source_branch.get("concept_map")
    if isinstance(concept_map, dict):
        definition = concept_map.get("definition")
        if isinstance(definition, str) and definition.strip():
            detail["definition"] = definition.strip()
        facets = []
        for facet in concept_map.get("facets", []):
            if not isinstance(facet, dict):
                continue
            statement = facet.get("statement")
            if not isinstance(statement, str) or not statement.strip():
                continue
            facets.append(
                {
                    "facet_id": facet.get("facet_id"),
                    "role": facet.get("role"),
                    "statement": statement.strip(),
                }
            )
        if facets:
            detail["distinctive_facets"] = facets

    concept_gloss = source_branch.get("concept_gloss")
    if isinstance(concept_gloss, dict):
        text = concept_gloss.get("text")
        applicability = concept_gloss.get("applicability")
        if isinstance(text, str) and text.strip():
            detail["concept_gloss"] = text.strip()
        if isinstance(applicability, str) and applicability.strip():
            detail["applicability"] = applicability.strip()

    synthesis = source_branch.get("source_synthesis")
    if isinstance(synthesis, dict):
        summary = synthesis.get("common_summary")
        if isinstance(summary, str) and summary.strip():
            detail["source_summary"] = summary.strip()
        qualifications = []
        for item in synthesis.get("source_details", []):
            if not isinstance(item, dict):
                continue
            item_summary = item.get("summary")
            if not isinstance(item_summary, str) or not item_summary.strip():
                continue
            qualifications.append(
                {"kind": item.get("kind"), "summary": item_summary.strip()}
            )
        if qualifications:
            detail["source_qualifications"] = qualifications
    return detail


def _focus_root_occurrences(
    docket: dict[str, Any], root_id: Any, root_ar: Any
) -> list[dict[str, Any]]:
    root_key = _normalized_ar(root_ar)
    if not root_key and not isinstance(root_id, str):
        return []
    carriers = []
    for morpheme in docket.get("focus", {}).get("qac_morphemes", []):
        if not isinstance(morpheme, dict):
            continue
        qac_root = morpheme.get("root_ar")
        mapped_root_ids = docket.get("focus_root_mappings", {}).get(qac_root, [])
        mapped_match = isinstance(root_id, str) and root_id in mapped_root_ids
        fallback_match = _normalized_ar(qac_root) == root_key
        if not mapped_match and not fallback_match:
            continue
        carriers.append(
            {
                field: morpheme.get(field)
                for field in (
                    "qac_ref",
                    "qac_word_ref",
                    "surface_ar",
                    "lemma_ar",
                    "morpheme_role",
                    "pos",
                    "morph_features",
                )
            }
        )
    return carriers


def _focus_surface_evidence(docket: dict[str, Any]) -> dict[str, Any]:
    focus = docket.get("focus", {})
    word_rows: list[dict[str, Any]] = []
    for support in docket.get("support_registry", []):
        if not isinstance(support, dict) or support.get("source_type") != "word_analysis":
            continue
        pointer = support.get("json_pointer")
        if not isinstance(pointer, str) or not re.fullmatch(
            r"/word_analysis/words/[0-9]+", pointer
        ):
            continue
        text = support.get("text")
        if not isinstance(text, str):
            continue
        try:
            detail = json.loads(text)
        except json.JSONDecodeError:
            continue
        if not isinstance(detail, dict):
            continue
        word_index = int(pointer.rsplit("/", 1)[1])

        def display_parts(value: Any) -> dict[str, str]:
            if not isinstance(value, str):
                return {}
            match = re.fullmatch(
                r"\{\{ar:(.*?)\}\}\s*\(\{\{tr:(.*?)\}\}\)", value.strip()
            )
            if match is None:
                return {"note": value.strip()} if value.strip() else {}
            return {"arabic": match.group(1), "transliteration": match.group(2)}

        qac_ref_rows = focus.get("word_analysis_qac_refs", [])
        qac_refs = (
            qac_ref_rows[word_index] if word_index < len(qac_ref_rows) else []
        )
        word_rows.append(
            {
                "analysis_record_ref": support.get("source_local_id"),
                "qac_refs": qac_refs,
                "source_pointer": pointer,
                "surface": display_parts(detail.get("surface_display")),
                "root": display_parts(detail.get("root_display")),
                "analytic_gloss_range_en": detail.get("gloss_range"),
                "analytic_root_gloss_range_en": detail.get("root_gloss_range"),
            }
        )
    word_rows.sort(
        key=lambda item: int(str(item["source_pointer"]).rsplit("/", 1)[1])
    )
    return {
        "arabic_uthmani": focus.get("arabic_uthmani"),
        "qac_morphemes": focus.get("qac_morphemes", []),
        "word_analysis_refs": focus.get("word_analysis_refs", []),
        "word_analysis_qac_refs": focus.get("word_analysis_qac_refs", []),
        "word_rows": word_rows,
        "qualification": (
            "These records preserve supplied Arabic, transliteration, analytic "
            "gloss boundaries, and morphology for accurate prose. Analysis and "
            "QAC coordinates are internal provenance and must not appear in reader "
            "prose. English gloss ranges require a natural Turkish rendering. "
            "These are surface evidence, not a finding list and not proof of any "
            "secondary branch activation."
        ),
    }


def _locked_finding_assignments(
    reconciled: dict[str, Any],
) -> tuple[dict[str, dict[str, Any]], dict[str, list[str]]]:
    locked_findings = reconciled.get("locked_findings")
    if not isinstance(locked_findings, list) or any(
        not isinstance(finding, dict) for finding in locked_findings
    ):
        raise SystemExit("Reconciled findings lack a locked finding list")
    locked_refs = [
        finding.get("locked_finding_ref") for finding in locked_findings
    ]
    if any(not isinstance(ref, str) or not ref for ref in locked_refs):
        raise SystemExit("Every locked finding requires a nonempty reference")
    if len(set(locked_refs)) != len(locked_refs):
        raise SystemExit("Reconciled findings contain duplicate locked references")
    locked_by_ref = dict(zip(locked_refs, locked_findings, strict=True))

    assignments = reconciled.get("scope_assignments")
    if not isinstance(assignments, dict) or set(assignments) != set(LANES):
        raise SystemExit("Reconciled findings lack exact scope assignments")
    assigned_union: set[str] = set()
    for lane in LANES:
        assigned_refs = assignments[lane]
        if (
            not isinstance(assigned_refs, list)
            or any(
                not isinstance(item, str) or not item for item in assigned_refs
            )
            or len(set(assigned_refs)) != len(assigned_refs)
        ):
            raise SystemExit(f"Invalid {lane} scope assignment list")
        unknown = sorted(set(assigned_refs) - set(locked_by_ref))
        if unknown:
            raise SystemExit(
                f"{lane} assignments cite unknown locked findings: {unknown}"
            )
        assigned_union.update(assigned_refs)
    omitted = sorted(set(locked_by_ref) - assigned_union)
    if omitted:
        raise SystemExit(
            f"Locked findings omitted from all scope assignments: {omitted}"
        )
    return locked_by_ref, assignments


def _flatten_branches(
    docket: dict[str, Any],
    source_bundle: dict[str, Any],
    candidates: list[dict[str, Any]],
    supports: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    candidate_links: dict[str, list[dict[str, Any]]] = {}
    for candidate in candidates:
        if not isinstance(candidate, dict):
            continue
        refs = {
            branch_ref
            for field in (
                "branch_refs",
                "focus_branch_refs",
                "nominated_branch_refs",
                "unresolved_branch_refs",
            )
            for branch_ref in candidate.get(field, [])
            if isinstance(branch_ref, str) and branch_ref
        }
        for branch_ref in refs:
            candidate_links.setdefault(branch_ref, []).append(
                {
                    "candidate_id": candidate.get("candidate_id"),
                    "lane": candidate.get("lane"),
                }
            )

    support_links: dict[str, list[str]] = {}
    for support in supports:
        if not isinstance(support, dict):
            continue
        support_id = support.get("support_id")
        for branch_ref in support.get("branch_refs", []):
            if isinstance(branch_ref, str) and branch_ref:
                support_links.setdefault(branch_ref, []).append(support_id)

    def record(
        *,
        branch: dict[str, Any],
        registry: str,
        root_id: Any,
        root_ar: Any,
        gloss: Any,
        boundary: Any,
        status: Any,
        branch_kind: Any,
    ) -> dict[str, Any]:
        branch_ref = branch.get("branch_ref")
        source_pointer = branch.get("source_pointer")
        source_branch = (
            _json_pointer_get(source_bundle, source_pointer)
            if isinstance(source_pointer, str) and source_pointer
            else None
        )
        if not isinstance(source_branch, dict):
            raise SystemExit(f"Branch source is not an object: {branch_ref}")
        if registry == "focus" and source_branch.get("branch_ref") != branch_ref:
            raise SystemExit(f"Focus branch source identity mismatch: {branch_ref}")
        if registry == "nominated" and source_branch.get("root_id") != root_id:
            raise SystemExit(
                f"Nominated branch source root identity mismatch: {branch_ref}"
            )
        source_detail = _branch_semantic_detail(source_branch)
        return {
            "branch_ref": branch_ref,
            "registry": registry,
            "root_id": root_id,
            "root_ar": root_ar,
            "lexicon_identity_status": status,
            "branch_kind": branch_kind,
            "gloss": gloss,
            "boundary": boundary,
            "source_pointer": source_pointer,
            "semantic_detail": source_detail,
            "focus_root_occurrences": _focus_root_occurrences(
                docket, root_id, root_ar
            ),
            "root_occurrence_qualification": (
                "These are focus-ayah occurrences mapped to the same root. "
                "They identify possible surface carriers but do not prove that "
                "this branch sense is active. Activation still requires an "
                "independent linguistic or contextual trigger."
            ),
            "candidate_links": candidate_links.get(branch_ref, []),
            "support_links": sorted(
                item
                for item in support_links.get(branch_ref, [])
                if isinstance(item, str) and item
            ),
        }

    flattened: list[dict[str, Any]] = []
    for root in docket.get("branch_registry", []):
        for branch in root.get("branches", []):
            flattened.append(
                record(
                    branch=branch,
                    registry="focus",
                    root_id=root.get("root_id"),
                    root_ar=root.get("root_ar"),
                    status=branch.get("status"),
                    branch_kind=branch.get("branch_kind"),
                    gloss=branch.get("gloss"),
                    boundary=branch.get("boundary"),
                )
            )
    for branch in docket.get("nominated_branch_registry", []):
        flattened.append(
            record(
                branch=branch,
                registry="nominated",
                root_id=str(branch.get("branch_ref", "")).split("/", 1)[0],
                root_ar=branch.get("root_ar"),
                status=None,
                branch_kind=None,
                gloss=branch.get("image_en") or branch.get("image_ar"),
                boundary=branch.get("scope_en") or branch.get("scope_ar"),
            )
        )
    return flattened


def _hft_authoring_projection(
    docket: dict[str, Any], source_bundle: dict[str, Any]
) -> dict[str, Any]:
    """Project every parseable HFT insight without inheriting legacy gates.

    The prepared docket may legitimately keep strict provenance and publication
    checks. Those checks are qualifications at the experimental authoring
    boundary: they must not make readable linguistic material disappear before
    a scope agent can assess it.
    """

    focus_ref = str(docket["identity"]["ayah_ref"])
    pericope_refs = {
        ref
        for ref in docket["scope"]["pericope"].get("refs", [])
        if isinstance(ref, str)
    }
    raw_hft = source_bundle.get("v12_focus_trace_hermetic")
    source_present = raw_hft is not None
    unstructured_hft = (
        raw_hft
        if raw_hft is not None and not isinstance(raw_hft, dict)
        else None
    )
    hft = raw_hft if isinstance(raw_hft, dict) else {}
    docket_assessment = docket.get("scope", {}).get("hft")
    diagnostics: list[dict[str, Any]] = []
    records: list[dict[str, Any]] = []
    reader_metadata: list[dict[str, Any]] = []

    policy = {
        "parseable_hft_is_always_visible_to_authoring": True,
        "provenance_affects_qualification_not_visibility": True,
        "scope_mismatch_affects_lane_assignment_not_visibility": True,
        "unresolved_branch_citations_do_not_suppress_records": True,
        "every_assigned_record_requires_explicit_review": True,
    }
    if not source_present:
        diagnostics.append(
            {
                "source_pointer": "/v12_focus_trace_hermetic",
                "warning": "HFT payload is absent",
            }
        )
    elif unstructured_hft is not None:
        diagnostics.append(
            {
                "source_pointer": "/v12_focus_trace_hermetic",
                "warning": (
                    "HFT payload is not an object; its raw value is preserved as "
                    "a global unstructured review record"
                ),
            }
        )

    packet_summary = hft.get("packet_summary")
    packet_window = (
        packet_summary.get("window")
        if isinstance(packet_summary, dict)
        and isinstance(packet_summary.get("window"), list)
        else []
    )
    valid_packet_window = {
        ref
        for ref in packet_window
        if isinstance(ref, str)
        and re.fullmatch(r"[1-9][0-9]*:[1-9][0-9]*", ref)
    }
    if valid_packet_window == pericope_refs:
        packet_scope_relation = "exact_declared_pericope"
    elif pericope_refs and pericope_refs < valid_packet_window:
        packet_scope_relation = "broader_than_declared_pericope"
    elif valid_packet_window and valid_packet_window < pericope_refs:
        packet_scope_relation = "narrower_than_declared_pericope"
    else:
        packet_scope_relation = "different_or_unresolved"

    raw_readers = hft.get("readers")
    unstructured_readers = (
        raw_readers
        if raw_readers is not None and not isinstance(raw_readers, dict)
        else None
    )
    readers = raw_readers if isinstance(raw_readers, dict) else {}
    if unstructured_readers is not None:
        diagnostics.append(
            {
                "source_pointer": "/v12_focus_trace_hermetic/readers",
                "warning": (
                    "HFT readers value is not an object; its raw value is "
                    "preserved as a global unstructured review record"
                ),
            }
        )

    def add_record(
        *,
        reader_id: str,
        kind: str,
        item_id: str,
        source_pointer: str,
        raw_item: Any,
        reader_identity_status: str,
        anchor_refs: list[str],
        branch_refs: list[str],
        item_warnings: list[str],
        anchor_scope_complete: bool = True,
    ) -> None:
        unique_anchors = sorted(set(anchor_refs))
        unique_branches = sorted(set(branch_refs))
        if not anchor_scope_complete:
            owning_lane = "global"
            lane_basis = (
                "one or more HFT anchors could not be resolved, so the record "
                "is conservatively visible in the widest lane"
            )
            evidence_scope = "wider_or_unresolved_record"
        elif unique_anchors and set(unique_anchors) == {focus_ref}:
            owning_lane = "micro"
            lane_basis = "all explicit HFT anchors are the focus ayah"
            evidence_scope = "focus_ayah"
        elif unique_anchors and set(unique_anchors) <= pericope_refs:
            owning_lane = "macro"
            lane_basis = "all explicit HFT anchors lie in the declared pericope"
            evidence_scope = "declared_pericope"
        else:
            owning_lane = "global"
            lane_basis = (
                "one or more explicit HFT anchors lie beyond the declared pericope"
                if unique_anchors
                else "unanchored reader synthesis is assigned to the widest lane"
            )
            evidence_scope = "wider_record"

        hft_ref = "hft_" + _sha256_json(
            {
                "reader_id": reader_id,
                "kind": kind,
                "item_id": item_id,
                "source_pointer": source_pointer,
            }
        )[:20]
        support_id = "sup_" + _sha256_json(
            {
                "hft_ref": hft_ref,
                "raw_payload": raw_item,
            }
        )[:20]
        candidate_id = "cand_" + _sha256_json(
            {
                "ayah_ref": focus_ref,
                "lane": owning_lane,
                "hft_ref": hft_ref,
            }
        )[:20]
        records.append(
            {
                "hft_ref": hft_ref,
                "reader_id": reader_id,
                "kind": kind,
                "item_id": item_id,
                "source_local_id": f"{reader_id}:{item_id}",
                "source_pointer": source_pointer,
                "anchor_refs": unique_anchors,
                "branch_refs": unique_branches,
                "owning_lane": owning_lane,
                "lane_basis": lane_basis,
                "evidence_scope": evidence_scope,
                "candidate_id": candidate_id,
                "support_id": support_id,
                "raw_item": raw_item,
                "qualification": {
                    "reader_identity_status": reader_identity_status,
                    "packet_scope_relation": packet_scope_relation,
                    "anchor_scope_complete": anchor_scope_complete,
                    "record_warnings": list(dict.fromkeys(item_warnings)),
                    "authoring_effect": (
                        "Source qualifications affect epistemic status and "
                        "containment, never visibility or presumptive outcome."
                    ),
                },
            }
        )

    if unstructured_hft is not None:
        add_record(
            reader_id="unstructured_hft",
            kind="unstructured_hft_payload",
            item_id="unstructured_hft_payload",
            source_pointer="/v12_focus_trace_hermetic",
            raw_item=unstructured_hft,
            reader_identity_status="unresolved",
            anchor_refs=[],
            branch_refs=[],
            item_warnings=["top-level HFT payload is not an object"],
            anchor_scope_complete=False,
        )
    if unstructured_readers is not None:
        add_record(
            reader_id="unstructured_readers",
            kind="unstructured_hft_readers",
            item_id="unstructured_hft_readers",
            source_pointer="/v12_focus_trace_hermetic/readers",
            raw_item=unstructured_readers,
            reader_identity_status="unresolved",
            anchor_refs=[],
            branch_refs=[],
            item_warnings=["HFT readers value is not an object"],
            anchor_scope_complete=False,
        )

    def pointer_token(value: Any) -> str:
        return str(value).replace("~", "~0").replace("/", "~1")

    for extension_key, extension_value in hft.items():
        if extension_key in {"packet_summary", "readers"}:
            continue
        extension_pointer = (
            "/v12_focus_trace_hermetic/" + pointer_token(extension_key)
        )
        diagnostics.append(
            {
                "source_pointer": extension_pointer,
                "warning": (
                    "Unrecognized HFT envelope field is preserved as a global "
                    "review record"
                ),
            }
        )
        add_record(
            reader_id="hft_envelope",
            kind="hft_envelope_extension",
            item_id=f"envelope_extension:{extension_key}",
            source_pointer=extension_pointer,
            raw_item=extension_value,
            reader_identity_status="unresolved",
            anchor_refs=[],
            branch_refs=[],
            item_warnings=["unrecognized HFT envelope field"],
            anchor_scope_complete=False,
        )

    def summary_leaves(
        value: Any, source_pointer: str, path: tuple[str, ...] = ()
    ) -> list[tuple[tuple[str, ...], str, Any]]:
        leaves: list[tuple[tuple[str, ...], str, Any]] = []
        if isinstance(value, dict) and value:
            for key, child in value.items():
                leaves.extend(
                    summary_leaves(
                        child,
                        f"{source_pointer}/{pointer_token(key)}",
                        (*path, str(key)),
                    )
                )
        elif isinstance(value, list) and value:
            for index, child in enumerate(value):
                leaves.extend(
                    summary_leaves(
                        child,
                        f"{source_pointer}/{index}",
                        (*path, str(index)),
                    )
                )
        else:
            leaves.append((path, source_pointer, value))
        return leaves

    for reader_id in sorted(readers):
        raw_reader = readers[reader_id]
        reader_pointer = (
            "/v12_focus_trace_hermetic/readers/" + pointer_token(reader_id)
        )
        if not isinstance(reader_id, str) or not isinstance(raw_reader, dict):
            diagnostics.append(
                {
                    "source_pointer": reader_pointer,
                    "warning": (
                        "HFT reader response has invalid structure; its raw value "
                        "is preserved as a global unstructured review record"
                    ),
                }
            )
            add_record(
                reader_id=str(reader_id),
                kind="unstructured_hft_reader",
                item_id="unstructured_reader",
                source_pointer=reader_pointer,
                raw_item=raw_reader,
                reader_identity_status="unresolved",
                anchor_refs=[],
                branch_refs=[],
                item_warnings=["HFT reader response is not an object"],
                anchor_scope_complete=False,
            )
            continue
        packet_identity = raw_reader.get("packet_identity")
        reader_identity_status = (
            "identity_supplied_unverified"
            if isinstance(packet_identity, dict)
            else "legacy_unbound"
        )
        reader_metadata.append(
            {
                "reader_id": reader_id,
                "focus_ref": raw_reader.get("focus_ref"),
                "protocol": raw_reader.get("protocol"),
                "trace_kind": raw_reader.get("trace_kind"),
                "packet_identity": packet_identity,
                "identity_status": reader_identity_status,
                "source_pointer": reader_pointer,
            }
        )

        if "summary" in raw_reader:
            for summary_path, summary_pointer, summary_item in summary_leaves(
                raw_reader.get("summary"), f"{reader_pointer}/summary"
            ):
                path_label = "/".join(summary_path) or "value"
                add_record(
                    reader_id=reader_id,
                    kind="reader_summary_claim",
                    item_id=f"reader_summary:{path_label}",
                    source_pointer=summary_pointer,
                    raw_item=summary_item,
                    reader_identity_status=reader_identity_status,
                    anchor_refs=[],
                    branch_refs=[],
                    item_warnings=[
                        "Unanchored reader synthesis must be assessed as one "
                        "inventory item, not accepted as a surah thesis."
                    ],
                )

        recognized_reader_fields = {
            "reader_id",
            "focus_ref",
            "protocol",
            "trace_kind",
            "packet_identity",
            "summary",
            *(field for field, _kind, _id_field in HFT_RECORD_FIELDS),
        }
        for extension_key, extension_value in raw_reader.items():
            if extension_key in recognized_reader_fields:
                continue
            extension_pointer = (
                f"{reader_pointer}/{pointer_token(extension_key)}"
            )
            diagnostics.append(
                {
                    "source_pointer": extension_pointer,
                    "warning": (
                        "Unrecognized HFT reader field is preserved as a global "
                        "review record"
                    ),
                }
            )
            add_record(
                reader_id=reader_id,
                kind="hft_reader_extension",
                item_id=f"reader_extension:{extension_key}",
                source_pointer=extension_pointer,
                raw_item=extension_value,
                reader_identity_status=reader_identity_status,
                anchor_refs=[],
                branch_refs=[],
                item_warnings=["unrecognized HFT reader field"],
                anchor_scope_complete=False,
            )

        for field, kind, id_field in HFT_RECORD_FIELDS:
            raw_items = raw_reader.get(field)
            field_pointer = f"{reader_pointer}/{field}"
            if not isinstance(raw_items, list):
                diagnostics.append(
                    {
                        "source_pointer": field_pointer,
                        "warning": f"{field} is not an array",
                    }
                )
                if raw_items is not None:
                    add_record(
                        reader_id=reader_id,
                        kind=f"{kind}_unstructured_field",
                        item_id=f"{field}_unstructured",
                        source_pointer=field_pointer,
                        raw_item=raw_items,
                        reader_identity_status=reader_identity_status,
                        anchor_refs=[],
                        branch_refs=[],
                        item_warnings=[
                            f"{field} is not an array; raw JSON remains visible"
                        ],
                        anchor_scope_complete=False,
                    )
                continue
            for index, raw_item in enumerate(raw_items):
                source_pointer = f"{field_pointer}/{index}"
                item_warnings: list[str] = []
                if isinstance(raw_item, dict):
                    raw_item_id = raw_item.get(id_field)
                    item_id = (
                        raw_item_id.strip()
                        if isinstance(raw_item_id, str) and raw_item_id.strip()
                        else f"{field}_{index}"
                    )
                    if item_id == f"{field}_{index}":
                        item_warnings.append(
                            f"record has no nonempty {id_field}; fallback identity used"
                        )
                    activation_trace = raw_item.get("activation_trace")
                else:
                    item_id = f"{field}_{index}"
                    activation_trace = None
                    item_warnings.append(
                        "record is not an object; raw JSON remains visible"
                    )

                anchor_refs: list[str] = []
                branch_refs: list[str] = []
                anchor_scope_complete = True
                if not isinstance(activation_trace, list):
                    anchor_scope_complete = False
                    item_warnings.append(
                        "activation_trace is absent or is not an array"
                    )
                else:
                    for trace_index, trace in enumerate(activation_trace):
                        if not isinstance(trace, dict):
                            anchor_scope_complete = False
                            item_warnings.append(
                                f"activation_trace[{trace_index}] is not an object"
                            )
                            continue
                        source_ref = trace.get("source_ref")
                        if isinstance(source_ref, str) and re.fullmatch(
                            r"[1-9][0-9]*:[1-9][0-9]*", source_ref
                        ):
                            anchor_refs.append(source_ref)
                        else:
                            anchor_scope_complete = False
                            item_warnings.append(
                                f"activation_trace[{trace_index}] has no canonical "
                                "source_ref"
                            )
                        root_id = trace.get("mapped_root_id")
                        branch_id = trace.get("branch_id")
                        if (
                            isinstance(root_id, str)
                            and root_id
                            and isinstance(branch_id, str)
                            and branch_id
                        ):
                            branch_refs.append(f"{root_id}/{branch_id}")
                        elif root_id is not None or branch_id is not None:
                            item_warnings.append(
                                f"activation_trace[{trace_index}] has an incomplete "
                                "branch citation"
                            )
                add_record(
                    reader_id=reader_id,
                    kind=kind,
                    item_id=item_id,
                    source_pointer=source_pointer,
                    raw_item=raw_item,
                    reader_identity_status=reader_identity_status,
                    anchor_refs=anchor_refs,
                    branch_refs=branch_refs,
                    item_warnings=item_warnings,
                    anchor_scope_complete=anchor_scope_complete,
                )

    refs = [record["hft_ref"] for record in records]
    candidate_ids = [record["candidate_id"] for record in records]
    support_ids = [record["support_id"] for record in records]
    if len(refs) != len(set(refs)):
        raise SystemExit("HFT authoring projection produced duplicate record refs")
    if len(candidate_ids) != len(set(candidate_ids)):
        raise SystemExit("HFT authoring projection produced duplicate candidate IDs")
    if len(support_ids) != len(set(support_ids)):
        raise SystemExit("HFT authoring projection produced duplicate support IDs")

    manifest_fields = (
        "hft_ref",
        "reader_id",
        "kind",
        "item_id",
        "source_local_id",
        "source_pointer",
        "anchor_refs",
        "branch_refs",
        "owning_lane",
        "lane_basis",
        "candidate_id",
        "support_id",
        "qualification",
    )
    return {
        "policy": policy,
        "source_present": source_present,
        "packet_summary": packet_summary,
        "docket_assessment": docket_assessment,
        "reader_metadata": reader_metadata,
        "provenance": {
            "packet_scope_relation": packet_scope_relation,
            "legacy_docket_assessment": docket_assessment,
            "reader_identity": reader_metadata,
            "authoring_effect": (
                "This is one neutral source qualification. It controls "
                "epistemic status and containment, never evidence visibility "
                "or presumptive acceptance/rejection."
            ),
        },
        "records": records,
        "record_manifest": [
            {field: record[field] for field in manifest_fields}
            for record in records
        ],
        "lane_counts": {
            lane: sum(record["owning_lane"] == lane for record in records)
            for lane in LANES
        },
        "structured_insight_count": sum(
            record["kind"]
            in {"baseline_model", "context_delta", "surprising_outlier"}
            for record in records
        ),
        "reader_synthesis_count": sum(
            record["kind"] == "reader_summary_claim" for record in records
        ),
        "unstructured_record_count": sum(
            "unstructured" in record["kind"]
            or record["kind"].endswith("_extension")
            for record in records
        ),
        "diagnostics": diagnostics,
    }


def _lane_packet(
    docket: dict[str, Any],
    lane: str,
    source_bundle: dict[str, Any],
    hft_projection: dict[str, Any],
    reciprocal_evidence: dict[str, list[dict[str, Any]]],
    reciprocal_source_coverage: dict[str, Any],
    quran_text_evidence: dict[str, dict[str, Any]],
    quran_text_coverage: dict[str, Any],
) -> dict[str, Any]:
    assigned_hft = [
        record
        for record in hft_projection.get("records", [])
        if record.get("owning_lane") == lane
    ]
    hft_candidates = [
        {
            "candidate_id": record["candidate_id"],
            "ayah_ref": docket["identity"]["ayah_ref"],
            "lane": lane,
            "source_type": "hft",
            "source_local_id": record["source_local_id"],
            "source_pointer": record["source_pointer"],
            "kind": record["kind"],
            "title": record["item_id"],
            "scope": record["evidence_scope"],
            "anchor_refs": record["anchor_refs"],
            "branch_refs": record["branch_refs"],
            "support_ids": [record["support_id"]],
            "trust": record["qualification"]["reader_identity_status"],
            "hft_ref": record["hft_ref"],
            "lane_assignment_basis": record["lane_basis"],
            "provenance_qualification": record["qualification"],
            "authoring_origin": "lossless_raw_hft_projection",
            "obligation": "review",
        }
        for record in assigned_hft
    ]
    hft_supports: list[dict[str, Any]] = []
    for record in assigned_hft:
        anchor_evidence: list[dict[str, Any]] = []
        missing_anchor_refs: list[str] = []
        for anchor_ref in record["anchor_refs"]:
            evidence = quran_text_evidence.get(anchor_ref)
            if isinstance(evidence, dict):
                anchor_evidence.append(evidence)
            else:
                missing_anchor_refs.append(anchor_ref)
        hft_supports.append(
            {
                "support_id": record["support_id"],
                "source_type": "hft",
                "source_local_id": record["source_local_id"],
                "scope": lane,
                "json_pointer": record["source_pointer"],
                "role": "hft_nomination_evidence",
                "branch_refs": record["branch_refs"],
                "payload": record["raw_item"],
                "anchor_evidence": anchor_evidence,
                "anchor_evidence_coverage": {
                    "cited_anchor_count": len(record["anchor_refs"]),
                    "supplied_anchor_count": len(anchor_evidence),
                    "missing_anchor_refs": missing_anchor_refs,
                    "exact_arabic_is_surface_evidence_only": True,
                    "target_morphology_supplied": False,
                    "boundary": (
                        "Exact Arabic verifies surface contact only. HFT-stated "
                        "segmentation, word indices, roots, branches, and roles "
                        "remain attributed nominations unless independently "
                        "supplied elsewhere in this packet."
                    ),
                },
                "trust": record["qualification"]["reader_identity_status"],
                "qualification": record["qualification"],
            }
        )
    replace_legacy_hft_candidates = bool(hft_projection.get("records"))
    raw_candidates = [
        candidate
        for candidate in docket.get("candidates", [])
        if candidate.get("lane") == lane
        and not (
            replace_legacy_hft_candidates
            and candidate.get("source_type") == "hft"
        )
    ] + hft_candidates
    transport_fields = {
        "mandatory",
        "selection_eligible",
        "selection_ineligibility_reasons",
        "adjudicable",
        "obligation",
    }
    candidates = [
        {
            **{
                key: value
                for key, value in candidate.items()
                if key not in transport_fields
            },
            "commentary_obligation": candidate.get("obligation"),
        }
        for candidate in raw_candidates
    ]
    candidate_refs = [candidate.get("candidate_id") for candidate in candidates]
    if len(candidate_refs) != len(set(candidate_refs)):
        raise SystemExit(f"{lane} packet contains duplicate candidate IDs")
    support_ids = {
        support_id
        for candidate in candidates
        for support_id in candidate.get("support_ids", [])
    }
    supports = [
        support
        for support in docket.get("support_registry", [])
        if support.get("support_id") in support_ids
    ] + hft_supports
    support_refs = [support.get("support_id") for support in supports]
    if len(support_refs) != len(set(support_refs)):
        raise SystemExit(f"{lane} packet contains duplicate support IDs")
    if {item.get("support_id") for item in supports} != support_ids:
        missing = sorted(support_ids - {item.get("support_id") for item in supports})
        raise SystemExit(f"{lane} packet is missing candidate supports: {missing}")

    candidate_branch_refs = {
        branch_ref
        for candidate in candidates
        for field in (
            "branch_refs",
            "focus_branch_refs",
            "nominated_branch_refs",
            "unresolved_branch_refs",
        )
        for branch_ref in candidate.get(field, [])
    }
    support_branch_refs = {
        branch_ref
        for support in supports
        for branch_ref in support.get("branch_refs", [])
    }
    relevant_branch_refs = candidate_branch_refs | support_branch_refs
    flattened_branches = _flatten_branches(
        docket, source_bundle, candidates, supports
    )
    known_branches: dict[str, dict[str, Any]] = {}
    for item in flattened_branches:
        branch_ref = item.get("branch_ref")
        if not isinstance(branch_ref, str) or not branch_ref:
            continue
        if branch_ref in known_branches:
            raise SystemExit(f"Duplicate branch reference in lane atlas: {branch_ref}")
        known_branches[branch_ref] = item
    # Every lane needs the complete focus-root atlas to discover an uncandidate
    # contact. Scope isolation is carried by each lane's evidence and decision
    # question, not by hiding local semantic facets from macro/global readers.
    included_refs = {
        branch_ref
        for branch_ref, item in known_branches.items()
        if item.get("registry") == "focus"
    } | (relevant_branch_refs & set(known_branches))
    branches = [known_branches[branch_ref] for branch_ref in sorted(included_refs)]
    unresolved_branch_refs = sorted(relevant_branch_refs - set(known_branches))
    hft_branch_citations: dict[str, list[dict[str, Any]]] = {}
    for record in assigned_hft:
        raw_item = record.get("raw_item")
        traces = raw_item.get("activation_trace") if isinstance(raw_item, dict) else []
        if not isinstance(traces, list):
            continue
        for trace in traces:
            if not isinstance(trace, dict):
                continue
            root_id = trace.get("mapped_root_id")
            branch_id = trace.get("branch_id")
            if not (
                isinstance(root_id, str)
                and root_id
                and isinstance(branch_id, str)
                and branch_id
            ):
                continue
            branch_ref = f"{root_id}/{branch_id}"
            hft_branch_citations.setdefault(branch_ref, []).append(
                {
                    "hft_ref": record["hft_ref"],
                    "source_ref": trace.get("source_ref"),
                    "root": trace.get("root"),
                    "source_word_indices": trace.get("source_word_indices"),
                    "role": trace.get("role"),
                    "qualification": (
                        "This is the HFT reader's exact attributed branch role, "
                        "not an independently supplied lexicon entry."
                    ),
                }
            )
    branches.extend(
        {
            "branch_ref": branch_ref,
            "registry": "unresolved",
            "root_id": branch_ref.split("/", 1)[0],
            "root_ar": None,
            "lexicon_identity_status": "unresolved",
            "branch_kind": None,
            "gloss": None,
            "boundary": (
                "No separate registered branch descriptor is supplied. The exact "
                "HFT citation and attributed role remain reviewable, but they do "
                "not become independently verified lexicon evidence."
            ),
            "source_pointer": None,
            "semantic_detail": {},
            "focus_root_occurrences": [],
            "root_occurrence_qualification": (
                "No registered root occurrence is supplied; this unresolved "
                "citation cannot establish a branch carrier."
            ),
            "candidate_links": [
                {
                    "candidate_id": candidate.get("candidate_id"),
                    "lane": candidate.get("lane"),
                }
                for candidate in candidates
                if branch_ref
                in {
                    cited_ref
                    for field in (
                        "branch_refs",
                        "focus_branch_refs",
                        "nominated_branch_refs",
                        "unresolved_branch_refs",
                    )
                    for cited_ref in candidate.get(field, [])
                }
            ],
            "support_links": sorted(
                support.get("support_id")
                for support in supports
                if branch_ref in support.get("branch_refs", [])
                and isinstance(support.get("support_id"), str)
            ),
            "hft_citations": hft_branch_citations.get(branch_ref, []),
        }
        for branch_ref in unresolved_branch_refs
    )
    projected_refs = {item["branch_ref"] for item in branches}
    if not relevant_branch_refs <= projected_refs:
        raise SystemExit(f"{lane} packet failed to preserve every referenced branch")

    connection_registry: list[dict[str, Any]] = []
    connection_rows = source_bundle.get("inter_ayah_rows", [])
    if not isinstance(connection_rows, list):
        raise SystemExit("Source inter_ayah_rows must be a list")
    focus_ref = str(docket["identity"]["ayah_ref"])
    focus_surah = focus_ref.split(":", 1)[0]
    pericope_refs = set(docket["scope"]["pericope"].get("refs", []))

    def target_evidence(target_ref: str) -> dict[str, Any]:
        evidence = quran_text_evidence.get(target_ref)
        if not isinstance(evidence, dict):
            raise SystemExit(f"Quran text source lacks connection target {target_ref}")
        return evidence

    for index, row in enumerate(connection_rows):
        if not isinstance(row, dict):
            raise SystemExit(f"Malformed inter-ayah row at index {index}")
        target_ref = row.get("ref")
        if not isinstance(target_ref, str) or not re.fullmatch(
            r"[1-9][0-9]*:[1-9][0-9]*", target_ref
        ):
            raise SystemExit(f"Malformed inter-ayah target at index {index}")
        if target_ref == focus_ref:
            raise SystemExit(f"Self-referential inter-ayah row at index {index}")
        if target_ref in pericope_refs:
            owning_lane = "macro"
            relation_scope = "declared_pericope"
        else:
            owning_lane = "global"
            relation_scope = (
                "inter_surah"
                if target_ref.split(":", 1)[0] != focus_surah
                else "same_surah_beyond_pericope"
            )
        if lane != owning_lane:
            continue
        source_pointer = f"/inter_ayah_rows/{index}"
        connection_ref = "conn_" + _sha256_json(
            {
                "focus_ref": focus_ref,
                "target_ref": target_ref,
                "note": row.get("note"),
                "source_pointer": source_pointer,
            }
        )[:20]
        reverse_rows = reciprocal_evidence.get(target_ref, [])
        connection = {
            "connection_ref": connection_ref,
            "target_ref": target_ref,
            "relation_scope": relation_scope,
            "origin": "authored_focus_row",
            "prior_label": row.get("label"),
            "note": row.get("note"),
            "source_pointer": source_pointer,
            "target_evidence": target_evidence(target_ref),
            "reciprocal_evidence": reverse_rows,
            "qualification": {
                "prior_label_is_not_a_decision": True,
                "reciprocal_evidence_is_nomination_only": bool(reverse_rows),
                "reciprocal_origin_label_is_not_a_reverse_decision": bool(
                    reverse_rows
                ),
                "target_ayah_text_supplied": True,
                "target_morphology_supplied": False,
                "boundary": (
                    "Use this row to discover and assess the stated relation. "
                    "The exact target Arabic is supplied, but target morphology "
                    "and lexical analysis are not. Do not invent those missing "
                    "details or treat opposite-direction labels as verdicts."
                ),
            },
        }
        connection_registry.append(connection)

    if lane in {"macro", "global"}:
        authored_targets = {
            item["target_ref"]
            for item in connection_registry
        }
        for origin_ref, evidence_rows in reciprocal_evidence.items():
            origin_surah = origin_ref.split(":", 1)[0]
            if origin_ref in pericope_refs:
                owning_lane = "macro"
                relation_scope = "declared_pericope_reciprocal_seed"
            else:
                owning_lane = "global"
                relation_scope = (
                    "inter_surah_reciprocal_seed"
                    if origin_surah != focus_surah
                    else "same_surah_beyond_pericope_reciprocal_seed"
                )
            if lane != owning_lane or origin_ref in authored_targets:
                continue
            evidence_hashes = [
                item["origin_row_sha256"] for item in evidence_rows
            ]
            connection_ref = "conn_" + _sha256_json(
                {
                    "focus_ref": focus_ref,
                    "target_ref": origin_ref,
                    "origin": "derived_reciprocal_seed",
                    "origin_row_sha256": evidence_hashes,
                }
            )[:20]
            connection_registry.append(
                {
                    "connection_ref": connection_ref,
                    "target_ref": origin_ref,
                    "relation_scope": relation_scope,
                    "origin": "derived_reciprocal_seed",
                    "prior_label": None,
                    "note": None,
                    "source_pointer": None,
                    "source_pointers": [
                        item["origin_pointer"] for item in evidence_rows
                    ],
                    "target_evidence": target_evidence(origin_ref),
                    "reciprocal_evidence": evidence_rows,
                    "qualification": {
                        "derived_reciprocal_seed": True,
                        "origin_label_is_not_a_reverse_direction_decision": True,
                        "receiving_direction_requires_fresh_assessment": True,
                        "target_ayah_text_supplied": True,
                        "target_morphology_supplied": False,
                        "boundary": (
                            "The target ayah's document meaningfully linked back "
                            "to the focus ayah, but the focus document omitted the "
                            "reverse row. Treat the origin note only as a discovery "
                            "seed. Reassess the relation from the focus ayah using "
                            "the supplied exact target Arabic, do not invent missing "
                            "target morphology, and do not inherit its label as a "
                            "verdict."
                        ),
                    },
                }
            )
    connection_refs = [item["connection_ref"] for item in connection_registry]
    if len(connection_refs) != len(set(connection_refs)):
        raise SystemExit(f"Duplicate {lane} connection references")

    publication = source_bundle.get("v12_cross_run_publication")
    primary_floor = (
        publication.get("baseline") if isinstance(publication, dict) else None
    )
    hft_anchor_refs = sorted(
        {
            anchor_ref
            for record in assigned_hft
            for anchor_ref in record.get("anchor_refs", [])
        }
    )
    supplied_hft_anchor_refs = sorted(
        {
            evidence["ayah_ref"]
            for support in hft_supports
            for evidence in support.get("anchor_evidence", [])
        }
    )
    missing_hft_anchor_refs = sorted(
        set(hft_anchor_refs) - set(supplied_hft_anchor_refs)
    )
    packet: dict[str, Any] = {
        "schema_version": "commentary-v3-lane-evidence-packet-v1",
        "identity": {
            "ayah_ref": docket["identity"]["ayah_ref"],
            "lane": lane,
            "source_canonical_sha256": docket["identity"][
                "source_canonical_sha256"
            ],
            "docket_payload_sha256": docket["identity"]["docket_payload_sha256"],
        },
        "focus": docket["focus"],
        "primary_floor": primary_floor,
        "focus_surface_evidence": _focus_surface_evidence(docket),
        "scope": {
            "pericope": docket["scope"]["pericope"],
            "lane_contract": docket["scope"]["lane_contract"].get(lane),
            "hft": {
                "authoring_status": "visible_with_provenance_qualification",
                "assigned_record_count": len(assigned_hft),
                "authoring_policy": hft_projection.get("policy"),
            },
            "readiness": {
                "docket_ready": docket["adjudication_gate"].get("ready"),
                "docket_mode": docket["adjudication_gate"].get("mode"),
                "authoring_effect": (
                    "Docket readiness is reported for source provenance. HFT "
                    "visibility is governed by the authoring policy above."
                ),
            },
        },
        "candidate_inventory": candidates,
        "support_registry": supports,
        "branch_registry": branches,
        "connection_registry": connection_registry,
        "hft_evidence": {
            "policy": hft_projection.get("policy"),
            "source_present": hft_projection.get("source_present"),
            "packet_summary": hft_projection.get("packet_summary"),
            "provenance": hft_projection.get("provenance"),
            "lane_counts": hft_projection.get("lane_counts", {}),
            "structured_insight_count": hft_projection.get(
                "structured_insight_count", 0
            ),
            "reader_synthesis_count": hft_projection.get(
                "reader_synthesis_count", 0
            ),
            "unstructured_record_count": hft_projection.get(
                "unstructured_record_count", 0
            ),
            "assigned_record_count": len(assigned_hft),
            "assigned_records": [
                {
                    key: value
                    for key, value in record.items()
                    if key != "raw_item"
                }
                for record in assigned_hft
            ],
            "diagnostics": hft_projection.get("diagnostics", []),
            "anchor_evidence_coverage": {
                "cited_unique_anchor_count": len(hft_anchor_refs),
                "supplied_unique_anchor_count": len(supplied_hft_anchor_refs),
                "missing_anchor_refs": missing_hft_anchor_refs,
            },
            "payload_location": (
                "Each assigned record's exact raw payload and exact available "
                "anchor Arabic are in support_registry under its support_id."
            ),
        },
        "source_coverage": {
            "docket": docket["coverage"],
            "lane_candidate_count": len(candidates),
            "lane_support_count": len(supports),
            "lane_branch_count": len(branches),
            "assigned_hft_record_count": len(assigned_hft),
            "total_hft_record_count": len(hft_projection.get("records", [])),
            "hft_anchor_evidence_count": len(supplied_hft_anchor_refs),
            "missing_hft_anchor_refs": missing_hft_anchor_refs,
            "connection_count": len(connection_registry),
            "authored_connection_count": sum(
                item["origin"] == "authored_focus_row"
                for item in connection_registry
            ),
            "derived_reciprocal_seed_count": sum(
                item["origin"] == "derived_reciprocal_seed"
                for item in connection_registry
            ),
            "authored_connections_with_reciprocal_evidence": sum(
                item["origin"] == "authored_focus_row"
                and bool(item["reciprocal_evidence"])
                for item in connection_registry
            ),
            "connection_scopes": {
                scope: sum(
                    item["relation_scope"] == scope
                    for item in connection_registry
                )
                for scope in sorted(
                    {item["relation_scope"] for item in connection_registry}
                )
            },
            "reciprocal_source": (
                reciprocal_source_coverage if lane in {"macro", "global"} else None
            ),
            "quran_text_source": quran_text_coverage,
            "unresolved_branch_refs": unresolved_branch_refs,
            "source_types": sorted(
                {
                    candidate.get("source_type")
                    for candidate in candidates
                    if candidate.get("source_type")
                }
            ),
        },
        "contract": {
            "previous_model_decisions_are_not_supplied": True,
            "upstream_transport_decision_fields_are_omitted": True,
            "every_candidate_requires_one_decision": True,
            "new_grounded_findings_are_allowed": True,
            "noncanonical_findings_are_allowed": True,
            "uncertainty_changes_label_not_visibility": True,
            "hft_provenance_changes_qualification_not_visibility": True,
            "every_assigned_hft_record_is_exactly_one_candidate": True,
            "accepted_hft_candidates_must_retain_their_support_and_boundary": True,
            "unresolved_hft_branch_citations_do_not_erase_the_record": True,
            "branch_ids_do_not_count_as_semantic_coverage": True,
            "distinctive_branch_facets_must_be_explained": True,
            "prior_connection_labels_are_not_decisions": True,
            "reciprocal_seed_origin_labels_are_not_reverse_decisions": True,
            "connections_require_explicit_review": lane in {"macro", "global"},
            "conflict_is_not_a_rejection_reason": True,
            "prose_length_is_not_a_decision_criterion": True,
        },
    }
    packet["identity"]["lane_packet_sha256"] = (
        _payload_hash_with_identity_field_removed(packet, "lane_packet_sha256")
    )
    return packet


def _prompt_manifest(
    *,
    stage: str,
    ayah_ref: str,
    prompt: str,
    expected_response: Path | None,
    inputs: dict[str, str],
    authoring_request_sha256: str,
    expected_outputs: dict[str, Path] | None = None,
) -> dict[str, Any]:
    return {
        "schema_version": "commentary-v3-authoring-prompt-manifest-v1",
        "stage": stage,
        "ayah_ref": ayah_ref,
        "prompt_sha256": _sha256_bytes(prompt.encode("utf-8")),
        "prompt_bytes": len(prompt.encode("utf-8")),
        "authoring_request_sha256": authoring_request_sha256,
        "expected_response": str(expected_response) if expected_response else None,
        "expected_outputs": (
            {key: str(path) for key, path in expected_outputs.items()}
            if expected_outputs
            else None
        ),
        "inputs": inputs,
    }


def _render_scopes(args: argparse.Namespace) -> None:
    run_dir = _resolve_run_dir(args.run_dir)
    docket_path = args.docket or _default_docket(args.ayah)
    source_path = args.source_bundle or _default_source_bundle(args.ayah)
    docket = _load_object(docket_path)
    source_bundle = _load_object(source_path)
    if docket.get("identity", {}).get("ayah_ref") != args.ayah:
        raise SystemExit("Docket ayah identity does not match --ayah")
    if source_bundle.get("ayahRef") != args.ayah:
        raise SystemExit("Source bundle ayah identity does not match --ayah")
    if (
        _sha256_json(source_bundle)
        != docket.get("identity", {}).get("source_canonical_sha256")
    ):
        raise SystemExit("Source bundle canonical hash does not match docket")
    reciprocal_evidence, reciprocal_source_coverage = (
        _reciprocal_connection_evidence(args.ayah, args.inter_ayah_dir)
    )
    quran_text_evidence, quran_text_coverage = _quran_text_evidence(
        args.quran_text
    )
    hft_projection = _hft_authoring_projection(docket, source_bundle)
    reciprocal_evidence_sha256 = _sha256_json(reciprocal_evidence)
    stage_dir = run_dir / "scope"
    workspace_dir = run_dir / "workspace"
    _ensure_directory(run_dir, workspace_dir)
    result: dict[str, Any] = {"ayah_ref": args.ayah, "stages": {}}
    for lane in LANES:
        packet = _lane_packet(
            docket,
            lane,
            source_bundle,
            hft_projection,
            reciprocal_evidence,
            reciprocal_source_coverage,
            quran_text_evidence,
            quran_text_coverage,
        )
        template = _read_prompt(f"scope-{lane}.md")
        template_sha256 = _sha256_bytes(template.encode("utf-8"))
        request_inputs = {
            "ayah_ref": args.ayah,
            "lane": lane,
            "lane_packet_sha256": packet["identity"]["lane_packet_sha256"],
            "template_sha256": template_sha256,
        }
        request_sha256 = _request_sha256(f"scope-{lane}-review", request_inputs)
        prompt = _render(
            template,
            {
                "@@AYAH_REF@@": args.ayah,
                "@@LANE_PACKET_SHA256@@": packet["identity"][
                    "lane_packet_sha256"
                ],
                "@@AUTHORING_REQUEST_SHA256@@": request_sha256,
                "@@LANE_PACKET_JSON@@": _canonical_json(packet),
            },
            label=f"{lane} scope",
        )
        packet_path = stage_dir / f"{lane}.packet.json"
        prompt_path = stage_dir / f"{lane}.prompt.md"
        response_path = stage_dir / f"{lane}.review.json"
        manifest_path = stage_dir / f"{lane}.manifest.json"
        manifest = _prompt_manifest(
            stage=f"scope-{lane}-review",
            ayah_ref=args.ayah,
            prompt=prompt,
            expected_response=response_path,
            authoring_request_sha256=request_sha256,
            inputs={
                "docket": str(docket_path.resolve()),
                "docket_sha256": _sha256_bytes(docket_path.read_bytes()),
                "source_bundle": str(source_path.resolve()),
                "source_bundle_sha256": _sha256_bytes(source_path.read_bytes()),
                "reciprocal_source_directory": str(
                    args.inter_ayah_dir.resolve()
                ),
                "reciprocal_evidence_sha256": reciprocal_evidence_sha256,
                "quran_text_source": str(args.quran_text.resolve()),
                "quran_text_source_sha256": quran_text_coverage["source_sha256"],
                "lane_packet_sha256": packet["identity"]["lane_packet_sha256"],
                "template_sha256": template_sha256,
            },
        )
        _write(run_dir, packet_path, _pretty_json(packet))
        _write(run_dir, prompt_path, prompt)
        _write(run_dir, manifest_path, _pretty_json(manifest))
        result["stages"][lane] = {
            "prompt": str(prompt_path),
            "manifest": str(manifest_path),
            "expected_response": str(response_path),
            "workspace": str(workspace_dir),
            "candidate_count": len(packet["candidate_inventory"]),
            "connection_count": len(packet["connection_registry"]),
            "assigned_hft_record_count": packet["hft_evidence"][
                "assigned_record_count"
            ],
        }
    print(_pretty_json(result), end="")


def _review_path(args: argparse.Namespace, lane: str, run_dir: Path) -> Path:
    explicit = getattr(args, f"{lane}_review", None)
    return explicit or (run_dir / "scope" / f"{lane}.review.json")


def _packet_path(lane: str, run_dir: Path) -> Path:
    return run_dir / "scope" / f"{lane}.packet.json"


def _load_bound_scope_artifacts(
    args: argparse.Namespace, run_dir: Path
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]], dict[str, Path]]:
    packets = {lane: _load_object(_packet_path(lane, run_dir)) for lane in LANES}
    review_paths = {lane: _review_path(args, lane, run_dir) for lane in LANES}
    reviews = {lane: _load_object(review_paths[lane]) for lane in LANES}
    for lane in LANES:
        identity = packets[lane].get("identity", {})
        if identity.get("ayah_ref") != args.ayah or identity.get("lane") != lane:
            raise SystemExit(f"{lane} packet identity does not match this run")
        expected_packet_hash = _payload_hash_with_identity_field_removed(
            packets[lane], "lane_packet_sha256"
        )
        if identity.get("lane_packet_sha256") != expected_packet_hash:
            raise SystemExit(f"{lane} packet payload hash is stale or tampered")
        review_identity = reviews[lane].get("identity", {})
        manifest = _load_object(run_dir / "scope" / f"{lane}.manifest.json")
        if reviews[lane].get("ayah_ref") != args.ayah or reviews[lane].get("lane") != lane:
            raise SystemExit(f"{lane} review identity does not match this run")
        if (
            review_identity.get("ayah_ref") != args.ayah
            or review_identity.get("lane") != lane
            or review_identity.get("lane_packet_sha256") != expected_packet_hash
            or review_identity.get("authoring_request_sha256")
            != manifest.get("authoring_request_sha256")
        ):
            raise SystemExit(f"{lane} review is stale or not bound to its prompt")
    return packets, reviews, review_paths


def _render_reconcile(args: argparse.Namespace) -> None:
    run_dir = _resolve_run_dir(args.run_dir)
    packets, reviews, _review_paths = _load_bound_scope_artifacts(args, run_dir)

    template = _read_prompt("scope-reconcile.md")
    template_sha256 = _sha256_bytes(template.encode("utf-8"))
    request_inputs = {
        "ayah_ref": args.ayah,
        "template_sha256": template_sha256,
        **{
            f"{lane}_packet_sha256": packets[lane]["identity"][
                "lane_packet_sha256"
            ]
            for lane in LANES
        },
        **{
            f"{lane}_review_sha256": _sha256_json(reviews[lane])
            for lane in LANES
        },
    }
    request_sha256 = _request_sha256("scope-reconcile", request_inputs)
    prompt = _render(
        template,
        {
            "@@AYAH_REF@@": args.ayah,
            "@@AUTHORING_REQUEST_SHA256@@": request_sha256,
            "@@MICRO_PACKET_JSON@@": _canonical_json(packets["micro"]),
            "@@MICRO_REVIEW_JSON@@": _canonical_json(reviews["micro"]),
            "@@MACRO_PACKET_JSON@@": _canonical_json(packets["macro"]),
            "@@MACRO_REVIEW_JSON@@": _canonical_json(reviews["macro"]),
            "@@GLOBAL_PACKET_JSON@@": _canonical_json(packets["global"]),
            "@@GLOBAL_REVIEW_JSON@@": _canonical_json(reviews["global"]),
        },
        label="scope reconciliation",
    )
    stage_dir = run_dir / "reconcile"
    prompt_path = stage_dir / "reconcile.prompt.md"
    response_path = stage_dir / "reconciled.json"
    manifest_path = stage_dir / "reconcile.manifest.json"
    manifest = _prompt_manifest(
        stage="scope-reconcile",
        ayah_ref=args.ayah,
        prompt=prompt,
        expected_response=response_path,
        authoring_request_sha256=request_sha256,
        inputs={
            f"{lane}_packet_sha256": packets[lane]["identity"][
                "lane_packet_sha256"
            ]
            for lane in LANES
        }
        | {
            f"{lane}_review_sha256": _sha256_json(reviews[lane])
            for lane in LANES
        }
        | {
            "template_sha256": template_sha256,
        },
    )
    _write(run_dir, prompt_path, prompt)
    _write(run_dir, manifest_path, _pretty_json(manifest))
    print(
        _pretty_json(
            {
                "ayah_ref": args.ayah,
                "prompt": str(prompt_path),
                "manifest": str(manifest_path),
                "expected_response": str(response_path),
                "workspace": str(run_dir / "workspace"),
            }
        ),
        end="",
    )


def _reconciled_path(args: argparse.Namespace, run_dir: Path) -> Path:
    return args.reconciled or (
        run_dir / "reconcile" / "reconciled.json"
    )


def _render_scope_prose(args: argparse.Namespace) -> None:
    run_dir = _resolve_run_dir(args.run_dir)
    packets, reviews, _review_paths = _load_bound_scope_artifacts(args, run_dir)
    reconciled = _load_object(_reconciled_path(args, run_dir))
    if reconciled.get("ayah_ref") != args.ayah:
        raise SystemExit("Reconciled finding identity does not match --ayah")
    if reconciled.get("ready_for_prose") is not True:
        raise SystemExit("Reconciled finding set is not ready for prose")
    reconcile_manifest = _load_object(
        run_dir / "reconcile" / "reconcile.manifest.json"
    )
    reconciled_identity = reconciled.get("identity", {})
    if (
        reconciled_identity.get("ayah_ref") != args.ayah
        or reconciled_identity.get("authoring_request_sha256")
        != reconcile_manifest.get("authoring_request_sha256")
    ):
        raise SystemExit("Reconciled findings are stale or not prompt-bound")
    locked_by_ref, assignments = _locked_finding_assignments(reconciled)
    assigned_refs = assignments.get(args.lane)
    locked = [
        locked_by_ref[finding_ref]
        for finding_ref in assigned_refs
    ]
    packet = packets[args.lane]
    review = reviews[args.lane]
    support_ids = {
        support_id
        for finding in locked
        for support_id in finding.get("support_ids", [])
        if isinstance(support_id, str)
    }
    branch_refs = {
        branch_ref
        for finding in locked
        for branch_ref in finding.get("branch_refs", [])
        if isinstance(branch_ref, str)
    }
    connection_refs = {
        connection_ref
        for finding in locked
        for connection_ref in finding.get("connection_refs", [])
        if isinstance(connection_ref, str)
    }
    candidate_ids = {
        candidate_id
        for finding in locked
        for candidate_id in finding.get("candidate_ids", [])
        if isinstance(candidate_id, str)
    }

    def unique_cross_lane_records(
        registry_name: str, ref_field: str, wanted_refs: set[str]
    ) -> list[dict[str, Any]]:
        by_ref: dict[str, dict[str, Any]] = {}
        source_lanes: dict[str, list[str]] = {}
        for source_lane in LANES:
            for item in packets[source_lane].get(registry_name, []):
                item_ref = item.get(ref_field)
                if item_ref not in wanted_refs:
                    continue
                if item_ref in by_ref and _canonical_json(by_ref[item_ref]) != (
                    _canonical_json(item)
                ):
                    raise SystemExit(
                        f"Conflicting cross-lane {registry_name} record: {item_ref}"
                    )
                by_ref[item_ref] = item
                source_lanes.setdefault(item_ref, []).append(source_lane)
        missing = sorted(wanted_refs - set(by_ref))
        if missing:
            raise SystemExit(
                f"Locked findings cite missing {registry_name} records: {missing}"
            )
        return [
            {
                **by_ref[item_ref],
                "available_in_lanes": sorted(set(source_lanes[item_ref])),
            }
            for item_ref in sorted(by_ref)
        ]

    cited_support_records = unique_cross_lane_records(
        "support_registry", "support_id", support_ids
    )
    cited_connection_records = unique_cross_lane_records(
        "connection_registry", "connection_ref", connection_refs
    )
    cited_branch_records = [
        {"source_lane": source_lane, **item}
        for source_lane in LANES
        for item in packets[source_lane].get("branch_registry", [])
        if item.get("branch_ref") in branch_refs
    ]
    missing_branch_refs = sorted(
        branch_refs
        - {item.get("branch_ref") for item in cited_branch_records}
    )
    if missing_branch_refs:
        raise SystemExit(
            f"Locked findings cite missing branch records: {missing_branch_refs}"
        )
    review_context_fields = (
        "surface_coverage",
        "branch_screen",
        "connection_coverage",
        "support_coverage",
        "atlas_facets_tested",
        "scope_referrals",
        "friction_notes",
    )
    prose_context = {
        "lane": args.lane,
        "locked_findings": locked,
        "primary_floor": packet.get("primary_floor"),
        "focus_surface_evidence": packet.get("focus_surface_evidence"),
        "review_context": {
            field: review.get(field, []) for field in review_context_fields
        }
        | {
            "candidate_decisions": [
                {"source_lane": source_lane, **decision}
                for source_lane in LANES
                for decision in reviews[source_lane].get(
                    "candidate_decisions", []
                )
                if decision.get("candidate_id") in candidate_ids
            ]
        },
        "cited_support_records": cited_support_records,
        "cited_branch_records": cited_branch_records,
        "cited_connection_records": cited_connection_records,
        "instruction": (
            "This context preserves exact surface values, decision coverage, "
            "friction, and cited evidence across all origin lanes. HFT support "
            "payloads retain their source containment and exact anchor Arabic. "
            "It is for faithful prose preparation only; do not reopen decisions "
            "or add findings."
        ),
    }
    template = _read_prompt(f"scope-{args.lane}-prose-followup.md")
    template_sha256 = _sha256_bytes(template.encode("utf-8"))
    reconciled_sha256 = _sha256_json(reconciled)
    request_inputs = {
        "ayah_ref": args.ayah,
        "lane": args.lane,
        "template_sha256": template_sha256,
        "reconciled_sha256": reconciled_sha256,
        "assigned_finding_refs_sha256": _sha256_json(assigned_refs),
        "lane_packet_sha256": packet["identity"]["lane_packet_sha256"],
        "lane_review_sha256": _sha256_json(review),
        "prose_context_sha256": _sha256_json(prose_context),
    }
    request_sha256 = _request_sha256(
        f"scope-{args.lane}-prose", request_inputs
    )
    prompt = _render(
        template,
        {
            "@@AYAH_REF@@": args.ayah,
            "@@RECONCILED_SHA256@@": reconciled_sha256,
            "@@AUTHORING_REQUEST_SHA256@@": request_sha256,
            "@@LANE_PROSE_CONTEXT_JSON@@": _canonical_json(prose_context),
        },
        label=f"{args.lane} prose follow-up",
    )
    stage_dir = run_dir / "scope"
    prompt_path = stage_dir / f"{args.lane}.prose-followup.md"
    response_path = stage_dir / f"{args.lane}.draft.json"
    manifest_path = stage_dir / f"{args.lane}.prose-followup.manifest.json"
    manifest = _prompt_manifest(
        stage=f"scope-{args.lane}-prose",
        ayah_ref=args.ayah,
        prompt=prompt,
        expected_response=response_path,
        authoring_request_sha256=request_sha256,
        inputs={
            "reconciled_sha256": reconciled_sha256,
            "locked_finding_count": str(len(locked)),
            "assigned_finding_refs_sha256": _sha256_json(assigned_refs),
            "lane_packet_sha256": packet["identity"]["lane_packet_sha256"],
            "lane_review_sha256": _sha256_json(review),
            "prose_context_sha256": _sha256_json(prose_context),
            "template_sha256": template_sha256,
        },
    )
    _write(run_dir, prompt_path, prompt)
    _write(run_dir, manifest_path, _pretty_json(manifest))
    print(
        _pretty_json(
            {
                "ayah_ref": args.ayah,
                "lane": args.lane,
                "prompt": str(prompt_path),
                "manifest": str(manifest_path),
                "expected_response": str(response_path),
                "locked_finding_count": len(locked),
            }
        ),
        end="",
    )


def _draft_path(args: argparse.Namespace, lane: str, run_dir: Path) -> Path:
    explicit = getattr(args, f"{lane}_draft", None)
    return explicit or (run_dir / "scope" / f"{lane}.draft.json")


def _render_merge(args: argparse.Namespace) -> None:
    run_dir = _resolve_run_dir(args.run_dir)
    reconciled = _load_object(_reconciled_path(args, run_dir))
    if reconciled.get("ayah_ref") != args.ayah:
        raise SystemExit("Reconciled finding identity does not match --ayah")
    if reconciled.get("ready_for_prose") is not True:
        raise SystemExit("Reconciled finding set is not ready for prose")
    reconcile_manifest = _load_object(
        run_dir / "reconcile" / "reconcile.manifest.json"
    )
    reconciled_identity = reconciled.get("identity", {})
    if (
        reconciled_identity.get("ayah_ref") != args.ayah
        or reconciled_identity.get("authoring_request_sha256")
        != reconcile_manifest.get("authoring_request_sha256")
    ):
        raise SystemExit("Reconciled findings are stale or not prompt-bound")
    _locked_by_ref, assignments = _locked_finding_assignments(reconciled)
    micro_packet = _load_object(_packet_path("micro", run_dir))
    micro_packet_identity = micro_packet.get("identity", {})
    expected_micro_packet_hash = _payload_hash_with_identity_field_removed(
        micro_packet, "lane_packet_sha256"
    )
    if (
        micro_packet_identity.get("ayah_ref") != args.ayah
        or micro_packet_identity.get("lane") != "micro"
        or micro_packet_identity.get("lane_packet_sha256")
        != expected_micro_packet_hash
    ):
        raise SystemExit("Micro surface packet is stale or not bound to this run")
    if (
        reconcile_manifest.get("inputs", {}).get("micro_packet_sha256")
        != expected_micro_packet_hash
    ):
        raise SystemExit(
            "Micro surface packet differs from the packet used for reconciliation"
        )
    focus_surface_evidence = micro_packet.get("focus_surface_evidence")
    if not isinstance(focus_surface_evidence, dict):
        raise SystemExit("Micro packet lacks exact focus-surface evidence")
    focus_surface_evidence = {
        "primary_floor": micro_packet.get("primary_floor"),
        **focus_surface_evidence,
    }
    drafts = {
        lane: _load_object(_draft_path(args, lane, run_dir)) for lane in LANES
    }
    for lane in LANES:
        if drafts[lane].get("ayah_ref") != args.ayah or drafts[lane].get("lane") != lane:
            raise SystemExit(f"{lane} prose draft identity does not match this run")
        draft_manifest = _load_object(
            run_dir / "scope" / f"{lane}.prose-followup.manifest.json"
        )
        draft_identity = drafts[lane].get("identity", {})
        if (
            draft_identity.get("ayah_ref") != args.ayah
            or draft_identity.get("lane") != lane
            or draft_identity.get("reconciled_sha256") != _sha256_json(reconciled)
            or draft_identity.get("authoring_request_sha256")
            != draft_manifest.get("authoring_request_sha256")
        ):
            raise SystemExit(f"{lane} prose draft is stale or not prompt-bound")
        if drafts[lane].get("coverage_complete") is not True:
            raise SystemExit(f"{lane} prose draft does not attest complete coverage")
        movements = drafts[lane].get("movements")
        if not isinstance(movements, list) or any(
            not isinstance(movement, dict) for movement in movements
        ):
            raise SystemExit(f"{lane} prose draft lacks a movement list")
        movement_keys = [movement.get("movement_key") for movement in movements]
        if any(not isinstance(key, str) or not key for key in movement_keys):
            raise SystemExit(f"{lane} prose draft has an invalid movement key")
        if len(set(movement_keys)) != len(movement_keys):
            raise SystemExit(f"{lane} prose draft repeats a movement key")
        movements_by_key = dict(zip(movement_keys, movements, strict=True))
        for movement in movements:
            if (
                not isinstance(movement.get("draft_prose"), str)
                or not movement["draft_prose"].strip()
            ):
                raise SystemExit(f"{lane} prose draft has an empty movement")
            finding_refs = movement.get("finding_refs")
            if (
                not isinstance(finding_refs, list)
                or not finding_refs
                or any(
                    not isinstance(ref, str) or not ref for ref in finding_refs
                )
                or len(set(finding_refs)) != len(finding_refs)
                or not set(finding_refs) <= set(assignments[lane])
            ):
                raise SystemExit(f"{lane} prose movement has invalid finding refs")
        landings = drafts[lane].get("finding_landings")
        if not isinstance(landings, list) or any(
            not isinstance(landing, dict) for landing in landings
        ):
            raise SystemExit(f"{lane} prose draft lacks a finding landing list")
        landing_refs = [landing.get("finding_ref") for landing in landings]
        if any(not isinstance(ref, str) or not ref for ref in landing_refs):
            raise SystemExit(f"{lane} prose draft has an invalid finding landing")
        if len(set(landing_refs)) != len(landing_refs):
            raise SystemExit(f"{lane} prose draft repeats a finding landing")
        if set(landing_refs) != set(assignments[lane]):
            raise SystemExit(
                f"{lane} prose draft finding landings do not cover its locked set"
            )
        for landing in landings:
            movement_key = landing.get("movement_key")
            if (
                not isinstance(movement_key, str)
                or movement_key not in movements_by_key
                or landing["finding_ref"]
                not in movements_by_key[movement_key]["finding_refs"]
            ):
                raise SystemExit(
                    f"{lane} prose draft has a detached finding landing"
                )

    principles_path = REPO_ROOT / "PRINCIPLES.md"
    commentary_spec_path = REPO_ROOT / "COMMENTARY_SPEC.md"
    channels_path = REPO_ROOT / "docs" / "CHANNELS.md"
    canonical_prompt_path = REPO_ROOT / "_ayah_commentary" / "v2" / "PROMPT.md"
    principles = principles_path.read_text(encoding="utf-8")
    commentary_spec = commentary_spec_path.read_text(encoding="utf-8")
    channels = channels_path.read_text(encoding="utf-8")
    canonical_prompt = canonical_prompt_path.read_text(encoding="utf-8")
    _surah, _ayah, _folder, stem = _ayah_parts(args.ayah)
    final_dir = run_dir / "final"
    outputs = {
        "prose": final_dir / f"{stem}.prose.tr.md",
        "evidence": final_dir / f"{stem}.evidence.tr.md",
        "index": final_dir / f"{stem}.index.tr.md",
        "friction": final_dir / f"{stem}.friction.tr.md",
    }
    template = _read_prompt("scope-merge.md")
    template_sha256 = _sha256_bytes(template.encode("utf-8"))
    request_inputs = {
        "ayah_ref": args.ayah,
        "template_sha256": template_sha256,
        "principles_sha256": _sha256_bytes(principles.encode("utf-8")),
        "commentary_spec_sha256": _sha256_bytes(
            commentary_spec.encode("utf-8")
        ),
        "channels_sha256": _sha256_bytes(channels.encode("utf-8")),
        "canonical_prompt_sha256": _sha256_bytes(
            canonical_prompt.encode("utf-8")
        ),
        "reconciled_sha256": _sha256_json(reconciled),
        "focus_surface_evidence_sha256": _sha256_json(focus_surface_evidence),
        **{
            f"{lane}_draft_sha256": _sha256_json(drafts[lane])
            for lane in LANES
        },
    }
    request_sha256 = _request_sha256("canonical-merge", request_inputs)
    prompt = _render(
        template,
        {
            "@@AYAH_REF@@": args.ayah,
            "@@PROSE_OUTPUT_PATH@@": str(outputs["prose"]),
            "@@EVIDENCE_OUTPUT_PATH@@": str(outputs["evidence"]),
            "@@INDEX_OUTPUT_PATH@@": str(outputs["index"]),
            "@@FRICTION_OUTPUT_PATH@@": str(outputs["friction"]),
            "@@PRINCIPLES_MD@@": principles,
            "@@COMMENTARY_SPEC_MD@@": commentary_spec,
            "@@CHANNELS_MD@@": channels,
            "@@CANONICAL_PROMPT_V2@@": canonical_prompt,
            "@@RECONCILED_FINDINGS_JSON@@": _canonical_json(reconciled),
            "@@FOCUS_SURFACE_EVIDENCE_JSON@@": _canonical_json(
                focus_surface_evidence
            ),
            "@@MICRO_DRAFT_JSON@@": _canonical_json(drafts["micro"]),
            "@@MACRO_DRAFT_JSON@@": _canonical_json(drafts["macro"]),
            "@@GLOBAL_DRAFT_JSON@@": _canonical_json(drafts["global"]),
        },
        label="canonical merge",
    )
    stage_dir = run_dir / "merge"
    prompt_path = stage_dir / "merge.prompt.md"
    manifest_path = stage_dir / "merge.manifest.json"
    manifest = _prompt_manifest(
        stage="canonical-merge",
        ayah_ref=args.ayah,
        prompt=prompt,
        expected_response=None,
        expected_outputs=outputs,
        authoring_request_sha256=request_sha256,
        inputs={
            "template_sha256": template_sha256,
            "principles_sha256": _sha256_bytes(principles.encode("utf-8")),
            "commentary_spec_sha256": _sha256_bytes(
                commentary_spec.encode("utf-8")
            ),
            "channels_sha256": _sha256_bytes(channels.encode("utf-8")),
            "canonical_prompt_sha256": _sha256_bytes(
                canonical_prompt.encode("utf-8")
            ),
            "reconciled_sha256": _sha256_json(reconciled),
            "focus_surface_evidence_sha256": _sha256_json(
                focus_surface_evidence
            ),
            **{
                f"{lane}_draft_sha256": _sha256_json(drafts[lane])
                for lane in LANES
            },
        },
    )
    _ensure_directory(run_dir, final_dir)
    _write(run_dir, prompt_path, prompt)
    _write(run_dir, manifest_path, _pretty_json(manifest))
    print(
        _pretty_json(
            {
                "ayah_ref": args.ayah,
                "prompt": str(prompt_path),
                "manifest": str(manifest_path),
                "workspace": str(run_dir),
                "outputs": {key: str(path) for key, path in outputs.items()},
                "editorial_followup": str(PROMPTS_ROOT / "editorial-followup.md"),
            }
        ),
        end="",
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    scopes = subparsers.add_parser("scopes", help="Render three lane review prompts")
    scopes.add_argument("--ayah", required=True)
    scopes.add_argument("--run-dir", required=True, type=Path)
    scopes.add_argument("--docket", type=Path)
    scopes.add_argument("--source-bundle", type=Path)
    scopes.add_argument(
        "--inter-ayah-dir",
        type=Path,
        default=DEFAULT_INTER_AYAH_DIR,
        help=(
            "Directory containing the complete per-ayah inter-ayah TSV source "
            "used to derive reciprocal discovery seeds"
        ),
    )
    scopes.add_argument(
        "--quran-text",
        type=Path,
        default=DEFAULT_QURAN_TEXT,
        help=(
            "Complete ayah-text TSV used to attach exact target Arabic to every "
            "macro/global connection"
        ),
    )
    scopes.set_defaults(func=_render_scopes)

    reconcile = subparsers.add_parser(
        "reconcile", help="Render the cross-scope reconciliation prompt"
    )
    reconcile.add_argument("--ayah", required=True)
    reconcile.add_argument("--run-dir", required=True, type=Path)
    for lane in LANES:
        reconcile.add_argument(f"--{lane}-review", type=Path)
    reconcile.set_defaults(func=_render_reconcile)

    scope_prose = subparsers.add_parser(
        "scope-prose", help="Render a same-agent lane prose follow-up"
    )
    scope_prose.add_argument("--ayah", required=True)
    scope_prose.add_argument("--run-dir", required=True, type=Path)
    scope_prose.add_argument("--lane", required=True, choices=LANES)
    scope_prose.add_argument("--reconciled", type=Path)
    scope_prose.set_defaults(func=_render_scope_prose)

    merge = subparsers.add_parser(
        "merge", help="Render the fresh canonical merge-writer prompt"
    )
    merge.add_argument("--ayah", required=True)
    merge.add_argument("--run-dir", required=True, type=Path)
    merge.add_argument("--reconciled", type=Path)
    for lane in LANES:
        merge.add_argument(f"--{lane}-draft", type=Path)
    merge.set_defaults(func=_render_merge)
    return parser


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
