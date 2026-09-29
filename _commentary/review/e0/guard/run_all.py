"""Run the detector over every Quranic occurrence of every root that has collocation or non_bare branches and write
the VERIFICATION RECORD guard_calls.tsv (one row per occurrence x guarded branch). This file is for the user and
for verification scripts only: it must never be copied into a brief, supply or any text a model reads.
Also writes eval_by_branch.tsv (per-branch dossier comparison) and run_all_summary.json."""
import sys, os, csv, json, collections, time
sys.dont_write_bytecode = True
import gdata as G
import detector as Dt
import eval_dossier as E

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    t = time.time()
    B = G.dictionary()['branches']
    cnt = collections.Counter()
    kinds = collections.Counter()
    reasons = collections.Counter()
    n = 0
    with open(os.path.join(HERE, 'guard_calls.tsv'), 'w', encoding='utf-8') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(['occurrence', 'surface', 'branch_ref', 'root', 'branch_kind', 'call', 'level', 'reason',
                    'matched_statement'])
        for occ, ref, call, lv, why, cons in Dt.all_calls():
            n += 1
            cnt[call] += 1
            kinds[(B[ref]['kind'], call)] += 1
            reasons[why.split(';')[0]] += 1
            w.writerow([occ, G.words()[occ]['surface'], ref, B[ref]['root'], B[ref]['kind'], call, lv, why, cons])
    res, rows = E.run(names=('main',))
    per = collections.defaultdict(collections.Counter)
    for r in rows:
        if r['kind'] == 'true':
            per[r['branch']][r['call']] += 1
    with open(os.path.join(HERE, 'eval_by_branch.tsv'), 'w', encoding='utf-8') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(['branch_ref', 'root', 'image', 'split', 'placements', 'present', 'absent', 'unknown',
                    'top_reason_not_present'])
        for b, v in sorted(per.items(), key=lambda x: -sum(x[1].values())):
            why = collections.Counter(r['why'].split(';')[0] + (';' + r['why'].split(';')[1] if ';' in r['why'] else '')
                                      for r in rows if r['kind'] == 'true' and r['branch'] == b and r['call'] != 'present')
            split = 'excluded' if b in E.GRAM | E.NOISY else ('dev' if b in E.DEV else 'test')
            w.writerow([b, B[b]['root'], B[b]['image'], split, sum(v.values()), v['present'], v['absent'], v['unknown'],
                        '; '.join(f'{k} ({c})' for k, c in why.most_common(2))])
    summ = dict(rows=n, calls=dict(cnt), by_kind={f'{k}:{c}': v for (k, c), v in sorted(kinds.items())},
                reasons=dict(reasons.most_common()), seconds=round(time.time() - t, 1))
    json.dump(summ, open(os.path.join(HERE, 'run_all_summary.json'), 'w'), ensure_ascii=False, indent=1)
    print(json.dumps(summ, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
