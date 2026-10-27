"""Plots for Lecture 4 (signals_4.pdf): sampling spectrum, DFT example, Z-transform ROC.

Generates:
  wiki/assets/plots/sampling_spectrum.png
  wiki/assets/plots/dft_periodic_cosine.png
  wiki/assets/plots/z_transform_roc_regions.png
"""
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Sampled spectrum: no aliasing (fs=4/T) vs aliasing (fs=1/T), base spectrum
#     a trapezoid-like X(f) with support up to B = 2/T (triangle+rect combo envelope)
B = 2.0  # normalized bandwidth (in units of 1/T)
def base_spectrum(f):
    # trapezoid: flat top |f|<1, linear taper to 0 at |f|=2
    f = np.abs(f)
    return np.clip(2 - f, 0, 1) * (f < 2) + 0.0

f = np.linspace(-6, 6, 3000)

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
for ax, fs, title in zip(axes, [4.0, 1.0], ["No aliasing ($f_s=4/T > 2B$)", "Aliasing ($f_s=1/T < 2B$)"]):
    xs = np.zeros_like(f)
    for k in range(-3, 4):
        xs += base_spectrum(f - k * fs)
    ax.plot(f, xs, color="tab:orange")
    ax.set_title(title)
    ax.set_xlabel("f  [1/T]")
    ax.axhline(0, color="black", linewidth=0.6)
    ax.grid(True, linewidth=0.3)
fig.tight_layout()
fig.savefig("wiki/assets/plots/sampling_spectrum.png", dpi=150)
plt.close(fig)

# --- 2. DFT of x[k] = cos(2*pi*k/6), N=6 and N=12
def dft_mag(x, N):
    n = np.arange(N)
    X = np.array([np.sum(x * np.exp(-1j * 2 * np.pi * n_ * np.arange(len(x)) / N)) for n_ in n])
    return n, X.real

fig, axes = plt.subplots(1, 2, figsize=(11, 4))

N = 6
k = np.arange(N)
x = np.cos(2 * np.pi * k / 6)
n, X = dft_mag(x, N)
axes[0].stem(n, X, basefmt=" ")
axes[0].set_title(r"$N=6$: $X[n]$ (nonzero at $n=1,5$)")
axes[0].set_xlabel("n")

N = 12
k = np.arange(N)
x = np.cos(2 * np.pi * k / 6)
n, X = dft_mag(x, N)
axes[1].stem(n, X, basefmt=" ")
axes[1].set_title(r"$N=12$: $X[n]$ (nonzero at $n=2,10$)")
axes[1].set_xlabel("n")

for ax in axes:
    ax.axhline(0, color="black", linewidth=0.6)
    ax.grid(True, linewidth=0.3)
fig.tight_layout()
fig.savefig("wiki/assets/plots/dft_periodic_cosine.png", dpi=150)
plt.close(fig)

# --- 3. Z-transform ROC regions for H(z) = 11z / ((z-1/4)(z-3))
theta = np.linspace(0, 2 * np.pi, 200)
fig, ax = plt.subplots(figsize=(5.5, 5.5))
ax.plot(0.25 * np.cos(theta), 0.25 * np.sin(theta), color="gray", linestyle="--")
ax.plot(3 * np.cos(theta), 3 * np.sin(theta), color="gray", linestyle="--")
ax.plot([0.25], [0], "x", color="tab:red", markersize=10, label="poles (z=1/4, z=3)")
ax.plot([3], [0], "x", color="tab:red", markersize=10)
ax.fill(0.25 * np.cos(theta), 0.25 * np.sin(theta), color="tab:blue", alpha=0.25, label="Region I: |z|<1/4")
r_out = np.linspace(0.25, 3, 2)
ax.fill_between(3 * np.cos(theta), -3 * np.sin(theta), 3 * np.sin(theta), color="none")
ann_ring_theta = np.linspace(0, 2 * np.pi, 200)
ax.fill(np.concatenate([3*np.cos(ann_ring_theta), 0.25*np.cos(ann_ring_theta[::-1])]),
        np.concatenate([3*np.sin(ann_ring_theta), 0.25*np.sin(ann_ring_theta[::-1])]),
        color="tab:orange", alpha=0.25, label="Region II: 1/4<|z|<3")
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.axhline(0, color="black", linewidth=0.6)
ax.axvline(0, color="black", linewidth=0.6)
ax.set_aspect("equal")
ax.set_title(r"Pole-zero plot and ROC regions of $H(z)=\frac{11z}{(z-1/4)(z-3)}$")
ax.legend(loc="upper right", fontsize=8)
fig.tight_layout()
fig.savefig("wiki/assets/plots/z_transform_roc_regions.png", dpi=150)
plt.close(fig)

print("saved all 3")
