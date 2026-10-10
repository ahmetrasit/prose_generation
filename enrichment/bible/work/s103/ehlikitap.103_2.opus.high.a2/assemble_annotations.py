"""Format-only helper: apply my id renumbering, drop the record I decided to remove, add new records, sort by paragraph."""
import json
from pathlib import Path

D = Path(__file__).resolve().parent
RENAME = {
    "S103-TEV-MTF-014": "S103-TEV-MTF-016", "S103-TEV-MTF-013": "S103-TEV-MTF-015",
    "S103-TEV-MTF-012": "S103-TEV-MTF-014", "S103-TEV-MTF-011": "S103-TEV-MTF-013",
    "S103-TEV-MTF-010": "S103-TEV-MTF-012", "S103-TEV-MTF-009": "S103-TEV-MTF-011",
    "S103-TEV-MTF-008": "S103-TEV-MTF-010", "S103-TEV-MTF-007": "S103-TEV-MTF-009",
    "S103-TEV-MTF-006": "S103-TEV-MTF-008", "S103-TEV-MTF-005": "S103-TEV-MTF-007",
    "S103-TEV-MTF-004": "S103-TEV-MTF-005", "S103-TEV-MTF-003": "S103-TEV-MTF-004",
    "S103-INC-MTF-007": "S103-INC-MTF-009",
}
DROP = {"S103-TEV-MTF-015"}  # Taanit 23a, removed by my decision (old id)
old = [json.loads(l) for l in (D / "annotations.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
out = []
for r in old:
    if r["id"] in DROP:
        continue
    r["id"] = RENAME.get(r["id"], r["id"])
    if r["id"] == "S103-INC-MTF-009":
        r["kaynak"] = "SBLGNT:Luke.15.13|SBLGNT:Luke.15.17|SBLGNT:Luke.15.24"
    out.append(r)
out += [json.loads(l) for l in (D / "new_records.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
ids = [r["id"] for r in out]
assert len(ids) == len(set(ids)), ids
out.sort(key=lambda r: (int(r["paragraf"]), r["id"].split("-")[1] != "TEV", r["id"]))
(D / "annotations.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in out), encoding="utf-8")
print(len(out))
for r in out:
    print(r["paragraf"], r["id"])
