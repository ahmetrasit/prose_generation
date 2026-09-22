#!/usr/bin/env python3
"""Prepare V5 scope prompts for one prefatory basmala without changing workflow.py."""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path
from typing import Any


V5_ROOT = Path(__file__).resolve().parent
REPO_ROOT = V5_ROOT.parents[1]
sys.path.insert(0, str(REPO_ROOT))

from _commentary.v8_batch import composition as compositions  # noqa: E402
from _commentary.v8_batch import workflow  # noqa: E402
from scripts import build_bundle as bundle_builder  # noqa: E402
from v3lib import prepare as v3_prepare  # noqa: E402


_ORIGINAL_BASMALA_DOCKET_TEMPLATE = workflow._basmala_docket_template
_ORIGINAL_ADAPT_BASMALA_DOCKET = workflow._adapt_basmala_docket
S0_REF_RE = re.compile(r"[1-9][0-9]*:0")
INTRINSIC_SOURCE_TYPES = frozenset({"qac_morpheme", "word_analysis"})
HOST_SOURCE_TYPES = frozenset({
    "channel",
    "cross_run_publication",
    "legacy_reader_response",
    "v12_reader_walks",
    "v12_reader_walks_wide",
})
HOST_EVIDENCE_FIELDS = (
    "v12_reader_responses",
    "v12_reader_walks",
    "v12_reader_walks_wide",
    "v12_cross_run_publication",
    "butuncul_okuma_line",
    "inter_ayah_rows",
    "channel_subchannels_anchored_here",
    "channel_generated_outputs",
)


def _walk_seed_count(value: Any, label: str) -> int:
    if not isinstance(value, dict) or not value:
        raise workflow.WorkflowError(f"S:0 requires nonempty {label}")
    count = 0
    for reader_id, reader in value.items():
        if not isinstance(reader_id, str) or not isinstance(reader, dict):
            raise workflow.WorkflowError(f"S:0 {label} readers must be objects")
        for field in ("activated_readings_md", "retrospective_surprises_md"):
            text = reader.get(field)
            if text in (None, ""):
                continue
            if not isinstance(text, str):
                raise workflow.WorkflowError(
                    f"S:0 {label}.{reader_id}.{field} must be text"
                )
            count += len(v3_prepare._split_markdown_items(text))
    if count == 0:
        raise workflow.WorkflowError(f"S:0 {label} has no reviewable items")
    return count


def _optional_walk_seed_count(
    source_bundle: dict[str, Any], field: str
) -> int | None:
    value = source_bundle.get(field)
    coverage = source_bundle.get("coverage", {}).get(field, {})
    if value:
        return _walk_seed_count(value, field)
    if isinstance(coverage, dict):
        readers = coverage.get("readers", {})
        parse_failures = sorted(
            reader_id
            for reader_id, reader in readers.items()
            if isinstance(reader, dict) and reader.get("zero_headings_parsed")
        ) if isinstance(readers, dict) else []
        if parse_failures:
            raise workflow.WorkflowError(
                f"S:0 {field} contains unparseable reader files: "
                f"{', '.join(parse_failures)}"
            )
        if coverage.get("present"):
            raise workflow.WorkflowError(
                f"S:0 {field} coverage says present but payload is empty"
            )
    return None


def _validate_optional_whole_reading(source_bundle: dict[str, Any]) -> None:
    whole_reading = source_bundle.get("butuncul_okuma_line")
    if whole_reading:
        if not isinstance(whole_reading, (str, dict)):
            raise workflow.WorkflowError(
                "S:0 butuncul_okuma_line must be text or an object"
            )
        return

    coverage = source_bundle.get("coverage", {}).get("butuncul_okuma", {})
    if not isinstance(coverage, dict):
        return
    if coverage.get("present"):
        raise workflow.WorkflowError(
            "S:0 whole-reading coverage says present but payload is empty"
        )
    files_found = coverage.get("files_found", [])
    if isinstance(files_found, list) and files_found and all(
        isinstance(row, dict) and row.get("ayah_count_parsed") == 0
        for row in files_found
    ):
        raise workflow.WorkflowError(
            "S:0 whole-reading files were found but no ayah lines parsed"
        )


def _required_host_seed_counts(source_bundle: dict[str, Any]) -> dict[str, int]:
    target_ref = str(source_bundle.get("ayahRef"))
    surah = int(target_ref.split(":", 1)[0])
    publication = source_bundle.get("v12_cross_run_publication")
    if not isinstance(publication, dict) or not publication:
        raise workflow.WorkflowError(
            "S:0 requires a nonempty v12_cross_run_publication"
        )
    if publication.get("ayah_ref") != target_ref:
        raise workflow.WorkflowError(
            "S:0 publication ayah_ref does not match the focus"
        )
    if publication.get("canonical_ayah_ref") != target_ref:
        raise workflow.WorkflowError(
            "S:0 publication canonical_ayah_ref does not match the focus"
        )
    if publication.get("surah") != surah:
        raise workflow.WorkflowError(
            "S:0 publication surah does not match the host surah"
        )
    findings = publication.get("findings")
    if not isinstance(findings, list) or not findings:
        raise workflow.WorkflowError("S:0 publication has no findings")

    _validate_optional_whole_reading(source_bundle)
    counts = {"cross_run_publication": len(findings)}
    for field in ("v12_reader_walks", "v12_reader_walks_wide"):
        count = _optional_walk_seed_count(source_bundle, field)
        if count is not None:
            counts[field] = count
    return counts


def _s0_docket_template(source_bundle: dict[str, Any]) -> dict[str, Any]:
    """Build the 1:1 linguistic template without discarding host evidence."""
    _required_host_seed_counts(source_bundle)
    template = _ORIGINAL_BASMALA_DOCKET_TEMPLATE(source_bundle)
    for field in HOST_EVIDENCE_FIELDS:
        template[field] = copy.deepcopy(source_bundle.get(field))

    # V3 requires a numbered focus while parsing publication anchors. The
    # publication is restored to the real S:0 identity in the final packet.
    publication = template.get("v12_cross_run_publication")
    if isinstance(publication, dict):
        if "ayah_ref" in publication:
            publication["ayah_ref"] = "1:1"
        if "canonical_ayah_ref" in publication:
            publication["canonical_ayah_ref"] = "1:1"
        if "surah" in publication:
            publication["surah"] = 1
    return template


def _support_identity(support: dict[str, Any]) -> str:
    return v3_prepare._stable_id(
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
            "text_sha256": v3_prepare.sha256_bytes(
                support["text"].encode("utf-8")
            ),
        },
    )


def _replace_exact_ids(value: Any, replacements: dict[str, str]) -> Any:
    if isinstance(value, dict):
        return {
            key: _replace_exact_ids(item, replacements)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [_replace_exact_ids(item, replacements) for item in value]
    if isinstance(value, str):
        return replacements.get(value, value)
    return value


def _validate_s0_docket(
    docket: dict[str, Any],
    source_bundle: dict[str, Any],
    template_docket: dict[str, Any],
) -> None:
    try:
        workflow.validate_docket(template_docket)
    except workflow.ValidationError as exc:
        raise workflow.WorkflowError(
            f"S:0 numbered validation template is invalid: {exc}"
        ) from exc

    target_ref = str(source_bundle["ayahRef"])
    if docket.get("identity", {}).get("ayah_ref") != target_ref:
        raise workflow.WorkflowError("S:0 docket identity does not match its source")
    if docket["identity"].get("source_canonical_sha256") != workflow.v3._sha256_json(
        source_bundle
    ):
        raise workflow.WorkflowError("S:0 docket source hash is stale")
    if docket["identity"].get(
        "docket_payload_sha256"
    ) != workflow._docket_payload_hash(docket):
        raise workflow.WorkflowError("S:0 docket payload hash is stale")
    focus = docket.get("focus", {})
    if (
        focus.get("surface_ref") != target_ref
        or focus.get("linguistic_source_ref") != "1:1"
    ):
        raise workflow.WorkflowError("S:0 focus reference aliases are invalid")

    supports = docket.get("support_registry", [])
    support_ids = [support.get("support_id") for support in supports]
    if len(support_ids) != len(set(support_ids)) or any(
        support.get("support_id") != _support_identity(support)
        for support in supports
    ):
        raise workflow.WorkflowError("S:0 support identities are stale or duplicated")
    if any(
        support.get("source_type") in HOST_SOURCE_TYPES
        and support.get("scope") != "macro"
        for support in supports
    ):
        raise workflow.WorkflowError("S:0 host support escaped the macro scope")
    known_support_ids = set(support_ids)

    candidate_ids: list[str] = []
    for candidate in docket.get("candidates", []):
        candidate_id = candidate.get("candidate_id")
        candidate_ids.append(candidate_id)
        if candidate_id != v3_prepare._candidate_identity(
            candidate, ayah_ref=target_ref
        ):
            raise workflow.WorkflowError("S:0 candidate identity is stale")
        if not set(candidate.get("support_ids", [])) <= known_support_ids:
            raise workflow.WorkflowError("S:0 candidate cites an unknown support")
        if (
            candidate.get("ayah_ref") != target_ref
            or candidate.get("surface_ref") != target_ref
            or candidate.get("linguistic_source_ref") != "1:1"
        ):
            raise workflow.WorkflowError(
                "S:0 candidate reference aliases are invalid"
            )
        source_type = candidate.get("source_type")
        if source_type in INTRINSIC_SOURCE_TYPES:
            if candidate.get("lane") != "micro":
                raise workflow.WorkflowError(
                    "S:0 intrinsic candidate escaped the micro lane"
                )
        elif source_type in HOST_SOURCE_TYPES:
            if (
                candidate.get("lane") != "macro"
                or candidate.get("scope") != "macro"
                or "1:1" in candidate.get("anchor_refs", [])
            ):
                raise workflow.WorkflowError(
                    "S:0 host candidate has invalid routing or focus anchors"
                )
    if len(candidate_ids) != len(set(candidate_ids)):
        raise workflow.WorkflowError("S:0 candidate identities are duplicated")


def _s0_adapt_docket(
    source_bundle: dict[str, Any], template_docket: dict[str, Any]
) -> dict[str, Any]:
    """Retarget intrinsic evidence and assign host-authored evidence to macro."""
    docket = _ORIGINAL_ADAPT_BASMALA_DOCKET(source_bundle, template_docket)
    target_ref = str(source_bundle["ayahRef"])
    candidates = copy.deepcopy(template_docket.get("candidates", []))
    required_counts = _required_host_seed_counts(source_bundle)
    actual_counts = {
        source_type: sum(
            candidate.get("source_type") == source_type
            for candidate in candidates
        )
        for source_type in required_counts
    }
    if actual_counts != required_counts:
        raise workflow.WorkflowError(
            "S:0 host evidence was not losslessly candidateized: "
            f"expected={required_counts}, actual={actual_counts}"
        )
    unexpected_types = sorted({
        str(candidate.get("source_type"))
        for candidate in candidates
        if candidate.get("source_type")
        not in INTRINSIC_SOURCE_TYPES | HOST_SOURCE_TYPES
    })
    if unexpected_types:
        raise workflow.WorkflowError(
            "S:0 preparation encountered unsupported candidate sources: "
            f"{unexpected_types}"
        )

    host_support_ids: set[str] = set()
    for candidate in candidates:
        source_type = candidate.get("source_type")
        candidate.update({
            "ayah_ref": target_ref,
            "surface_ref": target_ref,
            "linguistic_source_ref": "1:1",
        })
        if source_type in HOST_SOURCE_TYPES:
            candidate["lane"] = "macro"
            candidate["scope"] = "macro"
            candidate["anchor_refs"] = sorted(
                target_ref if ref == "1:1" else ref
                for ref in candidate.get("anchor_refs", [])
            )
            host_support_ids.update(
                support_id
                for support_id in candidate.get("support_ids", [])
                if isinstance(support_id, str)
            )

    all_support_ids = {
        support_id
        for candidate in candidates
        for support_id in candidate.get("support_ids", [])
        if isinstance(support_id, str)
    }
    supports = [
        copy.deepcopy(support)
        for support in template_docket.get("support_registry", [])
        if support.get("support_id") in all_support_ids
    ]
    support_id_map: dict[str, str] = {}
    for support in supports:
        old_id = support["support_id"]
        if support.get("support_id") in host_support_ids:
            support["scope"] = "macro"
        support["support_id"] = _support_identity(support)
        support_id_map[old_id] = support["support_id"]

    candidate_id_map: dict[str, str] = {}
    for candidate in candidates:
        old_id = candidate["candidate_id"]
        candidate["support_ids"] = sorted(
            support_id_map.get(support_id, support_id)
            for support_id in candidate.get("support_ids", [])
        )
        candidate["candidate_id"] = v3_prepare._candidate_identity(
            candidate, ayah_ref=target_ref
        )
        candidate_id_map[old_id] = candidate["candidate_id"]

    docket["candidates"] = candidates
    docket["support_registry"] = supports
    docket = _replace_exact_ids(
        docket, {**support_id_map, **candidate_id_map}
    )
    docket["identity"]["docket_payload_sha256"] = workflow._docket_payload_hash(
        docket
    )
    _validate_s0_docket(docket, source_bundle, template_docket)
    return docket


def _load_s0_focus_inputs(
    args: argparse.Namespace,
    context_bundles_dir: Path,
    member_bundles_dir: Path,
) -> tuple[dict[str, Any], dict[str, Any]]:
    source_path = workflow._focus_bundle_path(
        args, context_bundles_dir, member_bundles_dir
    )
    _source_payload, source_bundle = workflow._load_json_object(source_path)
    try:
        identity = compositions.validate_unit_bundle(
            source_bundle, expected_ref=args.ayah
        )
    except compositions.CompositionError as exc:
        raise workflow.WorkflowError(str(exc)) from exc
    if identity["unit_kind"] != "prefatory_basmala":
        raise workflow.WorkflowError("prepare_s0.py requires a prefatory bundle")

    template = _s0_docket_template(source_bundle)
    template_payload = workflow._canonical_json(template).encode("utf-8")
    try:
        _prepared, template_docket = workflow.build_prepared_artifacts(
            template,
            source_path=source_path,
            source_raw=template_payload,
            options=workflow.PREPARE_OPTIONS,
        )
    except workflow.ValidationError as exc:
        raise workflow.WorkflowError(
            f"Cannot prepare S:0 focus bundle {source_path}: {exc}"
        ) from exc

    docket = _s0_adapt_docket(source_bundle, template_docket)
    if docket.get("identity", {}).get("ayah_ref") != args.ayah:
        raise workflow.WorkflowError("S:0 docket ayah identity does not match focus")
    return source_bundle, docket


def _source_context_bundle(
    surah: int,
    ayah: int,
    cache: dict[int, dict[str, Any]],
) -> dict[str, Any]:
    if surah not in cache:
        root_id_map, root_records = bundle_builder.load_qac_furuq_root_map()
        channel_review, _coverage, _path = bundle_builder.load_channel_review(
            surah
        )
        branch_path = (
            bundle_builder.V12_TR_DIR
            / f"s{surah:03d}"
            / "full_context_packet.json"
        )
        if not branch_path.is_file():
            raise workflow.WorkflowError(
                f"Cannot reconstruct S:0 context: missing {branch_path}"
            )
        branch_packet = json.loads(branch_path.read_text(encoding="utf-8"))
        branch_inventories = branch_packet.get("branch_inventories")
        if not isinstance(branch_inventories, list) or not branch_inventories:
            raise workflow.WorkflowError(
                "Cannot reconstruct S:0 context: empty branch inventory in "
                f"{branch_path}"
            )
        cache[surah] = {
            "quran_text": bundle_builder.load_quran_text(surah),
            "word_analysis": bundle_builder.load_word_analysis(surah),
            "qac_by_ayah": bundle_builder.load_qac_morphemes(surah),
            "root_id_map": root_id_map,
            "root_records": root_records,
            "channel_review": channel_review,
            "branch_path": branch_path,
            "branch_inventories": branch_inventories,
            "root_material": {},
        }
    sources = cache[surah]
    ref = f"{surah}:{ayah}"
    quran_text = sources["quran_text"].get(ref)
    word_analysis = sources["word_analysis"].get(ref)
    qac_rows = sources["qac_by_ayah"].get(ayah)
    if quran_text is None or word_analysis is None or not qac_rows:
        raise workflow.WorkflowError(
            f"Cannot reconstruct missing S:0 context bundle {ref} from "
            "canonical Quran, word-analysis, and QAC sources"
        )

    channel_blocks = bundle_builder.channel_blocks_for_ayah(
        sources["channel_review"], ref
    )
    scoped_branches, _scoping = bundle_builder.scope_branch_inventories_to_ayah(
        sources["branch_inventories"], qac_rows, channel_blocks, ref
    )
    branch_inventories = {
        "full_context_packet": {
            "source_file": bundle_builder.relpath(sources["branch_path"]),
            "branch_inventories": scoped_branches,
        }
    }
    roots = []
    for row in qac_rows:
        root = row.get("root_ar") if isinstance(row, dict) else None
        if isinstance(root, str) and root and root not in roots:
            roots.append(root)
    root_lexicon = {}
    per_root = {}
    for root in roots:
        material = sources["root_material"].get(root)
        if material is None:
            targets, mapping = bundle_builder._root_targets(
                root, sources["root_id_map"], sources["root_records"]
            )
            entries = {}
            for target in targets:
                root_id = target.get("furuq_root_id")
                if not isinstance(root_id, str) or not root_id:
                    continue
                dictionary, _path = bundle_builder.load_dictionary_entry(
                    root_id
                )
                dictionary, _trim = bundle_builder._trim_occurrence_evidence(
                    dictionary
                )
                entries[root_id] = {
                    "root_ar": root,
                    "qac_roots_ar": [root],
                    "root_id": root_id,
                    "qac_root_mappings": [{
                        "root_ar": root,
                        "target_rank": target.get("target_rank"),
                    }],
                    "dictionary_entry": dictionary,
                }
            material = (entries, {"root_mapping": mapping})
            sources["root_material"][root] = material
        entries, root_coverage = material
        per_root[root] = copy.deepcopy(root_coverage)
        for root_id, record in entries.items():
            if root_id not in root_lexicon:
                root_lexicon[root_id] = copy.deepcopy(record)
                continue
            existing = root_lexicon[root_id]
            if root not in existing["qac_roots_ar"]:
                existing["qac_roots_ar"].append(root)
            if not any(
                row.get("root_ar") == root
                for row in existing["qac_root_mappings"]
            ):
                existing["qac_root_mappings"].extend(
                    copy.deepcopy(record["qac_root_mappings"])
                )
    bundle = {
        "bundle_type": "ayah",
        "schema_version": bundle_builder.BUNDLE_SCHEMA_VERSION,
        "unit_kind": "numbered_ayah",
        "surah": surah,
        "ayah": ayah,
        "ayahRef": ref,
        "surface_ref": ref,
        "linguistic_source_ref": ref,
        "text": {
            "arabic_uthmani": quran_text,
            "source": bundle_builder.relpath(bundle_builder.QURAN_TEXT_TSV),
        },
        "qac_morphemes": qac_rows,
        "word_analysis": word_analysis,
        "branch_inventories": branch_inventories,
        "root_lexicon": root_lexicon,
        "coverage": {"root_lexicon": {"per_root": per_root}},
    }
    try:
        compositions.validate_unit_bundle(bundle, expected_ref=ref)
    except compositions.CompositionError as exc:
        raise workflow.WorkflowError(
            f"Reconstructed S:0 context bundle is invalid for {ref}: {exc}"
        ) from exc
    return bundle


def _s0_composition_context(
    composition: compositions.Composition,
    focus_ref: str,
    focus_bundle: dict[str, Any],
    context_root: Path,
) -> dict[str, list[dict[str, Any]]]:
    by_lane: dict[str, list[dict[str, Any]]] = {
        lane: [] for lane in workflow.LANES
    }
    source_cache: dict[int, dict[str, Any]] = {}
    for row in composition.context_rows(focus_ref):
        ref = row["ref"]
        path = compositions.unit_bundle_path(context_root, ref)
        if path.is_file() or path.is_symlink():
            try:
                _path, bundle, _identity = compositions.load_unit_bundle(
                    context_root, ref
                )
            except compositions.CompositionError as exc:
                raise workflow.WorkflowError(str(exc)) from exc
        else:
            surah, ayah = (int(part) for part in ref.split(":"))
            bundle = _source_context_bundle(surah, ayah, source_cache)
        by_lane[row["lane"]].append(
            compositions.project_context_unit(
                context_row=row,
                bundle=bundle,
                focus_bundle=focus_bundle,
            )
        )
    return by_lane


def prepare_s0(args: argparse.Namespace) -> dict[str, Any]:
    """Prepare one S:0 using the V5 output contract without monkeypatching V5."""
    layout = workflow.layout_for(args.ayah, workflow._analysis_id(args))
    composition = getattr(args, "composition", None)
    if composition is None:
        raise workflow.WorkflowError(
            "S:0 preparation requires its complete host-surah composition"
        )
    context_root = Path(args.context_bundles_dir).resolve(strict=False)
    member_root = Path(args.member_bundles_dir).resolve(strict=False)
    source_bundle, docket = _load_s0_focus_inputs(
        args, context_root, member_root
    )
    quran_evidence, quran_coverage = workflow._quran_text_projection(
        Path(args.quran_text)
    )
    if composition is not None:
        workflow._validate_basmala_focus_context(composition, quran_evidence)
    inter_rows, reciprocal, inter_coverage = workflow._load_inter_ayah_projection(
        args.ayah,
        Path(args.inter_ayah_dir),
        Path(args.inter_ayah_parent_dir),
        quran_evidence,
    )
    try:
        hft_projection = workflow.v3._hft_authoring_projection(
            docket, source_bundle
        )
    except SystemExit as exc:
        raise workflow.WorkflowError(str(exc)) from exc
    context_by_lane = _s0_composition_context(
        composition,
        args.ayah,
        source_bundle,
        context_root,
    )
    host_basmala = workflow._required_host_basmala(
        source_bundle, member_root, composition
    )

    packets: dict[str, dict[str, Any]] = {}
    for lane in workflow.LANES:
        packets[lane] = workflow._build_lane_packet(
            lane=lane,
            docket=docket,
            source_bundle=source_bundle,
            hft_projection=hft_projection,
            inter_rows=inter_rows,
            reciprocal=reciprocal,
            inter_coverage=inter_coverage,
            quran_evidence=quran_evidence,
            quran_coverage=quran_coverage,
            composition=composition,
            context_by_lane=context_by_lane,
            host_basmala=host_basmala,
        )
    workflow._finalize_compact_lane_packets(packets, source_bundle)
    alignment = source_bundle.get("coverage", {}).get(
        "word_morpheme_spans", {}
    )
    for packet in packets.values():
        packet["focus_word_alignment"] = {
            key: alignment[key]
            for key in (
                "alignment_version",
                "words_total",
                "words_resolved",
                "words_unresolved",
                "unresolved",
                "note",
                "source_namespace",
                "target_namespace",
                "bridge",
                "shared_morphemes",
            )
            if key in alignment
        }

    def load_lexical_source(ref: str) -> dict[str, Any]:
        path = compositions.unit_bundle_path(context_root, ref)
        root = context_root if path.is_file() else member_root
        return compositions.load_unit_bundle(root, ref)[1]

    try:
        supplements = workflow.reviewed_supplements.attach(
            packets,
            quran_evidence,
            Path(
                getattr(
                    args, "qac_morphology", workflow.DEFAULT_QAC_MORPHOLOGY
                )
            ),
            Path(
                getattr(
                    args,
                    "qac_cache_dir",
                    workflow.packet_evidence.DEFAULT_CACHE_DIR,
                )
            ),
            load_lexical_source,
        )
    except (
        workflow.reviewed_supplements.SupplementError,
        compositions.CompositionError,
    ) as exc:
        raise workflow.WorkflowError(str(exc)) from exc
    context_morphology_status = (
        "targeted" if supplements["micro_reference_refs"] else "not_requested"
    )
    prompts = {
        lane: workflow._build_scope_prompt(layout, lane, packets[lane])
        for lane in workflow.LANES
    }

    if getattr(args, "check_only", False):
        return {
            "schema_version": "commentary-v5-preparation-check-v1",
            "status": "checked",
            "analysis_id": layout.analysis_id,
            "ayah_ref": layout.ayah_ref,
            "agent_input_contract": "early-v5-compact",
            "context_morphology_status": context_morphology_status,
            "missing_context_morphology_refs": [],
            "reviewed_supplements": supplements,
            "prompt_bytes": {
                lane: len(prompt.encode("utf-8"))
                for lane, prompt in prompts.items()
            },
            "word_alignment": source_bundle.get("coverage", {}).get(
                "word_morpheme_spans", {}
            ),
        }

    workflow._assert_confined(layout.raw, workflow.RAW_ROOT)
    workflow._assert_confined(layout.editorial, workflow.EDITORIAL_ROOT)
    layout.raw.mkdir(parents=True, exist_ok=True)
    layout.editorial.mkdir(parents=True, exist_ok=True)
    for lane, prompt in prompts.items():
        workflow._atomic_write(
            layout.scope_prompt(lane),
            prompt.encode("utf-8"),
            root=workflow.INPUT_ROOT,
        )

    return {
        "schema_version": "commentary-v5-prepared-v1",
        "status": "prepared",
        "agent_input_contract": "early-v5-compact",
        "context_morphology_status": context_morphology_status,
        "missing_context_morphology_refs": [],
        "reviewed_supplements": supplements,
        "focus_word_alignment": packets["micro"]["focus_word_alignment"],
        "analysis_id": layout.analysis_id,
        "ayah_ref": layout.ayah_ref,
        "focus_context_brief": {
            "focus_ref": layout.ayah_ref,
            "analysis_id": layout.analysis_id,
            "context_refs": list(composition.context_refs(layout.ayah_ref)),
            "automatic_host_basmala_ref": (
                host_basmala[2]["ayah_ref"] if host_basmala is not None else None
            ),
            "external_ayat_refs": list(composition.added_ayat_refs),
        },
        "handoffs": [
            {
                "lane": lane,
                "prompt": str(layout.scope_prompt(lane).resolve(strict=False)),
                "discovery_output": str(
                    layout.scope_discovery(lane).resolve(strict=False)
                ),
                "scope_prose_output": str(
                    layout.scope_prose(lane).resolve(strict=False)
                ),
                "scope_ledger_output": str(
                    layout.scope_ledger(lane).resolve(strict=False)
                ),
                "composition_template": str(
                    (workflow.PROMPTS_ROOT / "composition.md").resolve(
                        strict=False
                    )
                ),
                "launch": "fresh_agent",
                "keep_session_open": True,
            }
            for lane in workflow.LANES
        ],
        "orchestration": {
            "scope_launch": "launch all three handoffs in parallel",
            "scope_follow_up": (
                "after nomination, fill prompts/composition.md and ask each same "
                "live agent to write its scope prose and landing ledger"
            ),
            "consolidation": (
                "close scope agents, then give the three scope prose texts, "
                "the pinned project guidance, and a short focus/context brief "
                "to one fresh consolidator"
            ),
            "editorial": (
                "ask that same consolidator for the editorial rewrite, then close"
            ),
            "invitation": (
                "after editorial completion, run prepare-invitation and launch its "
                "fresh Luna max handoff as a monitored invitation stage"
            ),
            "post_launch_gates": [],
        },
        "generated_files": [
            str(layout.scope_prompt(lane).resolve(strict=False))
            for lane in workflow.LANES
        ],
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Prepare one prefatory S:0 focus for commentary V5."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    prepare_parser = subparsers.add_parser(
        "prepare", help="Validate and write the three S:0 scope prompts."
    )
    prepare_parser.add_argument(
        "--check-only",
        action="store_true",
        help="Validate the prompts without writing files or handoffs.",
    )
    prepare_parser.add_argument(
        "--ayah",
        action="extend",
        nargs="+",
        required=True,
        metavar="S:0",
        help="Exactly one prefatory basmala reference.",
    )
    prepare_parser.add_argument("--analysis-id", default="native")
    prepare_parser.add_argument(
        "--segment", action="append", default=[], metavar="ID=REFS"
    )
    prepare_parser.add_argument("--analysis", type=Path)
    prepare_parser.add_argument("--member-surah", type=int)
    prepare_parser.add_argument(
        "--add-ayat",
        "--add-member",
        dest="add_ayat",
        action="append",
        default=[],
        metavar="REF[,REF...]",
    )
    workflow._source_options(prepare_parser)
    return parser


def _single_s0_request(
    args: argparse.Namespace,
) -> tuple[str, compositions.Composition | None]:
    refs, composition = workflow._resolve_request(args)
    if len(refs) != 1 or S0_REF_RE.fullmatch(refs[0]) is None:
        raise workflow.WorkflowError(
            "prepare_s0.py accepts exactly one S:0 focus and no numbered ayat"
        )
    if args.docket is not None:
        raise workflow.WorkflowError(
            "--docket is not accepted because S:0 evidence must be rebuilt "
            "from its source bundle"
        )
    return refs[0], composition


def main() -> int:
    args = _parser().parse_args()
    try:
        ref, composition = _single_s0_request(args)
        workflow._preflight_qac(args)
        result = prepare_s0(
            argparse.Namespace(
                **{**vars(args), "ayah": ref, "composition": composition}
            )
        )
    except (workflow.WorkflowError, compositions.CompositionError, OSError) as exc:
        print(
            json.dumps({"status": "error", "error": str(exc)}, ensure_ascii=False),
            file=sys.stderr,
        )
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
