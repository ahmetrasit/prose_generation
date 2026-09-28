"""What the construction-scope guard would remove or flag: (1) v12 reader activations, (2) v15 scene-index memberships
and window links, (3) slm-selected branch pairs for context-linked words, (4) gold items (S1 ledger, 29:38 links)."""
import csv, glob, collections, json, sys, itertools, random
sys.dont_write_bytecode = True
import common as C, guard as G
W = {w['ref']: w for w in C.WORDS}
out = {}

# ---- (1) v12 reader activations
V = f'{C.P}/latent_activation/_status/v12_cross_run'
cnt = collections.defaultdict(collections.Counter); ex = collections.defaultdict(list)
for f in glob.glob(f'{V}/s[0-9][0-9][0-9]/derived/finding_word_branches.v3.tsv'):
    for r in csv.DictReader(open(f, encoding='utf-8'), delimiter='\t'):
        i = C.GI.get((r['root_id'], r['branch_id'])); w = W.get(r['qac_word_ref'])
        if i is None or w is None: continue
        k = C.kind_of(i)
        if k != 'collocation':
            cnt[r['grade']]['non-collocation'] += 1; continue
        st, det = G.status(i, w)
        cnt[r['grade']][st] += 1
        if st == 'absent' and len(ex[r['grade']]) < 400: ex[r['grade']].append((r['qac_word_ref'], C.DISP[i], C.TEXT[i][0], det))
out['v12_activations'] = {g: dict(v) for g, v in cnt.items()}
print('v12 anchored activations by grade and guard status:')
for g, v in cnt.items():
    tot = sum(v.values()); col = tot - v['non-collocation']
    print(f"  {g}: total {tot}, collocation-branch {col} ({col/tot:.1%}); of these absent {v['absent']} ({v['absent']/max(1,col):.1%}), strict {v['present_strict']}, window {v['present_window']}, prep-only {v['possible_prep_only']}, unknown {v['unknown']}")
random.seed(3)
print('  examples (strong, construction absent):')
for e in random.sample(ex['strong'], 12): print('   ', e)
db = [e for g in ex for e in ex[g] if e[1].startswith('ض ر ب B002')]
print('  ض ر ب B002 activations with construction absent:', db[:10])

# ---- (2) v15 scene index
mem = collections.Counter(); only_absent = 0; tot_ws = 0
link_tot = 0; link_removed = 0
scene_ws = {}
for (s, a), ws in C.BY_AYAH.items():
    for w in ws:
        by_scene = collections.defaultdict(set)
        for r in w['roots']:
            for i in C.BY_ROOT.get(r, []):
                st = G.status(i, w)[0]
                for fr, role in C.TAGS.get(i, ()):
                    by_scene[fr].add(st)
        for fr, sts in by_scene.items():
            tot_ws += 1
            ok = sts - {'absent'}
            if not ok: only_absent += 1
            scene_ws[(w['ref'], fr)] = bool(ok)
print(f'v15 scene index: word-scene memberships {tot_ws}; supported only by collocation branches whose construction is absent: {only_absent} ({only_absent/tot_ws:.2%})')
out['v15_scene_memberships'] = dict(total=tot_ws, only_absent_collocation=only_absent)
# window links: pairs of words within +-3 ayat sharing a scene (as v15 scene lines do), sampled over all surahs
random.seed(5)
refs_by_s = collections.defaultdict(list)
for w in C.WORDS: refs_by_s[w['s']].append(w)
sc_by_word = collections.defaultdict(dict)
for (ref, fr), ok in scene_ws.items(): sc_by_word[ref][fr] = ok
samp_ayat = random.sample(sorted(C.BY_AYAH), 600)
for (s, a) in samp_ayat:
    focus = C.BY_AYAH[(s, a)]
    others = [w for (s2, a2) in C.window(s, a, 3) for w in C.BY_AYAH[(s2, a2)]]
    for x in focus:
        for y in others:
            if y['ref'] == x['ref'] or set(x['roots']) & set(y['roots']): continue
            shared = set(sc_by_word[x['ref']]) & set(sc_by_word[y['ref']])
            for fr in shared:
                link_tot += 1
                if not (sc_by_word[x['ref']][fr] and sc_by_word[y['ref']][fr]): link_removed += 1
print(f'v15-style scene links (600 random focus ayat, window +-3, word pairs sharing a scene): {link_tot}; removed by the guard {link_removed} ({link_removed/max(1,link_tot):.2%})')
out['v15_scene_links_sample'] = dict(focus_ayat=600, links=link_tot, removed=link_removed)
# ḍaraba B002 travel partners at 4:34
w434 = W['4:34:29']
b002 = [i for i in C.BY_ROOT['ض ر ب'] if C.BID[i] == 'B002'][0]
trav = {fr for fr, role in C.TAGS.get(b002, ())}
print('ض ر ب B002 scenes:', sorted(C.TAGS.get(b002, ())), '; status at 4:34:', G.status(b002, w434))
part = []
for (s2, a2) in C.window(4, 34, 3):
    for y in C.BY_AYAH[(s2, a2)]:
        sh = set(sc_by_word[y['ref']]) & trav
        if sh and y['ref'] != '4:34:29': part.append((y['ref'], y['surface'], sorted(sh)))
print('  scene partners of ḍaraba at 4:34 (+-3 ayat) that exist only through B002:', len(part), part[:8])
b1 = {fr for i in C.BY_ROOT['ض ر ب'] if C.kind_of(i) != 'collocation' for fr, _ in C.TAGS.get(i, ())}
only_b002 = [p for p in part if not set(p[2]) & b1]
print('  of which not also reachable through a non-collocation branch of ḍaraba:', len(only_b002))
out['daraba_434'] = dict(partners=len(part), only_via_B002=len(only_b002), examples=only_b002[:10])

# ---- (3) slm branch choice for context-linked word pairs in the same ayah
random.seed(9)
sel_tot = sel_guard = 0
for (s, a) in random.sample(sorted(C.BY_AYAH), 400):
    ws = [w for w in C.BY_AYAH[(s, a)] if w['roots']]
    for x, y in itertools.combinations(ws, 2):
        if x['roots'][0] == y['roots'][0]: continue
        bx = C.BY_ROOT.get(x['roots'][0], []); by = C.BY_ROOT.get(y['roots'][0], [])
        if not bx or not by: continue
        best = max(((C.s_fused(i, j), i, j) for i in bx for j in by))
        sel_tot += 1
        _, i, j = best
        if G.status(i, x)[0] == 'absent' or G.status(j, y)[0] == 'absent': sel_guard += 1
print(f'slm top-1 branch pair for same-ayah word pairs (400 random ayat): {sel_tot}; involving a collocation branch whose construction is absent: {sel_guard} ({sel_guard/max(1,sel_tot):.1%})')
out['slm_top1_pairs_sample'] = dict(pairs=sel_tot, guarded=sel_guard)

# ---- (4) gold tension
print('\nGold items that use a collocation-bound branch:')
g29 = [("ع و د", "B009", '29:38:1'), ("ع م ل", "B011", '29:38:11'), ("ص د د", "B004", '29:38:12'), ("ص د د", "B013", '29:38:12'), ("س ب ل", "B010", '29:38:14'),
       ("ب ي ن", "B007", '29:38:4'), ("ع م ل", "B010", '29:38:11'), ("ز ي ن", "B001", '29:38:8'), ("ش ط ن", "B005", '29:38:10'), ("ش ط ن", "B003", '29:38:10'),
       ("س ب ل", "B010", '29:38:14'), ("س ك ن", "B004", '29:38:7'), ("ص د د", "B005", '29:38:12'), ("ص د د", "B002", '29:38:12'), ("س ب ل", "B005", '29:38:14'),
       ("ش ط ن", "B001", '29:38:10'), ("ز ي ن", "B001", '29:38:8'), ("ع م ل", "B012", '29:38:11'), ("س ب ل", "B010", '29:38:14')]
blocked29 = []
for r, b, ref in g29:
    i = [j for j in C.BY_ROOT[r] if C.BID[j] == b][0]
    st = G.status(i, W[ref])[0]
    if st == 'absent': blocked29.append((r, b, C.TEXT[i][0]))
print('  29:38 cold-Opus links (19):', len(blocked29), 'use a collocation branch whose construction is absent:', blocked29)
s1words = [w for w in C.WORDS if w['s'] == 1]
blockedS1 = []
seen = set()
for l in open(f'{C.SLM}/reports/s1_ar3_v1_gold_ledger.jsonl'):
    g = json.loads(l)
    if not g['eligibility']['eligible']: continue
    for n in g['required_branch_anchors'] + [x for grp in g['required_branch_anchor_groups'] for x in grp['node_ids']]:
        i = C.NODE.get(n)
        if i is None or C.kind_of(i) != 'collocation' or (g['gold_id'], n) in seen: continue
        seen.add((g['gold_id'], n))
        sts = [G.status(i, w)[0] for w in s1words if C.ROOTKEY[i] in w['roots']]
        blockedS1.append((g['gold_id'], C.DISP[i], C.TEXT[i][0], collections.Counter(sts).most_common()))
print('  S1 gold (26 eligible items): collocation anchors and their status at every Fatiha occurrence of the root:')
for b in blockedS1: print('   ', b)
out['gold_blocked'] = dict(s29=blocked29, s1=[list(map(str, b)) for b in blockedS1])
json.dump(out, open(C.HERE + '/guard_impact.json', 'w'), ensure_ascii=False, indent=1)
