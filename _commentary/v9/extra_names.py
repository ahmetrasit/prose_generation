"""Names for dictionary root ids that quran-slm's card list (corpus_branches_ar.tsv) does not name.

quran-data's newer entries carry only an id: the supplemental roots (root_9000xx; named by the gateway's `qacRoot`)
and the Furūq transfers (root_001959 ب ن و, root_005125 ه ي د, root_005296 و ل ه, root_005544 ح ي و; named only in the
dictionary repo's furuq root packets, `root_norm`). The reviewed word-root analyses also name their target roots
(`rootArabic` + `dictionaryRootId`). Used by V9 prepare.py (root_name), V11 verify_src.py (tags citing `و ل ه B004`)
and, with the same logic, root-dossier corpus.py.
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

PROJECTS = Path(__file__).resolve().parents[3]
QD = PROJECTS / "quran-data" / "data"
FURUQ_PACKETS = PROJECTS / "dictionary" / "data" / "output" / "furuq" / "root_packets"


@lru_cache(maxsize=None)
def extra_root_names() -> dict[str, str]:
    """root id → spaced Arabic root, from the gateway, the reviewed word-root analyses and the furuq root packets."""
    out: dict[str, str] = {}
    gw = QD / "bridges" / "qac-dictionary-root-resolutions.json"
    if gw.exists():
        for r in json.loads(gw.read_text(encoding="utf-8"))["roots"]:
            if len(r.get("rootIds") or []) == 1 and r.get("qacRoot"):
                out.setdefault(r["rootIds"][0], r["qacRoot"])
    alts = QD / "bridges" / "qac-dictionary-word-root-analyses.json"
    if alts.exists():
        for rec in json.loads(alts.read_text(encoding="utf-8")).get("records", []):
            for an in rec.get("analyses", []):
                if an.get("dictionaryRootId") and an.get("rootArabic"):
                    out.setdefault(an["dictionaryRootId"], " ".join(an["rootArabic"].replace(" ", "")))
    for f in (QD / "dictionary" / "tr").glob("*_entry.json"):
        for rid in f.name[: -len("_entry.json")].split("--"):
            p = FURUQ_PACKETS / f"{rid}.json"
            if rid not in out and p.exists():
                name = json.loads(p.read_text(encoding="utf-8")).get("root_norm")
                if name:
                    out[rid] = name
    return out
