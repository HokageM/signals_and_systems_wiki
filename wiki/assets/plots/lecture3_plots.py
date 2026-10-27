"""Plots for Lecture 3 (signals_3.pdf): filter types, allpass filter, analog filter impulse response.

Generates:
  wiki/assets/plots/filter_types.png
  wiki/assets/plots/allpass_filter_magnitude_phase.png
  wiki/assets/plots/analog_filter_impulse_response.png
"""
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Schematic lowpass/highpass/bandpass/bandstop magnitude responses
f = np.linspace(-5, 5, 2000)
fc, fl, fu = 2.0, 1.2, 3.0

lp = (np.abs(f) < fc).astype(float)
hp = (np.abs(f) > fc).astype(float)
bp = ((np.abs(f) > fl) & (np.abs(f) < fu)).astype(float)
bs = 1 - bp

fig, axes = plt.subplots(2, 2, figsize=(10, 6))
titles = ["Lowpass", "Highpass", "Bandpass", "Bandstop"]
data = [lp, hp, bp, bs]
for ax, title, d in zip(axes.flat, titles, data):
    ax.plot(f, d, color="tab:orange")
    ax.set_title(f"{title} filter " + r"$|H(f)|$")
    ax.set_xlabel("f")
    ax.set_ylim(-0.1, 1.2)
    ax.axhline(0, color="black", linewidth=0.6)
    ax.grid(True, linewidth=0.3)
fig.tight_layout()
fig.savefig("wiki/assets/plots/filter_types.png", dpi=150)
plt.close(fig)

# --- 2. Allpass filter H(f) = (1-j2*pi*f*T)/(1+j2*pi*f*T)
T = 1.0
f2 = np.linspace(-5, 5, 2000)
H = (1 - 1j * 2 * np.pi * f2 * T) / (1 + 1j * 2 * np.pi * f2 * T)
mag = np.abs(H)
phase = np.angle(H)

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].plot(f2, mag, color="tab:orange")
axes[0].set_title(r"$|H(f)|$ (allpass, constant magnitude)")
axes[0].set_ylim(0, 1.5)
axes[1].plot(f2, phase, color="tab:blue")
axes[1].set_title(r"$\varphi(f) = -2\arctan(2\pi f T)$")
for ax in axes:
    ax.set_xlabel("f")
    ax.axhline(0, color="black", linewidth=0.6)
    ax.grid(True, linewidth=0.3)
fig.tight_layout()
fig.savefig("wiki/assets/plots/allpass_filter_magnitude_phase.png", dpi=150)
plt.close(fig)

# --- 3. Analog filter impulse response h(t) = 2 e^{-t} cos(4t) eps(t)
t = np.linspace(-1, 6, 2000)
h = np.where(t >= 0, 2 * np.exp(-t) * np.cos(4 * t), 0.0)
envelope = np.where(t >= 0, 2 * np.exp(-t), np.nan)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(t, h, color="tab:orange", label=r"$h(t)=2e^{-t}\cos(4t)\,\varepsilon(t)$")
ax.plot(t, envelope, color="gray", linestyle="--", linewidth=0.8, label=r"envelope $\pm 2e^{-t}$")
ax.plot(t, -envelope, color="gray", linestyle="--", linewidth=0.8)
ax.axhline(0, color="black", linewidth=0.6)
ax.axvline(0, color="black", linewidth=0.6)
ax.set_title("Analog filter impulse response (poles at $-1\\pm j4$)")
ax.set_xlabel("t")
ax.legend()
ax.grid(True, linewidth=0.3)
fig.tight_layout()
fig.savefig("wiki/assets/plots/analog_filter_impulse_response.png", dpi=150)
plt.close(fig)

print("saved all 3")
