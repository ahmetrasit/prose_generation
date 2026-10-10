import json, sys
d = json.load(open(sys.argv[1], encoding="utf-8"))
for blk in d["findings"]:
    v = blk["validation"]
    print("==", blk["model"], "rows", v.get("rows"), "uniq", v.get("unique_references"), "dups", len(v.get("duplicates", [])), "schema_errors", v.get("schema_errors"))
    for k, val in v.items():
        if k not in ("findings", "file", "rows", "unique_references", "duplicates", "schema_errors", "strengths"):
            print("  extra", k, json.dumps(val, ensure_ascii=False)[:500])
    for f in v.get("findings", []):
        extra = {k: f[k] for k in f if k not in ("line", "ref", "kind", "message")}
        print(f"  L{f.get('line')}\t{f.get('ref')}\t{f.get('kind')}\t{json.dumps(extra, ensure_ascii=False)[:300]}")
other = {k: d[k] for k in d if k not in ("findings", "provenance")}
print(json.dumps(other, ensure_ascii=False)[:1000])
