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
from contextlib import contextmanager
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen
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
TERMINAL_EVENTS = frozenset({"completed", "failed", "interrupted", "attention"})
EVENTS = frozenset({"started", *TERMINAL_EVENTS})
ROLES = frozenset({"scope", "canonical", "validator", "orchestrator"})
LANES = ("micro", "macro", "global")
MAX_ARTIFACT_BYTES = 900_000
DEFAULT_FIREBASE_PROJECT_ID = "v5-monitor"
DEFAULT_FIREBASE_API_KEY = "AIzaSyArWIsYnZvo5Sbf87htqjxE21omQNKtsyU"
FIRESTORE_API_ROOT = "https://firestore.googleapis.com/v1"

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
    return datetime.now(UTC).isoformat(timespec="microseconds").replace("+00:00", "Z")


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


def stop_marker(registration: dict[str, Any]) -> Path:
    return control_marker(registration).with_name("STOP")


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


def _event_task_name(role: str, lane: str | None) -> str:
    return str(lane) if role == "scope" else role


def resolve_attempt(
    registration: dict[str, Any],
    ayah_ref: str,
    role: str,
    lane: str | None,
    status: str,
    agent_id: str | None,
    requested: int | None,
) -> int:
    if requested is not None:
        if requested < 1:
            raise MonitorError("Attempt must be at least 1")
        return requested
    directory = event_path(registration, ayah_ref, role, lane, 1).parent
    task_name = re.escape(_event_task_name(role, lane))
    attempts: dict[int, list[dict[str, Any]]] = {}
    for path in directory.glob(f"{_event_task_name(role, lane)}.*.jsonl"):
        match = re.fullmatch(rf"{task_name}\.(\d+)\.jsonl", path.name)
        if match is not None:
            attempts[int(match.group(1))] = _read_event_file(path)
    if status == "started":
        return max(attempts, default=0) + 1
    open_attempts = [
        number
        for number, events in attempts.items()
        if not events or events[-1].get("event") not in TERMINAL_EVENTS
    ]
    matching = [
        number
        for number in open_attempts
        if agent_id
        and any(event.get("agent_id") == agent_id for event in attempts[number])
    ]
    if agent_id and matching:
        return max(matching)
    if agent_id and open_attempts:
        raise MonitorError(
            f"No open attempt for agent {agent_id!r}; refusing to close another agent's attempt"
        )
    if len(open_attempts) == 1:
        return open_attempts[0]
    if len(open_attempts) > 1:
        raise MonitorError("Multiple attempts are open; provide --agent-id or --attempt")
    if status == "attention":
        return max(attempts, default=0) + 1
    raise MonitorError("No open attempt matches this terminal event")


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
    for key, label in (
        ("run_id", "run ID"),
        ("worker_id", "worker ID"),
        ("orchestrator_id", "orchestrator ID"),
        ("analysis_id", "analysis ID"),
    ):
        if not isinstance(value.get(key), str):
            raise MonitorError(f"Registration {key} must be a string")
        validate_id(value[key], label)
    scope_refs = value.get("scope_refs")
    if not isinstance(scope_refs, list) or not scope_refs:
        raise MonitorError("Registration scope_refs must be a nonempty list")
    if any(not isinstance(ref, str) for ref in scope_refs):
        raise MonitorError("Registration scope_refs must contain only strings")
    normalized_refs = expand_scope(scope_refs)
    if normalized_refs != scope_refs:
        raise MonitorError("Registration scope_refs are invalid, duplicated, or not normalized")
    if value.get("scope_count") is not None and value["scope_count"] != len(scope_refs):
        raise MonitorError("Registration scope_count does not match scope_refs")
    try:
        poll_seconds = float(value.get("poll_seconds", 10))
    except (TypeError, ValueError) as exc:
        raise MonitorError("Registration poll_seconds must be numeric") from exc
    if poll_seconds <= 0:
        raise MonitorError("Registration poll_seconds must be greater than zero")
    return value


class RemoteSink(Protocol):
    def register(self, registration: dict[str, Any]) -> str: ...

    def desired_state(self, registration: dict[str, Any]) -> str | None: ...

    def heartbeat(self, registration: dict[str, Any], at: str) -> None: ...

    def upsert_task(self, task: dict[str, Any]) -> None: ...

    def upsert_artifact(self, task: dict[str, Any], artifact: dict[str, Any]) -> None: ...

    def close(self, registration: dict[str, Any], at: str) -> None: ...


def public_registration(registration: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value
        for key, value in registration.items()
        if key != "firebase_passcode_hash"
    }


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
        current = public_registration(
            self.value["orchestrators"].get(registration["orchestrator_id"], {})
        )
        self.value["orchestrators"][registration["orchestrator_id"]] = {
            **current,
            **public_registration(registration),
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
            registration["orchestrator_id"], public_registration(registration)
        )
        if record.get("desired_state") == state:
            return
        record["desired_state"] = state
        record["control_mirrored_at"] = utc_now()
        self._mark("orchestrators", registration["orchestrator_id"])

    def heartbeat(self, registration: dict[str, Any], at: str) -> None:
        worker = self.value["workers"].setdefault(
            registration["worker_id"], {"worker_id": registration["worker_id"]}
        )
        worker.update({"status": "online", "heartbeat_at": at})
        self._mark("workers", registration["worker_id"])
        record = self.value["orchestrators"].setdefault(
            registration["orchestrator_id"], public_registration(registration)
        )
        record.update({"monitor_state": "online", "heartbeat_at": at})
        self._mark("orchestrators", registration["orchestrator_id"])

    def upsert_task(self, task: dict[str, Any]) -> None:
        self.value["tasks"][task["task_id"]] = task
        self._mark("tasks", task["task_id"])

    def replace_artifacts(
        self, task: dict[str, Any], artifacts: list[dict[str, Any]]
    ) -> None:
        self.value["artifacts"][task["task_id"]] = {
            artifact["kind"]: {
                key: value for key, value in artifact.items() if key != "content"
            }
            for artifact in artifacts
        }
        self._mark("artifacts", task["task_id"])

    def close(self, registration: dict[str, Any], at: str) -> None:
        record = self.value["orchestrators"].get(registration["orchestrator_id"])
        if record is not None:
            record["monitor_state"] = "offline"
            record["heartbeat_at"] = at
            self._mark("orchestrators", registration["orchestrator_id"])
        self.flush()


def _firestore_value(value: Any) -> dict[str, Any]:
    if value is None:
        return {"nullValue": None}
    if isinstance(value, bool):
        return {"booleanValue": value}
    if isinstance(value, int):
        return {"integerValue": str(value)}
    if isinstance(value, float):
        return {"doubleValue": value}
    if isinstance(value, str):
        return {"stringValue": value}
    if isinstance(value, (list, tuple)):
        return {"arrayValue": {"values": [_firestore_value(item) for item in value]}}
    if isinstance(value, dict):
        return {
            "mapValue": {
                "fields": {str(key): _firestore_value(item) for key, item in value.items()}
            }
        }
    raise MonitorError(f"Unsupported Firestore value: {type(value).__name__}")


def _from_firestore_value(value: dict[str, Any]) -> Any:
    if "nullValue" in value:
        return None
    if "booleanValue" in value:
        return value["booleanValue"]
    if "integerValue" in value:
        return int(value["integerValue"])
    if "doubleValue" in value:
        return value["doubleValue"]
    if "stringValue" in value:
        return value["stringValue"]
    if "timestampValue" in value:
        return value["timestampValue"]
    if "arrayValue" in value:
        return [
            _from_firestore_value(item)
            for item in value["arrayValue"].get("values", [])
        ]
    if "mapValue" in value:
        return {
            key: _from_firestore_value(item)
            for key, item in value["mapValue"].get("fields", {}).items()
        }
    raise MonitorError("Unsupported Firestore response value")


def _firestore_document(value: dict[str, Any]) -> dict[str, Any]:
    return {"fields": {key: _firestore_value(item) for key, item in value.items()}}


def _from_firestore_document(value: dict[str, Any]) -> dict[str, Any]:
    return {
        key: _from_firestore_value(item)
        for key, item in value.get("fields", {}).items()
    }


class FirebaseRestSink:
    """Direct Firestore REST adapter authenticated by a revocable passcode hash."""

    def __init__(self, project_id: str, api_key: str, passcode_hash: str) -> None:
        self.project_id = validate_id(project_id, "Firebase project ID")
        if not api_key:
            raise MonitorError("Firebase API key is required")
        if re.fullmatch(r"[0-9a-f]{64}", passcode_hash) is None:
            raise MonitorError("Firebase passcode hash is invalid")
        self.api_key = api_key
        self.passcode_hash = passcode_hash
        self.last_desired_state: str | None = None
        self.base_url = (
            f"{FIRESTORE_API_ROOT}/projects/{quote(project_id, safe='')}"
            "/databases/(default)/documents"
        )

    @staticmethod
    def _path(*parts: str) -> str:
        return "/".join(quote(str(part), safe="") for part in parts)

    @staticmethod
    def _control_id(registration: dict[str, Any]) -> str:
        return f"{registration['run_id']}--{registration['orchestrator_id']}"

    def _request(
        self,
        method: str,
        path: str,
        value: dict[str, Any] | None = None,
        *,
        update_fields: Iterable[str] | None = None,
        allow_not_found: bool = False,
    ) -> dict[str, Any] | None:
        query: list[tuple[str, str]] = [("key", self.api_key)]
        if update_fields is not None:
            query.extend(("updateMask.fieldPaths", field) for field in update_fields)
        url = f"{self.base_url}/{path}?{urlencode(query)}"
        payload = None
        headers = {"Accept": "application/json"}
        if value is not None:
            payload = json.dumps(_firestore_document(value)).encode("utf-8")
            headers["Content-Type"] = "application/json"
        request = Request(url, data=payload, headers=headers, method=method)
        for attempt in range(3):
            try:
                with urlopen(request, timeout=20) as response:
                    body = response.read()
                return json.loads(body) if body else {}
            except HTTPError as exc:
                if exc.code == 404 and allow_not_found:
                    return None
                if exc.code in {429, 500, 502, 503, 504} and attempt < 2:
                    time.sleep(attempt + 1)
                    continue
                try:
                    detail = json.loads(exc.read()).get("error", {}).get("message")
                except (json.JSONDecodeError, AttributeError):
                    detail = None
                raise MonitorError(
                    f"Firestore {method} {path} failed ({exc.code})"
                    + (f": {detail}" if detail else "")
                ) from exc
            except (URLError, TimeoutError) as exc:
                if attempt < 2:
                    time.sleep(attempt + 1)
                    continue
                raise MonitorError(f"Firestore {method} {path} failed: {exc}") from exc
        raise MonitorError(f"Firestore {method} {path} failed")

    def _write(
        self,
        path: str,
        value: dict[str, Any],
        *,
        update_fields: Iterable[str] | None = None,
    ) -> None:
        secured = {**value, "_passcode_hash": self.passcode_hash}
        fields = None
        if update_fields is not None:
            fields = [*update_fields, "_passcode_hash"]
        self._request("PATCH", path, secured, update_fields=fields)

    def _get(self, path: str) -> dict[str, Any] | None:
        document = self._request("GET", path, allow_not_found=True)
        return _from_firestore_document(document) if document is not None else None

    def _orchestrator_path(self, registration: dict[str, Any]) -> str:
        return self._path(
            "runs",
            registration["run_id"],
            "orchestrators",
            registration["orchestrator_id"],
        )

    def register(self, registration: dict[str, Any]) -> str:
        desired = self._read_control_state(registration) or "running"
        self.last_desired_state = desired
        self._write(
            self._path("runs", registration["run_id"]),
            {
                "run_id": registration["run_id"],
                "last_registered_at": utc_now(),
            },
        )
        self._write(
            self._path("workers", registration["worker_id"]),
            {
                "worker_id": registration["worker_id"],
                "status": "online",
                "heartbeat_at": utc_now(),
            },
        )
        self._write(
            self._orchestrator_path(registration),
            {
                **public_registration(registration),
                "desired_state": desired,
                "monitor_state": "online",
                "registered_at": utc_now(),
            },
        )
        return desired

    def _read_control_state(self, registration: dict[str, Any]) -> str | None:
        control = self._get(
            self._path("controls", self._control_id(registration))
        )
        if control is None or control.get("desired_state") not in {"running", "paused"}:
            return None
        return str(control["desired_state"])

    def desired_state(self, registration: dict[str, Any]) -> str | None:
        desired = self._read_control_state(registration)
        if desired is not None and desired != self.last_desired_state:
            self._write(
                self._orchestrator_path(registration),
                {"desired_state": desired, "control_mirrored_at": utc_now()},
                update_fields=("desired_state", "control_mirrored_at"),
            )
            self.last_desired_state = desired
        return desired

    def heartbeat(self, registration: dict[str, Any], at: str) -> None:
        self._write(
            self._path("workers", registration["worker_id"]),
            {"status": "online", "heartbeat_at": at},
            update_fields=("status", "heartbeat_at"),
        )
        self._write(
            self._orchestrator_path(registration),
            {"monitor_state": "online", "heartbeat_at": at},
            update_fields=("monitor_state", "heartbeat_at"),
        )

    def upsert_task(self, task: dict[str, Any]) -> None:
        self._write(
            self._path("runs", task["run_id"], "tasks", task["task_id"]), task
        )

    def upsert_artifact(self, task: dict[str, Any], artifact: dict[str, Any]) -> None:
        self._write(
            self._path(
                "runs",
                task["run_id"],
                "tasks",
                task["task_id"],
                "artifacts",
                artifact["kind"],
            ),
            artifact,
        )

    def close(self, registration: dict[str, Any], at: str) -> None:
        self._write(
            self._orchestrator_path(registration),
            {"monitor_state": "offline", "heartbeat_at": at},
            update_fields=("monitor_state", "heartbeat_at"),
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
    grouped: dict[str, list[dict[str, Any]]] = {}
    for event in events:
        grouped.setdefault(_event_stage(event), []).append(event)
    result: dict[str, dict[str, Any]] = {}
    for stage, stage_events in grouped.items():
        latest_attempt = max(int(event.get("attempt", 0)) for event in stage_events)
        attempt_events = [
            event
            for event in stage_events
            if int(event.get("attempt", 0)) == latest_attempt
        ]
        latest = max(attempt_events, key=lambda item: _timestamp_key(item.get("at")))
        starts = [
            event
            for event in attempt_events
            if event.get("event") == "started" and event.get("at")
        ]
        result[stage] = {
            **latest,
            "_started_at": (
                min(starts, key=lambda item: _timestamp_key(item.get("at"))).get("at")
                if starts
                else None
            ),
        }
    return result


def _timestamp_key(value: Any) -> datetime:
    if isinstance(value, str):
        try:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
            return parsed if parsed.tzinfo is not None else parsed.replace(tzinfo=UTC)
        except ValueError:
            pass
    return datetime.min.replace(tzinfo=UTC)


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
    attempt_started_at = event.get("_started_at")

    def artifact_is_current(kind: str) -> bool:
        artifact = artifacts.get(kind)
        if not artifact:
            return False
        if not attempt_started_at:
            return True
        return _timestamp_key(artifact.get("modified_at")) >= _timestamp_key(
            attempt_started_at
        )

    if event_status in {"failed", "interrupted", "attention"}:
        state["status"] = event_status
        return state

    if event_status == "completed":
        required_artifact = stage if stage in LANES else "editorial"
        if stage == "validator":
            state["status"] = "passed" if "editorial" in artifacts else "attention"
        else:
            state["status"] = (
                "completed" if artifact_is_current(required_artifact) else "attention"
            )
        return state

    if event_status == "started":
        state["status"] = "active"
        if stage in LANES and artifact_is_current(f"{stage}_discovery"):
            state["status"] = "composing"
        elif stage == "canonical" and artifact_is_current("consolidated"):
            state["status"] = "editing"
        return state

    if stage in LANES:
        if stage in artifacts:
            state["status"] = "completed"
        elif f"{stage}_discovery" in artifacts:
            state["status"] = "composing"
        elif f"{stage}_prompt" in artifacts:
            state["status"] = "ready"
    elif stage == "canonical":
        if "editorial" in artifacts:
            state["status"] = "completed"
        elif "consolidated" in artifacts:
            state["status"] = "editing"
        elif all(lane in artifacts for lane in LANES):
            state["status"] = "ready"
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
    v5_root = V5_ROOT.resolve()
    for spec in artifact_specs(registration, ayah_ref):
        try:
            resolved = spec.path.resolve(strict=True)
            resolved.relative_to(v5_root)
            stat = resolved.stat()
        except (OSError, RuntimeError):
            continue
        except ValueError:
            continue
        if not resolved.is_file():
            continue
        payload: bytes | None = None
        content: str | None = None
        if spec.reader_visible:
            try:
                payload = resolved.read_bytes()
                second_stat = resolved.stat()
                if (
                    second_stat.st_mtime_ns != stat.st_mtime_ns
                    or second_stat.st_size != stat.st_size
                ):
                    continue
                if len(payload) <= MAX_ARTIFACT_BYTES:
                    content = payload.decode("utf-8")
            except (OSError, UnicodeDecodeError):
                continue
        metadata = {
            "kind": spec.kind,
            "path": str(spec.path.relative_to(REPO_ROOT)),
            "size": stat.st_size,
            "modified_at": datetime.fromtimestamp(stat.st_mtime, UTC)
            .isoformat(timespec="microseconds")
            .replace("+00:00", "Z"),
        }
        artifacts[spec.kind] = metadata
        latest_mtime_ns = max(latest_mtime_ns, stat.st_mtime_ns)
        if spec.reader_visible:
            assert payload is not None
            artifact = {
                **metadata,
                "sha256": hashlib.sha256(payload).hexdigest(),
                "oversize": len(payload) > MAX_ARTIFACT_BYTES,
                "content": content,
            }
            reader_artifacts.append(artifact)

    latest = _latest_by_stage(events)
    stages = {
        stage: _stage_state(stage, latest, artifacts)
        for stage in (*LANES, "canonical", "validator")
    }
    if "validator" not in latest and stages["canonical"]["status"] == "completed":
        canonical = stages["canonical"]
        stages["validator"] = {
            "status": "passed",
            "attempt": canonical["attempt"],
            "agent_id": canonical["agent_id"],
            "updated_at": canonical["updated_at"],
        }
    attention = [
        {
            "stage": _event_stage(event),
            "status": event.get("event"),
            "message": event.get("message") or "Agent attention required",
            "at": event.get("at"),
        }
        for event in events
        if event.get("event") in {"failed", "interrupted", "attention"}
    ]
    current_failures = [
        stage for stage, value in stages.items() if value["status"] == "failed"
    ]
    current_attention = [
        stage
        for stage, value in stages.items()
        if value["status"] in {"attention", "interrupted"}
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
    ):
        status = "active"
    else:
        status = "pending"

    timestamps = [str(event.get("at")) for event in events if event.get("at")]
    if latest_mtime_ns:
        timestamps.append(
            datetime.fromtimestamp(latest_mtime_ns / 1_000_000_000, UTC)
            .isoformat(timespec="microseconds")
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
        "updated_at": (
            max(timestamps, key=_timestamp_key)
            if timestamps
            else registration["started_at"]
        ),
    }
    return task, reader_artifacts


class Monitor:
    def __init__(
        self,
        registration: dict[str, Any],
        *,
        interval: float,
        heartbeat_interval: float,
        firebase: RemoteSink | None,
    ) -> None:
        self.registration = registration
        self.interval = interval
        self.heartbeat_interval = heartbeat_interval
        self.firebase = firebase
        self.local = LocalSnapshot()
        self.stop_requested = False
        self.fingerprints: dict[Path, tuple[int, int]] = {}
        self.synced_artifacts: dict[tuple[str, str], str] = {}
        self.pending_refs: set[str] = set()
        self.scope = set(registration["scope_refs"])
        self.last_heartbeat = 0.0
        self.registration_synced = firebase is None

    def _safe_remote(self, method: str, *args: Any) -> tuple[bool, Any]:
        if self.firebase is None:
            return True, None
        try:
            return True, getattr(self.firebase, method)(*args)
        except Exception as exc:  # keep local monitoring alive during network loss
            print(f"{utc_now()} firebase {method} failed: {exc}", flush=True)
            return False, None

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
        for ayah_ref in self.registration["scope_refs"]:
            for spec in artifact_specs(self.registration, ayah_ref):
                yield spec.path

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
        self.local.replace_artifacts(task, artifacts)
        remote_ok = True
        for artifact in artifacts:
            key = (task["task_id"], artifact["kind"])
            if self.synced_artifacts.get(key) == artifact["sha256"]:
                continue
            artifact_ok, _value = self._safe_remote("upsert_artifact", task, artifact)
            remote_ok = remote_ok and artifact_ok
            if artifact_ok:
                self.synced_artifacts[key] = artifact["sha256"]
        task_ok, _value = self._safe_remote("upsert_task", task)
        remote_ok = remote_ok and task_ok
        if remote_ok:
            self.pending_refs.discard(ayah_ref)
        else:
            self.pending_refs.add(ayah_ref)

    def tick(self) -> None:
        if not self.registration_synced:
            registered, remote_desired = self._safe_remote("register", self.registration)
            self.registration_synced = registered
            if registered:
                self._mirror_control(remote_desired)
        _desired_ok, desired = self._safe_remote("desired_state", self.registration)
        self._mirror_control(desired)
        changed = self.changed_refs() | self.pending_refs
        for ayah_ref in sorted(changed, key=lambda ref: ref_parts(ref)):
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
        registered, remote_desired = self._safe_remote("register", self.registration)
        self.registration_synced = registered
        self._mirror_control(remote_desired or desired)
        self.local.flush()
        while True:
            self.tick()
            should_stop = self.stop_requested or stop_marker(self.registration).exists()
            if once or (should_stop and not self.pending_refs):
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


def _monitor_lock_path(registration: dict[str, Any]) -> Path:
    return _monitor_log_path(registration).with_suffix(".lock")


@contextmanager
def _exclusive_lock(path: Path) -> Iterable[None]:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as lock:
        try:
            import fcntl

            fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        except ImportError:
            pass
        try:
            yield
        finally:
            try:
                import fcntl

                fcntl.flock(lock.fileno(), fcntl.LOCK_UN)
            except ImportError:
                pass


def _read_monitor_pid(path: Path) -> int | None:
    try:
        value = path.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return None
    except OSError as exc:
        raise MonitorError(f"Cannot read monitor PID file {path}: {exc}") from exc
    try:
        pid = int(value)
    except ValueError as exc:
        raise MonitorError(f"Invalid monitor PID file: {path}") from exc
    if pid <= 1:
        raise MonitorError(f"Invalid monitor PID file: {path}")
    return pid


def _process_exists(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def _is_expected_monitor_process(pid: int, registration: dict[str, Any]) -> bool:
    expected_script = str(Path(__file__).resolve())
    expected_registration = str(
        registration_path(
            registration["run_id"], registration["orchestrator_id"]
        ).resolve()
    )
    try:
        result = subprocess.run(
            ["ps", "-p", str(pid), "-o", "command="],
            capture_output=True,
            check=False,
            text=True,
            timeout=2,
        )
    except (OSError, subprocess.SubprocessError):
        return False
    command = result.stdout.strip()
    return (
        result.returncode == 0
        and expected_script in command
        and expected_registration in command
        and " run " in f" {command} "
    )


def create_registration(
    args: argparse.Namespace, *, orchestrator_id: str | None = None
) -> tuple[Path, dict[str, Any]]:
    run_id = validate_id(args.run_id, "run ID")
    worker_id = validate_id(args.worker_id or socket.gethostname().split(".")[0], "worker ID")
    orchestrator_id = validate_id(
        orchestrator_id
        or args.orchestrator_id
        or f"orch-{datetime.now(UTC).strftime('%Y%m%dT%H%M%S')}-{uuid.uuid4().hex[:8]}",
        "orchestrator ID",
    )
    analysis_id = validate_id(args.analysis_id, "analysis ID")
    scope_refs = expand_scope(args.scope)
    if args.poll_seconds <= 0:
        raise MonitorError("--poll-seconds must be greater than zero")
    passcode = (args.passcode or "").strip()
    if not args.local_only and len(passcode) < 12:
        raise MonitorError("--passcode or V5_MONITOR_PASSCODE must be at least 12 characters")
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
        "firebase_api_key": args.firebase_api_key,
        "firebase_passcode_hash": (
            hashlib.sha256(passcode.encode("utf-8")).hexdigest() if passcode else None
        ),
    }
    path = registration_path(run_id, orchestrator_id)
    _atomic_write_json(path, registration)
    return path, registration


def command_start(args: argparse.Namespace) -> int:
    if not args.local_only:
        if not args.firebase_project:
            raise MonitorError("--firebase-project is required unless --local-only is used")
        if not args.firebase_api_key:
            raise MonitorError("--firebase-api-key is required unless --local-only is used")
    run_id = validate_id(args.run_id, "run ID")
    orchestrator_id = validate_id(
        args.orchestrator_id
        or f"orch-{datetime.now(UTC).strftime('%Y%m%dT%H%M%S')}-{uuid.uuid4().hex[:8]}",
        "orchestrator ID",
    )
    identity = {"run_id": run_id, "orchestrator_id": orchestrator_id}
    with _exclusive_lock(_monitor_lock_path(identity)):
        existing_pid = _read_monitor_pid(_pid_path(identity))
        if existing_pid is not None and _process_exists(existing_pid):
            raise MonitorError(
                f"Monitor is already running for {run_id}/{orchestrator_id} "
                f"as process {existing_pid}"
            )
        if existing_pid is not None:
            _pid_path(identity).unlink(missing_ok=True)

        path, registration = create_registration(
            args, orchestrator_id=orchestrator_id
        )
        stop_marker(registration).unlink(missing_ok=True)
        remote_desired: str | None = None
        remote: FirebaseRestSink | None = None
        if not args.local_only:
            passcode_hash = registration.get("firebase_passcode_hash")
            if not passcode_hash:
                raise MonitorError("Registration has no Firebase passcode hash")
            remote = FirebaseRestSink(
                str(registration["firebase_project_id"]),
                str(registration["firebase_api_key"]),
                str(passcode_hash),
            )
            remote_desired = remote.register(registration)
            if remote_desired == "paused":
                _atomic_write_text(control_marker(registration), f"paused_at={utc_now()}\n")
            elif remote_desired == "running":
                control_marker(registration).unlink(missing_ok=True)
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
        try:
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
        except OSError:
            if remote is not None:
                try:
                    remote.close(registration, utc_now())
                except Exception:
                    pass
            raise
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
                "remote_desired_state": remote_desired,
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
        api_key = registration.get("firebase_api_key")
        passcode_hash = registration.get("firebase_passcode_hash")
        if not project_id or not api_key or not passcode_hash:
            raise MonitorError("Registration has incomplete Firebase API credentials")
        firebase = FirebaseRestSink(project_id, api_key, passcode_hash)
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
        owns_pid_file = False
        try:
            if pid_path.read_text(encoding="utf-8").strip() == str(os.getpid()):
                owns_pid_file = True
                pid_path.unlink(missing_ok=True)
        except OSError:
            pass
        if owns_pid_file:
            stop_marker(registration).unlink(missing_ok=True)
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
    directory = event_path(registration, args.ayah_ref, args.role, args.lane, 1).parent
    directory.mkdir(parents=True, exist_ok=True)
    lock_path = directory / f".{_event_task_name(args.role, args.lane)}.lock"
    with lock_path.open("a", encoding="utf-8") as lock:
        try:
            import fcntl

            fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        except ImportError:
            pass
        attempt = resolve_attempt(
            registration,
            args.ayah_ref,
            args.role,
            args.lane,
            args.status,
            args.agent_id,
            args.attempt,
        )
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
            "attempt": attempt,
            "message": args.message,
        }
        destination = event_path(
            registration, args.ayah_ref, args.role, args.lane, attempt
        )
        _append_jsonl(destination, event)
        try:
            import fcntl

            fcntl.flock(lock.fileno(), fcntl.LOCK_UN)
        except ImportError:
            pass
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


def command_stop(args: argparse.Namespace) -> int:
    registration = load_registration(
        registration_path(args.run_id, args.orchestrator_id)
    )
    pid_path = _pid_path(registration)
    with _exclusive_lock(_monitor_lock_path(registration)):
        pid = _read_monitor_pid(pid_path)
        if pid is None or not _process_exists(pid):
            pid_path.unlink(missing_ok=True)
            stop_marker(registration).unlink(missing_ok=True)
            print(
                json.dumps(
                    {
                        "status": "stopped",
                        "run_id": registration["run_id"],
                        "orchestrator_id": registration["orchestrator_id"],
                        "already_stopped": True,
                    },
                    indent=2,
                    sort_keys=True,
                )
            )
            return 0
        _atomic_write_text(stop_marker(registration), f"stop_requested_at={utc_now()}\n")
        if _is_expected_monitor_process(pid, registration):
            try:
                os.kill(pid, signal.SIGTERM)
            except ProcessLookupError:
                pid_path.unlink(missing_ok=True)
                stop_marker(registration).unlink(missing_ok=True)
            except PermissionError:
                pass
        deadline = time.monotonic() + args.timeout_seconds
        while pid_path.exists() and time.monotonic() < deadline:
            if not _process_exists(pid):
                pid_path.unlink(missing_ok=True)
                stop_marker(registration).unlink(missing_ok=True)
                break
            time.sleep(0.2)
        if pid_path.exists():
            raise MonitorError(
                f"Monitor process {pid} is still completing its final sync; "
                f"the stop request remains at {stop_marker(registration)}"
            )
    print(
        json.dumps(
            {
                "status": "stopped",
                "run_id": registration["run_id"],
                "orchestrator_id": registration["orchestrator_id"],
                "pid": pid,
            },
            indent=2,
            sort_keys=True,
        )
    )
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
    start.add_argument(
        "--firebase-project",
        default=os.environ.get("FIREBASE_PROJECT_ID", DEFAULT_FIREBASE_PROJECT_ID),
    )
    start.add_argument(
        "--firebase-api-key",
        default=os.environ.get("FIREBASE_API_KEY", DEFAULT_FIREBASE_API_KEY),
    )
    start.add_argument("--passcode", default=os.environ.get("V5_MONITOR_PASSCODE"))
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
    event.add_argument(
        "--attempt",
        type=int,
        help="Override the automatically assigned or matched attempt number.",
    )
    event.add_argument("--status", choices=sorted(EVENTS), required=True)
    event.add_argument("--agent-id")
    event.add_argument("--message")
    event.set_defaults(func=command_event)

    wait = subparsers.add_parser("wait", help="Block locally while pause is requested.")
    wait.add_argument("--run-id", required=True)
    wait.add_argument("--orchestrator-id", required=True)
    wait.add_argument("--poll-seconds", type=float, default=10)
    wait.set_defaults(func=command_wait)

    stop = subparsers.add_parser("stop", help="Stop a background monitor.")
    stop.add_argument("--run-id", required=True)
    stop.add_argument("--orchestrator-id", required=True)
    stop.add_argument("--timeout-seconds", type=float, default=45)
    stop.set_defaults(func=command_stop)

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
