#!/usr/bin/env python3
"""Recall test for the 29:38 network (a test only; never shown to agents).

Gold 1: links the cold Opus reading used (pilot/29_38-v2/29_38.harvest.md), as (root, branch, target) where the
target is a focus word (w index) or a context ayah. Gold 2: every Luna "reading" record on a dictionary branch
(earlier run, archived records), as (branch, trigger ayah).

Usage: python3 _commentary/v9/network/eval_29_38.py network/out/29_38/network.k3.json [LUNA_RECORDS_DIR]
"""
import json
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from network import weight  # noqa: E402
from collections import defaultdict
from pathlib import Path

GOLD = [  # (root, branch, target, what the Opus reading does with it)
    ("ع و د", "B009", "F:1>F:14", "old road → al-sabīl (road hub)"),
    ("ع م ل", "B011", "F:14", "trodden road → al-sabīl"),
    ("ص د د", "B004", "F:14", "road to water → al-sabīl"),
    ("ص د د", "B013", "F:16", "kohl → mustabṣirīn (eye hub)"),
    ("س ب ل", "B010", "F:16", "eye-film → mustabṣirīn"),
    ("ب ي ن", "B007", "F:16", "land as far as the eye reaches → mustabṣirīn"),
    ("ع م ل", "B010", "F:16", "far-seeing eye → mustabṣirīn"),
    ("ز ي ن", "B001", "F:10", "beauty 'opposite of shayn' ↔ al-shayṭān"),
    ("ش ط ن", "B005", "F:8", "ugly snake ↔ zayyana"),
    ("ش ط ن", "B003", "F:12", "turning from one's intended direction ↔ ṣaddahum"),
    ("س ب ل", "B010", "A:29:41", "eye-film 'like spider web' ↔ 29:41 spider"),
    ("س ك ن", "B004", "A:29:37", "night as rest ↔ destroyed by morning (29:37)"),
    ("ص د د", "B005", "A:7:74", "barrier mountain ↔ Thamud carving mountains"),
    ("ص د د", "B002", "A:89:9", "valley sides ↔ Thamud in the valley"),
    ("س ب ل", "B005", "A:46:24", "rain ↔ ʿĀd took the cloud for rain"),
    ("ش ط ن", "B001", "A:11:68", "distance ↔ 'away with Thamud'"),
    ("ز ي ن", "B001", "A:29:7", "beauty ↔ aḥsana (29:7)"),
    ("ع م ل", "B012", "A:29:29", "foot travellers ↔ cutting the road (29:29)"),
    ("س ب ل", "B010", "A:1:6", "eye-film ↔ ق و م 'eye standing, sight gone' in al-mustaqīm"),
    ("س ك ن", "B007", "A:29:29", "(control: knife ↔ cutting; Opus rejected as no trigger)"),
]
PAIRS_F = [("F:4", "F:8", "tabayyana ~ zayyana"), ("F:16", "A:1:6", "Form X participle mustabṣirīn ~ al-mustaqīm"),
           ("F:16", "A:29:41", "kānū + predicate chain (29:41 law kānū yaʿlamūn)")]


def main():
    d = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    N, E = d["nodes"], d["edges"]
    adj = defaultdict(list)
    for e in E:
        adj[(e["a"], e["b"])].append(e)
        adj[(e["b"], e["a"])].append(e)
    hub_of = defaultdict(list)
    for score, h, members, n in d["hubs"][:16]:
        for m in members:
            hub_of[m].append(h)
    tri_nodes = defaultdict(int)
    for _k, b, x, y in d["triangles"][:60]:
        tri_nodes[(b, x)] += 1
        tri_nodes[(b, y)] += 1

    def bnode(root, bid):
        return [n for n, x in N.items() if x["type"] == "B" and x["root"] == root and x["bid"] == bid]

    found = 0
    print(f"== Opus links ({sys.argv[1]})")
    for root, bid, target, what in GOLD:
        best = None
        for b in bnode(root, bid):
            for t in target.split(">") if ">" in target else [target]:
                es = adj.get((b, t), [])
                if es:
                    best = (b, t, es)
        if best:
            b, t, es = best
            kinds = sorted({f"{e['kind']}/{e['sub']}" if e["sub"] else e["kind"] for e in es})
            strong = any(weight(e) > 0 for e in es)
            found += strong
            print(f"  {'STRONG' if strong else 'weak  '} {root} {bid} → {t}: {', '.join(kinds)}"
                  f"{' | hub ' + ','.join(hub_of[b]) if hub_of.get(b) else ''}{' | triangle' if tri_nodes.get((b, t)) else ''} — {what}")
        else:
            print(f"  MISS   {root} {bid} → {target} — {what}")
    print(f"  strong {found}/{len(GOLD) - 1} (last line is a control)")
    for a, b, what in PAIRS_F:
        es = adj.get((a, b), [])
        print(f"  {'yes ' if es else 'MISS'} {a} ↔ {b}: {', '.join(sorted({e['kind'] for e in es}))} — {what}")
    tri_hit = [t for t in d["triangles"][:60] if "root_000672:B010" in t[1] and {"F:16", "A:29:41"} & {t[2], t[3]}]
    print(f"  eye-film triangle in top 60: {'yes' if tri_hit else 'no'}")
    print(f"  size: {len(N)} nodes, {len(E)} edges, strong edges "
          f"{sum(1 for e in E if e['kind'] not in ('img', 'hft'))}, hubs {len(d['hubs'])}, triangles {len(d['triangles'])}")

    if len(sys.argv) > 2:
        recs = []
        for f in sorted(Path(sys.argv[2]).glob("*.jsonl")):
            for line in f.read_text(encoding="utf-8").splitlines():
                r = json.loads(line)
                if r.get("verdict") == "reading" and r.get("id", "").startswith("R") and r.get("branch"):
                    recs.append(r)
        hit = strong_hit = 0
        for r in recs:
            parts = r["branch"].split()
            root, bid = " ".join(parts[:-1]), parts[-1]
            ref = r.get("trigger_ref", "")
            targets = {f"A:{ref}"} if ref != "29:38" else {n for n in N if n.startswith("F:")}
            es = [e for b in bnode(root, bid) for t in targets for e in adj.get((b, t), [])]
            hit += bool(es)
            strong_hit += any(weight(e) > 0 for e in es)
        print(f"== Luna branch readings (earlier run): {len(recs)}; linked in network {hit} "
              f"({hit / max(1, len(recs)):.0%}), by a non-image edge {strong_hit} ({strong_hit / max(1, len(recs)):.0%})")


if __name__ == "__main__":
    main()
