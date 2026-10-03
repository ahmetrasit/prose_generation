#!/usr/bin/env python3
"""Fetch per-ayah tafsir pages from quran-tafsir.net into a shared, resumable corpus.

Layout: corpus/tafsir/<book>/<surah>_<ayah>.txt  (extracted text of div.nass)
Index : corpus/tafsir_index.jsonl  (one line per attempt: url, sha256 of raw html, chars, status, fetched_at)
Raw HTML is not kept (≈145 KB/page of site chrome); sha256 of the raw page is recorded for audit.

usage: fetch_tafsir.py [--surahs 87-114] [--books a,b,c] [--workers 4] [--limit N]
"""
import argparse, hashlib, json, sys, time, threading, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "tafsir"
INDEX = ROOT / "tafsir_index.jsonl"
QURAN = Path("/Volumes/aro/projects/quran-data/data/text/quran-uthmani.tsv")

# slug -> author/work (as labelled on quran-tafsir.net; verify before citing)
BOOKS = {
    "tabary": "al-Tabari, Jami' al-bayan",
    "katheer": "Ibn Kathir, Tafsir al-Qur'an al-'azim",
    "seoty": "al-Suyuti (site 'seoty'; verify whether al-Durr al-manthur)",
    "zamakhshary": "al-Zamakhshari, al-Kashshaf",
    "alrazy": "Fakhr al-Din al-Razi, Mafatih al-ghayb",
    "baidawy": "al-Baydawi, Anwar al-tanzil",
    "beqaay": "al-Biqa'i, Nazm al-durar",
    "qortoby": "al-Qurtubi, al-Jami' li-ahkam al-Qur'an",
    "atia": "Ibn 'Atiyya, al-Muharrar al-wajiz",
    "hayyan": "Abu Hayyan, al-Bahr al-muhit",
    "alusy": "al-Alusi, Ruh al-ma'ani",
    "baghawy": "al-Baghawi, Ma'alim al-tanzil",
    "mawardy": "al-Mawardi, al-Nukat wa-l-'uyun",
    "wahidy": "al-Wahidi (site 'wahidy'; verify which work: likely al-Wasit, not Asbab al-nuzul)",
    "ashour": "Ibn 'Ashur, al-Tahrir wa-l-tanwir",
    "nasafy": "al-Nasafi, Madarik al-tanzil",
}


class Nass(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.out = []
        self.found = False

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


def ayah_counts():
    c = {}
    for line in QURAN.read_text(encoding="utf-8").splitlines():
        k = line.split("|")[0]
        if ":" in k:
            s = int(k.split(":")[0])
            c[s] = c.get(s, 0) + 1
    # the local file lists the basmala as :1 of every surah except 1 and 9
    return {s: (n if s in (1, 9) else n - 1) for s, n in c.items()}


def targets(lo, hi):
    counts = ayah_counts()
    t = [(s, a) for s in range(lo, hi + 1) for a in range(1, counts[s] + 1)]
    if lo > 1:  # last ayah of the preceding surah, for naẓm at the boundary
        t.insert(0, (lo - 1, counts[lo - 1]))
    return t


lock = threading.Lock()


def fetch(book, s, a, tries=4):
    dest = OUT / book / f"{s}_{a}.txt"
    if dest.exists() and dest.stat().st_size > 0:
        return None
    url = f"https://quran-tafsir.net/{book}/sura{s}-aya{a}.html"
    rec = dict(book=book, surah=s, ayah=a, url=url)
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research corpus fetch)"})
            raw = urllib.request.urlopen(req, timeout=40).read()
            p = Nass()
            p.feed(raw.decode("utf-8", "replace"))
            txt = "\n".join(x.strip() for x in "".join(p.out).splitlines() if x.strip())
            rec.update(sha256_raw=hashlib.sha256(raw).hexdigest(), chars=len(txt),
                       status="ok" if txt else ("no_text" if p.found else "no_nass_div"))
            if txt:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(txt + "\n", encoding="utf-8")
            break
        except urllib.error.HTTPError as e:
            rec.update(status=f"http_{e.code}")
            if e.code == 404:
                break
        except Exception as e:  # network/timeouts: retry with backoff
            rec.update(status=f"error:{type(e).__name__}")
        time.sleep(2 ** i)
    rec["fetched_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with lock, INDEX.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    time.sleep(0.2)
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--surahs", default="87-114")
    ap.add_argument("--books", default=",".join(BOOKS))
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()
    lo, hi = (int(x) for x in args.surahs.split("-")) if "-" in args.surahs else (int(args.surahs),) * 2
    books = args.books.split(",")
    jobs = [(b, s, a) for b in books for s, a in targets(lo, hi)]
    if args.limit:
        jobs = jobs[: args.limit]
    print(f"{len(jobs)} pages, {len(books)} books", flush=True)
    done = bad = 0
    with ThreadPoolExecutor(args.workers) as ex:
        for rec in ex.map(lambda j: fetch(*j), jobs):
            if rec is None:
                continue
            done += 1
            bad += rec["status"] != "ok"
            if done % 100 == 0:
                print(f"fetched {done}, not ok {bad}", flush=True)
    print(f"done: fetched {done}, not ok {bad}")


if __name__ == "__main__":
    main()
