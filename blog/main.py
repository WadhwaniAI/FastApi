from fastapi import FastAPI
import models
from routers import blog
from database import engine
from routers import user

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)