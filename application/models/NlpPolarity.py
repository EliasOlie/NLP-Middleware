from pydantic import BaseModel

class PolarityReq(BaseModel):
    phrase: str