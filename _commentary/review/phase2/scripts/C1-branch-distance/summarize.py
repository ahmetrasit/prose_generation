"""Assemble the metric x evaluation-set table from the JSON outputs (no computation of its own)."""
import json, os
H = os.path.dirname(os.path.abspath(__file__))
L = lambda f: json.load(open(os.path.join(H, f)))
t1 = L('eval_t1_new.json'); v12 = L('eval_v12.json'); na = L('na_eval3.json')['results']; g = L('gold2.json')
ALIAS = {'typed_union_v2': 'union_rrf', 'typed_union2': 'union_rrf', 'typed_union_floor': 'union_floor',
         'typed_union_v2+guard': 'union_rrf+guard', 'typed_union_floor+guard': 'union_floor+guard', 'random_exact': 'random',
         'prior_B001': 'prior_B001', 'prior_b001': 'prior_B001'}
rows = {}
def put(metric, col, val):
    m = ALIAS.get(metric, metric)
    rows.setdefault(m, {})[col] = val
for m, v in t1.items():
    put(m, 'T1_v12_pair_given_MRR_nonB001', v.get('nonB001'))
for m in ('learned_no_prior (5-fold surah CV)', 'learned_no_prior_guard (5-fold surah CV)', 'learned_with_prior (5-fold surah CV)', 'learned_slm_only (5-fold surah CV)'):
    put(m.split(' (')[0], 'T1_v12_pair_given_MRR_nonB001', v12['T1'][m]['nonB001'])
for ctx, col in (('partner_guarded', 'T6_NA_partner_guarded'), ('ayah_guarded', 'T6_NA_ayah_guarded'), ('ayah', 'T6_NA_ayah_unguarded')):
    for m, v in na[ctx].items():
        put(m, col + '_MRR_latent', v['latent_among_latent'])
        put(m, col + '_R@3_latent', round(v['latent_R@3'], 3))
for m, v in v12['T2'].items():
    if isinstance(v, float): put(m, 'T2_v12_strong_vs_reject_AUC', v)
for m, v in g['T3_S1_pairs'].items():
    put(m, 'T3_S1_pairs_le10_of_62', v['le10']); put(m, 'T3_S1_pairs_median_rank_of_~130', v['median'])
for m, v in g['T3_S1_items_with_pair_le10'].items():
    put(m, 'T3_S1_items_le10_of_26', v)
for m, v in g['T4_29_38_summary'].items():
    put(m, 'T4_2938_links_branch_MRR_of_19', v['branch_choice_MRR'])
for k, v in g['T5_eye_film'].items():
    parts = k.split()
    m, wdw = parts[0], parts[1]
    if len(parts) > 2: continue
    put(m, f'T5_eye_film_{wdw}_rank_in_8_sabil', v['rank_in_sabil'])
    put(m, f'T5_eye_film_{wdw}_rank_in_74_latent', v['rank_among_nonprimary_of_ayah'])
for m, v in g['T5_spider_29_41'].items():
    put(m, 'T5_spider_29_41_rank_among_6235_ayat', v['global_rank'])
out = dict(table=rows, notes=dict(
    T1='v12 strong findings, partner branch given, rank the co-cited branch among all branches of the other root (12,000 cases; expected RR with random tie-breaking); nonB001 targets',
    T6='v12 strong findings, only context given (partner words, or all words of the ayah); rank the cited latent branch among the root\'s non-B001 branches; guarded = construction-absent branches cannot activate and are ordered last',
    T2='AUC of strong vs reject co-cited cross-root pairs (3,000 vs 489)',
    T3='S1 gold ledger 62 cross-root anchor pairs; rank of the partner among ~130 other-root S1 branches (S1 is in-sample for slm weights)',
    T4='29:38 cold-Opus links (19), branch choice given the target word/ayah',
    T5='29:38 watch case; win0 = ayah words only, win3 = +-3 ayat', M8=g.get('T3b_M8_coalition_growth_12_steps'),
    union_min_list_size=g.get('T3_S1_union_min_effective_list_size_for_top10'), slm_at_same_size=g.get('T3_S1_slm_fused_at_union_min_size')))
json.dump(out, open(os.path.join(H, 'metric_results.json'), 'w'), ensure_ascii=False, indent=1)
cols = sorted({c for r in rows.values() for c in r})
keep = ['slm_fused', 'slm_neo', 'clause_max', 'mention_shared', 'xref', 'xref_idf', 'bridge', 'bridge_lemma', 'bridge_dir', 'scene_other', 'scene_same',
        'dict_rel', 'dict_contrast', 'union_rrf', 'union_rrf+guard', 'union_floor', 'union_floor+guard', 'union_min', 'learned_no_prior', 'learned_no_prior_guard',
        'learned_with_prior', 'learned_slm_only', 'prior_B001', 'random']
for c in cols:
    print(c)
    print('   ' + '  '.join(f"{m}={rows[m][c]}" for m in keep if m in rows and c in rows[m]))
