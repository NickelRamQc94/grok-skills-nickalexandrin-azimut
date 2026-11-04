#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BioSKU Ternary — annexe angle ternaire (base 3 / trits)
========================================================
Préfixe Bio-  : couche du vivant / organisme / flux (applicable à tout langage)
Suffixe -SKU  : Stenosyntaxe Keeping's Kerneling Unit (triplet Op·Vec·État)

Cette annexe fixe l'ANGLE d'observation : tout symbole SKU est lu/écrit
via des trits (0,1,2) non balancés, 6 trits ≈ 1 octet (schéma tritbyte).
Même langue SKU, lunette ternaire du même château.
"""
from __future__ import annotations
from typing import List
import math

try:
    from BioSKU_Engine import BioSKUEngine
except ImportError:
    try:
        from scripts.BioSKU_Engine import BioSKUEngine
    except ImportError:
        BioSKUEngine = None


def byte_to_trits(b: int) -> str:
    b = b & 0xFF
    trits = []
    for _ in range(6):
        trits.append(str(b % 3))
        b //= 3
    return "".join(trits)


def trits_to_byte(t: str) -> int:
    t = "".join(c for c in t if c in "012")[:6].ljust(6, "0")
    v = 0
    p = 1
    for c in t:
        v += int(c) * p
        p *= 3
    return min(v, 255)


def text_to_trits(s: str) -> str:
    return "".join(byte_to_trits(b) for b in s.encode("utf-8"))


def sku_unit_to_trits(unit: str) -> str:
    if len(unit) != 3:
        raise ValueError("SKU unit must be length 3")
    return text_to_trits(unit)


def trits_favorability(trits: str) -> dict:
    if not trits:
        return {"entropy": 0.0, "aligned6": True, "favorable_ternary": False}
    from collections import Counter
    c = Counter(trits)
    n = len(trits)
    ent = 0.0
    for ch in "012":
        p = c.get(ch, 0) / n
        if p > 0:
            ent -= p * math.log2(p)
    aligned = (n % 6 == 0)
    diversity = sum(1 for ch in "012" if c.get(ch, 0) > 0)
    return {
        "entropy_bits": ent,
        "aligned6": aligned,
        "diversity": diversity,
        "favorable_ternary": aligned and diversity >= 2 and ent > 0.5,
    }


def run_demo() -> int:
    program = ["K11", "S1Ø", "U99"]
    print("=== BioSKU Ternary (angle base-3) ===")
    print("Préfixe Bio- + suffixe -SKU · lunette ternaire")
    for u in program:
        tr = sku_unit_to_trits(u)
        fav = trits_favorability(tr)
        print(f"  {u} → {tr} | favorable={fav['favorable_ternary']} H={fav['entropy_bits']:.3f}")
    if BioSKUEngine is not None:
        eng = BioSKUEngine()
        for line in eng.run_sequence(program):
            print(" ", line)
    print("LE SYSTÈME EST TOTAL. LOCKÉ EN TABARNAK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(run_demo())
