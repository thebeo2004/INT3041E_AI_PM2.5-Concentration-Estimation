import numpy as np
import pandas as pd 
from datetime import datetime, timedelta
from numpy import nan

import os
root_folder = os.path.dirname(os.path.abspath(os.getcwd()))
file_path = root_folder + "/data/meteorological/meteorological.csv"

date_format = '%Y-%m-%d'
begin_date = datetime.strptime('2020-01-01', date_format)
end_date = datetime.strptime('2021-12-31', date_format)
time_delta = timedelta(days=1)

def fill_missing_date(df: pd.DataFrame, id: int, lat: float, lon: float):
    curr_date = begin_date
    
    while(curr_date <= end_date):
        if (df.loc[(df['ID'] == id) & (df['time'] == curr_date)].empty):
            
            new_row = [curr_date, id, nan, lat, lon, nan, nan, nan, nan, nan, nan, nan, nan, nan]
            
            df.loc[len(df)] = new_row
        
        curr_date = curr_date + time_delta
    
    return df

def meteorological_df(include_missing_date=False) -> pd.DataFrame:
    
    df = pd.read_csv(file_path)
    df['time'] = pd.to_datetime(df['time'])
    
    if (include_missing_date):
        print("Warning: This option will perform adding missing date into meteorological dataframe, even if other fields are null")
        print("This option should be set for the purpose of visualization")
        print("If you just want to fetch meteorological data for training, set the parameter include_missing_data to False")
        id_list = df['ID'].unique()

        coordination_list = []

        for id in id_list:
            coordination_list.append(np.array(df.loc[df['ID'] == id].iloc[0][['lat', 'lon']]))
        
        for (i, id) in enumerate(id_list):
            lat = coordination_list[i][0]
            lon = coordination_list[i][1]
            df = fill_missing_date(df = df, id = id, lat = lat, lon = lon)
    
    df = df.sort_values(by=['time', 'ID'], ascending=True)
    
    return df
    
    