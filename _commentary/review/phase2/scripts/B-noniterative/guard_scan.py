"""Scan earlier outputs (v11-v15 ledgers, records, prose) for 'root Bnnn' citations and apply the branch_kind guard.

Question: would a script-level branch_kind guard have had anything to catch in what earlier versions produced?
For every distinct (focus ayah, root, branch) cited:
  - kind from quran-data TR entries (lexicalization_scope.branch_kind)
  - if collocation-bound and the root occurs in the focus ayah: is the construction key present (+-4 words / ayah)?
Output: guard_scan.tsv + a summary on stdout.
"""
import re, os, glob, collections, csv
import load, construction

PG = load.PG + "/_commentary"
PAT = re.compile(r"([ء-ي] [ء-ي] [ء-ي](?: [ء-ي])?) (B\d{3})")
FOCUS = re.compile(r"/s(\d{3})/(\d+)_(\d+)/")

files = []
for v in ("v11", "v12", "v13", "v14", "v15"):
    for f in glob.glob(f"{PG}/{v}/out*/**/*", recursive=True):
        if os.path.isfile(f) and f.endswith((".md", ".json")) and not f.endswith(("prompt.md",)) and "raw.json" not in f:
            if FOCUS.search(f):
                files.append((v, f))

triples = collections.defaultdict(set)   # (focus, root, B) -> versions
for v, f in files:
    m = FOCUS.search(f)
    focus = f"{int(m.group(2))}:{int(m.group(3))}"
    try:
        txt = open(f, encoding="utf-8").read()
    except Exception:
        continue
    for root, b in PAT.findall(txt):
        triples[(focus, load.nroot(root), b)].add(v)

br = load.branches()
kinds = collections.Counter()
rows = []
for (focus, root, b), vs in sorted(triples.items()):
    row = br.get((root, b))
    if not row:
        kinds["no such branch"] += 1
        rows.append([focus, root, b, "no_such_branch", "", "", "", ",".join(sorted(vs))])
        continue
    kind = load.kind_of(row)[0]
    kinds[kind] += 1
    in_focus = [w["ref"] for w in load.words()[1].get(focus, []) if root in [load.nroot(x) for x in (w["roots"] or "").split("|")]]
    lic4 = licA = ""
    if kind == "collocation" and in_focus:
        keys = construction.keys_for(row)
        lic4 = any(construction.licensed_v2(o, row, 4) for o in in_focus)
        licA = any(construction.licensed_v2(o, row, None) for o in in_focus)
        lic4, licA = str(lic4), str(licA)
        keys = " ".join(keys)
    else:
        keys = ""
    rows.append([focus, root, b, kind, "yes" if in_focus else "no", keys, lic4 + "/" + licA if lic4 else "",
                 ",".join(sorted(vs)), row["image"]])

with open(os.path.join(load.OUT, "guard_scan.tsv"), "w", encoding="utf-8") as fh:
    w = csv.writer(fh, delimiter="\t")
    w.writerow(["focus", "root", "branch", "kind", "root_in_focus", "construction_keys", "licensed_pm4/ayah",
                "versions", "image"])
    w.writerows(rows)

print(f"files scanned: {len(files)}; distinct (focus, root, branch) citations: {len(triples)}")
print("by branch_kind:", dict(kinds))
coll = [r for r in rows if r[3] == "collocation"]
print(f"collocation-bound citations: {len(coll)}; root in focus ayah: {sum(1 for r in coll if r[4]=='yes')}")
unl = [r for r in coll if r[4] == "yes" and r[6].startswith("False")]
print(f"  of which construction key NOT found within +-4 words: {len(unl)}; not found anywhere in the ayah: "
      f"{sum(1 for r in unl if r[6].endswith('False'))}")
for r in unl:
    print("   ", r[0], r[1], r[2], "| keys:", r[5], "|", r[6], "|", r[7], "|", r[8][:60])
