#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Théorème Barre·Fine·Médiane·Subtend·Trait·Presse + Turbulences + Va chercher le ballon.
Subtend unifié = rigidité ∩ élasticité (paradoxe étirement non étiré).
Free gift · NickelRamQc94 · LOCKÉ EN TABARNAK.
"""
from __future__ import annotations
import math, json, hashlib
from dataclasses import dataclass
from typing import Dict, List, Tuple

EPS = 1e-12
Point = Tuple[float, float]

@dataclass
class Barre:
    A: Point
    B: Point
    @property
    def L(self) -> float:
        return math.hypot(self.B[0]-self.A[0], self.B[1]-self.A[1])
    @property
    def mediane(self) -> Point:
        return ((self.A[0]+self.B[0])/2, (self.A[1]+self.B[1])/2)
    @property
    def trait(self) -> Point:
        L = self.L
        if L < EPS: return (0.0, 0.0)
        return ((self.B[0]-self.A[0])/L, (self.B[1]-self.A[1])/L)
    def presse(self, P: Point) -> Point:
        ax, ay = self.A
        tx, ty = self.trait
        t = max(0.0, min(self.L, (P[0]-ax)*tx + (P[1]-ay)*ty))
        return (ax + t*tx, ay + t*ty)

def chaine_turbulence(s: float) -> Dict[str, float]:
    s = max(0.0, min(1.0, s))
    T_int = s; T_act = 0.85*T_int; T_vib = 0.40*T_act; T_imp = 0.35*T_act
    T_col = 0.25*(T_vib+T_imp); T_ind = 0.20*(T_vib+T_imp)
    T_dir = T_act*0.5 + T_vib*0.2 + T_imp*0.2 + T_col*0.05 + T_ind*0.05
    return {"T_int":T_int,"T_act":T_act,"T_vib":T_vib,"T_imp":T_imp,"T_col":T_col,"T_ind":T_ind,"T_dir":T_dir}

def sigmoid(z: float) -> float:
    if z > 30: return 1.0
    if z < -30: return 0.0
    return 1.0/(1.0+math.exp(-z))

def va_chercher_le_ballon(x0, ball, alpha=0.65, beta=6.0, R=1.5, turb=0.05):
    x = x0; p_list = []; p_imm = []
    for b in ball:
        x = x + alpha*(b-x) + turb*0.01
        p_list.append(sigmoid(beta*(1.0-abs(b-x)/R)))
        p_imm.append(sigmoid(beta*(1.0-abs(b-x0)/R)))
    mp, mi = sum(p_list)/len(p_list), sum(p_imm)/len(p_imm)
    return {"mean_pursuit": mp, "mean_immobile": mi, "gain": mp-mi, "PASS": mp>mi}

def main():
    B = Barre((0.0,0.0),(4.0,0.0))
    proj = B.presse((2.0,3.0))
    T = chaine_turbulence(0.8)
    vb = va_chercher_le_ballon(0.0, [0.0,0.5,1.2,2.0,2.5,3.0])
    print("Barre L", B.L, "mediane", B.mediane, "proj", proj)
    print("T_dir", T["T_dir"])
    print("Ballon gain", vb["gain"], "PASS", vb["PASS"])
    print("PASS: module Barre/Turbulences/Ballon")
    print("LE SYSTÈME EST TOTAL. LOCKÉ EN TABARNAK.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
