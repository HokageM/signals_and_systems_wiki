---
title: "Digital filters"
type: concept
sources:
  - "../../raw/signals_5.pdf"
tags:
  - signals-and-systems
  - digital-filters
  - z-transform
---

# Digital filters

Source: [Lecture 5, pp. 1–10](../../raw/signals_5.pdf). A digital filter maps
a discrete-time input $x[k]$ to an output $y[k]$. The notes distinguish
non-recursive finite impulse response (FIR) filters from recursive infinite
impulse response (IIR) filters and use the Z-transform to describe their
transfer functions.

## FIR filters

A non-recursive filter has the form

$$y[k]=\sum_{m=0}^{M}f_mx[k-m],\qquad
H(z)=\sum_{m=0}^{M}f_mz^{-m}.$$

Its impulse response is finite: $h[k]=f_k$ for $0\le k\le M$, and zero
otherwise. With finite coefficients it is BIBO stable; the form above is
causal because it uses only the current and earlier input values (pp. 1–2, 5).

The notes identify two FIR zero patterns associated with linear phase: zeros
on the unit circle, or zeros in pairs symmetric with respect to the unit
circle (p. 7). For example, the comb filter

$$h[k]=\delta[k]+\delta[k-k_0],\qquad
H(z)=1+z^{-k_0}$$

has equally spaced zeros on the unit circle (p. 7).

## IIR filters

A recursive filter uses previous output values as well as input values:

$$y[k]=\sum_{m=0}^{M}f_mx[k-m]
-\sum_{\nu=1}^{N}b_\nu y[k-\nu],$$

so, with $b_0=1$,

$$H(z)=\frac{Y(z)}{X(z)}
=\frac{\sum_{m=0}^{M}f_mz^{-m}}
{1+\sum_{\nu=1}^{N}b_\nu z^{-\nu}}.$$

This form has feedback and can have an infinite impulse response (pp. 1,
3). A causal rational filter is BIBO stable when its ROC includes the unit
circle; equivalently, its poles lie strictly inside the unit circle (pp. 5,
10). See [Z-transform](z-transform.md) for the ROC condition.

## Pole-zero description and response

The transfer function's zeros and poles characterize the filter; for a
real-coefficient system they occur as real values or complex-conjugate pairs
(pp. 3–4). The frequency response is obtained by evaluating on the unit
circle, $z=e^{j\Omega}$:

$$H(e^{j\Omega})=H(z)\big|_{z=e^{j\Omega}}.$$

The magnitude and phase responses are $|H(e^{j\Omega})|$ and
$\arg H(e^{j\Omega})$ (p. 4).

## Related pages

- [Z-transform](z-transform.md)
- [LTI systems](lti-systems.md)
- [LTI system frequency response and filter types](lti-frequency-response.md)
- [Exercise — Digital filters](../examples/exercise-digital-filters.md)
- [Lecture 5 summary](../summaries/signals-5.md)
