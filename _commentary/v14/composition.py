"""Isolated synthesis -> prose experiment over an existing frozen evidence arm. No model client."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import shutil

import experiment as EX
import sources as SRC
import synthesis as S

PHASES = ("synth", "write")
FIELDS = {"schema", "ref", "explanation", "reader_change", "source_items", "branches",
          "quran_refs", "concordance_roots", "limits"}


def read(path):
    return json.loads(path.read_text())


def new(path, value):
    text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    with path.open("x", encoding="utf-8") as handle:
        handle.write(text)


def now():
    return datetime.now(timezone.utc).isoformat()


def branches(out):
    result, root = {}, None
    for line in (out / "inputs/dictionary.md").read_text().splitlines():
        header = re.match(r"### (.+?) —", line)
        if header:
            root = header[1]
        match = re.match(r"- (B\d+) (.+)", line)
        if root and match:
            result[f"{root} {match[1]}"] = f"- {root} {match[1]} {match[2]}"
    for line in (out / "inputs/branches.md").read_text().splitlines():
        match = re.match(r"- (.+? B\d+) (.+)", line)
        if match:
            result.setdefault(match[1], line)
    return result


def concordances(out):
    result = {}
    for block in re.split(r"(?m)(?=^## )", (out / "inputs/concordance.md").read_text()):
        match = re.match(r"## (.+?) —", block)
        if match:
            result[match[1]] = block.strip()
    return result


def research(data, keys=None):
    """Put annotations beside their finding; retain every chosen record exactly once."""
    keys = set(data["items"]) if keys is None else set(keys)
    lines, seen = [], set()
    for key, item in data["items"].items():
        if key not in keys or key in seen:
            continue
        lines.append(f"[{key}] {item['text']}")
        seen.add(key)
        annotation = "E_" + key
        if annotation in keys and annotation not in seen:
            lines.append(f"[{annotation}] {data['items'][annotation]['text']}")
            seen.add(annotation)
        lines.append("")
    return "\n".join(lines)


def assemble(files):
    return "\n\n".join(f"===== {name} =====\n{text.strip()}" for name, text in files) + "\n"


def access(arm, ref, phase):
    command = f"python3 -B {EX.ROOT / 'composition.py'} lookup {ref} --tag {arm.name.removeprefix('out-')} --phase {phase}"
    return ("# Frozen source access\n\nUse only the following helper for additional evidence. No model call is made.\n\n"
            f"    {command} --kind quran --keys S:A,S:A --context 1\n\n"
            f"    {command} --kind items --keys F1,E_F1\n\n"
            f"    {command} --kind branches --keys 'SPACED_ROOT Bnnn,SPACED_ROOT Bnnn'\n\n"
            f"    {command} --kind concordance --keys 'SPACED_ROOT'\n\n"
            "Replace the placeholder keys with actual references. Request 1–16 keys; Quran context is 0–3 ayat "
            "per side. Each response is logged. A branch returns its exact frozen line; a concordance root returns "
            "its supplied section, whose scope may be limited. Missing evidence remains missing. "
            "Do not read other files or the whole Quran corpus.\n")


def verify(arm, ref):
    manifest = EX.verify(arm)
    if manifest.get("protocol") != "composition-1" or manifest.get("refs") != [ref]:
        raise ValueError("Not a matching composition experiment")
    for path, digest in manifest["code"].items():
        if S.sha(Path(path)) != digest:
            raise ValueError("Experiment code changed: " + path)
    out = EX.ayah_dir(arm, ref)
    for phase in PHASES:
        receipt_path = out / f"{phase}.input.json"
        if receipt_path.exists():
            receipt = read(receipt_path)
            if (S.sha(out / f"{phase}.input.md") != receipt["sha256"] or
                    S.sha(arm / "experiment.json") != receipt["experiment_sha256"]):
                raise ValueError("Prepared input changed: " + phase)
            if phase == "write" and S.sha(out / "composition.json") != receipt["composition_sha256"]:
                raise ValueError("Composition changed")
    return manifest


def prepare(arm, source, ref):
    if EX.archived(arm) or arm.exists() or source.resolve().parent != EX.ROOT.resolve():
        raise ValueError("Choose a new arm and a frozen source inside v14")
    original = EX.verify(source)
    if ref not in original["refs"] or original.get("source_mode") != "lookup":
        raise ValueError("Source needs this ayah and a frozen Quran corpus")
    src, dest = EX.ayah_dir(source, ref), EX.ayah_dir(arm, ref)
    rel = src.relative_to(source)
    names = ["act.md", "qeq.md", "synthesis.json", "inputs/ayah.md", "inputs/window_text.md",
             "inputs/dictionary.md", "inputs/branches.md", "inputs/concordance.md", "inputs/variants.md"]
    copies = {str(rel / name): src / name for name in names}
    copies["inputs/quran.tsv"] = source / "inputs/quran.tsv"
    for key, path in copies.items():
        if key not in original["files"] or S.sha(path) != original["files"][key]:
            raise ValueError("Source file was not frozen: " + key)
    prompts = {"inputs/compose.md": EX.ROOT / "prompts/compose.md",
               "inputs/write_composition.md": EX.ROOT / "prompts/write_composition.md"}
    for path in prompts.values():
        if not path.is_file():
            raise ValueError("Missing prompt: " + str(path))
    arm.mkdir()
    hashes, origins = {}, {}
    for key, path in {**copies, **prompts}.items():
        target = arm / key
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        hashes[key], origins[key] = S.sha(target), str(path)
    data = read(dest / "synthesis.json")
    archive = dest / "research.md"
    new(archive, "# Candidate research, not a prose worklist\n\n" + research(data))
    hashes[str(archive.relative_to(arm))] = S.sha(archive)
    origins[str(archive.relative_to(arm))] = "Frozen records; annotations placed beside their finding"
    manifest = {"schema": 1, "protocol": "composition-1", "writer_contract": 4, "source_mode": "lookup",
                "source_arm": source.name, "source_manifest_sha256": S.sha(source / "experiment.json"),
                "refs": [ref], "files": hashes, "origins": origins, "quran_source": original["quran_source"],
                "code": {str(path): S.sha(path) for path in [Path(__file__).resolve(),
                         Path(EX.__file__).resolve(), Path(SRC.__file__).resolve(), Path(S.__file__).resolve()]},
                "previous_prose": [], "network_groups": len(data["groups"]),
                "research_items": len(data["items"]), "copied_source_files": list(copies)}
    files = [("compose.md", (arm / "inputs/compose.md").read_text())]
    for name in ["ayah.md", "window_text.md"]:
        files.append((name, (dest / "inputs" / name).read_text()))
    files.append(("research.md", archive.read_text()))
    for name in ["dictionary.md", "branches.md", "concordance.md", "variants.md"]:
        files.append((name, (dest / "inputs" / name).read_text()))
    files.append(("source_access.md", access(arm, ref, "synth")))
    new(dest / "synth.input.md", assemble(files))
    manifest["files"][str((dest / "synth.input.md").relative_to(arm))] = S.sha(dest / "synth.input.md")
    new(arm / "experiment.json", manifest)
    new(dest / "synth.input.json", {"sha256": S.sha(dest / "synth.input.md"),
        "bytes": (dest / "synth.input.md").stat().st_size, "experiment_sha256": S.sha(arm / "experiment.json")})
    return manifest


def check_composition(out, value):
    data = read(out / "synthesis.json")
    if not isinstance(value, dict) or set(value) != FIELDS or value["schema"] != 1 or value["ref"] != data["ref"]:
        raise ValueError("Composition schema/fields/reference do not match")
    for name in ["explanation", "reader_change"]:
        if not isinstance(value[name], str) or not value[name].strip():
            raise ValueError("Missing composed explanation: " + name)
    for name in FIELDS - {"schema", "ref", "explanation", "reader_change"}:
        if not isinstance(value[name], list) or any(not isinstance(x, str) or not x.strip() for x in value[name]):
            raise ValueError("Expected strings: " + name)
        if len(set(value[name])) != len(value[name]):
            raise ValueError("Duplicate source/limit: " + name)
    choices = {"source_items": data["items"], "branches": branches(out),
               "concordance_roots": concordances(out), "quran_refs": SRC.corpus(out.parents[1] / "inputs/quran.tsv")}
    if not value["source_items"]:
        raise ValueError("No supporting research selected")
    for name, available in choices.items():
        missing = set(value[name]) - available.keys()
        if missing:
            raise ValueError("Unknown " + name + ": " + ", ".join(sorted(missing)))
    return data


def build_writer(arm, ref, composition):
    out = EX.ayah_dir(arm, ref)
    data = check_composition(out, composition)
    chosen = set(composition["source_items"])
    qualification_ids = {k for k, v in data["items"].items()
                         if v["kind"] == "contradicts" or (v["kind"] == "shifts" and v.get("finding") in chosen)}
    # Preserve qualifications independently of whether the composer remembered to select them.
    qualifications = research(data, qualification_ids)
    explanation = composition["explanation"] + "\n\nReader's changed understanding:\n" + composition["reader_change"]
    if composition["limits"]:
        explanation += "\n\nMaterial limits:\n" + "\n".join(composition["limits"])
    bmap, cmap = branches(out), concordances(out)
    files = [("write_composition.md", (arm / "inputs/write_composition.md").read_text()),
             ("ayah.md", (out / "inputs/ayah.md").read_text()),
             ("window_text.md", (out / "inputs/window_text.md").read_text()),
             ("composition.md", explanation),
             ("dictionary.selected.md", "\n".join(bmap[k] for k in composition["branches"])),
             ("concordance.selected.md", "\n\n".join(cmap[k] for k in composition["concordance_roots"])),
             ("passages.selected.md", SRC.render(SRC.corpus(arm / "inputs/quran.tsv"), set(composition["quran_refs"]))),
             ("qualifications.md", qualifications or "No additional contradiction or selected-finding shift records."),
             ("variants.md", (out / "inputs/variants.md").read_text()),
             ("source_access.md", access(arm, ref, "write"))]
    new(out / "write.input.md", assemble(files))
    new(out / "write.input.json", {"sha256": S.sha(out / "write.input.md"),
        "bytes": (out / "write.input.md").stat().st_size, "composition_sha256": S.sha(out / "composition.json"),
        "experiment_sha256": S.sha(arm / "experiment.json"), "qualification_ids": sorted(qualification_ids),
        "source_selection": {k: composition[k] for k in ["source_items", "branches", "quran_refs", "concordance_roots"]}})
    archive = {key: {"selected_by_composer": key in chosen, "qualification_supplied": key in qualification_ids,
                      "record": item["text"]} for key, item in data["items"].items()}
    new(out / "research.disposition.json", {"note": "Selection and retention only; no claim of use or completeness in prose. "
         "Unselected research is preserved here without a promise to publish it later.", "items": archive})


def start(arm, ref, phase, model, effort):
    verify(arm, ref)
    out = EX.ayah_dir(arm, ref)
    if phase == "write" and read(out / "synth.status.json")["state"] != "done":
        raise ValueError("Synthesis must finish successfully before writing")
    receipt = read(out / f"{phase}.input.json")
    if S.sha(out / f"{phase}.input.md") != receipt["sha256"] or S.sha(arm / "experiment.json") != receipt["experiment_sha256"]:
        raise ValueError("Prepared input changed")
    if phase == "write" and S.sha(out / "composition.json") != receipt["composition_sha256"]:
        raise ValueError("Composition changed")
    claim = {"model": model, "effort": effort, "input_sha256": receipt["sha256"], "started_utc": now(),
             "input_receipt_sha256": S.sha(out / f"{phase}.input.json")}
    new(out / f"{phase}.started.json", claim)
    new(out / f"{phase}.status.json", {"state": "started", **claim})
    return out / f"{phase}.input.md"


def ingest(arm, ref, phase, response):
    verify(arm, ref)
    out = EX.ayah_dir(arm, ref)
    status, claim = read(out / f"{phase}.status.json"), read(out / f"{phase}.started.json")
    if status["state"] != "started":
        raise ValueError("Only one started generation can be ingested")
    if (S.sha(out / f"{phase}.input.md") != claim["input_sha256"] or
            S.sha(out / f"{phase}.input.json") != claim["input_receipt_sha256"]):
        raise ValueError("Claimed input or receipt changed")
    new(out / f"{phase}.raw.txt", response)
    errors = []
    if phase == "synth":
        try:
            value = json.loads(response)
            check_composition(out, value)
            new(out / "composition.json", value)
            build_writer(arm, ref, value)
        except (ValueError, TypeError, KeyError) as exc:
            errors.append(str(exc))
        new(out / "composition.check.json", {"structurally_valid": not errors, "errors": errors,
            "semantic_acceptance": "Independent review required; valid sources are not proof of good synthesis."})
    else:
        if not response.strip() or "===== SYNTHESIS =====" in response or response.lstrip().startswith("{"):
            errors.append("Expected finished prose only")
        new(out / f"{ref.replace(':', '_')}.reading.tr.md", response.strip() + "\n")
    status = {"state": "failed" if errors else ("done" if phase == "synth" else "review-needed"), **claim,
              "completed_utc": now(), "errors": errors, "raw_sha256": S.sha(out / f"{phase}.raw.txt"),
              "usage": None, "generation_count": 1, "repair_count": 0}
    EX.dump(out / f"{phase}.status.json", status)
    return status


def lookup(arm, ref, phase, kind, keys, context=1):
    verify(arm, ref)
    out = EX.ayah_dir(arm, ref)
    if read(out / f"{phase}.status.json")["state"] != "started":
        raise ValueError("Lookup requires an active generation")
    requested = list(dict.fromkeys(k.strip() for k in keys.split(",")))
    if not 1 <= len(requested) <= 16 or any(not k for k in requested):
        raise ValueError("Request 1–16 keys")
    returned = requested
    if kind == "quran":
        corpus = SRC.corpus(arm / "inputs/quran.tsv")
        returned = sorted(SRC.select(corpus, set(requested), context))
        result = SRC.render(corpus, set(returned))
    else:
        available = read(out / "synthesis.json")["items"] if kind == "items" else branches(out) if kind == "branches" else concordances(out)
        missing = set(requested) - available.keys()
        if missing:
            raise ValueError("Unknown frozen source keys: " + ", ".join(sorted(missing)))
        result = (research({"items": available}, requested) if kind == "items" else "\n\n".join(available[k] for k in requested))
    record = {"phase": phase, "kind": kind, "requested": requested, "returned": returned,
              "context": context if kind == "quran" else None, "bytes": len(result.encode()),
              "sha256": __import__("hashlib").sha256(result.encode()).hexdigest()}
    with (out / f"{phase}.lookups.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("step", choices=["prepare", "start", "ingest", "verify", "lookup"])
    ap.add_argument("ref")
    ap.add_argument("--tag", required=True)
    ap.add_argument("--source-tag")
    ap.add_argument("--phase", choices=PHASES)
    ap.add_argument("--model")
    ap.add_argument("--effort", default="max")
    ap.add_argument("--response", type=Path)
    ap.add_argument("--kind", choices=["quran", "items", "branches", "concordance"])
    ap.add_argument("--keys")
    ap.add_argument("--context", type=int, default=1)
    args = ap.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_-]+", args.tag) or not re.fullmatch(r"[1-9]\d*:[1-9]\d*", args.ref):
        ap.error("Invalid tag or reference")
    arm = EX.ROOT / f"out-{args.tag}"
    if args.step == "prepare":
        if not args.source_tag or not re.fullmatch(r"[A-Za-z0-9_-]+", args.source_tag):
            ap.error("Valid --source-tag required")
        result = prepare(arm, EX.ROOT / f"out-{args.source_tag}", args.ref)
    elif args.step == "verify":
        result = verify(arm, args.ref)
    else:
        if not args.phase:
            ap.error("--phase required")
        if args.step == "start":
            if not args.model:
                ap.error("--model required")
            result = str(start(arm, args.ref, args.phase, args.model, args.effort))
        elif args.step == "ingest":
            if not args.response:
                ap.error("--response required")
            result = ingest(arm, args.ref, args.phase, args.response.read_text())
        else:
            if not args.kind or not args.keys:
                ap.error("--kind and --keys required")
            print(lookup(arm, args.ref, args.phase, args.kind, args.keys, args.context))
            return
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
