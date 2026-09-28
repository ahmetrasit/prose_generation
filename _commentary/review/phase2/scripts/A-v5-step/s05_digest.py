# Prototype deterministic per-ayah digest: v5 discovery harvest (3 lanes) + script layers v5 lacked.
# Read-only on all repos. Writes digest (the pushed packet) and lookup (the one-read-away full lists).
# Usage: python3 s05_digest.py 1:6 1:2 5:6 18:86 18:96 100:1 103:1 29:38
import json, os, re, csv, sys, collections, glob
csv.field_size_limit(10**9)
H=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.join(H,'out'); DG=os.path.join(OUT,'digests'); os.makedirs(DG,exist_ok=True)
V5='/Volumes/OZTURK/_projects/prose_generation/_commentary/v5'
BI=json.load(open(os.path.join(OUT,'branch_index.json'))); OCC=json.load(open(os.path.join(OUT,'root_occ.json')))
LANES={'1:':'s001-fresh-20260910','5:':'s005-p01-with-fatiha','18:':'s018-regular-20260912','100:':'s100-regular-20260911','103:':'s103-regular-20260911'}
DIAC=re.compile(r'[ؐ-ًؚ-ٰٟۖ-ۭـ]')
def norm(s):
    s=DIAC.sub('',s or ''); s=re.sub('[أإآٱ]','ا',s); return s.replace('ى','ي').replace('ة','ه').replace('ؤ','و').replace('ئ','ي')
# ---------- corpus
TXT={}
for r in csv.DictReader(open('/Volumes/OZTURK/_projects/quran-slm/resources/source/quran_ayah_text_ar.tsv',encoding='utf-8'),delimiter='\t'): TXT[r['ayah_ref']]=r['text_uthmani']
QRA=list(csv.DictReader(open('/Volumes/OZTURK/_projects/quran-slm/resources/source/qac_root_ayah.tsv',encoding='utf-8'),delimiter='\t'))
root_ayahs=collections.defaultdict(set); ayah_roots=collections.defaultdict(set); word_surface={}; ayah_rootrows=collections.defaultdict(list)
for r in QRA:
    root_ayahs[r['root_norm']].add(r['ayah_ref']); ayah_roots[r['ayah_ref']].add(r['root_norm']); ayah_rootrows[r['ayah_ref']].append(r)
    for q,s in zip(r['qac_refs'].split(';'),r['surfaces_ar'].split(';')):
        word_surface[':'.join(q.split(':')[:3])]=s
DEFDF=collections.Counter()
for _b,_v in BI.items():
    _t=norm(' '.join([_v.get('image_ar') or '',_v.get('what_is_ar') or '',_v.get('src_ar') or '']))
    _T=set(re.findall(r'[ء-ي]+',_t)); _T|={re.sub(r'^(وال|فال|بال|لل|ال|و|ف|ب|ل|ك)','',z) for z in list(_T)}; _T|={re.sub(r'(ها|هم|هن|كم|نا|ه|ك)$','',z) for z in list(_T) if len(z)>3}
    DEFDF.update(_T)
RID={}  # root letters -> root id
for b,v in BI.items(): RID.setdefault(v['root'],b.split('/')[0])
STOP={r for r,a in root_ayahs.items() if len(a)>700}  # very frequent roots (ء ل ه, ق و ل, ك و ن ...)
def aref(x):
    m=re.match(r'(\d+):(\d+)',str(x)); return f'{m.group(1)}:{m.group(2)}' if m else None
def wlabel(x):
    parts=str(x).split(':')
    if len(parts)>=3: return word_surface.get(':'.join(parts[:3]),':'.join(parts[:3]))
    return str(x)
def short(b): return b.split('/')[0].replace('root_00','r')+'/'+b.split('/')[1]
def kindflag(b):
    v=BI.get(b) or {}; k=v.get('kind')
    return {'collocation':' [COLLOCATION-BOUND]','non_bare':' [derived-form]','unresolved':' [unresolved]'}.get(k,'')
# ---------- load v5 lanes
def lanes_for(ref):
    s,a=ref.split(':')
    if ref=='29:38':
        g=os.path.join(OUT,'git2938'); return {l:json.load(open(f'{g}/ledger.{l}.json')) for l in ('micro','macro','global')}, None
    aid=LANES.get(s+':')
    if not aid or not os.path.isdir(f'{V5}/raw/{aid}/s{int(s):03d}/{s}_{a}'):
        c=[x for x in glob.glob(f'{V5}/raw/s{int(s):03d}-*/s{int(s):03d}/{s}_{a}') if 'basmala' not in x and os.path.exists(x+'/macro.discovery.json')]
        aid=c[0].split('/raw/')[1].split('/')[0]
    d=f'{V5}/raw/{aid}/s{int(s):03d}/{s}_{a}'
    L={l:json.load(open(f'{d}/{l}.discovery.json')) for l in ('micro','macro','global')}
    pk={}
    for l in L:
        p=f'{V5}/input/{aid}/s{int(s):03d}/{s}_{a}/{l}.discovery.prompt.md'
        if os.path.exists(p):
            t=open(p,encoding='utf-8').read(); i=t.find('<lane_packet_json>'); j=t.find('</lane_packet_json>')
            pk[l]={c['candidate_id']:c for c in json.loads(t[i+len('<lane_packet_json>'):j])['candidate_inventory']}
    return L,pk
# ---------- channel reviews (existing chains)
def channels(s):
    p=f'/Volumes/OZTURK/_projects/quran-data/data/analysis/channels/network-v3/s{int(s):03d}/review/reader_a_pilot.md'
    if not os.path.exists(p): return []
    t=open(p,encoding='utf-8').read(); out=[]; parent=''
    for blk in re.split(r'\n(?=### |#### )',t):
        if blk.startswith('### '): parent=blk.split('\n')[0][4:].strip(); continue
        if not blk.startswith('#### '): continue
        title=blk.split('\n')[0][5:].strip()
        mline=blk.split('Active motifs:')[1].split('\n')[0] if 'Active motifs:' in blk else ''
        motifs=[(m[0],m[1].replace(':','/')) for m in re.findall(r'([^;`]+?)\s*`quranic:(root_\d+:B\d+)/m\d+`',mline)]
        motifs+=[(m[0],RID.get(m[1],'?')+'/'+m[2]) for m in re.findall(r'([^;`]+?)\s*`([^`:]+?):(B\d+)/m\d+`',mline) if not m[1].startswith('quranic')]
        anch=blk.split('Ayah anchors:')[1].split('\n')[0] if 'Ayah anchors:' in blk else ''
        syn=blk.split('Synthesis:')[1].split('\n')[0].strip() if 'Synthesis:' in blk else ''
        scene=blk.split('Scene or process:')[1].split('\n')[0].strip() if 'Scene or process:' in blk else ''
        ays=set()
        for m in re.finditer(r'(\d+):([\d,\-]+)',re.sub(r'`[^`]*`','',anch)):
            su=m.group(1)
            for part in m.group(2).split(','):
                if '-' in part:
                    x,y=part.split('-'); ays|={f'{su}:{k}' for k in range(int(x),int(y)+1) if x.isdigit() and y.isdigit()}
                elif part.isdigit(): ays.add(f'{su}:{part}')
        out.append({'parent':parent,'title':title,'scene':scene,'motifs':[(m[0].strip(' ;'),m[1]) for m in motifs],'ayat':ays,'syn':syn})
    return out
def build(ref):
    s,a=ref.split(':'); s=int(s); a=int(a)
    L,pk=lanes_for(ref); pk=pk or {}
    froots=[r for r in dict.fromkeys(x['root_norm'] for x in ayah_rootrows[ref])]
    fwords={x['root_norm']:x['surfaces_ar'].replace(';','، ') for x in ayah_rootrows[ref]}
    frids={RID[r]:r for r in froots if r in RID}
    acts=collections.defaultdict(lambda:{'trig':collections.Counter(),'find':[],'modes':collections.Counter(),'lanes':set()})
    finds=[]; notes=[]; excl=[]
    for lane,d in L.items():
        cands=pk.get(lane,{})
        for f in d.get('findings',[]):
            if not isinstance(f,dict): continue
            fid=f"{lane[:2]}{len(finds)+1}"
            bl=[x for x in (f.get('branch_activations') or []) if isinstance(x,dict) and x.get('branch_ref')]
            nonprim=[x for x in bl if not (x['branch_ref'].split('/')[0] in frids and x.get('application_mode')=='lexical')]
            if lane=='micro' and not nonprim:
                notes.append(f.get('title','')); continue
            finds.append((fid,lane,f.get('title',''),re.split(r'(?<=[.;])\s',(f.get('claim') or '').strip())[0],[x['branch_ref'] for x in bl],f))
            for x in bl:
                A=acts[x['branch_ref']]; A['find'].append(fid); A['modes'][x.get('application_mode')]+=1; A['lanes'].add(lane)
                for t in (x.get('trigger_refs') or [])+(x.get('carrier_refs') or []):
                    ar=aref(t)
                    lab = (str(wlabel(t))+(' '+ar if ar and ar!=ref else '')) if len(str(t).split(':'))>=3 else (ar if ar and ar!=ref else ('focus' if ar else str(t)))
                    A['trig'][lab]+=1
        for c in d.get('candidate_decisions',[]):
            ctitle=(cands.get(c.get('candidate_id')) or {}).get('title','')
            for be in c.get('branch_exclusions') or []:
                if isinstance(be,dict) and be.get('branch_ref'): excl.append((be['branch_ref'],lane,c.get('decision'),ctitle,be.get('reason','')))
            if c.get('decision')=='reject':
                cc=cands.get(c.get('candidate_id')) or {}
                for b in set((cc.get('branch_refs') or [])+(cc.get('nominated_branch_refs') or [])):
                    excl.append((b,lane,'reject',ctitle,c.get('reason','')))
    D=[]; LK=[]
    D.append(f'# {ref}\n{TXT.get(ref,"")}\n')
    # A. focus-root branches v5 activated
    D.append('## A. Branches of this ayah\'s words that the harvest activated (word: branch gloss ← contact words/ayat)')
    ctx=[]
    for b,A in sorted(acts.items(),key=lambda kv:-len(kv[1]['find'])):
        v=BI.get(b) or {'root':'?','gloss':'?'}
        trig=', '.join(k for k,_ in A['trig'].most_common(6))
        line=f"- {v['root']} {short(b)} {v.get('gloss')}{kindflag(b)} ← {trig} [{len(A['find'])} readings]"
        (D if b.split('/')[0] in frids else ctx).append(line)
    D.append('## B. Branches of other words (window, surah, wider) that the harvest brought to this ayah'); D+=ctx
    D.append('## C. Readings the harvest built (lane; title; first clause; branches)')
    for fid,lane,title,claim,brs,f in finds:
        D.append(f"- {fid} {title}: {claim} {{{', '.join(short(b) for b in dict.fromkeys(brs))}}}")
    D.append('## C2. Word and grammar notes (titles): '+' | '.join(dict.fromkeys(notes)))
    # D. set aside upstream, not activated anywhere in the ayah
    act_set=set(acts); seen=set(); lines=[]
    for b,lane,dec,ct,reason in excl:
        if b in act_set or b in seen: continue
        seen.add(b); v=BI.get(b) or {'root':'?','gloss':'?'}
        lines.append(f"- {v['root']} {short(b)} {v.get('gloss')}{kindflag(b)}" + (f" (proposed in: {ct})" if ct else ''))
    D.append('## D. Proposed upstream but not bound to this ayah (no verdict carried; reasons in lookup)'); D+=lines
    # E. unused branches of focus roots
    D.append('## E. Other attested branches of this ayah\'s roots (not used above)')
    for rid,rn in frids.items():
        rest=[b for b in BI if b.startswith(rid+'/') and b not in act_set and b not in seen]
        if rest: D.append(f"- {rn} ({fwords.get(rn,'')}): "+'; '.join(f"{b.split('/')[1]} {BI[b]['gloss']}{kindflag(b)}" for b in rest))
    # F1 concordance / recurring roles
    D.append('## F1. Quranic distribution of this ayah\'s less frequent roots (ayat; co-occurring roots with counts; refs of top partner)')
    for rn in froots:
        ays=root_ayahs.get(rn,set())
        if not ays or len(ays)>60 or rn in STOP: continue
        co=collections.Counter()
        for x in ays:
            for r2 in ayah_roots[x]:
                if r2!=rn and r2 not in STOP: co[r2]+=1
        top=[(r2,c) for r2,c in co.most_common(8) if c>=2]
        if not top: D.append(f"- {rn}: {len(ays)} ayat ({', '.join(sorted(ays,key=lambda z:tuple(map(int,z.split(':')))))})"); continue
        r0=top[0][0]; refs0=sorted([x for x in ays if r0 in ayah_roots[x]],key=lambda z:tuple(map(int,z.split(':'))))
        D.append(f"- {rn}: {len(ays)} ayat; with "+', '.join(f"{r2} {c}" for r2,c in top)+f"; {r0} at {', '.join(refs0)}" + (f"; all: {', '.join(sorted(ays,key=lambda z:tuple(map(int,z.split(':')))))}" if len(ays)<=25 else ''))
    # F2 definitional cross-references (dictionary definitions naming another root present in the surah)
    surah_ayat=[k for k in TXT if k.split(':')[0]==str(s)]
    sroots=collections.defaultdict(set)
    for k in surah_ayat:
        for r2 in ayah_roots[k]: sroots[r2].add(k)
    forms=collections.defaultdict(set)
    for k in surah_ayat:
        for x in ayah_rootrows[k]:
            for f_ in re.split(r'[;|,\s]+',x['lemmas_ar']+';'+x['surfaces_ar']):
                n=norm(f_); n=re.sub(r'^(وال|فال|بال|لل|ال|و|ف)','',n) if len(n)>4 else n
                if len(n)>=3 or (len(n)==2 and f_ in x['lemmas_ar']): forms[x['root_norm']].add(n)
    def toks(b):
        v=BI[b]; t=norm(' '.join([v.get('image_ar') or '',v.get('what_is_ar') or '',v.get('src_ar') or '']))
        T=set(re.findall(r'[ء-ي]+',t)); T|={re.sub(r'^(وال|فال|بال|لل|ال|و|ف|ب|ل|ك)','',z) for z in list(T)}; T|={re.sub(r'(ها|هم|هن|كم|نا|ه|ك)$','',z) for z in list(T) if len(z)>3}
        return T
    xr=[]
    for rid,rn in frids.items():
        for b in [b for b in BI if b.startswith(rid+'/')]:
            T=toks(b)
            for r2,fs in forms.items():
                if r2==rn or len(root_ayahs.get(r2,()))>1500: continue
                m=fs&T
                if m:
                    near=sorted(sroots[r2],key=lambda z:abs(int(z.split(':')[1])-a))[:3]
                    xr.append((abs(int(near[0].split(':')[1])-a) if near else 999,f"- {rn} {b.split('/')[1]} {BI[b]['gloss']} — its definition names {'/'.join(sorted(m)[:2])} ({r2}) → {', '.join(near)}"))
    # reverse: window roots whose branch definitions name a focus-root form (window ±7)
    win=[f'{s}:{k}' for k in range(max(1,a-7),a+8) if f'{s}:{k}' in TXT and k!=a]
    wroots={r2 for k in win for r2 in ayah_roots[k] if len(root_ayahs.get(r2,()))<=1500}-set(froots)
    fforms=collections.defaultdict(set)
    for x in ayah_rootrows[ref]:
        for f_ in re.split(r'[;|,\s]+',x['lemmas_ar']+';'+x['surfaces_ar']):
            n=norm(f_); n=re.sub(r'^(وال|فال|بال|لل|ال|و|ف)','',n) if len(n)>4 else n
            if len(n)>=3 or (len(n)==2 and f_ in x['lemmas_ar']): fforms[x['root_norm']].add(n)
    for r2 in wroots:
        if r2 not in RID: continue
        for b in [b for b in BI if b.startswith(RID[r2]+'/')]:
            T=toks(b)
            for rn,fs in fforms.items():
                if len(root_ayahs.get(rn,()))>1500: continue
                m=fs&T
                if m:
                    near=sorted([k for k in win if r2 in ayah_roots[k]],key=lambda z:abs(int(z.split(':')[1])-a))[:2]
                    xr.append((abs(int(near[0].split(':')[1])-a),f"- {r2} {b.split('/')[1]} {BI[b]['gloss']} (at {', '.join(near)}) — its definition names {'/'.join(sorted(m)[:2])} ({rn}, this ayah)"))
    D.append('## F2. Dictionary definitions that name another word of the surah (nearest ayat first; far/common hits in lookup)')
    for dist,line in sorted(xr):
        rr=re.search(r'\(([^()]+?)(, this ayah)?\)',line.split('names')[1]).group(1)
        tok=line.split('names ')[1].split(' ')[0].split('/')[0]
        df=DEFDF.get(tok,0)
        if (dist==0 and df<=350) or (df<=60) or (df<=200 and dist<=2): D.append(line)
        else: LK.append(json.dumps({'xref_far':line},ensure_ascii=False))
    # F3 existing surah chains touching this ayah
    D.append('## F3. Surah image chains (channel review) that touch this ayah: title — scene — members')
    for c in channels(s):
        mem=[m for m in c['motifs'] if m[1].split('/')[0] in frids]
        if ref in c['ayat'] or mem:
            D.append(f"- {c['title']} — {c['scene']} — members: "+'; '.join(f"{m[0]} ({BI.get(m[1],{}).get('root','?')} {m[1].split('/')[1]})" for m in c['motifs']))
    # F4 same-surah parallels (≥2 shared non-stop roots)
    par=[]
    idf=lambda r2: 1/len(root_ayahs[r2])
    for k in surah_ayat:
        if k==ref: continue
        sh=(set(froots)-STOP)&ayah_roots[k]
        if len(sh)>=2 or any(len(root_ayahs[r2])<=150 for r2 in sh): par.append((-sum(idf(r2) for r2 in sh),k,sorted(sh)))
    D.append('## F4. Same-surah ayat sharing this ayah\'s roots (rarest first)')
    D+=[f"- {k}: {' '.join(sh)}" for _,k,sh in sorted(par)[:40]]
    # F5 Turkish loss (error profile of the activated branches of this ayah's words)
    D.append('## F5. Turkish gloss losses/additions recorded by the dictionary (activated branches of this ayah\'s words)')
    for b in acts:
        if b.split('/')[0] in frids:
            v=BI[b]
            if v.get('loses') or v.get('adds'): D.append(f"- {v['root']} {b.split('/')[1]} «{v['gloss']}»: loses {v.get('loses')}; adds {v.get('adds')}")
            for g in v.get('tr_glosses') or []:
                D.append(f"- {v['root']} {b.split('/')[1]} «{g[0]}» ({g[1]}): loses {g[2]}; adds {g[3]}" + (f"; collides {g[4]}" if g[4] else ''))
    # F6 early-source phrases for activated non-primary branches of this ayah's words
    D.append('## F6. Early-source phrases (the project dictionary) for the branches in A')
    for b in acts:
        if b.split('/')[0] in frids and not b.endswith('/B001'):
            v=BI[b]; cl=[c.strip() for c in (v.get('src_ar') or '').split('؛') if c.strip()]
            D.append(f"- {v['root']} {b.split('/')[1]}: {'؛ '.join(cl[:2])}" + (f" | scope: {v.get('scope_note')}" if v.get('kind')=='collocation' else ''))
            if len(cl)>2: LK.append(json.dumps({'src_full':b,'src':v.get('src_ar')},ensure_ascii=False))
    # F7 cross-word branch pairs inside the ayah (quran-slm fused affinity; ordering only)
    global _PAIRS
    try: _PAIRS
    except NameError:
        _ns={}; exec(open(os.path.join(H,'s06_intra_ayah_coherence.py')).read().split("if __name__=='__main__':")[0],_ns); _PAIRS=_ns
    ns=_PAIRS; roots7=[r for r in froots if r in ns['by_rootkey'] and len(root_ayahs.get(r,()))<=1500]
    P=[]
    for i,X in enumerate(roots7):
        for Y in roots7[i+1:]:
            A7=ns['by_rootkey'][X]; B7=ns['by_rootkey'][Y]; S7=ns['fused'](A7,B7)
            for ia in range(len(A7)):
                for ib in range(len(B7)):
                    if S7[ia,ib]>0: P.append((float(S7[ia,ib]),ns['lab'][A7[ia]],ns['lab'][B7[ib]]))
    P.sort(reverse=True)
    def g7(l):
        r_,b_=l.rsplit(' ',1); rid_=RID.get(r_); v_=BI.get(f'{rid_}/{b_}',{}); return f"{l} {v_.get('gloss','')}{kindflag(f'{rid_}/{b_}')}"
    D.append('## F7. Branch pairs across this ayah\'s words that lie close in the dictionary-similarity space (closest first; ordering only)')
    D+=[f"- {g7(a_)} ~ {g7(b_)}" for sc,a_,b_ in P[:30]]
    for sc,a_,b_ in P[30:300]: LK.append(json.dumps({'pair':[a_,b_],'score':round(sc,4)},ensure_ascii=False))
    # lookup: everything else, full
    for fid,lane,title,claim,brs,f in finds:
        LK.append(json.dumps({'id':fid,'lane':lane,'title':title,'claim':f.get('claim'),'mechanism':f.get('mechanism'),'payoff':f.get('reader_payoff'),'containment':f.get('containment'),'status':(f.get('epistemic') or {}).get('status'),'acts':[{k:x.get(k) for k in ('branch_ref','application_mode','carrier_refs','trigger_refs','independent_trigger','activation')} for x in f.get('branch_activations',[]) if isinstance(x,dict)]},ensure_ascii=False))
    for e in excl: LK.append(json.dumps({'excluded':e[0],'lane':e[1],'decision':e[2],'proposal':e[3],'reason':e[4]},ensure_ascii=False))
    dig='\n'.join(D); lk='\n'.join(LK)
    fn=ref.replace(':','_')
    open(os.path.join(DG,f'{fn}.digest.md'),'w').write(dig); open(os.path.join(DG,f'{fn}.lookup.jsonl'),'w').write(lk)
    # section sizes
    secs=collections.OrderedDict(); cur='head'
    for line in D:
        for l_ in line.split('\n'):
            if l_.startswith('## '): cur=l_[3:6].strip('. ')
            secs[cur]=secs.get(cur,0)+len(l_.encode())+1
    raw=sum(os.path.getsize(p) for p in []) 
    return len(dig.encode()),len(lk.encode()),secs,len(finds),len(acts),len(seen)
if __name__=='__main__':
    print('ayah\tdigest_bytes\t~tokens(2.0B/t)\tlookup_bytes\t~tokens\tfindings\tbranches\tset_aside\tsections(bytes)')
    for ref in sys.argv[1:]:
        db,lb,secs,nf,na,ns=build(ref)
        print(f"{ref}\t{db}\t{db//2}\t{lb}\t{lb//2}\t{nf}\t{na}\t{ns}\t"+' '.join(f"{k}:{v}" for k,v in secs.items()))
