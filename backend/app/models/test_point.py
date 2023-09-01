from pydantic import BaseModel
from datetime import datetime
from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey

class Testpoint(Base):
    __tablename__ = "test_point"

    id = Column(Integer, primary_key=True, index=True)
    tp_number = Column(Integer)
    tp_description = Column(Integer)
    note = Column(String)
    
    cml_id = Column(
        Integer, ForeignKey("cml.id")
    )