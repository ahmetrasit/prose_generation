#!/usr/bin/env python3
"""Build traceable non-tiered pericope bundle roots.

This is a wrapper around scripts/build_bundle.py's span mode. It keeps the
lower-level whole-surah/ayah builder unchanged while emitting a pericope
package root that the active commentary workflow can consume with
--context-bundles-dir.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import build_bundle
import pericope_bundle_manifest as package_manifest


SCHEMA_VERSION = package_manifest.SCHEMA_VERSION
SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parent.parent
DEFAULT_PERICOPE_INDEX = build_bundle.PERICOPES_PATH


def compact_json_text(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )


def repo_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path.resolve())


def pericope_slug(pericope: int, ayah_from: int, ayah_to: int) -> str:
    return f"p{pericope:02d}_{ayah_from:03d}-{ayah_to:03d}"


def validate_row(row: dict[str, Any], *, source: str) -> dict[str, Any]:
    required = ("surah", "pericope", "ayah_from", "ayah_to", "label")
    missing = [key for key in required if key not in row]
    if missing:
        raise RuntimeError(f"{source}: missing required key(s): {', '.join(missing)}")
    out = {
        "surah": int(row["surah"]),
        "pericope": int(row["pericope"]),
        "ayah_from": int(row["ayah_from"]),
        "ayah_to": int(row["ayah_to"]),
        "label": str(row["label"]),
    }
    if out["surah"] < 1 or out["surah"] > 114:
        raise RuntimeError(f"{source}: surah must be 1-114")
    if out["pericope"] < 1:
        raise RuntimeError(f"{source}: pericope must be positive")
    if out["ayah_from"] <= 0 or out["ayah_to"] <= 0:
        raise RuntimeError(f"{source}: pericope spans must contain numbered ayahs only")
    if out["ayah_from"] > out["ayah_to"]:
        raise RuntimeError(f"{source}: ayah_from must be <= ayah_to")
    return out


def load_index_rows(index_path: Path, surah: int) -> list[dict[str, Any]]:
    if not index_path.is_file():
        raise RuntimeError(f"Pericope index is missing: {index_path}")
    rows: list[dict[str, Any]] = []
    with index_path.open(encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise RuntimeError(f"{index_path}:{lineno}: invalid JSON: {exc}") from exc
            if row.get("surah") == surah:
                rows.append(validate_row(row, source=f"{index_path}:{lineno}"))
    return sorted(rows, key=lambda row: row["pericope"])


def rows_from_args(args: argparse.Namespace) -> list[dict[str, Any]]:
    if args.ayah_from is not None or args.ayah_to is not None:
        if args.ayah_from is None or args.ayah_to is None:
            raise RuntimeError("--ayah-from and --ayah-to must be passed together")
        return [
            validate_row(
                {
                    "surah": args.surah,
                    "pericope": args.pericope or 1,
                    "ayah_from": args.ayah_from,
                    "ayah_to": args.ayah_to,
                    "label": args.pericope_label
                    or f"Ayahs {args.ayah_from}-{args.ayah_to}",
                },
                source="cli",
            )
        ]

    rows = load_index_rows(args.pericope_index, args.surah)
    if not rows:
        raise RuntimeError(
            f"No pericope rows found for surah {args.surah} in {args.pericope_index}"
        )
    if args.pericope is not None:
        rows = [row for row in rows if row["pericope"] == args.pericope]
        if not rows:
            raise RuntimeError(
                f"No pericope {args.pericope} found for surah {args.surah}"
            )
    elif not args.all:
        raise RuntimeError("Pass --pericope N, --all, or an explicit --ayah-from/--ayah-to span")
    return rows


def output_dir_for(row: dict[str, Any], out_root: Path, out: Path | None) -> Path:
    if out is not None:
        return out
    return out_root / pericope_slug(row["pericope"], row["ayah_from"], row["ayah_to"])


def build_command(
    row: dict[str, Any],
    out_dir: Path,
    *,
    exclude_focus_trace: bool,
    focus_trace_variant: str | None,
) -> list[str]:
    command = [
        sys.executable,
        str(REPO_ROOT / "scripts" / "build_bundle.py"),
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
        str(out_dir.resolve(strict=False)),
    ]
    if exclude_focus_trace:
        command.append("--exclude-focus-trace")
    if focus_trace_variant is not None:
        command.extend(["--focus-trace-variant", focus_trace_variant])
    return command


def generated_file_records(row: dict[str, Any], out_dir: Path) -> list[dict[str, Any]]:
    try:
        return package_manifest.generated_file_records(row, out_dir, REPO_ROOT)
    except package_manifest.PericopeManifestError as exc:
        raise RuntimeError(str(exc)) from exc


def write_manifest(
    row: dict[str, Any],
    out_dir: Path,
    *,
    command: list[str],
    pericope_index: Path | None,
    source: str,
) -> Path:
    files = generated_file_records(row, out_dir)
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "builder": package_manifest.file_record(SCRIPT_PATH, REPO_ROOT),
        "manifest_implementation": package_manifest.file_record(
            REPO_ROOT / "scripts" / "pericope_bundle_manifest.py", REPO_ROOT
        ),
        "lower_level_builder": package_manifest.file_record(
            REPO_ROOT / "scripts" / "build_bundle.py", REPO_ROOT
        ),
        "alignment_implementation": package_manifest.file_record(
            REPO_ROOT / "scripts" / "word_morpheme_alignment.py", REPO_ROOT
        ),
        "command": command,
        "source": source,
        "pericope_index": (
            package_manifest.file_record(pericope_index, REPO_ROOT)
            if pericope_index is not None
            else None
        ),
        "output_dir": repo_path(out_dir),
        "surah": row["surah"],
        "pericope": row["pericope"],
        "ayah_from": row["ayah_from"],
        "ayah_to": row["ayah_to"],
        "label": row["label"],
        "ayah_refs": [record["ayah_ref"] for record in files],
        "ayah_bundle_files": files,
        "generation_policy": package_manifest.generation_policy(),
    }
    path = out_dir / "pericope.bundle-manifest.json"
    path.write_text(compact_json_text(manifest), encoding="utf-8")
    try:
        package_manifest.validate_manifest(
            path,
            repo_root=REPO_ROOT,
            expected_builder=SCRIPT_PATH,
            expected_lower_level_builder=REPO_ROOT / "scripts" / "build_bundle.py",
        )
    except package_manifest.PericopeManifestError as exc:
        raise RuntimeError(str(exc)) from exc
    return path


def build_one(row: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    out_dir = output_dir_for(row, args.out_root, args.out)
    command = build_command(
        row,
        out_dir,
        exclude_focus_trace=args.exclude_focus_trace,
        focus_trace_variant=args.focus_trace_variant,
    )
    if args.dry_run:
        return {
            "surah": row["surah"],
            "pericope": row["pericope"],
            "output_dir": str(out_dir),
            "command": command,
            "dry_run": True,
        }
    print("running " + " ".join(command), flush=True)
    subprocess.run(command, check=True)
    manifest_path = write_manifest(
        row,
        out_dir,
        command=command,
        pericope_index=args.pericope_index if args.ayah_from is None else None,
        source="index" if args.ayah_from is None else "cli-span",
    )
    print(f"wrote {manifest_path}")
    return {
        "surah": row["surah"],
        "pericope": row["pericope"],
        "output_dir": str(out_dir),
        "manifest": str(manifest_path),
        "ayah_count": row["ayah_to"] - row["ayah_from"] + 1,
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--pericope", type=int, default=None)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--ayah-from", type=int, default=None)
    parser.add_argument("--ayah-to", type=int, default=None)
    parser.add_argument("--pericope-label", default=None)
    parser.add_argument("--pericope-index", type=Path, default=DEFAULT_PERICOPE_INDEX)
    parser.add_argument("--out-root", type=Path, default=None)
    parser.add_argument("--out", type=Path, default=None)
    parser.add_argument("--exclude-focus-trace", action="store_true")
    parser.add_argument("--focus-trace-variant", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    if args.surah < 1 or args.surah > 114:
        parser.error("--surah must be 1-114")
    if args.all and args.pericope is not None:
        parser.error("--all cannot be combined with --pericope")
    if args.all and (args.ayah_from is not None or args.ayah_to is not None):
        parser.error("--all cannot be combined with an explicit span")
    if args.out is not None and args.all:
        parser.error("--out can only be used for a single pericope/span")
    if args.exclude_focus_trace and args.focus_trace_variant is not None:
        parser.error("--focus-trace-variant cannot be combined with --exclude-focus-trace")
    if args.out_root is None:
        args.out_root = REPO_ROOT / "bundles" / f"s{args.surah:03d}-pericopes"
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        rows = rows_from_args(args)
        results = [build_one(row, args) for row in rows]
    except subprocess.CalledProcessError as exc:
        print(f"FATAL: lower-level builder failed with exit {exc.returncode}", file=sys.stderr)
        return exc.returncode or 1
    except RuntimeError as exc:
        print(f"FATAL: {exc}", file=sys.stderr)
        return 1
    print(compact_json_text({"results": results}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
