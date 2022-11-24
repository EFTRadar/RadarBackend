from pydantic import BaseModel


class SessionResponse(BaseModel):
    session_id: str
    authentication_token: str
