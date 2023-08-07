from typing import List, Optional
from pydantic import BaseModel


class BlogBase(BaseModel):
    key: str
    value: str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    username:str
    email:str
    password:str
    full_name:str
    age: int
    gender : str


class ShowUser(BaseModel):
    username:str
    email:str
    full_name:str
    age: int
    gender : str
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    key: str
    value:str

    class Config():
        orm_mode = True


class Login(BaseModel):
    email: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None