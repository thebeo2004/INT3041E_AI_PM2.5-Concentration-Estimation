import pandas as pd 
import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta

import sys
import os

root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fetch_data_folder = root_folder + "\\fetch_data"

sys.path.append(fetch_data_folder)
from fetching_meteorological import meteorological_df
from fetching_consolidated_data import consolidated_df

time_format = "%Y-%m-%d"

training_splits = [datetime.strptime("2021-09-01", time_format), 
                  datetime.strptime("2021-10-01", time_format),
                  datetime.strptime("2021-11-01", time_format)]


def split(df, training_split):
    
    validation_split = training_split + relativedelta(months=1)
    test_split = validation_split + relativedelta(months=1)
    
    train = df.loc[df['time'] < training_split]
    validation = df.loc[(df['time'] >= training_split) & (df['time'] < validation_split)]
    test = df.loc[(df['time'] >= validation_split) & (df['time'] < test_split)]
    
    return train, validation, test

def split_original_data(): 
    
    df = meteorological_df()
    
    folds_data = []
    
    for split_date in training_splits:
        
        train, validation, test = split(df, split_date)
        
        fold = {
            'train': train,
            'validation': validation, 
            'test': test
        }
        
        folds_data.append(fold)
    
    return folds_data

def split_consolidated_data():
    
    df = consolidated_df()
    
    folds_data = []
    
    for split_date in training_splits:
        
        train, validation, test = split(df, split_date)
        
        fold = {
            'train': train,
            'validation': validation, 
            'test': test
        }
        
        folds_data.append(fold)
    
    return folds_data
