---
title: "Laplace transform"
type: concept
sources:
  - "../../raw/signals_3.pdf"
tags:
  - signals-and-systems
  - lecture-3
  - laplace-transform
---

# Laplace transform

Source: [Lecture 3, pp. 14–16, 21](../../raw/signals_3.pdf). Generalizes the
[Fourier transform](fourier-transform.md).

## Definition

$$X_{\mathcal{L}}(s) = \int_{-\infty}^{\infty} x(t)\,e^{-st}\,dt, \qquad
s = \sigma + j\omega = \sigma + j2\pi f, \qquad x(t) \longleftrightarrow X(s)$$

The Laplace transform exists only if **both** one-sided integrals converge:

$$\int_0^{\infty} x(t)\,e^{-st}\,dt \quad\text{and}\quad \int_{-\infty}^{0} x(t)\,e^{-st}\,dt$$

The set of $s$ for which this holds is the **region of convergence (ROC)**
(p. 14). The inverse Laplace transform (Bromwich integral) is

$$x(t) = \frac{1}{2\pi j}\int_{\sigma-j\infty}^{\sigma+j\infty} X(s)\,e^{st}\,ds$$

(p. 14). A two-sided signal such as $x(t) = e^{a|t|}$ has **no common
convergence region** between its causal and anti-causal parts, so its
two-sided Laplace transform does not exist (p. 14) — unlike the one-sided
exponentials in the pairs table below, which do converge.

## Relation to the Fourier transform

$$X_{\mathcal{F}}(f) = X_{\mathcal{L}}(s)\big|_{s=j2\pi f}$$

valid whenever the ROC of the Laplace transform **includes the imaginary
axis**; in that case both transforms exist and are related by this
substitution (p. 15).

## Causal complex exponential and pole location

For $x(t) = e^{at}\varepsilon(t)$ with $a = \mathrm{Re}\{a\} + j\,\mathrm{Im}\{a\}$:

$$X(s) = \frac{1}{s-a}, \qquad \text{pole at } s=a$$

- $\mathrm{Re}\{a\} < 0$: decaying oscillation (stable-looking time behavior).
- $\mathrm{Re}\{a\} > 0$: growing oscillation.
- $\mathrm{Re}\{a\} = 0$: constant-amplitude oscillation.

(p. 21). This pole-location/time-behavior correspondence underlies
[LTI systems in the s-domain](lti-systems-s-domain.md) (BIBO stability via
pole location).

## Some standard pairs

| $x(t)$ | $X_{\mathcal{L}}(s)$ | ROC |
|---|---|---|
| $\delta(t)$ | $1$ | all $s$ |
| $x(t)=1$ | does not exist | — |
| $\varepsilon(t)$ | $1/s$ | $\mathrm{Re}\{s\}>0$ |
| $\mathrm{rect}(t/T)$ | $\tfrac{1}{s}\big(e^{sT/2}-e^{-sT/2}\big)$ | all $s$ |
| $\mathrm{sgn}(t)$ | does not exist | — |
| $e^{at}\varepsilon(t)$ | $\tfrac{1}{s-a}$ | $\mathrm{Re}\{s\}>\mathrm{Re}\{a\}$ |
| $-e^{at}\varepsilon(-t)$ | $\tfrac{1}{s-a}$ | $\mathrm{Re}\{s\}<\mathrm{Re}\{a\}$ |

(pp. 15–16, 25). Note the pair $e^{at}\varepsilon(t) \leftrightarrow 1/(s-a)$
and $-e^{at}\varepsilon(-t) \leftrightarrow 1/(s-a)$ share the **same formula**
but different ROCs — the ROC is essential to recovering the correct inverse
transform. See
[Exercise — Fourier vs. Laplace transform](../examples/exercise-fourier-vs-laplace-transform.md)
and
[Exercise — Inverse Laplace transform and region of convergence](../examples/exercise-inverse-laplace-transform-and-roc.md).

## Properties

| $x(t)$ | $X(s)$ | ROC note |
|---|---|---|
| $\sum_i a_i x_i(t)$ | $\sum_i a_i X_i(s)$ | $\kappa \supseteq \bigcap_i \kappa_i$ |
| $x(t-t_0)$ | $e^{-st_0}X(s)$ | $\kappa$ |
| $e^{at}x(t)$ | $X(s-a)$ | $\kappa$ shifted by $a$ |
| $\int_{-\infty}^{t} x(\tau)d\tau$ | $\tfrac{1}{s}X(s)$ | |
| $x(at)$, $a>0$ | $\tfrac{1}{a}X(s/a)$ | $\kappa \cdot a$ |
| $x^*(t)$ | $X^*(s^*)$ | $\kappa$ |
| $x(-t)$ | $X(-s)$ | $-\kappa$ |
| $x^*(-t)$ | $X^*(-s)$ | $-\kappa$ |
| $x(t)*y(t)$ | $X(s)\,Y(s)$ | $\kappa \supseteq \kappa_x \cap \kappa_y$ |
| $\dfrac{d}{dt}x(t)$ | $s\,X(s)$ | |
| $-t\,x(t)$ | $\dfrac{d}{ds}X(s)$ | |

(p. 16).

## Related pages

- [Fourier transform](fourier-transform.md)
- [LTI systems in the s-domain](lti-systems-s-domain.md)
- [Exercise — Fourier vs. Laplace transform](../examples/exercise-fourier-vs-laplace-transform.md)
- [Exercise — Inverse Laplace transform and region of convergence](../examples/exercise-inverse-laplace-transform-and-roc.md)
