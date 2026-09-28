import json, os, re
from pathlib import Path
from collections import Counter, defaultdict
W = Path('/Volumes/OZTURK/_projects/prose_generation/_commentary/v9/lines/work')
def codex_usage(f):
    t=Counter()
    for line in f.read_text(errors='ignore').splitlines():
        try: e=json.loads(line)
        except: continue
        if e.get('type')=='turn.completed':
            u=e.get('usage',{})
            t['in']+=u.get('input_tokens',0); t['cached']+=u.get('cached_input_tokens',0); t['out']+=u.get('output_tokens',0); t['reason']+=u.get('reasoning_output_tokens',0); t['turns']+=1
    return t
for sa in sorted(os.listdir(W), key=lambda x:[int(p) for p in x.split('_')]):
    d=W/sa
    bundles=Counter(re.match(r'(local|usage|surah|related)_\d+\.md',f.name).group(1) for f in d.glob('*_*.md') if re.match(r'(local|usage|surah|related)_\d+\.md',f.name))
    items = sum(1 for _ in open(d/'items.tsv')) -1 if (d/'items.tsv').exists() else None
    st=Counter(); sup=Counter(); rel=Counter(); nrec=0; perline=Counter()
    rd=d/'records'
    recfiles = sorted(rd.glob('*.jsonl')) if rd.exists() else []
    for f in recfiles:
        ln=f.stem.split('_')[0]
        for line in f.read_text(errors='ignore').splitlines():
            try: r=json.loads(line)
            except: continue
            nrec+=1; s=r.get('status','?'); st[s]+=1; perline[(ln,s)]+=1
            if s in ('reading','open','note'):
                sup[r.get('support')]+=1; rel[r.get('relevance')]+=1
            if r.get('id','').split('.')[-1].startswith('X') or '.X' in r.get('id','') or r.get('id','').startswith('X'): st['X-ids']+=1
    tot=Counter()
    lg=d/'logs'
    if lg.exists():
        for f in lg.glob('*.jsonl'):
            tot+=codex_usage(f)
    pkg = (d/'package.md').stat().st_size if (d/'package.md').exists() else 0
    slim = (d/'package.slim.md').stat().st_size if (d/'package.slim.md').exists() else 0
    ctx = (d/'context.md').stat().st_size if (d/'context.md').exists() else 0
    print(f"{sa}: bundles {dict(bundles)} items {items} recfiles {len(recfiles)} records {nrec} status {dict(st)} rel {dict(rel)} sup {dict(sup)} | luna tokens in {tot['in']} cached {tot['cached']} out {tot['out']} reason {tot['reason']} turns {tot['turns']} | ctx {ctx} pkg {pkg} slim {slim}")
