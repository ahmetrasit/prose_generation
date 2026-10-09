#!/bin/bash
# Pause every codex_run.py runner (SIGSTOP: no new agents start; running agents finish) while the system disk has
# under 1.5 GB free; resume them (SIGCONT) above 2.5 GB. Logs each change. Runs until killed.
LOG=/Volumes/aro/projects/prose_generation/enrichment/v9/work/disk_throttle.log
state=run
while true; do
  free=$(df -k / | tail -1 | awk '{print $4}')
  if [ $free -lt 1500000 ] && [ $state = run ]; then
    pkill -STOP -f "codex_run.py"; state=paused; echo "$(date +%H:%M) paused runners, free ${free}k" >> $LOG
  elif [ $free -gt 2500000 ] && [ $state = paused ]; then
    pkill -CONT -f "codex_run.py"; state=run; echo "$(date +%H:%M) resumed runners, free ${free}k" >> $LOG
  fi
  sleep 30
done
