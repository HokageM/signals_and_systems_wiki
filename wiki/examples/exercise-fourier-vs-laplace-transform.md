---
title: "Exercise — Fourier vs. Laplace transform"
type: example
sources:
  - "../../raw/signals_3.pdf"
tags:
  - signals-and-systems
  - exercise
  - laplace-transform
---

# Exercise — Fourier vs. Laplace transform

Source: [Lecture 3, pp. 17–20](../../raw/signals_3.pdf). Compares the
[Fourier transform](../concepts/fourier-transform.md) and the
[Laplace transform](../concepts/laplace-transform.md) for the same six
signals.

## a) $x(t) = 1$

- Fourier: $X_{\mathcal F}(f) = \delta(f)$ (standard pair).
- Laplace: $X_{\mathcal L}(s) = \int_{-\infty}^{\infty} e^{-st}\,dt$ does not
  converge for any $s$ — **the Laplace transform does not exist** for this
  signal (p. 17).

## b) $x(t) = \varepsilon(t)$

- Fourier: $X_{\mathcal F}(f) = \tfrac12\delta(f) + \tfrac{1}{j2\pi f}$.
- Laplace: $X_{\mathcal L}(s) = \dfrac{1}{s}$, $\mathrm{Re}\{s\}>0$ (p. 17).

## c) $x(t) = \delta(t)$

- Fourier: $X_{\mathcal F}(f) = 1$.
- Laplace: $X_{\mathcal L}(s) = 1$, for all $s\in\mathbb{C}$ (p. 18).

## d) $x(t) = e^{at}\varepsilon(t)$, $a>0$

- Fourier: does not exist as an ordinary Fourier transform (the signal is
  not absolutely/square integrable, since it grows — not an energy signal).
- Laplace: $X_{\mathcal L}(s) = \dfrac{1}{s-a}$, $\mathrm{Re}\{s\} > a$ (p. 18).

## e) $x(t) = -e^{at}\varepsilon(-t)$, $a>0$

- Fourier: $X_{\mathcal F}(f) = \dfrac{1}{j2\pi f - a}$.
- Laplace: $X_{\mathcal L}(s) = \dfrac{1}{s-a}$, $\mathrm{Re}\{s\} < a$ (p. 19).

Note that (d) and (e) have the **same** Laplace expression $1/(s-a)$ but
**disjoint ROCs** — the ROC alone distinguishes a causal exponential from an
anti-causal one, matching the general observation in
[Laplace transform](../concepts/laplace-transform.md).

## f) $x(t) = \mathrm{rect}(t/T)$

- Fourier: $X_{\mathcal F}(f) = |T|\,si(\pi f T)$ (per
  [Fourier transform pairs](../concepts/fourier-transform-pairs.md)).
- Laplace: $X_{\mathcal L}(s) = \dfrac{1}{s}\Big[e^{sT/2}-e^{-sT/2}\Big]$,
  valid for all $s \in \mathbb{C}$ since `rect` has finite support (p. 19–20).

## Takeaways

- A signal with finite energy generally has **both** a Fourier and a Laplace
  transform, related by $X_{\mathcal F}(f) = X_{\mathcal L}(s)|_{s=j2\pi f}$
  whenever the ROC includes the imaginary axis.
- A one-sided growing exponential has **no** Fourier transform but **does**
  have a Laplace transform (with an ROC that excludes the imaginary axis).
- Pure constants and pure `sgn`-type signals can fail to have a (two-sided)
  Laplace transform at all.

## Related pages

- [Fourier transform](../concepts/fourier-transform.md)
- [Laplace transform](../concepts/laplace-transform.md)
