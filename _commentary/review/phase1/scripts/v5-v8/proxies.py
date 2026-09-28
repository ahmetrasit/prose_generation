import glob,re,statistics as st,collections,os
B='/Volumes/OZTURK/_projects/prose_generation/_commentary/v5/editorial'
tag=re.compile(r'\{ar:[^}]*\}')
dicts=re.compile(r'(Lis[âa]n|K[âa]m[ûu]s|T[âa]c[üu]|Cevher[îi]|Ezher[îi]|R[âa]g[ıi]b|Hal[îi]l|Mek[âa]y[îi]s|S[ıi]h[âa]h|İbn F[âa]ris|Ferâhîdî|Müfred[âa]t|Cemhere|Muhkem|Tehz[îi]b)',re.I)
ref=re.compile(r'\b(\d{1,3}):(\d{1,3})\b')
stats=collections.defaultdict(list)
for p in glob.glob(B+'/*/*/*/*.prose.editorial.tr.md'):
    if 'luna-6' in p: continue
    aid=p[len(B)+1:].split('/')[0]
    grp='S1-Astra' if aid.startswith('s001') else ('S87-114' if int(aid[1:4])>=87 else 'S5-32')
    if 'basmala' in aid: grp='basmala'
    t=open(p,encoding='utf-8').read()
    plain=tag.sub(' X ',t); words=len(plain.split())
    s,a=map(int,re.search(r'/(\d+)_(\d+)\.prose',p).groups())
    refs=set(m.group(0) for m in ref.finditer(t))
    other=set(r for r in refs if int(r.split(':')[0])!=s)
    same=set(r for r in refs if int(r.split(':')[0])==s)
    stats[(grp,'words')].append(words)
    stats[(grp,'turkce_mention')].append(1 if re.search(r'Türkçe',t) else 0)
    stats[(grp,'sozluk_mentions')].append(len(re.findall(r'sözlü',t,re.I)))
    stats[(grp,'named_dict')].append(1 if dicts.search(t) else 0)
    stats[(grp,'degil_per_1k')].append(1000*len(re.findall(r'\bdeğil',t))/max(words,1))
    stats[(grp,'refs_other_surah')].append(len(other))
    stats[(grp,'refs_same_surah')].append(len(same))
    stats[(grp,'ar_tags')].append(len(tag.findall(t)))
    stats[(grp,'headings')].append(len(re.findall(r'^## ',t,re.M)))
for k in sorted(stats):
    v=stats[k]
    print(f'{k[0]:10s} {k[1]:18s} n={len(v):4d} mean={st.mean(v):8.2f} median={st.median(v):8.2f}')
