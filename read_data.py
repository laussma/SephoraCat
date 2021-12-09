import pandas as pd
from ColumnNames import column_names

def read_data(filepath, nrows=None, start_row=None):
    if nrows and start_row is not None:
        df = pd.read_csv(filepath, names=column_names, delimiter=",", skiprows=start_row, nrows=nrows)
    else:
        df = pd.read_csv(filepath, names=column_names, delimiter=",")
    return df