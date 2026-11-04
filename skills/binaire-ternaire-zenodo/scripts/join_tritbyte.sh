#!/bin/bash
# M1 helper — reconstruct tritbyte.py from part1+part2
set -e
P1="${1:-tritbyte.part1.py}"
P2="${2:-tritbyte.part2.py}"
OUT="${3:-tritbyte.py}"
grep -v '^# PART ' "$P1" > "$OUT.tmp" || cp "$P1" "$OUT.tmp"
grep -v '^# PART ' "$P2" >> "$OUT.tmp" || cat "$P2" >> "$OUT.tmp"
mv "$OUT.tmp" "$OUT"
python3 -m py_compile "$OUT"
echo "OK $OUT"
