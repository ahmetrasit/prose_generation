#!/usr/bin/env python3
"""Reproduce the independent ayah-enrichment audit without changing production.

No model calls, network, corpus writes, pack rebuilds or accepted-output writes.
Temporary synthetic inputs exercise the existing validators. Results describe
observed weaknesses, not successful enrichment. Run from any working directory:

  python3 -B enrichment/v2/audits/2026-10-06-ayah-independent/audit.py
"""
from __future__ import annotations

import contextlib
import copy
import hashlib
import io
import json
import re
import sqlite3
import sys
import tempfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
V2 = HERE.parents[1]
PG = V2.parents[1]
sys.path.insert(0, str(V2))
import grup as G
import render as R
import validate as V


def digest(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")


def inventory() -> dict:
    upstream = {}
    for d in sorted((PG / "_commentary/v16/out").iterdir()):
        if not d.is_dir() or not re.fullmatch(r"\d+_\d+", d.name):
            continue
        pat = f"DM.r13.images.r13.*/{d.name}.reading.tr.md"
        raw = [p for p in d.glob(pat) if "session-limit" not in str(p)]
        aug = [p for p in d.glob(f"DM.r13.images.r13.*/augment.augment9.opus/{d.name}.reading.tr.md")
               if "session-limit" not in str(p)]
        upstream[d.name.replace("_", ":")] = {
            "r13": [str(p.relative_to(PG)) for p in raw],
            "augment9": [str(p.relative_to(PG)) for p in aug],
        }
    packs = {}
    for pk in sorted((V2 / "work").glob("s*/pack")):
        entries = json.loads((pk / "base.json").read_text())["ayat"]
        rows = {}
        for ref, entry in entries.items():
            if not entry:
                rows[ref] = {"base": None}
                continue
            original = PG / entry["path"]
            local = pk / "base" / (ref.replace(":", "_") + ".md")
            rows[ref] = {
                "base": entry["path"], "sha256": entry["sha256"],
                "augment9": "/augment.augment9.opus/" in entry["path"],
                "upstream_matches": original.exists() and digest(original) == entry["sha256"],
                "copy_matches": local.exists() and digest(local) == entry["sha256"],
            }
        packs[pk.parent.name] = rows
    return {
        "upstream": upstream,
        "upstream_counts": dict(Counter("r13+augment9" if x["augment9"] else
                                        "r13_without_augment9" if x["r13"] else "neither"
                                        for x in upstream.values())),
        "packs": packs,
    }


def output_coverage() -> list[dict]:
    rows = []
    for d in sorted((V2 / "work/s001").glob("zengin*1_1*")):
        ann = d / "annotations.jsonl"
        if not ann.exists():
            continue
        records = R.load(ann)
        paras = R.paragraphs(R.target_page(1, "1:1")[1])
        nums = R.prose_index(paras)
        counts = Counter(int(r["paragraf"]) for r in records)
        rows.append({
            "directory": str(d.relative_to(PG)), "annotations_sha256": digest(ann),
            "paragraphs": len(nums), "annotations": len(records),
            "counts_per_paragraph": {str(n): counts[n] for n in nums},
            "paragraphs_without_annotations": [n for n in nums if not counts[n]],
            "memory_records": sum("hafiza" in r.get("kaynak", "") for r in records),
            "caveat": "Paragraph presence is only a lower bound; it does not establish claim coverage.",
        })
    return rows


def validator_probes(records: list[dict]) -> dict:
    base = R.target_page(1, "1:1")[1]
    out = {"accepted_records_current_validation": V.validate(1, "1:1", copy.deepcopy(records), None),
           "empty_annotations": V.validate(1, "1:1", [], None)}
    with tempfile.TemporaryDirectory(prefix="ayah-enrichment-audit-") as tmp:
        d = Path(tmp)
        out["missing_placement_files"] = {"errors": G.check_place(1, d, "1:1")[1]}
        write_jsonl(d / "input_lines.jsonl", [{"id": "rivayet.u01/L1", "m": "Synthetic position"}])
        write_jsonl(d / "yer.jsonl", [{"id": "rivayet.u01/L1", "p": 1}])
        out["one_placed_line_no_claim_inventory"] = {"errors": G.check_place(1, d, "1:1")[1]}
        (d / "page.md").write_text(base + "\n## Kaynak kayıtları\n", encoding="utf-8")
        out["rendered_page_all_annotations_deleted"] = {
            "expected_records": len(records), "errors": V.check_page(d / "page.md", base, records)}

        # Isolate only orchestration/accounting: production semantic validators
        # still run. No logs or started markers are written into work/.
        place_dir = d / "place"
        place_dir.mkdir()
        (place_dir / "started.json").write_text(json.dumps({"unit": "yer.1_1", "pages": ["1:1"]}))
        (place_dir / "yer.jsonl").write_text("")
        with patch.object(G, "call_dir", return_value=place_dir), \
                patch.object(G, "run_usage", return_value=None), patch.object(G, "log", return_value=None), \
                contextlib.redirect_stdout(io.StringIO()):
            out["finish_place_missing_input_and_bos"] = G.finish_place(1, "1:1", "astra", "high")

        drop_dir = d / "drop"
        drop_dir.mkdir()
        (drop_dir / "started.json").write_text(json.dumps({"unit": "synthetic.u01", "output": "kapsam.jsonl"}))
        write_jsonl(drop_dir / "lines.jsonl", [{"id": "L1", "pg": "1:1", "w": "ayah", "t": "bogus",
                                               "f": "aciklama", "k": "TAB:1:1", "m": "Invalid type"}])
        write_jsonl(drop_dir / "kapsam.jsonl", [{"seg": "TAB:1:1", "durum": "ilgisiz"}])
        (drop_dir / "gaps.json").write_text("{}")
        unit = {"id": "synthetic.u01", "group": "synthetic", "pages": ["1:1"], "items": ["TAB:1:1"]}
        with patch.object(G, "call_dir", return_value=drop_dir), patch.object(G, "run_usage", return_value=None), \
                patch.object(G, "log", return_value=None), patch.object(G, "load_plan", return_value={"units": [unit]}), \
                patch.object(G, "GROUPS", {"groups": [{"id": "synthetic"}]}), \
                contextlib.redirect_stdout(io.StringIO()):
            out["finish_extract_dropped_only_line"] = G.finish(1, "synthetic.u01", "astra", "high")

        import enrich as E
        empty_dir = d / "empty-trial"
        empty_dir.mkdir()
        (empty_dir / "annotations.jsonl").write_text("")
        out["empty_one_call_trial_finish"] = E.finish(1, "1:1", empty_dir, trial=True)

    novelty = copy.deepcopy(next(r for r in records if r["tur"] == "yenilik"))
    second = copy.deepcopy(novelty)
    novelty["id"], second["id"] = "S001-YNL-998", "S001-YNL-999"
    second["metin"] = "Aynı paragraftaki başka bir bulgu için taranan kaynaklarda doğrudan öncül bulunamadı."
    kept, dropped, _ = V.check_records(1, "1:1", [novelty, second])
    out["two_novel_claim_records_same_paragraph"] = {"kept": len(kept), "dropped": dropped}
    hadith = copy.deepcopy(next(r for r in records if r["tur"] == "hadis"))
    hadith.update(kaynak="KASHSHAF:1:1", metin="Kaynak türü doğrulamasını sınamak için yapay hadis kaydı.")
    kept, dropped, _ = V.check_records(1, "1:1", [hadith])
    out["sahih_claim_without_hadith_source"] = {"kept": len(kept), "dropped": dropped}
    return out


def retrieval_probes(con: sqlite3.Connection) -> dict:
    held = G.held_sources()
    group = next(g for g in G.GROUPS["groups"] if g["id"] == "hadis")
    items, info = G.group_items(con, 1, group, [sid for sid in group["sources"] if sid in held])
    locs = {it["seg"] for it in items}
    out = {"hadith_1": {
        "selected_segments": len(items),
        "per_page": {p: sum(p in it["pages"] for it in items) for p in G.pages(1)},
        "searches": info.get("queries", []), "known_relevant_reports": {},
    }}
    for loc in ("BUKHARI:5376", "ABUDAWUD:1694", "BUKHARI:5988"):
        row = con.execute("SELECT text,extra FROM seg WHERE seg=?", (loc,)).fetchone()
        extra = json.loads(row[1]) if row else {}
        out["hadith_1"]["known_relevant_reports"][loc] = {
            "exists": bool(row), "selected": loc in locs, "sahih_in_corpus": extra.get("sahih"),
            "text_sha256": hashlib.sha256(row[0].encode()).hexdigest() if row else None,
            "reference": extra.get("reference"),
        }
    counts = {}
    for q in ("اهدنا الصرط المستقيم", "اهدنا الصراط المستقيم", "لله رب العلمين", "لله رب العالمين",
              "ملك يوم الدين", "مالك يوم الدين"):
        counts[q] = con.execute("SELECT count(*) FROM f JOIN seg ON seg.id=f.rowid WHERE f MATCH ? "
                               "AND seg.src='MUSLIM' AND json_extract(seg.extra,'$.sahih')=1",
                               ('"' + q + '"',)).fetchone()[0]
    out["exact_phrase_spelling_counts_in_muslim"] = counts
    routes = {}
    for gid in ("rivayet", "mezhep"):
        group = next(g for g in G.GROUPS["groups"] if g["id"] == gid)
        items, _ = G.group_items(con, 1, group, [sid for sid in group["sources"] if sid in held])
        for item in items:
            if item["seg"] in ("MUQATIL:1:1-4", "MUQATIL:1:5-7", "TABATABAI:1:1-5#5"):
                routes[item["seg"]] = item["pages"]
    out["range_segment_routes"] = routes
    out["group_execution"] = {}
    for s in (1, 87):
        d = G.gdir(s)
        plan = G.load_plan(s)
        out["group_execution"][str(s)] = {
            "prepared": len(list(d.glob("*.*.*/started.json"))),
            "finished": len(list(d.glob("*.*.*/run.log.json"))),
            "planned_units": len(plan["units"]), "pages": plan["pages"],
            "units_over_material_budget": [{"unit": u["id"], "chars": u["material_chars"]}
                                            for u in plan["units"] if u["material_chars"] > plan["budget_chars"]],
        }
    assigned = {sid for g in G.GROUPS["groups"] for sid in g["sources"]}
    excluded = {sid for g in G.GROUPS.get("not_read", []) for sid in g["sources"]}
    out["unassigned_held_sources_excluding_pack_inputs_and_explicit_exclusions"] = [
        [sid, kind] for sid, kind, access in con.execute("SELECT id,kind,access FROM src ORDER BY id")
        if sid not in assigned | excluded and access != "hafiza"
        and kind not in ("meal", "translation", "turkish_dict", "quran")]
    out["memory_only_sources"] = con.execute("SELECT id,kind FROM src WHERE access='hafiza' ORDER BY id").fetchall()
    # A distinct final position is not a duplicate merely because most of the
    # segment repeats an earlier edition. Exercise the actual deduplication code.
    with sqlite3.connect(":memory:") as synthetic:
        synthetic.execute("CREATE TABLE seg (id INTEGER PRIMARY KEY,seg TEXT,src TEXT,s INTEGER,a INTEGER,"
                          "a_end INTEGER,head TEXT,text TEXT,extra TEXT)")
        synthetic.execute("CREATE TABLE ref (seg_id INTEGER,s INTEGER,a INTEGER,a_end INTEGER)")
        original = con.execute("SELECT text FROM seg WHERE seg='TAB:1:1'").fetchone()[0][:6000]
        tail = (" وذهب آخرون إلى قول مخالف لم يذكر في النص المختصر لأن سبب هذا الحكم مختلف "
                "وهذا هو الرأي الزائد المستقل في النسخة المطولة")
        synthetic.execute("INSERT INTO seg VALUES(1,?,?,?,?,?,?,?,?)",
                          ("TEST:1:1", "TEST", 1, 1, 1, "", original, "{}"))
        synthetic.execute("INSERT INTO seg VALUES(2,?,?,?,?,?,?,?,?)",
                          ("TEST-FULL:1:1", "TEST-FULL", 1, 1, 1, "", original + tail, "{}"))
        kept, dropped = G.ayah_items(synthetic, 1, ["TEST", "TEST-FULL"], {"surah", "1:1"})
        out["synthetic_distinct_position_lost_by_deduplication"] = {
            "retained": [it["seg"] for it in kept], "dropped": dropped,
            "distinct_tail": tail, "tail_in_retained_material": any(tail in it["text"] for it in kept),
            "caveat": "Synthetic loss demonstration, not a claim that this sentence occurs in Tabari.",
        }
    return out


def main() -> None:
    records = R.load(V2 / "work/s001/zengin.1_1.opus.high/annotations.jsonl")
    with sqlite3.connect(f"file:{G.C.INDEX}?mode=ro", uri=True) as con:
        result = {
            "generated_utc": datetime.now(timezone.utc).isoformat(),
            "scope": "Ayah workflow audit. Existing output and synthetic probes; no generation or acceptance.",
            "code_sha256": {str(p.relative_to(PG)): digest(p) for p in
                            [V2 / n for n in ("grup.py", "enrich.py", "pack.py", "render.py", "validate.py",
                                              "groups.json", "prompts/grup.md", "prompts/grup_yer.md",
                                              "prompts/grup_oncul.md", "tools/blocks.py", "tools/corpus.py")]},
            "inventory": inventory(), "output_coverage": output_coverage(),
            "validator_probes": validator_probes(records), "retrieval_probes": retrieval_probes(con),
        }
    path = HERE / "results.json"
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    v = result["validator_probes"]
    reproduced = {
        "empty_annotations_pass": v["empty_annotations"]["passed"],
        "missing_placement_files_pass": not v["missing_placement_files"]["errors"],
        "single_line_no_claim_inventory_pass": not v["one_placed_line_no_claim_inventory"]["errors"],
        "deleted_annotations_not_detected": not v["rendered_page_all_annotations_deleted"]["errors"],
        "missing_placement_inputs_marked_ok": v["finish_place_missing_input_and_bos"]["status"] == "ok",
        "dropped_only_line_marked_ok": v["finish_extract_dropped_only_line"]["status"] == "ok",
        "empty_one_call_trial_marked_ok": v["empty_one_call_trial_finish"]["ok"],
        "second_novel_claim_dropped": v["two_novel_claim_records_same_paragraph"]["kept"] == 1,
        "hadith_without_hadith_source_pass": v["sahih_claim_without_hadith_source"]["kept"] == 1,
        "distinct_position_discarded_as_duplicate": not result["retrieval_probes"][
            "synthetic_distinct_position_lost_by_deduplication"]["tail_in_retained_material"],
    }
    print(json.dumps({"results": str(path.relative_to(PG)), "reproduced_weaknesses": reproduced,
                      "all_reproduced": all(reproduced.values())}, indent=2))
    # Exit success means the audit ran and reproduced its observations.
    # It is never an enrichment-readiness signal.
    raise SystemExit(0 if all(reproduced.values()) else 1)


if __name__ == "__main__":
    main()
