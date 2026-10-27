---
title: "Fourier transform"
type: concept
sources:
  - "../../raw/signals_2.pdf"
tags:
  - signals-and-systems
  - lecture-2
  - fourier-transform
---

# Fourier transform

Source: [Lecture 2, pp. 23–24, 27–28](../../raw/signals_2.pdf). Generalizes
the [Fourier series](fourier-series.md) to non-periodic, continuous-time
signals: as the period $T \to \infty$ of a periodic repetition of a signal,
the discrete spectrum lines merge into a continuous spectrum (p. 23).

## Definition (Fourier integral)

$$X(f) = \int_{-\infty}^{\infty} x(t)\,e^{-j2\pi f t}\,dt, \qquad
x(t) = \int_{-\infty}^{\infty} X(f)\,e^{j2\pi f t}\,df$$

written $x(t) \longleftrightarrow X(f)$ (p. 23).

## Convergence conditions

The Fourier integral exists if

$$\int_{-\infty}^{\infty} |x(t)|\,dt < \infty \;\Rightarrow\; \int_{-\infty}^{\infty} |x(t)|^2\,dt < \infty$$

i.e. for energy-limited signals (see
[Power and energy of signals](power-and-energy-of-signals.md)). This causes
problems for pure power signals, which are not absolutely integrable (p. 24).
To handle such signals, the Fourier transform with a convergence
(attenuation) factor $e^{-\alpha|t|}$ is used:

$$X_F(f) = \lim_{\alpha\to 0}\int_{-\infty}^{\infty} x(t)\,e^{-\alpha|t|}\,e^{-j2\pi f t}\,dt$$

(p. 24).

## Time–bandwidth product

The time–bandwidth product $T \cdot B$ of an arbitrarily chosen time interval
$T$ and frequency interval $B$ is unaffected by temporal scaling: if a
time-domain signal is expanded by a factor $a$, the Fourier spectrum is
compressed by the same factor ($x(at) \leftrightarrow \tfrac{1}{|a|}X(f/a)$, p. 27).

## Time-limited vs. band-limited signals

A signal is **band-limited** if its spectrum is zero above a cut-off
frequency $f_0$: $X(f) = 0$ for $|f| \ge f_0$. **A time-limited signal is
never band-limited, and a band-limited signal is never time-limited** (p. 27).

## Bandwidth

The **bandwidth** $B$ is the frequency range of the spectrum at positive
frequencies (p. 28).

## Related pages

- [Fourier series](fourier-series.md)
- [Fourier transform properties](fourier-transform-properties.md)
- [Fourier transform pairs](fourier-transform-pairs.md)
