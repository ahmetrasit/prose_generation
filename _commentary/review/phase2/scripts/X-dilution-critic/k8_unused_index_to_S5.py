# K8: size of A's per-surah "unused index" that S5 is supposed to read. Upper bound = the surah's total digest
# (bytes/2.0 tokens, A's own ratio); a plausible estimate assumes the ayah commentary cites 20-40% of digest items
# (Inference: A's digests have median 238 atomized items; v15/v13 prose cites tens of items per ayah).
import json, collections
d=json.load(open('/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/A-v5-step/out/all_digest_sizes.json'))
per=collections.defaultdict(lambda:[0,0])
for ref,b,lk,secs,*_ in d:
    s=int(ref.split(':')[0]); per[s][0]+=1; per[s][1]+=b
rows=sorted(per.items(),key=lambda x:-x[1][1])
print('surah ayat digest_total_tokens unused@60% unused@80%')
for s,(n,b) in rows[:10]+[(100,per[100]),(103,per[103]) if 103 in per else (1,per[1])]:
    t=b/2.0; print(s,n,int(t),int(t*.6),int(t*.8))
big=[s for s,(n,b) in per.items() if b/2.0*0.6>150000]
print('v5 surahs whose unused index (60% of digest) exceeds 150k tokens:',len(big),'of',len(per))
