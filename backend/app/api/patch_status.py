from fastapi import APIRouter, HTTPException
from app.models import PatchStatus
from app.schemas import PatchStatusCreate
from app.services import patch_service

router = APIRouter()

@router.get("/")
def get_patch_status():
    return patch_service.get_all_patch_status()

@router.post("/")
def create_patch_status(patch_status: PatchStatusCreate):
    return patch_service.create_patch_status(patch_status)