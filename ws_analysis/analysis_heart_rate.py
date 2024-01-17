from .utilities import create_user_qty_cat_df
import pandas as pd
from datetime import datetime, timedelta

def create_df_daily_heart_rate(df):
    df_heart_rate = df[df.sampleType == 'HKQuantityTypeIdentifierHeartRate']
    # df_steps['quantity'] = pd.to_numeric(df_steps['quantity'])
    df_heart_rate['quantity'] = df_heart_rate['quantity'].astype('float')
    aggregated_heart_rate_data = df_heart_rate.groupby('dateUserTz')['quantity'].mean().reset_index()
    aggregated_heart_rate_data.rename(columns=({'quantity':'heart_rate_avg'}),inplace=True)
    return aggregated_heart_rate_data


def create_df_n_minus1_daily_heart_rate(df_daily_heart_rate):
    # df_daily_steps['dateUserTz'] = pd.to_datetime(df_daily_steps['dateUserTz'])
    df_daily_heart_rate['dateUserTz'] = pd.to_datetime(df_daily_heart_rate['dateUserTz'])
    # Subtract one day from each date in the column
    df_daily_heart_rate['dateUserTz'] = df_daily_heart_rate['dateUserTz'] - timedelta(days=1)
    # Convert back to 'YYYY-MM-DD' format if needed
    df_daily_heart_rate['dateUserTz'] = df_daily_heart_rate['dateUserTz'].dt.strftime('%Y-%m-%d')

    return df_daily_heart_rate
