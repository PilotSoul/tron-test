from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import Settings
from routers import wallets

app = FastAPI()
app.include_router(wallets.router, prefix="/api")
settings = Settings()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
