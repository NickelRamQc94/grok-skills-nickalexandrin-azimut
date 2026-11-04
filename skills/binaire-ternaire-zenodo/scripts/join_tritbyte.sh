#!/bin/bash
# M1 — Reconstruct tritbyte.py from part files
set -euo pipefail
P1="${1:-tritbyte.part1.py}"
P2="${2:-tritbyte.part2.py}"
OUT="${3:-tritbyte.py}"
{
  grep -v '^# PART ' "$P1" || cat "$P1"
  grep -v '^# PART ' "$P2" || cat "$P2"
} > "$OUT.tmp"
mv "$OUT.tmp" "$OUT"
python3 -m py_compile "$OUT"
echo "OK compiled $OUT"
ls -la "$OUT"
