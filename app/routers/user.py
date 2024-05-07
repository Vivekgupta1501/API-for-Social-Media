from .. import models,schemas,utils
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter


router  = APIRouter(
    prefix = "/users",tags=['Users']
    )

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate,db: Session  = Depends(get_db)):
    
    #HASH THE PASSWORD - USER.PASSWORD

    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.__dict__)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/{id}",response_model=schemas.UserOut)
def get_user(id: int,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f" User with id: {id} does not exist")
    
    return user

@router.put("/forgotpassWord",response_model=schemas.UserOut,status_code=status.HTTP_202_ACCEPTED)
def forgot_password(user: schemas.UserCreate,db:Session  = Depends(get_db)):
    
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    db.query(models.User).filter(models.User.email == user.email).update({models.User.password : hashed_password},synchronize_session=False)
    
    
     

     