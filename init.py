from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def init() :
    return {
        "Name" : "Sampath Houde",
        "Company" : "Wadhwani AI",
        "Location" : "Mumbai"
    }
    
@app.get("/about")
def about():
    return {
        "about page":"About"
    }