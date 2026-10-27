---
title: "Even/odd and conjugate-symmetric decomposition"
type: concept
sources:
  - "../../raw/signals_1.pdf"
tags:
  - signals-and-systems
  - fundamentals
---

# Even/odd and conjugate-symmetric decomposition

Source: [Lecture 1, pp. 1–2, 9](../../raw/signals_1.pdf).

## Real signals: even and odd parts

Any real signal can be written as the sum of an even part and an odd part:

$$x(t) = x_e(t) + x_o(t)$$

with

$$x_e(t) = x_e(-t) = \tfrac{1}{2}\big[x(t) + x(-t)\big], \qquad
x_o(t) = -x_o(-t) = \tfrac{1}{2}\big[x(t) - x(-t)\big]$$

(p. 1).

## Complex signals: real/imaginary parts

A complex signal is split into real and imaginary parts:

$$x(t) = x_R(t) + j\,x_I(t), \qquad
x_R(t) = \tfrac{1}{2}\big[x(t) + x^*(t)\big], \qquad
x_I(t) = \tfrac{1}{2j}\big[x(t) - x^*(t)\big]$$

(p. 1).

## Conjugate-even and conjugate-odd signals (symmetry of complex signals)

For complex signals, "even" and "odd" generalize to **conjugate-even** and
**conjugate-odd**:

- Conjugate-even: $x(t) = x^*(-t)$, equivalently
  $x_R(t) + j x_I(t) = x_R(-t) - j x_I(-t)$ (p. 2).
- Conjugate-odd: $x(t) = -x^*(-t)$, equivalently
  $x_R(t) + j x_I(t) = -x_R(-t) + j x_I(-t)$ (p. 2).

### Worked example

For $x(t) = 2e^{j2\pi f_0 t} = 2\cos(2\pi f_0 t) + j\,2\sin(2\pi f_0 t)$
(p. 9, [Exercise 1](../examples/exercise-1-elementary-and-complex-signals.md)):

$$x_R(t) = 2\cos(2\pi f_0 t), \quad x_I(t) = 2\sin(2\pi f_0 t), \quad
x_e(t) = 2\cos(2\pi f_0 t), \quad x_o(t) = j\,2\sin(2\pi f_0 t)$$

Here the conjugate-even part of $x(t)$ equals $x(t) = x^*(-t)$, confirmed by
$\cos(-t) = \cos(t)$ with a sign flip applied to $-j\sin(t)$ (p. 9).

## Related pages

- [Signal transformations](signal-transformations.md)
- [Exercise 1 — Elementary and complex signals](../examples/exercise-1-elementary-and-complex-signals.md)
- [Lecture 1 summary](../summaries/signals-1.md)
