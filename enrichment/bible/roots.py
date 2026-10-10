#!/usr/bin/env python3
"""Arabic roots of a focus ayah against their Hebrew/Aramaic correspondents (user design, 2026-10-09).

Every root of the ayah comes from the Quranic Arabic Corpus morphology (quran-data), not from the commentary. The
cognate candidates come from hebrew.py (regular sound correspondences found in the lexicon). One model call per
ayah names the true cognate, how the meanings relate (same, narrowed, broadened, shifted, false_friend, none) and
the Hebrew Bible verses where the cognate carries the ayah's sense or forms the same phrase. Each verse is then
checked against the WLC words: does a word of that Hebrew root occur in it (at the given reference, or a nearby one
when Hebrew and English numbering differ)? Unconfirmed verses are kept and flagged, never dropped.

  roots.py run    --surah S --tag T --ayat S:A,S:A [--model sol|luna|terra] [--effort high] [--parallel 3]
  roots.py verify --surah S --tag T
  roots.py show   --surah S --tag T
Work: enrichment/bible/work/sSSS/roots/T/<S_A>/<model>/.
"""
from __future__ import annotations

import argparse
import atexit
import concurrent.futures as cf
import gzip
import json
import re
import shutil
import sqlite3
import sys
import tempfile
import threading
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))
from enrichment.bible import codexrun as CR, hebrew as H, recall as RC  # noqa: E402

QAC = ROOT.parent / 'quran-data' / 'data' / 'morphology' / 'qac.sqlite.gz'
RELATIONS = ('same', 'narrowed', 'broadened', 'shifted', 'false_friend', 'none')
OSIS = RC.OSIS
_QAC_FILE, _QAC_LOCK, _QAC_LOCAL = None, threading.Lock(), threading.local()


def qac() -> sqlite3.Connection:
    """The QAC morphology database: unpacked once per process, one connection per thread (sqlite3 connections
    cannot cross threads)."""
    global _QAC_FILE
    with _QAC_LOCK:
        if _QAC_FILE is None:
            tmp = Path(tempfile.mkdtemp()) / 'qac.sqlite'
            atexit.register(shutil.rmtree, tmp.parent, ignore_errors=True)
            with gzip.open(QAC) as src, tmp.open('wb') as dst:
                shutil.copyfileobj(src, dst)
            _QAC_FILE = tmp
    if getattr(_QAC_LOCAL, 'con', None) is None:
        _QAC_LOCAL.con = sqlite3.connect(_QAC_FILE)
    return _QAC_LOCAL.con


def ayah_roots(ayah: str) -> list[tuple[str, list[str]]]:
    """[(root as spaced letters, [the ayah's words with it])] in order of first use."""
    s, a = map(int, ayah.split(':'))
    out = {}
    for surface, roots in qac().execute('select surface_ar, root_join_keys from qac_words where surah=? and ayah=? '
                                        'order by word_index', (s, a)):
        for r in filter(None, roots.split(';')):
            out.setdefault(' '.join(r), []).append(surface)
    return list(out.items())


def run_dir(s, tag):
    return HERE / 'work' / f's{s:03d}' / 'roots' / tag


def table_text(roots) -> str:
    out = []
    for r, words in roots:
        out.append(f"## {r} (in the ayah: {', '.join(words)})")
        out += H.cmd_cognates(r, full=False)[1:]   # returns lines, prints nothing
        out.append('')
    return '\n'.join(out)


def parse(text: str, roots: list[str]):
    rows, bad = [], []
    for line in text.splitlines():
        if not line.strip():
            continue
        f = [x.strip() for x in line.split('\t')]
        if len(f) != 4 or f[0] not in ('root', 'verse'):
            bad.append(f'not a four-field root/verse row: {line[:140]}')
            continue
        kind, ar, x, rest = f
        if ar not in roots:
            bad.append(f'unknown Arabic root {ar!r}: {line[:140]}')
            continue
        if kind == 'root':
            rel, _, why = rest.partition(':')
            if rel.strip() not in RELATIONS:
                bad.append(f'bad relation: {line[:140]}')
                continue
            rows.append(dict(kind='root', ar=ar, he=None if x == 'none' else H.cons(x), relation=rel.strip(),
                             note=why.strip()))
        else:
            if not OSIS.match(x):
                bad.append(f'bad ref: {line[:140]}')
                continue
            rows.append(dict(kind='verse', ar=ar, ref=x, explanation=rest))
    missing = sorted(set(roots) - {r['ar'] for r in rows if r['kind'] == 'root'})
    if missing:
        bad.append(f'no root row for {missing}')
    return rows, bad


def one(s, tag, ayah, model, effort, q) -> str:
    d = run_dir(s, tag) / RC.key(ayah) / model
    if (d / 'rows.json').exists():
        return f'{ayah} {model}: done already'
    roots = ayah_roots(ayah)
    if not roots:
        return f'{ayah}: no roots in the morphology; nothing to ask'
    d.mkdir(parents=True, exist_ok=True)
    prompt = ((HERE / 'prompts' / 'roots.md').read_text().replace('{{REF}}', ayah).replace('{{ARABIC}}', q[ayah])
              .replace('{{TABLE}}', table_text(roots)))
    (d / 'prompt.md').write_text(prompt)
    t = CR.turn(d, 1, prompt, RC.MODELS[model], effort)
    if not t['completed']:
        return f'ERROR {ayah} {model}: turn did not complete (rc {t["returncode"]}); see {d}'
    rows, bad = parse((d / 'turn1.last.txt').read_text(), [r for r, _ in roots])
    tools = sum(1 for line in (d / 'turn1.stream.jsonl').read_text().splitlines()
                if '"command_execution"' in line and '"item.started"' in line)
    cost = CR.cost(CR.rollout(t['thread_id']))
    (d / 'rows.json').write_text(json.dumps(dict(ayah=ayah, model=RC.MODELS[model], effort=effort,
                                                 roots=[r for r, _ in roots], rows=rows, malformed=bad,
                                                 tool_calls=tools, cost=cost), ensure_ascii=False, indent=1) + '\n')
    nv = sum(r['kind'] == 'verse' for r in rows)
    return (f"{ayah} {model}: {len(roots)} roots, {nv} verses, {len(bad)} malformed, {tools} tool calls, "
            f"${cost['usd_equivalent']:.3f}")


def occ_refs(he_key: str) -> set[str]:
    d = H.data()
    return {ref for e in H.family(he_key) for ref, _ in d['occ'].get(e, [])}


def nearby(ref: str):
    """The reference itself, then neighbours where Hebrew and English numbering often differ."""
    b, c, v = OSIS.match(ref).groups()
    c, v = int(c), int(v)
    yield ref
    for dv in (1, -1, 2, -2):
        if v + dv > 0:
            yield f'{b}.{c}.{v + dv}'
    for dc in (1, -1):       # chapter boundaries move (Joel 2:28-32 = WLC 3:1-5, Mal 4 = WLC 3:19-24)
        for vv in sorted(set(range(max(1, v - 6), v + 7)) | set(range(1, 11)) | set(range(max(1, v - 30), v - 20))
                         | set(range(v + 10, v + 25))):
            if c + dc > 0:
                yield f'{b}.{c + dc}.{vv}'


def cmd_verify(a):
    for f in sorted(run_dir(a.surah, a.tag).glob('*/*/rows.json')):
        r = json.loads(f.read_text())
        cog = {x['ar']: x['he'] for x in r['rows'] if x['kind'] == 'root'}
        n = {'verified': 0, 'nearby': 0, 'unconfirmed': 0, 'no cognate named': 0, 'not Hebrew Bible': 0}
        for x in r['rows']:
            if x['kind'] != 'verse':
                continue
            he = cog.get(x['ar'])
            book = OSIS.match(x['ref'])[1]
            if book not in RC.OT:
                x['check'] = 'not Hebrew Bible'
            elif not he:
                x['check'] = 'no cognate named'
            else:
                refs = occ_refs(he)
                hit = next((c for c in nearby(x['ref']) if c in refs), None)
                x['check'] = 'verified' if hit == x['ref'] else (f'nearby' if hit else 'unconfirmed')
                if hit and hit != x['ref']:
                    x['wlc_ref'] = hit
            n[x['check']] += 1
        f.write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n')
        print(f"{f.parents[1].name} {f.parent.name}: " + ', '.join(f'{k} {v}' for k, v in n.items() if v))


def cmd_show(a):
    for f in sorted(run_dir(a.surah, a.tag).glob('*/*/rows.json')):
        r = json.loads(f.read_text())
        print(f"=== {r['ayah']} ({f.parent.name}, ${r['cost']['usd_equivalent']:.3f})")
        for x in r['rows']:
            if x['kind'] == 'root':
                print(f"  {x['ar']} -> {x['he'] or 'none'} [{x['relation']}] {x['note']}")
                vs = [y for y in r['rows'] if y['kind'] == 'verse' and y['ar'] == x['ar']]
                for y in vs:
                    print(f"      {y['ref']:<14} {y.get('check', '?'):<12}{(' WLC ' + y['wlc_ref']) if y.get('wlc_ref') else ''}"
                          f"  {y['explanation'][:110]}")
        for b in r['malformed']:
            print(f'  MALFORMED {b}')


def cmd_run(a):
    q = RC.quran()
    ayat = a.ayat.split(',')
    for x in ayat:
        if x not in q or int(x.split(':')[0]) != a.surah:
            raise SystemExit(f'{x}: not an ayah of surah {a.surah}')
    with cf.ThreadPoolExecutor(a.parallel) as ex:
        for msg in ex.map(lambda x: one(a.surah, a.tag, x, a.model, a.effort, q), ayat):
            print(msg, flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cmd', choices=('run', 'verify', 'show'))
    ap.add_argument('--surah', type=int, required=True)
    ap.add_argument('--tag', required=True)
    ap.add_argument('--ayat')
    ap.add_argument('--model', default='sol', choices=('sol', 'luna', 'terra'))
    ap.add_argument('--effort', default='high')
    ap.add_argument('--parallel', type=int, default=3)
    a = ap.parse_args()
    if a.cmd == 'run' and not a.ayat:
        raise SystemExit('run needs --ayat')
    globals()[f'cmd_{a.cmd}'](a)


if __name__ == '__main__':
    main()
