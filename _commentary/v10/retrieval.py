"""Optional quran-slm candidate retrieval, never a semantic admission rule."""
from __future__ import annotations

import json
from pathlib import Path


def neighbours(focus_branches: set[str], inventory: set[str], directory: Path, k: int = 3) -> tuple[list[dict], dict]:
    import numpy as np

    net = directory / "artifacts/corpus_network"
    cat_path = net / "catalog.json"
    catalog = json.loads(cat_path.read_text())
    cards = catalog["cards"]
    n = len(cards)
    indices = {f"{c['source_root_id']}/{c['branch_id']}": c["global_index"]
               for c in cards if c["origin_corpus"] == "quranic"}
    paths = [(0.35, net / "e5_directional_rank.u16le"),
             (0.35, directory / "artifacts/corpus_ensemble/neoarabert_directional_rank.u16le"),
             (0.30, net / "character_directional_rank.u16le")]
    for _, path in paths:
        if path.stat().st_size != n * n * 2:
            raise ValueError(f"Rank matrix shape does not match catalog: {path}")
    ranks = [(weight, np.memmap(path, dtype="<u2", mode="r", shape=(n, n))) for weight, path in paths]
    pool = sorted(inventory & indices.keys())
    pool_ix = np.array([indices[b] for b in pool])
    results = []
    for branch in sorted(focus_branches & indices.keys()):
        i = indices[branch]
        scores = np.zeros(len(pool), dtype=np.float64)
        for weight, matrix in ranks:
            forward = np.asarray(matrix[i, pool_ix], dtype=np.float64)
            reverse = np.asarray(matrix[pool_ix, i], dtype=np.float64)
            valid = (forward > 0) & (reverse > 0)
            scores += weight * np.where(valid, 0.5 * (1 / (10 + forward) + 1 / (10 + reverse)), 0)
        order = sorted(range(len(pool)), key=lambda j: (-scores[j], pool[j]))
        # Distinct roots prevent a dense same-root family consuming the small retrieval budget.
        roots = {branch.split("/")[0]}
        selected = []
        for j in order:
            root = pool[j].split("/")[0]
            if scores[j] > 0 and root not in roots:
                selected.append({"branch_ref": pool[j], "affinity": round(float(scores[j]), 8)})
                roots.add(root)
            if len(selected) == k:
                break
        results.append({"focus_branch": branch, "candidates": selected})
    provenance = {"catalog": str(cat_path.resolve()), "branch_snapshot_sha256": catalog.get("branch_snapshot_sha256"),
                  "rank_catalog_sha256": catalog.get("rank_catalog_sha256"), "weights": [0.35, 0.35, 0.30],
                  "offset": 10, "k_per_focus_branch": k, "rank_files": [
                      {"path": str(p.resolve()), "bytes": p.stat().st_size, "mtime_ns": p.stat().st_mtime_ns} for _, p in paths],
                  "verification": "catalog provenance plus matrix size/mtime; rank contents not rehashed",
                  "meaning": "Retrieval affinity only; not relevance, evidence strength, contextual probability or a finding."}
    return results, provenance
