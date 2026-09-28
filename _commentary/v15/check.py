#!/usr/bin/env python3
"""v15 checks (scripts only, no model calls).

  record --ref S:A        anchors exist (word, root, branch), triggers exist, containment wording
  window --surah S        image members exist; plan covers every ayah within the image limit
  prose --ref S:A         length against the budget; every {{ar:…}} quotation resolved to a source
                          -> out/sNNN/S_A/commentary.tagged.tr.md
  surah-prose --surah S   sources for the surah commentary -> out/sNNN/surah.tagged.tr.md
"""
import argparse
import os
import re
import sys

import build
import lib
from lib import CFG, OUT

NOT_BUT = re.compile(r"\bnot\b[^.;:]{0,80}\bbut\b|\brather than\b|\binstead of\b", re.I)


def word_by_ref():
    return {w['ref']: w for ws in lib.words().values() for w in ws}


def valid_ref(ref):
    parts = ref.split(':')
    if len(parts) == 2:
        return ref in lib.quran()
    if len(parts) == 3:
        return ref in word_by_ref()
    return False


def roots_for(wd):
    return {r for r, _, _, _ in build.word_roots(wd)}


def check_member(m, words_idx, bk, problems, where):
    ref, root, br = m.get('ref', ''), m.get('root', ''), m.get('branch', '')
    wd = words_idx.get(ref)
    if not wd:
        problems.append(f"{where}: word {ref} does not exist")
        return
    if root and root not in roots_for(wd):
        problems.append(f"{where}: {ref} {wd['surface']} does not carry root {root} (has {sorted(roots_for(wd))})")
    if br and f'{root} {br}' not in bk:
        problems.append(f"{where}: branch {root} {br} is not in the dictionary")


def check_record(ref):
    s, a = [int(x) for x in ref.split(':')]
    rec = lib.read_json(os.path.join(build.out_ayah_dir(s, a), 'record.json'))
    words_idx, bk = word_by_ref(), lib.branch_by_key()
    problems, notes = [], []
    counts = {'lead': 0, 'support': 0, 'record': 0}
    for f in rec.get('findings', []):
        fid = f.get('id', '?')
        an = f.get('anchor', {})
        if f.get('kind') not in ('grammar', 'variant') or an.get('branch'):
            check_member(an, words_idx, bk, problems, f"{fid} anchor")
        for t in f.get('triggers', []):
            if t.get('ref') and not valid_ref(t['ref']):
                problems.append(f"{fid} trigger: {t['ref']} does not exist")
        if NOT_BUT.search(f.get('statement', '')):
            notes.append(f"{fid} statement may break containment: {f['statement'][:140]}")
        if f.get('memory'):
            notes.append(f"{fid} rests on memory (not in the dictionary)")
        counts[f.get('for_prose', 'record')] = counts.get(f.get('for_prose', 'record'), 0) + 1
    print(f"{ref}: {len(rec.get('findings', []))} findings {counts}; {len(rec.get('set_aside', []))} set aside; "
          f"{len(rec.get('losses', []))} losses; {len(rec.get('loaded_words', []))} loaded words")
    for p in problems:
        print('  PROBLEM', p)
    for n in notes:
        print('  note', n)
    return not problems


def check_window(s):
    words_idx, bk = word_by_ref(), lib.branch_by_key()
    ok = True
    for lo, hi, _ in lib.windows_of_surah(s):
        p = os.path.join(build.out_window_dir(s, lo, hi), 'window.json')
        if not os.path.exists(p):
            continue
        w = lib.read_json(p)
        problems = []
        ids = {i['id'] for i in w.get('images', [])}
        for im in w.get('images', []):
            for m in im.get('members', []):
                check_member(m, words_idx, bk, problems, f"{im['id']} member")
        planned = {x['ayah'] for x in w.get('plan', [])}
        for a in range(lo, hi + 1):
            if f'{s}:{a}' not in planned:
                problems.append(f"plan: {s}:{a} missing")
        for x in w.get('plan', []):
            placed = x.get('opens', []) + x.get('advances', []) + x.get('completes', [])
            if len(placed) > CFG['prose']['max_images_per_ayah']:
                problems.append(f"plan: {x['ayah']} places {len(placed)} images")
            for iid in placed:
                if iid not in ids:
                    problems.append(f"plan: {x['ayah']} names unknown image {iid}")
        print(f"window {s}:{lo}-{hi}: {len(ids)} images, {len(w.get('concepts', []))} concepts, "
              f"{len(w.get('other_activations', []))} other activations")
        for p_ in problems:
            print('  PROBLEM', p_)
        ok = ok and not problems
    return ok


# ------------------------------------------------------------------ sources for Arabic quotations

AR = re.compile(r'\{\{ar:([^}|]+)\}\}')


def resolve(text, s, a, cited):
    sk = lib.skeleton(text).replace(' ', '')
    if not sk:
        return None
    lo, hi = lib.local_range(s, a)
    order = [a] + [x for x in range(lo, hi + 1) if x != a]
    for x in order:
        toks = lib.tokens(f'{s}:{x}')
        for i, t in enumerate(toks, 1):
            if sk == lib.skeleton(t).replace(' ', ''):
                return f'{s}:{x}:{i}'
        joined = lib.skeleton(' '.join(toks)).replace(' ', '')
        if len(sk) > 3 and sk in joined:
            return f'{s}:{x}'
    for key in cited:
        b = lib.branch_by_key().get(key)
        if b and sk in lib.skeleton(b['image'] + b['what_is'] + b['source_phrase']).replace(' ', ''):
            return key
    for ref, t in lib.quran().items():
        if len(sk) > 4 and sk in lib.skeleton(t).replace(' ', ''):
            return ref
    for wd in lib.words()[f'{s}:{a}']:
        for root in roots_for(wd):
            for b in lib.branches().get(root, []):
                if len(sk) > 3 and sk in lib.skeleton(b['image'] + b['what_is'] + b['source_phrase']).replace(' ', ''):
                    return f"{root} {b['branch']}"
    return None


def tag(path, s, a, cited):
    with open(path, encoding='utf-8') as f:
        text = f.read()
    unresolved = []

    def sub(m):
        src = resolve(m.group(1), s, a, cited)
        if not src:
            unresolved.append(m.group(1))
            return '{{ar:' + m.group(1) + '|src:?}}'
        return '{{ar:' + m.group(1) + '|src:' + src + '}}'
    tagged = AR.sub(sub, text)
    out = path.replace('.tr.md', '.tagged.tr.md')
    lib.write_text(out, tagged)
    n = len(AR.findall(text))
    words = len(AR.sub('', text).split())
    return n, unresolved, words, out


def check_prose(ref):
    s, a = [int(x) for x in ref.split(':')]
    o = build.out_ayah_dir(s, a)
    rec = lib.read_json(os.path.join(o, 'record.json'))
    cited = [f"{f['anchor']['root']} {f['anchor']['branch']}" for f in rec.get('findings', [])
             if f.get('anchor', {}).get('branch')]
    n, unresolved, words, out = tag(os.path.join(o, 'commentary.tr.md'), s, a, cited)
    t, cap = CFG['prose']['ayah_words_target'], CFG['prose']['ayah_words_cap']
    flag = 'OVER CAP' if words > cap else ('over target' if words > t else 'ok')
    print(f"{ref}: {words} words (target {t}, cap {cap}: {flag}); {n} Arabic quotations, "
          f"{n - len(unresolved)} sourced -> {os.path.relpath(out, lib.HERE)}")
    for u in unresolved:
        print('  unresolved:', u)
    return words <= cap and not unresolved


def check_surah_prose(s):
    p = os.path.join(OUT, f's{s:03d}', 'surah.tr.md')
    cited = []
    for a in range(1, lib.surah_len(s) + 1):
        rp = os.path.join(build.out_ayah_dir(s, a), 'record.json')
        if os.path.exists(rp):
            cited += [f"{f['anchor']['root']} {f['anchor']['branch']}" for f in lib.read_json(rp).get('findings', [])
                      if f.get('anchor', {}).get('branch')]
    n, unresolved, words, out = tag(p, s, 1, cited)
    print(f"surah {s}: {words} words; {n} Arabic quotations, {n - len(unresolved)} sourced -> {os.path.relpath(out, lib.HERE)}")
    for u in unresolved:
        print('  unresolved:', u)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cmd')
    ap.add_argument('--ref')
    ap.add_argument('--surah', type=int)
    x = ap.parse_args()
    if x.cmd == 'record':
        check_record(x.ref)
    elif x.cmd == 'window':
        check_window(x.surah)
    elif x.cmd == 'prose':
        check_prose(x.ref)
    elif x.cmd == 'surah-prose':
        check_surah_prose(x.surah)
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main()
