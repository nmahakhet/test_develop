from pydantic import BaseModel
from datetime import datetime
from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Info(Base):
    __tablename__ = "info"

    id = Column(Integer, primary_key=True)
    line_number = Column(String(255))
    location = Column(String(255))
    from_location = Column(String(255))
    to_location = Column(String(255))
    drawing_number = Column(String(255))
    service = Column(String(255))
    material = Column(String(255))
    inservice_date = Column(Date, default=datetime.now)
    pipe_size = Column(Float , default=0)
    original_thickness = Column(Float , default=0)
    stress = Column(Float , default=0)
    joint_efficiency = Column(Float , default=0)
    ca = Column(Float , default=0)
    design_life = Column(Float , default=0)
    design_pressure = Column(Float , default=0)
    operating_pressure = Column(Float , default=0)
    design_temperature = Column(Float , default=0)
    operating_temperature = Column(Float , default=0)
