import sqlalchemy as sa
from sqlalchemy import Column, String, Boolean, Enum
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import Date, Integer
from app.constant import MedicineType, MedicineTime
from app.database import metadata


medicine_info = sa.Table(
    "medicine_info",
    metadata,
    sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
    sa.Column("name", sa.String(55), nullable=False),
    sa.Column("type", sa.String(55)),
    sa.Column("time", sa.String(55), nullable=False),
    sa.Column("start_date", sa.Date(), nullable=False),
    sa.Column("end_date", sa.Date(), nullable=False),
    sa.Column("quantity", sa.String(255), nullable=False),
    sa.Column("has_taken", sa.BOOLEAN),
)


doctor_info = sa.Table(
    "doctor_info",
    metadata,
    sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
    sa.Column("name", sa.String(55), nullable=False),
    sa.Column("phone", sa.String(55)),
    sa.Column("address", sa.String(55)),
)


patient_info = sa.Table(
    "patient_info",
    metadata,
    sa.Column("id", postgresql.UUID(as_uuid=False), primary_key=True),
    sa.Column("name", sa.String(55), nullable=False),
    sa.Column("phone", sa.String(55)),
    sa.Column("address", sa.String(55)),
)
