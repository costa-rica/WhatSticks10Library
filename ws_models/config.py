print("- in ws_models/config.py")
import os
from ws_config import ConfigDev, ConfigProd, ConfigLocal

if os.environ.get('FLASK_CONFIG_TYPE')=='local':
    config = ConfigLocal()
    print('- ws_models/config: Local')
elif os.environ.get('FLASK_CONFIG_TYPE')=='dev':
    config = ConfigDev()
    print('- ws_models/config: Development')
elif os.environ.get('FLASK_CONFIG_TYPE')=='prod':
    config = ConfigProd()
    print('- ws_models/config: Production')

# ############################################################################
# ## Build Auxiliary directories in DB_ROOT
# if not os.path.exists(config.DB_ROOT):
#     os.makedirs(config.DB_ROOT)

# ############################################################################
# ## Build Sqlite database files for DB_NAME_BLOGPOST

# if os.path.exists(os.path.join(config.DB_ROOT,os.environ.get('DB_NAME_BLOG_POSTS'))):
#     logger_init.info(f"db already exists: {os.path.join(config_for_flask.DB_ROOT,os.environ.get('DB_NAME_BLOG_POSTS'))}")
# else:
#     dict_base['Base_blog_posts'].metadata.create_all(dict_engine['engine_blog_posts'])
#     logger_init.info(f"NEW db created: {os.path.join(config.DB_ROOT,os.environ.get('DB_NAME_BLOG_POSTS'))}")

