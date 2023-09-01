from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class CmlBase(BaseModel):
    cml_number: Optional[float]
    cml_description: Optional[str]
    actual_outside_diameter: Optional[float]
    design_thickness: Optional[float]
    structural_thickness: Optional[float]
    required_thickness: Optional[float]
    info_id: Optional[int]

class CmlInDBBase(CmlBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class CmlUpdate(BaseModel):
    cml_number: Optional[float]
    cml_description: Optional[str]
    actual_outside_diameter: Optional[float]
    design_thickness: Optional[float]
    structural_thickness: Optional[float]
    required_thickness: Optional[float]