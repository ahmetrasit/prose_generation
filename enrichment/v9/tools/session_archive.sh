#!/bin/bash
# Every 5 minutes move Codex session files idle for 10+ minutes from ~/.codex/sessions (system disk) to
# /Volumes/aro/codex_sessions_archive/ (same relative path). Never deletes: repairs copy sessions back. Runs until killed.
SRC=$HOME/.codex/sessions; DST=/Volumes/aro/codex_sessions_archive
while true; do
  find "$SRC" -type f -name '*.jsonl' -mmin +10 | while read -r f; do
    d="$DST/${f#$SRC/}"; mkdir -p "$(dirname "$d")" && mv "$f" "$d"
  done
  sleep 300
done
