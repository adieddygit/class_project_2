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
    
class ClinicalInfo(Base, BaseModel):
    __tablename__ = 'clinical_info'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    created_by:Mapped[str] = mapped_column(String(200))
    upated_by:Mapped[str] = mapped_column(String(200))
    health_provider:Mapped[str] = mapped_column(String(100))
    phone_number:Mapped[str] = mapped_column(String(100))
    
    
class ClientInfo(Base, BaseModel):
    __tablename__ = 'client_info'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    created_by:Mapped[str] = mapped_column(String(200))
    upated_by:Mapped[str] = mapped_column(String(200))
    name:Mapped[str] = mapped_column(String(100))
    date_of_birth:Mapped[datetime] = mapped_column(DateTime)
    gender:Mapped[str] = mapped_column(String(100))
    phone_number:Mapped[Optional[str]] = mapped_column(String(100))
    alt_phone_number:Mapped[Optional[str]] = mapped_column(String(100))
    street:Mapped[Optional[str]] = mapped_column(String(100))
    city:Mapped[Optional[str]] = mapped_column(String(100))
    zip_code:Mapped[Optional[str]] = mapped_column(String(100))
    preg_test_results:Mapped[Optional[str]] = mapped_column(String(100))
    ethnicity:Mapped[Optional[str]] = mapped_column(String(100))
    race:Mapped[str] = mapped_column(String(100), unique=True)
    gender_of_sex_partners:Mapped[str] = mapped_column(String(100))
    test_result_type:Mapped[str] = mapped_column(String(100))
    date_of_result_type:Mapped[str] = mapped_column(DateTime)
    previous_hiv_test:Mapped[Optional[str]] = mapped_column(String(100))
    reasons_for_exam:Mapped[Optional[str]] = mapped_column(String(100))
    diagnosis:Mapped[Optional[str]] = mapped_column(String(100))
    site:Mapped[str] = mapped_column(String(100))

class GonoTreatment(BaseModel, Base):
    __tablename__ = 'gono_treatment'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    created_by:Mapped[str] = mapped_column(String(200))
    upated_by:Mapped[str] = mapped_column(String(200))
    treatment:Mapped[str] = mapped_column(String(200))
    date_of_treatment:Mapped[str] = mapped_column(DateTime)
    alt_treatment:Mapped[str] = mapped_column(String(200))
    date_of_alt_treatment:Mapped[str] = mapped_column(DateTime)
    other_treatment:Mapped[str] = mapped_column(DateTime)
    date_of_other_treatment:Mapped[str] = mapped_column(DateTime)

class ChlamydiaTreatment(BaseModel, Base):
    __tablename__ = 'chlamydia_treatment'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    created_by:Mapped[str] = mapped_column(String(200))
    upated_by:Mapped[str] = mapped_column(String(200))
    treatment:Mapped[str] = mapped_column(String(200))
    date_of_treatment:Mapped[str] = mapped_column(DateTime)
    alt_treatment:Mapped[str] = mapped_column(String(200))
    date_of_alt_treatment:Mapped[str] = mapped_column(DateTime)
    other_treatment:Mapped[str] = mapped_column(DateTime)
    date_of_other_treatment:Mapped[str] = mapped_column(DateTime)

class NoTreatment(BaseModel, Base):
    __tablename__ = 'no_treatment'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    created_by:Mapped[str] = mapped_column(String(200))
    upated_by:Mapped[str] = mapped_column(String(200))
    patient_notofied:Mapped[str] = mapped_column(String(200))
    provider_assistance:Mapped[str] = mapped_column(String(200))
    provider_request_of_contact:Mapped[str] = mapped_column(String(200))