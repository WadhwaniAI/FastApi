from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response
from repository import blogRepo
import schemas, database, database, hashing
from sqlalchemy.orm import Session  

router = APIRouter(
    prefix='/blog',
    tags=['blogs']
)

get_db = database.get_db

@router.get('/',tags=['blogs'], response_model=List[schemas.ShowBlog]) 
def all(db: Session = Depends(get_db)):
    return blogRepo.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)) :
    return blogRepo.create(db, request)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get(id, response: Response,db: Session = Depends(get_db)):
    return blogRepo.get(id, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db: Session = Depends(get_db)):
    return blogRepo.delete(id, db)
          
@router.put('/{id}')
def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    return blogRepo .update(id, request, db)