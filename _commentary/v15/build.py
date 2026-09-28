#!/usr/bin/env python3
"""v15 builder (scripts only, no model calls).

  base                      derive data/words.tsv, branches.tsv, lemmas.tsv, quran.tsv
  jobs frames|loanwords|profiles --surahs 1,100
                            write Luna job inputs for what the scope still lacks
  jobs frames --sample 120 --exclude 1,100,103,5:6
                            scene-tag jobs for a random sample of branches (inventory coverage test)
  pull --surahs 1,100       write per-root classical entries and per-lemma concordances
  window --surah S          packet for the window reading (whole short surah or one pericope)
  ayah --ref S:A            packet for the ayah reading
  evidence --ref S:A        packet for Luna's evidence pass (needs out/.../record.json)
  write --ref S:A           packet for the Turkish commentary (needs record + evidence)
  surah --surah S           packet for the surah commentary (needs all ayah records)
  sizes --surahs 1,100      character sizes of every packet present
"""
import argparse
import glob
import hashlib
import json
import os
import random
import re
import sys
from collections import Counter, defaultdict

import lib
from lib import CFG, DATA, WORK, OUT

# ============================================================== base tables


def build_base():
    q = lib.quran()
    lib.write_tsv(os.path.join(DATA, 'quran.tsv'),
                  [{'ref': r, 'text': t} for r, t in q.items()], ['ref', 'text'])

    # words: every word of every ayah, with QAC roots/lemmas where the word has a root
    rows = lib.read_tsv(lib.src('root_ayah'))
    per = defaultdict(lambda: defaultdict(lambda: {'roots': [], 'lemmas': [], 'pos': []}))
    mismatched = 0
    lem = defaultdict(list)
    for r in rows:
        ref = r['ayah_ref']
        toks = lib.tokens(ref)
        idxs = r['word_indices'].split(';')
        for wi, surf in zip(idxs, r['surfaces_ar'].split(';')):
            i = int(wi) - 1
            if not (i < len(toks) and lib.skeleton(surf) in lib.skeleton(toks[i])):
                mismatched += 1
        lems = r['lemmas_ar'].split(';')
        poss = r['pos_tags'].split(';')
        for i, wi in enumerate(idxs):
            w = int(wi)
            d = per[ref][w]
            if r['root_norm'] not in d['roots']:
                d['roots'].append(r['root_norm'])
                d['lemmas'].append(lems[i] if i < len(lems) else '')
                d['pos'].append(poss[i] if i < len(poss) else '')
            lem[(r['root_norm'], lems[i] if i < len(lems) else '')].append(f'{ref}:{w}')
    out = []
    for ref in q:
        s, a = ref.split(':')
        for w, surface in enumerate(lib.tokens(ref), 1):
            d = per[ref].get(w, {'roots': [], 'lemmas': [], 'pos': []})
            out.append({'surah': s, 'ayah': a, 'w': w, 'ref': f'{ref}:{w}', 'surface': surface,
                        'roots': '|'.join(d['roots']), 'lemmas': '|'.join(d['lemmas']), 'pos': '|'.join(d['pos'])})
    lib.write_tsv(os.path.join(DATA, 'words.tsv'), out,
                  ['surah', 'ayah', 'w', 'ref', 'surface', 'roots', 'lemmas', 'pos'])

    def refkey(x):
        return [int(p) for p in x.split(':')]
    lib.write_tsv(os.path.join(DATA, 'lemmas.tsv'),
                  [{'root': k[0], 'lemma': k[1], 'count': len(v), 'refs': ';'.join(sorted(set(v), key=refkey))}
                   for k, v in sorted(lem.items())], ['root', 'lemma', 'count', 'refs'])

    # branches: Furuq branch table + Turkish concept gloss from the Turkish dictionary entries
    tr = {}
    tr_branch = {}
    for p in glob.glob(lib.src('tr_entries_glob')):
        try:
            d = lib.read_json(p)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        for b in d.get('branches', []):
            ref = b.get('branch_ref', '')
            if '/' not in ref:
                continue
            key = tuple(ref.split('/'))
            tr_branch[key] = b
            g = (b.get('concept_gloss') or {}).get('text')
            if g:
                tr[key] = g
    brows = []
    for r in lib.read_tsv(lib.src('branches')):
        brows.append({'root': r['surface_root'], 'branch': r['branch_id'], 'root_id': r['source_root_id'],
                      'image': r['branch_image_ar'], 'what_is': r['what_is_ar'],
                      'source_phrase': r['source_phrase_ar'], 'qac_attested': r['qac_attested'],
                      'subset': r['subset_class'], 'tr_gloss': tr.get((r['source_root_id'], r['branch_id']), '')})
    # the Turkish dictionary (the reader app's dictionary) attests branches the Furuq table lacks: add them
    have_b = {(r['root_id'], r['branch']) for r in brows}
    root_of = {r['root_id']: r['root'] for r in brows}

    def flat(v):
        return '؛ '.join(str(x) for x in v) if isinstance(v, list) else (v or '')
    added = 0
    for (rid, bid), b in tr_branch.items():
        if (rid, bid) in have_b or rid not in root_of:
            continue
        brows.append({'root': root_of[rid], 'branch': bid, 'root_id': rid, 'image': flat(b.get('branch_image_ar')),
                      'what_is': flat(b.get('what_is_ar')), 'source_phrase': flat(b.get('source_phrase_ar')),
                      'qac_attested': 'yes', 'subset': 'tr_entry_only', 'tr_gloss': tr.get((rid, bid), '')})
        added += 1
    brows.sort(key=lambda r: (r['root'], int(re.sub(r'\D', '', r['branch']) or 0)))
    lib.write_tsv(os.path.join(DATA, 'branches.tsv'), brows,
                  ['root', 'branch', 'root_id', 'image', 'what_is', 'source_phrase', 'qac_attested', 'subset', 'tr_gloss'])
    print(f"branches added from the Turkish dictionary (absent from the Furuq table): {added}")

    roots_used = {x for r in out for x in r['roots'].split('|') if x}
    have = {b['root'] for b in brows}
    print(f"quran.tsv {len(q)} ayat; words.tsv {len(out)} words; lemmas.tsv {len(lem)} lemmas; "
          f"branches.tsv {len(brows)} branches ({sum(1 for b in brows if b['tr_gloss'])} with Turkish gloss)")
    print(f"rooted occurrences not matching their word: {mismatched}; "
          f"QAC roots without branches: {sorted(roots_used - have)}")


# ============================================================== scope helpers


def parse_surahs(spec):
    out = []
    for part in spec.split(','):
        if '-' in part:
            lo, hi = part.split('-')
            out += list(range(int(lo), int(hi) + 1))
        elif part:
            out.append(int(part))
    return out


def ayah_words(ref):
    return lib.words()[ref]


def word_roots(wd):
    """(root, lemma, is_alt, reason) for a word: its own roots, then alternatives."""
    out = []
    roots = [x for x in wd['roots'].split('|') if x]
    lems = wd['lemmas'].split('|')
    for i, r in enumerate(roots):
        lemma = lems[i] if i < len(lems) else ''
        out.append((r, lemma, False, ''))
        for alt, why in lib.alternative_roots(wd['ref'], r, lemma, wd['surface']):
            out.append((alt, lemma, True, why))
    return out


def scope_roots(surahs):
    roots = set()
    for s in surahs:
        for ref in lib.refs_of_surah(s):
            for wd in ayah_words(ref):
                for r, _, _, _ in word_roots(wd):
                    roots.add(r)
    return roots


def scope_lemmas(surahs):
    out = set()
    for s in surahs:
        for ref in lib.refs_of_surah(s):
            for wd in ayah_words(ref):
                for r, lemma, alt, _ in word_roots(wd):
                    if not alt and lemma:
                        out.add((r, lemma))
    return out


def safe(name):
    return re.sub(r'\s+', '', lib.skeleton(name)) + '_' + hashlib.sha1(name.encode()).hexdigest()[:6]


# ============================================================== Luna job inputs


def qnet_hints():
    p = lib.src('qnet_keywords')
    out = defaultdict(list)
    if os.path.exists(p):
        for r in lib.read_tsv(p):
            if r['keyword_type'] == 'core':
                out[(r['root_id'], r['branch_id'])].append(r['keyword'])
    return out


def excluded_roots(spec):
    """Roots occurring in the excluded scope: surahs ('1'), ayat ('5:6') or ayah ranges ('29:39-45')."""
    refs = []
    for part in (spec or '').split(','):
        part = part.strip()
        if not part:
            continue
        if ':' not in part:
            refs += lib.refs_of_surah(int(part))
        else:
            s, a = part.split(':')
            lo, hi = a.split('-') if '-' in a else (a, a)
            refs += [f'{s}:{x}' for x in range(int(lo), int(hi) + 1)]
    return {r for ref in refs for wd in ayah_words(ref) for r, _, _, _ in word_roots(wd)}


def jobs_frames(surahs, sample=None, seed=15, exclude=None):
    """Scene-tag jobs for every untagged branch of the scope's roots, or for a random sample of
    branches from the whole Quran outside an excluded scope (a coverage test of the inventory)."""
    have = lib.frames()
    hints = qnet_hints()
    if sample:
        skip = excluded_roots(exclude)
        pool = [r for r in sorted(scope_roots(range(1, 115))) if r not in skip]
    else:
        pool = sorted(scope_roots(surahs))
    todo = []
    for root in pool:
        for b in lib.branches().get(root, []):
            key = f"{root} {b['branch']}"
            if key not in have:
                todo.append((key, b))
    pending = set()
    for p in glob.glob(os.path.join(DATA, 'frames', 'jobs', '*', 'keys.json')):
        pending |= set(lib.read_json(p))
    todo = [t for t in todo if t[0] not in pending]
    if sample:
        todo = random.Random(seed).sample(todo, min(sample, len(todo)))
    n = CFG['jobs']['frames_per_job']
    made = 0
    for i in range(0, len(todo), n):
        batch = todo[i:i + n]
        jid = ('frames_sample_' if sample else 'frames_') + hashlib.sha1('|'.join(k for k, _ in batch).encode()).hexdigest()[:10]
        lines = []
        for key, b in batch:
            h = ', '.join(hints.get((b['root_id'], b['branch']), [])[:8])
            lines.append(f"- {key} | {b['image']} | {b['what_is']} | {b['source_phrase'][:320]}"
                         + (f" | hints: {h}" if h else ''))
        d = os.path.join(DATA, 'frames', 'jobs', jid)
        lib.write_text(os.path.join(d, 'input.md'),
                       f"# Branches to tag ({len(batch)})\n\nkey | image | definition | classical phrases | hints\n\n"
                       + '\n'.join(lines) + '\n')
        lib.write_json(os.path.join(d, 'keys.json'), [k for k, _ in batch])
        lib.write_json(os.path.join(d, 'job.json'), {'kind': 'frames', 'prompt': 'luna_frames.md',
                                                     'schema': 'frames.schema.json',
                                                     'extra': ['data/frames_inventory.json'],
                                                     'out': f'data/frames/out/{jid}.json'})
        made += 1
    print(f"frames: {len(todo)} branches need tags -> {made} new jobs")


def trim(text, limit):
    if not limit or len(text) <= limit:
        return text
    cut = text[:limit].rsplit(' ', 1)[0]
    return cut + ' …'


_ROOT_USES = {}


def root_uses(root):
    if not _ROOT_USES:
        for (r, _), v in lib.lemmas().items():
            _ROOT_USES[r] = _ROOT_USES.get(r, 0) + len(v)
    return _ROOT_USES.get(root, 0)


def root_index_lines(root, limit=None, tr=True, image_only=False):
    """One line per branch: id | image | definition (| Turkish gloss). Never drops a branch."""
    out = []
    for b in lib.branches().get(root, []):
        line = f"{b['branch']} | {b['image']}"
        if not image_only:
            line += f" | {trim(re.sub(r'^يدخل فيه\s*', '', b['what_is']), limit)}"
        if tr and b['tr_gloss']:
            line += f" | tr: {b['tr_gloss']}"
        out.append(line)
    return out


def jobs_loanwords(surahs):
    have = lib.loanword_cards()
    todo = sorted(k for k in scope_lemmas(surahs) if f'{k[0]}|{k[1]}' not in have)
    n = CFG['jobs']['lemmas_per_loanword_job']
    made = 0
    for i in range(0, len(todo), n):
        batch = todo[i:i + n]
        jid = 'loan_' + hashlib.sha1('|'.join(f'{r}|{l}' for r, l in batch).encode()).hexdigest()[:10]
        d = os.path.join(DATA, 'loanwords', 'jobs', jid)
        if os.path.exists(d):
            continue
        parts = []
        for root, lemma in batch:
            parts.append(f"## {lemma} — root {root}\n" + '\n'.join(root_index_lines(root, 160)))
        lib.write_text(os.path.join(d, 'input.md'), f"# Lemmas ({len(batch)})\n\n" + '\n\n'.join(parts) + '\n')
        lib.write_json(os.path.join(d, 'job.json'), {'kind': 'loanwords', 'prompt': 'luna_loanwords.md',
                                                     'schema': 'loanwords.schema.json', 'extra': [],
                                                     'out': f'data/loanwords/out/{jid}.json'})
        made += 1
    print(f"loanwords: {len(todo)} lemmas need cards -> {made} new jobs")


def jobs_profiles(surahs):
    have = lib.profiles()
    lem = lib.lemmas()
    todo = sorted(k for k in scope_lemmas(surahs)
                  if len(lem.get(k, [])) >= CFG['jobs']['profile_min_uses'] and f'{k[0]}|{k[1]}' not in have)
    made = 0
    for root, lemma in todo:
        jid = 'prof_' + safe(root + '_' + lemma)
        d = os.path.join(DATA, 'profiles', 'jobs', jid)
        if os.path.exists(d):
            continue
        refs = lem[(root, lemma)]
        cap = CFG['jobs']['profile_sample_max']
        shown = refs if len(refs) <= cap else [refs[int(i * len(refs) / cap)] for i in range(cap)]
        head = (f"# {lemma} — root {root} — {len(refs)} uses"
                + (f" (an evenly spaced sample of {len(shown)} is listed; give counts for the sample and say so)"
                   if len(shown) < len(refs) else ''))
        lines = [f"- {r} {lib.kwic(r, 6)}" for r in shown]
        lib.write_text(os.path.join(d, 'input.md'), head + '\n\n' + '\n'.join(lines) + '\n')
        lib.write_json(os.path.join(d, 'job.json'), {'kind': 'profiles', 'prompt': 'luna_profiles.md',
                                                     'schema': 'profiles.schema.json', 'extra': [],
                                                     'out': f'data/profiles/out/{jid}.json',
                                                     'root': root, 'lemma': lemma, 'uses': len(refs)})
        made += 1
    print(f"profiles: {len(todo)} lemmas with >= {CFG['jobs']['profile_min_uses']} uses need profiles -> {made} new jobs")


# ============================================================== pull files


def build_pull(surahs):
    ids = {b['root']: b['root_id'] for rs in lib.branches().values() for b in rs}
    n_e = n_k = 0
    for root in sorted(scope_roots(surahs)):
        dst = os.path.join(DATA, 'entries', root.replace(' ', '') + '.md')
        if os.path.exists(dst) or root not in ids:
            continue
        p = os.path.join(lib.PROJECTS, CFG['sources']['root_packets_dir'], ids[root] + '.json')
        if not os.path.exists(p):
            continue
        d = lib.read_json(p)
        parts = [f"# {root} — classical entries (full text)\n"]
        for s in d.get('dictionary_sources', []):
            t = (s.get('entry_text_clean') or '').strip()
            if t and t != '-':
                parts.append(f"## {s.get('source_id')}\n{t}\n")
        lib.write_text(dst, '\n'.join(parts))
        n_e += 1
    lem = lib.lemmas()
    for root, lemma in sorted(scope_lemmas(surahs)):
        refs = lem.get((root, lemma), [])
        if len(refs) <= CFG['concordance']['kwic_max_uses']:
            continue
        dst = os.path.join(DATA, 'kwic', safe(root + '_' + lemma) + '.md')
        if os.path.exists(dst):
            continue
        lib.write_text(dst, f"# {lemma} — root {root} — {len(refs)} uses\n\n"
                       + '\n'.join(f"- {r} {lib.kwic(r)}" for r in refs) + '\n')
        n_k += 1
    print(f"pull files: {n_e} root entry files, {n_k} concordance files")


# ============================================================== packet sections


def text_block(s, lo, hi, focus=None):
    out = []
    for a in range(lo, hi + 1):
        mark = '  ◀ focus' if focus == a else ''
        out.append(f"{s}:{a}| {lib.quran()[f'{s}:{a}']}{mark}")
    return '\n'.join(out)


def words_block(refs):
    out = []
    for ref in refs:
        for wd in ayah_words(ref):
            if wd['roots']:
                out.append(f"{wd['ref']} {wd['surface']} | {wd['roots']} | {wd['lemmas']} | {wd['pos']}")
    return '\n'.join(out)


def dictionary_block(refs):
    """Every branch of every root of the given ayat (own roots first, then alternatives)."""
    uses = defaultdict(list)
    alts = {}
    order = []
    for ref in refs:
        for wd in ayah_words(ref):
            for root, lemma, alt, why in word_roots(wd):
                if root not in uses:
                    order.append(root)
                uses[root].append(f"{wd['ref']} {wd['surface']}")
                if alt:
                    alts[root] = why
    out = []
    for root in order:
        n = root_uses(root)
        common = n > CFG['concordance']['image_only_above_uses']
        head = (f"### {root}" + (f" ~alt ({alts[root]})" if root in alts else '')
                + f" — {n} uses; here: " + '; '.join(dict.fromkeys(uses[root]))
                + (" (frequent root: images only; definitions in branches.tsv)" if common else ''))
        lines = root_index_lines(root, CFG['concordance']['definition_chars'], tr=False,
                                 image_only=common) or ['(no branches in the dictionary)']
        out.append(head + '\n' + '\n'.join(lines))
    return '\n\n'.join(out)


def scene_members(refs):
    fr = lib.frames()
    members = defaultdict(list)
    for ref in refs:
        for wd in ayah_words(ref):
            for root, lemma, alt, _ in word_roots(wd):
                for b in lib.branches().get(root, []):
                    for frame, role in fr.get(f"{root} {b['branch']}", []):
                        members[frame].append((wd['ref'], wd['surface'], root, b['branch'], role, alt))
    return members


def scene_lines(refs, focus_refs=None, min_words=2):
    focus = {wd['ref'] for r in (focus_refs or []) for wd in ayah_words(r)}
    lines = []
    for frame, ms in scene_members(refs).items():
        ws = {m[0] for m in ms}
        if len(ws) < min_words or (focus and not ws & focus):
            continue
        roles = {m[4] for m in ms}
        byw = defaultdict(list)
        for m in ms:
            byw[(m[0], m[1])].append(f"{m[2]}{'~alt' if m[5] else ''} {m[3]} {m[4]}")
        parts = [f"{w[1]} {w[0]}: " + ', '.join(dict.fromkeys(v)) for w, v in
                 sorted(byw.items(), key=lambda x: [int(p) for p in x[0][0].split(':')])]
        label = frame
        if frame.startswith('new.') and frame in lib.new_frames():
            label += f" ({lib.new_frames()[frame]['scene']})"
        lines.append((len(ws), len(roles), frame, f"- {label} [{len(ws)} words, {len(roles)} roles] " + ' · '.join(parts)))
    lines.sort(key=lambda x: (-x[0], -x[1], x[2]))
    return [x[3] for x in lines]


def motif_keys(motif_line):
    """Branch keys from an 'Active motifs' line. Reviews write either `ع ل م:B002/m02` or
    `quranic:root_000123:B002/m01`; internal root ids are resolved to Arabic roots."""
    ids = lib.root_by_id()
    out = []
    for root, br in re.findall(r'`(?:quranic:)?([^`:]+):(B\d+)', motif_line or ''):
        out.append(f"{ids.get(root, root)}:{br}")
    return ', '.join(dict.fromkeys(out))


def anchor_spans(s, anchor_line):
    """(from, to) ayah spans named in an anchor line, expanding ranges like 2:271-273."""
    return [(int(m.group(1)), int(m.group(2) or m.group(1)))
            for m in re.finditer(rf'\b{s}:(\d+)(?:[–-](\d+))?', anchor_line or '')]


def channel_index(s, lo=None, hi=None):
    """Invariants, scenes, motifs and places from the earlier channel review, scoped to the window's ayat.
    A parent channel is shown only when at least one of its subchannels is anchored in the window."""
    p = lib.src('channel_review', S=s)
    if not os.path.exists(p):
        return ''
    out, pending = [], None

    def in_scope(anchor_line):
        if lo is None:
            return True
        return any(a <= hi and b >= lo for a, b in anchor_spans(s, anchor_line))

    def places(anchor_line):
        return ', '.join(dict.fromkeys(f'{s}:{a}' + (f'-{b}' if b != a else '')
                                       for a, b in anchor_spans(s, anchor_line)))
    with open(p, encoding='utf-8') as f:
        text = f.read()
    for block in re.split(r'\n(?=#{3,4} )', text):
        head = block.split('\n', 1)[0]
        scene = re.search(r'Scene or process:(.*)', block)
        motifs = re.search(r'Active motifs:(.*)', block)
        anchors = re.search(r'Ayah anchors:(.*)', block)
        a = anchors.group(1).strip() if anchors else ''
        mot = motif_keys(motifs.group(1) if motifs else '')
        if head.startswith('### ') and not head.startswith('#### '):
            parent = head[4:].strip()
            pending = None
            inv = re.search(r'Semantic invariant:(.*)', block)
            if re.match(r'S\d+\.', parent):
                if in_scope(a):
                    out.append(f"\n### standalone: {parent}\n- scene: {trim(scene.group(1).strip(), 220) if scene else ''}"
                               f" | motifs: {mot} | at {places(a)}")
            elif inv:
                pending = f"\n### {parent}\ninvariant: {trim(inv.group(1).strip(), 220)}"
            continue
        if head.startswith('#### '):
            if not in_scope(a):
                continue
            if pending:
                out.append(pending)
                pending = None
            out.append(f"- {head[5:].strip()}: {trim(scene.group(1).strip(), 220) if scene else ''}"
                       f" | motifs: {mot} | at {places(a)}")
    return '\n'.join(out).strip()


def qiraat_block(refs):
    out = []
    for ref in refs:
        for wd in ayah_words(ref):
            for v in lib.qiraat().get(wd['ref'], []):
                note = v['qiraat_note'].split(' — ')[0][:90]
                out.append(f"{wd['ref']} {wd['surface']} → {v['qiraat_arabic']} ({v['qiraat_transliteration']}; "
                           f"{v['qiraat_reader_set']}; {v['qiraat_transmission_type']}) {note}")
    return '\n'.join(out)


def concordance_block(ref):
    lem = lib.lemmas()
    prof = lib.profiles()
    out = []
    seen = set()
    for wd in ayah_words(ref):
        for root, lemma, alt, _ in word_roots(wd):
            if alt or not lemma or (root, lemma) in seen:
                continue
            seen.add((root, lemma))
            refs = lem.get((root, lemma), [])
            head = f"### {lemma} — {root} — {len(refs)} uses in the Quran"
            if len(refs) <= CFG['concordance']['kwic_max_uses']:
                out.append(head + '\n' + '\n'.join(f"- {r} {lib.kwic(r)}" for r in refs))
            else:
                p = prof.get(f'{root}|{lemma}')
                body = json.dumps(p, ensure_ascii=False) if p else '(no use profile yet)'
                out.append(head + f"\nuse profile: {body}\nevery use: data/kwic/{safe(root + '_' + lemma)}.md")
    return '\n\n'.join(out)


def loanword_block(ref):
    cards = lib.loanword_cards()
    out = []
    for wd in ayah_words(ref):
        for root, lemma, alt, _ in word_roots(wd):
            c = cards.get(f'{root}|{lemma}')
            if c and c.get('loanwords'):
                out.append(f"- {lemma} ({root}): " + json.dumps(c['loanwords'], ensure_ascii=False))
    return '\n'.join(dict.fromkeys(out))


def pull_paths(s):
    return '\n'.join([
        f"- classical entries per root: {os.path.join(DATA, 'entries')}/<root letters without spaces>.md",
        f"- every use of a frequent lemma: {os.path.join(DATA, 'kwic')}/",
        f"- the Quran text: {os.path.join(DATA, 'quran.tsv')}; words: {os.path.join(DATA, 'words.tsv')}; "
        f"lemma index: {os.path.join(DATA, 'lemmas.tsv')}",
        f"- the whole dictionary: {os.path.join(DATA, 'branches.tsv')}",
    ])


def section(title, body):
    return f"## {title}\n\n{body.strip() if body and body.strip() else '(none)'}\n"


# ============================================================== packets


def window_dir(s, lo, hi):
    return os.path.join(WORK, f's{s:03d}', f'window_{lo}-{hi}')


def ayah_dir(s, a):
    return os.path.join(WORK, f's{s:03d}', f'{s}_{a}')


def out_ayah_dir(s, a):
    return os.path.join(OUT, f's{s:03d}', f'{s}_{a}')


def out_window_dir(s, lo, hi):
    return os.path.join(OUT, f's{s:03d}', f'window_{lo}-{hi}')


def build_window(s, only=None):
    wins = lib.windows_of_surah(s)
    long_surah = len(wins) > 1
    for lo, hi, label in wins:
        if only and not (lo <= only <= hi):
            continue
        refs = [f'{s}:{a}' for a in range(lo, hi + 1)]
        chains = channel_index(s, lo, hi) if long_surah else channel_index(s)
        parts = [f"# Window {s}:{lo}–{hi} ({label})\n",
                 section('Text', text_block(s, lo, hi)),
                 section('Existing chain map (earlier machine review; the starting point: ground, correct, extend, '
                         'connect; unranked, partly noisy)', chains or '(no chain map for this surah)'),
                 section('Words (ref surface | root | lemma | pos)', words_block(refs)),
                 section('Dictionary: every branch of every root (branch | image | definition)', dictionary_block(refs)),
                 section('Scene map in this window (mechanical, generous; for what the chain map missed)',
                         '\n'.join(scene_lines(refs)) or '(scene tags not built yet)')]
        if long_surah:
            surah_refs = lib.refs_of_surah(s)
            wide = [l for l in scene_lines(surah_refs, focus_refs=refs, min_words=3)]
            parts.append(section('Scene lines across the whole surah that touch this window', '\n'.join(wide)))
        parts += [section('Variant readings', qiraat_block(refs)),
                  section('Paths you may read', pull_paths(s))]
        d = window_dir(s, lo, hi)
        lib.write_text(os.path.join(d, 'packet.md'), '\n'.join(parts))
        print(f"window packet {s}:{lo}-{hi}: {sum(len(p) for p in parts):,} chars -> {d}")


def plan_block(s, a):
    lo, hi, _ = lib.window_of_ayah(s, a)
    p = os.path.join(out_window_dir(s, lo, hi), 'window.json')
    if not os.path.exists(p):
        return '(no window reading yet)'
    w = lib.read_json(p)
    imgs = {i['id']: i for i in w.get('images', [])}
    mine = next((x for x in w.get('plan', []) if x.get('ayah') == f'{s}:{a}'), None)
    out = []
    if mine:
        for k in ('opens', 'advances', 'completes'):
            for iid in mine.get(k, []):
                im = imgs.get(iid, {})
                mem = '; '.join(f"{m.get('surface')} {m.get('ref')} {m.get('branch')} {m.get('role')}" for m in im.get('members', []))
                out.append(f"- {k}: {iid} {im.get('name', '')} — {im.get('scene', '')}. Members: {mem}. "
                           f"Perceptible: {im.get('perceptible', '')}")
        out.append(f"- note: {mine.get('note', '')}")
    earlier = []
    for x in w.get('plan', []):
        xa = int(x['ayah'].split(':')[1])
        if xa < a:
            for iid in x.get('opens', []):
                earlier.append(f"- {x['ayah']} opened {iid} {imgs.get(iid, {}).get('name', '')}")
    out.append('\nOpened by earlier ayat:\n' + ('\n'.join(earlier) if earlier else '(none)'))
    out.append(f"\nWindow movement: {w.get('movement', '')}")
    return '\n'.join(out)


def build_ayah(s, a):
    ref = f'{s}:{a}'
    lo, hi = lib.local_range(s, a)
    local = [f'{s}:{x}' for x in range(lo, hi + 1)]
    wide = [l for l in scene_lines(lib.refs_of_surah(s), focus_refs=[ref], min_words=3)]
    parts = [f"# Ayah {ref}\n",
             section(f'The ayah in its neighbourhood ({s}:{lo}–{hi})', text_block(s, lo, hi, focus=a)),
             section('Its words (ref surface | root | lemma | pos)', words_block([ref])),
             section('Dictionary for its roots (branch | image | definition | tr: Turkish gloss)', dictionary_block([ref])),
             section('Scene lines touching its words, in the neighbourhood', '\n'.join(scene_lines(local, focus_refs=[ref])) or '(none)'),
             section('Scene lines touching its words, across the surah', '\n'.join(wide)),
             section('Plan from the window reading', plan_block(s, a)),
             section('Concordance for its lemmas', concordance_block(ref)),
             section('Variant readings', qiraat_block([ref])),
             section('Turkish loanword cards', loanword_block(ref)),
             section('Paths you may read', pull_paths(s))]
    d = ayah_dir(s, a)
    lib.write_text(os.path.join(d, 'discover.md'), '\n'.join(parts))
    print(f"ayah packet {ref}: {sum(len(p) for p in parts):,} chars -> {d}")


def build_evidence(s, a):
    ref = f'{s}:{a}'
    rec_p = os.path.join(out_ayah_dir(s, a), 'record.json')
    rec = lib.read_json(rec_p)
    cited = set()
    lemmas_cited = set()
    for f in rec.get('findings', []):
        an = f.get('anchor', {})
        if an.get('root') and an.get('branch'):
            cited.add(f"{an['root']} {an['branch']}")
    for wd in ayah_words(ref):
        for root, lemma, alt, _ in word_roots(wd):
            if not alt and lemma:
                lemmas_cited.add((root, lemma))
    bk = lib.branch_by_key()
    blines = [f"- {k} | {bk[k]['image']} | {bk[k]['what_is']} | {bk[k]['source_phrase']}" if k in bk
              else f"- {k} | NOT IN THE DICTIONARY" for k in sorted(cited)]
    rel = []
    for strength, target, note in lib.inter_ayah(ref):
        if strength in ('strong', 'medium'):
            rel.append(f"- {target} ({strength}): {note}\n  {lib.quran().get(target, '')}")
    parts = [f"# Evidence for {ref}\n",
             section('The ayah', lib.quran()[ref]),
             section('Its words', words_block([ref])),
             section('Findings to annotate (JSON)', json.dumps(rec.get('findings', []), ensure_ascii=False, indent=1)),
             section('Cited branches with classical phrases', '\n'.join(blines)),
             section('Concordance for the ayah\'s lemmas', concordance_block(ref)),
             section('Related-passage list (earlier machine reviews; incomplete, sometimes misleading)', '\n'.join(rel)),
             section('Paths you may read (search the Quran text and lemma index)', pull_paths(s))]
    d = ayah_dir(s, a)
    lib.write_text(os.path.join(d, 'evidence.md'), '\n'.join(parts))
    print(f"evidence packet {ref}: {sum(len(p) for p in parts):,} chars")


def build_write(s, a):
    ref = f'{s}:{a}'
    o = out_ayah_dir(s, a)
    rec = lib.read_json(os.path.join(o, 'record.json'))
    ev = lib.read_json(os.path.join(o, 'evidence.json'))
    bk = lib.branch_by_key()
    cited = sorted({f"{f['anchor']['root']} {f['anchor']['branch']}" for f in rec.get('findings', [])
                    if f.get('anchor', {}).get('root') and f.get('anchor', {}).get('branch')})
    glosses = [f"- {k} | {bk[k]['image']} | tr: {bk[k]['tr_gloss'] or '-'}" for k in cited if k in bk]
    parts = [f"# Commentary material for {ref}\n",
             section('The ayah', lib.quran()[ref]),
             section('Its neighbourhood', text_block(s, *lib.local_range(s, a, 2), focus=a)),
             section('Plan', plan_block(s, a)),
             section('Record of its reading (JSON)', json.dumps(rec, ensure_ascii=False, indent=1)),
             section('Evidence notes (JSON)', json.dumps(ev, ensure_ascii=False, indent=1)),
             section("Cited branches with the dictionary's Turkish gloss (the app's hover shows these entries)",
                     '\n'.join(glosses))]
    lib.write_text(os.path.join(ayah_dir(s, a), 'write.md'), '\n'.join(parts))
    print(f"write packet {ref}: {sum(len(p) for p in parts):,} chars")


def build_surah(s):
    parts = [f"# Surah {s}\n", section('Text', text_block(s, 1, lib.surah_len(s)))]
    for lo, hi, label in lib.windows_of_surah(s):
        p = os.path.join(out_window_dir(s, lo, hi), 'window.json')
        if os.path.exists(p):
            parts.append(section(f'Window reading {s}:{lo}–{hi} ({label})',
                                 json.dumps(lib.read_json(p), ensure_ascii=False, indent=1)))
    lead = []
    for a in range(1, lib.surah_len(s) + 1):
        p = os.path.join(out_ayah_dir(s, a), 'record.json')
        if os.path.exists(p):
            rec = lib.read_json(p)
            fs = [f for f in rec.get('findings', []) if f.get('for_prose') in ('lead', 'support')]
            lead.append(f"### {s}:{a}\nground: {rec.get('ground', '')}\nreread: {rec.get('reread', '')}\n"
                        + '\n'.join(f"- {f.get('statement', '')} [{f.get('anchor', {}).get('root', '')} "
                                    f"{f.get('anchor', {}).get('branch', '')}]" for f in fs))
    parts.append(section('Per ayah: ground, lead and supporting findings, reread', '\n\n'.join(lead)))
    lib.write_text(os.path.join(WORK, f's{s:03d}', 'surah.md'), '\n'.join(parts))
    print(f"surah packet {s}: {sum(len(p) for p in parts):,} chars")


def sizes(surahs):
    for s in surahs:
        for p in sorted(glob.glob(os.path.join(WORK, f's{s:03d}', '**', '*.md'), recursive=True)):
            print(f"{os.path.getsize(p):>9,}  {os.path.relpath(p, lib.HERE)}")


# ============================================================== cli


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cmd')
    ap.add_argument('kind', nargs='?')
    ap.add_argument('--surahs')
    ap.add_argument('--surah', type=int)
    ap.add_argument('--ayah', type=int)
    ap.add_argument('--ref')
    ap.add_argument('--sample', type=int, help='frames only: tag a random sample of branches from the whole Quran')
    ap.add_argument('--seed', type=int, default=15)
    ap.add_argument('--exclude', help="with --sample: surahs, ayat or ranges whose roots are left out, e.g. '1,100,5:6,29:39-45'")
    x = ap.parse_args()
    if x.cmd == 'base':
        build_base()
    elif x.cmd == 'jobs' and x.kind == 'frames':
        jobs_frames(parse_surahs(x.surahs or ''), sample=x.sample, seed=x.seed, exclude=x.exclude)
    elif x.cmd == 'jobs':
        {'loanwords': jobs_loanwords, 'profiles': jobs_profiles}[x.kind](parse_surahs(x.surahs))
    elif x.cmd == 'pull':
        build_pull(parse_surahs(x.surahs))
    elif x.cmd == 'window':
        build_window(x.surah, x.ayah)
    elif x.cmd in ('ayah', 'evidence', 'write'):
        s, a = [int(p) for p in x.ref.split(':')]
        {'ayah': build_ayah, 'evidence': build_evidence, 'write': build_write}[x.cmd](s, a)
    elif x.cmd == 'surah':
        build_surah(x.surah)
    elif x.cmd == 'sizes':
        sizes(parse_surahs(x.surahs))
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main()
