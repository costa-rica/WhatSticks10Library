from .utilities import create_user_qty_cat_df
import pandas as pd
from datetime import datetime, timedelta

def create_df_daily_steps(df):
    df_steps = df[df['sampleType']=='HKQuantityTypeIdentifierStepCount']
    if len(df_steps) == 0:
        return pd.DataFrame()#<-- return must return dataframe, expecting df on other end
    df_steps['quantity'] = pd.to_numeric(df_steps['quantity'])
    aggregated_steps_data = df_steps.groupby('dateUserTz')['quantity'].sum().reset_index()
    aggregated_steps_data.rename(columns=({'quantity':'step_count'}),inplace=True)
    return aggregated_steps_data


def create_df_n_minus1_daily_steps(df_daily_steps):
    df_daily_steps['dateUserTz'] = pd.to_datetime(df_daily_steps['dateUserTz'])
    # Subtract one day from each date in the column
    df_daily_steps['dateUserTz'] = df_daily_steps['dateUserTz'] - timedelta(days=1)
    # Convert back to 'YYYY-MM-DD' format if needed
    df_daily_steps['dateUserTz'] = df_daily_steps['dateUserTz'].dt.strftime('%Y-%m-%d')

    return df_daily_steps