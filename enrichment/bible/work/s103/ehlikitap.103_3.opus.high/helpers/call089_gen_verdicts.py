import csv, json, sys
csv.field_size_limit(10**9)
tsv, notes_path, ann_path, out_path = sys.argv[1:5]
notes = json.load(open(notes_path, encoding="utf-8"))
anns = {}
for line in open(ann_path, encoding="utf-8"):
    if line.strip():
        r = json.loads(line)
        anns[r["id"]] = r
ST = {"A": "accepted", "R": "rejected", "U": "unresolved", "N": "unavailable"}

def locals_of(aid):
    a = anns[aid]
    return [l.strip() for l in a["kaynak"].split("|") if l.strip() and l.strip() != "hafiza"]

def build(ref, entry, extra_reason=""):
    status, paras, aid, reason = entry[0], entry[1], entry[2], entry[3]
    override = entry[4] if len(entry) > 4 else None
    aids = [aid] if isinstance(aid, str) and aid else (list(aid) if isinstance(aid, list) else [])
    ev = []
    if override is not None:
        ev.extend(override)
    elif status in ("A", "R") and ref.split(":")[0] in ("WLC", "SBLGNT", "SEFARIA", "QURAN", "KJV", "CORPUSCORANICUM"):
        ev.append(ref)
    for x in aids:
        if x not in anns:
            raise SystemExit(f"unknown annotation {x} for {ref}")
        ev.extend(locals_of(x))
    if status in ("A", "R") and ref.split(":")[0] in ("WLC", "SBLGNT") and ref not in ev:
        ev.insert(0, ref)
    seen = []
    for e in ev:
        if e not in seen:
            seen.append(e)
    return {"ref": ref, "status": ST[status], "reason": reason + extra_reason, "paragraphs": paras,
            "evidence": seen, "annotations": aids}

rows = list(csv.DictReader(open(tsv, encoding="utf-8"), delimiter="\t"))
out = []
covered = set()
missing = []
for r in rows:
    for e in json.loads(r["evidence"]):
        ref = r["ref"]
        if ref not in notes["discovery"]:
            missing.append(ref); continue
        v = build(ref, notes["discovery"][ref], f" Reader proposal ({e.get('model')}, {e.get('kind')}, {e.get('strength')}): {e.get('basis')}.")
        rec = {"connection_id": e["connection_id"]}
        rec.update(v)
        out.append(rec)
        covered.update(v["annotations"])
for ref, entry in notes["research"].items():
    v = build(ref, entry)
    rec = {"connection_id": None, "origin": "research"}
    rec.update(v)
    out.append(rec)
    covered.update(v["annotations"])
if missing:
    print("MISSING discovery refs:", sorted(set(missing)))
unc = sorted(set(anns) - covered)
print("verdicts", len(out), "uncovered annotations", unc)
unused = sorted(set(notes["discovery"]) - {r["ref"] for r in rows})
print("notes refs not in tsv", unused)
with open(out_path, "w", encoding="utf-8") as f:
    for rec in out:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
