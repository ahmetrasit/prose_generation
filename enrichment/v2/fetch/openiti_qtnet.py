"""quran-tafsir.net per-ayah pages for works OpenITI lacks (same site and extraction as v1/corpus/fetch_tafsir.py).

Only the surahs named in the registry entry (`surahs`, default S1 and 86-114) are fetched. Raw HTML is kept
gzip-compressed under raw/html/ (the page is mostly site chrome); its sha256 is the sha256 of the HTML as served.
"""
from __future__ import annotations

import gzip
import hashlib
import json
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

from openiti_quran import quran

UA = {"User-Agent": "Mozilla/5.0 (research corpus fetch; prose_generation enrichment)"}


class Nass(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth, self.out, self.found = 0, [], False

    def handle_starttag(self, t, a):
        a = dict(a)
        if t == "div" and "nass" in (a.get("class") or "").split():
            self.depth, self.found = 1, True
        elif self.depth and t == "div":
            self.depth += 1
        if self.depth and t in ("p", "br", "hr"):
            self.out.append("\n")

    def handle_endtag(self, t):
        if self.depth and t == "div":
            self.depth -= 1
        if self.depth and t == "p":
            self.out.append("\n")

    def handle_data(self, d):
        if self.depth:
            self.out.append(d)


def get(url: str, tries: int = 5) -> tuple[int, bytes]:
    last = "no try"
    for i in range(tries):
        try:
            return 200, urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40).read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return 404, b""
            last = f"HTTP {e.code}"
        except Exception as e:  # retried; reported below if every try fails
            last = f"{type(e).__name__}: {e}"
        time.sleep(2 ** i)
    print(f"FETCH FAILED after {tries} tries: {url} ({last}); recorded as http_0", file=sys.stderr)
    return 0, b""


def do_qtnet(w: dict, corpus: Path, force: bool = False) -> dict:
    d = corpus / w["id"]
    html_dir = d / "raw" / "html"
    html_dir.mkdir(parents=True, exist_ok=True)
    q = quran()
    surahs = w.get("surahs") or [1] + list(range(86, 115))
    targets = [(s, a) for s in surahs for a in range(1, q.count[s] + 1)]
    slug = w["slug"]
    index_p = d / "raw" / "index.jsonl"
    done = {}
    if index_p.exists():
        for line in index_p.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            done[(r["s"], r["a"])] = r

    def one(sa):
        s, a = sa
        dest = html_dir / f"{s}_{a}.html.gz"
        if not force and dest.exists() and done.get(sa, {}).get("status") == "ok":
            return None
        url = f"https://quran-tafsir.net/{slug}/sura{s}-aya{a}.html"
        code, raw = get(url)
        rec = {"s": s, "a": a, "url": url, "status": "ok" if code == 200 else f"http_{code}",
               "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        if code == 200:
            dest.write_bytes(gzip.compress(raw))
            rec["sha256"] = hashlib.sha256(raw).hexdigest()
        time.sleep(0.3)
        return rec

    with ThreadPoolExecutor(max_workers=2) as ex:
        for rec in ex.map(one, targets):
            if rec:
                done[(rec["s"], rec["a"])] = rec
    with index_p.open("w", encoding="utf-8") as f:
        for k in sorted(done):
            f.write(json.dumps(done[k], ensure_ascii=False) + "\n")

    n, prev = 0, None
    with (d / "segments.jsonl").open("w", encoding="utf-8") as out:
        for s, a in targets:
            p = html_dir / f"{s}_{a}.html.gz"
            if not p.exists():
                continue
            parser = Nass()
            parser.feed(gzip.decompress(p.read_bytes()).decode("utf-8", "replace"))
            txt = "\n".join(x.strip() for x in "".join(parser.out).splitlines() if x.strip())
            if not txt:
                continue
            # the site repeats one passage on every ayah of a verse group: keep it once (a..a_end)
            if prev and prev["text"] == txt and prev["s"] == s:
                prev["a_end"] = a
                continue
            if prev:
                out.write(json.dumps(prev, ensure_ascii=False) + "\n")
                n += 1
            prev = {"seg": f"{w['id']}:{s}:{a}", "s": s, "a": a, "a_end": a, "page": None, "head": None, "text": txt}
        if prev:
            out.write(json.dumps(prev, ensure_ascii=False) + "\n")
            n += 1
    ok = sum(1 for r in done.values() if r["status"] == "ok")
    meta = {"id": w["id"], "title": w["title"], "author": w["author"], "death_ah": w["death_ah"], "kind": w["kind"],
            "tradition": w["tradition"], "language": "ar", "edition": f"quran-tafsir.net, slug '{slug}'",
            "access": "yerel", "locator": "ayah",
            "coverage": ",".join(str(x) for x in surahs[:1]) + (f",{surahs[1]}-{surahs[-1]}" if len(surahs) > 1 else ""),
            "urls": [f"https://quran-tafsir.net/{slug}/sura{{s}}-aya{{a}}.html"],
            "fetched_at": datetime.now(timezone.utc).date().isoformat(),
            "files": {"raw/index.jsonl": hashlib.sha256(index_p.read_bytes()).hexdigest()},
            "licence": "copyrighted work served openly by quran-tafsir.net; local research copy of the fetched "
                       "ayahs only (per-page sha256 of the served HTML in raw/index.jsonl)",
            "notes": w["notes"] + f" Pages fetched ok: {ok}/{len(targets)}; consecutive identical pages (one "
                                  "passage served under each ayah of a verse group) are stored once as a..a_end.",
            "segments": n}
    (d / "source.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"id": w["id"], "status": "ok", "segments": n}
