import pandas as pd 

import os
root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = root_folder + "\\data\\consolidation\\remotesensing_atmospheric.csv"


def consolidated_df() -> pd.DataFrame:
    
    df = pd.read_csv(file_path)
    
    df['time'] = pd.to_datetime(df['time'])
    
    df = df.sort_values(by=['time', 'ID'], ascending=True)
    
    return df
    