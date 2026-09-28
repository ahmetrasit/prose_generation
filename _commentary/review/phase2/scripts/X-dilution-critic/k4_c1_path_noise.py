# K4: how much of C1's pushed evidence ("N kinds" + typed paths) rests on generic lemmas?
# Counts path segments in all harvest2/*.push.md whose bridge lemma is one of C1's own named noise words
# (الشيء, الناس, بينهما; plus near-variants) and branch lines whose displayed "N kinds" includes such a path.
import glob, re, collections
H='/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/scratchpad/phase2/C1-branch-distance/harvest2'
GEN=re.compile(r'«(ال|لل|وال|بال)?(شيء|شيي|شي|ناس|بينهما)»')
c=collections.Counter()
for p in sorted(glob.glob(H+'/*.push.md')):
    for l in open(p,encoding='utf-8'):
        m=re.match(r'\s+- (B\d+) .*?\] (\d+) kinds',l)
        if not m: continue
        segs=[s for s in re.split(r' \| |: ',l) if 'Quran pairs' in s or 'names «' in s]
        g=[s for s in segs if GEN.search(s)]
        c['lines']+=1; c['paths']+=l.count(' | ')+1; c['lemma_paths']+=len(segs); c['generic_paths']+=len(g)
        if g: c['lines_with_generic']+=1
print(dict(c))
print(f"branch lines whose displayed evidence includes a generic-lemma path: {c['lines_with_generic']}/{c['lines']} ({c['lines_with_generic']/c['lines']:.0%})")
print(f"generic-lemma paths among lexical-bridge/names paths: {c['generic_paths']}/{c['lemma_paths']} ({c['generic_paths']/max(1,c['lemma_paths']):.0%})")
