---
title: "Lecture 3 summary — Signals and Systems"
type: summary
sources:
  - "../../raw/signals_3.pdf"
tags:
  - signals-and-systems
  - lecture-3
---

# Lecture 3 summary — Signals and Systems

Source: [`raw/signals_3.pdf`](../../raw/signals_3.pdf) (32 pages). Handwritten
notes covering LTI systems in the frequency domain, phase/group delay, the
Laplace transform, and LTI systems in the s-domain, interleaved with worked
exercises.

## Lecture content

1. **LTI system frequency response and filter types** — magnitude/phase
   response, transmission factor, attenuation/gain in dB, frequency-flat vs.
   selective systems, lowpass/highpass/bandpass/bandstop filters — see
   [LTI system frequency response and filter types](../concepts/lti-frequency-response.md) (pp. 1–3).
2. **Phase delay, group delay, distortion-free systems** — see
   [Phase and group delay](../concepts/phase-and-group-delay.md) (pp. 4–5).
3. **Laplace transform** — definition, ROC, relation to the Fourier
   transform, causal complex exponentials, standard pairs, properties
   table — see [Laplace transform](../concepts/laplace-transform.md) (pp. 14–16, 21).
4. **LTI systems in the s-domain** — transfer function, pole-zero plots,
   allpass filters, minimum-/maximum-phase filters, BIBO stability via pole
   location — see [LTI systems in the s-domain](../concepts/lti-systems-s-domain.md)
   (pp. 22–24, 28–30).

## Worked exercises

- **Group and phase delay of an allpass filter** (pp. 6–7). See
  [Exercise — Group and phase delay of an allpass filter](../examples/exercise-group-and-phase-delay-allpass-filter.md).
- **Multicarrier transmission** (pp. 8–13): transmitting two cosine carriers
  through a real/even frequency response, checking orthogonality at
  different frequency ratios, and designing a triangular bandpass filter to
  isolate one carrier. See
  [Exercise — Multicarrier transmission](../examples/exercise-multicarrier-transmission.md).
- **Fourier vs. Laplace transform** (pp. 17–20): side-by-side comparison for
  six standard signals, highlighting when each transform exists. See
  [Exercise — Fourier vs. Laplace transform](../examples/exercise-fourier-vs-laplace-transform.md).
- **Inverse Laplace transform and region of convergence** (pp. 25–27): partial
  fractions and three different inverse transforms of the same $X(s)$
  depending on the chosen ROC. See
  [Exercise — Inverse Laplace transform and region of convergence](../examples/exercise-inverse-laplace-transform-and-roc.md).
- **Analog filter design** (pp. 28–32): pole-zero plot, stability check,
  magnitude-squared response, and the damped-oscillation impulse response of
  a second-order analog filter. See
  [Exercise — Analog filter design](../examples/exercise-analog-filter-design.md).

## Notation and conventions observed

- Transfer function in the s-domain: $H(s)$, with $s=\sigma+j2\pi f$.
- ROC abbreviated $\kappa$ in the properties table.
- Poles/zeros of $H(s)$ written $s_{\infty\ell}$ / $s_{0k}$ respectively.

## Open questions / unclear source details

- p. 9: the multicarrier exercise's general correlation formula for
  $f_2=2f_1$ appears to suggest nonzero correlation (flagged with "!" in the
  original), while the direct per-period integral the student computes
  immediately after evaluates to zero. The wiki page records this tension
  explicitly and treats the direct per-period computation as authoritative;
  revisit if this becomes relevant to later material.
- p. 10–11: the exact passband edge behavior for $f_2=2f_1$ under the
  triangular bandpass filter was transcribed from a partially dense
  derivation; re-check against the source if a precise attenuation value is
  needed.
