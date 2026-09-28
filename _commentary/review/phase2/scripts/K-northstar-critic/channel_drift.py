"""How much of the existing chains (network-v3 channel reviews) rests on collocation-bound branches whose
construction is not detected at the anchored ayah?  Uses the dictionary's branch_kind (kb.py) and C2's
per-occurrence construction index (R5 rule; recall 0.33 vs root-dossier, so 'not detected' over-counts drift).
Read-only; outputs to this dir."""
import re,glob,csv,collections,json,sys,os
sys.path.insert(0,os.path.dirname(__file__))
import kb
B=kb.load()
NET='/Volumes/OZTURK/_projects/quran-data/data/analysis/channels/network-v3'
C2='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/C2-loaded-parallels/construction_index.tsv'
# construction presence per (surah:ayah, branch_ref)
pres=collections.defaultdict(int); seen=set()
for r in csv.DictReader(open(C2),delimiter='\t'):
    s,a,w=r['ref3'].split(':'); key=(f'{s}:{a}',r['branch'])
    seen.add(key); pres[key]=max(pres[key],int(r['present']))
rid2root={b['rid']:b['root'] for b in B.values()}
def expand(tok):
    # '29:4,7-9' -> list of s:a
    out=[]; m=re.match(r'(\d+):(.*)',tok)
    if not m: return out
    s=m.group(1)
    for part in m.group(2).split(','):
        part=part.strip()
        if '-' in part:
            x,y=part.split('-'); 
            try: out+= [f'{s}:{i}' for i in range(int(x),int(y)+1)]
            except: pass
        elif part.isdigit(): out.append(f'{s}:{part}')
    return out
stats=collections.Counter(); rows=[]; per_surah=collections.Counter(); per_surah_tot=collections.Counter()
for f in sorted(glob.glob(NET+'/s*/review/reader_a_pilot.md')):
    sur=f.split('/')[-3]
    txt=open(f).read()
    for block in re.split(r'\n### ',txt):
        title=block.split('\n',1)[0][:90]
        motifs=re.findall(r'quranic:(root_\d+):(B\d+)',block)
        anc=re.search(r'Ayah anchors:(.*)',block)
        if not motifs or not anc: continue
        anchors=collections.defaultdict(list)
        for piece in anc.group(1).split(';'):
            piece=piece.strip().rstrip('.')
            m=re.match(r'([^\d]+?)\s+(\d.*)',piece)
            if not m: continue
            root=m.group(1).strip()
            for t in m.group(2).split():
                anchors[root]+=expand(t)
        for rid,bid in set(motifs):
            ref=f'{rid}/{bid}'; b=B.get(ref)
            if not b: stats['member_missing_in_dict']+=1; continue
            root=b['root']; ayat=anchors.get(root,[])
            stats['members']+=1; per_surah_tot[sur]+=1
            stats['kind_'+str(b['kind'])]+=1
            if b['kind']!='collocation': continue
            if not ayat: stats['colloc_no_anchor']+=1; continue
            det=[a for a in ayat if pres.get((a,ref),0)]
            known=[a for a in ayat if (a,ref) in seen]
            if det: stats['colloc_construction_detected']+=1
            elif known: stats['colloc_construction_not_detected']+=1; per_surah[sur]+=1; rows.append((sur,title,root,bid,b['image'],','.join(ayat[:6]),(b['note'] or '')[:120]))
            else: stats['colloc_root_absent_at_anchor']+=1
print(json.dumps(stats,ensure_ascii=False,indent=1))
m=stats['members']; c=stats['kind_collocation']
print(f"collocation share of members: {c}/{m} = {c/m:.3f}; not detected at anchor: {stats['colloc_construction_not_detected']}/{m} = {stats['colloc_construction_not_detected']/m:.3f}")
for s in ['s001','s018','s029','s100','s103','s005','s004']:
    if per_surah_tot[s]: print(s, per_surah[s], '/', per_surah_tot[s])
with open(os.path.join(os.path.dirname(__file__),'channel_drift_rows.tsv'),'w') as o:
    o.write('surah\tsubchannel\troot\tbranch\timage\tanchored_ayat\tscope_note\n')
    for r in rows: o.write('\t'.join(r)+'\n')
print('rows',len(rows))
