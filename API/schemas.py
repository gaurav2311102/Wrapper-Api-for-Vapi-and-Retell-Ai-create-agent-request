from pydantic import BaseModel, Field
from typing import Literal, Optional,Dict

class AgentCreateRequest(BaseModel):
    Api_provider: Literal["vapi", "retell"]
    name: str
    voice: str
    response_engine : Optional[Dict[str, str]] = None

