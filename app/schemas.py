from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional



class UserCreate(BaseModel):
    email: EmailStr
    password: str
    date_Of_birth: datetime

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True
        
#pydantic model
class PostBase(BaseModel):
    title: str
    content: str
    published: bool =True

class PostCrate(PostBase):
    pass

class Post(PostBase):
    id:int
    created_at: datetime
    owner_id: int
    owner: UserOut
    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] 

class Vote(BaseModel):
    post_id: int
    dir : bool