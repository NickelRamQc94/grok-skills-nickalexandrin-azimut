#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BioSKU — Stenosyntaxe Keeping's Kerneling Unit (engine exécutable)
Triplet [Opérateur][Vecteur][État] — format strict 3 caractères.
Falsifiable · déterministe · ancré TNCSA / Parallelodoxe.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional
import math

VALID_OPS = set("KSU")
VALID_VEC = set("0123456789ABCDEFØ")
VALID_STATE = set("0123456789ABCDEFØ")


@dataclass
class BioSKUEngine:
    kernel_registry: Dict[str, Optional[float]] = field(
        default_factory=lambda: {"0": 0.0, "1": 0.0, "X": 0.0, "Ø": None}
    )
    is_connected: bool = False
    state_name: str = "K_cold"
    history: List[str] = field(default_factory=list)

    def shannon_entropy(self, s: str) -> float:
        if not s:
            return 0.0
        from collections import Counter
        c = Counter(s)
        n = len(s)
        return -sum((v / n) * math.log2(v / n) for v in c.values())

    def validate_unit(self, code: str) -> None:
        if len(code) != 3:
            raise ValueError("SKU-01: rigidité sténosyntaxique — longueur ≠ 3")
        op, vec, st = code[0], code[1], code[2]
        if op not in VALID_OPS:
            raise ValueError(f"SKU-02: opérateur invalide {op!r}")
        if vec not in VALID_VEC:
            raise ValueError(f"SKU-03: vecteur invalide {vec!r}")
        if st not in VALID_STATE:
            raise ValueError(f"SKU-04: état invalide {st!r}")

    def execute(self, code_block: str) -> str:
        self.validate_unit(code_block)
        op, vec, st = code_block[0], code_block[1], code_block[2]
        self.history.append(code_block)
        if op == "K":
            if vec in ("1", "X"):
                self.is_connected = True
                self.kernel_registry["X"] = 1.0
                self.state_name = "K_kinetic"
                return "[SKU:KERNELING] Connexion établie. Flux cinétique activé."
            if vec == "0":
                self.kernel_registry = {k: (0.0 if k != "Ø" else None) for k in self.kernel_registry}
                self.is_connected = False
                self.state_name = "K_cold"
                return "[SKU:KEEPING] Registre refroidi (zéro)."
            self.state_name = "K_cold"
            return f"[SKU:KEEPING] Vecteur {vec} enregistré (froid)."
        if op == "S":
            self.state_name = "S_reflex"
            self.kernel_registry["1"] = self.kernel_registry.get("1", 0.0) + 1.0
            return f"[SKU:STENO] Réflexe sténosyntaxique sur vecteur {vec}."
        if op == "U":
            self.state_name = "U_synth"
            nums = [v for v in self.kernel_registry.values() if isinstance(v, (int, float))]
            synth = sum(nums) / len(nums) if nums else 0.0
            self.kernel_registry["X"] = synth
            return f"[SKU:UNIT] Synthèse U — X={synth:.6g} état={st}."
        return "[SKU:NOP]"

    def run_sequence(self, program: List[str]) -> List[str]:
        return [self.execute(u) for u in program]


def main() -> int:
    eng = BioSKUEngine()
    program = ["K11", "S1Ø", "U99"]
    print("BioSKU sequence:", program)
    for line in eng.run_sequence(program):
        print(" ", line)
    print("state:", eng.state_name, "connected:", eng.is_connected)
    print("registry:", eng.kernel_registry)
    H = eng.shannon_entropy("".join(program))
    print(f"Shannon H(program)={H:.6g} bits")
    try:
        eng.execute("BAD")
        print("FAIL: bad unit accepted")
        return 1
    except ValueError:
        print("PASS: bad unit rejected")
    print("LE SYSTÈME EST TOTAL. LOCKÉ EN TABARNAK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
