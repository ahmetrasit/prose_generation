import csv, json, sys
csv.field_size_limit(10**9)
pf = json.load(open(sys.argv[1], encoding="utf-8"))
rows = list(csv.DictReader(open(sys.argv[2], encoding="utf-8"), delimiter="\t"))
refs = sorted({r["ref"] for r in rows if not (r["ref"].startswith("WLC:") or r["ref"].startswith("SBLGNT:"))})
by = {}
for c in pf["candidates"]:
    by.setdefault(c["ref"], []).append(c)
print("limitation:", pf["limitation"])
print("coverage_complete", pf["coverage_complete"], "related_fetched", pf["related_fetched"])
print("missing sample:", json.dumps(pf["missing"][:3], ensure_ascii=False))
miss = {}
for m in pf["missing"]:
    key = m.get("ref") if isinstance(m, dict) else m
    miss[key] = m
for r in refs:
    cs = by.get(r, [])
    for c in cs:
        print(r, "|", c.get("status"), "|", c.get("locators"), "|", c.get("related"), "|", {k: c[k] for k in c if k not in ("ref", "status", "locators", "related", "tradition")})
    if not cs:
        print(r, "| NOT IN PREFETCH")
    if r in miss:
        print("   missing:", json.dumps(miss[r], ensure_ascii=False)[:300])
