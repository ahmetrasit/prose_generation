#!/bin/bash
# Smoke test: check.py on the existing outputs named in the E0 task. Writes smoke/check/*.json and prints one line each.
cd "$(dirname "$0")"
C=../../..
run() { python3 check.py "$1" --ref "$2" --out "smoke/check/$3.json"; }
run $C/v15/out-nocap/s004/4_34/commentary.tr.md 4:34 v15nocap_4_34
run $C/v15/out-nocap/s005/5_6/commentary.tr.md 5:6 v15nocap_5_6
for f in $C/review/experiments/e1/*/rep*/*.reading.tr.md; do
  sa=$(basename "$(dirname "$(dirname "$f")")"); rep=$(basename "$(dirname "$f")"); run "$f" "${sa/_/:}" "e1_${sa}_${rep}"; done
for f in $C/review/experiments/e2/*/rep*/final.tr.md; do
  sa=$(basename "$(dirname "$(dirname "$f")")"); rep=$(basename "$(dirname "$f")"); run "$f" "${sa/_/:}" "e2_${sa}_${rep}"; done
for f in $C/v9/lines/work/*/synth/w10-opus-cold*/*.reading.tr.md; do
  arm=$(basename "$(dirname "$f")"); sa=$(basename "$(dirname "$(dirname "$(dirname "$f")")")"); run "$f" "${sa/_/:}" "v9_${arm}_${sa}"; done
