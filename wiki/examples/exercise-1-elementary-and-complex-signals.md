---
title: "Exercise 1 — Elementary and complex signals"
type: example
sources:
  - "../../raw/signals_1.pdf"
tags:
  - signals-and-systems
  - exercise
---

# Exercise 1 — Elementary and complex signals

Source: [Lecture 1, Exercise 1, pp. 7–9](../../raw/signals_1.pdf).

## a) Shifted and scaled rectangular pulse

Define and sketch $x(t) = 3\,\mathrm{rect}\!\left(\dfrac{t-t_0}{2T}\right)$,
$t_0 > 0$, $T > 0$:

$$x(t) = \begin{cases} 0, & |t-t_0| > T \\ 3/2, & |t-t_0| = T \\ 3, & |t-t_0| < T \end{cases}$$

The pulse is centered at $t_0$ with half-width $T$ (full width $2T$) and
height 3 (p. 7). See [Elementary signals](../concepts/elementary-signals.md)
for the base `rect` definition and [Signal transformations](../concepts/signal-transformations.md)
for the shift/scale rules applied here.

## b) Period of a sine via the rectangular function

For $\sin(2\pi f_0 t)$, the period is $T = \dfrac{2\pi}{2\pi f_0} = \dfrac{1}{f_0}$.
A single period can be isolated with a rectangular window:

$$x(t) = \mathrm{rect}(f_0 t)\,\sin(2\pi f_0 t)$$

(p. 7).

## c) Sketch of the si-function

$x(t) = si(2\pi f_0 t) = \dfrac{\sin(2\pi f_0 t)}{2\pi f_0 t}$. Zero crossings
at $t = \dfrac{n}{2f_0}$, $n \neq 0$ integer (the first zero, from
$\sin(\pi) = 0 \Rightarrow 2\pi f_0 t = \pi \Rightarrow t = \tfrac{1}{2f_0}$)
(p. 8). See [Elementary signals](../concepts/elementary-signals.md) for the
si-function plot.

## d) Real/imaginary/even/odd parts of a complex exponential

For $x(t) = 2e^{j2\pi f_0 t} = 2\big(\cos(2\pi f_0 t) + j\sin(2\pi f_0 t)\big)$ (p. 9):

$$x_R(t) = \tfrac{1}{2}\big[x(t)+x^*(t)\big] = 2\cos(2\pi f_0 t)$$

$$x_I(t) = \tfrac{1}{2j}\big[x(t)-x^*(t)\big] = 2\sin(2\pi f_0 t)$$

$$x_e(t) = \tfrac{1}{2}\big[x(t)+x(-t)\big] = 2\cos(2\pi f_0 t)$$

$$x_o(t) = \tfrac{1}{2}\big[x(t)-x(-t)\big] = j\,2\sin(2\pi f_0 t)$$

The source also states the definition of conjugate-even signals,
$x(t) = x^*(-t)$ (p. 9), continued into the lecture material on
[conjugate-even/odd signals](../concepts/even-odd-decomposition.md).

## Related pages

- [Lecture 1 summary](../summaries/signals-1.md)
- [Elementary signals](../concepts/elementary-signals.md)
- [Signal transformations](../concepts/signal-transformations.md)
- [Even/odd decomposition](../concepts/even-odd-decomposition.md)
