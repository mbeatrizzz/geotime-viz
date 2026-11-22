"""E4: sensitivity of the ED ranking to pipeline choices.

Compares the ED ranking of the reference configuration (L2 depth, r = 100
levels, hourly resolution, all variables, full day) against variations, using
Kendall's tau over all days and the overlap of the top-10 outlying days.

    venv/bin/python -m experiments.e4_sensitivity
"""
import os

import numpy as np
import pandas as pd
from scipy.stats import kendalltau

from .common import RESULTS_DIR, daily_curves, load, md_table, score_ed, score_integrated_depth

SCENARIOS = [
    ("taxis", "NYC (all zones)", None, True),
    ("airports", "US (all airports) +cancel", None, False),
    ("airports", "ORD +cancel", ["ORD"], False),
]


def rebin(X, bins):
    """Aggregate hourly curves into `bins` equal blocks (mean)."""
    N, P, V = X.shape
    return X.reshape(N, bins, P // bins, V).mean(axis=2)


def variants(X, names):
    yield "Spatial depth", score_ed(X, names, "spatial")
    yield "r = 20 levels", score_ed(X, names, "L2", r=[(i + 1) / 20 for i in range(20)])
    yield "r = 10 levels", score_ed(X, names, "L2", r=[(i + 1) / 10 for i in range(10)])
    yield "2-hour bins (P=12)", score_ed(rebin(X, 12), names, "L2")
    yield "4-hour bins (P=6)", score_ed(rebin(X, 6), names, "L2")
    yield "Hours 06-23 only", score_ed(X[:, 6:, :], names, "L2")
    # leave-one-variable-out
    for k, v in enumerate(names):
        keep = [j for j in range(len(names)) if j != k]
        yield f"Without '{v}'", score_ed(X[:, :, keep], [names[j] for j in keep], "L2")
    yield "Integrated depth (no ED ordering)", score_integrated_depth(X, names, "L2")


def top(s, k=10):
    return set(np.argsort(-s, kind="stable")[:k])


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    rows = []
    cache = {}
    for ds, label, zones, with_count in SCENARIOS:
        cache.setdefault(ds, load(ds))
        X, names, dates = daily_curves(cache[ds], zones, with_count)
        ref = score_ed(X, names, "L2")
        print(f"== {ds} / {label}")
        for name, s in variants(X, names):
            tau = kendalltau(ref, s).statistic
            ov = len(top(ref) & top(s)) / 10
            rows.append({"scenario": f"{ds} / {label}", "variation": name,
                         "kendall_tau": tau, "top10_overlap": ov})
            print(f"  {name:36s} tau={tau:.3f} top10={ov:.1f}")
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(RESULTS_DIR, "e4_sensitivity.csv"), index=False)
    with open(os.path.join(RESULTS_DIR, "e4_summary.md"), "w") as f:
        f.write("Reference: ED with L2 depth, r = 100 levels, hourly (P=24), all variables, full day.\n\n")
        f.write(md_table(df))
        f.write("\n")


if __name__ == "__main__":
    main()
