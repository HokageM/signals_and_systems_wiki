---
title: "Lecture 2 summary — Signals and Systems"
type: summary
sources:
  - "../../raw/signals_2.pdf"
tags:
  - signals-and-systems
  - lecture-2
---

# Lecture 2 summary — Signals and Systems

Source: [`raw/signals_2.pdf`](../../raw/signals_2.pdf) (36 pages). Handwritten
notes covering LTI systems, convolution, Fourier series, and Fourier
transform, interleaved with worked exercises.

## Lecture content

1. **LTI systems** — linearity, time invariance, impulse response — see
   [LTI systems](../concepts/lti-systems.md) (p. 1).
2. **Convolution** — definition, properties, cyclic convolution, convolution
   with a Dirac comb, correlation-as-convolution — see
   [Convolution](../concepts/convolution.md) (pp. 2–3, 9).
3. **Properties of LTI systems** — causality, BIBO stability, memoryless vs.
   dynamic systems — see [LTI systems](../concepts/lti-systems.md) (pp. 10–11).
4. **Fourier series** — taxonomy of transforms, real and complex Fourier
   series, discrete spectrum of periodic signals — see
   [Fourier series](../concepts/fourier-series.md) (pp. 19–21, 36).
5. **Fourier transform** — definition, convergence conditions, convergence
   factor, time–bandwidth product, time-limited vs. band-limited signals —
   see [Fourier transform](../concepts/fourier-transform.md) (pp. 23–24, 27–28).
6. **Fourier transform properties** — linearity, duality, shift, modulation,
   differentiation/integration, Parseval's relation, symmetry properties —
   see [Fourier transform properties](../concepts/fourier-transform-properties.md)
   (pp. 25–28).
7. **Fourier transform pairs** — standard reference table — see
   [Fourier transform pairs](../concepts/fourier-transform-pairs.md) (pp. 25–26, 29).

## Worked exercises

- **Convolution exercises** (pp. 4–8): causal exponential through an
  integrator; raised-cosine impulse response with a rectangular input. See
  [Exercise — Convolution of LTI systems](../examples/exercise-convolution-of-lti-systems.md).
- **Cyclic convolution/correlation** (pp. 9–10): $\cos$/$\sin$ cyclic
  convolution and correlation. See
  [Exercise — Cyclic convolution and correlation](../examples/exercise-cyclic-convolution-and-correlation.md).
- **Pedestrian recognition** (pp. 12–18): a matched-filter application
  distinguishing pedestrian vs. car radar reflections via correlation. See
  [Exercise — Pedestrian recognition](../examples/exercise-pedestrian-recognition.md).
- **Fourier series symmetry** (pp. 21–22): conjugate-even coefficients of a
  real signal; asserted real/complex Fourier series equivalence. See
  [Exercise — Fourier series symmetry and equivalence](../examples/exercise-fourier-series-symmetry-and-equivalence.md).
- **Fourier transform of rect/triangle/periodic signals** (pp. 30–36):
  duality derivations, triangular pulse transform, periodic triangular train
  spectrum, and the Fourier-series/Fourier-transform relationship. See
  [Exercise — Fourier transform of rect, triangle, and periodic signals](../examples/exercise-fourier-transform-rect-triangle-and-periodic-signals.md).

## Notation and conventions observed

- Impulse response $h(t)$; frequency response $H(f)$ (mentioned but not yet
  derived in detail in this lecture).
- Cyclic convolution denoted with $\circledast$.
- Even/odd-type decomposition of $X(f)$ mirrors the time-domain decomposition
  (real-even/real-odd/imaginary-even/imaginary-odd).

## Open questions / unclear source details

- p. 8 (third branch of the raised-cosine convolution exercise): the
  algebra is dense and partly illegible in places; the final closed form was
  not independently re-derived in the wiki page — flagged in
  [Exercise — Convolution of LTI systems](../examples/exercise-convolution-of-lti-systems.md).
- p. 22: the equivalence of the real and complex Fourier series forms is
  asserted in the source ("useless proof!") without full derivation; recorded
  as such in
  [Exercise — Fourier series symmetry and equivalence](../examples/exercise-fourier-series-symmetry-and-equivalence.md).
