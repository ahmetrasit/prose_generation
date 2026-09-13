#!/usr/bin/env python3
"""Build and publish surah readings sourced exclusively from final ayah editorials."""

from __future__ import annotations

import argparse
import fcntl
import importlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path
from typing import Any

from common import (
    REPO_ROOT, WORKFLOW_ROOT, atomic_write_text, content_hash, immutable_write_json,
    immutable_write_text, load_json, normalize_language, portable_path, sha256_text,
)

PACKET_SCHEMA = "surah-editorial-source-v1"
OUTLINE_SCHEMA = "surah-editorial-outline-v1"
COMPOSITION_SCHEMA = "surah-editorial-composition-v1"
STAGES = {
    "outline": ("10-editorial-outline.md", "editorial-outline-v1.schema.json"),
    "compose": ("11-editorial-compose.md", "editorial-composition-v1.schema.json"),
    "edit": ("12-editorial-edit.md", "editorial-composition-v1.schema.json"),
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"error: {message}")


def exact(value: Any, keys: set[str], context: str) -> None:
    require(isinstance(value, dict) and set(value) == keys, f"{context}: invalid fields")


def nonempty(value: Any, context: str) -> None:
    require(isinstance(value, str) and bool(value.strip()), f"{context}: expected nonempty text")


def objects(value: Any, context: str) -> None:
    require(isinstance(value, list) and all(isinstance(row, dict) for row in value),
            f"{context}: expected an array of objects")


def unique_anchor(anchor: Any, text: str, context: str) -> None:
    nonempty(anchor, context)
    require(len(anchor.split()) >= 6 and text.count(anchor) == 1,
            f"{context}: anchor must contain at least six words and occur exactly once")


def prose_errors(text: str, path: Path) -> list:
    sys.path.insert(0, str(REPO_ROOT))
    try:
        validator = importlib.import_module("_commentary.v5.validate_prose")
    finally:
        sys.path.pop(0)
    return validator.validate_text(text, path=path)


def packet_payload(packet: dict) -> dict:
    return {key: value for key, value in packet.items() if key not in {"packetHash", "runId"}}


def validate_packet(packet: dict) -> None:
    exact(packet, {"schemaVersion", "surah", "ayahCount", "language", "analysisId",
                   "completedBy", "editorials", "packetHash", "runId"}, "packet")
    require(packet["schemaVersion"] == PACKET_SCHEMA, "unsupported packet schema")
    require(type(packet["surah"]) is int and 1 <= packet["surah"] <= 114, "invalid surah")
    require(type(packet["ayahCount"]) is int and packet["ayahCount"] > 0, "invalid ayah count")
    require(packet["language"] == normalize_language(packet["language"]), "invalid language")
    nonempty(packet["analysisId"], "analysisId")
    nonempty(packet["completedBy"], "completedBy")
    objects(packet["editorials"], "editorials")
    expected = [f"{packet['surah']}:{ayah}" for ayah in range(1, packet["ayahCount"] + 1)]
    require([row.get("ayahRef") for row in packet["editorials"]] == expected,
            "editorials must cover every numbered ayah exactly once in order")
    for row in packet["editorials"]:
        exact(row, {"ayahRef", "sourcePath", "sha256", "text"}, "editorial")
        nonempty(row["sourcePath"], "sourcePath")
        nonempty(row["text"], row["ayahRef"])
        require(row["sha256"] == sha256_text(row["text"]), f"changed editorial: {row['ayahRef']}")
        errors = prose_errors(row["text"], Path(row["sourcePath"]))
        require(not errors, f"invalid editorial {row['ayahRef']}: {errors}")
    digest = content_hash(packet_payload(packet))
    require(packet["packetHash"] == digest, "packet hash mismatch")
    require(packet["runId"] == f"s{packet['surah']:03d}-{packet['language']}-editorial-{digest[:16]}",
            "run ID mismatch")


def build_packet(*, editorial_root: Path, analysis_id: str, surah: int,
                 ayah_count: int, language: str, completed_by: str) -> dict:
    require(bool(re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9._-]*", analysis_id)), "invalid analysis ID")
    require(type(surah) is int and 1 <= surah <= 114 and ayah_count > 0, "invalid surah/ayah count")
    language = normalize_language(language)
    nonempty(completed_by, "explicit completed-by attestation")
    directory = editorial_root / analysis_id / f"s{surah:03d}"
    require(directory.is_dir(), f"editorial directory missing: {directory}")
    numbered = {int(path.name.split("_")[1]) for path in directory.iterdir()
                if path.is_dir() and re.fullmatch(rf"{surah}_[1-9][0-9]*", path.name)}
    require(numbered == set(range(1, ayah_count + 1)),
            "editorial ayah directories do not match the declared complete surah")
    rows, paths = [], []
    for ayah in range(1, ayah_count + 1):
        key = f"{surah}_{ayah}"
        path = directory / key / f"{key}.prose.editorial.{language}.md"
        require(path.is_file(), f"completed editorial missing: {path}")
        text = path.read_bytes().decode("utf-8")
        rows.append({"ayahRef": f"{surah}:{ayah}", "sourcePath": portable_path(path),
                     "sha256": sha256_text(text), "text": text})
        paths.append(path)
    packet = {"schemaVersion": PACKET_SCHEMA, "surah": surah, "ayahCount": ayah_count,
              "language": language, "analysisId": analysis_id, "completedBy": completed_by,
              "editorials": rows}
    packet["packetHash"] = content_hash(packet)
    packet["runId"] = f"s{surah:03d}-{language}-editorial-{packet['packetHash'][:16]}"
    validate_packet(packet)
    require(all(sha256_text(path.read_bytes().decode("utf-8")) == row["sha256"]
                for path, row in zip(paths, rows)),
            "editorial changed during snapshot; wait for completion and rebuild")
    return packet


def run_dir(packet: dict) -> Path:
    return WORKFLOW_ROOT / "runs" / "editorial-v1" / f"s{packet['surah']:03d}" / packet["language"] / packet["runId"]


def source_texts(packet: dict) -> dict[str, str]:
    return {row["ayahRef"]: row["text"] for row in packet["editorials"]}


def validate_outline(outline: dict, packet: dict) -> None:
    exact(outline, {"schemaVersion", "packetHash", "primaryArc", "movements", "ayahCoverage", "friction"}, "outline")
    require(outline["schemaVersion"] == OUTLINE_SCHEMA, "unsupported outline schema")
    require(outline["packetHash"] == packet["packetHash"], "outline source lineage mismatch")
    texts = source_texts(packet)
    exact(outline["primaryArc"], {"text", "evidence"}, "primaryArc")
    nonempty(outline["primaryArc"]["text"], "primaryArc.text")
    objects(outline["primaryArc"]["evidence"], "primaryArc.evidence")
    require(bool(outline["primaryArc"]["evidence"]), "primary arc needs editorial evidence")
    for row in outline["primaryArc"]["evidence"]:
        exact(row, {"ayahRef", "anchor"}, "primary evidence")
        require(row["ayahRef"] in texts, "unknown primary evidence ayah")
        unique_anchor(row["anchor"], texts[row["ayahRef"]], "primary evidence")
    objects(outline["movements"], "movements")
    ids = []
    memberships: dict[str, set[str]] = {ref: set() for ref in texts}
    for movement in outline["movements"]:
        exact(movement, {"id", "title", "contribution", "members"}, "movement")
        require(isinstance(movement["id"], str) and bool(re.fullmatch(r"[a-z][a-z0-9-]*", movement["id"])), "invalid movement ID")
        ids.append(movement["id"])
        nonempty(movement["title"], "movement title")
        nonempty(movement["contribution"], "movement contribution")
        objects(movement["members"], "members")
        refs = []
        for member in movement["members"]:
            exact(member, {"ayahRef", "image", "contribution", "qualification", "anchors"}, "member")
            ref = member["ayahRef"]
            require(ref in texts, "unknown member ayah")
            refs.append(ref)
            memberships[ref].add(movement["id"])
            for field in ("image", "contribution", "qualification"):
                nonempty(member[field], f"member {field}")
            require(isinstance(member["anchors"], list) and bool(member["anchors"]), "member needs source anchors")
            for anchor in member["anchors"]:
                unique_anchor(anchor, texts[ref], f"source member {ref}")
        require(len(refs) >= 2 and len(refs) == len(set(refs)), "each movement needs at least two distinct member ayahs")
    require(len(ids) == len(set(ids)), "duplicate movement IDs")
    objects(outline["ayahCoverage"], "ayahCoverage")
    require([row.get("ayahRef") for row in outline["ayahCoverage"]] == list(texts),
            "outline must account for every ayah in order")
    for row in outline["ayahCoverage"]:
        exact(row, {"ayahRef", "movementIds", "note"}, "ayah coverage")
        require(isinstance(row["movementIds"], list) and all(isinstance(x, str) for x in row["movementIds"]), "invalid coverage IDs")
        require(set(row["movementIds"]) == memberships[row["ayahRef"]] and
                len(row["movementIds"]) == len(set(row["movementIds"])), "coverage/member mismatch")
        nonempty(row["note"], "coverage note")
    require(isinstance(outline["friction"], list) and all(isinstance(x, str) and x.strip() for x in outline["friction"]), "invalid friction")


def validate_composition(composition: dict, packet: dict, outline: dict, *, phase: str | None = None) -> None:
    exact(composition, {"schemaVersion", "packetHash", "outlineHash", "phase", "prelude", "postlude",
                        "primaryLanding", "landings", "friction"}, "composition")
    require(composition["schemaVersion"] == COMPOSITION_SCHEMA, "unsupported composition schema")
    require(composition["packetHash"] == packet["packetHash"] and composition["outlineHash"] == content_hash(outline), "composition lineage mismatch")
    require(composition["phase"] in ("draft", "editorial"), "invalid phase")
    require(phase is None or composition["phase"] == phase, f"expected {phase} composition")
    for surface in ("prelude", "postlude"):
        nonempty(composition[surface], surface)
        require(not re.search(r"\b(?:packetHash|outlineHash|movementIds|schemaVersion|Layer [23])\b", composition[surface]),
                f"workflow metadata in {surface}")
    require(composition["prelude"].strip() != composition["postlude"].strip(),
            "prelude and postlude must serve distinct reader moments")
    unique_anchor(composition["primaryLanding"], composition["postlude"], "primary landing")
    objects(composition["landings"], "landings")
    require([r.get("movementId") for r in composition["landings"]] == [m["id"] for m in outline["movements"]],
            "composition must land every outline movement in order")
    for movement, row in zip(outline["movements"], composition["landings"]):
        exact(row, {"movementId", "preludeAnchor", "postludeAnchor", "members"}, "landing")
        unique_anchor(row["preludeAnchor"], composition["prelude"], "prelude promise")
        unique_anchor(row["postludeAnchor"], composition["postlude"], "postlude movement")
        objects(row["members"], "landing members")
        require([m.get("ayahRef") for m in row["members"]] == [m["ayahRef"] for m in movement["members"]], "missing composition member")
        for member in row["members"]:
            exact(member, {"ayahRef", "anchor"}, "member landing")
            unique_anchor(member["anchor"], composition["postlude"], "member landing")
    require(isinstance(composition["friction"], list) and all(isinstance(x, str) and x.strip() for x in composition["friction"]), "invalid friction")


def assemble(stage: str, packet: dict, *, outline: dict | None = None,
             draft: dict | None = None, output: Path) -> str:
    validate_packet(packet)
    context: dict[str, Any] = {"packetHash": packet["packetHash"], "surah": packet["surah"],
                               "language": packet["language"],
                               "editorials": [{"ayahRef": row["ayahRef"], "text": row["text"]}
                                              for row in packet["editorials"]]}
    if stage != "outline":
        require(outline is not None, "outline required")
        validate_outline(outline, packet)
        context.update(outline=outline, outlineHash=content_hash(outline))
    if stage == "edit":
        require(draft is not None, "draft required")
        validate_composition(draft, packet, outline)
        context["draft"] = draft
    prompt_name, schema_name = STAGES[stage]
    prompt = (WORKFLOW_ROOT / "prompts" / prompt_name).read_text(encoding="utf-8")
    schema = load_json(WORKFLOW_ROOT / "schemas" / schema_name)
    return (prompt + f"\nWrite only `{output}`.\n\n## Output Schema\n```json\n" +
            json.dumps(schema, ensure_ascii=False) + "\n```\n\n## Editorial Input\n```json\n" +
            json.dumps(context, ensure_ascii=False) + "\n```\n")


def publication_files(packet: dict, outline: dict, composition: dict, approved_by: str) -> dict[str, str]:
    nonempty(approved_by, "semantic approval identity")
    validate_packet(packet)
    validate_outline(outline, packet)
    validate_composition(composition, packet, outline, phase="editorial")
    prefix = f"{packet['surah']}.surah-reading"
    language = packet["language"]
    prelude, postlude = (composition[key].rstrip() + "\n" for key in ("prelude", "postlude"))
    evidence = {"schemaVersion": "surah-editorial-publication-v1", "runId": packet["runId"],
                "packetHash": packet["packetHash"], "outlineHash": content_hash(outline),
                "compositionHash": content_hash(composition), "approvedBy": approved_by,
                "surfaceHashes": {"prelude": sha256_text(prelude), "postlude": sha256_text(postlude)},
                "sources": [{key: value for key, value in row.items() if key != "text"} for row in packet["editorials"]],
                "primaryArc": outline["primaryArc"], "movements": outline["movements"],
                "primaryLanding": composition["primaryLanding"], "landings": composition["landings"]}
    friction = list(dict.fromkeys(outline["friction"] + composition["friction"]))
    return {
        f"{prefix}.prelude.{language}.md": prelude,
        f"{prefix}.postlude.{language}.md": postlude,
        f"{prefix}.friction.{language}.md": "# Publication Friction\n\n" +
            ("\n".join(f"- {item}" for item in friction) if friction else "No unresolved friction reported.") + "\n",
        f"{prefix}.evidence.{language}.json": json.dumps(evidence, ensure_ascii=False, indent=2) + "\n",
    }


def write_immutable_set(directory: Path, files: dict[str, str]) -> None:
    for name, text in files.items():
        target = directory / name
        require(not target.exists() or target.read_text(encoding="utf-8") == text,
                f"immutable publication already differs: {target}")
    for name, text in files.items():
        immutable_write_text(directory / name, text)


def replace_stable(directory: Path, files: dict[str, str], history: Path) -> None:
    """Serialize publishers, preserve the old set, and commit evidence last."""
    directory.mkdir(parents=True, exist_ok=True)
    history.mkdir(parents=True, exist_ok=True)
    with (history / ".publish.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        previous = {name: (directory / name).read_text(encoding="utf-8")
                    for name in files if (directory / name).exists()}
        if previous == files:
            return
        if previous:
            write_immutable_set(history / content_hash(previous), previous)
        temporary: dict[str, Path] = {}
        replaced = []
        try:
            for name, text in files.items():
                with tempfile.NamedTemporaryFile(dir=directory, mode="w", encoding="utf-8", delete=False) as handle:
                    temporary[name] = Path(handle.name)
                    handle.write(text)
                    handle.flush()
                    os.fsync(handle.fileno())
            for name in files:
                os.replace(temporary[name], directory / name)
                replaced.append(name)
        except BaseException:
            for name in reversed(replaced):
                if name in previous:
                    with tempfile.NamedTemporaryFile(dir=directory, mode="w", encoding="utf-8", delete=False) as handle:
                        handle.write(previous[name])
                        restore = Path(handle.name)
                    os.replace(restore, directory / name)
                else:
                    (directory / name).unlink(missing_ok=True)
            raise
        finally:
            for path in temporary.values():
                path.unlink(missing_ok=True)


def publish(packet: dict, outline: dict, composition: dict, *, approved_by: str,
            stable: bool = False) -> Path:
    files = publication_files(packet, outline, composition, approved_by)
    revision = content_hash(files)
    directory = run_dir(packet) / "published" / revision
    accepted = run_dir(packet) / "accepted" / revision
    write_immutable_set(accepted, {
        "source-packet.json": json.dumps(packet, ensure_ascii=False, indent=2) + "\n",
        "outline.json": json.dumps(outline, ensure_ascii=False, indent=2) + "\n",
        "composition.json": json.dumps(composition, ensure_ascii=False, indent=2) + "\n",
    })
    write_immutable_set(directory, files)
    if stable:
        replace_stable(WORKFLOW_ROOT / "outputs" / f"s{packet['surah']:03d}", files,
                       WORKFLOW_ROOT / "publication-history" / f"s{packet['surah']:03d}" / packet["language"])
    return directory


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    build = commands.add_parser("build")
    build.add_argument("--editorial-root", type=Path, default=REPO_ROOT / "_commentary/v5/editorial")
    build.add_argument("--analysis-id", required=True)
    build.add_argument("--surah", required=True, type=int)
    build.add_argument("--ayah-count", required=True, type=int)
    build.add_argument("--language", default="tr")
    build.add_argument("--completed-by", required=True)
    for command in ("instantiate", "validate", "publish"):
        sub = commands.add_parser(command)
        sub.add_argument("--packet", required=True, type=Path)
        sub.add_argument("--outline", type=Path)
        sub.add_argument("--composition", type=Path)
        if command == "instantiate":
            sub.add_argument("stage", choices=STAGES)
        elif command == "validate":
            sub.add_argument("--phase", choices=("draft", "editorial"))
        elif command == "publish":
            sub.add_argument("--approved-by", required=True)
            sub.add_argument("--publish-stable", action="store_true")
    args = parser.parse_args()
    if args.command == "build":
        packet = build_packet(editorial_root=args.editorial_root.resolve(), analysis_id=args.analysis_id,
                              surah=args.surah, ayah_count=args.ayah_count, language=args.language,
                              completed_by=args.completed_by)
        path = run_dir(packet) / "source-packet.json"
        immutable_write_json(path, packet)
        print(path)
        return 0
    packet = load_json(args.packet)
    validate_packet(packet)
    outline = load_json(args.outline) if args.outline else None
    composition = load_json(args.composition) if args.composition else None
    if outline is not None:
        validate_outline(outline, packet)
    if composition is not None:
        require(outline is not None, "--composition requires --outline")
        validate_composition(composition, packet, outline,
                             phase=args.phase if args.command == "validate" else None)
    if args.command == "validate" and args.phase:
        require(composition is not None, "--phase requires --composition")
    if args.command == "validate":
        print("ok")
    elif args.command == "instantiate":
        output = run_dir(packet) / "outputs" / f"{args.stage}.json"
        path = run_dir(packet) / "inputs" / f"{args.stage}.prompt.md"
        atomic_write_text(
            path,
            assemble(
                args.stage,
                packet,
                outline=outline,
                draft=composition,
                output=output,
            ),
        )
        print(path)
        print(output)
    else:
        require(outline is not None and composition is not None, "publication requires --outline and --composition")
        print(publish(packet, outline, composition, approved_by=args.approved_by, stable=args.publish_stable))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
