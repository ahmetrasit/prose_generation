"""Prepare and inspect frozen writing experiments. No model client is imported here."""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

import synthesis as S
import sources as SRC

ROOT = Path(__file__).resolve().parent
SNAPSHOT = ROOT / "baseline.manifest.json"


def dump(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def ayah_dir(arm: Path, ref: str) -> Path:
    return arm / f"s{int(ref.split(':')[0]):03d}" / ref.replace(":", "_")


def archived(arm: Path) -> bool:
    names = {Path(p).parts[0] for p in json.loads(SNAPSHOT.read_text())["files"]}
    return arm.resolve().parent != ROOT.resolve() or arm.name in names


def baseline_check() -> dict:
    manifest = json.loads(SNAPSHOT.read_text())
    source = ROOT / manifest["source"]
    changed = [name for name, digest in manifest["files"].items()
               if "__pycache__" not in Path(name).parts
               and (not (source / name).is_file() or S.sha(source / name) != digest)]
    # Compiled Python caches are runtime byproducts; all copies were verified before any edits.
    copies_changed = [name for name, digest in manifest["files"].items()
                      if name.startswith(("out/", "out-", "work/"))
                      and (not (ROOT / name).is_file() or S.sha(ROOT / name) != digest)]
    return {"source_changed": changed, "archived_data_changed": copies_changed,
            "ok": not changed and not copies_changed}


def prepare(arm: Path, source: Path, refs: list[str], source_mode: str = "inline") -> dict:
    if source_mode not in ("inline", "lookup"):
        raise ValueError("Source mode must be inline or lookup")
    if archived(arm):
        raise ValueError("Choose a new --tag; copied v13 arms are immutable")
    if arm.exists():
        raise ValueError("Arm already exists; preparation never overwrites an experiment")
    if source.resolve().parent != ROOT.resolve():
        raise ValueError("Seed source must be an arm inside v14")
    refs = sorted(set(refs), key=lambda r: tuple(map(int, r.split(":"))))
    if not refs or any(not re.fullmatch(r"[1-9]\d*:[1-9]\d*", r) for r in refs):
        raise ValueError("Expected positive S:A references")
    copies = {}
    inventories = {}
    quran = SRC.corpus()
    for ref in refs:
        saved = ayah_dir(source, ref)
        dest = ayah_dir(Path("."), ref)
        for step in ("act", "qeq"):
            status = json.loads((saved / f"{step}.status.json").read_text())
            if status.get("state") not in ("done", "reused"):
                raise ValueError(f"{ref} {step} has no finished upstream result")
            copies[str(dest / f"{step}.md")] = saved / f"{step}.md"
        nf = saved.parent / "network.md"
        if nf.exists():
            copies[str(dest.parent / "network.md")] = nf
        for name in ("ayah.md", "dictionary.md", "concordance.md"):
            copies[str(dest / "inputs" / name)] = ayah_dir(ROOT / "work", ref) / name
        copies[str(dest / "inputs" / "branches.md")] = saved / "branches.md"
        inventories[ref] = S.inventory(ref, (saved / "act.md").read_text(), (saved / "qeq.md").read_text(),
                                       nf.read_text() if nf.exists() else "")
        for prior in source.glob(f"{dest.parts[0]}/*/*.reading.tr.md"):
            a = int(prior.parent.name.split("_")[1])
            if a == int(ref.split(":")[1]) - 1:
                # Only earlier prose can enter a writing input. Target/next baselines stay evaluation-only.
                copies[str(Path("context") / dest.parts[0] / prior.name)] = prior
        work = ayah_dir(ROOT / "work", ref)
        window = (work / "window").read_text().strip()
        copies[str(dest / "inputs" / "window_text.md")] = ROOT / window / "window_text.md"
    copies["inputs/write.md"] = ROOT / "prompts" / "write.md"
    if source_mode == "lookup":
        copies["inputs/quran.tsv"] = SRC.QURAN_TEXT
    # Validate all sources before creating the destination.
    for src in copies.values():
        if not src.is_file():
            raise ValueError(f"Missing frozen input: {src}")
    arm.mkdir()
    hashes, origins = {}, {}
    for name, src in copies.items():
        target = arm / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, target)
        hashes[name] = S.sha(target)
        origins[name] = str(src.relative_to(ROOT)) if src.is_relative_to(ROOT) else str(src)
    for ref, data in inventories.items():
        out = ayah_dir(arm, ref)
        for name, normalize in (("concordance.md", SRC.concordance), ("window_text.md", SRC.window)):
            target = out / "inputs" / name
            target.write_text(normalize(target.read_text(), quran), encoding="utf-8")
            key = str(target.relative_to(arm))
            hashes[key] = S.sha(target)
            origins[key] += " (Quran quotations mapped to the verifier corpus)"
        concordance_refs = set(re.findall(r"^- (\d+:\d+):\d+ ", (out / "inputs" / "concordance.md").read_text(), re.M))
        window_refs = set(re.findall(r"^(\d+:\d+)\|", (out / "inputs" / "window_text.md").read_text(), re.M))
        references = set(data["passages"]) | concordance_refs | window_refs | {ref}
        if source_mode == "inline":
            pf = out / "inputs" / "passages.md"
            pf.write_text(SRC.render(quran, references), encoding="utf-8")
        else:
            pf = out / "inputs" / "source_access.md"
            command = f"python3 -B {ROOT / 'sources.py'} --tag {arm.name.removeprefix('out-')} --ref {ref} --refs S:A,S:A --context 1"
            pf.write_text("# source_access.md — exact Quran passages on demand\n\n"
                          "Before developing a Quran cross-reference, retrieve its actual text and adjacent context. "
                          "Use this command, replacing S:A,S:A with the references you need (up to 16 per request):\n\n"
                          f"    {command}\n\n"
                          "The helper reads only the frozen Quran corpus and logs the returned references and bytes. "
                          "It never calls a model. Context may be 0, 1, 2 or 3 ayat on each side; use further requests "
                          "when a scene needs more context. Do not read the entire corpus or unrelated repository files. "
                          "Copy Quran quotations from returned text or the normalized concordance. Retrieval is for "
                          "checking and understanding the passages you develop, not for turning all candidates into "
                          "obligatory quotations. The full preceding prose is reader context, not a quotation source.\n",
                          encoding="utf-8")
        hashes[str(pf.relative_to(arm))] = S.sha(pf)
        origins[str(pf.relative_to(arm))] = "Verifier Quran corpus; exact passages or selective lookup access"
        digest = ROOT.parent / "v9" / "lines" / "work" / ref.replace(":", "_") / "digest_v2.md"
        variants = "No supplied variant readings. Do not invent one.\n"
        if digest.exists():
            match = re.search(r"(?ms)^## 1\. Variant readings.*?(?=^## 2\.|\Z)", digest.read_text())
            if match:
                variants = match[0].strip() + "\n"
        vf = out / "inputs" / "variants.md"
        vf.write_text(variants, encoding="utf-8")
        hashes[str(vf.relative_to(arm))] = S.sha(vf)
        origins[str(vf.relative_to(arm))] = str(digest) + " (variant section only; excludes legacy usage counts)"
        dump(out / "synthesis.json", data)
        (out / "synthesis.md").write_text(S.render(data), encoding="utf-8")
        for name in ("synthesis.json", "synthesis.md"):
            hashes[str((out / name).relative_to(arm))] = S.sha(out / name)
        for step in ("act", "qeq"):
            dump(out / f"{step}.status.json", {"state": "reused", "source": origins[str((out / f'{step}.md').relative_to(arm))],
                                             "sha256": S.sha(out / f"{step}.md"), "cost": 0})
    manifest = {"schema": 1, "writer_contract": 2, "source_mode": source_mode, "source_arm": source.name, "refs": refs, "upstream": "frozen",
                "quran_source": {"path": str(SRC.QURAN_TEXT), "sha256": S.sha(SRC.QURAN_TEXT)},
                "default_writer": {"model": "opus", "effort": "high"}, "files": hashes, "origins": origins}
    dump(arm / "experiment.json", manifest)
    return manifest


def verify(arm: Path) -> dict:
    if archived(arm):
        raise ValueError("Copied v13 data is read-only")
    manifest = json.loads((arm / "experiment.json").read_text())
    source = manifest.get("quran_source")
    if source and S.sha(Path(source["path"])) != source["sha256"]:
        raise ValueError("Verifier Quran corpus changed since preparation")
    changed = [name for name, digest in manifest["files"].items()
               if not (arm / name).is_file() or S.sha(arm / name) != digest]
    if changed:
        raise ValueError("Frozen evidence changed: " + ", ".join(changed))
    return manifest


def previous(arm: Path, ref: str, manifest: dict) -> tuple[str, list[dict]]:
    s, a = map(int, ref.split(":"))
    paragraphs = ["# Earlier prose actually available to the reader", "",
                  "This contains only the immediately preceding ayah's actual prose. More distant prose is not supplied; "
                  "do not assume it explained a reading. A network disclosure plan is not proof of earlier delivery.", ""]
    provenance = []
    for n in range(max(1, a - 1), a):
        prior_ref = f"{s}:{n}"
        path = arm / "context" / f"s{s:03d}" / f"{s}_{n}.reading.tr.md"
        label = "frozen earlier baseline"
        if prior_ref in manifest["refs"]:
            out = ayah_dir(arm, prior_ref)
            status_path = out / "write.status.json"
            status = json.loads(status_path.read_text()) if status_path.exists() else {}
            if status.get("state") != "review-needed" or not status.get("account_valid"):
                raise ValueError(f"{ref}: waiting for structurally valid candidate {prior_ref}; no baseline fallback")
            path = out / f"{s}_{n}.reading.tr.md"
            label = "earlier candidate, awaiting semantic review"
        if not path.exists():
            paragraphs.append(f"## {prior_ref}: no earlier prose available\n")
            continue
        provenance.append({"ref": prior_ref, "path": str(path.relative_to(arm)), "sha256": S.sha(path), "kind": label})
        paragraphs += [f"## {prior_ref} — {label}", path.read_text(), ""]
    return "\n".join(paragraphs), provenance


def packet(arm: Path, ref: str) -> tuple[str, dict]:
    manifest = verify(arm)
    if ref not in manifest["refs"]:
        raise ValueError(f"{ref} was not prepared in this arm")
    out = ayah_dir(arm, ref)
    earlier, provenance = previous(arm, ref, manifest)
    # Explicit allowlist: never read eval/, review files, north star, or the target baseline.
    files = [arm / "inputs" / "write.md", out / "inputs" / "ayah.md", out / "inputs" / "window_text.md",
             out / "synthesis.md", out / "inputs" / "dictionary.md", out / "inputs" / "branches.md",
             out / "inputs" / "concordance.md", out / "inputs" / "variants.md"]
    if manifest.get("writer_contract", 1) >= 2:
        files.append(out / "inputs" / ("source_access.md" if manifest.get("source_mode") == "lookup" else "passages.md"))
    text = "\n\n".join(f"===== {p.name} =====\n{p.read_text()}" for p in files)
    text += "\n\n===== previous.md =====\n" + earlier
    return text, {"ref": ref, "files": {str(p.relative_to(arm)): S.sha(p) for p in files},
                  "earlier_prose": provenance, "experiment_sha256": S.sha(arm / "experiment.json")}


def export(arm: Path, ref: str) -> dict:
    text, provenance = packet(arm, ref)
    out = ayah_dir(arm, ref)
    if (out / "write.started.json").exists():
        raise ValueError("Writer already started; exported input is immutable")
    path = out / "write.input.md"
    path.write_text(text, encoding="utf-8")
    provenance["input_sha256"] = S.sha(path)
    provenance["input_bytes"] = path.stat().st_size
    dump(out / "write.input.json", provenance)
    return provenance


def claim(arm: Path, ref: str, model: str, effort: str) -> Path:
    verify(arm)
    out = ayah_dir(arm, ref)
    if (out / "write.status.json").exists():
        st = json.loads((out / "write.status.json").read_text())
        if st.get("state") in ("started", "done", "failed", "review-needed", "reused"):
            raise ValueError("Writer already called; never twice")
    packet_path = out / "write.input.md"
    if not packet_path.exists():
        raise ValueError("Export the frozen writing input first")
    receipt = json.loads((out / "write.input.json").read_text())
    current_text, current = packet(arm, ref)
    if receipt["input_sha256"] != S.sha(packet_path) or current_text != packet_path.read_text() or current["earlier_prose"] != receipt["earlier_prose"]:
        raise ValueError("Exported input or earlier prose changed")
    data = {"model": model, "effort": effort, "input_sha256": S.sha(packet_path)}
    with (out / "write.started.json").open("x", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    dump(out / "write.status.json", {"state": "started", **data})
    return packet_path


def ingest(arm: Path, ref: str, response: str, usage: dict | None = None) -> dict:
    manifest = verify(arm)
    out = ayah_dir(arm, ref)
    started = json.loads((out / "write.started.json").read_text())
    if S.sha(out / "write.input.md") != started["input_sha256"]:
        raise ValueError("Claimed writer input changed during generation")
    status = json.loads((out / "write.status.json").read_text())
    if status.get("state") != "started":
        raise ValueError("Only a started, not-yet-ingested call can be ingested")
    raw = out / "write.raw.txt"
    with raw.open("x", encoding="utf-8") as handle:
        handle.write(response)
    body, marker, tail = response.partition("===== SYNTHESIS =====")
    errors = []
    try:
        account = json.loads(tail.strip()) if marker else {}
    except json.JSONDecodeError as exc:
        account = {}
        errors.append(f"Invalid synthesis JSON: {exc}")
    if not marker or len(body.split()) < 300 or "===== CONTINUE =====" in response:
        errors.append("Missing final synthesis marker, incomplete output or insufficient prose")
    data = json.loads((out / "synthesis.json").read_text())
    if manifest.get("writer_contract", 1) >= 2 and (not isinstance(account, dict) or account.get("schema") != 2):
        errors.append("This arm requires the compact synthesis account (schema 2)")
    check = S.check_account(data, body.strip(), account)
    check["errors"] += errors
    check["structurally_valid"] = check["structurally_valid"] and not errors
    (out / f"{ref.replace(':', '_')}.reading.tr.md").write_text(body.strip() + "\n", encoding="utf-8")
    dump(out / "synthesis.account.json", account)
    dump(out / "synthesis.check.json", check)
    (out / "handforward.md").write_text(S.handforward(data, check), encoding="utf-8")
    status = {"state": "failed" if errors else "review-needed", **started, "usage": usage,
              "account_valid": check["structurally_valid"], "semantic_acceptance": "pending independent review",
              "errors": check["errors"], "words": len(body.split())}
    dump(out / "write.status.json", status)
    return status
