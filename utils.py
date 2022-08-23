import pandas as pd


def data_load(file_path, headers):
    df = pd.read_csv(file_path, sep='::', header=0, names=headers, engine='python')

    return df

