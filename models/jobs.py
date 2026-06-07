from db import Base
from datetime import datetime
from sqlalchemy import String , Integer , Column  , DateTime



class Jobs(Base):
    __tablename__ = "Jobs"
    id = Column(Integer , unique=True , primary_key=True , index=True)
    title = Column(String , unique=True , index=True )
    create_at = Column(DateTime , default=datetime.utcnow, index=True )