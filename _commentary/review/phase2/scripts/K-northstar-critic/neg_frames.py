"""Negation/disclaimer frames per 1,000 words in existing finished readings (stand-ins for B's R_mem = cold arm,
R_lex = dict arm) and in v5 editorials if present. Also prints the dismissive sentences on the watch ayat.
Read-only."""
import glob,re,statistics,os
W='/Volumes/OZTURK/_projects/prose_generation/_commentary/v9/lines/work'
NEG=re.compile(r'değil|anlamına gelmez|söylemez|iddia etmez|eşitleme|kanıtlamaz|demek değildir|taşımaz',re.I)
for arm in ['w10-opus-cold','w10-opus-dict','w10-opus-package']:
    rates=[]
    for f in sorted(glob.glob(f'{W}/*/synth/{arm}/*.reading.tr.md')):
        t=open(f).read(); w=len(t.split()); n=len(NEG.findall(t)); rates.append(1000*n/max(1,w))
    if rates: print(f'{arm}: n={len(rates)} median neg/1k={statistics.median(rates):.1f} range {min(rates):.1f}-{max(rates):.1f}')
for ay in ['18_86','18_96','4_34']:
    for arm in ['w10-opus-cold']:
        for f in glob.glob(f'{W}/{ay}/synth/{arm}/*.reading.tr.md'):
            for s in re.split(r'(?<=[.!?])\s+',open(f).read()):
                if re.search(r'eşitleme|değildir|anlamına gelmez|taşımaz',s) and re.search(r'حم|hame|Hamie|nef|نفخ|ضرب|yolculuk|kök',s,re.I):
                    print(ay,arm,'|',s[:260])
