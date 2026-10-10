#!/bin/bash
# corpus_parts.sh — regenerate the committed copy of the Islamic corpus index:
# enrichment/corpus/corpus.sqlite -> corpus.sqlite.gz.partNN (90 MiB each) + corpus.sqlite.gz.stamp.json.
# Refuses a stale index (corpus.py fresh). The new parts are built and verified (reassembled and compared with the
# index byte for byte) in a scratch directory; the committed parts are replaced only after that check passes.
# Then: git add -f the parts and the stamp, commit, push.
# Reassemble on another machine: cat enrichment/corpus/corpus.sqlite.gz.part* | gunzip > enrichment/corpus/corpus.sqlite
set -euo pipefail
cd /Volumes/aro/projects/prose_generation
C=enrichment/corpus
T=$C/.parts.building
python3 -B enrichment/v2/tools/corpus.py fresh | grep -v '^committed gz parts' || { echo "index stale: rebuild first"; exit 1; }
rm -rf "$T"; mkdir "$T"
gzip -c -6 $C/corpus.sqlite > "$T/corpus.sqlite.gz"
split -b 94371840 -a 2 "$T/corpus.sqlite.gz" "$T/p."
n=0; for f in "$T"/p.??; do mv "$f" "$(printf '%s/corpus.sqlite.gz.part%02d' "$T" $n)"; n=$((n+1)); done
[ $n -le 99 ] || { echo "more than 99 parts: the two-digit names would not sort"; exit 1; }
cat "$T"/corpus.sqlite.gz.part[0-9][0-9] | gunzip | cmp - $C/corpus.sqlite || { echo "parts do not reassemble to the index (did it change during the run?); committed parts untouched"; exit 1; }
rm -f $C/corpus.sqlite.gz.part[0-9][0-9]
mv "$T"/corpus.sqlite.gz.part[0-9][0-9] $C/
mv "$T/corpus.sqlite.gz" $C/corpus.sqlite.gz
rmdir "$T"
python3 - <<'EOF'
import hashlib, json, time
from pathlib import Path
C = Path('enrichment/corpus')
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()
db = C / 'corpus.sqlite'
parts = sorted(C.glob('corpus.sqlite.gz.part[0-9][0-9]'))
stamp = {'built_at': time.strftime('%Y-%m-%dT%H:%M:%S%z', time.localtime(db.stat().st_mtime)),
         'sqlite_sha256': sha(db), 'sqlite_bytes': db.stat().st_size,
         'parts': {p.name: sha(p) for p in parts},
         'check': 'python3 -B enrichment/v2/tools/corpus.py fresh'}
(C / 'corpus.sqlite.gz.stamp.json').write_text(json.dumps(stamp, indent=1) + '\n')
print(f"{len(parts)} parts, verified, stamp written ({stamp['built_at']})")
EOF
