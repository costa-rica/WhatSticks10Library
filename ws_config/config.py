import os
import json
from dotenv import load_dotenv

load_dotenv()
print("- reading dd07modules/pw_config/config.py")
print(f"- FLASK_CONFIG_TYPE: {os.environ.get('FLASK_CONFIG_TYPE')}")
print(f"- FLASK_DEBUG: {os.environ.get('FLASK_DEBUG')}")
print(f"- Config File: {os.path.join(os.environ.get('CONFIG_PATH_LOCAL'), os.environ.get('CONFIG_FILE_NAME'))}")
print(f"- DB: sqlite:///{os.environ.get('DB_ROOT')}{os.environ.get('DB_NAME_WHAT_STICKS')}")

match os.environ.get('FLASK_CONFIG_TYPE'):
    # case 'dev' | 'prod':
    #     with open(os.path.join(os.environ.get('CONFIG_PATH_SERVER'), os.environ.get('CONFIG_FILE_NAME'))) as env_file:
    #         env_dict = json.load(env_file)
    #         print(f".env path: {os.path.join(os.environ.get('CONFIG_PATH_SERVER'), os.environ.get('CONFIG_FILE_NAME'))}")
    # case 'prod' :
    #     with open(os.path.join(os.environ.get('CONFIG_PATH_SERVER'), os.environ.get('CONFIG_FILE_NAME'))) as env_file:
    #         env_dict = json.load(env_file)
    #         print(f".env path: {os.path.join(os.environ.get('CONFIG_PATH_SERVER'), os.environ.get('CONFIG_FILE_NAME'))}")
    # case _:
    #     with open(os.path.join(os.environ.get('CONFIG_PATH_LOCAL'), os.environ.get('CONFIG_FILE_NAME'))) as env_file:
    #         env_dict = json.load(env_file)
    #         print(f".env path: {os.path.join(os.environ.get('CONFIG_PATH_LOCAL'), os.environ.get('CONFIG_FILE_NAME'))}")
    case 'dev' | 'prod':
        config_path = os.environ.get('CONFIG_PATH_SERVER')
        config_file_name = os.environ.get('CONFIG_FILE_NAME')
        with open(os.path.join(config_path, config_file_name)) as env_file:
            env_dict = json.load(env_file)
            print(f".env path: {os.path.join(config_path, config_file_name)}")
    case _:
        config_path = os.environ.get('CONFIG_PATH_LOCAL')
        config_file_name = os.environ.get('CONFIG_FILE_NAME')
        with open(os.path.join(config_path, config_file_name)) as env_file:
            env_dict = json.load(env_file)
            print(f".env path: {os.path.join(config_path, config_file_name)}")

class ConfigBasic():

    def __init__(self):
        self.SECRET_KEY = env_dict.get('SECRET_KEY')
        self.WEB_ROOT = os.environ.get('WEB_ROOT')
        self.API_ROOT = os.environ.get('API_ROOT')
        self.APPLE_SERVICE_ROOT = os.environ.get('APPLE_SERVICE_ROOT')
        self.APPLE_SERVICE_11_ROOT = os.environ.get('APPLE_SERVICE_11_ROOT')
        
        # Database
        self.DB_ROOT = os.environ.get('DB_ROOT')
        self.SQL_URI_WHAT_STICKS_DB = f"sqlite:///{self.DB_ROOT}{os.environ.get('DB_NAME_WHAT_STICKS')}"
        # self.SQL_URI_BLOG_POSTS = f"sqlite:///{self.DB_ROOT}{os.environ.get('DB_NAME_BLOG_POSTS')}"

        # database helper files
        self.DATABASE_HELPER_FILES = os.path.join(self.DB_ROOT,"database_helpers")
        self.APPLE_HEALTH_DIR = os.path.join(self.DATABASE_HELPER_FILES,"apple_health")# <-- store Apple Health compressed
        self.DATAFRAME_FILES_DIR = os.path.join(self.DATABASE_HELPER_FILES,"dataframe_files")# <-- store pkl files for dashbaord data item
        self.OURA_SLEEP_RESPONSES = os.path.join(self.DATABASE_HELPER_FILES,"oura_sleep_responses")

        # wsios_helper files
        self.WS_IOS_HELPER_FILES = os.path.join(self.DB_ROOT,"ws_ios_helpers")
        self.DASHBOARD_FILES_DIR = os.path.join(self.WS_IOS_HELPER_FILES,"dashboard_table_obj_files")# <-- store pkl files for dashbaord data item
        self.DATA_SOURCE_FILES_DIR = os.path.join(self.WS_IOS_HELPER_FILES,"data_source_obj_files")# <-- store pkl files for dashbaord data item

        # user files
        self.USER_FILES = os.path.join(self.DB_ROOT,"user_files")
        self.DAILY_CSV = os.path.join(self.USER_FILES,"daily_csv")
        self.RAW_FILES_FOR_DAILY_CSV = os.path.join(self.USER_FILES,"raw_files_for_daily_csv")

        # website files
        self.WEBSITE_FILES = f"{self.DB_ROOT}website_files"# <-- store website files
        self.DIR_WEBSITE_UTILITY_IMAGES = os.path.join(self.WEBSITE_FILES,"website_utility_images")# <-- store blog word documents
        self.DIR_WEBSITE_VIDEOS = os.path.join(self.WEBSITE_FILES,"website_videos")# <-- store videos
        #Other Directories in /databases/WhatSticks10
        # self.DIR_DB_BLOG = os.path.join(self.DIR_DB_AUXILIARY,"blog")# <-- store blog word documents
        # self.DIR_DB_BLOG = f"{self.DB_ROOT}blog"# <-- store blog word documents
        # self.DIR_DB_NEWS = os.path.join(self.DIR_DB_AUXILIARY,"news")# <-- store blog word documents
        # self.DIR_DB_NEWS = f"{self.DB_ROOT}news"# <-- store blog word documents

        # self.DIR_DB_AUX_OURA_SLEEP_RESPONSES = f"{self.DIR_DB_AUXILIARY}/oura_sleep_responses"
        
        # paramters for database/dataframe files
        self.APPLE_HEALTH_QUANTITY_CATEGORY_FILENAME_PREFIX = "AppleHealthQuantityCategory"
        self.APPLE_HEALTH_WORKOUTS_FILENAME_PREFIX = "AppleHealthWorkouts"

        #Email stuff
        self.MAIL_SERVER = env_dict.get('MAIL_SERVER_GMAIL')
        self.MAIL_PORT = env_dict.get('MAIL_PORT')
        self.MAIL_USE_TLS = True
        self.MAIL_USERNAME = env_dict.get('EMAIL_WHAT_STICKS_GMAIL')
        self.MAIL_PASSWORD = env_dict.get('EMAIL_WHAT_STICKS_GMAIL_PASSWORD')
        self.ACCEPTED_EMAILS = env_dict.get('ACCEPTED_EMAILS')

        #web Guest
        self.GUEST_EMAIL = env_dict.get('GUEST_EMAIL')
        self.GUEST_PASSWORD = env_dict.get('GUEST_PASSWORD')

        #API
        self.WS_API_PASSWORD = env_dict.get('WS_API_PASSWORD')

        #Admin stuff
        self.ADMIN_EMAILS = env_dict.get('ADMIN_EMAILS')

        #Captcha
        # self.SITE_KEY_CAPTCHA = env_support_dict.get('SITE_KEY_CAPTCHA')
        # self.SECRET_KEY_CAPTCHA = env_support_dict.get('SECRET_KEY_CAPTCHA')
        self.VERIFY_URL_CAPTCHA = 'https://www.google.com/recaptcha/api/siteverify'

        #Oura Ring
        self.OURA_API_URL_BASE = env_dict.get('OURA_API_URL_BASE')

        #Visual Crossing - weather
        # self.VISUAL_CROSSING_BASE_URL = env_dict.get('VISUAL_CROSSING_BASE_URL')
        # https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/
        self.VISUAL_CROSSING_BASE_URL = "https://weather.visualcrossing.com/"
        self.VISUAL_CROSSING_TOKEN = env_dict.get('VISUAL_CROSSING_TOKEN')

        #Nominatim API - location
        self.NOMINATIM_API_URL = "https://nominatim.openstreetmap.org/"
        # f"https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json"


class ConfigLocal(ConfigBasic):
    
    def __init__(self):
        super().__init__()
        
        #API
        self.API_URL = env_dict.get("WS_API_URL_BASE_LOCAL")

    DEBUG = True

class ConfigDev(ConfigBasic):

    def __init__(self):
        super().__init__()

        #API
        self.API_URL = env_dict.get("WS_API_URL_BASE_DEVELOPMENT")

    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True

class ConfigProd(ConfigBasic):
        
    def __init__(self):
        super().__init__()

        #API
        self.API_URL = env_dict.get("WS_API_URL_BASE_PRODUCTION")

    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True
