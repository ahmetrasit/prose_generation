#!/usr/bin/env python3
"""Read complete evidence records and assemble V7 authoring handoffs.

No semantic selection, generated findings, or persistent reading state lives here.
Agent-authored files are only read, never rewritten.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from _commentary.v7 import workflow as w


SECTIONS = {
    "candidate_inventory": ("candidate", "candidate_id"),
    "support_registry": ("support", "support_id"),
    "branch_registry": ("branch", "branch_ref"),
    "connection_registry": ("connection", "connection_evidence_ref"),
    "context_evidence": ("context", "ayah_ref"),
}
READ_BYTES = 28_000
BLOCK_NAMES = (
    "authoring_inputs", "first_pass_prose",
    *(f"{lane}_{kind}" for lane in w.LANES
      for kind in ("discovery_json", "scope_prose", "source_evidence_json")),
)


def read_text(path: Path) -> str:
    if path.stat().st_size > w.MAX_JSON_BYTES:
        raise w.WorkflowError(f"Input exceeds the file limit: {path}")
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        raise w.WorkflowError(f"Input is empty: {path}")
    return text


def read_packet(path: Path) -> dict[str, Any]:
    text = read_text(path)
    opening, closing = "\n<lane_packet_json>\n", "\n</lane_packet_json>"
    if text.count(opening) != 1 or text.count(closing) != 1:
        raise w.WorkflowError(f"Expected one complete lane packet: {path}")
    packet = json.loads(text.split(opening, 1)[1].split(closing, 1)[0])
    if not isinstance(packet, dict):
        raise w.WorkflowError(f"Lane packet is not an object: {path}")
    return packet


def source_index(packet: dict[str, Any]) -> dict[str, Any]:
    records: dict[str, Any] = {}
    for section, (kind, id_key) in SECTIONS.items():
        if section == "connection_registry":
            continue
        for record in packet[section]:
            ref = f"{kind}:{record[id_key]}"
            if ref in records:
                raise w.WorkflowError(f"Duplicate evidence identity: {ref}")
            records[ref] = record
    # A conceptual connection can have several independently qualified rows.
    # Resolving its alias returns every row, never just the first match.
    connections: dict[str, list[dict[str, Any]]] = {}
    for record in packet["connection_registry"]:
        ids = {record["connection_ref"], record.get("connection_evidence_ref")}
        # Derived reciprocal nominations have no top-level evidence ID. Their
        # IDs identify records inside the full receiving-direction wrapper.
        ids.update(row.get("connection_evidence_ref")
                   for row in record.get("reciprocal_evidence", []))
        for identity in ids - {None}:
            rows = connections.setdefault(f"connection:{identity}", [])
            if record not in rows:
                rows.append(record)
    records.update(connections)
    return records


def validate_discovery(discovery: Any, packet: dict[str, Any]) -> None:
    """Validate transport identities and shape, not whether a reading is sound."""
    if not isinstance(discovery, dict):
        raise w.WorkflowError("Discovery must be a JSON object")
    identity = packet["identity"]
    for key, expected in (("schema_version", w.SCOPE_DISCOVERY_SCHEMA_VERSION),
                          ("ayah_ref", identity["ayah_ref"]), ("lane", identity["lane"])):
        if discovery.get(key) != expected:
            raise w.WorkflowError(f"Discovery {key} must be {expected!r}")
    for key in ("findings", "candidate_decisions", "friction_notes"):
        if not isinstance(discovery.get(key), list):
            raise w.WorkflowError(f"Discovery {key} must be an array")
    index = source_index(packet)
    finding_refs: set[str] = set()
    for finding in discovery["findings"]:
        if not isinstance(finding, dict):
            raise w.WorkflowError("Each finding must be an object")
        for key in ("finding_ref", "title", "reading"):
            if not isinstance(finding.get(key), str) or not finding[key].strip():
                raise w.WorkflowError(f"Finding needs nonempty {key}")
        ref = finding["finding_ref"]
        if not ref.startswith(identity["lane"] + ":") or ref in finding_refs:
            raise w.WorkflowError(f"Invalid or duplicate finding identity: {ref}")
        finding_refs.add(ref)
        sources = finding.get("evidence_refs")
        if not isinstance(sources, list) or any(not isinstance(x, str) for x in sources):
            raise w.WorkflowError(f"{ref}: evidence_refs must be an array of strings")
        for source in sources:
            if source not in index:
                raise w.WorkflowError(f"{ref}: evidence does not exist in this lane: {source}")
    candidates = {c["candidate_id"] for c in packet["candidate_inventory"]
                  if c.get("kind") != "focus_root_occurrence"}
    seen: set[str] = set()
    for decision in discovery["candidate_decisions"]:
        if not isinstance(decision, dict):
            raise w.WorkflowError("Each candidate decision must be an object")
        ref = decision.get("candidate_id")
        if not isinstance(ref, str) or ref not in candidates or ref in seen:
            raise w.WorkflowError(f"Invalid or duplicate candidate identity: {ref}")
        seen.add(ref)
        if decision.get("decision") not in {"accept", "narrow", "represented", "reject"}:
            raise w.WorkflowError(f"{ref}: unknown decision")
        if not isinstance(decision.get("reason"), str) or not decision["reason"].strip():
            raise w.WorkflowError(f"{ref}: decision needs a reason")
        refs = decision.get("finding_refs")
        if not isinstance(refs, list) or any(not isinstance(x, str) or x not in finding_refs for x in refs):
            raise w.WorkflowError(f"{ref}: finding_refs contains an unknown finding")
        if bool(refs) != (decision["decision"] != "reject"):
            raise w.WorkflowError(f"{ref}: retained decisions need findings; rejected decisions have none")
    if seen != candidates:
        raise w.WorkflowError("Missing candidate decisions: " + ", ".join(sorted(candidates - seen)))


def attached_evidence(discovery: dict[str, Any], packet: dict[str, Any]) -> dict[str, Any]:
    """Copy source records once, retaining every field and statement variant."""
    index = source_index(packet)
    refs = {ref for f in discovery["findings"] for ref in f["evidence_refs"]}
    refs.update("candidate:" + d["candidate_id"] for d in discovery["candidate_decisions"])
    # Include candidate-specific source material even if a writer omitted its
    # explicit citation. Availability is not an activation or a verdict.
    for ref in list(refs):
        if ref.startswith("candidate:"):
            candidate = index[ref]
            for field, kind in (("candidate_specific_support_ids", "support"),
                                ("branch_refs", "branch"), ("required_context_refs", "context")):
                refs.update(f"{kind}:{value}" for value in candidate.get(field, [])
                            if f"{kind}:{value}" in index)
    return {
        "identity": packet["identity"],
        "analysis_context": packet.get("analysis_context"),
        "scope": packet["scope"],
        "focus": packet["focus"],
        "focus_surface_evidence": packet["focus_surface_evidence"],
        "focus_word_alignment": packet["focus_word_alignment"],
        "context_morpheme_columns": packet["context_morpheme_columns"],
        "context_evidence_coverage": packet["context_evidence_coverage"],
        "records": [{"evidence_ref": ref, "record": index[ref]} for ref in sorted(refs)],
    }


def block(name: str, content: str) -> str:
    return f"<{name}>\n{content}\n</{name}>"


def block_text(text: str, name: str) -> str:
    if name not in BLOCK_NAMES:
        raise w.WorkflowError(f"Unknown authoring block: {name}")
    opening, closing = f"<{name}>\n", f"\n</{name}>"
    if text.count(opening) != 1 or text.count(closing) != 1:
        raise w.WorkflowError(f"Expected one complete {name} block")
    return text.split(opening, 1)[1].split(closing, 1)[0]


def render_handoff(layout: w.Layout, stage: str, lane: str | None = None) -> tuple[Path, str]:
    if stage not in {"composition", "canonical", "editorial"}:
        raise w.WorkflowError(f"Unknown handoff stage: {stage}")
    if (stage == "composition" and lane not in w.LANES) or (stage != "composition" and lane is not None):
        raise w.WorkflowError("--lane is required only for composition")
    lanes = (lane,) if lane else w.LANES
    inputs, evidence, commands = [], [], []
    for scope in lanes:
        prompt_path = layout.scope_prompt(scope)
        packet = read_packet(prompt_path)
        if packet["identity"]["ayah_ref"] != layout.ayah_ref or packet["identity"]["lane"] != scope:
            raise w.WorkflowError(f"Wrong packet identity: {prompt_path}")
        raw_discovery = read_text(layout.scope_discovery(scope))
        discovery = json.loads(raw_discovery)
        validate_discovery(discovery, packet)
        inputs.append(block(f"{scope}_discovery_json", raw_discovery))
        if stage != "composition":
            inputs.append(block(f"{scope}_scope_prose", read_text(layout.scope_prose(scope))))
        evidence.append(block(f"{scope}_source_evidence_json", w._record_line_json(attached_evidence(discovery, packet))))
        commands.append(f"- {scope}: `python3 _commentary/v7/authoring.py read --prompt {w._repo_path(prompt_path)} --section SECTION`")
    if stage == "editorial":
        inputs.insert(0, block("first_pass_prose", read_text(layout.consolidated_prose())))
    output = (layout.scope_prose(lane) if stage == "composition" else
              layout.consolidated_prose() if stage == "canonical" else layout.editorial_prose())
    path = (layout.scope_composition_prompt(lane) if stage == "composition" else
            layout.canonical_prompt() if stage == "canonical" else layout.editorial_prompt())
    values = {
        "@@AYAH_REF@@": layout.ayah_ref,
        "@@READING_STANDARD@@": read_text(w.PROMPTS_ROOT / "reading-standard.md"),
        "@@AUTHORING_INPUTS@@": block("authoring_inputs", "\n\n".join(inputs)),
        "@@EVIDENCE_INPUTS@@": "\n\n".join(evidence),
        "@@SOURCE_COMMANDS@@": "\n".join(commands),
        "@@HANDOFF_PROMPT_PATH@@": w._repo_path(path),
        "@@PROSE_OUTPUT_PATH@@": w._repo_path(output),
    }
    if lane:
        values["@@LANE@@"] = lane
    prompt = w._render(read_text(w.PROMPTS_ROOT / f"{stage}.md"), values, label=f"{stage} handoff")
    if len(prompt.encode("utf-8")) > w.MAX_JSON_BYTES:
        raise w.WorkflowError("Handoff exceeds the file limit; no input was dropped")
    return path, prompt


def text_window(text: str, offset: int, limit: int) -> dict[str, Any]:
    if offset < 0 or offset > len(text) or limit < 1 or limit > READ_BYTES:
        raise w.WorkflowError(f"Invalid text window; limit must be 1–{READ_BYTES} characters")
    end = min(len(text), offset + limit)
    return {"offset": offset, "next_offset": end if end < len(text) else None,
            "total_characters": len(text), "text": text[offset:end]}


def read_evidence(args: argparse.Namespace) -> dict[str, Any]:
    text = read_text(args.prompt)
    if args.block:
        return text_window(block_text(text, args.block), args.offset or 0, args.limit)
    if not args.section and not args.refs:
        if args.offset is not None:
            return text_window(text, args.offset, args.limit)
        # A quick first read exposes instructions and available blocks without
        # spending the output budget on an arbitrary fragment of source data.
        marker = ("\n<lane_packet_json>\n" if "\n<lane_packet_json>\n" in text
                  else "\n<authoring_inputs>\n")
        if marker not in text:
            raise w.WorkflowError("Not a V7 discovery or authoring prompt")
        instructions = text.split(marker, 1)[0]
        if len(instructions.encode("utf-8")) > READ_BYTES:
            return text_window(text, 0, args.limit)
        blocks = {name: len(block_text(text, name)) for name in BLOCK_NAMES
                  if f"<{name}>\n" in text}
        return {"instructions": instructions, "blocks_characters": blocks,
                "packet_sections": list(read_packet(args.prompt)) if "lane_packet_json" in marker else []}
    packet = read_packet(args.prompt)
    if args.refs:
        index = source_index(packet)
        missing = set(args.refs) - index.keys()
        if missing:
            raise w.WorkflowError("Unknown source references: " + ", ".join(sorted(missing)))
        records = [{"evidence_ref": ref, "record": index[ref]} for ref in args.refs]
    else:
        if args.section not in packet:
            raise w.WorkflowError("Unknown packet section: " + str(args.section))
        section = packet[args.section]
        records = section if isinstance(section, list) else [section]
    if args.start < 0 or args.start > len(records) or args.count < 1:
        raise w.WorkflowError("Invalid record range")
    if args.offset is not None:
        window_records = records[args.start:args.start + args.count]
        return text_window(json.dumps(window_records, ensure_ascii=False, indent=2), args.offset, args.limit)
    selected = []
    size = 0
    end = args.start
    for record in records[args.start:args.start + args.count]:
        record_size = len(json.dumps(record, ensure_ascii=False).encode("utf-8"))
        if size + record_size > READ_BYTES:
            if selected:
                break
            raise w.WorkflowError(
                f"Record {end} exceeds the whole-record output budget. Read it intact in text windows "
                f"with --start {end} --count 1 --offset 0, then each returned next_offset; "
                "keep the same --section or --refs."
            )
        selected.append(record)
        size += record_size
        end += 1
    return {"section": args.section, "start": args.start, "total_records": len(records),
            "next_start": end if end < len(records) else None,
            "context_morpheme_columns": packet["context_morpheme_columns"], "records": selected}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    read = sub.add_parser("read", help="Read whole records, or exact text windows without filtering")
    read.add_argument("--prompt", type=Path, required=True)
    selection = read.add_mutually_exclusive_group()
    selection.add_argument("--section")
    selection.add_argument("--refs", nargs="+")
    selection.add_argument("--block", choices=BLOCK_NAMES)
    read.add_argument("--start", type=int, default=0)
    read.add_argument("--count", type=int, default=20)
    read.add_argument("--offset", type=int)
    read.add_argument("--limit", type=int, default=12_000)
    handoff = sub.add_parser("handoff", help="Embed complete existing inputs and their cited source records")
    handoff.add_argument("--ayah", required=True)
    handoff.add_argument("--analysis-id", default="native")
    handoff.add_argument("--stage", choices=("composition", "canonical", "editorial"), required=True)
    handoff.add_argument("--lane", choices=w.LANES)
    args = parser.parse_args()
    try:
        if args.command == "read":
            result = read_evidence(args)
        else:
            layout = w.layout_for(args.ayah, args.analysis_id)
            path, prompt = render_handoff(layout, args.stage, args.lane)
            w._atomic_write(path, prompt.encode("utf-8"), root=w.INPUT_ROOT)
            result = {"status": "rendered", "prompt": w._repo_path(path),
                      "bytes": len(prompt.encode("utf-8"))}
        print(json.dumps(result, ensure_ascii=False))
        return 0
    except (w.WorkflowError, OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"status": "error", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
