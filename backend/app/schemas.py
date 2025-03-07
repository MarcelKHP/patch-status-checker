from pydantic import BaseModel
from datetime import datetime

class PatchStatusCreate(BaseModel):
    endpoint: str
    os_type: str
    last_checked: datetime
    missing_updates: str

class PatchStatus(PatchStatusCreate):
    id: int

    class Config:
        orm_mode = True