#!/usr/bin/env python3
"""Build, submit, and collect V8 discovery-only OpenAI Batch jobs."""

from __future__ import annotations

import argparse
import hashlib
import http.client
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from typing import Any, Iterable
from urllib import error as urlerror
from urllib import parse as urlparse
from urllib import request as urlrequest
import uuid


V8_ROOT = Path(__file__).resolve().parent
REPO_ROOT = V8_ROOT.parents[1]
BATCH_ROOT = V8_ROOT / "batches"
MODEL = "gpt-5.6-luna"
LANES = ("micro", "macro", "global")
DISCOVERY_SCHEMA_VERSION = "commentary-v5-scope-discovery-v1"
MANIFEST_SCHEMA_VERSION = "commentary-v8-batch-discovery-manifest-v1"
SUBMISSION_SCHEMA_VERSION = "commentary-v8-batch-discovery-submission-v1"
MAX_BATCH_FILE_BYTES = 195_000_000
API_BATCH_FILE_LIMIT_BYTES = 200_000_000
MAX_BATCH_REQUESTS = 50_000
MAX_OUTPUT_TOKENS = 128_000
API_BASE = "https://api.openai.com"

sys.path.insert(0, str(REPO_ROOT))
from _commentary.v8_batch import workflow  # noqa: E402


class BatchError(RuntimeError):
    """Raised when a batch artifact or API response violates the contract."""


def _json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n").encode(
        "utf-8"
    )


def _pretty_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode(
        "utf-8"
    )


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _atomic_write(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as handle:
        temporary = Path(handle.name)
        handle.write(payload)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, path)


def _repo_path(path: Path) -> str:
    try:
        return path.resolve(strict=False).relative_to(REPO_ROOT).as_posix()
    except ValueError as exc:
        raise BatchError(f"Path is outside the repository: {path}") from exc


def _resolve_repo_path(value: str) -> Path:
    path = (REPO_ROOT / value).resolve(strict=False)
    try:
        path.relative_to(REPO_ROOT)
    except ValueError as exc:
        raise BatchError(f"Manifest path escapes the repository: {value!r}") from exc
    return path


def _safe_name(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-.")
    if not cleaned:
        raise BatchError("Batch name has no safe filename characters")
    return cleaned[:100]


def _custom_id(analysis_id: str, ayah_ref: str, lane: str) -> str:
    identity = f"{analysis_id}|{ayah_ref}|{lane}"
    digest = hashlib.sha256(identity.encode("utf-8")).hexdigest()[:12]
    surah, ayah = ayah_ref.split(":", 1)
    return f"s{int(surah):03d}-a{int(ayah):03d}-{lane}-{digest}"


def _tool() -> dict[str, Any]:
    return {
        "type": "function",
        "name": "write_discovery_json",
        "description": (
            "Return the single discovery JSON object requested by the supplied "
            "commentary discovery prompt at its exact destination path."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "document": {"type": "object"},
            },
            "required": ["path", "document"],
            "additionalProperties": False,
        },
    }


def _request_body(prompt: str) -> dict[str, Any]:
    return {
        "model": MODEL,
        "input": prompt,
        "reasoning": {"effort": "max"},
        "max_output_tokens": MAX_OUTPUT_TOKENS,
        "store": False,
        "tools": [_tool()],
        "tool_choice": {"type": "function", "name": "write_discovery_json"},
        "parallel_tool_calls": False,
    }


def _request_record(
    *, custom_id: str, prompt: str
) -> dict[str, Any]:
    return {
        "custom_id": custom_id,
        "method": "POST",
        "url": "/v1/responses",
        "body": _request_body(prompt),
    }


def _manifest_record(
    *, analysis_id: str, ayah_ref: str, lane: str, part: str
) -> dict[str, Any]:
    layout = workflow.layout_for(ayah_ref, analysis_id)
    prompt_path = layout.scope_prompt(lane)
    if not prompt_path.is_file():
        raise BatchError(
            f"Missing prepared discovery prompt: {_repo_path(prompt_path)}. "
            "Run workflow.py prepare first."
        )
    return {
        "custom_id": _custom_id(analysis_id, ayah_ref, lane),
        "analysis_id": analysis_id,
        "ayah_ref": ayah_ref,
        "lane": lane,
        "part": part,
        "prompt_path": _repo_path(prompt_path),
        "prompt_sha256": _sha256(prompt_path),
        "discovery_output_path": _repo_path(layout.scope_discovery(lane)),
    }


def build(args: argparse.Namespace) -> dict[str, Any]:
    refs = workflow._expand_ayah_selectors(args.ayah)
    if not refs:
        raise BatchError("At least one ayah is required")
    if len(refs) != len(set(refs)):
        raise BatchError("Ayah selectors contain duplicate units")
    if not 1 <= args.max_file_bytes <= MAX_BATCH_FILE_BYTES:
        raise BatchError(
            f"--max-file-bytes must be between 1 and {MAX_BATCH_FILE_BYTES}"
        )
    name = _safe_name(args.name or f"{args.analysis_id}-discovery")
    batch_dir = Path(args.batch_dir).resolve(strict=False)
    try:
        batch_dir.relative_to(REPO_ROOT)
    except ValueError as exc:
        raise BatchError("--batch-dir must remain inside the repository") from exc
    batch_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = batch_dir / f"{name}.manifest.json"
    if manifest_path.exists() or any(batch_dir.glob(f"{name}.part-*.jsonl")):
        raise BatchError(
            f"Batch build artifacts already exist for {name!r}; choose a new --name"
        )

    records: list[dict[str, Any]] = []
    parts: list[dict[str, Any]] = []
    part_index = 0
    part_handle: Any | None = None
    part_path: Path | None = None
    part_bytes = 0
    part_requests = 0

    def close_part() -> None:
        nonlocal part_handle, part_path, part_bytes, part_requests
        if part_handle is None or part_path is None:
            return
        part_handle.flush()
        os.fsync(part_handle.fileno())
        part_handle.close()
        parts.append(
            {
                "path": _repo_path(part_path),
                "sha256": _sha256(part_path),
                "bytes": part_bytes,
                "requests": part_requests,
            }
        )
        part_handle = None
        part_path = None
        part_bytes = 0
        part_requests = 0

    try:
        for ayah_ref in refs:
            for lane in LANES:
                layout = workflow.layout_for(ayah_ref, args.analysis_id)
                prompt_path = layout.scope_prompt(lane)
                if not prompt_path.is_file():
                    raise BatchError(
                        f"Missing prepared discovery prompt: {_repo_path(prompt_path)}. "
                        "Run workflow.py prepare first."
                    )
                prompt = prompt_path.read_text(encoding="utf-8")
                custom_id = _custom_id(args.analysis_id, ayah_ref, lane)
                line = _json_bytes(_request_record(custom_id=custom_id, prompt=prompt))
                if len(line) > args.max_file_bytes:
                    raise BatchError(
                        f"One request exceeds the configured shard size: "
                        f"{ayah_ref} {lane} ({len(line)} bytes)"
                    )
                needs_new_part = (
                    part_handle is None
                    or part_bytes + len(line) > args.max_file_bytes
                    or part_requests >= MAX_BATCH_REQUESTS
                )
                if needs_new_part:
                    close_part()
                    part_index += 1
                    part_path = batch_dir / f"{name}.part-{part_index:03d}.jsonl"
                    part_handle = part_path.open("wb")
                assert part_handle is not None and part_path is not None
                part_handle.write(line)
                part_bytes += len(line)
                part_requests += 1
                records.append(
                    _manifest_record(
                        analysis_id=args.analysis_id,
                        ayah_ref=ayah_ref,
                        lane=lane,
                        part=_repo_path(part_path),
                    )
                )
    finally:
        close_part()

    manifest = {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "model": MODEL,
        "reasoning_effort": "max",
        "endpoint": "/v1/responses",
        "analysis_id": args.analysis_id,
        "ayah_refs": refs,
        "parts": parts,
        "requests": records,
    }
    _atomic_write(manifest_path, _pretty_bytes(manifest))
    return {
        "status": "built",
        "manifest": _repo_path(manifest_path),
        "parts": len(parts),
        "requests": len(records),
        "bytes": sum(item["bytes"] for item in parts),
    }


def _load_json_object(path: Path, label: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise BatchError(f"Cannot read {label} {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise BatchError(f"{label} must contain one JSON object: {path}")
    return value


def _load_manifest(path: Path) -> dict[str, Any]:
    manifest = _load_json_object(path, "manifest")
    if manifest.get("schema_version") != MANIFEST_SCHEMA_VERSION:
        raise BatchError("Manifest schema is missing or stale")
    requests = manifest.get("requests")
    parts = manifest.get("parts")
    if not isinstance(requests, list) or not isinstance(parts, list):
        raise BatchError("Manifest requests or parts are malformed")
    return manifest


def _verify_manifest_files(manifest: dict[str, Any]) -> None:
    for part in manifest["parts"]:
        if not isinstance(part, dict) or not isinstance(part.get("path"), str):
            raise BatchError("Manifest part is malformed")
        path = _resolve_repo_path(part["path"])
        if not path.is_file() or _sha256(path) != part.get("sha256"):
            raise BatchError(f"Batch request shard changed or is missing: {part['path']}")
        if path.stat().st_size > API_BATCH_FILE_LIMIT_BYTES:
            raise BatchError(f"Batch request shard exceeds 200 MB: {part['path']}")
    for item in manifest["requests"]:
        if not isinstance(item, dict) or not isinstance(item.get("prompt_path"), str):
            raise BatchError("Manifest request is malformed")
        prompt_path = _resolve_repo_path(item["prompt_path"])
        if not prompt_path.is_file() or _sha256(prompt_path) != item.get(
            "prompt_sha256"
        ):
            raise BatchError(
                f"Prepared discovery prompt changed after build: {item['prompt_path']}"
            )


class OpenAIClient:
    def __init__(self) -> None:
        token = os.environ.get("OPENAI_API_KEY")
        if not token:
            raise BatchError("OPENAI_API_KEY is not set")
        self.token = token
        self.base = os.environ.get("OPENAI_API_BASE", API_BASE).rstrip("/")
        parsed = urlparse.urlparse(self.base)
        if parsed.scheme != "https" or not parsed.netloc:
            raise BatchError("OPENAI_API_BASE must be an https URL")
        self.parsed = parsed

    def _url(self, path: str) -> str:
        prefix = self.parsed.path.rstrip("/")
        return f"{self.parsed.scheme}://{self.parsed.netloc}{prefix}{path}"

    def json_request(
        self, method: str, path: str, body: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        payload = None if body is None else json.dumps(body).encode("utf-8")
        headers = {"Authorization": f"Bearer {self.token}"}
        if payload is not None:
            headers["Content-Type"] = "application/json"
        request = urlrequest.Request(
            self._url(path), data=payload, headers=headers, method=method
        )
        try:
            with urlrequest.urlopen(request, timeout=120) as response:
                result = json.loads(response.read().decode("utf-8"))
        except (urlerror.URLError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise BatchError(f"OpenAI API {method} {path} failed: {exc}") from exc
        if not isinstance(result, dict):
            raise BatchError(f"OpenAI API {method} {path} returned a non-object")
        return result

    def bytes_request(self, path: str) -> bytes:
        request = urlrequest.Request(
            self._url(path),
            headers={"Authorization": f"Bearer {self.token}"},
            method="GET",
        )
        try:
            with urlrequest.urlopen(request, timeout=300) as response:
                return response.read()
        except urlerror.URLError as exc:
            raise BatchError(f"OpenAI API GET {path} failed: {exc}") from exc

    def upload_batch_file(self, path: Path) -> dict[str, Any]:
        boundary = f"----commentary-v8-{uuid.uuid4().hex}"
        preamble = (
            f"--{boundary}\r\n"
            'Content-Disposition: form-data; name="purpose"\r\n\r\n'
            "batch\r\n"
            f"--{boundary}\r\n"
            f'Content-Disposition: form-data; name="file"; filename="{path.name}"\r\n'
            "Content-Type: application/jsonl\r\n\r\n"
        ).encode("utf-8")
        ending = f"\r\n--{boundary}--\r\n".encode("utf-8")
        content_length = len(preamble) + path.stat().st_size + len(ending)
        prefix = self.parsed.path.rstrip("/")
        connection = http.client.HTTPSConnection(self.parsed.netloc, timeout=600)
        try:
            connection.putrequest("POST", f"{prefix}/v1/files")
            connection.putheader("Authorization", f"Bearer {self.token}")
            connection.putheader("Content-Type", f"multipart/form-data; boundary={boundary}")
            connection.putheader("Content-Length", str(content_length))
            connection.endheaders()
            connection.send(preamble)
            with path.open("rb") as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    connection.send(chunk)
            connection.send(ending)
            response = connection.getresponse()
            payload = response.read()
        except OSError as exc:
            raise BatchError(f"OpenAI file upload failed for {path}: {exc}") from exc
        finally:
            connection.close()
        try:
            result = json.loads(payload.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise BatchError(f"OpenAI file upload returned invalid JSON for {path}") from exc
        if response.status >= 300:
            raise BatchError(f"OpenAI file upload failed ({response.status}): {result}")
        if not isinstance(result, dict) or not isinstance(result.get("id"), str):
            raise BatchError(f"OpenAI file upload response is malformed: {result}")
        return result


def submit(args: argparse.Namespace) -> dict[str, Any]:
    manifest_path = Path(args.manifest).resolve(strict=True)
    manifest = _load_manifest(manifest_path)
    _verify_manifest_files(manifest)
    client = OpenAIClient()
    submission_path = manifest_path.with_name(
        manifest_path.name.removesuffix(".manifest.json") + ".submission.json"
    )
    if submission_path.exists():
        raise BatchError(
            f"Submission record already exists; refusing duplicate submission: "
            f"{_repo_path(submission_path)}"
        )
    submission: dict[str, Any] = {
        "schema_version": SUBMISSION_SCHEMA_VERSION,
        "manifest": _repo_path(manifest_path),
        "jobs": [],
    }
    _atomic_write(submission_path, _pretty_bytes(submission))
    for part in manifest["parts"]:
        path = _resolve_repo_path(part["path"])
        uploaded = client.upload_batch_file(path)
        batch = client.json_request(
            "POST",
            "/v1/batches",
            {
                "input_file_id": uploaded["id"],
                "endpoint": "/v1/responses",
                "completion_window": "24h",
                "metadata": {
                    "workflow": "commentary-v8-batch-discovery",
                    "manifest": manifest_path.name[:64],
                },
            },
        )
        if not isinstance(batch.get("id"), str):
            raise BatchError(f"Create-batch response is malformed: {batch}")
        submission["jobs"].append(
            {
                "part": part["path"],
                "input_file_id": uploaded["id"],
                "batch_id": batch["id"],
            }
        )
        _atomic_write(submission_path, _pretty_bytes(submission))
    return {
        "status": "submitted",
        "submission": _repo_path(submission_path),
        "jobs": submission["jobs"],
    }


def _load_submission(path: Path) -> dict[str, Any]:
    submission = _load_json_object(path, "submission")
    if submission.get("schema_version") != SUBMISSION_SCHEMA_VERSION:
        raise BatchError("Submission schema is missing or stale")
    if not isinstance(submission.get("jobs"), list):
        raise BatchError("Submission jobs are malformed")
    return submission


def status(args: argparse.Namespace) -> dict[str, Any]:
    submission = _load_submission(Path(args.submission).resolve(strict=True))
    client = OpenAIClient()
    jobs = []
    for job in submission["jobs"]:
        batch = client.json_request("GET", f"/v1/batches/{job['batch_id']}")
        jobs.append(
            {
                "part": job["part"],
                "batch_id": job["batch_id"],
                "status": batch.get("status"),
                "request_counts": batch.get("request_counts"),
                "errors": batch.get("errors"),
            }
        )
    return {"status": "ok", "jobs": jobs}


def _iter_jsonl(payload: bytes, label: str) -> Iterable[dict[str, Any]]:
    for line_number, raw_line in enumerate(payload.splitlines(), start=1):
        if not raw_line.strip():
            continue
        try:
            item = json.loads(raw_line.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise BatchError(f"{label} line {line_number} is invalid JSON: {exc}") from exc
        if not isinstance(item, dict):
            raise BatchError(f"{label} line {line_number} is not an object")
        yield item


def _extract_document(result: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    if result.get("error") is not None:
        raise BatchError(f"Batch request {result.get('custom_id')} failed: {result['error']}")
    response = result.get("response")
    if not isinstance(response, dict) or response.get("status_code") != 200:
        raise BatchError(
            f"Batch request {result.get('custom_id')} has no successful response"
        )
    body = response.get("body")
    if not isinstance(body, dict):
        raise BatchError(f"Batch response body is malformed: {result.get('custom_id')}")
    calls = [
        item
        for item in body.get("output", [])
        if isinstance(item, dict)
        and item.get("type") == "function_call"
        and item.get("name") == "write_discovery_json"
    ]
    if len(calls) != 1:
        raise BatchError(
            f"Batch response must contain exactly one discovery tool call: "
            f"{result.get('custom_id')}"
        )
    arguments = calls[0].get("arguments")
    if isinstance(arguments, str):
        try:
            arguments = json.loads(arguments)
        except json.JSONDecodeError as exc:
            raise BatchError(
                f"Discovery tool arguments are invalid JSON: {result.get('custom_id')}"
            ) from exc
    if not isinstance(arguments, dict):
        raise BatchError(
            f"Discovery tool arguments are malformed: {result.get('custom_id')}"
        )
    document = arguments.get("document")
    if not isinstance(document, dict):
        raise BatchError(f"Discovery document is not an object: {result.get('custom_id')}")
    usage = body.get("usage") if isinstance(body.get("usage"), dict) else {}
    return {"path": arguments.get("path"), "document": document}, usage


def _validate_document(
    document: dict[str, Any], *, ayah_ref: str, lane: str
) -> None:
    expected_fields = {
        "schema_version",
        "ayah_ref",
        "lane",
        "coverage_complete",
        "candidate_decisions",
        "findings",
        "friction_notes",
    }
    if set(document) != expected_fields:
        raise BatchError(f"{ayah_ref} {lane}: discovery top-level fields are malformed")
    if document.get("schema_version") != DISCOVERY_SCHEMA_VERSION:
        raise BatchError(f"{ayah_ref} {lane}: discovery schema version is stale")
    if document.get("ayah_ref") != ayah_ref or document.get("lane") != lane:
        raise BatchError(f"{ayah_ref} {lane}: discovery identity mismatch")
    if document.get("coverage_complete") is not True:
        raise BatchError(f"{ayah_ref} {lane}: discovery coverage is not complete")
    for field in ("candidate_decisions", "findings", "friction_notes"):
        if not isinstance(document.get(field), list):
            raise BatchError(f"{ayah_ref} {lane}: discovery {field} is not an array")
    finding_refs = []
    for finding in document["findings"]:
        if not isinstance(finding, dict):
            raise BatchError(f"{ayah_ref} {lane}: discovery finding is malformed")
        finding_ref = finding.get("finding_ref")
        if not isinstance(finding_ref, str) or not finding_ref.startswith(f"{lane}:"):
            raise BatchError(f"{ayah_ref} {lane}: discovery finding ref is malformed")
        finding_refs.append(finding_ref)
    if len(finding_refs) != len(set(finding_refs)):
        raise BatchError(f"{ayah_ref} {lane}: discovery finding refs are duplicated")


def _fill_composition(layout: workflow.Layout, lane: str) -> str:
    template = (workflow.PROMPTS_ROOT / "composition.md").read_text(encoding="utf-8")
    return workflow._render(
        template,
        {
            "@@AYAH_REF@@": layout.ayah_ref,
            "@@LANE@@": lane,
            "@@DISCOVERY_OUTPUT_PATH@@": _repo_path(layout.scope_discovery(lane)),
            "@@SCOPE_PROSE_OUTPUT_PATH@@": _repo_path(layout.scope_prose(lane)),
            "@@SCOPE_LEDGER_OUTPUT_PATH@@": _repo_path(layout.scope_ledger(lane)),
        },
        label=f"{lane} composition prompt",
    )


def _fill_replacement_handoff(layout: workflow.Layout, lane: str) -> str:
    template = (workflow.PROMPTS_ROOT / "composition-from-batch.md").read_text(
        encoding="utf-8"
    )
    return workflow._render(
        template,
        {
            "@@AYAH_REF@@": layout.ayah_ref,
            "@@LANE@@": lane,
            "@@DISCOVERY_PROMPT_PATH@@": _repo_path(layout.scope_prompt(lane)),
            "@@DISCOVERY_OUTPUT_PATH@@": _repo_path(layout.scope_discovery(lane)),
            "@@COMPOSITION_PROMPT_PATH@@": _repo_path(
                layout.input / f"{lane}.composition.prompt.md"
            ),
        },
        label=f"{lane} batch composition handoff",
    )


def _prepare_composition_handoffs(
    analysis_id: str, ayah_refs: Iterable[str]
) -> list[dict[str, Any]]:
    handoffs = []
    for ayah_ref in ayah_refs:
        layout = workflow.layout_for(ayah_ref, analysis_id)
        for lane in LANES:
            discovery_path = layout.scope_discovery(lane)
            if not discovery_path.is_file():
                raise BatchError(
                    f"Cannot prepare composition without discovery: {_repo_path(discovery_path)}"
                )
            composition_path = layout.input / f"{lane}.composition.prompt.md"
            handoff_path = layout.input / f"{lane}.composition-from-batch.prompt.md"
            _atomic_write(composition_path, _fill_composition(layout, lane).encode("utf-8"))
            _atomic_write(
                handoff_path, _fill_replacement_handoff(layout, lane).encode("utf-8")
            )
            handoffs.append(
                {
                    "ayah_ref": ayah_ref,
                    "lane": lane,
                    "prompt": _repo_path(handoff_path),
                    "launch_message": (
                        "Read and execute the complete batch-to-regular composition "
                        f"handoff at workspace path `{_repo_path(handoff_path)}`."
                    ),
                    "model": MODEL,
                    "reasoning_effort": "max",
                    "launch": "fresh_agent",
                    "follow_up": None,
                }
            )
    return handoffs


def _usage_cost(usage: dict[str, Any]) -> dict[str, float | int]:
    input_tokens = int(usage.get("input_tokens") or 0)
    output_tokens = int(usage.get("output_tokens") or 0)
    input_details = usage.get("input_tokens_details")
    cached_tokens = (
        int(input_details.get("cached_tokens") or 0)
        if isinstance(input_details, dict)
        else 0
    )
    cached_tokens = min(max(cached_tokens, 0), input_tokens)
    uncached_tokens = input_tokens - cached_tokens
    long_context = input_tokens > 272_000
    input_rate = 0.40 if long_context else 0.20
    cached_rate = 0.04 if long_context else 0.02
    output_rate = 1.80 if long_context else 1.20
    standard = (
        uncached_tokens * input_rate
        + cached_tokens * cached_rate
        + output_tokens * output_rate
    ) / 1_000_000
    return {
        "input_tokens": input_tokens,
        "cached_input_tokens": cached_tokens,
        "output_tokens": output_tokens,
        "standard_usd": standard,
        "batch_usd": standard / 2,
        "savings_usd": standard / 2,
    }


def collect(args: argparse.Namespace) -> dict[str, Any]:
    manifest_path = Path(args.manifest).resolve(strict=True)
    manifest = _load_manifest(manifest_path)
    submission = _load_submission(Path(args.submission).resolve(strict=True))
    if submission.get("manifest") != _repo_path(manifest_path):
        raise BatchError("Submission does not belong to this manifest")
    client = OpenAIClient()
    output_payloads = []
    job_statuses = []
    for job in submission["jobs"]:
        batch = client.json_request("GET", f"/v1/batches/{job['batch_id']}")
        job_statuses.append({"batch_id": job["batch_id"], "status": batch.get("status")})
        if batch.get("status") != "completed":
            raise BatchError(
                f"Batch {job['batch_id']} is {batch.get('status')!r}, not completed"
            )
        output_file_id = batch.get("output_file_id")
        if not isinstance(output_file_id, str):
            raise BatchError(f"Batch {job['batch_id']} has no output file")
        output_payloads.append(
            client.bytes_request(f"/v1/files/{output_file_id}/content")
        )

    expected = {item["custom_id"]: item for item in manifest["requests"]}
    parsed: dict[str, tuple[dict[str, Any], dict[str, Any]]] = {}
    for index, payload in enumerate(output_payloads, start=1):
        for result in _iter_jsonl(payload, f"batch output {index}"):
            custom_id = result.get("custom_id")
            if not isinstance(custom_id, str) or custom_id not in expected:
                raise BatchError(f"Unknown batch custom_id: {custom_id!r}")
            if custom_id in parsed:
                raise BatchError(f"Duplicate batch custom_id: {custom_id}")
            call, usage = _extract_document(result)
            item = expected[custom_id]
            if call["path"] != item["discovery_output_path"]:
                raise BatchError(
                    f"{custom_id}: tool destination disagrees with the manifest"
                )
            _validate_document(
                call["document"], ayah_ref=item["ayah_ref"], lane=item["lane"]
            )
            parsed[custom_id] = (call["document"], usage)
    missing = sorted(set(expected) - set(parsed))
    if missing:
        raise BatchError(f"Batch output is missing {len(missing)} request(s): {missing}")

    for custom_id, item in expected.items():
        document, _usage = parsed[custom_id]
        output_path = _resolve_repo_path(item["discovery_output_path"])
        _atomic_write(output_path, _pretty_bytes(document))

    handoffs = _prepare_composition_handoffs(
        manifest["analysis_id"], manifest["ayah_refs"]
    )
    totals = {
        "input_tokens": 0,
        "cached_input_tokens": 0,
        "output_tokens": 0,
        "standard_usd": 0.0,
        "batch_usd": 0.0,
        "savings_usd": 0.0,
    }
    for _document, usage in parsed.values():
        row = _usage_cost(usage)
        for key in totals:
            totals[key] += row[key]  # type: ignore[operator]
    for key in ("standard_usd", "batch_usd", "savings_usd"):
        totals[key] = round(float(totals[key]), 6)
    return {
        "status": "collected",
        "jobs": job_statuses,
        "discoveries": len(parsed),
        "composition_handoffs": handoffs,
        "discovery_cost": totals,
        "automatic_retry": False,
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    build_parser = subparsers.add_parser(
        "build", help="Build sharded Batch JSONL from exact prepared discovery prompts."
    )
    build_parser.add_argument("--analysis-id", required=True)
    build_parser.add_argument(
        "--ayah", action="extend", nargs="+", required=True, metavar="REF_OR_RANGE"
    )
    build_parser.add_argument("--name")
    build_parser.add_argument("--batch-dir", type=Path, default=BATCH_ROOT)
    build_parser.add_argument(
        "--max-file-bytes", type=int, default=MAX_BATCH_FILE_BYTES
    )
    build_parser.set_defaults(handler=build)

    submit_parser = subparsers.add_parser(
        "submit", help="Upload every request shard and create its 24h Batch job."
    )
    submit_parser.add_argument("--manifest", type=Path, required=True)
    submit_parser.set_defaults(handler=submit)

    status_parser = subparsers.add_parser("status", help="Read all Batch job states.")
    status_parser.add_argument("--submission", type=Path, required=True)
    status_parser.set_defaults(handler=status)

    collect_parser = subparsers.add_parser(
        "collect",
        help="Validate completed outputs, write discoveries, and prepare regular composition.",
    )
    collect_parser.add_argument("--manifest", type=Path, required=True)
    collect_parser.add_argument("--submission", type=Path, required=True)
    collect_parser.set_defaults(handler=collect)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        result = args.handler(args)
    except (BatchError, workflow.WorkflowError, OSError) as exc:
        print(json.dumps({"status": "error", "error": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
