from app.core.deps import get_db
from sqlalchemy.orm import Session
from app import schemas
from app.models.cml import Cml
from app.models.test_point import Testpoint
from app.crud.base import CRUDBase
from fastapi.encoders import jsonable_encoder

class CRUDTestpoint(CRUDBase):
    def get_test_point(self, db: Session, key_info: int):
        return (
            db.query(Testpoint).filter(Testpoint.cml_id == key_info).all()
        )

    def insert_test_point(self, db: Session, obj_in: schemas.TestpointBase):
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update_test_point(
        self, test_point_key: int, db: Session, obj_in: schemas.TestpointUpdate
    ):
        db.query(Testpoint).filter(Testpoint.id == test_point_key).update({**obj_in.dict()})
        db.commit()
test_point = CRUDTestpoint(Testpoint)