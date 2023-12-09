from .base import Base, sess
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date, Boolean
from datetime import datetime
from .config import config
import os

from .models_users import Users

class CommunityPosts(Base):
    __tablename__ = 'communityposts'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id_name_string = Column(Text)
    title = Column(Text)
    description = Column(Text)
    date_published = Column(DateTime, nullable=False, default=datetime.now)
    edited = Column(Text)
    post_html_filename = Column(Text)
    notes = Column(Text)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)
    comments = relationship('CommunityComments', backref='comments', lazy=True)

    def __repr__(self):
        return f'CommunityPosts(id: {self.id}, user_id: {self.user_id}, title: {self.title})'


class CommunityComments(Base):
    __tablename__ = 'communitycomments'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("communityposts.id"), nullable=False)
    comment = Column(Text)
    date_published = Column(DateTime, nullable=False, default=datetime.now)
    edited = Column(Text)
    post_html_filename = Column(Text)
    notes = Column(Text)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f'CommunityComments(id: {self.id}, user_id: {self.user_id}, date_published: {self.date_published})'


class NewsPosts(Base):
    __tablename__ = 'newsposts'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id_name_string = Column(Text)
    title = Column(Text)
    description = Column(Text)
    date_published = Column(DateTime, nullable=False, default=datetime.now)
    edited = Column(Text)
    post_html_filename = Column(Text)
    notes = Column(Text)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)
    comments = relationship('NewsComments', backref='comments', lazy=True)

    def __repr__(self):
        return f'NewsPosts(id: {self.id}, user_id: {self.user_id}, title: {self.title})'


class NewsComments(Base):
    __tablename__ = 'newscomments'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("newsposts.id"), nullable=False)
    comment = Column(Text)
    date_published = Column(DateTime, nullable=False, default=datetime.now)
    edited = Column(Text)
    post_html_filename = Column(Text)
    notes = Column(Text)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f'NewsComments(id: {self.id}, user_id: {self.user_id}, date_published: {self.date_published})'

