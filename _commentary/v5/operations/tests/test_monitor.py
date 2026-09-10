import argparse
import importlib.util
import json
import os
import sys
import tempfile
import time
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

    def test_registration_creates_run_index_for_session_discovery(self):
        sink = monitor.FirebaseRestSink("v5-monitor", "public-key", "a" * 64)
        registration = registration_fixture()
        with (
            patch.object(sink, "_read_control_state", return_value=None),
            patch.object(sink, "_write") as write,
        ):
            self.assertEqual("running", sink.register(registration))
        self.assertEqual("runs/run-1", write.call_args_list[0].args[0])
        self.assertEqual("run-1", write.call_args_list[0].args[1]["run_id"])


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

    def test_attention_closes_attempt_for_terminal_matching(self):
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
        self.assertEqual(0, write("attention", "agent-1"))
        self.assertEqual(0, write("started", "agent-2"))
        first = monitor.event_path(self.registration, "29:38", "scope", "macro", 1)
        second = monitor.event_path(self.registration, "29:38", "scope", "macro", 2)
        self.assertTrue(first.exists())
        self.assertTrue(second.exists())

    def test_terminal_event_never_closes_another_agents_attempt(self):
        started = argparse.Namespace(
            run_id="run-1",
            orchestrator_id="orch-1",
            ayah_ref="29:38",
            role="scope",
            lane="macro",
            attempt=None,
            status="started",
            agent_id="agent-1",
            message=None,
        )
        monitor.command_event(started)
        with self.assertRaisesRegex(monitor.MonitorError, "another agent"):
            monitor.command_event(
                argparse.Namespace(
                    **{
                        **vars(started),
                        "status": "completed",
                        "agent_id": "agent-2",
                    }
                )
            )

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

    def test_old_artifact_cannot_complete_a_later_attempt(self):
        artifact = self.v5 / "raw" / "native" / "s029" / "29_38" / "micro.scope.tr.md"
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_text("old", encoding="utf-8")
        os.utime(artifact, (100, 100))
        destination = monitor.event_path(
            self.registration, "29:38", "scope", "micro", 2
        )
        for event in ("started", "completed"):
            monitor._append_jsonl(
                destination,
                {
                    "event": event,
                    "at": (
                        "2026-09-04T12:00:00.100000Z"
                        if event == "started"
                        else "2026-09-04T12:00:01Z"
                    ),
                    "role": "scope",
                    "lane": "micro",
                    "attempt": 2,
                    "agent_id": "agent-8",
                },
            )
        task, _artifacts = monitor.build_task(self.registration, "29:38")
        self.assertEqual("attention", task["stages"]["micro"]["status"])

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

    def test_new_run_waits_for_required_invitation(self):
        self.registration["invitation_required"] = True
        editorial = (
            self.v5 / "editorial" / "native" / "s029" / "29_38"
            / "29_38.prose.editorial.tr.md"
        )
        editorial.parent.mkdir(parents=True, exist_ok=True)
        editorial.write_text("editorial", encoding="utf-8")
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
        self.assertEqual("pending", task["stages"]["invitation"]["status"])
        self.assertEqual("active", task["status"])

    def test_required_invitation_completion_finishes_task(self):
        self.registration["invitation_required"] = True
        editorial_dir = self.v5 / "editorial" / "native" / "s029" / "29_38"
        editorial_dir.mkdir(parents=True, exist_ok=True)
        (editorial_dir / "29_38.prose.editorial.tr.md").write_text(
            "editorial", encoding="utf-8"
        )
        invitation = editorial_dir / "29_38.invitation.tr.md"
        invitation.write_text("invitation", encoding="utf-8")
        for role, agent_id in (("canonical", "agent-c"), ("invitation", "agent-i")):
            monitor._append_jsonl(
                monitor.event_path(self.registration, "29:38", role, None, 1),
                {
                    "event": "completed",
                    "at": "2026-09-04T13:00:00Z",
                    "role": role,
                    "lane": None,
                    "attempt": 1,
                    "agent_id": agent_id,
                },
            )

        task, artifacts = monitor.build_task(self.registration, "29:38")

        self.assertEqual("completed", task["stages"]["invitation"]["status"])
        self.assertEqual("completed", task["status"])
        self.assertIn("invitation", {item["kind"] for item in artifacts})

    def test_editorial_artifact_without_event_does_not_imply_validation(self):
        artifact = (
            self.v5
            / "editorial"
            / "native"
            / "s029"
            / "29_38"
            / "29_38.prose.editorial.tr.md"
        )
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_text("", encoding="utf-8")

        task, _artifacts = monitor.build_task(self.registration, "29:38")

        self.assertEqual("editing", task["stages"]["canonical"]["status"])
        self.assertEqual("pending", task["stages"]["validator"]["status"])
        self.assertEqual("active", task["status"])

    def test_local_control_creates_and_removes_marker(self):
        for state in ("paused", "running"):
            args = argparse.Namespace(
                run_id="run-1", orchestrator_id="orch-1", state=state
            )
            self.assertEqual(0, monitor.command_control(args))
        self.assertFalse(monitor.control_marker(self.registration).exists())

    def test_check_reports_pause_without_waiting(self):
        args = argparse.Namespace(run_id="run-1", orchestrator_id="orch-1")
        monitor._atomic_write_text(
            monitor.control_marker(self.registration), "paused_at=test\n"
        )
        started = time.monotonic()
        self.assertEqual(0, monitor.command_check(args))
        self.assertLess(time.monotonic() - started, 0.5)

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

    def test_start_verifies_remote_registration_before_spawning(self):
        args = argparse.Namespace(
            run_id="run-2",
            worker_id="worker-2",
            orchestrator_id="orch-2",
            agent_id="agent-orch",
            analysis_id="native",
            scope=["29:38"],
            poll_seconds=10,
            firebase_project="v5-monitor",
            firebase_api_key="public-key",
            passcode="abcdefghijkl",
            local_only=False,
        )
        with (
            patch.object(
                monitor.FirebaseRestSink,
                "register",
                side_effect=monitor.MonitorError("revoked passcode"),
            ) as register,
            patch.object(monitor.subprocess, "Popen") as popen,
        ):
            with self.assertRaisesRegex(monitor.MonitorError, "revoked passcode"):
                monitor.command_start(args)
        register.assert_called_once()
        popen.assert_not_called()

    def test_start_mirrors_initial_remote_pause_before_spawning(self):
        args = argparse.Namespace(
            run_id="run-paused",
            worker_id="worker-paused",
            orchestrator_id="orch-paused",
            agent_id="agent-orch",
            analysis_id="native",
            scope=["29:38"],
            poll_seconds=10,
            firebase_project="v5-monitor",
            firebase_api_key="public-key",
            passcode="abcdefghijkl",
            local_only=False,
        )
        process = argparse.Namespace(pid=9876)
        with (
            patch.object(monitor.FirebaseRestSink, "register", return_value="paused"),
            patch.object(monitor.subprocess, "Popen", return_value=process),
        ):
            self.assertEqual(0, monitor.command_start(args))
        registration = monitor.load_registration(
            monitor.registration_path("run-paused", "orch-paused")
        )
        self.assertTrue(monitor.control_marker(registration).exists())

    def test_duplicate_start_is_refused_without_spawning(self):
        args = argparse.Namespace(
            run_id="run-1",
            worker_id="worker-1",
            orchestrator_id="orch-1",
            agent_id="agent-orch",
            analysis_id="native",
            scope=["29:38"],
            poll_seconds=10,
            firebase_project=None,
            firebase_api_key=None,
            passcode=None,
            local_only=True,
        )
        monitor._atomic_write_text(monitor._pid_path(self.registration), "1234\n")
        with (
            patch.object(monitor, "_process_exists", return_value=True),
            patch.object(monitor.subprocess, "Popen") as popen,
        ):
            with self.assertRaisesRegex(monitor.MonitorError, "already running"):
                monitor.command_start(args)
        popen.assert_not_called()

    def test_failed_rerun_spawn_gets_a_new_attention_attempt(self):
        destination = monitor.event_path(
            self.registration, "29:38", "scope", "global", 1
        )
        for event in ("started", "failed"):
            monitor._append_jsonl(
                destination,
                {
                    "event": event,
                    "at": "2026-09-04T12:00:00Z",
                    "role": "scope",
                    "lane": "global",
                    "attempt": 1,
                    "agent_id": "agent-1",
                },
            )
        args = argparse.Namespace(
            run_id="run-1",
            orchestrator_id="orch-1",
            ayah_ref="29:38",
            role="scope",
            lane="global",
            attempt=None,
            status="attention",
            agent_id="agent-2",
            message="Spawn failed",
        )
        self.assertEqual(0, monitor.command_event(args))
        self.assertTrue(
            monitor.event_path(
                self.registration, "29:38", "scope", "global", 2
            ).exists()
        )

    def test_stop_requests_cooperative_final_sync(self):
        self.registration["run_id"] = "run-stop"
        self.registration["orchestrator_id"] = "orch-stop"
        destination = monitor.registration_path("run-stop", "orch-stop")
        monitor._atomic_write_json(destination, self.registration)
        pid_path = monitor._pid_path(self.registration)
        monitor._atomic_write_text(pid_path, "1234\n")
        args = argparse.Namespace(
            run_id="run-stop", orchestrator_id="orch-stop", timeout_seconds=1
        )

        def fake_exists(_pid):
            if monitor.stop_marker(self.registration).exists():
                pid_path.unlink(missing_ok=True)
                return False
            return True

        with patch.object(monitor, "_process_exists", side_effect=fake_exists) as exists:
            self.assertEqual(0, monitor.command_stop(args))
        self.assertGreaterEqual(exists.call_count, 2)
        self.assertFalse(monitor.stop_marker(self.registration).exists())

    def test_stop_returns_after_wait_window_while_final_sync_continues(self):
        self.registration["run_id"] = "run-stop-pending"
        self.registration["orchestrator_id"] = "orch-stop-pending"
        destination = monitor.registration_path(
            "run-stop-pending", "orch-stop-pending"
        )
        monitor._atomic_write_json(destination, self.registration)
        pid_path = monitor._pid_path(self.registration)
        monitor._atomic_write_text(pid_path, "1234\n")
        args = argparse.Namespace(
            run_id="run-stop-pending",
            orchestrator_id="orch-stop-pending",
            timeout_seconds=0,
        )

        with patch.object(monitor, "_process_exists", return_value=True):
            self.assertEqual(0, monitor.command_stop(args))

        self.assertTrue(pid_path.exists())
        self.assertTrue(monitor.stop_marker(self.registration).exists())

    def test_local_stop_marker_interrupts_long_poll_sleep(self):
        daemon = monitor.Monitor(
            self.registration,
            interval=30,
            heartbeat_interval=60,
            firebase=None,
        )
        monitor._atomic_write_text(
            monitor.stop_marker(self.registration), "stop_requested_at=test\n"
        )
        started = time.monotonic()
        daemon._sleep_until_next_tick()
        self.assertLess(time.monotonic() - started, 0.5)

    def test_daemon_retries_pending_upload_before_cooperative_stop(self):
        artifact = self.v5 / "raw" / "native" / "s029" / "29_38" / "micro.scope.tr.md"
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_text("retry", encoding="utf-8")
        sink = FailingArtifactSink()
        daemon = monitor.Monitor(
            self.registration,
            interval=0,
            heartbeat_interval=60,
            firebase=sink,
        )
        monitor._atomic_write_text(
            monitor.stop_marker(self.registration), "stop_requested_at=test\n"
        )
        daemon.run()
        self.assertEqual(2, sink.artifact_calls)
        self.assertEqual(set(), daemon.pending_refs)

    def test_daemon_stops_after_bounded_failed_final_syncs(self):
        artifact = self.v5 / "raw" / "native" / "s029" / "29_38" / "micro.scope.tr.md"
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_text("retry", encoding="utf-8")
        sink = FailingArtifactSink()

        def always_fail(_task, _artifact):
            sink.artifact_calls += 1
            raise RuntimeError("still unavailable")

        sink.upsert_artifact = always_fail
        daemon = monitor.Monitor(
            self.registration,
            interval=0,
            heartbeat_interval=60,
            firebase=sink,
        )
        monitor._atomic_write_text(
            monitor.stop_marker(self.registration), "stop_requested_at=test\n"
        )

        daemon.run()

        self.assertEqual(monitor.MAX_STOP_SYNC_ATTEMPTS, sink.artifact_calls)
        self.assertEqual({"29:38"}, daemon.pending_refs)

    def test_load_registration_rejects_invalid_scope_count(self):
        path = monitor.registration_path("run-bad", "orch-bad")
        invalid = {**self.registration, "run_id": "run-bad", "orchestrator_id": "orch-bad"}
        invalid["scope_count"] = 99
        monitor._atomic_write_json(path, invalid)
        with self.assertRaisesRegex(monitor.MonitorError, "scope_count"):
            monitor.load_registration(path)


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
