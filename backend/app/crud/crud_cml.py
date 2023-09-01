from app.core.deps import get_db
from sqlalchemy.orm import Session
from app import schemas
from app.models.info import Info
from app.models.cml import Cml
from app.crud.base import CRUDBase
from fastapi.encoders import jsonable_encoder

class CRUDCml(CRUDBase):
    def get_cml(self, db: Session, key_info: int):
        return (
            db.query(Cml).filter(Cml.info_id == key_info).all()
        )

    def insert_cml(self, db: Session, obj_in: schemas.CmlBase):
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update_cml(
        self, cml_key: int, db: Session, obj_in: schemas.CmlUpdate
    ):
        db.query(Cml).filter(Cml.id == cml_key).update({**obj_in.dict()})
        db.commit()
cml = CRUDCml(Cml)