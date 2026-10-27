---
title: "Exercise — Power and energy classification"
type: example
sources:
  - "../../raw/signals_1.pdf"
tags:
  - signals-and-systems
  - exercise
---

# Exercise — Power and energy classification

Source: [Lecture 1, pp. 10–12](../../raw/signals_1.pdf). Three signals are
classified using the definitions in
[Power and energy of signals](../concepts/power-and-energy-of-signals.md).

## a) $x(t) = 0.5 + \sin(2\pi f_0 t)$ — power signal

Using $\sin^2(at) = \tfrac12 - \tfrac12\cos(2at)$ and that sine/cosine
integrate to zero over a full period:

$$P_x = \frac{1}{T}\int_0^{T} \big[0.5+\sin(2\pi f_0 t)\big]^2 dt = 0.25 + \tfrac12 = 0.75$$

So $P_x = 0.75$ (finite, nonzero) $\Rightarrow$ power signal, with
$E_x \to \infty$ (p. 10–11).

## b) $x(t) = e^{-a|t|}$, $a>0$ — energy signal

$$E_x = \int_{-\infty}^{\infty} e^{-2a|t|}\,dt = 2\int_0^\infty e^{-2at}\,dt = \frac{1}{a}$$

So $E_x = 1/a$ (finite) $\Rightarrow$ energy signal, with $P_x = 0$ (p. 11).
Sample instantaneous powers given as a check: $P_{x}(t{=}0) = 1$,
$P_{x}(t{=}1) = e^{-2a}$.

## c) $x(t) = \rho(t)$ (ramp) — neither power nor energy signal

$$P_x = \lim_{T\to\infty} \frac{1}{2T}\int_0^T t^2\,dt = \lim_{T\to\infty} \frac{T^2}{6} \to \infty$$

$$E_x = \int_0^\infty t^2\,dt \to \infty$$

Both power and energy are infinite, so the ramp is **neither** a power nor an
energy signal (p. 12) — contrast with the classification rule in
[Power and energy of signals](../concepts/power-and-energy-of-signals.md).

## Related pages

- [Power and energy of signals](../concepts/power-and-energy-of-signals.md)
- [Lecture 1 summary](../summaries/signals-1.md)
