from fastapi import APIRouter, Depends, HTTPException
from app import schemas, crud
from sqlalchemy.orm import Session
from app.core.deps import get_db
from typing import List
from app.models.info import Info

api_router = APIRouter()

@api_router.get("/info")
async def get_info(*, db: Session = Depends(get_db)):
    info_all = crud.info.get_info_all(db)
    return info_all

@api_router.post("/insert_info")
async def insert_info(
    *,
    db: Session = Depends(get_db),
    info_data: schemas.InfoBase
):
    return crud.info.insert_info(db, info_data)

@api_router.put("/update_info/{info_key}")
async def update_info(
    *,
    db: Session = Depends(get_db),
    info_data: schemas.InfoBase,
    info_key: int
):
    return crud.info.update_info(info_key, db, info_data)

@api_router.delete("/delete_info/{info_key}")
async def delete_info(
    *,
    db: Session = Depends(get_db),
    info_key: int,
):
    return crud.info.remove(db, id=info_key)

@api_router.post("/insert_cml")
async def insert_cml(
    *,
    db: Session = Depends(get_db),
    cml_data: schemas.CmlBase
):
    return crud.cml.create(db, obj_in=cml_data)

@api_router.put("/update_cml/{cml_key}")
async def update_cml(
    *,
    db: Session = Depends(get_db),
    cml_data: schemas.CmlUpdate,
    cml_key: int
):
    return crud.cml.update_cml(cml_key, db, cml_data)

@api_router.get("/cml/{info_key}")
async def get_cml_by_id(*, db: Session = Depends(get_db), info_key: int):
    return crud.cml.get_cml(db, info_key)

@api_router.delete("/delete_cml/{cml_key}")
async def delete_cml(
    *,
    db: Session = Depends(get_db),
    cml_key: int,
):
    return crud.cml.remove(db, id=cml_key)

@api_router.get("/testpoint/{cml_key}")
async def get_testpoint_by_id(*, db: Session = Depends(get_db), cml_key: int):
    return crud.test_point.get_test_point(db, cml_key)

@api_router.post("/insert_testpoint")
async def insert_testpoint(
    *,
    db: Session = Depends(get_db),
    testpoint_data: schemas.TestpointBase
):
    return crud.test_point.create(db, obj_in=testpoint_data)

@api_router.put("/update_testpoint/{testpoint_key}")
async def update_testpoint(
    *,
    db: Session = Depends(get_db),
    testpoint_data: schemas.TestpointUpdate,
    testpoint_key: int
):
    return crud.test_point.update_test_point(testpoint_key, db, testpoint_data)

@api_router.delete("/delete_testpoint/{testpoint_key}")
async def delete_testpoint(
    *,
    db: Session = Depends(get_db),
    testpoint_key: int,
):
    return crud.test_point.remove(db, id=testpoint_key)


@api_router.get("/thickness/{thick_key}")
async def get_thickness_by_id(*, db: Session = Depends(get_db), thick_key: int):
    return crud.thickness.get_thickness(db, thick_key)

@api_router.post("/insert_thickness")
async def insert_thickness(
    *,
    db: Session = Depends(get_db),
    thickness_data: schemas.ThicknessBase
):
    return crud.thickness.create(db, obj_in=thickness_data)

@api_router.put("/update_thickness/{thickness_key}")
async def update_thickness(
    *,
    db: Session = Depends(get_db),
    thickness_data: schemas.ThicknessUpdate,
    thickness_key: int
):
    return crud.thickness.update_thickness(thickness_key, db, thickness_data)

@api_router.delete("/delete_thickness/{thickness_key}")
async def delete_thickness(
    *,
    db: Session = Depends(get_db),
    thickness_key: int,
):
    return crud.thickness.remove(db, id=thickness_key)