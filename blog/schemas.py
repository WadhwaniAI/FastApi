
from typing import List, Union
from pydantic import BaseModel


#Blog Class
class Blog(BaseModel):
    title: str
    body: str
        
class User(BaseModel):
    name: str
    email: str
    password: str 
    
    
class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List
    
    class Config():
        orm_mode = True
        
class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    
    class Config():
        orm_mode = True
        
class Login(BaseModel):
    username: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None