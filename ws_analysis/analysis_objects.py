import pandas as pd
from .analysis_sleep import create_df_daily_sleep
from .utilities import create_user_df
from .analysis_steps import create_df_daily_steps

def corr_sleep_steps(user_id):
    df, list_of_user_data = create_user_df(user_id=user_id)
    if 'HKCategoryTypeIdentifierSleepAnalysis' in list_of_user_data:
        df_daily_sleep = create_df_daily_sleep(df)
        df_daily_sleep.rename(columns=({'dateFr_3pm':'dateFr'}),inplace=True)

        if 'HKCategoryTypeIdentifierSleepAnalysis' in list_of_user_data:
            df_daily_steps = create_df_daily_steps(df)

            # This will keep only the rows that have matching 'dateFr' values in both dataframes
            df_daily_sleep_steps = pd.merge(df_daily_sleep,df_daily_steps, on='dateFr')

            # Calculate the correlation between step_count and sleepTimeFr
            correlation = df_daily_sleep_steps['step_count'].corr(df_daily_sleep_steps['sleepTimeFr'])
            return correlation
    
    return "insufficient data"

