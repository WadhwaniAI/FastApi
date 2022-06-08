import schemas, database, models, hashing
import blogtoken
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/auth',
    tags=['authentication']
)

get_db = database.get_db

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'User with username {request.username} not found.' )
    
    if not hashing.Hash.verify(user.password  ,request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect Password')
        
    access_token = blogtoken.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}