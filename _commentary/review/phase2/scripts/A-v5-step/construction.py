"""Attachment-based construction check (more precise than the phrase-collocate heuristic in kinds.py):
for each occurrence of a root, list its grammatical attachments (relation, preposition, partner root) from the
dictionary's occurrence_evidence (quran-data grammar attachments). Demonstrated on ض ر ب (root_000906):
B002 (travel) requires ḍaraba + fī + al-arḍ; B003 (parable) requires a mathal object."""
import json, collections, sys
import lib
rid = sys.argv[1] if len(sys.argv) > 1 else 'root_000906'
d = json.load(open(f'{lib.DICT}/{rid}_entry.json'))
rows = []
for o in d['occurrence_evidence']['occurrences']:
    at = (o.get('alignment') or {}).get('attachments') or []
    sig = [(a.get('relation'), a.get('prep_base') or '', a.get('other_root') or '') for a in at if a.get('focus_role') == 'head']
    rows.append((o['ayah_ref'], o['surface_ar'], sig))
def has(sig, prep=None, root=None, rel=None):
    return any((prep is None or p == prep) and (root is None or r.replace('ء','أ') in (root, root.replace('ء','أ')) or r == root) and (rel is None or rl == rel) for rl, p, r in sig)
b002 = [(a, s) for a, s, sig in rows if any(p in ('في', 'فِي') for rl, p, r in sig) and any(r in ('أ ر ض', 'ء ر ض') for rl, p, r in sig)]
b003 = [(a, s) for a, s, sig in rows if any(r == 'م ث ل' for rl, p, r in sig)]
print('occurrences', len(rows))
print('construction fi l-ard (B002):', b002)
print('mathal object (B003):', len(b003), [a for a, s in b003][:20])
for a, s, sig in rows:
    if a in ('17:48', '4:34', '4:101', '73:20', '2:273', '8:12', '47:4'):
        print(a, s, sig)
