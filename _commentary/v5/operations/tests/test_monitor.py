import argparse
import importlib.util
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = Path(__file__).resolve().parents[1] / "monitor.py"
SPEC = importlib.util.spec_from_file_location("commentary_v5_monitor", MODULE_PATH)
monitor = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = monitor
SPEC.loader.exec_module(monitor)


class ScopeTests(unittest.TestCase):
    def test_full_quran_has_6236_numbered_ayat(self):
        refs = monitor.expand_scope(["1-114"])
        self.assertEqual(6236, len(refs))
        self.assertEqual("1:1", refs[0])
        self.assertEqual("114:6", refs[-1])

    def test_scope_accepts_lists_and_deduplicates(self):
        self.assertEqual(
            ["29:38", "29:39", "30:1"],
            monitor.expand_scope(["29:38-39, 30:1", "29:38"]),
        )

    def test_scope_validates_ayah_bounds(self):
        with self.assertRaises(monitor.MonitorError):
            monitor.expand_scope(["114:7"])

    def test_prefatory_unit_is_explicit(self):
        self.assertEqual(["29:0"], monitor.expand_scope(["29:0"]))
        with self.assertRaises(monitor.MonitorError):
            monitor.expand_scope(["9:0"])


class SnapshotTests(unittest.TestCase):
    def test_snapshot_batches_writes_until_flush(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "snapshot.json"
            snapshot = monitor.LocalSnapshot(path)
            registration = registration_fixture()
            snapshot.register(registration)
            snapshot.upsert_task({"task_id": "task-1"})
            self.assertFalse(path.exists())
            snapshot.flush()
            value = json.loads(path.read_text(encoding="utf-8"))
            self.assertIn("task-1", value["tasks"])


class EventAndTaskTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.operations = self.root / "_commentary" / "v5" / "operations"
        self.v5 = self.operations.parent
        self.runtime = self.operations / "runtime"
        self.patches = [
            patch.object(monitor, "OPERATIONS_ROOT", self.operations),
            patch.object(monitor, "V5_ROOT", self.v5),
            patch.object(monitor, "REPO_ROOT", self.root),
            patch.object(monitor, "RUNTIME_ROOT", self.runtime),
            patch.object(monitor, "SNAPSHOT_PATH", self.runtime / "snapshot.json"),
        ]
        for item in self.patches:
            item.start()
        self.registration = registration_fixture()
        destination = monitor.registration_path("run-1", "orch-1")
        monitor._atomic_write_json(destination, self.registration)

    def tearDown(self):
        for item in reversed(self.patches):
            item.stop()
        self.temporary.cleanup()

    def test_event_is_appended_and_reduced(self):
        for status in ("started", "completed"):
            args = argparse.Namespace(
                run_id="run-1",
                orchestrator_id="orch-1",
                ayah_ref="29:38",
                role="scope",
                lane="micro",
                attempt=1,
                status=status,
                agent_id="agent-7",
                message=None,
            )
            self.assertEqual(0, monitor.command_event(args))
        task, _artifacts = monitor.build_task(self.registration, "29:38")
        self.assertEqual("completed", task["stages"]["micro"]["status"])
        self.assertEqual("agent-7", task["stages"]["micro"]["agent_id"])

    def test_new_attempt_is_not_hidden_by_old_artifact(self):
        artifact = self.v5 / "raw" / "native" / "s029" / "29_38" / "micro.scope.tr.md"
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_text("old", encoding="utf-8")
        os.utime(artifact, (100, 100))
        event = {
            "event": "started",
            "at": "2026-09-04T12:00:00Z",
            "role": "scope",
            "lane": "micro",
            "attempt": 2,
            "agent_id": "agent-8",
        }
        monitor._append_jsonl(
            monitor.event_path(self.registration, "29:38", "scope", "micro", 2),
            event,
        )
        task, _artifacts = monitor.build_task(self.registration, "29:38")
        self.assertEqual("active", task["stages"]["micro"]["status"])
        self.assertEqual(2, task["stages"]["micro"]["attempt"])

    def test_local_control_creates_and_removes_marker(self):
        for state in ("paused", "running"):
            args = argparse.Namespace(
                run_id="run-1", orchestrator_id="orch-1", state=state
            )
            self.assertEqual(0, monitor.command_control(args))
        self.assertFalse(monitor.control_marker(self.registration).exists())


def registration_fixture():
    return {
        "schema_version": "commentary-v5-orchestrator-registration-v1",
        "run_id": "run-1",
        "worker_id": "worker-1",
        "orchestrator_id": "orch-1",
        "agent_id": "agent-orch",
        "analysis_id": "native",
        "scope_selectors": ["29:38-39"],
        "scope_refs": ["29:38", "29:39"],
        "scope_count": 2,
        "started_at": "2026-09-04T11:00:00Z",
        "repo_root": "/repo",
        "poll_seconds": 10,
        "firebase_project_id": None,
    }


if __name__ == "__main__":
    unittest.main()
