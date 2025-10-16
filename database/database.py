from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class RoadAnalyst(Base):
    __tablename__ = "road_analysts"
    id = Column(Integer, primary_key=True)
    aggressive_percent = Column(Float, nullable=False)
    drivers_count = Column(Integer, nullable=False)
    aggressive_drivers_count = Column(Integer, nullable=False)
    normal_drivers_count= Column(Integer, nullable=False)
    abrupt_braking_count = Column(Integer, nullable=False)
    abrupt_acceleration_count = Column(Integer, nullable=False)
    max_speed = Column(Float, nullable=True)
    min_speed = Column(Float, nullable=True)
    avg_speed = Column(Float, nullable=True)
