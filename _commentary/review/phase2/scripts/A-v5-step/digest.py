"""Prototype deterministic digest of v5's stored Luna/Astra discovery for one ayah.

Design (attention argument in the proposal):
 KEEP  - every distinct activated branch, grouped by root, with dictionary branch_kind, early-source phrase,
         carriers (surface words), triggers (resolved to ayah refs / words), and which findings use it
       - every finding's title + claim + payoff (one line each), branch list, cross-ayah refs
       - every set-aside candidate (reject / narrowed-away facets) with its CONTENT and a neutral cause class
         (binding / scope / semantic), never the verdict wording as a label
 DROP  - epistemic status, accept/narrow labels, trust labels, support ids, containment/boundary/mechanism prose,
         templated trigger sentences, duplicate activations, word-topic restatements of the plain sense
 FULL  - raw discovery JSON path printed in the header (one read away)
"""
import json, os, re, sys, collections
import lib

TEMPLATE = re.compile(r'(Independent contextual grounding enters at|The (context|focus) occurrence at \S+ carries the supplied branch sense)')
BIND = re.compile(r'(no exact|unanchored|without (an )?exact|zero exact|no (supplied )?(anchor|carrier|focus.return|trigger)|lacks? (an? )?(exact|anchor|carrier|focus)|not anchored|no focus-return|cannot be (anchored|bound)|anchor refs?)', re.I)
SCOPE = re.compile(r'(outside (this |the )?(lane|micro|macro|scope|pericope|packet)|belongs to (the )?(macro|global|micro)|another lane|not in (this|the) lane|lane boundary|routed)', re.I)
DUP = re.compile(r'(already represented|duplicate|represented by|covered by|same (mechanism|reading) as|repeats)', re.I)


def reason_class(r):
    r = r or ''
    if DUP.search(r): return 'dup'
    if SCOPE.search(r): return 'scope'
    if BIND.search(r): return 'binding'
    return 'semantic'


def surf_of(qref, surf):
    # qref like 18:86:10:1 or 18:86:10
    p = qref.split(':')
    if len(p) >= 3:
        return surf.get(':'.join(p[:3]), '')
    return ''


def word_surfaces(ref):
    """word ref S:A:W -> surface, from the ayah text (split on spaces; QAC word index is 1-based)"""
    t = lib.quran_text()
    out = {}
    s, a = ref.split(':')
    words = [w for w in t.get(ref, '').split() if re.search(r'[\u0621-\u064A\u0671]', w)]
    for i, w in enumerate(words, 1):
        out[f'{s}:{a}:{i}'] = w
    return out


def build(ref, disc=None, packets=None, raw_dir=None, include_rejects=True, include_micro_plain=False):
    idx, roots = lib.dict_index()
    rmap = lib.root_ar_map()
    if disc is None:
        disc, raw_dir = lib.load_discovery(ref)
    if packets is None:
        packets = {l: lib.load_packet(ref, l, raw_dir) for l in disc}
    # surfaces for any ayah referenced
    surf_cache = {}

    def surf(qref):
        p = qref.split(':')
        if len(p) < 3: return ''
        ay = ':'.join(p[:2])
        if ay not in surf_cache:
            surf_cache[ay] = word_surfaces(ay)
        return surf_cache[ay].get(':'.join(p[:3]), '')

    conn = {}; cands = {}
    for l, pk in packets.items():
        if not pk: continue
        for c in pk.get('connection_registry', []):
            conn[c['connection_ref']] = c.get('target_ref') or c.get('source_target_ref')
        for c in pk.get('candidate_inventory', []):
            cands[c['candidate_id']] = c

    def trig(t):
        if t.startswith('conn_'):
            return '→' + str(conn.get(t, '?'))
        if re.match(r'^\d+:\d+:\d+', t):
            w = surf(t)
            return f'{":".join(t.split(":")[:3])} {w}'
        return t

    branches = collections.OrderedDict()  # bref -> info
    findings = []
    stats = collections.Counter()
    for l in lib.LANES:
        d = disc.get(l)
        if not d: continue
        for f in d.get('findings', []):
            acts = [a for a in (f.get('branch_activations') or []) if isinstance(a, dict)]
            stats['findings'] += 1
            stats['acts'] += len(acts)
            if l == 'micro' and not include_micro_plain:
                # skip word-topic restatements: findings whose activations are all lexical and of the word's plain branch B001
                if acts and all(a.get('application_mode') == 'lexical' for a in acts) and not f.get('connection_refs'):
                    stats['micro_plain_skipped'] += 1
                    # still index branches (so nothing silently vanishes from the branch index)
            fid = f"{l[:2]}{len(findings)+1}"
            xrefs = set()
            blist = []
            for a in acts:
                b = a.get('branch_ref')
                if not b: continue
                if TEMPLATE.match(str(a.get('independent_trigger', ''))): stats['templated'] += 1
                bi = branches.setdefault(b, dict(lanes=set(), modes=collections.Counter(), carriers=set(), triggers=set(), fids=[], gloss=a.get('branch_gloss')))
                bi['lanes'].add(l); bi['modes'][a.get('application_mode')] += 1
                for c in a.get('carrier_refs') or []:
                    bi['carriers'].add(f'{":".join(c.split(":")[:3])} {surf(c)}'.strip())
                for t in (a.get('trigger_refs') or []):
                    tt = trig(t); bi['triggers'].add(tt)
                    if tt.startswith('→'): xrefs.add(tt[1:])
                    elif re.match(r'^\d+:\d+', tt) and not tt.startswith(ref + ':'): xrefs.add(':'.join(tt.split(':')[:2]))
                for c in a.get('carrier_refs') or []:
                    if not c.startswith(ref + ':'): xrefs.add(':'.join(c.split(':')[:2]))
                if fid not in bi['fids']: bi['fids'].append(fid)
                if b not in blist: blist.append(b)
            for c in f.get('connection_refs') or []:
                xrefs.add(str(conn.get(c, c)))
            for c in f.get('context_refs') or []:
                if re.match(r'^\d+:\d+$', str(c)) and c != ref: xrefs.add(c)
            findings.append(dict(fid=fid, lane=l, title=f.get('title', ''), claim=f.get('claim', ''), payoff=f.get('reader_payoff', ''),
                                 blist=blist, xrefs=sorted(x for x in xrefs if x and x != 'None'), plain=(l == 'micro' and acts and all(a.get('application_mode') == 'lexical' for a in acts))))
    # set-asides
    sets = []
    for l in lib.LANES:
        d = disc.get(l)
        if not d: continue
        for c in d.get('candidate_decisions', []):
            dec = c.get('decision')
            excl = []
            for k in ('branch_exclusions', 'facet_exclusions', 'context_exclusions'):
                for e in c.get(k) or []:
                    excl.append(e if isinstance(e, str) else (e.get('branch_ref') or e.get('facet_id') or e.get('context_ref') or '') + ((': ' + e.get('reason', '')) if isinstance(e, dict) and e.get('reason') else ''))
            if dec == 'reject' or (dec == 'narrow' and excl):
                cd = cands.get(c['candidate_id'], {})
                if cd.get('kind') == 'focus_root_occurrence':
                    stats['dropped_root_occurrence_setaside'] += 1
                    continue
                cls = reason_class((c.get('reason') or '') + ' ' + ' '.join(excl))
                if re.search(r'(not (locally )?supplied|not a supplied context|micro packet|outside the micro|require[s]? macro|cannot be local)', ' '.join(excl) + ' ' + (c.get('reason') or ''), re.I):
                    cls = 'scope'
                sets.append(dict(lane=l, dec=dec, cls=cls, kind=cd.get('kind', '?'),
                                 title=(cd.get('title') or cd.get('item_id') or cd.get('source_local_id') or c['candidate_id']),
                                 branches=cd.get('branch_refs') or cd.get('nominated_branch_refs') or [],
                                 reason=c.get('reason', ''), excl=excl))
    return dict(ref=ref, raw_dir=raw_dir, branches=branches, findings=findings, sets=sets, stats=stats)


def render(D, variant='full'):
    """variant: 'full' (branch index + findings + set-asides), 'nosets', 'branches_only'"""
    idx, roots = lib.dict_index()
    rmap = lib.root_ar_map()
    ref = D['ref']
    L = []
    L.append(f"# v5 harvest digest {ref}")
    L.append(f"source: {D['raw_dir']}/{{micro,macro,global}}.discovery.json (full records one read away)")
    L.append(f"counts: {D['stats']['findings']} findings, {len(D['branches'])} distinct branches, {len(D['sets'])} set-aside items")
    L.append("labels removed: accept/narrow/reject, grounded/qualified/exploratory, trust. branch_kind from the project dictionary.")
    L.append("")
    L.append("## Branches (every branch of every root of the ayah, activated or not, plus other activated branches; kind; early-source phrase; carriers; triggers; findings)")
    byroot = collections.OrderedDict()
    for b, bi in D['branches'].items():
        rid = b.split('/')[0]
        byroot.setdefault(rid, []).append((b, bi))
    # focus roots from the concordance
    inv = collections.defaultdict(list)
    for rid_, r_ in rmap.items(): inv[r_].append(rid_)
    focus_rids = set()
    for root_, occ_ in lib.concordance().items():
        if any(a_ == ref for a_, *_ in occ_):
            for rid_ in inv.get(root_, []): focus_rids.add(rid_)
    for b_ in idx:
        rid_ = b_.split('/')[0]
        if rid_ in focus_rids and b_ not in D['branches']:
            byroot.setdefault(rid_, []).append((b_, None))
    for rid in sorted(byroot, key=lambda r: -sum(len(bi['fids']) for _, bi in byroot[r] if bi)):
        n = (roots.get(rid) or {}).get('n_words')
        L.append(f"### {rmap.get(rid, rid)} ({rid}; Quran words: {n})")
        for b, bi in sorted(byroot[rid], key=lambda x: x[0]):
            di = idx.get(b, {})
            if bi is None:
                ph0 = (di.get('phrase_ar') or '').split('؛')[0][:160]
                L.append(f"- {b.split('/')[1]} [{di.get('kind') or '?'}] {di.get('gloss') or ''} | {ph0} | not activated upstream" + (f" | SCOPE: {di.get('note','')}" if di.get('kind') == 'collocation' else ''))
                continue
            kind = di.get('kind') or '?'
            ph = (di.get('phrase_ar') or '')
            ph = ph.split('؛')[0][:160]
            gl = di.get('gloss') or bi.get('gloss') or ''
            car = '; '.join(sorted(bi['carriers'])[:4]) + (f' (+{len(bi["carriers"])-4})' if len(bi['carriers']) > 4 else '')
            trg = '; '.join(sorted(bi['triggers'])[:5]) + (f' (+{len(bi["triggers"])-5})' if len(bi['triggers']) > 5 else '')
            line = f"- {b.split('/')[1]} [{kind}] {gl} | {ph} | carriers: {car} | triggers: {trg} | in: {','.join(bi['fids'][:12])}{'…' if len(bi['fids'])>12 else ''}"
            if kind == 'collocation':
                line += f" | SCOPE: {di.get('note','')}"
            L.append(line)
    if variant == 'branches_only':
        return '\n'.join(L)
    L.append("")
    if variant == 'packet':
        L.append("## Coalitions found upstream (title; branches grouped together; other ayat). Claims one read away.")
        groups = collections.OrderedDict(); notes = []
        for f in D['findings']:
            if f['plain']: continue
            if not f['blist']:
                notes.append(f['title']); continue
            k = tuple(sorted(f['blist']))
            g = groups.setdefault(k, dict(titles=[], fids=[], xrefs=set()))
            g['titles'].append(f['title']); g['fids'].append(f['fid']); g['xrefs'] |= set(f['xrefs'])
        for k, g in groups.items():
            bl = ','.join(f"{rmap.get(b.split('/')[0], b.split('/')[0])}/{b.split('/')[1]}" for b in k[:12])
            xr = ','.join(sorted(g['xrefs'], key=lib.refkey)[:10])
            L.append(f"- {g['fids'][0]}{'+'+str(len(g['fids'])-1) if len(g['fids'])>1 else ''} {' / '.join(dict.fromkeys(g['titles']))[:300]} [{bl}]" + (f" [ayat: {xr}]" if xr else ''))
        if notes:
            L.append(f"- word notes ({len(notes)}): " + ' | '.join(dict.fromkeys(notes)))
        plain = [f for f in D['findings'] if f['plain']]
        if plain:
            L.append(f"- plain-sense word findings ({len(plain)}): " + ' | '.join(f['title'] for f in plain))
    else:
      L.append("## Findings (one line each; lane; branches; other ayat)")
    for f in (D['findings'] if variant != 'packet' else []):
        if f['plain']:
            continue
        bl = ','.join(f"{rmap.get(b.split('/')[0], b.split('/')[0])}/{b.split('/')[1]}" for b in f['blist'][:10])
        xr = ','.join(f['xrefs'][:10])
        L.append(f"- {f['fid']} {f['title']}: {f['claim']} Payoff: {f['payoff']} [{bl}]" + (f" [ayat: {xr}]" if xr else ''))
    plain = [f for f in D['findings'] if f['plain']]
    if plain and variant != 'packet':
        L.append(f"- plain-sense word findings ({len(plain)}): " + ' | '.join(f['title'] for f in plain))
    if variant == 'nosets':
        return '\n'.join(L)
    L.append("")
    L.append("## Set aside upstream (content kept; cause class: binding = could not be anchored inside the lane packet; scope = outside the lane; dup; semantic)")
    for s in D['sets']:
        bl = ','.join(f"{rmap.get(b.split('/')[0], b.split('/')[0])}/{b.split('/')[1]}" for b in s['branches'][:8])
        exb = sorted({m for x in s['excl'] for m in re.findall(r'root_\d+/B\d+', x)})
        ex = ('; branches set aside: ' + ','.join(f"{rmap.get(b.split('/')[0], b.split('/')[0])}/{b.split('/')[1]}" for b in exb)) if exb else ''
        L.append(f"- [{s['lane']} {s['cls']}] ({s['kind']}) {s['title'][:300]} [{bl}]{ex}")
    return '\n'.join(L)


if __name__ == '__main__':
    refs = sys.argv[1:] or ['1:6', '1:2', '5:6', '18:86', '18:96', '100:1', '103:1']
    os.makedirs(lib.W + '/out', exist_ok=True)
    print('ref\tfindings\tacts\tbranches\tsets\ttemplated\tv5_disc_bytes\tfull_bytes\tfull_tok\tnosets_tok\tbranches_tok\tbytes/4')
    for r in refs:
        D = build(r)
        disc_bytes = sum(os.path.getsize(f"{D['raw_dir']}/{l}.discovery.json") for l in lib.LANES if os.path.exists(f"{D['raw_dir']}/{l}.discovery.json"))
        full = render(D, 'full'); nos = render(D, 'nosets'); bo = render(D, 'branches_only')
        open(f"{lib.W}/out/digest_{r.replace(':','_')}.txt", 'w').write(full)
        print(f"{r}\t{D['stats']['findings']}\t{D['stats']['acts']}\t{len(D['branches'])}\t{len(D['sets'])}\t{D['stats']['templated']}\t{disc_bytes}\t{len(full.encode())}\t{lib.est_tokens(full)}\t{lib.est_tokens(nos)}\t{lib.est_tokens(bo)}\t{len(full.encode())//4}")
