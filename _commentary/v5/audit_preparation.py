#!/usr/bin/env python3
"""Run actual V5 preparation over saved inputs, without writing agent artifacts.

Checks every available canonical and package ayah. Package checks use their
declared span; S:0 checks use the entire host surah. --whole-surah additionally
checks each numbered canonical focus with its entire host as explicit context.
Detailed JSONL results include failures and actual prompt byte sizes.
"""

import argparse
from concurrent.futures import ProcessPoolExecutor
import json
from pathlib import Path
import re
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from _commentary.v5 import workflow


def check(task):
    path, mode, host_count = task
    path = Path(path)
    started = time.monotonic()
    try:
        s, a = map(int, path.name.removesuffix(".ayah.json").split("_"))
        ref = f"{s}:{a}"
        argv = ["prepare", "--ayah", ref, "--source-bundle", str(path), "--check-only"]
        if mode != "package":
            context_root = path.parent.parent if path.parent.name == f"s{s:03d}" else path.parent
            argv += ["--context-bundles-dir", str(context_root),
                     "--member-bundles-dir", str(context_root)]
        if mode == "package":
            bundle = json.loads(path.read_text(encoding="utf-8"))
            span = bundle["pericope"]
            argv += ["--context-bundles-dir", str(path.parent),
                     "--analysis-id", "inventory-package",
                     "--segment", f"package={s}:{span['ayah_from']}-{span['ayah_to']}"]
        elif mode == "whole_surah":
            argv += ["--analysis-id", "inventory-whole-surah", "--segment", f"host={s}:1-{host_count}"]
        args = workflow._parser().parse_args(argv)
        refs, composition = workflow._resolve_request(args)
        args.ayah, args.composition = refs[0], composition
        result = workflow.prepare(args)
        result.pop("word_alignment", None)  # migration report contains the full gap inventory
    except Exception as exc:
        result = {"status": "error", "error": f"{type(exc).__name__}: {exc}"}
    return {"path": str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path), "mode": mode,
            "seconds": round(time.monotonic() - started, 3), **result}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundles-dir", type=Path, default=ROOT / "bundles")
    parser.add_argument("--whole-surah", action="store_true")
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    if args.workers < 1:
        parser.error("--workers must be positive")
    defaults = workflow._parser().parse_args(["prepare", "--ayah", "1:1", "--check-only"])
    workflow._preflight_qac(defaults)
    quran, _ = workflow._quran_text_projection(defaults.quran_text)
    tasks = []
    for path in sorted(args.bundles_dir.resolve().rglob("*.ayah.json")):
        canonical = re.fullmatch(r"s\d{3}", path.parent.name) is not None
        tasks.append((str(path), "native" if canonical else "package", None))
        identity = re.fullmatch(r"([1-9][0-9]*)_([0-9]+)\.ayah\.json", path.name)
        if identity is None:
            continue  # check() records the malformed filename as an error
        s, a = map(int, identity.groups())
        if args.whole_surah and canonical and a and 1 <= s <= 114:
            tasks.append((str(path), "whole_surah", len(workflow._numbered_surah_refs(quran, s))))
    counts, largest = {}, {}
    with args.report.open("w", encoding="utf-8") as stream, ProcessPoolExecutor(max_workers=args.workers) as pool:
        for index, result in enumerate(pool.map(check, tasks, chunksize=1), 1):
            stream.write(json.dumps(result, ensure_ascii=False) + "\n")
            stream.flush()
            status = result["status"]
            counts[status] = counts.get(status, 0) + 1
            for lane, size in result.get("prompt_bytes", {}).items():
                if size > largest.get(lane, {}).get("bytes", 0):
                    largest[lane] = {"bytes": size, "path": result["path"], "mode": result["mode"]}
            if index % 50 == 0 or index == len(tasks):
                print(json.dumps({"completed": index, "total": len(tasks), "counts": counts}), flush=True)
    print(json.dumps({"counts": counts, "largest_prompts": largest}, ensure_ascii=False))
    return int(bool(counts.get("error")))


if __name__ == "__main__":
    raise SystemExit(main())
