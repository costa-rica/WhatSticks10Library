from .base import Base
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date
from datetime import datetime
from sqlalchemy.orm import relationship


class OuraToken(Base):
    __tablename__ = 'oura_token'
    id = Column(Integer, primary_key = True )
    user_id = Column(Integer, ForeignKey("users.id"))
    token = Column(Text)
    oura_sleep = relationship('OuraSleepDescriptions', backref='Oura_sleep_descrip', lazy=True)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f'OuraToken(id: {self.id}, token: {self.token})'

class OuraSleepDescriptions(Base):
    __tablename__ = 'oura_sleep_descriptions'
    id = Column(Integer, primary_key = True)
    user_id=Column(Integer, ForeignKey('users.id'), nullable=False)
    token_id=Column(Integer, ForeignKey('oura_token.id'), nullable=False)
    summary_date = Column(Text)
    period_id = Column(Integer)
    is_longest = Column(Integer)
    timezone = Column(Integer)
    location = Column(Integer)#haven't found in oura data yet
    bedtime_end = Column(Text)
    bedtime_start = Column(Text)
    breath_average = Column(Float)
    duration = Column(Integer)
    total = Column(Integer)
    awake = Column(Integer)
    rem = Column(Integer)
    deep = Column(Integer)
    light = Column(Integer)
    midpoint_time = Column(Integer)
    efficiency = Column(Integer)
    restless = Column(Integer)
    onset_latency = Column(Integer)
    rmssd = Column(Integer)
    score = Column(Integer)
    score_alignment = Column(Integer)
    score_deep = Column(Integer)
    score_disturbances = Column(Integer)
    score_efficiency = Column(Integer)
    score_latency = Column(Integer)
    score_rem = Column(Integer)
    score_total = Column(Integer)
    temperature_deviation = Column(Float)
    bedtime_start_delta = Column(Integer)
    bedtime_end_delta = Column(Integer)
    midpoint_at_delta = Column(Integer)
    temperature_delta = Column(Float)
    hr_lowest = Column(Integer)
    hr_average = Column(Float)
    # temperature_trend_deviation=Column(Float)

    time_stamp_utc = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"OuraSleepDescriptions(id: {self.id}, user_id: {self.user_id}," \
            f"summary_date:{self.summary_date}," \
            f"score: {self.score}, score_total: {self.score_total}," \
            f"hr_lowest: {self.hr_lowest}, hr_average: {self.hr_average}," \
            f"bedtime_start: {self.bedtime_start}, bedtime_end: {self.bedtime_end}," \
            f"duration: {self.duration}, onset_latency: {self.onset_latency})"


