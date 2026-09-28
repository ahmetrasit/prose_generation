import json,re,glob,random,os,statistics as st,collections
B='/Volumes/OZTURK/_projects/prose_generation/_commentary/v5'
random.seed(3)
eds=[p for p in glob.glob(B+'/editorial/*/*/*/*.prose.editorial.tr.md') if 'luna-6' not in p and 'basmala' not in p]
s1=[p for p in eds if '/s001-' in p]
sample=s1+random.sample([p for p in eds if p not in s1],120)
res=collections.defaultdict(list)
for ed in sample:
    parts=ed[len(B)+1:].split('/'); aid,sd,ay=parts[1],parts[2],parts[3]
    gp=f'{B}/input/{aid}/{sd}/{ay}/global.discovery.prompt.md'
    if not os.path.exists(gp): continue
    t=open(gp,encoding='utf-8').read()
    i=t.find('<lane_packet_json>'); j=t.find('</lane_packet_json>')
    pk=json.loads(t[i+len('<lane_packet_json>'):j])
    rows=pk.get('connection_registry',[])
    s=int(ay.split('_')[0])
    tgt=set()
    for r in rows:
        js=json.dumps(r,ensure_ascii=False)
        for m in re.finditer(r'(?<![\d:])(\d{1,3}):(\d{1,3})(?![\d:])',js):
            if int(m.group(1))!=s: tgt.add(m.group(0))
    e=open(ed,encoding='utf-8').read()
    er=set(m.group(0) for m in re.finditer(r'(?<![\d:])(\d{1,3}):(\d{1,3})(?![\d:])',e) if int(m.group(1))!=s)
    grp='S1-Astra' if aid.startswith('s001') else 'Luna/Sol'
    res[(grp,'rows')].append(len(rows)); res[(grp,'row_targets_other_surah')].append(len(tgt)); res[(grp,'editorial_other_refs')].append(len(er)); res[(grp,'editorial_refs_in_rows')].append(len(er&tgt))
    res[(grp,'frac_row_targets_used')].append(len(er&tgt)/max(len(tgt),1))
for k in sorted(res):
    v=res[k]; print(k, 'n',len(v),'median',round(st.median(v),3),'mean',round(st.mean(v),3))
