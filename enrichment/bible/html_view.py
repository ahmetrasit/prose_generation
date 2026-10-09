#!/usr/bin/env python3
"""Reading view of accepted Bible (ehlikitap) pages as one self-contained HTML file. Launches no model.

The frozen page as written, with every accepted Tevrat/İncil record as a collapsed <details> under the paragraph it
annotates (same layout and colour tokens as the v9 Islamic reading view, enrichment/v9/page_html.py), then the
page's Arabic-root decisions and its gap summary. Several pages of one surah go into one file, with a page menu.

  html_view.py --surah 103 --pages surah 103:1 103:2 103:3 --out FILE.html
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'v9'))
from page_html import CSS  # noqa: E402  (the v9 reading-view style, shared on purpose)

TAG = re.compile(r'\{(ar|he|el):(.*?), tr:(.*?), gloss:(.*?), source:(.*?)\}|\{source:(.*?)\}')
LANG = {'ar': ('ar', 'ar', 'rtl'), 'he': ('he', 'he', 'rtl'), 'el': ('grc', 'el', 'ltr')}
GELENEK = {'tevrat': ('Tevrat', 'tev'), 'incil': ('İncil', 'inc')}
TUR = {'paralel': 'Paralel', 'motif': 'Motif', 'karsi_anlati': 'Karşı anlatı', 'soydas': 'Soydaş kök',
       'yorum_gelenegi': 'Yorum geleneği', 'kaynak_notu': 'Kaynak notu', 'elenen': 'Elenen'}
DURUM = {'yorum': 'yorum', 'cikarim': 'çıkarım', 'degerlendirilmedi': 'değerlendirilmedi (yalnız hafızadan)'}
DECISION = {'used': 'kullanıldı', 'no_qualifying_parallel': 'uygun paralel yok', 'false_friend': 'yalancı akraba',
            'no_hebrew_cognate': 'İbranice akrabası yok'}
EXTRA = """
.he{font-family:"SBL Hebrew","Ezra SIL","Noto Serif Hebrew",var(--arabic);font-size:1.12em;direction:rtl;unicode-bidi:isolate}
.el{font-family:"Gentium Plus","Noto Serif",var(--serif)}
.tev{--k:var(--ink-blue)} .inc{--k:var(--teal)} .kar{--k:var(--ochre)} .eln{--k:var(--slate)}
nav.pages{display:flex;gap:.4rem;flex-wrap:wrap;margin:.8rem 0 0}
nav.pages a{font:500 .8rem var(--sans);color:var(--ink);text-decoration:none;border:1px solid var(--rule);border-radius:4px;padding:.3rem .6rem;background:var(--card)}
section.page{border-top:2px solid var(--rule);margin-top:2.5rem;padding-top:.5rem}
section.page>h1{font:600 1.6rem/1.25 var(--serif);margin:.6rem 0 .2rem}
.roots{font:.86rem/1.5 var(--sans)} .roots li{margin:.4rem 0} .roots .dec{font-weight:600}
.gaps{font:.8rem/1.5 var(--sans);color:var(--muted)}
"""


def tagged(s):
    out, last = [], 0
    for m in TAG.finditer(s):
        out.append(html.escape(s[last:m.start()]))
        if m.group(1):
            lang, cls, d = LANG[m.group(1)]
            out.append(f'<span class="{cls}" lang="{lang}" dir="{d}">{html.escape(m.group(2))}</span> '
                       f'(<span class="tr">{html.escape(m.group(3))}</span>, “{html.escape(m.group(4))}”)'
                       f'<span class="src">{html.escape(m.group(5).strip(chr(34)))}</span>')
        else:
            out.append(f'<span class="src">{html.escape(m.group(6).strip(chr(34)))}</span>')
        last = m.end()
    out.append(html.escape(s[last:]))
    return ''.join(out)


def plain(s, n=150):
    t = TAG.sub(lambda m: m.group(2) or '', s)
    first = re.split(r'(?<=[.!?])\s', t, maxsplit=1)[0]
    return first if len(first) <= n else first[:n].rsplit(' ', 1)[0] + '…'


def record(r):
    label, cls = GELENEK.get(r['gelenek'], (r['gelenek'], 'tev'))
    if r['tur'] == 'karsi_anlati':
        cls += ' kar'
    if r['tur'] == 'elenen':
        cls = 'eln'
    meta = [r['id'], f"ayet {r['ayet']}", f"kaynak {r['kaynak'].replace('|', ', ')}" if r.get('kaynak') else '',
            DURUM.get(r.get('durum'), r.get('durum') or ''), f"katman {r.get('kat')}" if r.get('kat') else '']
    return (f'<details class="b {cls}"><summary><span class="kind">{label} · {TUR.get(r["tur"], r["tur"])}</span>'
            f'<span class="topic">{html.escape(plain(r["metin"]))}</span></summary>'
            f'<div class="body">{tagged(r["metin"])}<div class="meta">{html.escape(" · ".join(x for x in meta if x))}</div></div></details>')


def page(out_dir, stem, title):
    recs = {}
    for line in (out_dir / f'{stem}.ehlikitap.annotations.jsonl').read_text().splitlines():
        if line.strip():
            r = json.loads(line)
            recs[r['id']] = r
    body, pending, n = [], [], 0
    for line in (out_dir / f'{stem}.ehlikitap.md').read_text().splitlines():
        s = line.strip()
        if not s or s.startswith('<!--'):
            continue
        m = re.match(r'^\{id:"([^"]+)"', s)
        if m:
            r = recs.get(m.group(1))
            if r is None:
                print(f'WARNING {stem}: {m.group(1)} is on the page but not in the annotations; shown as written')
                pending.append(f'<p class="para">{tagged(s)}</p>')
            else:
                pending.append(record(r))
                n += 1
            continue
        if pending:
            body.append(f'<div class="blocks">{"".join(pending)}</div>')
            pending = []
        if s.startswith('#'):
            body.append(f'<h2>{tagged(s.lstrip("#").strip())}</h2>')
        else:
            body.append(f'<p class="para">{tagged(s)}</p>')
    if pending:
        body.append(f'<div class="blocks">{"".join(pending)}</div>')
    if n != len(recs):
        print(f'WARNING {stem}: {len(recs)} accepted records, {n} placed on the page')
    roots = []
    rv = out_dir / f'{stem}.ehlikitap.root_verdicts.jsonl'
    for line in (rv.read_text().splitlines() if rv.exists() else []):
        if line.strip():
            x = json.loads(line)
            roots.append(f'<li><span class="ar" lang="ar">{html.escape(x["root"])}</span> → '
                         f'<span class="he" lang="he" dir="rtl">{html.escape(", ".join(x.get("hebrew") or []))}</span> · '
                         f'<span class="dec">{DECISION.get(x["decision"], x["decision"])}</span><br>{html.escape(x.get("reason") or "")}</li>')
    gaps = json.loads((out_dir / f'{stem}.ehlikitap.gaps.json').read_text())
    gap = ' · '.join(f'{k}: {len(v) if isinstance(v, (list, dict)) else v}' for k, v in gaps.items())
    return n, (f'<section class="page" id="p-{stem.replace("_", "-")}"><h1>{html.escape(title)}</h1>'
               f'<p class="gaps">{n} Tevrat/İncil kaydı. Eksik kaynaklar ({html.escape(gap)}) sayfanın gap kaydında.</p>'
               + ''.join(body)
               + (f'<h2>Arapça kök kararları</h2><ol class="roots">{"".join(roots)}</ol>' if roots else '')
               + '</section>')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--surah', type=int, required=True)
    ap.add_argument('--pages', nargs='+', required=True, help='surah and/or S:A')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    out_dir = HERE / 'out' / f's{a.surah:03d}'
    sections, nav, total = [], [], 0
    for p in a.pages:
        stem = 'surah' if p == 'surah' else p.replace(':', '_')
        title = f'Sure {a.surah} şerhi' if p == 'surah' else f'{p} okuması'
        n, s = page(out_dir, stem, title)
        total += n
        sections.append(s)
        nav.append(f'<a href="#p-{stem.replace("_", "-")}">{html.escape(title)}</a>')
    doc = f"""<title>Sure {a.surah} Ehl-i Kitap</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Amiri&family=IBM+Plex+Sans:wght@400;500;600&family=Literata:opsz,wght@7..72,400;7..72,600&family=Noto+Serif+Hebrew&family=Gentium+Plus&display=swap">
<style>{CSS}{EXTRA}</style>
<main>
<header class="top">
  <div class="eyebrow">Ehl-i Kitap katmanı · önizleme (editoryal okuma yapılmadı)</div>
  <h1>Sure {a.surah}: Tevrat ve İncil ile karşılaştırma</h1>
  <p>Dondurulmuş şerh olduğu gibi; altındaki {total} kutu İbranice (WLC), Yunanca (SBLGNT) ve Yahudi/Hristiyan yorum metinlerinden paralelleri, karşı anlatıları ve ortak kökleri gösterir. Kutular kapalı gelir.</p>
  <div class="controls"><button type="button" id="open-all">Hepsini aç</button><button type="button" id="close-all">Hepsini kapat</button></div>
  <nav class="pages">{''.join(nav)}</nav>
</header>
{''.join(sections)}
</main>
<script>
document.getElementById('open-all').addEventListener('click',()=>document.querySelectorAll('details.b').forEach(d=>d.open=true));
document.getElementById('close-all').addEventListener('click',()=>document.querySelectorAll('details.b').forEach(d=>d.open=false));
</script>
"""
    Path(a.out).write_text(doc)
    print(f'{a.out}: {len(a.pages)} pages, {total} records, {len(doc):,} characters')


if __name__ == '__main__':
    main()
