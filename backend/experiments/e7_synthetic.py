"""E7: controlled benchmark with injected anomalies.

Inliers are daily multivariate profiles (P = 24, V = 3) with a two-peak shape,
correlated variables, random amplitude and noise. For each anomaly type, 3% of
the curves are replaced by anomalous ones; AP and P@k are averaged over seeds.

Anomaly types
    magnitude_persistent : whole curve shifted up/down (all variables)
    magnitude_isolated   : short spike/drop in 2-3 consecutive hours
    shape_phase          : peaks shifted by 3-5 hours (same level)
    amplitude            : peaks flattened (near-constant profile)
    single_variable      : only one variable deviates (others normal)
    collapse             : all variables near zero over the day (Sandy-like)

    venv/bin/python -m experiments.e7_synthetic
"""
import os

import numpy as np
import pandas as pd

from .common import METHODS, RESULTS_DIR, evaluate, md_table

N, P, V = 300, 24, 3
CONTAM = 0.03
SEEDS = range(10)
TYPES = ["magnitude_persistent", "magnitude_isolated", "shape_phase",
         "amplitude", "single_variable", "collapse"]
t = np.arange(P)


def profile(shift=0.0, amp=1.0):
    h = (t - shift) % P
    return 1.0 + amp * (np.exp(-((h - 8) ** 2) / 6) + 1.3 * np.exp(-((h - 18) ** 2) / 8))


def inlier(rng):
    a = rng.normal(1, 0.08)
    base = profile(shift=rng.normal(0, 0.5), amp=rng.normal(1, 0.1)) * a
    weights = np.array([1.0, 0.7, 1.4])
    X = base[:, None] * weights[None, :] + rng.normal(0, 0.08, (P, V))
    return X


def anomaly(rng, kind):
    X = inlier(rng)
    if kind == "magnitude_persistent":
        X *= rng.choice([0.6, 1.4])
    elif kind == "magnitude_isolated":
        h = rng.integers(2, P - 3)
        X[h:h + 3] *= rng.choice([0.2, 2.2])
    elif kind == "shape_phase":
        X = np.roll(X, int(rng.choice([-5, -4, -3, 3, 4, 5])), axis=0)
    elif kind == "amplitude":
        X = X.mean(axis=0, keepdims=True) + 0.15 * (X - X.mean(axis=0, keepdims=True))
    elif kind == "single_variable":
        k = rng.integers(V)
        X[:, k] *= rng.choice([0.4, 1.8])
    elif kind == "collapse":
        X *= 0.1
    return X


def dataset(seed, kind):
    rng = np.random.default_rng(seed)
    n_out = int(round(CONTAM * N))
    X = np.stack([inlier(rng) for _ in range(N)])
    idx = rng.choice(N, n_out, replace=False)
    for i in idx:
        X[i] = anomaly(rng, kind)
    lab = np.full(N, -1)
    lab[idx] = np.arange(n_out)
    return X, lab, n_out


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    names = [f"v{k}" for k in range(V)]
    rows = []
    for kind in TYPES:
        for seed in SEEDS:
            X, lab, n_out = dataset(seed, kind)
            for m, fn in METHODS.items():
                r = evaluate(fn(X, names), lab, n_out, ks=(n_out,))
                rows.append({"type": kind, "seed": seed, "method": m,
                             "AP": r["AP"], "P@k": r[f"P@{n_out}"]})
        print("done", kind, flush=True)
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(RESULTS_DIR, "e7_synthetic_raw.csv"), index=False)
    ap = df.pivot_table(index="type", columns="method", values="AP", aggfunc="mean")
    pk = df.pivot_table(index="type", columns="method", values="P@k", aggfunc="mean")
    ap.loc["mean"] = ap.mean()
    pk.loc["mean"] = pk.mean()
    with open(os.path.join(RESULTS_DIR, "e7_summary.md"), "w") as f:
        f.write(f"N={N}, P={P}, V={V}, contamination={CONTAM:.0%}, {len(SEEDS)} seeds. "
                "k = number of injected anomalies.\n\n### Average precision\n\n")
        f.write(md_table(ap, index=True))
        f.write("\n\n### Precision@k (k = #anomalies)\n\n")
        f.write(md_table(pk, index=True))
        f.write("\n")
    print(open(os.path.join(RESULTS_DIR, "e7_summary.md")).read())


if __name__ == "__main__":
    main()
