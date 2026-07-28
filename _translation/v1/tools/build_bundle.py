#!/usr/bin/env python3
"""Build a compact translation-agent bundle from live sibling-repo data."""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import os
import sqlite3
import tempfile
import unicodedata
from pathlib import Path


V1_DIR = Path(__file__).resolve().parents[1]
WORKSPACE = V1_DIR.parents[2]
ROOT_PACKET_DIR = WORKSPACE / "dictionary" / "data" / "output" / "root_packets"


def read_json(path: Path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def write_compact_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, separators=(",", ":"))
        handle.write("\n")


def root_packet_path(root_id: str) -> Path:
    exact = ROOT_PACKET_DIR / f"{root_id}.json"
    if exact.exists():
        return exact

    merged = sorted(
        path
        for pattern in (f"{root_id}--*.json", f"*--{root_id}.json")
        for path in ROOT_PACKET_DIR.glob(pattern)
    )
    if len(merged) == 1:
        return merged[0]
    if merged:
        raise FileNotFoundError(
            f"Multiple merged dictionary packets for {root_id}: {merged}"
        )
    raise FileNotFoundError(f"Missing dictionary evidence for {root_id}: {exact}")


def dictionary_root_packet(root_id: str) -> dict:
    packet = read_json(root_packet_path(root_id))
    if packet.get("root_envelope_id") == root_id:
        return packet

    scoped = {**packet}
    scoped["branches"] = [
        branch
        for branch in packet.get("branches", [])
        if branch.get("root_id", root_id) == root_id
    ]
    if not scoped["branches"]:
        raise FileNotFoundError(
            f"Dictionary packet {root_packet_path(root_id)} has no branches for {root_id}"
        )
    return scoped


def word_ref(morpheme_ref: str) -> str:
    return morpheme_ref.rsplit(":", 1)[0]


def morphology(row: dict[str, str]) -> dict[str, str]:
    result = {
        "role": row["morpheme_role"],
        "pos": row["pos"],
    }
    optional = {
        "aspect": "aspect",
        "mood": "mood",
        "voice": "voice",
        "measure": "measure",
        "person": "person",
        "gender": "gender",
        "number": "number",
        "case": "grammatical_case",
    }
    for output_key, source_key in optional.items():
        if row[source_key]:
            result[output_key] = row[source_key]
    return result


def language_policy(language: str) -> dict:
    if language == "tr":
        return {
            "standard": "Natural Contemporary Standard Turkey Turkish",
            "ordinaryVocabularyRule": (
                "Use fully established ordinary Turkish vocabulary regardless "
                "of historical etymology. Do not replace a natural Turkish "
                "word merely because it entered Turkish from another language."
            ),
            "religiousLabelRule": (
                "Do not use a conventional religious technical label as a "
                "substitute for translating the source occurrence. Express "
                "the occurrence-specific act or concept in transparent Turkish "
                "whenever the label would conceal its source-grounded meaning."
            ),
            "properNameRule": "Retain Allah as the source proper name.",
            "allowedUntranslatedProperNames": ["Allah"],
            "fallbackRule": (
                "When no single natural word is adequate, write a short, "
                "transparent Turkish phrase."
            ),
        }
    return {
        "standard": f"Contemporary standard language for {language}",
        "loanwordRule": "Follow ordinary target-language usage.",
        "allowedLoanwords": [],
    }


def gloss_evidence(source: dict, error_key: str = "error") -> dict:
    evidence = {
        "text": source["text"],
        "facetIds": source.get("facet_ids", []),
    }
    error = source.get(error_key, {})
    error_profile = {}
    if error.get("fit"):
        error_profile["fit"] = error["fit"]
    if error.get("preserves"):
        error_profile["preserves"] = error["preserves"]
    if error.get("loses_facet_ids"):
        error_profile["losesFacetIds"] = error["loses_facet_ids"]
    if error.get("loses"):
        error_profile["loses"] = error["loses"]
    if error.get("adds"):
        error_profile["adds"] = error["adds"]
    if error.get("collision"):
        error_profile["collision"] = error["collision"]
    if error.get("reason"):
        error_profile["reason"] = error["reason"]
    if error_profile:
        evidence["errorProfile"] = error_profile
    return evidence


def reviewed_entry_gloss_source(
    language: str,
    root_id: str,
    branch_ids: list[str],
) -> dict | None:
    result_root_id = root_packet_path(root_id).stem
    candidate_paths = [
        WORKSPACE
        / "quran-data"
        / "data"
        / "dictionary"
        / language
        / f"{result_root_id}_entry.json",
        WORKSPACE
        / "dictionary"
        / "v2"
        / "work"
        / "entry_creation"
        / result_root_id
        / language
        / "output"
        / f"{result_root_id}_entry.json",
        WORKSPACE
        / "dictionary"
        / "v2"
        / "work"
        / "entry_creation"
        / result_root_id
        / language
        / "fragments"
        / f"{result_root_id}_entry.json",
    ]
    path = next((candidate for candidate in candidate_paths if candidate.exists()), None)
    if path is None:
        return None

    entry = read_json(path)
    branch_cores: list[dict] = []
    contextual_senses: list[dict] = []
    for branch_id in branch_ids:
        branch_ref = f"{root_id}/{branch_id}"
        branch = next(
            item for item in entry["branches"] if item["branch_ref"] == branch_ref
        )
        branch_cores.append(
            {
                "branchId": branch_id,
                **gloss_evidence(
                    branch["concept_gloss"],
                    error_key="error_profile",
                ),
            }
        )
        for contextual in branch.get("contextual_glosses", []):
            contextual_senses.append(
                {
                    "branchId": branch_id,
                    **gloss_evidence(
                        contextual,
                        error_key="error_profile",
                    ),
                }
            )

    return {
        "evidenceLanguage": language,
        "branchCores": branch_cores,
        "contextualSenses": contextual_senses,
    }


def bridge_gloss_source(
    root_id: str,
    branch_ids: list[str],
) -> dict:
    packet = dictionary_root_packet(root_id)
    branch_cores: list[dict] = []
    contextual_senses: list[dict] = []
    for branch_id in branch_ids:
        branch = next(
            item for item in packet["branches"] if item["branch_id"] == branch_id
        )
        branch_cores.append(
            {
                "branchId": branch_id,
                "text": branch.get("what_is_en") or branch["branch_image_en"],
                "facetIds": [],
            }
        )
        if branch.get("branch_image_en"):
            contextual_senses.append(
                {
                    "branchId": branch_id,
                    "text": branch["branch_image_en"],
                    "facetIds": [],
                }
            )

    return {
        "evidenceLanguage": "en",
        "branchCores": branch_cores,
        "contextualSenses": contextual_senses,
    }


def gloss_source(
    language: str,
    root_id: str,
    branch_ids: list[str],
) -> dict:
    result_path = (
        WORKSPACE
        / "dictionary"
        / "v2"
        / "gloss_generation"
        / "results"
        / language
        / f"{root_packet_path(root_id).stem}.json"
    )
    if not result_path.exists():
        reviewed_entry = reviewed_entry_gloss_source(
            language,
            root_id,
            branch_ids,
        )
        if reviewed_entry:
            return compact_gloss_source(reviewed_entry, language)
        return compact_gloss_source(
            bridge_gloss_source(root_id, branch_ids),
            language,
        )

    result = read_json(result_path)
    branch_cores: list[dict] = []
    contextual_senses: list[dict] = []

    for branch_id in branch_ids:
        branch_ref = f"{root_id}/{branch_id}"
        branch = next(
            item for item in result["branches"] if item["branch_ref"] == branch_ref
        )

        concept = branch.get("concept_gloss")
        core_text = concept.get("text") if concept else None
        if not core_text:
            contextual = branch.get("contextual_glosses", [])
            core_text = contextual[0].get("text") if contextual else None
        if not core_text:
            raise ValueError(
                f"No target-language branch core for {root_id}/{branch_id} "
                f"in {language}"
            )
        branch_cores.append(
            {
                "branchId": branch_id,
                **gloss_evidence(concept or {"text": core_text}),
            }
        )

        for contextual in branch.get("contextual_glosses", []):
            contextual_senses.append(
                {
                    "branchId": branch_id,
                    **gloss_evidence(contextual),
                }
            )

    return compact_gloss_source({
        "evidenceLanguage": language,
        "branchCores": branch_cores,
        "contextualSenses": contextual_senses,
    }, language)


def compact_gloss_source(source: dict, target_language: str) -> dict:
    """Default evidenceLanguage to the target while preserving bridge evidence."""
    compact = dict(source)
    if compact.get("evidenceLanguage") == target_language:
        compact.pop("evidenceLanguage")
    return compact


def selected_evidence_ref(root_id: str, branch_ids: list[str]) -> str:
    """Return the stable key for one root and its selected branch set."""
    normalized = sorted(set(branch_ids))
    if not normalized:
        raise ValueError(f"{root_id}: selected branch set must not be empty")
    if len(normalized) != len(branch_ids):
        raise ValueError(f"{root_id}: selected branch IDs must be unique")
    return f"{root_id}/" + "+".join(normalized)


def _read_quran_release_id() -> str:
    release = read_json(WORKSPACE / "quran-data" / "RELEASE.json")
    return release["release_id"]


def root_join_key(root_norm: str) -> str:
    return "".join((root_norm or "").split())


def normalize_arabic_surface(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value or "")
    letters = [
        char
        for char in normalized
        if unicodedata.category(char) != "Mn" and char not in "ـ۞"
    ]
    return (
        "".join(letters)
        .replace("ٱ", "ا")
        .replace("آ", "ا")
        .replace("أ", "ا")
        .replace("إ", "ا")
    )


def _bridge_db_rows(path: Path) -> list[sqlite3.Row]:
    with gzip.open(path, "rb") as source:
        with tempfile.NamedTemporaryFile(suffix=".sqlite", delete=False) as temp:
            temp.write(source.read())
            temp_path = temp.name
    try:
        connection = sqlite3.connect(temp_path)
        connection.row_factory = sqlite3.Row
        try:
            return list(
                connection.execute(
                    """
                    SELECT
                      qac_root_norm,
                      qac_root_join_key,
                      mapping_status,
                      qac_total_occurrences,
                      matched_occurrences,
                      target_rank,
                      frozen_root_norm,
                      furuq_root_id,
                      furuq_root_norm,
                      furuq_source_root_norm,
                      furuq_resolution,
                      target_occurrences,
                      is_dominant,
                      has_furuq_root,
                      unmapped_reason
                    FROM qac_to_furuq
                    ORDER BY qac_root_norm, target_rank
                    """
                )
            )
        finally:
            connection.close()
    finally:
        os.unlink(temp_path)


def _compact_target(row: sqlite3.Row) -> dict:
    target = {
        "targetRank": row["target_rank"],
        "rootId": row["furuq_root_id"],
        "frozenRootNorm": row["frozen_root_norm"],
        "furuqRootNorm": row["furuq_root_norm"],
        "furuqSourceRootNorm": row["furuq_source_root_norm"],
        "resolution": row["furuq_resolution"],
        "occurrences": row["target_occurrences"],
        "isDominant": bool(row["is_dominant"]),
        "hasFuruqRoot": bool(row["has_furuq_root"]),
    }
    return {key: value for key, value in target.items() if value not in (None, "")}


def root_resolutions(surah: int, v12_dir: Path) -> tuple[dict[str, dict], str]:
    """QAC-root to Furuq-root gateway, preserving split target sets."""
    bridge_path = (
        WORKSPACE
        / "quran-data"
        / "data"
        / "bridges"
        / "qac-furuq-v4-root-map.sqlite.gz"
    )
    if bridge_path.exists():
        resolutions: dict[str, dict] = {}
        for row in _bridge_db_rows(bridge_path):
            join_key = row["qac_root_join_key"]
            resolution = resolutions.setdefault(
                join_key,
                {
                    "qacRootNorm": row["qac_root_norm"],
                    "qacRootJoinKey": join_key,
                    "mappingStatus": row["mapping_status"],
                    "qacTotalOccurrences": row["qac_total_occurrences"],
                    "matchedOccurrences": row["matched_occurrences"],
                    "targets": [],
                },
            )
            if row["has_furuq_root"]:
                resolution["targets"].append(_compact_target(row))
            elif row["unmapped_reason"]:
                resolution["unmappedReason"] = row["unmapped_reason"]
        return resolutions, _read_quran_release_id()

    return _legacy_root_resolutions(surah, v12_dir)


def _legacy_root_resolutions(surah: int, v12_dir: Path) -> tuple[dict[str, dict], str]:
    surah_key = f"s{surah:03d}"
    crosswalk_path = (
        WORKSPACE
        / "quran-apps"
        / "packages"
        / "content-compiler"
        / "crosswalks"
        / f"{surah_key}-qac-root-to-furuq.json"
    )
    if crosswalk_path.exists():
        crosswalk = read_json(crosswalk_path)
        return (
            {
                item["qacRootJoinKey"]: {
                    "qacRootJoinKey": item["qacRootJoinKey"],
                    "mappingStatus": "unique",
                    "targets": [
                        {
                            "targetRank": 1,
                            "rootId": item["furuqRootId"],
                            "isDominant": True,
                            "hasFuruqRoot": True,
                        }
                    ],
                }
                for item in crosswalk["mappings"]
            },
            crosswalk["quranDataReleaseId"],
        )

    anchor_map = read_json(v12_dir / "anchor_map.v3.json")
    columns = {name: index for index, name in enumerate(anchor_map["columns"])}
    candidates: dict[str, set[str]] = {}
    for row in anchor_map["rows"]:
        join_key = "".join(row[columns["source_root"]].split())
        candidates.setdefault(join_key, set()).add(row[columns["root_id"]])
    ambiguous = {key: ids for key, ids in candidates.items() if len(ids) != 1}
    if ambiguous:
        raise ValueError(f"Ambiguous V12 root bindings: {ambiguous}")

    return (
        {
            key: {
                "qacRootJoinKey": key,
                "mappingStatus": "unique",
                "targets": [
                    {
                        "targetRank": 1,
                        "rootId": next(iter(ids)),
                        "isDominant": True,
                        "hasFuruqRoot": True,
                    }
                ],
            }
            for key, ids in candidates.items()
        },
        _read_quran_release_id(),
    )


def root_bindings(surah: int, v12_dir: Path) -> tuple[dict[str, str], str]:
    """Compatibility view for consumers that require one root id per QAC root."""
    resolutions, release = root_resolutions(surah, v12_dir)
    used_keys: set[str] = set()
    morphemes_path = v12_dir / "linguistic" / "morphemes.tsv"
    if morphemes_path.exists():
        with morphemes_path.open(encoding="utf-8", newline="") as handle:
            used_keys = {
                row["root_join_key"]
                for row in csv.DictReader(handle, delimiter="\t")
                if row["root_join_key"]
            }

    bindings: dict[str, str] = {}
    ambiguous: dict[str, list[str]] = {}
    no_targets: dict[str, str] = {}
    for join_key, resolution in resolutions.items():
        if used_keys and join_key not in used_keys:
            continue
        targets = [target for target in resolution["targets"] if target.get("rootId")]
        if len(targets) == 1 and resolution["mappingStatus"] == "unique":
            bindings[join_key] = targets[0]["rootId"]
        elif targets:
            ambiguous[join_key] = [target["rootId"] for target in targets]
        else:
            no_targets[join_key] = (
                resolution.get("unmappedReason")
                or str(resolution.get("mappingStatus"))
            )
    if ambiguous:
        raise ValueError(
            f"Ambiguous root bindings require root-scoped anchors: {ambiguous}"
        )
    if no_targets:
        raise ValueError(f"Root bindings without Furuq targets: {no_targets}")
    return bindings, release


def root_resolution_for_join_key(resolutions: dict[str, dict], join_key: str) -> dict:
    try:
        return resolutions[join_key]
    except KeyError as exc:
        raise ValueError(f"No QAC/Furuq root resolution for {join_key!r}") from exc


def usable_targets(resolution: dict) -> list[dict]:
    return [target for target in resolution.get("targets", []) if target.get("rootId")]


def component_root_targets(
    base_resolutions: dict[str, dict],
    component_roots: list[str],
) -> list[dict]:
    targets: list[dict] = []
    seen: set[str] = set()
    for component_root in component_roots:
        component = base_resolutions.get(root_join_key(component_root))
        if not component:
            continue
        component_targets = usable_targets(component)
        if len(component_targets) != 1:
            continue
        target = {**component_targets[0]}
        root_id = target["rootId"]
        if root_id in seen:
            continue
        target["targetRank"] = len(targets) + 1
        target["componentRootNorm"] = component_root
        target["componentQacRootNorm"] = component.get("qacRootNorm")
        target["componentMappingStatus"] = component.get("mappingStatus")
        target["isDominant"] = False
        targets.append(target)
        seen.add(root_id)
    return targets


def frozen_occurrence_overlays(
    surah: int,
    morpheme_rows: list[dict[str, str]],
    base_resolutions: dict[str, dict],
) -> dict[str, dict]:
    audit_path = (
        WORKSPACE
        / "latent_activation"
        / "_status"
        / "v12_cross_run"
        / "audits"
        / "frozen-qac-root-bridge-occurrences.tsv"
    )
    if not audit_path.exists():
        return {}

    rooted_rows = [
        row
        for row in morpheme_rows
        if row["root_join_key"] and row["morpheme_role"] == "STEM"
    ]
    by_ayah: dict[str, list[dict[str, str]]] = {}
    for row in rooted_rows:
        ayah_ref = ":".join(row["qac_ref"].split(":")[:2])
        by_ayah.setdefault(ayah_ref, []).append(row)

    overlays: dict[str, dict] = {}
    with audit_path.open(encoding="utf-8", newline="") as handle:
        for audit in csv.DictReader(handle, delimiter="\t"):
            word_ref = audit["word_ref"]
            if not word_ref.startswith(f"{surah}:"):
                continue
            raw_root = audit["frozen_root_raw"]
            if "/" not in raw_root:
                continue
            if audit["furuq_resolution"] != "missing_furuq_root":
                continue

            component_roots = [
                component.strip()
                for component in raw_root.split("/")
                if component.strip()
            ]
            targets = component_root_targets(base_resolutions, component_roots)
            if len(targets) < 2:
                continue

            ayah_ref = ":".join(word_ref.split(":")[:2])
            audit_surface = normalize_arabic_surface(audit["surface_ar"])
            candidates = []
            for row in by_ayah.get(ayah_ref, []):
                qac_word = normalize_arabic_surface(row.get("surface_ar") or "")
                qac_stem = normalize_arabic_surface(row.get("stem_ar") or "")
                if audit_surface in qac_word or qac_stem in audit_surface:
                    candidates.append(row)
            if len(candidates) != 1:
                continue

            row = candidates[0]
            overlays[row["qac_ref"]] = {
                "qacRootNorm": row["root"],
                "qacRootJoinKey": row["root_join_key"],
                "mappingStatus": "split",
                "resolutionSource": "frozen_occurrence_combined_root",
                "frozenOccurrenceWordRef": word_ref,
                "frozenRootNorm": audit["frozen_root_norm"],
                "frozenRootRaw": raw_root,
                "targets": targets,
            }
    return overlays


def root_resolution_for_row(
    base_resolutions: dict[str, dict],
    occurrence_overlays: dict[str, dict],
    row: dict[str, str],
) -> dict:
    return occurrence_overlays.get(
        row["qac_ref"],
        root_resolution_for_join_key(base_resolutions, row["root_join_key"]),
    )


def select_anchor_root_id(anchor: dict, resolution: dict, qac_ref: str) -> str:
    targets = usable_targets(resolution)
    target_ids = [target["rootId"] for target in targets]
    if not targets:
        raise ValueError(
            f"No Furuq root target for rooted {qac_ref}: "
            f"{resolution.get('unmappedReason') or resolution.get('mappingStatus')}"
        )
    root_id = anchor.get("rootId")
    if root_id:
        if root_id not in target_ids:
            raise ValueError(
                f"{qac_ref}: selected rootId {root_id!r} is not among "
                f"QAC/Furuq targets {target_ids}"
            )
        return root_id
    if len(targets) == 1 and resolution.get("mappingStatus") == "unique":
        return targets[0]["rootId"]
    raise ValueError(
        f"{qac_ref}: rootId is required because QAC root "
        f"{resolution.get('qacRootNorm') or resolution.get('qacRootJoinKey')} "
        f"has {resolution.get('mappingStatus')} targets {target_ids}"
    )


def primary_anchor(anchor: dict) -> dict:
    """Compatibility view over v1-v4 anchor records."""
    primary = anchor.get("primary")
    if primary is not None:
        if not isinstance(primary, dict):
            raise ValueError(
                f"{anchor.get('qacMorphemeRef')}: primary must be an object"
            )
        return primary
    return anchor


def grammar_unit_ref(unit_id: str) -> str | None:
    value = unit_id.strip()
    parts = value.split(":")
    if (
        len(parts) == 4
        and parts[0] == "q"
        and all(part.isdigit() for part in parts[1:])
    ):
        return value
    return None


def grammar_support_by_ayah(surah: int) -> dict[str, list[dict]]:
    path = (
        WORKSPACE
        / "quran-data"
        / "data"
        / "grammar"
        / "attachments"
        / "translation_support.tsv"
    )
    support: dict[str, list[dict]] = {}
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if row["row_kind"] != "support" or int(row["sura"]) != surah:
                continue

            refs: list[str] = []
            raw_refs = [row["anchor_unit_id"]]
            raw_refs.extend(row["related_word_unit_ids"].split(";"))
            for raw_ref in raw_refs:
                ref = grammar_unit_ref(raw_ref)
                if ref and ref not in refs:
                    refs.append(ref)
            if not row["risk"]:
                continue

            item = {
                "type": row["support_type"],
                "instruction": row["translation_instruction"],
                "guidance": row["risk"],
            }
            if refs:
                item["grammarUnitRefs"] = refs
            if row["construction"]:
                item["construction"] = row["construction"]
            if row["scope"]:
                item["scope"] = row["scope"]
            if row["force"]:
                item["force"] = row["force"]

            ayah_ref = f"{surah}:{int(row['ayah'])}"
            support.setdefault(ayah_ref, []).append(item)
    return support


def reading_alignment(baseline: dict) -> list[dict[str, list[str]]]:
    groups: list[dict[str, list[str]]] = []
    for _, refs in baseline["target_tokens"]:
        if groups and groups[-1]["qacWordRefs"] == refs:
            continue
        groups.append({"qacWordRefs": refs})
    return groups


def parse_ayah_range(value: str | None) -> tuple[int, int] | None:
    if not value:
        return None
    if "-" in value:
        first, last = value.split("-", 1)
        return int(first), int(last)
    return int(value), int(value)


def in_ayah_range(surah: int, ayah_ref: str, ayahs: tuple[int, int] | None) -> bool:
    if ayahs is None:
        return True
    ayah_surah, ayah_number = (int(part) for part in ayah_ref.split(":"))
    if ayah_surah == surah:
        return ayahs[0] <= ayah_number <= ayahs[1]
    # Prefatory basmalah rows carry another surah's ref and belong to the
    # first chunk only, matching build_anchor_input.py.
    return ayahs[0] <= 1


def validate_translation_input(bundle: dict) -> list[str]:
    """Ensure writer-visible evidence never escapes the selected branches."""
    errors: list[str] = []
    target_language = bundle.get("targetLanguage")
    evidence_registry = bundle.get("selectedBranchEvidence")
    if not isinstance(evidence_registry, dict):
        return ["selectedBranchEvidence must be an object"]

    used_evidence_refs: set[str] = set()
    for ayah in bundle.get("ayat", []):
        for card in ayah.get("cards", []):
            ref = card.get("qacMorphemeRef", "<unknown>")
            forbidden = {
                "candidateGlossSources",
                "rootResolution",
                "qacWordRef",
                "glossId",
                "glossSource",
            } & set(card)
            if forbidden:
                errors.append(f"{ref}: forbidden writer fields {sorted(forbidden)}")
            if "rootId" not in card:
                if "evidenceRef" in card:
                    errors.append(f"{ref}: unrooted card has evidenceRef")
                continue

            branch_ids = card.get("branchIds", [])
            selected = set(branch_ids)
            try:
                expected_evidence_ref = selected_evidence_ref(
                    card["rootId"],
                    branch_ids,
                )
            except ValueError as error:
                errors.append(f"{ref}: {error}")
                continue
            evidence_ref = card.get("evidenceRef")
            if evidence_ref != expected_evidence_ref:
                errors.append(
                    f"{ref}: evidenceRef must be {expected_evidence_ref!r}, "
                    f"found {evidence_ref!r}"
                )
                continue
            used_evidence_refs.add(evidence_ref)
            source = evidence_registry.get(evidence_ref)
            if not isinstance(source, dict):
                errors.append(
                    f"{ref}: evidenceRef {evidence_ref!r} has no registry entry"
                )
                continue
            evidence_language = source.get("evidenceLanguage", target_language)
            if source.get("evidenceLanguage") == target_language:
                errors.append(
                    f"{evidence_ref}: evidenceLanguage matching targetLanguage "
                    "must be omitted"
                )
            if not isinstance(evidence_language, str) or not evidence_language:
                errors.append(f"{evidence_ref}: invalid evidence language")

            core_branches = {
                item.get("branchId")
                for item in source.get("branchCores", [])
                if isinstance(item, dict)
            }
            if core_branches != selected:
                errors.append(
                    f"{ref}: branch-core evidence {sorted(core_branches)} "
                    f"does not equal selected branches {sorted(selected)}"
                )
            for index, item in enumerate(source.get("contextualSenses", [])):
                branch_id = item.get("branchId") if isinstance(item, dict) else None
                if branch_id not in selected:
                    errors.append(
                        f"{ref}: contextualSenses[{index}] exposes unselected "
                        f"branch {branch_id!r}"
                    )
            if "lexicalSenses" in source:
                errors.append(f"{evidence_ref}: lexicalSenses is forbidden")

    unused = sorted(set(evidence_registry) - used_evidence_refs)
    if unused:
        errors.append(f"unused selectedBranchEvidence entries: {unused}")
    return errors


def build_bundle(
    surah: int,
    language: str,
    ayahs: tuple[int, int] | None = None,
    anchor_path: Path | None = None,
) -> dict:
    surah_key = f"s{surah:03d}"
    v12_dir = (
        WORKSPACE / "latent_activation" / "_status" / "v12_cross_run" / surah_key
    )
    roster = read_json(v12_dir / "ayah_roster.v3.json")
    anchor_path = anchor_path or V1_DIR / "source" / f"{surah_key}.primary-anchors.json"
    if not anchor_path.exists():
        raise SystemExit(
            f"error: no primary-anchor seed for surah {surah}: {anchor_path}\n"
            "stage 0 has not run for this surah. See _translation/v1/orchestrator.md:\n"
            f"  python3 _translation/v1/tools/build_anchor_input.py --surah {surah}\n"
            f"  python3 _translation/v1/tools/instantiate.py --surah {surah} --stage anchors"
        )
    anchor_seed = read_json(anchor_path)
    anchors = {
        item["qacMorphemeRef"]: item for item in anchor_seed["anchors"]
    }
    unresolved_anchors = {
        item.get("qacMorphemeRef"): item
        for item in anchor_seed.get("unresolved", [])
        if isinstance(item, dict)
    }

    resolutions, quran_data_release_id = root_resolutions(surah, v12_dir)
    grammar_support = grammar_support_by_ayah(surah)

    morphemes_by_ayah: dict[str, list[dict[str, str]]] = {}
    morpheme_rows: list[dict[str, str]] = []
    with (v12_dir / "linguistic" / "morphemes.tsv").open(
        encoding="utf-8", newline=""
    ) as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            morpheme_rows.append(row)
            ayah_ref = ":".join(row["qac_ref"].split(":")[:2])
            morphemes_by_ayah.setdefault(ayah_ref, []).append(row)
    occurrence_overlays = frozen_occurrence_overlays(
        surah,
        morpheme_rows,
        resolutions,
    )

    ayat = []
    selected_branch_evidence: dict[str, dict] = {}
    for v12_ref, arabic_text, ayah_ref, baseline in roster["rows"]:
        del v12_ref
        if not in_ayah_range(surah, ayah_ref, ayahs):
            continue
        cards = []
        for row in morphemes_by_ayah.get(ayah_ref, []):
            qac_ref = row["qac_ref"]
            card = {
                "qacMorphemeRef": qac_ref,
                "arabic": row["surface_ar"],
                "morphology": morphology(row),
            }
            if row["lemma_ar"]:
                card["lemma"] = row["lemma_ar"]

            anchor = anchors.get(qac_ref)
            if row["root_join_key"]:
                resolution = root_resolution_for_row(
                    resolutions,
                    occurrence_overlays,
                    row,
                )
                if anchor is None:
                    unresolved = unresolved_anchors.get(qac_ref)
                    if unresolved:
                        raise ValueError(
                            f"Unresolved primary anchor for rooted {qac_ref}: "
                            f"{unresolved.get('reason')}"
                        )
                    raise ValueError(f"Missing primary anchor for rooted {qac_ref}")
                selected_anchor = primary_anchor(anchor)
                root_id = select_anchor_root_id(
                    selected_anchor,
                    resolution,
                    qac_ref,
                )
                branch_ids = selected_anchor["branchIds"]
                evidence_ref = selected_evidence_ref(root_id, branch_ids)
                if evidence_ref not in selected_branch_evidence:
                    selected_branch_evidence[evidence_ref] = gloss_source(
                        language,
                        root_id,
                        sorted(branch_ids),
                    )
                card.update(
                    {
                        "rootId": root_id,
                        "branchIds": branch_ids,
                        "evidenceRef": evidence_ref,
                    }
                )
            elif anchor is not None:
                raise ValueError(f"Unexpected anchor on unrooted {qac_ref}")

            cards.append(card)

        ayat.append(
            {
                "ayahRef": ayah_ref,
                "arabicText": arabic_text,
                "primaryReading": {
                    "alignmentGroups": reading_alignment(baseline),
                },
                "grammarSupport": grammar_support.get(ayah_ref, []),
                "cards": cards,
            }
        )

    bundle = {
        "schemaVersion": "translation-input-v2",
        "targetLanguage": language,
        "languagePolicy": language_policy(language),
        "quranDataReleaseId": quran_data_release_id,
        "surah": surah,
        "selectedBranchEvidence": selected_branch_evidence,
        "ayat": ayat,
    }
    errors = validate_translation_input(bundle)
    if errors:
        raise ValueError("Invalid translation input:\n" + "\n".join(errors))
    return bundle


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--language", required=True)
    parser.add_argument(
        "--ayahs",
        help="ayah chunk, e.g. '1' or '1-20'. Prefatory basmalah rows are "
        "included in the first chunk.",
    )
    parser.add_argument("--anchors", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    surah_key = f"s{args.surah:03d}"
    ayahs = parse_ayah_range(args.ayahs)
    suffix = f".{ayahs[0]}-{ayahs[1]}" if ayahs else ""
    output = args.output or (
        V1_DIR / "input" / args.language / f"{surah_key}{suffix}.json"
    )

    # Build before opening the file. Opening first left an empty bundle behind
    # whenever the build raised — a file that is present and says nothing, which
    # is the failure mode this repo treats as worse than an absent one.
    bundle = build_bundle(args.surah, args.language, ayahs, args.anchors)

    write_compact_json(output, bundle)


if __name__ == "__main__":
    main()
