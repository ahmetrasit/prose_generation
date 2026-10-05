#!/usr/bin/env python3
"""A Hindawi book (hindawi.org, born-digital Arabic) as a corpus source, one segment per chapter (user,
2026-10-05: al-Khūlī's own *Manāhij* deferred; his method is covered by Bint al-Shāṭiʾ's preface and by secondary
studies, labelled secondary). The site sits behind a browser check (plain HTTP and the EPUB links answer 403), so
each chapter page is rendered once by headless Chrome and its HTML cached under <source>/raw/hindawi/<n>.html
(a page at most every 5 s). From <article class="chapterContent">: the chapter heading, the paragraphs as printed,
the footnotes (in `notes`, «[n] text», the text's markers kept as the book prints them).

  python3 -B enrichment/v2/fetch/hindawi_book.py RIFAI-KHULI 28184726
  python3 -B enrichment/v2/fetch/hindawi_book.py YKHULI-TAJDID 86174619
(the source.json must exist first; this fills segments.jsonl and the ingestion record)
"""
from __future__ import annotations

import argparse
import html
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"


def render(url: str, profile: Path, out: Path, tries: int = 3, need: str = "</html>") -> str:
    """The rendered DOM, written straight to a file (a pipe lost everything past 64 KiB when Chrome, which may not
    exit after dumping, was stopped by the timeout). A page without its closing </html> is fetched again; after
    `tries` it is refused."""
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--no-first-run", f"--user-data-dir={profile}",
           f"--user-agent={UA}", "--virtual-time-budget=15000", "--dump-dom", url]
    for k in range(tries):
        with out.open("wb") as f:
            try:
                subprocess.run(cmd, stdout=f, stderr=subprocess.DEVNULL, timeout=60)
            except subprocess.TimeoutExpired:
                pass
        subprocess.run(["pkill", "-f", str(profile)], capture_output=True)
        page = out.read_text(encoding="utf-8", errors="replace")
        if "</html>" in page and need in page:
            return page
        print(f"  {url}: incomplete page ({len(page):,} chars), attempt {k + 1}", flush=True)
        time.sleep(5)
    out.unlink(missing_ok=True)
    raise SystemExit(f"{url}: no complete page after {tries} attempts; nothing written for it")


def text_of(fragment: str) -> str:
    t = re.sub(r"<br\s*/?>", "\n", fragment)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t).replace("\xa0", " ")
    return re.sub(r"[ \t\r\n]+", " ", t).strip()


def parse(page: str) -> dict | None:
    m = re.search(r'<article class="chapterContent">(.*?)</article>', page, re.S)
    if not m:
        return None
    body = m.group(1)
    head = " — ".join(text_of(x) for x in re.findall(r'<(?:div class="part_number[^"]*"|h1[^>]*)>(.*?)</(?:div|h1)>',
                                                      body, re.S)[:2])
    main, _, foot = body.partition('<div class="footnote_line">')
    # the whole article text: block ends become paragraph breaks, so nothing inside an odd tag is lost
    main = re.sub(r'<div class="part_number[^"]*">.*?</div>|<h1[^>]*>.*?</h1>', "", main, count=2, flags=re.S)
    marked = re.sub(r"</(p|div|h[1-6]|blockquote|li|tr)>|<br\s*/?>", "\x00", main)
    paras = [x for x in (text_of(s) for s in marked.split("\x00")) if x]
    notes = []
    for f in re.findall(r'<div class="footnote">(.*?)</div>', foot, re.S):
        mm = re.match(r"\s*<sup>.*?>\s*([٠-٩\d]+)", f, re.S)
        n = mm.group(1) if mm else "?"
        notes.append(f"[{n}] " + text_of(re.sub(r"<sup>.*?</sup>", "", f, count=1, flags=re.S)))
    return {"head": head, "paras": paras, "notes": notes}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sid")
    ap.add_argument("book")
    a = ap.parse_args()
    d = IC.src_dir(a.sid)
    cache = d / "raw" / "hindawi"
    cache.mkdir(parents=True, exist_ok=True)
    profile = Path("/tmp") / f"hindawi-chrome-{a.sid}"
    front = cache / "front.html"
    if not front.exists():
        render(f"https://www.hindawi.org/books/{a.book}/", profile, front)
    chapters = sorted({int(x) for x in re.findall(rf"/books/{a.book}/(\d+)/", front.read_text(encoding="utf-8"))})
    if not chapters:
        raise SystemExit("the book's front page lists no chapters")
    segs, missing = [], []
    for n in chapters:  # the book's own contents list (chapter 0 is an introduction where there is one)
        f = cache / f"{n}.html"
        art = '<article class="chapterContent">'
        if f.exists() and art not in f.read_text(encoding="utf-8", errors="replace"):
            print(f"  cached {f.name} has no chapter text (an error page?): fetched again")
            f.unlink()
        if not f.exists():
            render(f"https://www.hindawi.org/books/{a.book}/{n}/", profile, f, need=art)
            time.sleep(5)
        ch = parse(f.read_text(encoding="utf-8"))
        if ch is None:
            missing.append(n)
            continue
        text = "\n\n".join(ch["paras"])
        g = {"seg": f"{a.sid}:c{n}", "head": ch["head"], "text": text, "url": f"https://www.hindawi.org/books/{a.book}/{n}/"}
        if ch["notes"]:
            g["notes"] = "\n".join(ch["notes"])
        g["refs"] = IC.find_refs(text + "\n" + "\n".join(ch["notes"]))
        segs.append(g)
        print(f"c{n}: {ch['head'][:60]} — {len(ch['paras'])} paragraphs, {len(ch['notes'])} notes, {len(text):,} chars")
    real_missing = missing
    if missing:
        print(f"WARNING: listed chapters with no content: {missing}")
    IC.write(a.sid, segs, {
        "script": f"enrichment/v2/fetch/hindawi_book.py {a.sid} {a.book}",
        "from": {f"raw/hindawi/{p.name}": IC.C.sha256(p) for p in sorted(cache.glob("*.html"))},
        "method": "hindawi.org chapter pages rendered by headless Chrome (the site blocks plain HTTP and EPUB "
                  "downloads); article.chapterContent paragraphs and footnotes, text as published",
        "chapters_listed": chapters, "chapters_without_content": real_missing,
    })


if __name__ == "__main__":
    main()
