# Dissertation experiments (E2–E7)

Run from `backend/` with the project venv:

```bash
venv/bin/python -m experiments.build_tensors taxis      # ~10 min, raw parquet -> data/taxis.npz
venv/bin/python -m experiments.build_tensors airports   # ~10 min, raw csv     -> data/airports.npz
venv/bin/python -m experiments.e3_compare      # E2+E3: documented events, ED vs. baselines
venv/bin/python -m experiments.e4_sensitivity  # E4: Kendall tau vs. pipeline choices
venv/bin/python -m experiments.e7_synthetic    # E7: injected anomalies (10 seeds)
venv/bin/python -m experiments.e5_scalability  # E5: runtime vs N and P (+ figure)
```

Outputs go to `results/` (`*_summary.md` tables, raw `*.csv`, `e5_scalability.pdf`).

- `ground_truth.py` — event list (E2). **Verify and cite each date.**
- `common.py` — data loading (one curve per day, hourly, aggregated over zones),
  methods (ED calls `service/ED.py` directly), metrics (P@k, event recall@k, AP, best rank).

Seed: 42. Taxi cleaning: 0 < duration ≤ 240 min, distance ≤ 100 mi, fare ≤ $500, zone 1–263.
Airports: missing delay-cause fields = 0; `Cancelled` mean = cancellation rate.
