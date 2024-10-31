import pkg_resources
import pandas as pd

def load():
    data_path = pkg_resources.resource_filename('fortnight', 'datasets/weather.csv') # gets a path
    return pd.read_csv(data_path, header = 0)
