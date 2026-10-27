---
title: "Formula sheet summary — Signals and Systems"
type: summary
sources:
  - "../../raw/signals_formulas.pdf"
tags:
  - signals-and-systems
  - reference
---

# Formula sheet summary — Signals and Systems

Source: [`raw/signals_formulas.pdf`](../../raw/signals_formulas.pdf) (4 pages).
A condensed, handwritten reference sheet collecting formulas from across the
whole module (Lectures 1–5). It introduces no new concepts; it is a
cross-check and quick-reference companion to the concept pages below.

## Cross-check against existing concept pages

Reviewed each section against the already-ingested lecture material; all
formulas are **consistent** with the corresponding concept pages (same
notation and conventions throughout):

| Formula sheet section | Page | Corresponding concept page(s) |
|---|---|---|
| Fourier transform pairs table | p. 1 | [Fourier transform pairs](../concepts/fourier-transform-pairs.md) |
| Magnitude/phase response, phase delay, group delay | p. 1 | [LTI system frequency response and filter types](../concepts/lti-frequency-response.md), [Phase and group delay](../concepts/phase-and-group-delay.md) |
| Fourier series, Fourier transform of periodic signals | p. 1 | [Fourier series](../concepts/fourier-series.md) |
| Standard trig identities ($\cos^2$, $\sin^2$, product-to-sum) | p. 1 | used throughout the [Lecture 1](signals-1.md)/[Lecture 2](signals-2.md) worked exercises |
| Laplace transform definition, properties, standard pairs | p. 2 | [Laplace transform](../concepts/laplace-transform.md) |
| Allpass / minimum-phase / maximum-phase filter conditions; stable/quasi-stable/unstable pole conditions | p. 2 | [LTI systems in the s-domain](../concepts/lti-systems-s-domain.md) |
| Sampling without aliasing ($f_s \ge 2B$), sampled-signal formula | p. 2 | [Sampling and reconstruction](../concepts/sampling.md) |
| DTFT and DFT definitions, periodic extension, even/odd DFT symmetry | p. 3 | [Discrete-time Fourier transform](../concepts/discrete-time-fourier-transform.md), [Discrete Fourier transform](../concepts/discrete-fourier-transform.md) |
| Z-transform definition, standard pairs, properties, ROC/causality/stability rules | p. 3 | [Z-transform](../concepts/z-transform.md) |
| General rational transfer function $H(z)=Y(z)/X(z)$; FIR/IIR filter diagrams | p. 3 | [Digital filters](../concepts/digital-filters.md) |
| Instantaneous/average/periodic power, energy | p. 4 | [Power and energy of signals](../concepts/power-and-energy-of-signals.md) |
| Cross-/autocorrelation (energy and power signals), correlation via convolution | p. 4 | [Correlation and orthogonality](../concepts/correlation-and-orthogonality.md), [Convolution](../concepts/convolution.md) |
| Convolution definition and properties | p. 4 | [Convolution](../concepts/convolution.md) |
| Causal/BIBO/memoryless system conditions; even/odd and conjugate-even/odd decomposition | p. 4 | [LTI systems](../concepts/lti-systems.md), [Even/odd decomposition](../concepts/even-odd-decomposition.md) |

## Notable confirmations

- The allpass/minimum-phase/maximum-phase filter definitions and the
  stable/quasi-stable/unstable pole classifications on p. 2 exactly match
  [LTI systems in the s-domain](../concepts/lti-systems-s-domain.md),
  confirming those pages are transcribed correctly.
- The sampling condition $f_s > 2B$ (p. 2) matches
  [Sampling and reconstruction](../concepts/sampling.md).
- The Z-transform standard pairs and properties on p. 3 match
  [Z-transform](../concepts/z-transform.md), including the causal/anti-causal
  ROC distinction.

## Open questions / unclear source details

- No new or conflicting material was found; this source did not require any
  changes to existing concept pages.
