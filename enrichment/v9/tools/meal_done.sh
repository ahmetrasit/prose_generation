#!/bin/bash
# usage: meal_done.sh S A — after a meal agent replies: status, meal check, render the page, commit + push its paths
S=$1; A=$2; cd /Volumes/aro/projects/prose_generation
W=w_${S}_${A}_20261009; M=meal_${S}_${A}_20261009
bash enrichment/v9/tools/page_status.sh $S $A 2>&1 | grep -E " (w|meal):"
python3 -B enrichment/v9/meal.py check $M 2>&1 | tail -1 | grep -q '^OK' || { echo "MEAL CHECK FAILED $S:$A"; python3 -B enrichment/v9/meal.py check $M 2>&1 | tail -5; exit 1; }
python3 -B enrichment/v9/render.py $W --meal $M 2>&1 | tail -2
git add enrichment/v9/work/$M enrichment/v9/work/$W && git commit -qm "S$S meal $S:$A done, page $S:$A rendered" && git push -q && git log --oneline -1
