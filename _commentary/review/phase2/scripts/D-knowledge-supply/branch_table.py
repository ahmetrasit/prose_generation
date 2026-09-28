#!/usr/bin/env python3
"""Unified per-branch table for the knowledge-supply policy (read-only; writes only to this scratch dir).

Joins, for every branch of every root in the Turkish dictionary entries (quran-data/data/dictionary/tr/*_entry.json):
  branch_kind + lexicalization note, early-source list (MQ AY JA SI TA MU), Arabic image / what_is / source phrase,
  Turkish concept + contextual + lexical glosses, root use count (v15 lemmas.tsv = QAC), branch index and count,
  activation history: HFT (any step / baseline-model step / surprising-outlier step), v12 cross-run anchors,
  channel-review motif citations, root-dossier plain branch (dominant role) counts.
Output: branches.tsv (one row per branch) + branches.json (gloss lists for the recall detector).
"""
import csv, glob, json, os, re
from collections import Counter, defaultdict

P = '/Volumes/OZTURK/_projects'
OUT = os.path.dirname(os.path.abspath(__file__))
csv.field_size_limit(10**9)

# ---- root use counts (QAC words per root) from v15 lemmas.tsv
root_uses = Counter()
root_letters_by_id = {}
for r in csv.DictReader(open(f'{P}/prose_generation/_commentary/v15/data/lemmas.tsv', encoding='utf-8'), delimiter='\t'):
    root_uses[r['root']] += int(r['count'])
for r in csv.DictReader(open(f'{P}/prose_generation/_commentary/v15/data/branches.tsv', encoding='utf-8'), delimiter='\t'):
    root_letters_by_id[r['root_id']] = r['root']

# ---- HFT activation
hft_any, hft_base, hft_out, hft_delta = Counter(), Counter(), Counter(), Counter()
for f in glob.glob(f'{P}/latent_activation/focus_trace/runs/s*/readers/reader_hft_a/*.focus_trace.json'):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for sect, ctr in (('baseline_models', hft_base), ('context_deltas', hft_delta), ('surprising_valid_outliers', hft_out)):
        for m in d.get(sect, []) or []:
            for st in m.get('activation_trace', []) or []:
                rid, bid = st.get('mapped_root_id'), st.get('branch_id')
                if rid and bid:
                    k = f'{rid}/{bid}'
                    ctr[k] += 1
                    hft_any[k] += 1

# ---- v12 anchors
v12 = Counter()
for f in glob.glob(f'{P}/quran-data/data/analysis/ayah-activation/v12-cross-run/tr/*_ayah_findings_publication.json'):
    d = json.load(open(f, encoding='utf-8'))
    for a in d.get('ayat', []):
        for fd in a.get('findings', []):
            if fd.get('grade') == 'reject':
                continue
            for anc in fd.get('anchors', []):
                if len(anc) == 3:
                    for b in anc[2]:
                        v12[f'{anc[1]}/{b}'] += 1

# ---- channel reviews
chan = Counter()
for f in glob.glob(f'{P}/quran-data/data/analysis/channels/network-v3/s*/review/reader_a_pilot.md'):
    for m in re.finditer(r'(root_\d{6}):(B\d{3})', open(f, encoding='utf-8').read()):
        chan[f'{m.group(1)}/{m.group(2)}'] += 1

# ---- root-dossier plain branch (dominant role) counts
dossier_dom, dossier_roots = Counter(), set()
p = f'{P}/root-dossier/out/activation_map.tsv'
for r in csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'):
    if r.get('branch_ref'):
        dossier_roots.add(r['branch_ref'].split('/')[0])
        if r.get('role') == 'dominant':
            dossier_dom[r['branch_ref']] += 1

rows, gl = [], {}
for f in sorted(glob.glob(f'{P}/quran-data/data/dictionary/tr/root_*_entry.json')):
    d = json.load(open(f, encoding='utf-8'))
    rid = d['root_envelope_id']
    letters = root_letters_by_id.get(rid, '')
    brs = d.get('branches', [])
    occ = (d.get('occurrence_evidence') or {}).get('summary', {}) or {}
    for i, b in enumerate(brs):
        ref = b['branch_ref']
        bid = ref.split('/')[1]
        ls = b.get('lexicalization_scope') or {}
        cg = (b.get('concept_gloss') or {}).get('text') or ''
        ctx = [g.get('text') or '' for g in b.get('contextual_glosses', []) or []]
        lex = [g.get('target_gloss') or '' for g in b.get('lexical_glosses', []) or []]
        src = b.get('sources', []) or []
        rows.append({
            'branch_ref': ref, 'root_id': rid, 'root': letters, 'branch': bid, 'idx': i + 1, 'n_branches': len(brs),
            'root_words': occ.get('word_count', root_uses.get(letters, 0)) or 0,
            'root_uses_v15': root_uses.get(letters, 0),
            'branch_kind': ls.get('branch_kind', ''), 'scope_note': (ls.get('note') or '').replace('\t', ' '),
            'n_sources': len(src), 'sources': ' '.join(src),
            'image_ar': b.get('branch_image_ar', ''), 'what_is_ar': (b.get('what_is_ar') or '').replace('\t', ' '),
            'phrase_ar': (b.get('source_phrase_ar') or '').replace('\t', ' '),
            'tr_concept': cg, 'tr_glosses': ' ; '.join(ctx + lex),
            'status': (b.get('identity_judgment') or {}).get('status', ''),
            'hft_any': hft_any.get(ref, 0), 'hft_base': hft_base.get(ref, 0), 'hft_delta': hft_delta.get(ref, 0),
            'hft_outlier': hft_out.get(ref, 0), 'v12': v12.get(ref, 0), 'channel': chan.get(ref, 0),
            'dossier_root': int(rid in dossier_roots), 'dossier_dominant': dossier_dom.get(ref, 0),
        })
        gl[ref] = {'concept': cg, 'ctx': ctx, 'lex': lex, 'image_ar': b.get('branch_image_ar', ''),
                   'what_is_ar': b.get('what_is_ar', ''), 'phrase_ar': b.get('source_phrase_ar', ''),
                   'kind': ls.get('branch_kind', ''), 'note': ls.get('note', '')}

cols = list(rows[0].keys())
with open(os.path.join(OUT, 'branches.tsv'), 'w', encoding='utf-8') as fh:
    fh.write('\t'.join(cols) + '\n')
    for r in rows:
        fh.write('\t'.join(str(r[c]) for c in cols) + '\n')
json.dump(gl, open(os.path.join(OUT, 'branches.json'), 'w', encoding='utf-8'), ensure_ascii=False)

# ---- summary
print('branches', len(rows), 'roots', len({r['root_id'] for r in rows}))
print('branch_kind', Counter(r['branch_kind'] for r in rows).most_common())
q = [r for r in rows if r['root_words']]
print('Quranic (root_words>0)', len(q))
def bucket(n):
    n = int(n)
    return '0-1' if n <= 1 else '2-10' if n <= 10 else '11-100' if n <= 100 else '>100'
tab = defaultdict(Counter)
for r in q:
    act = r['hft_any'] > 0 or r['v12'] > 0
    tab[bucket(r['root_words'])]['n'] += 1
    tab[bucket(r['root_words'])]['never'] += (not act)
for k in ('0-1', '2-10', '11-100', '>100'):
    print(k, tab[k]['n'], tab[k]['never'], round(tab[k]['never'] / max(1, tab[k]['n']), 3))
kk = defaultdict(Counter)
for r in q:
    act = r['hft_any'] > 0 or r['v12'] > 0
    kk[r['branch_kind']]['n'] += 1; kk[r['branch_kind']]['never'] += (not act)
    kk[r['branch_kind']]['base'] += r['hft_base'] > 0
print('never-activated and HFT-baseline rate by branch_kind:')
for k, c in kk.items():
    print(' ', k, c['n'], 'never', round(c['never'] / c['n'], 3), 'in_baseline', round(c['base'] / c['n'], 3))
