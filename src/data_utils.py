from pathlib import Path
import polars as pl
from typing import Dict

def load_config(cfg: Dict) -> Dict:
    return cfg

def read_csv(path: str, **kwargs) -> pl.DataFrame:
    return pl.read_csv(path, infer_schema_length=0, ignore_errors=True, **kwargs)

def load_mal_tables(raw_dir: str) -> Dict[str, pl.DataFrame]:
    raw = Path(raw_dir)
    dfs = {}
    paths = {
        "animelist": raw / "animelist.csv",
        "rating_complete": raw / "rating_complete.csv",
        "anime_meta": raw / "anime.csv",
    }
    for key, p in paths.items():
        if p.exists():
            dfs[key] = read_csv(str(p))
    return dfs
