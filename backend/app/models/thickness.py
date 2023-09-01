from pydantic import BaseModel
from datetime import datetime
from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey

class Thickness(Base):
    __tablename__ = "thickness"

    id = Column(Integer, primary_key=True, index=True)
    actual_thickness = Column(Float, index=True)
    inspection_date = Column(DateTime(timezone=True), server_default=func.now())

    test_point_id = Column(
        Integer, ForeignKey("test_point.id")
    )