---
title: "Signal classification"
type: concept
sources:
  - "../../raw/signals_1.pdf"
tags:
  - signals-and-systems
  - fundamentals
---

# Signal classification

Source: [Lecture 1, p. 1](../../raw/signals_1.pdf).

Signals are classified by whether the time axis and the amplitude axis are
continuous or discrete.

| Class | Time axis | Amplitude axis |
|---|---|---|
| Analog | continuous | continuous |
| Discrete-time | discrete | continuous |
| Quantized | continuous | discrete |
| Digital | discrete | discrete |

Continuous-time (analog) signals are written `x(t)`; discrete-time signals are
written `x[k]` with integer index `k`. This distinction underlies the parallel
continuous/discrete formulas used throughout the module, e.g. in
[Power and energy of signals](power-and-energy-of-signals.md) and
[Correlation and orthogonality](correlation-and-orthogonality.md).

## Related pages

- [Signal transformations](signal-transformations.md)
- [Even/odd decomposition](even-odd-decomposition.md)
- [Elementary signals](elementary-signals.md)
- [Lecture 1 summary](../summaries/signals-1.md)
