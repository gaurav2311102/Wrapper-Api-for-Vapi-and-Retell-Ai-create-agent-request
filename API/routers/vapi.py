import requests
from config import settings

def create_vapi_agent(name, voice):
    url = "https://api.vapi.ai/assistant"
    headers = {
        "Authorization": f"Bearer {settings.VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "firstMessageMode":"assistant-speaks-first",
        "name": name,
        "voice":voice

    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
