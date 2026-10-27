---
title: "LTI systems"
type: concept
sources:
  - "../../raw/signals_2.pdf"
tags:
  - signals-and-systems
  - lecture-2
  - lti-systems
---

# LTI systems

Source: [Lecture 2, pp. 1, 10–11](../../raw/signals_2.pdf).

A system is **linear and time-invariant (LTI)** if it satisfies both:

- **Linearity**: for input $x_T(t)$ producing output $y_T(t)$,
  $\sum_i a_i x_i(t) \Rightarrow \sum_i a_i y_i(t)$ (superposition).
- **Time invariance**: a shifted input produces an identically shifted output
  — "the signal behaves identically regardless of shift" (p. 1).

## Impulse response

The impulse response $h(t)$ of an LTI system is the (normalized) output
signal $y(t)$ when the input is a (normalized) Dirac impulse
$x(t) = \delta(t)$: $h(t) = y(t)/U$ for $x(t) = U\delta(t)$ (p. 1). An LTI
system is fully characterized either by its impulse response $h(t)$ in the
time domain, or equivalently by its frequency response $H(f)$ in the
frequency domain (p. 1, p. 10). The output is obtained via
[convolution](convolution.md): $y(t) = h(t) * x(t)$.

## Causal systems

A system is **causal** if the output $y(t_0)$ at any time $t_0$ does not
depend on future input values $x(t > t_0)$ (p. 10). Equivalently:

$$h(t) = 0 \text{ for } t < 0, \qquad y(t_0) = \mathcal{H}\{x(t \le t_0)\}$$

## Stable systems (BIBO stability)

A system is **BIBO-stable** (bounded-input, bounded-output) if every bounded
input $|x(t)| < \infty$ produces a bounded output $|y(t)| < \infty$. For LTI
systems this holds if and only if the impulse response is absolutely
integrable (p. 10):

$$\int_{-\infty}^{\infty} |h(\tau)|\,d\tau < \infty$$

## Memoryless vs. dynamic systems

A system is **memoryless** (static) if the output $y(t_0)$ depends only on
the input value $x(t_0)$ at the same instant; otherwise it is called
**dynamic** (p. 11). The notes sketch a simple dynamic system combining a
direct path (gain $h_0$) and a delayed/filtered path (gain $h_1$), with an
added noise term at the output (p. 11).

## Related pages

- [Convolution](convolution.md)
- [Exercise — Convolution of LTI systems](../examples/exercise-convolution-of-lti-systems.md)
- [Exercise — Pedestrian recognition](../examples/exercise-pedestrian-recognition.md)
