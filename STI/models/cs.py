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
    

class MaternalInfo(Base, BaseModel):
    __tablename__ = 'maternal_info'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    created_by:Mapped[str] = mapped_column(String(200))
    upated_by:Mapped[str] = mapped_column(String(200))
    country:Mapped[str] = mapped_column(String(100))
    city:Mapped[Optional[str]] = mapped_column(String(100))
    zip_code:Mapped[Optional[str]] = mapped_column(String(100))
    race:Mapped[str] = mapped_column(String(100), unique=True)
    ethnicity:Mapped[Optional[str]] = mapped_column(String(100))
    date_of_birth:Mapped[datetime] = mapped_column(DateTime)
    obs_history:Mapped[str] = mapped_column(String(100))
    lmp:Mapped[datetime] = mapped_column(DateTime)
    first_prenatal_visit:Mapped[datetime] = mapped_column(DateTime)
    trimester_first_prenatal_visit:Mapped[datetime] = mapped_column(DateTime)    
    trepo_test_first_prenatal:Mapped[Optional[str]] = mapped_column(String(100))
    trepo_test_week28_32:Mapped[Optional[str]] = mapped_column(String(100))
    trepo_test_delivery:Mapped[Optional[str]] = mapped_column(String(100))
    marital_status:Mapped[Optional[str]] = mapped_column(String(100))
    date_most_recent_trepo:Mapped[Optional[datetime]] = mapped_column(DateTime)
    result_most_recent_trepo:Mapped[Optional[str]] = mapped_column(String(100))
    titer_most_recent_trepo:Mapped[Optional[str]] = mapped_column(String(100))
    trepo_test_type:Mapped[Optional[str]] = mapped_column(String(100))
    date_nontrepo:Mapped[Optional[datetime]] = mapped_column(DateTime)
    result_nontrepo:Mapped[Optional[str]] = mapped_column(String(100))
    titer_nontrepo:Mapped[Optional[str]] = mapped_column(String(100))
    preg_hiv_status:Mapped[Optional[str]] = mapped_column(String(100))
    preg_syphilis_stage:Mapped[Optional[str]] = mapped_column(String(100))
    preg_surv_syphilis_stage:Mapped[Optional[str]] = mapped_column(String(100))
    date_first_benzathine:Mapped[Optional[str]] = mapped_column(String(100))
    dosage_benzathine:Mapped[Optional[str]] = mapped_column(String(100))
    serologic_response:Mapped[Optional[str]] = mapped_column(String(100))

class ChildInfo(Base, BaseModel):
    __tablename__ = 'child_info'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    created_by:Mapped[str] = mapped_column(String(200))
    upated_by:Mapped[str] = mapped_column(String(200))
    del_date:Mapped[datetime] = mapped_column(DateTime)
    vital_status:Mapped[Optional[str]] = mapped_column(String(100))
    date_of_birth:Mapped[datetime] = mapped_column(DateTime)
    birth_weight:Mapped[Optional[str]] = mapped_column(String(100))
    est_gest_age:Mapped[str] = mapped_column(String(100), unique=True)
    reactive_nontrepo_test:Mapped[Optional[str]] = mapped_column(String(100))
    reactive_trepo_test:Mapped[str] = mapped_column(String(100))
    dfa_placenta_cord:Mapped[datetime] = mapped_column(DateTime)
    signs_of_cs:Mapped[datetime] = mapped_column(DateTime)
    long_bone_xray:Mapped[datetime] = mapped_column(DateTime)    
    csf_count:Mapped[Optional[str]] = mapped_column(String(100))
    treated:Mapped[Optional[str]] = mapped_column(String(100))

class ChildInfo(Base, BaseModel):
    __tablename__ = 'child_info'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    created_by:Mapped[str] = mapped_column(String(200))
    upated_by:Mapped[str] = mapped_column(String(200))
    case_clasification:Mapped[Optional[str]] = mapped_column(String(100))

    