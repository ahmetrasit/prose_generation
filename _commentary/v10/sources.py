"""Read canonical evidence; preserve occurrence identity separately from resonance."""
from __future__ import annotations

import gzip
import hashlib
import json
import math
import re
import shutil
import sqlite3
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DATA = REPO.parent / "quran-data" / "data"
REF_RE = re.compile(r"(?<![\d:])(\d{1,3}):(\d{1,3})(?![\d:])")
BRANCH_RE = re.compile(r"(?:quranic:)?(root_\d+)[/:](B\d+)(?:/m\d+)?")
AR_BRANCH_RE = re.compile(r"([\u0621-\u064a](?:\s+[\u0621-\u064a]){1,4}):(B\d+)(?:/m\d+)?")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def norm_ar(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).replace("ـ", "").replace("ٱ", "ا")
    return " ".join("".join(c for c in text if unicodedata.category(c) != "Mn").split())


def ref_key(ref: str) -> tuple[int, int]:
    return tuple(map(int, ref.split(":")))


def references(text: str) -> list[str]:
    """Expand written ayah ranges as well as single anchors, without crossing surahs."""
    refs = {f"{int(s)}:{int(a)}" for s, a in REF_RE.findall(text)}
    for s, a, other_s, b in re.findall(r"\b(\d{1,3}):(\d{1,3})\s*[-–]\s*(?:(\d{1,3}):)?(\d{1,3})\b", text):
        if (not other_s or other_s == s) and int(a) <= int(b) <= 286:
            refs.update(f"{int(s)}:{n}" for n in range(int(a), int(b) + 1))
    return sorted(refs, key=ref_key)


class Sources:
    def __init__(self, data: Path = DATA, cache: Path | None = None):
        self.data = data.resolve()
        self.cache = cache or Path(__file__).parent / ".cache"
        self.manifest: dict[str, dict] = {}
        self._file_manifest: dict[str, dict] = {}
        self._entries: dict[str, dict] = {}
        self._words: dict[str, list[dict]] = {}
        self._analysis: dict[int, dict] = {}
        self.inventory: dict[str, dict] = {}
        self.root_labels: dict[str, set[str]] = {}
        self.labels_to_roots: dict[str, set[str]] = {}
        self.texts = {}
        for line in self.read(self.data / "text/quran-uthmani.tsv").decode("utf-8-sig").splitlines():
            ref, text = line.split("|", 1)
            if ref_key(ref)[1] > 0:
                self.texts[ref] = text
        self.gateway = {r["qacRootJoinKey"]: r for r in self.json(self.data / "bridges/qac-dictionary-root-resolutions.json")["roots"]}
        self.alternatives = self.json(self.data / "bridges/qac-dictionary-word-root-analyses.json")["records"]
        self.qac = self.database(self.data / "morphology/qac.sqlite.gz")
        self.rootmap = self.database(self.data / "bridges/qac-furuq-v4-root-map.sqlite.gz")
        self._base_manifest = self.manifest.copy()

    def begin_scope(self) -> None:
        self.manifest = self._base_manifest.copy()
        self.inventory.clear()
        self.root_labels.clear()
        self.labels_to_roots.clear()

    def read(self, path: Path) -> bytes:
        raw = path.read_bytes()
        self.manifest[str(path.resolve())] = {"sha256": digest(raw), "bytes": len(raw)}
        self._file_manifest[str(path.resolve())] = self.manifest[str(path.resolve())]
        return raw

    def json(self, path: Path) -> dict:
        return json.loads(self.read(path))

    def database(self, path: Path) -> sqlite3.Connection:
        raw = self.read(path)
        self.cache.mkdir(parents=True, exist_ok=True)
        target = self.cache / f"{path.stem}-{digest(raw)}.sqlite"
        if not target.exists():
            # Unique temporary files make simultaneous preparations safe.
            import tempfile
            with tempfile.NamedTemporaryFile(dir=self.cache, delete=False) as tmp:
                name = Path(tmp.name)
                with gzip.open(path, "rb") as source:
                    shutil.copyfileobj(source, tmp)
            name.replace(target)
        db = sqlite3.connect(f"{target.as_uri()}?mode=ro&immutable=1", uri=True)
        db.row_factory = sqlite3.Row
        return db

    def close(self) -> None:
        self.qac.close()
        self.rootmap.close()

    def word_analysis(self, ref: str) -> dict:
        s, _ = ref_key(ref)
        path = self.data / f"analysis/word-analysis/s{s:03d}.jsonl.zst"
        if not path.exists():
            return {}
        if s not in self._analysis:
            from compression import zstd  # Python 3.14; no third-party dependencies.
            raw = self.read(path)
            self._analysis[s] = {row["ref"]: row for row in
                                 (json.loads(line) for line in zstd.decompress(raw).decode().splitlines() if line.strip())}
        else:
            self.manifest[str(path.resolve())] = self._file_manifest[str(path.resolve())]
        return self._analysis[s].get(ref, {})

    def load_inventory(self, surah: int) -> None:
        path = self.data / f"analysis/ayah-activation/v12-tr/s{surah:03d}/full_context_packet.json"
        if not path.exists():
            return
        packet = self.json(path)
        for group in packet.get("branch_inventories", []):
            for branch in group.get("branches", []):
                for variant in branch.get("variants", []):
                    rid = variant["root_id"]
                    bid = f"{rid}/{branch['branch_id']}"
                    # A split inventory can describe different roots under one QAC label.
                    self.inventory.setdefault(bid, variant)
                    self.root_labels.setdefault(rid, set()).add(group["root"])
                    self.labels_to_roots.setdefault(norm_ar(group["root"]).replace(" ", ""), set()).add(rid)

    def entry(self, rid: str) -> dict:
        path = self.data / f"dictionary/tr/{rid}_entry.json"
        if rid not in self._entries:
            self._entries[rid] = self.json(path) if path.exists() else {}
        elif str(path.resolve()) in self._file_manifest:
            self.manifest[str(path.resolve())] = self._file_manifest[str(path.resolve())]
        return self._entries[rid]

    def branch(self, branch_ref: str, full: bool = True) -> dict:
        rid, _ = branch_ref.split("/")
        branch = next((b for b in self.entry(rid).get("branches", []) if b["branch_ref"] == branch_ref), {})
        inv = self.inventory.get(branch_ref, {})
        if not branch and not inv:
            raise ValueError(f"Unresolved branch: {branch_ref}")
        gloss = branch.get("concept_gloss", {})
        card = {
            "branch_ref": branch_ref,
            "inventory_qac_labels": sorted(self.root_labels.get(rid, [])),
            "image_ar": branch.get("branch_image_ar") or inv.get("image_ar", ""),
            "scope_ar": inv.get("scope_ar") or branch.get("what_is_ar", ""),
            "gloss_tr": gloss.get("text", "") if isinstance(gloss, dict) else gloss,
        }
        if full:
            card.update({
                "attestation_ar": branch.get("source_phrase_ar", ""),
                "sources": branch.get("sources", []),
                "source_details": branch.get("source_synthesis", {}).get("source_details", []),
                "definition_tr": branch.get("concept_map", {}).get("definition", ""),
                "lexicalization_scope": branch.get("lexicalization_scope", {}),
                "identity_judgment": branch.get("identity_judgment", {}),
                "source_status": "dictionary_entry" if branch else "inventory_only",
            })
        return card

    def words(self, ref: str) -> list[dict]:
        if ref in self._words:
            return self._words[ref]
        rows = self.qac.execute(
            "select qac_word_ref,word_index,surface_ar,root_join_keys,lemmas_ar,pos_tags "
            "from qac_words where surah=? and ayah=? order by word_index", ref_key(ref))
        words = []
        for row in rows:
            w = dict(row)
            w["root_join_keys"] = [r for r in w["root_join_keys"].split(";") if r]
            w["lemmas_ar"] = [r for r in w["lemmas_ar"].split(";") if r]
            w["morphemes"] = [dict(m) for m in self.qac.execute(
                "select qac_ref,surface_ar,root_join_key,lemma_ar,pos,morph_features "
                "from qac_morphemes where qac_word_ref=? order by morpheme_index", (w["qac_word_ref"],))]
            mappings = []
            for key in w["root_join_keys"]:
                gate = self.gateway.get(key, {})
                for rid in gate.get("rootIds", []):
                    mappings.append({"root_id": rid, "kind": "identity", "reason": gate.get("resolution", "")})
                for record in self.alternatives:
                    sel = record["selector"]
                    if sel.get("qacRootJoinKey") != key:
                        continue
                    if (sel.get("qacLemma") in w["lemmas_ar"] or
                            sel.get("qacRef") in {m["qac_ref"] for m in w["morphemes"]}):
                        for alt in record["analyses"]:
                            if alt.get("dictionaryRootId") and alt["standing"] != "primary":
                                mappings.append({"root_id": alt["dictionaryRootId"], "kind": "attributed_alternative",
                                                 "reason": alt.get("reasonTr", ""), "attribution": alt.get("attributionTr", "")})
                echoes = set(gate.get("withheldTargetIds", []))
                echoes.update(r[0] for r in self.rootmap.execute(
                    "select furuq_root_id from qac_furuq_targets where qac_root_join_key=? and is_dominant=0", (key,)))
                mapped = {r["root_id"] for r in mappings}
                mappings.extend({"root_id": r, "kind": "observed_echo_only", "reason": "Observed split mapping; not an etymology."}
                                for r in sorted(echoes - mapped))
            w["root_mappings"] = mappings
            words.append(w)
        self._words[ref] = words
        return words

    def resolve_step(self, step: dict) -> dict:
        """Never silently trust legacy word positions or turn a split mapping into identity."""
        words = self.words(step["source_ref"])
        key = norm_ar(step.get("root", "")).replace(" ", "")
        candidates = [w for w in words if key in w["root_join_keys"]]
        indexed = [w for w in candidates if str(w["word_index"]) in list(map(str, step.get("source_word_indices", [])))]
        chosen = indexed or candidates
        return {
            **step, "branch_ref": f"{step['mapped_root_id']}/{step['branch_id']}",
            "binding_status": "exact" if indexed else "root_matched_legacy_index_differs" if candidates else "unresolved",
            "occurrences": [{"ref": w["qac_word_ref"], "surface_ar": w["surface_ar"],
                             "mapping": next((r for r in w["root_mappings"] if r["root_id"] == step["mapped_root_id"]),
                                             {"root_id": step["mapped_root_id"], "kind": "unverified_mapping"})}
                            for w in chosen],
        }

    def branch_citations(self, text: str) -> tuple[list[str], list[str]]:
        ids = {f"{rid}/{bid}" for rid, bid in BRANCH_RE.findall(text)}
        unresolved = []
        for root, bid in AR_BRANCH_RE.findall(text):
            key = norm_ar(root).replace(" ", "")
            candidates = [f"{rid}/{bid}" for rid in self.labels_to_roots.get(key, set())
                          if f"{rid}/{bid}" in self.inventory]
            if candidates:
                ids.update(candidates)  # Preserve all split variants; do not pick a convenient root.
            else:
                unresolved.append(f"{root}:{bid}")
        return sorted(ids), sorted(set(unresolved))

    def passage(self, ref: str, radius: int = 2) -> list[str]:
        if ref not in self.texts:
            raise ValueError(f"Not a Quran ayah: {ref}")
        s, a = ref_key(ref)
        return [f"{s}:{n}" for n in range(max(1, a - radius), a + radius + 1) if f"{s}:{n}" in self.texts]

    def usage(self, words: list[dict]) -> list[dict]:
        result = []
        for key in sorted({k for w in words for k in w["root_join_keys"]}):
            groups = {}
            for row in self.qac.execute(
                "select surah,ayah,lemma_ar,qac_word_ref from qac_morphemes "
                "where root_join_key=? order by surah,ayah,word_index", (key,)):
                group = groups.setdefault(row["lemma_ar"], {"lemma_ar": row["lemma_ar"], "occurrences": set(), "refs": set()})
                group["occurrences"].add(row["qac_word_ref"])
                group["refs"].add(f"{row['surah']}:{row['ayah']}")
            result.append({"qac_root": key, "lemmas": [
                {"lemma_ar": v["lemma_ar"], "word_count": len(v["occurrences"]), "refs": sorted(v["refs"], key=ref_key)}
                for v in groups.values()]})
        return result

    def contrast_candidates(self, usage: list[dict], focus_ref: str, limit: int = 12) -> list[dict]:
        """Prefer informative co-occurrences; ubiquitous roots cannot retrieve alone."""
        by_ref: dict[str, set[str]] = {}
        dfs = {}
        for root in usage:
            refs = {r for lemma in root["lemmas"] for r in lemma["refs"]}
            dfs[root["qac_root"]] = len(refs)
            for ref in refs:
                by_ref.setdefault(ref, set()).add(root["qac_root"])
        candidates = []
        for ref, roots in by_ref.items():
            if ref == focus_ref or len(roots) < 2 or not any(dfs[k] <= 500 for k in roots):
                continue
            score = sum(math.log((len(self.texts) + 1) / (dfs[k] + 1)) for k in roots)
            candidates.append({"ref": ref, "shared_roots": sorted(roots), "retrieval_score": round(score, 4)})
        return sorted(candidates, key=lambda r: (-r["retrieval_score"], ref_key(r["ref"])))[:limit]
