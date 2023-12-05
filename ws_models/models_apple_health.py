# from colorama import Fore
from .base import Base
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date, UniqueConstraint
from datetime import datetime

class AppleHealthExport(Base):# This is used for XML file exported from iPhone
    __tablename__ = 'apple_health_export'
    id = Column(Integer,primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(Text)
    sourceName = Column(Text)
    sourceVersion = Column(Text)
    unit = Column(Text)
    creationDate = Column(Text)
    startDate = Column(Text)
    endDate = Column(Text)
    value = Column(Text)
    device = Column(Text)
    MetadataEntry = Column(Text)
    HeartRateVariabilityMetadataList = Column(Text)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f'AppleHealthExport(id: {self.id}, user_id: {self.user_id},' \
            f'type: {self.type}, sourceName: {self.sourceName}, unit: {self.unit},' \
            f'creationDate: {self.creationDate}, time_stamp_utc: {self.time_stamp_utc})'


class AppleHealthSteps(Base):
    __tablename__ = 'apple_health_steps'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date_time = Column(Text)
    steps_count = Column(Integer)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f'AppleHealthSteps(id: {self.id}, user_id: {self.user_id},' \
            f'date_time: {self.date_time}, steps_count: {self.steps_count})'


class AppleHealhKit(Base):# This is used for XML file exported from iPhone
    __tablename__ = 'apple_health_kit'
    id = Column(Integer,primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    sampleType = Column(Text)
    startDate = Column(Text)
    endDate = Column(Text)
    metadataAppleHealth = Column(Text)
    sourceName = Column(Text)
    sourceVersion = Column(Text)
    sourceProductType = Column(Text)
    device = Column(Text)
    UUID = Column(Text)
    quantity = Column(Text)
    value = Column(Text)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f'AppleHealhKit(id: {self.id}, user_id: {self.user_id},' \
            f'sampleType: {self.sampleType}, startDate: {self.startDate}, quantity: {self.quantity},' \
            f'time_stamp_utc: {self.time_stamp_utc}, UUID: {self.UUID})'
    
    # Add a UniqueConstraint to the table definition
    __table_args__ = (
        UniqueConstraint('user_id', 'sampleType', 'UUID', name='_user_sample_uuid_uc'),
    )