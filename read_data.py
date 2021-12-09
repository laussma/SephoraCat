import pandas as pd
from ColumnNames import column_names

def read_data(filepath, nrows=None, start_row=None):
    df = pd.read_csv(filepath, names=column_names, delimiter=",", dtype={"raw_ingrediat_desc": str})
    return df
