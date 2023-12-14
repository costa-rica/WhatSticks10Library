import pandas as pd
from ws_models import engine
from datetime import datetime
import pytz


def create_user_df(user_id):
    # Query data from database into pandas dataframe
    user_id=user_id
    query = f"SELECT * FROM apple_health_kit WHERE user_id = {user_id}"
    df = pd.read_sql_query(query, engine)
    # Applying the conversion to new columns
    df['startDateFr'] = df['startDate'].apply(convert_to_paris_time)
    df['endDateFr'] = df['endDate'].apply(convert_to_paris_time)
    # Extract just the date part from startDateFr
    df['dateFr'] = df['startDateFr'].dt.date
    list_of_user_data = list(df.sampleType.unique())
    return df, list_of_user_data

# Function to convert date from UTC to Paris time
def convert_to_paris_time(utc_str):
    utc_time = datetime.strptime(utc_str, '%Y-%m-%d %H:%M:%S %z')
    paris_tz = pytz.timezone('Europe/Paris')
    paris_time = utc_time.astimezone(paris_tz)
    return paris_time

# Function to determine the dateFr_3pm
def get_dateFr_3pm(row):
    if row['startDateFr'].time() >= pd.Timestamp('15:00:00').time():
        return row['dateFr']
    else:
        return row['dateFr'] - pd.Timedelta(days=1)

# Function to calculate the duration in hours as a float
def calculate_duration_in_hours(start, end):
    duration = end - start
    hours = duration.total_seconds() / 3600
    return hours
