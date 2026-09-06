#!/usr/bin/env python3
"""Read frozen evidence, checkpoint discovery, and publish a checked result.

One agent owns one work file. The helper records delivery and completion;
the agent owns all analytical wording, decisions, observations and findings.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from typing import Any

V6_ROOT = Path(__file__).resolve().parent
ROOT = V6_ROOT.parents[1]
sys.path.insert(0, str(ROOT))
from _commentary.v6 import reading

RAW_ROOT = V6_ROOT / "raw"
WORK_SCHEMA = "commentary-v6-discovery-work-v2"
DISCOVERY_SCHEMA = "commentary-v6-scope-discovery-v2"
DECISIONS = {"accept", "narrow", "represented", "reject"}
EXCLUSIONS = {
    "branch_exclusions": "branch_ref",
    "context_exclusions": "context_ref",
    "semantic_obligation_exclusions": "obligation_ref",
}


class DiscoveryError(ValueError):
    pass


def _require(condition: Any, message: str) -> None:
    if not condition:
        raise DiscoveryError(message)


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _strings(value: Any, label: str) -> list[str]:
    _require(isinstance(value, list) and all(_text(v) for v in value), f"{label} must be a string array")
    _require(len(value) == len(set(value)), f"{label} repeats an identity")
    return value


def _rows(value: Any, label: str) -> list[dict[str, Any]]:
    _require(isinstance(value, list) and all(isinstance(v, dict) for v in value),
             f"{label} must be an object array")
    return value


def _atomic(path: Path, value: Any, root: Path, *, replace: bool = True) -> None:
    absolute = Path(os.path.abspath(path))
    base = Path(os.path.abspath(root))
    try:
        relative = absolute.relative_to(base)
    except ValueError as exc:
        raise DiscoveryError("Work path escapes the output root") from exc
    cursor = base
    _require(not cursor.is_symlink(), "Output root is a symlink")
    for part in relative.parts:
        cursor /= part
        _require(not cursor.is_symlink(), "Work path crosses a symlink")
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.", suffix=".tmp")
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(reading.encode(value) + b"\n")
            stream.flush()
            os.fsync(stream.fileno())
        if replace:
            os.replace(temporary, path)
        else:
            os.link(temporary, path)  # Publish atomically without replacing another result.
    finally:
        temporary.unlink(missing_ok=True)


def _source_refs(packet: dict[str, Any]) -> tuple[set[str], set[str]]:
    known: set[str] = set()
    focus: set[str] = set()
    focus_record = packet.get("focus", {})
    for owner in (focus_record, packet.get("focus_surface_evidence", {})):
        for field in ("word_analysis_refs", "word_analysis_qac_refs"):
            focus.update(v for v in owner.get(field, []) if isinstance(v, str))
        for row in owner.get("qac_morphemes", []):
            focus.update(row[k] for k in ("qac_ref", "qac_word_ref") if isinstance(row.get(k), str))
    known.update(focus)
    known.add(packet["identity"]["ayah_ref"])
    for registry, index in reading.registry_maps(packet).items():
        known.update(index)
    for unit in packet.get("context_evidence", []):
        for row in unit.get("morphemes", []):
            if row and isinstance(row[0], str):
                known.add(row[0])
                known.add(row[0].rsplit(":", 1)[0])
    for branch in packet.get("branch_registry", []):
        for field in ("focus_root_occurrences", "context_root_occurrences"):
            for row in branch.get(field, []):
                known.update(row[k] for k in ("qac_ref", "qac_word_ref") if isinstance(row.get(k), str))
    return known, focus


def validate_discovery(packet: dict[str, Any], result: dict[str, Any]) -> None:
    """Check explicit source accounting, not the truth of an interpretation."""
    lane = packet["identity"]["lane"]
    _require(set(result) == {"schema_version", "ayah_ref", "lane", "coverage_complete",
                             "candidate_decisions", "findings", "friction_notes"},
             "Discovery has missing or unexpected top-level fields")
    _require(result["schema_version"] == DISCOVERY_SCHEMA, "Wrong discovery schema")
    _require(result["ayah_ref"] == packet["identity"]["ayah_ref"] and result["lane"] == lane,
             "Discovery focus or lane differs from the packet")
    _require(result["coverage_complete"] is True, "Discovery is still incomplete")
    _strings(result["friction_notes"], "friction_notes")
    indexes = reading.registry_maps(packet)
    candidates = {r["candidate_id"]: r for r in packet.get("candidate_inventory", [])}
    branches = {r["branch_ref"]: r for r in packet.get("branch_registry", [])}
    known, focus_refs = _source_refs(packet)
    contexts = set(indexes["context_evidence"])
    focus_ayahs = {packet["identity"]["ayah_ref"],
                  packet["identity"].get("linguistic_source_ref")}
    all_obligations = {r["obligation_ref"] for c in candidates.values()
                       for r in c.get("semantic_obligations", [])}
    findings = {}
    landed_contexts: dict[str, set[str]] = {}
    for finding in _rows(result["findings"], "findings"):
        ref = finding.get("finding_ref")
        _require(_text(ref) and ref.startswith(lane + ":") and ref not in findings,
                 f"Invalid or duplicate finding ref: {ref}")
        findings[ref] = finding
        for key in ("title", "claim", "mechanism", "reader_payoff", "containment"):
            _require(_text(finding.get(key)), f"{ref} lacks {key}")
        origin = finding.get("origin_candidate_id")
        _require(origin is None or origin in candidates, f"{ref} has unknown origin candidate")
        for key, allowed in (("support_ids", set(indexes["support_registry"])),
                             ("connection_refs", set(indexes["connection_registry"])),
                             ("context_refs", contexts),
                             ("semantic_obligation_refs", all_obligations),
                             ("represented_candidate_ids", set(candidates))):
            _require(set(_strings(finding.get(key), f"{ref}.{key}")) <= allowed,
                     f"{ref} cites unknown {key}")
        epistemic = finding.get("epistemic", {})
        _require(isinstance(epistemic, dict) and epistemic.get("status") in
                 {"grounded", "qualified", "exploratory"} and _text(epistemic.get("reason")),
                 f"{ref} lacks an epistemic qualification")
        _strings(epistemic.get("source_trust"), f"{ref}.source_trust")
        facts = _rows(finding.get("evidence_facts"), f"{ref}.evidence_facts")
        _require(facts, f"{ref} lacks source evidence facts")
        for fact in facts:
            support_id = fact.get("support_id")
            _require(support_id is None or support_id in finding["support_ids"],
                     f"{ref} evidence fact cites unknown support")
            _require(fact.get("function") in {"carrier", "grammar", "trigger", "lexical_source", "boundary"}
                     and _text(fact.get("fact")), f"{ref} has a malformed evidence fact")
            reading.resolve(packet, fact.get("source_pointer"))
            if support_id is not None:
                prefixes = (indexes["support_registry"][support_id],
                            "/support_registry/" + reading.escape(support_id))
                _require(any(fact["source_pointer"] == p or fact["source_pointer"].startswith(p + "/")
                             for p in prefixes),
                         f"{ref} evidence fact points outside its named support")
        used_contexts: set[str] = set()
        for activation in _rows(finding.get("branch_activations"), f"{ref}.branch_activations"):
            branch_ref = activation.get("branch_ref")
            _require(branch_ref in branches, f"{ref} cites unknown branch {branch_ref}")
            branch = branches[branch_ref]
            _require(activation.get("branch_gloss") == branch.get("gloss"),
                     f"{ref} changed a source branch gloss")
            facets = {r["facet_id"]: r for r in branch.get("review_facets", [])}
            facet_id = activation.get("facet_id")
            if facet_id is None:
                _require(not facets and activation.get("facet_statement") is None,
                         f"{ref} omitted an available facet identity")
            else:
                _require(facet_id in facets, f"{ref} cites unknown facet {branch_ref}/{facet_id}")
                _require(activation.get("facet_statement") in facets[facet_id].get("statements", {}).values(),
                         f"{ref} changed a source facet statement")
            _require(activation.get("application_mode") in {"lexical", "intrinsic_cross_root",
                     "contextual_resonance", "analogical", "attributed"}, f"{ref} has invalid application mode")
            for key in ("carrier", "independent_trigger", "activation", "resulting_reading", "boundary"):
                _require(_text(activation.get(key)), f"{ref} activation lacks {key}")
            for key in ("carrier_refs", "trigger_refs"):
                refs = _strings(activation.get(key), f"{ref}.{key}")
                _require(refs and set(refs) <= known, f"{ref} has missing or unknown {key}")
                for source_ref in refs:
                    match = re.match(r"^(\d+:\d+)(?::|$)", source_ref)
                    if match:
                        # A prefatory unit keeps its host identity even when
                        # morphology uses a separately supplied linguistic alias.
                        if match[1] in contexts:
                            owners = {match[1]}
                        else:
                            owners = {u["ayah_ref"] for u in packet.get("context_evidence", [])
                                      if match[1] == u.get("linguistic_source_ref")}
                            # The host reference disambiguates shared basmala
                            # morphology; citing one alias does not use all hosts.
                            owners &= set(finding["context_refs"])
                        if match[1] not in focus_ayahs:
                            _require(owners, f"{ref} must identify the context owner of {source_ref}")
                        used_contexts.update(owners)
            returns = _strings(activation.get("focus_return_refs"), f"{ref}.focus_return_refs")
            _require(returns and set(returns) <= focus_refs,
                     f"{ref} must return through actual focus word/morpheme refs")
        _require(used_contexts <= set(finding["context_refs"]), f"{ref} omits a used context ayah")
        landed_contexts[ref] = used_contexts

    decisions = {}
    for decision in _rows(result["candidate_decisions"], "candidate_decisions"):
        cid = decision.get("candidate_id")
        _require(cid in candidates and cid not in decisions, f"Unknown or repeated candidate decision: {cid}")
        decisions[cid] = decision
        kind = decision.get("decision")
        _require(kind in DECISIONS and _text(decision.get("reason")), f"{cid} has invalid decision/reason")
        refs = _strings(decision.get("finding_refs"), f"{cid}.finding_refs")
        _require(set(refs) <= findings.keys(), f"{cid} cites unknown findings")
        if kind in {"accept", "narrow"}:
            _require(refs and all(findings[r].get("origin_candidate_id") == cid for r in refs),
                     f"{cid} requires its own retained finding")
        elif kind == "represented":
            _require(len(refs) == 1 and cid in findings[refs[0]]["represented_candidate_ids"],
                     f"{cid} lacks its exact-duplicate finding link")
        else:
            _require(not refs, f"Rejected candidate {cid} still owns findings")
        candidate = candidates[cid]
        expected = {
            "branch_exclusions": set(candidate.get("branch_refs", [])),
            "context_exclusions": set(candidate.get("required_context_refs", [])),
            "semantic_obligation_exclusions": {r["obligation_ref"] for r in candidate.get("semantic_obligations", [])},
        }
        retained = {
            "branch_exclusions": {a["branch_ref"] for r in refs for a in findings[r]["branch_activations"]},
            "context_exclusions": {r for f in refs for r in landed_contexts[f]},
            "semantic_obligation_exclusions": {r for f in refs for r in findings[f]["semantic_obligation_refs"]},
        }
        for key, identity in EXCLUSIONS.items():
            excluded = _rows(decision.get(key), f"{cid}.{key}")
            ids = [r.get(identity) for r in excluded]
            _require(all(_text(i) for i in ids) and len(ids) == len(set(ids))
                     and all(_text(r.get("reason")) for r in excluded), f"{cid} has invalid {key}")
            _require(set(ids) <= expected[key] and not (set(ids) & retained[key]),
                     f"{cid} has unknown or contradictory {key}")
            _require(expected[key] <= retained[key] | set(ids), f"{cid} silently drops {key}")
            if kind in {"accept", "represented"}:
                _require(not ids, f"{cid} cannot exclude evidence with decision {kind}")
        facet_rows = _rows(decision.get("facet_exclusions"), f"{cid}.facet_exclusions")
        excluded_facets = {(r.get("branch_ref"), r.get("facet_id")) for r in facet_rows}
        _require(len(excluded_facets) == len(facet_rows) and all(_text(r.get("reason")) for r in facet_rows),
                 f"{cid} has invalid facet exclusions")
        required_facets = {(r["branch_ref"], r["facet_id"]) for r in candidate.get("required_branch_facets", [])}
        available_facets = {(b, f["facet_id"]) for b in candidate.get("branch_refs", [])
                            for f in branches[b].get("review_facets", [])}
        available_facets.update((b, None) for b in candidate.get("branch_refs", [])
                                if not branches[b].get("review_facets"))
        _require(excluded_facets <= available_facets | required_facets,
                 f"{cid} excludes unknown or unattached facets")
        landed_facets = {(a["branch_ref"], a.get("facet_id")) for f in refs for a in findings[f]["branch_activations"]}
        _require(required_facets <= landed_facets | excluded_facets, f"{cid} silently drops required facets")
        _require(not (excluded_facets & landed_facets), f"{cid} both retains and excludes a facet")
        _require(kind not in {"accept", "represented"} or not excluded_facets,
                 f"{cid} cannot exclude facets with decision {kind}")
        if kind == "narrow" and expected["semantic_obligation_exclusions"]:
            _require(expected["semantic_obligation_exclusions"] & retained["semantic_obligation_exclusions"],
                     f"{cid} narrows away every semantic obligation")
    _require(set(decisions) == set(candidates), "Not every supplied candidate has exactly one decision")
    for ref, finding in findings.items():
        cid = finding.get("origin_candidate_id")
        if cid is not None:
            _require(ref in decisions[cid]["finding_refs"] and decisions[cid]["decision"] in {"accept", "narrow"},
                     f"{ref} is orphaned from its candidate decision")
        for represented in finding["represented_candidate_ids"]:
            _require(decisions[represented]["decision"] == "represented"
                     and decisions[represented]["finding_refs"] == [ref], f"{ref} has an orphaned duplicate link")


class Session:
    def __init__(self, plan_path: Path, *, raw_root: Path = RAW_ROOT):
        self.plan_path = plan_path
        self.plan, self.packet = reading.load_plan(plan_path)
        self.plan_hash = reading.digest(self.plan)
        self.raw_root = raw_root
        analysis_id, ref, lane = (self.plan[k] for k in ("analysis_id", "ayah_ref", "lane"))
        _require(re.fullmatch(r"[a-z0-9](?:[a-z0-9._-]{0,79})", analysis_id), "Invalid analysis ID")
        _require(re.fullmatch(r"[1-9][0-9]*:(?:0|[1-9][0-9]*)", ref), "Invalid focus ref")
        surah, ayah = map(int, ref.split(":"))
        folder = raw_root / analysis_id / f"s{surah:03d}" / f"{surah}_{ayah}"
        self.work_path = folder / f"{lane}.work.json"
        self.output_path = folder / f"{lane}.discovery.json"
        self.batches = {b["batch_id"]: b for b in self.plan["batches"]}

    def empty_work(self) -> dict[str, Any]:
        return {"schema_version": WORK_SCHEMA, "plan_sha256": self.plan_hash,
                "read_pages": {}, "completed_batches": [], "catalog_pages": {},
                "notes": [], "leads": [], "cross_batch_review": "",
                "discovery": {"schema_version": DISCOVERY_SCHEMA,
                              "ayah_ref": self.plan["ayah_ref"], "lane": self.plan["lane"],
                              "coverage_complete": False, "candidate_decisions": [],
                              "findings": [], "friction_notes": []}}

    def load_work(self) -> dict[str, Any]:
        _require(self.work_path.is_file() and not self.work_path.is_symlink(), "Run init before discovery")
        try:
            work = json.loads(self.work_path.read_bytes())
        except (OSError, ValueError) as exc:
            raise DiscoveryError(f"Cannot load checkpoint: {exc}") from exc
        _require(isinstance(work, dict) and work.get("schema_version") == WORK_SCHEMA
                 and work.get("plan_sha256") == self.plan_hash,
                 "Checkpoint belongs to different evidence/instructions; use a fresh analysis ID")
        _require(isinstance(work.get("read_pages"), dict) and isinstance(work.get("catalog_pages"), dict),
                 "Checkpoint delivery records are malformed")
        for field, allowed in (("read_pages", set(self.batches)),
                               ("catalog_pages", {"branches", "connections"})):
            _require(set(work[field]) <= allowed, f"Checkpoint has unknown {field} keys")
            for numbers in work[field].values():
                _require(isinstance(numbers, list) and
                         all(type(n) is int and n > 0 for n in numbers) and
                         len(numbers) == len(set(numbers)), f"Checkpoint has invalid {field} numbers")
        done = _strings(work.get("completed_batches"), "completed_batches")
        _require(done == list(self.batches)[:len(done)], "Completed batches must follow the reading plan order")
        _rows(work.get("notes"), "notes")
        _rows(work.get("leads"), "leads")
        _require(isinstance(work.get("discovery"), dict), "Checkpoint lacks discovery")
        for field in ("candidate_decisions", "findings"):
            _rows(work["discovery"].get(field), field)
        return work

    def save(self, work: dict[str, Any]) -> None:
        _atomic(self.work_path, work, self.raw_root)

    def init(self) -> dict[str, Any]:
        if self.work_path.exists():
            self.load_work()
        else:
            _require(not self.output_path.exists(), "A final discovery already exists; use a fresh analysis ID")
            self.save(self.empty_work())
        return self.status()

    def checkpoint(self, update: dict[str, Any]) -> dict[str, Any]:
        """Save literal judgments; never select or generate analytical content."""
        _require(not self.output_path.exists() and not self.output_path.is_symlink(),
                 "Discovery is finalized; use a fresh analysis ID")
        allowed = {"notes", "leads", "findings", "candidate_decisions", "remove_finding_refs",
                   "cross_batch_review", "coverage_complete", "friction_notes"}
        _require(isinstance(update, dict) and update and set(update) <= allowed,
                 "Checkpoint accepts only analytical update fields")
        work = self.load_work()
        for note in _rows(update.get("notes", []), "notes"):
            if note not in work["notes"]:
                work["notes"].append(note)
        for field, identity in (("leads", "lead_id"), ("findings", "finding_ref"),
                                ("candidate_decisions", "candidate_id")):
            incoming = _rows(update.get(field, []), field)
            _strings([row.get(identity) for row in incoming], f"{field}.{identity}")
            owner = work if field == "leads" else work["discovery"]
            positions = {row[identity]: i for i, row in enumerate(owner[field])}
            for row in incoming:
                if row[identity] in positions:
                    owner[field][positions[row[identity]]] = row
                else:
                    owner[field].append(row)
        removed = set(_strings(update.get("remove_finding_refs", []), "remove_finding_refs"))
        _require(not removed.intersection(row["finding_ref"] for row in update.get("findings", [])),
                 "Cannot update and remove the same finding")
        if removed:
            _require(removed <= {row["finding_ref"] for row in work["discovery"]["findings"]},
                     "Cannot remove an unknown finding")
            work["discovery"]["findings"] = [row for row in work["discovery"]["findings"]
                                             if row["finding_ref"] not in removed]
        if "cross_batch_review" in update:
            _require(_text(update["cross_batch_review"]), "Cross-batch review must be nonempty text")
            work["cross_batch_review"] = update["cross_batch_review"]
        if "coverage_complete" in update:
            _require(type(update["coverage_complete"]) is bool, "coverage_complete must be boolean")
            work["discovery"]["coverage_complete"] = update["coverage_complete"]
        if "friction_notes" in update:
            work["discovery"]["friction_notes"] = _strings(update["friction_notes"], "friction_notes")
        self._check_notes(work)
        self._check_leads(work, final=False)
        self.save(work)
        return self.status()

    def state(self, kind: str, pointer: str | None, page: int) -> dict[str, Any]:
        """Read exact analytical state in bounded pages, without recording delivery."""
        _require(kind in {"work", "discovery"}, "Unknown state kind")
        work = self.load_work()
        value = work
        if kind == "discovery":
            _require(self.output_path.is_file(), "Finish discovery before reading its final state")
            self._check_existing_output(work["discovery"])
            value = work["discovery"]
        pointers = [pointer] if pointer is not None else ["/" + reading.escape(k) for k in sorted(value)]
        output = reading.pages(value, pointers, label=f"state:{kind}",
                               packet_sha256=self.plan["packet_sha256"],
                               read_bytes=reading.READ_BYTES - 512)
        _require(1 <= page <= len(output), f"Page must be in 1..{len(output)}")
        result = output[page - 1]
        result["state_sha256"] = reading.digest(value)
        for row in result["records"]:
            row["state_pointer"] = row.pop("source_pointer")
        return result

    def batch_pages(self, batch_id: str) -> list[dict[str, Any]]:
        _require(batch_id in self.batches, f"Unknown batch: {batch_id}")
        return reading.batch_pages(self.packet, self.plan, self.batches[batch_id])

    def catalog(self, kind: str) -> dict[str, Any]:
        _require(kind in {"branches", "connections"}, "Unknown catalog")
        fields = (("branch_ref", "root_ar", "gloss", "boundary", "review_facets")
                  if kind == "branches" else ("connection_ref", "target_ref", "note", "reciprocal_evidence"))
        registry = "branch_registry" if kind == "branches" else "connection_registry"
        return {"records": [{"packet_pointer": f"/{registry}/{i}",
                             **{k: row[k] for k in fields if k in row}}
                            for i, row in enumerate(self.packet.get(registry, []))]}

    def catalog_view(self, kind: str) -> list[dict[str, Any]]:
        output = reading.pages(self.catalog(kind), ["/records"], label=f"catalog:{kind}",
                               packet_sha256=self.plan["packet_sha256"])
        for page in output:
            for row in page["records"]:
                row["catalog_pointer"] = row.pop("source_pointer")
        return output

    def status(self) -> dict[str, Any]:
        work = self.load_work()
        pending = [b for b in self.batches if b not in work["completed_batches"]]
        next_id = pending[0] if pending else None
        next_pages = len(self.batch_pages(next_id)) if next_id else 0
        return {"plan_sha256": self.plan_hash, "work_file": str(self.work_path),
                "final_discovery": str(self.output_path),
                "completed_batches": len(work["completed_batches"]), "total_batches": len(self.batches),
                "next_batch": next_id, "next_batch_pages": next_pages,
                "next_unread_pages": [n for n in range(1, next_pages + 1)
                                      if n not in work["read_pages"].get(next_id, [])],
                "candidate_decisions": len(work.get("discovery", {}).get("candidate_decisions", [])),
                "findings": len(work.get("discovery", {}).get("findings", [])),
                "open_lead_ids": [r.get("lead_id") for r in work.get("leads", []) if r.get("status") == "open"],
                "catalog_pages_after_batches": work["catalog_pages"],
                "next_step": "review_batch" if pending else "cross_batch_review_then_finish"}

    def read(self, batch_id: str | None, catalog: str | None, page: int) -> dict[str, Any]:
        work = self.load_work()
        pending = [bid for bid in self.batches if bid not in work["completed_batches"]]
        next_id = pending[0] if pending else None
        if batch_id:
            _require(batch_id in self.batches, f"Unknown batch: {batch_id}")
            _require(batch_id in work["completed_batches"] or batch_id == next_id,
                     f"Checkpoint and complete {next_id} before reading a later batch; "
                     "use lookup for a specific cross-batch lead")
        else:
            _require(not pending, "Complete the reading batches before reviewing the catalogs")
        output = self.batch_pages(batch_id) if batch_id else self.catalog_view(catalog)
        _require(1 <= page <= len(output), f"Page must be in 1..{len(output)}")
        if batch_id:
            delivered = work["read_pages"].setdefault(batch_id, [])
        else:
            delivered = work["catalog_pages"].setdefault(catalog, [])
        if page not in delivered:
            delivered.append(page)
            delivered.sort()
            self.save(work)
        return output[page - 1]

    def complete(self, batch_id: str) -> dict[str, Any]:
        work = self.load_work()
        _require(batch_id in self.batches, f"Unknown batch: {batch_id}")
        pending = [bid for bid in self.batches if bid not in work["completed_batches"]]
        _require(batch_id in work["completed_batches"] or batch_id == pending[0],
                 "Complete the current batch before advancing")
        count = len(self.batch_pages(batch_id))
        _require(set(work["read_pages"].get(batch_id, [])) == set(range(1, count + 1)),
                 "The reader has not delivered every page of this batch")
        self._check_notes(work)
        self._check_leads(work, final=False)
        self._check_batch_note(work, batch_id)
        if batch_id not in work["completed_batches"]:
            work["completed_batches"].append(batch_id)
            work["catalog_pages"] = {}
            work["cross_batch_review"] = ""
            self.save(work)
        return self.status()

    def _check_notes(self, work: dict[str, Any]) -> None:
        for note in _rows(work.get("notes"), "notes"):
            _require(_text(note.get("note")), "A checkpoint note lacks its observation")
            if "batch_id" in note:
                _require(note["batch_id"] in self.batches, "A note cites an unknown batch")
            pointers = _strings(note.get("source_pointers"), "note.source_pointers")
            _require(pointers, "A checkpoint note needs source pointers")
            for pointer in pointers:
                reading.resolve(self.packet, pointer)

    def _check_batch_note(self, work: dict[str, Any], batch_id: str) -> None:
        indexes = reading.registry_maps(self.packet)
        for note in work["notes"]:
            if note.get("batch_id") != batch_id:
                continue
            for pointer in note["source_pointers"]:
                # Treat emitted numeric pointers and equivalent evidence-ID
                # pointers alike when checking a note's batch membership.
                parts = pointer.split("/")
                if len(parts) >= 3 and parts[1] in indexes:
                    identity = parts[2].replace("~1", "/").replace("~0", "~")
                    if identity in indexes[parts[1]]:
                        pointer = indexes[parts[1]][identity] + "/".join([""] + parts[3:])
                if any(pointer == owner or pointer.startswith(owner + "/")
                       for owner in self.batches[batch_id]["pointers"]):
                    return
        raise DiscoveryError(f"Save a notes entry with batch_id={batch_id}, a concise review, "
                             "and a source pointer from this batch before completing it")

    def _check_leads(self, work: dict[str, Any], *, final: bool) -> None:
        lead_ids = set()
        for lead in _rows(work.get("leads"), "leads"):
            lid = lead.get("lead_id")
            _require(_text(lid) and lid not in lead_ids, "Leads need unique IDs")
            lead_ids.add(lid)
            _require(_text(lead.get("note")), f"Lead {lid} lacks its observation")
            pointers = _strings(lead.get("source_pointers"), f"{lid}.source_pointers")
            _require(pointers, f"Lead {lid} needs source pointers")
            for pointer in pointers:
                reading.resolve(self.packet, pointer)
            _require(lead.get("status") in {"open", "landed", "closed", "unresolved"},
                     f"Lead {lid} has an invalid status")
            if not final:
                continue
            _require(lead["status"] != "open" and _text(lead.get("resolution")),
                     f"Lead {lid} still needs an explicit disposition")
            if lead["status"] == "unresolved":
                _require(lead["resolution"] in work["discovery"].get("friction_notes", []),
                         f"Unresolved lead {lid} must remain in friction_notes")
            if lead["status"] == "landed":
                findings = {r["finding_ref"] for r in work["discovery"].get("findings", [])}
                refs = _strings(lead.get("finding_refs"), f"{lid}.finding_refs")
                _require(refs and set(refs) <= findings, f"Lead {lid} lacks its retained findings")

    def lookup(self, pointer: str, page: int) -> dict[str, Any]:
        output = reading.pages(self.packet, [pointer], label="source_lookup",
                               packet_sha256=self.plan["packet_sha256"])
        _require(1 <= page <= len(output), f"Page must be in 1..{len(output)}")
        return output[page - 1]

    def check(self) -> dict[str, Any]:
        work = self.load_work()
        checked = self._check_work(work)
        if self.output_path.exists():
            self._check_existing_output(work["discovery"])
        return checked

    def _check_existing_output(self, result: dict[str, Any]) -> None:
        _require(not self.output_path.is_symlink()
                 and json.loads(self.output_path.read_bytes()) == result,
                 "A different final discovery exists; refusing to overwrite agent output")

    def _check_work(self, work: dict[str, Any]) -> dict[str, Any]:
        _require(set(work["completed_batches"]) == set(self.batches), "Discovery has unfinished reading batches")
        for bid in self.batches:
            count = len(self.batch_pages(bid))
            _require(set(work["read_pages"].get(bid, [])) == set(range(1, count + 1)),
                     f"Batch {bid} has incomplete delivery accounting")
        for catalog in ("branches", "connections"):
            count = len(self.catalog_view(catalog))
            _require(set(work["catalog_pages"].get(catalog, [])) == set(range(1, count + 1)),
                     f"Cross-batch review has not read the complete {catalog} catalog")
        _require(_text(work.get("cross_batch_review")), "Explain the cross-batch review before finishing")
        self._check_notes(work)
        for bid in self.batches:
            self._check_batch_note(work, bid)
        self._check_leads(work, final=True)
        result = work.get("discovery")
        _require(isinstance(result, dict), "Checkpoint lacks discovery")
        validate_discovery(self.packet, result)
        return {"status": "checked", "plan_sha256": self.plan_hash,
                "completed_batches": len(self.batches),
                "candidates": len(result["candidate_decisions"]), "findings": len(result["findings"])}

    def finish(self) -> dict[str, Any]:
        work = self.load_work()
        checked = self._check_work(work)
        result = work["discovery"]
        if self.output_path.exists():
            self._check_existing_output(result)
        else:
            _atomic(self.output_path, result, self.raw_root, replace=False)
        return {**checked, "status": "finalized", "discovery_file": str(self.output_path)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("init", "status", "check", "finish"):
        commands.add_parser(name)
    commands.add_parser("checkpoint", help="Save literal analytical updates from JSON on stdin")
    state = commands.add_parser("state", help="Read bounded checkpoint or final-discovery pages")
    state.add_argument("--kind", choices=("work", "discovery"), default="work")
    state.add_argument("--pointer")
    state.add_argument("--page", type=int, default=1)
    read = commands.add_parser("read")
    selector = read.add_mutually_exclusive_group(required=True)
    selector.add_argument("--batch")
    selector.add_argument("--catalog", choices=("branches", "connections"))
    read.add_argument("--page", type=int, default=1)
    complete = commands.add_parser("complete")
    complete.add_argument("--batch", required=True)
    lookup = commands.add_parser("lookup")
    lookup.add_argument("--pointer", required=True)
    lookup.add_argument("--page", type=int, default=1)
    args = parser.parse_args(argv)
    try:
        session = Session(args.plan)
        if args.command == "read":
            result = session.read(args.batch, args.catalog, args.page)
        elif args.command == "complete":
            result = session.complete(args.batch)
        elif args.command == "lookup":
            result = session.lookup(args.pointer, args.page)
        elif args.command == "checkpoint":
            result = session.checkpoint(json.load(sys.stdin))
        elif args.command == "state":
            result = session.state(args.kind, args.pointer, args.page)
        else:
            result = getattr(session, args.command)()
        print(reading.encode(result).decode("utf-8"))
        return 0
    except (DiscoveryError, reading.ReadingError, OSError, ValueError, TypeError, KeyError) as exc:
        print(f"V6 discovery: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
