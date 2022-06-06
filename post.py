from cgitb import text
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


#Blog Class
class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]

#Post
@app.post('/blog')
def create_blog(request: Blog):
    if request.published_at: return {
        "response" : {
            "blog created" : {
                "title" : request.title,
                "body": request.body
            }
        }
    } 
    else: return {
        "response" : {
            "blog created" : "Not created"
        }
    }