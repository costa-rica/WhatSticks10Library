import os
import json
# from ws_config import ConfigLocal
# from .config import config
from .utilities import create_user_df, convert_to_user_tz, get_DateUserTz_3pm, \
    calculate_duration_in_hours
import pandas as pd
from ws_models import sess, inspect, engine, OuraSleepDescriptions, AppleHealthQuantityCategory
from datetime import datetime
import pytz


# Function to run to get table of sleep time
def create_df_daily_sleep(df):
    df_sleep = create_df_sleep(df)
    df_daily_sleep_table = create_aggregated_sleep_table(df_sleep)
    return df_daily_sleep_table

def create_df_sleep(df):
    df_sleep = df[df['sampleType']=='HKCategoryTypeIdentifierSleepAnalysis']
    # Apply the function to each row to create the new DateUserTz_3pm column
    df_sleep['DateUserTz_3pm'] = df_sleep.apply(get_DateUserTz_3pm, axis=1)
    return df_sleep

def create_aggregated_sleep_table(df_sleep):
    df_sleep_states_3_4_5 = df_sleep[df_sleep['value'].isin(["3.0", "4.0", "5.0"])]
    # Apply the function to each row in the dataframe
    df_sleep_states_3_4_5['sleepTimeFr'] = df_sleep_states_3_4_5.apply(lambda row: calculate_duration_in_hours(row['startDateUserTz'], row['endDateUserTz']), axis=1)
    # Now, let's aggregate by DateUserTz_3pm and sum the sleepTimeFr values
    aggregated_sleep_data = df_sleep_states_3_4_5.groupby('DateUserTz_3pm')['sleepTimeFr'].sum().reset_index()
    return aggregated_sleep_data

