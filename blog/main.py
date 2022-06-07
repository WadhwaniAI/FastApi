from operator import mod
from os import stat
from fastapi import Depends, FastAPI, status, Response, HTTPException
import models, schemas
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close
        


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)) :
    new_blog = models.Blog(title=request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog') 
def all(db):
    blogs = db.query(models.Blog).all()
    return blogs 

@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def getBlog(id, response: Response,db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} is not available')
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'Detail': f'Blog with id {id} is not available'}
    return blog

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not found.')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'deleted'
          
@app.put('/blog/{id}')
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Blog with id {id} not found.')
    blog.update(request.dict())
    db.commit()
    return {'Blog updated' : request}