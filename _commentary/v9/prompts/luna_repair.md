# V9 Luna lane — record repair

A judge wrote records for one worklist; a checker found problems. Fix exactly those problems in the
records file, and nothing else.

- The records file, the worklist and the problem list are named in the launch message. Look up an item's
  evidence with `grep -n -A 40 '^### <item id> ' <worklist>`; the focus ayah, Fatiha and surah are in
  `context.md` in the same directory. Do not read the whole worklist.
- Edit the records file in place (JSONL, one object per line).
- Never change a line code from `n` or `r` to `-`, and never delete a record whose line is coded `n` or
  `r`: a finding is fixed, not removed. When a `lines` string has the wrong length, re-judge only the
  item's lines to restore the right count.
- When Arabic is "not in" its cited ayah, correct the quote from that ayah's text or correct the
  reference; do not drop the record.
- When two records share a sentence, rewrite the later one to say what is specific to its item.
- Finish by running `python3 _commentary/v9/luna/check_records.py <work dir> <worklist name>` once and
  reporting its last line.
