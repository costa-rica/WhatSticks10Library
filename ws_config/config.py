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
    case 'dev' :
        with open(os.path.join(os.environ.get('CONFIG_PATH_SERVER'), os.environ.get('CONFIG_FILE_NAME'))) as env_file:
            env_dict = json.load(env_file)
    case 'prod' :
        with open(os.path.join(os.environ.get('CONFIG_PATH_SERVER'), os.environ.get('CONFIG_FILE_NAME'))) as env_file:
            env_dict = json.load(env_file)
    case _:
        with open(os.path.join(os.environ.get('CONFIG_PATH_LOCAL'), os.environ.get('CONFIG_FILE_NAME'))) as env_file:
            env_dict = json.load(env_file)

class ConfigBasic():

    def __init__(self):
        self.SECRET_KEY = env_dict.get('SECRET_KEY')
        self.WEB_ROOT = os.environ.get('WEB_ROOT')
        self.API_ROOT = os.environ.get('API_ROOT')
        
        # Database
        self.DB_ROOT = os.environ.get('DB_ROOT')
        self.SQL_URI_WHAT_STICKS_DB = f"sqlite:///{self.DB_ROOT}{os.environ.get('DB_NAME_WHAT_STICKS')}"
        # self.SQL_URI_BLOG_POSTS = f"sqlite:///{self.DB_ROOT}{os.environ.get('DB_NAME_BLOG_POSTS')}"
        
        #Other Directories in /databases/WhatSticks10
        self.APPLE_HEALTH_DIR = f"{self.DB_ROOT}apple_health"# <-- store Apple Health compressed
        self.DF_FILES_DIR = f"{self.DB_ROOT}df_files"# <-- store pkl files for dashbaord data item
        self.DIR_DB_BLOG = f"{self.DB_ROOT}blog"# <-- store blog word documents
        self.DIR_DB_NEWS = f"{self.DB_ROOT}news"# <-- store blog word documents
        self.DIR_DB_AUXIILARY = f"{self.DB_ROOT}auxiliary"# <-- store website files
        self.DIR_DB_AUX_IMAGES_PEOPLE = f"{self.DIR_DB_AUXIILARY}/images_people"# <-- store website images of people
        self.DIR_DB_AUX_FILES_UTILITY = f"{self.DIR_DB_AUXIILARY}/files_utility"
        self.DIR_DB_AUX_OURA_SLEEP_RESPONSES = f"{self.DIR_DB_AUXIILARY}/oura_sleep_responses"

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
        self.API_URL = os.env_dict.get("WS_API_URL_BASE_DEVELOPMENT")

    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True

class ConfigProd(ConfigBasic):
        
    def __init__(self):
        super().__init__()

        #API
        self.API_URL = os.env_dict.get("WS_API_URL_BASE_PRODUCTION")

    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True
