import os
import numpy as np
import pandas as pd
import pyarrow.parquet as pq
from sqlalchemy import func
from .curve import Curve
from .plots_service import PlotService
from api.database import SessionLocal
from api.models import CurveModel
from config import DATASET, load_dataset_config

# Rows read per batch: keeps memory bounded for datasets with 100M+ records
BATCH_SIZE = 2_000_000


def data_already_processed():
    try:
        with SessionLocal() as db:
            return (db.query(func.count(CurveModel.primary_key)).scalar() or 0) > 0
    except Exception as e:
        print(f"Error checking existing data: {e}")
        return False


def read_batches(filename, columns):
    """Yield DataFrames of at most BATCH_SIZE rows from a parquet or csv file."""
    if filename.endswith(".parquet"):
        for batch in pq.ParquetFile(filename).iter_batches(batch_size=BATCH_SIZE, columns=columns):
            yield batch.to_pandas()
    else:
        yield from pd.read_csv(filename, usecols=columns, chunksize=BATCH_SIZE)


def prepare_batch(df, files_details):
    """Return a frame with columns zone, date, hour and the analysis variables."""
    time_variable = files_details['time_variable']
    zone_variable = files_details['zone_variable']
    hour_variable = files_details.get('time_resolution_variable')
    variables = files_details['variables']

    # derived variables, e.g. duration = dropoff - pickup (minutes)
    for name, (end, start) in files_details.get('derived_variables', {}).items():
        df[name] = (pd.to_datetime(df[end]) - pd.to_datetime(df[start])).dt.total_seconds() / 60.0

    timestamps = pd.to_datetime(df[time_variable])
    if hour_variable:
        # hour encoded as HHMM (e.g. CRSDepTime); rows without it are skipped
        df = df[df[hour_variable].notna()]
        timestamps = timestamps.loc[df.index]
        hours = df[hour_variable].astype(int) // 100 % 24
    else:
        hours = timestamps.dt.hour

    keep = pd.Series(True, index=df.index)
    for column, (low, high) in files_details.get('valid_ranges', {}).items():
        keep &= df[column].between(low, high)
    if 'date_range' in files_details:
        first, last = files_details['date_range']
        keep &= timestamps.between(pd.Timestamp(first), pd.Timestamp(last) + pd.Timedelta(days=1), inclusive="left")

    out = pd.DataFrame({
        'zone': df[zone_variable].astype(str),
        'date': timestamps.dt.normalize(),
        'hour': hours.astype(int),
    })
    for var in variables:
        out[var] = df[var].fillna(0.0).astype(float)   # missing values count as 0
    out['values'] = 1.0                                # record counter
    return out[keep]


def aggregate_files(files_details):
    """Sum every variable and count records per (zone, date, hour), file by file."""
    columns = [
        files_details['time_variable'],
        files_details['zone_variable'],
        *[c for c in [files_details.get('time_resolution_variable')] if c],
        *[v for v in files_details['variables'] if v not in files_details.get('derived_variables', {})],
        *[c for pair in files_details.get('derived_variables', {}).values() for c in pair],
    ]
    columns = list(dict.fromkeys(columns))
    keys = ['zone', 'date', 'hour']

    total = None
    for filename in files_details['filenames']:
        if not os.path.exists(filename):
            print(f"File {filename} does not exist. Please check the path.")
            continue
        print(f"Reading file: {filename}")
        for df in read_batches(filename, columns):
            part = prepare_batch(df, files_details).groupby(keys).sum()
            total = part if total is None else total.add(part, fill_value=0.0)
    return total


def build_curves(aggregated, files_details):
    """One Curve per (zone, date) holding hourly sums of each variable and the record count."""
    variables = files_details['variables']
    P = files_details['resolution']
    R = 100

    zone_names = sorted(aggregated.index.get_level_values('zone').unique())
    zone_ids = {zone: i for i, zone in enumerate(zone_names)}
    all_dates = sorted(aggregated.index.get_level_values('date').unique())
    date_ids = {date: j for j, date in enumerate(all_dates)}
    print(f"Number of days (N): {len(all_dates)}, zones (Z): {len(zone_names)}, resolution (P): {P}")

    C = []
    for (zone, date), group in aggregated.groupby(level=['zone', 'date']):
        hours = group.index.get_level_values('hour').to_numpy()
        curve = Curve(P, date_ids[date], R, variables)
        curve.zone = zone_ids[zone]
        curve.zone_name = zone
        curve.date = pd.Timestamp(date).to_pydatetime()
        curve.weekDay = curve.date.weekday()
        for var in variables + ['values']:
            series = np.zeros(P)
            series[hours] = group[var].to_numpy()
            curve.data[var] = series
        C.append(curve)

    print(f"Built {len(C)} curves (zone, day) with at least one record.")
    return C


def pre_process_data_func():
    if data_already_processed():
        print("Data already processed. Skipping pre-processing.")
        return

    print(f"Reading data for the first time (dataset: {DATASET})")
    files_details = load_dataset_config()

    aggregated = aggregate_files(files_details)
    if aggregated is None:
        print("No files to read. Please check the files-<dataset>.json configuration.")
        return

    C = build_curves(aggregated, files_details)

    print("Saving data to zone database")
    PlotService.save_curves_to_db(C)
    print("Data saved to database")
