from fastapi import FastAPI

app = FastAPI()

#Query Parameters
@app.get('/blog')
def show(limit = 10, published: bool = True):
    if published: 
        return {
        "data" : f"Published blogs {limit}"
    }
    else:
        return {
            'data': 'All the blogs unpublished'
        }