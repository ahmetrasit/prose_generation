#!/usr/bin/env python3
"""Per-paragraph markdown tables for REPORT.md from results.json (config B, the faithful method)."""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent
R = json.loads((HERE / 'results.json').read_text())
B = 'B faithful (lex+pat+tr)'
for ay, res in R.items():
    print(f'\n**{ay}**\n')
    print('| ¶ | verses cited | roots | all notes (chars) | kept by B (chars) | kept % chars |')
    print('|---|---|---|---|---|---|')
    for p, d in res['paras'].items():
        b = res['baseline']['per_para'][p]
        c = res['configs'][B]['per_para'][p]
        print(f"| {p} | {len(d['cites'])} | {len(d['roots'])} | {b['n']:,} ({b['chars']:,}) | {c['n']:,} ({c['chars']:,}) | "
              f"{100 * c['chars'] / b['chars']:.0f}% |")
