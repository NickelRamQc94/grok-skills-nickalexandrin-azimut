#!/usr/bin/env python3
"""Count priority signals in a local text file.

Heuristic only. A count is not a proof of relevance, truth, or quantum use.
No network. No writes.
"""

from __future__ import annotations

import sys
from pathlib import Path

TERMS = (
    "algorithme",
    "algorithm",
    "équation",
    "equation",
    "preuve",
    "proof",
    "qbit",
    "qubit",
    "willow",
    "tritbyte",
    "biosku",
    "sha-256",
    "sha256",
)


def score(text: str) -> dict[str, int]:
    folded = text.casefold()
    occupied = [False] * len(folded)
    counts: dict[str, int] = {}
    # Longest first so "algorithme" does not also count as "algorithm",
    # and "sha-256" is not confused with a shorter token.
    for term in sorted(TERMS, key=len, reverse=True):
        count = 0
        start = 0
        while True:
            index = folded.find(term, start)
            if index < 0:
                break
            span = range(index, index + len(term))
            if any(occupied[i] for i in span):
                start = index + 1
                continue
            for i in span:
                occupied[i] = True
            count += 1
            start = index + len(term)
        counts[term] = count
    return counts


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: priorite.py FILE", file=sys.stderr)
        return 2
    path = Path(argv[1])
    text = path.read_text(encoding="utf-8")
    counts = score(text)
    total = sum(counts.values())
    rank = "haute" if total >= 3 else "basse"
    print(f"file: {path}")
    print(f"total: {total}")
    print(f"rang: {rank}")
    print("note: heuristique, pas une preuve")
    for term, count in counts.items():
        if count:
            print(f"  {term}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
