#!/usr/bin/env python3
"""TDV İslâm Ansiklopedisi (islamansiklopedisi.org.tr) -> enrichment/corpus/TDVIA/

  ref_tdvia.py surah 107 [108 ...]        surah articles ("MÂÛN SÛRESİ")
  ref_tdvia.py surah 1 22 87-114          ranges allowed
  ref_tdvia.py term KALP NAMAZ "ZEKÂT"     term articles (resolved via the site's title search)
  ref_tdvia.py author "Taberî"            articles about authors
  ref_tdvia.py slug maun-suresi           a known article slug
  ref_tdvia.py reparse                    rebuild segments.jsonl from raw/ (no network)
  ref_tdvia.py drop <slug> ...            remove an unwanted article (segments + cached page)

Article URL scheme: https://islamansiklopedisi.org.tr/<slug>   (e.g. maun-suresi, kalb--kalp, din)
Title search (public autocomplete used by the site):
  https://islamansiklopedisi.org.tr/ajax_search_auto.php?sp=aa&=ac&q=<query>   (sp=y: contributors)
Segments: one per article part (bölüm): seg "TDVIA:<slug>#<n>", with authors, the printed-volume line
("Bu madde ... 28. cildinde, 175-176 numaralı sayfalarda ...") and the site's citation text.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import urllib.parse

from ref_common import Source, ascii_fold, detect_challenge, html_to_text, slugify, tr_lower

BASE = "https://islamansiklopedisi.org.tr"
SID = "TDVIA"

SURAH_TR = """Fâtiha Bakara Âl-i_İmrân Nisâ Mâide En‘âm A‘râf Enfâl Tevbe Yûnus Hûd Yûsuf Ra‘d İbrâhîm Hicr Nahl
İsrâ Kehf Meryem Tâhâ Enbiyâ Hac Mü’minûn Nûr Furkān Şuarâ Neml Kasas Ankebût Rûm Lokmân Secde Ahzâb Sebe’
Fâtır Yâsîn Sâffât Sâd Zümer Mü’min Fussılet Şûrâ Zuhruf Duhân Câsiye Ahkāf Muhammed Fetih Hucurât Kāf Zâriyât
Tûr Necm Kamer Rahmân Vâkıa Hadîd Mücâdele Haşr Mümtehine Saf Cuma Münâfikūn Tegābün Talâk Tahrîm Mülk Kalem
Hâkka Meâric Nûh Cin Müzzemmil Müddessir Kıyâme İnsan Mürselât Nebe’ Nâziât Abese Tekvîr İnfitâr Mutaffifîn
İnşikāk Bürûc Târık A‘lâ Gāşiye Fecr Beled Şems Leyl Duhâ İnşirâh Tîn Alak Kadir Beyyine Zilzâl Âdiyât Kāria
Tekâsür Asr Hümeze Fîl Kureyş Mâûn Kevser Kâfirûn Nasr Tebbet İhlâs Felak Nâs""".split()
SURAH_TR = [n.replace("_", " ") for n in SURAH_TR]
assert len(SURAH_TR) == 114

BASE_META = {
    "id": SID,
    "title": "TDV İslâm Ansiklopedisi",
    "author": "various (signed articles; authors recorded per segment)",
    "death_ah": None,
    "kind": "reference",
    "tradition": "academic (Turkish Islamic studies), TDV/İSAM",
    "language": "tr",
    "edition": "online edition of the 44-vol. print encyclopaedia (1988–2013) + Ek 1–2 (2016); "
               "volume/page/year per article as printed on the site",
    "access": "yerel",
    "locator": "section",
    "licence": "© TDV İslâm Araştırmaları Merkezi; free to read online; citation requested in the site's "
               "format; local research copy only, no redistribution",
    "notes": "seg TDVIA:<slug>#<part>. Fields per segment: url, title, authors, printed (the site's 'Bu madde ... "
             "cildinde ... sayfalarda yer almıştır' line), vol, pages, year, pdf, cite. Surah articles carry s. "
             "Bibliography of each part is kept at the end of its text after 'BİBLİYOGRAFYA'.",
}


def _xhr():
    return {"X-Requested-With": "XMLHttpRequest", "Referer": BASE + "/"}


# ------------------------------------------------------------------ search / resolve
def search(src: Source, q: str, sp: str = "aa", refresh=False) -> list[dict]:
    url = f"{BASE}/ajax_search_auto.php?sp={sp}&=ac&q={urllib.parse.quote(q)}"
    rel = f"search/{sp}_{slugify(q) or 'q'}.html"
    st, body = src.fetch(url, rel, headers=_xhr(), refresh=refresh)
    h = body.decode("utf-8", "replace")
    out = []
    for m in re.finditer(r'<a href="/([^"#?]+)"><li><span class="sr-title">(.*?)</span>(.*?)</li></a>', h, re.S):
        slug, title, rest = m.group(1), html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).replace("\xa0", " "), m.group(3)
        see = re.search(r'bk\. <a href="/([^"]+)">', rest)
        desc = re.sub(r"\s+", " ", html_to_text(rest.replace("</span>", "</span> "))).strip()
        out.append({"slug": slug, "title": title.strip(), "see": see.group(1) if see else None, "desc": desc})
    return out


def _norm_title(t: str) -> str:
    t = re.sub(r"[؀-ۿ\s]+$", "", t)      # drop trailing Arabic title
    return re.sub(r"[^a-z0-9]+", " ", ascii_fold(t)).strip()


def _strict(t: str) -> str:
    t = re.sub(r"[\u0600-\u06FF]+", " ", t)
    return re.sub(r"\s+", " ", tr_lower(t)).strip()


def resolve_hit(src: Source, query: str, refresh=False) -> dict | None:
    """Pick the best title-search hit: exact title with diacritics, then folded exact, then prefix."""
    hits = search(src, query, refresh=refresh)
    qs, qn = _strict(query), _norm_title(query)
    tests = (lambda h: _strict(h["title"]) == qs,
             lambda h: _norm_title(h["title"]) == qn,
             lambda h: _norm_title(h["title"]).startswith(qn))
    for i, t in enumerate(tests):
        m = [h for h in hits if t(h)]
        if len(m) > 1 and i == 2:
            print(f"AMBIGUOUS '{query}': " + "; ".join(f"{h['slug']} ({h['title']})" for h in m) +
                  "  -> rerun with `slug <slug>` or the full headword", file=sys.stderr)
            return None
        if m:
            return m[0]
    if hits:
        print(f"'{query}': no title match; candidates: " + "; ".join(h["slug"] for h in hits), file=sys.stderr)
    return None


def resolve(src: Source, query: str, refresh=False) -> str | None:
    h = resolve_hit(src, query, refresh)
    return (h["see"] or h["slug"]) if h else None


def stub_segment(h: dict) -> dict:
    """A cross-reference entry ('X bk. Y') kept as a tiny segment so the gloss is not lost."""
    return {"seg": f"{SID}:{h['slug']}#stub", "s": None, "a": None, "a_end": None, "page": None,
            "head": h["title"], "text": h["desc"], "url": f"{BASE}/{h['slug']}", "title": h["title"],
            "see": h["see"], "kind_of_article": "cross-reference"}


# ------------------------------------------------------------------ article parse
def fetch_article(src: Source, slug: str, refresh=False) -> tuple[int, str]:
    st, body = src.fetch(f"{BASE}/{slug}", f"article/{slug}.html", refresh=refresh)
    if detect_challenge(body):
        raise SystemExit(f"{slug}: bot challenge page received -- stopping (recorded in raw/)")
    return st, body.decode("utf-8", "replace")


def parse_article(slug: str, h: str, s: int | None = None) -> list[dict]:
    tm = re.search(r'<div class="article_title"><h1>(.*?)</h1>', h, re.S)
    if not tm:
        return []
    title = html_to_text(tm.group(1))
    am = re.search(r'<div class="arabic_title">(.*?)</div>', h, re.S)
    arabic = html_to_text(am.group(1)) if am else None
    im = re.search(r'<div class="article_info"><h2>(.*?)</h2>', h, re.S)
    gloss = html_to_text(im.group(1)) if im else None
    starts = [(m.start(), m.group(1)) for m in re.finditer(r'<div class="article-part" id="_([^"]*)"', h)]
    segs = []
    for i, (pos, pid) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(h)
        chunk = h[pos:end]
        n = int(re.match(r"\d+", pid).group(0)) if re.match(r"\d+", pid) else i + 1
        authors = [html_to_text(a) for a in re.findall(r"<span class='val'>(.*?)</span>",
                   (re.search(r'<div class="ak-muellif">(.*?)</div>', chunk, re.S) or [None, ""])[1] or "", re.S)]
        if not authors:
            authors = [html_to_text(a) for a in re.findall(r'href="/muellif/[^"]*"><b>(.*?)</b>', chunk)]
        cite = re.search(r'<div class="ak-copytext"[^>]*>(.*?)</div>', chunk, re.S)
        cite = re.sub(r"\s*\(\d\d\.\d\d\.\d{4}\)\.?\s*$", "", html_to_text(cite.group(1))) if cite else None
        bm = re.search(r"Baskı Tarihi: </b><span class=\"val\">(.*?)</span>", chunk)
        printed = re.search(r"((?:Bu madde|Maddenin bu bölümü) TDV İslâm Ansiklopedisi[^<]*?yer almıştır\.)", chunk)
        printed = re.sub(r"\s+", " ", printed.group(1)).strip() if printed else None
        vol = pages = year = None
        if printed:
            pm = re.search(r"(\d{4}) yılında.*?basılan (.*?) cildinde, ([\d\-–]+) numaralı", printed)
            if pm:
                year, vol, pages = pm.group(1), pm.group(2).strip().rstrip("."), pm.group(3)
        pdf = re.search(r'class="dosyaindir" href="([^"]+\.pdf)"', chunk)
        cm = re.search(r'<div class="m-content"[^>]*>(.*?)<div class="article-ps"', chunk, re.S) or \
            re.search(r'<div class="m-content"[^>]*>(.*)', chunk, re.S)
        body = cm.group(1) if cm else ""
        body = body.replace("<bibl>", "<bibl>\n\n")
        text = html_to_text(body)
        hm = re.match(r"\s*(?:<p>\s*<b>|<b>\s*<p>)(.*?)</b>", body, re.S)
        head = html_to_text(hm.group(1)) if hm else title
        if len(head) > 160:
            head = head[:157] + "…"
        segs.append({
            "seg": f"{SID}:{slug}#{n}", "s": s, "a": None, "a_end": None, "page": pages,
            "head": head if head == title else f"{title} — {head}",
            "text": text,
            "url": f"{BASE}/{slug}" + (f"#{pid}" if len(starts) > 1 else ""),
            "title": title, "arabic_title": arabic, "gloss": gloss,
            "part": n, "parts": len(starts), "authors": authors,
            "printed": printed, "vol": vol, "pages": pages, "year": year or (bm.group(1) if bm else None),
            "pdf": pdf.group(1) if pdf else None, "cite": cite,
        })
    return segs


TR_UNITS = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
TR_UNITS_ORD = ["", "birinci", "ikinci", "üçüncü", "dördüncü", "beşinci", "altıncı", "yedinci", "sekizinci", "dokuzuncu"]
TR_TENS = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
TR_TENS_ORD = ["", "onuncu", "yirminci", "otuzuncu", "kırkıncı", "ellinci", "altmışıncı", "yetmişinci", "sekseninci", "doksanıncı"]


def tr_ordinal(n: int) -> str:
    h, t, u = n // 100, (n // 10) % 10, n % 10
    if n == 100:
        return "yüzüncü"
    parts = ["yüz"] if h else []
    if u:
        if t:
            parts.append(TR_TENS[t])
        parts.append(TR_UNITS_ORD[u])
    elif t:
        parts.append(TR_TENS_ORD[t])
    return " ".join(parts)


def surah_slug_guess(n: int) -> str:
    return slugify(SURAH_TR[n - 1]) + "-suresi"


def do_surah(src: Source, n: int, refresh=False) -> list[dict]:
    slug = surah_slug_guess(n)
    st, h = fetch_article(src, slug, refresh)
    segs = parse_article(slug, h, s=n) if st == 200 else []
    if not segs or "SÛRESİ" not in segs[0]["title"]:
        alt = resolve(src, f"{SURAH_TR[n - 1]} sûresi", refresh)
        if not alt:
            print(f"S{n}: no article found (guess {slug})", file=sys.stderr)
            return []
        slug = alt
        st, h = fetch_article(src, slug, refresh)
        segs = parse_article(slug, h, s=n)
    gloss = (segs[0].get("gloss") or "") if segs else ""
    if segs and tr_ordinal(n) not in tr_lower(gloss) and not (n == 1 and "ilk" in tr_lower(gloss)):
        print(f"WARNING S{n}: {slug} gloss '{gloss}' lacks ordinal '{tr_ordinal(n)}'", file=sys.stderr)
    for s in segs:
        s["kind_of_article"] = "surah"
    return segs


def do_slug(src: Source, slug: str, kind: str, refresh=False, s=None) -> list[dict]:
    st, h = fetch_article(src, slug, refresh)
    if st != 200:
        print(f"{slug}: HTTP {st}", file=sys.stderr)
        return []
    segs = parse_article(slug, h, s=s)
    for x in segs:
        x["kind_of_article"] = kind
    return segs


def parse_nums(items):
    out = []
    for it in items:
        if "-" in it:
            a, b = it.split("-")
            out += list(range(int(a), int(b) + 1))
        else:
            out.append(int(it))
    return out


def reparse(src: Source):
    """Rebuild all segments from cached raw/article/*.html (no network)."""
    old = {s["seg"].split("#")[0]: s for s in src.load_segments()}
    segs = [s for s in src.load_segments() if s["seg"].endswith("#stub")]
    for p in sorted((src.raw / "article").glob("*.html")):
        slug = p.stem
        o = old.get(f"{SID}:{slug}", {})
        segs += [dict(x, kind_of_article=o.get("kind_of_article")) for x in
                 parse_article(slug, p.read_text(encoding="utf-8"), s=o.get("s"))]
    return segs


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["surah", "term", "author", "slug", "reparse", "drop"])
    ap.add_argument("items", nargs="*")
    ap.add_argument("--refresh", action="store_true", help="re-fetch even if cached")
    a = ap.parse_args()
    src = Source(SID)
    allsegs = []
    if a.mode == "surah":
        for n in parse_nums(a.items):
            segs = do_surah(src, n, a.refresh)
            if segs:
                src.upsert_segments(segs, drop_prefix=segs[0]["seg"].split("#")[0] + "#")
                print(f"S{n}: {segs[0]['seg'].split('#')[0]}  parts={len(segs)}  {segs[0]['printed'] or ''}")
            allsegs += segs
    elif a.mode in ("term", "author", "slug"):
        for q in a.items:
            hit = None if a.mode == "slug" else resolve_hit(src, q, a.refresh)
            slug = q if a.mode == "slug" else (hit and (hit["see"] or hit["slug"]))
            if hit and hit["see"]:
                src.upsert_segments([stub_segment(hit)])
            if not slug:
                print(f"{q}: not found in title search", file=sys.stderr)
                continue
            segs = do_slug(src, slug, a.mode if a.mode != "slug" else "article", a.refresh)
            if segs:
                src.upsert_segments(segs, drop_prefix=f"{SID}:{slug}#")
                print(f"{q} -> {slug}  parts={len(segs)}  authors={sorted({x for s in segs for x in s['authors']})}")
            allsegs += segs
    elif a.mode == "drop":
        for slug in a.items:
            (src.raw / "article" / f"{slug}.html").unlink(missing_ok=True)
            lines = [l for l in src.log_path.read_text(encoding="utf-8").splitlines()
                     if json.loads(l)["path"] != f"article/{slug}.html"]
            src.log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            src.upsert_segments([], drop_prefix=f"{SID}:{slug}#")
            sj = json.loads((src.dir / "source.json").read_text(encoding="utf-8"))
            sj.get("articles", {}).pop(slug, None)
            (src.dir / "source.json").write_text(json.dumps(sj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"dropped {slug}")
        src._log = src._read_log()
    else:
        allsegs = reparse(src)
        src.segments_path().unlink(missing_ok=True)
        src.upsert_segments(allsegs)
        print(f"reparsed {len(allsegs)} segments")
    arts = {}
    for s in src.load_segments():
        if s["seg"].endswith("#stub"):
            continue
        k = s["seg"].split("#")[0].split(":", 1)[1]
        e = arts.setdefault(k, {"title": s.get("title"), "s": s.get("s"), "kind": s.get("kind_of_article"),
                                "url": s.get("url", "").split("#")[0], "parts": s.get("parts"), "authors": [],
                                "printed": []})
        for x in s.get("authors") or []:
            if x not in e["authors"]:
                e["authors"].append(x)
        if s.get("printed") and s["printed"] not in e["printed"]:
            e["printed"].append(s["printed"])
    surahs = sorted({v["s"] for v in arts.values() if v["s"]})
    src.update_source(dict(BASE_META, coverage=f"surah articles: {','.join(map(str, surahs))}; "
                                               f"{sum(1 for v in arts.values() if not v['s'])} term/author articles"),
                      urls=[BASE], extra={"articles": arts})


if __name__ == "__main__":
    main()
