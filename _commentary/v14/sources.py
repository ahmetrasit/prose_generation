"""Exact Quran text for new writer packets, using the verifier's own text and normalizer."""
from __future__ import annotations

import importlib.util
import re
import unicodedata
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location('v14_verify_ar', Path(__file__).resolve().parent.parent / 'v9' / 'verify_ar.py')
_AR = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_AR)
QURAN_TEXT = _AR.QURAN_TEXT


def corpus(path: Path | None = None) -> dict[str, str]:
    result = {}
    for line in (path or QURAN_TEXT).read_text(encoding='utf-8-sig').splitlines():
        ref, sep, text = line.partition('|')
        if sep and text:
            result[ref.strip()] = unicodedata.normalize('NFC', text.lstrip('\ufeff'))
    return result


def exact_excerpt(text: str, ref: str, quran: dict[str, str]) -> str:
    """Map a supplied clause to its declared source; fail on wrong or ambiguous text."""
    source = quran[ref]
    query = unicodedata.normalize('NFC', text.replace('⟦', '').replace('⟧', ''))
    folded = _AR.loose(query)[0].strip()
    folded_source, indices = _AR.loose(source)
    start = folded_source.find(folded) if folded else -1
    if start < 0 or folded_source.find(folded, start + 1) >= 0:
        raise ValueError(f'Cannot uniquely resolve Quran clause at {ref}')
    return _AR.exact_span(source, indices, start, start + len(folded))


def concordance(text: str, quran: dict[str, str]) -> str:
    """Keep counts/word IDs and clause scope; quote canonical text without embedded highlights."""
    lines = []
    for line in text.splitlines():
        match = re.match(r'(- (\d+:\d+):\d+ \[[^\]]+\] )(.+)', line)
        if match:
            clause = match[3]
            before = '… ' if clause.startswith('…') else ''
            after = ' …' if clause.endswith('…') else ''
            line = match[1] + before + exact_excerpt(clause.strip('… '), match[2], quran) + after
        lines.append(line)
    return '\n'.join(lines).replace('with the word marked ⟦ ⟧', 'in the exact verifier spelling; the word ID identifies the focus') + '\n'


def window(text: str, quran: dict[str, str]) -> str:
    lines = []
    for line in text.splitlines():
        ref, sep, original = line.partition('|')
        if sep and re.fullmatch(r'\d+:\d+', ref):
            # Check identity before replacement; an upstream reference error must not disappear.
            if _AR.loose(original)[0] != _AR.loose(quran[ref])[0]:
                raise ValueError(f'Window text disagrees with source at {ref}')
            line = ref + '|' + quran[ref]
        lines.append(line)
    return '\n'.join(lines) + '\n'


def render(quran: dict[str, str], refs: set[str]) -> str:
    """Supply exact complete ayat once per reference, independently of QeQ's interpretation."""
    missing = refs - quran.keys()
    if missing:
        raise ValueError('Unknown Quran references: ' + ', '.join(sorted(missing)))
    lines = ['# passages.md — exact Quran text', '',
             'Copy Quran quotations from here. Other records explain or index these passages; '
             'their remembered Arabic is not the quotation authority. These are complete ayat, '
             'not a claim that every surrounding passage has been retrieved.', '']
    for ref in sorted(refs, key=lambda r: tuple(map(int, r.split(':')))):
        lines += [f'## {ref}', quran[ref], '']
    return '\n'.join(lines)


def select(quran: dict[str, str], requested: set[str], context: int = 1) -> set[str]:
    if not 0 <= context <= 3 or not 1 <= len(requested) <= 16:
        raise ValueError('Request 1–16 ayat and 0–3 neighbours per side')
    if requested - quran.keys() or any(not re.fullmatch(r'[1-9]\d*:[1-9]\d*', r) for r in requested):
        raise ValueError('Unknown or invalid Quran reference')
    selected = set(requested)
    for ref in requested:
        s, a = map(int, ref.split(':'))
        selected.update(f'{s}:{n}' for n in range(max(1, a - context), a + context + 1) if f'{s}:{n}' in quran)
    return selected


def main() -> None:
    import argparse
    import hashlib
    import json
    import sys
    import experiment as EX
    import synthesis as S
    ap = argparse.ArgumentParser(description='Read exact passages from a claimed writer arm; no model call.')
    ap.add_argument('--tag', required=True)
    ap.add_argument('--ref', required=True)
    ap.add_argument('--refs', required=True)
    ap.add_argument('--context', type=int, default=1)
    args = ap.parse_args()
    if not re.fullmatch(r'[a-zA-Z0-9_-]+', args.tag):
        ap.error('Invalid arm tag')
    arm = EX.ROOT / f'out-{args.tag}'
    manifest = EX.verify(arm)
    if manifest.get('source_mode') != 'lookup' or args.ref not in manifest['refs']:
        ap.error('This ayah was not prepared for source lookup')
    out = EX.ayah_dir(arm, args.ref)
    status = json.loads((out / 'write.status.json').read_text())
    if status.get('state') != 'started':
        ap.error('Source lookup is available during the claimed writer generation')
    snapshot = arm / 'inputs' / 'quran.tsv'
    quran = corpus(snapshot)
    requested = set(args.refs.split(','))
    selected = select(quran, requested, args.context)
    result = render(quran, selected)
    record = {'requested': sorted(requested), 'returned': sorted(selected), 'context': args.context,
              'bytes': len(result.encode()), 'text_sha256': hashlib.sha256(result.encode()).hexdigest(),
              'corpus_sha256': S.sha(snapshot)}
    with (out / 'source.lookups.jsonl').open('a', encoding='utf-8') as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + '\n')
    sys.stdout.write(result)


if __name__ == '__main__':
    main()
