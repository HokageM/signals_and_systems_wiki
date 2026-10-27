---
title: "Exercise — Cyclic convolution and correlation"
type: example
sources:
  - "../../raw/signals_2.pdf"
tags:
  - signals-and-systems
  - exercise
---

# Exercise — Cyclic convolution and correlation

Source: [Lecture 2, pp. 9–10](../../raw/signals_2.pdf). Builds on
[Convolution](../concepts/convolution.md) (cyclic convolution) and
[Correlation and orthogonality](../concepts/correlation-and-orthogonality.md).

Given $x(t) = \cos(2\pi f_0 t)$ and $y(t) = \sin(2\pi f_0 t)$, common period
$T = 1/f_0$.

## a) Cyclic convolution $x(t) \circledast y(t)$

$$x(t)\circledast y(t) = \int_0^{1/f_0} \cos(2\pi f_0 \tau)\,\sin\big(2\pi f_0(t-\tau)\big)\,d\tau$$

Using the product-to-sum identity
$\sin(\alpha)\cos(\beta) = \tfrac12\big[\sin(\alpha-\beta)+\sin(\alpha+\beta)\big]$:

$$= \int_0^{1/f_0} \tfrac12\Big[\sin\big(2\pi f_0(t-2\tau)\big) + \sin(2\pi f_0 t)\Big]\,d\tau$$

The first term integrates to zero over the full period (integrand oscillates
over whole periods); only the constant-in-$\tau$ term survives:

$$x(t) \circledast y(t) = \frac{1}{2}\sin(2\pi f_0 t)\cdot T = \frac{T}{2}\sin(2\pi f_0 t)$$

(p. 9).

## b) Cyclic (power) correlation $r_{xy}^{P}(\tau)$

By the same mechanism,

$$r_{xy}^{P}(\tau) = \frac{1}{2}\sin(2\pi f_0 \tau)$$

(p. 10).

## c) Interpretation at specific lags

- $r_{xy}^{P}(0) = 0$ — confirms $\cos \perp \sin$ (orthogonal), consistent
  with [Correlation and orthogonality](../concepts/correlation-and-orthogonality.md).
- $r_{xy}^{P}\!\left(\dfrac{T}{4}\right) = \dfrac12\sin\!\left(\dfrac{\pi f_0}{2f_0}\right) = \dfrac12$ —
  the correlation of two identical (in-phase) signals yields the full power.
- $r_{xy}^{P}\!\left(\dfrac{3T}{4}\right) = \dfrac12\sin\!\left(\dfrac{3\pi}{2}\right) = -\dfrac12$

(p. 10).

## Related pages

- [Convolution](../concepts/convolution.md)
- [Correlation and orthogonality](../concepts/correlation-and-orthogonality.md)
