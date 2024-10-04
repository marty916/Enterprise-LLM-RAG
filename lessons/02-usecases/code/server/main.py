# server/main.py
from fastapi import FastAPI
from api.chatbot import router as chatbot_router
from api.customersupport import router as customersupport_router
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

# Include the chatbot API routers
app.include_router(chatbot_router)
app.include_router(customersupport_router)
