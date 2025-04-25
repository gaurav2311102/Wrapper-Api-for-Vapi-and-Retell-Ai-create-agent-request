import requests
from config import settings

def create_retell_agent(name, voice, type, llm_id):
    url = "https://api.retellai.com/create-agent"
    headers = {
        "Authorization": f"Bearer {settings.RETELL_API_KEY}"
    }
    payload = {
        "agent_name": name,
        "voice_id": voice,
        "response_engine":{
            "type":type,
            "llm_id":llm_id
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
