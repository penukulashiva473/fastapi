from pydantic import BaseModel 
from typing import List, Optional

class BlogBase(BaseModel):
    title: str
    body: str | None = None
class Blog(BlogBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode = True
