#!/usr/bin/env python3
"""Build compact, exhaustive input for primary-branch selection.

Stage 0 sees every candidate Furuq root and every branch under each root, but
only the Arabic branch definition needed to distinguish them. The independently
authored Turkish ordinary baseline is included as non-authoritative assistance;
the anchor prompt defines its limited role.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from build_bundle import (
    dictionary_root_packet,
    frozen_occurrence_overlays,
    morphology,
    read_json,
    root_resolution_for_row,
    root_resolutions,
    usable_targets,
    word_ref,
    write_compact_json,
)

V1_DIR = Path(__file__).resolve().parents[1]
WORKSPACE = V1_DIR.parents[2]

BUILDER_VERSION = "anchor-input-v2"


class RequiredSourceMissing(RuntimeError):
    """A source that must exist for every canonical surah is absent."""


def v12_dir(surah: int) -> Path:
    path = (
        WORKSPACE
        / "latent_activation"
        / "_status"
        / "v12_cross_run"
        / f"s{surah:03d}"
    )
    if not path.is_dir():
        raise RequiredSourceMissing(f"no v12 cross-run directory: {path}")
    return path


def publication_path(surah: int) -> Path:
    path = (
        WORKSPACE
        / "quran-data"
        / "data"
        / "analysis"
        / "ayah-activation"
        / "v12-cross-run"
        / "tr"
        / f"{surah}_ayah_findings_publication.json"
    )
    if not path.exists():
        raise RequiredSourceMissing(f"no Turkish v12 publication: {path}")
    return path


def root_packet(root_id: str) -> dict:
    try:
        return dictionary_root_packet(root_id)
    except FileNotFoundError as exc:
        raise RequiredSourceMissing(str(exc)) from exc


def ordinary_turkish_baselines(
    surah: int,
    roster: dict,
) -> tuple[dict[str, dict], dict]:
    path = publication_path(surah)
    publication = read_json(path)
    expected = {
        "protocol": "v12-cross-run-publication-v3",
        "language": "tr",
        "surah": surah,
    }
    for key, value in expected.items():
        if publication.get(key) != value:
            raise RequiredSourceMissing(
                f"{path}: expected {key}={value!r}, found {publication.get(key)!r}"
            )

    roster_expected = {
        "protocol": "v12-cross-run-ayah-roster-v3",
        "language": "tr",
        "surah": surah,
    }
    for key, value in roster_expected.items():
        if roster.get(key) != value:
            raise RequiredSourceMissing(
                f"ayah roster: expected {key}={value!r}, found {roster.get(key)!r}"
            )
    baseline_sha256 = roster.get("baseline_sha256")
    if (
        not isinstance(baseline_sha256, str)
        or len(baseline_sha256) != 64
        or any(char not in "0123456789abcdef" for char in baseline_sha256)
    ):
        raise RequiredSourceMissing(
            f"ayah roster has invalid baseline_sha256 {baseline_sha256!r}"
        )

    columns = {name: index for index, name in enumerate(roster.get("columns", []))}
    required_columns = {"baseline_source_ref", "baseline"}
    if not required_columns <= set(columns):
        raise RequiredSourceMissing(
            f"ayah roster lacks baseline columns {sorted(required_columns - set(columns))}"
        )
    frozen_baselines: dict[str, dict] = {}
    for row_index, row in enumerate(roster.get("rows", [])):
        try:
            source_ref = row[columns["baseline_source_ref"]]
            baseline = row[columns["baseline"]]
        except (IndexError, TypeError) as exc:
            raise RequiredSourceMissing(
                f"ayah roster row {row_index} is malformed"
            ) from exc
        if (
            not isinstance(source_ref, str)
            or not isinstance(baseline, dict)
            or baseline.get("source_ref") != source_ref
            or source_ref in frozen_baselines
        ):
            raise RequiredSourceMissing(
                f"ayah roster row {row_index} has invalid baseline {source_ref!r}"
            )
        frozen_baselines[source_ref] = baseline

    baselines: dict[str, dict] = {}
    for ayah in publication.get("ayat", []):
        baseline = ayah.get("baseline")
        if not isinstance(baseline, dict):
            raise RequiredSourceMissing(
                f"{path}: {ayah.get('ayah_ref')!r} has no baseline object"
            )
        source_ref = baseline.get("source_ref")
        if not source_ref or source_ref in baselines:
            raise RequiredSourceMissing(
                f"{path}: invalid or duplicate baseline source_ref {source_ref!r}"
            )
        frozen = frozen_baselines.get(source_ref)
        if frozen is None:
            raise RequiredSourceMissing(
                f"{path}: publication baseline {source_ref} is absent from frozen roster"
            )
        if baseline != frozen:
            raise RequiredSourceMissing(
                f"{path}: publication baseline {source_ref} differs from frozen roster"
            )

        target_tokens = []
        for index, token in enumerate(baseline.get("target_tokens", [])):
            if (
                not isinstance(token, list)
                or len(token) != 2
                or not isinstance(token[0], str)
                or not token[0]
                or not isinstance(token[1], list)
                or not token[1]
            ):
                raise RequiredSourceMissing(
                    f"{path}: {source_ref} target token {index} is malformed"
                )
            target_tokens.append(
                {
                    "text": token[0],
                    "qacWordRefs": token[1],
                }
            )

        baselines[source_ref] = {
            "text": baseline["text"],
            "targetTokens": target_tokens,
        }

    missing_publication_baselines = sorted(set(frozen_baselines) - set(baselines))
    if missing_publication_baselines:
        raise RequiredSourceMissing(
            f"{path}: publication omits frozen baselines "
            f"{missing_publication_baselines}"
        )

    source = {
        "protocol": roster["protocol"],
        "language": roster["language"],
        "hashScope": "frozen-baseline-bundle",
        "baselineBundleSha256": baseline_sha256,
    }
    return baselines, source


def validate_exact_baseline_alignment(
    ayah_ref: str,
    baseline: dict,
    qac_word_refs: set[str],
) -> None:
    aligned_word_refs = {
        ref
        for token in baseline["targetTokens"]
        for ref in token["qacWordRefs"]
    }
    missing = sorted(qac_word_refs - aligned_word_refs)
    foreign = sorted(aligned_word_refs - qac_word_refs)
    if missing or foreign:
        raise RequiredSourceMissing(
            f"Turkish baseline {ayah_ref} QAC word alignment is not exact: "
            f"missing={missing}, foreign={foreign}"
        )


def branch_candidates(packet: dict, root_id: str) -> list[dict]:
    candidates = []
    seen: set[str] = set()
    for branch in packet.get("branches", []):
        branch_id = branch.get("branch_id")
        what_is_ar = branch.get("what_is_ar")
        if not branch_id or branch_id in seen:
            raise RequiredSourceMissing(
                f"dictionary packet for {root_id} has invalid branch id {branch_id!r}"
            )
        if not what_is_ar:
            raise RequiredSourceMissing(
                f"dictionary packet for {root_id}/{branch_id} has no what_is_ar"
            )
        seen.add(branch_id)
        candidates.append(
            {
                "branchId": branch_id,
                "what_is_ar": what_is_ar,
            }
        )
    if not candidates:
        raise RequiredSourceMissing(f"dictionary packet for {root_id} has no branches")
    return candidates


def compact_root_resolution(resolution: dict) -> dict:
    targets = []
    for target in usable_targets(resolution):
        root_id = target["rootId"]
        root_norm_ar = (
            target.get("furuqRootNorm")
            or target.get("frozenRootNorm")
            or target.get("furuqSourceRootNorm")
            or target.get("componentRootNorm")
        )
        if not root_norm_ar:
            packet = root_packet(root_id)
            root_record = next(
                (
                    item
                    for item in packet.get("v4_roots", [])
                    if item.get("root_id") == root_id
                ),
                None,
            )
            if root_record:
                root_norm_ar = (
                    root_record.get("root_norm")
                    or root_record.get("source_root_norm")
                )
            elif packet.get("root_envelope_id") == root_id:
                root_norm_ar = packet.get("root_norm")
        if not root_norm_ar:
            raise RequiredSourceMissing(
                f"root resolution target {root_id} has no Arabic root norm"
            )
        targets.append(
            {
                "rootId": root_id,
                "rootNormAr": root_norm_ar,
            }
        )
    if not targets:
        raise RequiredSourceMissing(
            "root resolution has no usable targets: "
            f"{resolution.get('qacRootJoinKey')!r}"
        )
    return {
        "mappingStatus": resolution.get("mappingStatus"),
        "targets": targets,
    }


def parse_ayah_range(value: str | None) -> tuple[int, int] | None:
    if not value:
        return None
    if "-" in value:
        first, last = value.split("-", 1)
        return int(first), int(last)
    return int(value), int(value)


def build_anchor_input(surah: int, ayahs: tuple[int, int] | None = None) -> dict:
    directory = v12_dir(surah)
    roster = read_json(directory / "ayah_roster.v3.json")
    resolutions, quran_data_release_id = root_resolutions(surah, directory)
    baselines, baseline_source = ordinary_turkish_baselines(surah, roster)

    morphemes_by_ayah: dict[str, list[dict[str, str]]] = {}
    morpheme_rows: list[dict[str, str]] = []
    with (directory / "linguistic" / "morphemes.tsv").open(
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

    packets: dict[str, dict] = {}
    output_ayat = []
    rooted_count = 0
    for _, arabic_text, ayah_ref, _ in roster["rows"]:
        if ayahs is not None:
            ayah_surah, ayah_number = (int(part) for part in ayah_ref.split(":"))
            in_chunk = (
                ayahs[0] <= ayah_number <= ayahs[1]
                if ayah_surah == surah
                else ayahs[0] <= 1
            )
            if not in_chunk:
                continue

        baseline = baselines.get(ayah_ref)
        if baseline is None:
            raise RequiredSourceMissing(
                f"Turkish publication has no ordinary baseline for {ayah_ref}"
            )
        qac_word_refs = {
            word_ref(row["qac_ref"])
            for row in morphemes_by_ayah.get(ayah_ref, [])
        }
        validate_exact_baseline_alignment(ayah_ref, baseline, qac_word_refs)

        stems = []
        for row in morphemes_by_ayah.get(ayah_ref, []):
            if not row["root_join_key"]:
                continue
            rooted_count += 1
            resolution = root_resolution_for_row(
                resolutions,
                occurrence_overlays,
                row,
            )
            compact_resolution = compact_root_resolution(resolution)
            for target in compact_resolution["targets"]:
                root_id = target["rootId"]
                if root_id not in packets:
                    packets[root_id] = root_packet(root_id)

            stem = {
                "qacMorphemeRef": row["qac_ref"],
                "qacWordRef": word_ref(row["qac_ref"]),
                "arabic": row["surface_ar"],
                "morphology": morphology(row),
                "rootAr": row["root"],
                "rootResolution": compact_resolution,
            }
            if row["lemma_ar"]:
                stem["lemma"] = row["lemma_ar"]
            stems.append(stem)

        output_ayat.append(
            {
                "ayahRef": ayah_ref,
                "arabicText": arabic_text,
                "ordinaryTurkishBaseline": baseline,
                "rootedStems": stems,
            }
        )

    if not rooted_count:
        scope = f" ayahs {ayahs[0]}-{ayahs[1]}" if ayahs else ""
        raise RequiredSourceMissing(
            f"surah {surah}{scope}: no rooted stems; refusing empty anchor input"
        )

    roots = {
        root_id: {
            "rootId": root_id,
            "branches": branch_candidates(packet, root_id),
        }
        for root_id, packet in sorted(packets.items())
    }

    return {
        "schemaVersion": "anchor-input-v2",
        "builderVersion": BUILDER_VERSION,
        "quranDataReleaseId": quran_data_release_id,
        "surah": surah,
        "ayahRange": list(ayahs) if ayahs else None,
        "assistance": {
            "ordinaryTurkishBaseline": baseline_source,
        },
        "coverage": {
            "rootedStems": rooted_count,
            "roots": len(roots),
            "branches": sum(len(root["branches"]) for root in roots.values()),
            "baselineAyat": len(output_ayat),
        },
        "roots": roots,
        "ayat": output_ayat,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument(
        "--ayahs",
        help="ayah chunk, e.g. '1' or '1-20'. Prefatory basmalah belongs "
        "to the first chunk.",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    ayahs = parse_ayah_range(args.ayahs)
    suffix = f".{ayahs[0]}-{ayahs[1]}" if ayahs else ""
    output = args.output or (
        V1_DIR / "anchors" / "input" / f"s{args.surah:03d}{suffix}.anchor-input.json"
    )
    bundle = build_anchor_input(args.surah, ayahs)
    write_compact_json(output, bundle)

    coverage = bundle["coverage"]
    print(
        f"{output}: {coverage['rootedStems']} rooted stems, "
        f"{coverage['roots']} roots, {coverage['branches']} branches, "
        f"{coverage['baselineAyat']} Turkish baseline ayat"
    )


if __name__ == "__main__":
    main()
