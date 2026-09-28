"""v15 records (out, out-nocap): which FINDING anchors (used readings, not set-asides) are collocation-bound, and is the
construction key present in the anchor's ayah? Findings' triggers are printed for manual reading."""
import json, glob, re
import load, construction
C = load.PG + "/_commentary/v15"
n = 0; coll = []
for f in sorted(glob.glob(f"{C}/out*/s*/*/record.json")):
    d = json.load(open(f, encoding="utf-8"))
    for fd in d.get("findings", []):
        a = fd.get("anchor") or {}
        root, b, ref = load.nroot(a.get("root", "")), a.get("branch", ""), a.get("ref", "")
        row = load.branches().get((root, b))
        if not row:
            continue
        n += 1
        kind = load.kind_of(row)[0]
        if kind == "collocation":
            keys = construction.keys_for(row)
            lic = construction.licensed_v2(ref, row, None) if ref.count(":") == 2 else None
            coll.append((f.split("/v15/")[1].rsplit("/", 1)[0], ref, root, b, row["image"], keys, lic, fd.get("for_prose"),
                         (fd.get("statement") or "")[:160]))
print(f"v15 finding anchors: {n}; collocation-bound: {len(coll)}")
for c in coll:
    print(" ", c[0], c[1], c[2], c[3], c[4], "| keys", c[5], "| key in ayah:", c[6], "|", c[7], "|", c[8])
