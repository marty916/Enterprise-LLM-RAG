# server/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from api.chatbot import get_chatbot_response
from api.customersupport import get_customer_support_response
from fastapi.middleware.cors import CORSMiddleware

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Allow CORS from client
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    
    response = get_chatbot_response(request.message)
    return {"reply": response}

@app.post("/customer-support")
async def customer_support_chat(request: ChatRequest):
    """
    Return a response from the customer support chatbot.

    Args:
        request: The input message to the chatbot.

    Returns:
        A dictionary containing the response from the chatbot.
    """
    response = get_customer_support_response(request.message)
    return {"reply": response}
