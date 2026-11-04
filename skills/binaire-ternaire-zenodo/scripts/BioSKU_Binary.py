#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BioSKU Binary — annexe angle binaire (base 2)
==============================================
Préfixe Bio-  : couche du vivant / organisme / flux (applicable à tout langage)
Suffixe -SKU  : Stenosyntaxe Keeping's Kerneling Unit (triplet Op·Vec·État)

Cette annexe fixe l'ANGLE d'observation : tout symbole SKU est lu/écrit
via des octets binaires (8 bits). Ce n'est pas une autre langue : c'est
la même langue SKU vue par la lunette binaire du château.
"""
from __future__ import annotations
from typing import List, Tuple
import math

try:
    from BioSKU_Engine import BioSKUEngine
except ImportError:
    try:
        from scripts.BioSKU_Engine import BioSKUEngine
    except ImportError:
        BioSKUEngine = None


def text_to_bits(s: str) -> str:
    return "".join(f"{b:08b}" for b in s.encode("utf-8"))


def bits_to_text(bits: str) -> str:
    bits = "".join(c for c in bits if c in "01")
    if len(bits) % 8:
        bits = bits[: len(bits) - (len(bits) % 8)]
    data = bytes(int(bits[i : i + 8], 2) for i in range(0, len(bits), 8))
    return data.decode("utf-8", errors="replace")


def sku_unit_to_bits(unit: str) -> str:
    if len(unit) != 3:
        raise ValueError("SKU unit must be length 3")
    return text_to_bits(unit)


def bits_favorability(bits: str) -> dict:
    if not bits:
        return {"entropy": 0.0, "ones_ratio": 0.0, "byte_aligned": True}
    ones = bits.count("1")
    n = len(bits)
    p1 = ones / n
    p0 = 1.0 - p1
    ent = 0.0
    for p in (p0, p1):
        if p > 0:
            ent -= p * math.log2(p)
    return {
        "entropy_bits": ent,
        "ones_ratio": p1,
        "byte_aligned": (n % 8 == 0),
        "favorable_binary": (n % 8 == 0) and 0.05 < p1 < 0.95,
    }


def run_demo() -> int:
    program = ["K11", "S1Ø", "U99"]
    print("=== BioSKU Binary (angle base-2) ===")
    print("Préfixe Bio- + suffixe -SKU · lunette binaire")
    for u in program:
        bits = sku_unit_to_bits(u)
        fav = bits_favorability(bits)
        print(f"  {u} → {bits} | favorable={fav['favorable_binary']} H={fav['entropy_bits']:.3f}")
    if BioSKUEngine is not None:
        eng = BioSKUEngine()
        for line in eng.run_sequence(program):
            print(" ", line)
    print("LE SYSTÈME EST TOTAL. LOCKÉ EN TABARNAK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(run_demo())
