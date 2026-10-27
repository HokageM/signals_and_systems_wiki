---
title: "Fourier transform properties"
type: concept
sources:
  - "../../raw/signals_2.pdf"
tags:
  - signals-and-systems
  - lecture-2
  - fourier-transform
---

# Fourier transform properties

Source: [Lecture 2, pp. 25–28](../../raw/signals_2.pdf). All pairs use the
notation $x(t) \longleftrightarrow X(f)$; see
[Fourier transform](fourier-transform.md) for the defining integral.

## Linearity and duality

$$\sum_i a_i x_i(t) \longleftrightarrow \sum_i a_i X_i(f)$$

$$\textbf{Duality:}\quad X(t) \longleftrightarrow x(-f)$$

(p. 25).

## Shift, modulation, scaling

$$x(t-t_0) \longleftrightarrow X(f)\,e^{-j2\pi f t_0}, \qquad
e^{j2\pi f_0 t}\,x(t) \longleftrightarrow X(f-f_0)$$

$$x(at) \longleftrightarrow \frac{1}{|a|} X\!\left(\frac{f}{a}\right)$$

(p. 25, p. 26, p. 28).

## Differentiation and integration

$$\frac{d}{dt}x(t) \longleftrightarrow j2\pi f\,X(f), \qquad
-j2\pi t\,x(t) \longleftrightarrow \frac{d}{df}X(f)$$

$$\int_{-\infty}^{t} x(\tau)\,d\tau \longleftrightarrow \frac12 X(0)\,\delta(f) + \frac{1}{j2\pi f}X(f)$$

(p. 28).

## Correlation/convolution duality and Parseval's relation

$$x(t)*y(t) \longleftrightarrow X(f)\,Y(f), \qquad
x(t)\cdot y(t) \longleftrightarrow X(f)*Y(f), \qquad
r_{xy}^{E}(\tau) \longleftrightarrow X^*(f)\,Y(f)$$

$$\int_{-\infty}^{\infty} x(t)\,y^*(t)\,dt = \int_{-\infty}^{\infty} X(f)\,Y^*(f)\,df
\;\Rightarrow\;
E_x = \int_{-\infty}^{\infty} |x(t)|^2\,dt = \int_{-\infty}^{\infty} |X(f)|^2\,df$$

(p. 25, p. 28). See [Power and energy of signals](power-and-energy-of-signals.md).

## Complex Fourier series as a special case

$$x(t) = \sum_{n=-\infty}^{\infty} X_n\,e^{j2\pi n f_0 t} \;\longleftrightarrow\;
X(f) = \sum_{n=-\infty}^{\infty} X_n\,\delta(f-n f_0)$$

(p. 28), connecting to [Fourier series](fourier-series.md).

## Symmetry properties

Writing $x(t) = x_{Re}(t) + x_{Ro}(t) + j x_{Ie}(t) + j x_{Io}(t)$ (real-even,
real-odd, imaginary-even, imaginary-odd parts) and the analogous decomposition
of $X(f)$, the following time/frequency-domain symmetry pairs hold (p. 26):

$$x(-t) \longleftrightarrow X(-f), \qquad
x^*(t) \longleftrightarrow X^*(-f), \qquad
x^*(-t) \longleftrightarrow X^*(f)$$

See [Even/odd decomposition](even-odd-decomposition.md) for the underlying
even/odd and conjugate-even/odd definitions.

## Related pages

- [Fourier transform](fourier-transform.md)
- [Fourier transform pairs](fourier-transform-pairs.md)
