# Signals and Systems Wiki — Index

This is the content catalog for the wiki. It is organized by page type. Update
this file whenever a wiki page is created, renamed, or removed. See `CLAUDE.md`
for conventions.

## Summaries

- [Lecture 1 summary](summaries/signals-1.md) — Signal classification, transformations, elementary signals, Dirac impulse, power/energy, correlation (source: `signals_1.pdf`).
- [Lecture 2 summary](summaries/signals-2.md) — LTI systems, convolution, Fourier series, Fourier transform (source: `signals_2.pdf`).
- [Lecture 3 summary](summaries/signals-3.md) — LTI frequency response/filters, phase/group delay, Laplace transform, s-domain analysis (source: `signals_3.pdf`).
- [Lecture 4 summary](summaries/signals-4.md) — Sampling, DTFT, DFT, multicarrier sampling, and Z-transform (source: `signals_4.pdf`).
- [Lecture 5 summary](summaries/signals-5.md) — FIR and IIR filters, stability, pole-zero analysis, and shelving filters (source: `signals_5.pdf`).
- [Formula sheet summary](summaries/signals-formulas.md) — Condensed cross-reference formula sheet covering the whole module (source: `signals_formulas.pdf`).

## Concepts

- [Signal classification](concepts/signal-classification.md) — Analog, discrete-time, quantized, digital signal classes.
- [Signal transformations](concepts/signal-transformations.md) — Time shift, reflection, scaling, causal/anti-causal signals.
- [Even/odd decomposition](concepts/even-odd-decomposition.md) — Even/odd parts, real/imaginary parts, conjugate-even/odd complex signals.
- [Elementary signals](concepts/elementary-signals.md) — Step, ramp, signum, rect, triangle, real exponential, si-function.
- [Dirac impulse](concepts/dirac-impulse.md) — Definition, sifting property, scaling property, Dirac comb.
- [Power and energy of signals](concepts/power-and-energy-of-signals.md) — Instantaneous/average power, periodic power, energy, power-vs-energy classification.
- [Correlation and orthogonality](concepts/correlation-and-orthogonality.md) — Inner product, orthogonality, cross-/autocorrelation (energy and power), correlation properties.
- [LTI systems](concepts/lti-systems.md) — Linearity, time invariance, impulse response, causality, BIBO stability, memoryless/dynamic systems.
- [Convolution](concepts/convolution.md) — Definition, properties, cyclic convolution, convolution with a Dirac comb, correlation-as-convolution.
- [Fourier series](concepts/fourier-series.md) — Transform taxonomy, real/complex Fourier series, conjugate-even coefficients, relation to the Fourier transform of one period.
- [Fourier transform](concepts/fourier-transform.md) — Definition, convergence conditions, convergence factor, time–bandwidth product, time/band-limited signals.
- [Fourier transform properties](concepts/fourier-transform-properties.md) — Linearity, duality, shift/modulation/scaling, differentiation/integration, Parseval's relation, symmetry.
- [Fourier transform pairs](concepts/fourier-transform-pairs.md) — Reference table of standard transform pairs.
- [LTI system frequency response and filter types](concepts/lti-frequency-response.md) — Magnitude/phase response, transmission factor, attenuation/gain, filter types.
- [Phase and group delay](concepts/phase-and-group-delay.md) — Phase delay, group delay, linear phase, distortion-free systems.
- [Laplace transform](concepts/laplace-transform.md) — Definition, ROC, relation to the Fourier transform, standard pairs, properties.
- [LTI systems in the s-domain](concepts/lti-systems-s-domain.md) — Transfer function, pole-zero plots, allpass/minimum-phase filters, BIBO stability via pole location.
- [Sampling and reconstruction](concepts/sampling.md) — Impulse-train sampling, spectral replicas, band-limited reconstruction condition.
- [Discrete-time Fourier transform](concepts/discrete-time-fourier-transform.md) — DTFT definition, inverse, periodicity, properties, and geometric-sequence example.
- [Discrete Fourier transform](concepts/discrete-fourier-transform.md) — Finite-block transform, cyclic properties, zero-padding, and FFT introduction.
- [Z-transform](concepts/z-transform.md) — Bilateral transform, ROC, causal/anti-causal sequences, and stability condition.
- [Digital filters](concepts/digital-filters.md) — FIR and IIR structures, transfer functions, pole-zero response, and stability.

## Examples

- [Exercise 1 — Elementary and complex signals](examples/exercise-1-elementary-and-complex-signals.md) — Shifted/scaled rect, sine period via rect, si-function sketch, parts of a complex exponential.
- [Exercise — Power and energy classification](examples/exercise-power-and-energy-classification.md) — Classifying a DC+sine, an exponential, and a ramp signal.
- [Exercise 2 — Orthogonality and correlation](examples/exercise-2-orthogonality-and-correlation.md) — Orthogonality of complex exponentials, discrete auto-/cross-correlation, continuous energy-signal correlation.
- [Exercise — Convolution of LTI systems](examples/exercise-convolution-of-lti-systems.md) — Exponential through an integrator; raised-cosine impulse response with a rectangular input.
- [Exercise — Cyclic convolution and correlation](examples/exercise-cyclic-convolution-and-correlation.md) — Cyclic convolution/correlation of cosine and sine.
- [Exercise — Pedestrian recognition](examples/exercise-pedestrian-recognition.md) — Matched-filter application distinguishing pedestrian vs. car radar reflections.
- [Exercise — Fourier series symmetry and equivalence](examples/exercise-fourier-series-symmetry-and-equivalence.md) — Conjugate-even Fourier coefficients; real/complex Fourier series equivalence.
- [Exercise — Fourier transform of rect, triangle, and periodic signals](examples/exercise-fourier-transform-rect-triangle-and-periodic-signals.md) — Duality derivations, triangular pulse transform, periodic pulse train spectrum.
- [Exercise — Group and phase delay of an allpass filter](examples/exercise-group-and-phase-delay-allpass-filter.md) — Magnitude/phase response, phase delay, group delay of an allpass filter.
- [Exercise — Multicarrier transmission](examples/exercise-multicarrier-transmission.md) — Transmitting two cosine carriers, orthogonality checks, triangular bandpass filter design.
- [Exercise — Fourier vs. Laplace transform](examples/exercise-fourier-vs-laplace-transform.md) — Side-by-side comparison of Fourier and Laplace transforms for six standard signals.
- [Exercise — Inverse Laplace transform and region of convergence](examples/exercise-inverse-laplace-transform-and-roc.md) — Partial fractions and ROC-dependent inverse transforms of the same X(s).
- [Exercise — Analog filter design](examples/exercise-analog-filter-design.md) — Pole-zero plot, stability, magnitude response, and impulse response of a second-order analog filter.
- [Exercise — DFT of a cosine sequence](examples/exercise-dft-cosine-sequence.md) — Six-point DFT of a cosine sequence with nonzero bins at 1 and 5.
- [Exercise — Digital filters](examples/exercise-digital-filters.md) — FIR and recursive-filter pole-zero analysis, plus analog/digital shelving-filter derivation.
