import json, sys, os, glob
root = sys.argv[1]
rows = []
for f in sorted(glob.glob(os.path.join(root, '**', '*.jsonl'), recursive=True)):
    res = []
    for line in open(f, encoding='utf-8'):
        if '"type":"result"' in line.replace(' ', ''):
            try: res.append(json.loads(line))
            except Exception: pass
    for d in res:
        u = d.get('usage', {})
        th = (u.get('output_tokens_details') or {}).get('thinking_tokens', 0)
        inp = u.get('input_tokens',0)+u.get('cache_creation_input_tokens',0)+u.get('cache_read_input_tokens',0)
        rows.append((os.path.relpath(f, root), d.get('total_cost_usd',0), inp, u.get('cache_read_input_tokens',0), u.get('output_tokens',0), th, d.get('num_turns'), round(d.get('duration_ms',0)/60000,1), list((d.get('modelUsage') or {}).keys())))
tot = 0
for r in rows:
    tot += r[1]
    print(f"{r[0]:70s} ${r[1]:6.2f} in={r[2]:>7,} cread={r[3]:>7,} out={r[4]:>7,} think={r[5]:>7,} turns={r[6]} min={r[7]} {r[8]}")
print('TOTAL', round(tot,2), 'n', len(rows))
