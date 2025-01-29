from fastapi.routing import APIRouter
from pydantic import BaseModel, EmailStr
from typing import Annotated
from fastapi import Depends
from ..config import get_settings, Settings
from datetime import datetime


router = APIRouter(prefix="/api/v1")

class DataModel(BaseModel):
    email: EmailStr
    current_datetime: datetime
    github_url: str


@router.get("/data", response_model=DataModel, status_code=200)
async def read_data(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "email": settings.email_value,
        "current_datetime": f"{datetime.now().isoformat()}Z",
        "github_url": settings.github_url,
    }
