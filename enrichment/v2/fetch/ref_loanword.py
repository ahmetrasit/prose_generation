#!/usr/bin/env python3
"""Turkish loanword history: Nişanyan Sözlük, Kubbealtı Lugatı, TDK Güncel Türkçe Sözlük (+ Tarama: blocked).

  ref_loanword.py kalp sadr gönül                     all available sources
  ref_loanword.py kalp --sources nisanyan,tdk         subset (nisanyan, kubbealti, tdk, tarama)
  ref_loanword.py --seed                              the seed list below
  ref_loanword.py --reparse                           rebuild all segments from raw/ (no network)

Sources / URL schemes (all public pages that the sites' own front-ends use):
  NISANYAN   https://www.nisanyansozluk.com/kelime/<word>   HTML; entry data embedded in the SvelteKit payload
             (robots.txt disallows /api/ — not used).  segs NISANYAN:<entry name>   (e.g. kalp, kalp2)
  KUBBEALTI  https://eski.lugatim.com/rest/s/<word>[/<page>] JSON used by https://lugatim.com (React app).
             segs KUBBEALTI:<headword>[#n]
  TDK        https://sozluk.gov.tr/gts?ara=<word>           legacy public JSON of the Güncel Türkçe Sözlük.
             segs TDK:<madde>[#n]
  TARAMA     Tarama Sözlüğü (and Derleme, Etimolojik, Köken Bilgisi, Osmanlıca) are only served by
             https://api.sozluk.gov.tr/<ts|ds|etms|koken-bilgisi|osmanlica>?ara=..., which answers 403
             "Bu API yalnızca yetkili web arayüzünden erişilebilir." -> blocked; recorded, not bypassed.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import urllib.parse

from ref_common import Source, ascii_fold, deaccent, detect_challenge, html_to_text, slugify, tr_lower

SEED = ("kalp sadr göğüs gönül namaz salât ibadet din âlem rab zekât sadaka yetim miskin riya gaflet sehv mâûn "
        "takva iman küfür şirk rahmet hamd").split()

META = {
    "NISANYAN": {
        "id": "NISANYAN", "title": "Nişanyan Sözlük — Çağdaş Türkçenin Etimolojisi (online)",
        "author": "Sevan Nişanyan", "death_ah": None, "kind": "lexicon", "tradition": "etymological dictionary (Turkish)",
        "language": "tr", "edition": "online edition nisanyansozluk.com (continuously updated; timeUpdated per entry)",
        "access": "yerel", "locator": "entry", "urls": ["https://www.nisanyansozluk.com/"],
        "licence": "© Sevan Nişanyan 2002–; entries freely readable online (no login needed for the fields cached); "
                   "'Alıntılarda kaynak gösterilmesi rica olunur'. robots.txt disallows /api/ (not used). "
                   "Local research copy only.",
        "notes": "One segment per homonym entry (kalp, kalp2 …). Fields: first_attested (earliest dated main "
                 "attestation), histories (dated attestations: date, source, quote, sense), frequency (site's "
                 "1945/2017 frequency figures as given), time_updated. Text renders etymology, notes, dated "
                 "attestations of the word and of derived phrases.",
    },
    "KUBBEALTI": {
        "id": "KUBBEALTI", "title": "Kubbealtı Lugatı — Misalli Büyük Türkçe Sözlük (online)",
        "author": "İlhan Ayverdi (Kubbealtı Akademisi Kültür ve San'at Vakfı)", "death_ah": None, "kind": "lexicon",
        "tradition": "Ottoman/Turkish literary dictionary with dated literary examples", "language": "tr",
        "edition": "online lugatim.com, data version ('sürüm') per entry, e.g. 2023-01",
        "access": "yerel", "locator": "entry", "urls": ["https://lugatim.com/", "https://eski.lugatim.com/rest/s/"],
        "licence": "© Kubbealtı Vakfı, 'Her hakkı mahfuzdur'; freely searchable online; local research copy only.",
        "notes": "Headword match: exact (with diacritics) first, else accent-folded. Text = senses with literary "
                 "examples and attributed authors (useful for Ottoman-era senses).",
    },
    "TDK": {
        "id": "TDK", "title": "TDK Güncel Türkçe Sözlük", "author": "Türk Dil Kurumu", "death_ah": None,
        "kind": "lexicon", "tradition": "standard modern Turkish dictionary", "language": "tr",
        "edition": "online GTS (legacy JSON endpoint sozluk.gov.tr/gts)", "access": "yerel", "locator": "entry",
        "urls": ["https://sozluk.gov.tr/gts?ara=<word>"],
        "licence": "© Türk Dil Kurumu; public online dictionary; local research copy only.",
        "notes": "Fields: lisan (origin language + source form as TDK gives it), senses with examples. Modern "
                 "senses only — no dated history. Historical TDK dictionaries: see TARAMA (blocked).",
    },
    "TARAMA": {
        "id": "TARAMA", "title": "TDK Tarama Sözlüğü (XIII. yüzyıldan beri Türkiye Türkçesiyle yazılmış kitaplardan "
                                 "toplanan tanıklarıyla)", "author": "Türk Dil Kurumu", "death_ah": None,
        "kind": "lexicon", "tradition": "historical Old Anatolian/Ottoman Turkish dictionary with dated attestations",
        "language": "tr", "edition": "online via sozluk.gov.tr (Tarama Sözlüğü, TS)", "access": "hafiza",
        "locator": "entry", "urls": ["https://sozluk.gov.tr/ (Tarama Sözlüğü tab)",
                                     "https://api.sozluk.gov.tr/ts?ara=<word>"],
        "licence": "© Türk Dil Kurumu.",
        "notes": "BLOCKED (2026-10-03): the new sozluk.gov.tr front-end loads all dictionaries other than GTS from "
                 "https://api.sozluk.gov.tr/<ts|ds|yeni-derleme|etms|koken-bilgisi|osmanlica>?ara=<w>, which returns "
                 "HTTP 403 {\"error\":\"FORBIDDEN\",\"message\":\"Bu API yalnızca yetkili web arayüzünden "
                 "erişilebilir.\"} to non-browser clients. The legacy sozluk.gov.tr/<ts|...>?ara= paths now return the "
                 "SPA shell. Not bypassed (no header spoofing). Evidence cached in raw/. Same block applies to "
                 "Derleme Sözlüğü, Türk Dilinin Etimolojik Sözlüğü (ETMS), Köken Bilgisi Sözlüğü and Osmanlı Türkçesi "
                 "Sözlüğü. Options: read in a browser and cite by hand; or the printed Tarama Sözlüğü (8 vols, TDK "
                 "1963–1977).",
    },
}


# ---------------------------------------------------------------- JS literal (devalue/uneval) parser
class _Ref:
    def __init__(self, name):
        self.name = name


def _subst(v, env):
    if isinstance(v, _Ref):
        return env[v.name]
    if isinstance(v, list):
        return [_subst(x, env) for x in v]
    if isinstance(v, dict):
        return {k: _subst(x, env) for k, x in v.items()}
    return v


class JSLit:
    """Parser for the JS object literals SvelteKit/devalue emits (unquoted keys, new Date(..), void 0,
    and the IIFE form `(function(a,b){return EXPR}(ARG1,ARG2))` used for repeated values)."""

    def __init__(self, s):
        self.s, self.i = s, 0
        self.scope = set()

    def expect(self, ch):
        self.ws()
        assert self.s[self.i] == ch, f"expected {ch!r} at {self.s[self.i:self.i + 40]!r}"
        self.i += 1

    def paren(self):
        self.i += 1
        self.ws()
        if self.s.startswith("function", self.i):
            self.i += len("function")
            self.expect("(")
            params = []
            while True:
                self.ws()
                if self.s[self.i] == ")":
                    self.i += 1
                    break
                m = re.compile(r"[A-Za-z_$][\w$]*").match(self.s, self.i)
                params.append(m.group(0))
                self.i = m.end()
                self.ws()
                if self.s[self.i] == ",":
                    self.i += 1
            self.expect("{")
            self.ws()
            assert self.s.startswith("return", self.i)
            self.i += len("return")
            saved = self.scope
            self.scope = saved | set(params)
            body = self.parse()
            self.scope = saved
            self.ws()
            if self.s[self.i] == ";":
                self.i += 1
            self.expect("}")
            self.expect("(")
            args = []
            while True:
                self.ws()
                if self.s[self.i] == ")":
                    self.i += 1
                    break
                args.append(self.parse())
                self.ws()
                if self.s[self.i] == ",":
                    self.i += 1
            val = _subst(body, dict(zip(params, args)))
        else:
            val = self.parse()
        self.expect(")")
        return val

    def ws(self):
        while self.i < len(self.s) and self.s[self.i] in " \t\r\n":
            self.i += 1

    def parse(self):
        self.ws()
        c = self.s[self.i]
        if c == "{":
            return self.obj()
        if c == "[":
            return self.arr()
        if c in "\"'":
            return self.string()
        if c == "(":
            return self.paren()
        if c in "-." or c.isdigit():
            m = re.compile(r"-?(?:\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?").match(self.s, self.i)
            self.i = m.end()
            t = m.group(0)
            return int(t) if re.fullmatch(r"-?\d+", t) else float(t)
        m = re.compile(r"[A-Za-z_$][\w$]*").match(self.s, self.i)
        if not m:
            raise ValueError(f"unexpected {self.s[self.i:self.i + 30]!r}")
        w = m.group(0)
        self.i = m.end()
        if w in self.scope:
            return _Ref(w)
        if w in ("true", "false"):
            return w == "true"
        if w in ("null", "undefined"):
            return None
        if w == "void":
            self.ws()
            self.parse()
            return None
        if w in ("NaN", "Infinity"):
            return None
        if w == "new":
            self.ws()
            m = re.compile(r"[A-Za-z_$][\w$]*").match(self.s, self.i)
            cls = m.group(0)
            self.i = m.end()
            self.ws()
            assert self.s[self.i] == "("
            self.i += 1
            self.ws()
            arg = None if self.s[self.i] == ")" else self.parse()
            self.ws()
            assert self.s[self.i] == ")"
            self.i += 1
            if cls == "Date" and isinstance(arg, (int, float)):
                return dt.datetime.fromtimestamp(arg / 1000, dt.timezone.utc).isoformat(timespec="seconds")
            return arg
        raise ValueError(f"unsupported identifier {w!r} at {self.i}")

    def string(self):
        q = self.s[self.i]
        j = self.i + 1
        buf = []
        while self.s[j] != q:
            if self.s[j] == "\\":
                buf.append(self.s[j:j + 2])
                j += 2
            else:
                buf.append(self.s[j])
                j += 1
        self.i = j + 1
        raw = "".join(buf)
        if q == "'":
            raw = raw.replace("\\'", "'").replace('"', '\\"')
        return json.loads('"' + raw + '"')

    def obj(self):
        self.i += 1
        out = {}
        while True:
            self.ws()
            if self.s[self.i] == "}":
                self.i += 1
                return out
            if self.s[self.i] in "\"'":
                k = self.string()
            else:
                m = re.compile(r"[\w$]+").match(self.s, self.i)
                k = m.group(0)
                self.i = m.end()
            self.ws()
            assert self.s[self.i] == ":", self.s[self.i:self.i + 40]
            self.i += 1
            out[k] = self.parse()
            self.ws()
            if self.s[self.i] == ",":
                self.i += 1

    def arr(self):
        self.i += 1
        out = []
        while True:
            self.ws()
            if self.s[self.i] == "]":
                self.i += 1
                return out
            out.append(self.parse())
            self.ws()
            if self.s[self.i] == ",":
                self.i += 1


def nodes_text(nodes) -> str:
    if nodes is None:
        return ""
    if isinstance(nodes, dict):
        nodes = [nodes]
    out = []
    for n in nodes:
        if isinstance(n, list):
            out.append(nodes_text(n))
        elif isinstance(n, dict):
            if "text" in n and isinstance(n["text"], str):
                out.append(n["text"])
            if n.get("children"):
                out.append(nodes_text(n["children"]))
        elif isinstance(n, str):
            out.append(n)
    return re.sub(r"\s+", " ", "".join(out)).strip()


# ---------------------------------------------------------------- NISANYAN
def nis_payload(h: str):
    for m in re.finditer(r"\.resolve\(2,\s*\(\)\s*=>\s*", h):
        p = JSLit(h)
        p.i = m.end()
        return p.parse()
    return None


def nis_entry_segments(e: dict) -> dict:
    name = e["name"]
    lines = [f"{name} — Nişanyan Sözlük"]
    ety = [nodes_text(par) for par in (e.get("etymologyNodes") or [])]
    if ety:
        lines.append("Köken: " + " ".join(x for x in ety if x))
    notes = [nodes_text(par) for par in (e.get("noteNodes") or [])]
    if any(notes):
        lines.append("Ek açıklama: " + " ".join(x for x in notes if x))
    hist = []
    for h in e.get("mainHistories") or []:
        src = h.get("source") or {}
        sname = " / ".join(x for x in (src.get("name"), src.get("book")) if x) or src.get("abbreviation")
        d = h.get("definition") or {}
        sense = nodes_text(d.get("quotedNodes")) if d else ""
        par = nodes_text(d.get("parentheticalNodes")) if d else ""
        hist.append({"date": h.get("date"), "source": sname, "abbr": src.get("abbreviation"),
                     "form": h.get("form") or None, "language": nodes_text(h.get("languageNode")) or None,
                     "quote": nodes_text(h.get("quoteNodes")), "sense": sense or None, "sense_note": par or None})
    if hist:
        lines.append("Tarihçe (tarihli tanıklar):")
        for x in hist:
            s = f"- {x['date']} {x['source']}: “{x['quote']}”"
            if x["sense"]:
                s += f" [anlam: “{x['sense']}”{(' ' + x['sense_note']) if x['sense_note'] else ''}]"
            if x["language"] or x["form"]:
                s += f" ({' '.join(y for y in (x['language'], x['form']) if y)})"
            lines.append(s)
    ph = []
    for h in e.get("phraseHistories") or []:
        src = h.get("source") or {}
        sname = " / ".join(x for x in (src.get("name"), src.get("book")) if x) or src.get("abbreviation")
        ph.append(f"- {(h.get('phrase') or {}).get('name')}: {h.get('date')} {sname}: “{nodes_text(h.get('quoteNodes'))}”")
    if ph:
        lines.append("Birleşik/türev tanıkları:")
        lines += ph
    nh = [p.get("name") for p in (e.get("noHistoryPhrases") or [])]
    if nh:
        lines.append("Diğer birleşik/türevler: " + ", ".join(nh))
    refs = [r.get("name") for r in (e.get("references") or []) if isinstance(r, dict)]
    if refs:
        lines.append("Bkz.: " + ", ".join(refs))
    ro = [r.get("name") for r in (e.get("referenceOf") or []) if isinstance(r, dict)]
    if ro:
        lines.append("Bu maddeden türeyenler: " + ", ".join(ro))
    dates = [int(re.match(r"\d+", x["date"]).group(0)) for x in hist if x["date"] and re.match(r"\d+", x["date"])]
    return {"seg": f"NISANYAN:{name}", "s": None, "a": None, "a_end": None, "page": None, "head": name,
            "text": "\n".join(lines), "first_attested": min(dates) if dates else None, "histories": hist,
            "frequency": e.get("frequency"), "time_updated": e.get("timeUpdated"),
            "url": f"https://www.nisanyansozluk.com/kelime/{urllib.parse.quote(name)}"}


def nisanyan(word: str, refresh=False, offline=False):
    src = Source("NISANYAN")
    tried = []
    for w in dict.fromkeys([word, deaccent(word)]):
        rel = f"kelime/{slugify(w) or 'w'}__{urllib.parse.quote(w, safe='')}.html"
        url = f"https://www.nisanyansozluk.com/kelime/{urllib.parse.quote(w)}"
        if offline and not src.cached(rel):
            continue
        st, body = src.fetch(url, rel, refresh=refresh)
        if detect_challenge(body):
            return src, [], f"challenge page at {url} -- stopped"
        data = nis_payload(body.decode("utf-8", "replace"))
        d = data[0] if isinstance(data, list) and data else {}
        if d.get("error"):
            tried.append(f"{w}: {d['error']} (suggestions: {', '.join((d.get('data') or {}).get('suggestions', [])[:10])})")
            continue
        entries = d.get("data") or []
        segs = [nis_entry_segments(e) for e in entries]
        for s in segs:
            s["query"] = word
        return src, segs, None
    return src, [], "; ".join(tried) or "not fetched"


# ---------------------------------------------------------------- KUBBEALTI
def kub_head_variants(k: str):
    return [v.strip() for v in re.split(r"\s+[–-]\s+|,", k) if v.strip()]


def kubbealti(word: str, refresh=False, offline=False):
    src = Source("KUBBEALTI")
    q = deaccent(tr_lower(word))
    content, pages = [], 1
    for page in (1, 2, 3):
        if page > pages:
            break
        path = f"s/{urllib.parse.quote(q)}" + (f"/{page}" if page > 1 else "")
        rel = f"s/{slugify(q)}__p{page}.json"
        if offline and not src.cached(rel):
            break
        st, body = src.fetch(f"https://eski.lugatim.com/rest/{path}", rel, refresh=refresh)
        if st != 200:
            return src, [], f"HTTP {st}"
        d = json.loads(body)
        pages = d.get("totalPages") or 1
        content += d.get("content") or []
        strict = [c for c in content if any(tr_lower(v) == tr_lower(word) for v in kub_head_variants(c["kelime"]))]
        folded = [c for c in content if any(ascii_fold(v) == ascii_fold(word) for v in kub_head_variants(c["kelime"]))]
        if strict or (folded and page == pages):
            break
    hits = strict or folded
    segs = []
    for i, c in enumerate(hits, 1):
        head = c["kelime"].strip()
        seg = f"KUBBEALTI:{tr_lower(kub_head_variants(head)[0])}" + (f"#{i}" if len(hits) > 1 else "")
        segs.append({"seg": seg, "s": None, "a": None, "a_end": None, "page": None, "head": head,
                     "text": f"{head}\n" + html_to_text(c.get("anlam") or ""), "query": word, "kub_id": c.get("id"),
                     "version": ((c.get("surum") or {}).get("value") or "").strip() or None,
                     "url": f"https://lugatim.com/s/{urllib.parse.quote(tr_lower(head.split(' – ')[0]))}"})
    return src, segs, None if segs else f"no headword match among {[c['kelime'] for c in content][:15]}"


# ---------------------------------------------------------------- TDK GTS
def tdk(word: str, refresh=False, offline=False):
    src = Source("TDK")
    tried = []
    for w in dict.fromkeys([word, deaccent(word)]):
        rel = f"gts/{slugify(w)}__{urllib.parse.quote(w, safe='')}.json"
        if offline and not src.cached(rel):
            continue
        st, body = src.fetch(f"https://sozluk.gov.tr/gts?ara={urllib.parse.quote(w)}", rel, refresh=refresh)
        try:
            d = json.loads(body)
        except ValueError:
            tried.append(f"{w}: non-JSON response (HTTP {st})")
            continue
        if isinstance(d, dict):
            tried.append(f"{w}: {d.get('error')}")
            continue
        segs = []
        for i, m in enumerate(d, 1):
            lines = [m.get("madde", w) + (f" ({m.get('lisan')})" if m.get("lisan") else "")]
            for an in m.get("anlamlarListe") or []:
                ozel = ", ".join(o.get("tam_adi", "") for o in (an.get("ozelliklerListe") or []))
                ex = "; ".join(f"“{o.get('ornek')}”" + (f" — {o['yazar'][0]['tam_adi']}" if o.get("yazar") else "")
                               for o in (an.get("orneklerListe") or []))
                lines.append(f"{an.get('anlam_sira')}. {('[' + ozel + '] ') if ozel else ''}{an.get('anlam')}"
                             + (f"  Örnek: {ex}" if ex else ""))
            if m.get("birlesikler"):
                lines.append("Birleşik sözler: " + m["birlesikler"])
            segs.append({"seg": f"TDK:{m.get('madde', w)}" + (f"#{i}" if len(d) > 1 else ""), "s": None, "a": None,
                         "a_end": None, "page": None, "head": m.get("madde"), "text": "\n".join(lines),
                         "lisan": m.get("lisan"), "query": word, "madde_id": m.get("madde_id"),
                         "url": f"https://sozluk.gov.tr/gts?ara={urllib.parse.quote(m.get('madde', w))}"})
        return src, segs, None
    return src, [], "; ".join(tried) or "not fetched"


# ---------------------------------------------------------------- TARAMA (blocked)
def tarama(word: str, refresh=False, offline=False):
    src = Source("TARAMA")
    rel = "blocked_probe_ts_kalp.json"
    if not offline or src.cached(rel):
        st, body = src.fetch("https://api.sozluk.gov.tr/ts?ara=kalp", rel)   # single cached evidence probe
        msg = body.decode("utf-8", "replace")[:200]
    else:
        st, msg = None, ""
    return src, [], f"blocked (HTTP {st}: {msg}); not bypassed"


FETCHERS = {"nisanyan": nisanyan, "kubbealti": kubbealti, "tdk": tdk, "tarama": tarama}
SIDS = {"nisanyan": "NISANYAN", "kubbealti": "KUBBEALTI", "tdk": "TDK", "tarama": "TARAMA"}


def queried_words(src: Source, kind: str) -> list[str]:
    out = []
    for r in src._log.values():
        p = r["path"]
        if "__" in p:
            q = urllib.parse.unquote(p.split("__", 1)[1].rsplit(".", 1)[0])
            if kind == "kubbealti":
                q = urllib.parse.unquote(r["url"].split("/rest/s/")[1].split("/")[0])
            out.append(q)
    return list(dict.fromkeys(out))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("words", nargs="*")
    ap.add_argument("--sources", default="nisanyan,kubbealti,tdk,tarama")
    ap.add_argument("--seed", action="store_true", help="fetch the seed word list")
    ap.add_argument("--reparse", action="store_true", help="rebuild from raw/ only (no network)")
    ap.add_argument("--refresh", action="store_true")
    a = ap.parse_args()
    words = list(a.words) + (SEED if a.seed else [])
    report = {}
    for name in [x.strip() for x in a.sources.split(",") if x.strip()]:
        fn = FETCHERS[name]
        sid = SIDS[name]
        if a.reparse:
            s0 = Source(sid)
            s0.segments_path().unlink(missing_ok=True)
            ws = queried_words(s0, name)
        else:
            ws = words
        src = Source(sid)
        status = {}
        for w in ws:
            try:
                src_, segs, err = fn(w, a.refresh, offline=a.reparse)
            except Exception as e:          # keep going; the raw response stays cached for a later reparse
                src_, segs, err = src, [], f"ERROR {type(e).__name__}: {e}"
            if segs:
                src_.upsert_segments(segs)
                status[w] = [s["seg"] for s in segs]
            else:
                status[w] = f"MISSING: {err}"
            print(f"{sid:10s} {w:10s} -> {status[w]}")
            if name == "tarama":
                break      # one evidence probe is enough; the whole source is blocked
        src = Source(sid)
        segs = src.load_segments()
        prev = {}
        p = src.dir / "source.json"
        if p.exists():
            prev = json.loads(p.read_text(encoding="utf-8")).get("queries", {})
        prev.update(status)
        meta = dict(META[sid])
        meta["coverage"] = f"{len(segs)} entries" if name != "tarama" else "none (blocked)"
        src.update_source(meta, extra={"queries": prev})
        report[sid] = status
    return report


if __name__ == "__main__":
    main()
