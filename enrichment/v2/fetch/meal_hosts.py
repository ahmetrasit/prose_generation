"""Host adapters for fetch_meal.py. Each host has fetch_*() (download into a raw/ cache, resumable:
files already present are skipped) and parse_*() (raw -> {(s,a): row}).

Witness keys: 'tanzil:<transID>', 'fawaz:<edition>', 'quranenc:<key>', 'kd:<ML>', 'km:<div key>',
'ak:<heading name>', 'mo:<author label>', 'svm:site'."""
import concurrent.futures as cf
import gzip
import json
import os
import re
import sqlite3
import threading

from meal_common import (AYAH_COUNTS, Blocked, FETCH_DIR, Host, all_ayat, clean, html_to_paras, log,
                         order_surahs, read_gz, src_dir, write_bytes, write_gz, write_text)

HOSTS = {}


def host(name, **kw):
    if name not in HOSTS:
        HOSTS[name] = Host(name, **kw)
    return HOSTS[name]


# ------------------------------------------------------------------ whole-file hosts

def tanzil_path(home, tid):
    return os.path.join(src_dir(home), 'raw', f'tanzil_{tid}.txt')


def tanzil_url(tid):
    return f'https://tanzil.net/trans/?transID={tid}&type=txt-2'


def fetch_tanzil(home, tid):
    p = tanzil_path(home, tid)
    if os.path.exists(p):
        return p
    t = host('tanzil.net').get(tanzil_url(tid), validate=lambda x: '1|1|' in x)
    if t is None:
        raise RuntimeError(f'tanzil {tid}: 404')
    write_text(p, t)
    return p


def parse_tanzil(home, tid):
    rows = {}
    for line in open(tanzil_path(home, tid), encoding='utf-8'):
        p = line.rstrip('\n').split('|', 2)
        if len(p) == 3 and p[0].isdigit():
            rows[(int(p[0]), int(p[1]))] = {'text': clean(p[2])}
    return rows


def fetch_arabic():
    p = os.path.join(FETCH_DIR, 'meal_quran_simple_clean.txt')
    if os.path.exists(p):
        return p
    url = 'https://tanzil.net/pub/download/index.php?quranType=simple-clean&outType=txt-2&agree=true'
    t = host('tanzil.net').get(url, validate=lambda x: '1|1|' in x)
    write_text(p, t)
    return p


def fawaz_path(home, ed):
    return os.path.join(src_dir(home), 'raw', f'fawaz_{ed}.json')


def fawaz_url(ed):
    return f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{ed}.json'


def fetch_fawaz(home, ed):
    p = fawaz_path(home, ed)
    if os.path.exists(p):
        return p
    t = host('cdn.jsdelivr.net').get(fawaz_url(ed), validate=lambda x: '"quran"' in x[:50])
    if t is None:
        raise RuntimeError(f'fawaz {ed}: 404')
    write_text(p, t)
    return p


def parse_fawaz(home, ed):
    d = json.load(open(fawaz_path(home, ed), encoding='utf-8'))
    return {(v['chapter'], v['verse']): {'text': clean(v['text'])} for v in d['quran']}


def alqc_path(home, ed):
    return os.path.join(src_dir(home), 'raw', f'alquran-cloud_{ed}.json')


def alqc_url(ed):
    return f'https://api.alquran.cloud/v1/quran/{ed}'


def fetch_alqc(home, ed):
    p = alqc_path(home, ed)
    if os.path.exists(p):
        return p
    t = host('api.alquran.cloud').get(alqc_url(ed), validate=lambda x: '"surahs"' in x)
    if t is None:
        raise RuntimeError(f'alquran.cloud {ed}: 404')
    write_text(p, t)
    return p


def parse_alqc(home, ed):
    d = json.load(open(alqc_path(home, ed), encoding='utf-8'))['data']
    return {(s['number'], a['numberInSurah']): {'text': clean(a['text'])} for s in d['surahs'] for a in s['ayahs']}


def quranenc_path(home, key):
    return os.path.join(src_dir(home), 'raw', f'quranenc_{key}.sqlite')


def quranenc_url(key):
    return f'https://quranenc.com/downloads/sqlite/{key}.sqlite'


def fetch_quranenc(home, key):
    p = quranenc_path(home, key)
    if os.path.exists(p):
        return p
    b = host('quranenc.com').get(quranenc_url(key), binary=True)
    if not b or not b.startswith(b'SQLite format 3'):
        raise RuntimeError(f'quranenc {key}: not a sqlite file')
    write_bytes(p, b)
    return p


def parse_quranenc(home, key):
    c = sqlite3.connect(quranenc_path(home, key))
    rows = {}
    for s, a, t, fn in c.execute('select sura, aya, translation, footnotes from translations'):
        r = {'text': clean(t)}
        if fn and fn.strip():
            r['notes'] = clean(fn)
        rows[(int(s), int(a))] = r
    return rows


# ------------------------------------------------------------------ kuran.diyanet.gov.tr (per mushaf page)

KD_HOME = {1: 'MEAL-DIB', 4: 'MEAL-TDV', 5: 'MEAL-KURANYOLU', 6: 'MEAL-ELMALILI'}
_KD_RE = re.compile(r'var MPageDmList = (\[.*?\]);\s*\n', re.S)


def kd_url(ml, s, a):
    route = 'kuran-tefsir-1' if ml == 1 else 'kuran-meal-1'   # ML=1 page also carries the Kur'an Yolu tefsir
    return f'https://kuran.diyanet.gov.tr/mushaf/{route}/sure-suresi-{s}/ayet-{a}/diyanet-isleri-baskanligi-meali-{ml}'


def kd_dir(ml):
    return os.path.join(src_dir(KD_HOME[ml]), 'raw', 'kd')


def kd_page_json(text):
    m = _KD_RE.search(text)
    return json.loads(m.group(1))[0] if m else None


def kd_cached_pages(ml):
    d = kd_dir(ml)
    idx_path = os.path.join(d, 'index.json')
    idx = json.load(open(idx_path)) if os.path.exists(idx_path) else {}
    changed = False
    if os.path.isdir(d):
        for f in os.listdir(d):
            m = re.match(r'p(\d+)\.html\.gz$', f)
            if m and m.group(1) not in idx:
                pj = kd_page_json(read_gz(os.path.join(d, f)))
                idx[m.group(1)] = sorted({(x['SureId'], x['AyetId']) for x in pj['MealAyats']})
                changed = True
    if changed:
        write_text(idx_path, json.dumps(idx))
    return idx


def fetch_kd(ml, surahs):
    h = host('kuran.diyanet.gov.tr', min_gap=0.5)
    idx = kd_cached_pages(ml)
    covered = {tuple(x) for v in idx.values() for x in v}
    targets = [x for x in all_ayat(order_surahs(surahs)) if x not in covered]
    tried = set()
    for (s, a) in targets:
        if (s, a) in covered or (s, a) in tried:
            continue
        tried.add((s, a))
        url = kd_url(ml, s, a)
        t = h.get(url, validate=lambda x: 'MPageDmList' in x)
        pj = kd_page_json(t or '')
        if not pj or not pj.get('MealAyats'):
            log(f'[kd ML{ml}] no page data for {s}:{a}')
            continue
        page = int(pj['PageNo'])
        write_gz(os.path.join(kd_dir(ml), f'p{page:03d}.html.gz'), t)
        ay = sorted({(x['SureId'], x['AyetId']) for x in pj['MealAyats']})
        idx[f'{page:03d}'] = ay
        covered.update(ay)
        if len(idx) % 25 == 0:
            write_text(os.path.join(kd_dir(ml), 'index.json'), json.dumps(idx))
            log(f'[kd ML{ml}] {len(idx)} pages cached, at {s}:{a}')
    write_text(os.path.join(kd_dir(ml), 'index.json'), json.dumps(idx))


def _kd_items(ml, field):
    d = kd_dir(ml)
    items = {}
    if not os.path.isdir(d):
        return items
    for f in sorted(os.listdir(d)):
        if f.endswith('.html.gz'):
            pj = kd_page_json(read_gz(os.path.join(d, f)))
            for x in pj.get(field) or []:
                items.setdefault((x['SureId'], x['AyetId']), x)
    return items


def _rng(num, a):
    m = re.match(r'^\s*(\d+)\s*-\s*(\d+)\s*$', str(num))
    return (int(m.group(1)), int(m.group(2))) if m else (a, a)


def parse_kd(ml):
    rows = {}
    items = _kd_items(ml, 'MealAyats')
    covered = set()
    for (s, a), x in sorted(items.items()):
        if not x.get('AyetVisible'):
            continue
        lo, hi = _rng(x['AyetNumber'], a)
        rows[(s, lo)] = {'text': clean(x['AyetText']), 'a_end': hi}
        covered.update((s, k) for k in range(lo, hi + 1))
    for (s, a), x in items.items():        # invisible item whose visible group head is on an uncached page
        if (s, a) not in covered and not x.get('AyetVisible'):
            rows[(s, a)] = {'text': clean(x['AyetText']), 'a_end': a, '_orphan': True}
    return rows


KD_TEFSIR_HEADS = [('Nuzul', 'Nüzûl'), ('AdiAyetSayisi', 'Adı ve âyet sayısı'), ('Konusu', 'Konusu'),
                   ('FaziletiOzelligi', 'Fazileti')]


def parse_kd_tefsir():
    rows = {}
    intros = {}
    for (s, a), x in sorted(_kd_items(1, 'TefsirList').items()):
        if not x.get('AyetVisible'):
            continue
        lo, hi = _rng(x['AyetNumber'], a)
        txt = html_to_paras(x.get('AyetText'))
        ek = html_to_paras(x.get('AyetEkText'))
        if ek:
            txt = (txt + '\n\n' + ek).strip()
        r = {'text': txt, 'a_end': hi}
        ref = html_to_paras(x.get('Dipnot'))
        if ref:
            r['ref'] = ref
        rows[(s, lo)] = r
        parts = []
        for k, label in KD_TEFSIR_HEADS:
            v = html_to_paras(x.get(k))
            if v:
                parts.append(f'{label}: {v}' if k != 'AdiAyetSayisi' else v)
        if parts and s not in intros:
            intros[s] = '\n\n'.join(parts)
    return rows, intros


# ------------------------------------------------------------------ kuranmeali.com (per ayah, ~55 meals per page)

KM_HOME = 'MEAL-BILMEN'


def km_url(s, a):
    return f'https://www.kuranmeali.com/AyetKarsilastirma.php?sure={s}&ayet={a}'


def km_path(s, a):
    return os.path.join(src_dir(KM_HOME), 'raw', 'kuranmeali', f'{s:03d}', f'{a:03d}.html.gz')


def _fetch_each(hostobj, items, url_fn, path_fn, validate, label, workers=2):
    todo = [x for x in items if not os.path.exists(path_fn(*x))]
    log(f'[{label}] {len(items) - len(todo)} cached, {len(todo)} to fetch')
    done = [0]
    lock = threading.Lock()
    stop = threading.Event()

    def one(x):
        if stop.is_set():
            return
        try:
            t = hostobj.get(url_fn(*x), validate=validate)
        except Blocked as e:
            stop.set()
            log(f'[{label}] BLOCKED: {e} - stopping this host (no bypass)')
            return
        except Exception as e:
            log(f'[{label}] failed {x}: {e}')
            return
        if t is None:
            log(f'[{label}] 404 {x}')
            return
        write_gz(path_fn(*x), t)
        with lock:
            done[0] += 1
            if done[0] % 100 == 0:
                log(f'[{label}] {done[0]}/{len(todo)} fetched (last {x})')

    with cf.ThreadPoolExecutor(workers) as ex:
        list(ex.map(one, todo))
    log(f'[{label}] finished: {done[0]} new pages')


def fetch_km(surahs):
    h = host('kuranmeali.com', min_gap=0.35)
    _fetch_each(h, all_ayat(order_surahs(surahs)), km_url, km_path,
                lambda x: "id='omernasuhi" in x or "id='hayrat" in x, 'kuranmeali')


def km_about_path(n):
    return os.path.join(src_dir(KM_HOME), 'raw', 'kuranmeali_about', f'{n}.html.gz')


def fetch_km_about(ids):
    h = host('kuranmeali.com', min_gap=0.35)
    for n in ids:
        p = km_about_path(n)
        if os.path.exists(p):
            continue
        t = h.get(f'https://www.kuranmeali.com/Aciklama.php?id={n}&islem=mealbilgi')
        if t:
            write_gz(p, t)


def km_about(n):
    p = km_about_path(n)
    if not os.path.exists(p):
        return None
    t = html_to_paras(re.sub(r'(?s)<script.*?</script>|<style.*?</style>', '', read_gz(p)))
    lines = [l for l in t.split('\n\n') if l.strip() and l.strip() not in ('Meal Açıklamaları', 'Kapat', 'Tıklayın')]
    return ' | '.join(lines)[:1200]


_KM_BLOCK = re.compile(r"<div id='([^'+]+)\+1'[^>]*>(.*?)(?=<div id='[^'+]+' style=|<div id='[^'+]+\+1'|$)", re.S)


def km_parse_page(h):
    out = {}
    for m in _KM_BLOCK.finditer(h):
        key, block = m.group(1), m.group(2)
        sp = re.search(r"<span style='font-size:16px;'>(.*?)</span>(?=\s*(?:<font|<div style='font-size:12px|</p>|<br))", block, re.S)
        if not sp:
            continue
        text = clean(re.sub(r'<[^>]+>', '', sp.group(1)))
        r = {'text': text}
        nd = re.search(r"<div style='font-size:12px[^']*'>(.*?)(?:<a href=|</div>)", block, re.S)
        if nd:
            notes = html_to_paras(nd.group(1)).replace('\n\n', '\n').strip()
            if notes:
                r['notes'] = notes
                if 'Devamı' in block[nd.start():]:
                    r['notes_truncated'] = True
        out[key] = r
    return out


_KM_CACHE = {}


def km_all(surahs):
    """{key: {(s,a): row}} for cached pages in the given surahs (parsed once)."""
    res = {}
    for s in surahs:
        for a in range(1, AYAH_COUNTS[s - 1] + 1):
            p = km_path(s, a)
            if (s, a) not in _KM_CACHE:
                if not os.path.exists(p):
                    continue
                _KM_CACHE[(s, a)] = km_parse_page(read_gz(p))
            for k, r in _KM_CACHE[(s, a)].items():
                res.setdefault(k, {})[(s, a)] = r
    return res


# ------------------------------------------------------------------ acikkuran.com (per-ayah markdown: all meals + footnotes)

AK_HOME = 'MEAL-ISLAMOGLU'


def ak_slugs():
    p = os.path.join(src_dir(AK_HOME), 'raw', 'acikkuran', 'surahs.md')
    if not os.path.exists(p):
        t = host('acikkuran.com').get('https://acikkuran.com/surahs.md', validate=lambda x: 'fatiha-suresi' in x)
        write_text(p, t)
    t = open(p, encoding='utf-8').read()
    slugs = {}
    for m in re.finditer(r'^\| (\d+) \| \[[^\]]*\]\(https://acikkuran\.com/([^)]+)\.md\)', t, re.M):
        slugs[int(m.group(1))] = m.group(2)
    return slugs


def ak_path(s, a):
    return os.path.join(src_dir(AK_HOME), 'raw', 'acikkuran', f'{s:03d}', f'{a:03d}.md.gz')


def fetch_ak(surahs):
    slugs = ak_slugs()
    h = host('acikkuran.com', min_gap=0.35)
    _fetch_each(h, all_ayat(order_surahs(surahs)),
                lambda s, a: f'https://acikkuran.com/{slugs[s]}/{a}-ayet-meali.md', ak_path,
                lambda x: x.startswith('# ') and '## Çeviriler' in x, 'acikkuran')


_MDLINK = re.compile(r'\[([^\]]*)\]\([^)]*\)')


def _md_inline(t):
    t = _MDLINK.sub(r'\1', t)
    t = re.sub(r'\\([\\`*_{}\[\]()#+\-.!>|])', r'\1', t)
    return t


def ak_parse_page(t):
    out = {}
    body = t.split('## Çeviriler', 1)[-1]
    for blk in re.split(r'\n### ', '\n' + body)[1:]:
        head, _, rest = blk.partition('\n')
        name = head.split(' — ')[0].strip()
        rest = rest.split('\n---\n')[0]
        text_part, _, notes_part = rest.partition('_Dipnotlar_')
        paras = [p.strip() for p in text_part.strip().split('\n\n') if p.strip()]
        text = clean(_md_inline(' '.join(paras)))
        r = {'text': text, 'title': head.strip()}
        notes = [_md_inline(l[2:].strip()) for l in notes_part.strip().split('\n') if l.startswith('- ')]
        if notes:
            r['notes'] = '\n'.join(clean(n) for n in notes)
        out[name] = r
    return out


_AK_CACHE = {}


def ak_all(surahs):
    res = {}
    for s in surahs:
        for a in range(1, AYAH_COUNTS[s - 1] + 1):
            p = ak_path(s, a)
            if (s, a) not in _AK_CACHE:
                if not os.path.exists(p):
                    continue
                _AK_CACHE[(s, a)] = ak_parse_page(read_gz(p))
            for k, r in _AK_CACHE[(s, a)].items():
                res.setdefault(k, {})[(s, a)] = r
    return res


# ------------------------------------------------------------------ mealler.org (per ayah, ~45 meals per page)

MO_HOME = 'MEAL-UNAL'


def mo_url(s, a):
    return f'https://mealler.org/SureveAyetler.aspx?sureid={s:03d}&ayet={a:03d}'


def mo_path(s, a):
    return os.path.join(src_dir(MO_HOME), 'raw', 'mealler', f'{s:03d}', f'{a:03d}.html.gz')


def fetch_mo(surahs):
    h = host('mealler.org', min_gap=0.4)
    _fetch_each(h, all_ayat(order_surahs(surahs)), mo_url, mo_path, lambda x: 'lblMeal' in x, 'mealler')


_MO_ROW = re.compile(r'<a title="([^"]+)" href="YazarinTumMealleri\.aspx\?id=(\d+)">[^<]*</a></td><td>\s*'
                     r'<span id="[^"]*_lblMeal">(.*?)</span>\s*</td>', re.S)


def mo_parse_page(h):
    out = {}
    for m in _MO_ROW.finditer(h):
        name = clean(m.group(1))
        out[name] = {'text': clean(re.sub(r'<[^>]+>', ' ', re.sub(r'(?i)<br\s*/?>', ' ', m.group(3)))),
                     'author_id': m.group(2)}
    return out


_MO_CACHE = {}


def mo_all(surahs):
    res = {}
    for s in surahs:
        for a in range(1, AYAH_COUNTS[s - 1] + 1):
            p = mo_path(s, a)
            if (s, a) not in _MO_CACHE:
                if not os.path.exists(p):
                    continue
                _MO_CACHE[(s, a)] = mo_parse_page(read_gz(p))
            for k, r in _MO_CACHE[(s, a)].items():
                res.setdefault(k, {})[(s, a)] = r
    return res


# ------------------------------------------------------------------ suleymaniyevakfimeali.com (owner's site, per surah)

SVM_HOME = 'MEAL-SULEYMANIYE'
SVM_BASE = 'https://www.suleymaniyevakfimeali.com'


def svm_index():
    p = os.path.join(src_dir(SVM_HOME), 'raw', 'site', 'index.html.gz')
    if not os.path.exists(p):
        t = host('suleymaniyevakfimeali.com', min_gap=0.5).get(SVM_BASE + '/', validate=lambda x: '/Meal/' in x)
        write_gz(p, t)
    t = read_gz(p)
    links = []
    for m in re.finditer(r'href="(/Meal/[^"]+\.htm)"', t):
        if m.group(1) not in links:
            links.append(m.group(1))
    return links


def svm_path(s):
    return os.path.join(src_dir(SVM_HOME), 'raw', 'site', f'{s:03d}.html.gz')


def fetch_svm(surahs):
    links = svm_index()
    if len(links) != 114:
        log(f'[svm] index has {len(links)} surah links, expected 114')
    h = host('suleymaniyevakfimeali.com', min_gap=0.5)
    _fetch_each(h, [(s,) for s in order_surahs(surahs) if s <= len(links)],
                lambda s: SVM_BASE + links[s - 1], svm_path, lambda x: 'trText' in x, 'svm', workers=1)


def svm_parse_page(h, s):
    out = {}
    blocks = re.split(r"<div id='(\d+(?:-\d+)?)'>", h)
    for i in range(1, len(blocks) - 1, 2):
        num, blk = blocks[i], blocks[i + 1]
        hdr = re.search(r'class="qrHeader">\(([^)]*?)(\d+)/(\d+)(?:-(\d+))?\)', blk)
        tm = re.search(r'<span id="[\d-]+text">(.*?)</span>', blk, re.S)
        if not tm:
            continue
        lo, hi = _rng(num, int(num.split('-')[0]))
        if hdr and hdr.group(4):
            hi = int(hdr.group(4))
        r = {'text': clean(re.sub(r'<[^>]+>', ' ', tm.group(1))), 'a_end': hi}
        nm = re.search(r'<hr />\s*<span>(.*?)</span>\s*</div>\s*</div>', blk[tm.end():], re.S)
        if nm:
            notes = html_to_paras(nm.group(1)).replace('\n\n', '\n').strip()
            if notes:
                r['notes'] = notes
        out[(s, lo)] = r
    return out


def parse_svm():
    rows = {}
    for s in range(1, 115):
        p = svm_path(s)
        if os.path.exists(p):
            rows.update(svm_parse_page(read_gz(p), s))
    return rows
