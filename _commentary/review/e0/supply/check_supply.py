#!/usr/bin/env python3
"""Evaluation only (never imported by build_supply.py): checks the built supply v0.

1. Watch-case ingredients (the named probes are evaluation inputs; nothing here feeds the build):
   29:38  s-b-l B010 with al-Jawhari's (Sihah) phrase, and the link from B010 to the spider root
   18:86  h-m-' uses 15:26 / 15:28 / 15:33 grouped under one construction
   18:96  n-f-kh uses grouped by construction (fi s-sur; fihi min ruh), and the s-w-y co-occurrence
   plus informative ingredient checks carried over from the Phase 2 probes (reported, not required).
2. Forbidden items (grep): verdict, grade and confidence labels, script presence verdicts, popularity labels,
   HFT section names, v15 scene ids (from the v15 inventory), the known brief contamination string, and North Star
   example phrases. Hits inside the script-authored text are failures; hits inside quoted source data are listed
   for the user with their context.
Writes checks.json next to this file and prints a summary.
"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get('SUPPLY_OUT') or os.path.join(HERE, 'out')
V15_INV = '/Volumes/OZTURK/_projects/prose_generation/_commentary/v15/data/frames_inventory.json'

DIAC = re.compile('[ؐ-ًؚ-ٰٟۖ-ۭـ]')


def fold(t):
    t = DIAC.sub('', t or '')
    return re.sub('[أإآٱ]', 'ا', t).replace('ى', 'ي').replace('ة', 'ه')


def read(ref):
    p = os.path.join(OUT, ref.replace(':', '_') + '.md')
    return open(p, encoding='utf-8').read() if os.path.exists(p) else ''


def section(md, letter):
    m = re.search(rf'^## {letter}\. .*?(?=^## [A-Z]\. |^## Files you may read|\Z)', md, re.S | re.M)
    return m.group(0) if m else ''


def block(sec, head_re):
    m = re.search(rf'^#### {head_re}.*?(?=^#### |^### |\Z)', sec, re.S | re.M)
    return m.group(0) if m else ''


def watch_checks():
    res = []
    md = read('29:38')
    b = [l for l in section(md, 'B').split('\n') if l.startswith('- root_000672/B010')]
    res.append(dict(ayah='29:38', item='s-b-l root_000672/B010 line with its Sihah phrase (spider weaving)',
                    ok=bool(b) and '(sihah)' in b[0] and 'نسج العنكبوت' in fold(b[0]), evidence=b[0][:300] if b else ''))
    c = [l for l in section(md, 'C').split('\n') if l.startswith('- root_000672/B010') and 'ع ن ك ب' in l]
    res.append(dict(ayah='29:38', item='link from root_000672/B010 to the spider root (ع ن ك ب)', ok=bool(c),
                    evidence=' || '.join(x[:300] for x in c)))
    md = read('18:86')
    blk = block(section(md, 'D'), 'ح م ء')
    grp = [l for l in blk.split('\n') if l.startswith('- ') and all(r in l for r in ('15:26', '15:28', '15:33'))]
    res.append(dict(ayah='18:86', item='h-m-\' uses 15:26, 15:28, 15:33 in one construction group',
                    ok=bool(grp), evidence=grp[0][:300] if grp else blk[:300]))
    md = read('18:96')
    d = section(md, 'D')
    blk = block(d, 'ن ف خ')
    sur = [l for l in blk.split('\n') if l.startswith('- ') and '(ص و ر)' in l]
    ruh = [l for l in blk.split('\n') if l.startswith('- ') and '(ر و ح)' in l]
    res.append(dict(ayah='18:96', item='n-f-kh uses grouped by construction: fi s-sur group',
                    ok=bool(sur) and len(re.findall(r'\d+:\d+', sur[0].split('—')[-1])) >= 10, evidence=sur[0][:300] if sur else ''))
    res.append(dict(ayah='18:96', item='n-f-kh uses grouped by construction: fihi min ruh group (15:29, 21:91, 32:9, 38:72, 66:12)',
                    ok=bool(ruh) and all(r in ruh[0] for r in ('15:29', '21:91', '32:9', '38:72', '66:12')),
                    evidence=ruh[0][:300] if ruh else ''))
    pair = [l for l in d.split('\n') if re.match(r'^- (س و ي \+ ن ف خ|ن ف خ \+ س و ي):', l)]
    res.append(dict(ayah='18:96', item='s-w-y and n-f-kh co-occurrence (15:29, 32:9, 38:72)',
                    ok=bool(pair) and all(r in pair[0] for r in ('15:29', '32:9', '38:72')), evidence=pair[0][:300] if pair else ''))
    return res


INFO = {  # carried over from the Phase 2 probe list (D's kapacket CHECKS); format-agnostic, informative only
    '1:6': [('sirat B002 swallowing (definition)', r'الغيبه في المرور'), ('qawm B012 device upright part', r'اله قايمه|آله قائمه|اله قائمه'),
            ('hady B003 the one ahead', r'المتقدم الهادي')],
    '4:34': [('4:128 husband\'s nushuz text in the page', r'خافت من ?بعلها'), ('nushuz phrase: husband harsh', r'نشز بعلها'),
             ('darb B002 travel with its construction phrase', r'root_000906/B002[^\n]*C\[')],
    '5:6': [('mirfaq leaning (irtifaq / ittika)', r'التوكو|الاتكا|ارتفق'), ('kaba B002 the square raised house', r'البيت المربع'),
            ('5:97 qiyaman text in the page', r'قيما للناس'), ('5:8 qawwamin text in the page', r'قومين لله|قوامين لله')],
    '18:86': [('the qiraa hamiya as an alternative root', r'### ح م ي'), ('ayn branch: the sun disk', r'عين الشمس|قرص الشمس')],
    '18:96': [('nafakha 3:49 / 5:110 uses', r'3:49[^0-9]'), ('21:91 and 66:12', r'21:91')],
    '29:38': [('ghishawa bridge beside basar (2:7, 45:23)', r'غشاوه[^\n]*2:7, 45:23'), ('sadd B013 kohl on a mirror', r'root_000848/B013'),
              ('29:41 spider-house text in the page', r'العنكبوت')],
}

LABELS = [
    ('confidence label', r'\bconfidence\b'), ('grade label', r'\bgrades?\b'), ('verdict', r'\bverdicts?\b'),
    ('no value', r'\bno value\b'), ('DEPARTS', r'DEPART'), ('presence verdict', r'present: ?(?:no|yes)|here: (?:present|not found)'),
    ('withheld', r'\bwithheld\b'), ('echo-tier label', r'echo only|echo tier|echo-tier'), ('popularity label', r'\[\d+ readings?\]|not used above'),
    ('score', r'\bscores?\b'), ('rank', r'\branks?\b|\branked\b'), ('loaded flag', r'loaded=|loaded: (?:true|false)'),
    ('strong/weak/reject', r'\bstrong\b|\bweak\b|\breject(?:ed)?\b'), ('HFT section names', r'surprising_valid_outliers|baseline_models|context_deltas|model_id|outlier_'),
    ('scene path/lens', r'scene path|scene lens|scene_other'), ('brief contamination string', r'\(15:26, 15:28, 15:33\)'),
]
NS_PHRASES = ["traveller's prayer", 'traveler\'s prayer', 'lead animal', 'eye disease', 'swallows its travellers', 'running horses',
              'the one who comes second', 'retention under compression', 'the thirsty hear water', 'way-marks', 'waymarks',
              'the herd led by its rabb', 'mud as human fabric', 'more than blowing the bellows']


def script_text_lines(md):
    """Lines the build script writes itself (section and subsection titles, legends), as opposed to quoted data.
    '#### ' headings carry data (channel-review titles, root names) and are not counted as script text."""
    out = []
    for l in md.split('\n'):
        if l.startswith('## ') or l.startswith('# ') or l.startswith('Branch lines follow') or l.startswith('Lenses:'):
            out.append(l)
        elif l.startswith('### ') and not re.match(r'### [\u0621-\u064a] ', l):
            out.append(l)
    return out


def forbidden(mds):
    inv = json.load(open(V15_INV, encoding='utf-8')) if os.path.exists(V15_INV) else {'frames': []}
    scene_ids = sorted({f['id'] for f in inv.get('frames', [])}, key=len, reverse=True)
    res = []
    ns_re = re.compile('|'.join(re.escape(p) for p in NS_PHRASES), re.I)
    for ref, md in mds.items():
        own = '\n'.join(script_text_lines(md))
        if not ns_re.search(md):
            pass
        for name, pat in LABELS:
            for m in re.finditer(pat, md, re.I):
                ctx = md[max(0, m.start() - 90):m.end() + 60].replace('\n', ' ')
                res.append(dict(ayah=ref, kind=name, match=m.group(0), in_script_text=bool(re.search(pat, own, re.I)),
                                context=ctx))
        for sid in scene_ids:
            if sid in md and re.search(r'(?<![\w.])' + re.escape(sid) + r'(?![\w.])', md):
                res.append(dict(ayah=ref, kind='v15 scene id', match=sid, in_script_text=sid in own, context=''))
        low = md.lower()
        for ph in NS_PHRASES:
            i = low.find(ph.lower())
            if i >= 0:
                res.append(dict(ayah=ref, kind='North Star example phrase', match=ph, in_script_text=ph.lower() in own.lower(),
                                context=md[max(0, i - 120):i + 80].replace('\n', ' ')))
    return res


def main():
    refs = sorted({os.path.basename(p)[:-3].replace('_', ':') for p in glob.glob(os.path.join(OUT, '*.md'))},
                  key=lambda r: tuple(map(int, r.split(':'))))
    mds = {r: read(r) for r in refs}
    pulls = {r: open(os.path.join(OUT, r.replace(':', '_') + '.pull.json'), encoding='utf-8').read() for r in refs
             if os.path.exists(os.path.join(OUT, r.replace(':', '_') + '.pull.json'))}
    w = watch_checks()
    info = []
    for ref, items in INFO.items():
        t = fold(mds.get(ref, ''))
        for name, pat in items:
            info.append(dict(ayah=ref, item=name, ok=bool(re.search(fold(pat), t))))
    fb = forbidden(mds)
    fbp = forbidden(pulls)
    ent = {os.path.basename(p): open(p, encoding='utf-8').read() for p in glob.glob(os.path.join(HERE, 'entries', '*.md'))}
    fbe = [x for x in forbidden(ent) if x['kind'] not in ('North Star example phrase',)]
    out = dict(watch=w, informative=info, forbidden_in_pages=fb, forbidden_in_pull=fbp, forbidden_in_entries=fbe)
    json.dump(out, open(os.path.join(HERE, 'checks.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('watch-case ingredients:')
    for x in w:
        print(f"  [{'x' if x['ok'] else ' '}] {x['ayah']} {x['item']}")
    print('informative (Phase 2 probe list):')
    for x in info:
        print(f"  [{'x' if x['ok'] else ' '}] {x['ayah']} {x['item']}")
    for name, rows in (('pages', fb), ('pull files', fbp), ('entries files', fbe)):
        own = [x for x in rows if x['in_script_text']]
        print(f"forbidden-item hits in {name}: {len(rows)} in quoted data/fields, of which in script-authored text: {len(own)}")
        by = {}
        for x in rows:
            by.setdefault((x['kind'], x['match'].lower()), 0)
            by[(x['kind'], x['match'].lower())] += 1
        for k, v in sorted(by.items(), key=lambda kv: -kv[1])[:25]:
            print(f"    {v:5d}  {k[0]}: {k[1]}")
    return 0 if all(x['ok'] for x in w) and not any(x['in_script_text'] for x in fb + fbp) else 1


if __name__ == '__main__':
    sys.exit(main())
