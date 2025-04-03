import numpy as np
import pandas as pd 

import os
root_folder = os.path.dirname(os.path.abspath(os.getcwd()))
data_folder = root_folder + "\\data\\satellite-based"

factors = ['CLOUD', 'CO', 'HCHO', 'NDVI', 'NO2', 'O3', 'SO2', 'AAI']

cols = ['cloud_fraction', 'CO_column_number_density', 'tropospheric_HCHO_column_number_density', 'NDVI', 
        'tropospheric_NO2_column_number_density', 'O3_column_number_density', 'SO2_column_number_density',
        'absorbing_aerosol_index']

def get_path(factor: str, year: int) -> str:
    
    # These 2 names are interchangable
    if (factor == 'AAI'):
        factor = 'UV'
    
    factor_folder = data_folder + "\\" + factor
    file_name = f"{factor}_{year}.csv"
    
    return factor_folder + "\\" + file_name

def remote_sensing_factor_df(factor: str, begin=2019, end=2024) -> pd.DataFrame:
    
    if not (factor in factors):
        print("Factor must be in f{factors}")
        return None
    
    years = np.arange(begin, end + 1)
    
    df = pd.read_csv(get_path(factor=factor, year=begin))
    
    for i in range(1, len(years)):
        df = pd.concat([df, pd.read_csv(get_path(factor=factor, year=years[i]))])   
        
    col_name = cols[factors.index(factor)]
    
    df.rename(columns={col_name: factor}, inplace=True)
    
    df['date'] = pd.to_datetime(df['date'])
    
    df = df.sort_values(by=['date', 'ID'], ascending=True)
    
    return df