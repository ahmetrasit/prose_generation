#!/usr/bin/env python3
"""Test (1), manual labels: which dictionary branches does context-only Opus (v9 w10-opus-cold, 'memory') reach unaided?

Labels come from my reading of every lexical-claim sentence of the cold readings (../r2/lex_claims_w10-opus-cold.txt,
produced by ../r2/lex_claims.py; line ids quoted below) and of the root sentences (../root_sents.py). A branch is a
cold 'latent' positive when the cold reading states that sense of the word's root (in Turkish, transliteration or
Arabic), other than the sense the word has in the ayah. The plain sense of each word is always known and is
excluded from the rates. Only the 13 ayat whose identity roots I could annotate completely are rated (1:1-1:7,
18:86, 100:1, 100:6, 100:10, 103:1, 103:2); denominators are all branches of their identity roots.

Comparison: the dictionary-fed v9 arms (Phase 1 q2a_branches.tsv, signals A_strict/A_loose = distinctive
non-Quranic Arabic tokens of the branch quoted by the fed arm). That detector sees Arabic script only, so it is
a lower bound for the fed arms; my manual labels for the cold arm are generous. 'fed-only' is therefore a lower
bound on what memory did not supply.
Writes recall_manual.tsv (one row per ayah x branch) and prints class tables."""
import csv, sys
from collections import defaultdict, Counter
from pathlib import Path
csv.field_size_limit(10**9)
HERE = Path(__file__).resolve().parent
B = [r for r in csv.DictReader(open(HERE.parent / 'branches.tsv', encoding='utf-8'), delimiter='\t')]
BY = defaultdict(list)
for r in B:
    BY[r['root']].append(r)
Q2A = Path('/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/'
           'scratchpad/phase1/dilution/q2a_branches.tsv')

ROOTS = {  # identity roots from v9/input/v2/<s>/<S_A>/01_dictionary.md headers (ECHO excluded; alt root kept)
    '1:1': ['س م و', 'ء ل ه', 'ر ح م', 'و س م'], '1:2': ['ح م د', 'ء ل ه', 'ر ب ب', 'ع ل م'], '1:3': ['ر ح م'],
    '1:4': ['م ل ك', 'ي و م', 'د ي ن'], '1:5': ['ع ب د', 'ع و ن'], '1:6': ['ه د ي', 'ص ر ط', 'ق و م'],
    '1:7': ['ص ر ط', 'ن ع م', 'غ ي ر', 'غ ض ب', 'ض ل ل'],
    '18:86': ['ب ل غ', 'غ ر ب', 'ش م س', 'و ج د', 'ع ي ن', 'ح م ء', 'ع ن د', 'ق و م', 'ق و ل', 'ق ر ن', 'ع ذ ب', 'ء خ ذ', 'ح س ن'],
    '100:1': ['ع د و', 'ض ب ح'], '100:6': ['ء ن س', 'ر ب ب', 'ك ن د'], '100:10': ['ح ص ل', 'ص د ر'],
    '103:1': ['ع ص ر'], '103:2': ['ء ن س', 'خ س ر'],
}
# plain branch(es) of each word in its ayah (my judgment; for unlisted roots: the branch with most dossier-dominant,
# then HFT-baseline hits)
PLAIN = {'1:1': ['س م و B005', 'ر ح م B001', 'و س م B001', 'ء ل ه B001', 'ء ل ه B002'],
         '1:2': ['ح م د B001', 'ر ب ب B001', 'ع ل م B003', 'ء ل ه B001', 'ء ل ه B002'],
         '1:3': ['ر ح م B001'], '1:4': ['د ي ن B002', 'م ل ك B002', 'م ل ك B003', 'ي و م B003'], '1:5': ['ع ب د B003', 'ع و ن B001'],
         '1:6': ['ه د ي B001', 'ص ر ط B001', 'ق و م B008'],
         '1:7': ['ص ر ط B001', 'ن ع م B001', 'غ ي ر B005', 'ض ل ل B001'],
         '18:86': ['غ ر ب B006', 'ع ي ن B006', 'ح م ء B001', 'ب ل غ B001', 'ش م س B001', 'و ج د B001', 'ع ن د B004',
                   'ق و م B001', 'ق ر ن B006', 'ع ذ ب B005', 'ء خ ذ B010', 'ح س ن B002'], '100:1': ['ع د و B002', 'ض ب ح B001'],
         '100:6': ['ر ب ب B001', 'ك ن د B002', 'ء ن س B001'], '100:10': ['ح ص ل B001', 'ص د ر B001'],
         '103:1': ['ع ص ر B001'], '103:2': ['خ س ر B001', 'ء ن س B001']}
# cold latent positives: (branch, evidence line in lex_claims_w10-opus-cold.txt / note)
COLD = {
    '1:1': [('س م و B001', '032 yükseklik'), ('س م و B004', '032 sema'), ('ر ح م B003', '061 ana rahmi'),
            ('ر ح م B002', '062-063 akrabalık 4:1')],  # 034 damga/iz = و س م B001, the alt root's own sense (plain)
    '1:2': [('ر ب ب B002', '054 Ragib: asama asama gelistirme'), ('ع ل م B001', '094 ilim'),
            ('ع ل م B002', '095-105 alamet, 42:32 a`lam (daglar gibi), alem as sign')],
    '1:3': [('ر ح م B003', '075 rahim'), ('ر ح م B002', '086 4:1 erham')],
    '1:4': [('د ي ن B003', '072 deyn borc'), ('د ي ن B001', '068 109:6 din'), ('د ي ن B004', '127 medin: buyruk altinda')],
    '1:5': [('ع ب د B005', '094 tariq mu`abbad'), ('ع ب د B001', '176 kul, kole')],
    '1:6': [('ه د ي B003', '026 hadi: atin boynu, onden giden'), ('ه د ي B004', '028 hediyye'),
            ('ص ر ط B002', '058-061 yutmak'), ('ق و م B002', '080 kame: ayaga kalkti')],
    '1:7': [('ص ر ط B002', '029 saraṭa'), ('ن ع م B002', '044-045 yumusak'), ('غ ي ر B003', '101 degistirdi'),
            ('ض ل ل B005', '116 dalla'), ('ض ل ل B002', '117 dalla l-ma`u fi l-laban (reversed; phrase unattested)')],
    '18:86': [('غ ر ب B007', '013-014 uzaklasmak, garib'), ('ع ي ن B001', '031-037 goz'),
              ],  # 18:77 lattakhadhta = ء خ ذ B010, the plain sense here
    '100:1': [('ع د و B003', '029 aduvv 2:36'), ('ع د و B001', '030-032 7:163, 2:229'), ('ع د و B004', '041 baskasinin alanina gecme'),
              ('ض ب ح B003', '047/068 atesin yuzeyi yakmasi')],
    '100:6': [('ر ب ب B002', '020 olgunluga ulastirma'), ('ك ن د B003', '030-031 ard kanud (collocation; construction absent)'),
              ('ك ن د B001', '033 kesmek')],
    '100:10': [('ح ص ل B002', '021 ikhraj al-lubb'), ('ص د ر B002', '100 on'), ('ص د ر B004', '103 cikis yeri'),
               ('ص د ر B003', '104 99:6 yasduru')],
    '103:1': [('ع ص ر B002', '061-067 sikmak 12:36'), ('ع ص ر B003', '071 mu`sirat 78:14')],
    '103:2': [('خ س ر B003', '031 55:9 teraziyi eksik'), ('ء ن س B003', '092 unsiyet'), ('ء ن س B002', '092 sezip fark etme')],
}

# fed arm hits (v9 dict-fed arms), Phase 1 q2a_branches.tsv
fed = defaultdict(set)
for r in csv.DictReader(open(Q2A, encoding='utf-8'), delimiter='\t'):
    if r['echo'] == '1':
        continue
    if r['dictv9_A_strict'] or r['dictv9_A_loose']:
        fed[r['ayah']].add(r['branch'])


def find(root, bid):
    return next((x for x in BY[root] if x['branch'] == bid), None)


rows = []
for ay, roots in ROOTS.items():
    plain = set(PLAIN.get(ay, []))
    for rt in roots:
        brs = BY.get(rt, [])
        if not any(f'{rt} {x["branch"]}' in plain for x in brs) and brs:
            best = max(brs, key=lambda x: (int(x['dossier_dominant']), int(x['hft_base'])))
            plain.add(f'{rt} {best["branch"]}')
    pos = {b for b, _ in COLD.get(ay, [])}
    for rt in roots:
        for x in BY.get(rt, []):
            key = f'{rt} {x["branch"]}'
            rows.append({'ayah': ay, 'branch': key, 'ref': x['branch_ref'], 'kind': x['branch_kind'],
                         'root_words': int(x['root_words'] or 0), 'n_sources': int(x['n_sources']),
                         'idx': int(x['idx']), 'hft_any': int(x['hft_any']), 'hft_base': int(x['hft_base']),
                         'v12': int(x['v12']), 'dossier_dom': int(x['dossier_dominant']),
                         'plain': int(key in plain), 'cold': int(key in pos or key in plain),
                         'fed': int(key in fed[ay]), 'concept': x['tr_concept'][:60]})
missing = [b for ay in COLD for b, _ in COLD[ay] if not any(r['ayah'] == ay and r['branch'] == b for r in rows)]
if missing:
    print('WARNING unmatched labels:', missing)
with open(HERE / 'recall_manual.tsv', 'w', encoding='utf-8') as fh:
    cols = list(rows[0])
    fh.write('\t'.join(cols) + '\n')
    for r in rows:
        fh.write('\t'.join(str(r[c]) for c in cols) + '\n')

lat = [r for r in rows if not r['plain']]
print(f'ayat {len(ROOTS)}, identity-root branches {len(rows)}, plain {sum(r["plain"] for r in rows)}, latent candidates {len(lat)}')
print(f'cold latent recalled {sum(r["cold"] for r in lat)} ({sum(r["cold"] for r in lat)/len(lat):.1%}); '
      f'fed latent (A-signal, lower bound) {sum(r["fed"] for r in lat)} ({sum(r["fed"] for r in lat)/len(lat):.1%}); '
      f'both {sum(1 for r in lat if r["cold"] and r["fed"])}; cold-only {sum(1 for r in lat if r["cold"] and not r["fed"])}; '
      f'fed-only {sum(1 for r in lat if r["fed"] and not r["cold"])}')


def bucket(n):
    return '0-1' if n <= 1 else '2-10' if n <= 10 else '11-100' if n <= 100 else '>100'


def table(name, keyf):
    t = defaultdict(Counter)
    for r in lat:
        k = keyf(r)
        t[k]['n'] += 1; t[k]['cold'] += r['cold']; t[k]['fed'] += r['fed']
        t[k]['fed_only'] += r['fed'] and not r['cold']
    print(f'\n{name}:  class | latent branches | cold recalled (rate) | fed quoted, lower bound (rate) | fed-only')
    for k in sorted(t, key=str):
        c = t[k]
        print(f'   {str(k):22} {c["n"]:4} | {c["cold"]:3} ({c["cold"]/c["n"]:.0%}) | {c["fed"]:3} ({c["fed"]/c["n"]:.0%}) | {c["fed_only"]}')


table('root frequency (QAC words)', lambda r: bucket(r['root_words']))
table('branch_kind', lambda r: r['kind'])
table('early sources (of 6)', lambda r: '1' if r['n_sources'] <= 1 else '2-3' if r['n_sources'] <= 3 else '4-6')
table('HFT/v12 activation history', lambda r: 'never' if r['hft_any'] + r['v12'] == 0 else
      'activated<10' if r['hft_any'] + r['v12'] < 10 else 'activated>=10')
table('position (B001-B003 vs later)', lambda r: 'B001-B003' if r['idx'] <= 3 else 'B004+')
print('\ncold latent positives by kind:', Counter(r['kind'] for r in lat if r['cold']).most_common())
print('fed-only latent (memory did not supply; lower bound):')
for r in lat:
    if r['fed'] and not r['cold']:
        print(f"   {r['ayah']:6} {r['branch']:10} {r['kind'][:5]:5} words={r['root_words']:4} src={r['n_sources']} "
              f"hft={r['hft_any']} v12={r['v12']} | {r['concept']}")
