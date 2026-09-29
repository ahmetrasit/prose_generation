"""Secondary, IN-SAMPLE check: which link types connect the 29:38 cold-Opus links
(_commentary/v9/network/eval_29_38.py GOLD, 19 links + 1 control) to their partner word.
The partner word of each gold link is read off the gold's own description (F:w = the 29:38 word; A:ref = the word in
the context ayah that the description names). Base rates as on the HFT set: (a) same branch, other words of the
partner's ayah; (b) other branches of the same root, same partner. 29:38 is a named watch case: this check can
never select or tune a threshold; it is reported only. Writes results_29_38.json."""
import sys, os, json
sys.dont_write_bytecode = True
import lib, links

X0 = (29, 38)
# (root, branch, partner ayah, partner root, note) -- partner roots read from eval_29_38.py descriptions
GOLD = [
    ('ع و د', 'B009', (29, 38), 'س ب ل', 'old road -> al-sabil'),
    ('ع م ل', 'B011', (29, 38), 'س ب ل', 'trodden road -> al-sabil'),
    ('ص د د', 'B004', (29, 38), 'س ب ل', 'road to water -> al-sabil'),
    ('ص د د', 'B013', (29, 38), 'ب ص ر', 'kohl -> mustabsirin'),
    ('س ب ل', 'B010', (29, 38), 'ب ص ر', 'eye-film -> mustabsirin'),
    ('ب ي ن', 'B007', (29, 38), 'ب ص ر', 'land as far as the eye reaches -> mustabsirin'),
    ('ع م ل', 'B010', (29, 38), 'ب ص ر', 'far-seeing eye -> mustabsirin'),
    ('ز ي ن', 'B001', (29, 38), 'ش ط ن', "beauty 'opposite of shayn' <-> al-shaytan"),
    ('ش ط ن', 'B005', (29, 38), 'ز ي ن', 'ugly snake <-> zayyana'),
    ('ش ط ن', 'B003', (29, 38), 'ص د د', "turning from one's direction <-> saddahum"),
    ('س ب ل', 'B010', (29, 41), 'ع ن ك ب', 'eye-film like spider web <-> 29:41 spider'),
    ('س ك ن', 'B004', (29, 37), 'ص ب ح', 'night as rest <-> destroyed by morning'),
    ('ص د د', 'B005', (7, 74), 'ج ب ل', 'barrier mountain <-> carving mountains'),
    ('ص د د', 'B002', (89, 9), 'و د ي', 'valley sides <-> in the valley'),
    ('س ب ل', 'B005', (46, 24), 'م ط ر', 'rain <-> cloud bringing rain'),
    ('ش ط ن', 'B001', (11, 68), 'ب ع د', "distance <-> 'away with Thamud'"),
    ('ز ي ن', 'B001', (29, 7), 'ح س ن', 'beauty <-> ahsana'),
    ('ع م ل', 'B012', (29, 29), 'ق ط ع', 'foot travellers <-> cutting the road'),
    ('س ب ل', 'B010', (1, 6), 'ق و م', "eye-film <-> q-w-m 'eye standing, sight gone'"),
]
CONTROL = ('س ك ن', 'B007', (29, 29), 'ق ط ع', 'control: knife <-> cutting (Opus rejected)')


def key(root, bid):
    ks = [k for k in lib.ROOT_BR.get(root, ()) if k[1] == bid]
    return ks[0] if ks else None


def main():
    out = dict(items=[], per_type={})
    names = list(links.TYPES)
    tot = {n: dict(hits=0, exp_a=0.0, exp_b=0.0) for n in names}
    for root, bid, Y, pr, note in GOLD + [CONTROL]:
        T = key(root, bid)
        ctrl = (root, bid, Y, pr, note) == CONTROL
        fired = {}
        others = [w['roots'][0] for w in lib.BY_AYAH[Y] if w['roots'] and w['roots'][0] not in (root, pr)]
        ob = [k for k in lib.RID_BR[T[0]] if k != T]
        for n in names:
            fam, scope, f = links.TYPES[n]
            el = f(T, pr, X0)
            if el:
                fired[n] = str(el)
            if not ctrl:
                tot[n]['hits'] += bool(el)
                tot[n]['exp_a'] += (sum(1 for r in others if f(T, r, X0)) / len(others)) if others else 0
                tot[n]['exp_b'] += (sum(1 for t in ob if f(t, pr, X0)) / len(ob)) if ob else 0
        out['items'].append(dict(branch=f'{root} {bid}', partner=f'{pr} @ {Y[0]}:{Y[1]}', note=note, control=ctrl,
                                 fired=fired))
    for n in names:
        t = tot[n]
        out['per_type'][n] = dict(hits=t['hits'], of=len(GOLD), expected_base_a=round(t['exp_a'], 2),
                                  expected_base_b=round(t['exp_b'], 2))
    json.dump(out, open(os.path.join(lib.HERE, 'results_29_38.json'), 'w'), ensure_ascii=False, indent=1)
    for it in out['items']:
        print(('CTRL ' if it['control'] else '     ') + it['branch'], '->', it['partner'], '|', ', '.join(sorted(it['fired'])))
    print()
    for n in names:
        p = out['per_type'][n]
        print(f"{n:24s} hits {p['hits']:2d}/{p['of']}  exp(a) {p['expected_base_a']:5.2f}  exp(b) {p['expected_base_b']:5.2f}")


if __name__ == '__main__':
    main()
