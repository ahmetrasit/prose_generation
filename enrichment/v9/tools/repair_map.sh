#!/bin/bash
# usage: repair_map.sh RUN AYAH(S:A) — same-session repair of one verse map (Sol high)
RUN=$1; AYAH=$2; K=${AYAH/:/-}; cd /Volumes/aro/projects/prose_generation
R=enrichment/v9/work/$RUN/map/runs/v9m_${RUN}_sol-high_$K
TID=$(head -1 $R/stream.jsonl | python3 -c "import json,sys;print(json.loads(sys.stdin.readline())['thread_id'])")
A=$(find /Volumes/aro/codex_sessions_archive -name "*$TID.jsonl" | head -1)
if [ -n "$A" ] && [ -z "$(find ~/.codex/sessions -name "*$TID.jsonl" | head -1)" ]; then D=~/.codex/sessions/${A#/Volumes/aro/codex_sessions_archive/}; mkdir -p "$(dirname "$D")"; cp "$A" "$D"; fi
N=1; while [ -e $R/repair$N.last.txt ]; do N=$((N+1)); done
PROBS=$(python3 -B enrichment/v9/map.py check $RUN --ayah $AYAH 2>&1 | head -80)
{
echo "Repair request for your verse map. You may read and edit only your own output file enrichment/v9/work/$RUN/map/out/sol-high/$K.raw.jsonl and reread your own input parts. The checker reports (first lines):"
echo
echo "$PROBS"
echo
echo "Fix every problem and change nothing else. A note id is written exactly as in the input without the surrounding square brackets (e.g. SOURCE:loc/r1, not [SOURCE:loc/r1]). A note is never in both \"rows\" and \"against\" of the same position: keep it where its text places it. Then run \`python3 -B enrichment/v9/map.py check $RUN --ayah $AYAH\` until it prints OK, and reply with one line."
} > $R/repair$N.message.txt
codex exec resume --ignore-user-config -c model_reasoning_effort="high" -c web_search="disabled" -c sandbox_mode="workspace-write" --skip-git-repo-check --json -o $R/repair$N.last.txt $TID - < $R/repair$N.message.txt > $R/repair$N.stream.jsonl 2> $R/repair$N.stderr.txt
echo "$AYAH repair$N rc $?: $(tail -c 300 $R/repair$N.last.txt | tr '\n' ' ')"
