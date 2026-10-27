---
title: "Exercise — Inverse Laplace transform and region of convergence"
type: example
sources:
  - "../../raw/signals_3.pdf"
tags:
  - signals-and-systems
  - exercise
  - laplace-transform
---

# Exercise — Inverse Laplace transform and region of convergence

Source: [Lecture 3, pp. 25–27](../../raw/signals_3.pdf). Builds on
[Laplace transform](../concepts/laplace-transform.md): the same rational
$X(s)$ can correspond to different time-domain signals depending on the ROC.

## Forward direction: combining two one-sided exponentials

**a)** $x(t) = e^{-2t}\varepsilon(t) + e^{-3t}\varepsilon(t)$:

$$X_{\mathcal L}(s) = \frac{1}{s+2}+\frac{1}{s+3}, \qquad \mathrm{Re}\{s\}>-2$$

(the ROC is the intersection of the two individual ROCs, p. 25).

**b)** $x(t) = -e^{-3t}\varepsilon(-t) + e^{2t}\varepsilon(-t)$:

$$X_{\mathcal L}(s) = \frac{1}{s+3}+\frac{1}{s-2}, \qquad -3<\mathrm{Re}\{s\}<2$$

(p. 25).

**c)** $x(t) = e^{2t}\varepsilon(t) + e^{-3t}\varepsilon(-t)$:

$$X_{\mathcal L}(s) = \frac{1}{s-2}+\frac{1}{s+3}$$

with ROC candidates $\mathrm{Re}\{s\}>2$ and $\mathrm{Re}\{s\}<-3$ having
**no overlap** — this combination has **no common convergence region**, so
(as with $e^{a|t|}$ in [Laplace transform](../concepts/laplace-transform.md))
the two-sided Laplace transform does **not exist** for this signal (p. 25).

## Reverse direction: partial fractions from a pole-zero plot

For $X_{\mathcal L}(s) = \dfrac{1}{s+2}+\dfrac{1}{s+3} = \dfrac{2(s+5/2)}{(s+2)(s+3)}$,
and similarly for $\dfrac{1}{s+3}+\dfrac{1}{s-2} = \dfrac{2(s+1/2)}{(s+3)(s-2)}$
and $\dfrac{1}{s-2}+\dfrac{1}{s+3}$ — the pole-zero plot alone does not
determine the ROC; the problem set sketches the different possible ROC
strips (left of leftmost pole, between poles, right of rightmost pole) for
the same pole-zero configuration (p. 26).

## Fully worked example

$$X(s) = \frac{2s+4}{s^2+4s+3} = \frac{2s+4}{(s+1)(s+3)} = \frac{A}{s+1}+\frac{B}{s+3}$$

Solving $2s+4 = A(s+3)+B(s+1)$:

- At $s=-1$: $2 = A\cdot 2 \Rightarrow A=1$.
- At $s=-3$: $-2 = B\cdot(-2) \Rightarrow B=1$.

$$X(s) = \frac{1}{s+1}+\frac{1}{s+3}$$

(p. 27). Three different inverse transforms depending on the chosen ROC:

- **d) $\mathrm{Re}\{s\}>-1$** (right of both poles, causal):
  $$x(t) = e^{-t}\varepsilon(t) + e^{-3t}\varepsilon(t)$$
- **e) $\mathrm{Re}\{s\}<-3$** (left of both poles, anti-causal):
  $$x(t) = -e^{-t}\varepsilon(-t) - e^{-3t}\varepsilon(-t)$$
- **f) $-3<\mathrm{Re}\{s\}<-1$** (between the poles, two-sided/mixed):
  $$x(t) = -e^{-t}\varepsilon(-t) + e^{-3t}\varepsilon(t)$$

(p. 27). This directly illustrates why the ROC must always accompany a
Laplace transform expression.

## Related pages

- [Laplace transform](../concepts/laplace-transform.md)
- [LTI systems in the s-domain](../concepts/lti-systems-s-domain.md)
