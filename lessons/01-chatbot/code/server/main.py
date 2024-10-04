# server/main.py
from fastapi import FastAPI
from api.chatbot import router as chatbot_router
from core.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the chatbot API router
app.include_router(chatbot_router)
