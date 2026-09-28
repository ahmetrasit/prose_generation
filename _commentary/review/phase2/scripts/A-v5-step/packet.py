"""Assemble the prototype Opus packet for one ayah and measure it: core text + v5 digest + script supplements.
The brief itself is a placeholder of measured length (brief_draft.md); no model is called."""
import sys, os, re
import lib, digest, supplement as S


def core(ref, k=3):
    s, a = map(int, ref.split(':'))
    t = lib.quran_text()
    L = [f"# {ref} and its window (±{k})"]
    for x in range(a - k, a + k + 1):
        r = f'{s}:{x}'
        if r in t:
            L.append(f"{'>> ' if x == a else ''}{r} {t[r]}")
    return '\n'.join(L)


def build(ref, f_top=40):
    D = digest.build(ref)
    parts = {}
    parts['core'] = core(ref)
    parts['digest_branches'] = digest.render(D, 'branches_only')
    full = digest.render(D, 'packet')
    parts['digest_findings_setasides'] = full[len(parts['digest_branches']):]
    sup = S.render_supp(ref, D)
    # cap F at f_top lines in the packet (full list one read away / in the audit index)
    lines = sup.split('\n'); out = []; inF = False; n = 0
    for ln in lines:
        if ln.startswith('## F.'): inF = True; out.append(ln); continue
        if ln.startswith('## ') and inF: inF = False
        if inF:
            n += 1
            if n > f_top: continue
        out.append(ln)
    parts['supplements'] = '\n'.join(out)
    brief = open(lib.W + '/brief_draft.md').read() if os.path.exists(lib.W + '/brief_draft.md') else ''
    parts['brief'] = brief
    return parts


if __name__ == '__main__':
    refs = sys.argv[1:] or ['1:6', '1:2', '5:6', '18:86', '18:96', '100:1', '103:1']
    print('ref\t' + '\t'.join(['brief', 'core', 'digest_branches', 'digest_findings_setasides', 'supplements', 'TOTAL_tok', 'TOTAL_bytes']))
    for r in refs:
        P = build(r)
        txt = '\n\n'.join(P[k] for k in ['brief', 'core', 'digest_branches', 'digest_findings_setasides', 'supplements'])
        open(f"{lib.W}/out/packet_{r.replace(':','_')}.txt", 'w').write(txt)
        toks = [lib.cal_tokens(P[k]) for k in ['brief', 'core', 'digest_branches', 'digest_findings_setasides', 'supplements']]
        print(r, *toks, sum(toks), len(txt.encode()), sep='\t')
