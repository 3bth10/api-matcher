from db import Base
from sqlalchemy import Column, Integer, String , DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True) 
    role = Column(String, index=True , default='user') 
    hashed_password = Column(String)
    create_at = Column(DateTime, default=datetime.datetime.utcnow)