#!/usr/bin/env python3
import argparse
import base64
import binascii
from decimal import Decimal, InvalidOperation, ROUND_CEILING
import fcntl
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
import wave


ENDPOINT = "https://texttospeech.googleapis.com/v1beta1/text:synthesize"
PROJECT_ID = "quran-roots"
SAMPLE_RATE = 24000
BYTES_PER_SAMPLE = 2
CHANNELS = 1
WAV_HEADER_BYTES = 44
MP3_BITRATE_BPS = "64000"
MP3_BITRATE_FFMPEG = "64k"
INPUT_COST_PER_MILLION_CHARS = Decimal("1")
OUTPUT_COST_PER_MILLION_CHARS = Decimal("20")
UNKNOWN_REMOTE_OUTCOMES = {"in_flight", "unknown"}
COLLECTION_SOURCE_KINDS = {
    "surah": "surah",
    "ayah": "ayah",
    "ayah-recitation": "ayah",
}
EXPECTED_AUDIO_CONFIG = {
    "audioEncoding": "LINEAR16",
    "pitch": 0,
    "speakingRate": 1,
}
EXPECTED_VOICE = {
    "languageCode": "tr-TR",
    "modelName": "gemini-3.1-flash-tts-preview",
    "name": "Rasalgethi",
}
CHUNK_ID_RE = re.compile(r"^sec-(?P<section>\d{3})-p-(?P<paragraph>\d{3})$")
_REMOTE_AUTHORIZATION = object()


class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    """Do not let an API response redirect a request to another URL."""

    def redirect_request(self, request, fp, code, msg, headers, new_url):
        return None


NO_REDIRECT_OPENER = urllib.request.build_opener(NoRedirectHandler())


def reject_duplicate_json_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON object key: {key}")
        result[key] = value
    return result


def strict_json_loads(value):
    return json.loads(value, object_pairs_hook=reject_duplicate_json_keys)


def reject_symlink_components(path, field):
    """Reject existing symlinks before resolving an input collection path."""

    path = Path(path).expanduser()
    if not path.is_absolute():
        path = Path.cwd() / path
    current = Path(path.anchor)
    for part in path.parts[1:]:
        current /= part
        if current.is_symlink():
            raise ValueError(f"Refusing symlinked {field} component: {current}")


def atomic_write_bytes(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_name(f".{path.name}.tmp")
    tmp_path.write_bytes(payload)
    os.replace(tmp_path, path)


def atomic_write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_name(f".{path.name}.tmp")
    tmp_path.write_text(text, encoding="utf-8")
    os.replace(tmp_path, path)


def stable_json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_bytes(payload):
    return hashlib.sha256(payload).hexdigest()


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def safe_relative_path(root, value, field):
    if not isinstance(value, str) or not value:
        raise ValueError(f"{field} must be a non-empty relative path")
    if "\\" in value:
        raise ValueError(f"{field} must use forward-slash relative paths: {value}")
    relative = PurePosixPath(value)
    if relative.is_absolute() or any(part in ("", ".", "..") for part in relative.parts):
        raise ValueError(f"Unsafe {field} path: {value}")
    root = root.resolve()
    candidate = root
    for part in relative.parts:
        candidate /= part
        if candidate.is_symlink():
            raise ValueError(f"Symlinked {field} path is not allowed: {value}")
    resolved = candidate.resolve()
    try:
        resolved.relative_to(root)
    except ValueError as error:
        raise ValueError(f"{field} escapes the collection: {value}") from error
    return resolved


def canonical_chunk_paths(chunk_id):
    if not isinstance(chunk_id, str):
        raise ValueError(f"Chunk id must be a string: {chunk_id!r}")
    match = CHUNK_ID_RE.fullmatch(chunk_id)
    if not match:
        raise ValueError(f"Invalid chunk id: {chunk_id}")
    return {
        "request": f"requests/{chunk_id}.json",
        "response": f"responses/{chunk_id}.json",
        "wav": f"originals/wav/{chunk_id}.wav",
        "mp3": f"originals/mp3/{chunk_id}.mp3",
    }


def canonical_section_paths(section_index):
    if not isinstance(section_index, int) or section_index < 1:
        raise ValueError(f"Invalid section index: {section_index}")
    return {
        "wav": f"sections/wav/sec-{section_index:03d}.wav",
        "mp3": f"sections/mp3/sec-{section_index:03d}.mp3",
    }


def validate_chunk_paths(surah_dir, chunk):
    chunk_id = chunk.get("chunkId")
    expected = canonical_chunk_paths(chunk_id)
    paths = {}
    for field, expected_value in expected.items():
        if chunk.get(field) != expected_value:
            raise ValueError(
                f"{chunk_id} has non-canonical {field} path: "
                f"{chunk.get(field)!r}; expected {expected_value!r}"
            )
        paths[field] = safe_relative_path(surah_dir, expected_value, f"{chunk_id}.{field}")
    return paths


def load_manifest(path):
    if path.is_symlink():
        raise ValueError(f"Refusing symlinked manifest: {path}")
    try:
        manifest = strict_json_loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ValueError(f"Missing required artifact: {path}") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid manifest JSON: {path}: {error}") from error
    if not isinstance(manifest, dict):
        raise ValueError(f"Manifest must be a JSON object: {path}")
    return manifest


def validate_manifest_and_chunks(surah_dir, manifest, chunks):
    surah_dir = surah_dir.resolve()
    if not surah_dir.is_dir():
        raise ValueError(f"Collection directory does not exist: {surah_dir}")
    if not re.fullmatch(r"S\d{3}", surah_dir.name):
        raise ValueError(f"Collection directory must be named SNNN: {surah_dir}")
    if manifest.get("surahId") != surah_dir.name:
        raise ValueError("Manifest surahId does not match the collection directory")
    if manifest.get("chunksJsonl") != "chunks.jsonl":
        raise ValueError("Manifest must point to the canonical chunks.jsonl")
    if manifest.get("chunkCount") != len(chunks):
        raise ValueError("Manifest chunkCount does not match chunks.jsonl")
    source_kind = manifest.get("sourceKind")
    if source_kind not in {"surah", "ayah"}:
        raise ValueError("Manifest has an unsupported sourceKind")
    collection = manifest.get("collection")
    if COLLECTION_SOURCE_KINDS.get(collection) != source_kind:
        raise ValueError("Manifest collection does not match sourceKind")
    if manifest.get("voice") != EXPECTED_VOICE:
        raise ValueError("Manifest voice does not match the approved TTS voice")
    if manifest.get("audioConfig") != EXPECTED_AUDIO_CONFIG:
        raise ValueError("Manifest audioConfig does not match the approved TTS config")
    if not isinstance(manifest.get("prompt"), str) or not manifest["prompt"].strip():
        raise ValueError("Manifest is missing prompt")
    if not isinstance(manifest.get("promptSha256"), str):
        raise ValueError("Manifest is missing promptSha256")
    if sha256_text(manifest["prompt"]) != manifest["promptSha256"]:
        raise ValueError("Manifest prompt hash does not match prompt")

    sections = manifest.get("sections")
    if not isinstance(sections, list) or not sections:
        raise ValueError("Manifest has no sections")
    expected_section_indexes = list(range(1, len(sections) + 1))
    actual_section_indexes = [section.get("sectionIndex") for section in sections]
    if actual_section_indexes != expected_section_indexes:
        raise ValueError("Manifest section indexes are not consecutive")

    chunk_ids = []
    chunk_by_id = {}
    for chunk in chunks:
        if not isinstance(chunk, dict):
            raise ValueError("Every chunk record must be a JSON object")
        chunk_id = chunk.get("chunkId")
        if chunk_id in chunk_by_id:
            raise ValueError(f"Duplicate chunk id: {chunk_id}")
        validate_chunk_paths(surah_dir, chunk)
        chunk_match = CHUNK_ID_RE.fullmatch(chunk_id)
        if chunk.get("surahId") != surah_dir.name:
            raise ValueError(f"{chunk_id} surahId does not match the collection directory")
        if chunk.get("sourceKind") != source_kind:
            raise ValueError(f"{chunk_id} sourceKind does not match the manifest")
        if not isinstance(chunk.get("ttsText"), str) or not chunk["ttsText"].strip():
            raise ValueError(f"{chunk_id} has empty ttsText")
        if chunk.get("ttsCharCount") != len(chunk["ttsText"]):
            raise ValueError(f"{chunk_id} ttsCharCount does not match ttsText")
        section_index = chunk.get("sectionIndex")
        paragraph_index = chunk.get("paragraphIndex")
        if type(section_index) is not int or type(paragraph_index) is not int:
            raise ValueError(f"{chunk_id} has non-integer section/paragraph indexes")
        if section_index < 1 or paragraph_index < 1:
            raise ValueError(f"{chunk_id} has invalid section/paragraph indexes")
        if int(chunk_match.group("section")) != section_index or int(
            chunk_match.group("paragraph")
        ) != paragraph_index:
            raise ValueError(f"{chunk_id} does not encode its section/paragraph indexes")
        for field in (
            "requestSha256",
            "textSha256",
            "promptSha256",
            "voiceSha256",
            "audioConfigSha256",
        ):
            if not isinstance(chunk.get(field), str) or not chunk[field]:
                raise ValueError(f"{chunk_id} is missing {field}")
        remote_outcome = chunk.get("remoteOutcome")
        if remote_outcome is not None and remote_outcome not in UNKNOWN_REMOTE_OUTCOMES:
            raise ValueError(f"{chunk_id} has an unsupported remoteOutcome: {remote_outcome}")
        chunk_ids.append(chunk_id)
        chunk_by_id[chunk_id] = chunk

    manifest_ids = []
    for section in sections:
        if not isinstance(section, dict):
            raise ValueError("Every manifest section must be a JSON object")
        section_index = section.get("sectionIndex")
        if type(section_index) is not int or section_index < 1:
            raise ValueError("Manifest sectionIndex must be a positive integer")
        section_paths = canonical_section_paths(section_index)
        for field, expected in section_paths.items():
            if section.get(field) != expected:
                raise ValueError(
                    f"Section {section['sectionIndex']} has non-canonical {field} path"
                )
            safe_relative_path(surah_dir, expected, f"section.{field}")
        paragraphs = section.get("paragraphs")
        if not isinstance(paragraphs, list) or not paragraphs:
            raise ValueError(f"Section {section['sectionIndex']} has no paragraphs")
        for expected_paragraph_index, paragraph in enumerate(paragraphs, start=1):
            if not isinstance(paragraph, dict):
                raise ValueError(f"Section {section['sectionIndex']} has a non-object paragraph")
            chunk_id = paragraph.get("chunkId")
            if chunk_id not in chunk_by_id:
                raise ValueError(f"Manifest references unknown chunk: {chunk_id}")
            if chunk_id in manifest_ids:
                raise ValueError(f"Manifest references chunk twice: {chunk_id}")
            chunk = chunk_by_id[chunk_id]
            if paragraph.get("paragraphIndex") != expected_paragraph_index:
                raise ValueError(f"Manifest paragraph order is invalid in section {section_index}")
            for field in (
                "paragraphIndex",
                "kind",
                "text",
                "ttsText",
                "ttsCharCount",
                "request",
                "response",
                "wav",
                "mp3",
                "remoteOutcome",
            ):
                if paragraph.get(field) != chunk.get(field):
                    raise ValueError(f"Manifest paragraph {chunk_id} disagrees on {field}")
            if chunk["sectionIndex"] != section["sectionIndex"]:
                raise ValueError(f"Chunk {chunk_id} is in the wrong manifest section")
            manifest_ids.append(chunk_id)

    if manifest_ids != chunk_ids:
        raise ValueError("Manifest paragraph order does not match chunks.jsonl")

    for chunk in chunks:
        validate_request_file(
            safe_relative_path(surah_dir, chunk["request"], f"{chunk['chunkId']}.request"),
            chunk,
            manifest,
        )
    return chunk_by_id


def request_set_digest(chunks, request_bodies):
    """Digest the exact ordered POST bodies with unambiguous boundaries."""

    digest = hashlib.sha256()
    for chunk in chunks:
        body = request_bodies.get(chunk["chunkId"])
        if not isinstance(body, bytes):
            raise ValueError(f"Missing frozen request body: {chunk['chunkId']}")
        digest.update(len(body).to_bytes(8, "big"))
        digest.update(body)
    return digest.hexdigest()


def cost_estimate(char_count, rate):
    if not rate.is_finite() or rate <= 0:
        raise ValueError("Cost rate must be finite and greater than zero")
    return (
        Decimal(char_count) * rate / Decimal(1_000_000)
    ).quantize(Decimal("0.000001"), rounding=ROUND_CEILING)


def estimate_request_costs(chunks, manifest):
    prompt = manifest.get("prompt")
    if not isinstance(prompt, str):
        raise ValueError("Manifest prompt is required for input cost estimation")
    output_chars = sum(chunk["ttsCharCount"] for chunk in chunks)
    input_chars = sum(len(prompt) + chunk["ttsCharCount"] for chunk in chunks)
    input_cost = cost_estimate(input_chars, INPUT_COST_PER_MILLION_CHARS)
    output_cost = cost_estimate(output_chars, OUTPUT_COST_PER_MILLION_CHARS)
    return {
        "inputChars": input_chars,
        "outputChars": output_chars,
        "inputCostUsd": input_cost,
        "outputCostUsd": output_cost,
        "totalCostUsd": input_cost + output_cost,
    }


class CollectionLock:
    def __init__(self, surah_dir):
        self.path = surah_dir / ".tts-generation.lock"
        self.handle = None

    def __enter__(self):
        if self.path.is_symlink():
            raise ValueError(f"Refusing symlinked collection lock: {self.path}")
        self.handle = self.path.open("a+", encoding="utf-8")
        try:
            fcntl.flock(self.handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            self.handle.close()
            self.handle = None
            raise RuntimeError(f"Another TTS process holds the collection lock: {self.path}") from error
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.handle is not None:
            fcntl.flock(self.handle.fileno(), fcntl.LOCK_UN)
            self.handle.close()
            self.handle = None


def load_jsonl(path):
    records = []
    if path.is_symlink():
        raise ValueError(f"Refusing symlinked chunks file: {path}")
    try:
        with path.open(encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                try:
                    record = strict_json_loads(line)
                except json.JSONDecodeError as error:
                    raise ValueError(f"Invalid JSON in {path}:{line_number}: {error}") from error
                if not isinstance(record, dict):
                    raise ValueError(f"Expected an object in {path}:{line_number}")
                records.append(record)
    except FileNotFoundError as error:
        raise ValueError(f"Missing required artifact: {path}") from error
    if not records:
        raise ValueError(f"No chunk records found in {path}")
    return records


def write_jsonl(path, records):
    atomic_write_text(
        path,
        "".join(json.dumps(record, ensure_ascii=False) + "\n" for record in records),
    )


def get_authorized_token(authorization=None):
    if authorization is not _REMOTE_AUTHORIZATION:
        raise PermissionError("Remote authorization is required before obtaining credentials")
    result = subprocess.run(
        ["gcloud", "auth", "print-access-token"],
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip()


def synthesize(request_body, token, chunk, generated_at, authorization=None):
    if authorization is not _REMOTE_AUTHORIZATION:
        raise PermissionError("Remote authorization is required before TTS synthesis")
    request = urllib.request.Request(
        ENDPOINT,
        data=request_body,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "x-goog-user-project": PROJECT_ID,
            "Content-Type": "application/json; charset=utf-8",
        },
    )
    try:
        with NO_REDIRECT_OPENER.open(request, timeout=180) as response:
            payload = response.read()
    except urllib.error.HTTPError as error:
        if 300 <= error.code < 400:
            raise RuntimeError(
                f"TTS endpoint returned redirect ({error.code}); refusing to follow it"
            ) from error
        payload = error.read()
    response = strict_json_loads(payload.decode("utf-8"))
    response["_generatedAt"] = generated_at
    return response


def wav_duration_seconds(path):
    with wave.open(str(path), "rb") as handle:
        if handle.getnchannels() != CHANNELS:
            raise ValueError(f"Unexpected channel count in {path}: {handle.getnchannels()}")
        if handle.getframerate() != SAMPLE_RATE:
            raise ValueError(f"Unexpected sample rate in {path}: {handle.getframerate()}")
        if handle.getsampwidth() != BYTES_PER_SAMPLE:
            raise ValueError(f"Unexpected sample width in {path}: {handle.getsampwidth()}")
        frames = handle.getnframes()
        if frames <= 0:
            raise ValueError(f"No audio frames in {path}")
        return frames / SAMPLE_RATE


def validate_wav_bytes(payload):
    with wave.open(io.BytesIO(payload), "rb") as handle:
        if handle.getnchannels() != CHANNELS:
            raise ValueError(f"Unexpected channel count: {handle.getnchannels()}")
        if handle.getframerate() != SAMPLE_RATE:
            raise ValueError(f"Unexpected sample rate: {handle.getframerate()}")
        if handle.getsampwidth() != BYTES_PER_SAMPLE:
            raise ValueError(f"Unexpected sample width: {handle.getsampwidth()}")
        if handle.getnframes() <= 0:
            raise ValueError("No audio frames")


def decode_audio_response(response):
    if "error" in response:
        return None
    audio_content = response.get("audioContent")
    if not audio_content:
        raise ValueError("Response has no audioContent")
    try:
        payload = base64.b64decode(audio_content, validate=True)
    except (binascii.Error, ValueError) as error:
        raise ValueError("Response audioContent is not valid base64") from error
    validate_wav_bytes(payload)
    return payload


def response_matches_chunk(response, chunk):
    if "error" in response:
        return False
    metadata = response.get("_requestMetadata")
    if not metadata:
        return False
    keys = (
        "requestSha256",
        "textSha256",
        "promptSha256",
        "voiceSha256",
        "audioConfigSha256",
    )
    return all(metadata.get(key) == chunk.get(key) for key in keys)


def request_metadata(chunk):
    return {
        key: chunk.get(key)
        for key in (
            "requestSha256",
            "textSha256",
            "promptSha256",
            "voiceSha256",
            "audioConfigSha256",
        )
    }


def validate_request_file(request_path, chunk, manifest=None):
    try:
        request = strict_json_loads(request_path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ValueError(f"Missing request file for {chunk['chunkId']}: {request_path}") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid request JSON for {chunk['chunkId']}: {error}") from error
    if not isinstance(request, dict):
        raise ValueError(f"Request must be a JSON object: {request_path}")
    if set(request) != {"audioConfig", "input", "voice"}:
        raise ValueError(f"Request has unexpected top-level fields: {request_path}")
    if request.get("audioConfig") != EXPECTED_AUDIO_CONFIG:
        raise ValueError(f"Request audioConfig is not allowlisted: {request_path}")
    if request.get("voice") != EXPECTED_VOICE:
        raise ValueError(f"Request voice is not allowlisted: {request_path}")
    input_block = request.get("input")
    if not isinstance(input_block, dict) or set(input_block) != {"prompt", "text"}:
        raise ValueError(f"Request input must contain only prompt and text: {request_path}")
    if not isinstance(input_block.get("prompt"), str) or not input_block["prompt"].strip():
        raise ValueError(f"Request prompt is empty: {request_path}")
    if not isinstance(input_block.get("text"), str):
        raise ValueError(f"Request text is not a string: {request_path}")
    request_sha256 = sha256_text(stable_json(request))
    if request_sha256 != chunk.get("requestSha256"):
        raise ValueError(
            f"{chunk['chunkId']} request hash mismatch: file={request_sha256} "
            f"chunk={chunk.get('requestSha256')}"
        )
    expected_text = chunk.get("ttsText")
    if not isinstance(expected_text, str) or not expected_text:
        raise ValueError(f"{chunk['chunkId']} has no valid ttsText")
    if request.get("input", {}).get("text") != expected_text:
        raise ValueError(f"{chunk['chunkId']} request text does not match chunk ttsText")
    if chunk.get("ttsCharCount") != len(expected_text):
        raise ValueError(f"{chunk['chunkId']} ttsCharCount does not match request text")
    if sha256_text(request.get("input", {}).get("prompt", "")) != chunk.get("promptSha256"):
        raise ValueError(f"{chunk['chunkId']} request prompt hash mismatch")
    if manifest is not None and chunk.get("promptSha256") != manifest.get("promptSha256"):
        raise ValueError(f"{chunk['chunkId']} prompt hash does not match manifest")
    if sha256_text(stable_json(request.get("voice"))) != chunk.get("voiceSha256"):
        raise ValueError(f"{chunk['chunkId']} request voice hash mismatch")
    if sha256_text(stable_json(request.get("audioConfig"))) != chunk.get("audioConfigSha256"):
        raise ValueError(f"{chunk['chunkId']} request audioConfig hash mismatch")


def update_manifest(manifest_path, records_by_chunk_id):
    manifest = load_manifest(manifest_path)
    for section in manifest.get("sections", []):
        for paragraph in section.get("paragraphs", []):
            record = records_by_chunk_id.get(paragraph.get("chunkId"))
            if not record:
                continue
            paragraph["wav"] = record.get("wav")
            paragraph["mp3"] = record.get("mp3")
            paragraph["durationSeconds"] = record.get("durationSeconds")
            paragraph["generatedAt"] = record.get("generatedAt")
            paragraph["audioSha256"] = record.get("audioSha256")
            paragraph["mp3Sha256"] = record.get("mp3Sha256")
            if record.get("remoteOutcome") is not None:
                paragraph["remoteOutcome"] = record["remoteOutcome"]
            else:
                paragraph.pop("remoteOutcome", None)
    atomic_write_text(
        manifest_path,
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
    )


def update_generation_state(manifest_path, status, request_digest=None, error=None):
    manifest = load_manifest(manifest_path)
    manifest["generationStatus"] = status
    if request_digest is not None:
        manifest["generationRequestSetSha256"] = request_digest
    if error:
        manifest["generationError"] = error
    else:
        manifest.pop("generationError", None)
    atomic_write_text(
        manifest_path,
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
    )


def load_response(path):
    if not path.exists():
        return None
    try:
        response = strict_json_loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid cached response JSON: {path}: {error}") from error
    if not isinstance(response, dict):
        raise ValueError(f"Cached response must be a JSON object: {path}")
    return response


def write_response(path, response, chunk):
    response = dict(response)
    response["_requestMetadata"] = request_metadata(chunk)
    atomic_write_text(path, json.dumps(response, ensure_ascii=False, indent=2) + "\n")


def materialize_wav_from_response(response, wav_path):
    audio = decode_audio_response(response)
    atomic_write_bytes(wav_path, audio)
    return round(wav_duration_seconds(wav_path), 3), sha256_bytes(audio)


def inspect_cached_chunk(surah_dir, chunk, paths):
    response_path = paths["response"]
    wav_path = paths["wav"]
    if response_path.exists():
        try:
            response = load_response(response_path)
            if not response_matches_chunk(response, chunk):
                return "mismatched_response"
            if "error" in response:
                return "error_response"
            audio = decode_audio_response(response)
        except (OSError, ValueError, json.JSONDecodeError):
            return "invalid_response"
        if wav_path.exists():
            try:
                if chunk.get("audioSha256") and sha256_bytes(wav_path.read_bytes()) != chunk.get("audioSha256"):
                    return "corrupt_wav"
                if chunk.get("durationSeconds") is not None and round(wav_duration_seconds(wav_path), 3) != chunk.get("durationSeconds"):
                    return "corrupt_wav"
            except (OSError, wave.Error, ValueError):
                return "corrupt_wav"
        elif not audio:
            return "invalid_response"
        return "verified_response"
    if wav_path.exists():
        return "orphaned_wav"
    return "missing"


def select_target_chunks(chunks, limit=None, chunk_ids=None):
    if limit is not None and chunk_ids:
        raise ValueError("--limit and --chunk-id are mutually exclusive")
    if chunk_ids is not None:
        if not chunk_ids:
            raise ValueError("At least one --chunk-id is required when selecting chunk IDs")
        requested = set()
        duplicates = []
        for chunk_id in chunk_ids:
            if chunk_id in requested:
                duplicates.append(chunk_id)
            requested.add(chunk_id)
        if duplicates:
            raise ValueError(
                "Duplicate --chunk-id values are not allowed: " + ", ".join(duplicates)
            )
        available = {chunk["chunkId"] for chunk in chunks}
        unknown = [chunk_id for chunk_id in chunk_ids if chunk_id not in available]
        if unknown:
            raise ValueError("Unknown --chunk-id values: " + ", ".join(unknown))
        # Preserve canonical chunks.jsonl order regardless of CLI argument order.
        return [chunk for chunk in chunks if chunk["chunkId"] in requested]
    if limit is not None and (limit <= 0 or limit > len(chunks)):
        raise ValueError(f"--limit must be between 1 and {len(chunks)}")
    return chunks[:limit] if limit is not None else chunks


def preflight_collection(
    surah_dir,
    limit=None,
    chunk_ids=None,
    force=False,
    reconcile_unknown=False,
):
    reject_symlink_components(surah_dir, "collection")
    surah_dir = surah_dir.expanduser().resolve()
    chunks_path = surah_dir / "chunks.jsonl"
    manifest_path = surah_dir / "manifest.json"
    if manifest_path.is_symlink() or chunks_path.is_symlink():
        raise ValueError("Manifest and chunks.jsonl must not be symlinks")
    manifest = load_manifest(manifest_path)
    chunks = load_jsonl(chunks_path)
    validate_manifest_and_chunks(surah_dir, manifest, chunks)
    request_bodies = {}
    for chunk in chunks:
        request_path = safe_relative_path(
            surah_dir, chunk["request"], f"{chunk['chunkId']}.request"
        )
        body = request_path.read_bytes()
        try:
            request = strict_json_loads(body)
        except json.JSONDecodeError as error:
            raise ValueError(f"Request changed to invalid JSON during preflight: {request_path}") from error
        if sha256_text(stable_json(request)) != chunk["requestSha256"]:
            raise ValueError(f"Request changed during preflight: {request_path}")
        request_bodies[chunk["chunkId"]] = body

    target_chunks = select_target_chunks(chunks, limit=limit, chunk_ids=chunk_ids)
    target_paths = {
        chunk["chunkId"]: validate_chunk_paths(surah_dir, chunk)
        for chunk in target_chunks
    }
    statuses = {
        chunk["chunkId"]: inspect_cached_chunk(
            surah_dir, chunk, target_paths[chunk["chunkId"]]
        )
        for chunk in target_chunks
    }
    unknown_chunks = [
        chunk
        for chunk in target_chunks
        if chunk.get("remoteOutcome") in UNKNOWN_REMOTE_OUTCOMES
    ]
    if unknown_chunks and not reconcile_unknown:
        unknown_ids = ", ".join(chunk["chunkId"] for chunk in unknown_chunks)
        raise ValueError(
            "A prior remote attempt has an unknown outcome for "
            f"{unknown_ids}; use --reconcile-unknown to explicitly permit a possible duplicate"
        )

    if force:
        remote_chunks = list(target_chunks)
    else:
        unsafe_cached = {
            chunk_id: status
            for chunk_id, status in statuses.items()
            if status not in {"missing", "verified_response"}
        }
        if unsafe_cached:
            details = ", ".join(f"{chunk_id}={status}" for chunk_id, status in unsafe_cached.items())
            raise ValueError(
                "Cached artifact state is ambiguous; use --force only with explicit "
                f"force confirmation to replace it: {details}"
            )
        remote_chunks = []
        for chunk in target_chunks:
            status = statuses[chunk["chunkId"]]
            if status == "missing" or (
                chunk.get("remoteOutcome") in UNKNOWN_REMOTE_OUTCOMES
                and status != "verified_response"
            ):
                remote_chunks.append(chunk)

    request_digest = request_set_digest(remote_chunks, request_bodies)
    costs = estimate_request_costs(remote_chunks, manifest)
    return {
        "surahDir": surah_dir,
        "manifestPath": manifest_path,
        "chunksPath": chunks_path,
        "manifest": manifest,
        "chunks": chunks,
        "targetChunks": target_chunks,
        "selection": (
            "chunk_ids"
            if chunk_ids is not None
            else "limit"
            if limit is not None
            else "all"
        ),
        "targetPaths": target_paths,
        "requestBodies": request_bodies,
        "statuses": statuses,
        "unknownChunks": unknown_chunks,
        "remoteChunks": remote_chunks,
        "requestDigest": request_digest,
        "ttsChars": costs["outputChars"],
        "inputChars": costs["inputChars"],
        "inputCostUsd": costs["inputCostUsd"],
        "outputCostUsd": costs["outputCostUsd"],
        "estimatedCostUsd": costs["totalCostUsd"],
    }


def require_remote_confirmation(args, preflight):
    remote_chunks = preflight["remoteChunks"]
    if not remote_chunks:
        return None
    if args.confirm_remote != preflight["requestDigest"]:
        raise PermissionError(
            "Remote confirmation must exactly match the preflight requestSetSha256: "
            f"{preflight['requestDigest']}"
        )
    expected_cost = preflight["estimatedCostUsd"]
    if args.confirm_cost_usd != expected_cost:
        raise PermissionError(
            "Remote cost confirmation does not match preflight: "
            f"expected {expected_cost}"
        )
    if args.max_cost_usd is None:
        raise PermissionError("Provide --max-cost-usd as an explicit spending ceiling")
    if expected_cost > args.max_cost_usd:
        raise PermissionError(
            f"Preflight cost {expected_cost} exceeds --max-cost-usd {args.max_cost_usd}"
        )
    if args.force and not args.confirm_force:
        raise PermissionError("--force requires the separate --confirm-force acknowledgement")
    return _REMOTE_AUTHORIZATION


def preflight_summary(preflight, dry_run):
    statuses = preflight["statuses"]
    summary = {
        "dryRun": dry_run,
        "surahDir": str(preflight["surahDir"]),
        "validatedChunks": len(preflight["chunks"]),
        "targetChunks": len(preflight["targetChunks"]),
        "remoteChunks": len(preflight["remoteChunks"]),
        "cachedChunks": sum(status == "verified_response" for status in statuses.values()),
        "unknownChunks": len(preflight["unknownChunks"]),
        "ttsChars": preflight["ttsChars"],
        "inputChars": preflight["inputChars"],
        "inputCostUsd": str(preflight["inputCostUsd"]),
        "outputCostUsd": str(preflight["outputCostUsd"]),
        "estimatedCostUsd": str(preflight["estimatedCostUsd"]),
        "requestSetSha256": preflight["requestDigest"],
        "remoteCalls": 0 if dry_run else len(preflight["remoteChunks"]),
    }
    if preflight["selection"] == "chunk_ids":
        summary["targetChunkIds"] = [
            chunk["chunkId"] for chunk in preflight["targetChunks"]
        ]
    return summary


def convert_wav_to_mp3(wav_path, mp3_path):
    ffmpeg = shutil.which("ffmpeg")
    afconvert = shutil.which("afconvert")
    if not ffmpeg and not afconvert:
        raise RuntimeError("ffmpeg or afconvert is required to create MP3 derivatives")
    mp3_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = mp3_path.with_name(f".{mp3_path.stem}.tmp.mp3")
    if tmp_path.exists():
        tmp_path.unlink()
    if ffmpeg:
        subprocess.run(
            [
                ffmpeg,
                "-y",
                "-hide_banner",
                "-loglevel",
                "error",
                "-i",
                str(wav_path),
                "-vn",
                "-codec:a",
                "libmp3lame",
                "-b:a",
                MP3_BITRATE_FFMPEG,
                str(tmp_path),
            ],
            check=True,
            text=True,
            capture_output=True,
        )
    else:
        subprocess.run(
            [
                afconvert,
                str(wav_path),
                str(tmp_path),
                "-f",
                "MPG3",
                "-d",
                ".mp3",
                "-b",
                MP3_BITRATE_BPS,
            ],
            check=True,
            text=True,
            capture_output=True,
        )
    os.replace(tmp_path, mp3_path)
    return sha256_bytes(mp3_path.read_bytes())


def join_wavs(input_paths, output_path):
    if not input_paths:
        return None, None
    output_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = output_path.with_name(f".{output_path.name}.tmp")
    params = None
    with wave.open(str(tmp_path), "wb") as output:
        for input_path in input_paths:
            with wave.open(str(input_path), "rb") as source:
                current_params = source.getparams()
                expected = (CHANNELS, BYTES_PER_SAMPLE, SAMPLE_RATE)
                actual = (
                    source.getnchannels(),
                    source.getsampwidth(),
                    source.getframerate(),
                )
                if actual != expected:
                    raise ValueError(f"Unexpected WAV params in {input_path}: {actual}")
                if params is None:
                    params = current_params
                    output.setparams(current_params)
                elif current_params[:3] != params[:3]:
                    raise ValueError(f"WAV params differ in {input_path}")
                output.writeframes(source.readframes(source.getnframes()))
    os.replace(tmp_path, output_path)
    return round(wav_duration_seconds(output_path), 3), sha256_bytes(output_path.read_bytes())


def materialize_original_mp3(surah_dir, chunk):
    paths = validate_chunk_paths(surah_dir, chunk)
    wav_path = paths["wav"]
    mp3_path = paths["mp3"]
    if not wav_path.exists():
        return
    chunk["mp3Sha256"] = convert_wav_to_mp3(wav_path, mp3_path)


def remove_file_if_exists(path):
    if path.exists():
        path.unlink()


def section_audio_paths(surah_dir, section):
    section_index = section["sectionIndex"]
    paths = canonical_section_paths(section_index)
    return paths["wav"], paths["mp3"], safe_relative_path(
        surah_dir, paths["wav"], "section.wav"
    ), safe_relative_path(surah_dir, paths["mp3"], "section.mp3")


def clear_section_derivative(surah_dir, section):
    section_wav_rel, section_mp3_rel, section_wav_path, section_mp3_path = section_audio_paths(
        surah_dir, section
    )
    remove_file_if_exists(section_wav_path)
    remove_file_if_exists(section_mp3_path)
    section["wav"] = section_wav_rel
    section["mp3"] = section_mp3_rel
    section["durationSeconds"] = None
    section.pop("wavSha256", None)
    section.pop("mp3Sha256", None)


def clear_affected_section_derivatives(surah_dir, manifest_path, affected_chunk_ids):
    manifest = load_manifest(manifest_path)
    affected_chunk_ids = set(affected_chunk_ids)
    for section in manifest.get("sections", []):
        section_chunk_ids = {
            paragraph.get("chunkId")
            for paragraph in section.get("paragraphs", [])
            if paragraph.get("chunkId")
        }
        if section_chunk_ids & affected_chunk_ids:
            clear_section_derivative(surah_dir, section)
    atomic_write_text(
        manifest_path,
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
    )


def chunk_has_verified_audio(chunk, wav_path):
    if not wav_path.exists() or chunk.get("durationSeconds") is None:
        return False
    stored_hash = chunk.get("audioSha256")
    if not stored_hash or sha256_bytes(wav_path.read_bytes()) != stored_hash:
        return False
    try:
        actual_duration = round(wav_duration_seconds(wav_path), 3)
    except (OSError, wave.Error, ValueError):
        return False
    return actual_duration == chunk.get("durationSeconds")


def build_section_derivatives(surah_dir, manifest_path, chunks, eligible_chunk_ids=None):
    manifest = load_manifest(manifest_path)
    chunks_by_id = {chunk["chunkId"]: chunk for chunk in chunks}
    for section in manifest.get("sections", []):
        paragraph_ids = [
            paragraph["chunkId"]
            for paragraph in section.get("paragraphs", [])
            if paragraph.get("chunkId")
        ]
        paragraph_chunks = [
            chunks_by_id[paragraph["chunkId"]]
            for paragraph in section.get("paragraphs", [])
            if paragraph.get("chunkId") in chunks_by_id
        ]
        if len(paragraph_chunks) != len(paragraph_ids):
            clear_section_derivative(surah_dir, section)
            continue
        if eligible_chunk_ids is not None:
            section_is_affected = any(
                chunk["chunkId"] in eligible_chunk_ids for chunk in paragraph_chunks
            )
            if not section_is_affected:
                continue
            if any(chunk["chunkId"] not in eligible_chunk_ids for chunk in paragraph_chunks):
                clear_section_derivative(surah_dir, section)
                continue
        wav_paths = [
            safe_relative_path(surah_dir, chunk["wav"], f"{chunk['chunkId']}.wav")
            for chunk in paragraph_chunks
        ]
        if not wav_paths or any(
            not chunk_has_verified_audio(chunk, path)
            for chunk, path in zip(paragraph_chunks, wav_paths)
        ):
            clear_section_derivative(surah_dir, section)
            continue
        section_wav_rel, section_mp3_rel, section_wav_path, section_mp3_path = section_audio_paths(
            surah_dir, section
        )
        duration_seconds, wav_sha256 = join_wavs(wav_paths, section_wav_path)
        mp3_sha256 = convert_wav_to_mp3(section_wav_path, section_mp3_path)
        section["wav"] = section_wav_rel
        section["mp3"] = section_mp3_rel
        section["durationSeconds"] = duration_seconds
        section["wavSha256"] = wav_sha256
        section["mp3Sha256"] = mp3_sha256
    atomic_write_text(
        manifest_path,
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
    )


def decimal_argument(value):
    try:
        number = Decimal(value)
    except (InvalidOperation, ValueError) as error:
        raise argparse.ArgumentTypeError(f"Invalid decimal: {value}") from error
    if not number.is_finite() or number < 0:
        raise argparse.ArgumentTypeError("Decimal values must be finite and non-negative")
    return number


def process_collection(preflight, args, authorization):
    surah_dir = preflight["surahDir"]
    manifest_path = preflight["manifestPath"]
    chunks_path = preflight["chunksPath"]
    chunks = preflight["chunks"]
    target_chunks = preflight["targetChunks"]
    target_ids = {chunk["chunkId"] for chunk in target_chunks}
    remote_chunks = preflight["remoteChunks"]
    processed = 0
    in_flight_chunk = None

    try:
        if remote_chunks:
            clear_affected_section_derivatives(surah_dir, manifest_path, target_ids)
            update_generation_state(
                manifest_path,
                "in_progress",
                preflight["requestDigest"],
            )
        token = get_authorized_token(authorization) if remote_chunks else None

        for index, chunk in enumerate(target_chunks, start=1):
            paths = preflight["targetPaths"][chunk["chunkId"]]
            status = preflight["statuses"][chunk["chunkId"]]
            if not args.force and status == "verified_response":
                response = load_response(paths["response"])
                duration_seconds, audio_sha256 = materialize_wav_from_response(
                    response, paths["wav"]
                )
                chunk["durationSeconds"] = duration_seconds
                chunk["audioSha256"] = audio_sha256
                chunk.pop("mp3Sha256", None)
                materialize_original_mp3(surah_dir, chunk)
                chunk["generatedAt"] = chunk.get("generatedAt") or response.get(
                    "_generatedAt"
                )
                chunk.pop("remoteOutcome", None)
                processed += 1
                continue

            print(f"{index}/{len(target_chunks)} {chunk['chunkId']}...", flush=True)
            generated_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            in_flight_chunk = chunk
            chunk["remoteOutcome"] = "in_flight"
            write_jsonl(chunks_path, chunks)
            update_manifest(manifest_path, {record["chunkId"]: record for record in chunks})
            response = synthesize(
                preflight["requestBodies"][chunk["chunkId"]],
                token,
                chunk,
                generated_at,
                authorization,
            )
            if "error" in response:
                raise RuntimeError(json.dumps(response["error"], ensure_ascii=False))

            # Validate the returned bytes before committing the response record.
            audio = decode_audio_response(response)
            atomic_write_bytes(paths["wav"], audio)
            chunk["durationSeconds"] = round(wav_duration_seconds(paths["wav"]), 3)
            chunk["audioSha256"] = sha256_bytes(audio)
            chunk.pop("mp3Sha256", None)
            write_response(paths["response"], response, chunk)
            materialize_original_mp3(surah_dir, chunk)
            chunk["generatedAt"] = generated_at
            chunk.pop("remoteOutcome", None)
            write_jsonl(chunks_path, chunks)
            update_manifest(manifest_path, {record["chunkId"]: record for record in chunks})
            in_flight_chunk = None
            processed += 1

        write_jsonl(chunks_path, chunks)
        update_manifest(manifest_path, {record["chunkId"]: record for record in chunks})
        build_section_derivatives(
            surah_dir,
            manifest_path,
            chunks,
            eligible_chunk_ids=(
                target_ids
                if args.limit is not None or args.chunk_ids is not None
                else None
            ),
        )
        update_generation_state(
            manifest_path,
            "partial"
            if args.limit is not None or args.chunk_ids is not None
            else "complete",
            preflight["requestDigest"],
        )
    except Exception as error:
        try:
            if in_flight_chunk is not None:
                in_flight_chunk["remoteOutcome"] = "unknown"
            write_jsonl(chunks_path, chunks)
            update_manifest(manifest_path, {record["chunkId"]: record for record in chunks})
            clear_affected_section_derivatives(surah_dir, manifest_path, target_ids)
            update_generation_state(
                manifest_path,
                "failed",
                preflight["requestDigest"],
                str(error),
            )
        except Exception as state_error:
            print(f"Failed to persist failure state: {state_error}", file=sys.stderr)
        print(f"Synthesis stopped without retry: {error}", file=sys.stderr)
        return 1

    print(
        json.dumps(
            {
                "processed": processed,
                "chunks": len(target_chunks),
                "remoteCalls": len(remote_chunks),
                "requestSetSha256": preflight["requestDigest"],
            },
            indent=2,
        )
    )
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("surah_dir", type=Path)
    selection_group = parser.add_mutually_exclusive_group()
    selection_group.add_argument("--limit", type=int)
    selection_group.add_argument(
        "--chunk-id",
        dest="chunk_ids",
        action="append",
        help="Select an exact chunk ID; repeat for multiple chunks.",
    )
    parser.add_argument("--force", action="store_true")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate the complete request set without credentials, network, or audio writes.",
    )
    parser.add_argument(
        "--confirm-remote",
        metavar="REQUEST_SET_SHA256",
        help="Exact requestSetSha256 printed by preflight; required for paid requests.",
    )
    parser.add_argument(
        "--confirm-cost-usd",
        type=decimal_argument,
        help="Exact estimated cost printed by preflight, to six decimal places.",
    )
    parser.add_argument(
        "--max-cost-usd",
        type=decimal_argument,
        help="Required spending ceiling for any run that will make remote requests.",
    )
    parser.add_argument(
        "--confirm-force",
        action="store_true",
        help="Acknowledge that --force may resend already-paid requests.",
    )
    parser.add_argument(
        "--reconcile-unknown",
        action="store_true",
        help="Explicitly allow resending a request whose prior transport outcome is unknown.",
    )
    args = parser.parse_args()
    if args.force and not args.confirm_force and not args.dry_run:
        parser.error("--force requires --confirm-force")

    reject_symlink_components(args.surah_dir, "collection")
    surah_dir = args.surah_dir.expanduser().resolve()
    if args.dry_run:
        try:
            preflight = preflight_collection(
                surah_dir,
                limit=args.limit,
                chunk_ids=args.chunk_ids,
                force=args.force,
                reconcile_unknown=args.reconcile_unknown,
            )
        except (OSError, ValueError, RuntimeError) as error:
            print(f"Preflight failed: {error}", file=sys.stderr)
            return 1
        print(json.dumps(preflight_summary(preflight, True), indent=2))
        return 0

    try:
        with CollectionLock(surah_dir):
            preflight = preflight_collection(
                surah_dir,
                limit=args.limit,
                chunk_ids=args.chunk_ids,
                force=args.force,
                reconcile_unknown=args.reconcile_unknown,
            )
            print(json.dumps(preflight_summary(preflight, False), indent=2))
            authorization = require_remote_confirmation(args, preflight)
            return process_collection(preflight, args, authorization)
    except (OSError, PermissionError, ValueError, RuntimeError) as error:
        print(f"Synthesis refused before remote execution: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
