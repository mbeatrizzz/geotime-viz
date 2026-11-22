"""Dataset selection.

The active dataset is chosen with the GEOTIME_DATASET environment variable
(default: "airports"). It selects the configuration file
./db/files-<dataset>.json and an isolated folder ./db/cache/<dataset>/
holding that dataset's SQLite databases, so switching datasets never reuses
curves processed for another one.

    GEOTIME_DATASET=taxis uvicorn main:app --reload
"""
import json
import os

DATASET = os.environ.get("GEOTIME_DATASET", "airports")
CONFIG_PATH = f"./db/files-{DATASET}.json"
CACHE_DIR = f"./db/cache/{DATASET}"

# Fixed seed so t-SNE/UMAP projections are reproducible across runs
RANDOM_STATE = int(os.environ.get("GEOTIME_SEED", "42"))

if not os.path.exists(CONFIG_PATH):
    raise FileNotFoundError(
        f"Dataset '{DATASET}' has no configuration file at {CONFIG_PATH}. "
        "Set GEOTIME_DATASET to a dataset with a files-<name>.json in ./db."
    )

os.makedirs(CACHE_DIR, exist_ok=True)


def load_dataset_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)


def database_url(name):
    return f"sqlite:///{CACHE_DIR}/{name}.db"
