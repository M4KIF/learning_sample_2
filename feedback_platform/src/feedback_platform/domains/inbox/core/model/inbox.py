from pydantic import BaseModel, ConfigDict

class Inbox(BaseModel):

    model_config = ConfigDict(from_attributes=True)
    topic:str
    signature:str
    expiration_date:int
    allow_anonymous_submissions:bool
