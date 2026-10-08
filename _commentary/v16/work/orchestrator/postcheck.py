"""After a v16 finish: ledger row, output files, read coverage of prompt.md, tool calls. Usage: postcheck.py <run dir rel to v16>..."""
import json, os, re, sys

V16 = "/Volumes/aro/projects/prose_generation/_commentary/v16"
rows = [json.loads(l) for l in open(f"{V16}/out/ledger.jsonl")]
for d in sys.argv[1:]:
    p = f"{V16}/{d}"
    name = os.path.basename(d)
    print(f"== {d}")
    print("  files:", sorted(os.listdir(p)))
    lines = sum(1 for _ in open(f"{p}/prompt.md", encoding="utf-8"))
    tc = json.load(open(f"{p}/tool_calls.json")) if os.path.exists(f"{p}/tool_calls.json") else []
    covered = set()
    others = []
    for c in tc:
        i = c.get("input", {})
        if c.get("name") == "Read" and i.get("file_path", "").endswith(f"{name}/prompt.md"):
            res = str(c.get("result", ""))
            nums = [int(m) for m in re.findall(r"(?m)^\s*(\d+)\t", res)]
            covered.update(nums)
        else:
            cmd = i.get("command") or i.get("file_path") or ""
            others.append(f"{c.get('name')}: {cmd[:160]}")
            if c.get("name") == "Edit":
                others.append(f"   OLD: {i.get('old_string','')[:250]!r}")
                others.append(f"   NEW: {i.get('new_string','')[:250]!r}")
    missing = [n for n in range(1, lines + 1) if n not in covered]
    rng = []
    for n in missing:
        if rng and n == rng[-1][1] + 1:
            rng[-1][1] = n
        else:
            rng.append([n, n])
    print(f"  prompt lines {lines}, read {len(covered)}, unread {len(missing)}"
          + (f": {', '.join(f'{a}-{b}' if a != b else str(a) for a, b in rng[:10])}" if missing else ""))
    for o in others:
        print("  other tool:", o)
    if os.path.exists(f"{p}/check.json"):
        cj = json.load(open(f"{p}/check.json"))
        for k in ("sources", "unsourced_unmarked", "arabic_outside_tags", "process_lines"):
            v = cj.get(k)
            if v:
                print(f"  check {k}: {json.dumps(v, ensure_ascii=False)[:700]}")
    rel = d.replace("out/", "")
    mine = [r for r in rows if rel.split("/")[-1].replace("surah.", "") in str(r.get("brief")) and
            (r.get("ref") == "S" + str(int(rel.split("/")[0][1:])) if rel.startswith("s") else True)]
    for r in mine[-2:]:
        print("  ledger:", {k: r.get(k) for k in ("ref", "arm", "brief", "estimate_usd", "cost_usd", "status", "check",
                                                  "check_findings", "post_error", "stop_reason") if k in r})
