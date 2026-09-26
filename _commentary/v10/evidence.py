"""Prepare a reusable evidence library and hydrate whole selected readings."""
from __future__ import annotations

import json
import re
from pathlib import Path

from .sources import REPO, Sources, digest, ref_key, references

SCHEMA = "commentary-v10-evidence-1"


def dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def channel_readings(text: str, surah: int, src: Sources, focus: str) -> list[dict]:
    """Retain every subsection and its parent framing, including unparsed prose."""
    result = []
    for parent in re.split(r"(?m)(?=^### [^#])", text):
        if not parent.startswith("### "):
            continue
        parts = re.split(r"(?m)(?=^#### )", parent)
        frame = parts[0].strip()
        for section in parts[1:] or [frame]:
            branch_refs, unresolved = src.branch_citations(section)
            anchors = re.search(r"(?im)^[-*] (?:Ayah anchors|Âyet dayanakları):\s*(.*)", section)
            refs = references(anchors.group(1) if anchors else section)
            result.append({
                "id": f"C{surah:03d}-{len(result)+1:03d}", "kind": "reviewed_subnetwork",
                "source_status": "upstream interpretation; first-pass review, not a lexical fact",
                "title": section.splitlines()[0].lstrip("# "),
                "parent_frame": frame, "reading": section.strip(),
                "branch_refs": branch_refs, "unresolved_branch_labels": unresolved,
                "ayah_refs": refs, "focus_linked": focus in refs,
            })
    if text.strip() and not result:
        raise ValueError(f"Channel review format unrecognized for S{surah}; refusing silent loss")
    return result


def hydrate_refs(src: Sources, seeds: set[str], radius: int = 2) -> tuple[dict, dict]:
    passages = {ref: src.passage(ref, radius) for ref in sorted(seeds, key=ref_key)}
    refs = {r for values in passages.values() for r in values}
    return {r: src.texts[r] for r in sorted(refs, key=ref_key)}, passages


def occurrence_bindings(src: Sources, refs: set[str], branch_ids: set[str]) -> dict:
    roots = {bid.split("/")[0] for bid in branch_ids}
    result = {}
    for ref in sorted(refs & src.texts.keys(), key=ref_key):
        for word in src.words(ref):
            mappings = [m for m in word["root_mappings"] if m["root_id"] in roots]
            if mappings:
                result[word["qac_word_ref"]] = {"surface_ar": word["surface_ar"], "qac_roots": word["root_join_keys"],
                                               "mappings": mappings,
                                               "morphology": [m["morph_features"] for m in word["morphemes"]]}
    return result


def prepare(ref: str, src: Sources, bundles: Path = REPO / "bundles", rare_limit: int = 24,
            upstream: str = "auto", network_k: int = 3) -> dict:
    src.begin_scope()
    if ref not in src.texts:
        raise ValueError(f"Unsupported focus: {ref}; v10 pilot supports numbered ayat")
    surah, _ = ref_key(ref)
    bundle_path = bundles / f"s{surah:03d}" / f"{ref.replace(':', '_')}.ayah.json"
    if not bundle_path.exists():
        candidates = sorted(bundles.glob(f"s{surah:03d}-pericopes/*/{ref.replace(':', '_')}.ayah.json"))
        if len(candidates) > 1:
            raise ValueError(f"Need one unambiguous bundle for {ref}; found {len(candidates)} pericope copies")
        if candidates:
            bundle_path = candidates[0]
    bundle = src.json(bundle_path) if bundle_path.exists() else {}
    if upstream == "auto" and not bundle.get("v12_focus_trace_hermetic", {}).get("readers"):
        base = REPO.parent / "latent_activation/focus_trace/runs"
        runs = sorted({base / f"s{surah:03d}", base / f"s{surah}"})
        populated = [list(p.glob(f"readers/*/{ref.replace(':', '_')}.focus_trace.json")) for p in runs]
        populated = [files for files in populated if files]
        if len(populated) > 1:
            raise ValueError(f"Ambiguous padded/unpadded HFT runs for {ref}")
        if populated:
            bundle["v12_focus_trace_hermetic"] = {"readers": {p.parent.name: src.json(p) for p in populated[0]}}
    if not bundle.get("word_analysis"):
        bundle["word_analysis"] = src.word_analysis(ref)
    if not bundle.get("inter_ayah_rows"):
        inter_path = src.data / f"analysis/inter-ayah/reciprocal/focus_{ref.replace(':', '_')}_cutoff_100.tsv"
        if inter_path.exists():
            bundle["inter_ayah_rows"] = [dict(zip(("label", "ref", "note"), line.split("\t", 2)))
                                         for line in src.read(inter_path).decode().splitlines() if line.strip()]
    src.load_inventory(surah)
    if surah != 1:
        src.load_inventory(1)
    warnings = []
    chains = []
    hft = bundle.get("v12_focus_trace_hermetic", {}).get("readers", {}) if upstream == "auto" else {}
    for reader, readings in hft.items():
        for kind in ("baseline_models", "context_deltas", "surprising_valid_outliers"):
            for original in readings.get(kind, []):
                steps = [src.resolve_step(s) for s in original.get("activation_trace", [])]
                chains.append({
                    "id": f"H{len(chains)+1:03d}", "kind": "hft", "reader": reader, "category": kind,
                    "source_status": "upstream interpretation; preserve its roles and qualifications",
                    "reading": original, "resolved_steps": steps,
                    "branch_refs": sorted({s["branch_ref"] for s in steps}),
                    "ayah_refs": sorted({s["source_ref"] for s in steps}, key=ref_key), "focus_linked": True,
                })
    if not chains:
        warnings.append("No bundled HFT records; discovery must use channels, usage and lexical evidence.")
    for s in sorted({surah, 1}) if upstream != "none" else []:
        path = src.data / f"analysis/channels/network-v3/s{s:03d}/review/reader_a_pilot.md"
        if path.exists():
            chains.extend(channel_readings(src.read(path).decode("utf-8"), s, src, ref))
        else:
            warnings.append(f"No reviewed subnetwork source for S{s}.")
    for kind in (("v12_reader_walks", "v12_reader_walks_wide") if upstream != "none" else []):
        for reader, payload in bundle.get(kind, {}).items():
            # Keep complete walks. They are independent interpretations, not confirmations by vote.
            text = "\n\n".join(v for v in payload.values() if isinstance(v, str))
            if text.strip():
                bids, unresolved = src.branch_citations(text)
                chains.append({"id": f"W-{kind}-{reader}", "kind": "reader_walk", "reading": text,
                               "branch_refs": bids, "unresolved_branch_labels": unresolved,
                               "ayah_refs": references(text), "focus_linked": True})
    words = src.words(ref)
    focus_roots = {m["root_id"] for w in words for m in w["root_mappings"]}
    focus_branches = {b["branch_ref"] for rid in focus_roots for b in src.entry(rid).get("branches", [])}
    chain_branches = {b for c in chains for b in c["branch_refs"]}
    # The full surah catalog allows new compositions across reviewed subnetworks.
    # Exact source phrases are additionally supplied for focus roots and focus-linked readings.
    catalog_ids = set(src.inventory) | focus_branches | chain_branches
    catalog = {}
    for bid in sorted(catalog_ids):
        try:
            catalog[bid] = src.branch(bid, full=False)
        except ValueError as exc:
            warnings.append(str(exc))
    source_ids = focus_branches | {b for c in chains if c["focus_linked"] for b in c["branch_refs"]}
    lexical = {b: src.branch(b) for b in sorted(source_ids) if b in catalog}
    bound_refs = {ref} | {r for c in chains if c["focus_linked"] for r in c["ayah_refs"]}
    bindings = occurrence_bindings(src, bound_refs, source_ids)
    retrieval, retrieval_provenance = [], {}
    if network_k > 0:
        try:
            from .retrieval import neighbours
            retrieval, retrieval_provenance = neighbours(focus_branches, set(src.inventory), REPO.parent / "quran-slm", network_k)
        except (ImportError, FileNotFoundError) as exc:
            warnings.append(f"Network retrieval unavailable; full branch catalog exposed: {exc}")
    candidate_ids = {b["branch_ref"] for row in retrieval for b in row["candidates"]}
    visible_ids = focus_branches | chain_branches | candidate_ids if retrieval else set(catalog)
    usage = src.usage(words)
    contrasts = src.contrast_candidates(usage, ref)
    panels = []
    rare_refs = set()
    # Rare-root concordances expose Quranic loading across different derivatives,
    # e.g. حَمِئَة in 18:86 and حَمَإ in 15:26,28,33. Matching only lemmas misses this.
    for root in usage:
        all_refs = {r for lemma in root["lemmas"] for r in lemma["refs"]}
        if len(all_refs) <= rare_limit:
            panels.append({"qac_root": root["qac_root"], "scope": "all root occurrences",
                           "refs": sorted(all_refs, key=ref_key)})
            rare_refs.update(all_refs)
        else:
            focus_lemmas = {l for w in words if root["qac_root"] in w["root_join_keys"] for l in w["lemmas_ar"]}
            for lemma in root["lemmas"]:
                if lemma["lemma_ar"] in focus_lemmas and len(lemma["refs"]) <= rare_limit:
                    panels.append({"qac_root": root["qac_root"], "lemma_ar": lemma["lemma_ar"],
                                   "scope": "all occurrences of this lemma", "refs": lemma["refs"]})
                    rare_refs.update(lemma["refs"])
    inter = bundle.get("inter_ayah_rows", [])
    seeds = {ref} | rare_refs | {c["ref"] for c in contrasts}
    seeds.update(r["ref"] for r in inter if r.get("ref") in src.texts)
    seeds.update(r for c in chains for r in c["ayah_refs"] if r in src.texts)
    # Also retrieve references used by grammatical observations, not just inter-ayah rows.
    linguistic = [{k: w[k] for k in ("aligned_qac_word_ref", "surface_display", "root_display", "gloss_range", "prose") if k in w}
                  for w in bundle.get("word_analysis", {}).get("words", [])]
    seeds.update(r for r in references(json.dumps(linguistic, ensure_ascii=False)) if r in src.texts)
    texts, passages = hydrate_refs(src, seeds)
    for r, text in src.texts.items():
        if ref_key(r)[0] in {surah, 1}:
            texts[r] = text
    # Fixed-width neighbours are a retrieval seed, not a claim about passage boundaries.
    evidence = {
        "schema": SCHEMA, "focus_ref": ref,
        "focus": {"arabic": src.texts[ref], "words": words, "linguistic_observations": linguistic},
        "surah_refs": [r for r in src.texts if ref_key(r)[0] == surah],
        "fatiha_refs": [f"1:{a}" for a in range(1, 8)],
        "chains": chains, "branch_catalog": catalog, "lexical_evidence": lexical,
        "occurrence_bindings": bindings,
        "visible_branch_ids": sorted(visible_ids), "network_candidates": retrieval,
        "retrieval_provenance": retrieval_provenance,
        "quran_usage_index": usage, "quran_usage_panels": panels,
        "contrast_candidates": contrasts,
        "inter_ayah": inter, "ayah_texts": dict(sorted(texts.items(), key=lambda p: ref_key(p[0]))),
        "passages": passages, "warnings": warnings,
        "preparation": {"upstream": upstream, "hft_records": len([c for c in chains if c['kind'] == 'hft']),
                        "bundle_present": bundle_path.exists(), "rare_concordance_limit": rare_limit, "neighbour_radius": 2,
                        "limits_are": "retrieval seeds; request more context through the reading brief",
                        "branch_policy": "No frequency, hub-degree or literal-image admission threshold."},
        "source_manifest": src.manifest.copy(),
    }
    evidence["evidence_id"] = digest(json.dumps(evidence, ensure_ascii=False, sort_keys=True).encode())
    return evidence


def hydrate_brief(brief: str, evidence: dict, src: Sources) -> dict:
    """A plain reading brief cites originals; no coverage ledger or semantic gate."""
    header = re.match(r"Focus:\s*(\d+:\d+)\s*(?:\n|$)", brief)
    if not header or header.group(1) != evidence["focus_ref"]:
        raise ValueError(f"Brief must start with 'Focus: {evidence['focus_ref']}'")
    src.begin_scope()
    src.load_inventory(ref_key(evidence["focus_ref"])[0])
    src.load_inventory(1)
    selected = set(re.findall(r"\b(?:H\d{3}|C\d{3}-\d{3}|W-v12_[A-Za-z0-9_-]+)\b", brief))
    unknown = selected - {c["id"] for c in evidence["chains"]}
    if unknown:
        raise ValueError("Unknown source pointers: " + ", ".join(sorted(unknown)))
    chains = [c for c in evidence["chains"] if c["id"] in selected]
    branch_ids = {b for c in chains for b in c["branch_refs"]}
    branch_ids.update(re.findall(r"root_\d+/B\d+", brief))
    lexical = {bid: src.branch(bid) for bid in sorted(branch_ids)}
    seeds = {evidence["focus_ref"]}
    seeds.update(r for c in chains for r in c["ayah_refs"] if r in src.texts)
    seeds.update(references(brief))
    # Corpus-loading panels survive semantic reduction, even if the curator overlooked them.
    seeds.update(r for p in evidence["quran_usage_panels"] for r in p["refs"])
    texts, passages = hydrate_refs(src, seeds)
    for r in evidence["surah_refs"] + evidence["fatiha_refs"]:
        texts[r] = src.texts[r]
    bindings = occurrence_bindings(src, seeds, branch_ids)
    current_sources = src.manifest.copy()
    for path, old in evidence["source_manifest"].items():
        if path in current_sources and current_sources[path] != old:
            raise ValueError(f"Source changed after preparation: {path}")
    return {
        "schema": "commentary-v10-writer-packet-1", "evidence_id": evidence["evidence_id"],
        "focus_ref": evidence["focus_ref"], "focus": evidence["focus"], "reading_brief": brief,
        "chains": chains, "lexical_evidence": lexical,
        "occurrence_bindings": bindings,
        "surah_refs": evidence["surah_refs"], "fatiha_refs": evidence["fatiha_refs"],
        "quran_usage_panels": evidence["quran_usage_panels"],
        "ayah_texts": dict(sorted(texts.items(), key=lambda p: ref_key(p[0]))), "passages": passages,
        "source_manifest": {**evidence["source_manifest"], **current_sources},
        "warning": "The brief is a proposed reading, not an authority. Correct it from these original sources."
    }


def model_payload(evidence: dict) -> str:
    """Transport facts once; omit filesystem provenance and redundant passage membership."""
    omitted = {"source_manifest", "passages", "preparation", "evidence_id", "schema", "visible_branch_ids", "retrieval_provenance"}
    payload = {k: v for k, v in evidence.items() if k not in omitted}
    if "branch_catalog" in payload:
        payload["branch_catalog"] = {b: evidence["branch_catalog"][b] for b in evidence["visible_branch_ids"]
                                     if b in evidence["branch_catalog"] and b not in evidence["lexical_evidence"]}
    if "quran_usage_index" in payload:
        limit = evidence.get("preparation", {}).get("rare_concordance_limit", 24)
        payload["quran_usage_index"] = []
        for root in evidence["quran_usage_index"]:
            all_refs = {r for lemma in root["lemmas"] for r in lemma["refs"]}
            lemmas = []
            for lemma in root["lemmas"]:
                item = {"lemma_ar": lemma["lemma_ar"], "word_count": lemma["word_count"], "ayah_count": len(lemma["refs"])}
                if len(lemma["refs"]) <= limit:
                    item["refs"] = lemma["refs"]
                else:
                    item["retrieval"] = "Frequent: use supplied contrast/context passages; request a specific construction or ref if needed."
                lemmas.append(item)
            payload["quran_usage_index"].append({"qac_root": root["qac_root"], "ayah_count": len(all_refs), "lemmas": lemmas})
    if "inter_ayah" in payload:
        # Old relevance judgments are not evidence about what a passage can mean.
        # In the first 18:86 pilot, "no value" notes overruled the creation passages.
        payload["inter_ayah"] = {
            "candidate_refs": sorted({row["ref"] for row in evidence["inter_ayah"] if row.get("ref") in evidence["ayah_texts"]}, key=ref_key),
            "instruction": "These are retrieval candidates, not endorsed or rejected interpretations. Read their actual text and context independently."
        }
    payload["chains"] = []
    for source in evidence["chains"]:
        c = source.copy()
        if c["kind"] == "hft":
            c["reading"] = {k: v for k, v in c["reading"].items() if k != "activation_trace"}
        elif c["kind"] == "reviewed_subnetwork" and not c["focus_linked"]:
            # Keep the complete image/operation/synthesis; remove repeated parent framing.
            c.pop("parent_frame", None)
        payload["chains"].append(c)
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))


def stats(evidence: dict) -> dict:
    payload = model_payload(evidence)
    return {"focus_ref": evidence["focus_ref"], "payload_bytes": len(payload.encode()),
            "payload_characters": len(payload), "chains": len(evidence["chains"]),
            "lexical_sources": len(evidence["lexical_evidence"]), "ayat": len(evidence["ayah_texts"]),
            "note": "Bytes and characters are measured; token counts come only from actual provider usage."}
