#!/usr/bin/env python3
"""Require an explicit evidence verdict for every Bible discovery connection."""
import argparse
from collections import Counter
from contextlib import closing
import csv
import json
from pathlib import Path
import re
import shlex
import sqlite3
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from enrichment.bible import discovery as D, render as R

STATUSES = {'accepted','rejected','unresolved','unavailable'}


def candidates(path):
    expected = {}
    with path.open() as stream:
        for row in csv.DictReader(stream,delimiter='\t'):
            evidence = json.loads(row['evidence'])
            if not evidence: raise ValueError(f"candidate without reader evidence: {row['ref']}")
            for item in evidence:
                cid = D.connection_id(row['target'],item)
                if item.get('connection_id') != cid or item['ref'] != row['ref'] or item['tradition'] != row['tradition']:
                    raise ValueError('invalid connection identity in handoff')
                expected[cid] = dict(ref=row['ref'],target=row['target'],tradition=row['tradition'],
                                     kind=item['kind'],basis=item['basis'],note=item['note'])
    return expected


def lookup_audit(calls):
    """Use actual get results for evidence; commands alone do not prove text was shown."""
    requested, opened = set(), set()
    for call in calls:
        if call.get('name') != 'Bash': continue
        try: args = shlex.split(str((call.get('input') or {}).get('command','')))
        except ValueError: continue
        if len(args)<3 or Path(args[1]).name!='corpus.py': continue
        tail=args[2:]
        if tail and tail[0]=='--intertext': tail=tail[1:]
        if not tail or tail[0]!='get': continue
        refs, skip = [], False
        for token in tail[1:]:
            if skip: skip=False; continue
            if token.startswith('--'): skip=True; continue
            refs.append(token)
        requested.update(refs)
        if call.get('is_error'): continue
        result = call.get('result','')
        if not isinstance(result,str): continue
        for match in re.finditer(r'^== (\S+)([^\n]*)\n([^\n]*)',result,re.M):
            ref, header, body = match.groups()
            if 'NOT FOUND' in header or not body.strip() or body.startswith('== '): continue
            if any(ref == r or ref.startswith(r+'#') for r in refs): opened.add(ref)
    return requested,opened


ROOT_DECISIONS = {'used','no_qualifying_parallel','false_friend','no_hebrew_cognate'}


def call_roots(d):
    """The Arabic roots of a call's frozen text (its Semitic root table), recorded by the preparing script in
    started.json; None for calls prepared before 2026-10-09."""
    f = d/'started.json'
    if not f.is_file(): return None
    return json.loads(f.read_text()).get('semitic_roots')


def check_roots(d, roots, annotations, paragraphs):
    """Every Arabic root of the table needs exactly one decision in root_verdicts.jsonl (no silent skip)."""
    errors, seen = [], {}
    path = d/'root_verdicts.jsonl'
    if not path.is_file():
        return [f'missing root_verdicts.jsonl: {len(roots)} Arabic roots need a decision'] if roots else []
    for i, text in enumerate(path.read_text().splitlines(), 1):
        if not text.strip(): continue
        prefix = f'root verdict {i}'
        try:
            row = json.loads(text)
            if not isinstance(row, dict): raise ValueError('expected an object')
        except (ValueError, TypeError) as exc:
            errors.append(f'{prefix}: {exc}'); continue
        root = ' '.join(str(row.get('root','')).split())
        if root not in roots: errors.append(f'{prefix}: {root!r} is not a root of this call'); continue
        if root in seen: errors.append(f'{prefix}: duplicate decision for {root}'); continue
        seen[root] = row
        if row.get('decision') not in ROOT_DECISIONS:
            errors.append(f'{prefix}: decision must be one of {sorted(ROOT_DECISIONS)}')
        if not isinstance(row.get('reason'),str) or not row['reason'].strip():
            errors.append(f'{prefix}: a specific reason is required')
        for key in ('hebrew','paragraphs','annotations'):
            if not isinstance(row.get(key), list):
                errors.append(f'{prefix}: {key} must be an array'); break
        else:
            if not set(row['paragraphs']).issubset(paragraphs): errors.append(f'{prefix}: invalid paragraph number')
            if row.get('decision') == 'used':
                if not row['annotations'] or not row['hebrew']:
                    errors.append(f'{prefix}: a used root names its Hebrew/Aramaic root and kept annotations')
                for rid in row['annotations']:
                    if rid not in annotations: errors.append(f'{prefix}: annotation {rid} was absent or dropped')
    missing = [r for r in roots if r not in seen]
    if missing: errors.append(f"{len(missing)} Arabic roots have no decision: {', '.join(missing)}")
    return errors


def check(d, discovery, base, kept, calls=None, require_opened=True, research_scopes=None, roots=None):
    errors = []
    roots = call_roots(d) if roots is None else roots
    expected = candidates(discovery)
    rows = []
    path = d/'verdicts.jsonl'
    if not path.is_file(): errors.append('missing verdicts.jsonl (an explicit empty file is required for zero verdicts)')
    else:
        for line,text in enumerate(path.read_text().splitlines(),1):
            if not text.strip(): continue
            try:
                obj=json.loads(text)
                if not isinstance(obj,dict): raise ValueError('expected an object')
                rows.append(obj)
            except (ValueError,TypeError) as exc: errors.append(f'verdict line {line}: {exc}')
    try:
        gaps=json.loads((d/'gaps.json').read_text())
        if not isinstance(gaps,dict) or any(not isinstance(gaps.get(k),list) for k in ('missing_sources','not_found','unresolved')):
            raise ValueError('gaps.json requires missing_sources, not_found and unresolved arrays')
    except (OSError,ValueError) as exc:
        gaps={}; errors.append(str(exc))
    prefetched=json.loads((discovery.parent/'prefetch.json').read_text())
    gap_text=json.dumps(gaps,ensure_ascii=False)
    for ref in prefetched.get('missing',[]):
        if ref not in gap_text: errors.append(f'prefetch gap is missing from gaps.json: {ref}')
    if calls is None:
        tc=d/'tool_calls.json'
        calls=json.loads(tc.read_text()) if tc.exists() else []
    requested,opened=lookup_audit(calls)
    seen, research_seen, judged, covered_annotations = set(),set(),set(),set()
    annotations={r['id']:r for r in kept}
    paragraphs=set(R.prose_index(R.paragraphs(base)))
    with closing(sqlite3.connect(f'file:{D.INDEX}?mode=ro',uri=True)) as con:
        for i,row in enumerate(rows,1):
            prefix=f'verdict {i}'
            cid,ref,status=row.get('connection_id'),row.get('ref'),row.get('status')
            if not isinstance(ref,str) or not ref.strip():
                errors.append(f'{prefix}: ref is required'); continue
            if not isinstance(cid,(str,type(None))):
                errors.append(f'{prefix}: connection_id must be a discovery ID or null'); continue
            if cid:
                if cid not in expected or ref != expected[cid]['ref']:
                    errors.append(f'{prefix}: unknown or mismatched discovery connection')
                elif cid in seen: errors.append(f'{prefix}: duplicate discovery verdict')
                else: seen.add(cid)
            else:
                if row.get('origin')!='research': errors.append(f'{prefix}: own research must name origin:research')
                scope=row.get('scope')
                if research_scopes is not None and scope not in research_scopes:
                    errors.append(f'{prefix}: invalid research image scope')
                if research_scopes is None and scope is not None:
                    errors.append(f'{prefix}: research scope is only allowed for a checked image assembly')
                research_key=(scope,ref) if research_scopes is not None else ref
                if research_key in research_seen: errors.append(f'{prefix}: duplicate research verdict for {ref}')
                research_seen.add(research_key)
            if status not in STATUSES: errors.append(f'{prefix}: invalid status')
            if not isinstance(row.get('reason'),str) or not row['reason'].strip():
                errors.append(f'{prefix}: a specific reason is required')
            malformed=False
            for key in ('paragraphs','evidence','annotations'):
                value=row.get(key)
                valid=isinstance(value,list) and all(type(v) is int if key=='paragraphs' else isinstance(v,str) and bool(v.strip()) for v in value)
                if not valid:
                    errors.append(f'{prefix}: {key} must be a typed array'); malformed=True
            if malformed: continue
            if not set(row['paragraphs']).issubset(paragraphs): errors.append(f'{prefix}: invalid paragraph number')
            if status=='accepted' and (not row['paragraphs'] or not row['annotations'] or not row['evidence']):
                errors.append(f'{prefix}: acceptance requires paragraphs, kept annotations and opened evidence')
            if status in ('accepted','rejected') and cid and ref.startswith(('WLC:','SBLGNT:')) and ref not in row['evidence']:
                errors.append(f'{prefix}: verify the cited original-language verse before accepting or rejecting')
            for loc in row['evidence']:
                if not con.execute('SELECT 1 FROM seg WHERE seg=?',(loc,)).fetchone():
                    errors.append(f'{prefix}: unresolved evidence locator {loc}')
                if require_opened and loc not in opened: errors.append(f'{prefix}: evidence was not opened with corpus get: {loc}')
            for rid in row['annotations']:
                if rid not in annotations: errors.append(f'{prefix}: annotation {rid} was absent or dropped'); continue
                annotation=annotations[rid]
                para=int(str(annotation['paragraf']).strip().lstrip('¶').strip())
                if para not in row['paragraphs']: errors.append(f'{prefix}: annotation paragraph differs from verdict')
                if status=='accepted' and (annotation.get('durum')=='degerlendirilmedi' or annotation.get('tur')=='elenen'):
                    errors.append(f'{prefix}: an unverified/rejected annotation cannot implement acceptance')
                cited={loc.strip() for loc in annotation['kaynak'].split('|') if loc.strip()!='hafiza'}
                local={loc for loc in cited if con.execute('SELECT 1 FROM seg WHERE seg=?',(loc,)).fetchone()}
                if not local.issubset(set(row['evidence'])):
                    errors.append(f'{prefix}: verdict evidence must cover the annotation local citations')
                covered_annotations.add(rid)
            if status in ('unresolved','unavailable'):
                gap_text=json.dumps(gaps.get('unresolved',[]) if status=='unresolved' else
                                    gaps.get('missing_sources',[])+gaps.get('not_found',[]),ensure_ascii=False)
                if ref not in gap_text: errors.append(f'{prefix}: {status} passage must be recorded in gaps.json: {ref}')
            judged.add(ref)
    missing=sorted(set(expected)-seen)
    unjudged=sorted((requested|opened)-judged)
    uncovered=sorted(set(annotations)-covered_annotations)
    if missing: errors.append(f'{len(missing)} discovery connections have no verdict')
    if unjudged: errors.append(f'{len(unjudged)} looked-up passages have no verdict (context-only passages need a reason too)')
    if uncovered: errors.append(f'{len(uncovered)} kept annotations have no verdict')
    if roots is not None:
        errors.extend(check_roots(d, roots, annotations, paragraphs))
    return dict(ok=not errors,semitic_roots=len(roots) if roots is not None else None,errors=errors,discovery_connections=len(expected),verdicts=len(rows),draft=not require_opened,
                status_counts=dict(Counter(r.get('status','missing') for r in rows)),
                missing_connections=missing,lookups_without_verdicts=unjudged,annotations_without_verdicts=uncovered,
                requested=sorted(requested),opened=sorted(opened),
                limits='Structural coverage and opened-evidence checks; semantic and quotation accuracy still need editorial review.')


def main():
    from enrichment.bible import enrich as E, validate as V
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--surah',type=int,required=True)
    ap.add_argument('--target',required=True)
    ap.add_argument('--annotations',type=Path,required=True)
    ap.add_argument('--report',type=Path)
    ap.add_argument('--draft',action='store_true',help='check structure while working; final transcript evidence is checked at finish')
    a=ap.parse_args()
    kept,dropped,_=V.check_records(a.surah,a.target,R.load(a.annotations))
    report=check(a.annotations.parent,E.discovery_list(a.surah,a.target),R.target_page(a.surah,a.target)[1],kept,
                 require_opened=not a.draft)
    if dropped: report['errors'].append('annotations contain invalid records'); report['ok']=False
    if a.report: D.save(a.report,report)
    print(json.dumps(report,ensure_ascii=False,indent=2))
    if not report['ok']: raise SystemExit(1)


if __name__=='__main__': main()
