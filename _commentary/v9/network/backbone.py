#!/usr/bin/env python3
"""Backbone document for the Sol writer: the ayah network turned into numbered, evidence-carrying items.

Sections (ids in brackets are what the plan and harvest cite):
  1 [M]  HFT mechanisms — the surah-level arguments, with the hubs each touches
  2 [H]  backbone hubs — images that rare branches of ≥3 roots converge on by script evidence; members with their
         dictionary sense, source phrase and evidence (script edges, Luna's judged reading)
  3 [L]  Luna hubs — the same, made by Luna's readings only (second tier)
  4 [F]  the Fatiha — standing lens: links from the ayah's words and branches to each Fatiha ayah
  5 [T]  triangles — three nodes pairwise linked (the image confirms itself)
  5 [J]  bridges — nodes that touch two hubs (joins, Kapanış)
  6 [G]  word level — sound, rare form, frame links, and the precomputed word notes (grammar that changes meaning)
  7 [C]  context hubs — surah, people passages, Fatiha, inter-ayah ayat that several rare branches point to
  8 [P]  formula groups — other ayat repeating ≥2 focus roots (plain parallels; pick a representative)
  9      text of every cited ayah outside the surah and the Fatiha (the surah and Fatiha are in context.md)

Usage: python3 _commentary/v9/network/backbone.py 29:38 [--net network.k3-inter-luna.json]
"""
from __future__ import annotations

import argparse
import itertools
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

V9 = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from network import weight  # noqa: E402

QURAN = V9.parents[2] / "quran-data" / "data" / "text" / "quran-uthmani.tsv"
MAX_TRIANGLES = 15
MAX_BRIDGES = 15
FATIHA_PER_AYAH = 6
CONTEXT_HUBS_PER_ZONE = 3


def load_quran() -> dict[str, str]:
    out = {}
    for line in QURAN.read_text(encoding="utf-8-sig").splitlines():
        ref, _, ar = line.partition("|")
        out[ref.strip()] = ar.strip()
    return out


def clip(s: str, n: int) -> str:
    s = " ".join((s or "").split())
    return s if len(s) <= n else s[: n - 1] + "…"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ref")
    ap.add_argument("--net", default="network.k3-inter-luna.json")
    a = ap.parse_args()
    s_, a_ = a.ref.split(":")
    out_dir = V9 / "network" / "out" / f"{s_}_{a_}"
    pkg = V9 / "input" / "v2" / f"s{int(s_):03d}" / f"{s_}_{a_}"
    d = json.loads((out_dir / a.net).read_text(encoding="utf-8"))
    N, E = d["nodes"], d["edges"]
    adj = defaultdict(lambda: defaultdict(list))
    for e in E:
        adj[e["a"]][e["b"]].append(e)
        adj[e["b"]][e["a"]].append(e)
    quran = load_quran()
    cited = set()

    def fw(f):
        return f"{N[f]['surface']}"

    def plain_of(f):
        return "; ".join(f"{x['gloss']} ({x['image']})" for x in N.values() if x["type"] == "B" and x.get("plain")
                         and x["word"] == f) or "—"

    def evidence(b, h):
        parts = []
        for e in adj[b][h]:
            if e["kind"] == "luna":
                if weight(e) > 0:
                    parts.append(f"Luna ({e['sub'].split('/')[-1]}): {e['evidence'].split(': ', 1)[-1]}")
            elif weight(e) > 0:
                parts.append(f"{e['kind']}{'/' + e['sub'] if e['sub'] else ''}: {clip(e['evidence'], 150)}")
        return " || ".join(dict.fromkeys(parts)) or "image similarity only"

    def backing(b, h):
        """[dictionary]: a script edge (shared word, dictionary relation, sound, form) links b and h;
        [judged]: only Luna's reading does."""
        return "[dictionary]" if any(e["kind"] != "luna" and weight(e) > 0 for e in adj[b][h]) else "[judged]"

    def branch_line(b, full=False):
        x = N[b]
        flags = ("echo root, sound family only; " if x["root_kind"] == "echo" else "") + \
                (f"{x['n_sources']} dictionaries" + (", sole attestation" if x["sole"] else ""))
        return (f"{x['root']} {x['bid']} «{x['gloss']}» {x['image']} — word {fw(x['word'])} ({flags}); "
                f"source: {clip(x['src'], 450 if full else 220)}")

    ids_of = defaultdict(list)  # branch node → every id it appears under (cross-references)

    def also(b, own):
        other = [i for i in ids_of[b] if i != own]
        return f" (also {', '.join(other[:6])})" if other else ""

    def ctx_touch(members):
        touch = defaultdict(set)
        for b in members:
            for t, es in adj[b].items():
                if t.startswith("A:") and N[t]["zone"] == "surah" and any(weight(e) > 0 for e in es):
                    touch[N[t]["ref"]].add(f"{N[b]['root']} {N[b]['bid']}")
        return " → ".join(f"{r} ({', '.join(sorted(v))})" for r, v in sorted(touch.items(), key=lambda kv: int(kv[0].split(':')[1])))

    L = [f"# Backbone for {a.ref}", "",
         "Built by script from the ayah network (shared dictionary words, the dictionary's own relations, sound, form,",
         "frame, same people, formulas) and Luna's judged meaning links. Every item has an id; cite ids in the plan",
         "and harvest. Evidence strings are proposals with their Arabic: judge them, choose what carries a thread.", ""]

    # 1 HFT mechanisms
    hft_text = (pkg / "02_hft.md").read_text(encoding="utf-8")
    blocks = re.split(r"^## ", hft_text, flags=re.M)[1:]
    hubs = [(score, h, members, n) for score, h, members, n in d["hubs"]]
    shown = [x for x in hubs if N[x[1]]["type"] == "F"]
    ctx = defaultdict(list)
    for x in hubs:
        if N[x[1]]["type"] == "A":
            ctx[N[x[1]]["zone"]].append(x)
    hub_ids = {}
    for i, (_, h, _, _) in enumerate([x for x in shown if N[x[1]].get("tier") == "backbone"], 1):
        hub_ids[h] = f"H{i}"
    for i, (_, h, _, _) in enumerate([x for x in shown if N[x[1]].get("tier") != "backbone"], 1):
        hub_ids[h] = f"L{i}"
    hub_members = {}
    for score, h, members, n in shown:
        ms = [b for b in members if N[b]["word"] != h]
        ms.sort(key=lambda b: (backing(b, h) != "[dictionary]", N[b]["root"], N[b]["bid"]))
        hub_members[h] = ms
        for k, b in enumerate(ms, 1):
            ids_of[b].append(f"{hub_ids[h]}.{k}")
    tri_list, seen_b = [], set()
    for kinds, b, x, y in d["triangles"]:
        if b in seen_b or len(tri_list) >= MAX_TRIANGLES:
            continue
        xy = [e for e in adj[x].get(y, []) if weight(e) > 0 or e["kind"] in ("img",)]
        if xy:
            seen_b.add(b)
            tri_list.append((b, x, y, xy[0]))
            ids_of[b].append(f"T{len(tri_list)}")

    L += ["## 1. Surah-level arguments (HFT mechanisms) [M]", ""]
    m_i = 0
    for blk in blocks:
        name = blk.split(" [", 1)[0].strip()
        if name.startswith("HFT reader"):
            continue
        m_i += 1
        after = re.search(r"^- after: (.*)$", blk, re.M)
        mech = re.search(r"^- mechanism: (.*)$", blk, re.M)
        steps = re.findall(r"^  - (\S+) w[\d,]+ \*\*(.+?)\*\* \((\S+ \S+ \S+) (B\d+)", blk, re.M)
        mnode = f"M:{name}"
        touched = sorted({hub_ids[h] for h in hub_ids for t in adj.get(mnode, {})
                          if t == h or t in dict((m, 1) for x in hubs if x[1] == h for m in x[2])
                          or (N.get(t, {}).get("type") == "B" and N[t]["word"] == h)})
        L.append(f"- **M{m_i}** {name} — {after.group(1) if after else ''}")
        if mech:
            L.append(f"  - mechanism: {mech.group(1)}")
        L.append("  - words: " + "; ".join(f"{r} {sf} ({rt} {bid})" for r, sf, rt, bid in steps))
        for r, *_ in steps:
            cited.add(r)
        if touched:
            L.append(f"  - touches hubs: {', '.join(touched)}")
    L.append("")

    # 2/3 hubs
    for title, tier, prefix in (("## 2. Backbone hubs [H]", "backbone", "H"), ("## 3. Luna hubs (second tier) [L]", "luna", "L")):
        L += [title, ""]
        for score, h, members, n in shown:
            if (N[h].get("tier") == "backbone") != (tier == "backbone"):
                continue
            hid = hub_ids[h]
            L += [f"### {hid} {fw(h)} — {n} roots converge", f"Plain sense of {fw(h)}: {plain_of(h)}"]
            ms = hub_members[h]
            for k, b in enumerate(ms, 1):
                tag = backing(b, h)
                L.append(f"- **{hid}.{k}** {tag} {branch_line(b, full=tag == '[dictionary]')}{also(b, f'{hid}.{k}')}")
                L.append(f"  - evidence: {evidence(b, h)}")
            touch = ctx_touch(ms)
            if touch:
                L.append(f"- surah ayat these members touch (chain material): {touch}")
            L.append("")

    # 4 triangles
    # Fatiha: a standing lens for every ayah (recited in every prayer)
    L += ["## 4. The Fatiha [F] (standing lens: recited in every prayer)", ""]
    f_i = 0
    for i in range(1, 8):
        r = f"1:{i}"
        node = f"A:{r}"
        links = []
        for b_or_f, es in adj.get(node, {}).items():
            kind = N.get(b_or_f, {}).get("type")
            if kind == "B" and (N[b_or_f]["rare"] or any(e["kind"] in ("rel", "lex", "luna") for e in es)):
                strong_es = [e for e in es if weight(e) > 0]
                if strong_es or ids_of.get(b_or_f):
                    links.append((0 if strong_es else 1, b_or_f, strong_es or es))
            elif kind == "F":
                for e in es:
                    if e["kind"] in ("form", "frame"):
                        links.append((0, b_or_f, [e]))
        L.append(f"### {r} {quran.get(r, '')}")
        seen_lines = set()
        uniq = []
        for rank, n_, es in sorted(links, key=lambda t: (t[0], t[1])):
            key = (n_, tuple(sorted(e["evidence"] for e in es)))
            if key not in seen_lines:
                seen_lines.add(key)
                uniq.append((rank, n_, es))
        for _, n_, es in uniq[:FATIHA_PER_AYAH]:
            f_i += 1
            ev = " || ".join(dict.fromkeys(f"{e['kind']}{'/' + e['sub'] if e['sub'] else ''}: {clip(e['evidence'], 150)}"
                                           for e in es))
            if N[n_]["type"] == "B":
                ids_of[n_].append(f"F{f_i}")
                L.append(f"- **F{f_i}** {branch_line(n_)}{also(n_, f'F{f_i}')} — {ev}")
            else:
                L.append(f"- **F{f_i}** word {fw(n_)} — {ev}")
    L.append("")

    L += ["## 5. Triangles [T]", ""]
    t_i = 0
    for b, x, y, xy0 in tri_list:
        xy = [xy0]
        t_i += 1
        lab = lambda n_: fw(n_) if n_.startswith("F:") else f"{N[n_]['ref']} [{N[n_]['zone']}]"
        for n_ in (x, y):
            if n_.startswith("A:"):
                cited.add(N[n_]["ref"])
        L.append(f"- **T{t_i}** {branch_line(b)}{also(b, f'T{t_i}')}")
        L.append(f"  - → {lab(x)}: {evidence(b, x)}")
        L.append(f"  - → {lab(y)}: {evidence(b, y)}")
        L.append(f"  - {lab(x)} ↔ {lab(y)}: {xy[0]['kind']}{'/' + xy[0]['sub'] if xy[0]['sub'] else ''}: {clip(xy[0]['evidence'], 150)}")
    L.append("")

    # 5 bridges
    L += ["## 6. Bridges (touch two hubs) [J]", ""]
    members_of = {hub_ids[h]: {m for x in hubs if x[1] == h for m in x[2]} for h in hub_ids}
    cands = []
    for n_, x in N.items():  # bridges inside the ayah, the Fatiha and the surah; most-joining first
        if x["type"] not in "FA" or n_ in hub_ids or (x["type"] == "A" and x["zone"] not in ("surah", "fatiha")):
            continue
        touching = sorted(hid for hid, ms in members_of.items()
                          if any(weight(e) > 0 for m in ms for e in adj[m].get(n_, [])))
        if len(touching) >= 2:
            cands.append((-sum(t.startswith("H") for t in touching), -len(touching), n_, touching))
    j_i = 0
    for _, _, n_, touching in sorted(cands)[:MAX_BRIDGES]:
        x = N[n_]
        j_i += 1
        lab = fw(n_) if x["type"] == "F" else f"{x['ref']} [{x['zone']}]"
        if x["type"] == "A":
            cited.add(x["ref"])
        L.append(f"- **J{j_i}** {lab} joins {', '.join(touching)}")
    L.append("")

    # 6 word level
    L += ["## 7. Word level: sound, form, frame, grammar [G]", ""]
    g_i = 0
    for e in E:
        if e["kind"] in ("sound", "form", "frame") and e["a"].startswith("F:"):
            g_i += 1
            tgt = fw(e["b"]) if e["b"].startswith("F:") else N[e["b"]]["ref"]
            if e["b"].startswith("A:"):
                cited.add(N[e["b"]]["ref"])
            L.append(f"- **G{g_i}** {e['kind']}: {fw(e['a'])} ~ {tgt}: {e['evidence']}")
    notes = (pkg / "00_ayah.md").read_text(encoding="utf-8").split("## Word notes", 1)[-1]
    for line in notes.splitlines():
        if line.startswith("- "):
            g_i += 1
            L.append(f"- **G{g_i}** word note: {clip(line[2:], 300)}")
    L.append("")

    # 7 context hubs
    L += ["## 8. Context hubs [C]", ""]
    c_i = 0
    for zone in ("surah", "fatiha", "people", "inter"):
        for score, h, members, n in ctx.get(zone, [])[:CONTEXT_HUBS_PER_ZONE]:
            c_i += 1
            r = N[h]["ref"]
            cited.add(r)
            L.append(f"- **C{c_i}** {r} [{zone}] — {n} roots: {quran.get(r, '')}")
            for b in sorted(members, key=lambda b: (N[b]["root"], N[b]["bid"])):
                if any(weight(e) > 0 for e in adj[b][h]):
                    L.append(f"  - {N[b]['root']} {N[b]['bid']} «{N[b]['gloss']}» @ {fw(N[b]['word'])}: {evidence(b, h)}")
    L.append("")

    # 8 formula groups: other ayat repeating focus roots (same-root leaves), grouped by the words they repeat
    L += ["## 9. Formula groups: other ayat repeating the ayah's own roots [P] (pick representatives)", ""]
    groups = defaultdict(list)
    for e in E:
        if e["kind"] == "root" and e["b"].startswith("A:") and N[e["b"]]["zone"] in ("inter", "people"):
            groups[e["b"]].append(fw(e["a"]))
    by_sig = defaultdict(list)
    for t, ws in groups.items():
        if len(set(ws)) >= 2:
            by_sig[tuple(sorted(set(ws)))].append(N[t]["ref"])
    for p_i, (sig, refs) in enumerate(sorted(by_sig.items(), key=lambda kv: (-len(kv[0]), -len(kv[1])))[:12], 1):
        refs.sort(key=lambda r: tuple(map(int, r.split(":"))))
        cited.update(refs[:4])
        L.append(f"- **P{p_i}** {' + '.join(sig)} ({len(refs)} ayat): {', '.join(refs[:10])}")
    L.append("")

    # 9 texts
    L += ["## 10. Text of cited ayat outside the surah and the Fatiha", ""]
    for r in sorted({r for r in cited if not r.startswith((f"{s_}:", "1:")) and r in quran},
                    key=lambda r: tuple(map(int, r.split(":")))):
        L.append(f"- {r} {quran[r]}")
    sol = out_dir / "sol"
    sol.mkdir(exist_ok=True)
    (sol / "backbone.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"backbone: {m_i} mechanisms, {len(hub_ids)} focus hubs, {f_i} Fatiha links, {t_i} triangles, {j_i} bridges, {g_i} word items, "
          f"{c_i} context hubs → {sol / 'backbone.md'} ({len(chr(10).join(L).encode())} bytes)")


if __name__ == "__main__":
    main()
