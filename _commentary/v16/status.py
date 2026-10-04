#!/usr/bin/env python3
"""Where each surah stands in the v16 production pipeline (RUNBOOK.md), from the files on disk and the ledger.
No model calls, writes nothing.

  python3 -B _commentary/v16/status.py 87 100 103
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import v16 as V  # noqa: E402

OUT = V.HERE / "out"
MAPS = ("surah.map3.nohft.tool", "surah.map3.nochannels.hftbundle.tool")
AUG = "augment.augment8.opus"


def ayat(s: int) -> list[int]:
    q = V.src().quran
    return [a for a in range(1, 300) if f"{s}:{a}" in q]


def costs() -> dict[tuple[str, str], float]:
    """(ref, arm) -> USD of the ok calls."""
    out: dict[tuple[str, str], float] = {}
    for line in (OUT / "ledger.jsonl").read_text(encoding="utf-8").splitlines():
        d = json.loads(line)
        if d.get("status") == "ok" and d.get("cost_usd"):
            k = (d["ref"], d["arm"])
            out[k] = out.get(k, 0.0) + d["cost_usd"]
    return out


def main() -> None:
    c = costs()
    for s in map(int, sys.argv[1:]):
        sd = OUT / f"s{s:03d}"
        mp = next((sd / m for m in MAPS if (sd / m / "map.md").exists()), None)
        im = sd / f"images.r13.{mp.name.removeprefix('surah.')}.tool" if mp else None
        im_ok = bool(im and (im / "images.md").exists())
        rd = f"DM.r13.{im.name}.tool" if im else ""
        n = ayat(s)
        reads = [a for a in n if (OUT / f"{s}_{a}" / rd / f"{s}_{a}.reading.tr.md").exists()]
        augs = [a for a in n if (OUT / f"{s}_{a}" / rd / AUG / f"{s}_{a}.reading.tr.md").exists()]
        started = [a for a in n if (OUT / f"{s}_{a}" / rd / AUG / "started.json").exists() and a not in augs]
        ref = f"S{s}"
        usd = (c.get((ref, "surah"), 0) + c.get((ref, "images"), 0)
               + sum(c.get((f"{s}:{a}", "DM"), 0) + c.get((f"{s}:{a}", "augment"), 0) for a in n))
        print(f"S{s} ({len(n)} ayat): map {mp.name if mp else '-'} | images {'r13' if im_ok else '-'} | "
              f"readings {len(reads)}/{len(n)} | augment8 {len(augs)}/{len(n)}"
              + (f" (started, no output: {', '.join(f'{s}:{a}' for a in started)})" if started else "")
              + f" | spent ${usd:.2f}")
        todo = [f"{s}:{a}" for a in n if a in reads and a not in augs and a not in started]
        if todo:
            print(f"  augment to run: {', '.join(todo)}")
        missing = [f"{s}:{a}" for a in n if a not in reads]
        if im_ok and missing:
            print(f"  readings to run: {', '.join(missing)}")


if __name__ == "__main__":
    main()
