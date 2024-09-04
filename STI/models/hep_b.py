from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from datetime import datetime
from typing import Optional

class Base(DeclarativeBase):
    pass

class BaseModel:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    
class ClientReg(Base, BaseModel):
    __tablename__ = 'client_reg'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    created_by:Mapped[str] = mapped_column(String(200))
    upated_by:Mapped[str] = mapped_column(String(200))
    first_name:Mapped[str] = mapped_column(String(100))
    middle_name:Mapped[str] = mapped_column(String(100))
    last_name:Mapped[str] = mapped_column(String(100))
    date_of_birth:Mapped[datetime] = mapped_column(DateTime)
    edd:Mapped[str] = mapped_column(DateTime, default=datetime.now())
    patient_aware_of_HepB:Mapped[str] = mapped_column(String(100))
    phone_number:Mapped[Optional[str]] = mapped_column(String(100))
    address:Mapped[Optional[str]] = mapped_column(String(100))
    city:Mapped[Optional[str]] = mapped_column(String(100))
    state:Mapped[Optional[str]] = mapped_column(String(100))
    country_of_birth:Mapped[Optional[str]] = mapped_column(String(100))
    zip_code:Mapped[Optional[str]] = mapped_column(String(100))
    insurance_type:Mapped[str] = mapped_column(String(100), unique=True)
    race:Mapped[Optional[str]] = mapped_column(String(100))
    hispanic:Mapped[Optional[str]] = mapped_column(String(100))
    primary_language:Mapped[Optional[str]] = mapped_column(String(100))
    interprater:Mapped[Optional[str]] = mapped_column(String(100))
    lab_investigation_type:Mapped[Optional[str]] = mapped_column(String(100))

class ClinicalInfo(BaseModel, Base):
    __tablename__ = 'clinical_info'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    created_by:Mapped[str] = mapped_column(String(200))
    upated_by:Mapped[str] = mapped_column(String(200))
    prov_last_name:Mapped[Optional[str]] = mapped_column(String(100))
    prov_first_name:Mapped[str] = mapped_column(String(100), unique=True)
    prov_type:Mapped[str] = mapped_column(String(100), unique=True)
    expd_facility:Mapped[Optional[str]] = mapped_column(String(100))
    report_facility:Mapped[Optional[str]] = mapped_column(String(100))
    address:Mapped[Optional[str]] = mapped_column(String(100))
    city:Mapped[Optional[str]] = mapped_column(String(100))
    state:Mapped[Optional[str]] = mapped_column(String(100))
    zip_code:Mapped[Optional[str]] = mapped_column(String(100))
    report_facility_contact:Mapped[Optional[str]] = mapped_column(String(100))
    report_facility_phone_numaber:Mapped[Optional[str]] = mapped_column(String(100))
    form_date:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    positve_lab_attached:Mapped[Optional[str]] = mapped_column(String(100))