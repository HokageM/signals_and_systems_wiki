---
title: "Lecture 5 summary — Signals and Systems"
type: summary
sources:
  - "../../raw/signals_5.pdf"
tags:
  - signals-and-systems
  - lecture-5
---

# Lecture 5 summary — Signals and Systems

Source: [`raw/signals_5.pdf`](../../raw/signals_5.pdf) (17 pages).
Handwritten notes introduce digital FIR and IIR filters, pole-zero analysis,
stability, and a shelving-filter design.

## Lecture content

1. **FIR and IIR filters** — non-recursive convolution form and recursive
   difference equations, transfer functions, and convolution-matrix
   representation. See [Digital filters](../concepts/digital-filters.md)
   (pp. 1–3).
2. **Pole-zero analysis and stability** — evaluate a filter on the unit
   circle for its magnitude and phase response; stable causal filters have
   poles strictly inside the unit circle, while non-recursive filters are
   BIBO stable. See [Digital filters](../concepts/digital-filters.md)
   (pp. 4–6).
3. **Allpass, minimum-phase, and linear-phase filters** — pole-zero
   reciprocal relationships, FIR zero patterns, and a comb-filter example
   (pp. 6–7).
4. **Shelving filters** — analog first-order prototype, response gain
   parameter, all-pass digital section, and combination into a digital
   shelving filter. See
   [Exercise — Digital filters](../examples/exercise-digital-filters.md)
   (pp. 11–17).

## Worked examples

- **FIR filter** $H(z)=1+z^{-1}+0.5z^{-2}$: finite impulse response and
  minimum-phase zero locations (pp. 8–9).
- **Recursive filter**: difference equation, transfer function, poles, zero,
  causality, and stability (pp. 9–10).
- **Digital shelving filter**: a one-pole all-pass section combined with a
  direct path to obtain the stated response (pp. 11–17).

## Notation and conventions observed

- Delay elements are written $z^{-1}$.
- The transfer function is $H(z)=Y(z)/X(z)$.
- Frequency response is evaluated at $z=e^{j\Omega}$.
- $G_0$ sets the analog shelf's low-frequency gain, and $a_c$ parameterizes
  the digital all-pass section.

## Open questions / unclear source details

- No materially ambiguous notation was identified in the examples summarized
  here. The filter equations and their pole/zero locations were checked
  against the displayed transfer functions.
