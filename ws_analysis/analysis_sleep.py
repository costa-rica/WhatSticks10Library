import os
import json
# from ws_config import ConfigLocal
# from .config import config
from .utilities import create_user_qty_cat_df, convert_to_user_tz, get_dateUserTz_3pm, \
    calculate_duration_in_hours
import pandas as pd
from ws_models import sess, inspect, engine, OuraSleepDescriptions, AppleHealthQuantityCategory
from datetime import datetime
import pytz


# Function to run to get table of sleep time
def create_df_daily_sleep(df):
    # df_sleep = create_df_sleep(df)
    print("- in create_df_daily_sleep")
    # print("- df -")
    # print(df.columns)
    # print(f"lengath df: {len(df)}")
    # print(" ------- ")

    df_sleep = df[df['sampleType']=='HKCategoryTypeIdentifierSleepAnalysis']
    # print("- df_sleep -")
    # print(df_sleep.columns)
    # print(f"lengath df_sleep: {len(df_sleep)}")
    # print(" ------- ")
    # Apply the function to each row to create the new dateUserTz_3pm column
    df_sleep['dateUserTz_3pm'] = df_sleep.apply(get_dateUserTz_3pm, axis=1)


    # df_daily_sleep_table = create_aggregated_sleep_table(df_sleep)

    df_sleep_states_3_4_5 = df_sleep[df_sleep['value'].isin(["3.0", "4.0", "5.0"])]
    # Apply the function to each row in the dataframe
    df_sleep_states_3_4_5['sleepTimeUserTz'] = df_sleep_states_3_4_5.apply(lambda row: calculate_duration_in_hours(row['startDateUserTz'], row['endDateUserTz']), axis=1)
    # Now, let's aggregate by dateUserTz_3pm and sum the sleepTimeUserTz values
    aggregated_sleep_data = df_sleep_states_3_4_5.groupby('dateUserTz_3pm')['sleepTimeUserTz'].sum().reset_index()

    # print("- df_sleep_states_3_4_5 -")
    # print(df_sleep_states_3_4_5.columns)
    # print(f"lengath df_sleep_states_3_4_5: {len(df_sleep_states_3_4_5)}")
    # print(" ------- ")


    return aggregated_sleep_data

