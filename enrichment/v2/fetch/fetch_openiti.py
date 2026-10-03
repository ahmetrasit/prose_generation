#!/usr/bin/env python3
"""Fetch whole-book Arabic sources (OpenITI; quran-tafsir.net for what OpenITI lacks) into enrichment/corpus/<ID>/.

Contract: enrichment/corpus/README.md — source.json + segments.jsonl + raw/ per source.
Registry: openiti_works.py (one pinned OpenITI version URI per ID, or another host, or a pointer).

  fetch_openiti.py --list
  fetch_openiti.py [--ids A,B,...] [--workers 2] [--force] [--parse-only] [--fetch-only]

OpenITI files come from raw.githubusercontent.com/OpenITI/<NNNNAH>/master/data/<author>/<book>/<version>[.ext]
(the most developed file of the version: .mARkdown > .completed > .inProgress > bare). The GitHub contents API
gives the file's git blob sha; the download is verified against it and skipped on re-runs when the local copy
still matches (resumable; partial downloads continue with HTTP Range). The version's .yml is kept beside it.
Requests: ≤ 2 at a time, retries with backoff.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import shutil
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from openiti_works import BY_ID, W  # noqa: E402
from openiti_parse import parse  # noqa: E402

PG = Path(__file__).resolve().parents[3]
CORPUS = PG / "enrichment" / "corpus"
UA = {"User-Agent": "Mozilla/5.0 (research corpus fetch; prose_generation enrichment)"}
EXT_ORDER = [".mARkdown", ".completed", ".inProgress", ""]
RELEASE_META = "https://raw.githubusercontent.com/OpenITI/RELEASE/master/metadata/OpenITI_metadata_2025-1-9.tsv"
LOCK = threading.Lock()


def log(*a):
    with LOCK:
        print(*a, flush=True)


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


# ---------------------------------------------------------------- GitHub

def gh_api(path: str):
    """GitHub REST GET; uses the gh CLI when logged in (5000 req/h), else anonymous urllib (60 req/h)."""
    for i in range(4):
        try:
            if shutil.which("gh"):
                r = subprocess.run(["gh", "api", path], capture_output=True, text=True, timeout=60)
                if r.returncode == 0:
                    return json.loads(r.stdout)
                if "Not Found" in r.stderr or "404" in r.stderr:
                    return None
            else:
                req = urllib.request.Request("https://api.github.com/" + path, headers=UA)
                tok = os.environ.get("GITHUB_TOKEN")
                if tok:
                    req.add_header("Authorization", f"Bearer {tok}")
                return json.loads(urllib.request.urlopen(req, timeout=60).read())
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
        except Exception:
            pass
        time.sleep(2 ** i)
    raise RuntimeError(f"GitHub API failed: {path}")


def repo_of(uri: str) -> str:
    return f"{math.ceil(int(uri[:4]) / 25) * 25:04d}AH"


def resolve(uri: str) -> dict:
    author, book = uri.split(".")[0], ".".join(uri.split(".")[:2])
    repo = repo_of(uri)
    folder = f"data/{author}/{book}"
    listing = gh_api(f"repos/OpenITI/{repo}/contents/{folder}")
    if not listing:
        raise RuntimeError(f"{uri}: folder not found in OpenITI/{repo}")
    files = {x["name"]: x for x in listing}
    for ext in EXT_ORDER:
        if uri + ext in files:
            f = files[uri + ext]
            break
    else:
        raise RuntimeError(f"{uri}: no text file in {repo}/{folder} ({sorted(files)})")
    commit = (gh_api(f"repos/OpenITI/{repo}/commits/master") or {}).get("sha")
    base = f"https://raw.githubusercontent.com/OpenITI/{repo}/master/{folder}/"
    return {"repo": repo, "folder": folder, "name": f["name"], "size": f["size"], "git_sha": f["sha"],
            "url": base + f["name"], "yml": base + uri + ".yml" if uri + ".yml" in files else None,
            "book_yml": base + book + ".yml" if book + ".yml" in files else None, "commit": commit}


def git_blob_sha(path: Path) -> str:
    h = hashlib.sha1(f"blob {path.stat().st_size}\0".encode())
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def download(url: str, dest: Path, size: int | None = None, tries: int = 6) -> None:
    """Stream url to dest (via dest.part, resuming with Range)."""
    part = dest.with_name(dest.name + ".part")
    dest.parent.mkdir(parents=True, exist_ok=True)
    for i in range(tries):
        have = part.stat().st_size if part.exists() else 0
        if size and have >= size:
            break
        req = urllib.request.Request(url, headers=dict(UA))
        if have:
            req.add_header("Range", f"bytes={have}-")
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                mode = "ab" if have and r.status == 206 else "wb"
                with part.open(mode) as f:
                    shutil.copyfileobj(r, f, 1 << 20)
            if not size or part.stat().st_size >= size:
                break
        except urllib.error.HTTPError as e:
            if e.code in (404, 410):
                raise
            if e.code == 416:  # range past end: complete already
                break
            log(f"  retry {i + 1} {url}: HTTP {e.code}")
        except Exception as e:  # network: retry with backoff, keeping the partial file
            log(f"  retry {i + 1} {url}: {type(e).__name__}")
        time.sleep(min(60, 2 ** (i + 1)))
    part.replace(dest)


# ---------------------------------------------------------------- per work

def write_json(path: Path, obj) -> None:
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def base_meta(w: dict) -> dict:
    return {"id": w["id"], "title": w["title"], "author": w["author"], "death_ah": w["death_ah"], "kind": w["kind"],
            "tradition": w["tradition"], "language": "ar"}


def do_pointer(w: dict) -> dict:
    d = CORPUS / w["id"]
    d.mkdir(parents=True, exist_ok=True)
    meta = {**base_meta(w), "edition": "not held locally", "access": "hafiza", "locator": "page",
            "coverage": "whole book (not local)", "urls": w.get("urls", []), "fetched_at": now()[:10], "files": {},
            "licence": "no free licensed text located; cite from memory only and mark it so",
            "notes": w["notes"]}
    write_json(d / "source.json", meta)
    return {"id": w["id"], "status": "pointer"}


def do_openiti(w: dict, force: bool, parse_only: bool, fetch_only: bool, release: dict) -> dict:
    d = CORPUS / w["id"]
    raw = d / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    state_p = raw / "fetch_state.json"
    state = json.loads(state_p.read_text()) if state_p.exists() else {}
    if not parse_only or not state.get("name"):
        if state.get("uri") != w["uri"] or force or not state.get("git_sha"):
            state = {"uri": w["uri"], **resolve(w["uri"]), "resolved_at": now()}
        dest = raw / state["name"]
        if force or not dest.exists() or git_blob_sha(dest) != state["git_sha"]:
            log(f"{w['id']}: downloading {state['name']} ({state['size'] / 1e6:.1f} MB)")
            dest.unlink(missing_ok=True)
            download(state["url"], dest, state["size"])
            got = git_blob_sha(dest)
            if got != state["git_sha"]:
                # master may have moved since the listing: re-resolve once
                state = {"uri": w["uri"], **resolve(w["uri"]), "resolved_at": now()}
                if got != state["git_sha"]:
                    raise RuntimeError(f"{w['id']}: git sha mismatch after download")
            state["fetched_at"] = now()
        for key in ("yml", "book_yml"):
            if state.get(key):
                p = raw / state[key].rsplit("/", 1)[1]
                if force or not p.exists():
                    download(state[key], p)
        write_json(state_p, state)
    if fetch_only:
        return {"id": w["id"], "status": "fetched"}
    dest = raw / state["name"]
    header, st = parse(dest, w, d / "segments.jsonl")
    files = {f"raw/{p.name}": sha256(p) for p in sorted(raw.iterdir()) if p.is_file() and p.name != "fetch_state.json"
             and not p.name.endswith(".part")}
    rel = release.get(w["uri"], {})
    qa = qa_note(w, st)
    notes = " ".join(x for x in (w.get("notes", ""), ("Version choice: " + w["why"]) if w.get("why") else "", qa) if x)
    meta = {**base_meta(w),
            "edition": rel.get("ed_info") or "; ".join(header.get(k, "") for k in ("Edition", "Publisher") if header.get(k))
                       or "OpenITI version " + w["uri"],
            "access": "yerel",
            "locator": "page" if st["has_pages"] else ("ayah" if w["qorder"] else "section"),
            "coverage": "whole book" + (f" (segments tied to surahs {st['surahs']})" if w["qorder"] and st["surahs"] else ""),
            "urls": [state["url"]],
            "fetched_at": (state.get("fetched_at") or now())[:10],
            "files": files,
            "licence": "OpenITI (Zenodo doi:10.5281/zenodo.3082463, release 2025.1.9: CC BY-NC-SA 4.0); "
                       "local research copy only",
            "notes": notes,
            "openiti": {"version_uri": w["uri"], "repo": f"OpenITI/{state['repo']}", "file": state["name"],
                        "git_blob_sha": state["git_sha"], "repo_commit": state.get("commit"),
                        "release_status": rel.get("status"), "release": "OpenITI_metadata_2025-1-9",
                        "char_length": int(rel["char_length"]) if rel.get("char_length") else None,
                        "tags": rel.get("tags"), "header": header},
            "segments": st["segments"],
            "stats": {k: v for k, v in st.items() if k not in ("segments", "surahs")}}
    write_json(d / "source.json", meta)
    log(f"{w['id']}: {st['segments']} segments, pages={st['has_pages']}, s={st['with_s']} a={st['with_a']}")
    return {"id": w["id"], "status": "ok", **st}


def qa_note(w: dict, st: dict) -> str:
    """Summary of the surah/ayah assignment; the eyeball check is recorded separately (openiti_works.QA)."""
    from openiti_works import QA  # noqa
    if not w["qorder"]:
        return "s/a not assigned (book not in muṣḥaf order)."
    n = st["segments"] or 1
    msg = (f"s/a assignment: {st['with_s']}/{n} segments carry a surah, {st['with_a']}/{n} an ayah "
           f"({st['a_from_head']} from explicit headings).")
    if QA.get(w["id"]):
        msg += " Spot-check: " + QA[w["id"]]
    return msg


def load_release(cache: Path) -> dict:
    import csv
    csv.field_size_limit(1 << 30)
    if not cache.exists():
        download(RELEASE_META, cache)
    with cache.open(encoding="utf-8") as f:
        return {r["version_uri"]: r for r in csv.DictReader(f, delimiter="\t")}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ids", default="")
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--parse-only", action="store_true")
    ap.add_argument("--fetch-only", action="store_true")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--cache", default=str(Path(__file__).resolve().parent / "openiti_cache"))
    a = ap.parse_args()
    if a.list:
        for w in W:
            print(f"{w['id']:24} {w['host']:8} {w['uri'] or ''}")
        return
    ids = [x for x in a.ids.split(",") if x] or [w["id"] for w in W]
    unknown = [i for i in ids if i not in BY_ID]
    if unknown:
        sys.exit(f"unknown ids: {unknown}")
    cache = Path(a.cache)
    cache.mkdir(parents=True, exist_ok=True)
    release = load_release(cache / "OpenITI_metadata_2025-1-9.tsv")

    def run(i):
        w = BY_ID[i]
        try:
            if w["host"] == "pointer":
                return do_pointer(w)
            if w["host"] == "qtnet":
                from openiti_qtnet import do_qtnet
                return do_qtnet(w, CORPUS, a.force)
            return do_openiti(w, a.force, a.parse_only, a.fetch_only, release)
        except Exception as e:
            log(f"{i}: FAILED {type(e).__name__}: {e}")
            return {"id": i, "status": f"failed: {e}"}

    with ThreadPoolExecutor(max_workers=max(1, min(2, a.workers))) as ex:
        results = list(ex.map(run, ids))
    log(json.dumps({r["id"]: r["status"] for r in results}, ensure_ascii=False))


if __name__ == "__main__":
    main()
