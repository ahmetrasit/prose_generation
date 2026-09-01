from __future__ import annotations

import io
import json
import math
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch


V3_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(V3_ROOT))

import render_authoring  # noqa: E402
from v3lib.common import ValidationError  # noqa: E402


class RenderAuthoringTests(unittest.TestCase):
    def test_load_object_rejects_duplicate_keys(self) -> None:
        with tempfile.TemporaryDirectory(dir=V3_ROOT) as temp_dir:
            path = Path(temp_dir) / "duplicate.json"
            path.write_text('{"status":"first","status":"second"}', encoding="utf-8")
            with self.assertRaisesRegex(ValidationError, "duplicate JSON object key"):
                render_authoring._load_object(path)

    def test_canonical_json_rejects_nonfinite_numbers(self) -> None:
        with self.assertRaisesRegex(ValidationError, "not canonical JSON"):
            render_authoring._canonical_json({"value": math.nan})

    def test_cli_reports_workflow_system_exit_as_json_error(self) -> None:
        stderr = io.StringIO()
        stdout = io.StringIO()
        with (
            patch.object(
                sys,
                "argv",
                ["render_authoring.py", "scopes", "--ayah", "not-an-ayah"],
            ),
            redirect_stdout(stdout),
            redirect_stderr(stderr),
        ):
            code = render_authoring.main()
        self.assertEqual(code, 2)
        self.assertEqual(stdout.getvalue(), "")
        error = json.loads(stderr.getvalue())
        self.assertEqual(error["status"], "error")
        self.assertEqual(error["error_type"], "SystemExit")
        self.assertIn("Invalid ayah reference", error["message"])

    def test_mixed_guard_lineage_is_documented_as_stop_state(self) -> None:
        text = (V3_ROOT / "ORCHESTRATION.md").read_text(encoding="utf-8")
        self.assertIn("canonical_workspace_guard_status: mixed_guard_lineage", text)
        self.assertIn("stop and report it", text)


if __name__ == "__main__":
    unittest.main()
