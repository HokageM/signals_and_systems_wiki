---
title: "Discrete-time Fourier transform"
type: concept
sources:
  - "../../raw/signals_4.pdf"
tags:
  - signals-and-systems
  - fourier-transform
  - discrete-time
---

# Discrete-time Fourier transform

Source: [Lecture 4, pp. 5–7](../../raw/signals_4.pdf). The discrete-time
Fourier transform (DTFT) represents a discrete-time sequence as a continuous,
periodic function of normalized angular frequency $\Omega$.

## Definition and inverse

For a sequence $x[k]$, the notes define

$$X(\Omega)=\sum_{k=-\infty}^{\infty}x[k]e^{-j\Omega k},
\qquad \Omega=2\pi fT_s,$$

and give the inverse formula

$$x[k]=\frac{1}{2\pi}\int_{-\pi}^{\pi}X(\Omega)e^{j\Omega k}\,d\Omega.$$

The DTFT is $2\pi$-periodic in $\Omega$ because $k$ is integer. Thus a
frequency interval of length $2\pi$ contains one complete period of the
spectrum (p. 5).

## Properties recorded in the notes

With the definition above, the notes list the following correspondences:

| Sequence | DTFT |
|---|---|
| $x[k-k_0]$ | $e^{-j\Omega k_0}X(\Omega)$ |
| $e^{j\Omega_0k}x[k]$ | $X(\Omega-\Omega_0)$ |
| $x[k]y[k]$ | $\dfrac{1}{2\pi}X(\Omega)*Y(\Omega)$, with periodic frequency convolution |
| $x[k]*y[k]$ | $X(\Omega)Y(\Omega)$ |
| $x^*[k]$ | $X^*(-\Omega)$ |
| $x^*[-k]$ | $X^*(\Omega)$ |

(pp. 5–6). The source also records the even- and odd-sequence symmetry
relations and the corresponding decomposition of real and imaginary parts
(p. 6).

## Example: causal geometric sequence

For $x[k]=a^k\varepsilon[k]$, with $|a|<1$, the DTFT follows from the
geometric series:

$$X(\Omega)=\sum_{k=0}^{\infty}a^ke^{-j\Omega k}
=\frac{1}{1-ae^{-j\Omega}}
=\frac{e^{j\Omega}}{e^{j\Omega}-a}.$$

This example and condition are given on p. 6.

## Related pages

- [Sampling and reconstruction](sampling.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Fourier transform](fourier-transform.md)
- [Lecture 4 summary](../summaries/signals-4.md)
