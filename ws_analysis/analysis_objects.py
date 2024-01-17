import pandas as pd;import numpy as np
from .config import config
import os
from .utilities import create_user_qty_cat_df
from .analysis_sleep import create_df_daily_sleep, \
    create_df_n_minus1_daily_sleep
from .analysis_steps import create_df_daily_steps, \
    create_df_n_minus1_daily_steps
from .analysis_heart_rate import create_df_daily_heart_rate, \
    create_df_n_minus1_daily_heart_rate
from .analysis_workouts import create_df_daily_workout_duration, \
    create_df_daily_workout_duration_dummies


def corr_sleep_steps(df):
    print("- in corr_sleep_steps")
    user_id = df['user_id'].iloc[0]
    # df, list_of_user_data = create_user_qty_cat_df(user_id=user_id)
    # if 'HKCategoryTypeIdentifierSleepAnalysis' in list_of_user_data:
    print("-- df ---")
    print(df.columns)
    print(df.head(2))

    df_daily_sleep = create_df_daily_sleep(df)
    df_daily_sleep.rename(columns=({'dateUserTz_3pm':'dateUserTz'}),inplace=True)

    # if 'HKCategoryTypeIdentifierSleepAnalysis' in list_of_user_data:
    df_daily_steps = create_df_daily_steps(df)
    try:
        if len(df_daily_steps) > 5:# arbitrary minimum

            # This will keep only the rows that have matching 'dateUserTz' values in both dataframes
            df_daily_sleep_steps = pd.merge(df_daily_sleep,df_daily_steps, on='dateUserTz')
            # save csv file for user
            csv_path_and_filename = os.path.join(config.DAILY_CSV, f"user_{user_id:04}_df_daily_sleep_steps.csv")
            df_daily_sleep_steps.to_csv(csv_path_and_filename)
            # Calculate the correlation between step_count and sleepTimeUserTz
            correlation = df_daily_sleep_steps['step_count'].corr(df_daily_sleep_steps['sleepTimeUserTz'])
            obs_count = len(df_daily_sleep_steps)
            # print(f"correlation: {correlation}, corr type: {correlation}")
            print(f"df_daily_sleep_steps correlation: {correlation}, corr type: {type(correlation)}")
            return correlation, obs_count
        else:
            return "insufficient data", "insufficient data"
    except Exception as e:
        print(f"error in corr_sleep_steps: {e}")
        return "insufficient data", "insufficient data"

def corr_sleep_heart_rate(df):
    print("- in corr_sleep_heart_rate")
    user_id = df['user_id'].iloc[0]

    df_daily_sleep = create_df_daily_sleep(df)
    df_daily_sleep.rename(columns=({'dateUserTz_3pm':'dateUserTz'}),inplace=True)

    df_daily_heart_rate = create_df_daily_heart_rate(df)

    try:
        print("- try corr_sleep_heart_rate")
        if len(df_daily_heart_rate) > 5:# arbitrary minimum
            print("- if len(df_daily_heart_rate) > 5")

            # This will keep only the rows that have matching 'dateUserTz' values in both dataframes
            df_daily_sleep_heart_rate = pd.merge(df_daily_sleep,df_daily_heart_rate, on='dateUserTz')

            # save csv file for user
            csv_path_and_filename = os.path.join(config.DAILY_CSV, f"user_{user_id:04}_df_daily_sleep_heart_rate.csv")
            df_daily_sleep_heart_rate.to_csv(csv_path_and_filename)

            # Calculate the correlation between step_count and sleepTimeUserTz
            correlation = df_daily_sleep_heart_rate['heart_rate_avg'].corr(df_daily_sleep_heart_rate['sleepTimeUserTz'])
            obs_count = len(df_daily_sleep_heart_rate)
            print(f"df_daily_sleep_heart_rate correlation: {correlation}, corr type: {type(correlation)}")
            return correlation, obs_count
        else:
            return "insufficient data", "insufficient data"
    except Exception as e:
        print(f"error in corr_sleep_heart_rate: {e}")
        return "insufficient data", "insufficient data"

def corr_sleep_workouts(df_qty_cat, df_workouts):

    print("- in corr_sleep_workouts")
    user_id = df_qty_cat['user_id'].iloc[0]
    df_daily_sleep = create_df_daily_sleep(df_qty_cat)
    df_daily_sleep.rename(columns=({'dateUserTz_3pm':'dateUserTz'}),inplace=True)

    df_daily_workout_duration = create_df_daily_workout_duration(df_workouts)
    # df_daily_workout_duration_csv_path_and_filename = os.path.join(config.DAILY_CSV, f"user_{user_id:04}_df_daily_workout_duration.csv")
    # df_daily_workout_duration.to_csv(df_daily_workout_duration_csv_path_and_filename)
    try:
        if len(df_daily_workout_duration) > 5:# arbitrary minimum

            # This will keep only the rows that have matching 'dateUserTz' values in both dataframes
            df_daily_sleep_workout_duration = pd.merge(df_daily_sleep,df_daily_workout_duration, on='dateUserTz')
            # # save csv file for user
            # csv_path_and_filename = os.path.join(config.DAILY_CSV, f"user_{user_id:04}_df_daily_sleep_workout_duration.csv")
            # df_daily_sleep_workout_duration.to_csv(csv_path_and_filename)
            # Calculate the correlation between step_count and sleepTimeUserTz
            correlation = df_daily_sleep_workout_duration['duration'].corr(df_daily_sleep_workout_duration['sleepTimeUserTz'])
            obs_count = len(df_daily_sleep_workout_duration)
            # print(f"correlation: {correlation}, corr type: {correlation}")
            print(f"df_daily_sleep_workout_duration correlation: {correlation}, corr type: {type(correlation)}")
            return correlation, obs_count
        else:
            return "insufficient data", "insufficient data"
    except Exception as e:
        print(f"error in corr_sleep_workouts: {e}")
        return "insufficient data", "insufficient data"

def corr_sleep_workout_dummies(df_qty_cat, df_workouts):

    print("- in corr_sleep_workout_dummies")
    user_id = df_qty_cat['user_id'].iloc[0]
    df_daily_sleep = create_df_daily_sleep(df_qty_cat)
    df_daily_sleep.rename(columns=({'dateUserTz_3pm':'dateUserTz'}),inplace=True)

    df_daily_workout_duration_dummies = create_df_daily_workout_duration_dummies(df_workouts)
    try:
        if len(df_daily_workout_duration_dummies) > 5:# arbitrary minimum
            # This will keep only the rows that have matching 'dateUserTz' values in both dataframes
            df_daily_sleep_workout_duration = pd.merge(df_daily_sleep,df_daily_workout_duration_dummies, on='dateUserTz')
            # save csv file for user
            csv_path_and_filename = os.path.join(config.DAILY_CSV, f"user_{user_id:04}_df_daily_sleep_workout_duration_dummies.csv")
            df_daily_sleep_workout_duration.to_csv(csv_path_and_filename)

            # List to store the tuples of column name and correlation
            col_names_and_correlations_tuple_list = []

            # Iterate over the columns to calculate correlation
            for col in df_daily_sleep_workout_duration.columns:
                if col.startswith('dur_') and col.endswith('_dummy'):
                    # Calculate the correlation
                    corr_value = df_daily_sleep_workout_duration['sleepTimeUserTz'].corr(df_daily_sleep_workout_duration[col])
                    
                    # Append the tuple (column name, correlation value) to the list
                    col_names_and_correlations_tuple_list.append((col, corr_value))

            obs_count = len(df_daily_sleep_workout_duration)

            return col_names_and_correlations_tuple_list, obs_count
        else:
            return "insufficient data", "insufficient data"
    except Exception as e:
        print(f"error in corr_sleep_workouts: {e}")
        return "insufficient data", "insufficient data"



#######################################
## Daily Workouts Dependent Variable ##
#######################################


def corr_workouts_sleep(df_workouts, df_qty_cat):

    print("- in corr_workouts_sleep")
    user_id = df_qty_cat['user_id'].iloc[0]
    df_daily_sleep = create_df_daily_sleep(df_qty_cat)# create daily sleep
    df_daily_sleep.rename(columns=({'dateUserTz_3pm':'dateUserTz'}),inplace=True)

    print("-------- df_daily_sleep ------")
    print(df_daily_sleep.dtypes)
    print(len(df_daily_sleep))

    df_n_minus1_daily_sleep = create_df_n_minus1_daily_sleep(df_daily_sleep)
    df_n_minus1_daily_sleep['dateUserTz']=pd.to_datetime(df_n_minus1_daily_sleep['dateUserTz'])

    print("-------- df_n_minus1_daily_sleep ------")
    print(df_n_minus1_daily_sleep.dtypes)
    print(len(df_n_minus1_daily_sleep))
    csv_path_and_filename = os.path.join(config.DAILY_CSV, f"user_{user_id:04}_df_n_minus1_daily_sleep.csv")
    df_n_minus1_daily_sleep.to_csv(csv_path_and_filename)


    df_daily_workout_duration = create_df_daily_workout_duration(df_workouts)
    df_daily_workout_duration['dateUserTz']=pd.to_datetime(df_daily_workout_duration['dateUserTz'])

    print("-------- df_daily_workout_duration ------")
    print(df_daily_workout_duration.dtypes)
    print(len(df_daily_workout_duration))
    csv_path_and_filename = os.path.join(config.DAILY_CSV, f"user_{user_id:04}_df_daily_workout_duration.csv")
    df_daily_workout_duration.to_csv(csv_path_and_filename)

    try:
        if len(df_daily_workout_duration) > 5:# arbitrary minimum

            # This will keep only the rows that have matching 'dateUserTz' values in both dataframes
            df_daily_workout_duration_sleep_n_minus1 = pd.merge(df_n_minus1_daily_sleep,df_daily_workout_duration, on='dateUserTz')
            df_daily_workout_duration_sleep_n_minus1['dateUserTz'] = df_daily_workout_duration_sleep_n_minus1['dateUserTz'].dt.strftime('%Y-%m-%d')
            # save csv file for user
            csv_path_and_filename = os.path.join(config.DAILY_CSV, f"user_{user_id:04}_df_daily_workout_sleep_n_minus1.csv")
            df_daily_workout_duration_sleep_n_minus1.to_csv(csv_path_and_filename)
            # Calculate the correlation between step_count and sleepTimeUserTz
            correlation = df_daily_workout_duration_sleep_n_minus1['duration'].corr(df_daily_workout_duration_sleep_n_minus1['sleepTimeUserTz'])
            obs_count = len(df_daily_workout_duration_sleep_n_minus1)
            # print(f"correlation: {correlation}, corr type: {correlation}")
            print(f"df_daily_workout_duration_sleep_n_minus1 correlation: {correlation}, corr type: {type(correlation)}")
            return correlation, obs_count
        else:
            return "insufficient data", "insufficient data"
    except Exception as e:
        print(f"error in corr_workouts_sleep: {e}")
        return "insufficient data", "insufficient data"


def corr_workouts_steps(df_workouts, df_qty_cat):

    print("- in corr_workouts_steps")
    user_id = df_qty_cat['user_id'].iloc[0]
    # df_daily_sleep = create_df_daily_sleep(df_qty_cat)# create daily sleep
    df_daily_steps = create_df_daily_steps(df_qty_cat)# create daily steps

    # df_n_minus1_daily_sleep = create_df_n_minus1_daily_sleep(df_daily_sleep)
    df_n_minus1_daily_steps = create_df_n_minus1_daily_steps(df_daily_steps)
    df_n_minus1_daily_steps['dateUserTz']=pd.to_datetime(df_n_minus1_daily_steps['dateUserTz'])

    csv_path_and_filename = os.path.join(config.DAILY_CSV, f"user_{user_id:04}_df_n_minus1_daily_steps.csv")
    df_n_minus1_daily_steps.to_csv(csv_path_and_filename)

    df_daily_workout_duration = create_df_daily_workout_duration(df_workouts)
    df_daily_workout_duration['dateUserTz']=pd.to_datetime(df_daily_workout_duration['dateUserTz'])

    csv_path_and_filename = os.path.join(config.DAILY_CSV, f"user_{user_id:04}_df_daily_workout_duration.csv")
    df_daily_workout_duration.to_csv(csv_path_and_filename)

    try:
        if len(df_daily_workout_duration) > 5:# arbitrary minimum

            # This will keep only the rows that have matching 'dateUserTz' values in both dataframes
            # df_daily_workout_duration_sleep_n_minus1 = pd.merge(df_n_minus1_daily_sleep,df_daily_workout_duration, on='dateUserTz')
            df_daily_workout_duration_steps_n_minus1 = pd.merge(df_n_minus1_daily_steps,df_daily_workout_duration, on='dateUserTz')
            df_daily_workout_duration_steps_n_minus1['dateUserTz'] = df_daily_workout_duration_steps_n_minus1['dateUserTz'].dt.strftime('%Y-%m-%d')
            # save csv file for user
            csv_path_and_filename = os.path.join(config.DAILY_CSV, f"user_{user_id:04}_df_daily_workout_steps_n_minus1.csv")
            df_daily_workout_duration_steps_n_minus1.to_csv(csv_path_and_filename)
            print("--- df_daily_workout_duration_steps_n_minus1 ----")
            print(df_daily_workout_duration_steps_n_minus1.columns)
            print(df_daily_workout_duration_steps_n_minus1.head(2))
            # Calculate the correlation between step_count and sleepTimeUserTz
            # correlation = df_daily_workout_duration_sleep_n_minus1['duration'].corr(df_daily_workout_duration_sleep_n_minus1['sleepTimeUserTz'])
            correlation = df_daily_workout_duration_steps_n_minus1['duration'].corr(df_daily_workout_duration_steps_n_minus1['step_count'])
            obs_count = len(df_daily_workout_duration_steps_n_minus1)
            # print(f"correlation: {correlation}, corr type: {correlation}")
            print(f"df_daily_workout_duration_steps_n_minus1 correlation: {correlation}, corr type: {type(correlation)}")
            return correlation, obs_count
        else:
            return "insufficient data", "insufficient data"
    except Exception as e:
        print(f"error in corr_workouts_sleep: {e}")
        return "insufficient data", "insufficient data"


def corr_workouts_heart_rate(df_workouts, df_qty_cat):

    print("- in corr_workouts_heart_rate")
    user_id = df_qty_cat['user_id'].iloc[0]
    # df_daily_steps = create_df_daily_steps(df_qty_cat)# create daily steps
    df_daily_heart_rate = create_df_daily_heart_rate(df_qty_cat)# create daily steps

    # df_n_minus1_daily_steps = create_df_n_minus1_daily_steps(df_daily_steps)
    df_n_minus1_daily_heart_rate = create_df_n_minus1_daily_heart_rate(df_daily_heart_rate)
    df_n_minus1_daily_heart_rate['dateUserTz']=pd.to_datetime(df_n_minus1_daily_heart_rate['dateUserTz'])

    csv_path_and_filename = os.path.join(config.DAILY_CSV, f"user_{user_id:04}_df_n_minus1_daily_heart_rate.csv")
    df_n_minus1_daily_heart_rate.to_csv(csv_path_and_filename)

    df_daily_workout_duration = create_df_daily_workout_duration(df_workouts)
    df_daily_workout_duration['dateUserTz']=pd.to_datetime(df_daily_workout_duration['dateUserTz'])

    csv_path_and_filename = os.path.join(config.DAILY_CSV, f"user_{user_id:04}_df_daily_workout_duration.csv")
    df_daily_workout_duration.to_csv(csv_path_and_filename)

    try:
        if len(df_daily_workout_duration) > 5:# arbitrary minimum

            # This will keep only the rows that have matching 'dateUserTz' values in both dataframes
            # df_daily_workout_duration_steps_n_minus1 = pd.merge(df_n_minus1_daily_steps,df_daily_workout_duration, on='dateUserTz')
            df_daily_workout_duration_heart_rate_n_minus1 = pd.merge(df_n_minus1_daily_heart_rate,df_daily_workout_duration, on='dateUserTz')
            df_daily_workout_duration_heart_rate_n_minus1['dateUserTz'] = df_daily_workout_duration_heart_rate_n_minus1['dateUserTz'].dt.strftime('%Y-%m-%d')
            # save csv file for user
            csv_path_and_filename = os.path.join(config.DAILY_CSV, f"user_{user_id:04}_df_daily_workout_duration_heart_rate_n_minus1.csv")
            df_daily_workout_duration_heart_rate_n_minus1.to_csv(csv_path_and_filename)
            # print("--- df_daily_workout_duration_steps_n_minus1 ----")
            # print(df_daily_workout_duration_steps_n_minus1.columns)
            # print(df_daily_workout_duration_steps_n_minus1.head(2))
            # Calculate the correlation between step_count and sleepTimeUserTz
            # correlation = df_daily_workout_duration_sleep_n_minus1['duration'].corr(df_daily_workout_duration_sleep_n_minus1['sleepTimeUserTz'])
            correlation = df_daily_workout_duration_heart_rate_n_minus1['duration'].corr(df_daily_workout_duration_heart_rate_n_minus1['heart_rate_avg'])
            obs_count = len(df_daily_workout_duration_heart_rate_n_minus1)
            # print(f"correlation: {correlation}, corr type: {correlation}")
            print(f"df_daily_workout_duration_heart_rate_n_minus1 correlation: {correlation}, corr type: {type(correlation)}")
            return correlation, obs_count
        else:
            return "insufficient data", "insufficient data"
    except Exception as e:
        print(f"error in corr_workouts_sleep: {e}")
        return "insufficient data", "insufficient data"



