# from colorama import Fore
from .base import Base
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date, UniqueConstraint
from datetime import datetime

# class AppleHealthKit(Base):
class AppleHealthQuantityCategory(Base):
    __tablename__ = 'apple_health_quantity_category'
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
        return f'AppleHealthQuantityCategory(id: {self.id}, user_id: {self.user_id},' \
            f'sampleType: {self.sampleType}, startDate: {self.startDate}, quantity: {self.quantity},' \
            f'time_stamp_utc: {self.time_stamp_utc}, UUID: {self.UUID})'
    
    # Add a UniqueConstraint to the table definition
    __table_args__ = (
        UniqueConstraint('user_id', 'sampleType', 'UUID', name='_user_sample_uuid_uc'),
    )

class AppleHealthWorkout(Base):
    __tablename__ = 'apple_health_workout'
    id = Column(Integer,primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    sampleType = Column(Text)
    startDate = Column(Text)
    endDate = Column(Text)
    duration = Column(Text)# seconds (Polar is minutes)
    totalEnergyBurned = Column(Text)
    totalDistance = Column(Text)
    sourceName = Column(Text)
    sourceVersion = Column(Text)
    device = Column(Text)
    UUID = Column(Text)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f'AppleHealthWorkout(id: {self.id}, user_id: {self.user_id},' \
            f'sampleType: {self.sampleType}, startDate: {self.startDate}, duration: {self.duration},' \
            f'time_stamp_utc: {self.time_stamp_utc}, UUID: {self.UUID})'
    
    # Add a UniqueConstraint to the table definition
    __table_args__ = (
        UniqueConstraint('user_id', 'sampleType', 'UUID', name='_user_sample_uuid_uc'),
    )

# This is the old table from What-Sticks web, used for XML file exported from iPhone
class AppleHealthExport(Base):
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



