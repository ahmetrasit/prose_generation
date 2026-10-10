#!/usr/bin/env python3
"""Mirror the corpus source files into the private repository prose_generation_sources (user, 2026-10-09).

The public repository never holds them: every enrichment/corpus/**/raw/ and enrichment/bible/corpus/**/raw/ folder
(the downloaded and acquired originals; each source.json records their URLs and sha256) and the files that contain
copyrighted text (the corpus.sqlite.gz parts and stamp, enrichment/corpus/corpus_intertext.sqlite.gz,
enrichment/bible/corpus/corpus.sqlite.gz, and the Bible previews with the Kutsal Kitap text). The files stay where the scripts read them (git-ignored here); this script
copies them into the sibling working tree ../prose_generation_sources under the same relative paths.

A file over 95 MB (GitHub refuses files over 100 MB) is stored as <file>.partNN (90 MiB each) and listed in
SPLIT.json with its size and sha256; every split is reassembled and checked before it is recorded. Reassemble with
`cat <file>.part?? > <file>`. Nothing is deleted from the mirror: a source file removed here stays in the mirror and
in its history (traceability). With --commit, each source folder is committed on its own and pushed right away, one
commit per push (GitHub refuses a push over 2 GB; a source folder over 1.9 GB is refused before committing); a
backlog left by an earlier failure is pushed commit by commit.

  sources_sync.py [--dry] [--commit]
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

MAIN = Path(__file__).resolve().parents[3]
MIRROR = MAIN.parent / 'prose_generation_sources'
ROOTS = ('enrichment/corpus', 'enrichment/bible/corpus')
DB_COPIES = ('enrichment/corpus/corpus.sqlite.gz.part[0-9][0-9]', 'enrichment/corpus/corpus.sqlite.gz.stamp.json',
             'enrichment/corpus/corpus_intertext.sqlite.gz', 'enrichment/bible/corpus/corpus.sqlite.gz',
             'enrichment/bible/work/*/recall/*/*/preview.md')   # previews carry the Kutsal Kitap text (© all rights reserved)
LIMIT = 95_000_000
PART = 94_371_840          # 90 MiB, as the corpus.sqlite.gz parts
UNIT_MAX = 1_900_000_000


def sha(p: Path) -> str:
    h = hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def units() -> dict[str, list[Path]]:
    """Commit unit (a source's raw folder, or 'database copies') -> its files, relative to MAIN."""
    out: dict[str, list[Path]] = {}
    for root in ROOTS:
        for d in sorted((MAIN / root).rglob('raw')):
            rel = d.relative_to(MAIN)
            if d.is_dir() and 'raw' not in rel.parts[:-1]:
                files = sorted(p.relative_to(MAIN) for p in d.rglob('*') if p.is_file() or p.is_symlink())
                if files:
                    out[str(rel)] = files
    dbs = sorted({p.relative_to(MAIN) for g in DB_COPIES for p in MAIN.glob(g) if p.is_file()})
    if dbs:
        out['database copies'] = dbs
    return out


def sync_file(rel: Path, split: dict, dry: bool) -> tuple[str, int]:
    """Copy one file into the mirror (split when large). Returns (what happened, bytes written)."""
    src, dst = MAIN / rel, MIRROR / rel
    if src.is_symlink():
        return f'NOTE symlink not mirrored: {rel} -> {src.readlink() if hasattr(src, "readlink") else "?"}', 0
    st = src.stat()
    key = str(rel)
    old_parts = sorted(dst.parent.glob(f'{glob.escape(dst.name)}.part[0-9][0-9]')) if dst.parent.exists() else []
    if st.st_size <= LIMIT:
        if dst.exists() and dst.stat().st_size == st.st_size and dst.stat().st_mtime_ns == st.st_mtime_ns \
                and not old_parts:
            return 'same', 0
        if not dry:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            for p in old_parts:          # it was split before (larger then): its parts would overwrite this copy
                p.unlink()
            split.pop(key, None)
        return 'copied', st.st_size
    rec = split.get(key)
    if rec and rec['size'] == st.st_size and rec['mtime'] == int(st.st_mtime) \
            and all((dst.parent / p).exists() for p in rec['parts']) and not dst.exists():
        return 'same', 0
    if dry:
        return 'split', st.st_size
    digest = sha(src)
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():                     # a whole copy from when it was smaller
        dst.unlink()
    names, h = [], hashlib.sha256()
    with src.open('rb') as f:
        n = 0
        while True:
            b = f.read(PART)
            if not b:
                break
            name = f'{dst.name}.part{n:02d}'
            (dst.parent / name).write_bytes(b)
            names.append(name)
            n += 1
    for old in dst.parent.glob(f'{glob.escape(dst.name)}.part[0-9][0-9]'):
        if old.name not in names:
            old.unlink()
    for name in names:                   # what is on disk, read back
        with (dst.parent / name).open('rb') as f:
            for b in iter(lambda: f.read(1 << 20), b''):
                h.update(b)
    if h.hexdigest() != digest:
        raise SystemExit(f'{rel}: parts do not reassemble to the source (changed while reading?); nothing recorded')
    split[key] = {'size': st.st_size, 'mtime': int(st.st_mtime), 'sha256': digest, 'parts': names,
                  'reassemble': f'cat {dst.name}.part?? > {dst.name}'}
    return 'split', st.st_size


def git(*args: str) -> str:
    r = subprocess.run(['git', '-C', str(MIRROR), *args], capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"git {' '.join(args)} failed ({r.returncode}): {r.stderr.strip()[-2000:]}\n"
                         'Local commits are kept; rerun this script to continue (it pushes the backlog commit by commit).')
    return r.stdout


def push_backlog() -> int:
    """Push every unpushed commit, oldest first, one per push. Returns how many were pushed."""
    if not git('rev-list', '-n1', '--all').strip():     # empty repository: nothing to push
        return 0
    git('fetch', '-q', 'origin')
    remote = subprocess.run(['git', '-C', str(MIRROR), 'rev-parse', '--verify', '-q', 'origin/main'],
                            capture_output=True, text=True).stdout.strip()
    todo = git('rev-list', '--reverse', f'{remote}..HEAD' if remote else 'HEAD').split()
    for c in todo:
        git('push', '-q', 'origin', f'{c}:refs/heads/main')
    if todo:
        git('fetch', '-q', 'origin')
        git('branch', '-q', '--set-upstream-to=origin/main', 'main')
    return len(todo)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--dry', action='store_true', help='list what would be copied; write nothing')
    ap.add_argument('--commit', action='store_true', help='commit each source folder and push in batches')
    a = ap.parse_args()
    if not (MIRROR / '.git').exists():
        raise SystemExit(f'{MIRROR} is not a git working tree (clone git@github.com:ahmetrasit/prose_generation_sources.git there)')
    manifest = MIRROR / 'SPLIT.json'
    split = json.loads(manifest.read_text()) if manifest.exists() else {}
    readme = MIRROR / 'README.md'
    if not readme.exists() and not a.dry:
        readme.write_text((__doc__ or '').replace('sources_sync.py [--dry] [--commit]',
                                                  'python3 -B enrichment/v2/tools/sources_sync.py --commit  '
                                                  '(run in prose_generation)') + '\n')
    total, notes = {'copied': 0, 'split': 0, 'same': 0}, []
    if a.commit and not a.dry:
        n = push_backlog()
        if n:
            print(f'pushed a backlog of {n} commit(s)', flush=True)
    for unit, files in units().items():
        if a.commit and not a.dry:
            size = sum((MAIN / p).stat().st_size for p in files if not (MAIN / p).is_symlink())
            if size > UNIT_MAX:
                raise SystemExit(f'{unit}: {size / 1e9:.2f} GB in one folder; one commit would exceed a push; split the '
                                 'unit before syncing')
        written = 0
        for rel in files:
            what, n = sync_file(rel, split, a.dry)
            if what.startswith('NOTE'):
                notes.append(what)
                continue
            total[what] += 1
            written += n
        if not a.dry:
            manifest.write_text(json.dumps(split, indent=1, sort_keys=True) + '\n')
        if written:
            print(f'{unit}: {written / 1e6:,.1f} MB written', flush=True)
        if a.commit and not a.dry:
            paths = [unit] if unit != 'database copies' else [str(p) for p in files]
            git('add', '-A', '--', *paths, 'SPLIT.json', 'README.md')
            if git('diff', '--cached', '--name-only').strip():
                git('commit', '-q', '-m', f'sync {unit}')
                push_backlog()
    if a.commit and not a.dry:
        git('add', '-A', '--', 'SPLIT.json', 'README.md')
        if git('diff', '--cached', '--name-only').strip():
            git('commit', '-q', '-m', 'sync: manifest and readme')
        n = push_backlog()
        print(f'pushed; nothing left unpushed' + (f' ({n} commit(s) in the last push round)' if n else ''), flush=True)
    for x in notes:
        print(x)
    print(f"{'would copy' if a.dry else 'copied'} {total['copied']}, split {total['split']}, unchanged {total['same']}"
          f"{'; NOTE ' + str(len(notes)) + ' file(s) not mirrored (listed above)' if notes else ''}")


if __name__ == '__main__':
    main()
