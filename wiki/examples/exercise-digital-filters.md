---
title: "Exercise — Digital filters"
type: example
sources:
  - "../../raw/signals_5.pdf"
tags:
  - signals-and-systems
  - exercise
  - digital-filters
  - z-transform
---

# Exercise — Digital filters

Source: [Lecture 5, pp. 8–17](../../raw/signals_5.pdf). The notes analyze an
FIR filter, a recursive filter, and a digital shelving filter.

## FIR example

For

$$H(z)=1+z^{-1}+0.5z^{-2},$$

the output is

$$y[k]=x[k]+x[k-1]+0.5x[k-2].$$

The impulse response is finite, so the filter is non-recursive and BIBO
stable (pp. 8, 5). Multiplying the transfer function by $z^2$ gives the
zero polynomial $z^2+z+0.5$, whose roots are

$$z_{0,1}=-\frac12+j\frac12,\qquad
z_{0,2}=-\frac12-j\frac12.$$

Both zeros have magnitude $1/\sqrt{2}<1$, so the notes classify this as a
minimum-phase filter (p. 9).

## Recursive-filter example

The notes give the difference equation

$$y[k]=2x[k-1]-1.2x[k-2]+y[k-1]-0.5y[k-2].$$

Rearranging the output terms and taking the Z-transform yields

$$H(z)=\frac{2z^{-1}-1.2z^{-2}}
{1-z^{-1}+0.5z^{-2}}
=\frac{2z-1.2}{z^2-z+0.5}.$$

The zero is $z_0=0.6$. The poles are

$$z_{\infty,1}=\frac12+j\frac12,\qquad
z_{\infty,2}=\frac12-j\frac12,$$

each with magnitude $1/\sqrt{2}<1$. The filter is causal and stable by the
pole-location criterion used in the notes (pp. 9–10).

## Digital shelving filter

The analog prototype in the notes is

$$H(s)=\frac{s+G_0\,2\pi f_c}{s+2\pi f_c},$$

with a zero at $s=-G_0\,2\pi f_c$ and pole at $s=-2\pi f_c$ (p. 11). Its
magnitude-squared response is

$$|H(f)|^2=\frac{G_0^2f_c^2+f^2}{f_c^2+f^2}.$$

Thus the low-frequency magnitude is $G_0$ and the high-frequency magnitude
tends to $1$; the notes describe $G_0<1$ as low-frequency attenuation and
$G_0>1$ as low-frequency boost (pp. 11–12).

For the digital version, the notes define

$$A(z)=\frac{z^{-1}+a_c}{1+a_cz^{-1}},\qquad |a_c|<1,$$

and combine it with the direct path to form

$$H_d(z)=\frac12\left[(G_0-1)A(z)+(G_0+1)\right].$$

For $G_0=2$ and $a_c=-1/2$, this simplifies to

$$H_d(z)=\frac{\frac52-\frac12z^{-1}}{2-z^{-1}}.$$

The source derives the all-pass form and its pole-zero relationship on pp.
12–17; the final expression above is transcribed from p. 17.

## Related pages

- [Digital filters](../concepts/digital-filters.md)
- [Z-transform](../concepts/z-transform.md)
- [LTI systems in the s-domain](../concepts/lti-systems-s-domain.md)
