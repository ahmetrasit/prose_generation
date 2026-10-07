#!/bin/bash
# Run a v7 stage's spawn files through enrichment/v5/run_codex.py (Codex), seven at a time; after each batch commit
# and push; at the end the stage's check and report. Agents that already have a run.json are skipped (never rerun).
# Usage: enrichment/v7/run.sh RUN tier1|tier2|write [TAG]     e.g. run.sh s103-1 tier1 luna-max
set -u
cd /Volumes/aro/projects/prose_generation
run=$1; stage=$2; tag=${3:-}
w=enrichment/v7/work/$run
case $stage in
  tier1) dir=$w/spawn ;;
  tier2) dir=$w/tier2/spawn ;;
  write) dir=$w/write/spawn ;;
  *) echo "stage must be tier1, tier2 or write"; exit 2 ;;
esac
if [ -n "$tag" ]; then files=($(ls "$dir"/"$tag"_*.md 2>/dev/null | sort)); else files=($(ls "$dir"/*.md 2>/dev/null | sort)); fi
n=${#files[@]}
[ "$n" -eq 0 ] && { echo "no spawn files in $dir${tag:+ for $tag}"; exit 2; }
echo "== $run $stage${tag:+ $tag}: $n agents"
b=0
for ((i=0; i<n; i+=7)); do
  b=$((b+1)); batch=("${files[@]:i:7}")
  echo "== batch $b: ${#batch[@]} agents $(date +%H:%M:%S)"
  python3 -B enrichment/v5/run_codex.py "${batch[@]}" --jobs 7
  git add enrichment/v7 >/dev/null 2>&1
  git commit -q -m "v7 $stage: $run batch $b (${#batch[@]} agents)" && git push -q 2>&1 | tail -1
done
case $stage in
  tier1) python3 -B enrichment/v7/digest.py check "$run"; python3 -B enrichment/v7/digest.py report "$run" ;;
  tier2) python3 -B enrichment/v7/merge.py check "$run"; python3 -B enrichment/v7/merge.py report "$run" ;;
  write) python3 -B enrichment/v7/write.py check "$run" --model "${tag:?write needs a TAG}"; python3 -B enrichment/v7/write.py report "$run" ;;
esac
git add enrichment/v7 >/dev/null 2>&1
git commit -q -m "v7 $stage: $run checks and report" && git push -q 2>&1 | tail -1
echo "== $run $stage done $(date +%H:%M:%S)"
