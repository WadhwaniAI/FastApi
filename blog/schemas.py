
from pydantic import BaseModel


#Blog Class
class Blog(BaseModel):
    title: str
    body: str
        
class ShowBlog(BaseModel):
    title: str
    
    class Config():
        orm_mode = True