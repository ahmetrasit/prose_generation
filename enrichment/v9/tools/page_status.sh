#!/bin/bash
# page_status.sh S A — writer and meal check + Opus cost for one page of the S surah plan (date from plan.json)
S=$1; A=$2; cd /Volumes/aro/projects/prose_generation
D=$(python3 -c "import json;print(json.load(open('enrichment/v9/work/prod_s$(printf %03d $((10#$S)))/plan.json'))['date'])")
for k in w meal; do
  run=${k}_${S}_${A}_$D; [ $k = w ] && script=writer.py agent=/root/v9w_${run}_opus-high_$S-$A || { script=meal.py; agent=/root/v9meal_${run}_opus-high_$S-$A; }
  [ -d enrichment/v9/work/$run ] || { echo "$S:$A $k: not built"; continue; }
  chk=$(python3 -B enrichment/v9/$script check $run 2>&1 | tail -1)
  usd=$(python3 -B -c "import sys;sys.path.insert(0,'enrichment/v7');import digest;u=digest.claude_usage('$agent');print('not run' if u is None else f\"\${u['usd']:.2f} completed={u['completed']}\")")
  echo "$S:$A $k: $chk | $usd"
done
