---
title: "Signal transformations: shift, reflection, scaling"
type: concept
sources:
  - "../../raw/signals_1.pdf"
tags:
  - signals-and-systems
  - fundamentals
---

# Signal transformations: shift, reflection, scaling

Source: [Lecture 1, pp. 1–2](../../raw/signals_1.pdf).

Given a signal `x(t)`, three elementary transformations of the time axis are
used repeatedly in the module:

- **Right shift** by `t₀ > 0`: `x(t − t₀)` moves the signal to the right.
- **Reflection**: `x(−t)` mirrors the signal about `t = 0`.
- **Scaling** by `a`: `x(a·t)` compresses the time axis for `|a| > 1` and
  stretches it for `|a| < 1`; a feature originally at `t = t₀` appears at
  `t = t₀ / a` (p. 1, p. 2).

These transformations apply identically to real and complex-valued signals,
and combine with the [even/odd decomposition](even-odd-decomposition.md) and
with the elementary signals defined in [Elementary signals](elementary-signals.md)
(e.g. the shifted/scaled rectangular pulse used in
[Exercise 1](../examples/exercise-1-elementary-and-complex-signals.md)).

## Causal and anti-causal signals

A signal is **causal** if `x(t) = 0` for `t < 0`, and **anti-causal** if
`x(t) = 0` for `t > 0` (p. 2). This property is used, for example, to restrict
the real exponential in [Elementary signals](elementary-signals.md) to `t ≥ 0`.

## Related pages

- [Signal classification](signal-classification.md)
- [Even/odd decomposition](even-odd-decomposition.md)
- [Lecture 1 summary](../summaries/signals-1.md)
