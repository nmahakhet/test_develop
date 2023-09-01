from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class ThicknessBase(BaseModel):
    actual_thickness: Optional[float] = None
    inspection_date: Optional[str] = None
    test_point_id: Optional[int] = None

class ThicknessInDBBase(ThicknessBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class ThicknessUpdate(BaseModel):
    actual_thickness: Optional[float] = None
    inspection_date: Optional[str] = None