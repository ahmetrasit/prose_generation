"""Shared helpers for the on-demand reference fetchers (ref_*.py).

Contract: enrichment/bible/corpus/README.md  (source.json + segments.jsonl + raw/).

* Politeness: at most 1 request / second per host (across processes, via a lock file per host),
  retries with backoff on network errors / 429 / 5xx, honest User-Agent.
* Cache: every response body is stored under <corpus>/<ID>/raw/<relpath> and logged in
  raw/_fetchlog.jsonl with URL, HTTP status, sha256 and date.  A cached URL is never fetched again
  (also negative results such as 404), unless --refresh is given.
* Segments: upserted by `seg` into segments.jsonl (existing order kept, new ones appended).
"""
from __future__ import annotations

import datetime as _dt
import fcntl
import hashlib
import html
import json
import os
import re
import sys
import time
import unicodedata
import urllib.parse
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[3]          # .../prose_generation
CORPUS = ROOT / "enrichment" / "bible" / "corpus"
UA = ("Mozilla/5.0 (compatible; quran-enrichment-research/1.0; local research cache; "
      "1 req/s; contact: ozturk.ahmetr@gmail.com)")
MIN_INTERVAL = 1.0      # seconds between requests to one host
LOCKDIR = Path(os.environ.get("TMPDIR", "/tmp")) / "bible_fetch_locks"


def today() -> str:
    return _dt.date.today().isoformat()


def now_iso() -> str:
    return _dt.datetime.now().astimezone().isoformat(timespec="seconds")


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


# ---------------------------------------------------------------- text helpers
_TR_LOWER = str.maketrans({"I": "ı", "İ": "i"})


def tr_lower(s: str) -> str:
    return s.translate(_TR_LOWER).lower()


def deaccent(s: str) -> str:
    """Strip circumflexes and other combining marks, keep Turkish letters (ç ğ ı ö ş ü)."""
    keep = {"ç", "ğ", "ı", "ö", "ş", "ü", "Ç", "Ğ", "İ", "Ö", "Ş", "Ü"}
    out = []
    for ch in s:
        if ch in keep:
            out.append(ch)
            continue
        d = unicodedata.normalize("NFD", ch)
        out.append("".join(c for c in d if not unicodedata.combining(c)))
    return unicodedata.normalize("NFC", "".join(out))


def ascii_fold(s: str) -> str:
    s = tr_lower(s)
    s = s.translate(str.maketrans("çğıöşü", "cgiosu"))
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if not unicodedata.combining(c))


def slugify(s: str) -> str:
    s = ascii_fold(s)
    s = re.sub(r"[’'‘ʼʿʾ`]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


_BLOCK_TAGS = r"(?:p|div|br|li|ul|ol|h[1-6]|tr|table|blockquote|bibl)"


def html_to_text(h: str) -> str:
    """Small, dependency-free HTML -> text (paragraphs separated by blank lines)."""
    h = re.sub(r"<(script|style)\b.*?</\1>", "", h, flags=re.S | re.I)
    h = re.sub(r"<!--.*?-->", "", h, flags=re.S)
    h = re.sub(r"\s+", " ", h)                      # source line breaks are not text breaks
    h = re.sub(r"<br\s*/?>", "\n", h, flags=re.I)
    h = re.sub(rf"</?{_BLOCK_TAGS}\b[^>]*>", "\n\n", h, flags=re.I)
    h = re.sub(r"<[^>]+>", "", h)
    h = html.unescape(h).replace("\xa0", " ").replace("\r", "")
    h = re.sub(r"[ \t]+", " ", h)
    h = re.sub(r" *\n *", "\n", h)
    h = re.sub(r"\n{3,}", "\n\n", h)
    return h.strip()


# ---------------------------------------------------------------- source dir
class Source:
    def __init__(self, sid: str):
        from enrichment.bible.corpus import running_calls
        if running_calls():
            raise ValueError('Bible page calls are active; do not change their source cache')
        self.id = sid
        self.dir = CORPUS / sid
        self.raw = self.dir / "raw"
        self.raw.mkdir(parents=True, exist_ok=True)
        self.log_path = self.raw / "_fetchlog.jsonl"
        self._log = self._read_log()

    # ---- fetch log / cache
    def _read_log(self) -> dict:
        d = {}
        if self.log_path.exists():
            for line in self.log_path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    r = json.loads(line)
                    d[r["path"]] = r
        return d

    def cached(self, rel: str) -> dict | None:
        r = self._log.get(rel)
        if r and (self.raw / rel).exists():
            return r
        return None

    def read_raw(self, rel: str) -> bytes:
        return (self.raw / rel).read_bytes()

    def fetch(self, url: str, rel: str, *, headers: dict | None = None, refresh: bool = False,
              ok_status=(200,), quiet=False) -> tuple[int, bytes]:
        """Return (status, body).  Served from raw/ when cached; otherwise fetched politely and cached."""
        c = None if refresh else self.cached(rel)
        if c is not None and c['status'] in ok_status:
            return c["status"], self.read_raw(rel)
        status, body, final = http_get(url, headers=headers)
        p = self.raw / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(body)
        rec = {"path": rel, "url": url, "final_url": final, "status": status,
               "sha256": sha256_bytes(body), "bytes": len(body), "fetched_at": now_iso()}
        with self.log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        self._log[rel] = rec
        if not quiet:
            print(f"  fetched [{status}] {url} -> raw/{rel}", file=sys.stderr)
        return status, body

    # ---- segments
    def segments_path(self) -> Path:
        return self.dir / "segments.jsonl"

    def load_segments(self) -> list[dict]:
        p = self.segments_path()
        if not p.exists():
            return []
        return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]

    def upsert_segments(self, segs: list[dict], drop_prefix: str | None = None) -> int:
        """Insert/replace by seg.  With drop_prefix, old segments whose seg starts with it and that are
        not in `segs` are removed (so a re-parse of one article/entry replaces all its parts)."""
        cur = self.load_segments()
        new_ids = {s["seg"] for s in segs}
        if drop_prefix:
            cur = [s for s in cur if not (s["seg"].startswith(drop_prefix) and s["seg"] not in new_ids)]
        idx = {s["seg"]: i for i, s in enumerate(cur)}
        for s in segs:
            s = normalise_seg(s)
            if s["seg"] in idx:
                cur[idx[s["seg"]]] = s
            else:
                idx[s["seg"]] = len(cur)
                cur.append(s)
        tmp = self.segments_path().with_suffix(".jsonl.tmp")
        with tmp.open("w", encoding="utf-8") as f:
            for s in cur:
                f.write(json.dumps(s, ensure_ascii=False) + "\n")
        tmp.replace(self.segments_path())
        return len(segs)

    # ---- source.json
    def update_source(self, base: dict, *, urls: list[str] = (), extra: dict | None = None):
        """Merge `base` (identity fields, only set when missing or when they are static) and refresh
        files/urls/fetched_at from the fetch log."""
        p = self.dir / "source.json"
        sj = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
        for k, v in base.items():
            sj[k] = v
        u = list(dict.fromkeys(list(sj.get("urls", [])) + list(urls)))
        sj["urls"] = u
        sj["fetched_at"] = now_iso()
        files = {}
        for rel, r in sorted(self._read_log().items()):
            if (self.raw / rel).exists():
                files[f"raw/{rel}"] = r["sha256"]
        sj["files"] = files
        sj["fetch_log"] = "raw/_fetchlog.jsonl (url, status, sha256, date per raw file)"
        if extra:
            for k, v in extra.items():
                if isinstance(v, dict) and isinstance(sj.get(k), dict):
                    sj[k].update(v)
                else:
                    sj[k] = v
        p.write_text(json.dumps(sj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return sj


def normalise_seg(s: dict) -> dict:
    out = {"seg": s["seg"], "s": s.get("s"), "a": s.get("a"), "a_end": s.get("a_end"),
           "page": s.get("page"), "head": s.get("head"), "text": s.get("text", "")}
    for k, v in s.items():
        if k not in out:
            out[k] = v
    return out


# ---------------------------------------------------------------- polite HTTP
_session = requests.Session()
_session.headers.update({"User-Agent": UA, "Accept-Language": "tr,en;q=0.8,de;q=0.6"})


def _throttle(host: str):
    LOCKDIR.mkdir(parents=True, exist_ok=True)
    lf = LOCKDIR / (re.sub(r"[^a-z0-9.-]", "_", host.lower()) + ".lock")
    fd = os.open(lf, os.O_RDWR | os.O_CREAT, 0o644)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX)
        raw = os.pread(fd, 64, 0).decode().strip()
        last = float(raw) if raw else 0.0
        wait = last + MIN_INTERVAL - time.time()
        if wait > 0:
            time.sleep(wait)
        stamp = f"{time.time():.3f}".ljust(32).encode()
        os.pwrite(fd, stamp, 0)
    finally:
        fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)


def http_get(url: str, headers: dict | None = None, tries: int = 4) -> tuple[int, bytes, str]:
    host = urllib.parse.urlsplit(url).hostname or "x"
    err = None
    for i in range(tries):
        _throttle(host)
        try:
            r = _session.get(url, headers=headers or {}, timeout=60, allow_redirects=True)
            if r.status_code in (429, 500, 502, 503, 504) and i < tries - 1:
                time.sleep(5 * (i + 1))
                continue
            return r.status_code, r.content, r.url
        except requests.exceptions.SSLError as e:
            # e.g. eski.lugatim.com serves an incomplete certificate chain; the system curl (macOS trust
            # store, AIA fetching) verifies it properly. Certificate verification stays ON.
            try:
                return _curl_get(url, headers)
            except Exception as ce:          # timeouts etc.: retry like any network error
                err = ce
                time.sleep(5 * (i + 1))
        except requests.RequestException as e:
            err = e
            time.sleep(5 * (i + 1))
    raise RuntimeError(f"GET {url} failed after {tries} tries: {err}")


def _curl_get(url: str, headers: dict | None) -> tuple[int, bytes, str]:
    import subprocess
    import tempfile
    with tempfile.NamedTemporaryFile() as tf:
        cmd = ["curl", "-sS", "-L", "--max-time", "60", "-A", UA, "-o", tf.name, "-w", "%{http_code} %{url_effective}"]
        for k, v in (headers or {}).items():
            cmd += ["-H", f"{k}: {v}"]
        out = subprocess.run(cmd + [url], capture_output=True, text=True, check=True).stdout.strip()
        code, final = out.split(" ", 1)
        return int(code), open(tf.name, "rb").read(), final


def detect_challenge(body: bytes) -> bool:
    """Cloudflare / bot challenge or login wall markers: if seen, stop and record it."""
    t = body[:20000].decode("utf-8", "replace").lower()
    return any(m in t for m in ("cf-challenge", "challenge-platform", "just a moment...",
                                "cf_chl_", "attention required! | cloudflare"))
