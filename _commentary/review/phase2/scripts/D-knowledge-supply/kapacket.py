#!/usr/bin/env python3
"""Test (2): build a knowledge-aware (KA) ayah packet by script and compare its size with the cold context, the v15
ayah packet and the v9 full package; check that it holds the watch-case ingredients. Read-only on every repo: v15's
lib/build are imported for their loaders and block builders, with build.WORK redirected to this scratch folder.

KA packet = what memory does not supply, pushed; everything else one read away:
  1 text: the whole surah when it is <= SURAH_TOKENS_MAX tokens (the cold arm's same-surah reach came from it), else
    the pericope window (+-7 at least); the surah file is pullable
  2 the ayah's words (QAC)
  3 branch index for the ayah's roots: EVERY branch keeps one line (id | image | Turkish gloss); branches with
    memory_score <= 1 (policy_eval.py) add the definition and one early-source phrase with its source; collocation /
    non_bare branches add their construction (scope note's first clause + the phrase) and whether a construction
    partner occurs at this occurrence (sibling C2 construction index, marked 'unknown' where it has no row)
  4 rare branches of the neighbourhood (+-NEIGH ayat, other roots): memory_score <= 1 only, image + gloss
  5 concordance: root level (all lemmas) when the root has <= KWIC_MAX uses: every use as keyword-in-context; else
    a descriptive collocation profile per form (quran-data grammar/contextual collocation_profiles_v2.tsv) + path
  6 same-surah occurrences of the ayah's roots outside the neighbourhood (refs + surface), for roots <= 400 uses
  7 variant readings; 8 the existing chain map lines anchored at this ayah (channel review; ground/extend, never
    rediscover); 9 pull paths.
Left to memory (and verified afterwards by script): Quran references and cross-surah parallels, famous senses,
grammar, Turkish loanword drift (v15 cards stay pullable), tafsir positions.
Writes packets/<S_A>.ka.md and sizes.tsv; prints the comparison and the ingredient checks."""
import csv, json, os, re, sys
from collections import defaultdict, Counter
from pathlib import Path
csv.field_size_limit(10**9)
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from common import est_tokens  # calibrated: 4581 + 1.151*arabic_chars + 0.366*other_chars (billed v9 runs)
V15 = Path('/Volumes/OZTURK/_projects/prose_generation/_commentary/v15')
V9 = Path('/Volumes/OZTURK/_projects/prose_generation/_commentary/v9')
sys.path.insert(0, str(V15))
sys.dont_write_bytecode = True
import lib, build  # noqa: E402
build.WORK = str(HERE / 'v15work')          # v15 packets for ayat v15 never ran are written here, never in the repo
C2 = Path('/private/tmp/claude-502/-Volumes-OZTURK--projects-prose-generation/9b253717-be1d-4238-a42b-f4b098b1d894/'
          'scratchpad/phase2/C2-loaded-parallels/construction_index.tsv')
COLLOC = Path('/Volumes/OZTURK/_projects/quran-data/data/grammar/contextual/collocation_profiles_v2.tsv')
SURAH_TOKENS_MAX = 60000
NEIGH = 3
KWIC_MAX = 30
SAME_SURAH_ROOT_MAX = 400
PUSH_MAX = 1

# ---- per-branch policy fields from the Turkish entries (../branches.tsv, built by ../branch_table.py)
BT = {}
for r in csv.DictReader(open(HERE.parent / 'branches.tsv', encoding='utf-8'), delimiter='\t'):
    BT[f"{r['root']} {r['branch']}"] = r


def mscore(r):
    return int(int(r['idx']) <= 3) + int(int(r['n_sources']) >= 4) + int(int(r['hft_any']) + int(r['v12']) >= 10)


def norm_root(rt):
    return rt.replace('أ', 'ء').replace('إ', 'ء').replace('ؤ', 'ء').replace('ئ', 'ء')


# ---- construction index (sibling agent C2, script): (ref3, branch_ref) -> present, evidence
CONS = {}
if C2.exists():
    for r in csv.DictReader(open(C2, encoding='utf-8'), delimiter='\t'):
        CONS[(r['ref3'], r['branch'])] = (r['present'], r['evidence'])
# ---- collocation profiles
PROF = defaultdict(list)
for r in csv.DictReader(open(COLLOC, encoding='utf-8'), delimiter='\t'):
    PROF[norm_root(r['root_arabic'])].append(r)


def shortest_phrase(phrase, budget=220):
    """Early-source phrase segments in their order, up to ~budget characters (source tags kept)."""
    segs = [s.strip() for s in re.split(r'؛|;', phrase or '') if s.strip()]
    out, n = [], 0
    for sg in segs:
        if out and n + len(sg) > budget:
            break
        out.append(sg); n += len(sg)
    return '؛ '.join(out)[:budget + 60]


def first_clause(note):
    return re.split(r'[;.]', note or '')[0][:160]


def root_uses(root):
    return sum(len(v) for (r, _), v in lib.lemmas().items() if r == root)


MODE = os.environ.get('KA_MODE', 'phrase')   # full | phrase | lean | index  (see sizes_variants in __main__)


def branch_lines(root, occ_refs, mode=None):
    """Every branch keeps one line. mode full: def(140)+early phrases(220) when memory_score<=1; phrase: early phrases
    (120) when score<=1; lean: early phrases (120) when score==0; index: no additions. Construction-bound branches
    (collocation/non_bare) always get a compact construction tag with its status at this occurrence."""
    mode = mode or MODE
    out = []
    for b in lib.branches().get(root, []):
        key = f"{root} {b['branch']}"
        t = BT.get(key)
        tr = (t['tr_concept'] if t else b.get('tr_gloss', ''))[:60]
        line = f"{b['branch']} | {b['image']} | {tr}"
        if t is None:
            out.append(line)
            continue
        kind, sc = t['branch_kind'], mscore(t)
        if mode == 'full' and sc <= PUSH_MAX:
            line += f" | def: {build.trim(re.sub(r'^يدخل فيه\\s*', '', b['what_is']), 140)} | early: {shortest_phrase(t['phrase_ar'])}"
        elif (mode == 'phrase' and sc <= PUSH_MAX) or (mode == 'lean' and sc == 0):
            line += f" | early: {shortest_phrase(t['phrase_ar'], 120)}"
        if kind in ('collocation', 'non_bare'):
            here = []
            for o in occ_refs:
                c = CONS.get((o, t['branch_ref']))
                here.append('present' if c and c[0] == '1' else 'not found' if c else 'unknown')
            tag = 'C' if kind == 'collocation' else 'F'
            cons_phrase = shortest_phrase(t['phrase_ar'], 60) if mode == 'full' else re.split(r'؛|;', t['phrase_ar'] or '')[0][:70]
            # the presence status is a script judgment (C2 index recall 0.21-0.46): kept OUT of the generative packet
            # (no pre-judged content) unless KA_STATUS=1; the verification step applies it after synthesis
            line += f" | {tag}[{cons_phrase}]" + (f" here: {'/'.join(dict.fromkeys(here)) or 'n/a'}" if os.environ.get('KA_STATUS') == '1' else '')
        out.append(line)
    return out


def ka_packet(ref):
    s, a = [int(x) for x in ref.split(':')]
    lo, hi = lib.local_range(s, a)
    surah_text = build.text_block(s, 1, lib.surah_len(s), focus=a)
    if est_tokens(surah_text) <= SURAH_TOKENS_MAX:
        text_title, text = f'The whole surah {s} (focus marked)', surah_text
        tlo, thi = 1, lib.surah_len(s)
    else:
        wlo, whi, _ = lib.window_of_ayah(s, a)
        tlo, thi = min(wlo, lo), max(whi, hi)
        text_title, text = f'Surah {s}, ayat {tlo}-{thi} (window; the whole surah: data/quran.tsv)', build.text_block(s, tlo, thi, focus=a)
    words = build.ayah_words(ref)
    roots, occ = [], defaultdict(list)
    for wd in words:
        for root, lemma, alt, why in build.word_roots(wd):
            if root not in roots:
                roots.append(root)
            occ[root].append(wd['ref'])
    idx = []
    for root in roots:
        idx.append(f"### {root} — {root_uses(root)} uses; here: {', '.join(dict.fromkeys(occ[root]))}\n"
                   + '\n'.join(branch_lines(root, list(dict.fromkeys(occ[root])))))
    # neighbourhood rare branches (other roots)
    nroots = []
    for x in range(max(1, a - NEIGH), min(lib.surah_len(s), a + NEIGH) + 1):
        if x == a:
            continue
        for wd in build.ayah_words(f'{s}:{x}'):
            for root, lemma, alt, why in build.word_roots(wd):
                if root not in roots and root not in [n for n, _ in nroots]:
                    nroots.append((root, wd['ref']))
    neigh = []
    for root, wref in nroots:
        rare = [f"{b['branch']} {b['image']} ({BT[f'{root} {b['branch']}']['tr_concept'][:45]})"
                for b in lib.branches().get(root, [])
                if f"{root} {b['branch']}" in BT and mscore(BT[f"{root} {b['branch']}"]) <= (PUSH_MAX if MODE in ('full', 'phrase') else 0)]
        if rare:
            neigh.append(f"- {root} ({wref}): " + '; '.join(rare))
    # concordance, root level
    conc = []
    for root in roots:
        refs = sorted({r for (rt, _), v in lib.lemmas().items() if rt == root for r in v}, key=build.refkey)
        if not refs:
            continue
        prof = sorted(PROF.get(norm_root(root), []), key=lambda r: (-int(r['instance_count']), -int(r['attach_count'])))
        forms = defaultdict(list)
        for p in prof:
            forms[(p['form_tag'], p['instance_count'])].append(f"{p['partner_root']} {p['attach_count']}/{p['total_attach']}")
        plines = [f"  {f} ({n} uses): with " + ', '.join(v[:4]) for (f, n), v in list(forms.items())[:6]] if len(refs) >= 3 else []
        ptxt = ('\n  partners by form (descriptive, grammar attachments):\n' + '\n'.join(plines)) if plines else ''
        if len(refs) <= KWIC_MAX:
            conc.append(f"### {root} — every use ({len(refs)})" + ptxt + "\n" + '\n'.join(f"- {r} {lib.kwic(r)}" for r in refs))
        else:
            conc.append(f"### {root} — {len(refs)} uses" + ptxt + f"\n  every use: data/lemmas.tsv + data/kwic/")
    # same-surah occurrences outside the text shown
    same = []
    for root in roots:
        if root_uses(root) > SAME_SURAH_ROOT_MAX:
            continue
        hits = []
        for x in range(1, lib.surah_len(s) + 1):
            if tlo <= x <= thi and thi - tlo < lib.surah_len(s) - 1:
                continue
            if abs(x - a) <= 7 or x == a:
                continue
            for wd in build.ayah_words(f'{s}:{x}'):
                if root in wd['roots'].split('|'):
                    hits.append(f"{s}:{x} {wd['surface']}")
        if hits:
            same.append(f"- {root}: " + '; '.join(dict.fromkeys(hits)))
    chains = build.channel_index(s, a, a)
    parts = [f"# Ayah {ref} — knowledge-aware packet\n",
             build.section(text_title, text),
             build.section('Its words (ref surface | root | lemma | pos)', build.words_block([ref])),
             build.section('Every branch of its roots (id | image | tr); rarely-recalled branches also carry their '
                           'definition and an early-source phrase; construction-bound branches carry their construction',
                           '\n\n'.join(idx)),
             build.section(f'Rarely-recalled branches of the neighbouring words (±{NEIGH})', '\n'.join(neigh)),
             build.section('Uses in the Quran (every use for roots up to 30 uses; otherwise partners by form)',
                           '\n\n'.join(conc)),
             build.section('Other places in this surah with the same roots', '\n'.join(same)),
             build.section('Existing chain map lines anchored here (earlier machine review; ground, extend, connect)',
                           chains or '(none)'),
             build.section('Variant readings', build.qiraat_block([ref])),
             build.section('Paths you may read', build.pull_paths(s))]
    return '\n'.join(parts), {'text': text, 'index': '\n\n'.join(idx), 'neigh': '\n'.join(neigh),
                              'conc': '\n\n'.join(conc), 'same': '\n'.join(same), 'chains': chains or ''}


def cold_context(ref):
    s, a = [int(x) for x in ref.split(':')]
    p = V9 / 'lines' / 'work' / f'{s}_{a}' / 'context.md'
    w10 = (V9 / 'prompts' / 'write_v10.md').read_text(encoding='utf-8')
    if p.exists():
        return w10 + p.read_text(encoding='utf-8'), 'v9 context.md'
    # equivalent for an ayah v9 never ran: ayah + words + Fatiha + whole surah (the cold arm's contents)
    t = (build.text_block(s, a, a) + '\n' + build.words_block([ref]) + '\n' + build.text_block(1, 1, 7) + '\n'
         + build.text_block(s, 1, lib.surah_len(s)))
    return w10 + t, 'rebuilt (ayah, words, Fatiha, whole surah)'


def v15_packet(ref):
    s, a = [int(x) for x in ref.split(':')]
    real = V15 / 'work' / f's{s:03d}' / f'{s}_{a}' / 'discover.md'
    if real.exists():
        return real.read_text(encoding='utf-8'), 'v15 work (real run)'
    build.build_ayah(s, a)
    p = Path(build.ayah_dir(s, a)) / 'discover.md'
    return p.read_text(encoding='utf-8'), 'rebuilt by v15 build_ayah (no window plan, loanword cards or profiles)'


def package(ref):
    s, a = [int(x) for x in ref.split(':')]
    w = V9 / 'lines' / 'work' / f'{s}_{a}'
    if (w / 'package.md').exists():
        return (w / 'context.md').read_text(encoding='utf-8') + (w / 'package.md').read_text(encoding='utf-8'), 'v9 context+package.md'
    return None, 'none'


_DI = re.compile('[\u0610-\u061a\u064b-\u065f\u0670\u06d6-\u06ed\u0640]')
_AL = str.maketrans({'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٱ': 'ا', 'ى': 'ي', 'ۥ': '', 'ۦ': ''})


def fold(t):
    return _DI.sub('', t or '').translate(_AL)


CHECKS = {  # format-agnostic: a distinctive string of the ingredient, wherever it sits in the input
    '29:38': [('sabal eye-film branch (Sihah definition)', r'غشاوة'), ('its classical phrase: spider weaving', r'نسج العنكبوت'),
              ('zayyana (ز ي ن) branch index', r'تزيين|الزين|زين الشيء'), ('basar (ب ص ر) branch index', r'البصر|الإبصار'),
              ('29:41 spider-house text in the input', r'ٱلْعَنكَبُوتِ')],
    '18:86': [('hama use 15:26', r'15:26'), ('hama use 15:28', r'15:28'), ('hama use 15:33', r'15:33'),
              ('hama with salsal (clause text)', r'صَلْصَٰلٍۢ مِّنْ حَمَإٍۢ|صلصال من حمإ|ص ل ص ل \d')],
    '18:96': [('nafakha 15:29', r'15:29'), ('38:72', r'38:72'), ('32:9', r'32:9[^0-9]'), ('3:49', r'3:49[^0-9]'), ('5:110', r'5:110'),
              ('21:91', r'21:91'), ('66:12', r'66:12'), ('nafakha partners: ruh count', r'ر و ح \d')],
    '1:6': [('sirat B002 swallowing (definition)', r'الغيبة في المرور'), ('qawm B012 device upright part', r'آلة قائمة'),
            ('hady B003 the one ahead', r'المتقدم الهادي'), ('malik B006 road middle (1:4, neighbour)', r'وسط الطريق|معظم الطريق|B006 [^|\n]*طريق'),
            ('malik B008 lead animal (1:4, neighbour)', r'B008 [^\n]{0,80}(تقدم|يقود|قائد|أمام)'),
            ('dall B005 lost camel (1:7)', r'الضالّة|الضالة'),
            ('abd B005 trodden road (1:5; memory-likely: the cold 1:5 arm recalled it)', r'التذليل والتسوية|طريق معبد')],
    '4:34': [('4:128 husband\'s nushuz text in the input', r'خَافَتْ مِنۢ بَعْلِهَا'),
             ('nushuz B004 phrase: husband harsh and beating', r'نشز بعلها جفاها'),
             ('darb B002 travel marked collocation with its construction', r'السعي في الأرض[^\n]*C\[ضرب في الأرض'),
             ('qawm B012', r'آلة قائمة')],
    '5:6': [('mirfaq leaning (irtifaq / ittika phrase)', r'التوكؤ|الاتكاء|ارتفق'), ('kaba B002 the square raised house', r'البيت المربع'),
            ('5:97 qiyaman text in the input', r'قِيَٰمًۭا لِّلنَّاسِ'), ('5:8 qawwamin text in the input', r'قَوَّٰمِينَ لِلَّهِ')],
}

if __name__ == '__main__':
    AYAT = sys.argv[1:] or ['1:6', '4:34', '5:6', '18:86', '18:96', '29:38', '2:282']
    os.makedirs(HERE / 'packets', exist_ok=True)
    rows = []
    for ref in AYAT:
        ka, comp = ka_packet(ref)
        (HERE / 'packets' / f"{ref.replace(':', '_')}.ka.{MODE}.md").write_text(ka, encoding='utf-8')
        cold, cold_src = cold_context(ref)
        v15, v15_src = v15_packet(ref)
        pkg, pkg_src = package(ref)
        P = 4581  # fixed billed prefix (claude -p system etc.), from calib.py
        row = {'ayah': ref, 'cold_tok': round(est_tokens(cold)) + P, 'v15_tok': round(est_tokens(v15)) + P,
               'package_tok': round(est_tokens(pkg)) + P if pkg else '', 'ka_tok': round(est_tokens(ka)) + P,
               'ka_text_tok': round(est_tokens(comp['text']) ), 'ka_index_tok': round(est_tokens(comp['index']) ),
               'ka_neigh_tok': round(est_tokens(comp['neigh']) ), 'ka_conc_tok': round(est_tokens(comp['conc']) ),
               'ka_same_tok': round(est_tokens(comp['same']) ), 'ka_chain_tok': round(est_tokens(comp['chains']) ),
               'cold_src': cold_src, 'v15_src': v15_src, 'package_src': pkg_src}
        rows.append(row)
        print(f"\n== {ref}: billed-input tokens (calibrated, incl. 4.6k prefix)  cold {row['cold_tok']:,} | v15 {row['v15_tok']:,} | "
              f"package {row['package_tok'] if row['package_tok'] != '' else '-'} | KA {row['ka_tok']:,}")
        print(f"   KA parts (tokens): text {row['ka_text_tok']:,}, branch index {row['ka_index_tok']:,}, neighbour rare {row['ka_neigh_tok']:,}, "
              f"uses {row['ka_conc_tok']:,}, same-surah {row['ka_same_tok']:,}, chain map {row['ka_chain_tok']:,}")
        print(f"   sources: cold={cold_src}; v15={v15_src}; package={pkg_src}")
        for name, pat in CHECKS.get(ref, []):
            got = {k: bool(re.search(fold(pat), fold(t))) for k, t in (('cold', cold), ('v15', v15), ('package', pkg), ('KA', ka))}
            print(f"   [{'x' if got['KA'] else ' '}] {name:45} cold={int(got['cold'])} v15={int(got['v15'])} package={int(got['package']) if pkg else '-'} KA={int(got['KA'])}")
    with open(HERE / f'sizes.{MODE}.tsv', 'w', encoding='utf-8') as fh:
        cols = list(rows[0])
        fh.write('\t'.join(cols) + '\n')
        for r in rows:
            fh.write('\t'.join(str(r[c]) for c in cols) + '\n')
