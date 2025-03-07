from fastapi import APIRouter
from app.api import patch_status

router = APIRouter()

router.include_router(patch_status.router, prefix="/patch-status", tags=["patch_status"])