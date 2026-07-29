#!/usr/bin/env python3
"""Build a hermetic source packet for the Layer 3 surah-reading workflow."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

from common import REPO_ROOT, WORKFLOW_ROOT, load_json, load_jsonl, portable_path, write_json


V11_FILES: tuple[tuple[str, str, str, str], ...] = (
    ("00-root-resolution-audit.json", "v11-root-audit", "v11-root-audit", "legacy-recall"),
    ("05-activation-pass.json", "v11-activation", "v11-activation", "legacy-recall"),
    ("06-mechanism.md", "v11-mechanism", "v11-mechanism", "legacy-recall"),
    (
        "07-secondary-expansion.json",
        "v11-secondary-expansion",
        "v11-secondary-expansion",
        "legacy-recall",
    ),
    ("09-final-report.md", "v11-final-report", "v11-final-report", "legacy-recall"),
)


def warn(message: str, warnings: list[str]) -> None:
    warnings.append(message)
    print(f"warning: {message}", file=sys.stderr)


def source_format(path: Path) -> str:
    if path.suffix == ".json" or path.suffix == ".jsonl":
        return "json"
    if path.suffix == ".tsv":
        return "tsv"
    return "markdown"


def read_content(path: Path) -> Any:
    if path.suffix == ".json":
        return load_json(path)
    if path.suffix == ".jsonl":
        return load_jsonl(path)
    return path.read_text(encoding="utf-8")


def facet_names(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    names = []
    for item in value:
        if isinstance(item, list) and item and isinstance(item[0], str):
            names.append(item[0])
        elif isinstance(item, str):
            names.append(item)
    return names


def branch_ref(branch: Any) -> str | None:
    if not isinstance(branch, dict):
        return None
    node_id = branch.get("node_id")
    if isinstance(node_id, str):
        return node_id
    root = branch.get("root")
    branch_id = branch.get("branch_id")
    if isinstance(root, str) and isinstance(branch_id, str):
        return f"{root}:{branch_id}"
    return None


def collect_branch(
    catalog: dict[str, dict[str, Any]], branch: Any
) -> str | None:
    ref = branch_ref(branch)
    if ref is None or not isinstance(branch, dict):
        return ref
    if ref not in catalog:
        catalog[ref] = {
            key: branch[key]
            for key in ("root", "branch_id", "ayahs", "image_ar")
            if key in branch
        }
    return ref


def branch_refs(
    catalog: dict[str, dict[str, Any]], branches: Any
) -> list[str]:
    if not isinstance(branches, list):
        return []
    refs = []
    for branch in branches:
        ref = collect_branch(catalog, branch)
        if ref is not None:
            refs.append(ref)
    return refs


def compact_network(
    network_dir: Path,
) -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
    catalog: dict[str, dict[str, Any]] = {}
    result: dict[str, Any] = {}

    candidate_path = network_dir / "channel_candidates.jsonl"
    if candidate_path.exists():
        candidates = []
        for row in load_jsonl(candidate_path):
            candidates.append(
                {
                    "candidateId": row.get("candidate_id"),
                    "label": row.get("label_hint"),
                    "ayahs": row.get("ayahs", []),
                    "branches": branch_refs(catalog, row.get("branches")),
                    "facets": facet_names(row.get("top_facets")),
                }
            )
        result["candidates"] = candidates

    family_path = network_dir / "families" / "channel_families.jsonl"
    if family_path.exists():
        families = []
        for row in load_jsonl(family_path):
            families.append(
                {
                    "familyId": row.get("family_id"),
                    "label": row.get("label_hint"),
                    "structuralType": row.get("structural_type"),
                    "candidateIds": row.get("candidate_ids", []),
                    "ayahs": row.get("ayahs", []),
                    "coreBranches": branch_refs(catalog, row.get("core_branches")),
                    "optionalBranches": branch_refs(
                        catalog, row.get("optional_branches")
                    ),
                    "rareBranches": branch_refs(catalog, row.get("rare_branches")),
                    "facets": facet_names(row.get("top_facets")),
                }
            )
        result["families"] = families

    path_family_path = (
        network_dir
        / "paths"
        / "path_families"
        / "semantic_path_families.jsonl"
    )
    if path_family_path.exists():
        path_families = []
        for row in load_jsonl(path_family_path):
            alternatives = {}
            raw_alternatives = row.get("branch_alternatives_by_root")
            if isinstance(raw_alternatives, dict):
                for root, branches in raw_alternatives.items():
                    alternatives[root] = branch_refs(catalog, branches)
            path_families.append(
                {
                    "pathFamilyId": row.get("path_family_id"),
                    "label": row.get("label_hint"),
                    "ayahs": row.get("ayahs", []),
                    "coreBranches": branch_refs(catalog, row.get("core_branches")),
                    "optionalBranches": branch_refs(
                        catalog, row.get("optional_branches")
                    ),
                    "branchAlternatives": alternatives,
                    "facets": facet_names(row.get("top_facets")),
                }
            )
        result["pathFamilies"] = path_families
    return catalog, result


def compact_v11_branches(path: Path) -> dict[str, Any]:
    data = load_json(path)
    compact_roots = []
    roots = data.get("roots", {})
    if isinstance(roots, dict):
        for root, item in roots.items():
            if not isinstance(item, dict):
                continue
            compact_branches = []
            branches = item.get("branches", {})
            if isinstance(branches, dict):
                for branch_id, branch in branches.items():
                    if not isinstance(branch, dict):
                        continue
                    image = branch.get("image", {})
                    if not isinstance(image, dict):
                        image = {}
                    compact_branches.append(
                        {
                            "branchId": branch_id,
                            "imageAr": image.get("branch_image_ar"),
                            "imageEn": image.get("branch_image_en"),
                            "scopeEn": image.get("what_is_en"),
                            "keywords": branch.get("raw_keywords", []),
                        }
                    )
            occurrences = []
            for occurrence in item.get("surface_occurrences", []):
                if isinstance(occurrence, dict):
                    occurrences.append(
                        {
                            "qacRef": occurrence.get("qac_ref"),
                            "surfaceAr": occurrence.get("surface_ar"),
                        }
                    )
            compact_roots.append(
                {
                    "root": root,
                    "rootId": item.get("root_id"),
                    "occurrences": occurrences,
                    "branches": compact_branches,
                }
            )
    return {
        "schema": data.get("schema"),
        "roots": compact_roots,
        "missingRoots": data.get("missing_roots", []),
        "omittedRoots": data.get("omitted_roots", []),
    }


def compact_v11_ranking(path: Path) -> dict[str, Any]:
    data = load_json(path)
    bridges = []
    for item in data.get("top_candidate_bridges", []):
        if not isinstance(item, dict):
            continue
        bridges.append(
            {
                key: item[key]
                for key in (
                    "source_branch_key",
                    "target_branch_key",
                    "shared_themes",
                    "shared_keywords",
                    "rare_shared_themes",
                    "activation_hint",
                )
                if key in item
            }
        )
    return {
        "rankingSemantics": data.get("ranking_semantics"),
        "topBranchCandidates": data.get("top_branch_candidates", []),
        "topCandidateBridges": bridges,
    }


def add_source(
    sources: list[dict[str, Any]],
    *,
    source_id: str,
    kind: str,
    role: str,
    path: Path,
    quran_data: Path,
    latent_activation: Path,
    content: Any | None = None,
    transform: str | None = None,
) -> str:
    item: dict[str, Any] = {
        "sourceId": source_id,
        "kind": kind,
        "role": role,
        "path": portable_path(
            path, quran_data=quran_data, latent_activation=latent_activation
        ),
        "format": source_format(path),
        "content": read_content(path) if content is None else content,
    }
    if transform:
        item["transform"] = transform
    sources.append(item)
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
    *,
    required: bool,
) -> Path | None:
    if label:
        candidate = directory / f"{surah}_{ayah}.{kind}.{label}.md"
        if candidate.exists():
            return candidate
        if required:
            raise SystemExit(f"error: missing required Layer-2 file: {candidate}")
        return None
    matches = sorted(directory.glob(f"{surah}_{ayah}.{kind}*.md"))
    if len(matches) == 1:
        return matches[0]
    if not matches:
        if required:
            raise SystemExit(
                f"error: missing Layer-2 {kind} for {surah}:{ayah} in {directory}"
            )
        return None
    rendered = "\n".join(f"  {path}" for path in matches)
    raise SystemExit(
        f"error: ambiguous Layer-2 {kind} for {surah}:{ayah}; pass "
        f"--layer2-label:\n{rendered}"
    )


def find_v11_dir(quran_data: Path, latent_activation: Path, surah: int) -> tuple[Path | None, bool]:
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
    notes: list[str] | None = None,
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
        "notes": notes or [],
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
    sources: list[dict[str, Any]] = []
    warnings: list[str] = []

    quran_path = quran_data / "data" / "text" / "quran-uthmani.tsv"
    if not quran_path.exists():
        raise SystemExit(f"error: required Quran text is missing: {quran_path}")
    quran_rows = parse_quran_text(quran_path, surah)
    quran_source_id = add_source(
        sources,
        source_id="quran-text",
        kind="quran-text",
        role="primary-ground",
        path=quran_path,
        quran_data=quran_data,
        latent_activation=latent_activation,
        content=quran_rows,
        transform=f"Rows scoped to surah {surah}.",
    )
    numbered_rows = [
        row for row in quran_rows if not row["ayahRef"].endswith(":0")
    ]
    expected_ayahs = [int(row["ayahRef"].split(":")[1]) for row in numbered_rows]

    if not layer2_dir.is_dir():
        raise SystemExit(f"error: Layer-2 directory does not exist: {layer2_dir}")
    layer2_ids: list[str] = []
    layer2_missing: list[str] = []
    ayah_source_refs: dict[int, list[str]] = {ayah: [quran_source_id] for ayah in expected_ayahs}
    for ayah in expected_ayahs:
        for kind, required, role in (
            ("prose", True, "local-reading"),
            ("evidence", True, "local-apparatus"),
            ("index", False, "local-apparatus"),
            ("friction", False, "production-context"),
        ):
            path = select_layer2_file(
                layer2_dir,
                surah,
                ayah,
                kind,
                layer2_label,
                required=required,
            )
            if path is None:
                layer2_missing.append(f"{surah}:{ayah}:{kind}")
                continue
            source_id = f"layer2-{kind}-{surah}-{ayah}"
            source_kind = f"layer2-{kind}"
            layer2_ids.append(
                add_source(
                    sources,
                    source_id=source_id,
                    kind=source_kind,
                    role=role,
                    path=path,
                    quran_data=quran_data,
                    latent_activation=latent_activation,
                )
            )
            ayah_source_refs[ayah].append(source_id)

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
    if network_dir.is_dir():
        for relative, source_id, kind, role in (
            (
                "review/reader_a_pilot.md",
                "network-review",
                "network-review",
                "reviewed-evidence",
            ),
            (
                "summary.json",
                "network-summary",
                "network-summary",
                "candidate-evidence",
            ),
        ):
            path = network_dir / relative
            if not path.exists():
                network_missing.append(relative)
                continue
            network_ids.append(
                add_source(
                    sources,
                    source_id=source_id,
                    kind=kind,
                    role=role,
                    path=path,
                    quran_data=quran_data,
                    latent_activation=latent_activation,
                )
            )
        branch_catalog, compact_network_data = compact_network(network_dir)
        network_compact_files = (
            (
                "channel_candidates.jsonl",
                "network-candidates",
                "network-candidates",
                "candidates",
            ),
            (
                "families/channel_families.jsonl",
                "network-families",
                "network-families",
                "families",
            ),
            (
                "paths/path_families/semantic_path_families.jsonl",
                "network-path-families",
                "network-path-families",
                "pathFamilies",
            ),
        )
        for relative, source_id, kind, content_key in network_compact_files:
            path = network_dir / relative
            if not path.exists():
                network_missing.append(relative)
                continue
            network_ids.append(
                add_source(
                    sources,
                    source_id=source_id,
                    kind=kind,
                    role="candidate-evidence",
                    path=path,
                    quran_data=quran_data,
                    latent_activation=latent_activation,
                    content=compact_network_data[content_key],
                    transform=(
                        "Every row retained; repeated branch objects, graph edges, "
                        "scores, and build diagnostics removed."
                    ),
                )
            )
        if branch_catalog:
            catalog_path = network_dir / "channel_candidates.jsonl"
            if not catalog_path.exists():
                catalog_path = network_dir / "families" / "channel_families.jsonl"
            network_ids.append(
                add_source(
                    sources,
                    source_id="network-branch-catalog",
                    kind="network-branch-catalog",
                    role="candidate-evidence",
                    path=catalog_path,
                    quran_data=quran_data,
                    latent_activation=latent_activation,
                    content=branch_catalog,
                    transform=(
                        "Deduplicated semantic branch records referenced by all "
                        "compacted network candidates, families, and path families."
                    ),
                )
            )
        if network_missing:
            warn(
                f"network-v3 is partial for s{surah:03d}; continuing without "
                + ", ".join(network_missing),
                warnings,
            )
    else:
        network_missing.append(str(network_dir))
        warn(f"network-v3 is absent for s{surah:03d}; continuing", warnings)

    v12_ids: list[str] = []
    v12_missing: list[str] = []
    v12_files = (
        (
            quran_data
            / "data"
            / "analysis"
            / "ayah-activation"
            / "v12-tr"
            / f"s{surah:03d}"
            / "publication.v3.draft.json",
            "v12-publication",
            "v12-publication",
        ),
        (
            quran_data
            / "data"
            / "analysis"
            / "ayah-activation"
            / "v12-cross-run"
            / language
            / f"{surah}_ayah_findings_publication.json",
            "v12-cross-run",
            "v12-cross-run",
        ),
    )
    for path, source_id, kind in v12_files:
        if not path.exists():
            v12_missing.append(portable_path(path, quran_data=quran_data))
            continue
        v12_ids.append(
            add_source(
                sources,
                source_id=source_id,
                kind=kind,
                role="candidate-evidence",
                path=path,
                quran_data=quran_data,
                latent_activation=latent_activation,
            )
        )
    if not v12_ids:
        warn(f"V12 publication evidence is absent for s{surah:03d}; continuing", warnings)
    elif v12_missing:
        warn(f"V12 publication evidence is partial for s{surah:03d}; continuing", warnings)

    v11_ids: list[str] = []
    v11_missing: list[str] = []
    v11_dir, v11_fallback = find_v11_dir(quran_data, latent_activation, surah)
    if v11_dir is None:
        v11_missing.append(f"v11/run/s{surah:03d}")
        warn(f"V11 is absent for s{surah:03d}; continuing", warnings)
        v11_root = None
    else:
        v11_root = portable_path(
            v11_dir, quran_data=quran_data, latent_activation=latent_activation
        )
        if v11_fallback:
            warn(
                f"V11 was not found in quran-data for s{surah:03d}; using "
                "latent_activation fallback",
                warnings,
            )
        for filename, source_id, kind, role in V11_FILES:
            path = v11_dir / filename
            if not path.exists():
                v11_missing.append(filename)
                continue
            v11_ids.append(
                add_source(
                    sources,
                    source_id=source_id,
                    kind=kind,
                    role=role,
                    path=path,
                    quran_data=quran_data,
                    latent_activation=latent_activation,
                )
            )
        branches_path = v11_dir / "02-branches.json"
        if branches_path.exists():
            v11_ids.append(
                add_source(
                    sources,
                    source_id="v11-branches",
                    kind="v11-branches",
                    role="legacy-recall",
                    path=branches_path,
                    quran_data=quran_data,
                    latent_activation=latent_activation,
                    content=compact_v11_branches(branches_path),
                    transform=(
                        "All roots and branches retained; repeated theme votes and "
                        "morphology diagnostics removed."
                    ),
                )
            )
        else:
            v11_missing.append("02-branches.json")
        ranking_path = v11_dir / "10-discovery-ranking.json"
        if ranking_path.exists():
            v11_ids.append(
                add_source(
                    sources,
                    source_id="v11-ranking",
                    kind="v11-ranking",
                    role="legacy-recall",
                    path=ranking_path,
                    quran_data=quran_data,
                    latent_activation=latent_activation,
                    content=compact_v11_ranking(ranking_path),
                    transform=(
                        "Top branch and bridge semantics retained; duplicate scoring "
                        "and discovery diagnostics removed."
                    ),
                )
            )
        else:
            v11_missing.append("10-discovery-ranking.json")
        holistic = next(iter(sorted(v11_dir.glob(f"{surah}-*-butuncul-okuma.md"))), None)
        if holistic is None:
            v11_missing.append("*-butuncul-okuma.md")
        else:
            v11_ids.append(
                add_source(
                    sources,
                    source_id="v11-holistic-reading",
                    kind="v11-holistic-reading",
                    role="legacy-recall",
                    path=holistic,
                    quran_data=quran_data,
                    latent_activation=latent_activation,
                )
            )
        if v11_missing:
            warn(
                f"V11 is partial for s{surah:03d}; continuing without "
                + ", ".join(v11_missing),
                warnings,
            )

    ayahs = []
    for row in quran_rows:
        ayah = int(row["ayahRef"].split(":")[1])
        ayahs.append(
            {
                "ayahRef": row["ayahRef"],
                "unitType": "basmala" if ayah == 0 else "ayah",
                "arabic": row["arabic"],
                "sourceRefs": [quran_source_id]
                if ayah == 0
                else ayah_source_refs[ayah],
            }
        )

    return {
        "schemaVersion": "layer3-source-packet-v1",
        "packetId": f"s{surah:03d}-{language}-layer3-v1",
        "surah": surah,
        "language": language,
        "ayahs": ayahs,
        "sources": sources,
        "coverage": {
            "quranText": coverage_group(
                source_ids=[quran_source_id],
                missing=[],
                required=True,
                notes=[f"{len(numbered_rows)} numbered ayahs; basmala retained when present."],
            ),
            "layer2": coverage_group(
                source_ids=layer2_ids,
                missing=layer2_missing,
                required=True,
                notes=[
                    "Prose and evidence are required; index and friction are optional.",
                    f"Layer-2 label: {layer2_label or 'unique match'}",
                ],
            ),
            "networkV3": coverage_group(
                source_ids=network_ids,
                missing=network_missing,
                required=False,
                notes=["Optional recall source; absence does not stop the workflow."],
                source_root=portable_path(network_dir, quran_data=quran_data),
            ),
            "v12": coverage_group(
                source_ids=v12_ids,
                missing=v12_missing,
                required=False,
                notes=["Optional publication findings; absence does not stop the workflow."],
            ),
            "v11": coverage_group(
                source_ids=v11_ids,
                missing=v11_missing,
                required=False,
                notes=["Optional recall-first legacy evidence; absence does not stop the workflow."],
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
        f"wrote {output} ({len(packet['sources'])} sources, "
        f"{len(packet['warnings'])} warnings)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
