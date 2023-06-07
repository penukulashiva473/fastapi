from pydantic import BaseModel 

class Item(BaseModel):
    title: str
    body: str | None = None