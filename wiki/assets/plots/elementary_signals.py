"""Plot the elementary continuous-time signals from Lecture 1 (signals_1.pdf, p.3-4).

Generates wiki/assets/plots/elementary_signals.png showing the unit step,
ramp, signum, rectangular, triangular, and real exponential functions.
"""
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-3, 3, 2000)

step = np.where(t > 0, 1.0, np.where(t < 0, 0.0, 0.5))
ramp = t * step
sgn = np.where(t > 0, 1.0, np.where(t < 0, -1.0, 0.0))
rect = np.where(np.abs(t) < 0.5, 1.0, np.where(np.abs(t) == 0.5, 0.5, 0.0))
tri = np.where(np.abs(t) > 1, 0.0, 1 - np.abs(t))
alpha = 1.2
exp_fn = np.where(t >= 0, np.exp(-alpha * t), np.nan)

fig, axes = plt.subplots(2, 3, figsize=(12, 6))

axes[0, 0].plot(t, step, color="tab:orange")
axes[0, 0].set_title(r"Unit step $\varepsilon(t)$")

axes[0, 1].plot(t, ramp, color="tab:orange")
axes[0, 1].set_title(r"Ramp $\rho(t) = t\,\varepsilon(t)$")

axes[0, 2].plot(t, sgn, color="tab:orange")
axes[0, 2].set_title(r"Signum $\mathrm{sgn}(t)$")

axes[1, 0].plot(t, rect, color="tab:orange")
axes[1, 0].set_title(r"Rectangular $\mathrm{rect}(t)$")

axes[1, 1].plot(t, tri, color="tab:orange")
axes[1, 1].set_title(r"Triangular $\Delta(t)$")

axes[1, 2].plot(t, exp_fn, color="tab:orange")
axes[1, 2].set_title(r"Real exponential $A e^{-\alpha t}\varepsilon(t)$")

for ax in axes.flat:
    ax.axhline(0, color="black", linewidth=0.6)
    ax.axvline(0, color="black", linewidth=0.6)
    ax.grid(True, linewidth=0.3)
    ax.set_xlabel("t")

fig.tight_layout()
fig.savefig("wiki/assets/plots/elementary_signals.png", dpi=150)
print("saved")
