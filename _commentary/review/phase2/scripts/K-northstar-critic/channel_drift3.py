"""Subchannel-level impact of construction-free collocation members (reuses channel_drift2 parsing)."""
import re,glob,csv,collections,sys,os
sys.path.insert(0,os.path.dirname(__file__))
exec(open(os.path.join(os.path.dirname(__file__),'channel_drift2.py')).read().split("st=collections.Counter()")[0])
tot=0; any1=0; half=0; examples=[]
for f in sorted(glob.glob(NET+'/s*/review/reader_a_pilot.md')):
    sur=f.split('/')[-3]; txt=open(f).read()
    for block in re.split(r'\n#{3,4} ',txt):
        title=block.split('\n',1)[0][:80]
        if 'Active motifs' not in block: continue
        mem=set(f'{r}/{b}' for r,b in M1.findall(block))
        for root,bid in M2.findall(block):
            rid=root2rid.get(root)
            if rid: mem.add(f'{rid}/{bid}')
        mem=[m for m in mem if m in B]
        if not mem: continue
        anc=re.search(r'Ayah anchors:(.*)',block); ayat=refs(anc.group(1)) if anc else refs(block)
        nd=0
        for ref in mem:
            if B[ref]['kind']!='collocation': continue
            here=[a for a in ayat if (a,ref) in seen]
            if here and not any(pres.get((a,ref)) for a in here): nd+=1
        tot+=1
        if nd: any1+=1
        if nd/len(mem)>=0.5: half+=1; examples.append((sur,title,nd,len(mem)))
print(f'subchannels {tot}; with >=1 construction-free collocation member {any1} ({any1/tot:.1%}); with >=50% such members {half}')
for e in examples[:12]: print(e)
