"""Serialize the parent's completed prose review and checked quotation findings."""
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import sys
import unicodedata

sys.path.insert(0, str(Path(__file__).resolve().parents[5]))
from enrichment.bible import image_enrich as I

root=Path(__file__).resolve().parent
reviewed={(r['section'],r['id']):r['sha256'] for r in I.read_json(root/'editorial-progress.json')['reviewed']}
records={}
hashes={}
for j in I.read_json(root/'started.json')['jobs']:
    d=root/j['target']
    assert I.read_json(d/'run.log.json')['status']=='ok', j['target']
    hashes[j['target']]=I.D.digest(d/'annotations.jsonl')
    for r in I.R.load(d/'annotations.jsonl'):
        assert reviewed[(j['target'],r['id'])]==hashlib.sha256(json.dumps(r,ensure_ascii=False,sort_keys=True).encode()).hexdigest(), (j['target'],r['id'])
        records[(j['target'],r['id'])]=r
quotes=I.read_json(root/'quote_audit.json')
hebrew={'WLC:Deut.32.3','WLC:Ps.7.18','WLC:Exod.20.24','WLC:1Sam.1.13',
        'WLC:Dan.6.11','WLC:Mal.1.11','WLC:Isa.29.13','WLC:Neh.9.3'}
greek={'SBLGNT:Acts.22.16','SBLGNT:Col.3.16'}
strip_he=lambda s:re.sub('[\u0591-\u05af\u05bd]','',unicodedata.normalize('NFC',s))
strip_el=lambda s:re.sub('[⸀⸁⸂⸃]','',unicodedata.normalize('NFC',s))
with sqlite3.connect(f'file:{I.C.INDEX_INTERTEXT}?mode=ro',uri=True) as con:
    for r in quotes['findings']:
        assert r['section']=='sec11', r
        source=con.execute('SELECT text FROM seg WHERE seg=?',(r['ref'],)).fetchone()[0]
        if r['language']=='he' and r['ref'] in hebrew:
            assert strip_he(r['quote']) in strip_he(source), r
            r['review']='Cantillation/meteg marks are omitted; the quoted words and vowel points agree with the frozen WLC witness.'
        elif r['language']=='el' and r['ref'] in greek:
            assert strip_el(r['quote']) in strip_el(source), r
            r['review']='SBLGNT apparatus delimiters are omitted; the quoted Greek words agree with the witness.'
        else:
            raise ValueError(f'Unreviewed quotation difference: {r}')
quotes.pop('rows')
quotes['author_corrections']=[dict(section='sec11',annotation='S087-TEV-MTF-002',source='WLC:Neh.8.6',
    change='Author reopened the original verse and replaced the extra-waw spelling with the exact frozen ketiv before completing the same native turn.',
    evidence='images/sec11/native-tool-calls.json')]
I.D.save(root/'quotation-review.json',quotes)
feedback=[
    ('sec11','S087-TEV-MTF-002','Exact WLC ketiv spelling in Nehemiah 8:6.'),
    ('sec7','S087-INC-MTF-004','2 Corinthians 1:22 seals the believers and gives the Spirit as a pledge in their hearts.'),
    ('sec13','S087-TEV-MTF-004','Proverbs 27:25 distinguishes the old grass going from the fresh greenery appearing.'),
    ('sec16','S087-TEV-MTF-007','God, rather than the threatening king, is the deliverer in Daniel 3:17–18.'),
    ('sec12','S087-TEV-MTF-002','Malachi 3:16 names the beneficiaries of the remembrance book; it is not written to induce them to think of the name.')
]
I.D.save(root/'editorial-review.json',dict(
    annotations_read=len(records),accepted_annotation_sha256=hashes,
    review='Parent read all final annotation explanations and quoted wording, including revisions checked by per-record hashes. All five requested changes were made by their original authors during their active native turns; the parent did not rewrite author deliverables.',
    feedback=[dict(section=s,annotation=a,issue=issue,final_record=records[(s,a)]) for s,a,issue in feedback],
    verdict_review='Sampled concise accepted, rejected, unavailable and unresolved reasons across the image ledgers. Full candidate coverage, cited-reference coverage and actual opened-source evidence were checked mechanically for every image.',
    limits='This does not claim an independent second semantic verification of every rejected candidate or exhaustive comparative-linguistic research. Original authors retain their separate judgments and recorded uncertainty.',
    operational_review='One exact status acknowledgment to the parent is preserved in sec11/operator-messages.json and the native audit, excluded from source evidence. Narrow print-only preview ranges, fixed-option text searches and trailing-line reads of each author’s own files are recognized by the Bible-only audit; the complete native commands are preserved.',
    source_mode='Frozen available-local-witnesses snapshot; absent secondary works were not fetched or searched.'))
print(json.dumps(dict(annotations=len(records),quotes=quotes['quotes'],reviewed_quote_differences=len(quotes['findings']),author_feedback=len(feedback))))
