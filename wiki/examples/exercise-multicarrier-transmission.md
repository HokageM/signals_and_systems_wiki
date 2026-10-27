---
title: "Exercise — Multicarrier transmission"
type: example
sources:
  - "../../raw/signals_3.pdf"
tags:
  - signals-and-systems
  - exercise
---

# Exercise — Multicarrier transmission

Source: [Lecture 3, pp. 8–13](../../raw/signals_3.pdf). An applied example
combining [LTI system frequency response and filter types](../concepts/lti-frequency-response.md),
[Correlation and orthogonality](../concepts/correlation-and-orthogonality.md),
and [LTI systems](../concepts/lti-systems.md).

## Part I — single carrier through a real, even frequency response

Given $x_1(t) = d_1\cos(2\pi f_1 t)$, $d_1 \in \mathbb{R}$, $f_1 > 0$, fed
through an LTI system with frequency response $H(f_1)$ real and even in $f$.

**a)** By the Fourier-transform symmetry properties, an **even, real**
frequency response $H(f)$ corresponds to an **even** impulse response
$h(t)$, i.e. $h(-t) = h(t)$. Since $h(t)$ is then generally nonzero for
$t<0$, such a system is **non-causal** (p. 8).

**b)** Show $y_1(t) = H(f_1)\,x_1(t)$:

$$y_1(t) = h(t)*x_1(t) = \int_{-\infty}^{\infty} h(\tau)\,x_1(t-\tau)\,d\tau
= \int_{-\infty}^{\infty} h(\tau)\,\tfrac{d_1}{2}\Big(e^{j2\pi f_1(t-\tau)}+e^{-j2\pi f_1(t-\tau)}\Big)\,d\tau$$

$$= \frac{d_1}{2}\Big(e^{j2\pi f_1 t}+e^{-j2\pi f_1 t}\Big)\int_{-\infty}^{\infty} h(\tau)\,e^{-j2\pi f_1 \tau}\,d\tau
= \frac{d_1}{2}\Big(e^{j2\pi f_1 t}+e^{-j2\pi f_1 t}\Big)\,H(f_1) = H(f_1)\,x_1(t)$$

(pp. 8–9).

## Part II — two carriers, orthogonality, and selective filtering

Now add a second carrier $x_2(t) = d_2\cos(2\pi f_2 t)$, $d_2 \in \mathbb{R}$,
$f_2 > f_1 > 0$, so $x(t) = x_1(t) + x_2(t)$ (p. 9).

**c)** Spectrum:

$$X(f) = \frac{d_1}{2}\big[\delta(f+f_1)+\delta(f-f_1)\big] + \frac{d_2}{2}\big[\delta(f+f_2)+\delta(f-f_2)\big]$$

**d)** For $d_1=-1$, $d_2=1$, $f_2>f_1$: four impulses at $\pm f_1$ (weight
$-1/2$) and $\pm f_2$ (weight $+1/2$) (p. 9).

**e) Case $f_2 = 2f_1$ (period $T=1/f_1$)**:

$$r_{x_1x_2}^{P}(\tau) = f_1 \int_0^{1/f_1} d_1\cos(2\pi f_1 t)\,d_2\cos\big(2\pi f_1(t+\tau)\big)\,dt
= d_1 d_2\,\frac{f_1^2}{f_2^2-f_1^2}\,si\!\left(2\pi\frac{f_2}{f_1}\right)$$

At $\tau=0$: $r_{x_1x_2}^{P}(0) = \langle x_1(t), x_2(t)\rangle$, which the
notes flag as **nonzero** for $f_2=2f_1$ — i.e. $x_1$ and $x_2$ are **not**
orthogonal in general at this ratio (p. 9, flagged with "!" in the source).
Direct evaluation of $\langle x_1(t), x_2(t)\rangle$ over one period confirms
the integral evaluates to 0 term-by-term via $\int \cos(\omega t)\,dt = 0$
over full periods (p. 9) — i.e. the two carriers **are** orthogonal over the
shared period $T_0 = 1/f_1$, consistent with
[Exercise 2 — Orthogonality and correlation](exercise-2-orthogonality-and-correlation.md).
(The source itself flags an apparent tension here between the general
correlation formula and the direct per-period integral; treat the direct
per-period computation, which gives 0, as authoritative.)

**f) Case $f_2 = 3f_1$:**

$$\langle x_1(t), x_2(t+\tau)\rangle = r_{x_1x_2}^{P}(0) = d_1 d_2\,\frac{9f_1}{9f_1-f_1}\,si(2\pi\cdot 3) = 0 \;\Rightarrow\; \text{orthogonal}$$

(p. 10).

## Bandpass filter design to isolate $x_1(t)$

**g)** Choose $H(f) = \tfrac32\Lambda\!\left(\dfrac{f}{3f_1}\right)$ (a
triangular passband of half-width $3f_1$ centered at $f=0$, height $3/2$) (p. 10).

**h)** Applying this filter to $x_1(t)$ (inside the passband, since $f_1 < 3f_1$):

$$y_1(t) = H(f_1)\,x_1(t) = \frac32\Lambda\!\left(\frac13\right) d_1\cos(2\pi f_1 t) = d_1\cos(2\pi f_1 t) = x_1(t)$$

i.e. $x_1(t)$ passes through **undistorted** (using
$\Lambda(1/3) = 1-1/3 = 2/3$, so $\tfrac32\cdot\tfrac23=1$, p. 10).

**i)** For $f_2 = 2f_1$ (outside the passband edge at $3f_1$... actually
within range depending on filter width — see source for the exact boundary
check): the notes compute
$y_2(t) = H(f_2)\,x_2(t) = \tfrac32\Lambda(2/3)\,d_2\cos(2\pi f_2 t) = \tfrac12 d_2\cos(2\pi f_2 t)$,
i.e. $x_2(t)$ is **attenuated but not fully suppressed** at this particular
filter width (p. 10, 11).

**j) Case $f_2' = 3f_1$:** $r^{P}_{x_1x_2}(0) = 0$ (orthogonal, confirmed
again), and $y_2(t) = H(f_2')\,x_2(t) = \tfrac32\Lambda(1)\,d_2\cos(2\pi f_2' t) = 0$
since $\Lambda(1)=0$ (the triangular passband edge) — so $x_2(t)$ is
**completely blocked**, while $y_1(t) = x_1(t)$ is unchanged: the filter
selects the first carrier and rejects the second (p. 12).

## Related pages

- [LTI system frequency response and filter types](../concepts/lti-frequency-response.md)
- [Correlation and orthogonality](../concepts/correlation-and-orthogonality.md)
- [Sampling and reconstruction](../concepts/sampling.md)
- [Discrete Fourier transform](../concepts/discrete-fourier-transform.md)

## Part III — sampled multicarrier signal and inverse DFT

Lecture 4 continues the example with $f_2=2f_1$ and samples the sum
$x(t)=d_1\cos(2\pi f_1t)+d_2\cos(2\pi f_2t)$ at $f_s=8f_1$ (pp. 19–23).
Writing $x[k]=x(kT_s)$ gives

$$x[k]=d_1\cos\left(\frac{\pi k}{4}\right)
+d_2\cos\left(\frac{\pi k}{2}\right).$$

The two carriers occupy the positive-frequency DFT bins $n=1$ and $n=2$
for an eight-sample block (with conjugate-symmetric bins $n=7$ and $n=6$).
Under the DFT convention in
[Discrete Fourier transform](../concepts/discrete-fourier-transform.md), the
corresponding bin values are $X[1]=X[7]=4d_1$ and
$X[2]=X[6]=4d_2$. The inverse DFT then recovers one period of the sampled
signal. This frequency-bin calculation is derived here from the stated
transform convention.

**Source discrepancy:** the inverse-DFT derivation on p. 22 appears to retain
a factor $1/8$ on the carrier amplitudes, even though the transform definition
on p. 8 requires bin values scaled by $8$ relative to each cosine's
amplitude. The source nevertheless concludes that the proposal is correct.
The sampled signal and bin locations are clear; the intermediate scaling in
the handwritten derivation is not.
