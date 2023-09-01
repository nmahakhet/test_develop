from app.core.deps import get_db
from sqlalchemy.orm import Session
from app import schemas
from app.models.thickness import Thickness
from app.crud.base import CRUDBase
from fastapi.encoders import jsonable_encoder

class CRUDThickness(CRUDBase):
    def get_thickness(self, db: Session, key_info: int):
        return (
            db.query(Thickness).filter(Thickness.test_point_id == key_info).all()
        )

    def insert_thickness(self, db: Session, obj_in: schemas.ThicknessBase):
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update_thickness(
        self, test_point_key: int, db: Session, obj_in: schemas.ThicknessUpdate
    ):
        db.query(Thickness).filter(Thickness.id == test_point_key).update({**obj_in.dict()})
        db.commit()
thickness = CRUDThickness(Thickness)