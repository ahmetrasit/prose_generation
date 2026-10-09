#!/bin/bash
# usage: repair_map.sh RUN AYAH(S:A) [UPDATE_N] — same-session repair of one verse map, or of its update N (Sol high)
RUN=$1; AYAH=$2; U=$3; K=${AYAH/:/-}; cd /Volumes/aro/projects/prose_generation
if [ -n "$U" ]; then R=enrichment/v9/work/$RUN/map/runs/v9u_${RUN}_sol-high_${K}_u$U; OUT=$K.u$U.raw.jsonl; else R=enrichment/v9/work/$RUN/map/runs/v9m_${RUN}_sol-high_$K; OUT=$K.raw.jsonl; fi
TID=$(head -1 $R/stream.jsonl | python3 -c "import json,sys;print(json.loads(sys.stdin.readline())['thread_id'])")
[ -n "$TID" ] || { echo "ERROR $R: no thread id in stream.jsonl; not repaired"; exit 1; }
A=$(find /Volumes/aro/codex_sessions_archive -name "*$TID.jsonl" | head -1)
[ -n "$A" ] || [ -n "$(find ~/.codex/sessions -name "*$TID.jsonl" | head -1)" ] || { echo "ERROR $R: session $TID not found (live or archive); not repaired"; exit 1; }
if [ -n "$A" ] && [ -z "$(find ~/.codex/sessions -name "*$TID.jsonl" | head -1)" ]; then D=~/.codex/sessions/${A#/Volumes/aro/codex_sessions_archive/}; mkdir -p "$(dirname "$D")"; cp "$A" "$D"; fi
N=1; while [ -e $R/repair$N.last.txt ]; do N=$((N+1)); done
PROBS=$(python3 -B enrichment/v9/map.py check $RUN --ayah $AYAH 2>&1 | head -80)
{
echo "Repair request for your verse map. You may read and edit only your own output file enrichment/v9/work/$RUN/map/out/sol-high/$OUT and reread your own input parts. The checker reports (first lines):"
echo
echo "$PROBS"
echo
echo "Fix every problem and change nothing else. A note id is written exactly as in the input without the surrounding square brackets (e.g. SOURCE:loc/r1, not [SOURCE:loc/r1]). A note is never in both \"rows\" and \"against\" of the same position: keep it where its text places it. Then run \`python3 -B enrichment/v9/map.py check $RUN --ayah $AYAH\` until it prints OK, and reply with one line."
} > $R/repair$N.message.txt
codex exec resume --ignore-user-config -c model_reasoning_effort="high" -c web_search="disabled" -c sandbox_mode="workspace-write" --skip-git-repo-check --json -o $R/repair$N.last.txt "$TID" - < $R/repair$N.message.txt > $R/repair$N.stream.jsonl 2> $R/repair$N.stderr.txt
echo "$AYAH repair$N rc $?: $(tail -c 300 $R/repair$N.last.txt | tr '\n' ' ')"
