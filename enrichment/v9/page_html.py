#!/usr/bin/env python3
"""Enrichment v9: one ayah page as a self-contained HTML reading view (preview of the reader UI). Launches no model.

The frozen page with each block as a collapsed <details> under its paragraph (tradition blocks, then meal blocks),
the closing group after the last paragraph, and an appendix with every map question the blocks cite in full
(positions, reasons, holders), linked from the blocks.

  page_html.py WRITE_RUN [--meal MEAL_RUN] --out FILE.html
"""
import argparse
import html
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

V9 = Path(__file__).resolve().parent
sys.path.insert(0, str(V9))
import writer  # noqa: E402
import q as Q  # noqa: E402

KIND = {'focus': ('Gelenek', 'focus'), 'cited': ('Atıf yapılan ayet', 'cited'), 'agreement': ('Mutabakat', 'agree'),
        'closing': ('Kapanış', 'closing'), 'meal': ('Mealler', 'meal')}
TAG = re.compile(r'\{ar:(.*?), tr:(.*?), gloss:(.*?), source:(.*?)\}|\{source:(.*?)\}')
ARABIC = re.compile(r'([؀-ۿ][؀-ۿً-ْٰ\s،]*[؀-ۿ])')
CSS = """
/* Layout: one reading column; blocks hang under their paragraph as collapsible notes; appendix of map questions. */
:root{
  --paper:#f7f8fa; --ink:#1d2430; --muted:#5b6575; --rule:#d9dee6; --card:#ffffff;
  --ink-blue:#2f4f86; --teal:#2f6f73; --green:#4d6b3c; --ochre:#8a6a1f; --slate:#5a6070;
  --serif:"Literata", Georgia, "Times New Roman", serif; --sans:"IBM Plex Sans", system-ui, sans-serif;
  --arabic:"Amiri", "Scheherazade New", "Noto Naskh Arabic", serif;
}
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){
  --paper:#14181f; --ink:#e3e7ee; --muted:#9aa4b4; --rule:#2c3440; --card:#1b212a;
  --ink-blue:#8fb0e8; --teal:#7cc3c5; --green:#a3c48e; --ochre:#d9b866; --slate:#aab1c0; color-scheme:dark }}
:root[data-theme="dark"]{
  --paper:#14181f; --ink:#e3e7ee; --muted:#9aa4b4; --rule:#2c3440; --card:#1b212a;
  --ink-blue:#8fb0e8; --teal:#7cc3c5; --green:#a3c48e; --ochre:#d9b866; --slate:#aab1c0; color-scheme:dark }
body{background:var(--paper);color:var(--ink);font:17px/1.65 var(--serif);margin:0}
main{max-width:44rem;margin:0 auto;padding-inline:16px;padding-block:2rem 4rem}
header.top{border-bottom:1px solid var(--rule);padding-bottom:1rem;margin-bottom:1.5rem}
header.top .eyebrow{font:600 .75rem/1 var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
header.top h1{font:600 1.9rem/1.2 var(--serif);margin:.4rem 0 .3rem;text-wrap:balance}
header.top .verse{font:2.2rem/1.4 var(--arabic);direction:rtl;margin:.2rem 0}
header.top p{font:.9rem/1.5 var(--sans);color:var(--muted);margin:.3rem 0 0}
.controls{display:flex;gap:.5rem;flex-wrap:wrap;margin-top:.8rem}
.controls button{font:500 .8rem var(--sans);background:var(--card);color:var(--ink);border:1px solid var(--rule);border-radius:4px;padding:.35rem .7rem;cursor:pointer}
.controls button:focus-visible,summary:focus-visible,a:focus-visible{outline:2px solid var(--ink-blue);outline-offset:2px}
h2{font:600 1.25rem/1.3 var(--serif);margin:2.2rem 0 .6rem;text-wrap:balance}
p.para{margin:.9rem 0;position:relative}
.pn{font:500 .7rem var(--sans);color:var(--muted);margin-right:.35rem;font-variant-numeric:tabular-nums}
.ar{font-family:var(--arabic);font-size:1.15em;direction:rtl;unicode-bidi:isolate}
.tr{font-style:italic;color:var(--muted)}
.src{font:.7rem var(--sans);color:var(--muted);vertical-align:super}
.blocks{display:flex;flex-direction:column;gap:.35rem;margin:.2rem 0 1.2rem}
details.b{background:var(--card);border:1px solid var(--rule);border-left:3px solid var(--k);border-radius:3px}
details.b>summary{list-style:none;cursor:pointer;padding:.45rem .7rem;font:.88rem/1.35 var(--sans);display:flex;gap:.6rem;align-items:baseline}
details.b>summary::-webkit-details-marker{display:none}
details.b>summary .kind{font-weight:600;font-size:.68rem;letter-spacing:.06em;text-transform:uppercase;color:var(--k);white-space:nowrap}
details.b>summary .topic{min-width:0}
details.b>summary::after{content:"+";margin-left:auto;color:var(--muted)}
details.b[open]>summary::after{content:"–"}
details.b .body{padding:.1rem .9rem .7rem;font:.95rem/1.6 var(--serif)}
details.b .meta{font:.75rem/1.4 var(--sans);color:var(--muted);margin-top:.5rem}
details.b .meta a{color:var(--k)}
.focus{--k:var(--ink-blue)} .cited{--k:var(--teal)} .agree{--k:var(--green)} .closing{--k:var(--slate)} .meal{--k:var(--ochre)}
section.appendix{margin-top:3rem;border-top:1px solid var(--rule);padding-top:1rem}
section.appendix h2{margin-top:.5rem}
.qa{margin:1rem 0;padding:.6rem .8rem;background:var(--card);border:1px solid var(--rule);border-radius:3px}
.qa h3{font:600 .95rem/1.4 var(--sans);margin:0 0 .3rem}
.qa .qid{font:.72rem var(--sans);color:var(--muted);font-variant-numeric:tabular-nums}
.qa .turn{font:.85rem/1.5 var(--sans);color:var(--muted);margin:.2rem 0 .4rem}
.qa ol{margin:.2rem 0 0;padding-left:1.3rem;font:.86rem/1.5 var(--sans)}
.qa li{margin:.35rem 0}
.qa .why{color:var(--muted)}
.qa details.orig{margin-top:.4rem;font:.8rem/1.45 var(--sans);color:var(--muted)}
.qa details.orig summary{cursor:pointer}
.qa .who{font-size:.78rem;color:var(--muted);overflow-wrap:anywhere}
@media (prefers-reduced-motion: no-preference){ details.b[open] .body{animation:fade .18s ease-out} @keyframes fade{from{opacity:.4}to{opacity:1}} }
"""


def esc_ar(s):
    return ARABIC.sub(lambda m: f'<span class="ar" lang="ar">{m.group(1)}</span>', html.escape(s))


def page_text(s):
    out, last = [], 0
    for m in TAG.finditer(s):
        out.append(html.escape(s[last:m.start()]))
        if m.group(1) is not None:
            out.append(f'<span class="ar" lang="ar">{html.escape(m.group(1))}</span> (<span class="tr">{html.escape(m.group(2))}</span>, '
                       f'“{html.escape(m.group(3))}”)<span class="src">{html.escape(m.group(4).strip(chr(34)))}</span>')
        else:
            out.append(f'<span class="src">{html.escape(m.group(5).strip(chr(34)))}</span>')
        last = m.end()
    out.append(html.escape(s[last:]))
    return ''.join(out)


def anchor(qid):
    return 'q-' + re.sub(r'[^0-9a-z]', '-', qid.lower())


def block_html(b, kind):
    label, cls = KIND[kind]
    meta = []
    qs = b.get('questions') or []
    if qs:
        meta.append('Haritada: ' + ', '.join(f'<a href="#{anchor(x)}">{html.escape(x)}</a>' for x in qs))
    if b.get('notes'):
        meta.append(f"{len(b['notes'])} not")
    if b.get('meals'):
        meta.append(f"{len(b['meals'])} meal")
    return (f'<details class="b {cls}"><summary><span class="kind">{label}</span><span class="topic">{esc_ar(b["topic"])}</span></summary>'
            f'<div class="body">{esc_ar(b["text"])}<div class="meta">{" · ".join(meta)}</div></div></details>')


_TR = {}


def question_html(qid):
    """The question in Turkish when its rendering is current (made from this English), with the English original
    one click away; otherwise in English."""
    v = qid.split('/')[0]
    qs, rows = Q.load(v)
    q = next((x for x in qs or [] if x['id'] == qid), None)
    if q is None:
        print(f'WARNING {qid}: cited by a block but not in any verse map; shown as missing')
        return (f'<div class="qa" id="{anchor(qid)}"><div class="qid">{html.escape(qid)}</div>'
                '<h3>Bu soru ayet haritasında bulunamadı.</h3></div>')
    if v not in _TR:
        import maptr
        _TR[v] = {k: t for k, t in Q.translation(v).items()}
        _TR[v]['__hash'] = maptr.qhash
    t = _TR[v].get(qid)
    status = '' if t else ' · İngilizce (çevirisi yok)'
    if t and t['src'] != _TR[v]['__hash'](q):
        t, status = None, ' · İngilizce (çeviri eski: harita sonradan değişti)'  # stale: the map changed after translation
    eng = q
    legend = {r['src']: r['author'] for r in rows.values()}
    items = []
    for p in q['positions']:
        pro, con = set(p.get('prefer') or []), p.get('against') or []
        by = defaultdict(set)
        for r in p['rows']:
            if r in rows:
                by[rows[r]['src']].add('+' if r in pro else '')
        who = '; '.join(legend.get(s, s) + ('+' if '+' in m else '') for s, m in by.items())
        against = '; '.join(sorted({legend.get(rows[r]['src'], rows[r]['src']) for r in con if r in rows}))
        tp = (t or {}).get('positions', {}).get(p['id'], {})
        pos_txt, why_txt = (tp.get('position') or p['position']), ((tp.get('reasons') or p.get('reasons')) if t else p.get('reasons'))
        # a note withdrawn from Tier 1 after mapping stays in the map (q.assembled marks it); the reader is told
        pulled = len({r for r in p['rows'] + con if r in rows and rows[r].get('tier1')})
        items.append(f'<li>{esc_ar(pos_txt)}'
                     + (f' <span class="why">— {esc_ar(why_txt)}</span>' if why_txt else '')
                     + f'<div class="who">{len(p["rows"])} not: {html.escape(who)}'
                     + (f' · karşı: {html.escape(against)}' if against else '')
                     + (f' · {pulled} notun kaydı harita hazırlandıktan sonra değişti veya kaldırıldı' if pulled else '')
                     + '</div></li>')
    qtext = (t['question'] if t else '') or q['question']
    turn = ((t or {}).get('turns_on') if t else '') or q.get('turns_on')
    orig = ''
    if t:
        lines = ''.join(f'<li>{esc_ar(p["position"])}' + (f' — {esc_ar(p["reasons"])}' if p.get('reasons') else '') + '</li>' for p in eng['positions'])
        orig = (f'<details class="orig"><summary>İngilizce aslı</summary><p>{esc_ar(eng["question"])}</p>'
                + (f'<p>Turns on: {esc_ar(eng["turns_on"])}</p>' if eng.get('turns_on') else '') + f'<ol>{lines}</ol></details>')
    return (f'<div class="qa" id="{anchor(qid)}"><div class="qid">{html.escape(qid)} · {html.escape(q["type"])}'
            + status + '</div>'
            f'<h3>{esc_ar(qtext)}</h3>'
            + (f'<div class="turn">Ayrılık noktası: {esc_ar(turn)}</div>' if turn else '')
            + f'<ol>{"".join(items)}</ol>{orig}</div>')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('run'); ap.add_argument('--meal'); ap.add_argument('--out', required=True)
    a = ap.parse_args()
    d = writer.wdir(a.run)
    man = json.loads((d / 'manifest.json').read_text())
    blocks = [json.loads(l) for l in (d / 'out' / man['tag'] / 'blocks.jsonl').read_text().splitlines() if l.strip()]
    meals = []
    if a.meal:
        md = V9 / 'work' / a.meal / 'meal'
        mm = json.loads((md / 'manifest.json').read_text())
        if (mm.get('ayah'), mm.get('page')) != (man['ayah'], man['page']):
            raise SystemExit(f"--meal {a.meal} is for {mm.get('ayah')}, not {man['ayah']}")
        meals = [json.loads(l) for l in (md / 'out' / mm['tag'] / 'blocks.jsonl').read_text().splitlines() if l.strip()]
    text, paras, _, _ = writer.write7.page(man['page'], man['ayah'])
    last = max(paras)
    after, close = defaultdict(list), []
    for b in blocks:
        if b['kind'] == 'closing':
            close.append(block_html(b, b['kind']))
        else:
            after[min(b['p'])].append(block_html(b, b['kind']))
    for b in meals:
        after[b['p']].append(block_html(b, 'meal'))
    after[last] += close                           # as render.py: closing after the last paragraph's meal blocks
    stray = sorted(set(k for k, v in after.items() if v) - set(paras))
    if stray:
        raise SystemExit(f'blocks attached to paragraphs not on the page: {stray}')
    body, pos = [], 0
    for p in sorted(paras, key=lambda x: paras[x][0]):
        lo, hi = paras[p]
        for line in text[pos:lo].splitlines():
            if line.startswith('#'):
                body.append(f'<h2>{page_text(line.lstrip("#").strip())}</h2>')
            elif line.strip():
                body.append(f'<p class="para">{page_text(line.strip())}</p>')
        body.append(f'<p class="para"><span class="pn">¶{p}</span>{page_text(text[lo:hi].strip())}</p>')
        if after[p]:
            body.append(f'<div class="blocks">{"".join(after[p])}</div>')
        pos = hi
    for line in text[pos:].splitlines():           # text after the last paragraph, rendered like the text before
        if line.startswith('#'):
            body.append(f'<h2>{page_text(line.lstrip("#").strip())}</h2>')
        elif line.strip():
            body.append(f'<p class="para">{page_text(line.strip())}</p>')
    cited = list(dict.fromkeys(x for b in blocks + meals for x in b.get('questions') or []))
    cited.sort(key=lambda x: (x.split('/')[0] != man['ayah'], tuple(map(int, x.split('/')[0].split(':'))), x))
    with Q.digest.connect() as con:
        s, n = map(int, man['ayah'].split(':'))
        verse = con.execute("SELECT text FROM seg JOIN src ON src.id=seg.src WHERE src.kind='quran' AND s=? AND a=?", (s, n)).fetchone()[0]
    nb = len(blocks) + len(meals)
    page = f"""<!doctype html>
<html lang="tr">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{man['ayah']} Enriched Reading</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Amiri&family=IBM+Plex+Sans:wght@400;500;600&family=Literata:opsz,wght@7..72,400;7..72,600&display=swap">
<style>{CSS}</style>
<main>
<header class="top">
  <div class="eyebrow">Ayet şerhi · zenginleştirme önizlemesi</div>
  <h1>{man['ayah']} okuması</h1>
  <div class="verse" lang="ar">{html.escape(verse)}</div>
  <p>Dondurulmuş metin olduğu gibi; altındaki {nb} kutu kaynakların söylediğini haritalar. Kutular kapalı gelir; açıp kapatarak istediğiniz ayrıntıyı görün. Kutulardaki soru bağlantıları sayfanın sonundaki ayet haritalarına gider.</p>
  <div class="controls"><button type="button" id="open-all">Hepsini aç</button><button type="button" id="close-all">Hepsini kapat</button></div>
</header>
{''.join(body)}
<section class="appendix"><h2>Ayet haritaları: kutuların dayandığı sorular</h2>
<p class="para">Her soru, kaynakların verdiği her cevabı (pozisyonu), gerekçesini ve sahiplerini gösterir. + tercih eden, “karşı” itiraz eden kaynaklardır.</p>
{''.join(question_html(x) for x in cited)}
</section>
</main>
<script>
document.getElementById('open-all').addEventListener('click',()=>document.querySelectorAll('details.b').forEach(d=>d.open=true));
document.getElementById('close-all').addEventListener('click',()=>document.querySelectorAll('details.b').forEach(d=>d.open=false));
</script>
</html>
"""
    Path(a.out).write_text(page, encoding='utf-8')
    print(f'{a.out}: {nb} blocks, {len(cited)} map questions, {len(page):,} characters')


if __name__ == '__main__':
    main()
