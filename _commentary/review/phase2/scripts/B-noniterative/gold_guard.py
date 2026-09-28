"""Which S1 gold items (quran-slm/reports/s1_ar3_v1_gold_ledger.jsonl) rest on collocation-bound branches, and would a
strict construction guard (construction key within the Fatiha ayah that carries the root) block them?

Evaluation-only use of gold (it never enters a prompt). Output: gold_guard.tsv + stdout summary.
"""
import json, collections, csv, os
import load, construction

GOLD = "/Volumes/OZTURK/_projects/quran-slm/reports/s1_ar3_v1_gold_ledger.jsonl"
rid2root = {}
for (root, b), r in load.branches().items():
    rid2root[r["root_id"]] = root

rows = []
kinds = collections.Counter()
items_blocked = set()
eligible = 0
for line in open(GOLD, encoding="utf-8"):
    g = json.loads(line)
    if not g.get("eligibility", {}).get("eligible"):
        continue
    eligible += 1
    anchors = list(g.get("required_branch_anchors", []))
    for grp in g.get("required_branch_anchor_groups", []):
        anchors += grp.get("node_ids", [])
    for a in anchors:
        _, rid, b = a.split(":")
        root = rid2root.get(rid)
        row = load.branches().get((root, b)) if root else None
        if not row:
            rows.append([g["gold_id"], a, root or "?", "?", "", "", g["description"][:90]])
            continue
        kind = load.kind_of(row)[0]
        kinds[kind] += 1
        # where does the root occur in S1?
        occ = [o for o in load.root_index().get(root, []) if o.startswith("1:")]
        verdict = ""
        if kind == "collocation":
            keys = construction.keys_for(row)
            lic = [o for o in occ if construction.licensed_v2(o, row, None)]
            verdict = "licensed" if lic else ("BLOCKED(strict)" if occ else "root not in S1")
            if verdict.startswith("BLOCKED"):
                items_blocked.add(g["gold_id"])
        rows.append([g["gold_id"], a, root, b, kind, verdict, row["image"], g["description"][:90]])

with open(os.path.join(load.OUT, "gold_guard.tsv"), "w", encoding="utf-8") as fh:
    w = csv.writer(fh, delimiter="\t")
    w.writerow(["gold_id", "node", "root", "branch", "kind", "strict_guard", "image", "description"])
    w.writerows(rows)
print(f"eligible gold items: {eligible}; required branch anchors by kind: {dict(kinds)}")
print(f"gold items with at least one required anchor (hard or in a group) a strict guard would block: {len(items_blocked)}")
# hard requirement vs group alternative
hard_blocked = []
for line in open(GOLD, encoding="utf-8"):
    g = json.loads(line)
    if g["gold_id"] not in items_blocked:
        continue
    blocked_nodes = {r[1] for r in rows if r[0] == g["gold_id"] and len(r) > 5 and r[5].startswith("BLOCKED")}
    hard = [a for a in g.get("required_branch_anchors", []) if a in blocked_nodes]
    groups_dead = [grp for grp in g.get("required_branch_anchor_groups", [])
                   if all(n in blocked_nodes for n in grp.get("node_ids", []))]
    if hard or groups_dead:
        hard_blocked.append(g["gold_id"])
print(f"gold items a strict guard would make unreachable (hard anchor or a whole group blocked): {len(hard_blocked)} of {eligible}: {hard_blocked}")
for r in rows:
    if len(r) > 5 and r[5].startswith("BLOCKED"):
        print("  ", r[0], r[2], r[3], r[6], "|", r[7])
