"""Shared construction and validation for pericope bundle manifests."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "pericope-bundle-manifest-v2"
MAX_JSON_BYTES = 128_000_000


class PericopeManifestError(RuntimeError):
    """Raised when a pericope package is incomplete, stale, or ambiguous."""


def canonical_sha256(value: Any) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def stable_path(path: Path, repo_root: Path) -> str:
    resolved = path.resolve(strict=False)
    try:
        return str(resolved.relative_to(repo_root.resolve(strict=False)))
    except ValueError:
        return str(resolved)


def resolve_path(value: str, repo_root: Path) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = repo_root / path
    return path.resolve(strict=False)


def file_record(path: Path, repo_root: Path) -> dict[str, Any]:
    if not path.is_file() or path.is_symlink():
        raise PericopeManifestError(f"Manifest source is missing or not regular: {path}")
    payload = path.read_bytes()
    return {
        "path": stable_path(path, repo_root),
        "bytes": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(),
    }


def verify_file_record(
    record: Any,
    *,
    label: str,
    repo_root: Path,
    expected: Path | None = None,
) -> Path:
    if not isinstance(record, dict):
        raise PericopeManifestError(f"{label} record must be an object")
    path_value = record.get("path")
    if not isinstance(path_value, str) or not path_value:
        raise PericopeManifestError(f"{label} record has no path")
    path = resolve_path(path_value, repo_root)
    if expected is not None and path != expected.resolve(strict=False):
        raise PericopeManifestError(f"{label} record names the wrong path: {path}")
    if not path.is_file() or path.is_symlink():
        raise PericopeManifestError(f"{label} is missing or not regular: {path}")
    payload = path.read_bytes()
    if record.get("bytes") != len(payload):
        raise PericopeManifestError(f"{label} byte count is stale: {path}")
    if record.get("sha256") != hashlib.sha256(payload).hexdigest():
        raise PericopeManifestError(f"{label} hash is stale: {path}")
    return path


def _expected_refs(row: dict[str, Any]) -> list[str]:
    return [
        f"{row['surah']}:{ayah}"
        for ayah in range(row["ayah_from"], row["ayah_to"] + 1)
    ]


def generation_policy() -> dict[str, str]:
    return {
        "package_scope": "pericope",
        "in_pericope_units": "non_tiered_full_base_bundles",
        "surah_aggregate": "not_emitted_for_pericope_roots",
        "prefatory_basmala": (
            "not emitted inside the pericope root; v4 injects S:0 from "
            "--member-bundles-dir when the numbered focus's surah has a "
            "prefatory basmala"
        ),
        "external_or_out_of_pericope_units": (
            "not generated here; pass a separate v4 --member-bundles-dir "
            "and declare context-only membership with --member-surah/--add-ayat"
        ),
        "v4_context_projection": (
            "full selected bundles remain hash-bound provenance sources; "
            "agent-facing non-focus members use lean ayah/root occurrences and "
            "compact mapped branch-image cues only"
        ),
    }


def _validate_build_command(
    command: Any,
    *,
    row: dict[str, Any],
    out_dir: Path,
    repo_root: Path,
    expected_lower_level_builder: Path,
) -> None:
    if not isinstance(command, list) or not all(
        isinstance(item, str) and item for item in command
    ):
        raise PericopeManifestError("Pericope manifest command must be a string array")
    if len(command) < 14:
        raise PericopeManifestError("Pericope manifest command is incomplete")
    command_builder = resolve_path(command[1], repo_root)
    if command_builder != expected_lower_level_builder.resolve(strict=False):
        raise PericopeManifestError(
            "Pericope manifest command names the wrong lower-level builder"
        )
    expected_prefix = [
        "--surah",
        str(row["surah"]),
        "--ayah-from",
        str(row["ayah_from"]),
        "--ayah-to",
        str(row["ayah_to"]),
        "--pericope",
        str(row["pericope"]),
        "--pericope-label",
        row["label"],
        "--out",
    ]
    if command[2:13] != expected_prefix:
        raise PericopeManifestError(
            "Pericope manifest command does not match its declared span"
        )
    if resolve_path(command[13], repo_root) != out_dir:
        raise PericopeManifestError(
            "Pericope manifest command names the wrong output directory"
        )
    optional = command[14:]
    if optional == ["--exclude-focus-trace"]:
        return
    if (
        len(optional) == 2
        and optional[0] == "--focus-trace-variant"
        and optional[1]
    ):
        return
    if optional:
        raise PericopeManifestError(
            "Pericope manifest command has unsupported or conflicting options"
        )


def _verify_index_row(index_path: Path, row: dict[str, Any]) -> None:
    payload = index_path.read_bytes()
    if len(payload) > MAX_JSON_BYTES:
        raise PericopeManifestError(f"Pericope index is too large: {index_path}")
    matches = 0
    try:
        lines = payload.decode("utf-8").splitlines()
    except UnicodeDecodeError as exc:
        raise PericopeManifestError(f"Invalid pericope index {index_path}: {exc}") from exc
    for lineno, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            indexed = json.loads(line)
        except json.JSONDecodeError as exc:
            raise PericopeManifestError(
                f"Invalid pericope index JSON {index_path}:{lineno}: {exc}"
            ) from exc
        if not isinstance(indexed, dict):
            raise PericopeManifestError(
                f"Pericope index row is not an object: {index_path}:{lineno}"
            )
        if all(indexed.get(key) == value for key, value in row.items()):
            matches += 1
    if matches != 1:
        raise PericopeManifestError(
            "Pericope index must contain exactly one row matching the package; "
            f"found {matches}"
        )


def _load_bundle(path: Path, row: dict[str, Any], ref: str) -> tuple[bytes, dict[str, Any]]:
    if not path.is_file() or path.is_symlink():
        raise PericopeManifestError(f"Expected pericope bundle is missing: {path}")
    payload = path.read_bytes()
    if len(payload) > MAX_JSON_BYTES:
        raise PericopeManifestError(f"Pericope bundle is too large: {path}")
    try:
        bundle = json.loads(payload)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PericopeManifestError(f"Invalid pericope bundle JSON {path}: {exc}") from exc
    if not isinstance(bundle, dict):
        raise PericopeManifestError(f"Pericope bundle must be one object: {path}")
    surah, ayah = (int(item) for item in ref.split(":"))
    if (
        bundle.get("bundle_type") != "ayah"
        or bundle.get("unit_kind", "numbered_ayah") != "numbered_ayah"
        or bundle.get("surah") != surah
        or bundle.get("ayah") != ayah
        or bundle.get("ayahRef") != ref
    ):
        raise PericopeManifestError(f"Pericope bundle identity does not match {ref}: {path}")
    pericope = bundle.get("pericope")
    expected_pericope = {
        key: row[key]
        for key in ("surah", "pericope", "ayah_from", "ayah_to", "label")
    }
    if not isinstance(pericope, dict) or any(
        pericope.get(key) != value for key, value in expected_pericope.items()
    ):
        raise PericopeManifestError(
            f"Pericope metadata does not match package span for {ref}: {path}"
        )
    return payload, bundle


def generated_file_records(
    row: dict[str, Any], out_dir: Path, repo_root: Path
) -> list[dict[str, Any]]:
    expected_refs = _expected_refs(row)
    expected_paths_in_order = [
        out_dir / f"{ref.replace(':', '_')}.ayah.json" for ref in expected_refs
    ]
    expected_paths = set(expected_paths_in_order)
    actual_paths = set(out_dir.rglob("*.ayah.json")) if out_dir.exists() else set()
    if actual_paths != expected_paths:
        missing = sorted(str(path) for path in expected_paths - actual_paths)
        extra = sorted(str(path) for path in actual_paths - expected_paths)
        raise PericopeManifestError(
            f"Pericope bundle file set is not exact; missing={missing}, extra={extra}"
        )

    records: list[dict[str, Any]] = []
    for ref, path in zip(expected_refs, expected_paths_in_order, strict=True):
        payload, bundle = _load_bundle(path, row, ref)
        records.append({
            "ayah_ref": ref,
            "path": stable_path(path, repo_root),
            "bytes": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest(),
            "canonical_sha256": canonical_sha256(bundle),
        })
    return records


def _manifest_row(manifest: dict[str, Any]) -> dict[str, Any]:
    row: dict[str, Any] = {}
    for key in ("surah", "pericope", "ayah_from", "ayah_to"):
        value = manifest.get(key)
        if not isinstance(value, int):
            raise PericopeManifestError(f"Pericope manifest {key} must be an integer")
        row[key] = value
    label = manifest.get("label")
    if not isinstance(label, str) or not label:
        raise PericopeManifestError("Pericope manifest label must be nonempty")
    row["label"] = label
    if not 1 <= row["surah"] <= 114:
        raise PericopeManifestError("Pericope manifest surah must be 1-114")
    if row["pericope"] <= 0 or row["ayah_from"] <= 0:
        raise PericopeManifestError("Pericope and ayah numbers must be positive")
    if row["ayah_to"] < row["ayah_from"]:
        raise PericopeManifestError("Pericope manifest span is descending")
    return row


def validate_manifest(
    manifest_path: Path,
    *,
    repo_root: Path,
    expected_builder: Path,
    expected_lower_level_builder: Path,
) -> dict[str, Any]:
    if not manifest_path.is_file() or manifest_path.is_symlink():
        raise PericopeManifestError(
            f"Pericope manifest is missing or not regular: {manifest_path}"
        )
    payload = manifest_path.read_bytes()
    try:
        manifest = json.loads(payload)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PericopeManifestError(
            f"Invalid pericope manifest JSON {manifest_path}: {exc}"
        ) from exc
    if not isinstance(manifest, dict):
        raise PericopeManifestError("Pericope manifest must be one object")
    if manifest.get("schema_version") != SCHEMA_VERSION:
        raise PericopeManifestError(
            f"Expected pericope manifest schema {SCHEMA_VERSION}"
        )

    row = _manifest_row(manifest)
    out_dir = manifest_path.parent.resolve(strict=False)
    if manifest.get("output_dir") != stable_path(out_dir, repo_root):
        raise PericopeManifestError("Pericope manifest output_dir is stale")
    verify_file_record(
        manifest.get("builder"),
        label="pericope builder",
        repo_root=repo_root,
        expected=expected_builder,
    )
    verify_file_record(
        manifest.get("manifest_implementation"),
        label="pericope manifest implementation",
        repo_root=repo_root,
        expected=expected_builder.parent / "pericope_bundle_manifest.py",
    )
    verify_file_record(
        manifest.get("lower_level_builder"),
        label="lower-level bundle builder",
        repo_root=repo_root,
        expected=expected_lower_level_builder,
    )

    source = manifest.get("source")
    index_record = manifest.get("pericope_index")
    if source == "index":
        index_path = verify_file_record(
            index_record,
            label="pericope index",
            repo_root=repo_root,
        )
        _verify_index_row(index_path, row)
    elif source == "cli-span":
        if index_record is not None:
            raise PericopeManifestError("CLI-span package must not bind an index")
    else:
        raise PericopeManifestError(f"Unknown pericope manifest source: {source!r}")

    _validate_build_command(
        manifest.get("command"),
        row=row,
        out_dir=out_dir,
        repo_root=repo_root,
        expected_lower_level_builder=expected_lower_level_builder,
    )
    if manifest.get("generation_policy") != generation_policy():
        raise PericopeManifestError("Pericope manifest generation policy is stale")

    actual_records = generated_file_records(row, out_dir, repo_root)
    expected_refs = _expected_refs(row)
    if manifest.get("ayah_refs") != expected_refs:
        raise PericopeManifestError("Pericope manifest ayah_refs are stale")
    if manifest.get("ayah_bundle_files") != actual_records:
        raise PericopeManifestError("Pericope manifest bundle records are stale")
    return manifest
