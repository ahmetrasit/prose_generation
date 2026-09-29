"""Evaluate the form-aware detector against root-dossier placements (E0).

Labels: root-dossier/out/activation_map.tsv rows with role 'dominant' whose branch is collocation-bound
(branch_kind 'collocation'): the dossier says the plain reading of that occurrence realises the branch, so its
construction should be present. These are Luna group labels (one branch per group), noisy by construction.
Negatives for false activation: at the same dossier occurrences, every OTHER collocation branch of the root.

Sets:  all (41 branches, 696 placements, as Phase 2 'all');  excl_gram (the two grammatical constructions
       نفس B012 and دون B003 removed: the 397 set behind the Phase 2 miss rates A 66%, B 79%, C2 67%);
       main = excl_gram minus the noisy ء ت ي B011 group (364);  dev / test = a seeded split of the main set's
       branches (split.json; rules were written looking at dev only).
Usage: python3 eval_dossier.py [--rows]   (writes eval_dossier.json, eval_rows.tsv)
"""
import sys, json, collections, csv, os
sys.dont_write_bytecode = True
import gdata as G
import detector as Dt

HERE = os.path.dirname(os.path.abspath(__file__))
SPLIT = json.load(open(os.path.join(HERE, 'split.json')))
GRAM = set(SPLIT['excluded_grammatical'])
NOISY = set(SPLIT['excluded_noisy'])
DEV, TEST = set(SPLIT['dev']), set(SPLIT['test'])


def labels():
    B = G.dictionary()['branches']
    pos, seen, occ_rows = [], set(), {}
    for r in G.dossier_rows():
        if r['role'] != 'dominant' or not r['branch_ref'].startswith('root_') or r['branch_ref'] not in B:
            continue
        rid = r['branch_ref'].split('/')[0]
        occ = r['qac_word_ref']
        occ_rows.setdefault((occ, rid), r['branch_ref'])
        if B[r['branch_ref']]['kind'] != 'collocation':
            continue
        k = (occ, r['branch_ref'])
        if k in seen:
            continue
        seen.add(k)
        pos.append(k)
    return pos, occ_rows


def subset(ref, name):
    if name == 'all':
        return True
    if name == 'excl_gram':
        return ref not in GRAM
    if name == 'main':
        return ref not in GRAM and ref not in NOISY
    if name == 'dev':
        return ref in DEV
    if name == 'test':
        return ref in TEST
    raise ValueError(name)


def run(policy='default', names=('all', 'excl_gram', 'main', 'dev', 'test')):
    B = G.dictionary()['branches']
    pos, occ_rows = labels()
    calls = {}

    def call(occ, rid):
        if (occ, rid) not in calls:
            calls[(occ, rid)] = Dt.decide(occ, rid, policy) if occ in G.words() else {}
        return calls[(occ, rid)]

    rows = []
    for occ, ref in pos:
        rid = ref.split('/')[0]
        c = call(occ, rid).get(ref, ('missing', 0, 'occurrence not in QAC', ''))
        rows.append(dict(kind='true', occ=occ, branch=ref, call=c[0], level=c[1], why=c[2], cons=c[3]))
    for (occ, rid), placed in occ_rows.items():
        cs = call(occ, rid)
        for ref, c in cs.items():
            if B[ref]['kind'] != 'collocation' or ref == placed:
                continue
            rows.append(dict(kind='other', occ=occ, branch=ref, placed=placed, call=c[0], level=c[1], why=c[2],
                             cons=c[3]))
    out = {}
    for name in names:
        T = [r for r in rows if r['kind'] == 'true' and subset(r['branch'], name)]
        if name in ('dev', 'test'):
            O = [r for r in rows if r['kind'] == 'other' and subset(r['placed'], name)]
        else:
            O = [r for r in rows if r['kind'] == 'other' and (subset(r['placed'], name) if B[r['placed']]['kind'] ==
                                                              'collocation' else True)]
        ct = collections.Counter(r['call'] for r in T)
        co = collections.Counter(r['call'] for r in O)
        nt, no = len(T), len(O)
        per = collections.defaultdict(collections.Counter)
        for r in T:
            per[r['branch']][r['call']] += 1
        shares = [v['present'] / sum(v.values()) for v in per.values()]
        out[name] = dict(
            true_placements=nt, branches=len(per),
            recall_present=round(ct['present'] / nt, 3) if nt else None,
            false_absent=round(ct['absent'] / nt, 3) if nt else None,
            unknown=round(ct['unknown'] / nt, 3) if nt else None,
            missed_not_present=round((nt - ct['present']) / nt, 3) if nt else None,
            macro_recall_by_branch=round(sum(shares) / len(shares), 3) if shares else None,
            branches_all_missed=sum(1 for s in shares if s == 0),
            other_branch_occurrences=no,
            false_activation_present=round(co['present'] / no, 4) if no else None,
            # precision of 'present' at the dossier's own placements: present calls for the placed branch against
            # present calls for another guarded branch of the same root at those placements. An upper bound for the
            # whole file: present calls away from dossier placements are not in it (the audit sheet's Part C is).
            present_calls_true=ct['present'], present_calls_other_branch=co['present'],
            present_precision_at_placements=round(ct['present'] / (ct['present'] + co['present']), 3)
            if (ct['present'] + co['present']) else None,
            other_unknown=round(co['unknown'] / no, 4) if no else None,
            reasons_true=dict(collections.Counter(r['why'].split(';')[0] for r in T if r['call'] == 'present')),
            reasons_other_present=dict(collections.Counter(r['why'].split(';')[0] for r in O if r['call'] == 'present')),
        )
    return out, rows


if __name__ == '__main__':
    policy = 'default'
    for a in sys.argv[1:]:
        if a.startswith('--policy='):
            policy = a.split('=', 1)[1]
    res, rows = run(policy)
    print(json.dumps(res, ensure_ascii=False, indent=1))
    json.dump(dict(policy=policy, results=res), open(os.path.join(HERE, f'eval_dossier{"" if policy == "default" else "_" + policy}.json'), 'w'),
              ensure_ascii=False, indent=1)
    with open(os.path.join(HERE, 'eval_rows.tsv'), 'w', encoding='utf-8') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(['kind', 'occ', 'branch', 'placed', 'call', 'level', 'why', 'construction'])
        for r in rows:
            w.writerow([r['kind'], r['occ'], r['branch'], r.get('placed', ''), r['call'], r['level'], r['why'],
                        r['cons']])


def run_non_bare(policy='default'):
    """Secondary held-out check (never inspected while writing rules): dossier placements whose plain branch is
    non_bare (form-bound). The detector should find the named form / formula present there."""
    B = G.dictionary()['branches']
    seen, T = set(), []
    for r in G.dossier_rows():
        if r['role'] != 'dominant' or r['branch_ref'] not in B or B[r['branch_ref']]['kind'] != 'non_bare':
            continue
        k = (r['qac_word_ref'], r['branch_ref'])
        if k in seen or r['qac_word_ref'] not in G.words():
            continue
        seen.add(k)
        c = Dt.decide(r['qac_word_ref'], r['branch_ref'].split('/')[0], policy).get(r['branch_ref'])
        T.append((r['branch_ref'], c[0] if c else 'missing', c[2] if c else ''))
    ct = collections.Counter(x[1] for x in T)
    per = collections.defaultdict(collections.Counter)
    for b, call, _ in T:
        per[b][call] += 1
    shares = [v['present'] / sum(v.values()) for v in per.values()]
    return dict(true_placements=len(T), branches=len(per), calls=dict(ct),
                recall_present=round(ct['present'] / len(T), 3) if T else None,
                macro_recall_by_branch=round(sum(shares) / len(shares), 3) if shares else None,
                top_branches={b: dict(v) for b, v in sorted(per.items(), key=lambda x: -sum(x[1].values()))[:12]},
                reasons=dict(collections.Counter(x[2].split(';')[0] for x in T).most_common(12)))
