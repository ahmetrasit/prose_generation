import csv, json, sys
csv.field_size_limit(10**9)
path = sys.argv[1]
mode = sys.argv[2] if len(sys.argv) > 2 else "sum"
rows = list(csv.DictReader(open(path, encoding="utf-8"), delimiter="\t"))
seen = {}
for r in rows:
    ev = json.loads(r["evidence"])
    for e in ev:
        cid = e.get("connection_id")
        seen.setdefault(cid, []).append((r["ref"], e))
print("rows", len(rows), "distinct cids", len(seen))
for cid, lst in seen.items():
    ref, e = lst[0]
    if mode == "sum":
        print(f"{cid}\t{ref}\t{e.get('tradition')}\t{e.get('kind')}\t{e.get('strength')}\t{e.get('model')}\t{e.get('basis')}")
    else:
        print(f"{cid}\t{ref}\t{e.get('tradition')}\t{e.get('kind')}\t{e.get('strength')}\t{e.get('model')}\t{e.get('basis')}\t{e.get('note')}")
