---
title: "Lecture 1 summary — Signals and Systems"
type: summary
sources:
  - "../../raw/signals_1.pdf"
tags:
  - signals-and-systems
  - lecture-1
---

# Lecture 1 summary — Signals and Systems

Source: [`raw/signals_1.pdf`](../../raw/signals_1.pdf) (27 pages). Handwritten
lecture notes (pages 1–6) followed by two worked exercise sets (pages 7–27).
Mixed German/English headers in the original ("Signale & Systeme"); all wiki
content here is written in English.

## Lecture content (pages 1–6)

1. **Signal classification** — see [Signal classification](../concepts/signal-classification.md).
   Analog, discrete-time, quantized, digital signals (p. 1).
2. **Signal transformations and symmetry** — time shift, reflection, scaling,
   even/odd decomposition for real and complex signals — see
   [Signal transformations](../concepts/signal-transformations.md) and
   [Even/odd decomposition](../concepts/even-odd-decomposition.md) (pp. 1–2).
3. **Elementary signals** — step, ramp, signum, rectangular, triangular,
   real exponential, si-function, causal/anti-causal signals — see
   [Elementary signals](../concepts/elementary-signals.md) (pp. 3–4).
4. **Dirac impulse** — definition, sifting property, scaling property, Dirac
   comb — see [Dirac impulse](../concepts/dirac-impulse.md) (p. 5).
5. **Power and energy of signals** — instantaneous power, average power,
   power of a periodic signal, energy; power-signal vs. energy-signal
   classification — see [Power and energy of signals](../concepts/power-and-energy-of-signals.md) (p. 6).
6. **Orthogonal systems and correlation** — inner product, orthogonality,
   cross-/autocorrelation for energy and power signals, properties of
   correlation (conjugate symmetry, maximum at zero lag) — see
   [Correlation and orthogonality](../concepts/correlation-and-orthogonality.md) (pp. 13–15).

## Worked exercises

- **Exercise 1 — Elementary signals and complex signals** (pp. 7–9): shifted/scaled
  rectangular pulse, period of a sine via the rect function, sketching
  `si(2πf₀t)`, real/imaginary/even/odd parts of `x(t) = 2e^{j2πf₀t}`. See
  [Exercise 1 — Elementary and complex signals](../examples/exercise-1-elementary-and-complex-signals.md).
- **Exercise on power and energy** (pp. 10–12): classifying `x(t) = 0.5 + sin(2πf₀t)`
  (power signal), `x(t) = e^{-a|t|}` (energy signal), and the ramp `x(t) = ρ(t)`
  (neither). See [Exercise — Power and energy classification](../examples/exercise-power-and-energy-classification.md).
- **Exercise 2 — Orthogonality and correlation** (pp. 16–27): orthogonality of
  complex exponentials `e^{j2πkf₀t}`, discrete autocorrelation of
  `x[k] = [1,1,1,-1,-1,1,-1]`, cross-correlation of two length-4 sequences,
  orthogonality of periodic sequences, and the continuous cross-/autocorrelation
  of a ramp-like pulse and a half-height rectangular pulse. See
  [Exercise 2 — Orthogonality and correlation](../examples/exercise-2-orthogonality-and-correlation.md).

## Notation and conventions observed

- Time-domain signals use lowercase `x(t)` (continuous) / `x[k]` (discrete).
- Even/odd parts denoted `x_e(t)`, `x_o(t)`; real/imaginary parts `x_R(t)`, `x_I(t)`.
- Energy-signal correlation uses superscript `E`: `r_xy^E(τ)`; power-signal
  correlation uses superscript `P`: `r_xy^P(τ)`.
- The rectangular function convention used throughout: `rect(t) = 1` for
  `|t| < 1/2`, `1/2` at `|t| = 1/2`, `0` for `|t| > 1/2` (p. 3).

## Open questions / unclear source details

- None of the handwriting in `signals_1.pdf` was illegible or ambiguous enough
  to affect interpretation.
