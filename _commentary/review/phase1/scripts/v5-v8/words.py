import os,glob,re,collections,statistics as st
B='/Volumes/OZTURK/_projects/prose_generation/_commentary/v5'
tag=re.compile(r'\{ar:[^}]*\}')
def wc(p):
    t=open(p,encoding='utf-8').read()
    t=tag.sub(' X ',t)
    return len(t.split())
def fam(aid):
    f=re.sub(r'-\d{8}$','',aid); f=re.sub(r'-p\d\d-','-pNN-',f); 
    return f
res=collections.defaultdict(list)
pats={'scope_micro':'raw/*/*/*/micro.scope.tr.md','scope_macro':'raw/*/*/*/macro.scope.tr.md','scope_global':'raw/*/*/*/global.scope.tr.md','canonical':'raw/*/*/*/*_*.prose.tr.md','editorial':'editorial/*/*/*/*.prose.editorial.tr.md','invitation':'editorial/*/*/*/*.invitation.tr.md','middle':'middle/*/*/*/*.prose.middle.tr.md','concise':'concise/*/*/*/*.prose.concise.tr.md'}
for k,pat in pats.items():
    for p in glob.glob(os.path.join(B,pat)):
        if 'luna-6' in p: continue
        aid=p[len(B)+1:].split('/')[1]
        res[(k,'ALL')].append(wc(p))
        s=re.match(r's(\d{3})',aid).group(1)
        grp='S1' if s=='001' else ('S87-114' if int(s)>=87 else 'S5-32')
        if 'basmala' in aid: grp='basmala'
        res[(k,grp)].append(wc(p))
for k in sorted(res):
    v=res[k]; print(f'{k[0]:14s} {k[1]:8s} n={len(v):4d} median={st.median(v):7.0f} mean={st.mean(v):7.0f} max={max(v):6d} total={sum(v)}')
