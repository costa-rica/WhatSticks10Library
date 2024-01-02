import pandas as pd
from ws_models import engine
from datetime import datetime
import pytz


def create_user_qty_cat_df(user_id, user_tz_str='Europe/Paris'):
    # Query data from database into pandas dataframe
    user_id=user_id
    query = f"SELECT * FROM apple_health_quantity_category WHERE user_id = {user_id}"
    df = pd.read_sql_query(query, engine)
    # Applying the conversion to new columns
    df['startDateUserTz'] = df['startDate'].apply(lambda utc_str: convert_to_user_tz(utc_str, user_tz_str))
    df['endDateUserTz'] = df['endDate'].apply(lambda utc_str: convert_to_user_tz(utc_str, user_tz_str))
    # Extract just the date part from startDateUserTz
    df['dateUserTz'] = df['startDateUserTz'].dt.date
    list_of_user_data = list(df.sampleType.unique())
    return df, list_of_user_data

def create_user_workouts_df(user_id, user_tz_str='Europe/Paris'):
    # Query data from database into pandas dataframe
    user_id=user_id
    query = f"SELECT * FROM apple_health_workout WHERE user_id = {user_id}"
    df = pd.read_sql_query(query, engine)
    # Applying the conversion to new columns
    df['startDateUserTz'] = df['startDate'].apply(lambda utc_str: convert_to_user_tz(utc_str, user_tz_str))
    df['endDateUserTz'] = df['endDate'].apply(lambda utc_str: convert_to_user_tz(utc_str, user_tz_str))
    # Extract just the date part from startDateUserTz
    df['dateUserTz'] = df['startDateUserTz'].dt.date
    list_of_user_data = list(df.sampleType.unique())
    return df, list_of_user_data

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
    if row['startDateUserTz'].time() >= pd.Timestamp('15:00:00').time():
        return row['dateUserTz']
    else:
        return row['dateUserTz'] - pd.Timedelta(days=1)

# Function to calculate the duration in hours as a float
def calculate_duration_in_hours(start, end):
    duration = end - start
    hours = duration.total_seconds() / 3600
    return hours
