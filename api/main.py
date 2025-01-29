from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
from .config import get_settings
from .routers.data import router


app = FastAPI()

settings = get_settings()

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=settings.allowed_hosts.split(",")
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.csrf_trusted_origins.split(","),
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(router)
