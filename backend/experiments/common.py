"""Shared helpers for the dissertation experiments (E2-E7).

Observations follow the GeotimeVis setting: one functional observation per
day, an hourly curve (P = 24) of several variables, aggregated over a set of
zones (all zones, or a selected region such as ORD).
"""
import contextlib
import io
import os

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import StandardScaler

from schemas.queryED import QueryED
from service.curve import Curve
from service.ED import ED, calculatePointwiseDepth
from service.depth_functions import L2_depth, spatial_depth

from .ground_truth import EVENTS

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
SEED = 42
R_LEVELS = [(i + 1) / 100 for i in range(100)]  # same r grid as the application


# ----------------------------------------------------------------------------- data

def load(name):
    d = np.load(os.path.join(DATA_DIR, f"{name}.npz"), allow_pickle=False)
    return {k: d[k] for k in d.files}


def daily_curves(t, zones=None, with_count=True):
    """Return X [N, P, V'], variable names, dates.

    For each (day, hour), variables are the mean per record over the chosen
    zones (sum of sums / sum of counts); `count` is the number of records.
    """
    sums, counts = t["sums"], t["counts"]
    if zones is not None:
        idx = [i for i, z in enumerate(t["zones"]) if z in set(zones)]
        if not idx:
            raise ValueError(f"no zone in {zones}")
        sums, counts = sums[idx], counts[idx]
    S = sums.sum(axis=0)            # [N, P, V]
    C = counts.sum(axis=0)          # [N, P]
    with np.errstate(divide="ignore", invalid="ignore"):
        M = np.where(C[..., None] > 0, S / C[..., None], 0.0)
    names = [str(v) for v in t["variables"]]
    if with_count:
        M = np.concatenate([C[..., None], M], axis=-1)
        names = ["count"] + names
    dates = pd.to_datetime(t["dates"])
    # drop days without any record (e.g. data gaps)
    keep = C.sum(axis=1) > 0
    return M[keep], names, dates[keep]


# ----------------------------------------------------------------------------- methods
# every method returns an outlyingness score: higher = more atypical

def _quiet(fn, *a, **kw):
    with contextlib.redirect_stdout(io.StringIO()):
        return fn(*a, **kw)


def _to_curves(X, names):
    N, P, V = X.shape
    C = []
    for i in range(N):
        c = Curve(P, i, len(R_LEVELS), names)
        for k, v in enumerate(names):
            c.data[v] = X[i, :, k].astype(float)
        C.append(c)
    return C


def score_ed(X, names, depth_type="L2", r=R_LEVELS):
    """Extremal Depth exactly as implemented in GeotimeVis (service/ED.py)."""
    C = _to_curves(X, names)
    q = QueryED(r=r, depth_type=depth_type, variables=names, hour_interval=(0, X.shape[1] - 1))
    C = _quiet(ED, C, q)
    ed = np.empty(len(C))
    for c in C:
        ed[c.id] = c.extremal_depth
    return -ed


def pointwise_depth(X, depth_type="L2"):
    """[N, P] multivariate pointwise depth (same functions used by ED)."""
    f = spatial_depth if depth_type.lower() == "spatial" else L2_depth
    return np.stack([f(X[:, t, :], X[:, t, :]) for t in range(X.shape[1])], axis=1)


def score_integrated_depth(X, names, depth_type="L2"):
    """Ablation: average the same pointwise depth over time (Fraiman-Muniz style)
    instead of the ED lexicographic ordering of depth CDFs."""
    return -pointwise_depth(X, depth_type).mean(axis=1)


def score_mbd(X, names):
    """Modified Band Depth (J = 2, Lopez-Pintado & Romo 2009), the depth behind
    the functional boxplot (Sun & Genton 2011); averaged over variables."""
    N = X.shape[0]
    pairs = N * (N - 1) / 2
    out = np.zeros(N)
    for k in range(X.shape[2]):
        x = X[:, :, k]
        below = (x[None, :, :] < x[:, None, :]).sum(axis=1)   # [N, P] curves strictly below
        above = (x[None, :, :] > x[:, None, :]).sum(axis=1)
        # bands from pairs (below, above) plus pairs touching an equal value
        inside = below * above + (N - 1)
        out += (inside / pairs).mean(axis=1)
    return -out / X.shape[2]


def _flat(X):
    return StandardScaler().fit_transform(X.reshape(X.shape[0], -1))


def score_iforest(X, names):
    m = IsolationForest(n_estimators=500, random_state=SEED).fit(_flat(X))
    return -m.score_samples(_flat(X))


def score_lof(X, names):
    m = LocalOutlierFactor(n_neighbors=20).fit(_flat(X))
    return -m.negative_outlier_factor_


def score_zscore(X, names):
    """Naive baseline: mean robust z-score w.r.t. the hour-wise median."""
    med = np.median(X, axis=0)
    mad = np.median(np.abs(X - med), axis=0) * 1.4826 + 1e-9
    return (np.abs(X - med) / mad).mean(axis=(1, 2))


METHODS = {
    "ED (L2)": lambda X, n: score_ed(X, n, "L2"),
    "ED (Spatial)": lambda X, n: score_ed(X, n, "spatial"),
    "Integrated depth (L2)": lambda X, n: score_integrated_depth(X, n, "L2"),
    "MBD / Func. boxplot": score_mbd,
    "Isolation Forest": score_iforest,
    "LOF": score_lof,
    "Robust z-score": score_zscore,
}


# ----------------------------------------------------------------------------- evaluation

def event_labels(dataset, dates, cats=("disruption", "holiday"), zones=None):
    """Return (day -> event idx or -1, list of events) restricted to categories
    and, when `zones` is given, to events expected in those zones."""
    evs = [e for e in EVENTS[dataset] if e["cat"] in cats]
    if zones is not None:
        evs = [e for e in evs if set(e.get("zones", [])) & set(zones)]
    lab = np.full(len(dates), -1)
    for j, e in enumerate(evs):
        m = (dates >= e["start"]) & (dates <= e["end"])
        lab[np.asarray(m)] = j
    return lab, evs


def evaluate(score, lab, n_events, ks=(5, 10, 20)):
    order = np.argsort(-score, kind="stable")
    rel = lab[order] >= 0
    res = {}
    for k in ks:
        res[f"P@{k}"] = rel[:k].mean()
        found = set(lab[order[:k]]) - {-1}
        res[f"EvR@{k}"] = len(found) / n_events if n_events else np.nan
    # average precision over event days
    hits = np.cumsum(rel)
    res["AP"] = (hits[rel] / (np.flatnonzero(rel) + 1)).mean() if rel.any() else 0.0
    # best (1-based) rank reached by each event
    rank_of = np.empty(len(order), int)
    rank_of[order] = np.arange(1, len(order) + 1)
    res["best_rank"] = [int(rank_of[lab == j].min()) for j in range(n_events)]
    return res


def md_table(df, index=False):
    """Minimal markdown table (avoids the optional `tabulate` dependency)."""
    if index:
        df = df.reset_index()
    cols = [str(c) for c in df.columns]
    fmt = lambda v: f"{v:.3f}" if isinstance(v, float) else str(v)
    lines = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    lines += ["| " + " | ".join(fmt(v) for v in row) + " |" for row in df.itertuples(index=False)]
    return "\n".join(lines)
