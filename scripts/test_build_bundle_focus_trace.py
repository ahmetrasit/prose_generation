#!/usr/bin/env python3
"""Focused tests for Hermetic Focus Trace lookup policy."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import build_bundle as bb


class FocusTraceLookupTests(unittest.TestCase):
    def setUp(self) -> None:
        self._old_runs_dir = bb.FOCUS_TRACE_RUNS_DIR
        self._old_include = bb.INCLUDE_HERMETIC_FOCUS_TRACE
        self._old_require = bb.REQUIRE_HERMETIC_FOCUS_TRACE
        self._old_variant = bb.FOCUS_TRACE_VARIANT
        self.tmp = tempfile.TemporaryDirectory(
            prefix="focus-trace-test-",
            dir=bb.PROSE_GEN_ROOT,
        )
        self.addCleanup(self.tmp.cleanup)
        self.addCleanup(self._restore_globals)
        bb.FOCUS_TRACE_RUNS_DIR = Path(self.tmp.name) / "runs"
        bb.INCLUDE_HERMETIC_FOCUS_TRACE = True
        bb.REQUIRE_HERMETIC_FOCUS_TRACE = True
        bb.FOCUS_TRACE_VARIANT = None

    def _restore_globals(self) -> None:
        bb.FOCUS_TRACE_RUNS_DIR = self._old_runs_dir
        bb.INCLUDE_HERMETIC_FOCUS_TRACE = self._old_include
        bb.REQUIRE_HERMETIC_FOCUS_TRACE = self._old_require
        bb.FOCUS_TRACE_VARIANT = self._old_variant

    def _write_hft(
        self,
        run_name: str,
        *,
        surah: int = 12,
        ayah: int = 1,
        reader: str = "reader_hft_a",
        packet: bool = True,
        response: bool = True,
        packet_focus_ref: str | None = None,
        response_focus_ref: str | None = None,
        packet_body: object | None = None,
        response_body: object | None = None,
    ) -> None:
        run_dir = bb.FOCUS_TRACE_RUNS_DIR / run_name
        if packet:
            packet_path = run_dir / "packets" / f"{surah}_{ayah}.packet.json"
            packet_path.parent.mkdir(parents=True, exist_ok=True)
            packet_path.write_text(
                json.dumps(
                    packet_body
                    if packet_body is not None
                    else {
                        "protocol": "focus-trace-pericope-lean-v1",
                        "focus_ref": packet_focus_ref or f"{surah}:{ayah}",
                        "window": [f"{surah}:{ayah}"],
                        "ayah_count": 1,
                        "root_mappings": [],
                    }
                ),
                encoding="utf-8",
            )
        if response:
            response_path = (
                run_dir
                / "readers"
                / reader
                / f"{surah}_{ayah}.focus_trace.json"
            )
            response_path.parent.mkdir(parents=True, exist_ok=True)
            response_path.write_text(
                json.dumps(
                    response_body
                    if response_body is not None
                    else {
                        "protocol": "focus-trace-hermetic-response-v4",
                        "focus_ref": response_focus_ref or f"{surah}:{ayah}",
                        "baseline_models": [{}],
                        "context_deltas": [{}],
                        "surprising_valid_outliers": [{}],
                    }
                ),
                encoding="utf-8",
            )

    def test_padded_run_dir_is_usable(self) -> None:
        self._write_hft("s012")

        payload, coverage = bb.load_v12_focus_trace_hermetic(12, 1)

        self.assertTrue(coverage["present"])
        self.assertEqual(coverage["selected_run_dir"].split("/")[-1], "s012")
        self.assertIn("reader_hft_a", payload["readers"])

    def test_unpadded_run_dir_is_usable(self) -> None:
        self._write_hft("s12")

        payload, coverage = bb.load_v12_focus_trace_hermetic(12, 1)

        self.assertTrue(coverage["present"])
        self.assertEqual(coverage["selected_run_dir"].split("/")[-1], "s12")
        self.assertIn("reader_hft_a", payload["readers"])

    def test_both_run_dirs_for_same_ayah_are_ambiguous(self) -> None:
        self._write_hft("s012")
        self._write_hft("s12")

        _payload, coverage = bb.load_v12_focus_trace_hermetic(12, 1)

        self.assertFalse(coverage["present"])
        self.assertIn("ambiguous", coverage["note"])
        self.assertEqual(len(coverage["active_run_dirs"]), 2)

    def test_missing_hft_records_all_checked_dirs(self) -> None:
        _payload, coverage = bb.load_v12_focus_trace_hermetic(12, 1)

        self.assertFalse(coverage["present"])
        self.assertIn("s012", " ".join(coverage["run_dirs_checked"]))
        self.assertIn("s12", " ".join(coverage["run_dirs_checked"]))

    def test_reader_without_packet_is_unusable(self) -> None:
        self._write_hft("s12", packet=False, response=True)

        _payload, coverage = bb.load_v12_focus_trace_hermetic(12, 1)

        self.assertFalse(coverage["present"])
        self.assertIn("packet is missing", coverage["note"])

    def test_packet_focus_ref_mismatch_is_unusable(self) -> None:
        self._write_hft("s12", packet_focus_ref="12:2")

        _payload, coverage = bb.load_v12_focus_trace_hermetic(12, 1)

        self.assertFalse(coverage["present"])
        self.assertIn("packet focus_ref", coverage["note"])

    def test_malformed_packet_shape_is_controlled_failure(self) -> None:
        self._write_hft("s12", packet_body=["not", "an", "object"])

        _payload, coverage = bb.load_v12_focus_trace_hermetic(12, 1)

        self.assertFalse(coverage["present"])
        self.assertIn("packet JSON must be an object", coverage["note"])

    def test_malformed_packet_root_mappings_is_controlled_failure(self) -> None:
        self._write_hft(
            "s12",
            packet_body={
                "protocol": "focus-trace-pericope-lean-v1",
                "focus_ref": "12:1",
                "root_mappings": 1,
            },
        )

        _payload, coverage = bb.load_v12_focus_trace_hermetic(12, 1)

        self.assertFalse(coverage["present"])
        self.assertIn("packet root_mappings must be a list", coverage["note"])

    def test_falsey_packet_root_mappings_is_controlled_failure(self) -> None:
        self._write_hft(
            "s12",
            packet_body={
                "protocol": "focus-trace-pericope-lean-v1",
                "focus_ref": "12:1",
                "root_mappings": None,
            },
        )

        _payload, coverage = bb.load_v12_focus_trace_hermetic(12, 1)

        self.assertFalse(coverage["present"])
        self.assertIn("packet root_mappings must be a list", coverage["note"])

    def test_invalid_reader_fails_even_with_another_valid_reader(self) -> None:
        self._write_hft("s12", reader="reader_hft_a")
        response_path = (
            bb.FOCUS_TRACE_RUNS_DIR
            / "s12"
            / "readers"
            / "reader_hft_b"
            / "12_1.focus_trace.json"
        )
        response_path.parent.mkdir(parents=True, exist_ok=True)
        response_path.write_text("{", encoding="utf-8")

        _payload, coverage = bb.load_v12_focus_trace_hermetic(12, 1)

        self.assertFalse(coverage["present"])
        self.assertIn("reader files are malformed", coverage["note"])
        self.assertEqual(coverage["valid_reader_count"], 1)

    def test_non_object_reader_json_fails_even_with_valid_reader(self) -> None:
        self._write_hft("s12", reader="reader_hft_a")
        self._write_hft("s12", reader="reader_hft_b", response_body=[])

        _payload, coverage = bb.load_v12_focus_trace_hermetic(12, 1)

        self.assertFalse(coverage["present"])
        self.assertIn("reader JSON must be an object", coverage["note"])
        self.assertEqual(coverage["valid_reader_count"], 1)

    def test_reader_focus_ref_mismatch_fails_even_with_valid_reader(self) -> None:
        self._write_hft("s12", reader="reader_hft_a")
        self._write_hft("s12", reader="reader_hft_b", response_focus_ref="12:2")

        _payload, coverage = bb.load_v12_focus_trace_hermetic(12, 1)

        self.assertFalse(coverage["present"])
        self.assertIn("focus_ref '12:2' does not match 12:1", coverage["note"])
        self.assertEqual(coverage["valid_reader_count"], 1)

    def test_exclude_focus_trace_is_explicit_in_coverage(self) -> None:
        bb.INCLUDE_HERMETIC_FOCUS_TRACE = False
        bb.REQUIRE_HERMETIC_FOCUS_TRACE = False

        _payload, coverage = bb.load_v12_focus_trace_hermetic(12, 1)

        self.assertFalse(coverage["present"])
        self.assertTrue(coverage["excluded"])
        self.assertIn("--exclude-focus-trace", coverage["note"])


if __name__ == "__main__":
    unittest.main()
