from pydantic import BaseModel

class Inbox(BaseModel):
    id: int
    uuid: int
    