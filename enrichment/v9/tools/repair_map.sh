#!/bin/bash
# Portable same-session repair; retains the original RUN/unit arguments.
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P) || exit 1
exec python3 -B "$SCRIPT_DIR/repair.py" map "$@"
