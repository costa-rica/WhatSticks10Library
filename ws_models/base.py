# # print("- in ws_models/Base")

from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from .config import config

Base = declarative_base()
# engine = create_engine(config.SQL_URI_WHAT_STICKS_DB, echo = False, connect_args={"check_same_thread": False})
engine = create_engine(config.SQL_URI_WHAT_STICKS_DB)
Session = sessionmaker(bind = engine)
sess = Session()
