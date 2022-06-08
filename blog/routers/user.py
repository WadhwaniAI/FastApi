from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
import schemas, database
from repository import userRepo

router = APIRouter(
    prefix='/user',
    tags=['user']
)

get_db = database.get_db

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return userRepo.create(request, db)

@router.post('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id, db: Session = Depends(get_db)):
    return userRepo.get(id, db)