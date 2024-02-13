from .base import Base, sess
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date, Boolean
from itsdangerous.url_safe import URLSafeTimedSerializer#new 2023
from datetime import datetime
from flask_login import UserMixin
from .config import config
import os
from flask import current_app


def default_username(context):
    return context.get_current_parameters()['email'].split('@')[0]


class Users(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    email = Column(Text, unique = True, nullable = False)
    password = Column(Text, nullable = False)
    username = Column(Text, default=default_username)
    lat = Column(Float(precision=4, decimal_return_scale=None))
    lon = Column(Float(precision=4, decimal_return_scale=None))
    timezone = Column(Text)
    location_permission = Column(Boolean, default=False)
    location_reoccuring_permission = Column(Boolean, default=False)
    share = Column(Text)
    notes = Column(Text)
    post_blog_permission = Column(Boolean, default=True)
    post_news_permission = Column(Boolean, default=False)
    comment_blog_permission = Column(Boolean, default=True)
    comment_news_permission = Column(Boolean, default=True)
    admin_blog_permission = Column(Boolean, default=False)
    admin_news_permission = Column(Boolean, default=False)
    admin_users_permission = Column(Boolean, default=False)
    guest_account = Column(Boolean, default=False)
    guest_account_mirror = Column(Boolean, default=False)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)
    oura_token_id = relationship("OuraToken", backref="oura_token_id", lazy=True)
    oura_sleep = relationship('OuraSleepDescriptions', backref='oura_sleep', lazy=True)
    loc_day = relationship('UserLocationDay', backref='user_loc_day', lazy=True)
    user_notes_ref = relationship('UserNotes', backref='user_notes_ref', lazy=True)
    community_posts = relationship('CommunityPosts', backref='community_posts', lazy=True)
    community_comments = relationship('CommunityComments', backref='community_comments', lazy=True)
    news_posts = relationship('NewsPosts', backref='news_posts', lazy=True)
    news_comments = relationship('NewsComments', backref='news_comments', lazy=True)


    def get_reset_token(self):
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        return serializer.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token):
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:
            payload = serializer.loads(token, max_age=1000)
            user_id = payload.get("user_id")
        except:
            return None

        return sess.query(Users).get(user_id)

    def __repr__(self):
        return f'Users(id: {self.id}, email: {self.email}, share: {self.share},' \
        f'post_news_permission: {self.post_news_permission})'


class UserNotes(Base):
    __tablename__ = 'user_notes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    datetime_of_note=Column(DateTime)
    note_title = Column(Text) #walking, running, empty is ok for something like mood
    note_details = Column(Text)
    source_name=Column(Text)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f"UserNotes({self.id},datetime_of_note:{self.datetime_of_note}," \
        f"note_title: {self.note_title}, note_details: {self.note_details}," \
        f"time_stamp_utc: {self.time_stamp_utc})"

