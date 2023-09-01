from typing import List, Optional
from pydantic import BaseModel

class TestpointBase(BaseModel):
    tp_number: Optional[int]
    tp_description: Optional[int]
    note: Optional[str]
    cml_id: Optional[int]

class TestpointInDBBase(TestpointBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class TestpointUpdate(BaseModel):
    tp_number: Optional[int]
    tp_description: Optional[int]
    note: Optional[str]