#!/usr/bin/env python3
"""Where each surah stands in the v16 production pipeline (RUNBOOK.md), from the files on disk and the ledger.
No model calls, writes nothing.

  python3 -B _commentary/v16/status.py 87 100 103

A step counts as done only when its finished file exists and is complete (map: ## Chains and ## Ayat; images:
an image section, ## Buluşmalar and ledger.md). A run dir that started but has no finished file is BLOCKED (never
rerun; the user decides). A *.partial.* file is never counted as done. Readings and augments whose check.json has
findings are listed. "Spent" is every ledger row's cost for the surah, whatever its status, trials included.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import v16 as V  # noqa: E402
import packets as P  # noqa: E402

OUT = V.HERE / "out"
MAPS = ("surah.map3.nohft.tool", "surah.map3.nochannels.hftbundle.tool")
AUG = "augment.augment9.opus"


def ayat(s: int) -> list[int]:
    q = V.src().quran
    return [a for a in range(1, 300) if f"{s}:{a}" in q]


MAP_BRIEFS = ("map3.nohft.tool", "map3.nochannels.hftbundle.tool")  # exact: map3.nohft.tool.check2 was a trial
PRODUCTION = ("images.r13.", "r13.images.r13.", "augment9.opus.")  # prefixes


def ledger() -> tuple[dict[str, float], dict[str, list[str]], dict[str, int]]:
    """Cost by ref (every row with a cost, whatever its status), and the production calls (r13, augment9) whose
    latest row is not ok, by ref. A post-processing error or a check that failed or found something is listed too."""
    cost: dict[str, float] = {}
    last: dict[tuple, dict] = {}
    aug_issues: dict[str, int] = {}  # augment9: check findings inside the additions (the augment's own)
    for line in (OUT / "ledger.jsonl").read_text(encoding="utf-8").splitlines():
        d = json.loads(line)
        ref = str(d.get("ref"))
        cost[ref] = cost.get(ref, 0.0) + (d.get("cost_usd") or 0.0)
        b = str(d.get("brief", ""))
        if (b in MAP_BRIEFS or b.startswith(PRODUCTION)) and d.get("status") is not None:
            last[(ref, d.get("arm"), d.get("brief"))] = d
        if d.get("arm") == "augment-applied" and b.startswith("augment9.opus."):
            aug_issues[ref] = d.get("insert_issues", 0)
        if d.get("post_error"):
            last[(ref, d.get("arm"), d.get("brief"), "post")] = d
    bad: dict[str, list[str]] = {}
    for k, d in last.items():
        why = [f"status {d.get('status')}"] if d.get("status") not in ("ok", None) else []
        why += [f"post_error {d['post_error'][:120]}"] if d.get("post_error") else []
        if why:
            bad.setdefault(k[0], []).append(f"{d.get('arm')} {d.get('brief')}: {'; '.join(why)}")
    return cost, bad, aug_issues


def state(d: Path, done: Path, complete: bool = True) -> str:
    """done | incomplete | partial | BLOCKED | - for one run dir."""
    if done.exists():
        return "done" if complete else "incomplete"
    if any(d.glob("*.partial.*")):
        return "partial"
    if V.blocked(d):
        return "BLOCKED"
    return "-"


def findings(record: Path) -> str:
    if not record.exists():
        return "no check.json"
    n = {k: v for k, v in V.check_counts(record).items() if k != "sources_unchecked"}
    return ", ".join(f"{k} {v}" for k, v in n.items())


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("usage: status.py <surah> [<surah> …]")
    try:
        surahs = [int(x) for x in sys.argv[1:]]
    except ValueError:
        raise SystemExit(f"surahs are numbers: {' '.join(sys.argv[1:])}")
    cost, bad, aug_issues = ledger()
    for s in surahs:
        sd = OUT / f"s{s:03d}"
        mp = next((sd / m for m in MAPS if (sd / m).exists()), sd / MAPS[0])
        m_state = state(mp, mp / "map.md", V.map_complete(mp / "map.md"))
        im = sd / f"images.r13.{mp.name.removeprefix('surah.')}.tool"
        i_state = state(im, im / "images.md", P.images_complete(im / "images.md") and (im / "ledger.md").exists())
        rd = f"DM.r13.{im.name}.tool"
        n = ayat(s)
        rows = {}
        for a in n:
            d = OUT / f"{s}_{a}" / rd
            r = state(d, d / f"{s}_{a}.reading.tr.md", (d / "ledger.md").exists())
            ad = d / AUG
            g = state(ad, ad / f"{s}_{a}.reading.tr.md") if r == "done" else "-"
            rows[a] = (r, g)
        usd = cost.get(f"S{s}", 0.0) + sum(cost.get(f"{s}:{a}", 0.0) for a in n)
        print(f"S{s} ({len(n)} ayat): map {m_state} ({mp.name}) | images {i_state} | "
              f"readings {sum(r == 'done' for r, _ in rows.values())}/{len(n)} | "
              f"augment9 {sum(g == 'done' for _, g in rows.values())}/{len(n)} | spent ${usd:.2f}")
        for label, pick in (("readings", 0), ("augment9", 1)):
            for st in ("incomplete", "partial", "BLOCKED"):
                xs = [f"{s}:{a}" for a, v in rows.items() if v[pick] == st]
                if xs:
                    print(f"  {label} {st} (the user decides): {', '.join(xs)}")
        if i_state == "done":
            todo = [f"{s}:{a}" for a, (r, _) in rows.items() if r == "-"]
            if todo:
                print(f"  readings to run: {', '.join(todo)}")
        todo = [f"{s}:{a}" for a, (r, g) in rows.items() if r == "done" and g == "-"]
        if todo:
            print(f"  augment9 to run: {', '.join(todo)}")
        for a, (r, g) in rows.items():
            d = OUT / f"{s}_{a}" / rd
            f = findings(d / "check.json") if r == "done" else ""
            if f:
                print(f"  check findings, {s}:{a} reading: {f}")
            if g == "done" and aug_issues.get(f"{s}:{a}"):
                print(f"  check findings, {s}:{a} augment9 additions: {aug_issues[f'{s}:{a}']} (augment.augment9.opus/check.json)")
        if i_state == "done" and (im / "check.json").exists() and findings(im / "check.json"):
            print(f"  check findings, images: {findings(im / 'check.json')}")
        for ref in [f"S{s}"] + [f"{s}:{a}" for a in n]:
            for x in bad.get(ref, []):
                print(f"  ledger, {ref}: {x}")


if __name__ == "__main__":
    main()
