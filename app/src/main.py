from fastapi import FastAPI

from src.audio.router import router as audio_router
from src.auth.router import router as auth_router

app = FastAPI()

app.include_router(audio_router, tags=["Audio"])
app.include_router(auth_router, tags=["Auth"])
