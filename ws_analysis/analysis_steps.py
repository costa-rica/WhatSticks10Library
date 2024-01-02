from .utilities import create_user_df
import pandas as pd


def create_df_daily_steps(df):
    df_steps = df[df['sampleType']=='HKQuantityTypeIdentifierStepCount']
    df_steps['quantity'] = pd.to_numeric(df_steps['quantity'])
    aggregated_steps_data = df_steps.groupby('dateUserTz')['quantity'].sum().reset_index()
    aggregated_steps_data.rename(columns=({'quantity':'step_count'}),inplace=True)
    return aggregated_steps_data