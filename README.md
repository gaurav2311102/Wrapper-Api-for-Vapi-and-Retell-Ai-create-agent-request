# 🤖 AI Agent Wrapper API (Vapi + Retell)

This is a FastAPI-based unified wrapper for creating AI agents on **Vapi** and **Retell** platforms using a single standardized endpoint.

---

## ✅ Features

- 🔄 One API to create agents on **Vapi** or **Retell**
- 🧩 Unified request format with provider-specific handling
- ⚙️ Supports `response_engine` only for Retell
- 🔐 Secure API key storage using `.env`

---


---

## 🧬 Request Schema

### POST `/create-agent`

Unified endpoint to create an agent in either **Vapi** or **Retell** depending on the `Api_provider`.

#### 🔸 Common Parameters (Both platforms)

{<br>
  "Api_provider": "vapi",  (or "retell")<br>
  "name": "test_agent",  (can be named anything )<br>
  "voice": "sarah-11labs", (or anything which is specified in the docs)<br>
}

Required parameter Only for Retell

"response_engine": {<br>
  "type": "retell-llm",<br>
  "llm_id": "<your llm_id >" (can be generated using dashboard or seperate endpoint)<br>
}

 #### Create Agent on Vapi

![Vapi agent  creation request](https://github.com/user-attachments/assets/c1bb0cac-9ca4-4e45-8136-ffd0735c6a25)

#### Create Agent on Retell (with response_engine)

![Retell Ai agent creation request](https://github.com/user-attachments/assets/2f08bc9a-92cf-4e96-be35-cec560309bd5)


#### Setup Instructions
1. Clone & Install

git clone https://github.com/gaurav2311102/Wrapper-Api-for-Vapi-and-Retell-Ai-create-agent-request.git<br>
cd Api<br>
python -m venv venv // (your virtual env created)<br>
source venv/bin/activate<br>
pip install -r requirements.txt

2. Configure Environment
Create a .env file in the root directory:

VAPI_API_KEY=your-vapi-api-key<br>
RETELL_API_KEY=your-retell-api-key

3. Run the App

uvicorn app.main:app --reload
