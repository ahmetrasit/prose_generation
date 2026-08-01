#!/usr/bin/env python3
import argparse
import base64
import binascii
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
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
import uuid
import wave


ENDPOINT = "https://texttospeech.googleapis.com/v1beta1/text:synthesize"
DEFAULT_PROJECT_ID = "quran-roots"
DEFAULT_LEDGER_DIR = Path(__file__).resolve().parents[1] / "ledger"
SAMPLE_RATE = 24000
BYTES_PER_SAMPLE = 2
CHANNELS = 1
WAV_HEADER_BYTES = 44
MP3_BITRATE_BPS = "64000"
MP3_BITRATE_FFMPEG = "64k"
INPUT_COST_PER_MILLION_TOKENS = Decimal("1")
OUTPUT_COST_PER_MILLION_TOKENS = Decimal("20")
AUDIO_TOKENS_PER_SECOND = Decimal("25")
ESTIMATED_CHARS_PER_INPUT_TOKEN = Decimal("4")
MAX_INPUT_TOKENS_PER_REQUEST = 8192
MAX_OUTPUT_TOKENS_PER_REQUEST = 16384
MAX_TEXT_BYTES_PER_REQUEST = 4000
MAX_PROMPT_BYTES_PER_REQUEST = 4000
MAX_COMBINED_INPUT_BYTES_PER_REQUEST = 8000
UNKNOWN_REMOTE_OUTCOMES = {"in_flight", "unknown"}
ACCESS_TOKEN_REFRESH_SECONDS = 45 * 60
SYNTHESIS_TIMEOUT_SECONDS = 300
KNOWN_ERROR_RETRY_DELAYS_SECONDS = (2, 5)
COLLECTION_SOURCE_KINDS = {
    "surah": {"surah"},
    "ayah": {"ayah"},
    "ayah-recitation": {"ayah"},
    "summary": {"summary"},
    "recitation": {"recitation"},
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
COMMENTARY_PROMPT = (
    "Speak as a warm, conversational Turkish narrator addressing one curious "
    "listener. Sound like a thoughtful person sharing a discovery as it becomes "
    "clear, with natural human cadence, varied sentence energy, and quiet "
    "curiosity. Let short reveal sentences land, then slow slightly for "
    "explanation. Use clear Istanbul Turkish diction and natural pauses. Avoid "
    "sermon, classroom lecture, documentary-announcer delivery, exaggerated "
    "drama, and a repeated rhetorical rise-and-fall. Do not give every section "
    "the same cadence. Pronounce Arabic Quranic words naturally as Arabic, then "
    "return smoothly to Turkish."
)
RECITATION_PROMPT = (
    "Read only the exact text in the text field. The text field is the complete "
    "script. Do not repeat, add, explain, translate, paraphrase, or continue it. "
    "Stop immediately after the final Arabic word. Say the Turkish label once, "
    "then recite the Arabic Quran text once, with a short natural pause after "
    "the label."
)
APPROVED_PROMPTS = {
    sha256: prompt
    for prompt in (COMMENTARY_PROMPT, RECITATION_PROMPT)
    for sha256 in (hashlib.sha256(prompt.encode("utf-8")).hexdigest(),)
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


def manifest_prompt_hashes(manifest):
    prompts = manifest.get("prompts")
    if prompts is None:
        prompt = manifest.get("prompt")
        prompt_hash = manifest.get("promptSha256")
        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError("Manifest is missing prompt")
        if not isinstance(prompt_hash, str) or sha256_text(prompt) != prompt_hash:
            raise ValueError("Manifest prompt hash does not match prompt")
        prompts = {"default": prompt}
    if not isinstance(prompts, dict) or not prompts:
        raise ValueError("Manifest prompts must be a non-empty object")

    hashes = set()
    for name, prompt in prompts.items():
        if not isinstance(name, str) or not name:
            raise ValueError("Manifest prompt names must be non-empty strings")
        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError(f"Manifest prompt {name!r} is empty")
        prompt_hash = sha256_text(prompt)
        if APPROVED_PROMPTS.get(prompt_hash) != prompt:
            raise ValueError(f"Manifest prompt {name!r} is not allowlisted")
        hashes.add(prompt_hash)
    return hashes


def validate_manifest_and_chunks(surah_dir, manifest, chunks):
    surah_dir = surah_dir.resolve()
    if not surah_dir.is_dir():
        raise ValueError(f"Collection directory does not exist: {surah_dir}")
    collection = manifest.get("collection")
    valid_directory_name = bool(re.fullmatch(r"S\d{3}", surah_dir.name)) or (
        collection == "recitation" and surah_dir.name == "besmele"
    )
    if not valid_directory_name:
        raise ValueError(f"Collection directory must be named SNNN or recitation/besmele: {surah_dir}")
    if manifest.get("surahId") != surah_dir.name:
        raise ValueError("Manifest surahId does not match the collection directory")
    if surah_dir.parent.name != collection:
        raise ValueError("Manifest collection does not match the parent directory")
    if manifest.get("chunksJsonl") != "chunks.jsonl":
        raise ValueError("Manifest must point to the canonical chunks.jsonl")
    if manifest.get("chunkCount") != len(chunks):
        raise ValueError("Manifest chunkCount does not match chunks.jsonl")
    source_kind = manifest.get("sourceKind")
    if source_kind not in {"surah", "ayah", "summary", "recitation"}:
        raise ValueError("Manifest has an unsupported sourceKind")
    if source_kind not in COLLECTION_SOURCE_KINDS.get(collection, set()):
        raise ValueError("Manifest collection does not match sourceKind")
    if manifest.get("voice") != EXPECTED_VOICE:
        raise ValueError("Manifest voice does not match the approved TTS voice")
    if manifest.get("audioConfig") != EXPECTED_AUDIO_CONFIG:
        raise ValueError("Manifest audioConfig does not match the approved TTS config")
    approved_prompt_hashes = manifest_prompt_hashes(manifest)

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
        if chunk["promptSha256"] not in approved_prompt_hashes:
            raise ValueError(f"{chunk_id} prompt hash is not declared by the manifest")
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
                "remoteAttemptId",
                "remoteAttemptStartedAt",
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


def request_set_digest(chunks, request_bodies, project_id=DEFAULT_PROJECT_ID):
    """Digest the billing project and exact ordered POST bodies."""

    digest = hashlib.sha256()
    project_bytes = project_id.encode("utf-8")
    digest.update(len(project_bytes).to_bytes(8, "big"))
    digest.update(project_bytes)
    for chunk in chunks:
        body = request_bodies.get(chunk["chunkId"])
        if not isinstance(body, bytes):
            raise ValueError(f"Missing frozen request body: {chunk['chunkId']}")
        digest.update(len(body).to_bytes(8, "big"))
        digest.update(body)
    return digest.hexdigest()


def token_cost(token_count, rate):
    if not rate.is_finite() or rate <= 0:
        raise ValueError("Cost rate must be finite and greater than zero")
    return (
        Decimal(token_count) * rate / Decimal(1_000_000)
    ).quantize(Decimal("0.000001"), rounding=ROUND_CEILING)


def estimate_request_costs(chunks, request_bodies):
    output_chars = sum(chunk["ttsCharCount"] for chunk in chunks)
    input_chars = 0
    for chunk in chunks:
        request = strict_json_loads(request_bodies[chunk["chunkId"]])
        input_chars += len(request["input"]["prompt"]) + len(request["input"]["text"])

    estimated_input_tokens = int(
        (Decimal(input_chars) / ESTIMATED_CHARS_PER_INPUT_TOKEN).to_integral_value(
            rounding=ROUND_CEILING
        )
    )
    request_count = len(chunks)
    maximum_input_tokens = request_count * MAX_INPUT_TOKENS_PER_REQUEST
    maximum_output_tokens = request_count * MAX_OUTPUT_TOKENS_PER_REQUEST
    estimated_input_cost = token_cost(
        estimated_input_tokens, INPUT_COST_PER_MILLION_TOKENS
    )
    maximum_input_cost = token_cost(
        maximum_input_tokens, INPUT_COST_PER_MILLION_TOKENS
    )
    maximum_output_cost = token_cost(
        maximum_output_tokens, OUTPUT_COST_PER_MILLION_TOKENS
    )
    return {
        "inputChars": input_chars,
        "outputChars": output_chars,
        "estimatedInputTokens": estimated_input_tokens,
        "estimatedInputCostUsd": estimated_input_cost,
        "maximumInputTokens": maximum_input_tokens,
        "maximumOutputTokens": maximum_output_tokens,
        "maximumInputCostUsd": maximum_input_cost,
        "maximumOutputCostUsd": maximum_output_cost,
        "maximumCostUsd": maximum_input_cost + maximum_output_cost,
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


def utc_timestamp():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def ledger_path_for_now(ledger_dir):
    return ledger_dir / f"{time.strftime('%Y-%m-%d', time.gmtime())}.jsonl"


def append_ledger_entry(ledger_dir, entry):
    """Durably append one entry, serializing concurrent writers with flock."""

    ledger_dir = Path(ledger_dir).expanduser().resolve()
    ledger_dir.mkdir(parents=True, exist_ok=True)
    path = ledger_path_for_now(ledger_dir)
    if path.is_symlink():
        raise ValueError(f"Refusing symlinked ledger: {path}")
    payload = json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n"
    with path.open("a", encoding="utf-8") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        try:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def ledger_has_success_terminal(ledger_dir, attempt_id):
    if not attempt_id:
        return False
    ledger_dir = Path(ledger_dir).expanduser()
    if not ledger_dir.is_dir():
        return False
    for path in sorted(ledger_dir.glob("*.jsonl")):
        if path.is_symlink():
            raise ValueError(f"Refusing symlinked ledger: {path}")
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                entry = strict_json_loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(f"Invalid ledger JSON at {path}:{line_number}") from error
            if entry.get("attemptId") == attempt_id and entry.get("event") in {
                "synthesized",
                "synthesized_recovered",
            }:
                return True
    return False


def build_ledger_entry(
    *,
    event,
    collection,
    chunk,
    request_body,
    attempt_id,
    project_id,
    duration_seconds=None,
    new_spend=False,
    error=None,
):
    request = strict_json_loads(request_body)
    prompt = request["input"]["prompt"]
    text = request["input"]["text"]
    input_chars = len(prompt) + len(text)
    estimated_input_tokens = int(
        (Decimal(input_chars) / ESTIMATED_CHARS_PER_INPUT_TOKEN).to_integral_value(
            rounding=ROUND_CEILING
        )
    )
    output_audio_tokens = (
        Decimal(str(duration_seconds)) * AUDIO_TOKENS_PER_SECOND
        if duration_seconds is not None
        else None
    )
    input_cost = token_cost(
        estimated_input_tokens, INPUT_COST_PER_MILLION_TOKENS
    )
    output_cost = (
        token_cost(output_audio_tokens, OUTPUT_COST_PER_MILLION_TOKENS)
        if output_audio_tokens is not None
        else Decimal("0")
    )
    estimated_billed_input = input_cost if new_spend else Decimal("0")
    billed_output = output_cost if new_spend else Decimal("0")
    entry = {
        "timestamp": utc_timestamp(),
        "event": event,
        "attemptId": attempt_id,
        "projectId": project_id,
        "collection": collection,
        "surahId": chunk.get("surahId"),
        "chunkId": chunk.get("chunkId"),
        "kind": chunk.get("kind"),
        "requestSha256": chunk.get("requestSha256"),
        "textCharCount": len(text),
        "promptCharCount": len(prompt),
        "estimatedInputTokens": estimated_input_tokens,
        "durationSeconds": duration_seconds,
        "outputAudioTokens": (
            str(output_audio_tokens.quantize(Decimal("0.001")))
            if output_audio_tokens is not None
            else None
        ),
        "newSpend": new_spend,
        "possibleNewSpend": event in {"attempted", "unknown"},
        "estimatedBilledInputUsd": str(estimated_billed_input),
        "billedOutputUsd": str(billed_output),
        "estimatedBilledTotalUsd": str(estimated_billed_input + billed_output),
    }
    if error is not None:
        entry["error"] = str(error)
    return entry


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


def synthesize(
    request_body,
    token,
    chunk,
    generated_at,
    project_id,
    authorization=None,
):
    if authorization is not _REMOTE_AUTHORIZATION:
        raise PermissionError("Remote authorization is required before TTS synthesis")
    request = urllib.request.Request(
        ENDPOINT,
        data=request_body,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "x-goog-user-project": project_id,
            "Content-Type": "application/json; charset=utf-8",
        },
    )
    http_error_code = None
    try:
        with NO_REDIRECT_OPENER.open(
            request, timeout=SYNTHESIS_TIMEOUT_SECONDS
        ) as response:
            payload = response.read()
    except urllib.error.HTTPError as error:
        if 300 <= error.code < 400:
            raise RuntimeError(
                f"TTS endpoint returned redirect ({error.code}); refusing to follow it"
            ) from error
        http_error_code = error.code
        payload = error.read()
    if not payload and http_error_code is not None:
        response = {
            "error": {
                "code": http_error_code,
                "message": f"TTS endpoint returned HTTP {http_error_code} with an empty body",
                "status": "HTTP_ERROR",
            }
        }
    else:
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


def response_metadata_matches_chunk(response, chunk):
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


def response_matches_chunk(response, chunk):
    return "error" not in response and response_metadata_matches_chunk(response, chunk)


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


def is_retryable_known_error(response):
    error = response.get("error") if isinstance(response, dict) else None
    return bool(
        isinstance(error, dict)
        and error.get("code") == 400
        and error.get("status") == "INVALID_ARGUMENT"
        and error.get("message") == "Request contains an invalid argument."
    )


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
    prompt_bytes = len(input_block["prompt"].encode("utf-8"))
    text_bytes = len(input_block["text"].encode("utf-8"))
    if prompt_bytes > MAX_PROMPT_BYTES_PER_REQUEST:
        raise ValueError(f"Request prompt exceeds {MAX_PROMPT_BYTES_PER_REQUEST} bytes: {request_path}")
    if text_bytes > MAX_TEXT_BYTES_PER_REQUEST:
        raise ValueError(f"Request text exceeds {MAX_TEXT_BYTES_PER_REQUEST} bytes: {request_path}")
    if prompt_bytes + text_bytes > MAX_COMBINED_INPUT_BYTES_PER_REQUEST:
        raise ValueError(
            f"Request prompt and text exceed {MAX_COMBINED_INPUT_BYTES_PER_REQUEST} bytes: {request_path}"
        )
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
    prompt = request.get("input", {}).get("prompt", "")
    prompt_hash = sha256_text(prompt)
    if prompt_hash != chunk.get("promptSha256"):
        raise ValueError(f"{chunk['chunkId']} request prompt hash mismatch")
    if APPROVED_PROMPTS.get(prompt_hash) != prompt:
        raise ValueError(f"{chunk['chunkId']} request prompt is not allowlisted")
    if manifest is not None and prompt_hash not in manifest_prompt_hashes(manifest):
        raise ValueError(f"{chunk['chunkId']} prompt hash is not declared by manifest")
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
            for field in ("remoteOutcome", "remoteAttemptId", "remoteAttemptStartedAt"):
                if record.get(field) is not None:
                    paragraph[field] = record[field]
                else:
                    paragraph.pop(field, None)
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
            if not response_metadata_matches_chunk(response, chunk):
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
    project_id=DEFAULT_PROJECT_ID,
):
    if not isinstance(project_id, str) or not re.fullmatch(r"[a-z][a-z0-9-]{4,28}[a-z0-9]", project_id):
        raise ValueError(f"Invalid Google Cloud project id: {project_id!r}")
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
        and statuses[chunk["chunkId"]] not in {"verified_response", "error_response"}
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
            if status not in {"missing", "verified_response", "error_response"}
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
            if status in {"missing", "error_response"} or (
                chunk.get("remoteOutcome") in UNKNOWN_REMOTE_OUTCOMES
                and status != "verified_response"
            ):
                remote_chunks.append(chunk)

    request_digest = request_set_digest(remote_chunks, request_bodies, project_id)
    costs = estimate_request_costs(remote_chunks, request_bodies)
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
        "projectId": project_id,
        "ttsChars": costs["outputChars"],
        "inputChars": costs["inputChars"],
        "estimatedInputTokens": costs["estimatedInputTokens"],
        "estimatedInputCostUsd": costs["estimatedInputCostUsd"],
        "maximumInputTokens": costs["maximumInputTokens"],
        "maximumOutputTokens": costs["maximumOutputTokens"],
        "maximumInputCostUsd": costs["maximumInputCostUsd"],
        "maximumOutputCostUsd": costs["maximumOutputCostUsd"],
        "maximumCostUsd": costs["maximumCostUsd"],
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
    expected_cost = preflight["maximumCostUsd"]
    if args.confirm_cost_usd != expected_cost:
        raise PermissionError(
            "Remote maximum-cost confirmation does not match preflight: "
            f"expected {expected_cost}"
        )
    if args.max_cost_usd is None:
        raise PermissionError("Provide --max-cost-usd as an explicit spending ceiling")
    single_request_maximum = estimate_request_costs(
        remote_chunks[:1], preflight["requestBodies"]
    )["maximumCostUsd"]
    if single_request_maximum > args.max_cost_usd:
        raise PermissionError(
            "The maximum cost of one request "
            f"{single_request_maximum} exceeds --max-cost-usd {args.max_cost_usd}"
        )
    if args.force and not args.confirm_force:
        raise PermissionError("--force requires the separate --confirm-force acknowledgement")
    return _REMOTE_AUTHORIZATION


def preflight_summary(preflight, dry_run):
    statuses = preflight["statuses"]
    summary = {
        "dryRun": dry_run,
        "surahDir": str(preflight["surahDir"]),
        "projectId": preflight["projectId"],
        "validatedChunks": len(preflight["chunks"]),
        "targetChunks": len(preflight["targetChunks"]),
        "remoteChunks": len(preflight["remoteChunks"]),
        "cachedChunks": sum(status == "verified_response" for status in statuses.values()),
        "unknownChunks": len(preflight["unknownChunks"]),
        "ttsChars": preflight["ttsChars"],
        "inputChars": preflight["inputChars"],
        "estimatedInputTokens": preflight["estimatedInputTokens"],
        "estimatedInputCostUsd": str(preflight["estimatedInputCostUsd"]),
        "maximumInputTokens": preflight["maximumInputTokens"],
        "maximumOutputTokens": preflight["maximumOutputTokens"],
        "maximumInputCostUsd": str(preflight["maximumInputCostUsd"]),
        "maximumOutputCostUsd": str(preflight["maximumOutputCostUsd"]),
        "maximumCostUsd": str(preflight["maximumCostUsd"]),
        "costBasis": "Gemini TTS provider token limits per remote request",
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


def archive_existing_chunk_artifacts(surah_dir, chunk, paths, attempt_id):
    """Preserve artifacts displaced by an explicitly confirmed force run."""

    archive_root = safe_relative_path(
        surah_dir,
        f"archive/stale/{chunk['chunkId']}/{attempt_id}",
        "stale archive",
    )
    for field in ("response", "wav", "mp3"):
        source = paths[field]
        if not source.exists():
            continue
        relative = PurePosixPath(chunk[field])
        destination = archive_root.joinpath(*relative.parts)
        destination.parent.mkdir(parents=True, exist_ok=True)
        os.replace(source, destination)


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


def clear_remote_attempt(chunk):
    chunk.pop("remoteOutcome", None)
    chunk.pop("remoteAttemptId", None)
    chunk.pop("remoteAttemptStartedAt", None)


def persist_chunk_state(chunks_path, manifest_path, chunks):
    write_jsonl(chunks_path, chunks)
    update_manifest(manifest_path, {record["chunkId"]: record for record in chunks})


def synthesize_with_retries(
    request_body,
    token,
    chunk,
    generated_at,
    project_id,
    authorization,
):
    response = synthesize(
        request_body,
        token,
        chunk,
        generated_at,
        project_id,
        authorization,
    )
    for retry_number, retry_delay in enumerate(
        KNOWN_ERROR_RETRY_DELAYS_SECONDS, start=1
    ):
        if not is_retryable_known_error(response):
            break
        print(
            "Retrying transient provider rejection for "
            f"{chunk['chunkId']} ({retry_number}/"
            f"{len(KNOWN_ERROR_RETRY_DELAYS_SECONDS)})...",
            file=sys.stderr,
            flush=True,
        )
        time.sleep(retry_delay)
        response = synthesize(
            request_body,
            token,
            chunk,
            generated_at,
            project_id,
            authorization,
        )
    return response


def maximum_single_request_cost():
    return token_cost(
        MAX_INPUT_TOKENS_PER_REQUEST, INPUT_COST_PER_MILLION_TOKENS
    ) + token_cost(
        MAX_OUTPUT_TOKENS_PER_REQUEST, OUTPUT_COST_PER_MILLION_TOKENS
    )


def affordable_pool_slots(
    spent_usd,
    budget_usd,
    workers,
    in_flight,
    remaining,
):
    if remaining <= 0 or in_flight >= workers:
        return 0
    available = budget_usd - spent_usd
    affordable_active = int(available // maximum_single_request_cost())
    return min(workers - in_flight, remaining, max(0, affordable_active - in_flight))


def process_collection(preflight, args, authorization):
    surah_dir = preflight["surahDir"]
    manifest_path = preflight["manifestPath"]
    chunks_path = preflight["chunksPath"]
    chunks = preflight["chunks"]
    target_chunks = preflight["targetChunks"]
    target_ids = {chunk["chunkId"] for chunk in target_chunks}
    remote_chunks = preflight["remoteChunks"]
    collection = preflight["manifest"]["collection"]
    processed = 0
    in_flight_chunk = None
    current_attempt_id = None
    current_request_body = None
    current_response = None
    remote_started = False

    try:
        token = get_authorized_token(authorization) if remote_chunks else None
        token_refreshed_at = time.monotonic() if remote_chunks else None
        if remote_chunks:
            clear_affected_section_derivatives(surah_dir, manifest_path, target_ids)
            update_generation_state(
                manifest_path,
                "in_progress",
                preflight["requestDigest"],
            )

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
                cached_attempt_id = response.get("_attemptId")
                recovered = cached_attempt_id and not ledger_has_success_terminal(
                    args.ledger_dir, cached_attempt_id
                )
                append_ledger_entry(
                    args.ledger_dir,
                    build_ledger_entry(
                        event="synthesized_recovered" if recovered else "cached",
                        collection=collection,
                        chunk=chunk,
                        request_body=preflight["requestBodies"][chunk["chunkId"]],
                        attempt_id=cached_attempt_id or f"cache-{uuid.uuid4().hex}",
                        project_id=args.project_id,
                        duration_seconds=duration_seconds,
                        new_spend=bool(recovered),
                    ),
                )
                clear_remote_attempt(chunk)
                persist_chunk_state(chunks_path, manifest_path, chunks)
                processed += 1
                continue

            print(f"{index}/{len(target_chunks)} {chunk['chunkId']}...", flush=True)
            generated_at = utc_timestamp()
            current_attempt_id = uuid.uuid4().hex
            current_request_body = preflight["requestBodies"][chunk["chunkId"]]
            current_response = None
            remote_started = False
            in_flight_chunk = chunk
            chunk["remoteOutcome"] = "in_flight"
            chunk["remoteAttemptId"] = current_attempt_id
            chunk["remoteAttemptStartedAt"] = generated_at
            persist_chunk_state(chunks_path, manifest_path, chunks)
            append_ledger_entry(
                args.ledger_dir,
                build_ledger_entry(
                    event="attempted",
                    collection=collection,
                    chunk=chunk,
                    request_body=current_request_body,
                    attempt_id=current_attempt_id,
                    project_id=args.project_id,
                ),
            )
            if args.force:
                archive_existing_chunk_artifacts(
                    surah_dir, chunk, paths, current_attempt_id
                )
            if time.monotonic() - token_refreshed_at >= ACCESS_TOKEN_REFRESH_SECONDS:
                token = get_authorized_token(authorization)
                token_refreshed_at = time.monotonic()
            remote_started = True
            current_response = synthesize(
                current_request_body,
                token,
                chunk,
                generated_at,
                args.project_id,
                authorization,
            )
            for retry_number, retry_delay in enumerate(
                KNOWN_ERROR_RETRY_DELAYS_SECONDS, start=1
            ):
                if not is_retryable_known_error(current_response):
                    break
                print(
                    "Retrying transient provider rejection for "
                    f"{chunk['chunkId']} ({retry_number}/"
                    f"{len(KNOWN_ERROR_RETRY_DELAYS_SECONDS)})...",
                    file=sys.stderr,
                    flush=True,
                )
                time.sleep(retry_delay)
                current_response = synthesize(
                    current_request_body,
                    token,
                    chunk,
                    generated_at,
                    args.project_id,
                    authorization,
                )
            current_response["_attemptId"] = current_attempt_id
            if "error" in current_response:
                write_response(paths["response"], current_response, chunk)
                append_ledger_entry(
                    args.ledger_dir,
                    build_ledger_entry(
                        event="failed",
                        collection=collection,
                        chunk=chunk,
                        request_body=current_request_body,
                        attempt_id=current_attempt_id,
                        project_id=args.project_id,
                        error=json.dumps(current_response["error"], ensure_ascii=False),
                    ),
                )
                clear_remote_attempt(chunk)
                persist_chunk_state(chunks_path, manifest_path, chunks)
                update_generation_state(
                    manifest_path,
                    "failed",
                    preflight["requestDigest"],
                    json.dumps(current_response["error"], ensure_ascii=False),
                )
                print(
                    json.dumps(current_response["error"], ensure_ascii=False, indent=2),
                    file=sys.stderr,
                )
                return 1

            # Validate the returned bytes before committing the response record.
            audio = decode_audio_response(current_response)
            atomic_write_bytes(paths["wav"], audio)
            chunk["durationSeconds"] = round(wav_duration_seconds(paths["wav"]), 3)
            chunk["audioSha256"] = sha256_bytes(audio)
            chunk.pop("mp3Sha256", None)
            write_response(paths["response"], current_response, chunk)
            append_ledger_entry(
                args.ledger_dir,
                build_ledger_entry(
                    event="synthesized",
                    collection=collection,
                    chunk=chunk,
                    request_body=current_request_body,
                    attempt_id=current_attempt_id,
                    project_id=args.project_id,
                    duration_seconds=chunk["durationSeconds"],
                    new_spend=True,
                ),
            )
            materialize_original_mp3(surah_dir, chunk)
            chunk["generatedAt"] = generated_at
            clear_remote_attempt(chunk)
            persist_chunk_state(chunks_path, manifest_path, chunks)
            in_flight_chunk = None
            current_attempt_id = None
            current_request_body = None
            current_response = None
            remote_started = False
            processed += 1

        persist_chunk_state(chunks_path, manifest_path, chunks)
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
                if remote_started:
                    in_flight_chunk["remoteOutcome"] = "unknown"
                    if current_response is not None:
                        unknown_path = safe_relative_path(
                            surah_dir,
                            f"responses/unknown/{in_flight_chunk['chunkId']}-{current_attempt_id}.json",
                            "unknown response",
                        )
                        write_response(unknown_path, current_response, in_flight_chunk)
                    try:
                        append_ledger_entry(
                            args.ledger_dir,
                            build_ledger_entry(
                                event="unknown",
                                collection=collection,
                                chunk=in_flight_chunk,
                                request_body=current_request_body,
                                attempt_id=current_attempt_id,
                                project_id=args.project_id,
                                error=error,
                            ),
                        )
                    except Exception as ledger_error:
                        print(f"Failed to append unknown ledger state: {ledger_error}", file=sys.stderr)
                else:
                    clear_remote_attempt(in_flight_chunk)
            persist_chunk_state(chunks_path, manifest_path, chunks)
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


def process_collection_bounded(preflight, args, authorization):
    surah_dir = preflight["surahDir"]
    manifest_path = preflight["manifestPath"]
    chunks_path = preflight["chunksPath"]
    chunks = preflight["chunks"]
    target_chunks = preflight["targetChunks"]
    target_ids = {chunk["chunkId"] for chunk in target_chunks}
    remote_chunks = preflight["remoteChunks"]
    collection = preflight["manifest"]["collection"]
    processed = 0
    spent_usd = Decimal("0")
    active_attempts = {}

    try:
        token = get_authorized_token(authorization) if remote_chunks else None
        token_refreshed_at = time.monotonic() if remote_chunks else None
        if remote_chunks:
            clear_affected_section_derivatives(surah_dir, manifest_path, target_ids)
            update_generation_state(
                manifest_path,
                "in_progress",
                preflight["requestDigest"],
            )

        for chunk in target_chunks:
            paths = preflight["targetPaths"][chunk["chunkId"]]
            status = preflight["statuses"][chunk["chunkId"]]
            if args.force or status != "verified_response":
                continue
            if (
                chunk.get("durationSeconds") is not None
                and chunk.get("audioSha256")
                and chunk.get("mp3Sha256")
                and paths["wav"].is_file()
                and paths["mp3"].is_file()
            ):
                clear_remote_attempt(chunk)
                processed += 1
                continue
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
            cached_attempt_id = response.get("_attemptId")
            recovered = cached_attempt_id and not ledger_has_success_terminal(
                args.ledger_dir, cached_attempt_id
            )
            append_ledger_entry(
                args.ledger_dir,
                build_ledger_entry(
                    event="synthesized_recovered" if recovered else "cached",
                    collection=collection,
                    chunk=chunk,
                    request_body=preflight["requestBodies"][chunk["chunkId"]],
                    attempt_id=cached_attempt_id or f"cache-{uuid.uuid4().hex}",
                    project_id=args.project_id,
                    duration_seconds=duration_seconds,
                    new_spend=bool(recovered),
                ),
            )
            clear_remote_attempt(chunk)
            processed += 1
        persist_chunk_state(chunks_path, manifest_path, chunks)

        remote_offset = 0
        uncertain_reserve_usd = Decimal("0")
        had_failures = False
        futures = {}
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            while remote_offset < len(remote_chunks) or futures:
                budget_used = spent_usd + uncertain_reserve_usd
                slots = affordable_pool_slots(
                    budget_used,
                    args.max_cost_usd,
                    args.workers,
                    len(futures),
                    len(remote_chunks) - remote_offset,
                )
                if slots:
                    new_attempts = []
                    for chunk in remote_chunks[remote_offset : remote_offset + slots]:
                        remote_offset += 1
                        print(
                            f"{remote_offset}/{len(remote_chunks)} "
                            f"{chunk['chunkId']}...",
                            flush=True,
                        )
                        generated_at = utc_timestamp()
                        attempt_id = uuid.uuid4().hex
                        request_body = preflight["requestBodies"][chunk["chunkId"]]
                        paths = preflight["targetPaths"][chunk["chunkId"]]
                        attempt = {
                            "chunk": chunk,
                            "paths": paths,
                            "generatedAt": generated_at,
                            "attemptId": attempt_id,
                            "requestBody": request_body,
                        }
                        active_attempts[chunk["chunkId"]] = attempt
                        new_attempts.append(attempt)
                        chunk["remoteOutcome"] = "in_flight"
                        chunk["remoteAttemptId"] = attempt_id
                        chunk["remoteAttemptStartedAt"] = generated_at
                        append_ledger_entry(
                            args.ledger_dir,
                            build_ledger_entry(
                                event="attempted",
                                collection=collection,
                                chunk=chunk,
                                request_body=request_body,
                                attempt_id=attempt_id,
                                project_id=args.project_id,
                            ),
                        )
                        if args.force:
                            archive_existing_chunk_artifacts(
                                surah_dir, chunk, paths, attempt_id
                            )
                    persist_chunk_state(chunks_path, manifest_path, chunks)

                    if time.monotonic() - token_refreshed_at >= ACCESS_TOKEN_REFRESH_SECONDS:
                        token = get_authorized_token(authorization)
                        token_refreshed_at = time.monotonic()
                    for attempt in new_attempts:
                        future = executor.submit(
                            synthesize_with_retries,
                            attempt["requestBody"],
                            token,
                            attempt["chunk"],
                            attempt["generatedAt"],
                            args.project_id,
                            authorization,
                        )
                        futures[future] = attempt

                if not futures:
                    if remote_offset < len(remote_chunks):
                        raise RuntimeError(
                            "Run spending ceiling reached before all chunks completed: "
                            f"used=${budget_used}, ceiling=${args.max_cost_usd}"
                        )
                    break

                done, _ = wait(futures, return_when=FIRST_COMPLETED)
                for future in done:
                    attempt = futures.pop(future)
                    chunk = attempt["chunk"]
                    paths = attempt["paths"]
                    try:
                        response = future.result()
                    except Exception as transport_error:
                        chunk["remoteOutcome"] = "unknown"
                        append_ledger_entry(
                            args.ledger_dir,
                            build_ledger_entry(
                                event="unknown",
                                collection=collection,
                                chunk=chunk,
                                request_body=attempt["requestBody"],
                                attempt_id=attempt["attemptId"],
                                project_id=args.project_id,
                                error=transport_error,
                            ),
                        )
                        uncertain_reserve_usd += maximum_single_request_cost()
                        print(
                            f"Unknown remote outcome for {chunk['chunkId']}: "
                            f"{transport_error}",
                            file=sys.stderr,
                            flush=True,
                        )
                        active_attempts.pop(chunk["chunkId"], None)
                        had_failures = True
                        continue

                    response["_attemptId"] = attempt["attemptId"]
                    if "error" in response:
                        write_response(paths["response"], response, chunk)
                        append_ledger_entry(
                            args.ledger_dir,
                            build_ledger_entry(
                                event="failed",
                                collection=collection,
                                chunk=chunk,
                                request_body=attempt["requestBody"],
                                attempt_id=attempt["attemptId"],
                                project_id=args.project_id,
                                error=json.dumps(response["error"], ensure_ascii=False),
                            ),
                        )
                        clear_remote_attempt(chunk)
                        print(
                            json.dumps(response["error"], ensure_ascii=False, indent=2),
                            file=sys.stderr,
                            flush=True,
                        )
                        active_attempts.pop(chunk["chunkId"], None)
                        had_failures = True
                        continue

                    audio = decode_audio_response(response)
                    atomic_write_bytes(paths["wav"], audio)
                    chunk["durationSeconds"] = round(
                        wav_duration_seconds(paths["wav"]), 3
                    )
                    chunk["audioSha256"] = sha256_bytes(audio)
                    chunk.pop("mp3Sha256", None)
                    write_response(paths["response"], response, chunk)
                    ledger_entry = build_ledger_entry(
                        event="synthesized",
                        collection=collection,
                        chunk=chunk,
                        request_body=attempt["requestBody"],
                        attempt_id=attempt["attemptId"],
                        project_id=args.project_id,
                        duration_seconds=chunk["durationSeconds"],
                        new_spend=True,
                    )
                    append_ledger_entry(args.ledger_dir, ledger_entry)
                    spent_usd += Decimal(ledger_entry["estimatedBilledTotalUsd"])
                    materialize_original_mp3(surah_dir, chunk)
                    chunk["generatedAt"] = attempt["generatedAt"]
                    clear_remote_attempt(chunk)
                    active_attempts.pop(chunk["chunkId"], None)
                    processed += 1
                persist_chunk_state(chunks_path, manifest_path, chunks)

        if had_failures:
            update_generation_state(
                manifest_path,
                "failed",
                preflight["requestDigest"],
                "One or more rolling requests failed or had unknown outcomes",
            )
            return 1

        persist_chunk_state(chunks_path, manifest_path, chunks)
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
            for attempt in active_attempts.values():
                chunk = attempt["chunk"]
                if chunk.get("remoteOutcome") != "in_flight":
                    continue
                chunk["remoteOutcome"] = "unknown"
                try:
                    append_ledger_entry(
                        args.ledger_dir,
                        build_ledger_entry(
                            event="unknown",
                            collection=collection,
                            chunk=chunk,
                            request_body=attempt["requestBody"],
                            attempt_id=attempt["attemptId"],
                            project_id=args.project_id,
                            error=error,
                        ),
                    )
                except Exception as ledger_error:
                    print(
                        f"Failed to append unknown ledger state: {ledger_error}",
                        file=sys.stderr,
                    )
            persist_chunk_state(chunks_path, manifest_path, chunks)
            clear_affected_section_derivatives(surah_dir, manifest_path, target_ids)
            update_generation_state(
                manifest_path,
                "failed",
                preflight["requestDigest"],
                str(error),
            )
        except Exception as state_error:
            print(f"Failed to persist failure state: {state_error}", file=sys.stderr)
        print(f"Synthesis stopped: {error}", file=sys.stderr)
        return 1

    print(
        json.dumps(
            {
                "processed": processed,
                "chunks": len(target_chunks),
                "remoteCalls": len(remote_chunks),
                "workers": args.workers,
                "estimatedBilledUsd": str(spent_usd),
                "requestSetSha256": preflight["requestDigest"],
            },
            indent=2,
        )
    )
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("surah_dir", type=Path)
    parser.add_argument(
        "--project-id",
        default=os.environ.get("GOOGLE_CLOUD_PROJECT", DEFAULT_PROJECT_ID),
        help="Google Cloud billing/quota project (default: GOOGLE_CLOUD_PROJECT or quran-roots).",
    )
    parser.add_argument(
        "--ledger-dir",
        type=Path,
        default=DEFAULT_LEDGER_DIR,
        help="Append-only attempt and spending ledger directory.",
    )
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
        "--workers",
        type=int,
        default=1,
        help="Maximum concurrent TTS requests within this collection.",
    )
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
        help="Exact maximumCostUsd printed by preflight, to six decimal places.",
    )
    parser.add_argument(
        "--max-cost-usd",
        type=decimal_argument,
        help=(
            "Required observed-spend ceiling. The sender reserves the provider "
            "maximum for every in-flight request before sending it."
        ),
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
    if args.workers < 1:
        parser.error("--workers must be at least 1")
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
                project_id=args.project_id,
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
                project_id=args.project_id,
            )
            print(json.dumps(preflight_summary(preflight, False), indent=2))
            authorization = require_remote_confirmation(args, preflight)
            return process_collection_bounded(preflight, args, authorization)
    except (OSError, PermissionError, ValueError, RuntimeError) as error:
        print(f"Synthesis refused before remote execution: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
