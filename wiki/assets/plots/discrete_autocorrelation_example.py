"""Plot the energy autocorrelation of x[k] = [1,1,1,-1,-1,1,-1] from signals_1.pdf p.16.

Generates wiki/assets/plots/discrete_autocorrelation_example.png.
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 1, 1, -1, -1, 1, -1])
full = np.correlate(x, x, mode="full")
lags = np.arange(-(len(x) - 1), len(x))

fig, ax = plt.subplots(figsize=(7, 4))
ax.stem(lags, full, basefmt=" ")
ax.set_title(r"Energy autocorrelation $r_{xx}^{E}[k]$ of $x[k]=[1,1,1,-1,-1,1,-1]$")
ax.set_xlabel("k")
ax.set_ylabel(r"$r_{xx}^{E}[k]$")
ax.axhline(0, color="black", linewidth=0.6)
ax.grid(True, linewidth=0.3)

fig.tight_layout()
fig.savefig("wiki/assets/plots/discrete_autocorrelation_example.png", dpi=150)
print("saved")
