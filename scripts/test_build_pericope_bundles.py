#!/usr/bin/env python3

from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import build_pericope_bundles as builder


def ayah_bundle(row: dict[str, object], ayah: int) -> dict[str, object]:
    surah = int(row["surah"])
    ref = f"{surah}:{ayah}"
    return {
        "bundle_type": "ayah",
        "schema_version": "input-bundle-v4",
        "unit_kind": "numbered_ayah",
        "surah": surah,
        "ayah": ayah,
        "ayahRef": ref,
        "surface_ref": ref,
        "linguistic_source_ref": ref,
        "pericope": {
            key: row[key]
            for key in ("surah", "pericope", "ayah_from", "ayah_to", "label")
        },
    }


def write_bundles(out_dir: Path, row: dict[str, object]) -> None:
    for ayah in range(int(row["ayah_from"]), int(row["ayah_to"]) + 1):
        (out_dir / f"{row['surah']}_{ayah}.ayah.json").write_text(
            json.dumps(ayah_bundle(row, ayah)), encoding="utf-8"
        )


class PericopeBundleScriptTests(unittest.TestCase):
    def test_pericope_slug_is_stable(self) -> None:
        self.assertEqual(builder.pericope_slug(2, 36, 69), "p02_036-069")

    def test_load_index_rows_filters_and_orders_surah(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            index = Path(tmp) / "surah_pericopes.jsonl"
            index.write_text(
                "\n".join(
                    [
                        json.dumps(
                            {
                                "surah": 29,
                                "pericope": 2,
                                "ayah_from": 36,
                                "ayah_to": 69,
                                "label": "Late",
                            }
                        ),
                        json.dumps(
                            {
                                "surah": 2,
                                "pericope": 1,
                                "ayah_from": 1,
                                "ayah_to": 20,
                                "label": "Other",
                            }
                        ),
                        json.dumps(
                            {
                                "surah": 29,
                                "pericope": 1,
                                "ayah_from": 1,
                                "ayah_to": 35,
                                "label": "Early",
                            }
                        ),
                    ]
                ),
                encoding="utf-8",
            )

            rows = builder.load_index_rows(index, 29)

        self.assertEqual([row["pericope"] for row in rows], [1, 2])
        self.assertEqual(rows[1]["ayah_from"], 36)

    def test_rows_from_args_accepts_manual_span_without_index(self) -> None:
        args = builder.parse_args(
            [
                "--surah",
                "29",
                "--pericope",
                "2",
                "--ayah-from",
                "36",
                "--ayah-to",
                "69",
                "--pericope-label",
                "Second half",
            ]
        )

        rows = builder.rows_from_args(args)

        self.assertEqual(
            rows,
            [
                {
                    "surah": 29,
                    "pericope": 2,
                    "ayah_from": 36,
                    "ayah_to": 69,
                    "label": "Second half",
                }
            ],
        )

    def test_build_command_uses_span_mode_and_output_root(self) -> None:
        row = {
            "surah": 29,
            "pericope": 2,
            "ayah_from": 36,
            "ayah_to": 69,
            "label": "Second half",
        }

        command = builder.build_command(
            row,
            Path("bundles/s029-pericopes/p02_036-069"),
            exclude_focus_trace=True,
            focus_trace_variant=None,
        )

        self.assertIn("scripts/build_bundle.py", command[1])
        self.assertIn("--ayah-from", command)
        self.assertIn("36", command)
        self.assertIn("--ayah-to", command)
        self.assertIn("69", command)
        self.assertIn("--exclude-focus-trace", command)

    def test_write_manifest_records_generated_files_and_policy(self) -> None:
        row = {
            "surah": 29,
            "pericope": 1,
            "ayah_from": 1,
            "ayah_to": 2,
            "label": "Opening",
        }
        with tempfile.TemporaryDirectory() as tmp:
            out_dir = Path(tmp)
            write_bundles(out_dir, row)
            path = builder.write_manifest(
                row,
                out_dir,
                command=builder.build_command(
                    row,
                    out_dir,
                    exclude_focus_trace=False,
                    focus_trace_variant=None,
                ),
                pericope_index=None,
                source="cli-span",
            )
            manifest = json.loads(path.read_text(encoding="utf-8"))

        self.assertEqual(manifest["schema_version"], builder.SCHEMA_VERSION)
        self.assertEqual(manifest["ayah_refs"], ["29:1", "29:2"])
        self.assertEqual(len(manifest["ayah_bundle_files"]), 2)
        self.assertEqual(
            manifest["generation_policy"]["in_pericope_units"],
            "non_tiered_full_base_bundles",
        )
        self.assertIn(
            "--member-bundles-dir",
            manifest["generation_policy"]["external_or_out_of_pericope_units"],
        )
        self.assertIn(
            "commentary_context_projection", manifest["generation_policy"]
        )
        self.assertNotIn("v4_context_projection", manifest["generation_policy"])
        self.assertIn("sha256", manifest["builder"])
        self.assertIn("canonical_sha256", manifest["ayah_bundle_files"][0])

    def test_legacy_policy_is_accepted_only_for_pinned_historical_manifest(self) -> None:
        historical_path = (
            builder.REPO_ROOT
            / "bundles"
            / "s029-pericopes"
            / "p03_028-044"
            / "pericope.bundle-manifest.json"
        )
        historical_payload = historical_path.read_bytes()
        historical = json.loads(historical_payload)
        validated_historical = builder.package_manifest.validate_manifest(
            historical_path,
            repo_root=builder.REPO_ROOT,
            expected_builder=builder.SCRIPT_PATH,
            expected_lower_level_builder=(
                builder.REPO_ROOT / "scripts" / "build_bundle.py"
            ),
        )
        self.assertEqual(
            validated_historical["ayah_refs"], historical["ayah_refs"]
        )
        self.assertEqual(
            builder.package_manifest._verify_manifest_implementation(
                historical["manifest_implementation"],
                manifest_path=historical_path,
                manifest_payload=historical_payload,
                repo_root=builder.REPO_ROOT,
                expected=(
                    builder.REPO_ROOT / "scripts" / "pericope_bundle_manifest.py"
                ),
            ),
            "legacy_v4",
        )

        row = {
            "surah": 29,
            "pericope": 1,
            "ayah_from": 1,
            "ayah_to": 1,
            "label": "Opening",
        }
        validate_kwargs = {
            "repo_root": builder.REPO_ROOT,
            "expected_builder": builder.SCRIPT_PATH,
            "expected_lower_level_builder": (
                builder.REPO_ROOT / "scripts" / "build_bundle.py"
            ),
        }
        with tempfile.TemporaryDirectory() as tmp:
            out_dir = Path(tmp)
            write_bundles(out_dir, row)
            path = builder.write_manifest(
                row,
                out_dir,
                command=builder.build_command(
                    row,
                    out_dir,
                    exclude_focus_trace=False,
                    focus_trace_variant=None,
                ),
                pericope_index=None,
                source="cli-span",
            )
            current = json.loads(path.read_text(encoding="utf-8"))
            legacy = copy.deepcopy(current)
            legacy_records = next(iter(
                builder.package_manifest.LEGACY_V4_MANIFEST_RECORDS.values()
            ))
            legacy_bytes, legacy_sha256 = legacy_records[
                "manifest_implementation"
            ]
            legacy["manifest_implementation"].update({
                "bytes": legacy_bytes,
                "sha256": legacy_sha256,
            })
            legacy["generation_policy"] = (
                builder.package_manifest.legacy_v4_generation_policy()
            )
            path.write_text(json.dumps(legacy), encoding="utf-8")
            with self.assertRaisesRegex(
                builder.package_manifest.PericopeManifestError,
                "stale or unknown",
            ):
                builder.package_manifest.validate_manifest(path, **validate_kwargs)

            legacy["manifest_implementation"] = current["manifest_implementation"]
            path.write_text(json.dumps(legacy), encoding="utf-8")
            with self.assertRaisesRegex(
                builder.package_manifest.PericopeManifestError, "policy"
            ):
                builder.package_manifest.validate_manifest(path, **validate_kwargs)

    def test_generated_file_records_reject_identity_and_stale_extras(self) -> None:
        row = {
            "surah": 29,
            "pericope": 1,
            "ayah_from": 1,
            "ayah_to": 1,
            "label": "Opening",
        }
        with tempfile.TemporaryDirectory() as tmp:
            out_dir = Path(tmp)
            write_bundles(out_dir, row)
            wrong = ayah_bundle(row, 1)
            wrong["ayahRef"] = "29:2"
            (out_dir / "29_1.ayah.json").write_text(
                json.dumps(wrong), encoding="utf-8"
            )
            with self.assertRaisesRegex(RuntimeError, "identity"):
                builder.generated_file_records(row, out_dir)

            write_bundles(out_dir, row)
            (out_dir / "29_2.ayah.json").write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "extra"):
                builder.generated_file_records(row, out_dir)

    def test_manifest_revalidation_detects_changed_index(self) -> None:
        row = {
            "surah": 29,
            "pericope": 1,
            "ayah_from": 1,
            "ayah_to": 1,
            "label": "Opening",
        }
        with tempfile.TemporaryDirectory() as tmp:
            out_dir = Path(tmp) / "package"
            out_dir.mkdir()
            index = Path(tmp) / "index.jsonl"
            index.write_text(json.dumps(row) + "\n", encoding="utf-8")
            write_bundles(out_dir, row)
            path = builder.write_manifest(
                row,
                out_dir,
                command=builder.build_command(
                    row,
                    out_dir,
                    exclude_focus_trace=False,
                    focus_trace_variant=None,
                ),
                pericope_index=index,
                source="index",
            )
            index.write_text("modified\n", encoding="utf-8")
            with self.assertRaisesRegex(
                builder.package_manifest.PericopeManifestError, "stale"
            ):
                builder.package_manifest.validate_manifest(
                    path,
                    repo_root=builder.REPO_ROOT,
                    expected_builder=builder.SCRIPT_PATH,
                    expected_lower_level_builder=(
                        builder.REPO_ROOT / "scripts" / "build_bundle.py"
                    ),
                )

    def test_manifest_rejects_false_command_policy_and_index_lineage(self) -> None:
        row = {
            "surah": 29,
            "pericope": 1,
            "ayah_from": 1,
            "ayah_to": 1,
            "label": "Opening",
        }
        with tempfile.TemporaryDirectory() as tmp:
            out_dir = Path(tmp) / "package"
            out_dir.mkdir()
            write_bundles(out_dir, row)
            command = builder.build_command(
                row,
                out_dir,
                exclude_focus_trace=False,
                focus_trace_variant=None,
            )
            path = builder.write_manifest(
                row,
                out_dir,
                command=command,
                pericope_index=None,
                source="cli-span",
            )
            manifest = json.loads(path.read_text(encoding="utf-8"))

            manifest["command"][5] = "2"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaisesRegex(
                builder.package_manifest.PericopeManifestError, "command"
            ):
                builder.package_manifest.validate_manifest(
                    path,
                    repo_root=builder.REPO_ROOT,
                    expected_builder=builder.SCRIPT_PATH,
                    expected_lower_level_builder=(
                        builder.REPO_ROOT / "scripts" / "build_bundle.py"
                    ),
                )

            manifest["command"] = command
            manifest["generation_policy"]["package_scope"] = "surah"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaisesRegex(
                builder.package_manifest.PericopeManifestError, "policy"
            ):
                builder.package_manifest.validate_manifest(
                    path,
                    repo_root=builder.REPO_ROOT,
                    expected_builder=builder.SCRIPT_PATH,
                    expected_lower_level_builder=(
                        builder.REPO_ROOT / "scripts" / "build_bundle.py"
                    ),
                )

            index = Path(tmp) / "index.jsonl"
            index.write_text(
                json.dumps({**row, "label": "Different"}) + "\n",
                encoding="utf-8",
            )
            manifest["generation_policy"] = builder.package_manifest.generation_policy()
            manifest["source"] = "index"
            manifest["pericope_index"] = builder.package_manifest.file_record(
                index, builder.REPO_ROOT
            )
            path.write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaisesRegex(
                builder.package_manifest.PericopeManifestError, "matching the package"
            ):
                builder.package_manifest.validate_manifest(
                    path,
                    repo_root=builder.REPO_ROOT,
                    expected_builder=builder.SCRIPT_PATH,
                    expected_lower_level_builder=(
                        builder.REPO_ROOT / "scripts" / "build_bundle.py"
                    ),
                )

    def test_build_one_executes_builder_and_writes_validated_manifest(self) -> None:
        row = {
            "surah": 29,
            "pericope": 1,
            "ayah_from": 1,
            "ayah_to": 2,
            "label": "Opening",
        }
        with tempfile.TemporaryDirectory() as tmp:
            out_dir = Path(tmp) / "package"
            args = builder.parse_args([
                "--surah", "29",
                "--pericope", "1",
                "--ayah-from", "1",
                "--ayah-to", "2",
                "--pericope-label", "Opening",
                "--out", str(out_dir),
            ])

            def generate(_command: list[str], check: bool) -> None:
                self.assertTrue(check)
                out_dir.mkdir(parents=True)
                write_bundles(out_dir, row)

            with patch.object(builder.subprocess, "run", side_effect=generate) as run:
                result = builder.build_one(row, args)

            run.assert_called_once()
            manifest_path = Path(result["manifest"])
            self.assertTrue(manifest_path.is_file())
            self.assertEqual(result["ayah_count"], 2)


if __name__ == "__main__":
    unittest.main()
