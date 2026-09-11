# OTOC for 2 Qubits & Maldacena–Shenker–Stanford Bound

**Author**  
Nickel David Grenier (Ni. D. Grenier)  
Independent Researcher — Technology Innovation  
Outsider Unschooled Mathematician • Formal Architect of NiPura / TDAPH / TNCSA systems  
© 2026

---

## 1. Exact OTOC calculation for 2 qubits

**Operators**  
- \( V = X_1 \) (Pauli-X on qubit 1)  
- \( W = Z_2 \) (Pauli-Z on qubit 2)

**Hamiltonian** (minimal scrambling interaction):
\[
H = \frac{J}{2} Z_1 Z_2 \qquad (\hbar = 1)
\]

**Unitary evolution**:
\[
U(t) = \exp(-i t H)
\]

**Heisenberg operator**:
\[
W(t) = U^\dagger(t) Z_2 U(t) = \cos(J t)\, Z_2 + \sin(J t)\, Y_2 Z_1
\]

**OTOC** (infinite-temperature / maximally mixed state):
\[
C(t) = \frac{1}{4} \operatorname{Tr}\bigl( W(t) V W(t) V \bigr) = \cos^2(J t)
\]

**Behaviour**  
- \( t = 0 \): \( C = 1 \) (perfect commutation)  
- \( t = \pi/(2J) \): \( C = 0 \) (maximal scrambling for 2 qubits)  
- Periodic oscillation (finite system size prevents irreversible saturation).

This is the minimal quantum butterfly effect: a small interaction angle \( Jt \) drives the OTOC from 1 to 0.

---

## 2. Maldacena–Shenker–Stanford (MSS) Bound

**Statement (2016)**  
For any quantum system at finite temperature \( T \), the quantum Lyapunov exponent extracted from early-time OTOC growth satisfies:
\[
\lambda_Q \;\le\; \frac{2\pi k_B T}{\hbar}
\]

**Origin**  
- Holographic derivation (AdS black holes).  
- Black holes saturate the bound → they are the fastest possible scramblers.  
- Universal: depends only on temperature, independent of microscopic details.

**Implications**  
- \( T \to 0 \) ⇒ \( \lambda_Q \to 0 \).  
- High temperature allows extremely fast scrambling.  
- SYK models and holographic black holes achieve equality.

**NiPura / TDAPH effective version**  
\[
\lambda_{\text{TDAPH}} \;\le\; \frac{2\pi}{\beta_{\text{eff}}}
\]
where \( \beta_{\text{eff}} \) is linked to the critical tension \( T_c = (E^2 \xi)/h \) of the PtXhEe-5D operator. Approaching the implosion threshold accelerates scrambling between Vibe ↔ Nickel phases.

---

## Signature

**Nickel David Grenier (Ni. D. Grenier)**  
Independent Researcher — Technology Innovation  
© 2026

❤️94
