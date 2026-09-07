"""Stream the QAC archive into a content-addressed, read-only SQLite cache."""

from __future__ import annotations

import fcntl
import gzip
import hashlib
import os
import shutil
import sqlite3
import tempfile
from contextlib import closing, contextmanager
from pathlib import Path
from typing import BinaryIO, Iterator


DEFAULT_CACHE_DIR = Path(__file__).resolve().parent / ".cache" / "qac"
CHUNK_BYTES = 1_048_576


def _signature(stat: os.stat_result) -> tuple[int, ...]:
    return stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns


DEFAULT_PROBE = "SELECT qac_ref FROM qac_morphemes LIMIT 0"


def _connect(path: Path, schema_probe: str = DEFAULT_PROBE) -> sqlite3.Connection:
    connection = sqlite3.connect(path.resolve().as_uri() + "?mode=ro", uri=True)
    try:
        connection.execute("PRAGMA query_only = ON")
        connection.execute("PRAGMA cache_size = -2048")
        connection.execute("PRAGMA mmap_size = 0")
        # Also detects a truncated/invalid cache before it can be reused.
        connection.execute(schema_probe)
        return connection
    except BaseException:
        connection.close()
        raise


def _build(compressed: BinaryIO, destination: Path, source: Path, signature: tuple[int, ...], schema_probe: str = DEFAULT_PROBE) -> None:
    descriptor, name = tempfile.mkstemp(prefix=destination.stem + ".", suffix=".tmp", dir=destination.parent)
    temporary = Path(name)
    try:
        compressed.seek(0)
        with os.fdopen(descriptor, "wb") as output, gzip.GzipFile(fileobj=compressed, mode="rb") as archive:
            shutil.copyfileobj(archive, output, length=CHUNK_BYTES)
            output.flush()
            os.fsync(output.fileno())
        with closing(_connect(temporary, schema_probe)) as connection:
            if connection.execute("PRAGMA quick_check").fetchall() != [("ok",)]:
                raise ValueError("QAC cache failed SQLite integrity validation")
        if _signature(os.fstat(compressed.fileno())) != signature or _signature(source.stat()) != signature:
            raise ValueError("QAC source changed while its cache was being built")
        os.replace(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)


@contextmanager
def open_database(source: Path, cache_dir: Path = DEFAULT_CACHE_DIR, *,
                  schema_probe: str = DEFAULT_PROBE) -> Iterator[tuple[sqlite3.Connection, str]]:
    """Hash the source on each use; decompress only on a cache miss.

    A per-digest lock coordinates processes. Readers see only validated, fully
    written databases; failed builds leave no partial SQLite file behind.
    """
    with source.open("rb") as compressed:
        signature = _signature(os.fstat(compressed.fileno()))
        digest = hashlib.sha256()
        while chunk := compressed.read(CHUNK_BYTES):
            digest.update(chunk)
        if _signature(os.fstat(compressed.fileno())) != signature or _signature(source.stat()) != signature:
            raise ValueError("QAC source changed while its fingerprint was being read")
        cache_dir.mkdir(parents=True, exist_ok=True)
        database = cache_dir / (digest.hexdigest() + ".sqlite")
        with database.with_suffix(".lock").open("a+b") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            try:
                if not database.is_file():
                    _build(compressed, database, source, signature, schema_probe)
                try:
                    connection = _connect(database, schema_probe)
                except sqlite3.DatabaseError:
                    # A damaged local cache can be regenerated from the source.
                    _build(compressed, database, source, signature, schema_probe)
                    connection = _connect(database, schema_probe)
            finally:
                fcntl.flock(lock, fcntl.LOCK_UN)
    try:
        yield connection, digest.hexdigest()
    finally:
        connection.close()
