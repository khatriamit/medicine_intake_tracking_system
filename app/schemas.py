from uuid import UUID, uuid4
from datetime import date
from typing import List, Optional
from pydantic import BaseModel as Model

from app.constant import MedicineType


class MedicineInfo(Model):
    id: Optional[UUID]
    name: str
    type: MedicineType
    time: str
    start_date: date
    end_date: date
    quantity: str
    has_taken: Optional[bool] = False

    class Config:
        orm_mode = True


class DoctorInfo(Model):
    id: Optional[UUID]
    name: str
    phone: str
    address: str

    class Config:
        orm_mode = True


class PatientInfo(Model):
    id: Optional[UUID]
    name: str
    phone: str
    address: str

    class Config:
        orm_mode = True


class MedicineID(Model):
    id: List[UUID]
