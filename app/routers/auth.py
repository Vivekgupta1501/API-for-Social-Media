from fastapi import APIRouter,Depends,status,HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from ..import schemas,models,utils,oauth2


router = APIRouter(tags = ['Authentication'])

#when we are using Oauth2Passwordrequestform it sotres EMAIL IN ysername and password in password
@router.post("/login")
def login(user_credentials: OAuth2PasswordRequestForm  =Depends(),db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,detail = f"Invalid Credentials {user_credentials.username}")
    
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid Credentials")
    
    #create a tokem
    #return the token
    access_token = oauth2.create_access_token(data={"user_id":user.id})
    return {"access_token" : access_token,"token_type":"bearer"}

