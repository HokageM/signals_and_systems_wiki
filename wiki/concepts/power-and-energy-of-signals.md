---
title: "Power and energy of signals"
type: concept
sources:
  - "../../raw/signals_1.pdf"
tags:
  - signals-and-systems
  - fundamentals
---

# Power and energy of signals

Source: [Lecture 1, p. 6](../../raw/signals_1.pdf).

## Instantaneous power

$$p_{x}(t) = |x(t)|^2 \qquad\qquad p_x[k] = |x[k]|^2$$

## Average power

$$P_x = \lim_{T\to\infty} \frac{1}{2T}\int_{-T}^{T} |x(t)|^2\,dt
\qquad\qquad
P_x = \lim_{n\to\infty} \frac{1}{2n+1}\sum_{k=-n}^{n} |x[k]|^2$$

## Power of a periodic signal (period `T` / `N`)

$$P_x = \frac{1}{T}\int_{t_0}^{t_0+T} |x(t)|^2\,dt
\qquad\qquad
P_x = \frac{1}{N}\sum_{k=k_0}^{k_0+N-1} |x[k]|^2$$

## Energy

$$E_x = \int_{-\infty}^{\infty} |x(t)|^2\,dt \qquad\qquad E_x = \sum_{k=-\infty}^{\infty} |x[k]|^2$$

## Classification

- $0 < P_x < \infty$: **power signal** — necessarily has infinite energy.
- $0 < E_x < \infty$: **energy signal** — necessarily has zero power.
- A signal can only be one of the two, or neither (p. 6).

This is confirmed by the worked examples: $x(t) = 0.5 + \sin(2\pi f_0 t)$ has
finite average power $P_x = 0.75$ and infinite energy (power signal);
$x(t) = e^{-a|t|}$ has finite energy $E_x = 1/a$ and zero power (energy
signal); the ramp $x(t) = \rho(t)$ has both infinite power and infinite
energy (neither). See
[Exercise — Power and energy classification](../examples/exercise-power-and-energy-classification.md).

## Related pages

- [Correlation and orthogonality](correlation-and-orthogonality.md)
- [Exercise — Power and energy classification](../examples/exercise-power-and-energy-classification.md)
- [Lecture 1 summary](../summaries/signals-1.md)
