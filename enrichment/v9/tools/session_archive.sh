#!/bin/bash
# Every 5 minutes move Codex session files idle for 30+ minutes and not open by any process from ~/.codex/sessions
# (system disk) to CODEX_SESSIONS_ARCHIVE_DIR (same relative path). Never deletes: repairs copy sessions
# back. A move across volumes is copy + unlink, so a file still open by an agent is never moved. Failures are logged.
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P) || exit 1
REPO_ROOT=$(cd -- "$SCRIPT_DIR/../../.." && pwd -P) || exit 1
cd -- "$REPO_ROOT" || exit 1
SRC=${CODEX_SESSIONS_DIR:-$HOME/.codex/sessions}
DST=${CODEX_SESSIONS_ARCHIVE_DIR:-$REPO_ROOT/.scratch/codex_sessions_archive}
LOG=$REPO_ROOT/enrichment/v9/work/session_archive.log
mkdir -p "$DST" "$(dirname "$LOG")" || exit 1
while true; do
  if [ ! -d "$DST" ]; then
    echo "$(date '+%F %T') FAILED archive dir $DST missing; nothing moved" >> "$LOG"
  else
    find "$SRC" -type f -name '*.jsonl' -mmin +30 | while read -r f; do
      [ -n "$(lsof -t "$f" 2>/dev/null)" ] && continue
      d="$DST/${f#$SRC/}"
      { mkdir -p "$(dirname "$d")" && mv "$f" "$d"; } 2>>"$LOG" || echo "$(date '+%F %T') FAILED to move $f" >> "$LOG"
    done
  fi
  sleep 300
done
