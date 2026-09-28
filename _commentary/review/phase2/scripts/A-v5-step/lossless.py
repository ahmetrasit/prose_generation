"""Check that the digest drops no branch, finding or set-aside item (only prose fields and labels)."""
import json, re, lib, digest
for ref in ['1:6', '1:2', '5:6', '18:86', '18:96', '100:1', '103:1']:
    disc, rd = lib.load_discovery(ref)
    raw_b = {a['branch_ref'] for d in disc.values() for f in d['findings'] for a in f.get('branch_activations') or [] if isinstance(a, dict) and a.get('branch_ref')}
    raw_f = sum(len(d['findings']) for d in disc.values())
    raw_rej = sum(1 for d in disc.values() for c in d['candidate_decisions'] if c['decision'] == 'reject')
    raw_nar_ex = sum(1 for d in disc.values() for c in d['candidate_decisions'] if c['decision'] == 'narrow' and (c.get('branch_exclusions') or c.get('facet_exclusions') or c.get('context_exclusions')))
    D = digest.build(ref)
    t = digest.render(D, 'full')
    dig_b = set(D['branches'])
    shown = sum(1 for b in raw_b if f"{b.split('/')[1]} [" in t)  # weak textual check
    print(ref, 'branches raw', len(raw_b), 'in digest index', len(raw_b & dig_b), '| findings raw', raw_f, 'digest', len(D['findings']),
          '| rejects raw', raw_rej, '+ narrow-with-exclusions', raw_nar_ex, '-> set-asides', len(D['sets']), 'dropped root-occurrence', D['stats']['dropped_root_occurrence_setaside'])
