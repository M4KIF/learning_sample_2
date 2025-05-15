from pydantic import BaseModel

class Creation(BaseModel):
    topic: str
    expiration_date: int
    allow_anonymous_submissions: bool