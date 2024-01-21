import pandas as pd
from ws_models import engine
from datetime import datetime
import pytz
from .config import config
import os

def create_user_qty_cat_df(user_id, user_tz_str='Europe/Paris'):
    # Query data from database into pandas dataframe
    print("- in create_user_qty_cat_df -")
    pickle_apple_qty_cat_path_and_name = create_pickle_apple_qty_cat_path_and_name(user_id)
    if os.path.exists(pickle_apple_qty_cat_path_and_name):
        print(f"- reading pickle file for workouts: {pickle_apple_qty_cat_path_and_name} -")
        # df_existing_user_workouts_data=pd.read_pickle(pickle_apple_qty_cat_path_and_name)
        df=pd.read_pickle(pickle_apple_qty_cat_path_and_name)

    else:
        query = f"SELECT * FROM apple_health_quantity_category WHERE user_id = {user_id}"
        df = pd.read_sql_query(query, engine)
    try:
        # Applying the conversion to new columns
        df['startDateUserTz'] = df['startDate'].apply(lambda utc_str: convert_to_user_tz(utc_str, user_tz_str))
        df['endDateUserTz'] = df['endDate'].apply(lambda utc_str: convert_to_user_tz(utc_str, user_tz_str))
        # Extract just the date part from startDateUserTz
        df['dateUserTz'] = df['startDateUserTz'].dt.date
        list_of_user_data = list(df.sampleType.unique())
        return df, list_of_user_data
    except Exception as e:
        print("* User probably has NO Apple Quantity or Category Data *")
        print(f"An error occurred (in send_data_source_objects): {e}")
        return "insufficient data", "insufficient data"

def create_user_workouts_df(user_id, user_tz_str='Europe/Paris'):
    print("- in create_user_workouts_df -")
    # Query data from database into pandas dataframe
    # user_id=user_id
    pickle_apple_workouts_path_and_name = create_pickle_apple_workouts_path_and_name(user_id)
    if os.path.exists(pickle_apple_workouts_path_and_name):
        print(f"- reading pickle file for workouts: {pickle_apple_workouts_path_and_name} -")
        # df_existing_user_workouts_data=pd.read_pickle(pickle_apple_workouts_path_and_name)
        df=pd.read_pickle(pickle_apple_workouts_path_and_name)
    else:
        query = f"SELECT * FROM apple_health_workout WHERE user_id = {user_id}"
        df = pd.read_sql_query(query, engine)
    
    try:
        # Applying the conversion to new columns
        df['startDateUserTz'] = df['startDate'].apply(lambda utc_str: convert_to_user_tz(utc_str, user_tz_str))
        df['endDateUserTz'] = df['endDate'].apply(lambda utc_str: convert_to_user_tz(utc_str, user_tz_str))
        # Extract just the date part from startDateUserTz
        df['dateUserTz'] = df['startDateUserTz'].dt.date
        print(f"df has: {len(df)} records")
        list_of_user_data = list(df.sampleType.unique())
        print(f"list_of_user_data: {list_of_user_data}")
        return df, list_of_user_data
    except Exception as e:
        print("* User probably has NO Apple Workouts Data *")
        print(f"An error occurred (in send_data_source_objects): {e}")
        return "insufficient data", "insufficient data"
# paris = 'Europe/Paris'
# us east coast = 'America/New_York', 'US/Eastern'

# Function to convert date from UTC to Paris time
# def convert_to_paris_time(utc_str):
def convert_to_user_tz(utc_str, user_tz_str):
    utc_time = datetime.strptime(utc_str, '%Y-%m-%d %H:%M:%S %z')
    # paris_tz = pytz.timezone('Europe/Paris')
    user_tz = pytz.timezone(user_tz_str)
    user_time = utc_time.astimezone(user_tz)
    return user_time

# Function to determine the dateUserTz_3pm
def get_dateUserTz_3pm(row):
    print("- in get_dateUserTz_3pm(row) -")
    print(row)
    if row['startDateUserTz'].time() >= pd.Timestamp('15:00:00').time():
        print("- after 15:00:00")
        print(row['dateUserTz'])
        return row['dateUserTz']
    else:
        print("- before 15:00:00")
        print(row['dateUserTz'] - pd.Timedelta(days=1))
        return row['dateUserTz'] - pd.Timedelta(days=1)

# Function to calculate the duration in hours as a float
def calculate_duration_in_hours(start, end):
    duration = end - start
    hours = duration.total_seconds() / 3600
    return hours

def create_pickle_apple_qty_cat_path_and_name(user_id_str):
    # user's existing data in pickle dataframe
    user_apple_health_dataframe_pickle_file_name = f"user_{int(user_id_str):04}_apple_health_dataframe.pkl"

    #pickle filename and path
    pickle_apple_qty_cat_path_and_name = os.path.join(config.DATAFRAME_FILES_DIR, user_apple_health_dataframe_pickle_file_name)
    return pickle_apple_qty_cat_path_and_name

def create_pickle_apple_workouts_path_and_name(user_id_str):
    # user's existing data in pickle dataframe
    user_apple_workouts_dataframe_pickle_file_name = f"user_{int(user_id_str):04}_apple_workouts_dataframe.pkl"

    #pickle filename and path
    pickle_apple_workouts_path_and_name = os.path.join(config.DATAFRAME_FILES_DIR, user_apple_workouts_dataframe_pickle_file_name)
    return pickle_apple_workouts_path_and_name