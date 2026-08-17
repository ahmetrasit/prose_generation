#!/usr/bin/env python3
"""Build an immutable, Layer-2-v2-aware source packet for Layer 3."""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any

from common import (
    REPO_ROOT,
    WORKFLOW_ROOT,
    content_hash,
    immutable_write_json,
    load_json,
    normalize_language,
    portable_path,
    sha256_file,
)


LAYER2_KINDS = ("prose", "evidence", "index", "friction")
LAYER2_ROLES = {
    "prose": "commentary-audit",
    "evidence": "claim-boundary",
    "index": "findings-handoff",
    "friction": "production-audit",
}
INDEX_ROW = re.compile(r"^\s*-\s+`([^`]+)`\s+(?:—|–|-)\s+(.+?)\s*$")
TRAILING_FLAG = re.compile(r"\s+\[([a-z-]+)\]\s*$")
RESONANCE_KEY = re.compile(r"^surprise:([a-z0-9][a-z0-9-]*)$")
ALLOWED_INDEX_FLAGS = {"inference", "supports-primary", "shifts-primary"}
V11_SECTION_IDS = {
    "most surprising discoveries": "surprising-discoveries",
    "acik sorular": "boundaries",
}


def warn(message: str, warnings: list[str]) -> None:
    warnings.append(message)
    print(f"warning: {message}", file=sys.stderr)


def folded(value: str) -> str:
    value = value.replace("\u0131", "i").replace("\u0130", "I")
    return "".join(
        character
        for character in unicodedata.normalize("NFKD", value)
        if not unicodedata.combining(character)
    ).casefold()


def source_format(path: Path) -> str:
    if path.suffix in {".json", ".jsonl"}:
        return "json"
    if path.suffix == ".tsv":
        return "tsv"
    return "markdown"


def register_source(
    registry: list[dict[str, Any]],
    *,
    source_id: str,
    kind: str,
    role: str,
    path: Path,
    projection: str,
    quran_data: Path,
    latent_activation: Path,
) -> str:
    registry.append(
        {
            "sourceId": source_id,
            "kind": kind,
            "role": role,
            "path": portable_path(
                path,
                quran_data=quran_data,
                latent_activation=latent_activation,
            ),
            "format": source_format(path),
            "sha256": sha256_file(path),
            "bytes": path.stat().st_size,
            "projection": projection,
        }
    )
    return source_id


def parse_quran_text(path: Path, surah: int) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    prefix = f"{surah}:"
    for raw_line in path.read_text(encoding="utf-8-sig").splitlines():
        if not raw_line.startswith(prefix):
            continue
        try:
            ayah_ref, arabic = raw_line.split("|", 1)
        except ValueError as exc:
            raise SystemExit(f"error: malformed Quran text row: {raw_line!r}") from exc
        rows.append({"ayahRef": ayah_ref, "arabic": arabic})
    if not rows:
        raise SystemExit(f"error: no Quran text found for surah {surah} in {path}")
    refs = [row["ayahRef"] for row in rows]
    if len(refs) != len(set(refs)):
        raise SystemExit(f"error: duplicate Quran rows for surah {surah} in {path}")
    return rows


def parse_primary_floor(
    path: Path,
    *,
    surah: int,
    language: str,
    required_refs: set[str],
) -> dict[str, str]:
    data = load_json(path)
    if not isinstance(data, dict):
        raise SystemExit(f"error: primary floor must be a JSON object: {path}")
    if data.get("schemaVersion") != "translation-layer-v1":
        raise SystemExit(f"error: unsupported primary-floor schema in {path}")
    if data.get("surah") != surah:
        raise SystemExit(
            f"error: primary floor in {path} is for surah {data.get('surah')}, "
            f"expected {surah}"
        )
    if normalize_language(str(data.get("language", ""))) != language:
        raise SystemExit(
            f"error: primary floor in {path} has language {data.get('language')!r}, "
            f"expected {language!r}"
        )
    lines: dict[str, str] = {}
    for item in data.get("ayat", []):
        if not isinstance(item, dict):
            continue
        ayah_ref = item.get("ayahRef")
        text = item.get("translation", {}).get("text")
        if ayah_ref in required_refs and isinstance(text, str) and text.strip():
            if ayah_ref in lines:
                raise SystemExit(
                    f"error: duplicate primary-floor line {ayah_ref} in {path}"
                )
            lines[ayah_ref] = text.strip()
    missing = sorted(required_refs - lines.keys())
    if missing:
        raise SystemExit(
            f"error: primary floor {path} is incomplete; missing "
            + ", ".join(missing)
        )
    return lines


def layer2_artifact_sets(
    directory: Path,
    surah: int,
    ayah: int,
) -> dict[str, dict[str, Path]]:
    prefix = f"{surah}_{ayah}."
    by_label: dict[str, dict[str, Path]] = {}
    for path in sorted(directory.glob(f"{surah}_{ayah}.*.md")):
        stem = path.name[: -len(".md")]
        if not stem.startswith(prefix):
            continue
        parts = stem[len(prefix) :].split(".")
        if not parts or parts[0] not in LAYER2_KINDS:
            continue
        kind = parts[0]
        label = ".".join(parts[1:])
        by_label.setdefault(label, {})[kind] = path
    return by_label


def select_layer2_artifact_set(
    directory: Path,
    surah: int,
    ayah: int,
    label: str | None,
) -> tuple[str, dict[str, Path]]:
    candidates = layer2_artifact_sets(directory, surah, ayah)
    complete = {
        candidate_label: paths
        for candidate_label, paths in candidates.items()
        if set(paths) == set(LAYER2_KINDS)
    }
    if label is not None:
        if label in complete:
            return label, complete[label]
        found = ", ".join(repr(item) for item in sorted(complete)) or "none"
        raise SystemExit(
            f"error: no complete Layer-2 artifact set labelled {label!r} for "
            f"{surah}:{ayah} in {directory}; complete labels: {found}"
        )
    if len(complete) == 1:
        return next(iter(complete.items()))
    if not complete:
        inventory = ", ".join(
            f"{candidate_label!r}={sorted(paths)}"
            for candidate_label, paths in sorted(candidates.items())
        ) or "no matching files"
        raise SystemExit(
            f"error: no complete Layer-2 prose/evidence/index/friction set for "
            f"{surah}:{ayah} in {directory}; found {inventory}"
        )
    rendered = "\n".join(f"  {item!r}" for item in sorted(complete))
    raise SystemExit(
        f"error: ambiguous complete Layer-2 artifact sets for {surah}:{ayah}; "
        f"pass --layer2-label:\n{rendered}"
    )


def parse_index(
    path: Path,
    *,
    surah: int,
    ayah: int,
    source_id: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    findings: list[dict[str, Any]] = []
    resonances: list[dict[str, Any]] = []
    resonance_refs: set[str] = set()
    for line_number, raw_line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not raw_line.strip():
            continue
        match = INDEX_ROW.fullmatch(raw_line)
        if match is None:
            raise SystemExit(
                f"error: malformed findings-index row at {path}:{line_number}: "
                f"{raw_line!r}"
            )
        index_key, body = match.groups()
        flags: list[str] = []
        while True:
            flag_match = TRAILING_FLAG.search(body)
            if flag_match is None:
                break
            flags.append(flag_match.group(1))
            body = body[: flag_match.start()].rstrip()
        flags.reverse()
        unknown = sorted(set(flags) - ALLOWED_INDEX_FLAGS)
        if unknown:
            raise SystemExit(
                f"error: unsupported findings-index flag(s) at {path}:{line_number}: "
                + ", ".join(unknown)
            )
        if not body:
            raise SystemExit(f"error: empty findings-index text at {path}:{line_number}")
        relation_flags = {
            flag for flag in flags if flag in {"supports-primary", "shifts-primary"}
        }
        finding_ref = f"finding:{surah}:{ayah}:{len(findings) + 1:03d}"
        record = {
            "findingRef": finding_ref,
            "indexKey": index_key,
            "text": body,
            "inference": "inference" in flags,
            "sourceRefs": [f"{source_id}#line-{line_number}"],
        }
        findings.append(record)
        resonance_match = RESONANCE_KEY.fullmatch(index_key)
        if resonance_match is None:
            if relation_flags:
                raise SystemExit(
                    f"error: primary-relation flag on non-surprise row at "
                    f"{path}:{line_number}"
                )
            continue
        if len(relation_flags) != 1:
            raise SystemExit(
                f"error: surprise row at {path}:{line_number} must carry exactly "
                "one of [supports-primary] or [shifts-primary]"
            )
        if "inference" not in flags:
            raise SystemExit(
                f"error: surprise row at {path}:{line_number} must carry [inference]"
            )
        resonance_ref = f"resonance:{surah}:{ayah}:{resonance_match.group(1)}"
        if resonance_ref in resonance_refs:
            raise SystemExit(
                f"error: duplicate local resonance {resonance_ref!r} in {path}"
            )
        resonance_refs.add(resonance_ref)
        resonances.append(
            {
                "resonanceRef": resonance_ref,
                "findingRef": finding_ref,
                "text": body,
                "primaryRelation": next(iter(relation_flags)),
                "sourceRefs": record["sourceRefs"],
            }
        )
    if not findings:
        raise SystemExit(f"error: findings index is empty: {path}")
    return findings, resonances


def heading_title(line: str) -> str | None:
    stripped = line.strip()
    hash_match = re.match(r"^#{1,6}\s+(.+?)\s*$", stripped)
    if hash_match:
        return hash_match.group(1)
    bold_match = re.match(r"^\*\*(.+?)\*\*(?::)?(?:\s+.*)?$", stripped)
    if bold_match:
        return bold_match.group(1)
    normalized = folded(stripped).rstrip(":")
    if normalized.startswith(("karsi", "korunan ret", "ret ve")):
        return stripped
    if normalized.startswith(("kapsam", "kapsama")):
        return stripped
    return None


def is_boundary_heading(title: str) -> bool:
    normalized = folded(title).lstrip("*# ").strip()
    return normalized.startswith(
        (
            "karsi",
            "korunan karsi",
            "korunan ret",
            "ret ",
            "retler",
            "sinir",
            "counter",
            "rejected",
            "preserved counter",
            "preserved rejected",
            "boundar",
        )
    )


def is_scope_heading(title: str) -> bool:
    return folded(title).startswith(("kapsam", "kapsama"))


def extract_layer2_boundaries(markdown: str) -> list[str]:
    """Retain explicit rejection/counterpressure sections only."""
    sections: list[str] = []
    active: list[str] | None = None
    for line in markdown.splitlines():
        title = heading_title(line)
        if title is not None:
            if active is not None:
                rendered = "\n".join(active).strip()
                if rendered:
                    sections.append(rendered)
                active = None
            if is_scope_heading(title):
                break
            if is_boundary_heading(title):
                active = [line]
                continue
        if active is not None:
            active.append(line)
    if active is not None:
        rendered = "\n".join(active).strip()
        if rendered:
            sections.append(rendered)
    return sections


def network_activation_cards(markdown: str) -> list[dict[str, Any]]:
    """Project reviewed subchannels without their prewritten syntheses."""
    cards: list[dict[str, Any]] = []
    parent_number: int | None = None
    current: dict[str, Any] | None = None

    def finish() -> None:
        nonlocal current
        if current is None:
            return
        missing = [
            key for key in ("ayahAnchors", "activeMotifs") if not current.get(key)
        ]
        if missing:
            raise SystemExit(
                f"error: reviewed activation card {current['activationRef']} is "
                f"missing {', '.join(missing)}"
            )
        current["ayahRefs"] = list(
            dict.fromkeys(
                re.findall(
                    r"\b[1-9][0-9]{0,2}:[1-9][0-9]*\b",
                    current["ayahAnchors"],
                )
            )
        )
        if not current["ayahRefs"]:
            raise SystemExit(
                f"error: reviewed activation card {current['activationRef']} "
                "has no parseable ayah reference"
            )
        current["signalRefs"] = re.findall(r"`([^`]+)`", current["activeMotifs"])
        cards.append(current)
        current = None

    for line in markdown.splitlines():
        parent_match = re.match(r"^###\s+([0-9]+)\.\s+", line)
        if parent_match:
            finish()
            parent_number = int(parent_match.group(1))
            continue
        standalone_match = re.match(r"^###\s+S([0-9]+)\.\s+", line)
        if standalone_match:
            finish()
            standalone = int(standalone_match.group(1))
            parent_number = None
            current = {
                "activationRef": f"activation:network-s{standalone:02d}",
                "ayahAnchors": None,
                "activeMotifs": None,
                "sourceRefs": [f"network-review#standalone-{standalone}"],
            }
            continue
        subchannel_match = re.match(r"^####\s+Subchannel\s+([A-Z]+)\.\s+", line)
        if subchannel_match:
            finish()
            if parent_number is None:
                raise SystemExit("error: reviewed subchannel has no parent")
            letter = subchannel_match.group(1).lower()
            current = {
                "activationRef": f"activation:network-p{parent_number:02d}-{letter}",
                "ayahAnchors": None,
                "activeMotifs": None,
                "sourceRefs": [
                    f"network-review#parent-{parent_number}/subchannel-{letter}"
                ],
            }
            continue
        if current is None:
            continue
        fields = {
            "- Active motifs:": "activeMotifs",
            "- Ayah anchors:": "ayahAnchors",
        }
        for prefix, key in fields.items():
            if line.startswith(prefix):
                current[key] = line[len(prefix) :].strip()
                break
    finish()
    return cards


def markdown_h2_sections(markdown: str) -> dict[str, tuple[str, str]]:
    sections: dict[str, tuple[str, str]] = {}
    current_title: str | None = None
    current_lines: list[str] = []
    for line in markdown.splitlines():
        match = re.match(r"^##\s+(.+?)\s*$", line)
        if match:
            if current_title is not None:
                sections[folded(current_title)] = (
                    current_title,
                    "\n".join(current_lines).strip(),
                )
            current_title = match.group(1)
            current_lines = []
        elif current_title is not None:
            current_lines.append(line)
    if current_title is not None:
        sections[folded(current_title)] = (
            current_title,
            "\n".join(current_lines).strip(),
        )
    return sections


def find_v11_dir(
    quran_data: Path,
    latent_activation: Path,
    surah: int,
) -> tuple[Path | None, bool]:
    suffix = f"s{surah:03d}"
    candidates = (
        quran_data / "data" / "analysis" / "ayah-activation" / "v11" / "run" / suffix,
        quran_data / "data" / "analysis" / "ayah-activation" / "v11" / suffix,
        quran_data / "data" / "analysis" / "v11" / "run" / suffix,
        quran_data / "v11" / "run" / suffix,
    )
    for candidate in candidates:
        if candidate.is_dir():
            return candidate, False
    fallback = latent_activation / "v11" / "run" / suffix
    if fallback.is_dir():
        return fallback, True
    return None, False


def coverage_group(
    *,
    source_ids: list[str],
    missing: list[str],
    required: bool,
    notes: list[str],
    fallback_used: bool | None = None,
    source_root: str | None = None,
) -> dict[str, Any]:
    status = "absent" if not source_ids else "partial" if missing else "complete"
    value: dict[str, Any] = {
        "status": status,
        "required": required,
        "sourceIds": source_ids,
        "missing": missing,
        "notes": notes,
    }
    if fallback_used is not None:
        value["fallbackUsed"] = fallback_used
    if source_root is not None:
        value["sourceRoot"] = source_root
    return value


def build_packet(
    *,
    surah: int,
    language: str,
    layer2_dir: Path,
    layer2_label: str | None,
    quran_data: Path,
    latent_activation: Path,
    primary_floor_path: Path | None = None,
    layer2_contract_path: Path | None = None,
) -> dict[str, Any]:
    language = normalize_language(language)
    registry: list[dict[str, Any]] = []
    warnings: list[str] = []

    quran_path = quran_data / "data" / "text" / "quran-uthmani.tsv"
    if not quran_path.exists():
        raise SystemExit(f"error: required Quran text is missing: {quran_path}")
    quran_rows = parse_quran_text(quran_path, surah)
    numbered_refs = {
        row["ayahRef"]
        for row in quran_rows
        if int(row["ayahRef"].split(":")[1]) != 0
    }
    quran_source_id = register_source(
        registry,
        source_id="quran-text",
        kind="quran-text",
        role="primary-ground",
        path=quran_path,
        projection=f"Rows scoped to surah {surah}.",
        quran_data=quran_data,
        latent_activation=latent_activation,
    )

    floor_path = primary_floor_path or (
        REPO_ROOT / "_translation" / "v1" / "output" / language / f"s{surah:03d}.json"
    )
    if not floor_path.exists():
        raise SystemExit(
            f"error: typed primary floor is required but missing: {floor_path}. "
            "Run Layer 1 or pass --primary-floor; Layer-2 prose is not a substitute."
        )
    floor_lines = parse_primary_floor(
        floor_path,
        surah=surah,
        language=language,
        required_refs=numbered_refs,
    )
    floor_source_id = register_source(
        registry,
        source_id="primary-floor",
        kind="primary-floor",
        role="primary-ground",
        path=floor_path,
        projection="Canonical typed Layer-1 translation lines for numbered ayahs.",
        quran_data=quran_data,
        latent_activation=latent_activation,
    )

    contract_path = layer2_contract_path or (
        REPO_ROOT / "_ayah_commentary" / "v2" / "PROMPT.md"
    )
    if not contract_path.exists():
        raise SystemExit(f"error: Layer-2 handoff contract is missing: {contract_path}")
    contract_source_id = register_source(
        registry,
        source_id="layer2-contract",
        kind="layer2-contract",
        role="handoff-contract",
        path=contract_path,
        projection="Contract used to interpret the four Layer-2 v2 artifacts.",
        quran_data=quran_data,
        latent_activation=latent_activation,
    )

    if not layer2_dir.is_dir():
        raise SystemExit(f"error: Layer-2 directory does not exist: {layer2_dir}")
    primary_ayahs: list[dict[str, Any]] = []
    handoff_ayahs: list[dict[str, Any]] = []
    layer2_source_ids: list[str] = [contract_source_id]
    local_resonance_count = 0
    boundary_count = 0
    for row in quran_rows:
        ayah = int(row["ayahRef"].split(":")[1])
        floor = None
        if ayah != 0:
            floor = {
                "text": floor_lines[row["ayahRef"]],
                "sourceRef": f"{floor_source_id}#{row['ayahRef']}",
            }
        primary_ayahs.append(
            {
                "ayahRef": row["ayahRef"],
                "unitType": "basmala" if ayah == 0 else "ayah",
                "arabic": row["arabic"],
                "floor": floor,
            }
        )
        if ayah == 0:
            continue

        selected_label, artifacts = select_layer2_artifact_set(
            layer2_dir, surah, ayah, layer2_label
        )
        artifact_refs: dict[str, str] = {}
        for kind in LAYER2_KINDS:
            source_id = f"layer2-{kind}-{surah}-{ayah}"
            artifact_refs[kind] = source_id
            layer2_source_ids.append(
                register_source(
                    registry,
                    source_id=source_id,
                    kind=f"layer2-{kind}",
                    role=LAYER2_ROLES[kind],
                    path=artifacts[kind],
                    projection=(
                        "Complete findings rows."
                        if kind == "index"
                        else "Explicit boundary sections only."
                        if kind == "evidence"
                        else "Hashed for lineage; content withheld from semantic passes."
                    ),
                    quran_data=quran_data,
                    latent_activation=latent_activation,
                )
            )
        findings, local_resonances = parse_index(
            artifacts["index"],
            surah=surah,
            ayah=ayah,
            source_id=artifact_refs["index"],
        )
        local_resonance_count += len(local_resonances)
        boundaries = []
        for section_index, section in enumerate(
            extract_layer2_boundaries(
                artifacts["evidence"].read_text(encoding="utf-8")
            ),
            start=1,
        ):
            boundary_count += 1
            boundaries.append(
                {
                    "boundaryRef": f"boundary:{surah}:{ayah}:{section_index:02d}",
                    "ayahRefs": [row["ayahRef"]],
                    "text": section,
                    "sourceRefs": [
                        f"{artifact_refs['evidence']}#boundary-{section_index}"
                    ],
                }
            )
        handoff_ayahs.append(
            {
                "ayahRef": row["ayahRef"],
                "artifactSetLabel": selected_label,
                "artifactRefs": artifact_refs,
                "findings": findings,
                "localResonances": local_resonances,
                "boundaries": boundaries,
            }
        )

    source_set_sources = [
        {
            "sourceId": source["sourceId"],
            "path": source["path"],
            "sha256": source["sha256"],
            "bytes": source["bytes"],
        }
        for source in registry
    ]
    source_set_hash = content_hash(
        {
            "contract": "layer2-handoff-v1",
            "surah": surah,
            "language": language,
            "sources": source_set_sources,
        }
    )
    source_set_id = f"s{surah:03d}-{language}-l2-{source_set_hash[:16]}"

    activation_cards: list[dict[str, Any]] = []
    network_ids: list[str] = []
    network_missing: list[str] = []
    network_dir = (
        quran_data
        / "data"
        / "analysis"
        / "channels"
        / "network-v3"
        / f"s{surah:03d}"
    )
    network_review = network_dir / "review" / "reader_a_pilot.md"
    if network_review.exists():
        network_source_id = register_source(
            registry,
            source_id="network-review",
            kind="network-review",
            role="activation-source",
            path=network_review,
            projection="Activation cards only; titles and syntheses excluded.",
            quran_data=quran_data,
            latent_activation=latent_activation,
        )
        network_ids.append(network_source_id)
        activation_cards = network_activation_cards(
            network_review.read_text(encoding="utf-8")
        )
        if not activation_cards:
            raise SystemExit(
                f"error: reviewed Network V3 file produced no activation cards: "
                f"{network_review}"
            )
    else:
        network_missing.append("review/reader_a_pilot.md")
        warn(
            f"reviewed network-v3 synthesis is absent for s{surah:03d}; continuing",
            warnings,
        )

    v11_ids: list[str] = []
    v11_missing: list[str] = []
    secondary_material: list[dict[str, Any]] = []
    v11_dir, v11_fallback = find_v11_dir(quran_data, latent_activation, surah)
    if v11_dir is None:
        v11_missing.append(f"v11/run/s{surah:03d}")
        v11_root = None
        warn(f"V11 is absent for s{surah:03d}; continuing", warnings)
    else:
        v11_root = portable_path(
            v11_dir,
            quran_data=quran_data,
            latent_activation=latent_activation,
        )
        if v11_fallback:
            warn(
                f"V11 was not found in quran-data for s{surah:03d}; using "
                "latent_activation fallback",
                warnings,
            )
        final_report = v11_dir / "09-final-report.md"
        if final_report.exists():
            parsed_sections = markdown_h2_sections(
                final_report.read_text(encoding="utf-8")
            )
            selected_sections: list[tuple[str, str, str]] = []
            for title_key, section_id in V11_SECTION_IDS.items():
                section = parsed_sections.get(title_key)
                if section is None:
                    v11_missing.append(f"09-final-report.md#{title_key}")
                    continue
                heading, content = section
                selected_sections.append((section_id, heading, content))
            if selected_sections:
                source_id = register_source(
                    registry,
                    source_id="v11-final-report",
                    kind="v11-final-report",
                    role="secondary-material",
                    path=final_report,
                    projection=(
                        "Selected surprising discoveries and open boundaries; "
                        "prior integrated mechanism excluded."
                    ),
                    quran_data=quran_data,
                    latent_activation=latent_activation,
                )
                v11_ids.append(source_id)
                for section_id, heading, content in selected_sections:
                    secondary_material.append(
                        {
                            "secondaryRef": f"secondary:v11:{section_id}",
                            "heading": heading,
                            "sourceRefs": [f"{source_id}#{section_id}"],
                            "text": content,
                        }
                    )
        else:
            v11_missing.append("09-final-report.md")
        if v11_missing:
            warn(
                f"V11 secondary material is partial for s{surah:03d}; continuing "
                "without " + ", ".join(v11_missing),
                warnings,
            )

    packet_hash = content_hash(
        {
            "contract": "layer3-source-packet-v3",
            "surah": surah,
            "language": language,
            "sourceSetHash": source_set_hash,
            "sources": [
                {
                    "sourceId": source["sourceId"],
                    "sha256": source["sha256"],
                    "projection": source["projection"],
                }
                for source in registry
            ],
        }
    )
    run_id = f"s{surah:03d}-{language}-l3v3-{packet_hash[:16]}"
    return {
        "schemaVersion": "layer3-source-packet-v3",
        "packetId": run_id,
        "runId": run_id,
        "packetHash": packet_hash,
        "sourceSetId": source_set_id,
        "sourceSetHash": source_set_hash,
        "surah": surah,
        "language": language,
        "sourceRegistry": registry,
        "primaryGround": {
            "quranSourceRef": quran_source_id,
            "floorSourceRef": floor_source_id,
            "ayahs": primary_ayahs,
        },
        "layer2Handoff": {
            "schemaVersion": "layer2-handoff-v1",
            "sourceSetId": source_set_id,
            "sourceSetHash": source_set_hash,
            "contractSourceRef": contract_source_id,
            "ayahs": handoff_ayahs,
        },
        "evidenceField": {
            "activationCards": activation_cards,
            "secondaryMaterial": secondary_material,
        },
        "coverage": {
            "quranText": coverage_group(
                source_ids=[quran_source_id],
                missing=[],
                required=True,
                notes=[
                    f"{len(numbered_refs)} numbered ayahs; basmala retained when present."
                ],
            ),
            "primaryFloor": coverage_group(
                source_ids=[floor_source_id],
                missing=[],
                required=True,
                notes=["Typed Layer-1 floor is complete for every numbered ayah."],
            ),
            "layer2": coverage_group(
                source_ids=layer2_source_ids,
                missing=[],
                required=True,
                notes=[
                    "All four Layer-2 artifacts are hashed for every numbered ayah.",
                    "The complete findings index is projected into typed records.",
                    f"{local_resonance_count} local resonance rows retained.",
                    f"{boundary_count} explicit boundary sections retained.",
                    "Prose and friction content are withheld from semantic passes.",
                ],
            ),
            "networkV3": coverage_group(
                source_ids=network_ids,
                missing=network_missing,
                required=False,
                notes=[
                    "Only activation cards are retained.",
                    "Raw candidates, titles, and prewritten syntheses are excluded.",
                ],
                source_root=portable_path(network_dir, quran_data=quran_data),
            ),
            "v11": coverage_group(
                source_ids=v11_ids,
                missing=v11_missing,
                required=False,
                notes=[
                    "Only surprising discoveries and open boundaries are retained.",
                    "Prior synthesis, rankings, and inventories are excluded.",
                ],
                fallback_used=v11_fallback,
                source_root=v11_root,
            ),
        },
        "warnings": warnings,
    }


def default_run_dir(packet: dict[str, Any]) -> Path:
    return (
        WORKFLOW_ROOT
        / "runs"
        / "v3"
        / f"s{packet['surah']:03d}"
        / packet["language"]
        / packet["runId"]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--language", default="tr")
    parser.add_argument("--layer2-dir", type=Path)
    parser.add_argument("--layer2-label")
    parser.add_argument("--primary-floor", type=Path)
    parser.add_argument("--quran-data", type=Path)
    parser.add_argument("--latent-activation", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    quran_data = (args.quran_data or REPO_ROOT.parent / "quran-data").resolve()
    latent_activation = (
        args.latent_activation or REPO_ROOT.parent / "latent_activation"
    ).resolve()
    layer2_dir = args.layer2_dir or (
        REPO_ROOT / "_commentary" / "outputs" / f"s{args.surah:03d}-default"
    )
    if not layer2_dir.is_absolute():
        layer2_dir = REPO_ROOT / layer2_dir
    primary_floor = args.primary_floor
    if primary_floor is not None and not primary_floor.is_absolute():
        primary_floor = REPO_ROOT / primary_floor

    packet = build_packet(
        surah=args.surah,
        language=args.language,
        layer2_dir=layer2_dir,
        layer2_label=args.layer2_label,
        quran_data=quran_data,
        latent_activation=latent_activation,
        primary_floor_path=primary_floor,
    )
    output = args.out or default_run_dir(packet) / f"{args.surah}.source-packet.json"
    if not output.is_absolute():
        output = REPO_ROOT / output

    from validate import validate_packet

    errors = validate_packet(packet, verify_sources=True)
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1
    wrote = immutable_write_json(output, packet, compact=True)
    verb = "wrote" if wrote else "unchanged"
    print(
        f"{verb} {output} ({len(packet['sourceRegistry'])} sources, "
        f"{len(packet['warnings'])} warnings)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
