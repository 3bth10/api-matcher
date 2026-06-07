from datetime import datetime
from db import Base 
from sqlalchemy import Column, Integer, String , DateTime , JSON 


class Resume(Base):
    __tablename__ = "resume"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String, index=True)
    experience = Column(JSON, index=True)
    created_at = Column(DateTime , default=datetime.utcnow)
