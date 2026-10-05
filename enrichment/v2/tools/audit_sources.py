#!/usr/bin/env python3
"""Read-only corpus/pack inventory. Writes only to --out; no model calls.

Run from the repo root:
  python3 -B enrichment/v2/tools/audit_sources.py --out .scratch/source-audit-new

Characters are Unicode code points, not tokens. Ayah attachment uses exactly
pack.sources_md's inclusive range rule. Exact-text reuse is an opportunity to
share displayed bodies with multiple citations, never evidence of equivalence
between editions. Extra metadata is counted separately from primary text.
"""
from pathlib import Path
import argparse
import collections as C
import csv
import hashlib
import json
import os
import sqlite3
import statistics

PG = Path(__file__).resolve().parents[3]
OUT: Path
CORPUS = PG / 'enrichment/corpus'

def save(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

def csvsave(name, rows):
    if not rows:
        return
    with (OUT / name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator='\n')
        w.writeheader()
        w.writerows(rows)

def flat(v):
    if isinstance(v, str):
        return v
    if isinstance(v, dict):
        return ' '.join(flat(x) for x in v.values())
    if isinstance(v, list):
        return ' '.join(flat(x) for x in v)
    return str(v)

def scan(dbname):
    con = sqlite3.connect(f'file:{CORPUS / dbname}?mode=ro', uri=True)
    con.execute('PRAGMA query_only=ON')
    meta = {sid: json.loads(m) for sid, m in con.execute('SELECT id, meta FROM src')}
    refs = {(s, a) for s, a in con.execute("SELECT s,a FROM seg WHERE src='QURAN' AND a>0")}
    totals = C.defaultdict(C.Counter)
    src_sizes = C.defaultdict(list)
    ay = {r: C.Counter() for r in refs}
    ay_src = C.defaultdict(C.Counter)
    ay_hash = C.defaultdict(set)
    surah = C.defaultdict(C.Counter)
    surah_hash = C.defaultdict(set)
    surah_src = C.defaultdict(C.Counter)
    digest_meta = {}
    segments = []
    extra_keys = C.Counter()
    for seg, src, s, a, ae, head, txt, extra in con.execute('SELECT seg,src,s,a,a_end,head,text,extra FROM seg'):
        txt = txt or ''
        ext = json.loads(extra or '{}')
        n = len(txt)
        extras = sum(len(flat(ext[k])) for k in ('en','tr','notes') if ext.get(k))
        h = hashlib.sha256(txt.encode()).hexdigest()
        st = totals[src]
        st.update(segments=1, text_chars=n, display_extra_chars=extras)
        st['max_segment_chars'] = max(st['max_segment_chars'], n)
        src_sizes[src].append(n)
        if ext.get('arabic_reliable') is False:
            st['arabic_unreliable_segments'] += 1
        st['replacement_characters'] += txt.count('\ufffd')
        st['empty_segments'] += not txt.strip()
        extra_keys.update(ext.keys())
        if h not in digest_meta:
            digest_meta[h] = {'chars': n, 'locs': [], 'sources': set()}
        digest_meta[h]['locs'].append(seg)
        digest_meta[h]['sources'].add(src)
        end = ae if ae is not None else a
        matches = [(s, aa) for aa in range(a, end + 1) if (s, aa) in refs] if s and a is not None and end is not None else []
        rec = dict(seg=seg,src=src,kind=meta[src].get('kind'),s=s,a=a,a_end=ae,text_chars=n,
                   display_extra_chars=extras,attached_ayat=len(matches),sha256=h)
        segments.append(rec)
        if matches:
            st.update(tied_segments=1, tied_text_chars=n, expanded_ayah_chars=n * len(matches))
            surah[s].update(tied_segments=1, unique_segment_chars=n, expanded_ayah_chars=n * len(matches))
            surah_src[s][src] += n
            if h not in surah_hash[s]:
                surah[s]['exact_unique_text_chars'] += n
                surah_hash[s].add(h)
            for ref in matches:
                ar = ay[ref]
                ar.update(segments=1,text_chars=n,display_extra_chars=extras)
                ar['largest_segment_chars'] = max(ar['largest_segment_chars'], n)
                ar['range_attached_chars'] += n if len(matches) > 1 else 0
                ay_src[ref][src] += n
                if h not in ay_hash[ref]:
                    ar['exact_unique_text_chars'] += n
                    ay_hash[ref].add(h)
                else:
                    ar['exact_repeated_text_chars'] += n
        elif s:
            st.update(surah_only_segments=1,surah_only_chars=n)
        else:
            st.update(unattached_segments=1,unattached_chars=n)
    ayrows = []
    for (s,a), cnt in ay.items():
        row = dict(ref=f'{s}:{a}',surah=s,ayah=a,**{k:cnt[k] for k in (
            'segments','text_chars','display_extra_chars','exact_unique_text_chars','exact_repeated_text_chars',
            'range_attached_chars','largest_segment_chars')}, sources=len(ay_src[s,a]))
        row['top_sources'] = '; '.join(f'{src}={n}' for src,n in ay_src[s,a].most_common(6))
        ayrows.append(row)
    ayrows.sort(key=lambda r:r['text_chars'],reverse=True)
    srows = []
    for s, cnt in surah.items():
        vals = [r['text_chars'] for r in ayrows if r['surah']==s]
        srows.append(dict(surah=s,ayat=len(vals),**dict(cnt),mean_ayah_chars=round(statistics.mean(vals)),
                          max_ayah_chars=max(vals),range_reread_factor=round(cnt['expanded_ayah_chars']/cnt['unique_segment_chars'],3),
                          top_sources='; '.join(f'{src}={n}' for src,n in surah_src[s].most_common(5))))
    srows.sort(key=lambda r:r['mean_ayah_chars'],reverse=True)
    srcrows=[]
    for sid,m in meta.items():
        cnt=totals[sid]
        ns=src_sizes[sid]
        srcrows.append(dict(id=sid,kind=m.get('kind'),language=m.get('language'),access=m.get('access'),
                            **{k:cnt[k] for k in ('segments','text_chars','display_extra_chars','tied_segments',
                            'tied_text_chars','expanded_ayah_chars','surah_only_segments','surah_only_chars',
                            'unattached_segments','unattached_chars','max_segment_chars','empty_segments',
                            'replacement_characters','arabic_unreliable_segments')},
                            median_chars=int(statistics.median(ns)) if ns else 0,
                            p95_chars=sorted(ns)[min(len(ns)-1,int(.95*len(ns)))] if ns else 0,
                            title=m.get('title'),edition=m.get('edition'),coverage=m.get('coverage'),notes=m.get('notes')))
    srcrows.sort(key=lambda r:r['text_chars'],reverse=True)
    duplicates=sorted((dict(chars=v['chars'],copies=len(v['locs']),redundant_chars=v['chars']*(len(v['locs'])-1),
                            sources=sorted(v['sources']),locs=v['locs']) for v in digest_meta.values() if len(v['locs'])>1),
                      key=lambda r:r['redundant_chars'],reverse=True)
    groups=C.defaultdict(C.Counter)
    for sid,m in meta.items():
        g=groups[m.get('kind')]
        g['sources']+=1
        g['memory_pointers']+=m.get('access')=='hafiza'
        for k in ('segments','text_chars','display_extra_chars','expanded_ayah_chars'):
            g[k]+=totals[sid][k]
    stem='islamic' if dbname=='corpus.sqlite' else 'intertext'
    csvsave(stem+'_ayah.csv',ayrows)
    csvsave(stem+'_surah.csv',srows)
    csvsave(stem+'_sources.csv',srcrows)
    csvsave(stem+'_segments.csv',segments)
    save(stem+'_duplicates.json',duplicates)
    save(stem+'_ay_sources.json',{f'{s}:{a}':dict(v.most_common()) for (s,a),v in ay_src.items()})
    save(stem+'_summary.json',dict(database=str((CORPUS/dbname).relative_to(PG)),database_mtime=(CORPUS/dbname).stat().st_mtime,
         kinds={k:dict(v) for k,v in groups.items()},sources=len(meta),local_sources=sum(m.get('access')!='hafiza' for m in meta.values()),
         segments=len(segments),text_chars=sum(r['text_chars'] for r in segments),
         display_extra_chars=sum(r['display_extra_chars'] for r in segments),quran_ayat=len(refs),
         exact_repeated_chars=sum(r['redundant_chars'] for r in duplicates),top_ayat=ayrows[:40],top_surah_mean=srows[:25],
         top_surah_total=sorted(srows,key=lambda r:r['expanded_ayah_chars'],reverse=True)[:20],
         largest_segments=sorted(segments,key=lambda r:r['text_chars'],reverse=True)[:50],extra_keys=dict(extra_keys)))
    print(stem, 'sources',len(meta),'segments',len(segments),'chars',sum(r['text_chars'] for r in segments),flush=True)
    print('top_ayah',[(r['ref'],r['text_chars']) for r in ayrows[:12]],flush=True)
    print('top_surah_mean',[(r['surah'],r['mean_ayah_chars']) for r in srows[:12]],flush=True)
    con.close()

def inventory():
    groups=C.defaultdict(C.Counter)
    by_source=C.defaultdict(C.Counter)
    pdfs=[]
    for d,dirs,files in os.walk(CORPUS):
        for name in files:
            p=Path(d)/name
            rel=p.relative_to(CORPUS)
            ext=''.join(p.suffixes[-2:]) if p.suffix in ('.gz','.zst') else p.suffix or '<extensionless>'
            role='raw' if 'raw' in rel.parts or 'pdf' in rel.parts else 'pages' if 'pages' in rel.parts else 'searchable' if name=='segments.jsonl' else 'index' if ext=='.sqlite' else 'metadata/other'
            st=p.stat()
            g=groups[role,ext]
            g.update(files=1,bytes=st.st_size)
            if len(rel.parts)>1:
                by_source[rel.parts[0]][ext]+=1
            if ext=='.pdf':
                pdfs.append(dict(path=str(rel),bytes=st.st_size,inode=st.st_ino))
    save('formats.json',dict(formats=[dict(role=k[0],extension=k[1],**v) for k,v in sorted(groups.items())],
         source_extensions={k:dict(v) for k,v in by_source.items()},pdfs=pdfs))
    packs=[]
    for pk in sorted((PG/'enrichment/v2/work').glob('s*/pack')):
        cats=C.Counter()
        largest=[]
        for p in pk.rglob('*'):
            if p.is_file():
                rel=p.relative_to(pk)
                if p.suffix in ('.md','.json'):
                    n=len(p.read_text())
                    cats[str(rel.parts[0])]+=n
                    largest.append((str(rel),n))
        packs.append(dict(path=str(pk.relative_to(PG)),category_chars=dict(cats),largest_files=sorted(largest,key=lambda t:t[1],reverse=True)[:20]))
    save('packs.json',packs)

if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--out', type=Path, required=True, help='new or empty output directory; bulk intermediates stay local')
    args = parser.parse_args()
    OUT = args.out.resolve()
    if OUT.exists() and (not OUT.is_dir() or any(OUT.iterdir())):
        parser.error('--out must be a new or empty directory; retain earlier audit snapshots')
    OUT.mkdir(parents=True, exist_ok=True)
    scan('corpus.sqlite')
    scan('corpus_intertext.sqlite')
    inventory()
