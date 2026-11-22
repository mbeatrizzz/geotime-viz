"""Build compact (zone, day, hour) tensors from the raw files, one file at a time.

Output: experiments/data/<dataset>.npz with
    sums    float64 [Z, N, P, V]  sum of each variable per (zone, day, hour)
    counts  float64 [Z, N, P]     number of records per (zone, day, hour)
    zones   [Z]  zone identifiers
    dates   [N]  ISO dates
    variables [V]

Usage (from backend/):
    venv/bin/python -m experiments.build_tensors taxis
    venv/bin/python -m experiments.build_tensors airports
"""
import glob
import os
import sys

import numpy as np
import pandas as pd
import pyarrow.parquet as pq

OUT_DIR = os.path.join(os.path.dirname(__file__), "data")
P = 24

DATASETS = {
    "taxis": {
        "files": sorted(glob.glob("./db/taxis/yellow_tripdata_2012-*.parquet")),
        "year": 2012,
        "variables": ["duration", "trip_distance", "fare_amount"],
    },
    "airports": {
        "files": sorted(
            glob.glob("./db/us-airports/On_Time_Reporting_*_2024_*.csv"),
            key=lambda f: int(f.rsplit("_", 1)[1].split(".")[0]),
        ),
        "year": 2024,
        # Cancelled: mean = cancellation rate (closures are invisible to delay-only variables)
        "variables": ["DepDelay", "CarrierDelay", "WeatherDelay", "SecurityDelay", "Cancelled"],
    },
}


BATCH = 2_000_000


def read_taxi(path):
    cols = ["tpep_pickup_datetime", "tpep_dropoff_datetime", "PULocationID", "trip_distance", "fare_amount"]
    for b in pq.ParquetFile(path).iter_batches(batch_size=BATCH, columns=cols):
        yield _taxi_frame(b.to_pandas())


def _taxi_frame(t):
    t["duration"] = (t.tpep_dropoff_datetime - t.tpep_pickup_datetime).dt.total_seconds() / 60.0
    # basic cleaning: drop impossible trips
    ok = (
        t.duration.between(0, 240)
        & t.trip_distance.between(0, 100)
        & t.fare_amount.between(0, 500)
        & (t.tpep_pickup_datetime.dt.year == 2012)
        & t.PULocationID.between(1, 263)
    )
    t = t[ok]
    return pd.DataFrame({
        "zone": t.PULocationID.astype(str).to_numpy(),
        "date": t.tpep_pickup_datetime.dt.normalize().to_numpy(),
        "hour": t.tpep_pickup_datetime.dt.hour.to_numpy(),
        "duration": t.duration.to_numpy(),
        "trip_distance": t.trip_distance.to_numpy(),
        "fare_amount": t.fare_amount.to_numpy(),
    })


def read_airports(path):
    cols = ["FlightDate", "Origin", "CRSDepTime", "Cancelled",
            "DepDelay", "CarrierDelay", "WeatherDelay", "SecurityDelay"]
    for t in pd.read_csv(path, usecols=cols, chunksize=BATCH):
        yield _airport_frame(t)


def _airport_frame(t):
    t = t[t.CRSDepTime.notna()]
    # delay-cause fields are only reported for delayed flights: missing -> 0 minutes
    for v in ["DepDelay", "CarrierDelay", "WeatherDelay", "SecurityDelay"]:
        t[v] = t[v].fillna(0.0)
    return pd.DataFrame({
        "zone": t.Origin.astype(str).to_numpy(),
        "date": pd.to_datetime(t.FlightDate).to_numpy(),
        "hour": (t.CRSDepTime.astype(int) // 100 % 24).to_numpy(),
        "DepDelay": t.DepDelay.to_numpy(),
        "CarrierDelay": t.CarrierDelay.to_numpy(),
        "WeatherDelay": t.WeatherDelay.to_numpy(),
        "SecurityDelay": t.SecurityDelay.to_numpy(),
        "Cancelled": t.Cancelled.fillna(0.0).to_numpy(),
    })


def main(name):
    cfg = DATASETS[name]
    reader = read_taxi if name == "taxis" else read_airports
    variables = cfg["variables"]
    dates = pd.date_range(f"{cfg['year']}-01-01", f"{cfg['year']}-12-31", freq="D")
    N = len(dates)

    zone_index = {}
    ZMAX = 500  # upper bound on zones (taxi: 263, airports: ~350)
    counts = np.zeros(ZMAX * N * P)
    sums = np.zeros((ZMAX * N * P, len(variables)))
    day0 = np.datetime64(dates[0], "D")

    def accumulate(df):
        for z in df.zone.unique():
            if z not in zone_index:
                zone_index[z] = len(zone_index)
        assert len(zone_index) <= ZMAX, "increase ZMAX"
        z_idx = df.zone.map(zone_index).to_numpy()
        d_idx = (df.date.to_numpy().astype("datetime64[D]") - day0).astype(int)
        h_idx = df.hour.to_numpy().astype(int)
        keep = (d_idx >= 0) & (d_idx < N)
        flat = ((z_idx * N + d_idx) * P + h_idx)[keep]
        size = ZMAX * N * P
        counts[:] += np.bincount(flat, minlength=size)
        for k, v in enumerate(variables):
            sums[:, k] += np.bincount(flat, weights=df[v].to_numpy()[keep], minlength=size)

    for path in cfg["files"]:
        print("reading", path, flush=True)
        for df in reader(path):
            accumulate(df)

    Z = len(zone_index)
    counts = counts[: Z * N * P]
    sums = sums[: Z * N * P]

    zones = np.array(sorted(zone_index, key=zone_index.get))
    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, f"{name}.npz")
    np.savez_compressed(
        out,
        sums=sums.reshape(Z, N, P, len(variables)),
        counts=counts.reshape(Z, N, P),
        zones=zones,
        dates=np.array([d.date().isoformat() for d in dates]),
        variables=np.array(variables),
    )
    print(f"saved {out}: Z={Z} N={N} P={P} V={len(variables)} records={int(counts.sum())}")


if __name__ == "__main__":
    main(sys.argv[1])
