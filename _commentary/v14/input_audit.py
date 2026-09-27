"""Offline input accounting, with explicit roles. Bytes are measured, token estimates are historical heuristics."""
import argparse
import json
import re
from pathlib import Path

import experiment as EX
import synthesis as S

ROOT = Path(__file__).resolve().parent


def audit(arm: Path, ref: str) -> dict:
    manifest = EX.verify(arm)
    out = EX.ayah_dir(arm, ref)
    packet, receipt = EX.packet(arm, ref)
    old = EX.ayah_dir(ROOT / manifest['source_arm'], ref)
    baseline = json.loads((old / 'write.status.json').read_text())
    roles = {
        'write.md': 'composition and accounting instructions',
        'ayah.md': 'focus text, translation and word-level morphology/notes',
        'window_text.md': 'exact local scene and neighbours',
        'synthesis.md': 'findings, QeQ jobs, image members and meetings; one source record per entry',
        'dictionary.md': 'complete focus concepts and Turkish losses; exact branch quotations',
        'branches.md': 'cross-root evidence beyond the focus dictionary',
        'concordance.md': 'verified count scope and recurring-use patterns',
        'variants.md': 'only meaningful alternative readings, no conflicting legacy usage table',
    }
    inputs = [{'file': name, 'bytes': (arm / name).stat().st_size, 'job': roles[Path(name).name]}
              for name in receipt['files']]
    inputs += [{'file': prior['path'], 'bytes': (arm / prior['path']).stat().st_size,
                'job': 'immediately preceding prose: continuity and avoiding repetition'} for prior in receipt['earlier_prose']]
    data = json.loads((out / 'synthesis.json').read_text())
    qeq = (out / 'qeq.md').read_text()
    old_tags = set(re.findall(r'(\d{1,3}:\d{1,3})\s*\[(staging|same-word)\]', qeq))
    corrected_tags = {(r, tag) for r, d in data['passages'].items() for tag in d['tags']}
    result = {'ref': ref, 'arm': arm.name, 'inputs': inputs, 'input_bytes': len(packet.encode()),
              'v13_recorded_writer_bytes': baseline.get('input_bytes'),
              'approx_input_tokens_at_measured_0_45_per_byte': round(len(packet.encode()) * .45),
              'inventory_items': len(data['items']), 'overlapping_navigation_groups': len(data['groups']),
              'tags_recovered_from_v13_parser': sorted(corrected_tags - old_tags),
              'generation_can_prove': 'input inclusion and explicit job, not whether the model internally used it',
              'upstream_changes_in_this_arm': 'none: act, QeQ and network are byte-frozen',
              'not_in_writer_input': ['gold/evaluation criteria', 'target baseline commentary', 'raw discovery scan',
                                      'raw HFT', 'pairs', 'legacy digest usage counts', 'reciprocal candidates'],
              'remaining_gaps': ['Surah commentary and reciprocal final check remain unbuilt.',
                                 'The discovery concordance thresholds entire roots; rare focus lemmas inside frequent roots lack full clauses.',
                                 'Inherited QeQ reads the legacy digest without explicit source-priority or variant-use instructions.',
                                 'QeQ passage leads are mostly references and descriptions, not retrieved Arabic with context.',
                                 'Previous context covers one ayah, not a complete verified surah reader state.',
                                 'Dictionary branches supply first classical phrases, not all attested quotations.']}
    reading = out / f"{ref.replace(':', '_')}.reading.tr.md"
    if reading.exists():
        text = reading.read_text()
        cited = S.prose_passages(text)
        result['observed_after_generation'] = {
            'qeq_candidates': len(data['passages']), 'candidate_passages_cited': len(cited & set(data['passages'])),
            'unused_passage_candidates': sorted(set(data['passages']) - cited),
            'note': 'Citation presence is a retrieval diagnostic, not explanatory quality or mandatory coverage.'}
    return result


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('ref')
    ap.add_argument('--tag', required=True)
    args = ap.parse_args()
    if not re.fullmatch(r'[a-zA-Z0-9_-]+', args.tag):
        ap.error('Invalid tag')
    arm = ROOT / f'out-{args.tag}'
    result = audit(arm, args.ref)
    target = EX.ayah_dir(arm, args.ref) / 'input.audit.json'
    EX.dump(target, result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
