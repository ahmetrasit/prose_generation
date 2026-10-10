import json, sys
d = json.load(open(sys.argv[1]))
print('confidence', json.dumps(d.get('confidence'), ensure_ascii=False)[:1500])
for f in d['findings']:
    print('== model', f.get('model'), {k: v for k, v in f.items() if k not in ('validation', 'model', 'target')})
    v = f['validation']
    print('rows', v.get('rows'), 'dups', v.get('duplicates'), 'schema', v.get('schema_errors'))
    for x in v.get('findings', []):
        if x['kind'] == 'reference_alias':
            print('  alias', x['line'], x.get('raw_ref'), '->', x['ref'])
        elif x['kind'] == 'unresolved_text':
            print('  unresolved', x['line'], x['ref'])
        else:
            vm = [r['reading'].get('type') + ':' + r['reading'].get('text', '') for r in x.get('variant_matches', [])]
            nb = x.get('matching_neighbours')
            print('  ', x['kind'], x['line'], x['ref'], x.get('field'), x.get('wording'), vm, nb, {k: v for k, v in x.items() if k not in ('line','ref','field','wording','variant_matches','matching_neighbours','kind','message','language')})
    for k in v:
        if k not in ('file','rows','unique_references','schema_errors','duplicates','strengths','findings'):
            print('  extra', k, json.dumps(v[k], ensure_ascii=False)[:2000])
