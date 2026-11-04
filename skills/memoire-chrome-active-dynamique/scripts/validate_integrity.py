#!/usr/bin/env python3
"""Structural integrity checker for Memoire Chrome Active Dynamique.
Counts the 41 canonical repositories and reports basic routing health.
Falsifiable: exit code 0 only if exactly 41 entries are present and well-formed.
"""

import sys
from pathlib import Path

MANIFEST = Path(__file__).resolve().parent.parent / "references" / "repo-manifest.md"

REQUIRED_COUNT = 41
CORE_ANCHORS = [
    "Archive-Principale-1",
    "Archive-Principale-2",
    "LogiqueNiPura-Core",
    "Vortex-Architecte",
    "Axiome-Risque-Nickelxiste",
    "Junior-LYE-Technical-Specs",
]


def main() -> int:
    if not MANIFEST.exists():
        print("FAIL: repo-manifest.md missing")
        return 1

    text = MANIFEST.read_text(encoding="utf-8")
    lines = [ln.strip() for ln in text.splitlines() if ln.strip().startswith("|") and "http" in ln]
    count = len(lines)

    print(f"Repository entries detected: {count}")
    if count != REQUIRED_COUNT:
        print(f"FAIL: expected {REQUIRED_COUNT}, got {count}")
        return 1

    missing = [a for a in CORE_ANCHORS if a not in text]
    if missing:
        print(f"FAIL: core anchors missing: {missing}")
        return 1

    print("PASS: structural integrity OK — 41 repositories + core anchors present")
    print("CYCLE_LYE_SEC invariant reference: 30.002103")
    return 0


if __name__ == "__main__":
    sys.exit(main())
