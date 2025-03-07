from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PatchStatus(Base):
    __tablename__ = "patch_status"

    id = Column(Integer, primary_key=True, index=True)
    endpoint = Column(String, index=True)
    os_type = Column(String)
    last_checked = Column(DateTime)
    missing_updates = Column(String)