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

    def test_replacing_artifacts_removes_deleted_content(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "snapshot.json"
            snapshot = monitor.LocalSnapshot(path)
            task = {"task_id": "task-1"}
            snapshot.replace_artifacts(task, [{"kind": "micro", "content": "old"}])
            snapshot.flush()
            value = json.loads(path.read_text(encoding="utf-8"))
            self.assertNotIn("content", value["artifacts"]["task-1"]["micro"])
            snapshot.replace_artifacts(task, [])
            snapshot.flush()
            value = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual({}, value["artifacts"]["task-1"])


class FirebaseRestTests(unittest.TestCase):
    def test_firestore_document_round_trip(self):
        value = {
            "name": "monitor",
            "count": 3,
            "active": True,
            "empty": None,
            "stages": {"micro": {"status": "active"}},
            "refs": ["1:1", "1:2"],
        }
        encoded = monitor._firestore_document(value)
        self.assertEqual(value, monitor._from_firestore_document(encoded))

    def test_public_registration_removes_bearer_hash(self):
        registration = registration_fixture()
        registration["firebase_passcode_hash"] = "a" * 64
        public = monitor.public_registration(registration)
        self.assertNotIn("firebase_passcode_hash", public)

    def test_unchanged_control_does_not_repeat_remote_write(self):
        sink = monitor.FirebaseRestSink("v5-monitor", "public-key", "a" * 64)
        registration = registration_fixture()
        with (
            patch.object(sink, "_get", return_value={"desired_state": "paused"}),
            patch.object(sink, "_write") as write,
        ):
            self.assertEqual("paused", sink.desired_state(registration))
            self.assertEqual("paused", sink.desired_state(registration))
        self.assertEqual(1, write.call_count)


class FailingArtifactSink:
    def __init__(self):
        self.artifact_calls = 0

    def register(self, _registration):
        return "running"

    def desired_state(self, _registration):
        return None

    def heartbeat(self, _registration, _at):
        return None

    def upsert_task(self, _task):
        return None

    def upsert_artifact(self, _task, _artifact):
        self.artifact_calls += 1
        if self.artifact_calls == 1:
            raise RuntimeError("temporary")

    def close(self, _registration, _at):
        return None


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
        artifact = self.v5 / "raw" / "native" / "s029" / "29_38" / "micro.scope.tr.md"
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_text("complete", encoding="utf-8")
        task, _artifacts = monitor.build_task(self.registration, "29:38")
        self.assertEqual("completed", task["stages"]["micro"]["status"])
        self.assertEqual("agent-7", task["stages"]["micro"]["agent_id"])

    def test_attempts_are_allocated_and_matched_automatically(self):
        def write(status, agent_id):
            return monitor.command_event(
                argparse.Namespace(
                    run_id="run-1",
                    orchestrator_id="orch-1",
                    ayah_ref="29:38",
                    role="scope",
                    lane="macro",
                    attempt=None,
                    status=status,
                    agent_id=agent_id,
                    message=None,
                )
            )

        self.assertEqual(0, write("started", "agent-1"))
        self.assertEqual(0, write("failed", "agent-1"))
        self.assertEqual(0, write("started", "agent-2"))
        self.assertEqual(0, write("completed", "agent-2"))
        artifact = self.v5 / "raw" / "native" / "s029" / "29_38" / "macro.scope.tr.md"
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_text("complete", encoding="utf-8")
        task, _artifacts = monitor.build_task(self.registration, "29:38")
        self.assertEqual(2, task["stages"]["macro"]["attempt"])
        self.assertEqual("completed", task["stages"]["macro"]["status"])

    def test_parallel_starts_get_distinct_attempts(self):
        common = {
            "run_id": "run-1",
            "orchestrator_id": "orch-1",
            "ayah_ref": "29:38",
            "role": "scope",
            "lane": "global",
            "attempt": None,
            "status": "started",
            "message": None,
        }
        monitor.command_event(argparse.Namespace(**common, agent_id="agent-1"))
        monitor.command_event(argparse.Namespace(**common, agent_id="agent-2"))
        first = monitor.event_path(self.registration, "29:38", "scope", "global", 1)
        second = monitor.event_path(self.registration, "29:38", "scope", "global", 2)
        self.assertTrue(first.exists())
        self.assertTrue(second.exists())

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

    def test_prompt_files_alone_leave_task_pending(self):
        prompt = self.v5 / "input" / "native" / "s029" / "29_38" / "micro.discovery.prompt.md"
        prompt.parent.mkdir(parents=True, exist_ok=True)
        prompt.write_text("prepared", encoding="utf-8")
        task, _artifacts = monitor.build_task(self.registration, "29:38")
        self.assertEqual("pending", task["status"])
        self.assertEqual("ready", task["stages"]["micro"]["status"])

    def test_later_old_attempt_does_not_override_new_attempt(self):
        directory = monitor.event_path(
            self.registration, "29:38", "scope", "micro", 1
        ).parent
        directory.mkdir(parents=True, exist_ok=True)
        monitor._append_jsonl(
            directory / "micro.002.jsonl",
            {
                "event": "started",
                "at": "2026-09-04T12:00:00Z",
                "role": "scope",
                "lane": "micro",
                "attempt": 2,
                "agent_id": "agent-2",
            },
        )
        monitor._append_jsonl(
            directory / "micro.001.jsonl",
            {
                "event": "failed",
                "at": "2026-09-04T13:00:00Z",
                "role": "scope",
                "lane": "micro",
                "attempt": 1,
                "agent_id": "agent-1",
            },
        )
        task, _artifacts = monitor.build_task(self.registration, "29:38")
        self.assertEqual(2, task["stages"]["micro"]["attempt"])
        self.assertEqual("active", task["stages"]["micro"]["status"])

    def test_failure_is_not_hidden_by_artifact(self):
        artifact = self.v5 / "raw" / "native" / "s029" / "29_38" / "global.scope.tr.md"
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_text("partial", encoding="utf-8")
        monitor._append_jsonl(
            monitor.event_path(self.registration, "29:38", "scope", "global", 1),
            {
                "event": "failed",
                "at": "2026-09-04T13:00:00Z",
                "role": "scope",
                "lane": "global",
                "attempt": 1,
                "agent_id": "agent-1",
            },
        )
        task, _artifacts = monitor.build_task(self.registration, "29:38")
        self.assertEqual("failed", task["stages"]["global"]["status"])
        self.assertEqual("failed", task["status"])

    def test_canonical_completion_implies_validation(self):
        artifact = (
            self.v5
            / "editorial"
            / "native"
            / "s029"
            / "29_38"
            / "29_38.prose.editorial.tr.md"
        )
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_text("editorial", encoding="utf-8")
        monitor._append_jsonl(
            monitor.event_path(self.registration, "29:38", "canonical", None, 1),
            {
                "event": "completed",
                "at": "2026-09-04T13:00:00Z",
                "role": "canonical",
                "lane": None,
                "attempt": 1,
                "agent_id": "agent-c",
            },
        )
        task, _artifacts = monitor.build_task(self.registration, "29:38")
        self.assertEqual("passed", task["stages"]["validator"]["status"])
        self.assertEqual("completed", task["status"])

    def test_local_control_creates_and_removes_marker(self):
        for state in ("paused", "running"):
            args = argparse.Namespace(
                run_id="run-1", orchestrator_id="orch-1", state=state
            )
            self.assertEqual(0, monitor.command_control(args))
        self.assertFalse(monitor.control_marker(self.registration).exists())

    def test_failed_remote_artifact_is_retried(self):
        artifact = self.v5 / "raw" / "native" / "s029" / "29_38" / "micro.scope.tr.md"
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_text("retry", encoding="utf-8")
        sink = FailingArtifactSink()
        daemon = monitor.Monitor(
            self.registration,
            interval=10,
            heartbeat_interval=60,
            firebase=sink,
        )
        daemon.sync_ref("29:38")
        self.assertIn("29:38", daemon.pending_refs)
        self.assertEqual({}, daemon.synced_artifacts)
        daemon.sync_ref("29:38")
        self.assertNotIn("29:38", daemon.pending_refs)
        self.assertEqual(2, sink.artifact_calls)


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
