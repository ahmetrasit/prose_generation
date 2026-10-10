import csv, json, runpy
D = '/Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/ehlikitap.103_3.opus.high.a2/'
DISC = '/Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/discovery/s103-20261009/'
J = runpy.run_path(D + 'judgements.py')
csv.field_size_limit(10**9)
anns = {}
for l in open(D + 'annotations.jsonl', encoding='utf-8'):
    r = json.loads(l); anns[r['id']] = r
def kaynak(aid):
    return [x for x in anns[aid]['kaynak'].split('|') if x != 'hafiza']
def full(a): return J['A'] + a

rows = list(csv.DictReader(open(DISC + '103_3.merged.tsv', encoding='utf-8'), delimiter='\t'))
out, missing = [], []
for r in rows:
    ref = r['ref']
    for e in json.loads(r['evidence']):
        cid = e['connection_id']
        bible = ref.startswith(('WLC:', 'SBLGNT:'))
        if cid in J['ACC']:
            p, aid, reason = J['ACC'][cid]
            loc = ref if bible else J['ACC_SEF'][cid]
            ev = [loc] + [k for k in kaynak(full(aid)) if k != loc]
            out.append(dict(connection_id=cid, ref=ref, status='accepted', reason=reason, paragraphs=[p], evidence=ev, annotations=[full(aid)]))
        elif cid in J['CID_REJ']:
            loc, reason = J['CID_REJ'][cid]
            out.append(dict(connection_id=cid, ref=ref, status='rejected', reason=reason, paragraphs=[], evidence=[loc], annotations=[]))
        elif bible and J['REJ'].get(ref):
            out.append(dict(connection_id=cid, ref=ref, status='rejected', reason=J['REJ'][ref], paragraphs=[], evidence=[ref], annotations=[]))
        elif ref in J['SEF']:
            st, loc, reason = J['SEF'][ref]
            out.append(dict(connection_id=cid, ref=ref, status=st, reason=reason, paragraphs=[], evidence=[loc], annotations=[]))
        elif ref in J['UNAVAILABLE']:
            out.append(dict(connection_id=cid, ref=ref, status='unavailable', reason=J['UNAVAILABLE'][ref], paragraphs=[], evidence=[], annotations=[]))
        else:
            missing.append((cid, ref))
# research verdicts for own lookups
for ref, (st, p, aid, reason) in J['RESEARCH'].items():
    if st == 'accepted':
        ev = [ref] + [k for k in kaynak(full(aid)) if k != ref]
        out.append(dict(connection_id=None, origin='research', ref=ref, status=st, reason=reason, paragraphs=[p], evidence=ev, annotations=[full(aid)]))
    else:
        out.append(dict(connection_id=None, origin='research', ref=ref, status=st, reason=reason, paragraphs=[], evidence=[ref] if st == 'rejected' else [], annotations=[]))
# research verdicts for each opened Sefaria locator of discovery refs
acc_sef = {}
for cid, loc in J['ACC_SEF'].items():
    acc_sef[loc] = J['ACC'][cid]
for ref, (st, loc, reason) in J['SEF'].items():
    out.append(dict(connection_id=None, origin='research', ref=loc, status='rejected', reason='Locator opened for discovery ref ' + ref + '. ' + reason, paragraphs=[], evidence=[loc], annotations=[]))
for loc, (p, aid, reason) in acc_sef.items():
    ev = [loc] + [k for k in kaynak(full(aid)) if k != loc]
    out.append(dict(connection_id=None, origin='research', ref=loc, status='accepted', reason='Locator opened for an accepted discovery ref. ' + reason, paragraphs=[p], evidence=ev, annotations=[full(aid)]))
with open(D + 'verdicts.jsonl', 'w', encoding='utf-8') as f:
    for o in out:
        f.write(json.dumps(o, ensure_ascii=False) + '\n')
print('verdicts', len(out), 'missing', missing)
from collections import Counter
print(Counter(o['status'] for o in out))
used = set(a for o in out if o['status'] == 'accepted' for a in o['annotations'])
print('annotations without accepted verdict', sorted(set(anns) - used))
