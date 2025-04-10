import pandas as pd 
import numpy as np

def linear_weighted_moving_average(window_series, k):
    center_index_in_window = k
    weighted_sum = 0.0
    sum_of_weights = 0.0 
    
    for i in range(len(window_series)):
        if (i == center_index_in_window):
            continue
        value = window_series.iloc[i]
        
        if not pd.isna(value):
            distance = abs (i - center_index_in_window)
            if (distance > 0):
                weight = 1.0 / distance 
                weighted_sum += weight * value 
                sum_of_weights += weight 
    
    if (sum_of_weights == 0):
        return np.nan 
    
    return weighted_sum / sum_of_weights

def lwmv_imputation(df: pd.DataFrame, factors: list, k = 3):
    
    window_size = 2 * k + 1
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by=['ID', 'date'])
    
    for factor in factors:
        lswm_series = df[factor].rolling(
            window=window_size,
            center=True,
            min_periods=1,
        ).apply(lambda x: linear_weighted_moving_average(x, k), raw=False)
        
        df[factor] = df[factor].fillna(lswm_series)
    
    return df