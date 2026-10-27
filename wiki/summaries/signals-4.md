---
title: "Lecture 4 summary — Signals and Systems"
type: summary
sources:
  - "../../raw/signals_4.pdf"
tags:
  - signals-and-systems
  - lecture-4
---

# Lecture 4 summary — Signals and Systems

Source: [`raw/signals_4.pdf`](../../raw/signals_4.pdf) (30 pages).
Handwritten notes covering sampling and discrete-time Fourier methods,
followed by the Z-transform and an application to multicarrier transmission.

## Lecture content

1. **Sampling and reconstruction** — impulse-train sampling, spectral
   replicas, the band-limited reconstruction condition $f_s\ge2B$, and ideal
   low-pass reconstruction. See
   [Sampling and reconstruction](../concepts/sampling.md) (pp. 1–4).
2. **Discrete-time Fourier transform (DTFT)** — definition, inverse,
   periodicity, properties, and the causal geometric-sequence example. See
   [Discrete-time Fourier transform](../concepts/discrete-time-fourier-transform.md)
   (pp. 5–7).
3. **Discrete Fourier transform (DFT)** — finite-block transform pair,
   periodic extension, cyclic shift and convolution, zero-padding, and
   frequency interpolation. See
   [Discrete Fourier transform](../concepts/discrete-fourier-transform.md)
   (pp. 8–18).
4. **Z-transform** — bilateral definition, ROC, relation to the Laplace
   transform and DTFT, properties, and BIBO stability condition. See
   [Z-transform](../concepts/z-transform.md) (pp. 24–30).
5. **Fast Fourier transform** — introductory even/odd sequence split for
   reducing an $N$-point DFT to smaller transforms (p. 24).

## Worked material

- **DFT of a cosine sequence** (pp. 17–18): six-point DFT of
  $x[k]=\cos(2\pi k/6)$, with nonzero bins at $n=1$ and $n=5$. See
  [Exercise — DFT of a cosine sequence](../examples/exercise-dft-cosine-sequence.md).
- **Multicarrier transmission, sampled signal** (pp. 19–23): sampling two
  cosine carriers at $f_s=8f_1$, mapping the carriers to DFT frequency bins,
  and checking the proposed inverse-DFT transmission. This continues
  [Exercise — Multicarrier transmission](../examples/exercise-multicarrier-transmission.md).
- **Z-transform examples** (pp. 25–30): causal and anti-causal exponential
  sequences and the effect of different ROCs for a rational function.

## Notation and conventions observed

- The sample interval and rate are $T_s$ and $f_s=1/T_s$.
- DTFT angular frequency is $\Omega=2\pi fT_s$ in radians per sample.
- DFT convention: negative exponential in the forward transform and a
  positive exponential with $1/N$ factor in the inverse.
- The bilateral Z-transform is $X(z)=\sum_k x[k]z^{-k}$; the ROC is part of
  its specification.

## Open questions / unclear source details

- On p. 22, the multicarrier inverse-DFT derivation appears to retain a factor
  $1/8$ on the carrier amplitudes, while the inverse-DFT definition on p. 8
  requires the DFT-bin values to include the corresponding factor of $8$ for
  those amplitudes to be recovered. The page then states that the proposed
  method is correct. The sampled frequencies are unambiguous, but the scaling
  in this intermediate derivation is not; it is called out in the linked
  exercise page.
- The rational Z-transform exercise on pp. 27–28 contains dense handwritten
  partial fractions and ROC-dependent inverses. The wiki records the general
  ROC principle rather than transcribing that calculation as verified.
