from app.core.deps import get_db
from sqlalchemy.orm import Session
from app import schemas
from app.models.info import Info
from app.crud.base import CRUDBase
from fastapi.encoders import jsonable_encoder

class CRUDInfo(CRUDBase):
    def get_info_all(self, db: Session):
        stmt = db.query(Info)
        return (
            stmt.all()
        )

    def insert_info(self, db: Session, obj_in: schemas.InfoBase):
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update_info(
        self, info_key: int, db: Session, obj_in: schemas.InfoBase
    ):
        db.query(Info).filter(Info.id == info_key).update({**obj_in.dict()})
        db.commit()
info = CRUDInfo(Info)