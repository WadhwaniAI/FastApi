from fastapi import FastAPI

app = FastAPI()

#Path Parameters

@app.get('/blog/unpublished')
def unpublished(): 
    return {
        "data":"all unpublished blogs"
    }

@app.get("/blog/{id}")
def show(id: int):
    return {
        "Blog Id": id
    } 