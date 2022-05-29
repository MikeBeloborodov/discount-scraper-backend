from jose import JWTError, jwt
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from database import global_settings
from database.utils import time_stamp


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


def create_access_token(data: dict) -> str:
    try:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=int(global_settings.settings.access_token_expire_minutes))
        to_encode.update({"exp": expire})

        # payload, secret key, algorithm
        encoded_jwt = jwt.encode(to_encode, global_settings.settings.secret_key, algorithm=global_settings.settings.algorithm)

        return encoded_jwt
    except JWTError as error:
        print(f"[{time_stamp()}][!!] CREATE ACCESS TOKEN ERROR: {error}")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Token creation error")


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, global_settings.settings.secret_key, algorithms=[global_settings.settings.algorithm])
        user_id = payload.get("user_id")

        if user_id is None:
            raise credentials_exception
            
    except JWTError as error:
        print(f"[{time_stamp()}][!!] VERIFY ACCESS TOKEN ERROR: {error}")
        raise credentials_exception

    return user_id


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate" : "Bearer"})

    return verify_access_token(token, credentials_exception)