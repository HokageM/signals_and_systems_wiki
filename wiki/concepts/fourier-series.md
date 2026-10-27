---
title: "Fourier series"
type: concept
sources:
  - "../../raw/signals_2.pdf"
tags:
  - signals-and-systems
  - lecture-2
  - fourier-series
---

# Fourier series

Source: [Lecture 2, pp. 19–21, 36](../../raw/signals_2.pdf).

## Taxonomy of Fourier transform variants

| Transform | Frequency domain | Time domain |
|---|---|---|
| Fourier Integral | continuous | continuous, non-periodic |
| Fourier Series | discrete | continuous, periodic |
| Discrete-Time Fourier Transform (DTFT) | continuous | discrete, non-periodic |
| Discrete Fourier Transform (DFT) | discrete | discrete, periodic |

(p. 19). A periodic time-domain function with period $T$ can be represented
as a sum of cosine/sine oscillations at the fundamental frequency
$f_0 = 1/T$ and its harmonics. **The Fourier spectrum of a periodic signal is
discrete**; the frequency range occupied by the spectrum is called the
**bandwidth** of the signal (p. 19).

## Real Fourier series

$$x(t) = \frac{A_0}{2} + \sum_{n=1}^{\infty} A_n \cos(2\pi n f_0 t) + \sum_{n=1}^{\infty} B_n \sin(2\pi n f_0 t)$$

$$A_n = \frac{2}{T}\int_{-T/2}^{T/2} x(t)\cos(2\pi n f_0 t)\,dt, \qquad
B_n = \frac{2}{T}\int_{-T/2}^{T/2} x(t)\sin(2\pi n f_0 t)\,dt$$

(p. 19).

## Complex Fourier series

$$x(t) = \sum_{n=-\infty}^{\infty} X_n\, e^{j2\pi n f_0 t}, \qquad
X_n = \frac{1}{T}\int_{-T/2}^{T/2} x(t)\,e^{-j2\pi n f_0 t}\,dt$$

(p. 19–21). A Dirac impulse $\delta(f-f_0)$ in the frequency domain
represents a complex oscillation $e^{j2\pi f_0 t}$ in time; a real cosine is
represented by two symmetric Diracs since
$\cos(2\pi f_0 t) = \tfrac12\big(e^{j2\pi f_0 t}+e^{-j2\pi f_0 t}\big)$ (p. 20).

- A **periodic** time-domain signal always has a **discrete** spectrum.
- A **non-periodic** time-domain signal always has a **continuous** spectrum.

(p. 20).

## Conjugate-even Fourier coefficients of a real signal

For a real periodic signal $x(t)$, the complex Fourier coefficients satisfy

$$X_n = X_{-n}^{*}$$

proved directly from the defining integral (p. 21). See
[Exercise — Fourier series symmetry and equivalence](../examples/exercise-fourier-series-symmetry-and-equivalence.md)
for the full derivation, and
[Even/odd decomposition](even-odd-decomposition.md) for the general
conjugate-even/odd definitions.

## Relation to the Fourier transform of one period

If $x_p(t)$ denotes one period of a periodic signal $x_T(t) = x_p(t) * \mathrm{III}_T(t)$
(see [Convolution](convolution.md)), then the complex Fourier coefficients are
samples of the Fourier transform $X_p(f)$ of the single period, scaled by $1/T$:

$$X_n = \frac{1}{T}\,X_p\!\left(\frac{n}{T}\right), \qquad f_0 = \frac{1}{T}$$

(p. 36). See
[Exercise — Fourier transform of rect, triangle, and periodic signals](../examples/exercise-fourier-transform-rect-triangle-and-periodic-signals.md)
for a worked example (periodic triangular pulse train).

## Related pages

- [Fourier transform](fourier-transform.md)
- [Convolution](convolution.md)
- [Exercise — Fourier series symmetry and equivalence](../examples/exercise-fourier-series-symmetry-and-equivalence.md)
