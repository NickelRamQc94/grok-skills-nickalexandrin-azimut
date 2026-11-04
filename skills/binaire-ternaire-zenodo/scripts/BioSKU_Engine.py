#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BioSKU Engine v2 — TFSM K_cold/K_kinetic/S_reflex/U_synth. Free gift NickelRamQc94."""
from __future__ import annotations
from collections import Counter
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
import math, time

VALID_OPS = frozenset("KSU")
VALID_VEC = frozenset("0123456789ABCDEFØ")
VALID_STATE = frozenset("0123456789ABCDEFØ")
STATE_COLD, STATE_KINETIC, STATE_REFLEX, STATE_SYNTH = "K_cold", "K_kinetic", "S_reflex", "U_synth"

@dataclass
class BioSKUEngine:
    kernel_registry: Dict[str, Optional[float]] = field(default_factory=lambda: {"0": 0.0, "1": 0.0, "X": 0.0, "Ø": None})
    is_connected: bool = False
    state_name: str = STATE_COLD
    history: List[str] = field(default_factory=list)
    error_count: int = 0
    exec_count: int = 0

    def shannon_entropy(self, s: str) -> float:
        if not s: return 0.0
        c = Counter(s); n = len(s)
        return -sum((v/n)*math.log2(v/n) for v in c.values())

    def snapshot(self):
        return {"state": self.state_name, "connected": self.is_connected, "registry": dict(self.kernel_registry),
                "history_len": len(self.history), "exec_count": self.exec_count, "error_count": self.error_count}

    def reset(self):
        self.kernel_registry = {"0": 0.0, "1": 0.0, "X": 0.0, "Ø": None}
        self.is_connected = False; self.state_name = STATE_COLD
        self.history.clear(); self.error_count = 0; self.exec_count = 0

    def validate_unit(self, code: str):
        if not isinstance(code, str): raise TypeError("SKU-00: code must be str")
        if len(code) != 3: raise ValueError("SKU-01: longueur ≠ 3")
        op, vec, st = code[0], code[1], code[2]
        if op not in VALID_OPS: raise ValueError(f"SKU-02: op {op!r}")
        if vec not in VALID_VEC: raise ValueError(f"SKU-03: vec {vec!r}")
        if st not in VALID_STATE: raise ValueError(f"SKU-04: state {st!r}")
        return op, vec, st

    def execute(self, code_block: str) -> str:
        try:
            op, vec, st = self.validate_unit(code_block)
        except (ValueError, TypeError):
            self.error_count += 1; raise
        self.history.append(code_block); self.exec_count += 1
        if op == "K":
            if vec in ("1", "X"):
                self.is_connected = True; self.kernel_registry["X"] = 1.0; self.state_name = STATE_KINETIC
                return "[SKU:KERNELING] Connexion établie."
            if vec == "0":
                self.kernel_registry = {k: (0.0 if k != "Ø" else None) for k in self.kernel_registry}
                self.is_connected = False; self.state_name = STATE_COLD
                return "[SKU:KEEPING] Registre refroidi."
            self.state_name = STATE_COLD
            return f"[SKU:KEEPING] Vecteur {vec} froid."
        if op == "S":
            self.state_name = STATE_REFLEX
            self.kernel_registry["1"] = float(self.kernel_registry.get("1") or 0.0) + 1.0
            return f"[SKU:STENO] Réflexe {vec}."
        if op == "U":
            self.state_name = STATE_SYNTH
            nums = [float(v) for v in self.kernel_registry.values() if isinstance(v, (int, float))]
            synth = sum(nums)/len(nums) if nums else 0.0
            self.kernel_registry["X"] = synth
            return f"[SKU:UNIT] X={synth:.6g} état={st}."
        return "[SKU:NOP]"

    def run_sequence(self, program):
        return [self.execute(u) for u in program]

    def run_safe(self, program):
        messages, errors = [], []
        for unit in program:
            try: messages.append(self.execute(unit))
            except (ValueError, TypeError) as e: errors.append(f"{unit}: {e}")
        return {"messages": messages, "errors": errors, "snapshot": self.snapshot(),
                "entropy": self.shannon_entropy("".join(u for u in program if len(u)==3))}

def main():
    eng = BioSKUEngine()
    for line in eng.run_sequence(["K11", "S1Ø", "U99"]): print(" ", line)
    try: eng.execute("BAD")
    except ValueError: print("PASS: bad unit rejected")
    eng.reset()
    t0 = time.perf_counter()
    for _ in range(1000):
        eng.reset(); eng.run_sequence(["K11", "S1Ø", "U99"])
    print(f"1000× {((time.perf_counter()-t0)*1000):.3f} ms")
    print("LE SYSTÈME EST TOTAL. LOCKÉ EN TABARNAK.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
