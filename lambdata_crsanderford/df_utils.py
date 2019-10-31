# DataFrame utility functions

import pandas as pd
import numpy as np

def list_to_column(a_list, column_name, df):
    ''' takes a list, a dataframe, and a name, and converts the list to a column
        in the dataframe with said name. '''
    df = df.copy()
    a_series = pd.Series(a_list)
    df[column_name] = a_series
    return df

def datesplit(df, date_column):
    ''' takes a dataframe and the name of a date column in the dataframe.
        returns the dataframe with year, month, and day columns. '''
    df = df.copy()
    df[date_column] = pd.to_datetime(df[date_column], infer_datetime_format=True)

    df[date_column+'_YEAR'] = df[date_column].dt.year
    df[date_column+'_MONTH'] = df[date_column].dt.month
    df[date_column+'_DAY'] = df[date_column].dt.day
    return df