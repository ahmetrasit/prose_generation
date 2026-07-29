#!/usr/bin/env python3
"""Build commentary-bundle ablation variants from an existing bundle tree.

This script does not rebuild source data. It copies one generated bundle tree
and applies named, auditable removals for commentary experiments.
"""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

import build_bundle


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_BUNDLES = ROOT / "bundles"


def read_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def copy_surah_tree(source_root: Path, dest_root: Path, surah: int) -> Path:
    source_dir = source_root / f"s{surah:03d}"
    if not source_dir.is_dir():
        raise SystemExit(f"error: source bundle dir not found: {source_dir}")
    dest_dir = dest_root / f"s{surah:03d}"
    if dest_dir.exists():
        shutil.rmtree(dest_dir)
    dest_dir.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source_dir, dest_dir)
    return dest_dir


def replace_focus_inventory_with_surah_fallback(bundle: dict, surah: int, ayah: int) -> None:
    fallback, fallback_coverage = build_bundle._load_branch_inventories_fallback(
        surah,
        ayah,
        build_bundle.V12_TR_DIR / f"s{surah:03d}" / f"focus_{surah}_{ayah}",
        bundle.get("qac_morphemes", []),
        bundle.get("channel_subchannels_anchored_here", []),
    )
    bundle["branch_inventories"] = fallback
    bundle.setdefault("coverage", {})["branch_inventories"] = fallback_coverage


def remove_focus_responses(bundle: dict) -> None:
    bundle["v12_reader_responses"] = {}
    bundle.setdefault("coverage", {})["v12_reader_responses"] = {
        "present": False,
        "variants": {},
        "note": "ABLATION: per-ayah focus-run reader responses removed deliberately.",
    }


def remove_focus_trace(bundle: dict) -> None:
    bundle["v12_focus_trace_hermetic"] = {}
    bundle.setdefault("coverage", {})["v12_focus_trace_hermetic"] = {
        "present": False,
        "packet_present": False,
        "readers": {},
        "note": "ABLATION: Hermetic Focus Trace evidence removed deliberately.",
    }


def remove_reader_derived(bundle: dict) -> None:
    remove_focus_responses(bundle)
    remove_focus_trace(bundle)
    bundle["v12_reader_walks"] = {}
    bundle["v12_reader_walks_wide"] = {}
    bundle["v12_cross_run_publication"] = None
    bundle["butuncul_okuma_line"] = None
    bundle["channel_subchannels_anchored_here"] = []

    coverage = bundle.setdefault("coverage", {})
    coverage["v12_reader_walks"] = {
        "present": False,
        "readers": {},
        "note": "ABLATION: full-context reader walks removed deliberately.",
    }
    coverage["v12_reader_walks_wide"] = {
        "present": False,
        "readers": {},
        "note": "ABLATION: plus/minus-5 reader walks removed deliberately.",
    }
    coverage["v12_cross_run_publication"] = {
        "present": False,
        "source_file": None,
        "note": "ABLATION: cross-run publication findings removed deliberately.",
    }
    coverage["butuncul_okuma"] = {
        "present": False,
        "source_file": None,
        "note": "ABLATION: whole-surah Turkish reader synthesis removed deliberately.",
    }
    coverage["channel_review"] = {
        "present": False,
        "review_status": "ablated",
        "note": "ABLATION: first-pass reader channel review removed deliberately.",
    }


def mutate_bundle(bundle_path: Path, surah: int, ayah: int, mode: str) -> None:
    bundle = read_json(bundle_path)
    bundle.setdefault("ablation", {})
    bundle["ablation"].update({
        "mode": mode,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    })

    if mode == "no-focus":
        replace_focus_inventory_with_surah_fallback(bundle, surah, ayah)
        remove_focus_responses(bundle)
        remove_focus_trace(bundle)
        bundle["ablation"]["label"] = "no-per-ayah-focus-run-evidence"
        bundle["ablation"]["removed"] = [
            "focus-scoped stage_00 branch inventories",
            "v12_reader_responses",
            "v12_focus_trace_hermetic",
        ]
        bundle["ablation"]["replacement"] = "surah full_context_packet branch inventory scoped to the ayah"
    elif mode == "no-reader":
        replace_focus_inventory_with_surah_fallback(bundle, surah, ayah)
        remove_reader_derived(bundle)
        bundle["ablation"]["label"] = "no-reader-derived-evidence"
        bundle["ablation"]["removed"] = [
            "focus-scoped stage_00 branch inventories",
            "v12_reader_responses",
            "v12_focus_trace_hermetic",
            "v12_reader_walks",
            "v12_reader_walks_wide",
            "v12_cross_run_publication",
            "butuncul_okuma_line",
            "channel_subchannels_anchored_here",
        ]
        bundle["ablation"]["replacement"] = "surah full_context_packet branch inventory scoped to the ayah"
    else:
        raise SystemExit(f"error: unsupported mode: {mode}")

    write_json(bundle_path, bundle)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--surah", type=int, required=True)
    parser.add_argument("--ayah", type=int, required=True)
    parser.add_argument("--mode", choices=["no-focus", "no-reader"], required=True)
    parser.add_argument("--source-bundles", type=Path, default=DEFAULT_BUNDLES)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    dest_dir = copy_surah_tree(args.source_bundles, args.out, args.surah)
    target = dest_dir / f"{args.surah}_{args.ayah}.ayah.json"
    if not target.is_file():
        raise SystemExit(f"error: copied ayah bundle not found: {target}")
    mutate_bundle(target, args.surah, args.ayah, args.mode)
    print(f"wrote {args.mode} ablation bundle: {target}")


if __name__ == "__main__":
    main()
