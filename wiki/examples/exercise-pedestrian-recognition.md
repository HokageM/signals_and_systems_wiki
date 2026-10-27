---
title: "Exercise — Pedestrian recognition (matched filter application)"
type: example
sources:
  - "../../raw/signals_2.pdf"
tags:
  - signals-and-systems
  - exercise
  - correlation
---

# Exercise — Pedestrian recognition (matched filter application)

Source: [Lecture 2, pp. 12–18](../../raw/signals_2.pdf). An applied example
combining [Convolution](../concepts/convolution.md),
[Correlation and orthogonality](../concepts/correlation-and-orthogonality.md),
and [LTI systems](../concepts/lti-systems.md): a car's sensor must
distinguish a pedestrian reflection from a car reflection in a radar/sonar
return signal (p. 12).

## Setup

The sensor emits $x(t) = \dfrac{1}{\sqrt{T}}\,\mathrm{rect}\!\left(\dfrac{t}{T}\right)$,
$T>0$. Two candidate reflecting objects are modeled as LTI systems with
distinct impulse responses (p. 12):

- **Pedestrian**: a single reflection, $h_F(t) = \delta(t-t_0)$.
- **Car**: three reflections (e.g. front, body, rear), with
  $h_A(t) = \dfrac{1}{\sqrt{3}}\Big[\delta(t-t_0+T) + \delta(t-t_0) + \delta(t-t_0-T)\Big]$,
  and $t_0 \gg T$ (p. 12).

## a)–b) Received signal for a pedestrian

$$y_F(t) = h_F(t) * x(t) = \delta(t-t_0) * x(t) = x(t-t_0) = \frac{1}{\sqrt{T}}\,\mathrm{rect}\!\left(\frac{t-t_0}{T}\right)$$

a single rectangular pulse of width $T$ centered at $t_0$ (p. 13).

## c)–d) Received signal for a car

$$y_A(t) = h_A(t)*x(t) = \frac{1}{\sqrt{3T}}\left[\mathrm{rect}\!\left(\frac{t-t_0+T}{T}\right) + \mathrm{rect}\!\left(\frac{t-t_0}{T}\right) + \mathrm{rect}\!\left(\frac{t-t_0-T}{T}\right)\right]$$

three adjacent rectangular pulses of width $T$, spanning
$[t_0 - 3T/2,\; t_0 + 3T/2]$ (p. 13–14).

## e)–g) Cross-correlation of the two received signals

$$r_{y_A y_F}(\tau) = \int_{-\infty}^{\infty} y_A^*(t)\,y_F(t+\tau)\,dt$$

Working through the piecewise overlap of the pulse trains (p. 14–16):

$$r_{y_A y_F}(\tau) = \begin{cases}
0, & |\tau| > 2T \\
\dfrac{\tau+2T}{\sqrt{3}\,T}, & -2T \le \tau < -T \\
\dfrac{1}{\sqrt{3}}, & -T \le \tau \le T \\
\dfrac{2T-\tau}{\sqrt{3}\,T}, & T < \tau \le 2T
\end{cases}$$

## h) Autocorrelations at zero lag

$$r_{y_F y_F}(\tau) = \Lambda\!\left(\frac{\tau}{T}\right), \qquad
r_{y_A y_A}(\tau) = \Lambda\!\left(\frac{\tau}{3T}\right)$$

(see [Elementary signals](../concepts/elementary-signals.md) for $\Lambda$),
with $r_{y_F y_F}(0) = 1 = E_{y_F}$ and $r_{y_A y_A}(0) = 1 = E_{y_A}$: both
received signals have the same energy (normalized by construction) (p. 17).

## i) Matched filter / classification scheme

Define matched filters $g_F(t) = y_F^*(t_0-t)$, $g_A(t) = y_A^*(t_0-t)$ and
correlator outputs $z_F(t) = r_{y_F y_F}(t-t_0)$, $z_A(t) = r_{y_A y_F}(t-t_0)$
(p. 17).

**Proof that $z_A(t) = r_{y_A y_F}(t-t_0)$:** by substitution $\tau = t'$ in the
defining correlation integral, shown directly in the notes (p. 18).

**Decision at $t = t_0$:**

$$z_F(t_0) = r_{y_F y_F}(0) = 1, \qquad z_A(t_0) = r_{y_A y_F}(0) = \frac{1}{\sqrt{3}}$$

Since $z_F(t_0) = 1 > z_A(t_0) = 1/\sqrt{3}$, the correlator matched to the
**pedestrian** filter produces the larger output when the true input is a
pedestrian reflection — demonstrating how **matched filtering**
(correlating a received signal against known reference signatures) can
discriminate between object classes (p. 18).

## Related pages

- [Convolution](../concepts/convolution.md)
- [Correlation and orthogonality](../concepts/correlation-and-orthogonality.md)
- [Elementary signals](../concepts/elementary-signals.md)
