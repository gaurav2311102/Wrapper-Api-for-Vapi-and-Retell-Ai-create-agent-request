import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    VAPI_API_KEY = os.getenv("VAPI_API_KEY")
    RETELL_API_KEY = os.getenv("RETELL_API_KEY")

settings = Settings()
