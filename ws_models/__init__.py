# print("- in __init__.py")
from .base import Base, create_engine, inspect, sess, engine, text
from .models_users import Users
from .models_blog_posts import CommunityPosts, CommunityComments,NewsPosts, NewsComments
from .models_locations import UserLocationDay, Locations, WeatherHistory
from .models_oura import OuraToken, OuraSleepDescriptions
import os
from flask_login import LoginManager

login_manager= LoginManager()
login_manager.login_view = 'bp_users.login'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(any_name_for_id_obj):# any_name_for_id_obj can be any name because its an arg that is the user id.
    # This is probably created somewhere inside flask_login when the user gets logged in. But i've not been able to track it.
    return sess.query(Users).filter_by(id = any_name_for_id_obj).first()