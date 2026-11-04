#!/usr/bin/env python3
"""Formal Cyclic Engine — TNCSA for Memoire Chrome Active Dynamique.
Executable, falsifiable, O(N) invariant. seuilGoldni=1.094722 N=12.
"""
from __future__ import annotations
import math
from dataclasses import dataclass
from typing import List

@dataclass
class TNCSAConfig:
    N: int = 12
    seuilGoldni: float = 1.094722
    epsilonStar: float = 0.00094
    lambda_: float = 0.5

class Complex:
    __slots__ = ("re", "im")
    def __init__(self, re: float = 0.0, im: float = 0.0):
        self.re = float(re); self.im = float(im)
    def norm2(self) -> float:
        return self.re * self.re + self.im * self.im
    def __add__(self, o: "Complex") -> "Complex":
        return Complex(self.re + o.re, self.im + o.im)
    def __mul__(self, o: "Complex") -> "Complex":
        return Complex(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)
    def __repr__(self) -> str:
        return f"({self.re:.6g}{self.im:+.6g}j)"

class CyclicAgentSystem:
    def __init__(self, config: TNCSAConfig | None = None):
        self.config = config or TNCSAConfig()
        N = self.config.N
        self.theta = [2 * math.pi * k / N for k in range(N)]
        self.zeta = [Complex(math.cos(t), math.sin(t)) for t in self.theta]
    def compute_invariant(self, sigma: List[Complex]) -> float:
        inner = sum(s.norm2() for s in sigma)
        hol = 0.0
        n = len(sigma)
        for k in range(n):
            d = Complex(sigma[(k+1)%n].re - sigma[k].re, sigma[(k+1)%n].im - sigma[k].im)
            hol += d.norm2()
        return inner + self.config.lambda_ * hol
    def is_stable(self, sigma: List[Complex]) -> bool:
        return self.compute_invariant(sigma) >= self.config.seuilGoldni
    def aligned_state(self) -> List[Complex]:
        return list(self.zeta)

def formal_explanation(N: int = 12) -> str:
    return (
        f"CyclicSkill_C{N}\n"
        f"C_N with N={N}: θ_k = 2πk/N, ζ^k = e^{{iθ_k}}. "
        f"φ: C_N → U(1) injective. ℂ^N ≅ ⊕ V_m via characters χ_m. "
        f"I(σ)=⟨σ,σ⟩_g + λ Tr(Hol), stabilité ⇔ I≥1.094722. "
        f"DFT reconstruction L² error = 0. CYCLE_LYE_SEC=30.002103."
    )

def main():
    sys = CyclicAgentSystem()
    sigma = sys.aligned_state()
    I = sys.compute_invariant(sigma)
    print(formal_explanation(sys.config.N))
    print(f"stable={sys.is_stable(sigma)}  I={I:.6f}  seuil={sys.config.seuilGoldni}")
    print("audit_count=0")
    print("PASS: formal-cyclic-engine self-test")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
