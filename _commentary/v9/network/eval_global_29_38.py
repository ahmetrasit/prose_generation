#!/usr/bin/env python3
"""Global-layer test for 29:38: of the ayat outside the surah and the Fatiha that the cold Opus reading cites
(harvest, sections S1–S6 and Ek Notlar), how many does the network reach, and how?

Usage: python3 _commentary/v9/network/eval_global_29_38.py NETWORK_JSON [...]
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from network import weight  # noqa: E402

HARVEST = Path(__file__).resolve().parents[1] / "pilot" / "29_38-v2" / "29_38.harvest.md"


def opus_refs():
    text = HARVEST.read_text(encoding="utf-8")
    block = text.split("## Inter-ayah rows used", 1)[1].split("\n## ", 1)[0]
    out = {}
    for line in block.splitlines():
        m = re.match(r"- (S\d|EN): (.*)", line.strip())
        if m:
            for r in re.findall(r"\d+:\d+", m.group(2)):
                if not r.startswith(("29:", "1:")):
                    out.setdefault(r, m.group(1))
    return out


def main():
    gold = opus_refs()
    for path in sys.argv[1:]:
        d = json.loads(Path(path).read_text(encoding="utf-8"))
        N, E = d["nodes"], d["edges"]
        how = {}
        for e in E:
            for a, b in ((e["a"], e["b"]), (e["b"], e["a"])):
                if b.startswith("A:") and N.get(a, {}).get("type") in ("B", "F"):
                    r = b[2:]
                    w = weight(e)
                    kind = f"{e['kind']}{'/' + e['sub'] if e['sub'] else ''}"
                    if w > 0:
                        how.setdefault(r, set()).add(("strong", kind, N[a].get("rare", False)))
                    else:
                        how.setdefault(r, set()).add(("weak", kind, N[a].get("rare", False)))
        zone = {n[2:]: x["zone"] for n, x in N.items() if x["type"] == "A"}
        c = Counter()
        rows = []
        for r, sec in sorted(gold.items(), key=lambda kv: tuple(map(int, kv[0].split(":")))):
            z = zone.get(r)
            h = how.get(r, set())
            status = ("not in network" if not z else "strong" if any(x[0] == "strong" for x in h)
                      else "weak only" if h else "in network, no edge")
            c[status] += 1
            rows.append(f"  {r:7} {sec:3} {z or '-':7} {status:20} {', '.join(sorted({x[1] for x in h if x[0] == 'strong'}))[:70]}")
        a_nodes = sum(1 for x in N.values() if x["type"] == "A")
        strong_a = sum(1 for r, h in how.items() if any(x[0] == "strong" for x in h))
        print(f"== {path}: {len(gold)} Opus-cited ayat outside surah/Fatiha; {dict(c)}")
        print(f"   network: {a_nodes} context ayat, {strong_a} with a strong edge from the focus ayah; zones {dict(Counter(zone.values()))}")
        if "-v" in sys.argv[0:1] or len(sys.argv) == 2:
            print("\n".join(rows))


if __name__ == "__main__":
    main()
