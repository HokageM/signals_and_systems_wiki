"""Plots for Lecture 2 (signals_2.pdf): convolution example, FT pairs, periodic spectrum.

Generates:
  wiki/assets/plots/convolution_exponential_step.png
  wiki/assets/plots/rect_si_fourier_pair.png
  wiki/assets/plots/triangle_si_squared_fourier_pair.png
  wiki/assets/plots/periodic_triangular_train_spectrum.png
"""
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Convolution of h(t)=eps(t) with x(t)=e^{-a t} eps(t) -> y(t) = (1/a)(1-e^{-a t}) eps(t)
a = 1.5
t = np.linspace(-1, 5, 2000)
y = np.where(t >= 0, (1 / a) * (1 - np.exp(-a * t)), 0.0)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(t, y, color="tab:orange")
ax.axhline(1 / a, color="gray", linestyle="--", linewidth=0.8, label=r"asymptote $1/\alpha$")
ax.axhline(0, color="black", linewidth=0.6)
ax.axvline(0, color="black", linewidth=0.6)
ax.set_title(r"$y(t) = h(t) * x(t)$, $h(t)=\varepsilon(t)$, $x(t)=e^{-\alpha t}\varepsilon(t)$, $\alpha=1.5$")
ax.set_xlabel("t")
ax.legend()
ax.grid(True, linewidth=0.3)
fig.tight_layout()
fig.savefig("wiki/assets/plots/convolution_exponential_step.png", dpi=150)
plt.close(fig)

# --- 2. rect(t/T) <-> T si(pi f T)
T = 1.0
t2 = np.linspace(-2, 2, 2000)
rect = np.where(np.abs(t2) < T / 2, 1.0, np.where(np.abs(t2) == T / 2, 0.5, 0.0))
f = np.linspace(-5, 5, 2000)
X = T * np.sinc(f * T)  # numpy sinc(x) = sin(pi x)/(pi x) -> T*si(pi f T)

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].plot(t2, rect, color="tab:orange")
axes[0].set_title(r"$x(t) = \mathrm{rect}(t/T)$, $T=1$")
axes[0].set_xlabel("t")
axes[1].plot(f, X, color="tab:blue")
axes[1].set_title(r"$X(f) = T\,si(\pi f T)$")
axes[1].set_xlabel("f")
for ax in axes:
    ax.axhline(0, color="black", linewidth=0.6)
    ax.axvline(0, color="black", linewidth=0.6)
    ax.grid(True, linewidth=0.3)
fig.tight_layout()
fig.savefig("wiki/assets/plots/rect_si_fourier_pair.png", dpi=150)
plt.close(fig)

# --- 3. Triangle Lambda(t) (support [-1,1]) <-> si^2(pi f)
t3 = np.linspace(-3, 3, 2000)
tri = np.where(np.abs(t3) > 1, 0.0, 1 - np.abs(t3))
f3 = np.linspace(-5, 5, 2000)
Xtri = (np.sinc(f3)) ** 2  # si(pi f)^2

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].plot(t3, tri, color="tab:orange")
axes[0].set_title(r"$\Lambda(t)$, support $[-1,1]$")
axes[0].set_xlabel("t")
axes[1].plot(f3, Xtri, color="tab:blue")
axes[1].set_title(r"$X(f) = si^2(\pi f)$")
axes[1].set_xlabel("f")
for ax in axes:
    ax.axhline(0, color="black", linewidth=0.6)
    ax.axvline(0, color="black", linewidth=0.6)
    ax.grid(True, linewidth=0.3)
fig.tight_layout()
fig.savefig("wiki/assets/plots/triangle_si_squared_fourier_pair.png", dpi=150)
plt.close(fig)

# --- 4. Periodic triangular train, period T=4, spectrum sampled from si^2(pi f) envelope
Tp = 4.0
tt = np.linspace(-6, 6, 3000)
xt = np.zeros_like(tt)
for k in range(-2, 3):
    shifted = tt - k * Tp
    xt += np.where(np.abs(shifted) > 1, 0.0, 1 - np.abs(shifted))

k_idx = np.arange(-6, 7)
Xn = (1 / Tp) * (np.sinc(k_idx / Tp)) ** 2

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].plot(tt, xt, color="tab:orange")
axes[0].set_title(r"$x_T(t)$, triangular pulse train, $T=4$")
axes[0].set_xlabel("t")
axes[1].stem(k_idx / Tp, Xn, basefmt=" ")
axes[1].set_title(r"$X_T(f) = \frac{1}{4}\sum_k si^2(\pi k/4)\,\delta(f-k/4)$")
axes[1].set_xlabel("f")
for ax in axes:
    ax.axhline(0, color="black", linewidth=0.6)
    ax.axvline(0, color="black", linewidth=0.6)
    ax.grid(True, linewidth=0.3)
fig.tight_layout()
fig.savefig("wiki/assets/plots/periodic_triangular_train_spectrum.png", dpi=150)
plt.close(fig)

print("saved all 4")
