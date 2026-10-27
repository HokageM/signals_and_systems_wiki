---
title: "Exercise — Fourier series symmetry and equivalence"
type: example
sources:
  - "../../raw/signals_2.pdf"
tags:
  - signals-and-systems
  - exercise
  - fourier-series
---

# Exercise — Fourier series symmetry and equivalence

Source: [Lecture 2, pp. 21–22](../../raw/signals_2.pdf). Builds on
[Fourier series](../concepts/fourier-series.md).

## a) Setup

The complex Fourier series of a periodic function $x(t)$ is

$$x(t) = \sum_{n=-\infty}^{\infty} X_n\,e^{j2\pi n f_0 t}, \qquad
X_n = \frac{1}{T}\int_{-T/2}^{T/2} x(t)\,e^{-j2\pi n f_0 t}\,dt$$

(p. 21).

## b) Show that the coefficients of a real periodic signal are conjugate-even: $X_n = X_{-n}^{*}$

$$X_n = \frac{1}{T}\int_{-T/2}^{T/2} x(t)\Big[\cos(-2\pi n f_0 t) + j\sin(-2\pi n f_0 t)\Big]\,dt$$

$$X_{-n} = \frac{1}{T}\int_{-T/2}^{T/2} x(t)\Big[\cos(-2\pi n f_0 t) - j\sin(-2\pi n f_0 t)\Big]\,dt$$

$$X_{-n}^{*} = \frac{1}{T}\int_{-T/2}^{T/2} x(t)\Big[\cos(-2\pi n f_0 t) + j\sin(-2\pi n f_0 t)\Big]\,dt = X_n \qquad \blacksquare$$

(p. 21), using that $x(t)$ is real so complex conjugation only flips the sign
of the imaginary ($j\sin$) term. This matches the general conjugate-even
symmetry pattern in
[Even/odd decomposition](../concepts/even-odd-decomposition.md).

## c) Equivalence of the real and complex Fourier series forms

The notes assert, without a full derivation ("useless proof!", p. 22, a
self-deprecating annotation in the original), that the real Fourier series

$$x(t) = \frac{A_0}{2} + \sum_{n=1}^{\infty} A_n\cos(2\pi n f_0 t) + \sum_{n=1}^{\infty} B_n\sin(2\pi n f_0 t)$$

is equivalent to the complex form, with $X_n = X_{n,r} + jX_{n,i}$ relating to
$A_n$, $B_n$ via the standard identities
$A_n = 2\,\mathrm{Re}(X_n)$, $B_n = -2\,\mathrm{Im}(X_n)$ for $n \ge 1$, and
$A_0 = 2X_0$ (p. 22). The source does not work through the full substitution
here; treat this equivalence as asserted rather than independently verified
in this note set.

## Related pages

- [Fourier series](../concepts/fourier-series.md)
- [Even/odd decomposition](../concepts/even-odd-decomposition.md)
