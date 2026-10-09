#!/bin/bash
# usage: repair_maptr.sh RUN NNN — same-session repair of one Turkish map-rendering chunk (Luna max)
RUN=$1; N=$2; cd /Volumes/aro/projects/prose_generation
R=enrichment/v9/work/$RUN/maptr/runs/v9t_${RUN}_luna-max_c$N
TID=$(head -1 $R/stream.jsonl | python3 -c "import json,sys;print(json.loads(sys.stdin.readline())['thread_id'])")
A=$(find /Volumes/aro/codex_sessions_archive -name "*$TID.jsonl" | head -1)
if [ -n "$A" ] && [ -z "$(find ~/.codex/sessions -name "*$TID.jsonl" | head -1)" ]; then D=~/.codex/sessions/${A#/Volumes/aro/codex_sessions_archive/}; mkdir -p "$(dirname "$D")"; cp "$A" "$D"; fi
K=1; while [ -e $R/repair$K.last.txt ]; do K=$((K+1)); done
PROBS=$(python3 -B enrichment/v9/maptr.py check $RUN --chunk $((10#$N)) 2>&1 | head -80)
{
echo "Repair request for your chunk. You may reread only your assigned chunk parts and read and edit only your own output file enrichment/v9/work/$RUN/maptr/out/luna-max/c$N.jsonl. The checker reports:"
echo
echo "$PROBS"
echo
echo "Translate every listed question or position as your brief defines and change nothing else. Then run \`python3 -B enrichment/v9/maptr.py check $RUN --chunk $((10#$N))\` until it prints OK, and reply with one line."
} > $R/repair$K.message.txt
codex exec resume --ignore-user-config -c model_reasoning_effort="max" -c web_search="disabled" -c sandbox_mode="workspace-write" --skip-git-repo-check --json -o $R/repair$K.last.txt $TID - < $R/repair$K.message.txt > $R/repair$K.stream.jsonl 2> $R/repair$K.stderr.txt
echo "c$N repair$K rc $?: $(tail -c 300 $R/repair$K.last.txt | tr '\n' ' ')"
