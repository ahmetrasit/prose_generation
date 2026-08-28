"""Deterministic serialization, hashing, and confined artifact writes."""

from __future__ import annotations

import hashlib
import html
import json
import os
import re
import tempfile
import unicodedata
from pathlib import Path
from typing import Any


V3_ROOT = Path(__file__).resolve().parent.parent
INPUTS_ROOT = V3_ROOT / "inputs"
OUTPUTS_ROOT = V3_ROOT / "outputs"
APPARATUS_ID_RE = re.compile(
    r"(?:cand|sup|find)_[0-9a-f]{12,}"
    r"|new(?:_[0-9a-f]{12,}|:[a-z][a-z0-9_-]{2,63})"
    r"|root_[0-9]+(?:/B[0-9]+)?"
    r"|B[0-9]+"
    r"|[0-9]+:[0-9]+:[0-9]+(?::[0-9]+)?",
    re.IGNORECASE,
)
HTML_MARKUP_RE = re.compile(r"<.*?>", re.DOTALL)
MARKDOWN_LINK_RE = re.compile(r"[\[\]]")
MARKDOWN_ESCAPE_RE = re.compile(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\]^_`{|}~])")
MARKDOWN_PRESENTATION_RE = re.compile(r"[*`~\[\]]")
MAX_ENTITY_DECODE_PASSES = 32


def _is_identifier_continuation(char: str) -> bool:
    category = unicodedata.category(char)
    return category[0] in ("L", "M", "N") or category in ("Pc", "Cf")


def contains_apparatus_id(text: str) -> bool:
    """Detect complete apparatus tokens after rendered-text obfuscation folding."""
    normalized = unicodedata.normalize("NFKC", text)
    for _ in range(MAX_ENTITY_DECODE_PASSES):
        decoded = html.unescape(normalized)
        if decoded == normalized:
            break
        normalized = decoded
    else:
        return True
    normalized = unicodedata.normalize("NFKC", normalized)
    if HTML_MARKUP_RE.search(normalized) or MARKDOWN_LINK_RE.search(normalized):
        return True
    normalized = MARKDOWN_ESCAPE_RE.sub(r"\1", normalized)
    scan_text = "".join(
        str(unicodedata.decimal(char))
        if unicodedata.category(char) == "Nd"
        else char
        for char in normalized
        if unicodedata.category(char)[0] != "M"
        and unicodedata.category(char) != "Cf"
    )
    scan_views = (scan_text, MARKDOWN_PRESENTATION_RE.sub("", scan_text))
    for view in scan_views:
        for match in APPARATUS_ID_RE.finditer(view):
            start, end = match.span()
            if (
                (start and _is_identifier_continuation(view[start - 1]))
                or (
                    end < len(view)
                    and _is_identifier_continuation(view[end])
                )
            ):
                continue
            return True
    return False


class WorkflowError(RuntimeError):
    """Base class for controlled workflow failures."""


class ValidationError(WorkflowError):
    """Raised when an input or artifact violates its contract."""


class ScopeError(ValidationError):
    """Raised when source identity or scope cannot be trusted."""

    def __init__(self, message: str, *, report: dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.report = report or {}


class BudgetError(ValidationError):
    """Raised when a bounded model packet would exceed a configured limit."""


class PathConfinementError(ValidationError):
    """Raised when an artifact path could escape the v3 tree."""


class ArtifactConflictError(ValidationError):
    """Raised when a fixed artifact path already contains different content."""


def _reject_nonfinite_json(token: str) -> None:
    raise ValueError(f"non-finite JSON number {token}")


def _validate_json_value(
    value: Any,
    *,
    path: str = "$",
    active_containers: set[int] | None = None,
) -> None:
    if active_containers is None:
        active_containers = set()
    value_type = type(value)
    if value is None or value_type in {str, int, float, bool}:
        return
    if value_type not in {list, dict}:
        raise TypeError(f"unsupported JSON type at {path}: {value_type.__name__}")
    container_id = id(value)
    if container_id in active_containers:
        raise ValueError(f"circular JSON container at {path}")
    active_containers.add(container_id)
    try:
        if value_type is list:
            for index, item in enumerate(value):
                _validate_json_value(
                    item,
                    path=f"{path}[{index}]",
                    active_containers=active_containers,
                )
            return
        for key, item in value.items():
            if type(key) is not str:
                raise TypeError(f"non-string object key at {path}: {key!r}")
            _validate_json_value(
                item,
                path=f"{path}.{key}",
                active_containers=active_containers,
            )
    finally:
        active_containers.remove(container_id)


def _object_without_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON object key {key!r}")
        value[key] = item
    return value


def _validate_json_depth(value: Any, *, max_depth: int = 512) -> None:
    stack: list[tuple[Any, int]] = [(value, 0)]
    while stack:
        current, depth = stack.pop()
        if depth > max_depth:
            raise ValueError(f"JSON nesting exceeds hard limit {max_depth}")
        if isinstance(current, list):
            stack.extend((item, depth + 1) for item in current)
        elif isinstance(current, dict):
            stack.extend((item, depth + 1) for item in current.values())


def canonical_json_bytes(value: Any) -> bytes:
    """Return the canonical bytes used for all semantic identity hashes."""
    try:
        _validate_json_value(value)
        return json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError, UnicodeError, RecursionError) as exc:
        raise ValidationError(f"Value is not canonical JSON: {exc}") from exc


def pretty_json_bytes(value: Any) -> bytes:
    """Return deterministic, human-readable artifact bytes."""
    try:
        _validate_json_value(value)
        rendered = json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
            allow_nan=False,
        )
    except (TypeError, ValueError, UnicodeError, RecursionError) as exc:
        raise ValidationError(f"Value is not canonical JSON: {exc}") from exc
    return (rendered + "\n").encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def canonical_sha256(value: Any) -> str:
    return sha256_bytes(canonical_json_bytes(value))


def parse_json_object_bytes(raw: bytes, *, label: str) -> dict[str, Any]:
    if not isinstance(raw, bytes):
        raise ValidationError(f"{label} must be bytes")
    try:
        value = json.loads(
            raw,
            parse_constant=_reject_nonfinite_json,
            object_pairs_hook=_object_without_duplicate_keys,
        )
        _validate_json_depth(value)
    except (UnicodeError, json.JSONDecodeError, ValueError, RecursionError) as exc:
        raise ValidationError(f"Invalid JSON source {label}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValidationError(f"JSON source must be an object: {label}")
    return value


def load_json_object(path: Path) -> tuple[dict[str, Any], bytes]:
    try:
        raw = path.read_bytes()
    except OSError as exc:
        raise ValidationError(f"Cannot read JSON source {path}: {exc}") from exc
    return parse_json_object_bytes(raw, label=str(path)), raw


def load_json_object_bounded(
    path: Path, *, max_bytes: int
) -> tuple[dict[str, Any], bytes]:
    if not isinstance(max_bytes, int) or isinstance(max_bytes, bool) or max_bytes <= 0:
        raise ValidationError("JSON source byte limit must be a positive integer")
    try:
        with path.open("rb") as source:
            chunks: list[bytes] = []
            remaining = max_bytes + 1
            while remaining:
                chunk = source.read(min(64 * 1024, remaining))
                if not chunk:
                    break
                chunks.append(chunk)
                remaining -= len(chunk)
            raw = b"".join(chunks)
    except OSError as exc:
        raise ValidationError(f"Cannot read JSON source {path}: {exc}") from exc
    if len(raw) > max_bytes:
        raise BudgetError(
            f"JSON source {path} exceeds the {max_bytes}-byte limit. "
            "Nothing was truncated."
        )
    return parse_json_object_bytes(raw, label=str(path)), raw


def json_pointer_escape(value: str) -> str:
    return value.replace("~", "~0").replace("/", "~1")


def _validate_relative_path(relative: Path) -> None:
    if relative.is_absolute() or not relative.parts:
        raise PathConfinementError(f"Artifact path must be relative: {relative}")
    if any(part in {"", ".", ".."} for part in relative.parts):
        raise PathConfinementError(f"Unsafe artifact path: {relative}")


def confined_destination(root: Path, relative: Path) -> Path:
    """Resolve a destination while rejecting traversal and symlink escapes."""
    _validate_relative_path(relative)
    v3_real = V3_ROOT.resolve()

    root_absolute = root.absolute()
    if ".." in root_absolute.parts:
        raise PathConfinementError(f"Unsafe artifact root: {root}")
    v3_absolute = V3_ROOT.absolute()
    if not root_absolute.is_relative_to(v3_absolute):
        raise PathConfinementError(f"Artifact root escapes v3: {root}")
    root_relative = root_absolute.relative_to(v3_absolute)
    current = V3_ROOT
    for part in root_relative.parts:
        current = current / part
        if current.is_symlink():
            raise PathConfinementError(
                f"Artifact root ancestor may not be a symlink: {current}"
            )
        if current.exists():
            if not current.is_dir():
                raise PathConfinementError(
                    f"Artifact root ancestor is not a directory: {current}"
                )
            if not current.resolve().is_relative_to(v3_real):
                raise PathConfinementError(f"Artifact root escapes v3: {root}")
            continue
        try:
            current.mkdir()
        except OSError as exc:
            raise ValidationError(
                f"Cannot create confined artifact directory {current}: {exc}"
            ) from exc
    root_real = root.resolve()
    if not root_real.is_relative_to(v3_real):
        raise PathConfinementError(f"Artifact root escapes v3: {root}")

    root = root_absolute
    current = root
    for part in relative.parts[:-1]:
        current = current / part
        if current.is_symlink():
            raise PathConfinementError(
                f"Artifact directory may not be a symlink: {current}"
            )
        if current.exists() and not current.is_dir():
            raise PathConfinementError(
                f"Artifact directory is not a directory: {current}"
            )
        try:
            current.mkdir(exist_ok=True)
        except OSError as exc:
            raise ValidationError(
                f"Cannot create confined artifact directory {current}: {exc}"
            ) from exc

    destination = root / relative
    if destination.is_symlink():
        raise PathConfinementError(
            f"Artifact destination may not be a symlink: {destination}"
        )
    if not destination.parent.resolve().is_relative_to(root_real):
        raise PathConfinementError(f"Artifact path escapes root: {destination}")
    return destination


def confined_existing_file(root: Path, relative: Path) -> Path:
    """Resolve an existing regular file without permitting symlink escapes."""
    _validate_relative_path(relative)
    v3_real = V3_ROOT.resolve()
    if root.is_symlink():
        raise PathConfinementError(f"Artifact root may not be a symlink: {root}")
    try:
        root_real = root.resolve(strict=True)
    except OSError as exc:
        raise ValidationError(f"Artifact root is unavailable: {root}: {exc}") from exc
    if not root_real.is_relative_to(v3_real):
        raise PathConfinementError(f"Artifact root escapes v3: {root}")

    current = root
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise PathConfinementError(f"Artifact path may not be a symlink: {current}")
    try:
        resolved = current.resolve(strict=True)
    except OSError as exc:
        raise ValidationError(f"Artifact does not exist: {current}: {exc}") from exc
    if not resolved.is_relative_to(root_real):
        raise PathConfinementError(f"Artifact path escapes root: {current}")
    if not resolved.is_file():
        raise ValidationError(f"Artifact is not a regular file: {current}")
    return resolved


def validate_exact_prompt_files(
    root: Path,
    prompt_relative: Path,
    manifest_relative: Path,
    *,
    expected_prompt: str,
    expected_manifest: dict[str, Any],
    label: str,
) -> None:
    """Require the persisted model handoff to equal its current derivation."""
    prompt_path = confined_existing_file(root, prompt_relative)
    if prompt_path.read_bytes() != expected_prompt.encode("utf-8"):
        raise ValidationError(f"{label} prompt file is not current")
    manifest_path = confined_existing_file(root, manifest_relative)
    if manifest_path.read_bytes() != pretty_json_bytes(expected_manifest):
        raise ValidationError(f"{label} prompt manifest is not current")


def write_bytes_confined(
    root: Path,
    relative: Path,
    payload: bytes,
    *,
    replace: bool = False,
) -> Path:
    """Atomically write exact bytes beneath a v3-owned root."""
    destination = confined_destination(root, relative)
    if destination.exists():
        existing = destination.read_bytes()
        if existing == payload:
            return destination
        if not replace:
            raise ArtifactConflictError(
                f"Artifact exists with different content: {destination}. "
                "Use the explicit force option to replace it."
            )
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            dir=destination.parent,
            prefix=f".{destination.name}.",
            delete=False,
        ) as handle:
            temporary = Path(handle.name)
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, destination)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()
    return destination


def preflight_confined_writes(
    root: Path,
    artifacts: dict[Path, bytes],
    *,
    replace: bool = False,
) -> dict[Path, Path]:
    """Check a related artifact set for conflicts before publishing any member."""
    destinations: dict[Path, Path] = {}
    for relative, payload in artifacts.items():
        destination = confined_destination(root, relative)
        destinations[relative] = destination
        if destination.exists() and destination.read_bytes() != payload and not replace:
            raise ArtifactConflictError(
                f"Artifact exists with different content: {destination}. "
                "Use the explicit force option to replace the artifact set."
            )
    return destinations


def write_json_confined(
    root: Path,
    relative: Path,
    value: Any,
    *,
    replace: bool = False,
) -> Path:
    """Atomically write deterministic JSON beneath a v3-owned root."""
    return write_bytes_confined(
        root,
        relative,
        pretty_json_bytes(value),
        replace=replace,
    )
