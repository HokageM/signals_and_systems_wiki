---
title: "Exercise — DFT of a cosine sequence"
type: example
sources:
  - "../../raw/signals_4.pdf"
tags:
  - signals-and-systems
  - exercise
  - discrete-fourier-transform
---

# Exercise — DFT of a cosine sequence

Source: [Lecture 4, pp. 17–18](../../raw/signals_4.pdf). The task is to find
the six-point DFT of

$$x[k]=\cos\left(\frac{2\pi k}{6}\right),\qquad k=0,\ldots,5.$$

Use the convention

$$X[n]=\sum_{k=0}^{5}x[k]e^{-j2\pi nk/6}.$$

## Solution

Expand the cosine into two complex exponentials:

$$x[k]=\frac12e^{j2\pi k/6}+\frac12e^{-j2\pi k/6}.$$

Then

$$X[n]=\frac12\sum_{k=0}^{5}e^{-j2\pi(n-1)k/6}
+\frac12\sum_{k=0}^{5}e^{-j2\pi(n+1)k/6}.$$

Each finite exponential sum is $6$ when its frequency index is a multiple
of $6$, and $0$ otherwise. Thus

$$X[n]=
\begin{cases}
3, & n=1 \text{ or } n=5,\\
0, & n\in\{0,2,3,4\}.
\end{cases}$$

With the periodic DFT extension, the nonzero bins repeat at
$n=6\ell\pm1$, $\ell\in\mathbb Z$, as shown in the notes (p. 18).

## Related pages

- [Discrete Fourier transform](../concepts/discrete-fourier-transform.md)
- [Discrete-time Fourier transform](../concepts/discrete-time-fourier-transform.md)
