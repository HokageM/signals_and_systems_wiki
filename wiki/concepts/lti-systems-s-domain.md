---
title: "LTI systems in the s-domain"
type: concept
sources:
  - "../../raw/signals_3.pdf"
tags:
  - signals-and-systems
  - lecture-3
  - laplace-transform
  - stability
---

# LTI systems in the s-domain

Source: [Lecture 3, pp. 22–24, 28–30](../../raw/signals_3.pdf). Builds on
[Laplace transform](laplace-transform.md) and [LTI systems](lti-systems.md).

## Transfer function

$$y(t) = h(t)*x(t) \;\Longleftrightarrow\; Y(s) = H(s)\,X(s), \qquad H(s) = \frac{Y(s)}{X(s)}$$

An LTI system is characterized equally by $h(t)$ (time domain), $H(f)$
(frequency domain), or $H(s)$ (s-domain); $H(f) = H(s)\big|_{s=j2\pi f}$
(p. 22).

## Rational transfer functions, poles, and zeros

$$H(s) = \frac{f_\mu}{b_N}\cdot\frac{\prod_{k=1}^{\mu}(s-s_{0k})}{\prod_{\ell=1}^{N}(s-s_{\infty\ell})}$$

where $s_{0k}$ are **zeros** and $s_{\infty\ell}$ are **poles** of $H(s)$ (p. 22).
Except for the leading gain factor $f_\mu/b_N$, a rational $H(s)$ is
completely described by its **pole-zero plot** (p. 23). Rational functions
$R(s)$ with real coefficients have only real or complex-conjugate-pair poles
and zeros (p. 23).

$$|H(f)| = |H(s)|_{s=j2\pi f} = \left|\frac{f_\mu}{b_N}\right|
\frac{\prod_k |j2\pi f - s_{0k}|}{\prod_\ell |j2\pi f - s_{\infty\ell}|}$$

$$\varphi(f) = \angle\!\left(\frac{f_\mu}{b_N}\right) + \sum_k \angle(j2\pi f - s_{0k}) - \sum_\ell \angle(j2\pi f - s_{\infty\ell})$$

(p. 22).

## Allpass filters

An allpass filter has constant magnitude response and poles/zeros related by
$s_{0k} = -s_{\infty k}^{*}$ (mirror images about the imaginary axis) — it
causes only a frequency-dependent phase shift and group delay, no amplitude
distortion (p. 24). See [Phase and group delay](phase-and-group-delay.md).

## Minimum-phase and maximum-phase filters

- **Minimum-phase filter**: all zeros in the left half-plane.
- **Maximum-phase filter**: all zeros in the right half-plane.

Both can share the same magnitude response; **minimum-phase filters have
minimum group delay** among all filters with that magnitude response.
**Mixed-phase filters** can be decomposed into the cascade (convolution) of a
minimum-phase subsystem and an allpass subsystem (p. 24).

## BIBO stability via pole location

A system is BIBO stable iff $\int_{-\infty}^{\infty}|h(\tau)|\,d\tau < \infty$
(see [LTI systems](lti-systems.md)). For a causal exponential
$h(t)=e^{at}\varepsilon(t) \leftrightarrow H(s) = 1/(s-a)$:

| Pole location | System behavior |
|---|---|
| Left half-plane | **Stable** (decaying response) |
| Right half-plane | **Unstable** (growing response) |
| On the imaginary axis | **Quasi-stable** (constant-amplitude oscillation) |

(pp. 28–29). Summary:

| | Stable | Quasi-stable | Unstable |
|---|---|---|---|
| Pole condition | All poles in left half-plane | All poles in left half-plane, or simple poles on the imaginary axis | Any pole in the right half-plane, or multiple poles on the imaginary axis |

For a **causal** system, the convergence region is always a **right
half-plane** bounded by the rightmost pole (p. 29, p. 30).

## Related pages

- [Laplace transform](laplace-transform.md)
- [LTI system frequency response and filter types](lti-frequency-response.md)
- [Phase and group delay](phase-and-group-delay.md)
- [Exercise — Analog filter design](../examples/exercise-analog-filter-design.md)
