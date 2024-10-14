"""
# server/core/config.py
Settings class to manage configuration parameters.
    
Attributes:
    OPENAI_API_KEY (str): API key for OpenAI service.
    ALLOWED_ORIGINS (list): List of allowed origins for requests.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    # Any API Keys will be moved to API Gateway or Encryption
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    ALLOWED_ORIGINS: list = ["http://localhost:3000"]

settings = Settings()
