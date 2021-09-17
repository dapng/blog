from typing import List, Optional
from pydantic import BaseModel
from pydantic.networks import EmailStr

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    
class ShowUser(BaseModel):
    name: str
    email: EmailStr
    blogs: List[Blog] = []

    class Config():
        orm_mode = True

class Creator(BaseModel):
    name: str

    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    id: int
    title: str
    body: str
    creator: Creator

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

class UserWithId(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config():
        orm_mode = True