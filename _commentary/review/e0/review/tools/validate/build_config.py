"""Assemble recommended_links.json (the supply builder's config) and results_table.tsv from the measured result files.
Rules and thresholds are frozen here; every number is copied from results_hft.json, selection.json, sizes.json,
robust_pos.json, results_29_38.json. Nothing is recomputed."""
import json, os, math
import lib

H = lib.HERE
R = json.load(open(os.path.join(H, 'results_hft.json')))
S = json.load(open(os.path.join(H, 'selection.json')))
Z = json.load(open(os.path.join(H, 'sizes.json')))
P = json.load(open(os.path.join(H, 'robust_pos.json')))
G = json.load(open(os.path.join(H, 'results_29_38.json')))
import links


def r2(x):
    if x is None:
        return None
    if isinstance(x, (list, tuple)):
        return [r2(v) for v in x]
    if isinstance(x, float):
        if math.isinf(x):
            return 'inf'
        if math.isnan(x):
            return None
        return round(x, 3)
    return x


def ev(nm):
    f, d, t, v = R['full'][nm], R['dev'][nm], R['test'][nm], R['volume'][nm]
    out = dict(variant=nm, coverage_of_true_pairs=r2(f['coverage']),
               lift_vs_freq_matched_word=r2(f['lift_af']), ci95_ayah=r2(f['lift_af_ci_ayah']), ci95_surah=r2(f['lift_af_ci_surah']),
               lift_vs_other_branch_same_root=r2(f.get('lift_b')), ci95_branch=r2(f.get('lift_b_ci_ayah')),
               dev_odd_surahs=dict(lift=r2(d['lift_af']), ci95=r2(d['lift_af_ci_ayah'])),
               test_even_surahs=dict(lift=r2(t['lift_af']), ci95=r2(t['lift_af_ci_ayah']), lift_branch=r2(t.get('lift_b')),
                                     ci95_branch=r2(t.get('lift_b_ci_ayah'))),
               units_per_ayah_hft_sample=dict(mean=r2(v['paths_per_ayah_mean']), p90=r2(v['paths_per_ayah_p90']),
                                              max=r2(v['paths_per_ayah_max'])),
               share_through_frequent_root_or_lemma=r2(v['share_frequent_element']))
    if nm in P['types']:
        out['lift_vs_pos_and_freq_matched_word'] = r2(P['types'][nm]['lift_pos_bin'])
        out['ci95_pos_matched'] = r2(P['types'][nm]['ci_ayah'])
    if nm in G['per_type']:
        g = G['per_type'][nm]
        out['in_sample_29_38'] = f"{g['hits']}/{g['of']} gold links (expected {g['expected_base_a']} for other words, {g['expected_base_b']} for other branches)"
    if nm in Z['types']:
        z = Z['types'][nm]
        out['calibrated_tokens_per_ayah_whole_quran_sample'] = dict(mean=r2(z['tokens_mean']), p90=r2(z['tokens_p90']),
                                                                    max=r2(z['tokens_max']), at_2_282=r2(z['tokens_2_282']))
    return out


cfg = {
    'schema': 'e0.validate.recommended_links.v1',
    'frozen': '2026-09-28',
    'status': ('recommendation from free local scripts; thresholds are frozen (a change needs a re-run of eval_hft.py and '
               'select_links.py); what is pushed versus pulled is the user\'s decision (push limits are not decided)'),
    'question': ('does a path of this type connect a neighbour-activated dictionary branch to the word that activated it, '
                 'more often than it connects the same branch to another word of the ayah (matched on frequency, and on '
                 'part of speech), and more often than another branch of the same root to the same word?'),
    'evaluation_set': dict(R['meta'], source='HFT surprising_valid_outliers (Sol, max effort) whose first trace step activates a '
                           'non-B001 branch of a focus word and whose trace cites another root of the same ayah; named surahs '
                           'excluded (K-northstar-critic/hft_na_set.py)', split='dev = odd surahs, test = even surahs',
                           ci='percentile bootstrap, 2,000 resamples, clustered by ayah (and by surah)'),
    'selection_rule': S['rule'],
    'label_caveats': [
        'HFT labels come from Sol readers and share their biases: they are surprise-seeking, canonical-leaning in what they accept '
        'as valid, and 13% of the target branches are collocation-bound (construction drift in the labels themselves).',
        'The HFT readers saw each focus branch\'s image and definition (what_is) and the images of the neighbour roots\' branches, '
        'but not the early source phrases, the dictionary neighbour relations, Qnet keywords or co-citations. Types built from the '
        'visible card text (definitional pointer, quran-slm card similarity, Qnet keywords generated from the same card prose) share '
        'the labeller\'s input and are likely inflated; the pointer restricted to the unseen early phrases has a lower lift '
        '(%.2f, 95%% CI %s) than the pointer in the seen fields (%.2f).' % (R['full']['ptr_phrase_only']['lift_af'],
                                                                             r2(R['full']['ptr_phrase_only']['lift_af_ci_ayah']),
                                                                             R['full']['ptr_imgwhat']['lift_af']),
        'Only within-ayah neighbour activation of non-B001 branches is tested. Cross-ayah links (window, surah, parallels such as '
        'formula echoes) and plain-sense activation are untested here; the 29:38 check is in-sample and never tuned anything.',
        'Activators are rarer content words than the average word of an ayah (median 74 vs 177 ayat), so the unmatched base rate '
        'is biased; all decisions use the frequency-matched base, and a POS+frequency matched base gives the same conclusions.',
        'Even the whole recommended set reaches only %.0f%% of HFT activator pairs; most neighbour activations have no script path.'
        % (100 * S['included']['union']['coverage_pairs'],),
    ],
    'display_rules': [
        'Descriptive lines only: no score, rank, PMI value, similarity value, confidence, count used for sorting, or any verdict '
        '(present/absent, strong/weak) in anything a model reads.',
        'Lines sit under their branch; branches in dictionary order; partner words in ayah word order; witness ayat in Quran order.',
        'Every branch line keeps its branch_kind scope note (the construction guard applies to link lines as to branch lines).',
        'No numeric limit on the number of lines of an included type (no caps); sizes are reported, not trimmed.',
        'Nothing named in the North Star or the watch cases may appear in a template or an example.',
    ],
    'push': [
        dict(id='definitional_pointer', family='definitional pointer',
             rule=dict(source='dictionary tr entry of the branch: branch_image_ar, what_is_ar, source_phrase_ar (source tags removed); '
                              'what_is_not_ar is never used',
                       normalize='strip diacritics and tatweel; أإآٱ→ا, ى→ي, ة→ه, ؤ→و, ئ→ي',
                       match='whole word: a token equals a QAC lemma (article removed) or a single-root surface form; the least-stripped '
                             'spelling wins (token; minus pronoun suffix ها هم هن كم نا ه ك; minus prefix وال فال بال كال لل ال و ف ب ل ك '
                             'with at least 3 letters left; both)',
                       skip='function words (lib.STOP_TOK) and و/ف + function word; the branch\'s own root; ء ل ه',
                       threshold='the named root is named in the texts of at most 400 of the dictionary\'s 11,773 branches (card df over the '
                                 'same three fields)',
                       direction='from every branch of every root in the ayah to every other word of the ayah whose root it names '
                                 '(validated); to window or surah words: allowed, not validated here',
                       implementation='links._ptr(T, r, cardcap=400); lib.NAMES; lib.CARD_DF'),
             display_template='{root} {Bnn} names «{token as written}» ({field}) → {surface} ({partner root}, w{n})',
             evidence=ev('ptr_card400'),
             note='The HFT-unseen early-phrase part alone is weaker and uncertain (see label_caveats). Chosen over the ayah-frequency '
                  'cap (ptr_df300, test lift %.2f) by the dev-half rule.' % R['test']['ptr_df300']['lift_af']),
        dict(id='dictionary_neighbour_relation', family='dictionary neighbour relation (typed), including antonym/polarity',
             rule=dict(source='neighbor_distinctions of both branches (symmetric)', relation_types='all: near_synonym, synonym, '
                       'near_neighbor, same_field, thematic, other, polarity_pair, antonym', implementation='links._nb(T, r)'),
             display_template='{root} {Bnn} «{image}» / {partner root} {Bmm} «{image}»: {relation_type} [optionally the dictionary\'s '
                              'own distinction sentence]',
             evidence=ev('nb_any'),
             antonym_polarity=dict(true_paths=r2(R['full']['nb_contrast']['true_paths']),
                                   expected_freq_matched=r2(R['full']['nb_contrast']['expected_af']),
                                   lift_vs_global_freq_matched=r2(R['full']['nb_contrast']['lift_g']),
                                   ci95=r2(R['full']['nb_contrast']['lift_g_ci_ayah']),
                                   note='too few cases to test alone (5 true paths); kept as a labelled subtype of the relation, '
                                        'never as a separate claim. Contrasts in general remain unsolved by script.'),
             note='Independent of what the HFT readers saw; the highest lift of all types, tiny volume.'),
        dict(id='root_cooccurrence', family='root co-occurrence (PMI over ayat)',
             rule=dict(unit='ayah; root sets from QAC words', exclude='the current ayah is removed from all counts',
                       threshold='c >= 2 other ayat contain both roots and ln(c*(N-1)/(nA*nB)) > 2.0 (nA, nB: other ayat with each root; '
                                 'N = 6,236)', implementation='links._cooc(T, r, X, "ayah", 2.0)'),
             display_template='{root} + {partner root} also meet in {every witness ayah, Quran order}',
             evidence=ev('cooc_ayah_pmi2'),
             note='Root-level: it cannot tell branches of one root apart. The ±3-ayah window variant (lift %.2f) was not chosen by the rule.'
                  % R['full']['cooc_win3_pmi1']['lift_af']),
    ],
    'pull_only_proposal': [
        dict(id='image_pair', family='quran-slm card similarity OR shared rare core Qnet keyword',
             rule=dict(slm='fused RRF (0.35 E5 + 0.35 NeoAraBERT + 0.30 character, symmetric) of the target branch with the best branch '
                           'of the partner root >= the 99th percentile of 20,000 random cross-root card pairs (%.5f)' % links.SLM_P99,
                       qnet='a shared core keyword whose keyword appears on at most 50 branches (Qnet v2 branch_keywords.tsv)',
                       implementation='links._slm_floor(T, r, 99) or links._qnet_ov(T, r, maxdf=50, core=True)'),
             display_template='{root} {Bnn} «{image}» ~ {partner root} {Bmm} «{image}»  (both dictionary images; no score, no keyword)',
             evidence=dict(merged=dict(coverage_of_true_pairs=r2(Z['imgpair_hft']['coverage']), lift_vs_freq_matched_word=r2(Z['imgpair_hft']['lift_af']),
                                       ci95_ayah=r2(Z['imgpair_hft']['ci']), lift_vs_other_branch_same_root=r2(Z['imgpair_hft']['lift_b']),
                                       ci95_branch=r2(Z['imgpair_hft']['ci_b']),
                                       calibrated_tokens_per_ayah_whole_quran_sample=dict(mean=r2(Z['types']['imgpair']['tokens_mean']),
                                                                                          p90=r2(Z['types']['imgpair']['tokens_p90']),
                                                                                          max=r2(Z['types']['imgpair']['tokens_max']),
                                                                                          at_2_282=r2(Z['types']['imgpair']['tokens_2_282']))),
                           slm_p99=ev('slm_p99'), qnet_core_df50=ev('qnet_core_df50')),
             why_not_pushed=['It passes the signal test (branch-discriminating too), but its volume is large and unbounded: mean %.0f lines and '
                             '%.0f calibrated tokens per ayah, %.0f tokens at 2:282; pushing it needs a push limit, which is undecided.'
                             % (Z['types']['imgpair']['lines_mean'], Z['types']['imgpair']['tokens_mean'], Z['types']['imgpair']['tokens_2_282']),
                             'It is unexplained similarity (no typed path in words); Phase 2 kept quran-slm pair lists out of the prompt.',
                             'Qnet keywords are English atoms a model produced from memory from the branch prose, not dictionary text: they may '
                             'serve as an index, never as evidence or as displayed wording.',
                             'Both quran-slm and Qnet read the same card text the HFT readers saw, so their lift is the most exposed to label bias.',
                             'Correction of scope: Phase 2 found quran-slm at chance for ORDERING a word\'s branches; as top-1% path existence '
                             'it is well above chance on the same HFT set.']),
    ],
    'per_ayah_layer_proposal': [
        dict(id='early_citations', family='early-source co-citation',
             rule=dict(source='six early entries only (dictionary/data/output/root_packets entry_text_clean); explicit refs (Mufradat '
                              '[surah/ n], Tahdhib ( surah : n )) and quoted runs of >= 3 words matching at most 2 ayat by consonant skeleton; '
                              'kept only when the cited ayah contains a word of the entry\'s root',
                       show='the early passage verbatim around the citation, with its source; no branch attribution',
                       implementation='cocite.py (cache/cocite.pkl), links.CC_ROOT / CC_QROOT'),
             index=json.load(open(os.path.join(H, 'cocite_stats.json'))),
             evidence=dict(quoted_words_link=ev('cc_quote_root'),
                           filed_under_target_branch=dict(lift_vs_other_branch_same_root=r2(R['full']['cc_here_branch']['lift_b']),
                                                          ci95=r2(R['full']['cc_here_branch']['lift_b_ci_ayah']),
                                                          note='early sources do not file the surprise branches\' ayat under them '
                                                               'more than under other branches: co-citation is a canonical signal')),
             attribution_check=json.load(open(os.path.join(H, 'cocite_attribution_check.json')))['estimate'],
             note='The "quoted words" link passes the rule weakly (construction adjacency in the lexicographer\'s quote); it is delivered '
                  'by showing the passage, not as a separate line. Its value as evidence for the plain sense and for the construction '
                  'guard is untested here.'),
    ],
    'exclude': [
        dict(id='rare_lemma_bridge', variants=['bridge30', 'bridge100', 'bridge30_sig2', 'bridge100_sig2', 'bridge30_rev'],
             why='at or below chance: lift %.2f-%.2f against the frequency-matched word, flood volume (%.0f-%.0f units per ayah); '
                 'a rare lemma meets almost any root somewhere' % (min(R['full'][v]['lift_af'] for v in ['bridge30', 'bridge100', 'bridge30_sig2', 'bridge100_sig2']),
                                                                  max(R['full'][v]['lift_af'] for v in ['bridge30', 'bridge100', 'bridge30_sig2', 'bridge100_sig2']),
                                                                  min(R['volume'][v]['paths_per_ayah_mean'] for v in ['bridge30_sig2', 'bridge100_sig2']),
                                                                  max(R['volume'][v]['paths_per_ayah_mean'] for v in ['bridge30', 'bridge100'])),
             evidence={v: ev(v) for v in ['bridge30', 'bridge100_sig2']}),
        dict(id='formula_cooccurrence', variants=['formula_k3', 'formula_k5', 'formula_k10', 'formula_k5_pmi'],
             why='no activation signal: test lift %.2f %s for the best variant; untested as a cross-ayah parallel pointer (a different job)'
                 % (R['test']['formula_k5_pmi']['lift_af'], r2(R['test']['formula_k5_pmi']['lift_af_ci_ayah'])),
             evidence={v: ev(v) for v in ['formula_k5', 'formula_k5_pmi']}),
        dict(id='pointer_without_generic_threshold', variants=['ptr', 'ptr_df1000'],
             why='%.0f%% of its paths go through roots found in more than 300 ayat (يدخل in "يدخل فيه", كان ...); lower lift'
                 % (100 * R['volume']['ptr']['share_frequent_element']), evidence={'ptr': ev('ptr')}),
        dict(id='weak_or_flooding_similarity', variants=['slm_pair10', 'slm_pair3', 'slm_p95', 'qnet_any', 'qnet_df200', 'qnet_core'],
             why='lift 1.1-2.1 with 60-260 units per ayah', evidence={v: ev(v) for v in ['slm_pair10', 'qnet_any']}),
        dict(id='cooccurrence_low_threshold', variants=['cooc_ayah_pmi0', 'cooc_win3_pmi0', 'cooc_ayah_pmi1', 'cooc_win3_pmi2'],
             why='PMI > 0 is at chance; lower thresholds only add volume', evidence={'cooc_ayah_pmi0': ev('cooc_ayah_pmi0')}),
        dict(id='cocitation_as_branch_link', variants=['cc_here_branch', 'cc_quote_branch', 'cc_else_branch', 'cc_else_root'],
             why='no branch-level signal (branch attribution is also only about 65% correct); "cited elsewhere with the partner" is at or below chance',
             evidence={v: ev(v) for v in ['cc_quote_branch', 'cc_else_root']}),
    ],
    'diagnostics': {
        'pointer_seen_fields_image_what': ev('ptr_imgwhat'),
        'pointer_unseen_early_phrase_only': ev('ptr_phrase_only'),
        'pointer_reverse_direction': dict(ev('ptr_rev'), note='the same type seen from the partner\'s branch; covered by running the '
                                                               'pointer over every branch'),
    },
    'recommended_push_size': dict(types=Z['push_core_total']['types'],
                                  calibrated_tokens_per_ayah=dict(mean=r2(Z['push_core_total']['tokens_mean']),
                                                                  p90=r2(Z['push_core_total']['tokens_p90']),
                                                                  at_2_282=r2(Z['push_core_total']['tokens_2_282'])),
                                  note='increments only (the 4,581-token per-call constant is not included)'),
    'recommended_set_on_hft': dict(union_of=S['included']['union']['types'], coverage_of_true_pairs=r2(S['included']['union']['coverage_pairs']),
                                   lift_vs_freq_matched_word=r2(S['included']['union']['lift_af']), ci95=r2(S['included']['union']['ci']),
                                   lift_vs_other_branch=r2(S['included']['union']['lift_b']), ci95_branch=r2(S['included']['union']['ci_b']),
                                   by_branch_kind={k: dict(pairs=v['pairs'], lift=r2(v['lift_af']), ci95=r2(v['ci'])) for k, v in S['included']['by_branch_kind'].items()}),
    'push_set_on_hft': {k: dict(types=Z[k]['types'], coverage_of_true_pairs=r2(Z[k]['coverage']), lift_vs_freq_matched_word=r2(Z[k]['lift_af']),
                                ci95=r2(Z[k]['ci']), lift_vs_other_branch=r2(Z[k]['lift_b']), ci95_branch=r2(Z[k]['ci_b']))
                        for k in ('push_core_hft', 'push_core_plus_imgpair_hft')},
    'in_sample_29_38': Z['in_sample_29_38'],
    'code': dict(dir=H, run_order=['cocite.py', 'eval_hft.py', 'select_links.py', 'robust_pos.py', 'sizes.py', 'eval_29_38.py', 'build_config.py'],
                 library='lib.py (loaders), links.py (type definitions)'),
}
json.dump(cfg, open(os.path.join(H, 'recommended_links.json'), 'w'), ensure_ascii=False, indent=1)

# compact results table
cols = ['type', 'family', 'scope', 'decision', 'coverage', 'lift_a_unmatched', 'lift_freq_matched', 'ci95_ayah', 'ci95_surah',
        'lift_pos_freq_matched', 'lift_other_branch', 'ci95_branch', 'test_half_lift', 'test_half_ci', 'test_half_branch_lift',
        'units_per_ayah', 'units_p90', 'share_frequent_element']
chosen = {v.get('chosen'): v.get('decision') for v in S['families'].values() if v.get('chosen')}
role = {'ptr_card400': 'PUSH', 'nb_any': 'PUSH', 'cooc_ayah_pmi2': 'PUSH', 'slm_p99': 'PULL (image pair)',
        'qnet_core_df50': 'PULL (image pair)', 'cc_quote_root': 'LAYER (early citations)', 'nb_contrast': 'PUSH (subtype of relation)'}
diag = {'ptr_imgwhat', 'ptr_imgwhat_df300', 'ptr_phrase', 'ptr_phrase_only', 'ptr_phrase_only_df300', 'ptr_rev', 'ptr_rev_df300', 'cc_here_branch', 'cc_here_root'}


def fm(x, d=2):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return ''
    if isinstance(x, float) and math.isinf(x):
        return 'inf'
    return f'{x:.{d}f}'


def fci(t):
    return '' if not t else f'[{fm(t[0])},{fm(t[1])}]'


rows = ['\t'.join(cols)]
for nm, (fam, scope, _) in links.TYPES.items():
    f, t, v = R['full'][nm], R['test'][nm], R['volume'][nm]
    fam_of = next((k for k, vs in __import__('select_links').FAMILIES.items() if nm in vs), None)
    fam_dec = S['families'].get(fam_of, {}).get('decision') if fam_of else None
    if nm in role:
        dec = role[nm]
    elif nm in diag:
        dec = 'diagnostic'
    elif fam_dec == 'exclude':
        dec = 'exclude'
    elif fam_of == 'dictionary_neighbour':
        dec = 'PUSH (subtype of relation)'
    else:
        dec = 'not chosen (weaker variant)' 
    pos = P['types'].get(nm, {}).get('lift_pos_bin')
    rows.append('\t'.join([nm, fam, scope, dec, fm(f['coverage'], 3), fm(f['lift_a']), fm(f['lift_af']), fci(f['lift_af_ci_ayah']),
                           fci(f['lift_af_ci_surah']), fm(pos), fm(f.get('lift_b')), fci(f.get('lift_b_ci_ayah')), fm(t['lift_af']),
                           fci(t['lift_af_ci_ayah']), fm(t.get('lift_b')), fm(v['paths_per_ayah_mean'], 1), fm(v['paths_per_ayah_p90'], 0),
                           fm(v['share_frequent_element'])]))
open(os.path.join(H, 'results_table.tsv'), 'w').write('\n'.join(rows) + '\n')
print('\n'.join(rows))
