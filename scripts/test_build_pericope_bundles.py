#!/usr/bin/env python3

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import build_pericope_bundles as builder


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
            (out_dir / "29_1.ayah.json").write_text('{"ayahRef":"29:1"}', encoding="utf-8")
            (out_dir / "29_2.ayah.json").write_text('{"ayahRef":"29:2"}', encoding="utf-8")
            with patch.object(builder, "REPO_ROOT", Path(tmp)):
                path = builder.write_manifest(
                    row,
                    out_dir,
                    command=["python3", "scripts/build_bundle.py"],
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


if __name__ == "__main__":
    unittest.main()
