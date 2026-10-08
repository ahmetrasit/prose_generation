#!/bin/bash
# step.sh map N MAPDIR   -> finish the map, check, commit+push; if ok, build images --spawn and verify its spawn.md
# step.sh images N IMGDIR -> finish the images, check, commit+push
set -u
R=/Volumes/aro/projects/prose_generation
V=$R/_commentary/v16
SP=/private/tmp/claude-502/-Volumes-aro-projects-prose-generation/80004558-da45-451e-b9cc-9a2fb4ee95d6/scratchpad
kind=$1; n=$2; d=$3; s=$(printf "s%03d" $n)
cd $R
echo "### finish $kind S$n"
out=$(python3 -B _commentary/v16/packets.py finish --run out/$s/$d 2>&1)
rc=$?
echo "$out" | grep -v "^NOTE: no HFT records"
if echo "$out" | grep -qE "WARNING|BLOCKED|Traceback|partial|error"; then echo "STOP: finish printed a warning/failure; no next step built"; rc=99; fi
echo "finish exit $rc"
python3 $SP/postcheck.py out/$s/$d | grep -v "other tool: Bash: python3 $V/missing.py "
if [ "$kind" = map ]; then
  f=$V/out/$s/$d/map.md
  [ -f "$f" ] && { echo "map.md $(wc -c < $f) chars; sections: $(grep '^## ' $f | tr '\n' ' ')"; } || echo "NO map.md"
  git add _commentary/v16/out/$s/$d _commentary/v16/out/ledger.jsonl
  cost=$(python3 -c "import json;r=[json.loads(l) for l in open('$V/out/ledger.jsonl')];r=[x for x in r if x.get('ref')=='S$n' and x.get('arm')=='surah'][-1];print(f\"{r['status']}, \${r.get('cost_usd') or 0:.2f} vs \${r['estimate_usd']} est\")")
  git commit -q -m "S$n surah map ($d): $cost" && git push -q 2>&1 | tail -2
  echo "committed: S$n map $cost"
  if [ $rc -eq 0 ] && [ -f "$f" ]; then
    python3 -B _commentary/v16/packets.py images --surah $n --brief r13 --tool --map out/$s/$d/map.md --spawn 2>&1 | grep -v "^NOTE: no HFT records"
    img=images.r13.${d#surah.}.tool
    T=$(sed 's#out/s096/surah.map3.nohft.tool#DIR#g' $V/out/s096/surah.map3.nohft.tool/spawn.md | md5)
    [ "$(sed "s#out/$s/$img#DIR#g" $V/out/$s/$img/spawn.md | md5)" = "$T" ] && echo "SPAWN READY: out/$s/$img (template-ok)" || echo "SPAWN TEXT DIFFERS: out/$s/$img"
  fi
else
  f=$V/out/$s/$d/images.md
  [ -f "$f" ] && { echo "images.md $(wc -c < $f) chars; ## sections: $(grep -c '^## ' $f); Buluşmalar: $(grep -c '^## Buluşmalar' $f); Kaynaklar lines: $(grep -c 'Kaynaklar:' $f)"; } || echo "NO images.md"
  ls $V/out/$s/$d
  git add _commentary/v16/out/$s/$d _commentary/v16/out/ledger.jsonl
  cost=$(python3 -c "import json;r=[json.loads(l) for l in open('$V/out/ledger.jsonl')];r=[x for x in r if x.get('ref')=='S$n' and x.get('arm')=='images'][-1];print(f\"{r['status']}, \${r.get('cost_usd') or 0:.2f} vs \${r['estimate_usd']} est, check {r.get('check')} {r.get('check_findings') or ''}\")")
  git commit -q -m "S$n surah commentary ($d): $cost" && git push -q 2>&1 | tail -2
  echo "committed: S$n images $cost"
fi
