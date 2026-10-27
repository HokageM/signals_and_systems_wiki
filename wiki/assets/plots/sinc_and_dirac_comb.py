"""Plot the si-function (unnormalized sinc) and a sampled Dirac comb.

Source: signals_1.pdf p.4 (si-function) and p.5 (Dirac impulse comb).
Generates wiki/assets/plots/sinc_and_dirac_comb.png.
"""
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

t = np.linspace(-3 * np.pi, 3 * np.pi, 2000)
si = np.sinc(t / np.pi)  # numpy sinc is sin(pi x)/(pi x) -> si(t) = sin(t)/t
axes[0].plot(t, si, color="tab:orange")
axes[0].set_title(r"$si(t) = \sin(t)/t$")
axes[0].axhline(0, color="black", linewidth=0.6)
axes[0].axvline(0, color="black", linewidth=0.6)
axes[0].set_xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi])
axes[0].set_xticklabels([r"$-2\pi$", r"$-\pi$", "0", r"$\pi$", r"$2\pi$"])
axes[0].grid(True, linewidth=0.3)
axes[0].set_xlabel("t")

T = 1.0
k = np.arange(-3, 4)
axes[1].stem(k * T, np.ones_like(k), basefmt=" ")
axes[1].set_title(r"Dirac comb $\mathrm{III}_T(t)=\sum_k \delta(t-kT)$")
axes[1].axhline(0, color="black", linewidth=0.6)
axes[1].set_xticks(k * T)
axes[1].set_xticklabels([f"{kk}T" if kk != 0 else "0" for kk in k])
axes[1].grid(True, linewidth=0.3)
axes[1].set_xlabel("t")
axes[1].set_ylabel("weight")

fig.tight_layout()
fig.savefig("wiki/assets/plots/sinc_and_dirac_comb.png", dpi=150)
print("saved")
