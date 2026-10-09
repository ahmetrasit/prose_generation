#!/bin/bash
# Pause every codex_run.py runner (SIGSTOP: no new agents start; running agents finish) while the system disk has
# under 1.5 GB free; resume them (SIGCONT) above 2.5 GB. The signal is sent on every check (not only on a change), so
# a restarted throttle or a runner started during a pause is brought to the right state. Resumes all on exit.
LOG=/Volumes/aro/projects/prose_generation/enrichment/v9/work/disk_throttle.log
PAT='enrichment/v9/codex_run.py --parallel'
trap 'pkill -CONT -f "$PAT"; echo "$(date +%H:%M) throttle exiting, runners resumed" >> $LOG; exit' EXIT TERM INT
state=run
while true; do
  free=$(df -k / | tail -1 | awk '{print $4}')
  if ! [ "$free" -ge 0 ] 2>/dev/null; then
    echo "$(date +%H:%M) could not read free space ('$free')" >> $LOG
  elif [ "$free" -lt 1500000 ]; then
    pkill -STOP -f "$PAT"; [ $state = run ] && echo "$(date +%H:%M) paused runners, free ${free}k" >> $LOG; state=paused
  elif [ "$free" -gt 2500000 ]; then
    pkill -CONT -f "$PAT"; [ $state = paused ] && echo "$(date +%H:%M) resumed runners, free ${free}k" >> $LOG; state=run
  fi
  sleep 30
done
