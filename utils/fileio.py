# This function imports a close price history file in csv format. It is formatted to date and organized by the dates which are in a "date" column.

import pandas as pd
from pathlib import Path

def data_import(path):
    data = pd.read_csv(
        Path(path),
        index_col="date",
        parse_dates=True,
        infer_datetime_format=True)
    return data