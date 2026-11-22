"""E2 + E3: detection of documented events, ED vs. alternative outlier methods.

    venv/bin/python -m experiments.e3_compare
Writes experiments/results/e3_*.csv and e3_summary.md
"""
import os
import time

import numpy as np
import pandas as pd

from .common import METHODS, md_table, RESULTS_DIR, daily_curves, evaluate, event_labels, load

# (dataset, scenario label, zones or None, with_count, variables to drop)
PAPER_AIR = ["Cancelled"]  # the paper used delay variables only
SCENARIOS = [
    ("taxis", "NYC (all zones)", None, True, []),
    ("taxis", "JFK + LGA", ["132", "138"], True, []),
]
for _label, _zones in [("US (all airports)", None), ("ORD", ["ORD"]), ("ATL", ["ATL"]),
                       ("TPA", ["TPA"]), ("IAH + HOU", ["IAH", "HOU"])]:
    SCENARIOS.append(("airports", f"{_label} [delays]", _zones, False, PAPER_AIR))
    SCENARIOS.append(("airports", f"{_label} [+cancel]", _zones, False, []))
CATS = {"all": ("disruption", "holiday"), "disruption": ("disruption",), "artifact": ("artifact",)}


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    rows, ranks = [], []
    cache = {}
    for ds, label, zones, with_count, drop in SCENARIOS:
        if ds not in cache:
            cache[ds] = load(ds)
        X, names, dates = daily_curves(cache[ds], zones, with_count)
        keep = [k for k, v in enumerate(names) if v not in drop]
        X, names = X[:, :, keep], [names[k] for k in keep]
        print(f"\n== {ds} / {label}: N={X.shape[0]} P={X.shape[1]} vars={names}")
        scores = {}
        for m, fn in METHODS.items():
            t0 = time.perf_counter()
            scores[m] = fn(X, names)
            print(f"  {m:24s} {time.perf_counter() - t0:6.2f}s")
        for cat_name, cats in CATS.items():
            lab, evs = event_labels(ds, dates, cats, zones)
            if not evs:
                continue
            for m, s in scores.items():
                r = evaluate(s, lab, len(evs))
                rows.append({"dataset": ds, "scenario": label, "events": cat_name, "n_events": len(evs),
                             "method": m, **{k: v for k, v in r.items() if k != "best_rank"}})
                for e, br in zip(evs, r["best_rank"]):
                    ranks.append({"dataset": ds, "scenario": label, "events": cat_name,
                                  "event": e["name"], "method": m, "best_rank": br})
        # top-10 days per method, for qualitative inspection
        top = {m: [dates[i].date().isoformat() for i in np.argsort(-s, kind="stable")[:10]]
               for m, s in scores.items()}
        pd.DataFrame(top).to_csv(os.path.join(RESULTS_DIR, f"e3_top10_{ds}_{label.replace(' ', '_').replace('[', '').replace(']', '').replace('+', 'plus')}.csv"),
                                 index_label="rank0")

    df = pd.DataFrame(rows)
    rk = pd.DataFrame(ranks)
    df.to_csv(os.path.join(RESULTS_DIR, "e3_metrics.csv"), index=False)
    rk.to_csv(os.path.join(RESULTS_DIR, "e3_event_ranks.csv"), index=False)

    with open(os.path.join(RESULTS_DIR, "e3_summary.md"), "w") as f:
        for (ds, sc, ev), g in df.groupby(["dataset", "scenario", "events"], sort=False):
            f.write(f"\n### {ds} — {sc} — events: {ev} (n={g.n_events.iloc[0]})\n\n")
            f.write(md_table(g.drop(columns=["dataset", "scenario", "events", "n_events"])))
            f.write("\n")
            piv = rk[(rk.dataset == ds) & (rk.scenario == sc) & (rk.events == ev)] \
                .pivot(index="event", columns="method", values="best_rank")
            f.write("\nBest rank of each event (1 = most outlying day):\n\n")
            f.write(md_table(piv, index=True))
            f.write("\n")
    print(open(os.path.join(RESULTS_DIR, "e3_summary.md")).read())


if __name__ == "__main__":
    main()
