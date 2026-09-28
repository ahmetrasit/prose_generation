import re,glob,sys
for f in sorted(glob.glob(sys.argv[1])):
    t=open(f,encoding='utf-8').read()
    m=re.search(r'(?ms)^### Chains\s*\n(.*?)(?=^### |\Z)',t)
    if not m: print(f,'no chains'); continue
    lines=[l for l in m.group(1).splitlines() if l.startswith('- ')]
    low=[l.lower() for l in lines]
    def c(*ks): return sum(1 for l in low if any(k in l for k in ks))
    print(f.split('/')[-1], 'chains lines',len(lines), 'holds',c('tutar','holds','geçerli'), 'corrected',c('düzelt','corrected'), 'not hold', c('tutmaz','does not hold','geçmez','tutmuyor'))
