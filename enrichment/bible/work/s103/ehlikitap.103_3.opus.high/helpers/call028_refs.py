import csv, sys
csv.field_size_limit(10**9)
rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8"), delimiter="\t"))
refs = []
for r in rows:
    if r["ref"] not in refs:
        refs.append(r["ref"])
wlc = [r for r in refs if r.startswith("WLC:")]
nt = [r for r in refs if r.startswith("SBLGNT:")]
oth = [r for r in refs if r not in wlc and r not in nt]
print(len(wlc), len(nt), len(oth))
for name, lst in (("WLC", wlc), ("NT", nt)):
    for i in range(0, len(lst), 25):
        print(name, " ".join(lst[i:i + 25]))
