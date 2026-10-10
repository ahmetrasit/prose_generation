#!/bin/bash
# usage: repair_t1.sh RUN N  — same-session repair of one tier-1 chunk
RUN=$1; N=$2
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P) || exit 1
REPO_ROOT=$(cd -- "$SCRIPT_DIR/../../.." && pwd -P) || exit 1
cd -- "$REPO_ROOT" || exit 1
LIVE_DIR=${CODEX_SESSIONS_DIR:-$HOME/.codex/sessions}
ARCHIVE_DIR=${CODEX_SESSIONS_ARCHIVE_DIR:-$REPO_ROOT/.scratch/codex_sessions_archive}
R=enrichment/v7/work/$RUN/runs/v7d_${RUN}_luna-max_c$N
TID=$(head -1 "$R/stream.jsonl" | python3 -c "import json,sys;print(json.loads(sys.stdin.readline())['thread_id'])")
[ -n "$TID" ] || { echo "ERROR $R: no thread id in stream.jsonl; not repaired"; exit 1; }
A=$(find "$ARCHIVE_DIR" -name "*$TID.jsonl" 2>/dev/null | head -1)
LIVE=$(find "$LIVE_DIR" -name "*$TID.jsonl" 2>/dev/null | head -1)
[ -n "$A" ] || [ -n "$LIVE" ] || { echo "ERROR $R: session $TID not found (live or archive); not repaired"; exit 1; }
if [ -n "$A" ] && [ -z "$LIVE" ]; then
  REL=${A#"$ARCHIVE_DIR"/}
  D=$LIVE_DIR/$REL
  mkdir -p "$(dirname "$D")" || exit 1
  cp "$A" "$D" || exit 1
fi
K=1; while [ -e "$R/repair$K.last.txt" ]; do K=$((K+1)); done
PROBS=$(python3 -B enrichment/v7/digest.py check "$RUN" --model luna-max --chunk $((10#$N)) 2>&1)
case "$PROBS" in
  *"legacy input snapshot unavailable"*)
    echo "ERROR $R: original chunk input is unavailable; rebuild this chunk before repair"
    exit 1
    ;;
esac
{
echo "Repair request for your chunk. You may reread only your assigned chunk parts and read and edit only your own output file enrichment/v7/work/$RUN/out/luna-max/c$N.jsonl. The checker reports:"
echo
echo "$PROBS"
echo
echo "Fix every listed problem and change nothing else. An anchor must be one continuous span copied exactly from the segment body, with the same characters and spaces. A tagged word must be a word of that verse's own text; if no word fits, use the whole-verse tag your brief defines. Every segment needs exactly one line. Then run \`python3 -B enrichment/v7/digest.py check $RUN --model luna-max --chunk $((10#$N))\` until it prints OK, and reply with one line."
} > "$R/repair$K.message.txt"
codex exec resume --ignore-user-config -c model_reasoning_effort="max" -c web_search="disabled" -c sandbox_mode="workspace-write" --skip-git-repo-check --json -o "$R/repair$K.last.txt" "$TID" - < "$R/repair$K.message.txt" > "$R/repair$K.stream.jsonl" 2> "$R/repair$K.stderr.txt"
echo "c$N repair$K rc $?: $(tail -c 300 "$R/repair$K.last.txt" | tr '\n' ' ')"
