from .utilities import create_user_workouts_df
import pandas as pd


def create_df_daily_workout_duration(df):
    # df_steps = df[df['sampleType']=='HKQuantityTypeIdentifierStepCount']
    df['duration'] = pd.to_numeric(df['duration'])
    aggregated_workout_durations = df.groupby('dateUserTz')['duration'].sum().reset_index()
    # aggregated_workout_durations.rename(columns=({'duration':'step_count'}),inplace=True)
    return aggregated_workout_durations