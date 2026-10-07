#!/bin/bash
# Run v5 spawn files through run_codex.py seven at a time; after each batch: progress check, commit and push (v5 only).
# Usage: enrichment/v5/run_batches.sh LABEL SPAWN_FILE...
set -u
cd /Volumes/aro/projects/prose_generation
label=$1; shift
files=("$@"); n=${#files[@]}; b=0
for ((i=0; i<n; i+=7)); do
  b=$((b+1)); batch=("${files[@]:i:7}")
  echo "== $label batch $b: ${#batch[@]} agents $(date +%H:%M:%S)"
  python3 -B enrichment/v5/run_codex.py "${batch[@]}" --jobs 7
  git add enrichment/v5 >/dev/null 2>&1
  git commit -q -m "v5 pilot: $label batch $b (${#batch[@]} Luna max extractors)" && git push -q 2>&1 | tail -1
done
echo "== $label done $(date +%H:%M:%S)"
