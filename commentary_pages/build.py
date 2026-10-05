#!/usr/bin/env python3
"""Build the public static commentary browser from repository outputs."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional

VERSION_RE = re.compile(r"^v(?P<num>\d+(?:\.\d+)*)$", re.I)
SURAH_DIR_RE = re.compile(r"^s0*(?P<s>\d{1,3})$", re.I)
AYAH_RE = re.compile(r"(?<!\d)(?P<s>\d{1,3})[_:-](?P<a>\d{1,3})(?!\d)")
ENRICHED_SURAH_RE = re.compile(r"^(?P<s>\d{1,3})_enriched(?:\.(?P<variant>.+))?\.md$", re.I)
ENRICHED_AYAH_RE = re.compile(r"^(?P<s>\d{1,3})[-_](?P<a>\d{1,3})enriched\.md$", re.I)
PLAIN_ENRICHED_AYAH_RE = re.compile(r"^(?P<s>\d{1,3})[_:-](?P<a>\d{1,3})\.md$", re.I)

PROSE_NAME_PATTERNS = [
    re.compile(r"^commentary(?:\.tagged)?(?:\.[a-z]{2})?\.md$", re.I),
    re.compile(r"^surah(?:\.tagged)?(?:\.[a-z]{2})?\.md$", re.I),
    re.compile(r"^\d{1,3}_\d{1,3}\.reading(?:\.[a-z]{2})?\.md$", re.I),
    re.compile(r"^\d{1,3}_\d{1,3}\.md$", re.I),
    re.compile(r"^\d{1,3}\.surah(?:\.[a-z]{2})?\.md$", re.I),
    re.compile(r"^images\.md$", re.I),
]

EXCLUDED_PARTS = {
    "prompt", "prompts", "runbook", "design", "review", "reviews", "status",
    "logs", "log", "ledger", "raw", "check", "checks", "packet", "packets", "started",
    "tool_calls", "tools", "schema", "schemas", "data", "inputs", "input",
}
EXCLUDED_SUFFIXES = (".prompt.md", ".raw.md", ".partial.md")


@dataclass(frozen=True)
class Entry:
    id: str
    version: str
    family: str
    surah: int
    ayah: Optional[int]
    scope: str
    variant: str
    status: str
    tagged: bool
    source_path: str
    content_path: str


def version_key(name: str) -> tuple[int, ...]:
    m = VERSION_RE.match(name)
    if not m:
        return ()
    return tuple(int(x) for x in m.group("num").split("."))


def normalized_parts(path: Path) -> list[str]:
    return [p.lower() for p in path.parts]


def is_excluded(path: Path) -> bool:
    low = str(path).lower()
    if low.endswith(EXCLUDED_SUFFIXES):
        return True
    for part in normalized_parts(path):
        token = part.rsplit(".", 1)[0]
        if token in EXCLUDED_PARTS:
            return True
        if any(x in token for x in ("prompt", "run.log", "run.stream", "ledger", "started", "tool_call")):
            return True
    return False


def is_commentary_prose(path: Path) -> bool:
    if path.suffix.lower() != ".md" or is_excluded(path):
        return False
    name = path.name
    if any(p.match(name) for p in PROSE_NAME_PATTERNS):
        return True
    low = name.lower()
    return ("reading" in low or low.startswith("commentary.")) and "prompt" not in low


def is_pending_enrichment(path: Path) -> bool:
    """Exclude scaffolds such as `<!-- Enrichment pending ... -->` from public output."""
    try:
        head = path.read_text(encoding="utf-8", errors="ignore")[:4096].lower()
    except OSError:
        return True
    return "enrichment pending" in head or "enrichment_placeholder" in head


def parse_location(path: Path) -> tuple[Optional[int], Optional[int]]:
    surah = None
    ayah = None
    enriched_surah = ENRICHED_SURAH_RE.match(path.name)
    if enriched_surah:
        return int(enriched_surah.group("s")), None
    enriched_ayah = ENRICHED_AYAH_RE.match(path.name)
    if enriched_ayah:
        return int(enriched_ayah.group("s")), int(enriched_ayah.group("a"))
    plain_enriched_ayah = PLAIN_ENRICHED_AYAH_RE.match(path.name)
    if plain_enriched_ayah and "enrichment" in {p.lower() for p in path.parts}:
        return int(plain_enriched_ayah.group("s")), int(plain_enriched_ayah.group("a"))
    for part in path.parts:
        sm = SURAH_DIR_RE.match(part)
        if sm:
            surah = int(sm.group("s"))
        am = AYAH_RE.search(part)
        if am:
            surah = int(am.group("s"))
            ayah = int(am.group("a"))
    am = AYAH_RE.search(path.name)
    if am:
        surah = int(am.group("s"))
        ayah = int(am.group("a"))
    return surah, ayah


def variant_label(version: str, rel: Path) -> str:
    parts = list(rel.parts)
    low_parts = [p.lower() for p in parts]
    name = rel.name.lower()

    enriched_surah = ENRICHED_SURAH_RE.match(name)
    if enriched_surah:
        suffix = enriched_surah.group("variant")
        return f"enriched surah · {suffix}" if suffix else "enriched surah"
    if name == "surah.md":
        return "enriched surah"
    if ENRICHED_AYAH_RE.match(name) or PLAIN_ENRICHED_AYAH_RE.match(name):
        return "enriched ayah"
    for p in reversed(parts[:-1]):
        if p.lower().startswith("augment."):
            return p
    output_flavor = next((p for p in parts if p.lower().startswith("out") and p.lower() != "out"), None)
    if "tagged" in name:
        return f"{output_flavor} · tagged" if output_flavor else "tagged"
    if re.match(r"^\d{1,3}_\d{1,3}\.md$", name):
        return f"{output_flavor} · full" if output_flavor else "full"
    if re.match(r"^\d{1,3}\.surah(?:\.[a-z]{2})?\.md$", name):
        return f"{output_flavor} · surah" if output_flavor else "surah"
    if name == "images.md":
        for p in reversed(parts[:-1]):
            if p.lower().startswith("images."):
                return p
        return "surah images"
    if name.startswith("surah."):
        return "surah tagged" if "tagged" in name else "surah"
    if any(p == "h" for p in low_parts):
        return "H test"
    if any(p == "v" for p in low_parts):
        return "V test"
    for p in reversed(parts[:-1]):
        if p.lower().startswith("dm."):
            return p
    if output_flavor:
        return output_flavor
    return version


def classify_status(version: str, rel: Path, newest_version: str) -> str:
    low = str(rel).lower()
    if "session-limit" in low or "failed" in low or ".partial" in low:
        return "failed"
    if "/h/" in f"/{low}/" or "/v/" in f"/{low}/" or "trial" in low or "test" in low:
        return "test"
    if version == newest_version:
        if "augment.augment9" in low or "images.r13" in low:
            return "production"
        return "current-base"
    return "historical"


def safe_output_name(source_rel: Path) -> str:
    digest = hashlib.sha1(source_rel.as_posix().encode("utf-8")).hexdigest()[:12]
    stem = re.sub(r"[^A-Za-z0-9._-]+", "-", source_rel.name)
    return f"{digest}-{stem}"


def scan_version_outputs(root: Path) -> list[tuple[str, Path, Path]]:
    base = root / "_commentary"
    if not base.exists():
        return []
    versions = sorted(
        [p for p in base.iterdir() if p.is_dir() and VERSION_RE.match(p.name)],
        key=lambda p: version_key(p.name),
    )
    found: list[tuple[str, Path, Path]] = []
    for version_dir in versions:
        for path in version_dir.rglob("*.md"):
            rel = path.relative_to(version_dir)
            containers = [part.lower() for part in rel.parts[:-1]]
            if not any(part.startswith("out") or part.startswith("result") or part in {"work", "experiments"} for part in containers):
                continue
            if is_commentary_prose(path):
                found.append((version_dir.name, rel, path))
    return found


def scan_enrichment_outputs(root: Path) -> list[tuple[str, Path, Path]]:
    base = root / "enrichment"
    if not base.exists():
        return []
    found: list[tuple[str, Path, Path]] = []
    for version_dir in sorted(
        [p for p in base.iterdir() if p.is_dir() and VERSION_RE.match(p.name)],
        key=lambda p: version_key(p.name),
    ):
        out = version_dir / "out"
        if not out.exists():
            continue
        for path in out.rglob("*.md"):
            if is_excluded(path) or is_pending_enrichment(path):
                continue
            rel = path.relative_to(version_dir)
            name = path.name.lower()
            is_final_enrichment = (
                name == "surah.md"
                or ENRICHED_SURAH_RE.match(name)
                or ENRICHED_AYAH_RE.match(name)
                or PLAIN_ENRICHED_AYAH_RE.match(name)
            )
            if is_final_enrichment:
                found.append((f"enrichment-{version_dir.name}", rel, path))
    return found


def find_latest_schema(root: Path) -> Optional[Path]:
    base = root / "enrichment"
    if not base.exists():
        return None
    candidates = []
    for p in base.iterdir():
        if p.is_dir() and VERSION_RE.match(p.name) and (p / "schema.json").exists():
            candidates.append(p)
    if not candidates:
        return None
    latest = max(candidates, key=lambda p: version_key(p.name))
    return latest / "schema.json"


def build(root: Path, output: Path) -> dict:
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True, exist_ok=True)
    content_dir = output / "content"
    data_dir = output / "data"
    content_dir.mkdir(parents=True, exist_ok=True)
    data_dir.mkdir(parents=True, exist_ok=True)

    version_files = scan_version_outputs(root)
    version_names = sorted({v for v, _, _ in version_files}, key=version_key)
    newest = version_names[-1] if version_names else ""

    entries: list[Entry] = []
    seen_sources: set[str] = set()

    def add_entry(family: str, version: str, rel: Path, path: Path, status: str) -> None:
        source_rel = path.relative_to(root)
        source_key = source_rel.as_posix()
        if source_key in seen_sources:
            return
        seen_sources.add(source_key)
        surah, ayah = parse_location(source_rel)
        if not surah:
            return
        scope = "ayah" if ayah else "surah"
        dest_name = safe_output_name(source_rel)
        shutil.copyfile(path, content_dir / dest_name)
        variant = variant_label(version, rel)
        entry_id = hashlib.sha1(source_key.encode("utf-8")).hexdigest()[:16]
        entries.append(Entry(
            id=entry_id,
            version=version,
            family=family,
            surah=surah,
            ayah=ayah,
            scope=scope,
            variant=variant,
            status=status,
            tagged=("tagged" in path.name.lower() or "{" in path.read_text(encoding="utf-8", errors="ignore")[:12000]),
            source_path=source_key,
            content_path=f"content/{dest_name}",
        ))

    for version, rel, path in version_files:
        add_entry("commentary", version, rel, path, classify_status(version, rel, newest))

    for version, rel, path in scan_enrichment_outputs(root):
        add_entry("enrichment", version, rel, path, "enrichment")

    status_rank = {"production": 0, "enrichment": 1, "current-base": 2, "test": 3, "historical": 4, "failed": 9}
    entries.sort(key=lambda e: (
        e.surah,
        e.ayah if e.ayah is not None else -1,
        status_rank.get(e.status, 8),
        tuple(-x for x in version_key(e.version.replace("enrichment-", ""))),
        e.variant,
        e.source_path,
    ))

    public_entries = []
    for e in entries:
        if e.status == "failed":
            continue
        item = asdict(e)
        item.pop("source_path", None)
        public_entries.append(item)
    manifest = {
        "format": 2,
        "newest_commentary_version": newest or None,
        "entries": public_entries,
    }
    (data_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    schema = find_latest_schema(root)
    if schema:
        shutil.copyfile(schema, data_dir / "schema.json")
    else:
        (data_dir / "schema.json").write_text(json.dumps({"fields": {}, "enums": {}}, indent=2), encoding="utf-8")

    asset_dir = Path(__file__).resolve().parent
    for asset in ("index.html", "styles.css"):
        src = asset_dir / asset
        if not src.exists():
            raise FileNotFoundError(f"missing site asset: {src}")
        shutil.copyfile(src, output / asset)

    app_parts = sorted(asset_dir.glob("app.part*.jsfrag"))
    if app_parts:
        app_text = "".join(p.read_text(encoding="utf-8") for p in app_parts)
    else:
        app_src = asset_dir / "app.js"
        if not app_src.exists():
            raise FileNotFoundError("missing app.js or app.part*.jsfrag")
        app_text = app_src.read_text(encoding="utf-8")
    (output / "app.js").write_text(app_text, encoding="utf-8")

    (output / ".nojekyll").write_text("", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent / "_site")
    args = parser.parse_args()
    manifest = build(args.root.resolve(), args.output.resolve())
    print(f"Built {len(manifest['entries'])} public prose entries into {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
