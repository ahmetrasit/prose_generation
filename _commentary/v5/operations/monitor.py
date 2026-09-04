#!/usr/bin/env python3
"""Local monitor and control bridge for commentary V5 orchestration."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import signal
import socket
import subprocess
import sys
import tempfile
import time
import uuid
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Iterable, Protocol


OPERATIONS_ROOT = Path(__file__).resolve().parent
V5_ROOT = OPERATIONS_ROOT.parent
REPO_ROOT = V5_ROOT.parents[1]
RUNTIME_ROOT = OPERATIONS_ROOT / "runtime"
SNAPSHOT_PATH = RUNTIME_ROOT / "snapshot.json"
ID_RE = re.compile(r"[A-Za-z0-9](?:[A-Za-z0-9._-]{0,127})")
AYAH_SELECTOR_RE = re.compile(
    r"([1-9][0-9]*):(0|[1-9][0-9]*)(?:-([1-9][0-9]*))?"
)
SURAH_SELECTOR_RE = re.compile(r"([1-9][0-9]*)(?:-([1-9][0-9]*))?")
UNIT_DIR_RE = re.compile(r"([1-9][0-9]*)_(0|[1-9][0-9]*)")
TERMINAL_EVENTS = frozenset({"completed", "failed", "interrupted"})
EVENTS = frozenset({"started", *TERMINAL_EVENTS, "attention"})
ROLES = frozenset({"scope", "canonical", "validator", "orchestrator"})
LANES = ("micro", "macro", "global")
MAX_ARTIFACT_BYTES = 900_000

# Numbered ayat by surah. Prefatory basmalas are selected explicitly as S:0.
QURAN_AYAH_COUNTS = (
    7, 286, 200, 176, 120, 165, 206, 75, 129, 109,
    123, 111, 43, 52, 99, 128, 111, 110, 98, 135,
    112, 78, 118, 64, 77, 227, 93, 88, 69, 60,
    34, 30, 73, 54, 45, 83, 182, 88, 75, 85,
    54, 53, 89, 59, 37, 35, 38, 29, 18, 45,
    60, 49, 62, 55, 78, 96, 29, 22, 24, 13,
    14, 11, 11, 18, 12, 12, 30, 52, 52, 44,
    28, 28, 20, 56, 40, 31, 50, 40, 46, 42,
    29, 19, 36, 25, 22, 17, 19, 26, 30, 20,
    15, 21, 11, 8, 8, 19, 5, 8, 8, 11,
    11, 8, 3, 9, 5, 4, 7, 3, 6, 3,
    5, 4, 5, 6,
)


class MonitorError(RuntimeError):
    """Raised when operational input is unsafe or inconsistent."""


def utc_now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def validate_id(value: str, label: str) -> str:
    if ID_RE.fullmatch(value) is None:
        raise MonitorError(f"Invalid {label}: {value!r}")
    return value


def _atomic_write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        dir=path.parent, prefix=f".{path.name}.", suffix=".tmp"
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def _atomic_write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        dir=path.parent, prefix=f".{path.name}.", suffix=".tmp"
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(value)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def _scope_tokens(values: Iterable[str]) -> list[str]:
    tokens: list[str] = []
    for value in values:
        tokens.extend(item for item in re.split(r"[\s,]+", value.strip()) if item)
    return tokens


def expand_scope(values: Iterable[str]) -> list[str]:
    """Expand S, S-T, S:A, and S:A-B selectors into unique Quran refs."""
    refs: list[str] = []
    seen: set[str] = set()
    for token in _scope_tokens(values):
        ayah_match = AYAH_SELECTOR_RE.fullmatch(token)
        if ayah_match is not None:
            surah = int(ayah_match.group(1))
            first = int(ayah_match.group(2))
            last = int(ayah_match.group(3) or first)
            if not 1 <= surah <= len(QURAN_AYAH_COUNTS):
                raise MonitorError(f"Surah is outside 1-114: {token}")
            if first == 0 and last != 0:
                raise MonitorError(f"A prefatory unit cannot begin a range: {token}")
            if last < first or last > QURAN_AYAH_COUNTS[surah - 1]:
                raise MonitorError(f"Ayah range is invalid for S{surah}: {token}")
            if first == 0 and surah in {1, 9}:
                raise MonitorError(f"Invalid prefatory unit: {token}")
            selected = (f"{surah}:{ayah}" for ayah in range(first, last + 1))
        else:
            surah_match = SURAH_SELECTOR_RE.fullmatch(token)
            if surah_match is None:
                raise MonitorError(f"Invalid scope selector: {token!r}")
            first_surah = int(surah_match.group(1))
            last_surah = int(surah_match.group(2) or first_surah)
            if not 1 <= first_surah <= last_surah <= len(QURAN_AYAH_COUNTS):
                raise MonitorError(f"Surah range is outside 1-114: {token}")
            selected = (
                f"{surah}:{ayah}"
                for surah in range(first_surah, last_surah + 1)
                for ayah in range(1, QURAN_AYAH_COUNTS[surah - 1] + 1)
            )
        for ref in selected:
            if ref not in seen:
                refs.append(ref)
                seen.add(ref)
    if not refs:
        raise MonitorError("At least one scope selector is required")
    return refs


def ref_parts(ayah_ref: str) -> tuple[int, int]:
    match = re.fullmatch(r"([1-9][0-9]*):(0|[1-9][0-9]*)", ayah_ref)
    if match is None:
        raise MonitorError(f"Invalid ayah ref: {ayah_ref!r}")
    return int(match.group(1)), int(match.group(2))


def unit_key(ayah_ref: str) -> str:
    surah, ayah = ref_parts(ayah_ref)
    return f"s{surah:03d}-a{ayah:03d}"


def registration_path(run_id: str, orchestrator_id: str) -> Path:
    return (
        RUNTIME_ROOT
        / "runs"
        / validate_id(run_id, "run ID")
        / "orchestrators"
        / validate_id(orchestrator_id, "orchestrator ID")
        / "registration.json"
    )


def control_marker(registration: dict[str, Any]) -> Path:
    return (
        RUNTIME_ROOT
        / "control"
        / registration["worker_id"]
        / registration["orchestrator_id"]
        / "PAUSE"
    )


def event_path(
    registration: dict[str, Any], ayah_ref: str, role: str, lane: str | None, attempt: int
) -> Path:
    surah, ayah = ref_parts(ayah_ref)
    task = lane if role == "scope" else role
    return (
        registration_path(
            registration["run_id"], registration["orchestrator_id"]
        ).parent
        / "events"
        / f"s{surah:03d}"
        / f"{surah}_{ayah}"
        / f"{task}.{attempt:03d}.jsonl"
    )


def _append_jsonl(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n"
    with path.open("a", encoding="utf-8") as handle:
        try:
            import fcntl

            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        except ImportError:
            pass
        handle.write(line)
        handle.flush()
        os.fsync(handle.fileno())
        try:
            import fcntl

            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        except ImportError:
            pass


def load_registration(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise MonitorError(f"Cannot read registration {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise MonitorError(f"Registration is not a JSON object: {path}")
    required = {
        "run_id",
        "worker_id",
        "orchestrator_id",
        "analysis_id",
        "scope_refs",
    }
    missing = sorted(required - set(value))
    if missing:
        raise MonitorError(f"Registration is missing fields: {missing}")
    return value


class RemoteSink(Protocol):
    def register(self, registration: dict[str, Any]) -> str: ...

    def desired_state(self, registration: dict[str, Any]) -> str | None: ...

    def heartbeat(self, registration: dict[str, Any], at: str) -> None: ...

    def upsert_task(self, task: dict[str, Any]) -> None: ...

    def upsert_artifact(self, task: dict[str, Any], artifact: dict[str, Any]) -> None: ...

    def close(self, registration: dict[str, Any], at: str) -> None: ...


class LocalSnapshot:
    """A browser-readable mirror used for local operation and recovery."""

    def __init__(self, path: Path | None = None) -> None:
        self.path = path or SNAPSHOT_PATH
        self.dirty = False
        self.dirty_keys: dict[str, set[str]] = {
            "workers": set(),
            "orchestrators": set(),
            "tasks": set(),
            "artifacts": set(),
        }
        self.value: dict[str, Any] = {
            "schema_version": "commentary-v5-operations-snapshot-v1",
            "generated_at": utc_now(),
            "workers": {},
            "orchestrators": {},
            "tasks": {},
            "artifacts": {},
        }
        if self.path.exists():
            try:
                existing = json.loads(self.path.read_text(encoding="utf-8"))
                if isinstance(existing, dict):
                    self.value.update(existing)
            except (OSError, json.JSONDecodeError):
                pass

    def flush(self) -> None:
        if not self.dirty:
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        lock_path = self.path.with_suffix(f"{self.path.suffix}.lock")
        with lock_path.open("a", encoding="utf-8") as lock:
            try:
                import fcntl

                fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
            except ImportError:
                pass
            merged = {
                "schema_version": "commentary-v5-operations-snapshot-v1",
                "workers": {},
                "orchestrators": {},
                "tasks": {},
                "artifacts": {},
            }
            if self.path.exists():
                try:
                    current = json.loads(self.path.read_text(encoding="utf-8"))
                    if isinstance(current, dict):
                        merged.update(current)
                except (OSError, json.JSONDecodeError):
                    pass
            for collection, keys in self.dirty_keys.items():
                target = merged.setdefault(collection, {})
                for key in keys:
                    target[key] = self.value[collection][key]
            merged["generated_at"] = utc_now()
            _atomic_write_json(self.path, merged)
            self.value = merged
            try:
                import fcntl

                fcntl.flock(lock.fileno(), fcntl.LOCK_UN)
            except ImportError:
                pass
        self.dirty = False
        for keys in self.dirty_keys.values():
            keys.clear()

    def _mark(self, collection: str, key: str) -> None:
        self.dirty_keys[collection].add(key)
        self.dirty = True

    def register(self, registration: dict[str, Any]) -> str:
        worker = {
            "worker_id": registration["worker_id"],
            "status": "online",
            "heartbeat_at": utc_now(),
        }
        self.value["workers"][registration["worker_id"]] = worker
        current = self.value["orchestrators"].get(registration["orchestrator_id"], {})
        self.value["orchestrators"][registration["orchestrator_id"]] = {
            **current,
            **registration,
            "desired_state": current.get("desired_state", "running"),
            "monitor_state": "online",
        }
        self._mark("workers", registration["worker_id"])
        self._mark("orchestrators", registration["orchestrator_id"])
        return self.value["orchestrators"][registration["orchestrator_id"]][
            "desired_state"
        ]

    def set_control_state(self, registration: dict[str, Any], state: str) -> None:
        record = self.value["orchestrators"].setdefault(
            registration["orchestrator_id"], dict(registration)
        )
        record["desired_state"] = state
        record["control_mirrored_at"] = utc_now()
        self._mark("orchestrators", registration["orchestrator_id"])

    def heartbeat(self, registration: dict[str, Any], at: str) -> None:
        worker = self.value["workers"].setdefault(
            registration["worker_id"], {"worker_id": registration["worker_id"]}
        )
        worker.update({"status": "online", "heartbeat_at": at})
        self._mark("workers", registration["worker_id"])

    def upsert_task(self, task: dict[str, Any]) -> None:
        self.value["tasks"][task["task_id"]] = task
        self._mark("tasks", task["task_id"])

    def upsert_artifact(self, task: dict[str, Any], artifact: dict[str, Any]) -> None:
        by_task = self.value["artifacts"].setdefault(task["task_id"], {})
        by_task[artifact["kind"]] = artifact
        self._mark("artifacts", task["task_id"])

    def close(self, registration: dict[str, Any], at: str) -> None:
        record = self.value["orchestrators"].get(registration["orchestrator_id"])
        if record is not None:
            record["monitor_state"] = "offline"
            record["heartbeat_at"] = at
            self._mark("orchestrators", registration["orchestrator_id"])
        self.flush()


class FirebaseSink:
    """Small Firebase Admin adapter; imported only when cloud sync is requested."""

    def __init__(self, project_id: str) -> None:
        try:
            import firebase_admin
            from firebase_admin import firestore
        except ImportError as exc:
            raise MonitorError(
                "Firebase sync requires `pip install -r operations/requirements.txt`"
            ) from exc
        app_name = f"commentary-v5-{os.getpid()}"
        self._app = firebase_admin.initialize_app(
            options={"projectId": project_id}, name=app_name
        )
        self._db = firestore.client(app=self._app)

    def _orchestrator_ref(self, registration: dict[str, Any]):
        return (
            self._db.collection("runs")
            .document(registration["run_id"])
            .collection("orchestrators")
            .document(registration["orchestrator_id"])
        )

    def register(self, registration: dict[str, Any]) -> str:
        worker_ref = self._db.collection("workers").document(registration["worker_id"])
        worker_ref.set(
            {
                "worker_id": registration["worker_id"],
                "status": "online",
                "heartbeat_at": utc_now(),
            },
            merge=True,
        )
        orchestrator_ref = self._orchestrator_ref(registration)
        current = orchestrator_ref.get()
        desired = "running"
        if current.exists:
            desired = (current.to_dict() or {}).get("desired_state", desired)
        orchestrator_ref.set(
            {
                **registration,
                "desired_state": desired,
                "monitor_state": "online",
                "registered_at": utc_now(),
            },
            merge=True,
        )
        return desired

    def desired_state(self, registration: dict[str, Any]) -> str | None:
        snapshot = self._orchestrator_ref(registration).get()
        if not snapshot.exists:
            return None
        return (snapshot.to_dict() or {}).get("desired_state")

    def heartbeat(self, registration: dict[str, Any], at: str) -> None:
        self._db.collection("workers").document(registration["worker_id"]).set(
            {"status": "online", "heartbeat_at": at}, merge=True
        )
        self._orchestrator_ref(registration).set(
            {"monitor_state": "online", "heartbeat_at": at}, merge=True
        )

    def upsert_task(self, task: dict[str, Any]) -> None:
        (
            self._db.collection("runs")
            .document(task["run_id"])
            .collection("tasks")
            .document(task["task_id"])
            .set(task, merge=True)
        )

    def upsert_artifact(self, task: dict[str, Any], artifact: dict[str, Any]) -> None:
        (
            self._db.collection("runs")
            .document(task["run_id"])
            .collection("tasks")
            .document(task["task_id"])
            .collection("artifacts")
            .document(artifact["kind"])
            .set(artifact, merge=True)
        )

    def close(self, registration: dict[str, Any], at: str) -> None:
        self._orchestrator_ref(registration).set(
            {"monitor_state": "offline", "heartbeat_at": at}, merge=True
        )


@dataclass(frozen=True)
class ArtifactSpec:
    kind: str
    path: Path
    reader_visible: bool


def artifact_specs(registration: dict[str, Any], ayah_ref: str) -> list[ArtifactSpec]:
    surah, ayah = ref_parts(ayah_ref)
    analysis_id = registration["analysis_id"]
    unit_dir = f"{surah}_{ayah}"
    input_dir = V5_ROOT / "input" / analysis_id / f"s{surah:03d}" / unit_dir
    raw_dir = V5_ROOT / "raw" / analysis_id / f"s{surah:03d}" / unit_dir
    editorial_dir = V5_ROOT / "editorial" / analysis_id / f"s{surah:03d}" / unit_dir
    specs: list[ArtifactSpec] = []
    for lane in LANES:
        specs.extend(
            [
                ArtifactSpec(
                    f"{lane}_prompt",
                    input_dir / f"{lane}.discovery.prompt.md",
                    False,
                ),
                ArtifactSpec(
                    f"{lane}_discovery",
                    raw_dir / f"{lane}.discovery.json",
                    False,
                ),
                ArtifactSpec(
                    lane,
                    raw_dir / f"{lane}.scope.tr.md",
                    True,
                ),
            ]
        )
    specs.extend(
        [
            ArtifactSpec("consolidated", raw_dir / f"{unit_dir}.prose.tr.md", True),
            ArtifactSpec(
                "editorial",
                editorial_dir / f"{unit_dir}.prose.editorial.tr.md",
                True,
            ),
        ]
    )
    return specs


def _read_event_file(path: Path) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return events
    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError:
            events.append(
                {
                    "event": "attention",
                    "at": utc_now(),
                    "message": f"Malformed event line {path.name}:{line_number}",
                }
            )
            continue
        if isinstance(value, dict):
            events.append(value)
    return events


def _event_stage(event: dict[str, Any]) -> str:
    role = event.get("role")
    if role == "scope":
        return str(event.get("lane") or "scope")
    return str(role or "unknown")


def _latest_by_stage(events: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for event in sorted(events, key=lambda item: (str(item.get("at", "")), int(item.get("attempt", 0)))):
        result[_event_stage(event)] = event
    return result


def _stage_state(
    stage: str,
    latest: dict[str, dict[str, Any]],
    artifacts: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    event = latest.get(stage, {})
    state: dict[str, Any] = {
        "status": "pending",
        "attempt": int(event.get("attempt", 0)),
        "agent_id": event.get("agent_id"),
        "updated_at": event.get("at"),
    }
    event_status = event.get("event")
    if event_status == "started":
        state["status"] = "active"
    elif event_status in TERMINAL_EVENTS:
        state["status"] = event_status
    elif event_status == "attention":
        state["status"] = "attention"
    event_at = str(event.get("at", ""))

    def artifact_is_current(kind: str) -> bool:
        artifact = artifacts.get(kind)
        return bool(artifact and str(artifact.get("modified_at", "")) >= event_at)

    if stage in LANES:
        if artifact_is_current(stage):
            state["status"] = "completed"
        elif artifact_is_current(f"{stage}_discovery") and state["status"] in {"pending", "active"}:
            state["status"] = "composing"
        elif artifact_is_current(f"{stage}_prompt") and state["status"] == "pending":
            state["status"] = "ready"
    elif stage == "canonical":
        if artifact_is_current("editorial"):
            state["status"] = "completed"
        elif artifact_is_current("consolidated") and state["status"] in {"pending", "active"}:
            state["status"] = "editing"
        elif all(lane in artifacts for lane in LANES) and state["status"] == "pending":
            state["status"] = "ready"
    elif stage == "validator" and event_status == "completed":
        state["status"] = "passed"
    return state


def build_task(registration: dict[str, Any], ayah_ref: str) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    event_root = event_path(registration, ayah_ref, "canonical", None, 1).parent
    events: list[dict[str, Any]] = []
    if event_root.is_dir():
        for path in sorted(event_root.glob("*.jsonl")):
            events.extend(_read_event_file(path))

    artifacts: dict[str, dict[str, Any]] = {}
    reader_artifacts: list[dict[str, Any]] = []
    latest_mtime_ns = 0
    for spec in artifact_specs(registration, ayah_ref):
        try:
            stat = spec.path.stat()
        except OSError:
            continue
        if not spec.path.is_file():
            continue
        latest_mtime_ns = max(latest_mtime_ns, stat.st_mtime_ns)
        metadata = {
            "kind": spec.kind,
            "path": str(spec.path.relative_to(REPO_ROOT)),
            "size": stat.st_size,
            "modified_at": datetime.fromtimestamp(stat.st_mtime, UTC)
            .isoformat(timespec="seconds")
            .replace("+00:00", "Z"),
        }
        artifacts[spec.kind] = metadata
        if spec.reader_visible:
            payload = spec.path.read_bytes()
            artifact = {
                **metadata,
                "sha256": hashlib.sha256(payload).hexdigest(),
                "oversize": len(payload) > MAX_ARTIFACT_BYTES,
                "content": None,
            }
            if not artifact["oversize"]:
                artifact["content"] = payload.decode("utf-8")
            reader_artifacts.append(artifact)

    latest = _latest_by_stage(events)
    stages = {
        stage: _stage_state(stage, latest, artifacts)
        for stage in (*LANES, "canonical", "validator")
    }
    attention = [
        {
            "stage": _event_stage(event),
            "status": event.get("event"),
            "message": event.get("message") or "Agent attention required",
            "at": event.get("at"),
        }
        for event in events
        if event.get("event") in {"failed", "attention"}
    ]
    current_failures = [
        stage for stage, value in stages.items() if value["status"] == "failed"
    ]
    current_attention = [
        stage for stage, value in stages.items() if value["status"] == "attention"
    ]
    if current_failures:
        status = "failed"
    elif current_attention:
        status = "attention"
    elif stages["validator"]["status"] == "passed":
        status = "completed"
    elif stages["canonical"]["status"] == "completed":
        status = "awaiting_validation"
    elif any(
        value["status"] not in {"pending", "ready"} for value in stages.values()
    ) or artifacts:
        status = "active"
    else:
        status = "pending"

    timestamps = [str(event.get("at")) for event in events if event.get("at")]
    if latest_mtime_ns:
        timestamps.append(
            datetime.fromtimestamp(latest_mtime_ns / 1_000_000_000, UTC)
            .isoformat(timespec="seconds")
            .replace("+00:00", "Z")
        )
    task_id = f"{registration['orchestrator_id']}--{unit_key(ayah_ref)}"
    task = {
        "schema_version": "commentary-v5-operation-task-v1",
        "task_id": task_id,
        "run_id": registration["run_id"],
        "worker_id": registration["worker_id"],
        "orchestrator_id": registration["orchestrator_id"],
        "analysis_id": registration["analysis_id"],
        "ayah_ref": ayah_ref,
        "status": status,
        "stages": stages,
        "attention": attention[-20:],
        "artifact_kinds": sorted(artifacts),
        "updated_at": max(timestamps) if timestamps else registration["started_at"],
    }
    return task, reader_artifacts


class Monitor:
    def __init__(
        self,
        registration: dict[str, Any],
        *,
        interval: float,
        heartbeat_interval: float,
        firebase: FirebaseSink | None,
    ) -> None:
        self.registration = registration
        self.interval = interval
        self.heartbeat_interval = heartbeat_interval
        self.firebase = firebase
        self.local = LocalSnapshot()
        self.stop_requested = False
        self.fingerprints: dict[Path, tuple[int, int]] = {}
        self.synced_artifacts: dict[tuple[str, str], str] = {}
        self.scope = set(registration["scope_refs"])
        self.last_heartbeat = 0.0

    def _safe_remote(self, method: str, *args: Any) -> Any:
        if self.firebase is None:
            return None
        try:
            return getattr(self.firebase, method)(*args)
        except Exception as exc:  # keep local monitoring alive during network loss
            print(f"{utc_now()} firebase {method} failed: {exc}", flush=True)
            return None

    def _mirror_control(self, desired: str | None) -> None:
        marker = control_marker(self.registration)
        if desired == "paused":
            if not marker.exists():
                _atomic_write_text(marker, f"paused_at={utc_now()}\n")
        elif desired == "running":
            marker.unlink(missing_ok=True)
        current = "paused" if marker.exists() else "running"
        self.local.set_control_state(self.registration, current)

    def _candidate_files(self) -> Iterable[Path]:
        event_root = registration_path(
            self.registration["run_id"], self.registration["orchestrator_id"]
        ).parent / "events"
        if event_root.is_dir():
            yield from event_root.rglob("*.jsonl")
        analysis_id = self.registration["analysis_id"]
        for root in (
            V5_ROOT / "input" / analysis_id,
            V5_ROOT / "raw" / analysis_id,
            V5_ROOT / "editorial" / analysis_id,
        ):
            if root.is_dir():
                yield from root.rglob("*")

    def _ref_from_path(self, path: Path) -> str | None:
        for parent in (path.parent, *path.parents):
            match = UNIT_DIR_RE.fullmatch(parent.name)
            if match is not None:
                ref = f"{int(match.group(1))}:{int(match.group(2))}"
                return ref if ref in self.scope else None
            if parent == V5_ROOT or parent == RUNTIME_ROOT:
                break
        return None

    def changed_refs(self) -> set[str]:
        current: dict[Path, tuple[int, int]] = {}
        changed: set[str] = set()
        for path in self._candidate_files():
            try:
                if not path.is_file():
                    continue
                stat = path.stat()
            except OSError:
                continue
            fingerprint = (stat.st_mtime_ns, stat.st_size)
            current[path] = fingerprint
            if self.fingerprints.get(path) != fingerprint:
                ref = self._ref_from_path(path)
                if ref is not None:
                    changed.add(ref)
        for path in self.fingerprints.keys() - current.keys():
            ref = self._ref_from_path(path)
            if ref is not None:
                changed.add(ref)
        self.fingerprints = current
        return changed

    def sync_ref(self, ayah_ref: str) -> None:
        task, artifacts = build_task(self.registration, ayah_ref)
        self.local.upsert_task(task)
        self._safe_remote("upsert_task", task)
        for artifact in artifacts:
            key = (task["task_id"], artifact["kind"])
            if self.synced_artifacts.get(key) == artifact["sha256"]:
                continue
            self.local.upsert_artifact(task, artifact)
            self._safe_remote("upsert_artifact", task, artifact)
            self.synced_artifacts[key] = artifact["sha256"]

    def tick(self) -> None:
        desired = self._safe_remote("desired_state", self.registration)
        self._mirror_control(desired)
        for ayah_ref in sorted(self.changed_refs(), key=lambda ref: ref_parts(ref)):
            self.sync_ref(ayah_ref)
        now = time.monotonic()
        if now - self.last_heartbeat >= self.heartbeat_interval:
            at = utc_now()
            self.local.heartbeat(self.registration, at)
            self._safe_remote("heartbeat", self.registration, at)
            self.last_heartbeat = now
        self.local.flush()

    def run(self, *, once: bool = False) -> None:
        desired = self.local.register(self.registration)
        remote_desired = self._safe_remote("register", self.registration)
        self._mirror_control(remote_desired or desired)
        self.local.flush()
        while not self.stop_requested:
            self.tick()
            if once:
                break
            time.sleep(self.interval)
        at = utc_now()
        self.local.close(self.registration, at)
        self._safe_remote("close", self.registration, at)


def _monitor_log_path(registration: dict[str, Any]) -> Path:
    return (
        RUNTIME_ROOT
        / "monitors"
        / registration["run_id"]
        / f"{registration['orchestrator_id']}.log"
    )


def _pid_path(registration: dict[str, Any]) -> Path:
    return _monitor_log_path(registration).with_suffix(".pid")


def create_registration(args: argparse.Namespace) -> tuple[Path, dict[str, Any]]:
    run_id = validate_id(args.run_id, "run ID")
    worker_id = validate_id(args.worker_id or socket.gethostname().split(".")[0], "worker ID")
    orchestrator_id = validate_id(
        args.orchestrator_id
        or f"orch-{datetime.now(UTC).strftime('%Y%m%dT%H%M%S')}-{uuid.uuid4().hex[:8]}",
        "orchestrator ID",
    )
    analysis_id = validate_id(args.analysis_id, "analysis ID")
    scope_refs = expand_scope(args.scope)
    registration = {
        "schema_version": "commentary-v5-orchestrator-registration-v1",
        "run_id": run_id,
        "worker_id": worker_id,
        "orchestrator_id": orchestrator_id,
        "agent_id": args.agent_id,
        "analysis_id": analysis_id,
        "scope_selectors": list(args.scope),
        "scope_refs": scope_refs,
        "scope_count": len(scope_refs),
        "started_at": utc_now(),
        "repo_root": str(REPO_ROOT),
        "poll_seconds": args.poll_seconds,
        "firebase_project_id": args.firebase_project,
    }
    path = registration_path(run_id, orchestrator_id)
    _atomic_write_json(path, registration)
    return path, registration


def command_start(args: argparse.Namespace) -> int:
    if not args.local_only:
        if not args.firebase_project:
            raise MonitorError("--firebase-project is required unless --local-only is used")
        try:
            import firebase_admin  # noqa: F401
        except ImportError as exc:
            raise MonitorError(
                "Firebase sync requires `pip install -r _commentary/v5/operations/requirements.txt`"
            ) from exc
    path, registration = create_registration(args)
    log_path = _monitor_log_path(registration)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    command = [
        sys.executable,
        str(Path(__file__).resolve()),
        "run",
        "--registration",
        str(path),
    ]
    if args.local_only:
        command.append("--local-only")
    with log_path.open("ab", buffering=0) as output:
        process = subprocess.Popen(
            command,
            cwd=REPO_ROOT,
            stdin=subprocess.DEVNULL,
            stdout=output,
            stderr=subprocess.STDOUT,
            start_new_session=True,
            close_fds=True,
        )
    _atomic_write_text(_pid_path(registration), f"{process.pid}\n")
    print(
        json.dumps(
            {
                "status": "started",
                "pid": process.pid,
                "run_id": registration["run_id"],
                "worker_id": registration["worker_id"],
                "orchestrator_id": registration["orchestrator_id"],
                "scope_count": registration["scope_count"],
                "registration": str(path),
                "pause_file": str(control_marker(registration)),
                "log": str(log_path),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


def command_run(args: argparse.Namespace) -> int:
    registration = load_registration(args.registration)
    firebase = None
    if not args.local_only:
        project_id = registration.get("firebase_project_id")
        if not project_id:
            raise MonitorError("Registration has no Firebase project ID")
        firebase = FirebaseSink(project_id)
    monitor = Monitor(
        registration,
        interval=float(registration.get("poll_seconds", 10)),
        heartbeat_interval=60,
        firebase=firebase,
    )

    def request_stop(_signum: int, _frame: Any) -> None:
        monitor.stop_requested = True

    signal.signal(signal.SIGTERM, request_stop)
    signal.signal(signal.SIGINT, request_stop)
    try:
        monitor.run(once=args.once)
    finally:
        pid_path = _pid_path(registration)
        try:
            if pid_path.read_text(encoding="utf-8").strip() == str(os.getpid()):
                pid_path.unlink(missing_ok=True)
        except OSError:
            pass
    return 0


def command_event(args: argparse.Namespace) -> int:
    path = registration_path(args.run_id, args.orchestrator_id)
    registration = load_registration(path)
    if args.ayah_ref not in set(registration["scope_refs"]):
        raise MonitorError(
            f"Ayah {args.ayah_ref} is outside orchestrator scope {args.orchestrator_id}"
        )
    if args.role == "scope" and args.lane not in LANES:
        raise MonitorError("Scope events require --lane micro, macro, or global")
    if args.role != "scope" and args.lane is not None:
        raise MonitorError("--lane is only valid for scope events")
    event = {
        "schema_version": "commentary-v5-operation-event-v1",
        "event": args.status,
        "at": utc_now(),
        "run_id": registration["run_id"],
        "worker_id": registration["worker_id"],
        "orchestrator_id": registration["orchestrator_id"],
        "agent_id": args.agent_id,
        "ayah_ref": args.ayah_ref,
        "role": args.role,
        "lane": args.lane,
        "attempt": args.attempt,
        "message": args.message,
    }
    destination = event_path(
        registration, args.ayah_ref, args.role, args.lane, args.attempt
    )
    _append_jsonl(destination, event)
    print(str(destination))
    return 0


def command_wait(args: argparse.Namespace) -> int:
    registration = load_registration(
        registration_path(args.run_id, args.orchestrator_id)
    )
    marker = control_marker(registration)
    announced = False
    while marker.exists():
        if not announced:
            print(f"paused: {marker}", flush=True)
            announced = True
        time.sleep(args.poll_seconds)
    print("running", flush=True)
    return 0


def command_control(args: argparse.Namespace) -> int:
    registration = load_registration(
        registration_path(args.run_id, args.orchestrator_id)
    )
    marker = control_marker(registration)
    if args.state == "paused":
        _atomic_write_text(marker, f"paused_at={utc_now()}\n")
    else:
        marker.unlink(missing_ok=True)
    print(args.state)
    return 0


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    subparsers = result.add_subparsers(dest="command", required=True)

    start = subparsers.add_parser("start", help="Register and start a background monitor.")
    start.add_argument("--run-id", required=True)
    start.add_argument("--worker-id")
    start.add_argument("--orchestrator-id")
    start.add_argument("--agent-id")
    start.add_argument("--analysis-id", default="native")
    start.add_argument(
        "--scope",
        action="append",
        required=True,
        help="S, S-T, S:A, or S:A-B; may be repeated.",
    )
    start.add_argument("--poll-seconds", type=float, default=10)
    start.add_argument("--firebase-project", default=os.environ.get("FIREBASE_PROJECT_ID"))
    start.add_argument("--local-only", action="store_true")
    start.set_defaults(func=command_start)

    run = subparsers.add_parser("run", help="Run a monitor in the foreground.")
    run.add_argument("--registration", type=Path, required=True)
    run.add_argument("--local-only", action="store_true")
    run.add_argument("--once", action="store_true")
    run.set_defaults(func=command_run)

    event = subparsers.add_parser("event", help="Append one agent lifecycle event.")
    event.add_argument("--run-id", required=True)
    event.add_argument("--orchestrator-id", required=True)
    event.add_argument("--ayah-ref", required=True)
    event.add_argument("--role", choices=sorted(ROLES), required=True)
    event.add_argument("--lane", choices=LANES)
    event.add_argument("--attempt", type=int, default=1)
    event.add_argument("--status", choices=sorted(EVENTS), required=True)
    event.add_argument("--agent-id")
    event.add_argument("--message")
    event.set_defaults(func=command_event)

    wait = subparsers.add_parser("wait", help="Block locally while pause is requested.")
    wait.add_argument("--run-id", required=True)
    wait.add_argument("--orchestrator-id", required=True)
    wait.add_argument("--poll-seconds", type=float, default=10)
    wait.set_defaults(func=command_wait)

    control = subparsers.add_parser("control", help="Set local control state for testing.")
    control.add_argument("--run-id", required=True)
    control.add_argument("--orchestrator-id", required=True)
    control.add_argument("state", choices=("running", "paused"))
    control.set_defaults(func=command_control)
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        return int(args.func(args))
    except MonitorError as exc:
        print(json.dumps({"status": "error", "error": str(exc)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
