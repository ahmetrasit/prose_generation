#!/usr/bin/env python3
"""Turn memory leads into corpus candidates: a script search, no model.

Reads FAMILY_DIR/leads/leads.jsonl (written by the leads agent), searches the family roster
for each term, and writes candidates.jsonl plus candidates.txt (what the search writer reads
with `read.py DIR candidates`). A candidate is only a place to read; the writer still opens
the passage before attributing anything. Leads without hits stay listed, never dropped.

  python3 -B enrichment/v5/leads.py DIR
"""
import argparse
import json
from pathlib import Path

from common import ROOT, connect, normalized, rows, usable, write_rows

PER_TERM = 6
SNIPPET = 260


def search(con, ids, term):
    words = normalized(term).split()
    if not words:
        return []
    expr = ' '.join('"' + w.replace('"', '""') + '"*' for w in words)
    sql = (f'SELECT seg.seg,seg.src,seg.head,seg.text FROM f JOIN seg ON seg.id=f.rowid '
           f'WHERE f MATCH ? AND seg.src IN ({",".join("?" * len(ids))}) ORDER BY seg.src,seg.id LIMIT 200')
    return con.execute(sql, [expr, *ids]).fetchall()


def snippet(text, term):
    plain, key = normalized(text), normalized(term).split()[0]
    i = plain.find(key)
    if i < 0:
        return plain[:SNIPPET]
    return '…' + plain[max(0, i - SNIPPET // 2):i + SNIPPET // 2] + '…'


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('dir')
    d = Path(parser.parse_args().dir)
    d = d if d.is_absolute() else ROOT / d
    leads = rows(d / 'leads/leads.jsonl')
    ids = usable(json.loads((d / 'sources.json').read_text()))
    out, text = [], []
    with connect() as con:
        for n, lead in enumerate(leads, 1):
            hits, seen = [], set()
            for term in lead.get('terms', []):
                found = search(con, ids, term)
                for loc, src, head, body in found[:PER_TERM]:
                    if loc not in seen:
                        seen.add(loc)
                        hits.append({'loc': loc, 'source': src, 'head': head or '', 'term': term,
                                     'term_total_hits': len(found), 'snippet': snippet(body, term)})
            out.append({**lead, 'lead': n, 'hits': hits})
            text.append(f"### Lead {n} — paragraphs {lead.get('p')} — {lead.get('author', '')}, {lead.get('work', '')} "
                        f"({lead.get('confidence', '?')})\nRemembered (unverified): {lead.get('claim', '')}\n"
                        f"Terms: {', '.join(lead.get('terms', []))}\n"
                        + ('\n'.join(f"- {h['loc']} [{h['source']}] {h['head'][:80]} | term «{h['term']}» "
                                     f"({h['term_total_hits']} hits) {h['snippet']}" for h in hits)
                           if hits else '- no corpus hit for these terms in the roster'))
    write_rows(d / 'leads/candidates.jsonl', out)
    (d / 'leads/candidates.txt').write_text('\n\n'.join(text) + '\n')
    with_hits = sum(bool(x['hits']) for x in out)
    print(f'{len(out)} leads; {with_hits} with corpus candidates; {len(out) - with_hits} without -> {d / "leads"}')


if __name__ == '__main__':
    main()
