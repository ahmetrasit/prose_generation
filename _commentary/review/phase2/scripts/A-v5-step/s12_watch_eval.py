# Evaluation only: where do watch-case ingredients appear in the prototype digests (section letters)?
import re, os
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'out','digests')
def secs(fn):
    t=open(os.path.join(D,fn)).read(); out={}; cur='head'
    for l in t.split('\n'):
        if l.startswith('## '): cur=l[3:6].strip('. '); continue
        out.setdefault(cur,[]).append(l)
    return out
W=[('29_38','eye film branch س ب ل B010',r'س ب ل (r0672/)?B010'),('29_38','eye film ↔ spider 29:41 (definitional)',r'B010.*عنكبوت.*29:41'),
   ('29_38','kohl branch of ṣadda (ص د د B013)',r'ص د د (r0848/)?B013'),('29_38','eye film ~ kohl pair',r'س ب ل B010.*ص د د B013|ص د د B013.*س ب ل B010'),
   ('29_38','zayyana adorning branch (ز ي ن B002)',r'ز ي ن (r0660/)?B002'),
   ('18_86','ḥamaʾ creation passages 15:26/28/33',r'15:26.*15:28.*15:33'),('18_86','ḥamaʾ ~ ṣalṣāl co-occurrence',r'ح م ء.*ص ل ص ل'),
   ('18_86','ʿayn = sun disk (ع ي ن B008)',r'ع ي ن (r1069/)?B008'),
   ('18_96','nafakha concordance with spirit (ر و ح)',r'ن ف خ.*ر و ح'),('18_96','15:29/38:72/32:9 listed',r'15:29.*32:9.*38:72'),
   ('1_2','waymark ع ل م B002',r'ع ل م (r1040/)?B002'),('1_2','ʿaylam well ع ل م B005',r'ع ل م (r1040/)?B005'),('1_2','herd ر ب ب B014',r'ر ب ب (r0532/)?B014'),('1_2','gathered water ر ب ب B013',r'ر ب ب (r0532/)?B013'),
   ('1_4','road middle م ل ك B006',r'م ل ك (r1444/)?B006'),('1_4','lead animal م ل ك B008 [collocation]',r'م ل ك (r1444/)?B008'),
   ('1_5','trodden road ع ب د B005',r'ع ب د (r0973/)?B005'),
   ('1_6','swallowing ص ر ط B002',r'ص ر ط (r0858/)?B002'),('1_6','well frame ق و م B012',r'ق و م (r1273/)?B012'),('1_6','leaning gait ه د ي B008',r'ه د ي (r1583/)?B008'),
   ('1_7','stray ض ل ل B005',r'ض ل ل (r0913/)?B005'),('1_7','stray ↔ rabb 1:2 (definitional)',r'ض ل ل B005.*رب.*1:2'),('1_7','stray ~ livestock pair',r'ض ل ل B005.*ن ع م B005'),
   ('5_6','mirfaq leaning ر ف ق B004',r'ر ف ق (r0\d+/)?B004'),('5_6','kaʿb ↔ Kaʿba 5:95/5:97',r'كعب.*5:9[57]|ك ع ب.*5:97'),('5_6','qiyām ↔ qawwāmīn 5:8',r'5:8'),
   ('100_1','ḍabḥ running/breath branches',r'ض ب ح'),('103_1','ʿaṣr branches (ع ص ر)',r'ع ص ر')]
for fn,label,rx in W:
    S=secs(fn+'.digest.md'); where=[k for k,v in S.items() if any(re.search(rx,l) for l in v)]
    print(f"{fn.replace('_',':'):6s} {label:45s} -> {','.join(where) if where else 'ABSENT'}")
