#!/usr/bin/env python3
"""Build a normalized hermetic packet for Layer 3 surah discovery."""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any

from common import REPO_ROOT, WORKFLOW_ROOT, portable_path, write_json


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
    registry: list[dict[str, str]],
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
    return rows


def select_layer2_file(
    directory: Path,
    surah: int,
    ayah: int,
    kind: str,
    label: str | None,
) -> Path:
    if label:
        candidate = directory / f"{surah}_{ayah}.{kind}.{label}.md"
        if candidate.exists():
            return candidate
        raise SystemExit(f"error: missing required Layer-2 file: {candidate}")
    matches = sorted(directory.glob(f"{surah}_{ayah}.{kind}*.md"))
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise SystemExit(
            f"error: missing Layer-2 {kind} for {surah}:{ayah} in {directory}"
        )
    rendered = "\n".join(f"  {path}" for path in matches)
    raise SystemExit(
        f"error: ambiguous Layer-2 {kind} for {surah}:{ayah}; pass "
        f"--layer2-label:\n{rendered}"
    )


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
    normalized = folded(title)
    return normalized.startswith(("kapsam", "kapsama"))


def extract_layer2_boundaries(markdown: str) -> list[str]:
    """Keep explicit rejection/counterpressure sections, not claim-map repeats."""
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
    quran_candidates = (
        quran_data / "data" / "analysis" / "ayah-activation" / "v11" / "run" / suffix,
        quran_data / "data" / "analysis" / "ayah-activation" / "v11" / suffix,
        quran_data / "data" / "analysis" / "v11" / "run" / suffix,
        quran_data / "v11" / "run" / suffix,
    )
    for candidate in quran_candidates:
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
    if not source_ids:
        status = "absent"
    elif missing:
        status = "partial"
    else:
        status = "complete"
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
) -> dict[str, Any]:
    registry: list[dict[str, str]] = []
    warnings: list[str] = []

    quran_path = quran_data / "data" / "text" / "quran-uthmani.tsv"
    if not quran_path.exists():
        raise SystemExit(f"error: required Quran text is missing: {quran_path}")
    quran_rows = parse_quran_text(quran_path, surah)
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

    if not layer2_dir.is_dir():
        raise SystemExit(f"error: Layer-2 directory does not exist: {layer2_dir}")
    layer2_ids: list[str] = []
    primary_ayahs: list[dict[str, Any]] = []
    local_boundaries: list[dict[str, Any]] = []
    boundary_count = 0
    for row in quran_rows:
        ayah = int(row["ayahRef"].split(":")[1])
        item: dict[str, Any] = {
            "ayahRef": row["ayahRef"],
            "unitType": "basmala" if ayah == 0 else "ayah",
            "arabic": row["arabic"],
            "reading": None,
        }
        if ayah != 0:
            prose_path = select_layer2_file(
                layer2_dir,
                surah,
                ayah,
                "prose",
                layer2_label,
            )
            prose_source_id = f"layer2-prose-{surah}-{ayah}"
            layer2_ids.append(
                register_source(
                    registry,
                    source_id=prose_source_id,
                    kind="layer2-prose",
                    role="local-reading",
                    path=prose_path,
                    projection="Complete accepted Layer-2 reader prose.",
                    quran_data=quran_data,
                    latent_activation=latent_activation,
                )
            )
            item["reading"] = {
                "sourceRef": prose_source_id,
                "text": prose_path.read_text(encoding="utf-8"),
            }

            evidence_path = select_layer2_file(
                layer2_dir,
                surah,
                ayah,
                "evidence",
                layer2_label,
            )
            boundary_sections = extract_layer2_boundaries(
                evidence_path.read_text(encoding="utf-8")
            )
            if boundary_sections:
                evidence_source_id = f"layer2-evidence-{surah}-{ayah}"
                layer2_ids.append(
                    register_source(
                        registry,
                        source_id=evidence_source_id,
                        kind="layer2-evidence",
                        role="claim-boundary",
                        path=evidence_path,
                        projection=(
                            "Explicit rejection, counterpressure, and boundary "
                            "sections only."
                        ),
                        quran_data=quran_data,
                        latent_activation=latent_activation,
                    )
                )
                for section_index, section in enumerate(
                    boundary_sections,
                    start=1,
                ):
                    boundary_count += 1
                    local_boundaries.append(
                        {
                            "boundaryId": (
                                f"l2-{surah}-{ayah}-boundary-{section_index}"
                            ),
                            "ayahRefs": [row["ayahRef"]],
                            "sourceRefs": [
                                f"{evidence_source_id}#boundary-{section_index}"
                            ],
                            "text": section,
                        }
                    )
        primary_ayahs.append(item)

    network_ids: list[str] = []
    network_missing: list[str] = []
    reviewed_channels: list[dict[str, Any]] = []
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
            role="reviewed-evidence",
            path=network_review,
            projection=(
                "Complete first-pass reviewed parent and standalone channel "
                "synthesis; upstream candidates and family files excluded."
            ),
            quran_data=quran_data,
            latent_activation=latent_activation,
        )
        network_ids.append(network_source_id)
        reviewed_channels.append(
            {
                "synthesisId": "network-v3-reviewed",
                "sourceRefs": [network_source_id],
                "text": network_review.read_text(encoding="utf-8"),
            }
        )
    else:
        network_missing.append("review/reader_a_pilot.md")
        warn(
            f"reviewed network-v3 synthesis is absent for s{surah:03d}; "
            "continuing",
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
                            "sectionId": section_id,
                            "heading": heading,
                            "sourceRefs": [f"{source_id}#{section_id}"],
                            "text": content,
                        }
                    )
        else:
            v11_missing.append("09-final-report.md")
        if v11_missing:
            warn(
                f"V11 secondary material is partial for s{surah:03d}; "
                "continuing without "
                + ", ".join(v11_missing),
                warnings,
            )

    return {
        "schemaVersion": "layer3-source-packet-v2",
        "packetId": f"s{surah:03d}-{language}-layer3-v2",
        "surah": surah,
        "language": language,
        "sourceRegistry": registry,
        "primaryGround": {
            "sourceRefs": [quran_source_id],
            "ayahs": primary_ayahs,
        },
        "evidenceField": {
            "localBoundaries": local_boundaries,
            "reviewedChannels": reviewed_channels,
            "secondaryMaterial": secondary_material,
        },
        "coverage": {
            "quranText": coverage_group(
                source_ids=[quran_source_id],
                missing=[],
                required=True,
                notes=[
                    f"{len(quran_rows) - 1} numbered ayahs; basmala retained "
                    "when present."
                ],
            ),
            "layer2": coverage_group(
                source_ids=layer2_ids,
                missing=[],
                required=True,
                notes=[
                    "Accepted prose is retained in full.",
                    (
                        f"{boundary_count} explicit rejection/counterpressure "
                        "sections retained from evidence files."
                    ),
                    "Routine evidence maps, scope notes, indexes, and production "
                    "friction are excluded.",
                    "V12 is not repeated because it is upstream ancestry of the "
                    "completed Layer-2 outputs.",
                    f"Layer-2 label: {layer2_label or 'unique match'}",
                ],
            ),
            "networkV3": coverage_group(
                source_ids=network_ids,
                missing=network_missing,
                required=False,
                notes=[
                    "Only the first-pass reviewed synthesis is retained.",
                    "Raw candidates and machine families are excluded by lineage.",
                ],
                source_root=portable_path(network_dir, quran_data=quran_data),
            ),
            "v11": coverage_group(
                source_ids=v11_ids,
                missing=v11_missing,
                required=False,
                notes=[
                    "Only surprising discoveries and their open boundaries are "
                    "retained.",
                    "Prior integrated mechanisms, branch inventories, rankings, "
                    "intermediate mechanisms, and prior prose are excluded.",
                ],
                fallback_used=v11_fallback,
                source_root=v11_root,
            ),
        },
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--language", default="tr")
    parser.add_argument("--layer2-dir", type=Path)
    parser.add_argument("--layer2-label")
    parser.add_argument("--quran-data", type=Path)
    parser.add_argument("--latent-activation", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    quran_data = (args.quran_data or REPO_ROOT.parent / "quran-data").resolve()
    latent_activation = (
        args.latent_activation or REPO_ROOT.parent / "latent_activation"
    ).resolve()
    layer2_dir = (
        args.layer2_dir
        or REPO_ROOT / "_commentary" / "outputs" / f"s{args.surah:03d}-default"
    )
    if not layer2_dir.is_absolute():
        layer2_dir = REPO_ROOT / layer2_dir
    output = (
        args.out
        or WORKFLOW_ROOT
        / "packets"
        / f"s{args.surah:03d}"
        / f"{args.surah}.source-packet.json"
    )
    if not output.is_absolute():
        output = REPO_ROOT / output

    packet = build_packet(
        surah=args.surah,
        language=args.language,
        layer2_dir=layer2_dir,
        layer2_label=args.layer2_label,
        quran_data=quran_data,
        latent_activation=latent_activation,
    )
    write_json(output, packet, compact=True)
    print(
        f"wrote {output} ({len(packet['sourceRegistry'])} sources, "
        f"{len(packet['warnings'])} warnings)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
