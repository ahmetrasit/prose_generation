#!/usr/bin/env python3
"""Bible-owned structural and wording review. A matching phrase is not a verdict."""
import argparse
from collections import Counter
from contextlib import closing
import json
from pathlib import Path
import re
import sqlite3
import sys
import unicodedata

sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from enrichment.bible import discovery as D

SCRIPTS = {'Hebrew':r'\u0590-\u05ff', 'Greek':r'\u0370-\u03ff\u1f00-\u1fff'}
LIMITS = ('Wording and reference checks only; no semantic, relevance, historical or cognacy validation. '
          'Pointing/accents are normalized; roots, inflections, orthography, segmentation and named '
          'witnesses require review. Qere is separate from the WLC ketiv text. Unmatched spans are findings, '
          'not automatic rejection; a match does not verify a connection.')


def normalize(text):
    text = unicodedata.normalize('NFKD',text).casefold().replace('ς','σ')
    return ' '.join(''.join(c if unicodedata.category(c).startswith('L') else
                           '' if unicodedata.combining(c) else ' ' for c in text).split())


def contains(text, phrase):
    return bool(phrase) and f' {phrase} ' in f' {normalize(text)} '


def spans(text):
    for language, chars in SCRIPTS.items():
        for m in re.finditer(f'[{chars}]+(?:[ \t\u05be]+[{chars}]+)*',text):
            if normalize(m.group()): yield language,m.group()


def check(path):
    rows, bad = D.parse_rows(path)
    keys = Counter(D.row_key(r) for r in rows)
    duplicates = [dict(key=list(k),count=n) for k,n in keys.items() if n>1]
    findings = []
    with closing(sqlite3.connect(f'file:{D.INDEX}?mode=ro',uri=True)) as con:
        for row in rows:
            ref = row['ref']
            canonical = con.execute('SELECT text,extra FROM seg WHERE seg=?',(ref,)).fetchone()
            if not canonical:
                findings.append(dict(line=row['line'],ref=ref,kind='unresolved_text',
                                     message='Named work requires prefetch or an explicit unavailable verdict.'))
            for field in ('basis','note'):
                for language, wording in spans(row[field]):
                    phrase = normalize(wording)
                    if canonical and contains(canonical[0],phrase): continue
                    variant_matches, neighbours = [], []
                    if canonical:
                        extra = json.loads(canonical[1] or '{}')
                        for note in extra.get('variant_notes',[]):
                            for reading in note.get('readings',[]):
                                if contains(reading.get('text',''),phrase):
                                    variant_matches.append(dict(after_word=note.get('after_word'),reading=reading))
                        if ref.startswith(('WLC:','SBLGNT:')) and len(phrase.split())>=2:
                            prefix, verse = ref.rsplit('.',1)
                            for v in (int(verse)-1,int(verse)+1):
                                adjacent = con.execute('SELECT text FROM seg WHERE seg=?',(f'{prefix}.{v}',)).fetchone()
                                if adjacent and contains(adjacent[0],phrase): neighbours.append(f'{prefix}.{v}')
                    findings.append(dict(line=row['line'],ref=ref,field=field,language=language,wording=wording,
                        kind='wording_review', variant_matches=variant_matches,matching_neighbours=neighbours,
                        message='Wording absent from cited main text; review quotation, root/form, witness and verse boundary.'))
    return dict(file=str(path),rows=len(rows),unique_references=len({(r['tradition'],r['ref']) for r in rows}),
                schema_errors=bad,duplicates=duplicates,strengths=dict(Counter(r['strength'] for r in rows)),
                findings=findings,limits=LIMITS)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('path',type=Path)
    ap.add_argument('--output',type=Path,help='optional report inside the Bible work directory')
    a=ap.parse_args()
    report=check(a.path)
    if a.output:
        if not a.output.resolve().is_relative_to((D.HERE/'work').resolve()):
            ap.error('output must be inside Bible work/')
        D.save(a.output,report)
    print(json.dumps(report,ensure_ascii=False,indent=2))
    if report['schema_errors'] or report['duplicates']: raise SystemExit(1)


if __name__=='__main__': main()
