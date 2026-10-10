#!/bin/bash
# Retry only evidenced failures before session creation. Every other failure needs
# same-session repair. Session completion still requires the stage checker/report.
# usage: run_until_done.sh PARALLEL RUNS_DIR LOG SPAWN_FILE...
if [ "$#" -lt 4 ]; then echo "usage: $0 PARALLEL RUNS_DIR LOG SPAWN_FILE..." >&2; exit 1; fi
P=$1; RUNS=$2; LOG=$3; shift 3
case "$P" in ''|*[!0-9]*) echo "PARALLEL must be a positive integer" >&2; exit 1;; esac
[ "$P" -gt 0 ] || exit 1
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P) || exit 1
cd -- "$SCRIPT_DIR/../../.." || exit 1
mkdir -p "$RUNS" "$(dirname -- "$LOG")" || exit 1
for pass in 1 2 3 4 5 6 7 8; do
  echo "== pass $pass $(date +%H:%M)" >> "$LOG" || exit 1
  python3 -B enrichment/v9/codex_run.py --parallel "$P" --runs-dir "$RUNS" "$@" >> "$LOG" 2>&1
  runner_rc=$?
  recovery=$(python3 -B enrichment/v9/tools/rerun_failed_start.py "$RUNS" 2>&1)
  recovery_rc=$?
  echo "$recovery" >> "$LOG"
  if [ "$recovery_rc" -ne 0 ]; then
    echo "== WARNING startup recovery failed; see above" >> "$LOG"; exit 1
  fi
  if echo "$recovery" | grep -q ': 0 agent'; then
    if [ "$runner_rc" -ne 0 ]; then
      echo "== WARNING sessions failed or remain unfinished; use same-session repair/recovery and the stage checker" >> "$LOG"
      exit 1
    fi
    echo "== sessions completed; run the stage checker and report before proceeding" >> "$LOG"
    exit 0
  fi
  [ "$pass" -eq 8 ] || sleep 120
done
echo "== WARNING still failing before session creation after 8 passes" >> "$LOG"
exit 1
