import pandas as pd
from .analysis_sleep import create_df_daily_sleep
from .utilities import create_user_df
from .analysis_steps import create_df_daily_steps
from .analysis_heart_rate import create_df_daily_heart_rate


def user_correlations(user_id):
    print("- in user_correlations ")
    df, list_of_user_data = create_user_df(user_id=user_id)
    list_of_arryIndepVarObjects_dict = []
    if 'HKCategoryTypeIdentifierSleepAnalysis' in list_of_user_data:
        arryIndepVarObjects_dict = {}
        # corr_sleep_steps(df)
        arryIndepVarObjects_dict["name"]= "Step Count"
        arryIndepVarObjects_dict["depVarName"]= "Sleep Time"
        arryIndepVarObjects_dict["correlationValue"]= corr_sleep_steps(df)
        list_of_arryIndepVarObjects_dict.append(arryIndepVarObjects_dict)

    if 'HKQuantityTypeIdentifierHeartRate' in list_of_user_data:
        arryIndepVarObjects_dict = {}
        # corr_sleep_heart_rate(df)
        arryIndepVarObjects_dict["name"]= "Heart Rate Avg"
        arryIndepVarObjects_dict["depVarName"]= "Sleep Time"
        arryIndepVarObjects_dict["correlationValue"]= corr_sleep_heart_rate(df)
        list_of_arryIndepVarObjects_dict.append(arryIndepVarObjects_dict)
    
    return list_of_arryIndepVarObjects_dict

def corr_sleep_steps(df):
    print("- in corr_sleep_steps")
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
            # print(f"correlation: {correlation}, corr type: {correlation}")
            print(f"df_daily_sleep_steps correlation: {correlation}, corr type: {type(correlation)}")
            return correlation
        else:
            return "insufficient data"
    except Exception as e:
        print(f"error in corr_sleep_steps: {e}")
        return "insufficient data"

def corr_sleep_heart_rate(df):
    print("- in corr_sleep_heart_rate")
    # df, list_of_user_data = create_user_df(user_id=user_id)
    # if 'HKCategoryTypeIdentifierSleepAnalysis' in list_of_user_data:
    df_daily_sleep = create_df_daily_sleep(df)
    df_daily_sleep.rename(columns=({'dateFr_3pm':'dateFr'}),inplace=True)

    # if 'HKCategoryTypeIdentifierSleepAnalysis' in list_of_user_data:
    df_daily_heart_rate = create_df_daily_heart_rate(df)
    print(f"- df_daily_heart_rate -")
    print(f"counte of df_daily_heart_rate: {len(df_daily_heart_rate)}")
    print(df_daily_heart_rate.head(2))
    try:
        print("- try corr_sleep_heart_rate")
        if len(df_daily_heart_rate) > 5:# arbitrary minimum
            print("- if len(df_daily_heart_rate) > 5")

            # This will keep only the rows that have matching 'dateFr' values in both dataframes
            df_daily_sleep_heart_rate = pd.merge(df_daily_sleep,df_daily_heart_rate, on='dateFr')

            # Calculate the correlation between step_count and sleepTimeFr
            correlation = df_daily_sleep_heart_rate['heart_rate_avg'].corr(df_daily_sleep_heart_rate['sleepTimeFr'])
            print(f"df_daily_sleep_heart_rate correlation: {correlation}, corr type: {type(correlation)}")
            return correlation
        else:
            return "insufficient data"
    except Exception as e:
        print(f"error in corr_sleep_heart_rate: {e}")
        return "insufficient data"