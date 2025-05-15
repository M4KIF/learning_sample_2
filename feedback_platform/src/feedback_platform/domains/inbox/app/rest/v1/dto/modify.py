from pydantic import BaseModel

class Modify(BaseModel):
    uuid:str
    topic:str