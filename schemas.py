
from pydantic import BaseModel


#Blog Class
class Blog(BaseModel):
    title: str
    body: str