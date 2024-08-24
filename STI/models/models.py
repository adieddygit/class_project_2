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

class Person(BaseModel, Base):
    __tablename__ = 'person'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String(50))