#!/usr/bin/env python3
"""Bible-only compatibility entrypoint. Implementation: enrichment/bible/discovery_native.py."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from enrichment.bible.discovery_native import main

if __name__ == '__main__':
    main()
