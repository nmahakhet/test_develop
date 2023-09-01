from pydantic import BaseModel
from datetime import datetime
from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey

class Cml(Base):
    __tablename__ = "cml"

    id = Column(Integer, primary_key=True)
    cml_number = Column(Float)
    cml_description = Column(String)
    actual_outside_diameter = Column(Float)
    design_thickness = Column(Float)
    structural_thickness = Column(Float)
    required_thickness = Column(Float)

    info_id = Column(
        Integer, ForeignKey("info.id")
    )    