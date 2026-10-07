#!/bin/bash
# Run v7 spawn files through enrichment/v5/run_codex.py seven at a time; after each batch: check, commit and push.
# Usage: enrichment/v7/run.sh RUN SPAWN_FILE...
set -u
cd /Volumes/aro/projects/prose_generation
run=$1; shift
files=("$@"); n=${#files[@]}; b=0
for ((i=0; i<n; i+=7)); do
  b=$((b+1)); batch=("${files[@]:i:7}")
  echo "== $run batch $b: ${#batch[@]} agents $(date +%H:%M:%S)"
  python3 -B enrichment/v5/run_codex.py "${batch[@]}" --jobs 7
  git add enrichment/v7 >/dev/null 2>&1
  git commit -q -m "v7 digests: $run batch $b (${#batch[@]} agents)" && git push -q 2>&1 | tail -1
done
python3 -B enrichment/v7/digest.py check "$run"
python3 -B enrichment/v7/digest.py report "$run"
echo "== $run done $(date +%H:%M:%S)"
