#!/usr/bin/env python3
"""Fixed scorecard and map-use diff for v16 readings (REVIEW_r7_r10.md, step 0). Mechanical, no model call.

Diagnostics, not targets: the user's criterion is deeper supported understanding. Probes are read as probes.

  python3 -B _commentary/v16/scorecard.py out/1_6/DM.r8 out/1_6/DM.r10 [--map out/s001/surah.r2/map.md]
  python3 -B _commentary/v16/scorecard.py out/1_6/DM.r10 --diff     # map-use diff for the reading's ayah
"""
import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TAG = re.compile(r"\{ar:([^,}]*)")
# Probes: named cases the user watches. Read, never tuned for; a brief must never name them.
PROBES = {
    "1:5": {"Iblis refusal (7:11-12, 2:34, 38:74-76)": r"\b(?:7:1[12]|2:34|38:7[4-6])\b|[İI]bl[iî]s"},
    "1:6": {"well/pulley": r"القامة|البكرة|makara", "well water": r"يستقى|ملك أمر|kuyu", "7:16": r"\b7:16\b"},
    "1:7": {"crossbeam": r"النعامة|kalas|kiriş"},
}


def reading(d: Path) -> tuple[str, str]:
    p = next(d.glob("*.reading.tr.md"))
    ref = p.name.split(".")[0].replace("_", ":")
    return p.read_text(encoding="utf-8"), ref


def card(d: Path) -> dict:
    t, ref = reading(d)
    surah = ref.split(":")[0]
    chk = json.loads((d / "check.json").read_text()) if (d / "check.json").exists() else {}
    s = chk.get("summary", {})
    words = s.get("words") or len(t.split())
    paras = [p for p in t.split("\n\n") if p.strip() and not p.lstrip().startswith("#")]
    sents = re.split(r"(?<=[.!?])\s+", t)
    refs = sorted({r for r in re.findall(r"\((\d+:\d+)", t) + re.findall(r"; (\d+:\d+)", t)
                   if r.split(":")[0] != surah}, key=lambda r: tuple(map(int, r.split(":"))))
    latin = [m for m in TAG.findall(t) if re.search(r"[A-Za-z]", m)]
    led = (d / "ledger.md").read_text(encoding="utf-8") if (d / "ledger.md").exists() else ""
    return {
        "run": f"{d.parent.name}/{d.name}", "words": words, "sections": len(re.findall(r"(?m)^## ", t)),
        "paragraphs": len(paras), "paras_3plus_tags": sum(1 for p in paras if len(TAG.findall(p)) >= 3),
        "tags": s.get("tags", len(TAG.findall(t))), "sourced": s.get("share_sourced"),
        "dict_tags_per_1k": round(1000 * s.get("by_source", {}).get("dictionary", 0) / words, 1),
        "aile_openings": sum(1 for x in sents if re.match(r"\s*Aile(?:nin|de|yi)?\b", x)),
        "sozluk": len(re.findall(r"[Ss]özlük", t)), "denir": len(re.findall(r"\bdenir\b", t)),
        "refs_outside_surah": len(refs), "arabic_outside_tags": s.get("arabic_outside_tags"),
        "latin_in_ar": len(latin), "unsourced": s.get("unsourced_unmarked"),
        "ledger_not_written": led.count("- not written"),
        "probes": {k: bool(re.search(v, t)) for k, v in PROBES.get(ref, {}).items()},
        "refs": refs,
    }


def parse_map(m: str) -> list[dict]:
    body = re.search(r"(?ms)^## Chains\n(.*?)^## ", m).group(1)
    chains = []
    for block in re.split(r"(?m)^### ", body)[1:]:
        title = block.splitlines()[0].strip()
        members, passages, inq = [], [], False
        for line in block.splitlines()[1:]:
            if line.strip().lower().startswith("quran"):
                inq = True
                continue
            if not line.startswith("- "):
                continue
            if inq:
                m2 = re.match(r"- (\d+:\d+)(?:[–-](\d+))?", line)
                if m2:
                    passages.append(m2.group(1))
                continue
            parts = line[2:].split(" · ")
            if len(parts) < 2:
                continue
            rb = re.match(r"(.+?) (B\d{3})", parts[1])
            if rb:
                members.append({"refs": re.findall(r"\b1:\d+\b", parts[0]) or ["same"], "root": rb.group(1).strip(),
                                "branch": rb.group(2), "line": line[:90]})
        prev = None  # "same" inherits the previous member's refs
        for mb in members:
            if mb["refs"] == ["same"] and prev:
                mb["refs"] = prev
            prev = mb["refs"]
        chains.append({"title": title, "members": members, "passages": passages})
    return chains


def diff(d: Path, map_path: Path) -> str:
    t, ref = reading(d)
    chk = json.loads((d / "check.json").read_text())
    cited = {(c["root"], c["branch"]) for c in chk.get("cited_branches", [])}
    out = [f"# Map use: {d.parent.name}/{d.name} against {map_path.relative_to(HERE)}", ""]
    for c in parse_map(map_path.read_text(encoding="utf-8")):
        own = [m for m in c["members"] if ref in m["refs"]]
        if not own:
            continue
        used = lambda m: (m["root"], m["branch"]) in cited  # noqa: E731
        out.append(f"## {c['title']}")
        for m in own:
            out.append(f"- {'USED' if used(m) else 'not used'}: this ayah {m['root']} {m['branch']}")
        others = [m for m in c["members"] if ref not in m["refs"]]
        if others:
            out.append(f"- other ayat's members quoted: {sum(map(used, others))}/{len(others)}")
        for p in c["passages"]:
            out.append(f"- passage {p}: {'USED' if re.search(rf'\b{re.escape(p)}\b', t) else 'not used'}")
        out.append("")
    return "\n".join(out)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("dirs", nargs="+", type=Path)
    ap.add_argument("--map", type=Path, default=HERE / "out" / "s001" / "surah.r2" / "map.md")
    ap.add_argument("--diff", action="store_true")
    a = ap.parse_args()
    dirs = [x if x.is_absolute() else (Path.cwd() / x) for x in a.dirs]
    dirs = [x if x.exists() else HERE / x for x in a.dirs]
    if a.diff:
        for d in dirs:
            print(diff(d, a.map if a.map.is_absolute() else HERE / a.map))
        return
    cols = ["run", "words", "sections", "paras_3plus_tags", "paragraphs", "tags", "sourced", "dict_tags_per_1k",
            "aile_openings", "sozluk", "denir", "refs_outside_surah", "arabic_outside_tags", "latin_in_ar",
            "unsourced", "ledger_not_written", "probes"]
    print("| " + " | ".join(cols) + " |")
    print("|" + "---|" * len(cols))
    for d in dirs:
        c = card(d)
        c["probes"] = ", ".join(f"{k}:{'Y' if v else '-'}" for k, v in c["probes"].items())
        print("| " + " | ".join(str(c[k]) for k in cols) + " |")


if __name__ == "__main__":
    sys.exit(main())
