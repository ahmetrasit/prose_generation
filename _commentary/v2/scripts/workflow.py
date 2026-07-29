#!/usr/bin/env python3
"""Instantiate hermetic prompts for the Commentary v2 workflow.

The script does not call a model. Each command writes prompt and manifest files
for one workflow stage.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Iterable

from validate import (
    load_json,
    sha256_path,
    validate_ledger_data,
    validate_plan_data,
    validate_registry_data,
    validate_run_config_data,
)

V2_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = V2_ROOT.parent.parent
SCHEMAS = V2_ROOT / "shared" / "schemas"
CONTRACT = V2_ROOT / "shared" / "EDITORIAL_CONTRACT.md"


@dataclass(frozen=True)
class Source:
    label: str
    kind: str
    text: str
    bytes: int
    sha256: str
    source_file_bytes: int | None = None
    source_file_sha256: str | None = None

    def manifest_row(self) -> dict[str, Any]:
        row: dict[str, Any] = {
            "path": self.label,
            "kind": self.kind,
            "bytes": self.bytes,
            "sha256": self.sha256,
        }
        if self.source_file_bytes is not None:
            row["sourceFileBytes"] = self.source_file_bytes
        if self.source_file_sha256 is not None:
            row["sourceFileSha256"] = self.source_file_sha256
        return row


def digest_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def relative_label(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return str(path.resolve())


def resolve_path(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else REPO_ROOT / path


def read_source(path: Path, kind: str, compact_json: bool = False) -> Source:
    if not path.is_file():
        raise SystemExit(f"error: required source does not exist: {path}")
    raw = path.read_text(encoding="utf-8")
    if not raw.strip():
        raise SystemExit(f"error: required source is present but empty: {path}")
    text = raw
    if compact_json:
        try:
            data = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"error: invalid JSON source {path}: {exc}") from exc
        text = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    return Source(
        label=relative_label(path),
        kind=kind,
        text=text,
        bytes=len(text.encode("utf-8")),
        sha256=digest_text(text),
        source_file_bytes=len(raw.encode("utf-8")) if text != raw else None,
        source_file_sha256=digest_text(raw) if text != raw else None,
    )


def virtual_source(label: str, kind: str, data: dict[str, Any]) -> Source:
    text = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    return Source(
        label=label,
        kind=kind,
        text=text,
        bytes=len(text.encode("utf-8")),
        sha256=digest_text(text),
    )


def load_config(path: Path) -> dict[str, Any]:
    try:
        data = load_json(path)
    except ValueError as exc:
        raise SystemExit(f"error: {exc}") from exc
    errors = validate_run_config_data(data)
    if errors:
        details = "\n".join(f"  {error}" for error in errors)
        raise SystemExit(f"error: invalid run configuration:\n{details}")
    return data


def output_root(config: dict[str, Any]) -> Path:
    configured = config.get("outputRoot")
    if configured:
        return resolve_path(configured)
    return V2_ROOT / "generated" / config["runId"]


def all_ayahs(config: dict[str, Any]) -> list[int]:
    return sorted(
        {
            ayah
            for pericope in config["pericopes"]
            for ayah in pericope["ayahs"]
        }
    )


def find_pericope(config: dict[str, Any], pericope_id: str) -> dict[str, Any]:
    for pericope in config["pericopes"]:
        if pericope["id"] == pericope_id:
            return pericope
    available = ", ".join(item["id"] for item in config["pericopes"])
    raise SystemExit(
        f"error: unknown pericope {pericope_id!r}; available: {available}"
    )


def ayah_ref(config: dict[str, Any], ayah: int) -> str:
    return f"{config['surah']}:{ayah}"


def unit_id(config: dict[str, Any], ayah: int) -> str:
    return f"{config['surah']}_{ayah}"


def ayah_source_paths(config: dict[str, Any], ayah: int) -> list[Path]:
    ref = ayah_ref(config, ayah)
    explicit = config.get("ayahSources", {}).get(ref)
    if explicit:
        return [resolve_path(item) for item in explicit]
    pattern = config.get("defaultAyahSourcePattern")
    if not pattern:
        raise SystemExit(f"error: no source configured for {ref}")
    value = pattern.format(
        surah=config["surah"],
        surah_padded=f"{config['surah']:03d}",
        ayah=ayah,
        ayah_ref=ref,
    )
    return [resolve_path(value)]


def governing_sources(config: dict[str, Any]) -> list[Source]:
    return [
        read_source(resolve_path(path), "governing")
        for path in config.get("governingSources", [])
    ]


def stage_paths(root: Path, stage: str) -> tuple[Path, Path]:
    if stage == "discovery":
        base = root / "layer_2" / "discovery"
    elif stage == "compiler":
        base = root / "shared" / "compiler"
    elif stage == "reconciler":
        base = root / "shared" / "reconciler"
    elif stage == "layer2":
        base = root / "layer_2" / "editorial"
    elif stage == "layer3":
        base = root / "layer_3"
    else:
        raise ValueError(f"unknown stage {stage}")
    return base / "inputs", base / "outputs"


def ledger_path(root: Path, config: dict[str, Any], ayah: int) -> Path:
    return (
        stage_paths(root, "discovery")[1]
        / f"{unit_id(config, ayah)}.ledger.json"
    )


def plan_path(root: Path, pericope_id: str) -> Path:
    return (
        stage_paths(root, "compiler")[1]
        / f"{pericope_id}.editorial-plan.json"
    )


def registry_path(root: Path, pericope_id: str) -> Path:
    return (
        stage_paths(root, "compiler")[1]
        / f"{pericope_id}.channel-registry.json"
    )


def reconciled_registry_path(root: Path) -> Path:
    return stage_paths(root, "reconciler")[1] / "whole-surah.channel-registry.json"


def read_and_validate_ledger(path: Path) -> dict[str, Any]:
    try:
        data = load_json(path)
    except ValueError as exc:
        raise SystemExit(f"error: {exc}") from exc
    errors = validate_ledger_data(data)
    if errors:
        details = "\n".join(f"  {error}" for error in errors)
        raise SystemExit(f"error: invalid discovery ledger {path}:\n{details}")
    return data


def pericope_ledgers(
    root: Path, config: dict[str, Any], pericope: dict[str, Any]
) -> tuple[list[dict[str, Any]], list[Path]]:
    paths = [ledger_path(root, config, ayah) for ayah in pericope["ayahs"]]
    missing = [path for path in paths if not path.is_file()]
    if missing:
        details = "\n".join(f"  {path}" for path in missing)
        raise SystemExit(f"error: missing discovery ledgers:\n{details}")
    return [read_and_validate_ledger(path) for path in paths], paths


def run_ledgers(
    root: Path, config: dict[str, Any]
) -> tuple[list[dict[str, Any]], list[Path]]:
    ayahs = all_ayahs(config)
    paths = [ledger_path(root, config, ayah) for ayah in ayahs]
    missing = [path for path in paths if not path.is_file()]
    if missing:
        details = "\n".join(f"  {path}" for path in missing)
        raise SystemExit(f"error: missing discovery ledgers:\n{details}")
    return [read_and_validate_ledger(path) for path in paths], paths


def fence_for(source: Source) -> str:
    if source.kind in {
        "schema",
        "ayah-source",
        "discovery-ledger",
        "compiler-input",
        "editorial-plan-slice",
        "channel-registry",
    }:
        return "json"
    return "markdown"


def render_prompt(
    *,
    config: dict[str, Any],
    stage: str,
    unit: str,
    run_date: str,
    sources: list[Source],
    expected_outputs: list[Path],
) -> tuple[str, dict[str, Any]]:
    lines = [
        "# Instantiated Commentary v2 Prompt",
        "",
        f"- run: `{config['runId']}`",
        f"- stage: `{stage}`",
        f"- unit: `{unit}`",
        f"- surah: {config['surah']}",
        f"- target language: `{config['language']}`",
        f"- generated: `{run_date}`",
        "- expected outputs:",
    ]
    for path in expected_outputs:
        lines.append(f"  - `{relative_label(path)}`")
    lines.extend(["- inlined sources:"])
    for source in sources:
        lines.append(
            f"  - `{source.label}` - {source.bytes:,} bytes - `{source.sha256}`"
        )
    lines.extend(
        [
            "",
            "**Hermeticity rule:** use only the material inlined below. Source "
            "paths are provenance identities, not instructions to browse.",
            "",
            "**Response rule:** write exactly the expected output files. Do not "
            "add an unrequested artifact or place one artifact inside another.",
            "",
            "---",
            "",
        ]
    )
    for source in sources:
        fence = fence_for(source)
        lines.extend(
            [
                f"## {source.kind}: `{source.label}`",
                "",
                f"```{fence}",
                source.text.rstrip("\n"),
                "```",
                "",
                "---",
                "",
            ]
        )
    manifest = {
        "schemaVersion": "commentary-v2-prompt-manifest-v1",
        "runId": config["runId"],
        "stage": stage,
        "unit": unit,
        "surah": config["surah"],
        "language": config["language"],
        "generated": run_date,
        "expectedOutputs": [relative_label(path) for path in expected_outputs],
        "sources": [source.manifest_row() for source in sources],
    }
    return "\n".join(lines).rstrip() + "\n", manifest


def write_prompt(
    input_dir: Path,
    stem: str,
    prompt: str,
    manifest: dict[str, Any],
) -> tuple[Path, Path]:
    input_dir.mkdir(parents=True, exist_ok=True)
    prompt_path = input_dir / f"{stem}.prompt.md"
    manifest_path = input_dir / f"{stem}.manifest.json"
    prompt_path.write_text(prompt, encoding="utf-8")
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return prompt_path, manifest_path


def base_sources(task: Path, schemas: Iterable[Path]) -> list[Source]:
    return [
        read_source(task, "task"),
        read_source(CONTRACT, "editorial-contract"),
        *(read_source(path, "schema") for path in schemas),
    ]


def instantiate_discovery(
    config: dict[str, Any],
    selected_ayah: int | None,
    run_date: str,
) -> list[Path]:
    root = output_root(config)
    input_dir, output_dir = stage_paths(root, "discovery")
    ayahs = [selected_ayah] if selected_ayah is not None else all_ayahs(config)
    unknown = [ayah for ayah in ayahs if ayah not in all_ayahs(config)]
    if unknown:
        raise SystemExit(f"error: ayah(s) outside configured pericopes: {unknown}")
    written: list[Path] = []
    fixed = base_sources(
        V2_ROOT / "layer_2" / "discovery" / "PROMPT.md",
        [SCHEMAS / "layer2-discovery-ledger.schema.json"],
    )
    fixed += governing_sources(config)
    for ayah in ayahs:
        unit = unit_id(config, ayah)
        ayah_sources = [
            read_source(path, "ayah-source", compact_json=path.suffix == ".json")
            for path in ayah_source_paths(config, ayah)
        ]
        expected = [
            output_dir / f"{unit}.ledger.json",
            output_dir / f"{unit}.memo.md",
            output_dir / f"{unit}.friction.md",
        ]
        prompt, manifest = render_prompt(
            config=config,
            stage="layer2-discovery",
            unit=unit,
            run_date=run_date,
            sources=fixed + ayah_sources,
            expected_outputs=expected,
        )
        prompt_path, manifest_path = write_prompt(input_dir, unit, prompt, manifest)
        written.extend([prompt_path, manifest_path])
    return written


def compiler_descriptor(
    config: dict[str, Any],
    pericope: dict[str, Any],
    paths: list[Path],
) -> dict[str, Any]:
    return {
        "schemaVersion": "commentary-v2-compiler-input-v1",
        "surah": config["surah"],
        "pericopeId": pericope["id"],
        "ayahRefs": [ayah_ref(config, ayah) for ayah in pericope["ayahs"]],
        "sourceLedgers": [
            {
                "ayahRef": ayah_ref(config, ayah),
                "sha256": sha256_path(path),
            }
            for ayah, path in zip(pericope["ayahs"], paths)
        ],
    }


def instantiate_compiler(
    config: dict[str, Any],
    pericope_id: str,
    run_date: str,
    include_memos: bool,
) -> list[Path]:
    root = output_root(config)
    pericope = find_pericope(config, pericope_id)
    ledgers, paths = pericope_ledgers(root, config, pericope)
    input_dir, output_dir = stage_paths(root, "compiler")
    descriptor = compiler_descriptor(config, pericope, paths)
    fixed = base_sources(
        V2_ROOT / "shared" / "compiler" / "PROMPT.md",
        [
            SCHEMAS / "pericope-editorial-plan.schema.json",
            SCHEMAS / "channel-registry.schema.json",
        ],
    )
    inputs = [
        virtual_source(
            f"{config['runId']}/{pericope_id}.compiler-input.json",
            "compiler-input",
            descriptor,
        )
    ]
    for path, ledger in zip(paths, ledgers):
        inputs.append(
            virtual_source(relative_label(path), "discovery-ledger", ledger)
        )
    if include_memos:
        memo_paths = [
            stage_paths(root, "discovery")[1]
            / f"{unit_id(config, ayah)}.memo.md"
            for ayah in pericope["ayahs"]
        ]
        missing = [path for path in memo_paths if not path.is_file()]
        if missing:
            raise SystemExit(
                "error: --include-memos requested but memo files are missing:\n  "
                + "\n  ".join(str(path) for path in missing)
            )
        inputs.extend(read_source(path, "discovery-memo") for path in memo_paths)
    expected = [
        output_dir / f"{pericope_id}.editorial-plan.json",
        output_dir / f"{pericope_id}.channel-registry.json",
        output_dir / f"{pericope_id}.friction.md",
    ]
    prompt, manifest = render_prompt(
        config=config,
        stage="pericope-compiler",
        unit=pericope_id,
        run_date=run_date,
        sources=fixed + inputs,
        expected_outputs=expected,
    )
    return list(write_prompt(input_dir, pericope_id, prompt, manifest))


def load_valid_plan(
    root: Path,
    config: dict[str, Any],
    pericope: dict[str, Any],
    ledgers: list[dict[str, Any]],
) -> tuple[dict[str, Any], Path]:
    path = plan_path(root, pericope["id"])
    try:
        data = load_json(path)
    except ValueError as exc:
        raise SystemExit(f"error: {exc}") from exc
    errors = validate_plan_data(data, ledgers)
    if errors:
        details = "\n".join(f"  {error}" for error in errors)
        raise SystemExit(f"error: invalid editorial plan {path}:\n{details}")
    expected_refs = {ayah_ref(config, ayah) for ayah in pericope["ayahs"]}
    if data.get("surah") != config["surah"]:
        raise SystemExit(f"error: editorial plan {path} belongs to another surah")
    if data.get("pericopeId") != pericope["id"]:
        raise SystemExit(f"error: editorial plan {path} names another pericope")
    if set(data.get("ayahRefs", [])) != expected_refs:
        raise SystemExit(f"error: editorial plan {path} has the wrong ayah set")
    return data, path


def verify_declared_ledger_hashes(
    artifact: dict[str, Any],
    ledgers: list[dict[str, Any]],
    paths: list[Path],
    label: str,
) -> None:
    actual = {
        ledger["ayahRef"]: sha256_path(path)
        for ledger, path in zip(ledgers, paths)
    }
    declared = {
        item.get("ayahRef"): item.get("sha256")
        for item in artifact.get("sourceLedgers", [])
        if isinstance(item, dict)
    }
    if declared != actual:
        raise SystemExit(
            f"error: {label} sourceLedgers do not match current discovery ledgers"
        )


def ayah_plan_slice(
    config: dict[str, Any],
    pericope: dict[str, Any],
    plan: dict[str, Any],
    plan_file: Path,
    ledger_file: Path,
    ayah: int,
) -> dict[str, Any]:
    ref = ayah_ref(config, ayah)
    ayah_plan = next(
        item for item in plan["ayahPlans"] if item.get("ayahRef") == ref
    )
    return {
        "schemaVersion": "commentary-v2-ayah-editorial-plan-slice-v1",
        "surah": config["surah"],
        "pericopeId": pericope["id"],
        "ayahRef": ref,
        "sourceLedgerSha256": sha256_path(ledger_file),
        "sourcePlanSha256": sha256_path(plan_file),
        "ayahPlan": ayah_plan,
        "findingCoverage": [
            item
            for item in plan["findingCoverage"]
            if item.get("sourceAyahRef") == ref
        ],
        "editorialSyntheses": [
            item
            for item in plan["editorialSyntheses"]
            if item.get("ownerAyahRef") == ref
        ],
    }


def instantiate_layer2(
    config: dict[str, Any],
    pericope_id: str,
    selected_ayah: int | None,
    run_date: str,
) -> list[Path]:
    root = output_root(config)
    pericope = find_pericope(config, pericope_id)
    ledgers, ledger_paths = pericope_ledgers(root, config, pericope)
    plan, plan_file = load_valid_plan(root, config, pericope, ledgers)
    verify_declared_ledger_hashes(plan, ledgers, ledger_paths, "editorial plan")
    input_dir, output_dir = stage_paths(root, "layer2")
    ayahs = [selected_ayah] if selected_ayah is not None else pericope["ayahs"]
    if any(ayah not in pericope["ayahs"] for ayah in ayahs):
        raise SystemExit("error: selected ayah is outside the requested pericope")
    fixed = base_sources(
        V2_ROOT / "layer_2" / "editorial" / "PROMPT.md",
        [SCHEMAS / "layer2-editorial-result.schema.json"],
    )
    fixed += governing_sources(config)
    ledger_by_ayah = {
        int(ledger["ayahRef"].split(":")[1]): (ledger, path)
        for ledger, path in zip(ledgers, ledger_paths)
    }
    written: list[Path] = []
    for ayah in ayahs:
        ledger, ledger_file = ledger_by_ayah[ayah]
        plan_slice = ayah_plan_slice(
            config, pericope, plan, plan_file, ledger_file, ayah
        )
        unit = unit_id(config, ayah)
        expected = [
            output_dir / f"{unit}.prose.md",
            output_dir / f"{unit}.evidence.md",
            output_dir / f"{unit}.index.md",
            output_dir / f"{unit}.result.json",
            output_dir / f"{unit}.friction.md",
        ]
        inputs = [
            virtual_source(
                relative_label(ledger_file), "discovery-ledger", ledger
            ),
            virtual_source(
                f"{config['runId']}/{pericope_id}/{unit}.plan-slice.json",
                "editorial-plan-slice",
                plan_slice,
            ),
        ]
        prompt, manifest = render_prompt(
            config=config,
            stage="layer2-editorial",
            unit=unit,
            run_date=run_date,
            sources=fixed + inputs,
            expected_outputs=expected,
        )
        written.extend(write_prompt(input_dir, unit, prompt, manifest))
    return written


def load_valid_registry(
    root: Path,
    config: dict[str, Any],
    pericope: dict[str, Any],
    ledgers: list[dict[str, Any]],
    plan_file: Path,
) -> tuple[dict[str, Any], Path]:
    path = registry_path(root, pericope["id"])
    try:
        data = load_json(path)
    except ValueError as exc:
        raise SystemExit(f"error: {exc}") from exc
    errors = validate_registry_data(data, ledgers, plan_file)
    if errors:
        details = "\n".join(f"  {error}" for error in errors)
        raise SystemExit(f"error: invalid channel registry {path}:\n{details}")
    if data.get("surah") != config["surah"]:
        raise SystemExit(f"error: channel registry {path} belongs to another surah")
    if data.get("pericopeId") != pericope["id"]:
        raise SystemExit(f"error: channel registry {path} names another pericope")
    return data, path


def pericope_registries(
    root: Path,
    config: dict[str, Any],
) -> list[tuple[dict[str, Any], Path]]:
    result: list[tuple[dict[str, Any], Path]] = []
    for pericope in config["pericopes"]:
        ledgers, ledger_paths = pericope_ledgers(root, config, pericope)
        _, plan_file = load_valid_plan(root, config, pericope, ledgers)
        registry, registry_file = load_valid_registry(
            root, config, pericope, ledgers, plan_file
        )
        verify_declared_ledger_hashes(
            registry, ledgers, ledger_paths, f"registry {pericope['id']}"
        )
        result.append((registry, registry_file))
    return result


def instantiate_reconciler(
    config: dict[str, Any],
    run_date: str,
) -> list[Path]:
    root = output_root(config)
    registries = pericope_registries(root, config)
    ledgers, ledger_paths = run_ledgers(root, config)
    input_dir, output_dir = stage_paths(root, "reconciler")
    descriptor = {
        "schemaVersion": "commentary-v2-reconciler-input-v1",
        "surah": config["surah"],
        "sourceRegistries": [
            {
                "pericopeId": registry["pericopeId"],
                "sha256": sha256_path(path),
            }
            for registry, path in registries
        ],
        "sourceLedgers": [
            {
                "ayahRef": ledger["ayahRef"],
                "sha256": sha256_path(path),
            }
            for ledger, path in zip(ledgers, ledger_paths)
        ],
    }
    fixed = base_sources(
        V2_ROOT / "shared" / "reconciler" / "PROMPT.md",
        [
            SCHEMAS / "channel-registry.schema.json",
            SCHEMAS / "registry-reconciliation.schema.json",
        ],
    )
    inputs = [
        virtual_source(
            f"{config['runId']}/whole-surah.reconciler-input.json",
            "compiler-input",
            descriptor,
        ),
        *[
            virtual_source(relative_label(path), "channel-registry", registry)
            for registry, path in registries
        ],
    ]
    expected = [
        output_dir / "whole-surah.channel-registry.json",
        output_dir / "whole-surah.registry-coverage.json",
        output_dir / "whole-surah.registry-friction.md",
    ]
    prompt, manifest = render_prompt(
        config=config,
        stage="surah-registry-reconciliation",
        unit="whole-surah",
        run_date=run_date,
        sources=fixed + inputs,
        expected_outputs=expected,
    )
    return list(write_prompt(input_dir, "whole-surah", prompt, manifest))


def write_layer3_prompt(
    *,
    config: dict[str, Any],
    root: Path,
    unit: str,
    registry: dict[str, Any],
    registry_file: Path,
    ayahs: list[int],
    run_date: str,
    include_layer2_prose: bool,
) -> list[Path]:
    input_dir, output_dir = stage_paths(root, "layer3")
    fixed = base_sources(
        V2_ROOT / "layer_3" / "PROMPT.md",
        [SCHEMAS / "layer3-result.schema.json"],
    )
    fixed += governing_sources(config)
    inputs = [
        virtual_source(
            f"{config['runId']}/{unit}.layer3-input.json",
            "compiler-input",
            {
                "schemaVersion": "commentary-v2-layer3-input-v1",
                "surah": config["surah"],
                "pericopeId": unit,
                "sourceRegistrySha256": sha256_path(registry_file),
            },
        ),
        virtual_source(
            relative_label(registry_file), "channel-registry", registry
        ),
    ]
    if include_layer2_prose:
        editorial_output = stage_paths(root, "layer2")[1]
        prose_paths = [
            editorial_output / f"{unit_id(config, ayah)}.prose.md"
            for ayah in ayahs
        ]
        missing = [path for path in prose_paths if not path.is_file()]
        if missing:
            raise SystemExit(
                "error: --include-layer2-prose requested but prose files are missing:\n  "
                + "\n  ".join(str(path) for path in missing)
            )
        inputs.extend(read_source(path, "layer2-edited-prose") for path in prose_paths)
    stem = f"{unit}.channels"
    expected = [
        output_dir / f"{stem}.prose.md",
        output_dir / f"{stem}.evidence.md",
        output_dir / f"{stem}.result.json",
        output_dir / f"{stem}.friction.md",
    ]
    prompt, manifest = render_prompt(
        config=config,
        stage="layer3-channel-authoring",
        unit=unit,
        run_date=run_date,
        sources=fixed + inputs,
        expected_outputs=expected,
    )
    return list(write_prompt(input_dir, stem, prompt, manifest))


def instantiate_layer3(
    config: dict[str, Any],
    pericope_id: str,
    run_date: str,
    include_layer2_prose: bool,
) -> list[Path]:
    root = output_root(config)
    pericope = find_pericope(config, pericope_id)
    ledgers, ledger_paths = pericope_ledgers(root, config, pericope)
    _, plan_file = load_valid_plan(root, config, pericope, ledgers)
    registry, registry_file = load_valid_registry(
        root, config, pericope, ledgers, plan_file
    )
    verify_declared_ledger_hashes(
        registry, ledgers, ledger_paths, "channel registry"
    )
    return write_layer3_prompt(
        config=config,
        root=root,
        unit=pericope_id,
        registry=registry,
        registry_file=registry_file,
        ayahs=pericope["ayahs"],
        run_date=run_date,
        include_layer2_prose=include_layer2_prose,
    )


def instantiate_layer3_surah(
    config: dict[str, Any],
    run_date: str,
    include_layer2_prose: bool,
) -> list[Path]:
    root = output_root(config)
    ledgers, ledger_paths = run_ledgers(root, config)
    registry_file = reconciled_registry_path(root)
    try:
        registry = load_json(registry_file)
    except ValueError as exc:
        raise SystemExit(f"error: {exc}") from exc
    errors = validate_registry_data(
        registry,
        ledgers,
        plan_path=None,
        ledger_paths=ledger_paths,
    )
    if errors:
        details = "\n".join(f"  {error}" for error in errors)
        raise SystemExit(
            f"error: invalid reconciled channel registry {registry_file}:\n{details}"
        )
    if registry.get("pericopeId") != "whole-surah":
        raise SystemExit(
            "error: reconciled registry pericopeId must be 'whole-surah'"
        )
    verify_declared_ledger_hashes(
        registry, ledgers, ledger_paths, "reconciled channel registry"
    )
    return write_layer3_prompt(
        config=config,
        root=root,
        unit="whole-surah",
        registry=registry,
        registry_file=registry_file,
        ayahs=all_ayahs(config),
        run_date=run_date,
        include_layer2_prose=include_layer2_prose,
    )


def status(config: dict[str, Any]) -> None:
    root = output_root(config)
    print(f"run: {config['runId']}")
    print(f"root: {root}")
    for pericope in config["pericopes"]:
        print(f"pericope {pericope['id']}:")
        for ayah in pericope["ayahs"]:
            unit = unit_id(config, ayah)
            discovery = ledger_path(root, config, ayah)
            editorial = stage_paths(root, "layer2")[1] / f"{unit}.result.json"
            print(
                f"  {ayah_ref(config, ayah)} "
                f"discovery={'yes' if discovery.is_file() else 'no'} "
                f"edited={'yes' if editorial.is_file() else 'no'}"
            )
        plan = plan_path(root, pericope["id"])
        registry = registry_path(root, pericope["id"])
        layer3 = (
            stage_paths(root, "layer3")[1]
            / f"{pericope['id']}.channels.result.json"
        )
        print(
            "  shared "
            f"plan={'yes' if plan.is_file() else 'no'} "
            f"registry={'yes' if registry.is_file() else 'no'} "
            f"layer3={'yes' if layer3.is_file() else 'no'}"
        )
    reconciled = reconciled_registry_path(root)
    surah_layer3 = (
        stage_paths(root, "layer3")[1] / "whole-surah.channels.result.json"
    )
    print(
        "surah scope: "
        f"registry={'yes' if reconciled.is_file() else 'no'} "
        f"layer3={'yes' if surah_layer3.is_file() else 'no'}"
    )


def report_written(paths: Iterable[Path]) -> None:
    for path in paths:
        print(relative_label(path))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    def common(subparser: argparse.ArgumentParser) -> None:
        subparser.add_argument("--config", type=Path, required=True)
        subparser.add_argument("--date", default=date.today().isoformat())

    discovery = subparsers.add_parser("discovery")
    common(discovery)
    discovery.add_argument("--ayah", type=int)

    compiler = subparsers.add_parser("compile")
    common(compiler)
    compiler.add_argument("--pericope", required=True)
    compiler.add_argument(
        "--include-memos",
        action="store_true",
        help="inline optional discovery memos in addition to compact ledgers",
    )

    layer2 = subparsers.add_parser("author-layer2")
    common(layer2)
    layer2.add_argument("--pericope", required=True)
    layer2.add_argument("--ayah", type=int)

    reconciler = subparsers.add_parser("reconcile")
    common(reconciler)

    layer3 = subparsers.add_parser("author-layer3")
    common(layer3)
    layer3_scope = layer3.add_mutually_exclusive_group(required=True)
    layer3_scope.add_argument("--pericope")
    layer3_scope.add_argument("--surah-scope", action="store_true")
    layer3.add_argument(
        "--include-layer2-prose",
        action="store_true",
        help="inline final Layer 2 prose; registry-only is the token-efficient default",
    )

    status_parser = subparsers.add_parser("status")
    status_parser.add_argument("--config", type=Path, required=True)

    args = parser.parse_args()
    config = load_config(args.config)
    if args.command == "discovery":
        report_written(instantiate_discovery(config, args.ayah, args.date))
    elif args.command == "compile":
        report_written(
            instantiate_compiler(
                config,
                args.pericope,
                args.date,
                args.include_memos,
            )
        )
    elif args.command == "author-layer2":
        report_written(
            instantiate_layer2(
                config,
                args.pericope,
                args.ayah,
                args.date,
            )
        )
    elif args.command == "reconcile":
        report_written(instantiate_reconciler(config, args.date))
    elif args.command == "author-layer3":
        if args.surah_scope:
            report_written(
                instantiate_layer3_surah(
                    config,
                    args.date,
                    args.include_layer2_prose,
                )
            )
        else:
            report_written(
                instantiate_layer3(
                    config,
                    args.pericope,
                    args.date,
                    args.include_layer2_prose,
                )
            )
    else:
        status(config)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
