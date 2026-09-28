"""Watch-case ingredient check in the stored v5 harvest (evaluation only; nothing here enters a prompt).
For each ingredient branch: where it is activated in findings (with the candidate decision that owns the finding),
where it only appears in set-aside candidates or exclusions, and whether it reaches the editorial."""
import json, os, re, glob, collections, sys
import lib

rm = lib.root_ar_map()


def branch_outcomes(disc, packets, targets):
    """targets: set of branch refs. returns {bref: [(lane, outcome, finding_title/candidate, triggers)]}"""
    out = collections.defaultdict(list)
    for l, d in disc.items():
        dec = {c['candidate_id']: c for c in d.get('candidate_decisions', [])}
        cands = {c['candidate_id']: c for c in (packets.get(l) or {}).get('candidate_inventory', [])} if packets.get(l) else {}
        conn = {c['connection_ref']: c.get('target_ref') for c in (packets.get(l) or {}).get('connection_registry', [])} if packets.get(l) else {}
        for f in d.get('findings', []):
            oc = f.get('origin_candidate_id')
            o = dec.get(oc, {}).get('decision', 'uncandidate') if oc else 'uncandidate'
            for a in f.get('branch_activations') or []:
                if not isinstance(a, dict): continue
                if a.get('branch_ref') in targets:
                    trg = [('→' + str(conn.get(t, t))) if t.startswith('conn_') else t for t in a.get('trigger_refs') or []]
                    out[a['branch_ref']].append((l, 'finding/' + o, f.get('title', '')[:80], a.get('application_mode'), ';'.join(trg)[:120], (a.get('resulting_reading') or '')[:160]))
        for cid, c in dec.items():
            cd = cands.get(cid, {})
            brs = set(cd.get('branch_refs') or []) | set(cd.get('nominated_branch_refs') or [])
            for b in brs & targets:
                if c['decision'] == 'reject':
                    out[b].append((l, 'candidate/reject', (cd.get('title') or cd.get('item_id') or '')[:80], cd.get('kind'), '', (c.get('reason') or '')[:200]))
            for e in c.get('branch_exclusions') or []:
                eb = e if isinstance(e, str) else e.get('branch_ref')
                if eb in targets:
                    out[eb].append((l, 'excluded_in_' + c['decision'], (cd.get('title') or '')[:80], '', '', json.dumps(e, ensure_ascii=False)[:200]))
    return out


def editorial_text(ref):
    s, a = ref.split(':')
    ps = glob.glob(f'{lib.V5}/editorial/*/s{int(s):03d}/{s}_{a}/{s}_{a}.prose.editorial.tr.md')
    ps = [p for p in ps if 'basmala' not in p]
    return open(ps[0]).read() if ps else ''


def middle_text(ref):
    s, a = ref.split(':')
    ps = glob.glob(f'{lib.V5}/middle/*/s{int(s):03d}/{s}_{a}/{s}_{a}.prose.middle.tr.md')
    return open(ps[0]).read() if ps else ''


def refs_in(text, refs):
    return {r: len(re.findall(r'(?<![\d:])' + re.escape(r) + r'(?![\d])', text)) for r in refs}


def run_fatiha():
    ING = {
        'road: waymark (ʿalam, 1:2)': 'root_001040/B002',
        'road: road middle (malik, 1:4)': 'root_001444/B006',
        'herd: lead animal (malik, 1:4)': 'root_001444/B008',
        'road: trodden road (naʿbudu, 1:5)': 'root_000973/B005',
        'road: swallowing road (ṣirāṭ, 1:6)': 'root_000858/B002',
        'herd: stray whose rabb is unknown (ḍāllīn, 1:7)': 'root_000913/B005',
        'water: abundant gathered water (rabb)': 'root_000532/B013',
        'water: cloud layers (rabāb)': 'root_000532/B008',
        'water: sea / abundant-water well (ʿaylam)': 'root_001040/B005',
        'water: water that sustains (malik)': 'root_001444/B007',
        'water: well frame / pulley (qāma, mustaqīm)': 'root_001273/B012',
        'herd: wild-cattle herd (rabrab)': 'root_000532/B014',
        'herd: wild-ass herd (ʿāna, nastaʿīn)': 'root_001064/B006',
        'herd: livestock (anʿamta)': 'root_001525/B005',
        'herd: the one in front (hādī)': 'root_001583/B003',
    }
    targets = set(ING.values())
    res = {}
    for ay in ['1:1', '1:2', '1:3', '1:4', '1:5', '1:6', '1:7']:
        disc, rd = lib.load_discovery(ay)
        packets = {l: lib.load_packet(ay, l, rd) for l in disc}
        bo = branch_outcomes(disc, packets, targets)
        res[ay] = bo
    table = []
    for name, b in ING.items():
        row = {'ingredient': name, 'branch': b, 'kind': lib.dict_index()[0].get(b, {}).get('kind')}
        for ay, bo in res.items():
            outs = collections.Counter(o[1] for o in bo.get(b, []))
            if outs: row[ay] = dict(outs)
        table.append(row)
    return table, res


def run_18_86():
    ay = '18:86'
    disc, rd = lib.load_discovery(ay)
    packets = {l: lib.load_packet(ay, l, rd) for l in disc}
    R = ['15:26', '15:28', '15:33', '55:14', '15:29', '38:71', '38:72', '18:50', '17:61', '7:12', '38:76', '23:12', '32:7']
    rep = {}
    # pushed rows
    for l, pk in packets.items():
        if not pk: continue
        rows = [c for c in pk.get('connection_registry', []) if c.get('target_ref') in R]
        rep[f'{l}_pushed_rows'] = [(c['target_ref'], c.get('prior_label'), (c.get('note') or '')[:140]) for c in rows]
    # used anywhere in lane output
    for l, d in disc.items():
        s = json.dumps(d, ensure_ascii=False)
        conns = {c['connection_ref']: c['target_ref'] for c in (packets.get(l) or {}).get('connection_registry', [])}
        used = collections.Counter()
        for cref, t in conns.items():
            if t in R and cref in s: used[t] += s.count(cref)
        rep[f'{l}_output_refs'] = dict(used)
        rep[f'{l}_literal_refs'] = {k: v for k, v in refs_in(s, R).items() if v}
    rep['editorial_refs'] = {k: v for k, v in refs_in(editorial_text(ay), R).items() if v}
    rep['canonical_prose_refs'] = {k: v for k, v in refs_in(open(rd + '/18_86.prose.tr.md').read(), R).items() if v}
    # inter-ayah ledger (separate exhaustive test)
    led = json.load(open(rd + '/global.inter-ayah.ledger.json'))
    rows = led.get('rows') or led.get('ledger') or led.get('connections') or []
    if isinstance(led, dict) and not rows:
        for k, v in led.items():
            if isinstance(v, list) and v and isinstance(v[0], dict): rows = v; break
    hits = []
    for r in rows:
        s = json.dumps(r, ensure_ascii=False)
        for t in R[:4]:
            if f'"{t}"' in s:
                hits.append((t, {k: (str(v)[:200]) for k, v in r.items() if k in ('surprise_strength', 'relation', 'relation_type', 'verdict', 'decision', 'activated_focus_branches', 'summary', 'finding', 'reading', 'strength')}))
                break
    rep['inter_ayah_ledger_keys'] = list(led.keys())[:20] if isinstance(led, dict) else 'list'
    rep['inter_ayah_ledger_hits'] = hits[:8]
    rep['inter_ayah_prose_refs'] = {k: v for k, v in refs_in(open(rd + '/18_86.global.inter-ayah.prose.tr.md').read(), R).items() if v}
    return rep


def run_18_96():
    ay = '18:96'
    disc, rd = lib.load_discovery(ay)
    packets = {l: lib.load_packet(ay, l, rd) for l in disc}
    nfkh = [k for k, v in rm.items() if v == 'ن ف خ'][0]
    idx = lib.dict_index()[0]
    nbr = sorted(b for b in idx if b.startswith(nfkh + '/'))
    R = ['15:29', '38:72', '32:9', '3:49', '5:110', '21:91', '66:12', '18:99', '36:51', '39:68', '69:13', '6:73', '20:102', '23:101', '27:87', '50:20', '78:18', '74:8']
    rep = {'nafakha_branches': [(b, idx[b]['kind'], idx[b]['gloss']) for b in nbr]}
    acts = []
    for l, d in disc.items():
        for f in d.get('findings', []):
            for a in f.get('branch_activations') or []:
                if isinstance(a, dict) and a.get('branch_ref', '').startswith(nfkh + '/'):
                    acts.append((l, a['branch_ref'], a.get('application_mode'), f.get('title', '')[:70], (a.get('resulting_reading') or '')[:200]))
    rep['nafakha_activations'] = acts
    for l, pk in packets.items():
        if not pk: continue
        rows = [c for c in pk.get('connection_registry', []) if c.get('target_ref') in R]
        rep[f'{l}_pushed_rows'] = [(c['target_ref'], c.get('prior_label')) for c in rows]
    for l, d in disc.items():
        s = json.dumps(d, ensure_ascii=False)
        conns = {c['connection_ref']: c['target_ref'] for c in (packets.get(l) or {}).get('connection_registry', [])}
        used = collections.Counter()
        for cref, t in conns.items():
            if t in R and cref in s: used[t] += 1
        rep[f'{l}_output_refs'] = dict(used)
        rep[f'{l}_literal_refs'] = {k: v for k, v in refs_in(s, R).items() if v}
    rep['editorial_refs'] = {k: v for k, v in refs_in(editorial_text(ay), R).items() if v}
    s = editorial_text(ay)
    rep['editorial_words'] = len(s.split())
    rep['editorial_animat_terms'] = {w: len(re.findall(w, s, re.I)) for w in ['can ver', 'hayat', 'ruh', 'dirilt', 'körük', 'üfle']}
    return rep


def run_29_38():
    base = lib.W + '/git2938'
    disc = {l: json.load(open(f'{base}/{l}.discovery.json')) for l in lib.LANES}
    idx = lib.dict_index()[0]
    sbl = [k for k, v in rm.items() if v == 'س ب ل'][0]
    rep = {'sbl_root': sbl, 'eye_film_kind': idx.get(sbl + '/B010', {}).get('kind')}
    acts = []
    for l, d in disc.items():
        for f in d.get('findings', []):
            for a in f.get('branch_activations') or []:
                if isinstance(a, dict) and a.get('branch_ref') == sbl + '/B010':
                    acts.append(dict(lane=l, title=f.get('title'), claim=f.get('claim', '')[:300], carriers=a.get('carrier_refs'), triggers=a.get('trigger_refs'), mode=a.get('application_mode'), reading=(a.get('resulting_reading') or '')[:300]))
    rep['eye_film_activations'] = acts
    s = json.dumps(disc, ensure_ascii=False)
    rep['mentions'] = {k: s.count(k) for k in ['29:41', 'عنكبوت', 'ٱلْعَنكَبُوتِ', 'spider', 'örümcek', 'kohl', 'sürme', 'كحل', 'mustab', 'zayyana', 'زين']}
    pr = open(base + '/29_38.prose.tr.md').read()
    rep['canonical_prose'] = {k: pr.count(k) for k in ['29:41', 'örümcek', 'göz perdesi', 'perde', 'sürme', 'السبل', 'سَبَل', 'kırmızı damar']}
    return rep


if __name__ == '__main__':
    out = {}
    t, res = run_fatiha()
    out['fatiha'] = t
    out['fatiha_detail'] = {ay: {b: v for b, v in bo.items()} for ay, bo in res.items()}
    out['18:86'] = run_18_86()
    out['18:96'] = run_18_96()
    out['29:38'] = run_29_38()
    json.dump(out, open(lib.W + '/out/watch.json', 'w'), ensure_ascii=False, indent=1)
    for row in t:
        print(row)
    for k in ['18:86', '18:96', '29:38']:
        print('=====', k)
        print(json.dumps(out[k], ensure_ascii=False, indent=1)[:6000])
