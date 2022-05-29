from sqlalchemy.orm import Session
from database.models import User
from fastapi import HTTPException, status
from passlib.context import CryptContext
from database.utils import *
from authentication import oauth
from schemas.login_user_request import LoginUserRequest
from schemas.login_user_response import LoginUserResponse

def handle_login_user(login_data: LoginUserRequest, db: Session):
     # retrieve user from db
    try:
        user_query = db.query(User).filter(User.email == login_data.email)
        found_user = user_query.first()
    except Exception as user_validation_error:
        print(f"[{time_stamp()}][!!] Error occured during user search in db: {user_validation_error.username}")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database internal error during user search")

    if not found_user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found.")
    
    # then we check if stored hashed password and given password are the same
    pwd_context = CryptContext(schemes=['bcrypt'])
    if not pwd_context.verify(login_data.password, found_user.password):
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Wrong credentials.")

    # if everything is okay we send data back
    access_token = oauth.create_access_token(data = {"user_id" : found_user.user_id})

    return LoginUserResponse(access_token=access_token, token_type="bearer")
