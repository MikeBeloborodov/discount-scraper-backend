from fastapi import FastAPI, status, Depends
from schemas.message import Message
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database.database_logic import get_db
from schemas.login_user_request import LoginUserRequest
from schemas.login_user_response import LoginUserResponse
from schemas.register_promo_request import RegisterPromoRequest
from schemas.register_promo_response import RegisterPromoResponse
from schemas.get_promo_response import GetPromoResponse
from schemas.get_limited_promo_response import GetLimitedPromoResponse
from handles.user_handles import handle_login_user
from handles.promo_handles import *
from authentication import oauth
from typing import List, Optional

#Base.metadata.create_all(bind=engine)


app = FastAPI()


# if you want only specific servers to be able to talk to your api
# put them in origins, otherwise use "*" to allow everyone
# origins = ["http://www.google.com"]
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# main page
@app.get("/", status_code=status.HTTP_200_OK, response_model=Message)
def root() -> Message:
    return Message(message="Welcome.")


# login
@app.get("/login", status_code=status.HTTP_200_OK, response_model=LoginUserResponse)
def login_user(login_data: LoginUserRequest,
                db: Session = Depends(get_db)):
    return handle_login_user(login_data, db)


# register new promo
@app.post("/promo", status_code=status.HTTP_201_CREATED, response_model=RegisterPromoResponse)
def register_promo(register_promo_data: RegisterPromoRequest,
                    user_id: int = Depends(oauth.get_current_user),
                    db: Session = Depends(get_db)):
    
    return handle_register_new_promo(register_promo_data, user_id, db)


# get all promos
@app.get("/promo", status_code=status.HTTP_200_OK, response_model=List[GetPromoResponse])
def get_all_promos(db: Session = Depends(get_db)):
    
    return handle_get_all_promos(db)


# delete all promos
@app.delete("/promo", status_code=status.HTTP_200_OK, response_model=Message)
def delete_all_promos(user_id: int = Depends(oauth.get_current_user),
                    db: Session = Depends(get_db)):
    answer = handle_delete_all_promos(user_id, db)
    if answer:
        return Message(message="OK")
    else:
        return Message(message="Error.")


# get limited promos
@app.get("/promo/slice", status_code=status.HTTP_200_OK, response_model=List[GetLimitedPromoResponse])
def get_limited_promos(db: Session = Depends(get_db),
                        limit = 10,
                        skip = 0):
    
    return handle_get_limited_promos(db, limit, skip)


# return count of filtered promos
@app.get("/promo/count", status_code=status.HTTP_200_OK)
def get_count_promos(db: Session = Depends(get_db),
                        search: Optional[str] = ""):

    return handle_get_count_promos(db, search)
