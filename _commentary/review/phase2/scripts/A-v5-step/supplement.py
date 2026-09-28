"""Script supplements for what v5 structurally lacks (Phase 1 §4.4, §5, §6):
 A concordance + frame profile per focus root (loaded-word detector: dominant collocate frame vs the focus)
 B existing image chains: network-v3 channel subchannels whose anchors include the ayah (ground/extend, never rediscover)
 C parallels: same-surah and other-surah ayat ranked by IDF of shared roots (ordering only)
 D early-source citations of this ayah inside the six early lexicon entries + Majaz al-Quran (construction shown)
 E Turkish baseline tokens per word + the dictionary's gloss error profile (loses/adds/collision) for the plain branch
 F definitional cross-references: a focus-root branch whose early definition names a word of another surah root, and
   vice versa (explainable path; e.g. a definition mentioning a word that occurs elsewhere in the surah)
 G branch_kind guard: every collocation-bound branch activated upstream, with construction present/absent (heuristic)
Nothing here is a verdict; everything is an ordering or a path. Evaluation cases never enter these rules."""
import json, os, re, glob, math, csv, collections, sqlite3, sys
import lib
from kinds import norm, surface_root_map, collocates, window

REV = '/Volumes/OZTURK/_projects/quran-data/data/analysis/channels/network-v3'
RP = '/Volumes/OZTURK/_projects/dictionary/data/output/root_packets'
V12 = '/Volumes/OZTURK/_projects/quran-data/data/analysis/ayah-activation/v12-cross-run/tr'
MAJAZ = '/Volumes/OZTURK/_projects/quran-roots/_corpus/lexicons/cache/openiti_context.sqlite'
EARLY = ('ayn', 'maqayis', 'jamhara', 'sihah', 'tahdhib', 'mufradat')


def ayah_roots_map():
    m = collections.defaultdict(list)  # ayah -> [(root, surfaces, qac_refs)]
    with open(lib.SLM + '/qac_root_ayah.tsv', encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            m[r['ayah_ref']].append((r['root_norm'], r['surfaces_ar'], r['qac_refs']))
    return m


AR = None; DF = None; NAY = None


def init():
    global AR, DF, NAY
    if AR is None:
        AR = ayah_roots_map()
        NAY = len(AR)
        DF = collections.Counter()
        for ay, lst in AR.items():
            for r in {x[0] for x in lst}: DF[r] += 1


def idf(r):
    return math.log(NAY / max(1, DF[r]))


def snippet(ref, root_surfs, k=3):
    words = [w for w in lib.quran_text().get(ref, '').split() if re.search(r'[ء-يٱ]', w)]
    sset = {norm(s) for s in root_surfs.split(';')}
    for i, w in enumerate(words):
        if norm(w) in sset:
            return ' '.join(words[max(0, i - k):i + k + 1])
    return ' '.join(words[:2 * k + 1])


# ---------- A: concordance frames ----------
def frames(root, focus, max_uses=80):
    init()
    uses = [(ay, s) for ay, s, *_ in [(a, sf) for a, sf, lm, n in lib.concordance()[root]]]
    n_words = sum(n for a, sf, lm, n in lib.concordance()[root])
    if len(uses) > max_uses:
        return dict(root=root, n_words=n_words, n_ayat=len(uses), profile='frequent (frames not computed)')
    col = collections.Counter(); where = collections.defaultdict(list)
    for ay, s in uses:
        for r in {x[0] for x in AR[ay]} - {root, 'ء ل ه'}:
            col[r] += 1; where[r].append(ay)
    # keep collocates in >=2 uses, weight by idf; greedy frames
    cands = sorted([r for r in col if col[r] >= 2], key=lambda r: -(col[r] * idf(r)))
    frames_ = []; covered = set()
    for r in cands:
        new = [a for a in where[r] if a not in covered]
        if len(new) >= 2 and idf(r) > 2.0:
            frames_.append((r, where[r]))
            covered |= set(where[r])
        if len(frames_) >= 6: break
    lines = []
    for r, ays in frames_:
        lines.append(f"with {r} ({len(ays)}): " + ', '.join(sorted(ays, key=lib.refkey)))
    rest = [a for a, s in uses if a not in covered]
    focus_in = [r for r, ays in frames_ if focus in ays]
    dom = max((len(a) for r, a in frames_), default=0)
    return dict(root=root, n_words=n_words, n_ayat=len(uses), frames=lines,
                other=sorted(rest, key=lib.refkey), focus_frames=focus_in, dominant_share=round(dom / len(uses), 2) if uses else 0,
                snippets={a: snippet(a, s) for a, s in uses} if len(uses) <= 24 else {})


# ---------- B: channels ----------
def parse_range(tok, s):
    tok = tok.strip()
    m = re.match(r'^(\d+):(\d+)(?:[-–](\d+))?', tok)
    if not m: return None
    if int(m.group(1)) != s: return None
    a = int(m.group(2)); b = int(m.group(3) or a)
    return a, b


def channels(ref):
    s, a = map(int, ref.split(':'))
    p = f'{REV}/s{s:03d}/review/reader_a_pilot.md'
    if not os.path.exists(p): return []
    t = open(p, encoding='utf-8').read()
    out = []
    parents = re.split(r'\n### ', t)
    for par in parents[1:]:
        ptitle = par.split('\n', 1)[0]
        inv = re.search(r'Semantic invariant: (.*)', par)
        reach = re.search(r'Surprising reach: (.*)', par)
        subs = re.split(r'\n#### ', par)
        for sub in subs[1:]:
            stitle = sub.split('\n', 1)[0]
            anch = re.search(r'Ayah anchors: (.*)', sub)
            if not anch: continue
            hit = None
            for part in re.split(r';', anch.group(1)):
                for tok in re.findall(r'\d+:\d+(?:[-–]\d+)?', part):
                    rg = parse_range(tok, s)
                    if rg and rg[0] <= a <= rg[1]:
                        hit = part.strip(); break
                if hit: break
            if hit:
                mot = re.search(r'Active motifs: (.*)', sub)
                rt = re.search(r'Reading type: (.*)', sub)
                syn = re.search(r'Synthesis: (.*)', sub)
                out.append(dict(parent=ptitle, invariant=(inv.group(1) if inv else ''), reach=(reach.group(1) if reach else ''),
                                sub=stitle, reading_type=(rt.group(1) if rt else ''), anchor=hit,
                                motifs=(mot.group(1) if mot else ''), synthesis=(syn.group(1) if syn else '')))
    return out


# ---------- C: parallels ----------
def parallels(ref, k_same=12, k_other=12):
    init()
    s = ref.split(':')[0]
    F = {x[0] for x in AR[ref]} - {'ء ل ه'}
    sc_same = []; sc_other = []
    for ay, lst in AR.items():
        if ay == ref: continue
        sh = F & {x[0] for x in lst}
        if not sh: continue
        score = sum(idf(r) for r in sh)
        item = (round(score, 1), ay, sorted(sh, key=lambda r: -idf(r))[:4])
        (sc_same if ay.split(':')[0] == s else sc_other).append(item)
    sc_same.sort(reverse=True); sc_other.sort(reverse=True)
    return sc_same[:k_same], sc_other[:k_other]


# ---------- D: early citations ----------
def early_citations(ref):
    init()
    s, a = ref.split(':')
    words = [norm(w) for w in lib.quran_text()[ref].split() if re.search(r'[ء-يٱ]', w)]
    words = [re.sub(r'^(وال|فال|بال|لل|ال)', '', w) for w in words]
    FW = {'في', 'اذا', 'حتي', 'ان', 'ما', 'من', 'لا', 'قد', 'لم', 'عن', 'علي', 'الي', 'ثم', 'او', 'اما', 'واما', 'هو', 'هم', 'لهم', 'له', 'به', 'فيه', 'فيها', 'فيهم', 'عند', 'عندها', 'ذلك', 'الذين', 'الذي', 'كان', 'كانوا', 'وكانوا', 'قال', 'قالوا', 'انا', 'انه', 'لكم', 'بما', 'كل'}
    bigrams = {f'{words[i]} {words[i+1]}' for i in range(len(words) - 1) if words[i] not in FW and words[i + 1] not in FW and len(words[i]) >= 3 and len(words[i + 1]) >= 3}
    idx, roots = lib.dict_index()
    rmap = lib.root_ar_map(); inv = collections.defaultdict(list)
    for rid, r in rmap.items(): inv[norm(r).replace(' ', '')].append(rid)
    out = []
    for root in sorted({x[0] for x in AR[ref]}):
        for rid in inv.get(norm(root).replace(' ', ''), []):
            p = f'{RP}/{rid}.json'
            if not os.path.exists(p): continue
            d = json.load(open(p))
            for src in d.get('dictionary_sources', []):
                if src.get('source_id') not in EARLY: continue
                txt = src.get('entry_text_clean') or ''
                nt = norm(txt)
                nt2 = re.sub(r'\b(وال|فال|بال|لل|ال)', '', nt)
                for bg in bigrams:
                    i = nt2.find(bg)
                    if i >= 0:
                        out.append((root, src['source_id'], bg, nt2[max(0, i - 160):i + 200].replace('~~', ' ')))
                        break
    # Majaz
    try:
        c = sqlite3.connect(MAJAZ)
        an = int(a) - (1 if s == '1' else 0)
        for sf, mk, txt in c.execute("select surface_form, ayah_marker, entry_text_clean from quran_specialized_entries where ayah_marker=?", (str(an),)):
            nsf = re.sub(r'\b(وال|فال|بال|لل|ال)', '', norm(sf or ''))
            if nsf and all(w in ' '.join(words) for w in nsf.split()[:2]):
                out.append(('-', 'majaz_quran', sf, norm(txt)[:360]))
    except Exception as e:
        out.append(('-', 'majaz_error', str(e), ''))
    return out


# ---------- E: Turkish ----------
def turkish(ref, plain_branches):
    s = ref.split(':')[0]
    p = f'{V12}/{s}_ayah_findings_publication.json'
    base = None
    if os.path.exists(p):
        for ay in json.load(open(p))['ayat']:
            if ay['ayah_ref'] == ref:
                base = ay['baseline']; break
    idx, roots = lib.dict_index()
    rows = []
    for b in plain_branches:
        di = idx.get(b)
        if not di: continue
        rows.append((b, di.get('gloss')))
    # error profiles
    prof = []
    for b, g in rows:
        rid = b.split('/')[0]
        if not os.path.exists(f'{lib.DICT}/{rid}_entry.json'): continue
        d = json.load(open(f'{lib.DICT}/{rid}_entry.json'))
        for br in d['branches']:
            if br['branch_ref'] == b:
                cg = br.get('concept_gloss') or {}
                ep = cg.get('error_profile') or {}
                ctx = [(x.get('text'), (x.get('error_profile') or {}).get('loses'), (x.get('error_profile') or {}).get('adds'), (x.get('error_profile') or {}).get('collision')) for x in br.get('contextual_glosses', [])]
                prof.append(dict(branch=b, gloss=cg.get('text'), loses=ep.get('loses'), adds=ep.get('adds'), collision=ep.get('collision'), contextual=[c for c in ctx if any(c[1:])][:3]))
    return dict(baseline=(base or {}).get('text'), profiles=prof)


# ---------- F: definitional cross-references ----------
def xrefs(ref, scope='surah'):
    init()
    s = int(ref.split(':')[0])
    idx, roots = lib.dict_index(); rmap = lib.root_ar_map()
    focus_roots = {x[0] for x in AR[ref]} - {'ء ل ه'}
    scope_ays = [ay for ay in AR if int(ay.split(':')[0]) == s]
    forms = collections.defaultdict(set); where = collections.defaultdict(set)
    for ay in scope_ays:
        for r, surfs, q in AR[ay]:
            where[r].add(ay)
            for x in surfs.split(';'):
                n = norm(x); n = re.sub(r'^(وال|فال|بال|لل|ال|و|ف)', '', n) if len(n) > 4 else n
                if len(n) >= 3: forms[r].add(n)
    def toks(txt):
        t = set(re.findall(r'[ء-ي]+', norm(txt)))
        t |= {re.sub(r'^(وال|فال|بال|لل|ال|و|ف|ب|ل)', '', x) for x in t}
        return t
    hits = []
    for b, di in idx.items():
        rid = b.split('/')[0]; rn = rmap.get(rid)
        if rn not in where: continue
        focus_side = rn in focus_roots
        txt = ' '.join(filter(None, [di.get('image_ar'), di.get('what_ar'), di.get('phrase_ar')]))
        tk = toks(re.sub(r'\([^)]*\)', ' ', txt))
        for rb in where:
            if rb == rn or rb == 'ء ل ه': continue
            if not (focus_side or rb in focus_roots): continue
            m = forms[rb] & tk
            if m:
                hits.append((round(idf(rb) + idf(rn), 1), b, rn, di.get('gloss'), di.get('kind'), rb, sorted(m)[:2],
                             sorted(where[rb] - {ref}, key=lib.refkey)[:6] if focus_side else [ref]))
    FWF = {'فيه', 'فيها', 'فيهم', 'عند', 'عنده', 'عندها', 'منه', 'منها', 'عليه', 'عليها', 'اليه', 'بين', 'قبل', 'بعد', 'فوق', 'تحت', 'دون', 'مثل', 'غير', 'كان', 'يكون', 'قال', 'يقال', 'ذات', 'ذلك', 'شيء', 'امر', 'اهل', 'يوم', 'ارض', 'ماء'}
    best = {}
    for h in hits:
        sc, b, rn, gl, kind, rb, m, ays = h
        m2 = [x for x in m if x not in FWF and len(x) >= 3]
        if not m2 or idf(rb) < 2.5: continue
        key = (rn, rb, tuple(m2))
        if key in best:
            best[key][1].append(b.split('/')[1]); continue
        best[key] = [h, [b.split('/')[1]]]
    out = []
    for key, (h, bl) in best.items():
        sc, b, rn, gl, kind, rb, m, ays = h
        out.append((sc, b, rn, gl, kind, rb, m, ays, bl))
    out.sort(reverse=True)
    return out


def guard(D):
    """G: collocation-bound branches in the digest with construction status"""
    idx, roots = lib.dict_index(); rmap = lib.root_ar_map(); smap = surface_root_map()
    init()
    out = []
    ref = D['ref']
    for b, bi in D['branches'].items():
        di = idx.get(b, {})
        if di.get('kind') != 'collocation': continue
        root = rmap.get(b.split('/')[0], '')
        cr = collocates(di.get('phrase_ar'), root, smap)
        same = cr & {x[0] for x in AR[ref]}
        win = cr & set().union(*[{x[0] for x in AR.get(w, [])} for w in window(ref)])
        out.append(dict(branch=b, root=root, gloss=di.get('gloss'), note=di.get('note'),
                        status=('present' if same else ('window' if win else ('absent' if cr else 'unknown'))), collocates=sorted(cr)[:6]))
    return out


def render_supp(ref, D=None, parts='ABCDEFG'):
    import digest
    init()
    if D is None: D = digest.build(ref)
    L = [f"# supplements {ref} (script-built; orderings and paths, not verdicts)"]
    focus_roots = sorted({x[0] for x in AR[ref]} - {'ء ل ه'}, key=lambda r: DF[r])
    if 'A' in parts:
        L.append("## A. Every Quranic use of the ayah's roots (frames = collocate roots shared by ≥2 uses)")
        for r in focus_roots:
            f = frames(r, ref)
            if 'frames' not in f:
                L.append(f"- {r}: {f['n_words']} words in {f['n_ayat']} ayat ({f['profile']})"); continue
            fr = ' | '.join(f['frames']) or '-'
            L.append(f"- {r}: {f['n_words']} words in {f['n_ayat']} ayat. {fr}. other: {', '.join(f['other'][:30])}. this ayah in frame: {', '.join(f['focus_frames']) or 'none'}")
            if f['snippets'] and f['n_ayat'] <= 24:
                L.append('  ' + ' / '.join(f"{a} {t}" for a, t in sorted(f['snippets'].items(), key=lambda x: lib.refkey(x[0]))))
    if 'B' in parts:
        ch = channels(ref)
        L.append(f"## B. Existing surah image chains touching {ref} (network-v3 channel review; {len(ch)} subchannels)")
        for c in ch:
            L.append(f"- {c['parent']} / {c['sub']} [{c['reading_type']}] invariant: {c['invariant']} | here: {c['anchor']} | motifs: {c['motifs']}")
    if 'C' in parts:
        same, other = parallels(ref)
        L.append("## C. Parallels by shared roots (IDF-weighted; ordering only)")
        L.append("- same surah: " + '; '.join(f"{a} [{' '.join(r)}]" for s, a, r in same))
        L.append("- other surahs: " + '; '.join(f"{a} [{' '.join(r)}]" for s, a, r in other))
    if 'D' in parts:
        ec = early_citations(ref)
        L.append(f"## D. The early lexicographers on this ayah (six early sources + Majaz; {len(ec)} passages)")
        for root, src, bg, txt in ec:
            L.append(f"- {src} ({root}; '{bg}'): {txt}")
    if 'E' in parts:
        plain = []; seen_roots = set()
        rmap_ = lib.root_ar_map()
        for f in D['findings']:
            if f['plain']:
                for b in f['blist']:
                    if b.split('/')[0] not in seen_roots:
                        plain.append(b); seen_roots.add(b.split('/')[0])
        inv_ = collections.defaultdict(list)
        for rid, r in rmap_.items(): inv_[r].append(rid)
        for r in focus_roots:
            for rid in inv_.get(r, []):
                if rid not in seen_roots and f'{rid}/B001' in lib.dict_index()[0]:
                    plain.append(f'{rid}/B001'); seen_roots.add(rid)
        tk = turkish(ref, plain)
        L.append("## E. Turkish: baseline and what the gloss of each plain branch loses/adds")
        L.append(f"- baseline: {tk['baseline']}")
        for p in tk['profiles']:
            bits = [f"loses: {p['loses']}" if p['loses'] else '', f"adds: {p['adds']}" if p['adds'] else '', f"collision: {p['collision']}" if p['collision'] else '']
            ctx = '; '.join(f"'{c[0]}' loses {c[1]}" for c in p['contextual'] if c[1])
            L.append(f"- {p['branch']} '{p['gloss']}' " + ' '.join(x for x in bits if x) + (f" | {ctx}" if ctx else ''))
    if 'F' in parts:
        xs = xrefs(ref)
        L.append(f"## F. Definitional cross-references in the surah ({len(xs)}; a branch definition naming a word of another root present in the surah)")
        for sc, b, rn, gl, kind, rb, m, ays, bl in xs[:60]:
            L.append(f"- {rn} {','.join(bl)} [{kind}] '{gl}' names {'/'.join(m)} → {rb} at {', '.join(ays)}")
        if len(xs) > 60: L.append(f"- (+{len(xs)-60} more, lower rarity)")
    if 'G' in parts:
        g = guard(D)
        L.append(f"## G. Collocation-bound branches activated upstream ({len(g)}): the sense belongs to its construction")
        for x in g:
            L.append(f"- {x['root']} {x['branch'].split('/')[1]} '{x['gloss']}': construction {x['status']} in text | {x['note']}")
    return '\n'.join(L)


if __name__ == '__main__':
    refs = sys.argv[1:] or ['1:6', '1:2', '5:6', '18:86', '18:96', '100:1', '103:1']
    print('ref\tsupp_tok\tA\tB\tC\tD\tE\tF\tG')
    for r in refs:
        import digest
        D = digest.build(r)
        full = render_supp(r, D)
        open(f"{lib.W}/out/supp_{r.replace(':','_')}.txt", 'w').write(full)
        parts = {p: lib.est_tokens(render_supp(r, D, parts=p)) for p in 'ABCDEFG'}
        print(r, lib.est_tokens(full), *parts.values(), sep='\t')
