from sqlalchemy.orm import Session
from app.models import PatchStatus
from app.schemas import PatchStatusCreate

def get_all_patch_status(db: Session):
    return db.query(PatchStatus).all()

def create_patch_status(db: Session, patch_status: PatchStatusCreate):
    db_patch_status = PatchStatus(**patch_status.dict())
    db.add(db_patch_status)
    db.commit()
    db.refresh(db_patch_status)
    return db_patch_status