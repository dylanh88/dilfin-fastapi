from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional
from pydantic.types import conint


# These tell us which data the user can send to us
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


# These tell us which data to send back to the user
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    
    class Config:
      orm_mode = True
# ^^Tells Pydantic model to ignore that we will not be communicating back a full dictionary

class PostOut(BaseModel):
    Post: Post
    votes: int 

    class Config:
      orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)