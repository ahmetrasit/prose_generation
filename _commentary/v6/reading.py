"""Deterministic, bounded views of a frozen V6 evidence packet.

The budget is UTF-8 bytes, a conservative upper bound for byte-tokenized text,
not a characters/4 estimate or an assertion about the active model's tokenizer.
No lexical evidence is summarized, filtered by strength, or fetched externally.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


PLAN_SCHEMA = "commentary-v6-reading-plan-v1"
DEFAULT_BATCH_BUDGET = 120_000
READ_BYTES = 24_000
REGISTRIES = {
    "candidate_inventory": "candidate_id",
    "support_registry": "support_id",
    "branch_registry": "branch_ref",
    "connection_registry": "connection_ref",
    "context_evidence": "ayah_ref",
    "selected_context_units": "ayah_ref",
}


class ReadingError(ValueError):
    pass


def encode(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":")).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(encode(value)).hexdigest()


def escape(value: str) -> str:
    return value.replace("~", "~0").replace("/", "~1")


def resolve(packet: dict[str, Any], pointer: str) -> Any:
    """Resolve emitted JSON Pointers, including JSON-encoded support text."""
    if not isinstance(pointer, str) or not pointer.startswith("/"):
        raise ReadingError(f"Expected a packet JSON Pointer: {pointer!r}")
    value: Any = packet
    for raw in pointer[1:].split("/"):
        part = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(value, str):
            try:
                value = json.loads(value)
            except ValueError as exc:
                raise ReadingError(f"Pointer enters plain text: {pointer}") from exc
        try:
            if isinstance(value, list):
                if part.isdigit():
                    value = value[int(part)]
                else:
                    matches = [row for row in value if isinstance(row, dict)
                               and any(row.get(key) == part
                                       for key in REGISTRIES.values())]
                    if len(matches) != 1:
                        raise KeyError(part)
                    value = matches[0]
            elif isinstance(value, dict):
                value = value[part]
            else:
                raise KeyError(part)
        except (KeyError, IndexError, TypeError) as exc:
            raise ReadingError(f"Unknown packet pointer: {pointer}") from exc
    return value


def registry_maps(packet: dict[str, Any]) -> dict[str, dict[str, str]]:
    result = {}
    for registry, key in REGISTRIES.items():
        rows = packet.get(registry, [])
        if not isinstance(rows, list):
            raise ReadingError(f"{registry} must be an array")
        index = {}
        for number, row in enumerate(rows):
            identity = row.get(key) if isinstance(row, dict) else None
            if not isinstance(identity, str) or not identity or identity in index:
                raise ReadingError(f"Missing or duplicate {registry} identity: {identity!r}")
            index[identity] = f"/{registry}/{number}"
        result[registry] = index
    return result


def make_plan(packet: dict[str, Any], *, analysis_id: str,
              batch_budget: int = DEFAULT_BATCH_BUDGET) -> dict[str, Any]:
    if not isinstance(batch_budget, int) or isinstance(batch_budget, bool) or not 8_000 <= batch_budget <= 160_000:
        raise ReadingError("Batch budget must be between 8,000 and 160,000 UTF-8 bytes")
    indexes = registry_maps(packet)
    packet_hash = digest(packet)
    read_bytes = min(READ_BYTES, batch_budget)
    batches: list[dict[str, Any]] = []
    assigned: set[str] = set()
    counts: dict[str, int] = {}

    def add(stage: str, groups: list[list[str]]) -> None:
        pending: list[str] = []
        pending_bytes = 0

        def emit(pointers: list[str], cost: int, **extra: Any) -> None:
            counts[stage] = counts.get(stage, 0) + 1
            batches.append({"batch_id": f"{stage}-{counts[stage]:03d}",
                            "stage": stage, "pointers": pointers,
                            "evidence_bytes": cost, **extra})

        def flush() -> None:
            nonlocal pending, pending_bytes
            if pending:
                emit(pending, pending_bytes)
                pending, pending_bytes = [], 0

        for group in groups:
            remaining = [p for p in dict.fromkeys(group) if p not in assigned]
            group_bytes = sum(len(encode(resolve(packet, p))) for p in remaining)
            if pending and pending_bytes + group_bytes > batch_budget:
                flush()
            # Related records stay together where they fit. Large dependency
            # groups remain linked by their original refs and may span batches.
            for pointer in remaining:
                cost = len(encode(resolve(packet, pointer)))
                if pending and pending_bytes + cost > batch_budget:
                    flush()
                if cost > batch_budget:
                    # Even one unusually large record must checkpoint within
                    # the budget. Page ranges preserve it without duplicating
                    # or silently truncating its fields or long strings.
                    record_pages = pages(packet, [pointer], label="large_record",
                                         packet_sha256=packet_hash, read_bytes=read_bytes)
                    first, size = 1, 0
                    for number, page in enumerate(record_pages, 1):
                        page_size = len(encode(page))
                        if size and size + page_size > batch_budget:
                            emit([pointer], size, record_pages=[first, number - 1])
                            first, size = number, 0
                        size += page_size
                    emit([pointer], size, record_pages=[first, len(record_pages)])
                    assigned.add(pointer)
                    continue
                pending.append(pointer)
                pending_bytes += cost
                assigned.add(pointer)
                if pending_bytes >= batch_budget:
                    flush()
        flush()

    # Include all non-registry fields once, including HFT material, coverage,
    # the complete focus, and the existing authoritative review inventory.
    add("focus", [["/" + escape(key)] for key in sorted(packet)
                  if key not in REGISTRIES])
    branch_groups: dict[str, list[str]] = {}
    for row in packet.get("branch_registry", []):
        key = row.get("root_id") or row["branch_ref"]
        branch_groups.setdefault(key, []).append(indexes["branch_registry"][row["branch_ref"]])
    add("branches", list(branch_groups.values()))
    candidate_groups = []
    for row in packet.get("candidate_inventory", []):
        group = [indexes["candidate_inventory"][row["candidate_id"]]]
        for support_id in row.get("support_ids", []):
            try:
                group.append(indexes["support_registry"][support_id])
            except KeyError as exc:
                raise ReadingError(f"Candidate cites unknown support: {support_id}") from exc
        for ref in row.get("required_context_refs", []):
            if ref not in indexes["context_evidence"]:
                raise ReadingError(f"Candidate lacks its context record: {ref}")
            group.append(indexes["context_evidence"][ref])
        candidate_groups.append(group)
    add("candidates", candidate_groups)
    add("supports", [[p] for p in indexes["support_registry"].values()])
    connection_groups: dict[str, list[str]] = {}
    for row in packet.get("connection_registry", []):
        group = connection_groups.setdefault(row.get("target_ref", row["connection_ref"]), [])
        group.append(indexes["connection_registry"][row["connection_ref"]])
        for ref in row.get("required_context_refs", []):
            if ref not in indexes["context_evidence"]:
                raise ReadingError(f"Connection lacks its context record: {ref}")
            group.append(indexes["context_evidence"][ref])
    add("connections", list(connection_groups.values()))
    add("context", [[p] for p in indexes["selected_context_units"].values()]
        + [[p] for p in indexes["context_evidence"].values()])
    expected = {"/" + escape(k) for k in packet if k not in REGISTRIES}
    expected.update(p for index in indexes.values() for p in index.values())
    if assigned != expected:
        raise ReadingError("Reading plan omitted packet records")
    return {
        "schema_version": PLAN_SCHEMA,
        "reader_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "checkpoint_helper_sha256": hashlib.sha256(Path(__file__).with_name("discovery.py").read_bytes()).hexdigest(),
        "analysis_id": analysis_id,
        "ayah_ref": packet["identity"]["ayah_ref"],
        "lane": packet["identity"]["lane"],
        "packet_sha256": packet_hash,
        "budget_basis": "utf8_bytes_conservative_not_exact_tokens",
        "batch_budget": batch_budget,
        "read_bytes": read_bytes,
        "record_counts": {key: len(index) for key, index in indexes.items()},
        "batches": batches,
    }


def _pieces(value: Any, pointer: str, record_pointer: str,
            record_id: str | None, limit: int) -> list[dict[str, Any]]:
    item = {"record_pointer": record_pointer, "record_id": record_id,
            "source_pointer": pointer, "value": value}
    if len(encode(item)) <= limit:
        return [item]
    if isinstance(value, dict):
        return [piece for k in sorted(value)
                for piece in _pieces(value[k], pointer + "/" + escape(k),
                                     record_pointer, record_id, limit)]
    if isinstance(value, list):
        return [piece for i, v in enumerate(value)
                for piece in _pieces(v, pointer + f"/{i}",
                                     record_pointer, record_id, limit)]
    if isinstance(value, str):
        pieces = []
        start = 0
        while start < len(value):
            end = len(value)
            while True:
                fragment = {**item, "value": value[start:end],
                            "string_fragment": {"start": start, "end": end,
                                                "total_characters": len(value)}}
                if len(encode(fragment)) <= limit:
                    break
                end = start + (end - start) // 2
                if end <= start:
                    raise ReadingError("Read budget cannot fit a source fragment")
            pieces.append(fragment)
            start = end
        return pieces
    raise ReadingError(f"Cannot page oversized value at {pointer}")


def pages(packet: dict[str, Any], pointers: list[str], *, label: str,
          packet_sha256: str, read_bytes: int = READ_BYTES) -> list[dict[str, Any]]:
    """Return bounded, lossless record pieces with exact source coordinates."""
    if not 2_000 <= read_bytes <= READ_BYTES:
        raise ReadingError(f"Read size must be between 2,000 and {READ_BYTES} bytes")
    metadata = {"packet_sha256": packet_sha256, "view": label,
                "context_morpheme_columns": packet.get("context_morpheme_columns", [])}
    capacity = read_bytes - len(encode(metadata)) - 500
    chunks: list[list[dict[str, Any]]] = []
    pending: list[dict[str, Any]] = []
    used = 0
    for pointer in pointers:
        value = resolve(packet, pointer)
        identity = next((value[k] for k in REGISTRIES.values()
                         if isinstance(value, dict) and isinstance(value.get(k), str)), None)
        for item in _pieces(value, pointer, pointer, identity, capacity):
            cost = len(encode(item)) + 1
            if pending and used + cost > capacity:
                chunks.append(pending)
                pending, used = [], 0
            pending.append(item)
            used += cost
    if pending or not chunks:
        chunks.append(pending)
    result = [{**metadata, "page": i + 1, "page_count": len(chunks),
               "records": records, "page_complete": True}
              for i, records in enumerate(chunks)]
    if any(len(encode(page)) > read_bytes for page in result):
        raise ReadingError("Rendered page exceeds its read budget")
    return result


def batch_pages(packet: dict[str, Any], plan: dict[str, Any],
                batch: dict[str, Any]) -> list[dict[str, Any]]:
    interval = batch.get("record_pages")
    output = pages(packet, batch["pointers"],
                   label="large_record" if interval else batch["batch_id"],
                   packet_sha256=plan["packet_sha256"], read_bytes=plan["read_bytes"])
    if interval:
        first, last = interval
        output = output[first - 1:last]
        output = [{**p, "view": batch["batch_id"], "page": i + 1,
                   "page_count": len(output)} for i, p in enumerate(output)]
    return output


def load_plan(path: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    """Only the plan's adjacent frozen snapshot and instructions are read."""
    if path.is_symlink() or not path.is_file():
        raise ReadingError("Reading plan must be a regular file")
    try:
        plan = json.loads(path.read_bytes())
        lane = plan["lane"]
        if lane not in {"micro", "macro", "global"} or path.name != f"{lane}.reading.json":
            raise ReadingError("Reading plan filename and lane differ")
        packet_path = path.with_name(f"{lane}.packet.json")
        prompt_path = path.with_name(f"{lane}.discovery.prompt.md")
        if packet_path.is_symlink() or prompt_path.is_symlink():
            raise ReadingError("Frozen input files may not be symlinks")
        packet = json.loads(packet_path.read_bytes())
        expected = make_plan(packet, analysis_id=plan["analysis_id"],
                             batch_budget=plan["batch_budget"])
        expected["instructions_sha256"] = hashlib.sha256(prompt_path.read_bytes()).hexdigest()
        if expected != plan:
            raise ReadingError("Reading plan, evidence or instructions changed; prepare a fresh run")
        return plan, packet
    except (OSError, ValueError, KeyError, TypeError) as exc:
        if isinstance(exc, ReadingError):
            raise
        raise ReadingError(f"Cannot load reading package: {exc}") from exc
