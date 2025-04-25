from fastapi import FastAPI, HTTPException
from schemas import AgentCreateRequest
from routers.vapi import create_vapi_agent
from routers.retell import create_retell_agent

app = FastAPI()

@app.post("/create-agent")
def create_agent(req: AgentCreateRequest):
    
    if req.Api_provider == "vapi":
        
        return create_vapi_agent(req.name, req.voice)
    
    elif req.Api_provider == "retell":
        
        return create_retell_agent(req.name, req.voice, req.response_engine.get("type"), req.response_engine.get("llm_id"))
    else:
        raise HTTPException(status_code=400, detail="Unsupported provider")
