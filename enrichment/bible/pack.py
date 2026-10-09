#!/usr/bin/env python3
"""Freeze Bible-owned copies of completed v16 texts; never rebuild the Islamic pack."""
from __future__ import annotations
import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
HERE = Path(__file__).resolve().parent
PG = HERE.parents[1]
sys.path.insert(0,str(PG))
from enrichment.bible import corpus as C, render as R


def running_calls(s):
    work = HERE/'work'/f's{s:03d}'
    starts = list(work.glob('ehlikitap*/started.json')) + list(work.glob('discovery/*/*/*/started.json'))
    return [str(p.parent.relative_to(work)) for p in starts
            if not (p.parent/'run.log.json').exists() and not (p.parent/'dead.json').exists()]


AYAH_BASES = ('augment9', 'r13')


def r13_reading(v16, s, a):
    """The frozen r13 ayah reading the v9 Islamic pages use: exactly one non-augment reading, else None/refusal."""
    d = v16/f'{s}_{a}'
    hits = [p for p in d.glob(f'*/{s}_{a}.reading.tr.md') if 'augment' not in str(p.relative_to(d))]
    if len(hits) > 1:
        raise ValueError(f'{s}:{a}: {len(hits)} r13 readings: {hits}')
    return hits[0] if hits else None


def build(s, force=False, from_pack=None, ayah_base='augment9'):
    """An explicit existing pack may select bases; it is only ever read. ayah_base: 'augment9' (S1/S87 packs) or
    'r13' (from 2026-10-09: the frozen r13 reading, the same paragraphs as the v9 Islamic pages)."""
    if ayah_base not in AYAH_BASES:
        raise ValueError(f'ayah base must be one of {AYAH_BASES}')
    if from_pack and ayah_base != 'augment9':
        raise ValueError('--from-pack selects bases already; it cannot be combined with --ayah-base r13')
    pk=HERE/'work'/f's{s:03d}'/'pack'
    if running_calls(s):
        raise ValueError(f'Bible calls active: {running_calls(s)}')
    if pk.exists() and not force:
        raise ValueError(f'{pk} exists; --force rebuilds only this Bible pack')
    if from_pack:
        supplied=json.loads((from_pack/'base.json').read_text())
        n=json.loads((from_pack/'pack.json').read_text())['ayat']
        sources={'surah':from_pack/'base/surah.md'}
        sources.update({ref:from_pack/'base'/f'{ref.replace(":","_")}.md' for ref,info in supplied['ayat'].items() if info})
        for ref,path in sources.items():
            info=supplied['surah'] if ref=='surah' else supplied['ayat'][ref]
            if C.sha256(path)!=info['sha256']:
                raise ValueError(f'{path}: selected upstream base changed')
    else:
        data=[json.loads(line) for line in (C.CORPUS/'QURAN/segments.jsonl').read_text().splitlines() if line.strip()]
        n=max(r['a'] for r in data if r.get('s')==s and r.get('a'))
        v16=PG/'_commentary/v16/out'
        surahs=list((v16/f's{s:03d}').glob('images.r13.*/images.md'))
        if len(surahs)!=1:
            raise ValueError(f'S{s}: expected one v16 r13 surah base, found {len(surahs)}; use --from-pack to select')
        sources={'surah':surahs[0]}
        for a in range(1,n+1):
            if ayah_base=='r13':
                hit=r13_reading(v16,s,a)
                if hit: sources[f'{s}:{a}']=hit
                else: print(f'WARNING {s}:{a}: no r13 ayah reading; no ayah page for it in this pack')
                continue
            hits=[p for p in (v16/f'{s}_{a}').glob(f'DM.r13.images.r13.*/{R.AYAH_AUGMENT}/{s}_{a}.reading.tr.md')
                  if 'session-limit' not in str(p)]
            if len(hits)>1: raise ValueError(f'{s}:{a}: several augment9 bases')
            if hits: sources[f'{s}:{a}']=hits[0]
    quran={f"{r['s']}:{r['a']}":r['text'] for r in map(json.loads,(C.CORPUS/'QURAN/segments.jsonl').read_text().splitlines())
           if r.get('s')==s and r.get('a') and r['a']>0}
    if len(quran)!=n: raise ValueError(f'S{s}: Quran source incomplete')
    tmp=pk.with_name('pack.building')
    if tmp.exists(): raise ValueError(f'interrupted Bible pack build: {tmp}')
    (tmp/'base').mkdir(parents=True)
    (tmp/'numbered').mkdir()
    base={'surah':None,'ayah_base':ayah_base,'ayat':{f'{s}:{a}':None for a in range(1,n+1)}}
    try:
        for ref,path in sources.items():
            name='surah.md' if ref=='surah' else ref.replace(':','_')+'.md'
            text=path.read_text()
            if ref!='surah' and R.marker_mismatches(text):
                raise ValueError(f'{path}: augment marker mismatch')
            original=(supplied['surah'] if ref=='surah' else supplied['ayat'][ref])['path'] if from_pack else str(path.relative_to(PG))
            if ref!='surah' and ayah_base=='augment9' and f'/{R.AYAH_AUGMENT}/' not in original:
                raise ValueError(f'{ref}: expected an augment9 base')
            if ref!='surah' and ayah_base=='r13' and 'augment' in original:
                raise ValueError(f'{ref}: expected an r13 reading, not an augment')
            info={'path':original,'sha256':C.sha256(path)}
            if ref=='surah': base['surah']=info
            else: base['ayat'][ref]=info
            (tmp/'base'/name).write_text(text)
            (tmp/'numbered'/name).write_text(R.numbered(text))
        (tmp/'base.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
        (tmp/'quran.json').write_text(json.dumps(quran,ensure_ascii=False,indent=2)+'\n')
        meta={'surah':s,'ayat':n,'built_at':datetime.now(timezone.utc).isoformat(),'base':base,
              'missing_ayah_bases':[ref for ref,info in base['ayat'].items() if not info],
              'files':{str(p.relative_to(tmp)):C.sha256(p) for p in tmp.rglob('*') if p.is_file()}}
        (tmp/'pack.json').write_text(json.dumps(meta,indent=2)+'\n')
        old=pk.with_name('pack.previous')
        if old.exists(): raise ValueError(f'previous Bible pack needs recovery: {old}')
        if pk.exists(): pk.rename(old)
        try: tmp.rename(pk)
        except BaseException:
            if old.exists(): old.rename(pk)
            raise
        if old.exists(): shutil.rmtree(old)
    except BaseException:
        if tmp.exists(): shutil.rmtree(tmp)
        raise
    print(f'S{s}: Bible pack {pk}; {n} ayat, {len(sources)-1} {ayah_base} ayah bases')
    return pk


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--surah',type=int,required=True)
    ap.add_argument('--from-pack',type=Path,help='read-only selection from an existing frozen pack')
    ap.add_argument('--force',action='store_true')
    ap.add_argument('--ayah-base',choices=AYAH_BASES,default='augment9',
                    help='r13: the frozen r13 reading (v9 pages; from 2026-10-09); augment9: the S1/S87 pilot packs')
    a=ap.parse_args(); build(a.surah,a.force,a.from_pack,a.ayah_base)

if __name__=='__main__': main()
