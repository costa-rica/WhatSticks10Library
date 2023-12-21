import pandas as pd
from .analysis_sleep import create_df_daily_sleep
from .utilities import create_user_df
from .analysis_steps import create_df_daily_steps
from .analysis_heart_rate import create_df_daily_heart_rate


def user_correlations(user_id):
    print("*** in user_correlations ***")
    df, list_of_user_data = create_user_df(user_id=user_id)
    list_of_correlations_dict = []
    if 'HKCategoryTypeIdentifierSleepAnalysis' in list_of_user_data:
        correlations_dict = {}
        # corr_sleep_steps(df)
        correlations_dict["name"]= "Step Count"
        correlations_dict["depVarName"]= "Sleep Time"
        correlations_dict["correlationValue"]= corr_sleep_steps(df)
        list_of_correlations_dict.append(correlations_dict)

    if 'HKQuantityTypeIdentifierHeartRate' in list_of_user_data:
        correlations_dict = {}
        # corr_sleep_heart_rate(df)
        correlations_dict["name"]= "Heart Rate Avg"
        correlations_dict["depVarName"]= "Sleep Time"
        correlations_dict["correlationValue"]= corr_sleep_heart_rate(df)
        list_of_correlations_dict.append(correlations_dict)
    
    return list_of_correlations_dict

def corr_sleep_steps(df):
    print("*** in corr_sleep_steps ***")
    # df, list_of_user_data = create_user_df(user_id=user_id)
    # if 'HKCategoryTypeIdentifierSleepAnalysis' in list_of_user_data:
    df_daily_sleep = create_df_daily_sleep(df)
    df_daily_sleep.rename(columns=({'dateFr_3pm':'dateFr'}),inplace=True)

    # if 'HKCategoryTypeIdentifierSleepAnalysis' in list_of_user_data:
    df_daily_steps = create_df_daily_steps(df)
    try:
        if len(df_daily_steps) > 5:# arbitrary minimum

            # This will keep only the rows that have matching 'dateFr' values in both dataframes
            df_daily_sleep_steps = pd.merge(df_daily_sleep,df_daily_steps, on='dateFr')

            # Calculate the correlation between step_count and sleepTimeFr
            correlation = df_daily_sleep_steps['step_count'].corr(df_daily_sleep_steps['sleepTimeFr'])
            print(f"correlation: {correlation}, corr type: {type(correlation)}")
            return correlation
        else:
            return "insufficient data"
    except:
        return "insufficient data"

def corr_sleep_heart_rate(df):
    print("*** in corr_sleep_heart_rate ***")
    # df, list_of_user_data = create_user_df(user_id=user_id)
    # if 'HKCategoryTypeIdentifierSleepAnalysis' in list_of_user_data:
    df_daily_sleep = create_df_daily_sleep(df)
    df_daily_sleep.rename(columns=({'dateFr_3pm':'dateFr'}),inplace=True)

    # if 'HKCategoryTypeIdentifierSleepAnalysis' in list_of_user_data:
    df_daily_heart_rate = create_df_daily_heart_rate(df)
    try:
        if len(df_daily_heart_rate) > 5:# arbitrary minimum
            
            # This will keep only the rows that have matching 'dateFr' values in both dataframes
            df_daily_sleep_steps = pd.merge(df_daily_sleep,df_daily_steps, on='dateFr')

            # Calculate the correlation between step_count and sleepTimeFr
            correlation = df_daily_sleep_steps['step_count'].corr(df_daily_sleep_steps['sleepTimeFr'])
            print(f"correlation: {correlation}, corr type: {type(correlation)}")
            return correlation
        else:
            return "insufficient data"
    except:
        return "insufficient data"