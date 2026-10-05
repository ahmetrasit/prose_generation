#!/usr/bin/env python3
"""A book from a Shamela desktop export (.bok, an MS Access database) held on archive.org, one segment per page.
User, 2026-10-05: Fāḍil al-Sāmarrāʾī counts in the bayānī line; .bok exports read with the pure-Python
access-parser (Homebrew's mdbtools would have rebuilt 12 packages from source on this Intel Mac and upgraded
python/sqlite/openssl: not done). Run with an interpreter that has access-parser, e.g. a venv:

  python3 -m venv /tmp/bokenv && /tmp/bokenv/bin/pip install access-parser
  /tmp/bokenv/bin/python -B enrichment/v2/fetch/import_shamela_bok.py SAMARRAI-LAMASAT alfirdwsiy2018_gmail_6040

The .bok's tables: Main (the book card), b<id> (pages: id, part, page, nass), t<id> (headings: id, tit). Text is
Windows-1256 read as Latin-1 by the parser: re-decoded. Segments <ID>:p<page> (v<part>p<page> for several parts;
#n when Shamela repeats a page number), `head` = the heading in force, tied to the surah a heading names («سورة
الفاتحة», «من سورة المائدة») on the verses the page quotes (else the heading's surah whole); `refs` = every ayah
quoted (skeleton match) or named. source.json is written from the book card if missing.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_common as IC  # noqa: E402
import import_bintshati as BS  # noqa: E402

UA = "quran-enrichment-research/1.0 (local research; ozturk.ahmetr@gmail.com)"


def fix(v) -> str:
    s = "" if v is None or str(v) == "None" else str(v)
    try:
        return s.encode("latin-1").decode("cp1256")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return s


def fetch(item: str, dest: Path) -> tuple[Path, dict]:
    meta = json.load(urllib.request.urlopen(f"https://archive.org/metadata/{item}"))
    f = [x for x in meta["files"] if x["name"].lower().endswith((".zip", ".bok"))][0]
    zp = dest / f"{item}{Path(f['name']).suffix.lower()}"
    if not zp.exists():
        data = urllib.request.urlopen(urllib.request.Request(
            f"https://archive.org/download/{item}/" + urllib.parse.quote(f["name"]), headers={"User-Agent": UA})).read()
        if str(len(data)) != str(f.get("size")) or hashlib.md5(data).hexdigest() != f.get("md5"):
            raise SystemExit(f"{item}: size/md5 differ from archive.org's file list; not used")
        zp.write_bytes(data)
    if zp.suffix == ".bok":
        return zp, meta
    z = zipfile.ZipFile(zp)
    boks = [i for i in z.infolist() if i.filename.lower().endswith(".bok")]
    if len(boks) != 1:
        raise SystemExit(f"{item}: {len(boks)} .bok files in the zip")
    out = dest / f"{item}.bok"
    out.write_bytes(z.read(boks[0]))
    return out, meta


def surah_of(title: str, names: dict[str, int]) -> int | None:
    m = re.search(r"سورة\s+(\S+(?:\s+\S+)?)", title)
    if not m:
        return None
    for cand in (m.group(1), m.group(1).split()[0]):
        c = re.sub("[أإآ]", "ا", cand).strip("()«»:،.")
        s = names.get(c) or names.get("ال" + c)
        if s:
            return s
    return None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sid")
    ap.add_argument("item", help="archive.org item holding the .bok (zipped or not)")
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    from access_parser import AccessParser
    d = IC.CORPUS / a.sid
    raw = d / "raw" / "acquired-2026-10-05"
    raw.mkdir(parents=True, exist_ok=True)
    bok, meta = fetch(a.item, raw)
    db = AccessParser(str(bok))
    bt = [t for t in db.catalog if re.fullmatch(r"b\d+", t)]
    tt = [t for t in db.catalog if re.fullmatch(r"t\d+", t)]
    if len(bt) != 1:
        raise SystemExit(f"page tables: {bt}")
    pages = db.parse_table(bt[0])
    heads = db.parse_table(tt[0]) if tt else {"id": [], "tit": []}
    card = {k: fix(v[0]) for k, v in db.parse_table("Main").items()}
    rows = sorted(zip(map(int, pages["id"]), pages["part"], pages["page"], pages["nass"]), key=lambda r: r[0])
    hl = sorted((int(i), fix(t).strip()) for i, t in zip(heads["id"], heads["tit"]))
    import biqai_intros
    names, _ = biqai_intros.names_and_lengths()
    q = BS.quran_index()
    counts = IC.ayah_counts()
    parts = {str(r[1]) for r in rows}
    # «[الكتاب مرقم آليا]»: Shamela numbered the pages itself; they are not the print's pages
    auto = "مرقم آليا" in card.get("Betaka", "")
    page_key = "shamela_page" if auto else "printed_page"
    segs, seen, n_in = [], set(), 0
    last_verse: dict[int, int] = {}
    for rid, part, page, nass in rows:
        text = fix(nass).replace("\r", "\n").strip()
        n_in += len(re.sub(r"\s", "", text))
        h = [t for i, t in hl if i <= rid]
        head = h[-1] if h else ""
        paged = str(page).isdigit()
        loc = f"{a.sid}:" + ((f"v{part}p{page}" if len(parts) > 1 else f"p{page}") if paged else f"r{rid}")
        if loc in seen:
            k = 2
            while f"{loc}#{k}" in seen:
                k += 1
            loc = f"{loc}#{k}"
        seen.add(loc)
        s_head = surah_of(head, names)
        hits = BS.quoted(text, q, s_head or 0)
        hits += [x for x in BS.named_refs(text, names) if x not in hits]
        g = {"seg": loc, page_key: int(page) if str(page).isdigit() else page, "head": head, "text": text,
             "text_status": "Shamela digital edition (typed); not checked against a scan of the print",
             "shamela_record": rid, "refs": [f"{s}:{v}" for s, v in hits]}
        if s_head:
            own = sorted(v for s, v in hits if s == s_head)
            if own:
                lo = min(own[0], last_verse.get(s_head, own[0]))
                g.update({"s": s_head, "a": lo if lo >= own[0] - 3 else own[0], "a_end": own[-1]})
                last_verse[s_head] = own[-1]
            elif s_head in last_verse:
                g.update({"s": s_head, "a": last_verse[s_head], "a_end": last_verse[s_head]})
            else:
                g.update({"s": s_head, "a": 1, "a_end": counts[s_head]})
        if len(text) > 8000:  # an unpaginated section: cut at paragraph ends into pieces of at most 8,000 characters
            pieces, cur = [], ""
            for para in text.split("\n"):
                if cur and len(cur) + len(para) + 1 > 8000:
                    pieces.append(cur)
                    cur = ""
                cur = cur + "\n" + para if cur else para
            pieces.append(cur)
            for k, piece in enumerate(pieces, 1):
                hk = BS.quoted(piece, q, s_head or 0)
                hk += [x for x in BS.named_refs(piece, names) if x not in hk]
                segs.append({**g, "seg": g["seg"] + (f"#{k}" if k > 1 else ""), "text": piece,
                             "refs": [f"{s}:{v}" for s, v in hk], "piece": f"{k}/{len(pieces)}"})
            continue
        segs.append(g)
    n_out = sum(len(re.sub(r"\s", "", g["text"])) for g in segs)
    tied = sum(1 for g in segs if g.get("s"))
    print(f"{a.sid}: {card.get('Bk')} — {len(rows)} pages, {len(hl)} headings, parts {sorted(parts)}; tied {tied}, "
          f"refs {sum(len(g['refs']) for g in segs)}; characters in {n_in:,} out {n_out:,}")
    print("headings:", [t for _, t in hl][:20])
    if n_in != n_out:
        raise SystemExit("character count differs: refusing to write")
    if a.dry:
        return
    if not (d / "source.json").exists():
        src = {"id": a.sid, "title": card.get("Bk"), "author": card.get("Auth"), "death_ah": None, "kind": "modern",
               "tradition": "bayani", "language": "ar", "access": "hafiza", "locator": "page",
               "edition": card.get("Betaka", "").split("\n")[2:4] and " ".join(
                   x.strip() for x in card.get("Betaka", "").splitlines()[2:5]),
               "coverage": "whole book by page; cited ayat in refs", "urls": [f"https://archive.org/details/{a.item}"],
               "fetched_at": "2026-10-05", "panel": False,
               "licence": "in copyright; local research copy only (user, 2026-10-05: licence is no barrier)",
               "notes": "Fāḍil al-Sāmarrāʾī, bayānī line (user, 2026-10-05: counts in the bayānī voices). Shamela "
                        "card: " + card.get("Betaka", "")[:600]}
        (d / "source.json").write_text(json.dumps(src, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    IC.write(a.sid, segs, {
        "script": f"enrichment/v2/fetch/import_shamela_bok.py {a.sid} {a.item}",
        "from": {str(bok.relative_to(d)): IC.C.sha256(bok)},
        "method": "Shamela .bok (MS Access) read with access-parser, cp1256 re-decoded; one segment per page; ties "
                  "from surah headings and the verses quoted",
        "text_status": "typed digital edition, not checked against a scan", "characters": n_out,
        "shamela_card": card.get("Betaka", ""),
        "page_numbers": "Shamela's own numbering (not the print)" if auto else "the print's pages (per Shamela)",
    })


if __name__ == "__main__":
    main()
