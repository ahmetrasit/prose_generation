"""Build the user's AUDIT SHEET (audit_sheet.md) and its key (audit_key.tsv).

Part A: 60 seeded root-dossier placements of collocation-bound branches (the evaluation set without the two
        grammatical constructions and without ء ت ي B011), round-robin over branches so that no branch dominates.
        The user marks whether the construction is really there.
Part B: 30 seeded collocation-bound and 30 seeded bare branch_kind labels, with the dossier's own placement of the
        branch as an example when there is one (no random example: a random occurrence of the root is usually of
        another branch). The user marks whether the label is right.
Part C: precision. 30 seeded 'present' calls of the detector away from dossier placements (lexeme and formula calls
        among them), mixed with 10 seeded 'absent' calls, shuffled. The user marks whether the construction is there.
The detector's calls are never shown on the sheet (they would anchor the answer); they are in audit_key.tsv.
Questions are asked positively (✓ = yes). This sheet is for the user only; nothing in it goes into a model's input.
"""
import sys, os, re, random, collections, csv, json
sys.dont_write_bytecode = True
import gdata as G
import detector as Dt
import eval_dossier as E

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20260928
SRC_NAMES = {'ayn': 'el-Ayn', 'maqayis': 'Makâyîs', 'jamhara': 'Cemhere', 'sihah': 'Sıhâh', 'tahdhib': 'Tehzîb',
             'mufradat': 'Müfredât'}

REASON_TR = {
    'partner': 'sözlükteki eş kelime burada bu kelimeye dilbilgisel olarak bağlı',
    'partner-2hop': 'sözlükteki eş kelime aynı söz öbeğinde, bir kelime ötede',
    'partner-def': 'bağlı kelimenin kendi sözlük tanımı eş kelimeyi içeriyor (ör. bir ateş adı)',
    'partner-other-form': 'eş kelime burada, ama fiilin biçimi sözlüktekinden farklı',
    'prep': 'sözlükteki edat burada bu kelimeye bağlı',
    'object': 'sözlükteki kalıp bir nesne istiyor; burada nesne var',
    'form': 'sözlük bu anlamı fiilin bu türemiş biçimine tek başına veriyor; burada o biçim var',
    'form-named': 'sözlük fiilin bu türemiş biçimini anıyor; burada o biçim var',
    'formula': 'sözlükteki kalıp kelimesi kelimesine burada',
    'lexeme': 'sözlüğün andığı kelime biçimi burada',
    'construction not found': 'sözlükteki kalıbın parçaları (eş kelime / edat / biçim) burada bulunamadı',
    'no checkable construction (bare Form I or no head word found)':
        'sözlükteki kalıp betiğin denetleyebileceği biçimde yazılmamış',
    'no grammar data for this word': 'bu kelime için dilbilgisi verisi yok',
    'prep-lam': 'kalıp yalnız çok yaygın "li" edatına dayanıyor',
    'object-formI': 'kalıp yalnız "düz bir nesne" istiyor; bu, fiilin sıradan kullanımından ayırt edilemiyor',
    'prep-other-form': 'edat burada, ama fiilin biçimi sözlüktekinden farklı',
    'subject-pronoun': 'kalıbın öznesi burada zamir olabilir; betik çözemiyor',
    'partner-win': 'eş kelime yakında ama dilbilgisel olarak bu kelimeye bağlı değil',
    'partner-before-pronoun': 'eş kelime zamirin gönderdiği yerde olabilir; betik emin değil',
}
CALL_TR = {'present': 'VAR', 'absent': 'YOK', 'unknown': 'BELİRSİZ'}


def reason_tr(why):
    parts = [p.strip() for p in why.split(';')]
    head = REASON_TR.get(parts[0], parts[0])
    tail = ''
    for p in parts[1:]:
        m = re.match(r'outranked by (B\d+)', p)
        if m:
            tail = f'; ama başka bir dalın ({m.group(1)}) kalıbı burada daha iyi uyuyor'
        m = re.match(r'shared with (B\d+)', p)
        if m:
            tail = f'; aynı kalıp {m.group(1)} dalında da var, betik ayıramıyor'
        if 'too common' in p:
            tail = '; betik karar veremiyor'
        if 'not grammatically linked' in p:
            tail = '; betik karar veremiyor'
    return head + tail


def ayah_snippet(ref3, width=7):
    W = G.words()
    d = W[ref3]
    ay = G.ayah_words()[(d['s'], d['a'])]
    k = ay.index(ref3)
    lo, hi = max(0, k - width), min(len(ay), k + width + 1)
    toks = []
    for j in range(lo, hi):
        s = W[ay[j]]['surface']
        toks.append(f'**{s}**' if j == k else s)
    return ('… ' if lo > 0 else '') + ' '.join(toks) + (' …' if hi < len(ay) else '')


def first_phrase(b):
    # split on the Arabic semicolon, or on ';' outside a source tag: '(ayn;tahdhib)' is one tag
    for seg in re.split(r'؛|;(?![^()]*\))', b['phrase'] or ''):
        seg = seg.strip()
        if seg:
            m = re.search(r'\(([a-z_;\- 0-9]+)\)\s*$', seg)
            src = ''
            if m:
                src = ', '.join(SRC_NAMES.get(re.sub(r'-v\d+$', '', x.strip()), x.strip()) for x in m.group(1).split(';'))
                seg = seg[:m.start()].strip()
            return seg + (f' ({src})' if src else '')
    return ''


def main_statement(ref):
    """the dictionary's own construction statement for the branch (first lexical unit, else first phrase)."""
    for u in G.lexunits().get((G.dictionary()['branches'][ref]['root_id'], ref.split('/')[1]), []):
        if u['expr']:
            return u['expr']
    return first_phrase(G.dictionary()['branches'][ref])


def statements_shown(ref, k=3):
    """the branch's own construction statements (lexical units, up to k), the same for every row of the branch
    whatever the detector matched, so that the sheet does not show which statement the script used."""
    out = []
    for u in G.lexunits().get((G.dictionary()['branches'][ref]['root_id'], ref.split('/')[1]), []):
        if u['expr'] and u['expr'] not in out:
            out.append(u['expr'])
    return out[:k] or [first_phrase(G.dictionary()['branches'][ref])]


def cell(s):
    return (s or '').replace('|', '/').replace('\n', ' ').strip()


def part_a(rng):
    pos, _ = E.labels()
    by = collections.defaultdict(list)
    for occ, ref in pos:
        if E.subset(ref, 'main') and occ in G.words():
            by[ref].append(occ)
    brs = sorted(by)
    rng.shuffle(brs)
    for b in brs:
        by[b].sort()
        rng.shuffle(by[b])
    rows, i = [], 0
    while len(rows) < 60:
        progressed = False
        for b in brs:
            if len(rows) >= 60:
                break
            if i < len(by[b]):
                rows.append((by[b][i], b))
                progressed = True
        i += 1
        if not progressed:
            break
    return rows


def part_b(rng, kind, n):
    B = G.dictionary()['branches']
    D = G.dictionary()
    cands = sorted(r for r, b in B.items() if b['kind'] == kind and D['occ'].get(b['root_id']))
    pick = rng.sample(cands, n)
    dossier_at = collections.defaultdict(list)
    for r in G.dossier_rows():
        if r['role'] == 'dominant' and r['branch_ref'] in B:
            dossier_at[r['branch_ref']].append(r['qac_word_ref'])
    out = []
    for ref in pick:
        occs = [o for o in dossier_at.get(ref, []) if o in G.words()]
        out.append((ref, rng.choice(sorted(set(occs))) if occs else None, bool(occs)))
    return out


def part_c(rng, n_present=30, n_absent=10):
    """Seeded detector calls away from dossier placements: n_present 'present' calls (a third of them lexeme or
    formula calls when there are enough) and n_absent 'absent' calls, shuffled together."""
    placed = {(r['qac_word_ref'], r['branch_ref']) for r in G.dossier_rows() if r['role'] == 'dominant'}
    rows = list(csv.DictReader(open(os.path.join(HERE, 'guard_calls.tsv'), encoding='utf-8'), delimiter='\t'))
    off = [r for r in rows if (r['occurrence'], r['branch_ref']) not in placed]
    lex = sorted((r for r in off if r['call'] == 'present' and r['reason'].split(';')[0] in ('lexeme', 'formula')),
                 key=lambda r: (r['occurrence'], r['branch_ref']))
    oth = sorted((r for r in off if r['call'] == 'present' and r['reason'].split(';')[0] not in ('lexeme', 'formula')),
                 key=lambda r: (r['occurrence'], r['branch_ref']))
    ab = sorted((r for r in off if r['call'] == 'absent'), key=lambda r: (r['occurrence'], r['branch_ref']))
    k_lex = min(len(lex), n_present // 3)
    pick = rng.sample(lex, k_lex) + rng.sample(oth, n_present - k_lex) + rng.sample(ab, n_absent)
    rng.shuffle(pick)
    return pick


def main():
    rng = random.Random(SEED)
    B = G.dictionary()['branches']
    A = part_a(rng)
    Bc = part_b(rng, 'collocation', 30)
    Bb = part_b(rng, 'bare', 30)
    Cc = part_c(rng)
    key = []
    L = []
    L.append('# Yapı denetimi: kontrol sayfası (E0, sürüm 2)')
    L.append('')
    L.append('Bu sayfa yalnız sizin içindir; hiçbir satırı bir modelin okuduğu metne girmez. Betiğin kararları bu '
             'sayfada gösterilmez (cevabınızı yönlendirmesinler diye); `audit_key.tsv` dosyasındadır.')
    L.append('')
    L.append('**Neyi sormuyor.** Kelimenin düz (kanonik) okunuşu, bağlama dayansa bile yerinde kalır (kararınız: "yalnız '
             'bağlam sayılmaz" kuralı gizli okumalar içindir; düz anlam kanonik / root-dossier okumasını izler). '
             'Buradaki soru yalnız şudur: sözlüğün bu dal için verdiği kalıp bu ayetin metninde görünüyor mu? '
             'Görünmüyorsa bu dal, bu ayette gizli bir okuma olarak ancak "yankı" diye anılabilir.')
    L.append('')
    L.append('**Nasıl doldurulur.** Bütün sorular olumlu sorulur: ✓ = evet, ✗ = hayır. İsterseniz "Not" sütununa kısa bir '
             'not ekleyin. Kelime ayet parçasında **kalın** yazılmıştır. "Erken kaynak ifadesi", sözlüğün altı erken '
             'kaynağından bu dala ait ilk alıntıdır.')
    L.append('')
    L.append('## A. Root-dossier yerleştirmeleri (60)')
    L.append('')
    L.append('Root-dossier bu kelimenin düz okunuşunu buradaki dala bağlamış. Bu dal sözlükte "kalıba bağlı" '
             '(collocation) işaretli: anlam yalnız belirli bir söz kalıbı içinde geçerli. **Soru:** bu ayette o kalıp '
             'gerçekten var mı? ✓ = kalıp burada var, ✗ = kalıp yok (anlam burada olsa olsa bir yankı).')
    L.append('')
    L.append('| # | Ayet | Kelime | Kök · dal | Dalın imgesi | Sözlüğün kapsam notu | Sözlüğün kalıbı · erken kaynak ifadesi '
             '| Ayet (parça) | Ne soruluyor | Kalıp burada var mı? (✓/✗) | Not |')
    L.append('|---|---|---|---|---|---|---|---|---|---|---|')
    for n, (occ, ref) in enumerate(A, 1):
        b = B[ref]
        d = G.words()[occ]
        call = Dt.decide(occ, b['root_id']).get(ref)
        stmt = main_statement(ref)
        q = (f'Sözlük bu anlamı «{stmt}» kalıbına bağlıyor. Bu ayette «{d["surface"]}» bu kalıpla mı '
             f'kullanılmış?')
        L.append(f'| A{n} | {d["s"]}:{d["a"]} | {d["surface"]} | {b["root"]} · {ref.split("/")[1]} | {cell(b["image"])} '
                 f'| {cell(b["note"])} | «{cell(stmt)}» · {cell(first_phrase(b))} | {cell(ayah_snippet(occ))} | {cell(q)} '
                 f'|  |  |')
        key.append(dict(row=f'A{n}', part='A', occ=occ, branch=ref, kind=b['kind'], call=call[0], reason=call[2],
                        construction=call[3]))
    L.append('')
    L.append('## B. `branch_kind` etiketleri (30 kalıba bağlı + 30 yalın)')
    L.append('')
    L.append('Sözlük her dala bir etiket vermiş: **kalıba bağlı** (collocation: anlam yalnız belirli bir kalıpta '
             'geçer) ya da **yalın** (bare: kelime tek başına bu anlamı taşıyabilir). **Soru:** etiket doğru mu? '
             'Karar sözlüğün kendi metninden (imge, kapsam notu, erken kaynak ifadesi) verilir. Örnek ayet yalnız '
             'root-dossier bu dalı bir ayette okuyorsa gösterilir; yoksa "—".')
    L.append('')
    L.append('| # | Kök · dal | Etiket | Dalın imgesi | Sözlüğün kapsam notu | Sözlüğün kalıbı · erken kaynak ifadesi '
             '| Örnek ayet (dossier) | Ne soruluyor | Etiket doğru mu? (✓/✗) | Not |')
    L.append('|---|---|---|---|---|---|---|---|---|---|')
    for n, (ref, occ, from_dossier) in enumerate(Bc + Bb, 1):
        b = B[ref]
        stmt = main_statement(ref) if b['kind'] == 'collocation' else ''
        if b['kind'] == 'collocation':
            lab = 'kalıba bağlı'
            q = f'Bu anlam yalnız «{stmt}» gibi bir kalıbın içinde mi geçer? Evetse ✓.'
            call = Dt.decide(occ, b['root_id']).get(ref) if occ else None
        else:
            lab = 'yalın'
            q = (f'Kelime bu anlamı («{cell(b["image"])}») tek başına, bir kalıba ihtiyaç duymadan taşıyabilir mi? '
                 f'Evetse ✓.')
            call = None
        ex = f'{G.words()[occ]["s"]}:{G.words()[occ]["a"]}: {cell(ayah_snippet(occ))}' if occ else '—'
        L.append(f'| B{n} | {b["root"]} · {ref.split("/")[1]} | {lab} | {cell(b["image"])} | {cell(b["note"])} '
                 f'| {("«" + cell(stmt) + "» · ") if stmt else ""}{cell(first_phrase(b))} | {ex} | {cell(q)} |  |  |')
        key.append(dict(row=f'B{n}', part='B', occ=occ or '', branch=ref, kind=b['kind'], call=call[0] if call else '',
                        reason=call[2] if call else '', construction=call[3] if call else '',
                        example_from_dossier=from_dossier))
    L.append('')
    L.append('## C. Betiğin kararlarından bir örneklem (40)')
    L.append('')
    L.append('Bu satırlar root-dossier yerleştirmelerinin dışından, betiğin karar verdiği yerlerden seçildi (bir kısmında '
             'betik kalıbı buldu, bir kısmında bulamadı; hangisinin hangisi olduğu gösterilmez). **Soru:** sözlüğün bu '
             'dal için verdiği kalıp bu ayette, bu kelimeyle gerçekten var mı? ✓ = var, ✗ = yok.')
    L.append('')
    L.append('| # | Ayet | Kelime | Kök · dal | Dalın imgesi | Sözlüğün kapsam notu | Sözlüğün kalıbı · erken kaynak ifadesi '
             '| Ayet (parça) | Kalıp burada var mı? (✓/✗) | Not |')
    L.append('|---|---|---|---|---|---|---|---|---|---|')
    for n, r in enumerate(Cc, 1):
        ref, occ = r['branch_ref'], r['occurrence']
        b = B[ref]
        d = G.words()[occ]
        stmts = ' / '.join(f'«{cell(x)}»' for x in statements_shown(ref))
        L.append(f'| C{n} | {d["s"]}:{d["a"]} | {d["surface"]} | {b["root"]} · {ref.split("/")[1]} | {cell(b["image"])} '
                 f'| {cell(b["note"])} | {stmts} · {cell(first_phrase(b))} | {cell(ayah_snippet(occ))} |  |  |')
        key.append(dict(row=f'C{n}', part='C', occ=occ, branch=ref, kind=b['kind'], call=r['call'], reason=r['reason'],
                        construction=r['matched_statement'], example_from_dossier=''))
    L.append('')
    L.append('Seçim: tohum 20260928 (`build_audit.py`). A bölümü, değerlendirme kümesinden (iki dilbilgisel kalıp ve '
             'ء ت ي B011 hariç) dallar arasında sırayla seçildi; bir dal en fazla birkaç satır alır. B bölümü, '
             'sözlükteki bütün kalıba bağlı ve yalın dallardan rastgele seçildi. C bölümü, betiğin `guard_calls.tsv` '
             'kaydından (dossier yerleştirmeleri dışında) 30 "var" ve 10 "yok" kararı karıştırılarak seçildi; "var" '
             'kararlarının yaklaşık üçte biri tek kelime ya da kalıp eşleşmesidir.')
    open(os.path.join(HERE, 'audit_sheet.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    with open(os.path.join(HERE, 'audit_key.tsv'), 'w', encoding='utf-8') as f:
        w = csv.DictWriter(f, delimiter='\t', fieldnames=['row', 'part', 'occ', 'branch', 'kind', 'call', 'reason',
                                                         'construction', 'example_from_dossier'])
        w.writeheader()
        for k in key:
            w.writerow(k)
    ca = collections.Counter(k['call'] for k in key if k['part'] == 'A')
    cc = collections.Counter(k['call'] for k in key if k['part'] == 'C')
    print('A calls', dict(ca), 'branches', len({k['branch'] for k in key if k['part'] == 'A'}))
    print('B examples from dossier', sum(1 for k in key if k['part'] == 'B' and k['example_from_dossier']))
    print('C calls', dict(cc), 'lexeme/formula', sum(1 for k in key if k['part'] == 'C' and
                                                      k['reason'].split(';')[0] in ('lexeme', 'formula')))


if __name__ == '__main__':
    main()
