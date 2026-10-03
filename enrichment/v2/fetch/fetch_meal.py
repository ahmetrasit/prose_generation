#!/usr/bin/env python3
"""Build the local Turkish meal / translation corpus (enrichment/corpus/MEAL-*, ASAD-*, ARBERRY, KURANYOLU-TEFSIR).

  python3 fetch_meal.py fetch      [--hosts tanzil,fawaz,quranenc,alqc,kd,km,kmabout,ak,mo,svm] [--sources ID,..] [--surahs 1,22,87-114|priority|all]
  python3 fetch_meal.py build      [--sources ID,..]
  python3 fetch_meal.py crosscheck [--sources ID,..] [--out matrix.json]
  python3 fetch_meal.py status

fetch is resumable (cached raw files are skipped) and polite (<=2 concurrent requests per host,
>=0.35 s between requests, retries with backoff, stops on challenge pages). Priority surahs
(1, 22, 87-114) are fetched first. Per-ayah hosts (kuranmeali, acikkuran, mealler) keep one
cached page per ayah that holds every meal on that host."""
import argparse
import concurrent.futures as cf
import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import meal_hosts as H  # noqa: E402
from meal_common import (AYAH_COUNTS, PRIORITY, TOTAL_AYAT, all_ayat, bracket_sig, build_segments,  # noqa: E402
                         coverage_of, coverage_string, expand, load_source_json, log, norm_cmp, norm_ws,
                         parse_surahs, raw_manifest, save_source_json, sim, src_dir, write_segments)
from meal_registry import AK_IDS, KM, LIC, POINTERS, SOURCES, TEFSIR, all_sources, witness_homes  # noqa: E402

HOMES = witness_homes()
SRC = {s['id']: s for s in all_sources()}


# ------------------------------------------------------------------ witnesses

def wsplit(w):
    h, k = w.split(':', 1)
    return h, k


def load_witness(w, surahs=None):
    surahs = surahs or list(range(1, 115))
    h, k = wsplit(w)
    if h == 'tanzil':
        rows = H.parse_tanzil(HOMES[w], k)
    elif h == 'fawaz':
        rows = H.parse_fawaz(HOMES[w], k)
    elif h == 'quranenc':
        rows = H.parse_quranenc(HOMES[w], k)
    elif h == 'alqc':
        rows = H.parse_alqc(HOMES[w], k)
    elif h == 'kd':
        rows = H.parse_kd(int(k))
    elif h == 'kdtefsir':
        rows = H.parse_kd_tefsir()[0]
    elif h == 'km':
        rows = H.km_all(surahs).get(k, {})
    elif h == 'ak':
        rows = H.ak_all(surahs).get(k, {})
    elif h == 'mo':
        rows = H.mo_all(surahs).get(k, {})
    elif h == 'svm':
        rows = H.parse_svm()
    else:
        raise ValueError(w)
    ss = set(surahs)
    return {x: r for x, r in rows.items() if x[0] in ss}


def witness_url(w):
    h, k = wsplit(w)
    if h == 'tanzil':
        return H.tanzil_url(k)
    if h == 'fawaz':
        return H.fawaz_url(k)
    if h == 'quranenc':
        return H.quranenc_url(k)
    if h == 'alqc':
        return H.alqc_url(k)
    if h in ('kd', 'kdtefsir'):
        return H.kd_url(int(k), '{s}', '{a}').replace('sure-suresi', '<slug>-suresi') + '  (one request per mushaf page; page JSON MPageDmList)'
    if h == 'km':
        return "https://www.kuranmeali.com/AyetKarsilastirma.php?sure={s}&ayet={a}  (div id='%s+1')" % k
    if h == 'ak':
        u = 'https://acikkuran.com/{slug}/{a}-ayet-meali.md  (section "### %s")' % k
        if k in AK_IDS:
            u += '; whole surah without footnotes: https://acikkuran.com/{slug}.md?author=%d' % AK_IDS[k]
        return u
    if h == 'mo':
        return 'https://mealler.org/SureveAyetler.aspx?sureid={sss}&ayet={aaa}  (row "%s")' % k
    if h == 'svm':
        return H.SVM_BASE + '/Meal/{Sure}.htm'
    return w


def witness_label(w):
    h, k = wsplit(w)
    return {'tanzil': f'tanzil.net {k}', 'fawaz': f'fawazahmed0/quran-api {k}', 'quranenc': f'QuranEnc {k}', 'alqc': f'api.alquran.cloud {k}',
            'kd': f'kuran.diyanet.gov.tr meal ML={k}', 'kdtefsir': 'kuran.diyanet.gov.tr TefsirList',
            'km': f'kuranmeali.com "{KM.get(k, (k,))[0]}" ({k})', 'ak': f'acikkuran.com "{k}"',
            'mo': f'mealler.org "{k}"', 'svm': 'suleymaniyevakfimeali.com'}[h]


# ------------------------------------------------------------------ fetch

def whole_file_path(w):
    h, k = wsplit(w)
    return {'tanzil': H.tanzil_path, 'fawaz': H.fawaz_path, 'quranenc': H.quranenc_path, 'alqc': H.alqc_path}[h](HOMES[w], k)


def relocate_whole_files():
    """If the registry moved a single-file witness to another home source, move its raw file instead of re-downloading."""
    import glob
    import shutil
    for w in HOMES:
        dst = whole_file_path(w)
        if os.path.exists(dst):
            continue
        name = os.path.basename(dst)
        for cand in glob.glob(os.path.join(src_dir('*'), 'raw', name)):
            sid = os.path.basename(os.path.dirname(os.path.dirname(cand)))
            if sid.startswith(('MEAL-', 'ASAD-', 'ARBERRY')):
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.move(cand, dst)
                log(f'moved {cand} -> {dst}')
                break


def do_fetch(args):
    surahs = parse_surahs(args.surahs)
    hosts = set(args.hosts.split(',')) if args.hosts else None
    wits = set()
    for s in SOURCES:
        if args.sources and s['id'] not in args.sources:
            continue
        wits.update([s['primary']] + s['cross'])
    if args.sources and 'KURANYOLU-TEFSIR' in args.sources:
        wits.add('kd:1')
    want = lambda h: hosts is None or h in hosts
    relocate_whole_files()
    whole = sorted(w for w in wits if wsplit(w)[0] in ('tanzil', 'fawaz', 'quranenc', 'alqc'))
    jobs = []
    if want('tanzil'):
        H.fetch_arabic()
    for w in whole:
        h, k = wsplit(w)
        if want(h):
            fn = {'tanzil': H.fetch_tanzil, 'fawaz': H.fetch_fawaz, 'quranenc': H.fetch_quranenc, 'alqc': H.fetch_alqc}[h]
            try:
                fn(HOMES[w], k)
                log(f'[{h}] ok {k}')
            except Exception as e:
                log(f'[{h}] FAILED {k}: {e}')
    hs = {wsplit(w)[0] for w in wits}
    with cf.ThreadPoolExecutor(8) as ex:
        if want('kd') and 'kd' in hs:
            mls = sorted(int(wsplit(w)[1]) for w in wits if wsplit(w)[0] == 'kd')
            # ML1 first (it carries the tefsir too), then the rest, never more than 2 walks at once
            def kd_all():
                with cf.ThreadPoolExecutor(2) as kx:
                    list(kx.map(lambda m: H.fetch_kd(m, surahs), mls))
            jobs.append(ex.submit(kd_all))
        if want('km') and 'km' in hs:
            jobs.append(ex.submit(H.fetch_km, surahs))
        if want('kmabout'):
            jobs.append(ex.submit(H.fetch_km_about, sorted({v[1] for v in KM.values()})))
        if want('ak') and 'ak' in hs:
            jobs.append(ex.submit(H.fetch_ak, surahs))
        if want('mo') and 'mo' in hs:
            jobs.append(ex.submit(H.fetch_mo, surahs))
        if want('svm') and 'svm' in hs:
            jobs.append(ex.submit(H.fetch_svm, surahs))
        for j in jobs:
            try:
                j.result()
            except Exception as e:
                log(f'job failed: {e!r}')
    log('fetch done; requests per host: ' + ', '.join(f'{k}={v.n}' for k, v in H.HOSTS.items()))


# ------------------------------------------------------------------ build

def own_raw(sid):
    return raw_manifest(sid)


def shared_raw_note(src):
    notes = []
    for w in [src['primary']] + src['cross']:
        h, k = wsplit(w)
        if h == 'km' and src['id'] != H.KM_HOME:
            notes.append(f'kuranmeali pages: ../{H.KM_HOME}/raw/kuranmeali/')
        elif h == 'ak' and src['id'] != H.AK_HOME:
            notes.append(f'acikkuran pages: ../{H.AK_HOME}/raw/acikkuran/')
        elif h == 'mo' and src['id'] != H.MO_HOME:
            notes.append(f'mealler.org pages: ../{H.MO_HOME}/raw/mealler/')
        elif h in ('kd', 'kdtefsir') and src['id'] != H.KD_HOME[int(k)]:
            notes.append(f'kuran.diyanet pages: ../{H.KD_HOME[int(k)]}/raw/kd/')
        elif h in ('tanzil', 'fawaz', 'quranenc', 'alqc') and HOMES.get(w) != src['id']:
            notes.append(f'{w}: ../{HOMES[w]}/raw/')
    return sorted(set(notes))


def edition_for(src):
    ed = src.get('edition') or ''
    h, k = wsplit(src['primary'])
    if h == 'km':
        about = H.km_about(KM[k][1])
        if about:
            ed = (ed + ' | ' if ed else '') + f'kuranmeali.com about-page (Aciklama.php?id={KM[k][1]}&islem=mealbilgi): ' + about[:400]
    if not ed:
        ed = f'as published by {witness_label(src["primary"])}'
    return ed


def build_one(src, today):
    sid = src['id']
    w = src['primary']
    h, k = wsplit(w)
    intros = {}
    if h == 'kdtefsir':
        rows, intros = H.parse_kd_tefsir()
    else:
        rows = load_witness(w)
    explicit = h in ('kd', 'kdtefsir', 'svm')
    rows = {x: r for x, r in rows.items() if not r.get('_orphan')}
    segs, info = build_segments(sid, rows, explicit_groups=explicit, strip_prefix=not explicit)
    for g in segs:
        g.pop('title', None)
    attached = 0
    if src.get('notes_from'):
        nrows = load_witness(src['notes_from'])
        nlabel = witness_label(src['notes_from'])
        for g in segs:
            if g.get('notes'):
                continue
            got, trunc = [], False
            for a in range(g['a'], g['a_end'] + 1):
                r = nrows.get((g['s'], a))
                if r and r.get('notes') and r['notes'] not in got:
                    got.append(r['notes'])
                    trunc = trunc or bool(r.get('notes_truncated'))
            if got:
                g['notes'] = '\n'.join(got)
                g['notes_host'] = nlabel
                if trunc:
                    g['notes_truncated'] = True
                attached += 1
    if intros:
        out = []
        done = set()
        for g in segs:
            if g['s'] in intros and g['s'] not in done:
                out.append({'seg': f'{sid}:{g["s"]}:0', 's': g['s'], 'a': 0, 'a_end': 0, 'page': None,
                            'head': 'Sûre girişi (nüzûl, ad, konu)', 'text': intros[g['s']]})
                done.add(g['s'])
            out.append(g)
        segs = out
    if not segs:
        log(f'[build] {sid}: no text yet')
        return None
    write_segments(sid, [g for g in segs])
    cov = coverage_of([g for g in segs if g['a'] > 0])
    old = load_source_json(sid) or {}
    trunc = sum(1 for g in segs if g.get('notes_truncated'))
    withnotes = sum(1 for g in segs if g.get('notes'))
    build_notes = []
    if info['merged_groups']:
        build_notes.append(f'{info["merged_groups"]} merged verse groups stored once as a..a_end.')
    if info['prefix_stripped']:
        build_notes.append(f'{info["prefix_stripped"]} host verse-number prefixes (e.g. "6, 7.", "(6-7)") removed from the text; the range is in a..a_end.')
    if attached:
        build_notes.append(f'{attached} segments carry notes attached from {witness_label(src["notes_from"])} (field notes_host).')
    if withnotes:
        build_notes.append(f'{withnotes} segments carry footnotes in "notes"' + (f' ({trunc} truncated by the host, flagged notes_truncated)' if trunc else '') + '.')
    if info['missing']:
        build_notes.append(f'{len(info["missing"])} ayat empty on the host: ' + ', '.join(f'{s}:{a}' for s, a in info['missing'][:15]) + ('...' if len(info['missing']) > 15 else ''))
    if len(cov) < TOTAL_AYAT:
        build_notes.append(f'Coverage incomplete ({len(cov)}/{TOTAL_AYAT}); re-run `fetch_meal.py fetch --sources {sid}` then `build` to resume.')
    lic_host = 'kd' if h == 'kdtefsir' else h
    obj = {
        'id': sid, 'title': src['title'], 'author': src['author'],
        'translator': src.get('translator') or src['author'],
        'death_ah': src.get('death_ah'), 'kind': src['kind'], 'tradition': src.get('tradition') or '',
        'language': src['language'], 'edition': edition_for(src) if h != 'kdtefsir' else src['edition'],
        'access': 'yerel', 'locator': 'ayah', 'coverage': coverage_string(cov),
        'urls': [witness_url(x) for x in [w] + src['cross']],
        'fetched_at': today, 'files': own_raw(sid),
        'lineage': src.get('lineage'), 'relay': src.get('relay'),
        'licence': LIC[lic_host], 'panel': bool(src.get('panel')),
        'host_label': witness_label(w), 'cross_witnesses': [witness_label(x) for x in src['cross']],
        'notes': '',
    }
    shared = shared_raw_note(src)
    if shared:
        obj['raw_shared'] = shared
    if old.get('crosscheck'):
        obj['crosscheck'] = old['crosscheck']
    obj['_static_notes'] = src.get('notes') or ''
    obj['_build_notes'] = ' '.join(build_notes)
    obj['notes'] = compose_notes(obj)
    obj.pop('_static_notes'); obj.pop('_build_notes')
    obj['_notes_parts'] = {'static': src.get('notes') or '', 'build': ' '.join(build_notes)}
    save_source_json(sid, obj)
    return obj, len(cov), info['merged_groups']


def compose_notes(obj):
    parts = obj.get('_notes_parts') or {}
    static = obj.get('_static_notes', parts.get('static', ''))
    build = obj.get('_build_notes', parts.get('build', ''))
    out = [x for x in (static, build) if x]
    cc = obj.get('crosscheck') or {}
    if cc.get('summary'):
        out.append(cc['summary'])
    return ' '.join(out)


def build_pointer(p, today):
    obj = {'id': p['id'], 'title': p['title'], 'author': p['author'], 'death_ah': p.get('death_ah'), 'kind': p['kind'],
           'tradition': p.get('tradition', ''), 'language': p['language'], 'edition': p.get('edition', ''),
           'access': 'hafiza', 'locator': 'ayah', 'coverage': 'not held locally', 'urls': [], 'fetched_at': today,
           'files': {}, 'lineage': None, 'relay': p.get('relay'),
           'licence': 'copyrighted; no licensed online source; nothing downloaded', 'panel': False, 'notes': p['notes']}
    save_source_json(p['id'], obj)


def do_build(args):
    today = datetime.date.today().isoformat()
    report = []
    for src in all_sources():
        if args.sources and src['id'] not in args.sources:
            continue
        try:
            r = build_one(src, today)
        except FileNotFoundError as e:
            log(f'[build] {src["id"]}: raw missing ({e})')
            continue
        if r:
            report.append((src['id'], r[1], r[2]))
            log(f'[build] {src["id"]}: {r[1]} ayat, {r[2]} groups')
    for p in POINTERS:
        if not args.sources or p['id'] in args.sources:
            build_pointer(p, today)


# ------------------------------------------------------------------ crosscheck

DIAC = re.compile('[âîûÂÎÛ]')


def per_ayah(w, surahs):
    rows = load_witness(w, surahs)
    h = wsplit(w)[0]
    explicit = h in ('kd', 'svm')
    rows = {x: r for x, r in rows.items() if not r.get('_orphan')}
    segs, info = build_segments('X', rows, explicit_groups=explicit, strip_prefix=not explicit)
    return expand(segs), info['merged_groups']


def compare(pa, pb):
    common = sorted(set(pa) & set(pb))
    if not common:
        return None
    ex = lo = 0
    sims = []
    br = []
    worst = []
    for x in common:
        a, b = pa[x], pb[x]
        if norm_ws(a) == norm_ws(b):
            ex += 1
        na, nb = norm_cmp(a), norm_cmp(b)
        if na == nb:
            lo += 1
            r = 1.0
        else:
            r = sim(na, nb)
        sims.append(r)
        if bracket_sig(a) != bracket_sig(b):
            br.append(x)
        worst.append((r, x))
    worst.sort()
    n = len(common)
    return {'n': n, 'exact_pct': round(100 * ex / n, 1), 'loose_pct': round(100 * lo / n, 1),
            'mean_sim': round(sum(sims) / n, 3), 'bracket_diff': len(br),
            'bracket_diff_examples': [f'{s}:{a}' for s, a in br[:5]],
            'worst': [{'ayah': f'{s}:{a}', 'sim': round(r, 2), 'primary': pa[(s, a)][:160], 'other': pb[(s, a)][:160]}
                      for r, (s, a) in worst[:3] if r < 0.98]}


def diac_rate(p):
    return round(100 * sum(1 for t in p.values() if DIAC.search(t)) / max(1, len(p)), 1)


def do_crosscheck(args):
    surahs = PRIORITY
    for src in SOURCES:
        if args.sources and src['id'] not in args.sources:
            continue
        if not src['cross']:
            continue
        sid = src['id']
        obj = load_source_json(sid)
        if not obj:
            continue
        pa, ga = per_ayah(src['primary'], surahs)
        if not pa:
            continue
        res = {'range': 'S1, S22, S87-114', 'primary': witness_label(src['primary']),
               'primary_diacritic_pct': diac_rate(pa), 'primary_groups': ga, 'vs': {}}
        lines = []
        for w in src['cross']:
            try:
                pb, gb = per_ayah(w, surahs)
            except FileNotFoundError:
                continue
            c = compare(pa, pb)
            if not c:
                continue
            c['diacritic_pct'] = diac_rate(pb)
            c['groups'] = gb
            res['vs'][witness_label(w)] = c
            s = (f'{witness_label(w)}: n={c["n"]}, exact {c["exact_pct"]}%, loose {c["loose_pct"]}%, sim {c["mean_sim"]}'
                 f'; â/î/û in {c["diacritic_pct"]}% of ayat (primary {res["primary_diacritic_pct"]}%)')
            if c['bracket_diff']:
                s += f'; bracket counts differ in {c["bracket_diff"]} ayat (e.g. {", ".join(c["bracket_diff_examples"][:3])})'
            if gb != ga:
                s += f'; verse groups {gb} vs {ga}'
            if c['worst']:
                wv = c['worst'][0]
                s += f'; most divergent {wv["ayah"]} (sim {wv["sim"]})'
            lines.append(s)
        if lines:
            res['summary'] = 'Cross-check over S1, S22, S87-114 (primary ' + witness_label(src['primary']) + ') - ' + ' | '.join(lines) + '.'
            if args.identity_notes and sid in args.identity_notes:
                res['summary'] += ' ' + args.identity_notes[sid]
            obj['crosscheck'] = res
            obj['notes'] = compose_notes(obj)
            save_source_json(sid, obj)
            log(f'[cc] {sid}: ' + ' | '.join(lines)[:400])
    if args.out:
        identity_matrix(args.out)


def identity_matrix(out):
    """Every witness on every host over the priority surahs, with its closest other witnesses."""
    surahs = PRIORITY
    texts = {}
    for k, rows in H.km_all(surahs).items():
        texts[f'km:{k}'] = rows
    for k, rows in H.ak_all(surahs).items():
        texts[f'ak:{k}'] = rows
    for k, rows in H.mo_all(surahs).items():
        texts[f'mo:{k}'] = rows
    for w in HOMES:
        try:
            texts[w] = load_witness(w, surahs)
        except FileNotFoundError:
            pass
    for ml in (1, 4, 5, 6):
        texts[f'kd:{ml}'] = load_witness(f'kd:{ml}', surahs)
    texts['svm:site'] = load_witness('svm:site', surahs)
    per = {}
    for w, rows in texts.items():
        if not rows:
            continue
        h = wsplit(w)[0]
        explicit = h in ('kd', 'svm')
        rows = {x: r for x, r in rows.items() if not r.get('_orphan')}
        segs, _ = build_segments('X', rows, explicit_groups=explicit, strip_prefix=not explicit)
        per[w] = {x: norm_cmp(t) for x, t in expand(segs).items()}
    keys = sorted(per)
    res = {}
    for a in keys:
        best = []
        for b in keys:
            if a == b:
                continue
            common = set(per[a]) & set(per[b])
            if len(common) < 50:
                continue
            eq = sum(1 for x in common if per[a][x] == per[b][x])
            best.append((round(100 * eq / len(common), 1), b, len(common)))
        best.sort(reverse=True)
        res[a] = {'n': len(per[a]), 'closest': [{'witness': b, 'loose_equal_pct': p, 'n': n} for p, b, n in best[:4]]}
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    log(f'identity matrix -> {out}')


# ------------------------------------------------------------------ status

def do_status(args):
    def count(d, ext):
        n = 0
        for dp, dn, fn in os.walk(d):
            n += sum(1 for f in fn if f.endswith(ext))
        return n
    print('kuranmeali pages', count(os.path.join(src_dir(H.KM_HOME), 'raw', 'kuranmeali'), '.html.gz'), '/', TOTAL_AYAT)
    print('acikkuran pages ', count(os.path.join(src_dir(H.AK_HOME), 'raw', 'acikkuran'), '.md.gz'), '/', TOTAL_AYAT)
    print('mealler pages   ', count(os.path.join(src_dir(H.MO_HOME), 'raw', 'mealler'), '.html.gz'), '/', TOTAL_AYAT)
    print('svm surahs      ', count(os.path.join(src_dir(H.SVM_HOME), 'raw', 'site'), '.html.gz') - 1, '/ 114')
    for ml in (1, 4, 5, 6):
        idx = H.kd_cached_pages(ml)
        cov = {tuple(x) for v in idx.values() for x in v}
        print(f'kd ML{ml} pages', len(idx), 'ayat', len(cov), '/', TOTAL_AYAT)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cmd', choices=['fetch', 'build', 'crosscheck', 'status'])
    ap.add_argument('--surahs', default='all', help="'1,22,87-114', 'priority' or 'all' (fetch only)")
    ap.add_argument('--sources', default=None, help='comma-separated source IDs (default: all)')
    ap.add_argument('--hosts', default=None, help='fetch only: tanzil,fawaz,quranenc,alqc,kd,km,kmabout,ak,mo,svm')
    ap.add_argument('--out', default=None, help='crosscheck: write the identity matrix JSON here')
    ap.add_argument('--identity-notes', default=None, help='crosscheck: JSON file {source_id: extra identity note}')
    args = ap.parse_args()
    args.sources = set(args.sources.split(',')) if args.sources else None
    if args.identity_notes:
        args.identity_notes = json.load(open(args.identity_notes, encoding='utf-8'))
    {'fetch': do_fetch, 'build': do_build, 'crosscheck': do_crosscheck, 'status': do_status}[args.cmd](args)


if __name__ == '__main__':
    main()
