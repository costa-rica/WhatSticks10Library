from .utilities import create_user_df
import pandas as pd


def create_df_daily_heart_rate(df):
    df_heart_rate = df[df.sampleType == 'HKQuantityTypeIdentifierHeartRate']
    # df_steps['quantity'] = pd.to_numeric(df_steps['quantity'])
    df_heart_rate['quantity'] = df_heart_rate['quantity'].astype('float')
    aggregated_heart_rate_data = df_heart_rate.groupby('dateFr')['quantity'].mean().reset_index()
    aggregated_heart_rate_data.rename(columns=({'quantity':'heart_rate_avg'}),inplace=True)
    return aggregated_heart_rate_data