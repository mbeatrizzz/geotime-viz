"""E5: runtime of the GeotimeVis ED implementation vs. N (curves) and P (resolution).

Measures the backend function service.ED.ED on synthetic data (from E7),
univariate (pairwise comparison, O(N^2 P)) and multivariate (L2 / Spatial).
Each point is the median of 3 runs.

    venv/bin/python -m experiments.e5_scalability
"""
import os
import time

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from .common import RESULTS_DIR, md_table, score_ed
from .e7_synthetic import inlier

REPS = 3
N_GRID = [50, 100, 200, 400, 800, 1600]
P_GRID = [12, 24, 48, 96]
N_FIXED, P_FIXED = 400, 24
UNIV_MAX_N = 800  # pure-Python O(N^2 P) loop: larger N takes minutes
CONFIGS = [("Univariate", 1, "L2"), ("Multivariate L2 (V=3)", 3, "L2"),
           ("Multivariate Spatial (V=3)", 3, "spatial")]


def data(n, p, v, seed=0):
    rng = np.random.default_rng(seed)
    X = np.stack([inlier(rng) for _ in range(n)])  # [n, 24, 3]
    if p != 24:  # resample to p points
        src = np.linspace(0, 1, 24)
        dst = np.linspace(0, 1, p)
        X = np.stack([np.stack([np.interp(dst, src, X[i, :, k]) for k in range(3)], -1) for i in range(n)])
    return X[:, :, :v]


def timed(X, depth):
    names = [f"v{k}" for k in range(X.shape[2])]
    ts = []
    for _ in range(REPS):
        t0 = time.perf_counter()
        score_ed(X, names, depth)
        ts.append(time.perf_counter() - t0)
    return float(np.median(ts))


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    rows = []
    for label, v, depth in CONFIGS:
        for n in N_GRID:
            if v == 1 and n > UNIV_MAX_N:
                continue
            s = timed(data(n, P_FIXED, v), depth)
            rows.append({"config": label, "axis": "N", "N": n, "P": P_FIXED, "seconds": s})
            print(label, "N", n, f"{s:.2f}s", flush=True)
        for p in P_GRID:
            s = timed(data(N_FIXED, p, v), depth)
            rows.append({"config": label, "axis": "P", "N": N_FIXED, "P": p, "seconds": s})
            print(label, "P", p, f"{s:.2f}s", flush=True)
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(RESULTS_DIR, "e5_scalability.csv"), index=False)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    for ax, axis, x in [(axes[0], "N", "N"), (axes[1], "P", "P")]:
        for label, g in df[df.axis == axis].groupby("config", sort=False):
            ax.plot(g[x], g.seconds, marker="o", label=label)
        ax.set_xscale("log", base=2)
        ax.set_yscale("log")
        ax.set_xlabel(f"{x} ({'curves' if x == 'N' else 'points per curve'})")
        ax.set_ylabel("time (s)")
        ax.set_title(f"Runtime vs {x} ({'P=%d' % P_FIXED if x == 'N' else 'N=%d' % N_FIXED})")
        ax.grid(True, which="both", alpha=0.3)
    axes[0].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(os.path.join(RESULTS_DIR, "e5_scalability.pdf"))
    fig.savefig(os.path.join(RESULTS_DIR, "e5_scalability.png"), dpi=150)

    # empirical growth exponent (slope in log-log) for N
    with open(os.path.join(RESULTS_DIR, "e5_summary.md"), "w") as f:
        f.write(md_table(df))
        f.write("\n\nEmpirical exponent b in time ~ N^b (log-log fit):\n\n")
        for label, g in df[df.axis == "N"].groupby("config", sort=False):
            b = np.polyfit(np.log(g.N), np.log(g.seconds), 1)[0]
            f.write(f"- {label}: b = {b:.2f}\n")
    print(open(os.path.join(RESULTS_DIR, "e5_summary.md")).read())


if __name__ == "__main__":
    main()
