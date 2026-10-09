#!/bin/bash
# Run spawn files through codex_run.py; after each pass move agents that failed at start (0 commands, $0: network
# outage or full disk) aside with rerun_failed_start.py and run again after a pause, until none fail (at most 8 passes).
#   run_until_done.sh PARALLEL RUNS_DIR LOG SPAWN_FILE…
P=$1; RUNS=$2; LOG=$3; shift 3
cd /Volumes/aro/projects/prose_generation
for pass in 1 2 3 4 5 6 7 8; do
  echo "== pass $pass $(date +%H:%M)" >> $LOG
  python3 -B enrichment/v9/codex_run.py --parallel $P "$@" | grep -v "already run" >> $LOG
  out=$(python3 -B enrichment/v9/tools/rerun_failed_start.py $RUNS); echo "$out" >> $LOG
  if echo "$out" | grep -q ": 0 agent"; then
    # agents that started earlier without run.json (runner killed, timeout) are not failed starts: report them
    w=$(sed -n "/== pass $pass /,\$p" $LOG | grep -c "started earlier without run.json")
    [ "$w" -gt 0 ] && echo "== WARNING $w agent(s) started earlier without run.json (running, or died: recover_run_json.py)" >> $LOG
    echo "== done" >> $LOG; exit 0
  fi
  sleep 120
done
echo "== WARNING still failing at start after 8 passes" >> $LOG
