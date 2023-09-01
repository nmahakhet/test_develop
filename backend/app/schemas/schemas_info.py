from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, date

class InfoBase(BaseModel):
    line_number: Optional[str]
    location: Optional[str]
    from_location: Optional[str]
    to_location: Optional[str]
    drawing_number: Optional[str]
    service: Optional[str]
    material: Optional[str]
    inservice_date: Optional[date]
    pipe_size: Optional[float]
    original_thickness: Optional[float]
    stress: Optional[float]
    joint_efficiency: Optional[float]
    ca: Optional[float]
    design_life: Optional[float]
    design_pressure: Optional[float]
    operating_pressure: Optional[float]
    design_temperature: Optional[float]
    operating_temperature: Optional[float]

    

class InfoInDBBase():
    id: Optional[int] = None

    class Config:
        orm_mode = True