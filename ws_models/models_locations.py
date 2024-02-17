from .base import Base
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date, JSON, UniqueConstraint
from datetime import datetime
from sqlalchemy.orm import relationship


class UserLocationDay(Base):
    __tablename__ = 'user_location_day'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    location_id = Column(Integer, ForeignKey("locations.id"))#TODO: should this remain nullable=False?
    date_utc_user_check_in = Column(Date)
    row_type = Column(Text)#user entered or scheduler entered row?
    date_time_utc_user_check_in = Column(DateTime)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f'UserLocationDay(id: {self.id}, user_id: {self.user_id},' \
            f'date_utc_user_check_in: {self.date_utc_user_check_in})'

    # Add a UniqueConstraint to the table definition
    __table_args__ = (
        UniqueConstraint('user_id', 'date_utc_user_check_in',  \
            name='_user_id_AND_date_utc_user_check_in'),
    )

class Locations(Base):
    __tablename__ = 'locations'
    id = Column(Integer,  primary_key = True)
    city = Column(Text)
    state = Column(Text)
    country = Column(Text)
    lat = Column(Float(precision=4, decimal_return_scale=None))
    lon = Column(Float(precision=4, decimal_return_scale=None))
    tz_id = Column(Text)
    boundingbox = Column(JSON)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)
    # oura_sleep = relationship('Oura_sleep_descriptions', backref='oura_sleep', lazy=True)
    loc_day = relationship('UserLocationDay', backref='user_loc_day_for_this_loc', lazy=True)
    weather_hist = relationship('WeatherHistory', backref = 'weath_hist', lazy = True)

    def __repr__(self):
        return f'Locations(id: {self.id}, city: {self.city}, lat: {self.lat}, ' \
            f'lon: {self.lon})'

class WeatherHistory(Base):
    __tablename__ = 'weather_history'
    id = Column(Integer, primary_key = True)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable = False)
    date_time = Column(Text)
    datetimeEpoch = Column(Integer)
    tempmax = Column(Float)
    tempmin = Column(Float)
    temp = Column(Float)
    feelslikemax = Column(Float)
    feelslikemin = Column(Float)
    feelslike = Column(Float)
    dew = Column(Text)
    humidity = Column(Text)
    precip = Column(Text)
    precipprob = Column(Text)
    precipcover = Column(Text)
    preciptype = Column(Text)
    snow = Column(Text)
    snowdepth = Column(Text)
    windgust = Column(Text)
    windspeed = Column(Text)
    winddir = Column(Text)
    pressure = Column(Text)
    cloudcover = Column(Text)
    visibility = Column(Text)
    solarradiation = Column(Text)
    solarenergy = Column(Text)
    uvindex = Column(Text)
    sunrise = Column(Text)
    sunriseEpoch = Column(Text)
    sunset = Column(Text)
    sunsetEpoch = Column(Text)
    moonphase = Column(Text)
    conditions = Column(Text)
    description = Column(Text)
    icon = Column(Text)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f"WeatherHistory(id: {self.id}, date_time: {self.date_time}, " \
            f"location_id: {self.location_id}, temp: {self.temp})"
