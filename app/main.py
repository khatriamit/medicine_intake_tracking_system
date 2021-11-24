from typing import List
from uuid import uuid4
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from app.database import database
from app import schemas, models
from pydantic import parse_obj_as

app = FastAPI(versionstr="0.1.0")


@app.on_event("startup")
async def startup():
    print("DB connected")
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    print("DB connected")
    await database.disconnect()


@app.get("/")
async def index():
    return {"message": "app running"}


@app.post("/medicine_info/", response_model=schemas.MedicineInfo)
async def add_medicine_info(info: schemas.MedicineInfo):
    query = models.medicine_info.insert().values(id=uuid4(), **info.dict())
    await database.execute(query)
    return info


@app.get("/medicine_info/")
async def get_medicine_info():
    query = models.medicine_info.select()
    q_res = await database.fetch_all(query)
    return parse_obj_as(
        List[schemas.MedicineInfo],
        jsonable_encoder(q_res),
    )


@app.delete("/medicine_info/{id:str}")
async def delete_medicine_info(id: str):
    query = models.medicine_info.delete().where(models.medicine_info.c.id == id)
    await database.execute(query)
    return {"message": "deleted successfully"}


@app.post("/doctor_info/", response_model=schemas.DoctorInfo)
async def add_doctor_info(info: schemas.DoctorInfo):
    query = models.doctor_info.insert().values(id=uuid4(), **info.dict())
    await database.execute(query)
    return info


@app.get("/doctor_info/")
async def add_medicine_info():
    query = models.doctor_info.select()
    q_res = await database.fetch_all(query)
    return parse_obj_as(
        List[schemas.DoctorInfo],
        jsonable_encoder(q_res),
    )


@app.delete("/doctor_info/{id:str}")
async def delete_doctor_info(id: str):
    query = models.doctor_info.delete().where(models.doctor_info.c.id == id)
    await database.execute(query)
    return {"message": "deleted successfully"}


@app.post("/patient_info/", response_model=schemas.PatientInfo)
async def add_patient(info: schemas.PatientInfo):
    query = models.patient_info.insert().values(id=uuid4(), **info.dict())
    await database.execute(query)
    return info


@app.get("/patient_info/")
async def add_medicine_info():
    query = models.patient_info.select()
    q_res = await database.fetch_all(query)
    return parse_obj_as(
        List[schemas.PatientInfo],
        jsonable_encoder(q_res),
    )


@app.delete("/patient_info/{id:str}")
async def delete_patient_info(id: str):
    query = models.patient_info.delete().where(models.patient_info.c.id == id)
    await database.execute(query)
    return {"message": "deleted successfully"}


@app.post("/mark_has_taken/")
async def mark_has_taken(medicine_ids: schemas.MedicineID):
    print(medicine_ids.dict())
    for i in medicine_ids.dict():
        print(i)
    return {"message": "deleted successfully"}
